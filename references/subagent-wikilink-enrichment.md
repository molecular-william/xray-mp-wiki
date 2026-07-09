# Wikilink Enrichment Subagent

**Load `references/AGENT-MANIFEST.md` first** — especially §3 (Conventions: link syntax, path awareness), §4 (Prohibitions: no regex on YAML, no `[[key|display]]`), §6 (Tool Reference).

---

## TASK: Add inline wikilinks and cross-references to existing YAML files

One subagent per batch of up to 10 YAML files.

### Steps (per file)

1. **Load entity catalog** — `references/entity_catalog.json`. Build alias map: `{lowercase_name: {path, title, type}}`. Sort by name length descending.

2. **Read YAML** — `yaml.safe_load()`. Identify type.

3. **Add inline wikilinks** in field VALUES:
   - Walk dict recursively.
   - For each string value, match against alias map using word-boundary regex (`(?<![a-zA-Z/])name(?![a-zA-Z/])`).
   - Replace with `[Display](/xray-mp-wiki/path/)`.
   - Match FULL hyphenated catalog keys (Manifest P10), not individual words.
   - Skip self-references. Skip fields: `title`, `created`, `type`, `layout`, `category`.

4. **Add cross_references** — append to existing list. Max 10 total. Dedup by path. Each: `{path, title, reason}`.

5. **Validate** — `python3 scripts/validate_yaml.py <type> <name> --strict`.

6. **Return JSON**:

```json
{
  "files_enriched": ["xray-mp-wiki/proteins_yaml/name.yaml"],
  "files_valid": true,
  "wikilinks_added": 12,
  "cross_refs_added": 5,
  "errors": []
}
```

### Critical
- YAML edits ONLY via `yaml.safe_load()` → modify dict → `yaml.dump()` → `write_file`. No regex/string.replace on YAML text (Manifest §3).
- **NO `[[key|display]]`** — use `[Display](/path/)`.
- No temp scripts. No result files on disk (Manifest P4).
- Do NOT modify existing cross_references — only APPEND.

### Allowed tools
`read_file`, `write_file`, `terminal`, `execute_code`. **BANNED:** `mcp_filesystem_*`, `patch` (on YAML), `browser`, `delegate_task`, `clarify`.

---

## START

YAML FILES:
{{YAML_FILES_LIST}}
