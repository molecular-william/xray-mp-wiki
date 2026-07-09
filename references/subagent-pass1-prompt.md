# Pass 1 Subagent Prompt (DOI Processing)

**Load `references/AGENT-MANIFEST.md` first** for full rules (§1–10), schema, tag taxonomy, prohibitions, and tool reference.

**Parent fills `{RAW_PAPER_PLACEHOLDER}`** with `raw/papers/<doi>.md`.

---

## TASK: Process one raw paper

### Steps (in order)

1. **Load entity catalog** — `references/entity_catalog.json`. Check existence before creating.

2. **Assess quality** — comment per Manifest §8.

3. **Extract ALL entities** — proteins (PDBs, construct, purification, crystallization, insights), reagents (detergents/buffers/lipids/ligands/tags/antibodies), methods (all techniques), concepts (families/mechanisms/strategies). Per Manifest P5 (maximum extraction).

4. **Write YAML** — `write_file` to `xray-mp-wiki/<type>_yaml/<name>.yaml`. Self-verify: read back.

5. **Validate** — `python3 scripts/validate_yaml.py <type> <name> --strict`. Fix errors.

6. **Generate** — `python3 scripts/generate_page.py <type> <name> --yes --skip-catalog` for new AND updated entities.

7. **Suggest cross-references from knowledge graph (DEFAULT):**
   ```bash
   python3 scripts/wiki_query.py suggest <entity-name> --limit 10
   ```
   Review the ranked suggestions and add relevant ones to `cross_references[]`. Each entry: `{path, title, reason, type}` — use the controlled type taxonomy from AGENT-MANIFEST.md §9 (detergent_used, ligand_bound, method_used, related_protein, related_concept, etc.). The `reason` is free-text for humans; `type` is the controlled vocabulary for graph queries.
   **To skip graph suggestions**, set `SKIP_GRAPH=1` or pass `--no-graph` to the orchestrator.

8. **Return JSON** in response text (do NOT write to disk):

```json
{
  "doi": "doi/10.xxxx##yyyy",
  "comment": "ok",
  "entities_created": ["type/name"],
  "yaml_files_written": ["xray-mp-wiki/proteins_yaml/name.yaml"],
  "pages_generated": ["xray-mp-wiki/proteins/subdir/name.md"],
  "entities_updated": [],
  "cross_refs_from_graph": ["ddm", "lmng", "lipidic-cubic-phase"],
  "cross_refs_added_with_types": true,
  "cross_refs_skipped_graph": false,
  "errors": []
}
```

### Allowed tools
`read_file`, `write_file` (to `xray-mp-wiki/*_yaml/` ONLY), `patch`, `terminal`, `execute_code`.
**BANNED:** `mcp_filesystem_*`, `browser`, `curl`, `web_search`, `delegate_task`, `clarify`, `memory`.

---

## START

Raw paper:
{RAW_PAPER_PLACEHOLDER}
