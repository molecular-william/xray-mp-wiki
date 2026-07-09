# xray-mp-wiki Change Log

| Date | Change | Impact |
|------|--------|--------|
| 2026-07-08 | Pass 2 detergent concentration normalization via subagents (3 concurrent, 208 files, 381 steps) | Coverage 97% (2,803/2,888 steps). 75 unparseable marked as empty. |
| 2026-07-08 | Removed 28 hallucinated DOIs from 22 YAML files (concepts: 22, methods: 6) | DOI coverage 84% → **100%** (3 genuine missing refs remain as known debt) |
| 2026-07-08 | Deleted 19 superseded archive scripts (superseded by consolidate/merge/repair/verify and main pipeline); kept 8 one-time scripts | Archive trimmed **27 → 8**; still runnable for audit |
| 2026-07-08 | Added `scripts/README.md` as quick-reference directory index | New contributors can orient without reading reference docs |
| 2026-07-08 | Added `wiki-aggregate-stats` entry point in pyproject.toml; removed dead `wiki-test` (pointed to deleted `test_all.py`) | Every active script now has a CLI entry point |
| 2026-07-07 | Normalized 1,292 raw paper filenames to lowercase; deleted 61 stale uppercase duplicates with partial content | Paper lookup is now case-consistent; DOIs resolve correctly |
| 2026-07-07 | Moved 9 one-time scripts to archive/; retired test_all.py (1,060 lines) | Main scripts/ down to 20 active files; one test runner (pytest) |
| 2026-07-07 | Pre-commit hooks added (ruff, trailing-whitespace, check-yaml) | Lint enforcement prevents new issues |
| 2026-07-07 | _HOST_MAP deduplicated to _base.py | Single source of truth for expression host normalization |
| 2026-07-06 | Parsed Anatrace Detergent Brochure PDF: 175 entries with MW, CMC, aggregation numbers | Structured physical property data for detergents |
| 2026-07-06 | Enriched 13 detergent YAMLs with mw/cmc from brochure (DDM, OG, DM, NG, LDAO, CYMALs, Fos-Cholines, etc.) | Every detergent page now has manufacturer-sourced physical properties |
| 2026-07-06 | Fixed `bulk_enrich_purif.py` (case-insensitive regex + nested publications structure) | Added **1,748 wikilinks** across 465 protein YAMLs — purification fields now 95% linkable |
| 2026-07-06 | Added `step_type` taxonomy to purification steps (2,684 steps classified in 649 files) | Enables queries: "which detergents at solubilization vs SEC?", "how often is detergent exchange performed?" |
| 2026-07-06 | 4 new scripts: `parse_anatrace.py`, `enrich_detergent_properties.py`, `enrich_step_types.py` + fixed `bulk_enrich_purif.py` | Infrastructure for purification pattern analysis |
| 2026-07-06 | Updated AGENT-MANIFEST.md §1 (step_type field), §6 (new scripts), §10 (Anatrace path) | Documentation stays current |
| 2026-07-06 | Triage of 417 broken links: 32 subdirectory moves, 3 non-entity types, ~140 genuinely missing | Clear picture of the broken-link landscape |
| 2026-07-06 | Applied 170 path rewrites via `path_fixes.json` | Broken links: 417 → **280** |
| 2026-07-06 | Optimized `fix_wikilink_paths.py` (combined regex + pre-filter) | Runtime: timeout → **~8s** (20× faster) |
| 2026-07-06 | Normalized detergent concentrations: 1,111 steps → structured `detergent_details` (reagent, concentration, unit) | Queryable numeric concentration data for 585 steps across 397 proteins |
| 2026-07-06 | Classified 688 expression systems into 12 canonical classes via `classify_expression.py` | Expression×resolution/detergent queries now clean |
| 2026-07-03 | Enriched 708 proteins with `uniprot_id`, 710 with `organism`, 65 tie_auto fixes | Sequence-aware, species-aware |
