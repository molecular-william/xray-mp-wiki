#!/usr/bin/env python3
"""Generate index.md for each subdirectory (proteins/gpcr/, reagents/detergents/, etc.).
Scans rendered .md pages, reads frontmatter, generates a table of contents page.
Run after adding new entities or reorganizing subdirectories."""
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
WIKI = BASE / "xray-mp-wiki"

def parse_frontmatter(text):
    m = re.search(r'^title:\s*"(.+?)"', text, re.MULTILINE)
    if m:
        return m.group(1)
    m = re.search(r"^title:\s*'(.+?)'", text, re.MULTILINE)
    if m:
        return m.group(1)
    m = re.search(r"^title:\s*(.+)", text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return None

subdir_display = {
    "gpcr": "G Protein-Coupled Receptors (GPCRs)",
    "rhodopsins": "Rhodopsins",
    "voltage-gated-channels": "Voltage-Gated Ion Channels",
    "cys-loop-receptors": "Cys-Loop Receptors",
    "other-ion-channels": "Other Ion Channels",
    "abc-transporters": "ABC Transporters",
    "mfs-transporters": "MFS Transporters",
    "slc-transporters": "SLC Family Transporters",
    "pumps-atpases": "Pumps & ATPases",
    "secretion-translocon": "Secretion & Translocon",
    "photosynthesis": "Photosynthesis",
    "enzymes": "Membrane Enzymes",
    "structural-adhesion": "Structural & Adhesion Proteins",
    "toxins": "Pore-Forming Toxins",
    "receptors-signaling": "Receptors & Signaling",
    "miscellaneous": "Miscellaneous Proteins",
    "additives": "Additives", "antibiotics": "Antibiotics",
    "antibodies": "Antibodies", "buffers": "Buffers",
    "cofactors": "Cofactors", "detergents": "Detergents",
    "ligands": "Ligands", "lipids": "Lipids",
    "protein-tags": "Protein Tags", "substrates": "Substrates",
    "cell-lysis": "Cell Lysis", "crystallization": "Crystallization",
    "expression-systems": "Expression Systems", "purification": "Purification",
    "quality-assessment": "Quality Assessment", "solubilization": "Solubilization",
    "structure-determination": "Structure Determination",
    "construct-design": "Construct Design",
    "enzyme-mechanisms": "Enzyme Mechanisms",
    "membrane-mimetics": "Membrane Mimetics",
    "methods-techniques": "Methods & Techniques",
    "protein-families": "Protein Families",
    "rhodopsin-mechanisms": "Rhodopsin Mechanisms",
    "signaling-receptors": "Signaling & Receptors",
    "structural-mechanisms": "Structural Mechanisms",
    "transport-mechanisms": "Transport Mechanisms",
}

count = 0
for parent_type in ["proteins", "reagents", "methods", "concepts"]:
    parent_dir = WIKI / parent_type
    if not parent_dir.exists():
        continue
    for subdir in sorted(parent_dir.iterdir()):
        if not subdir.is_dir():
            continue
        files = sorted([f for f in subdir.glob("*.md") if f.name != "index.md"])
        if not files:
            continue
        display = subdir_display.get(subdir.name, subdir.name.replace("-", " ").title())
        lines = ["---", "layout: default", f'title: "{display}"', "---", "",
                 f"# {display}", "", f"{len(files)} pages in this category.", "",
                 "| Page | Description |", "|------|-------------|"]
        for f in files:
            text = f.read_text()
            title = parse_frontmatter(text) or f.stem.replace("-", " ").title()
            body = re.sub(r'^---.*?---\s*', '', text, count=1, flags=re.DOTALL)
            body = re.sub(r'^#\s+.*\n?', '', body, count=1)
            first = ""
            for line in body.split('\n'):
                s = line.strip()
                if s and not s.startswith('<') and not s.startswith('#'):
                    first = s[:150] + ("..." if len(s) > 150 else "")
                    break
            lines.append(f"| [{title}](/xray-mp-wiki/{parent_type}/{subdir.name}/{f.stem}/) | {first} |")
        lines.append("")
        (subdir / "index.md").write_text("\n".join(lines))
        count += 1
print(f"Generated {count} subdirectory index pages")
