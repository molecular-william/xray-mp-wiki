# X-ray MP Wiki — Workflow Guide (Concise)

**Governed by `references/AGENT-MANIFEST.md` (§5 — The 10 Principles).** See manifest for rationale behind every step and full rules, schema, and conventions.

## Pipeline
```
raw/papers/<doi>.md  →  *_yaml/<name>.yaml  →  generate_page.py  →  wiki pages
```

## Step-by-Step

### 1. Read Raw Paper
Read `raw/papers/<doi>.md`. Extract entities. Classify per WIKI-REFERENCE.md.

### 2. Write YAML
YAML in `xray-mp-wiki/<type>_yaml/name.yaml` (flat directories). Output subdirectory auto-detected by `_base.py`:
- **Proteins:** via `mpstruc_classification.subgroup` → `PROTEIN_SUBDIR_MAP` (16 subdirs)
- **Reagents/Methods/Concepts:** via `subdirectory-{name}` tag, tag-prefix matching, or keyword classifier

### 3. Validate
```bash
python3 scripts/validate_yaml.py <type> <name> --strict
```
Required per type (see WIKI-REFERENCE.md § Validation). Fix errors before generating.

### 4. Generate
```bash
# Single page
python3 scripts/generate_page.py <type> <name> [--dry-run] [--diff] [--yes]

# Batch (skip catalog per-page, rebuild once)
python3 scripts/generate_page.py <type> <name> --yes --skip-catalog
# ... repeat for all entities ...
python3 scripts/rebuild_indexes.py --force
python3 scripts/rebuild_entity_catalog.py
```

`--dry-run`: print to stdout. `--diff`: show diff against existing. `--yes`: skip confirm.

### 5. User Review
Show `--diff` before live writes.

### 6. Wikilink Enrichment (Post-Creation)
```bash
# Local script (0 token cost, ~5K files/hr)
YAML_TYPE=proteins_yaml DRY_RUN=1 python3 scripts/enrich_wikilinks.py

# Subagent (edge cases only, ~240/hr, ~40% corrupt)
# Use prompt at references/subagent-wikilink-enrichment.md
# BAN [[key|display]] syntax in subagent prompt
```

### 7. Cross-References
Add cross-refs between related pages. Max 10 per page. Use correct subdirectory paths (check entity catalog).

### 8. Rebuild Indexes (after batch)
```bash
python3 scripts/rebuild_indexes.py --force
python3 scripts/rebuild_entity_catalog.py
```

## Protein Pages

### YAML Schema (Required)
`title`, `tags` (class + `membrane-protein`), `sources`, `overview`, `verified`. Optional: `structures[]`, `expression`, `purifications[]`, `crystallizations[]`, `biological_insights[]`, `cross_references[]`.

### Purifications Format
```yaml
purifications:
- source: doi/10.xxxx##yyyy
  expression_system: E. coli BL21
  expression_construct: His6-tag
  tag_info: His6-tag, TEV removed
  steps:
  - step: Cell culture
    method: Fermentation
    buffer: PBS pH 7.4
    detergent: 0.02% DDM
    resin: Ni-NTA
    notes: 2L culture
  final_sample: 10 mg/ml in X buffer
  yield: ~2 mg/L
  purity: >95% by SDS-PAGE
```

### Generated Heading Structure (2026-06-23 fix)
```
## Expression and Purification
### Purification Workflow                   ← SINGLE heading, not per-source
#### Source: doi/10.7554##eLife.31259       ← Per-source subheading
- **Expression system**: ...
##### Steps
[TABLE]
#### Source: doi/10.7554##eLife.69482
##### Steps
[TABLE]
```
This replaces the old structure (nested `### Purification Workflow` × N) which caused 209 duplicate-section lint warnings.

### Merge Rules
Edit YAML directly → regenerate. Rules: append sources (deduplicate), preserve `created`, update `updated`. Append structure rows (dedup by PDB), purification/crystallization entries, biological insights. Cross-refs: append, dedup by path.

### LCP vs Vapor Diffusion Detection
LCP: method contains "cubic phase" or "lcp" → LCP fields (Lipid, Ratio) before Temperature. Vapor fields (Reservoir, Ratio) after Protein Sample.

## Reagent Pages

YAML: `title`, `tags` (incl `subdirectory-*`), `sources`, `overview`. Optional: `uses[]`, `examples[]`, `binding`, `advantages[]`, `disadvantages[]`, `comparison[]`, `cross_references[]`.

Type-specific: Detergents (`cmc`, `hlb`, `head_group`, `tail_length`), Lipids (`acyl_chain`), Buffers (`pka`, `ph_range`), Additives (`function`), Ligands (`kd_ki`, `scaffold`), Tags (`source_organism`, `size`), Antibodies (`target`, `epitope`).

## Method Pages
YAML: `title`, `tags`, `sources`. Optional: `protocol` (reagents, steps), `applications[]`, `related_methods[]`, `cross_references[]`.

## Concept Pages (Hybrid)
YAML = metadata only (title, tags, sources, examples, cross-refs). **No prose in YAML** — LLM writes Overview + Mechanism/Details from raw paper. ~50-100 lines, split if >150.

## Batch DOI Processing

### Init
```bash
python3 scripts/wiki_manifest.py rebuild [--skip-file references/known-skip-dois.md]
```
Scans `raw/papers/` for DOIs, `*_yaml/` for source DOIs, computes pending.

### Per DOI
1. Read `raw/papers/<doi>.md`
2. Assign comment: `ok` | `abstract only` | `skip — cryoEM/review/computational` | `duplicate` | etc.
3. Classify entity. Check catalog for existing pages.
4. Write/update YAML. Validate. Generate.
5. Update manifest.

### Post-Batch
```bash
python3 scripts/rebuild_indexes.py --force
python3 scripts/rebuild_entity_catalog.py
```

## Subagent DOI Processing — Path Awareness
When writing cross-refs for existing entities, **query the entity catalog** for the correct subdirectory path:
```python
# Load catalog
import json
with open("references/entity_catalog.json") as f:
    catalog = json.load(f)
# Get path: catalog["kcsa"]["type"] = "proteins" → look up in proteins/
```
Do NOT hardcode flat paths like `/xray-mp-wiki/proteins/kcsa/`. Use actual paths like `/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/`.

## Two-Pass Source Verification

**Pass 1 (Bulk):** Extract structured data mechanically. Write YAML. Generate. Set `verified: false`.

**Pass 2 (Audit):** Read wiki page. For each DOI, strip `doi/` → read raw paper → verify claims. Set `verified: true`. Log corrections.

## Renderer Fix (2026-06-23)
`_base.py` line 217: `title: {data['title']}` → `title: "{data['title']}"`. Prevents YAML frontmatter breakage from colons in titles (e.g., "PZ Pocket: Inhibitor-Induced Binding Pocket"). Any titles with `: ` now automaically quoted.

## NEVER
- Interleave write → validate → generate per entity (batch instead).
- Use regex/sed on YAML files (destroys structure).
- Edit index.md catalog section manually (auto-maintained).
- Push to remotes (user only).
- Concatenate multiple DOIs into one string in `sources:`.
- Hardcode flat paths for proteins/concepts → use catalog or subdirectory-aware functions.
