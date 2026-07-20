# xray-mp-wiki Detergent Mining — Roadmap

## Phase 1: Surface from existing corpus (done)

| Task | Artifact |
|------|----------|
| Tag-group typecheck hygiene | `yaml/` regex checks |
| Buffer_details normalization | 1,769/2,888 steps structured (61.3%) |
| CMC values for 10 detergents | `reagents_yaml/` with Anatrace source |
| Wiki dataset CSV | `raw/datasets/wiki_dataset_v1.csv` (2,279 rows) |
| Missing-detergent DOI list | `raw/datasets/missing_detergent_dois.txt` (426 DOIs) |
| Batch Elsevier SI download | `raw/supplementary/` (46/63 = 73% hit) |

## Phase 2: Raw markdown completeness (done)

1,231 raw papers from LightONOCR-1B. Classified by section coverage and OCR quality.

| Score | Count | Meaning |
|-------|-------|---------|
| 0 | 1 | <10 lines |
| 1 | 422 | No Methods section header |
| 2 | 248 | Has Methods, no DOI-bearing refs |
| 3 | 560 | Full article: Methods + DOI refs |

Scripts: `scripts/mine/assess_markdown_completeness.py`, `scripts/mine/classify_score2_ocr.py`

## Phase 3: Re-OCR all papers (current — @wtliaf)

**Goal**: Re-OCR all 1,231 raw markdowns, then label each paper with `has_detailed_methods: true|false`.

Papers without a Methods section after re-OCR → mark as stub. Papers with a Methods section → classify as "inline methods" or "see SI for methods".

**Stop condition**: all 1,231 papers re-processed. No PDFs remain — each paper needs to be re-downloaded from publisher.

## Phase 4: Citation network

CrossRef batch → get reference lists for all DOIs. Edge list: source_DOI → target_DOI.

Then overlay the `has_detailed_methods` label. Papers that lack detailed methods but cite one that has them → method inheritance edge: "methods from B". This tells us which papers we need to fetch SI for.

## Phase 5: Download additional papers/SI

Guided by Phase 4: which no-methods papers cite an uncaptured protocol paper? Download that protocol paper first.

Non-negotiable: all 426 missing-detergent DOIs still need SI/manual extraction.

## Phase 6: Synthesis

With detergent + citation data in place: detergent–family–resolution clusters, shared protocol clusters (e.g. "all lipid transporters follow ref X"), detergent-buffer-pH combinations.
