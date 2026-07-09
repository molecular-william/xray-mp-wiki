# X-ray MP Wiki — Scripts Reference (Concise)

Run all scripts from project root (not `scripts/`).

## Script Layout (2026-07-07 Refresh)

```
scripts/
├── _base.py                     # Shared: path building, YAML, catalog, subdirectory detection, HOST_MAP
├── _subdir_utils.py             # Subdirectory detection per entity type
├── generate_page.py             # Unified entry: generate page from YAML
├── validate_yaml.py             # Schema validator + CLI
├── lint.py                      # Health audit (broken links, orphans, duplicates, DOI format)
├── {protein,reagent,method,concept}_page_renderer.py
├── rebuild_indexes.py           # Rebuild wiki catalog in index.md
├── rebuild_entity_catalog.py    # Rebuild entity_catalog.json
├── rebuild_graph.py             # Build knowledge graph JSON for graph.md; optional static PNG
├── enrich_wikilinks.py          # Batch inline wikilink enrichment (local, 0 token cost)
├── enrich_protein_classification.py  # Add mpstruc/tcdb classification to protein YAMLs
├── enrich_uniprot.py             # Batch resolve Uniprot IDs via RCSB PDB GraphQL
├── enrich_organism.py            # Derive organism field from PDB GraphQL cache
├── bulk_enrich_purif.py         # Bulk enrich purification/crystallization fields (local, fast)
├── fix_wikilink_paths.py        # Bulk URL path rewrites (reads path_fixes.json)
├── fix_yaml_quoting.py          # Fix unquoted YAML values starting with [
├── wiki_manifest.py             # DOI manifest management (status/rebuild/check-entity)
├── wiki_query.py                # Canonical query tool: structured queries, graph traversal, stats
├── aggregate_stats.py           # Aggregate statistics (resolution, expression, detergent matrix)
├── path_fixes.json              # URL mappings (data, not code)
├── conftest.py                  # Pytest shared fixtures
├── test_generate.py             # Pytest: generation pipeline
├── test_validate.py             # Pytest: validation
├── test_wiki_query.py           # Pytest: WikiQuery + roundtrip + sequence renderer
├── test_data_integrity.py       # Pytest: full-scan crossref/DOI/catalog integrity
├── test_maintenance.py          # Pytest: rebuild_entity_catalog, wiki_manifest, enrich_wikilinks, base utils
├── consolidate/
│   ├── merge.py                 # Duplicate detection + merging: --find --execute --batch
│   ├── repair.py                # YAML structural repairs: --broken-yamls --clean-sources --fix-pdbs
│   └── verify.py                # Source-truth checks: --pdb-in-paper --alias-matches --all-proteins
└── archive/                     # **8 one-time scripts preserved for audit (runnable)**
    ├── restructure_proteins.py  # DOI-grouped YAML migration (Jun 2026)
    ├── parse_anatrace.py        # Anatrace detergent PDF extraction (Jul 2026)
    ├── enrich_detergent_properties.py  # Add mw/cmc to detergent YAMLs (Jul 2026)
    ├── normalize_detergent.py   # Normalize detergent concentrations (Jul 2026)
    ├── enrich_step_types.py     # Add step_type taxonomy (Jul 2026)
    ├── enrich_crossref_types.py # Add controlled type to all cross-refs (Jun 2026)
    ├── classify_expression.py   # Expression classification (Jul 2026)
    └── fix_pdb_format.py        # PDB format cleanup
```
## Core Pipeline

Run in this order after batch changes:

```bash
# 1. Generate pages from YAML
generate_page.py <type> <name> [--dry-run] [--diff] [--yes] [--skip-catalog]

# 2. Validate YAML (before generating is ideal; also useful standalone)
validate_yaml.py <type> <name> [--strict]

# 3. Check health
lint.py

# 4. Rebuild indexes (MUST be in this order)
rebuild_indexes.py [--force]              # rebuild index.md catalog
rebuild_entity_catalog.py                  # rebuild entity_catalog.json (reads from index.md)
rebuild_graph.py [--image-only]           # rebuild graph.json + optional PNG of top-100 hubs
```

**Order matters:** `rebuild_entity_catalog.py` reads the catalog from `index.md` (written by `rebuild_indexes.py`). `rebuild_graph.py` reads `entity_catalog.json`. Running them out of order produces stale data.

**Batch regeneration:** Use `--skip-catalog` on each `generate_page.py` call, then run `rebuild_indexes.py --force` once at the end. Saves ~0.3s per page (790 proteins × 0.3s = ~4min).

**Stale catalog fix:** If `entity_catalog.json` is out of sync with YAML files on disk, run:
```bash
python3 scripts/rebuild_entity_catalog.py --from-filesystem
```
This scans YAML files directly instead of using the manifest.

### Flag details

| Flag | Applies to | Effect |
|------|-----------|--------|
| `--dry-run` | `generate_page.py` | Print generated page to stdout, don't write |
| `--diff` | `generate_page.py` | Show unified diff against existing page |
| `--yes` | `generate_page.py` | Skip overwrite confirmation |
| `--skip-catalog` | `generate_page.py` | Don't update catalog (batch mode — rebuild once at end) |
| `--strict` | `validate_yaml.py` | Enable tag-taxonomy enforcement (warnings → errors) |
| `--force` | `rebuild_indexes.py` | Rebuild catalog from scratch (remove all, rescan) |
| `--image-only` | `rebuild_graph.py` | Skip static PNG render (JSON only). Default: JSON + PNG. |
| `--from-filesystem` | `rebuild_entity_catalog.py` | Scan YAML files directly instead of reading manifest |

## Consolidation Scripts

### consolidate/merge.py
```bash
python3 scripts/consolidate/merge.py --find --type proteins    # find duplicates
python3 scripts/consolidate/merge.py --find --all              # all 4 entity types
python3 scripts/consolidate/merge.py --execute reagents        # merge interactively
python3 scripts/consolidate/merge.py --batch                   # run approved batch
python3 scripts/consolidate/merge.py --candidates              # scan for merge candidates
python3 scripts/consolidate/merge.py --dry-run                 # preview
```

### consolidate/repair.py
```bash
python3 scripts/consolidate/repair.py --broken-yamls           # fix unparseable YAMLs
python3 scripts/consolidate/repair.py --clean-sources          # remove dicts from sources
python3 scripts/consolidate/repair.py --fix-pdbs               # extract PDB codes from strings
python3 scripts/consolidate/repair.py --fill-pdbs              # fill empty PDBs from MPSTRUC
python3 scripts/consolidate/repair.py --check-wikilinks        # scan broken wikilinks
python3 scripts/consolidate/repair.py --fix-doubled-paths      # fix duplicated path segments
python3 scripts/consolidate/repair.py --all                    # run all repairs
```

### consolidate/verify.py
```bash
python3 scripts/consolidate/verify.py --pdb-in-paper <name>    # check PDBs against source papers
python3 scripts/consolidate/verify.py --identity <name>        # verify protein identity in source
python3 scripts/consolidate/verify.py --alias-matches          # find entity name→page matches
python3 scripts/consolidate/verify.py --all-proteins           # comprehensive protein data check
python3 scripts/consolidate/verify.py --all                    # run all non-specific checks
```

## Additional Maintenance Scripts

### bulk_enrich_purif.py
Regex-based enrichment of purification/crystallization YAML fields with inline wikilinks. Fast local script, 0 token cost. Scans for common reagent names (DDM, LMNG, OG, CHS, TEV, BRIL, Ni-NTA, etc.) and inserts wiki links.

```bash
python3 scripts/bulk_enrich_purif.py    # runs with hardcoded entity list
```

### fix_yaml_quoting.py
Fixes a common subagent corruption pattern: unquoted YAML values starting with `[`.

```bash
python3 scripts/fix_yaml_quoting.py     # scans and fixes all protein YAMLs in-place
```

### wiki_query.py
Canonical query tool for agents. Structured queries across all entity types, graph traversal, and statistics. Outputs JSON (default), table, or CSV.

**Fast path** (catalog + precomputed index, <0.2s):
```bash
python3 scripts/wiki_query.py stats --format table
python3 scripts/wiki_query.py get ddm
python3 scripts/wiki_query.py entities --type proteins --limit 5
python3 scripts/wiki_query.py search adenosine --limit 5
python3 scripts/wiki_query.py connections ddm --depth 2
python3 scripts/wiki_query.py path ddm kcsa
```

**Full path** (YAML scan, ~30s for first query, then cached):
```bash
python3 scripts/wiki_query.py proteins --tag gpcr --format table
python3 scripts/wiki_query.py proteins --detergent ddm --limit 10
python3 scripts/wiki_query.py proteins --resolution-max 2.0 --family GPCR
python3 scripts/wiki_query.py reagents --subdir detergents --cmc-max 1.0
python3 scripts/wiki_query.py counts --by family
python3 scripts/wiki_query.py resolution-stats
```

**Precomputed index** at `references/entity_index.json` (612KB) auto-generated on first query. Rebuild manually:
```bash
python3 scripts/wiki_query.py rebuild    # ~30s, then subsequent queries <0.2s
```

**Output format** (all queries support `--format`):
```bash
python3 scripts/wiki_query.py proteins --tag gpcr --limit 5 --format table   # human-readable
python3 scripts/wiki_query.py proteins --tag gpcr --limit 5 --format csv     # spreadsheet
python3 scripts/wiki_query.py proteins --tag gpcr --limit 5                   # JSON (default)
```

### aggregate_stats.py
Generate aggregate statistics from existing structured data (resolution per family, expression×resolution, detergent matrix, step-type counts, buffer frequency).

```bash
python3 scripts/aggregate_stats.py    # writes to references/stats/aggregate_stats.json
```

## Key Updates

### 2026-07-07 — Script Reorganization
- **9 one-time scripts moved to archive/:** restructure_proteins, parse_anatrace, enrich_detergent_properties, normalize_detergent, enrich_step_types, enrich_crossref_types, validate_dois, classify_expression, verify_prescreen
- **test_all.py retired:** 1,060-line custom test runner deleted. Tests migrated to `test_maintenance.py` (6 tests: rebuild_entity_catalog, wiki_manifest, enrich_wikilinks, base utilities)
- **DOI filename normalization:** All 1,292 raw paper filenames lowercased. 61 stale uppercase duplicates with partial content deleted (lowercase twins kept as authoritative)
- **55 test files consolidated:** 5 test files (53 pass + 2 xfail)
- **Pre-commit hooks added:** `.pre-commit-config.yaml` with ruff + trailing-whitespace + end-of-file-fixer + check-yaml
- **`_HOST_MAP` deduplicated:** Moved from wiki_query.py + protein_page_renderer.py to `_base.py`

### 2026-07-06 — Purification Pattern Analysis
- Parsed Anatrace Detergent Brochure: 175 entries
- Enriched 13 detergent YAMLs with mw/cmc
- Added 1,748 wikilinks across 465 protein YAMLs
- Added step_type taxonomy (2,684 steps in 649 files)

### 2026-06-30 — wiki_query.py & Precomputed Index
- Canonical query tool with structured queries, graph traversal, stats
- Precomputed index at `references/entity_index.json` (612KB)
- All query types tested

### 2026-06-30 — Graph Edge Typing (Cross-Reference Types)
- Controlled `type` field to all 10,687 cross-references
- AGENT-MANIFEST.md §9: 16-item type taxonomy

### 2026-06-30 — Renderer Refresh
- Position ruler, topology coloring, line width 60→120

### 2026-06-25 — Script Consolidation
- 50 scripts → 20 main + 3 consolidate + 27 archived

## Architecture Notes

- **YAML-first:** Edit YAML → regenerate page. No update scripts. YAML is single source of truth.
- **Subdirectory placement:** Proteins auto-assigned via `mpstruc_classification.subgroup` → `PROTEIN_SUBDIR_MAP`. Reagents/methods use `subdirectory-*` tags. Concepts use keyword classifier.
- **graph.json:** Auto-rebuilt by `rebuild_graph.py`. Interactive visualization at `/xray-mp-wiki/graph/`.
- **path_fixes.json:** Central registry for URL migrations. Add entries when moving entities between subdirectories.
- **entity_index.json:** Precomputed query index (612KB). Auto-built by `wiki_query.py` on first query.
- **entity_catalog.json:** 2,128 entries from filesystem scan. Rebuild with `rebuild_entity_catalog.py --from-filesystem`.
- **Archived scripts still runnable:** `python3 scripts/archive/repair_broken_yamls.py` still works. Archive is for clutter reduction, not deletion.
