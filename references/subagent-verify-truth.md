# Source-Truth Verification Subagent

**Load `references/AGENT-MANIFEST.md` first** — especially §1 (Schema), §4 (Prohibitions), §7 (Verification Standards), §10 (Project Paths).

---

## TASK: Verify YAML claims against raw papers

One subagent per batch of 3-5 YAML files.

### Steps

1. **Read YAML file.** Identify all DOIs in `sources`.

2. **For each DOI:** find `raw/papers/<doi>.md`. Case-insensitive matching (Manifest §3).

3. **Verify every claim** against paper text:

| Category | Check |
|----------|-------|
| PDB IDs | `python3 scripts/check_pdb.py <PDB> <DOI>` — checks paper + MPSTRUC CSV fallback |
| DOIs | Must use `doi/10.XXXX##journal-abbrev.YYYY` format (## separator, lowercase journal). Never bare DOIs like `10.1038/nature10191`. |
| Resolution | Matches paper's stated value |
| Space group | Matches paper |
| Construct | Residues, mutations, tags match |
| Expression | Host organism correct |
| Purification | Detergents, buffers, columns mentioned |
| Crystallization | Method, precipitant, pH accurate |
| Insights | Supported? Not embellished? |
| Overview | Accurate? No fabricated filler? |

4. **Classify each claim** per Manifest §7 (CORRECT/WRONG/NOT FOUND/PARTIAL/EMBELLISHED).

5. **Fix & enrich:** Remove unsupported claims. Correct wrong values. **Add missing information found in the paper** (detergents, buffers, pH, concentrations, crystallization conditions, expression details). Set `verified: true`. Validate --strict → regenerate.

6. **Return JSON** in response text, including `edit_suggestions` for any changes too risky to write directly:

```json
{
  "file": "xray-mp-wiki/proteins_yaml/<name>.yaml",
  "sources_checked": ["doi/..."],
  "sources_missing": [],
  "claims": {"total": 25, "correct": 20, "wrong": 1, "not_found": 2, "partial": 1, "embellished": 1},
  "issues": [
    {"severity": "HIGH", "field": "structures[0].pdb_id", "claimed": "7ABC", "actual": "not in paper", "fix": "removed"}
  ],
  "enrichments": [
    {"field": "steps[0].buffer_details[1].ph", "paper_source": "Methods, pH 8.0", "proposed": 8.0},
    {"field": "purifications[0].steps.add", "paper_source": "SEC in 25 mM HEPES pH 7.5", "proposed": "see suggested step"}
  ],
  "verdict": "PASS"
}
```

### Allowed tools
`read_file`, `write_file`, `patch`, `terminal`, `execute_code`. **BANNED:** `mcp_filesystem_*`, `browser`, `curl`, `web_search`, `delegate_task`, `clarify`.

---

## START

YAML FILES:
{{YAML_FILES_LIST}}
