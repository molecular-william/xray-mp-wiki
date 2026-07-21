# Snapshot Analysis — 2026-07-21

## 1. Scale & Coverage

| Metric | Value |
|--------|-------|
| Proteins (YAML) | 800 |
| Reagents (YAML) | 815 |
| Methods (YAML) | 70 |
| Concepts (YAML) | 483 |
| **Total entities** | **2,168** |
| Rendered wiki pages | 2,355 (including 47 subdirectory indexes) |
| Raw papers on disk | 1,231 |
| Total distinct structures | 799 |
| Resolution range | 0.88–18.0 Å (mean 2.86, median 2.80) |
| Protein families | 111 (from mpstruc_classification.subgroup) |
| Subdirectory index pages | 47 (43 content + 4 top-level category) |
| Entity catalog entries | 2,165 |
| Knowledge graph | 491 nodes, 2,647 edges |

### Top 10 protein families by structure count

| Family | Structures |
|--------|-----------|
| GPCRs: Class A | 112 |
| K/Na/H channels | 51 |
| ABC transporters | 44 |
| Bacterial/algal/viral rhodopsins | 44 |
| MFS transporters | 38 |
| Multi-drug efflux transporters | 34 |
| SLC transporters | 27 |
| Other ion channels | 24 |
| Aquaporins/glyceroporins | 20 |
| F-type ATPases | 20 |

---

## 2. Detergent Coverage

| Metric | Value |
|--------|-------|
| Total purification steps | 2,896 |
| Steps with detergent data | 1,800 (62.2%) |
| Steps with structured detergent_details | 1,180 (40.7%) |
| Distinct detergents in use | 50+ |

### Top 5 detergents

| Detergent | Proteins using it |
|-----------|------------------|
| DDM | 707 |
| CHS (cholesterol hemisuccinate) | 211 |
| DM (n-decyl-β-D-maltoside) | 168 |
| LMNG | 73 |
| OG (n-octyl-β-D-glucoside) | 68 |

**Assessment: ⚠️ Partial.** 62% of steps mention a detergent, but only 41% have fully structured `detergent_details` with parsed concentration/unit. The remaining 21% have free-text detergent mentions extractable by regex. The normalization pipeline (`normalize_detergent_concentrations.py`) exists and is idempotent — it handles 80% of cases in Pass 1. Remaining gap: ~620 steps with unstructured or missing data.

---

## 3. Buffer Coverage

| Metric | Value |
|--------|-------|
| Steps with buffer data | 2,355 (81.3%) |
| Steps with structured buffer_details | 1,766 (61.0%) |

**Assessment: ⚠️ Partial.** 61% of steps have structured `buffer_details` with component breakdown (reagent, concentration, unit, pH). The normalization script (`normalize_buffer_compositions.py`) exists and is idempotent. The ~20% gap (40.7% detergent vs 61.0% buffer) reflects that detergents are more commonly omitted from methods sections than buffers. Buffer pH is quoted-string throughout (consistent with schema).

---

## 4. Data Fitness Assessment

| Dimension | Status | Gap |
|-----------|--------|-----|
| Detergent usage by family | ✅ Ready | Structured detergent matrix in aggregate_stats.json |
| Detergent concentration (structured) | ⚠️ Partial | 41% structured; 21% extractable free-text |
| Buffer composition (structured) | ⚠️ Partial | 61% structured; 20% extractable free-text |
| Detergent × resolution correlation | ⚠️ Partial | Aggregate_stats computes it, but no rendered comparison page |
| Expression × detergent pairing | ⚠️ Partial | Data exists but no cross-tabulation page |
| Sequence/domain info (Uniprot) | ✅ Ready | 689/800 proteins have Uniprot IDs resolved |
| Step-type pipeline profiles | ✅ Ready | 21-value controlled vocabulary, 85%+ coverage |
| Crystallization conditions | ⚠️ Partial | 798/1,088 entries have structured crystallization_details (73%) |
| Search across all entities | ✅ New | Client-side search index with filter buttons added this session |
| Subdirectory browsing | ✅ New | 47 index pages added this session |
| Landing page stats | ✅ New | Auto-generated _data/stats.yml with tables |

---

## 5. Infrastructure Assessment

### CLI Design — ✅ Good
- All scripts support `--dry-run`, `argparse` help, and sensible defaults
- Entry points via `pyproject.toml` (`wiki-*` commands) for installed use
- Machine-readable JSON output from lint, aggregate_stats, wiki_query

### Skill System — ✅ Good (recently improved)
- 8 wiki skills, downsized from 4,921 to 751 lines this session
- Principles-only skills with pointers to repo reference files
- `wiki-yaml-repair` patterns moved to `references/yaml-repair-patterns.md`

### Validation Gates — ✅ Strong
- `validate_yaml.py --strict` with 25+ checks (tags, DOI format, step_type enum, unquoted numerics, wikilink syntax)
- `lint.py` — 10 checks (broken links, orphans, stale pages, stale cross-refs, duplicates)
- `.pre-commit-config.yaml` with ruff + trailing-whitespace + check-yaml
- 52 tests, 3 xfailed (pre-existing data debt)

### Error Recovery — ✅ Strong
- `--dry-run` on all modifying scripts (detergent, buffer, crystallization normalization)
- Snapshot archives before destructive operations
- `fix_yaml_quoting.py` for yaml.dump bracket corruption
- `_load_one_yaml` exception handling (skips broken files, logs warnings)

### Script Speed — ✅ Excellent (improved this session)

| Script | Before | After | Speedup |
|--------|--------|-------|---------|
| aggregate_stats | 58.5s | **1.1s** | **53x** |
| rebuild_entity_catalog | 31.4s | **0.9s** | **35x** |
| normalize_detergent_concentrations | 33.7s | **3.1s** | **11x** |
| normalize_buffer_compositions | 31.1s | **3.1s** | **10x** |
| normalize_crystallization | ~30s | **3.0s** | **10x** |
| lint | 1.9s | **1.0s** | 2x |

Methods: yaml.CSafeLoader (8x) + multiprocessing (4x) = ~32x cumulative.

### Agent Onboarding — ⚠️ Requires reading
- Entry point: `wiki-maintenance` skill → points to `references/AGENT-MANIFEST.md`
- AGENT-MANIFEST.md (312 lines) is comprehensive: schema, NEVER list, 10 principles, controlled vocabularies
- Scripts reference: `wiki-scripts` skill → `scripts/README.md`
- However: 8 wiki skills to scan, several reference files to load. A new agent needs ~5 skill loads + ~3 reference file reads before it can operate.

### Automation Readiness — ✅ Good
- All enrichment scripts idempotent, runnable from cron
- Cron job infrastructure exists (`cronjob` tool)
- JSON outputs chainable: aggregate_stats.json → generate_stats_data.py → _data/stats.yml
- GitHub Pages build via `.github/workflows/jekyll.yml`

---

## 6. Research Readiness

| Research question | Status | How to answer |
|------------------|--------|---------------|
| Which detergents per family? | ✅ Ready | aggregate_stats.json → detergent_matrix |
| DDM concentration range per family? | ✅ Ready | aggregate_stats.json → detergent_conc_ranges |
| Buffer pH × resolution? | ⚠️ Partial | pH is in buffer_details; resolution is in structures. No cross-calculated table yet. Would need aggregate_stats to add this dimension (~1 day). |
| Detergent exchange patterns? | ✅ Ready | aggregate_stats.py computes 43 exchange events |
| Crystallization method × detergent? | ⚠️ Partial | 73% of crystallizations have structured method_lc; detergent is at step level. Cross-referencing requires query join. |
| Expression system × detergent? | ✅ Ready | expression.class + detergent_details both structured |
| What detergent for a new GPCR? | ✅ Ready | Browse /proteins/gpcr/ → 125 entries → DDM/LMNG dominant |
| Which detergents are most common for Class A GPCRs? | ✅ Ready | GPCR Class A has ~383 detector mentions (DDM, CHS, DM, LMNG) |

### Key actionable gaps

1. **Buffer pH × resolution correlation** — data exists but not aggregated. Would be a powerful figure for the landing page ("higher pH correlates with better resolution for transporters?").
2. **Crystallization method × detergent × resolution** — three tables that exist but aren't joined. A cross-tabulation script would enable "LCP with LMNG gives better resolution than with DDM for GPCRs" type queries.
3. **1,179 stale pages** — pages not regenerated after schema changes. They render but may have broken sections.

---

## 7. Next Steps

| Priority | Task | What it enables | Effort |
|----------|------|-----------------|--------|
| **P0** | Fix `rebuild_indexes` catalog markers in index.md (currently "not found" error) | Catalog regeneration works again | 30 min |
| **P0** | Regenerate 1,179 stale pages | All pages render current schema | 2 hrs (parallel batch) |
| **P1** | Add buffer pH × resolution table to aggregate_stats | "Which pH for my target resolution?" query | ~1 day |
| **P1** | Cross-tabulation: crystallization method × detergent × family | "LCP vs vapor diffusion with LMNG for GPCRs" | ~1 day |
| **P2** | Full-text search across raw papers (not just entity titles) | Search across 1,231 methods sections | ~2 days (lunr index build over raw text) |
| **P2** | Fix the focA-vibrio-cholerae.yaml broken YAML | Clean validate_yaml across all 800 proteins | 30 min |
| **P3** | Automated snapshot on git push | Always have a recent backup | ~2 hrs (GitHub Actions) |
| **P3** | Visual browse: per-entity mini-graphs | See related entities without scrolling to cross-refs | ~1 day |

---

## Appendix: File sizes

| Directory | Size |
|-----------|------|
| `xray-mp-wiki/` (rendered site) | ~95 MB |
| `raw/papers/` (OCR outputs) | ~130 MB |
| `scripts/` | ~1.2 MB |
| `references/` | ~3.5 MB |
| `xray-mp-wiki/_data/` | ~0.5 MB (new: stats.yml + search_index.json) |

**Archive estimate:** `snapshot-20260721.zip` ~250 MB (including raw papers).
