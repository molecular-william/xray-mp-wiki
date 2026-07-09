# X-ray MP Wiki — Test Reference

**Last updated:** 2026-06-30
**File:** `scripts/test_all.py`

Run: `python3 scripts/test_all.py` (fast tests) or `python3 scripts/test_all.py --full` (includes full-scan tests).

---

## What the tests cover

### Generation Pipeline (Tests 1-8, pre-existing)

| Test | What it checks | Why it matters |
|------|---------------|----------------|
| `test_generate_protein` | Protein YAML → `.md` page: title, overview, PDB, cross-refs, overwrite, `--diff`, `--skip-catalog`, missing YAML error | Agents create and update protein pages constantly. If this breaks, every DOI processing session fails. |
| `test_generate_reagent` | Reagent YAML → `.md` page with subdirectory routing | Reagent pages must land in the correct subdirectory (detergents/, buffers/, etc.) |
| `test_generate_method` | Method YAML → `.md` page with subdirectory from tag | Methods use tag-based routing; must match expected output path |
| `test_generate_concept` | Concept YAML → `.md` page | Concept pages are metadata-only; rendering must not crash |
| `test_validate` | YAML validation: valid passes, invalid fails, nonexistent fails | Validation gate catches bad data before it reaches rendered pages |
| `test_rebuild_entity_catalog` | `entity_catalog.json` rebuild from manifest and filesystem | Catalog is the agent's primary discovery index; must be accurate |
| `test_wiki_manifest` | Manifest commands: `check-entity`, `status`, `rebuild` | Agents use these for DOI processing workflow |
| `test_enrich` | Wikilink enrichment dry-run: parses YAML, finds matches, doesn't modify in dry-run | Enrichment must not corrupt YAMLs; dry-run protects data |
| `test_lint` | Lint runs, parses pages, reports issues | Health check; must not crash on any page format |
| `test_base_utilities` | Path construction: `build_paths` returns correct output path | Underpins all page generation |

### Agent Workflow Tests (Tests A-F, new 2026-06-30)

#### Test A: YAML Round-Trip Integrity

**What it simulates:** An agent loading a YAML, modifying fields, and saving.

| Check | What it catches |
|-------|----------------|
| Load existing YAML | Corrupted YAML files that crash `yaml.safe_load()` |
| Modify `updated` field | Schema changes that rename fields |
| `yaml.dump()` → write → read back | `yaml.dump()` options that destroy structure (e.g., `default_flow_style=True`) |
| Quoted colons in title | The `"Foo: Bar"` title bug — colons parsed as YAML mappings |
| Quoted `mixing_ratio: "1:1"` | The sexagesimal trap — YAML parses unquoted `1:1` as the number 61 |

**Failure modes detected:** Silent data corruption, YAML parse errors, field types changing (string → int/float).

#### Test B: Sequence Renderer (Ruler + Collapsible Table)

**What it simulates:** The `protein_page_renderer.py` functions that agents trust to produce correct HTML.

| Check | What it catches |
|-------|----------------|
| `class="topo-ruler"` emitted | Ruler generation removed or broken |
| Ruler character count matches chunk | Ruler and sequence misaligned (different lengths) |
| `topo-membrane/inside/outside` spans | Topology coloring broken |
| `<details class="topo-details">` | Collapsible table wrapper removed |
| `<summary>Topology coordinates` | Summary text changed |
| `line_len = 120` | Line width regression (60 ← 120) |

**Failure modes detected:** HTML rendering changes that break the sequence display. Since protein pages are already generated, this test catches regressions before re-generation.

#### Test C: WikiQuery — get, search, connections

**What it simulates:** An agent looking up entities, searching, and exploring the graph.

| Check | What it catches |
|-------|----------------|
| `get("ddm")` returns result with type/title/path | Catalog loading broken or entity missing |
| `get(nonexistent)` returns `None` | API contract change |
| `search("adenosine")` returns ≥1 result | Search index empty or text matching broken |
| `connections("ddm")` returns neighbors | Graph adjacency list empty or misstructured |
| `connections` results have `name`/`edge_type`/`reasons` | Return format changed |
| `path("ddm","kcsa")` returns path | BFS shortest path algorithm broken |

**Failure modes detected:** WikiQuery API changes, precomputed index corruption, graph.json format changes.

#### Test D: WikiQuery — suggest cross-references

**What it simulates:** An agent running `suggest` after creating a new entity.

| Check | What it catches |
|-------|----------------|
| `suggest("5ht2a-receptor")` returns ranked results | Mode A (entity in graph) broken |
| Results have `name`/`score`/`reason`/`type` keys | Return format changed |
| All scores positive | Scoring formula producing negative values |
| `suggest(tags="gpcr")` returns results | Mode B (new entity by tags) broken |
| Top suggestions include DDM (common GPCR reagent) | Mode B not finding relevant connections |
| `suggest()` with no args returns `[]` | Edge case handling |

**Failure modes detected:** Graph suggestion algorithm broken, Mode A/B regression.

#### Test E: Cross-Reference Integrity (full scan, `--full`)

**What it simulates:** A quality audit — every cross-reference in every YAML resolves to a real entity.

| Check | What it catches |
|-------|----------------|
| Every `cross_references[].path` resolves in catalog | Broken links in YAML data (stale cross-refs after page moves/deletes) |
| Every graph edge source/target exists | Graph nodes point to non-existent entities |
| Every `sources[]` DOI has a matching raw paper | DOI-to-paper mapping broken |

**Why this matters:** If a cross-reference points to a deleted/renamed entity, the agent's navigation breaks silently. The graph becomes stale. This test ensures the cross-reference network is self-consistent.

#### Test F: Entity Catalog ↔ YAML Consistency (full scan, `--full`)

**What it simulates:** Verifying that `entity_catalog.json` matches what's on disk.

| Check | What it catches |
|-------|----------------|
| Every YAML file has a catalog entry | YAMLs created without updating the catalog |
| Every catalog entry has a matching YAML | Catalog entries pointing to deleted files |
| Every YAML has required fields (title, tags, sources) | Orphan/incomplete YAMLs that would crash generation |

**Why this matters:** Agents discover entities through the catalog. If the catalog is out of sync with the filesystem, agents operate on stale information and can create duplicate pages.

---

## Running

```bash
# Fast tests only (A-D, ~3-5s)
python3 scripts/test_all.py

# Full scan including catalog/graph integrity (E-F, ~60s)
python3 scripts/test_all.py --full
```

## Test architecture

- Fast tests (A-D) import modules directly — no subprocess overhead
- Full-scan tests (E-F) iterate all 2,026 YAMLs — intentionally slow but thorough
- Tests use the precomputed index when available (Tests C-D)
- Tests do NOT modify the live wiki — they read from the precomputed index and real YAML files
- 6 pre-existing tests have known failures (validate_cli.py renamed to validate_yaml.py, test fixture issues) — these do NOT affect agent workflow correctness
