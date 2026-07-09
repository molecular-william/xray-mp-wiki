# scripts/ — xray-mp-wiki Scripts

**Run all scripts from project root:** `python3 scripts/<name>.py [args]`
**Or via entry point:** `pip install -e .` then `wiki-<name> [args]`

---

## Quick Reference

### Core pipeline (run in order after batch changes)

```
validate_yaml.py → generate_page.py → lint.py → rebuild_indexes.py → rebuild_entity_catalog.py → rebuild_graph.py
```

| Script | What | Entry point |
|--------|------|-------------|
| `generate_page.py` | YAML → `.md` page (all 4 entity types) | `wiki-generate-page` |
| `validate_yaml.py` | Schema validation gate | `wiki-validate` |
| `lint.py` | Health audit (links, orphans, duplicates, DOI format) | `wiki-lint` |
| `rebuild_indexes.py` | Rebuild `index.md` catalog | `wiki-rebuild-indexes` |
| `rebuild_entity_catalog.py` | Rebuild `entity_catalog.json` (use `--from-filesystem` for full scan) | `wiki-rebuild-entity-catalog` |
| `rebuild_graph.py` | Rebuild `assets/graph.json` | (none) |

### Renderers (called by `generate_page.py`)

| File | Entity type |
|------|-------------|
| `protein_page_renderer.py` | Proteins — publications, sequences, topology, expression badges |
| `reagent_page_renderer.py` | Reagents — detergents, lipids, buffers, ligands, tags |
| `method_page_renderer.py` | Methods — protocols, advantages, related methods |
| `concept_page_renderer.py` | Concepts — mechanism, examples, cross-references |

### Enrichment & data augmentation

| Script | What it does | Entry point |
|--------|-------------|-------------|
| `enrich_wikilinks.py` | Add inline wikilinks to purification/crystallization fields | `wiki-enrich-wikilinks` |
| `enrich_protein_classification.py` | Add mpstruc/TCDB classification to proteins | (none) |
| `enrich_uniprot.py` | Resolve Uniprot IDs via RCSB PDB GraphQL | (none) |
| `enrich_organism.py` | Derive organism from PDB entity data | (none) |
| `bulk_enrich_purif.py` | Regex-based wikilink enrichment (DDM, LMNG, CHS, etc.) | (none) |

### Shared libraries

| File | Provides |
|------|----------|
| `_base.py` | Everything: `build_paths`, `parse_args`, `load_yaml`, `generate_main`, `HOST_MAP`, `normalize_host`, `normalize_hosts`, `render_frontmatter`, subdirectory finders (`find_protein_subdir`, `find_reagent_subdir`, `find_method_subdir`, `find_concept_subdir`) |
| `__init__.py` | Package init, version |

### Maintenance & fixes

| Script | When to use |
|--------|-------------|
| `fix_wikilink_paths.py` | Path rewrites after subdirectory moves (reads `path_fixes.json`) |
| `fix_yaml_quoting.py` | Fix unquoted `[` values from subagent corruption |

### Queries & reporting

| Script | What it does |
|--------|-------------|
| `wiki_query.py` | Canonical query tool — structured queries, graph traversal, stats, cross-ref suggestions |
| `wiki_manifest.py` | DOI manifest management — status, rebuild, check-entity |
| `aggregate_stats.py` | Generate aggregate statistics (resolution, detergents, expression, steps) | `wiki-aggregate-stats` |
| `normalize_detergent_concentrations.py` | Parse free-text detergent → structured `detergent_details` with concentration | (none — run via `python3 scripts/...`) |
| `normalize_buffer_compositions.py` | Parse free-text buffer → structured `buffer_details` with pH, components | (none — run via `python3 scripts/...`) |

### Consolidation utilities

| Script | What it does | Key flags |
|--------|-------------|-----------|
| `consolidate/merge.py` | Duplicate detection + merging | `--find`, `--execute`, `--batch`, `--candidates` |
| `consolidate/repair.py` | YAML structural repairs | `--broken-yamls`, `--clean-sources`, `--fix-pdbs`, `--fix-doubled-paths`, `--all` |
| `consolidate/verify.py` | Source-truth checks | `--pdb-in-paper`, `--identity`, `--alias-matches`, `--all-proteins` |

### Tests (run with `python3 -m pytest scripts/`)

| File | Tests | Speed |
|------|-------|-------|
| `test_generate.py` | 17 | Fast — generation pipeline |
| `test_validate.py` | 8 | Fast — schema validation |
| `test_wiki_query.py` | 17 | Fast — WikiQuery + sequence renderer + roundtrip |
| `test_maintenance.py` | 6 | Slow — manifest, enrichment, rebuild (use `--run-slow`) |
| `test_data_integrity.py` | 7 | Slow — full-scan crossref/DOI/catalog integrity |

### Archive (`archive/`)

8 one-time scripts from past fix campaigns, preserved for audit. Still runnable:
`python3 scripts/archive/<name>.py`

---

## When in doubt

**`references/WIKI-SCRIPTS.md`** — full documentation with examples, edge cases, and workflow advice.
**`references/AGENT-MANIFEST.md`** — constitution: schema, tags, conventions, prohibitions.
**`.pre-commit-config.yaml`** — lint enforcement (ruff check + format, trailing-whitespace, check-yaml).
