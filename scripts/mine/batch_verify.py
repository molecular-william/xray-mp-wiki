#!/usr/bin/env python3
"""Batch verify all PDB codes from 21 protein YAML files."""

from pathlib import Path

import yaml

BASE = Path("/home/wtliaf/Desktop/Research/coding_projects/xray-mp-wiki")
YAML_DIR = BASE / "xray-mp-wiki/proteins_yaml"
PAPER_DIR = BASE / "raw/papers"

files = [
    "acetylcholine-binding-protein",
    "af-tmem16",
    "arabidopsis-nitrate-transporter-nrt1-1",
    "betp",
    "bpe-fluoride-channel",
    "claudin-19-mouse",
    "clbm",
    "clostridium-boltrea-mray",
    "clpp",
    "cmclc",
    "cp-tric",
    "cysz",
    "cytochrome-b561",
    "cytochrome-b5-reductase",
    "cytochrome-b5",
    "d4-dopamine-receptor",
    "dgot",
    "fluc-ec2",
    "glt-ph",
    "human-claudin-4",
    "human-claudin-9",
]

results = {}

for fname in files:
    ypath = YAML_DIR / f"{fname}.yaml"
    if not ypath.exists():
        results[fname] = {"error": "YAML not found"}
        continue

    with open(ypath) as f:
        data = yaml.safe_load(f)

    file_result = {"sources": [], "structures": [], "issues": [], "verified": data.get("verified", "none")}

    # P0: Check paper files exist
    sources = data.get("sources", [])
    for src in sources:
        doi_path = src.replace("doi/", "").replace("/", "##").lower()
        paper_file = PAPER_DIR / f"{doi_path}.md"
        exists = paper_file.exists()
        result = {"doi": src, "paper_exists": exists}
        if not exists:
            for p in PAPER_DIR.glob(f"{doi_path}.*"):
                if p.suffix == ".md":
                    exists = True
                    result["paper_exists_via_glob"] = str(p.name)
                    result["paper_exists"] = True
                    break
        file_result["sources"].append(result)

    # Handle publications - could be dict or list
    pubs = data.get("publications", [])
    if isinstance(pubs, dict):
        pubs = [pubs]

    # Collect all PDB IDs from structures
    struct_pdbs = []
    for pub in pubs:
        if isinstance(pub, dict):
            src = pub.get("source", "")
            for s in pub.get("structures", []):
                if isinstance(s, dict):
                    pdb = s.get("pdb_id", "")
                    res = s.get("resolution", "")
                    if pdb and len(str(pdb)) == 4 and str(pdb).isalnum():
                        struct_pdbs.append({"pdb": pdb, "resolution": res, "source": src})

    file_result["structures"] = struct_pdbs

    # Check pdb_dois consistency
    pdb_dois = data.get("mpstruc_classification", {}).get("pdb_dois", {})
    if isinstance(pdb_dois, dict):
        pdb_dois_keys = list(pdb_dois.keys())
        struct_pdb_ids = [s["pdb"] for s in struct_pdbs]

        orphans = [p for p in pdb_dois_keys if p.upper() not in [x.upper() for x in struct_pdb_ids]]
        if orphans:
            file_result["issues"].append(f"PDBs in pdb_dois but not in structures: {orphans}")

        extra = [s for s in struct_pdb_ids if s.upper() not in [p.upper() for p in pdb_dois_keys]]
        if extra:
            file_result["issues"].append(f"PDBs in structures but not in pdb_dois: {extra}")

    # Check duplicate PDBs
    seen = {}
    for s in struct_pdb_ids:
        seen[s] = seen.get(s, 0) + 1
    dupes = {k: v for k, v in seen.items() if v > 1}
    if dupes:
        file_result["issues"].append(f"Duplicate PDBs in structures: {dupes}")

    # Check resolution quoting
    for s in struct_pdbs:
        res = s["resolution"]
        if isinstance(res, str) and " " in res and not res.startswith("'"):
            file_result["issues"].append(f"Resolution '{res}' contains space - may need quoting")

    results[fname] = file_result

# Print summary
print("=" * 80)
print("BATCH VERIFICATION SUMMARY")
print("=" * 80)

pass_count = 0
issue_count = 0

for fname, r in results.items():
    paper_ok = all(s.get("paper_exists", False) for s in r.get("sources", []))
    has_issues = len(r.get("issues", [])) > 0 or len(r.get("structures", [])) == 0

    if paper_ok and not has_issues:
        status = "✓ PASS"
        pass_count += 1
    else:
        status = "✗ ISSUES"
        issue_count += 1

    print(f"\n[{status}] {fname} (verified: {r.get('verified')})")
    for s in r.get("sources", []):
        flag = "✓" if s.get("paper_exists") else "✗"
        print(f"  {flag} Paper: {s['doi']}")
    for s in r.get("structures", []):
        print(f"    PDB: {s['pdb']} @ {s.get('resolution', '?')} — source: {s.get('source', '?')}")
    for iss in r.get("issues", []):
        print(f"  ⚠ {iss}")

print(f"\n{'=' * 80}")
print(f"PASS: {pass_count} | ISSUES: {issue_count}")
