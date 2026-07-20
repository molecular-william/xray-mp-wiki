#!/usr/bin/env python3
"""Fix fluc-ec2.yaml overview corruption and promote to agent."""
import re

fp = '/home/wtliaf/Desktop/Research/coding_projects/xray-mp-wiki/xray-mp-wiki/proteins_yaml/fluc-ec2.yaml'
with open(fp, 'r') as f:
    lines = f.readlines()

# Find the overview line
new_lines = []
in_overview = False
overview_replaced = False

for i, line in enumerate(lines):
    if line.startswith('overview: "Fluc Family of Fluoride Ion Channels-Ec2'):
        new_lines.append("overview: 'Ec2 is a fluoride ion channel from an E. coli virulence plasmid, belonging to the Fluc family. Fluc channels are small (~120 residues per subunit), dual-topology homodimeric membrane proteins that protect bacteria from environmental fluoride toxicity by allowing passive F- transit down its electrochemical gradient. Ec2 exhibits exceptionally high F-/Cl- selectivity and has two independent F- permeation pathways.'\n")
        in_overview = False
        overview_replaced = True
    elif line.startswith('overview:'):
        new_lines.append(line)
        in_overview = False
    elif in_overview:
        # Skip continuation lines until we hit the end of the quoted string
        if '\\n"' in line:
            in_overview = False
        # else skip
    elif line.strip().startswith('biological_insights:'):
        if in_overview:
            in_overview = False
        new_lines.append(line)
    else:
        new_lines.append(line)

# Also fix verified field
fixed = ''.join(new_lines)
fixed = re.sub(r'verified: regex(?=\s)', 'verified: agent', fixed)

with open(fp, 'w') as f:
    f.write(fixed)

print('Done' if overview_replaced else 'Overview not found')
