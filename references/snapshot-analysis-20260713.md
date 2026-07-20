# Snapshot Analysis — 2026-07-13

## 1. Scale & Coverage

| Metric | Value |
|--------|-------|
| Entity catalog entries | 2,120 |
| Proteins | 790 |
| Reagents | 802 |
| Methods | 70 |
| Concepts | 458 |
| Cross-ref edges | 2,642 |
| Graph nodes | 490 |
| Raw papers on disk | ~1,285 |
| Steps scanned | 2,888 |
| Resolutions recorded | 1,568 |

**Resolution:** mean 2.86 Å, median 2.80 Å. Best 0.88 Å (5-HT2A), worst 7.94 Å.  
**Families:** 110 families, 790 proteins. Class A GPCRs are the largest (112, 233 structures).  
**Expression:** E. coli dominates (51.5%), followed by Sf9 (17.9%), native tissue (6.4%), P. pastoris (6.1%), HEK293 (5.1%). Cell-free gives the best resolution (1.99 Å mean).  
**Detergent exchange:** 180/790 (22.8%) have exchange steps. DDM→CHS→DDM is the most common pattern (26 proteins).

## 2. Detergent Coverage

DDM is the most common detergent across nearly every family (702 mentions). GPCRs show an unusual dual-detergent pattern: DDM (141) and cholesterol-hydrogen-succinate (140) together — reflecting the GPCR-specific LCP methodology where CHS is added as a stabilizing additive. DM is dominant in potassium channels (63). LMNG (73) clusters heavily in GPCRs (40). Structured detergent_details exist for most steps but many use w/v% rather than mM.

**Top 5 detergents:** DDM (702), CHS (210), DM (168), LMNG (73), OG (68).

## 3. Buffer Coverage

Buffer composition is the weakest dimension. 1,769/2,888 steps have structured buffer_details (61.3%). The remaining 1,119 steps have free-text buffer fields only. Most structured buffers have the reagent name parsed, but pH is missing from ~30% of structured entries. Tris, HEPES, and NaCl are the dominant components across all families.

## 4. Data Fitness Assessment

| Dimension | Status | Gap |
|-----------|--------|-----|
| Detergent usage by family | ✅ ready | Aggregated in stats, queryable |
| Detergent concentration | ⚠️ partial | ~70% structured, 30% free-text; unit inconsistency (w/v% vs mM) |
| Buffer composition | ❌ blocked | 38.7% free-text; pH missing from ~30% of structured |
| Detergent × resolution | ✅ ready | Directly queryable via wiki_query |
| Expression × detergent | ⚠️ partial | Most YAMLs have expression system populated; detergent linked to steps |
| Sequence / domain info | ⚠️ partial | Uniprot IDs present for most proteins; no Pfam/TMHMM |
| Step-type pipeline profiles | ✅ ready | 20 step types, aggregated per family |

## 5. Infrastructure Assessment

| Dimension | Status | Notes |
|-----------|--------|-------|
| CLI design | ✅ ready | ~25 scripts with argparse, `--dry-run`, most produce JSON |
| Skill system | ✅ ready | ~15 skills covering verification, repair, enrichment, bulk ops |
| Validation gates | ✅ ready | `validate_yaml.py --strict`, `lint.py`, pre-commit, schema validation |
| Error recovery | ✅ ready | Dry-run on every destructive op, repair scripts, `consolidate/` scripts |
| Agent onboarding | ⚠️ partial | AGENT-MANIFEST is authoritative but long (4,300 tokens). Subagents need their own briefings (`references/subagent-*.md`). |
| Automation readiness | ✅ ready | Cron jobs, JSON chaining, pipeline scripts, no-gui operation |

## 6. Research Readiness

| Research question | Status | Blocker |
|---|---|---|
| Which detergents per family? | ✅ ready | — |
| DDM concentration range per family? | ⚠️ partial | Free-text concentrations in 30% of steps |
| Buffer pH × resolution? | ❌ blocked | 30% of structured buffers lack pH; 38.7% of steps have free-text buffers |
| Detergent exchange patterns? | ✅ ready | 22.8% have exchange; most common pattern: DDM→CHS→DDM |
| Crystallization method × detergent? | ⚠️ partial | Methods tagged but not all linked to specific detergent at crystallization step |
| Expression system × detergent? | ⚠️ partial | Most YAMLs have expression; detergent in steps — query needs join logic |

## 7. Next Steps

| Priority | Task | Enables | Effort |
|----------|------|---------|--------|
| P0 | Fix the 20 remaining regex files (DOI re-parenting, wrong PDBs) | 92% → 100% protein verification | 1 session |
| P0 | `normalize_buffer_compositions.py` — parse remaining free-text buffers | Queryable buffer×pH×resolution | 1–2 sessions |
| P1 | Phase out w/v% → w/v for unit consistency | Clean concentration queries | 1 session |
| P1 | Populate missing pH in structured buffer_details | Buffer pH×resolution correlation | 1 session |
| P2 | Add Pfam/TMHMM to protein YAMLs | Sequence-aware detergent analysis | 2 sessions |
| P2 | Bulk reagent verification (374 at regex) | 54% → 100% reagent verification | 2–3 sessions |
| P3 | Method verification (70 at none) | Full method coverage | 1 session |
| P3 | Concept verification (455 at none) | Full concept coverage | 2 sessions |
