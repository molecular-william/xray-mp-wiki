#!/usr/bin/env python3
"""Fix aqp2.yaml: overview blank lines, biological_insights, purification notes."""

import yaml
import re
from pathlib import Path

path = Path("/home/wtliaf/Desktop/Research/coding_projects/xray-mp-wiki/xray-mp-wiki/proteins_yaml/aqp2.yaml")

with open(path) as f:
    data = yaml.safe_load(f)

# ─── 1. Fix overview - collapse blank lines ───
overview = data.get("overview", "")
# Replace 2+ newlines with a single newline (but keep paragraph breaks)
overview = re.sub(r'\n{3,}', '\n\n', overview)
# Also remove trailing whitespace at end of lines
overview = re.sub(r' +\n', '\n', overview)
data["overview"] = overview
print("  overview: cleaned blank lines")

# ─── 2. Fix biological_insights content ───
insights_fixes = {
    "C-terminal conformational variability":
        "The C-terminal helix of AQP2 shows significant conformational "
        "variability across the four protomers of the tetramer. In protomer "
        "C, the C-terminal helix interacts with a symmetry-related AQP2 "
        "molecule via leucine residues (Leu230, 234, 237, 240), suggesting "
        "a role in protein-protein interactions relevant to AQP2 trafficking "
        "and LIP5 binding.",

    "Cd\u00b2\u207a and Ca\u00b2\u207a binding sites":
        "Two Cd\u00b2\u207a binding sites (Cd1 and Cd2) identified per AQP2 "
        "tetramer. Cd1 is at the interface between protomers A and D, ligated "
        "by GluA155 and GlnD57. Cd2 is located between loop B and the "
        "C-terminal tail in protomer C. Radioactive Ca\u00b2\u207a assays "
        "demonstrate that AQP2-expressing oocytes bind significantly more "
        "Ca\u00b2\u207a than controls, suggesting Ca\u00b2\u207a is the "
        "physiological ligand for these sites.",

    "NDI-causing mutations in the wild-type structure":
        "The wild-type AQP2 structure reveals locations of mutations causing "
        "NDI. Key sites include: Gln57 (Cd1 ligand), Ser148 (casein kinase II "
        "site), Thr125/Thr126 in loop C near the N-glycosylation site at "
        "Asn123, and Asp150 in loop D which mediates interactions with the "
        "C-terminal tail via Arg152. Most NDI-causing mutations are in "
        "transmembrane domains and cause misfolding and ER retention.",
}

for bi in data.get("biological_insights", []):
    title = bi.get("title", "")
    if title in insights_fixes:
        bi["content"] = insights_fixes[title]
        print(f"  biological_insights '{title}': fixed")

# ─── 3. Fix purification step notes (strip garbage) ───
GARBAGE_PATTERNS = [
    "Mladoxinstabilizationtiona",
    "Entropic Spring MechanismInjection",
    "TruncationllizationlizationPhasellization",
    "Cuscjmray",
    "ClppPn ProteaseProteased",
    "Proteaseubstratetease Mechanism",
    "Cyto Aeolicus Ftshchia Coli Sppa",
    "Protease Family Mechanismd Protease Substrate Specificity",
]

import re as re_module

for pub in data.get("publications", []):
    for purif in pub.get("purifications", []):
        for step in purif.get("steps", []):
            if "notes" in step and isinstance(step["notes"], str):
                orig = step["notes"]
                for pat in GARBAGE_PATTERNS:
                    idx = orig.find(pat)
                    if idx >= 0:
                        orig = orig[:idx].strip()
                if orig != step["notes"]:
                    print(f"  purification '{step.get('step', '?')[:40]}' notes: cleaned")
                    step["notes"] = orig

# ─── Write back ───
with open(path, "w") as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

print(f"Saved {path.name}")
