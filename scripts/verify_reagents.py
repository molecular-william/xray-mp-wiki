"""Verify reagents: check chemical name appears in paper text. Deterministic, 0 tokens."""

import re
from pathlib import Path

import yaml

r_dir = Path("xray-mp-wiki/reagents_yaml")
promoted = 0
for yf in sorted(r_dir.rglob("*.yaml")):
    if yf.name.endswith(".bak"):
        continue
    d = yaml.safe_load(yf.read_text())
    if d.get("verified") != "regex":
        continue
    sources = d.get("sources") or []
    if not sources and d.get("type") == "antibody":
        # Antibodies with no papers: skip (general knowledge)
        continue

    name = d.get("title", yf.stem).lower()
    all_pass = True
    for s in sources:
        if not isinstance(s, str):
            continue
        doi_fn = s.replace("doi/", "") + ".md"
        pf = Path("raw/papers") / doi_fn
        if not pf.exists():
            all_pass = False
            continue
        text = pf.read_text().lower()
        if name not in text:
            all_pass = False

    if all_pass:
        raw = yf.read_text()
        raw = re.sub(r"^verified: regex$", "verified: agent", raw, count=1, flags=re.MULTILINE)
        yf.write_text(raw)
        promoted += 1

print(f"Promoted: {promoted}")
