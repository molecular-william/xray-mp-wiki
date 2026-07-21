# X-ray MP Wiki — Agent Manifest

**The constitution. Load this file first in every session.** All subagent, orchestrator, and maintenance agent prompts assume you have read this manifest. Task-specific briefings (in `references/subagent-*.md`) contain only what's unique to that task.

---

## §1 — Schema

Each entity is a YAML file in `xray-mp-wiki/<type>_yaml/<name>.yaml`. The full formal JSON Schema is at `references/entity_schema.json`. Below is a quick reference.

### Common fields (all 4 entity types)

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `title` | string | yes | Always quoted (avoids colon-in-YAML bug: `title: "Foo: Bar"`) |
| `tags` | list of strings | yes | ≥1 anchor tag per taxonomy below |
| `sources` | list of strings | yes | Format: `doi/10.xxxx##yyyy`. Case-insensitive matching. Separate entries, never concatenated. |
| `created` | string (ISO date) | no | YYYY-MM-DD |
| `updated` | string (ISO date) | no | Bump on every edit |
| `layout` | string | no | `default` (the only valid value) |
| `verified` | enum | no | `"none"` (default), `"regex"` (automated pattern checks passed), `"pdb"` (PDB-DOI pairs verified via check_pdb.py), `"agent"` (LLM subagent confirmed against papers), `"human"` (domain expert reviewed) |
| `overview` | string | no | Human-readable summary |
| `cross_references` | list of objects | no | `{path, title, reason}` where `path` starts with `/xray-mp-wiki/` |

### Protein-specific fields

`publications[]`: each has `source` (DOI), plus optional `structures[]`, `purifications[]`, `crystallizations[]`, `sequences[]`.

- `structures[].pdb_id`: 4-char PDB code, string
- `purifications[].steps[]`: each has `step` (required), `method`, `resin`, `buffer`, `detergent`, `notes`, `detergent_details` (array of `{reagent, concentration, unit}`), `buffer_details` (array of `{reagent, concentration, unit, ph}`), `step_type` (controlled: `binding`, `clarification`, `complex_formation`, `concentration`, `crystallization_setup`, `deglycosylation`, `dialysis`, `elution`, `exchange`, `expression`, `hic`, `ion_exchange`, `lysis`, `membrane_prep`, `modification`, `polishing`, `purification`, `sec`, `solubilization`, `tag_cleavage`, `wash`)
|- `crystallizations[].method`: if contains "cubic phase" or "lcp" → LCP fields (Lipid, Ratio) used
|- `crystallizations[].mixing_ratio`: **MUST be quoted string** — YAML parses `1:1` as sexagesimal 61
|- `crystallizations[].crystallization_details`: optional structured parallel field (added by `normalize_crystallization.py`). Object with:
  - `method_lc`: controlled — `lcp`, `vapor-diffusion`, `microbatch`, `dialysis`, `bicelle`, `nanodisc`, `free-interface-diffusion`, `counter-diffusion`, `not-specified`
  - `ph`: quoted string (e.g. `"7.5"`)
  - `temperature_value`: quoted string (e.g. `"20"`)
  - `temperature_unit`: one of `C`, `K`, `°C`
  - `method_variant`: `sitting-drop` or `hanging-drop` (vapor diffusion subtypes)
  - `mixing_ratio`: **MUST be quoted string** (LCP-specific, e.g. `"1:1"`)
  - `protein_to_lipid_ratio`: quoted string (LCP-specific, e.g. `"2:3"`)
  - `lipid_note`: string (LCP-specific, free text)
  - `reservoir_components[]`: list of objects, each with:
    - `reagent`: wikilink path (e.g. `/xray-mp-wiki/reagents/buffers/hepes/`)
    - `concentration`: quoted string (e.g. `"0.1"`)
    - `unit`: one of `M`, `mM`, `%`
    - `role`: controlled — `buffer`, `salt`, `precipitant`, `additive`, `detergent`
    - `subtype`: optional string (e.g. `"PEG 400"` for peg-400)
    - `note`: optional string for extra context
- `sequences[].topology[].location`: one of `Membrane`, `Inside`, `Outside`, `Unknown`
- `mpstruc_classification.subgroup`: drives subdirectory routing
- `expression`: object with `system`, `construct`, `notes`, `class` (controlled: one of `e-coli`, `sf9`, `hek293`, `pichia-pastoris`, `saccharomyces-cerevisiae`, `hi5`, `native-tissue`, `cell-free`, `lexsy`, `other-bacterial`, `other-eukaryotic`, `not-specified`)
- `uniprot_id`: **string OR list of strings.** Single Uniprot accession (e.g. `"P0A334"`) for single-gene products; list (e.g. `["Q9H221", "Q9H222"]`) for multi-subunit complexes resolved from PDBTM chain→entity mapping. Resolved by `enrich_uniprot.py` using RCSB PDB GraphQL API. Validated against `^[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2}$`.
- `organism`: string. Scientific name (e.g. `"Homo sapiens"`, `"Escherichia coli"`). Derived from PDB GraphQL `rcsb_entity_source_organism` via `enrich_organism.py`, with weighted majority across clean entities and fusion partner exclusion.

### Reagent-specific fields

Type-specific property fields (all optional, all quoted strings):
- **Detergent:** `cmc`, `hlb`, `transition_temp`, `head_group`, `tail_length`
- **Lipid:** `acyl_chain`, `phase_transition`
- **Buffer:** `pka`, `ph_range`, `concentration_range`
- **Additive:** `function`, `solubility`, `typical_concentration`
- **Ligand:** `kd_ki`, `clinical_status`, `scaffold`
- **Protein tag:** `source_organism`, `fusion_strategy`, `size`
- **Antibody:** `target`, `format`, `epitope`, `isotype`

Structured fields: `uses[]` ({title, content}), `examples[]` ({protein, concentration, context, result}), `binding` (object or array), `advantages[]`, `disadvantages[]`, `comparison` (object or array).

### Method-specific fields

`principle`, `protocol` ({reagents[], steps[], conditions{}}), `proteins_using[]` ({protein, resolution, pdb, notes}). Overview pages use `methods_list[]`, `workflow`, `comparison`.

### Concept-specific fields

`mechanism` or `details`, `examples[]` ({protein, context}), `related_concepts[]` (object or plain string).

---

## §2 — Tag Taxonomy

### Proteins — ≥1 class tag required

`gpcr` | `ion-channel` | `transporter` | `enzyme` | `receptor` | `channel` | `pump` | `porin`

Plus general tags: `membrane-protein`, `xray-crystallography`

### Reagents — type prefix based on subdirectory

**Detergents:** `detergent-nonionic/zwitterionic/ionic/mild/strong`
**Buffers:** `buffer-{tris/hepes/phosphate/acetate/citrate/mops/pipes/bicine/tes/glycine/mes/cacodylate/ches/bis-tris-propane/additive}`
**Additives:** `additive-{stabilizer/reductant/precipitant/salt/ph/ligand/antibody/metal/organic-solvent/alkylating-agent/protease-inhibitor}`
**Lipids:** `lipid` / `lipid-monoacyl/diacyl/sterol/analog`
**General:** `ligand` | `enzyme` | `protease` | `protein-tag` | `antibody` | `cofactor` | `antibiotic` | `substrate`

### Methods — prefix-based

**Solubilization:** `solubilization-detergent/lcp/bicelle/nanodisc/smalp/maltoside`
**Purification:** `purification-affinity/ion-exchange/size-exclusion/tag/fractionation`
**Crystallization:** `crystallization-vapor-diffusion/lcp/microbatch/dialysis/sitting-drop/hanging-drop`
**Structure:** `structure-xray/sad/mad/molecular-replacement/cryoem/refinement/model-building`
**Also:** `cell-lysis` / `cell-lysis-pressure/mechanical` · `expression-system` · `quality-assessment`

### Concepts — `concept-` prefix

`concept-transport-mechanism` | `concept-protein-family` | `concept-membrane-mimetic` | `concept-crystallography-principle` | `concept-construct-design` | `concept-functional` | `concept-antibody-technology` | `concept-structural` | `concept-enzyme-mechanism`

### Subdirectory routing tags

`subdirectory-{name}` — used for reagents, methods, concepts. Protein subdirectories are auto-assigned from `mpstruc_classification.subgroup`.

### Rule
Every tag on a page must appear in taxonomy. New tags → propose with examples, user approves, add to both `validate_yaml.py` and this doc.

---

## §3 — Conventions

### YAML handling (MANDATORY)
- **ALWAYS** `yaml.safe_load()` → modify dict → `yaml.dump()`. **NEVER** regex/sed/awk on YAML text — destroys structure.
- All numeric values must be **quoted strings** (`"3.5"` not `3.5`).
- All dates must be quoted (`'2026-06-08'`) to prevent YAML parsing as date object.
- Use double quotes for strings containing apostrophes.
- Use `yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False)` for writing.
- `mixing_ratio: 1:1` — YAML parses as sexagesimal 61. **Always quote:** `mixing_ratio: "1:1"`.
- topology begin/end/pdb_* fields must be quoted strings.
- `CommentedMap` not `OrderedDict` for ruamel.yaml (avoids `!!omap` tag).

### Internal links
- `[Display Name](/xray-mp-wiki/path/to/page/)` — absolute paths.
- **NEVER** `[[key|display]]` — the validator rejects it.
- Paths must use correct subdirectory (check `entity_catalog.json`).
- No links to non-existent pages — create or leave as plain text.

### DOI format
- `doi/10.xxxx##yyyy` — the `##` is a literal separator, not a comment.
- Case-insensitive matching (`NATURE09580.md` vs `nature09580.md`).
- Multiple DOIs = separate list entries, NOT concatenated strings.
- Raw paper filename = lowercased DOI + `.md`.

### File naming
- `lowercase-hyphen.md`, no spaces, no abbreviations.
- For proteins: `<name>.yaml` → generated to `proteins/<subdir>/<name>.md`.
- For reagents/methods/concepts: `<name>.yaml` → generated to `reagents/<subdir>/<name>.md`.

### Append-only merge (P6)
Never delete existing content. Append and deduplicate:
- `sources[]` dedup by DOI string
- `cross_references[]` by path
- `examples[]` by protein
- `structures[]` by PDB ID
- `biological_insights[]` by title
- `uses[]` by title
- `advantages[]`/`disadvantages[]` by string content
- Always update `updated:` field when modifying.

### Path awareness
Query `references/entity_catalog.json` for existing entities' correct subdirectory paths. Do NOT hardcode flat paths like `/xray-mp-wiki/proteins/kcsa/` — use `/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/`.

### Cross-reference limits
Max 10 cross-references per page. Prioritize: purification reagents > methods > concepts.

---

## §4 — Prohibitions (NEVER list)

| # | Prohibition | Principle |
|---|-------------|-----------|
| 1 | Edit `.md` pages directly. YAML → validate → generate. | P1 |
| 2 | Use regex/sed/awk on YAML files. | P1 |
| 3 | Use `[[key\|display]]` wikilinks. | P1 |
| 4 | Create temp scripts at project root. All inline. | P4 |
| 5 | Write result JSON files to disk. Return in response text. | P4 |
| 6 | Create new directories without explicit user request. | P4 |
| 7 | Use `mcp_filesystem_*` tools (write_file/patch/read_file only). | P3 |
| 8 | Call APIs, curl, browser, or web_search (papers are local). | P2 |
| 9 | Fabricate claims. If paper doesn't support it, remove it. | P9 |
| 10 | Leave empty tables or add speculative content. | P9 |
| 11 | Create backup files (user responsibility). | P4 |
| 12 | Push to git remotes (user only). | P4 |
| 13 | Concatenate multiple DOIs into one string in `sources:`. | P1 |
| 14 | Use `clarify` in subagents (must decide autonomously). | P8 |
| 15 | Mix different task types in one subagent (one task per agent). | P7 |

---

## §5 — Rules (The 10 Principles)

**P1 — YAML is the single source of truth.** Never edit `.md` pages directly. YAML → validate → generate. No regex on YAML.

**P2 — Source-truth anchor every claim.** Every claim traces to a DOI'd raw paper on disk. No internet. DOI matching is case-insensitive. Self-verify every `write_file` by reading it back.

**P3 — mcp_filesystem_* tools are traps.** Use `write_file` (creation), `patch` (edits), `read_file` (reading) only.

**P4 — No side effects.** Return results in response text. No temp files at project root. No new directories. All files go into existing `*_yaml/` directories only.

**P5 — Maximum extraction.** When processing a paper, extract ALL entities that meet threshold. Better too many than too few.

**P6 — Append-only merge.** Never delete or replace existing content. Append and deduplicate. Always bump `updated:`.

**P7 — One task per subagent.** Each subagent has exactly one role. Never mix DOI processing and verification.

**P8 — Zero session context.** Subagents have no memory of past conversations. Everything must be in the prompt. No `clarify`, no `memory`, no `session_search`.

**P9 — No fabrication.** If you can't find evidence for a claim, leave it unsaid. Properties from papers: cite the DOI. General knowledge: mark as approximate.

**P10 — Graph-aware topology.** The wiki is a network (2,050+ nodes, 9,600+ edges). Cross-references are bidirectional. Match full hyphenated catalog keys, not individual words.

---

## §6 — Tool Reference

### Core pipeline (run from project root)

```bash
python3 scripts/generate_page.py <type> <name> [--dry-run] [--diff] [--yes] [--skip-catalog]
python3 scripts/validate_yaml.py <type> <name> [--strict]
python3 scripts/lint.py
python3 scripts/rebuild_indexes.py [--force]
python3 scripts/rebuild_entity_catalog.py
python3 scripts/rebuild_graph.py [--image-only]
```

### Maintenance

| Script | Purpose |
|--------|---------|
| `wiki_query.py` | **Canonical query tool** — structured queries across all entity types, network traversal, stats, and graph-based cross-reference suggestions. Fast path: <0.2s (precomputed index). Full path: ~30s (YAML scan). Output: JSON/table/CSV. Key subcommands: `suggest <name>` for graph-based cross-ref recommendations, `connections <name>` for graph neighbors, `path <a> <b>` for shortest path. |
| `consolidate/merge.py` | Duplicate detection + merging (`--find`, `--execute`, `--batch`) |
| `consolidate/repair.py` | YAML structural repairs (`--broken-yamls`, `--clean-sources`, `--fix-pdbs`) |
| `consolidate/verify.py` | Source-truth checks (`--pdb-in-paper`, `--identity`, `--all-proteins`) |
| `enrich_wikilinks.py` | Batch inline wikilink enrichment (local, 0 token cost; env var `YAML_TYPE`, `DRY_RUN`) |
| `enrich_protein_classification.py` | Add mpstruc/tcdb classification to protein YAMLs |
| `enrich_uniprot.py` | **Resolve Uniprot IDs for all proteins.** Batch RCSB PDB GraphQL (400 PDBs/req). Primary: PDBTM chain→entity→Uniprot. Fallback: majority vote. Writes string or list to `uniprot_id` field. Cache at `references/uniprot_cache.json`. Audit at `references/enrich_uniprot_report.json`. |
| `enrich_organism.py` | **Resolve organism field for all proteins.** Reads from PDB GraphQL cache (clean entity → direct; fusion → weighted majority with fusion partner exclusion). Cache at `references/uniprot_cache.json`. |
| `fix_wikilink_paths.py` | Bulk URL path rewrites (reads `path_fixes.json`) |
| `wiki_manifest.py` | DOI manifest management (`status`, `rebuild`, `check-entity`) |
| `aggregate_stats.py` | Generate aggregate statistics (resolution, expression, detergent matrix) |

### Used only for specific data fixes

| Script | When to use |
|--------|-------------|
| `bulk_enrich_purif.py` | **Bulk wikilink enrichment of purification/crystallization fields.** |
| `fix_yaml_quoting.py` | Fix unquoted YAML values starting with `[` (subagent corruption) |

---

## §7 — Verification Standards

When verifying YAML claims against raw papers, classify each claim as:

| Verdict | Meaning |
|---------|---------|
| CORRECT | Matches paper exactly |
| WRONG | Contradicts paper |
| NOT FOUND | Not mentioned (may be hallucinated) |
| PARTIAL | Partially correct (right PDB, wrong resolution) |
| EMBELLISHED | Based on paper but exaggerated |

**Rules:** Remove unsupported claims. Correct wrong values. Promote `verified` tier on completion: `none` → `regex` (automated pattern checks) → `agent` (subagent reads papers, confirms all claims) → `human` (domain expert review). Run `validate_yaml.py --strict` → regenerate after every promotion.

---

## §8 — DOI Assessment Comments

When processing DOIs, assign one of:

`ok` | `abstract only` | `methods in another citation` | `no purification detergent` | `no purification buffer` | `not a membrane protein` | `reagent only` | `data insufficient` | `skip — cryoEM` | `skip — review` | `skip — computational` | `duplicate`

Every processed DOI must have a comment. No blanks.

---

## §9 — Cross-Reference Type Taxonomy

Every cross_reference must have a `type` field from the controlled vocabulary below. The `reason` field (free-text) is preserved for humans; `type` is for agents and graph queries.

| Type | Meaning | Examples |
|------|---------|----------|
| `detergent_used` | Detergent in purification/solubilization/crystallization | "Solubilized in DDM", "Purified in LMNG" |
| `buffer_component` | Buffer, salt, or additive in purification | "Buffer component in SEC", "NaCl in purification" |
| `additive_used` | PEG, precipitant, cryoprotectant, imidazole | "PEG 3350 in crystallization", "Cryoprotectant" |
| `ligand_bound` | Bound ligand, agonist, antagonist, cofactor, substrate | "Co-crystallized with antagonist", "Binding partner" |
| `method_used` | Experimental method or technique | "Structure by SAD phasing", "FSEC analysis" |
| `fusion_tag` | Fusion protein or affinity tag | "T4L fusion for crystallization", "His-tag" |
| `crystallization_method` | Crystallization technique | "LCP crystallization", "Vapor diffusion" |
| `purification_method` | Purification technique | "Affinity chromatography", "SEC" |
| `related_protein` | Sequence/structure homologue or related protein | "Homologue", "Same family member" |
| `related_concept` | Related biological concept or mechanism | "Alternating access mechanism", "Active state" |
| `family_member` | Same protein family or superfamily | "ABC transporter family member" |
| `comparative_study` | Compared or referenced in same study | "Compared in same paper" |
| `entity_mentioned` | Mentioned in text, not central to the study | "Referenced in Methods section" |
| `antibiotic_selection` | Antibiotic resistance marker | "Ampicillin selection" |
| `expression_system` | Expression host or system | "Expressed in Sf9 cells" |
| `related` | **Fallback** — specific reason that doesn't fit above | Any unique descriptive sentence |

---

## §10 — Project Paths

| Path | Description |
|------|-------------|
| `/home/wtliaf/Desktop/Research/coding_projects/xray-mp-wiki/` | Project root |
| `xray-mp-wiki/proteins_yaml/*.yaml` | Protein YAML sources |
| `xray-mp-wiki/reagents_yaml/*.yaml` | Reagent YAML sources |
| `xray-mp-wiki/methods_yaml/*.yaml` | Method YAML sources |
| `xray-mp-wiki/concepts_yaml/*.yaml` | Concept YAML sources |
| `xray-mp-wiki/proteins/<subdir>/*.md` | Generated protein pages |
| `raw/papers/<doi>.md` | Source papers (local, no internet) |
| `references/entity_catalog.json` | Entity catalog (2,050+ entries) |
| `references/entity_schema.json` | Formal JSON Schema |
| `references/entity_index.json` | Precomputed query index (612KB, auto-built by wiki_query.py) |
| `scripts/` | All scripts |
