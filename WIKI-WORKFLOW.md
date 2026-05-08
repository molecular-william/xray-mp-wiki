# X-ray MP Wiki — Workflow Guide (Cave)

## Overview

Wiki pages generated from raw paper MD files via **YAML-driven, append-only pipeline**:

```
raw/papers/<doi>.md  →  *_yaml/<name>.yaml  →  scripts/  →  wiki pages
```

## The Four-Step Pipeline

### Step 1: Read Raw Paper

Read `raw/papers/<doi>.md`. Extract entities (proteins, reagents, methods, concepts).

### Step 1.5: Entity Classification & Concept Discovery

See WIKI-REFERENCE.md § Entity Classification. Ambiguity rules: "LCP crystallization" → Method. "Lipid polymorphism" → Concept. "BRIL fusion" → Reagent or Method (context). "MFS transporter" → Concept. "MFS transporter crystallization" → Method.

**BUFFER ENTITIES (CRITICAL):** Common buffers are reagents, NOT background chemicals. MUST create pages for: Tris (buffer-tris), HEPES (buffer-hepes), MOPS (buffer-mops), Sodium phosphate (buffer-phosphate), Cacodylate (buffer-cacodylate), Acetate (buffer-acetate), Citrate (buffer-citrate), PIPES (buffer-pipes), Bicine (buffer-bicine), TES (buffer-tes), Glycine (buffer-glycine), Ammonium acetate (buffer-ammonium-acetate), Ammonium sulfate (additive-precipitant). Buffer YAML tags MUST start with "buffer-" prefix so system auto-places them in reagents/buffers/.

For each entity: 1. Check if page exists. 2. Proteins/reagents/methods → write YAML to `*_yaml/`. 3. Concepts → if no page + meets threshold, write to `concepts_yaml/`. 4. Note cross-links.

### Step 2: Write YAML Files

YAML in `xray-mp-wiki/` (NOT `scripts/`).

### Step 3: Generate or Update

**New entity:** `python3 scripts/generate_<type>_page.py <name>` — reads YAML → writes page. Flags: `--dry-run`, `--diff`, `--yes`.

**Existing entity:** Edit the YAML file directly (add sources, append examples, update cross-refs), then run `python3 scripts/generate_<type>_page.py <name> --yes` — reads YAML → overwrites page. The generate script handles deduplication of PDB IDs, DOI sources, and cross-ref paths. No separate update script exists — YAML is the single source of truth.

**Why no update scripts:** YAML-first workflow minimizes complexity and room for error. The agent patches YAML directly (append-only, merge sources, deduplicate cross-refs), then regenerates. This avoids merge conflicts, preserves manual edits, and keeps the pipeline simple.

### Step 4: User Review

Always show `--diff` before writing. User approves → run without `--dry-run`.

### Step 4.5: Catalog Update

Auto-maintained after every generation/update. Entry added/updated (matched by path), sorted by title. Jekyll ignores (HTML comments). No user action.

### Step 5: Cross-References

Add cross-links between related pages after generation.

### Step 5.5: Post-Generation Entity Discovery

After generating primary pages, re-read the raw paper and identify ALL other entities mentioned (reagents, methods, concepts) that don't yet have wiki pages:

1. Read the raw paper text. Identify every reagent, method, and concept mentioned.
2. Check if a wiki page already exists by loading `index.md` and searching the wiki catalog for the entity name.
3. If page exists → note the cross-reference for the protein page.
4. If page doesn't exist AND entity meets page threshold (central to paper OR appears in 2+ sources) → write YAML + generate page.
5. **Regenerate all protein pages** from this DOI with updated Cross-References that include newly discovered entities.
6. Skip entities with ambiguous names (e.g., "DM" could be detergent or misread residue abbreviation) — leave as plain text in protein pages.

**Important:** Do NOT use automated entity discovery scripts. The agent reads the raw paper and uses judgment to identify entities. Many compounds have multiple names/abbreviations — only create pages for entities the agent can confidently classify.

### Step 6: Add to Category Index

Every new page → add to `categories/<type>/index.md`.

---

## Protein Pages

**Command:** `generate_protein_page.py <name>`. Flags: `--dry-run`, `--diff`, `--yes`.

**Update workflow:** Edit `xray-mp-wiki/proteins_yaml/<name>.yaml` directly (append sources, add structures, update cross-refs), then run `generate_protein_page.py <name> --yes`. The generate script deduplicates PDB IDs, DOI sources, and cross-ref paths.

### YAML Schema

**Required:** `title`, `tags` (from taxonomy), `sources` (DOI, `##` separator), `overview` (prose), `verified` (bool, default false).

**Optional:** `structures[]` — source ✅, pdb_id ✅, resolution ✅, space_group ⚠️, construct ⚠️, ligand ⚠️. `expression` — system ⚠️, construct ⚠️. `purifications[].steps[]` — step ⚠️, method ⚠️, resin ⚠️, buffer ⚠️, notes ⚠️. `crystallizations[]` — source ✅, method ⚠️, protein_sample ⚠️, reservoir ⚠️ (vapor only), mixing_ratio ⚠️ (vapor only), lipid ⚠️ (LCP only), protein_to_lipid_ratio ⚠️ (LCP only), temperature ⚠️, growth_time ⚠️, cryoprotection ⚠️, notes ⚠️. `biological_insights[]` — title ⚠️, content ⚠️. `cross_references[]` — path ✅, title ✅, reason ✅.

**YAML formatting:** `|-` for `biological_insights[].content` (preserves newlines). `|` for `overview`. `>` for `expression.system`/`expression.construct`. Cross-ref paths: `/xray-mp-wiki/path/to/page/`.

### Merge Rules (YAML-First)

**Agent patches YAML directly** — no update script. Rules for YAML editing:

Frontmatter: append sources (deduplicate), preserve `created`, update `updated`. Structure table: append rows, deduplicate by PDB ID. Purification: append new `### <Source>` subsections. Crystallization: append new `### <Source>` subsections. Biological insights: append new `### <Title>` entries. Cross-References: append new entries, deduplicate by path.

**After YAML edit:** Run `generate_<type>_page.py <name> --yes` — reads YAML → overwrites page.

### LCP vs Vapor Diffusion Detection

LCP: method contains "cubic phase" or "lcp". LCP fields (Lipid, Protein-to-lipid ratio) BEFORE Temperature. Vapor fields (Reservoir, Mixing ratio) AFTER Protein Sample.

### Pitfalls

1. **YAML newlines:** `|-` for `biological_insights[].content`, NOT `>`. 2. **Source dedup:** merged (not replaced). 3. **PDB dedup:** by PDB ID column (index 1). 4. **No wikilinks:** absolute markdown `[text](/xray-mp-wiki/path/)`. 5. **Table formatting:** no empty rows, use "—" for empty. 6. **Script import:** both scripts import from `protein_page_renderer.py` — same directory.

**Multi-Protein Papers:** one YAML per protein, same DOI.

---

## Reagent Pages

**Command:** `generate_reagent_page.py <name>`. Flags: `--dry-run`, `--diff`, `--yes`.

**Update workflow:** Edit `xray-mp-wiki/reagents_yaml/<name>.yaml` directly (append sources, add examples, update cross-refs), then run `generate_reagent_page.py <name> --yes`. The generate script deduplicates sources and cross-ref paths.

### YAML Schema

**Required:** `title`, `tags`, `sources`, `overview` (1-2 sentences), `verified` (bool, default false).

**Optional:** `uses[]` — title ⚠️, content ⚠️. `examples[]` — protein ✅ (markdown link), concentration ⚠️, context ⚠️, result ⚠️. `binding`/`binding_mode` (ligands) — target ✅, interactions ⚠️, pocket_volume ⚠️, key_residues ⚠️. `advantages[]`, `disadvantages[]`, `comparison[]` (array of objects with consistent keys), `cross_references[]` — path ✅, title ✅, reason ✅.

**Common properties:** chemical_name ⚠️, chemical_formula ⚠️, molecular_weight ⚠️, class ⚠️.

**Type-specific:**
- **Detergents:** cmc ⚠️, hlb ⚠️, transition_temp ⚠️, head_group ⚠️, tail_length ⚠️
- **Lipids:** acyl_chain ⚠️, phase_transition ⚠️
- **Buffers:** pka ⚠️, ph_range ⚠️, concentration_range ⚠️
- **Additives:** function ⚠️, solubility ⚠️, typical_concentration ⚠️
- **Ligands:** kd_ki ⚠️, clinical_status ⚠️, scaffold ⚠️
- **Protein Tags:** source_organism ⚠️, fusion_strategy ⚠️, size ⚠️
- **Antibodies:** target ⚠️, format ⚠️, epitope ⚠️, isotype ⚠️

**YAML formatting:** `|-` for `uses[].content`. `>` for `overview`. Cross-ref paths: `/xray-mp-wiki/path/to/page/`.

### Merge Rules (YAML-First)

**Agent patches YAML directly** — no update script. Rules for YAML editing:

Frontmatter: append sources (deduplicate), preserve `created`, update `updated`. Properties: preserve existing. Use in Work: append new `### <Title>` subsections. Examples table: append new rows, deduplicate by protein path. Binding Mode: append new `### Binding to <Target>` subsections. Advantages/Disadvantages: append to existing subsections. Comparison: preserve + append. Cross-References: append new entries, deduplicate by path.

**After YAML edit:** Run `generate_<type>_page.py <name> --yes` — reads YAML → overwrites page.

### Pitfalls

1. **YAML newlines:** `|-` for `uses[].content`, NOT `>`. 2. **Source dedup:** merged. 3. **Properties merge:** parsed + merged, not replaced. 4. **Advantages/Disadvantages:** insert into existing subsections. 5. **No wikilinks:** absolute markdown. 6. **Table formatting:** no empty rows, use "—". 7. **Script import:** both scripts import from `reagent_page_renderer.py`. 8. **Reagent naming:** lowercase-hyphen (e.g., `cholesterol-hydrogen-succinate.md`). 9. **Comparison tables:** only when 2+ reagents.

**Multi-Reagent Papers:** one YAML per reagent, same DOI.

---

## Concept Pages — Hybrid Workflow

Concepts = **narrative**, not tabular. YAML for metadata/structure, LLM for prose.

**Command:** `generate_concept_page.py <name>`. Flags: `--dry-run`, `--diff`, `--yes`.

**Update workflow:** Edit `xray-mp-wiki/concepts_yaml/<name>.yaml` directly (append sources, add examples, update cross-refs), then run `generate_concept_page.py <name> --yes`. The generate script deduplicates sources and cross-ref paths.

### YAML Schema — Metadata Only

YAML = metadata + structured lists only. No "overview" or "mechanism" prose — LLM writes from raw paper.

**Required:** `title`, `tags` (must include `concept-*` or `membrane-protein`), `sources`, `verified` (bool, default false).

**Optional:** `examples[]` — protein ✅ (markdown link), context ⚠️. `cross_references[]` — path ✅, title ✅, reason ✅. Cross-ref paths: `/xray-mp-wiki/path/to/page/`.

### LLM Process

**New page:** Read raw paper + YAML metadata → extract title, tags, sources, examples, cross-refs → write prose (Overview, Mechanism/Details, Examples, Cross-References) → output page (see WIKI-REFERENCE.md).

**Update:** Read existing page + new raw paper + YAML → merge insights into existing sections → append new examples/cross-refs (deduplicate by path) → update sources (deduplicate).

### Merge Rules (YAML-First)

**Agent patches YAML directly** — no update script. Rules for YAML editing:

Frontmatter: append sources (deduplicate), preserve `created`, update `updated`. Examples: append new entries, deduplicate by protein path. Cross-References: append new entries, deduplicate by path.

**After YAML edit:** Run `generate_<type>_page.py <name> --yes` — reads YAML → overwrites page. LLM handles prose regeneration from raw paper.

## Batch DOI Processing with Session Manifest

For processing 615+ unincorporated DOIs. Resumable via `wiki_manifest.json` at project root.

### Manifest Structure

```json
{"last_run":"...","batch_number":2,"batch_size":4,"processed":{"DOI":{"status":"done","pages":["name.md"],"entity_type":"protein","actions":["created"],"comments":"ok"}},"current_batch":{"DOI":{"status":"pending","assigned_to":"batch_1"}}}
```

### Initialization

```bash
python3 scripts/wiki_manifest.py init --batch-size 4
```

Loads all "no" entries from `protein_doi_checklist.csv` into `current_batch`.

### Agent Workflow

**Start:** `read_file` manifest → if pending DOIs, continue; else `init --batch-size 4`.

**Per DOI:** 1. Read `raw/papers/<doi>.md`. 2. Assign comment (see below). 3. Classify entity. 4. Check page existence. 5. Update or generate. 6. Update manifest with results + comment.

**After batch:** `python3 scripts/wiki_manifest.py update-csv` → syncs CSV (status→"yes", pages, comments). `write_file` updated manifest. Report.

### Comments Column

Agent's quality assessment of raw paper. Valid values: `ok` | `abstract only` | `methods in another citation` | `no purification detergent` | `no purification buffer` | `not a membrane protein` | `reagent only` | `data insufficient` | `skip — cryoEM` | `skip — review` | `skip — computational` | `duplicate`.

Usage: `ok` → normal processing. `no purification detergent/buffer` → extract, note gap. `abstract only`, `data insufficient` → minimal extract, flag for Pass 2. `skip —` → no page, mark skipped.

### Utility Commands

```bash
python3 scripts/wiki_manifest.py status    # Show state
python3 scripts/wiki_manifest.py load      # Print pending DOIs
python3 scripts/wiki_manifest.py reset     # Delete manifest
```

### Pitfalls

1. **Manifest is source of truth during processing.** CSV updated after batch. Mid-batch interruption → manifest preserves progress. 2. **Batch size 4 is optimal.** 3. **One DOI can produce multiple pages.** Track all in `pages[]`. 4. **CSV uses ## separator.** Don't convert to `/`. 5. **Not all DOIs are proteins.** Classify by content. 6. **Always run `update-csv` after batch.** CSV = persistent record. Manifest = session-local. 7. **Comments required.** Every DOI must have a comment. No blanks — use `ok`.

## Two-Pass Source Verification

### Pass 1 — Fast Extraction (Bulk)

When processing DOIs in bulk, do NOT verify every claim. Instead:
1. Extract structured data mechanically (PDB IDs, resolutions, conditions, reagent names, methods).
2. Write YAML, populate all extractable fields.
3. Generate page → `generate_<type>_page.py`.
4. Set `verified: false` (default).
5. Mark DOI processed in manifest.

**Why:** 1007 raw papers × full verification = token-heavy. Most DOIs map to existing protein pages. Pass 1 = mechanical extraction.

### Pass 2 — On-Demand Verification (Maintenance)

During audit sessions:
1. Read wiki page in full. 2. Extract factual claims (entity names, numbers, chemical properties, conditions). 3. For each DOI in `sources:`, strip `doi/` → look up `raw/papers/<doi>.md`. 4. Read each raw paper, search for supporting evidence. 5. Remove/correct unsupported claims. 6. Set `verified: true` in YAML. 7. Log corrections in `log.md`.

**Example:** GNP page lists CMC `0.17 mM` from `doi/10.1038##nature13074`. Raw paper has zero GNP mentions. Remove CMC and citation. Set `verified: true` only after all claims verified.

### YAML `verified` Field

Default: absent (treated as `false`). `verified: true` in YAML → renders in frontmatter. All 4 renderers support it. Lint: pages with `verified: true` should have all claims supported.

### When to Use

Bulk DOI ingestion / new page creation → Pass 1. Periodic audit / user reports incorrect claim / adding new source → Pass 2.

## Index Rebuild (Auto-Catalog)

After creating pages via `write_file` (bypassing generate scripts), catalog in `index.md` may be incomplete.

**Script:** `scripts/rebuild_indexes.py`. **Usage:** `python3 scripts/rebuild_indexes.py`. Scans category directories, reads frontmatter titles, adds missing entries. Conflict-free with `maintain_catalog()` (dedup by path). **Force mode:** `--force` rebuilds entire table.

### Pitfalls

1. **Concepts thin:** ~50-100 lines, split if >150. 2. **Overlap with methods common:** protocol → Method, principle → Concept. 3. **Cross-cutting:** single paper may touch 3+ concepts. 4. **No properties tables:** concepts = narrative, not tabular. 5. **Script import:** both scripts import from `concept_page_renderer.py` — same directory.