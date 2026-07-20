#!/usr/bin/env python3
"""
Safely add crystallization_details to a crystallization entry.
Called by subagent: python3 scripts/enrich/cry_step_patch.py <yaml_path> <pub_idx> <cry_idx> '<json_details>'
"""

import json
import sys
from pathlib import Path

from ruamel.yaml import YAML

yaml_path = Path(sys.argv[1])
pub_idx = int(sys.argv[2])
cry_idx = int(sys.argv[3])
details = json.loads(sys.argv[4])

ry = YAML()
ry.preserve_quotes = True
ry.indent(mapping=2, sequence=4, offset=2)

data = ry.load(yaml_path.read_text())
entry = data["publications"][pub_idx]["crystallizations"][cry_idx]

# Don't overwrite existing data
if "crystallization_details" not in entry:
    entry["crystallization_details"] = details
    ry.dump(data, yaml_path)
    print(f"OK: added crystallization_details to {yaml_path.name}[{pub_idx}][{cry_idx}]")
else:
    print("SKIP: already has crystallization_details")
