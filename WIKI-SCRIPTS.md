# X-ray MP Wiki — Scripts Reference (Cave)

## Script Inventory

All scripts in `scripts/` at project root. Import via `sys.path` in each script.

### Shared Utilities

| Script | Size | Purpose |
|--------|------|---------|
| `_base.py` | 481 lines | Shared utilities: path building, arg parsing, YAML loading, diff display, confirmation, page writing, catalog update, generate orchestration, method/reagent subdirectory detection |

**Key functions in `_base.py`:**
- `build_paths(entity_type, name)` → `(yaml_path, output_path)`
- `parse_args(argv, entity_type, extra_flags)` → parsed args dict
- `load_yaml(yaml_path)` → dict from YAML
- `show_diff(existing, new)` → prints unified diff
- `confirm_overwrite()` → yes/no prompt
- `write_page(path, content)` → writes file
- `maintain_catalog(type_name, name, title, summary, output_path)` → updates wiki catalog in index.md
- `generate_main(renderer, name, yaml_path, output_path)` → orchestrate generation
- `find_method_subdir(name, tags)` → auto-detect method subdirectory
- `find_existing_page(entity_type, name)` → find existing wiki page

### Rendering Scripts (Shared Logic)

| Script | Purpose |
|--------|---------|
| `protein_page_renderer.py` | Rendering + merge logic for protein pages |
| `reagent_page_renderer.py` | Rendering + merge logic for reagent pages |
| `method_page_renderer.py` | Rendering + merge logic for method pages |
| `concept_page_renderer.py` | Rendering + merge logic for concept pages (hybrid: YAML metadata + LLM prose) |

Each exports: `render_link(path, title)`, `render_frontmatter(data)`, type-specific render functions, `generate_page(yaml_data)`.

### Generate Scripts (Entry Points)

| Script | Purpose |
|--------|---------|
| `generate_protein_page.py` | Generate new protein page from YAML |
| `generate_reagent_page.py` | Generate new reagent page from YAML |
| `generate_method_page.py` | Generate new method page from YAML |
| `generate_concept_page.py` | Generate new concept page from YAML |

Each = thin wrapper: parses args, builds paths, calls `generate_main()` with renderer.

### Lint Script

| Script | Size | Purpose |
|--------|------|---------|
| `lint.py` | 458 lines | Wiki health audit (7 checks) |

**Checks:**
1. Broken links — internal links to non-existent pages
2. Orphan pages — zero inbound links
3. Duplicate sections — same heading twice in one page
4. Frontmatter consistency — category matches directory, type matches category, `layout: default` present, required fields exist
5. Minimum outbound links — every page ≥2 outbound links
6. DOI format — all DOIs use `doi/10.xxxx##yyyy` format
7. Stale pages — not updated >30 days

**Run:** `python3 scripts/lint.py` (from project root)

### Test Suite

| Script | Size | Purpose |
|--------|------|---------|
| `test_all.py` | 733 lines | Test suite for generate scripts (update scripts intentionally not implemented) |

**Tests:**
- Protein generation: new page, dry-run, diff, overwrite
- Reagent generation: new page, dry-run, diff
- Method generation: new page, dry-run, diff
- Error handling: nonexistent YAML, missing pages

**Note:** Update script tests (`update_protein_page.py`, `update_reagent_page.py`, `update_method_page.py`) are present in test_all.py but will fail — update scripts are intentionally not implemented. YAML is edited directly, then `generate_<type>_page.py` is run.

**Run:** `python3 scripts/test_all.py` (from project root)

## Script Execution Flow

**Generate (new or update):** Entry script → `parse_args()` → `build_paths()` → `_base.generate_main(renderer, name, yaml_path, output_path)` → load YAML → renderer generates page → show diff (if --diff) → confirm → write → `maintain_catalog()`.

**Update workflow:** Agent edits YAML file directly → runs `generate_<type>_page.py <name> --yes` → reads YAML → overwrites page.

Concept hybrid: concept renderers return skeleton (frontmatter + section headers). LLM fills prose (Overview, Mechanism/Details) from raw paper.

## Architecture

```
scripts/
├── _base.py              ← Shared utilities (imported by all)
├── *_page_renderer.py    ← Rendering logic (one per type)
├── generate_*_page.py    ← Entry: generate page from YAML
├── lint.py               ← Health audit
├── test_all.py           ← Test suite (generate scripts only)
└── wiki_manifest.py      ← DOI batch manifest
```

**Pattern:** Each type = renderer (shared logic) + generate script (entry). YAML is the single source of truth — edit YAML directly, then run generate script. No update scripts exist.

**Concept hybrid:** Concept YAML = metadata only (title, tags, sources, examples, cross-refs). LLM writes prose (Overview, Mechanism/Details) from raw paper. Don't put prose in YAML.

## Common Pitfalls

1. **Script import path:** Scripts use `sys.path.insert(0, str(Path(__file__).parent))`. Run from project root, NOT from within `scripts/`.
2. **YAML location:** YAML files in `xray-mp-wiki/<type>_yaml/`, NOT in `scripts/`.
3. **Output location:** Generated pages go to `xray-mp-wiki/<type>/`, NOT in `scripts/`.
4. **Method subdirectories:** Method pages go into subdirectories. Script auto-detects from tags, override with `subdirectory` field in YAML.
5. **YAML-first update workflow:** No update scripts exist. Edit YAML directly (append sources, deduplicate cross-refs), then run `generate_<type>_page.py <name> --yes`. The generate script overwrites the page from YAML.
6. **Concept hybrid workflow:** Concept YAML = metadata only (title, tags, sources, examples, cross-refs). LLM writes prose (Overview, Mechanism/Details) from raw paper. Don't put prose in YAML.
7. **Concept thinness:** Concept pages ~50-100 lines. Split if >150.
8. **No bulk writes:** Never use `echo`/`cat`/Python scripts to write multiple files. Use `write_file` tool (one page per call). Python scripts silently fail for bulk writes.
9. **Catalog auto-maintenance:** Wiki catalog in `index.md` auto-updated after every page generation. **DO NOT manually edit** catalog section (between `<!-- WIKI CATALOG -->` markers) — will be overwritten.
10. **No entity discovery script exists (by design).** Entity discovery is done by the agent reading raw papers and using judgment, not by automated pattern matching. Many compounds have ambiguous abbreviations (DM, NG, DM) that an automated script would misclassify. The agent reads context and makes judgment calls.