# Agent Verification Plan — `verified: agent` Across the Corpus

**Goal:** Promote every YAML from its current verification tier to `verified: agent`
by having LLM subagents read the cited raw papers and confirm all claims.

---

## §0 — Current State

| Entity Type | Total | `verified: none` | `verified: regex` | `verified: agent` | `verified: human` | No field / other |
|-------------|-------|-----------------|-------------------|-------------------|-------------------|------------------|
| **Proteins** | 790 | 0 | 777 | 10 | 0 | 0 — all have field |
| **Reagents** | 803 | 4 (`"none"`) | 0 | 18 | 0 | 277 missing + 504 `verified: false` |
| **Methods** | 70 | 7 (`"none"`) | 0 | 0 | 0 | 28 missing + 35 `verified: false` |
| **Concepts** | 458 | 0 | 0 | 3 | 0 | 152 missing + 303 `verified: false` |

**Problems:**
1. Non-protein entities use `verified: false` instead of the valid enum value `verified: "none"`
2. 457 YAMLs across reagents/methods/concepts have no `verified` field at all
3. Only 31 pages have `verified: agent` (10 proteins + 18 reagents + 3 concepts)
4. 104 protein files have at least one missing raw paper (125 papers total missing)

---

## §1 — Phase 0: Standardize to Valid Enum (Deterministic Script, 0 tokens)

**Goal:** Every YAML gets a valid `verified` field. Replaces `false` → `"none"`, adds
field where absent.

**Why first:** Subagents and the validator both need a consistent field to write to.
Running subagent verification on files with `verified: false` means they'd see a
non-standard value and either get confused or waste tokens fixing it.

### Script: `scripts/normalize_verified_field.py`

```python
"""Standardize the verified field across all entity YAMLs.
- no field → add `verified: "none"`
- `verified: false` → `verified: "none"`
- `verified: "none"` / `verified: regex` / `verified: agent` / `verified: human` → leave as-is
"""
import yaml
from pathlib import Path

BASE = Path("xray-mp-wiki")
VALID = {"none", "regex", "agent", "human"}

for yaml_dir in [BASE / "proteins_yaml", BASE / "reagents_yaml",
                 BASE / "methods_yaml", BASE / "concepts_yaml"]:
    for yf in sorted(yaml_dir.glob("*.yaml")):
        raw = yf.read_text()
        data = yaml.safe_load(raw)
        if not isinstance(data, dict):
            continue
        current = data.get("verified")
        if current is None:
            # Add field after 'updated' if present, else after 'sources'
            pass  # need ruamel.yaml or text-based insert
        elif current is False:  # Python bool False from `verified: false`
            pass  # replace with "none"
        # else valid string — skip
```

**Approach:** Use ruamel.yaml for round-trip preservation. Insert `verified: "none"`
after `updated:` (or `sources:` as fallback).

**Coverage:** ~2,121 files. Runs in <30s. Zero tokens.

### Output after Phase 0

| Type | `none` | `regex` | `agent` | `human` |
|------|--------|---------|---------|---------|
| Proteins | 3 | 777 | 10 | 0 |
| Reagents | 785 | 0 | 18 | 0 |
| Methods | 70 | 0 | 0 | 0 |
| Concepts | 455 | 0 | 3 | 0 |

---

## §2 — Phase 1: Promote Non-Proteins to `regex` (Deterministic, 0 tokens)

**Goal:** Run equivalent of `verify_prescreen.py` on reagents, methods, concepts.

The original `verify_prescreen.py` checked proteins for: source DOI file exists on
disk, PDB IDs appear in paper text, resolution in paper, space group in paper,
expression host in paper. Reagents/methods/concepts don't have PDB IDs, resolution,
or space groups — they only need a source-paper-exists check.

### Script: `scripts/promote_to_regex.py`

```python
"""Promote verified: none → verified: regex for non-protein entities.
Check: all source DOIs have a matching raw paper file on disk.
"""
```

**Checks per entity type:**

| Check | Proteins (already done) | Reagents | Methods | Concepts |
|-------|----------------------|----------|---------|----------|
| DOI files exist | ✅ Already checked | ✅ Check each source DOI | ✅ Same | ✅ Same |
| PDB in paper | ✅ Checked | N/A | N/A | N/A |
| Resolution in paper | ✅ Checked | N/A | N/A | N/A |
| Space group in paper | ✅ Checked | N/A | N/A | N/A |
| Expression host in paper | ✅ Checked | N/A | N/A | N/A |

For 3 proteins that somehow show `none` after Phase 0 (the ones with 0 sources or
missing papers), re-run the protein prescreen check to see if they can go to `regex`.

**Coverage:** ~1,310 non-protein files. Runs in <10s. Zero tokens.

### Output after Phase 1

| Type | `none` | `regex` | `agent` | `human` |
|------|--------|---------|---------|---------|
| Proteins | 3 | 777 | 10 | 0 |
| Reagents | ~0 | ~785 | 18 | 0 |
| Methods | ~0 | ~70 | 0 | 0 |
| Concepts | ~0 | ~455 | 3 | 0 |

Files staying at `none` will be those whose source papers are genuinely missing on
disk. These are separate from the agent verification workflow — they need paper
acquisition first.

---

## §3 — Phase 2: `verified: agent` for Proteins

**This is the main effort.** Each subagent reads protein YAMLs + their cited papers
and confirms all claims.

### 3.1 Batch Design

**Key numbers:**
- 777 proteins at `regex` to promote to `agent`
- 540 have exactly 1 source paper
- 134 have 2 source papers
- Median YAML + paper size: ~55KB (~14K tokens)
- 104 files have at least one missing paper (skip these)

**Batch strategy:** 10-12 files per subagent, grouped by paper count:

| Group | Paper count | Files | Files per batch | Batches | Token budget per batch |
|-------|-------------|-------|-----------------|---------|----------------------|
| A | 1 paper only | ~460 | 12 | ~39 | ~170K tokens |
| B | 2 papers | ~110 | 10 | ~11 | ~280K tokens |
| C | 3-5 papers | ~55 | 6 | ~10 | ~250K tokens |
| D | 6-10 papers | ~10 | 3 | ~4 | ~200K tokens |
| E | 11-19 papers | ~8 | 1-2 | ~6 | ~250K tokens |

**Total batches:** ~70 subagent calls (3 concurrent → ~24 rounds)

### 3.2 Pre-Batch Processing Script

Script `scripts/prep_verification_batches.py` outputs JSON batch files:

```bash
python3 scripts/prep_verification_batches.py --type protein --output references/verify_batches/
```

Output per batch: `protein_verify_batch_N.json` with:
```json
{
  "batch_id": 1,
  "files": [
    {
      "name": "kcsa",
      "yaml_path": "xray-mp-wiki/proteins_yaml/kcsa.yaml",
      "papers": [
        "raw/papers/10.1126##science.280.5360.69.md",
        "raw/papers/10.1038##35102009.md"
      ],
      "existing_papers": 18,
      "missing_papers": ["raw/papers/10.1016##j.jmb.2021.167296.md"],
      "yaml_size_bytes": 220000,
      "paper_total_size_bytes": 780000,
      "estimated_tokens": 195000,
      "skip_reason": null
    }
  ],
  "total_estimated_tokens": 1850000
}
```

Also output a **skip list** for files with missing papers — these need paper
acquisition before agent verification.

### 3.3 Verification Scope (What the Subagent Checks)

Subagents verify claims in priority order. If context is tight, skip lower-priority
checks but report the gap.

| Priority | Category | What to verify | How to verify |
|----------|----------|----------------|---------------|
| **P0** | DOI → paper | Each `sources[]` DOI has a matching paper on disk | Check file exists at `raw/papers/<doi>.md` |
| **P1** | PDB IDs | Every `structures[].pdb_id` matches one in the paper text | Case-insensitive grep for the 4-char code in paper |
| **P1** | Resolution | `structures[].resolution` matches paper's stated value | Find resolution table in paper |
| **P1** | Expression host | `expression.system` matches paper | Search for cell line/organism mention |
| **P2** | Detergents | `detergent_details[].reagent` names appear in paper | Search for detergent name in paper |
| **P2** | Buffers | `buffer_details[].reagent` concentrations/pH match paper | Search for buffer components |
| **P2** | Crystallization method | `crystallizations[].method` matches paper | Check method section |
| **P3** | Biological insights | Each `biological_insights[].content` is supported | Find supporting text in paper |
| **P3** | Construct details | Residues, mutations, tags match paper | Check construct section |
| **P3** | Cross-references | Cross-referenced entities exist and are relevant | Query entity_catalog.json |

### 3.4 Subagent Prompt Template

```
You are a membrane protein structural biologist verifying claims in a wiki against
raw research papers.

## Task
Read each YAML file and its cited papers. Classify every claim as CORRECT, WRONG,
NOT FOUND, PARTIAL, or EMBELLISHED per the verification standards below. For WRONG
or NOT FOUND claims, output the fix needed.

## Verification Standards
- CORRECT: Matches paper exactly
- WRONG: Contradicts paper
- NOT FOUND: Not mentioned in paper (may be hallucinated)
- PARTIAL: Partially correct (right PDB, wrong resolution)
- EMBELLISHED: Based on paper but exaggerated

## Checks (priority order)
[table of P0-P3 checks from §3.3]

## Rules
- P9 — No fabrication. If a claim isn't in the paper, mark it NOT FOUND.
- Never invent properties, concentrations, or resolution values.
- P6 — Append-only. Do NOT delete content. Flag issues for removal.
- Always quote numeric YAML values (resolution: "3.5" not 3.5).
- Set `verified: agent` only after ALL P0 and P1 checks pass for the file
  AND at least 80% of P2-P3 checks pass.

## Output Format — One JSON object per file
```json
{
  "file": "xray-mp-wiki/proteins_yaml/<name>.yaml",
  "sources_checked": ["doi/10.xxx"],
  "sources_missing": [],
  "claims": {"total": N, "correct": N, "wrong": N, "not_found": N, "partial": N, "embellished": N},
  "can_promote": true,
  "issues": [
    {"severity": "HIGH|MEDIUM|LOW", "field": "path.to.field", "claimed": "as-is",
     "actual": "what paper says", "fix": "correction or remove"}
  ],
  "changes_made": ["Set verified: agent", "Fixed resolution 2.8→2.81"],
  "yaml_modified": true
}
```

## Files to verify
[list of YAML paths and their source paper paths]
```

### 3.5 Post-Batch Validation

After each batch (~3 concurrent subagents finish):

```bash
# Validate all modified YAMLs
for yf in $(grep -l 'verified: agent' xray-mp-wiki/proteins_yaml/*.yaml); do
    python3 scripts/validate_yaml.py protein $(basename $yf .yaml) --strict
done
```

After all protein batches:

```bash
# Generate pages for all newly agent-verified proteins
ls xray-mp-wiki/proteins_yaml/*.yaml | sed 's|.*/||;s|\.yaml$||' | \
  xargs -P 4 -I{} python3 scripts/generate_page.py protein {} --yes --skip-catalog 2>&1

# Rebuild indexes once
python3 scripts/rebuild_indexes.py --force
python3 scripts/rebuild_entity_catalog.py
python3 scripts/wiki_manifest.py rebuild
```

---

## §4 — Phase 3: `verified: agent` for Reagents

### 4.1 Scale

803 reagent YAMLs. 18 already at `agent`. 785 to verify. Most are 1-2 papers each.
YAMLs are very lean (median 2.3KB). Paper sizes dominate the token budget.

**Batch strategy:** 20-25 files per subagent (reagent YAMLs are simpler than
proteins — fewer fields, no structures, no purification steps).

| Group | Papers | Files | Per batch | Batches |
|-------|--------|-------|-----------|---------|
| A | 1 paper | ~566 | 25 | ~23 |
| B | 2 papers | ~120 | 20 | ~6 |
| C | 3-5 papers | ~60 | 15 | ~4 |
| D | 6-29 papers | ~27 | 5 | ~6 |

**Total batches:** ~39

### 4.2 Verification Scope for Reagents

Reagent YAMLs have different claim types than proteins:

- **chemical_name / IUPAC name** — does it match the paper?
- **Physical properties** — CMC, MW, aggregation number, HLB (are these cited?)
- **Tags** — correct type (detergent-nonionic, buffer-tris, etc.)
- **Overview** — accurate description of what the reagent does
- **Uses / examples** — Do the cited papers actually use/describe this reagent this way?
- **Binding** — affinity values, targets (if a ligand) — match paper?
- **Cross-references** — are linked entities relevant?

### 4.3 Subagent Prompt Template (Reagents)

Same structure as protein template but with reagent-specific checks:

```
## Verification Scope for Reagents
- title/chemical_name — does name match the paper?
- physical properties (cmc, mw, transition_temp) — are these stated in the paper?
- tags — correct classification?
- overview — accurate, supported by paper?
- uses[] — each use cites a paper that actually mentions this use?
- examples[] — each example verified against its paper?
- binding — kd/ic50 values match paper? (for ligands only)
- cross_references — valid and relevant?

## Rules
- P9: If the paper doesn't state a CMC, mark NOT FOUND. Do NOT fabricate.
- P9: If a paper uses the reagent as a tool (e.g., SDS for SDS-PAGE), say so.
- property_field: values like CMC, MW must be traceable to a source paper.
```

### 4.4 Special Reagent Cases

- **Detergents:** Focus on CMC, MW, head_group, tail_length. Many of these come from
  Anatrace brochure, not a research paper. Flag `cmc_source` field as the source.
- **Ligands:** Focus on binding affinity (Ki, IC50), target protein, clinical status.
  These should be verifiable against the paper.
- **Buffers:** Physical properties (pKa, concentration range) are general knowledge —
  mark as CORRECT if broadly accurate even without paper citation.
- **Protein tags:** Tag size, fusion strategy, source organism should match the paper.

---

## §5 — Phase 4: `verified: agent` for Methods (70 files)

Smallest phase. 2 methods have 68 papers (likely catch-all review topics). Most
have 1-2 papers.

**Batch strategy:** 15-20 files per subagent. For the 3 methods with >20 papers,
use 1 file per batch.

### Verification Scope for Methods

- **principle / overview** — Does the method description match the paper?
- **protocol** — Steps, reagents, conditions match cited sources?
- **proteins_using[]** — Does each cited protein actually use this method?
- **tags** — Correct category (crystallization, purification, expression)?

---

## §6 — Phase 5: `verified: agent` for Concepts (455 files)

3 already at agent. 452 to verify. Most have 1-2 papers. Concept YAMLs are prose-
heavy: overview, mechanism, details, examples. The verification is mostly checking
that the prose isn't embellished.

**Batch strategy:** 20-25 files per subagent.

### Verification Scope for Concepts

- **overview / mechanism / details** — Are the scientific claims supported by the
  cited papers? No embellishment?
- **examples[]** — Each example ties back to a cited paper?
- **related_concepts[]** — Valid cross-references?
- **Tags** — Correct subcategory (transport-mechanism, protein-family, etc.)?

### Special: Concepts with No Papers

~8 concept files have 0 source papers. These are broad topics where the overview is
drawn from general knowledge (e.g., "SARS-CoV-2", "Mycobacterium tuberculosis").
For these, `verified: agent` is inappropriate by definition (no paper to check).
Leave at `regex` and mark `verified: knowledge-base` or skip.

---

## §7 — Subagent Infrastructure

### 7.1 The Three Scripts to Write

| Script | Phase | Purpose | Lines |
|--------|-------|---------|-------|
| `normalize_verified_field.py` | Phase 0 | Standardize `verified` → valid enum | ~60 |
| `promote_to_regex.py` | Phase 1 | Check source DOIs → promote to regex | ~50 |
| `prep_verification_batches.py` | All phases | Read YAMLs, count papers, compute tokens, group into batch JSON files | ~120 |

### 7.2 Batch Processing Pattern

```
for batch in protein_verify_batch_*.json; do
    # Read batch file
    files=$(python3 -c "import json; d=json.load(open('$batch')); [print(f['name']) for f in d['files']]")

    # Spawn 3 concurrent subagents, each with 10-12 files
    for i in 0 3 6; do
        batch_slice=$(python3 -c "import json; d=json.load(open('$batch')); print(json.dumps(d['files'][$i:$i+12]))")
        delegate_task goal="Verify protein YAMLs...", context="Batch $name slice $i"
    done

    # Wait for all 3 to complete
    # Validate all changed files
    # Generate pages
done
```

### 7.3 Time/Cost Estimate

| Phase | Entity Type | Files | Batches | Subagent rounds | Est. tokens out | Est. cost (at $1/M output) |
|-------|-------------|-------|---------|-----------------|-----------------|----------------------------|
| 0 | Standardize | 2,121 | 1 | 0 (script) | 0 | $0 |
| 1 | Promote to regex | 1,310 | 1 | 0 (script) | 0 | $0 |
| 2 | Proteins | 777 | ~70 | ~24 rounds × 3 | ~1M | ~$1 |
| 3 | Reagents | 785 | ~39 | ~13 rounds × 3 | ~0.6M | ~$0.60 |
| 4 | Methods | 70 | ~6 | ~2 rounds × 3 | ~0.1M | ~$0.10 |
| 5 | Concepts | 452 | ~20 | ~7 rounds × 3 | ~0.3M | ~$0.30 |

**Total agent rounds:** ~135 subagent calls across ~46 rounds. Estimated output
tokens: ~2M. Estimated cost: ~$2 total at DeepSeek V4 pricing.

### 7.4 Subagent Tool Restrictions

Per Manifest §4 Prohibitions and the subagent-verify-truth template:

**Allowed:** `read_file`, `write_file`, `patch`, `terminal`, `execute_code`
**BANNED:** `mcp_filesystem_*`, `browser`, `curl`, `web_search`, `delegate_task`,
`clarify`, `memory`, `session_search`

The subagent reads YAML files and papers from disk using `read_file`. It writes
changes using `patch` on the YAML. It does NOT call external APIs.

---

## §8 — Output Metrics to Track

After each phase, report:

```
=== Agent Verification — Phase N Complete ===
Before: X files at agent
After:  Y files at agent (+Δ)
Z files skipped (missing papers)
W issues found (H/M/L: reported)
Avg. issues per file: Q
Top issue categories: 1. PDB not in paper (24%), 2. Resolution mismatch (18%)...
```

This tells the user not just "we promoted N files" but what kinds of errors the
corpus actually has — which is the research-relevant finding.

---

## §9 — Risk Assessment

| Risk | Likelihood | Mitigation |
|------|-----------|------------|
| Subagent hallucinates verification (says PASS when wrong) | Medium | Two-tier: regex pre-screen first, then agent only confirms what regex can't. Also: post-batch spot-check 5% of promoted files. |
| Subagent exceeds context window | Medium | Batch sizing computed from YAML+paper byte sizes. Max batch: 200K tokens. If a batch overflows, the subagent can read files one at a time. |
| Subagent corrupts YAML structure | Low | Allow only `patch` tool for changes. Never `write_file` on YAML. |
| Paper not on disk (can't verify) | Medium (104 protein files) | Pre-skip in batch prep. Report as "needs paper acquisition". |
| Subagent misses embedded corruption (Pattern J) | Medium | Post-batch grep for sidebar garbage markers as a final check. |
| Subagent returns fabricated PDB/resolution values | Medium | Cross-check against known values in aggregate_stats.json. |
