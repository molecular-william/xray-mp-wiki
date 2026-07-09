# Reagent Content Enrichment Subagent

**Load `references/AGENT-MANIFEST.md` first** — especially §1 (Reagent schema, property fields), §2 (Reagent tag taxonomy), §3 (Conventions), §4 (Prohibitions), §7 (Verification Standards).

---

## TASK: Enrich a reagent YAML with properties, uses, examples, advantages, disadvantages

One subagent per YAML file.

### Steps

1. **Read YAML** — `read_file('{YAML_FILE}')`. Note existing fields, especially `sources[]`.

2. **Read source papers** — For each DOI in `sources:`, look up `raw/papers/<doi>.md`.

3. **Extract properties** — Populate these if evidence found in papers:

| Field | Examples |
|-------|----------|
| `chemical_name` | "n-Dodecyl-beta-D-maltopyranoside" |
| `molecular_weight` | "510.6 g/mol" |
| `cmc` | "0.17 mM" |
| `hlb` | "~13" |
| `head_group` | "maltoside" |
| `tail_length` | "C12" |
| `pka` | "7.5" (buffer) |
| `kd_ki` | "0.5 nM" (ligand) |
| Plus all others defined in Manifest §1. |

4. **Extract uses[]** — {title, content} per application. Dedup by title. Use `>` folded block scalar for content.

5. **Extract examples[]** — {protein, concentration, context, result}. `protein` must be wikilink `[Name](/xray-mp-wiki/path/)`. Look up entity catalog for correct path. Dedup by protein.

6. **Extract advantages[]/disadvantages[]** — Each string must be supported by ≥1 source. Dedup by content.

7. **Update YAML** — `yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)`. Bump `updated:`. Self-verify: read back.

8. **Validate & Generate** — `validate_yaml.py reagent {NAME} --strict` → `generate_page.py reagent {NAME} --yes --skip-catalog`.

9. **Return JSON**:

```json
{
  "yaml": "xray-mp-wiki/reagents_yaml/<name>.yaml",
  "sources_read": ["doi1", "doi2"],
  "fields_added": {"properties": ["cmc", "mw"], "uses": 2, "examples": 3, "advantages": 2, "disadvantages": 1},
  "validation_passed": true,
  "errors": []
}
```

### Allowed tools
`read_file`, `write_file`, `terminal`, `execute_code`. **BANNED:** `mcp_filesystem_*`, `browser`, `curl`, `web_search`, `delegate_task`, `clarify`.

---

## START

YAML: {YAML_FILE}
