#!/usr/bin/env python3
"""Promote verified pdb->agent for fixed files."""

from collections import Counter
from datetime import date
from pathlib import Path

import yaml

base = Path("xray-mp-wiki/proteins_yaml")

files = [
    "human-dhhc20",
    "human-ebp",
    "human-ep4-receptor",
    "human-glut3",
    "human-glyt1",
    "human-endothelin-etb-receptor-et1",
    "kv1-2-2-1-3m-channel",
    "kv1-2-2-1-2m-channel",
    "kv1-2-2-1-v406w",
    "ktrb",
    "leubat",
    "human-connexin-26-gap-junction-channel",
    "human-dopamine-d3-receptor",
    "human-endothelin-etb-receptor-irl2500",
    "human-histamine-h1-receptor",
    "human-histamine-h3-receptor",
    "human-k2p1-twik-1",
]

for f in files:
    yf = base / f"{f}.yaml"
    if not yf.exists():
        print(f"{f}: MISSING")
        continue
    with open(yf) as fh:
        data = yaml.safe_load(fh)

    old_v = data.get("verified", "?")
    issues = []

    pdb_dois = data.get("mpstruc_classification", {}).get("pdb_dois") or {}
    publications = data.get("publications", [])
    if isinstance(publications, dict):
        publications = [publications]
    for pub in publications:
        for s in pub.get("structures", []):
            pdb = s.get("pdb_id", "")
            if pdb and len(pdb) == 4 and pdb.isalnum() and pdb not in pdb_dois:
                issues.append(f"{pdb} not in pdb_dois")

    all_pdbs = []
    for pub in publications:
        for s in pub.get("structures", []):
            p = s.get("pdb_id", "")
            if p and len(p) == 4 and p.isalnum():
                all_pdbs.append(p)
    for k, v in Counter(all_pdbs).items():
        if v > 1:
            issues.append(f"Duplicate PDB: {k}")

    if not issues and old_v in ("pdb", "regex"):
        data["verified"] = "agent"
        data["updated"] = str(date.today())
        with open(yf, "w") as fh:
            yaml.dump(data, fh, default_flow_style=False, allow_unicode=True, sort_keys=False)
        print(f"{f}: {old_v} -> agent ✓")
    elif not issues and old_v in ("agent", "human"):
        print(f"{f}: already {old_v} ✓")
    else:
        print(f"{f}: {old_v} -> BLOCKED: {issues}")
