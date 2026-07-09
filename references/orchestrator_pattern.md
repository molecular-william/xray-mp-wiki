# Orchestrator Pattern — Wiki Maintenance & DOI Processing

**Load `references/AGENT-MANIFEST.md` first** for all rules, schema, taxonomy, prohibitions, and tool reference. This file covers only orchestration logistics.

---

## Overview

The orchestrator (main session) splits work into non-overlapping batches, spawns leaf subagents, collects results, and merges state atomically.

Three subagent roles (each loads AGENT-MANIFEST.md + its own task briefing):

| Role | Files | Toolsets | Batch Size |
|------|-------|----------|------------|
| DOI Processor | `references/subagent-pass1-prompt.md` | `["file","terminal"]` | 2 DOIs |
| Verification | `references/subagent-verify-truth.md` | `["file","terminal"]` | 3-5 YAMLs |
| Enrichment | `references/subagent-wikilink-enrichment.md` or `subagent-enrich-reagent-content.md` | `["file","terminal"]` | 10 YAMLs |

---

## Mode 1: DOI Ingestion

### Main Session
1. Pick 6 pending DOIs from manifest (or fewer if remaining < 6)
2. Spawn 3 subagents (2 DOIs each):
   ```python
   delegate_task with tasks=[{"goal": "...", "context": "Full prompt in subagent-pass1-prompt.md",
       "toolsets": ["file", "terminal"]}, ...]
   ```
3. Collect JSON results → rebuild indexes:
   ```bash
   python3 scripts/rebuild_indexes.py --force
   python3 scripts/rebuild_entity_catalog.py
   ```
4. Verify: `find xray-mp-wiki/proteins -name "*.md" | wc -l`

---

## Mode 2: Source-Truth Verification

1. Select pages with `verified: false` or user-specified
2. Spawn verification subagent per batch of 3-5 pages
3. Collect results → report corrections → rebuild indexes

---

## Mode 3: Lint Fixing

1. Run `python3 scripts/lint.py` → capture categories
2. User picks category → spawn lint-fix subagent
3. Re-lint → report decrease

---

## Mode 4: Entity Discovery

1. Scan raw papers for entities without wiki pages
2. Check page threshold (central to paper OR 2+ sources)
3. Create if threshold met → update indexes

---

## Post-Batch Merge (all modes)

```bash
python3 scripts/rebuild_indexes.py --force
python3 scripts/rebuild_entity_catalog.py
python3 scripts/rebuild_graph.py [--image-only]
```

### Key logistics
- Non-overlapping DOI ranges per subagent
- Subagents have zero chat context — everything in the prompt + AGENT-MANIFEST.md
- Subagents cannot use `clarify`, `memory`, `session_search`
- Subagent summaries are self-reported — verify file counts after merge
- One fix category at a time — present to user, wait for approval
- Never push to git — user handles deployment
- Always run `rebuild_indexes.py` after subagent batch
- Batch size 2 DOIs per subagent is optimal for token limits
- **Graph suggestions are DEFAULT** — after creating/updating entities, run `wiki_query.py suggest <entity-name> --limit 10` and add relevant cross-refs. Set `SKIP_GRAPH=1` to skip.

### Manifest management
```bash
python3 scripts/wiki_manifest.py status       # Show state
python3 scripts/wiki_manifest.py update-csv   # Sync manifest → CSV after batch
```

### File reference map
| File | Purpose |
|------|---------|
| `xray-mp-wiki/index.md` | Wiki catalog (entity paths + titles) |
| `xray-mp-wiki/log.md` | Change log |
| `references/AGENT-MANIFEST.md` | **Constitution** — rules, schema, taxonomy, conventions, prohibitions |
| `references/entity_schema.json` | Formal JSON Schema |
| `references/entity_catalog.json` | Entity index (2,050+ entries with paths and types) |
| `references/subagent-*.md` | Task-specific briefings (lean, 20-30 lines) |
| `wiki_manifest.json` | Batch progress state |
| `protein_doi_checklist.csv` | DOI processing status |
