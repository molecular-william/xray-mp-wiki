# YAML Repair Patterns Reference

**Purpose:** Quick-reference for fixing broken YAML files in the xray-mp-wiki.
**First:** Always load `references/AGENT-MANIFEST.md` — P1 (no regex on YAML), P6 (append-only), P9 (no fabrication) govern all repairs.
**Validate:** `python3 scripts/validate_yaml.py <type> <name> --strict`
**Regenerate:** `python3 scripts/generate_page.py <type> <name> --yes [--skip-catalog]`

---

## Validation System

| Check | Error example |
|-------|--------------|
| Empty tags | `tags: must have ≥1 tag from taxonomy` |
| Missing required fields | Missing `title`, `sources`, `overview` |
| Invalid DOI format | Must be `doi/10.xxxx##yyyy` |
| Non-Jekyll wikilinks | `[[key]]` → use `[Key](/path/)` |
| Missing protein class tag | Must be one of: gpcr, ion-channel, transporter, enzyme, receptor, channel, pump, porin |
| Empty overview | `overview:` with blank content |
| Unquoted numerics | `resolution: 3.5` → `resolution: "3.5"` |
| Invalid step_type | Must be one of 21 controlled values in `STEP_TYPES` set |
| Non-canonical detergent unit | `unit` must be `"%"` or `"mM"` |
| Tilde-prefixed resolution | `resolution: ~3.5` — replace with actual RCSB value |
| Missing created/updated | Recommended — renderer defaults to today |


## Valid Formats (Do Not Touch)

```yaml
# uniprot_id: string OR array (multi-subunit complexes)
uniprot_id: "P0A334"
uniprot_id: ["Q9H221", "Q9H222"]

# detergent_details / buffer_details arrays (normalization fields)
buffer_details:
  - reagent: /xray-mp-wiki/reagents/buffers/hepes/
    concentration: "20"
    unit: "mM"
    ph: "7.5"                    # MUST be quoted string
  - reagent: /xray-mp-wiki/reagents/additives/sodium-chloride/
    concentration: "150"
    unit: "mM"
```

**CRITICAL — pH must be quoted:** `ph: 7.5` fails — always `ph: "7.5"`. Null values (`ph:` with empty) are valid.

After buffer normalization, run: `python3 scripts/fix_yaml_quoting.py`


## Common Fix Patterns (Quick Table)

| Symptom | Cause | Fix |
|---------|-------|-----|
| YAML parse error on `:` in value | Colon+space in unquoted string | Quote the value: `"PDB: 1UAZ"` |
| `ComposerError: expected a single document` | Duplicate frontmatter (`---` twice) | Remove duplicate `---title:` block |
| `'str' object has no attribute 'get'` | List where dict expected | Wrap in list or add structure |
| `source entry: must be string, got dict` | `sources:` mixed with `structures[].source` | Run `scripts/consolidate/repair.py --clean-sources` |
| Unquoted numeric value | Resolution, pH, temperature as raw numbers | Quote all: `"3.5"`, `"7.5"`, `"298"` |
| Broken wikilinks with `/x/` prefix | Subagent regex truncated `/xray-mp-wiki/` | Replace: `s|/x/|/xray-mp-wiki/|` |
| Concatenated DOI strings | Multiple DOIs in one `sources:` entry | Split on ` - ` into separate list items |
| Family from `tags` instead of mpstruc | Agent reads `tags` array for family | Read `mpstruc_classification.subgroup` instead |


## Subagent Corruption Patterns

### Pattern A: `[[key|display]]` Syntax

Violates P1 (validator rejects non-Jekyll wikilinks). Strip from yaml-loaded dict:

```python
def walk_strip(obj):
    if isinstance(obj, dict): return {k: walk_strip(v) for k, v in obj.items()}
    elif isinstance(obj, list): return [walk_strip(i) for i in obj]
    elif isinstance(obj, str): return re.sub(r'\[\[.*?\]\]', '', obj)
    return obj
```

Re-enrich with `enrich_wikilinks.py` after. Scope: 10 protein YAMLs, 71 occurrences (2026-06-26).

### Pattern B: Doubled Paths

Page name matches subdirectory name → mass wikilink rewrite doubles path.
**Fix:** Text-level replace: `/(membrane-mimetics/){2,}/` → `/membrane-mimetics/`.
**Scope:** 6 files.

### Pattern C: Individual Word Over-Matching

Violates P10 (match full keys, not words). Restore overview from `.md` page, rebuild YAML.

### Pattern D: Resolution/Space-Group Values with `A` Suffix

`resolution: 2.5 A` — YAML treats as string (not flagged by unquoted-numeric check). Grep for `resolution: \d+\.?\d*\s*[AÅ]` in YAMLs.

**Fix:** `resolution: 2.5 A` → `resolution: '2.5'`. Drop angstrom suffix.

**Regex trap — `\s` consumes newlines:** Use lookahead that excludes `\n`:
```python
# BAD: \s eats newline, corrupts YAML:
re.sub(r'(resolution): (\d+\.?\d*)\s*A(?:\s|$)', r"\1: '\2'", raw)
# GOOD: lookahead preserves line breaks:
re.sub(r'(resolution): (\d+\.?\d*)\s*A(?:(?=[ \t])|$)', r"\1: '\2'", raw)
```

### Pattern E: yaml.dump() Unquoted Bracket Values

`yaml.dump()` outputs `[DDM](/path/)` without quotes. Run `scripts/fix_yaml_quoting.py` after bulk yaml.dump()-based enrichment.

### Pattern E2: ruamel.yaml `!!omap` Tag

Using `collections.OrderedDict` + ruamel.yaml emits `!!omap` tag. `yaml.safe_load()` returns list instead of dict.

**Fix:** Use `CommentedMap` everywhere:
```python
from ruamel.yaml.comments import CommentedMap
data = CommentedMap()  # instead of OrderedDict()
```

### Pattern F: YAML Sexagesimal Trap — `1:1` Parsed as `61`

PyYAML interprets `mixing_ratio: 1:1` as base-60 = 61. Same for `protein_to_lipid_ratio`.

**Detection:** `yaml.safe_load()` silently converts `1:1` to int 61.

**Fix (text-level — yaml already converted the value):**
```python
for field in ["mixing_ratio", "protein_to_lipid_ratio"]:
    raw = re.sub(rf'(?m)^([\s-]*{field}:)\s*(\d+:\d+(?:\.\d+)?)\s*$',
                 lambda m: m.group(1) + " '" + m.group(2) + "'", raw)
```

**Prevention:** Always write as `mixing_ratio: '1:1'`.

### Pattern G: Tag Taxonomy Update

When `validate_yaml.py --strict` rejects an unknown tag, add it to the relevant vocabulary set in `validate_yaml.py`. Common entity tags: gpcr, ion-channel, transporter, enzyme, receptor, pump, porin.

### Pattern H: `patch` Tool Indentation Drift

Adding a new PDB entry to `pdb_dois` via `patch` places it at wrong indentation — looks like sibling of parent key instead of child.

**Detection:** `data['mpstruc_classification']['pdb_dois']` is `None` when it should be a dict.

**Fix:** Manually re-indent lines to 2+ spaces deeper than parent. After any `patch` on a YAML dict key, read the file back and verify indentation.

**Prevention:** Do NOT use `patch` for YAML dict value insertion. Use ruamel.yaml:
```python
with open("file.yaml") as f: data = yaml.load(f)
data["mpstruc_classification"]["pdb_dois"]["5GLH"] = "doi/10.1038##nature19319"
with open("file.yaml", "w") as f: yaml.dump(data, f)
```

### Pattern I: Regex Captures Trailing `)`

Extracting a slug from a markdown link with `([^/]+)` captures trailing `)`. Fix: use `([^/)]+)` — exclude `)` from capture class.

### Pattern J: Sidebar/Nav Index Content Injection

`enrich_wikilinks.py` matches entity names inside sidebar content already embedded in free-text fields, producing concatenated garbage.

**Signature:** Garbled text from other pages' navigation bars/sidebars. Known markers:
`ComplexcComplex`, `Yajcmp-wiki`, `Cuscjmray`, `C-Sars Cov 2 Ctd`, `DltbhhReceptor`, `SecgamaB3`

**Detection:** `grep -rl "ComplexcComplex" xray-mp-wiki/proteins_yaml/`

**Fix — strip-then-rewrite:**
```python
GARBAGE_MARKERS = ["ComplexcComplex", "Yajcmp-wiki", "Cuscjmray", ...]
def strip_garbage(text):
    for marker in GARBAGE_MARKERS:
        idx = text.find(marker)
        if idx > 0: return text[:idx].strip()
    return text
```

For totally corrupted fields, rewrite from the raw paper at `raw/papers/<doi>.md`.

Always check YAML source first (`grep` in `proteins_yaml/*.yaml`). If YAML is clean but `.md` is dirty, the renderer is the problem.

### Pattern K: PDB Code Verification After Repair

Use `check_pdb.py` for lightweight PDB-DOI verification:
```bash
python3 scripts/check_pdb.py <PDB> <DOI>
# Returns FOUND_PAPER | FOUND_MPSTRUC | NOT_FOUND
```

For batch: `scripts/consolidate/verify.py --pdb-in-paper`

**False-negative is expected** — raw paper files may not contain the PDB code string (it lives in supplementary tables). Check MPSTRUC CSV and RCSB API as fallbacks.

### Pattern L: yaml.dump() Reorders Dict Keys

PyYAML's `yaml.dump()` sorts keys alphabetically by default. Always use ruamel.yaml for round-trip preservation.

### Pattern L2: Orphaned Overview Continuation Lines

After partial text-level replacement of a multi-line overview, orphaned continuation lines remain. YAML parser fails with `expected <block end>, but found <scalar>`.

**Fix:** Remove lines between the fixed key and the next top-level key:
```python
lines = open('file.yaml').readlines()
overview_idx = next_key_idx = None
for i, line in enumerate(lines):
    if line.startswith("overview: '"): overview_idx = i
    if line.strip().startswith('biological_insights:'): next_key_idx = i; break
if overview_idx is not None and next_key_idx is not None:
    lines = lines[:overview_idx+1] + lines[next_key_idx:]
    open('file.yaml', 'w').writelines(lines)
```

### Pattern M: PDB ID Digit/Letter Confusion

O↔0, l↔1, S↔5 swaps in PDB IDs (e.g., `6E9O` instead of `6E90`). Detect via RCSB API:
```bash
curl -s "https://data.rcsb.org/rest/v1/core/entry/6E9O" | python3 -c "import sys,json; print(json.load(sys.stdin).get('struct',{}).get('title','NOT FOUND'))"
```

### Pattern M2: Composite PDB Failure

Multiple wrong + swapped + missing PDBs in one source. When ANY PDB is wrong, enumerate ALL PDBs deposited under that DOI — the correct PDB is often numerically adjacent (4GBZ→4GC0).

**Procedure:**
1. Match resolution values from paper abstract/methods to RCSB-confirmed entries
2. Search adjacent PDB IDs (±2 from known set) filtered by primary citation DOI
3. Replace wrong PDBs, fix swapped metadata, add missing entries
4. Validate: `validate_yaml.py protein <name> --strict`


## P0 Trap: Source DOI Case Sensitivity

`sources[]` entries like `doi/10.1038##NSMB.2721` use uppercase journal prefix that doesn't match lowercase filename `10.1038##nsmb.2721.md`. Check:

```python
for src in data.get("sources", []):
    f = src.replace("doi/", "") + ".md"
    if not os.path.exists(os.path.join("raw/papers", f)):
        print(f"P0 FAIL: {f}")
```

**Fix:** Normalize all source DOIs to lowercase, or rename files to match.

**Scope:** Common uppercase journal prefixes: NSMB, NATURE, ELIFE, EMBOJ, SJ.EMBOJ, RA.

---

## Verification Workflow: `regex → pdb`

Run `check_pdb.py` for every PDB-DOI pair in `mpstruc_classification.pdb_dois`:
```bash
python3 scripts/check_pdb.py <PDB> <DOI>
```

If all pass, promote: `verified: regex` → `verified: pdb`. Use `patch` mode for the change.

**FOUND_MPSTRUC is a valid pass** — the MPSTRUC CSV fallback is reliable.

**Not a substitute for full P0-P3 verification** — only confirms PDB belongs to DOI, not resolution/ligand/expression accuracy.


## Checking PDB via RCSB API (alternate to check_pdb.py)

```bash
# Single PDB
curl -s 'https://data.rcsb.org/rest/v1/core/entry/{PDB}' | \
  python3 -c "import sys,json; d=json.load(sys.stdin); \
    t=d.get('struct',{}).get('title',''); \
    r=d.get('rcsb_entry_info',{}).get('resolution_combined',[''])[0]; \
    doi=d.get('rcsb_primary_citation',{}).get('pdbx_database_id_DOI',''); \
    print(f'{t} @ {r}Å  DOI: {doi}')"

# Batch
python3 scripts/mine/rcsb_batch_check.py PDB1 PDB2 PDB3
```


## Post-Repair Checklist

1. `python3 scripts/validate_yaml.py <type> <name> --strict`
2. `python3 scripts/generate_page.py <type> <name> --yes [--skip-catalog]`
3. Check page renders correctly: `cat xray-mp-wiki/<type_s>/<name>.md | head -30`
4. For batch repairs: `python3 scripts/lint.py` → check broken link count
5. If many files changed: `python3 scripts/rebuild_indexes.py --force` + `rebuild_entity_catalog.py --from-filesystem`
