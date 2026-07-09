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
| PDB IDs | Every PDB appears in paper. No hallucinated codes. |
| Resolution | Matches paper's stated value |
| Space group | Matches paper |
| Construct | Residues, mutations, tags match |
| Expression | Host organism correct |
| Purification | Detergents, buffers, columns mentioned |
| Crystallization | Method, precipitant, pH accurate |
| Insights | Supported? Not embellished? |
| Overview | Accurate? No fabricated filler? |

4. **Classify each claim** per Manifest §7 (CORRECT/WRONG/NOT FOUND/PARTIAL/EMBELLISHED).

5. **Fix issues:** Remove unsupported claims. Correct wrong values. Set `verified: true`. Validate --strict → regenerate.

6. **Return JSON** in response text:

```json
{
  "file": "xray-mp-wiki/proteins_yaml/<name>.yaml",
  "sources_checked": ["doi/..."],
  "sources_missing": [],
  "claims": {"total": 25, "correct": 20, "wrong": 1, "not_found": 2, "partial": 1, "embellished": 1},
  "issues": [
    {"severity": "HIGH", "field": "structures[0].pdb_id", "claimed": "7ABC", "actual": "not in paper", "fix": "removed"}
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
