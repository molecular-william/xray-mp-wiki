#!/usr/bin/env python3
"""Fix unquoted values starting with [ — bulk enrich introduced these."""

from pathlib import Path

import yaml

W = Path("/home/wtliaf/Desktop/Research/coding_projects/xray-mp-wiki/xray-mp-wiki")

total_fixed = 0
files_fixed = set()

for yf in sorted((W / "proteins_yaml").rglob("*.yaml")):
    data = yaml.safe_load(yf.read_text())
    if not isinstance(data, dict):
        continue

    modified = False
    targets = []

    # Collect all target field references
    for pi, p in enumerate(data.get("purifications", []) or []):
        for si, s in enumerate(p.get("steps", []) or []):
            if not isinstance(s, dict):
                continue
            for f in ["detergent", "method", "resin", "buffer", "notes"]:
                val = s.get(f, "")
                if isinstance(val, str) and val.startswith("[") and not val.startswith("[["):
                    targets.append((f"purifications[{pi}].steps[{si}].{f}", val))

    for ci, c in enumerate(data.get("crystallizations", []) or []):
        if not isinstance(c, dict):
            continue
        for f in ["method", "protein_sample", "reservoir", "notes"]:
            val = c.get(f, "")
            if isinstance(val, str) and val.startswith("[") and not val.startswith("[["):
                targets.append((f"crystallizations[{ci}].{f}", val))

    if targets:
        raw = yf.read_text()
        new_raw = raw
        for _, val in targets:
            if "'" + val + "'" not in raw and '"' + val + '"' not in raw:
                new_raw = new_raw.replace(f": {val}\n", f": '{val}'\n", 1)
        if new_raw != raw:
            yf.write_text(new_raw)
            files_fixed.add(yf.stem)
            total_fixed += len(targets)

print(f"Fixed: {len(files_fixed)} files, {total_fixed} bracket-at-start values quoted")
