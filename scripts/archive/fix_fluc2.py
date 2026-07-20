#!/usr/bin/env python3
"""Fix fluc-ec2.yaml - remove orphaned overview continuation lines."""

fp = "/home/wtliaf/Desktop/Research/coding_projects/xray-mp-wiki/xray-mp-wiki/proteins_yaml/fluc-ec2.yaml"
with open(fp, "r") as f:
    lines = f.readlines()

# Find the overview line and the biological_insights line
overview_idx = None
bio_idx = None
for i, line in enumerate(lines):
    if line.startswith("overview: 'Ec2 is a fluoride ion channel"):
        overview_idx = i
    if line.strip().startswith("biological_insights:"):
        bio_idx = i
        break

if overview_idx is not None and bio_idx is not None:
    # Remove all lines between overview and biological_insights (the orphaned continuation)
    new_lines = lines[: overview_idx + 1] + lines[bio_idx:]
    with open(fp, "w") as f:
        f.writelines(new_lines)
    print(f"Removed {bio_idx - overview_idx - 1} orphaned lines")
else:
    print(f"overview_idx={overview_idx}, bio_idx={bio_idx}")
