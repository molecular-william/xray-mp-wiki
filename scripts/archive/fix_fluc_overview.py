#!/usr/bin/env python3
"""Fix fluc-ec2 overview corruption."""

with open(
    "/home/wtliaf/Desktop/Research/coding_projects/xray-mp-wiki/xray-mp-wiki/proteins_yaml/fluc-ec2.yaml", "r"
) as f:
    content = f.read()

# Find and replace the corrupted overview
old_start = 'overview: "Fluc Family of Fluoride Ion Channels-Ec2 is a Ec2-specific Ion Ec2 from'
idx = content.find(old_start)
if idx > 0:
    end_marker = '.\\n"'
    end_idx = content.find(end_marker, idx)
    if end_idx > 0:
        new_overview = "overview: 'Ec2 is a fluoride ion channel from an E. coli virulence plasmid, belonging to the Fluc family. Fluc channels are small (~120 residues per subunit), dual-topology homodimeric membrane proteins that protect bacteria from environmental fluoride toxicity by allowing passive F- transit down its electrochemical gradient. Ec2 exhibits exceptionally high F-/Cl- selectivity and has two independent F- permeation pathways.'"
        new_content = content[:idx] + new_overview + content[end_idx + len(end_marker) :]
        with open(
            "/home/wtliaf/Desktop/Research/coding_projects/xray-mp-wiki/xray-mp-wiki/proteins_yaml/fluc-ec2.yaml", "w"
        ) as f:
            f.write(new_content)
        print("Fixed overview")
    else:
        print("Could not find end marker")
else:
    print("Could not find old overview, trying alternative...")
    # Try finding just the start
    alt_start = "Fluc Family of Fluoride Ion Channels-Ec2"
    idx2 = content.find(alt_start)
    if idx2 > 0:
        # Find the line start
        line_start = content.rfind("\n", 0, idx2) + 1
        prefix = content[line_start:idx2]
        print(f"Found at line with prefix: {prefix[:50]}...")
