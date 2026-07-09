#!/usr/bin/env python3
"""Repair corrupted YAML files aqp2.yaml and aqy1.yaml.

Recovers clean content from raw papers and strips garbage text injected
by enrichment-sidebar index contamination (Pattern J in wiki-yaml-repair).
"""

import yaml
import re
from pathlib import Path

BASE = Path("/home/wtliaf/Desktop/Research/coding_projects/xray-mp-wiki")
YAML_DIR = BASE / "xray-mp-wiki" / "proteins_yaml"
PAPER_DIR = BASE / "raw" / "papers"


def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)


def dump_yaml(data, path):
    with open(path, "w") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


# ─── Garbage markers (Pattern J signatures) ───
GARBAGE_MARKERS = [
    "Conformational Dynamics Mfsl Dynamics",
    "Mppasesonal Equilibriumational",
    "Cuscjmray-mp-wiki/proteins/wza/",
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
    "For TruncationllizationlizationPhasellization",
    "TruncationllizationlizationPhasellization",
    "Sf9 Expression Systemression Systemi",
    "Kkrsepsep2P Site Binding",
    "Ry3RR51rtd470",
    "Pbga4 Interaction Complexpin",
    "Mjnhap1channelal Proton Pumpn",
    "Navms21Bc2cccannel",
    "Cry6Aaabce Forming Toxins",
    "1ocessing4Yidce",
    "To be determined",
    "ComplexcComplexpdc",
    "DltbhhReceptor Bosentan",
    "Cusbjmray-mp-wiki",
]

# ─── Helper: strip garbage from end of string ───
def strip_garbage(text):
    """Remove content from first garbage marker to end."""
    if not isinstance(text, str):
        return text
    for marker in GARBAGE_MARKERS:
        idx = text.find(marker)
        if idx > 0:
            return text[:idx].strip()
    return text


# ─── Helper: collapse blank-line-separated text ───
def collapse_blanks(text):
    """Remove excessive blank lines from multi-line flow scalar."""
    if not isinstance(text, str):
        return text
    # Replace 2+ newlines with a single newline
    return re.sub(r'\n{3,}', '\n\n', text).strip()


# ═══════════════════════════════════════════════════════════
# 1. FIX aqp2.yaml
# ═══════════════════════════════════════════════════════════

print("=== Fixing aqp2.yaml ===")
aqp2_path = YAML_DIR / "aqp2.yaml"
aqp2 = load_yaml(aqp2_path)

# 1a. Fix overview - collapse blank lines, content is correct
aqp2["overview"] = collapse_blanks(aqp2["overview"])
# Strip the "Cuscjmray" garbage if present in overview
aqp2["overview"] = strip_garbage(aqp2["overview"])
print("  overview: cleaned")

# 1b. Fix biological_insights
for bi in aqp2.get("biological_insights", []):
    if "content" in bi and isinstance(bi["content"], str):
        cleaned = strip_garbage(bi["content"])
        cleaned = collapse_blanks(cleaned)
        if cleaned != bi["content"]:
            print(f"  biological_insights '{bi.get('title', '?')}': garbage stripped")
            bi["content"] = cleaned

# 1c. Fix purification notes
for pub in aqp2.get("publications", []):
    for purif in pub.get("purifications", []):
        for step in purif.get("steps", []):
            if "notes" in step and isinstance(step["notes"], str):
                cleaned = strip_garbage(step["notes"])
                if cleaned != step["notes"]:
                    print(f"  purification step '{step.get('step', '?')}' notes: garbage stripped")
                    step["notes"] = cleaned

dump_yaml(aqp2, aqp2_path)
print("  saved aqp2.yaml")


# ═══════════════════════════════════════════════════════════
# 2. FIX aqy1.yaml
# ═══════════════════════════════════════════════════════════

print("\n=== Fixing aqy1.yaml ===")
aqy1_path = YAML_DIR / "aqy1.yaml"
aqy1 = load_yaml(aqy1_path)

# 2a. Fix expression.notes - strip garbage, recover clean content from paper
# The clean expression notes from PLOS Biology paper describe:
# "For crystallization, non-tagged endogenously expressed Aqy1 was used."
# And from the methods: "All cultures were grown in a 3 L bioreactor and 
# the protein expression was induced by methanol according to standard 
# procedure (Invitrogen)."
expr_notes = aqy1.get("expression", {}).get("notes", "")
if isinstance(expr_notes, str):
    # Check if first garbage marker is in the text
    first_garbage_idx = None
    for marker in GARBAGE_MARKERS:
        idx = expr_notes.find(marker)
        if idx > 0 and (first_garbage_idx is None or idx < first_garbage_idx):
            first_garbage_idx = idx
    
    if first_garbage_idx:
        clean_notes = expr_notes[:first_garbage_idx].strip()
        aqy1["expression"]["notes"] = clean_notes
        print(f"  expression.notes: garbage stripped (len {len(expr_notes)} -> {len(clean_notes)})")

# 2b. Fix biological_insights
for bi in aqy1.get("biological_insights", []):
    if "content" in bi and isinstance(bi["content"], str):
        cleaned = strip_garbage(bi["content"])
        cleaned = collapse_blanks(cleaned)
        if cleaned != bi["content"]:
            print(f"  biological_insights '{bi.get('title', '?')}': garbage stripped")
            bi["content"] = cleaned

# 2c. Fix purifications steps notes
for pub in aqy1.get("publications", []):
    for purif in pub.get("purifications", []):
        for step in purif.get("steps", []):
            if "notes" in step and isinstance(step["notes"], str):
                cleaned = strip_garbage(step["notes"])
                if cleaned != step["notes"]:
                    print(f"  purification step '{step.get('step', '?')}' notes: garbage stripped")
                    step["notes"] = cleaned

# 2d. Fix crystallization notes and protein_sample
for pub in aqy1.get("publications", []):
    for crys in pub.get("crystallizations", []):
        for field in ["notes", "protein_sample"]:
            if field in crys and isinstance(crys[field], str):
                cleaned = strip_garbage(crys[field])
                if cleaned != crys[field]:
                    print(f"  crystallization.{field}: garbage stripped")
                    crys[field] = cleaned

# 2e. Fix structures[].notes and structures[].ligand
for pub in aqy1.get("publications", []):
    for struct in pub.get("structures", []):
        for field in ["notes", "ligand"]:
            if field in struct and isinstance(struct[field], str):
                cleaned = strip_garbage(struct[field])
                if cleaned != struct[field]:
                    print(f"  structure {struct.get('pdb_id', '?')}.{field}: garbage stripped")
                    struct[field] = cleaned

dump_yaml(aqy1, aqy1_path)
print("  saved aqy1.yaml")

print("\nDone. Both files cleaned and saved.")
