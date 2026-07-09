#!/usr/bin/env python3
"""Rewrite aqy1.yaml expression.notes and biological_insights content from raw papers."""

import yaml
from pathlib import Path

BASE = Path("/home/wtliaf/Desktop/Research/coding_projects/xray-mp-wiki")
YAML_DIR = BASE / "xray-mp-wiki" / "proteins_yaml"
PAPER_DIR = BASE / "raw" / "papers"

path = YAML_DIR / "aqy1.yaml"
with open(path) as f:
    data = yaml.safe_load(f)

# ─── Read raw papers ───
science_paper = (PAPER_DIR / "10.1126##science.1234306.md").read_text()
plos_paper = (PAPER_DIR / "10.1371##journal.pbio.1000130.md").read_text()

# ─── 1. Fix expression.notes ───
data["expression"]["notes"] = (
    "For crystallization, non-tagged endogenously expressed Aqy1 was used. "
    "For functional assays, His6-tagged constructs of Aqy1 and Aqy1\u0394N36 "
    "(lacking residues 1-36) were expressed. Point mutants Y31A, S107D, "
    "and S107A created by site-directed mutagenesis. Cultures grown in a "
    "3 L bioreactor, induced by methanol (Invitrogen protocol)."
)

# ─── 2. Rewrite biological_insights content from raw papers ───
bio_insights = data.get("biological_insights", [])

# Find each by title and set content
for bi in bio_insights:
    title = bi.get("title", "")

    if title == "NPA motif H-bond donor interactions with water":
        bi["content"] = (
            "The dual NPA asparagine residues (Asn112 and Asn224 in Aqy1) donate "
            "H-bonds to passing water molecules, establishing a bipolar orientation "
            "of water molecules within the channel. Subangstrom resolution enables "
            "direct visualization of these H-bond donor interactions through residual "
            "electron density from hydrogen omit maps."
        )

    elif title == "Selectivity filter tautomeric states":
        # Content is actually partially correct - the paper says His212 N-delta is protonated
        # Let's preserve the clean part. The issue is at "N-Masr1rb Ac..."
        # Clean content: "The tautomeric states of the SF residues His212 and Arg227
        # were assigned from omit maps. His212 Nδ is protonated and donates an H-bond
        # to the carbonyl oxygen of Leu208, while Nε is not protonated. Arg227 shows
        # concentrated positive charge on Nη2 (closest to the pore), maximizing
        # repulsion of hydronium ions."
        bi["content"] = (
            "The tautomeric states of the selectivity filter (SF) residues His212 "
            "and Arg227 were assigned from hydrogen omit maps. His212 N\u03b4 is "
            "protonated and donates an H-bond to the carbonyl oxygen of Leu208, "
            "while N\u03b5 is not protonated. Arg227 shows concentrated positive "
            "charge on N\u03b72 (closest to the water channel), maximizing "
            "electrostatic repulsion of hydronium ions."
        )

    elif title == "Four-site pair-wise water transport in the selectivity filter":
        # Keep the clean start, rewrite the garbage part
        bi["content"] = (
            "Four water positions (Wat1-Wat4) within the SF have complementary "
            "occupancies of 34% (Wat1/Wat3) and 66% (Wat2/Wat4) with 1.5 \u00c5 "
            "separation, too close for simultaneous occupation. This is analogous "
            "to the pair-wise ion transport through potassium channels, implying "
            "very little energy difference between configurations 1,3 and 2,4 "
            "for optimal water conduction."
        )

    elif title == "Correlated water movements prevent Grotthuss proton hopping":
        bi["content"] = (
            "MD simulations show strongly correlated movements of adjacent water "
            "molecules at the SF and NPA regions. The H-bond connectivity of water "
            "is significantly perturbed at both the NPA and SF regions, breaking "
            "the continuous H-bond network required for Grotthuss proton transport. "
            "This explains why mutation of SF residues disrupts proton exclusion."
        )

    elif title == "Evolutionary optimization of water channel geometry":
        bi["content"] = (
            "Subangstrom resolution reveals how evolution has fine-tuned the water "
            "channel geometry: all four H-bond donor and acceptor interactions are "
            "filled as water moves through the SF, achieving exceptional water "
            "selectivity. Hydroxide ions suffer a geometric penalty (cannot "
            "simultaneously donate H-bonds to Ala221 and His212), while all "
            "H-bond interactions are distorted from ideal water geometry to avoid "
            "binding water too tightly."
        )

    elif title == "N-terminal gating mechanism":
        bi["content"] = (
            "Aqy1 has an extended N terminus (34 residues longer than AQP1) that "
            "folds into a tightly wound helical bundle on the cytoplasmic side of "
            "the tetramer. Tyr31 enters the water channel and forms H-bond "
            "interactions with a water molecule within the pore, thereby occluding "
            "the channel entrance. This represents a gating mechanism distinct from "
            "the D-loop gating observed in plant aquaporins."
        )

    elif title == "Dual regulation by phosphorylation and mechanosensitivity":
        # Keep the clean part from the YAML (before garbage), add clean ending
        bi["content"] = (
            "Water transport assays and molecular dynamics simulations suggest Aqy1 "
            "is regulated by a combination of phosphorylation at Ser107 and "
            "mechanosensitivity. The S107D mutation (mimicking phosphorylation) "
            "shows increased water transport. MD simulations with increased "
            "lateral pressure (10 bar) or membrane bending both induce spontaneous "
            "channel opening at the Tyr31 gate, involving local rearrangement of "
            "residues Leu189, Ala190, and Val191."
        )

    elif title == "Freeze tolerance function":
        bi["content"] = (
            "Aqy1 deletion causes a freeze-sensitive phenotype in P. pastoris. "
            "Overproduction of Aqy1 or the N-terminally truncated form (Aqy1\u0394N36) "
            "rescues freeze tolerance. However, the permanently open Aqy1\u0394N36 "
            "is detrimental when overproduced in wild-type strains, suggesting that "
            "gating balances water flux for optimal freeze survival."
        )

# ─── 3. Fix purifications steps notes ───
for pub in data.get("publications", []):
    for purif in pub.get("purifications", []):
        for step in purif.get("steps", []):
            if "notes" in step and isinstance(step["notes"], str):
                orig = step["notes"]
                # Clean up common garbage patterns in notes
                # Keep only the text before first garbage marker
                for marker in [
                    "HepeseteteHclr",
                    "Cuscjmray",
                    "Cusbjmray",
                    "Mladoxinstabilization",
                    "1ocessing4Yidce",
                    "Complex release",
                ]:
                    idx = orig.find(marker)
                    if idx >= 0:
                        orig = orig[:idx].strip()
                step["notes"] = orig

# ─── 4. Fix purifications buffer fields ───
for pub in data.get("publications", []):
    for purif in pub.get("purifications", []):
        for step in purif.get("steps", []):
            for field in ["buffer"]:
                if field in step and isinstance(step[field], str):
                    orig = step[field]
                    for marker in [
                        "HepeseteteHclr",
                        "TrisPs Hclray",
                        "fer Trisfer Bis",
                        "Bis [Tris]",
                        "Chesr Hepesr",
                        "Glyciner Acetater",
                        "Succinater Mesm",
                        "Colil 3 Phosphatel",
                        "GlycerolColil",
                    ]:
                        idx = orig.find(marker)
                        if idx >= 0:
                            orig = orig[:idx].strip()
                    step[field] = orig

# ─── 5. Fix crystallization fields ───
for pub in data.get("publications", []):
    for crys in pub.get("crystallizations", []):
        for field in ["notes", "protein_sample", "reservoir"]:
            if field in crys and isinstance(crys[field], str):
                orig = crys[field]
                for marker in [
                    "HepeseteteHclr",
                    "Chesr Hepesr",
                    "Glyciner Acetater",
                    "Succinater Mesm",
                    "Citrater Bis",
                    "TrisPs Hclfer",
                    "Colil 3 Phosphatel",
                    "GlycerolColil",
                    "Cuscjmray",
                    "Mladoxinstabilization",
                    "Complexc",
                    "Complexs",
                    "1ocessing4",
                    "MimeticsCdc50",
                    "ve Lipid Binding",
                    "Center Mechanism",
                    "Side Chain Packing",
                    "Coupling Mechanism",
                    "ponent Signaling",
                    "upported Membrane",
                    "Atpase Stator",
                    "Networks Membrane",
                    "Oligomerizationne",
                    "Crystals For Neutron",
                    "Diffractionrected",
                    "Spin Labeling Membrane",
                    "tom Derivative",
                    "Detergents And Lipids",
                    "1A3 Family",
                    "Family 1obrevin",
                    "FamilyYidcov",
                    "2 Ctd Agonismotein",
                    "Kir3 2dral Twinning",
                    "Mep Protein Family",
                    "rome B561 Family",
                    "Couplinge Binding",
                    "Proteincholine Binding",
                    "Proteinopology Architecturetein",
                    "Nitrosomonas Europaeae",
                    "Cytoplasmic Poreree",
                    "Protein Synthesischromatium",
                    "Tepidum Hipipaeodactylum",
                    "TricornutumGas Anaesthetic",
                    "Networks Membrane Protein",
                    "Oligomerizationne",
                    "Protein Crystals For Neutron",
                    "Diffractionirected",
                    "Spin Labeling Membrane",
                    "ProteinAtom Derivative",
                    "Detergents And Lipids",
                    "Structure Based Antipsychotic Design",
                ]:
                    idx = orig.find(marker)
                    if idx >= 0:
                        orig = orig[:idx].strip()
                crys[field] = orig

# ─── 6. Fix structures notes ───
for pub in data.get("publications", []):
    for struct in pub.get("structures", []):
        for field in ["notes", "ligand", "construct"]:
            if field in struct and isinstance(struct[field], str):
                orig = struct[field]
                for marker in [
                    "Rhodopsin 2 2A",
                    "AQP1ray-mp-wiki",
                    "nray-mp-wiki",
                    "Zray-mp-wiki",
                    "1uaporin",
                    "uaporin 1ray-mp-wiki",
                    "O1 Channelr Network",
                    "H-[Dsbb]",
                    "Barrier Hydrogen Bond",
                    "Pot Family",
                    "Substrate Specificitymer",
                    "Interaction Proteorhodopsin",
                    "Squid Rhodopsin",
                    "Conformational States Clc",
                    "Selectivity Filtertingder",
                    "Selectivity Filterracellular",
                    "Ion Selectivitynnel",
                    "Ion Permeability Selectivityg",
                    "Ion Bound Configurations",
                    "Gas Selectivity Filter",
                    "Couplingded Selectivity Filter",
                    "rmational Coupling Gating",
                ]:
                    idx = orig.find(marker)
                    if idx >= 0:
                        orig = orig[:idx].strip()
                struct[field] = orig

# ─── Write back ───
with open(path, "w") as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

print(f"  Saved {path.name}")
print("Done.")
