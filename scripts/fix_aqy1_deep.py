#!/usr/bin/env python3
"""Fix aqy1.yaml expression.notes and deeply clean biological_insights content."""

import yaml
import re
from pathlib import Path

BASE = Path("/home/wtliaf/Desktop/Research/coding_projects/xray-mp-wiki")
YAML_DIR = BASE / "xray-mp-wiki" / "proteins_yaml"

# Load aqy1
path = YAML_DIR / "aqy1.yaml"
with open(path) as f:
    raw = f.read()

data = yaml.safe_load(raw)

# ─── 1. Fix expression.notes ───
# Recover clean text from raw papers:
# PLOS Biology paper methods: "For crystallization, nontagged, endogenously expressed Aqy1 was used."
# "All cultures were grown in a 3 L bioreactor and the protein expression was induced by methanol" 
# "For functional assays, His6-tagged constructs of Aqy1 and Aqy1ΔN36 were expressed."
# "Point mutants Y31A, S107D, and S107A created by site-directed mutagenesis."

data["expression"]["notes"] = (
    "For crystallization, non-tagged endogenously expressed Aqy1 was used. "
    "For functional assays, His6-tagged constructs of Aqy1 and Aqy1\u0394N36 "
    "(lacking residues 1-36) were expressed. Point mutants Y31A, S107D, "
    "and S107A created by site-directed mutagenesis. Cultures grown in a "
    "3 L bioreactor, induced by methanol (Invitrogen protocol)."
)

# ─── 2. Define known garbage markers ───
GARBAGE_MARKERS = [
    "Conformational Dynamics Mfsl Dynamics",
    "Mppasesonal Equilibriumational",
    "Cuscjmray-mp-wiki/proteins/wza/",
    "Cusbjmray-mp-wiki",
    "C-Nav1 4 Cterm",
    "Mladoxinstabilizationtiona",
    "Yajcmp-wiki/proteins/",
    "Kkrsepsep",
    "Fkbp12",
    "Ton Complexc",
    "ComplexcComplex",
    "Acidophila Molischianum",
    "SecgamaB3",
    "DltbhhReceptor",
    "Tat A Substrate",
    "C-Sars Cov 2 Ctd",
    "N-Sars Cov 2 Ctd",
    "For Truncationllization",
    "Truncationllization",
    "Sf9 Expression Systemression Systemi",
    "Kkrsepsep2P Site Binding",
    "Ry3RR51rtd470",
    "Pbga4 Interaction Complexpin",
    "Mjnhap1channelal Proton Pumpn",
    "Navms21Bc2cccannel",
    "Cry6Aaabce Forming Toxins",
    "1ocessing4Yidce",
    "The Th Pf02Pf01Pf03l",
    "Cuscjmray",
    "Yajcmp",
]

def strip_garbage(text):
    if not isinstance(text, str):
        return text
    for marker in GARBAGE_MARKERS:
        idx = text.find(marker)
        if idx >= 0:
            return text[:idx].strip()
    return text

# ─── 3. Clean all biological_insights content ───
for bi in data.get("biological_insights", []):
    if "content" in bi and isinstance(bi["content"], str):
        orig = bi["content"]
        cleaned = strip_garbage(orig)
        if cleaned != orig:
            print(f"  biological_insights '{bi.get('title', '?')}' content: {len(orig)} -> {len(cleaned)} chars")
            bi["content"] = cleaned

# ─── 4. Clean expressions.notes ───
# Already set above

# ─── 5. Clean purifications steps notes ───
for pub in data.get("publications", []):
    for purif in pub.get("purifications", []):
        for step in purif.get("steps", []):
            if "notes" in step and isinstance(step["notes"], str):
                orig = step["notes"]
                cleaned = strip_garbage(orig)
                if cleaned != orig:
                    print(f"  purification step '{step.get('step', '?')}' notes: {len(orig)} -> {len(cleaned)} chars")
                    step["notes"] = cleaned

# ─── 6. Clean crystallization fields ───
for pub in data.get("publications", []):
    for crys in pub.get("crystallizations", []):
        for field in ["notes", "protein_sample", "reservoir"]:
            if field in crys and isinstance(crys[field], str):
                orig = crys[field]
                cleaned = strip_garbage(orig)
                if cleaned != orig:
                    print(f"  crystallization.{field}: {len(orig)} -> {len(cleaned)} chars")
                    crys[field] = cleaned

# ─── 7. Clean structures fields ───
for pub in data.get("publications", []):
    for struct in pub.get("structures", []):
        for field in ["notes", "ligand", "construct"]:
            if field in struct and isinstance(struct[field], str):
                orig = struct[field]
                cleaned = strip_garbage(orig)
                if cleaned != orig:
                    print(f"  structure {struct.get('pdb_id', '?')}.{field}: {len(orig)} -> {len(cleaned)} chars")
                    struct[field] = cleaned

# ─── 8. Clean other free-text fields ───
for field in ["overview"]:
    if field in data and isinstance(data[field], str):
        orig = data[field]
        cleaned = strip_garbage(orig)
        if cleaned != orig:
            print(f"  {field}: {len(orig)} -> {len(cleaned)} chars")
            data[field] = cleaned

# ─── Write back ───
with open(path, "w") as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

print(f"  Saved {path.name}")
print("Done.")
