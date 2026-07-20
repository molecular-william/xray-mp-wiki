# Bulk Verification — Post-Mortem

**Session:** 2026-07-09, ~3h, ~$2 total in subagent tokens

## Results

| Type | Total | Agent | Regex (broken) | % |
|------|-------|-------|----------------|---|
| Proteins | 790 | 685 | 105 | 87% |
| Reagents | 808 | 434 | 374 | 54% |
| Methods | 70 | 0 | 70 | 0% |
| Concepts | 458 | 3 | 455 | 0% |

## What worked

**Two-pass (deterministic → LLM) is the correct order.** Every time we started with a
deterministic script, it handled 80-90% at 0 tokens and the LLM cleaned the tail.
Every time we started with LLM (batches 001-003), we wasted tokens on easy cases.

| Pass | Cost | Coverage |
|------|------|----------|
| 1. Standardize `verified` field | 0 tokens | 2,126 YAMLs |
| 2. Check DOI files exist → `regex` | 0 tokens | 1,081 promoted |
| 3. Check PDB via `check_pdb.py` (MPSTRUC fallback) | 0 tokens | 291 proteins promoted |
| 4. Fix `structures[]` from `pdb_dois` | 0 tokens | 117 files repaired |
| 5. Check reagent name in paper text | 0 tokens | 366 reagents promoted |
| 6. Subagent deep-verify edge cases | ~$2/tokens | ~100 proteins, ~68 reagents |

**Key discovery:** `mpstruc_classification.pdb_dois` is the ground truth for PDB→DOI
mapping. `structures[]` is often wrong. `check_pdb.py` checks paper text then falls
back to MPSTRUC CSV. `fix_pdb_from_pdbdois.py` copies correct PDBs from pdb_dois
into structures[].

## Files needed next time

### Core scripts (5)

| File | What | Why |
|------|------|-----|
| `scripts/normalize_verified_field.py` | Standardize `verified` → valid enum | Run before any verification |
| `scripts/promote_to_regex.py` | Check DOIs exist on disk → promote | Baseline check before deeper work |
| `scripts/check_pdb.py` | PDB in paper? Fallback to MPSTRUC CSV | Avoids false-negatives for PDBs in supp info |
| `scripts/fix_pdb_from_pdbdois.py` | Copy correct PDBs from pdb_dois → structures[] | Fixes Pattern U (most common bug) |
| `scripts/verify_reagents.py` | Deterministic name-in-paper check | 80% of reagent verification in 30s |

### Workflow

```
1. normalize_verified_field.py     # 0 tok, 2 min
2. promote_to_regex.py              # 0 tok, 30s
3. Proteins:
   a. check_pdb.py                   # 0 tok, identify candidates
   b. fix_pdb_from_pdbdois.py        # 0 tok, auto-repair
   c. check_pdb.py again              # remaining at regex get subagent
   d. Subagent on tail (~105 files)   # ~$0.50
4. Reagents:
   a. verify_reagents.py              # 0 tok, 366 promoted
   b. Subagent on tail (~374 files)   # ~$1 — most have broken DOIs
5. Methods: (70 files, all deterministic-eligible)
   a. name-in-paper check (reuse verify_reagents pattern)
   b. Subagent on tail
6. Concepts: (458 files, hardest — prose-heavy)
   a. Subagent only (no PDBs, no chemical names to grep)
```

### Prompt improvements

**`references/subagent-verify-truth.md` must include:**
- Per-file gates (never batch gate)
- `python3 scripts/check_pdb.py <PDB> <DOI>` for PDB verification
- Search tool for subdirectories (reagent files live in `reagents_yaml/*/`)
- Ignore DOI mismatches between batch listing and YAML sources — trust the YAML

### Pitfalls encoded
- Batch-level gate (subagent blocks all files because 1 fails) — fixed with per-file prompt
- Subdirectory YAMLs (reagent files in `detergents/`, `buffers/`, etc.) — subagent needs `rglob`
- Paper DOI != batch-listed DOI (happens often) — subagent must read YAML sources directly
- MPSTRUC CSV doesn't cover cryo-EM structures (only X-ray) — 7F3X/7F40 type failures expected
- `verified: pdb` vs `verified: agent` — subagent wrote "pdb" instead of "agent" on some patches
