#!/usr/bin/env python3
"""Fix aqy1.yaml biological_insights content fields programmatically."""

import yaml
from pathlib import Path

path = Path("/home/wtliaf/Desktop/Research/coding_projects/xray-mp-wiki/xray-mp-wiki/proteins_yaml/aqy1.yaml")

with open(path) as f:
    raw = f.read()

data = yaml.safe_load(raw)

# Recover clean biological_insights content from raw papers
insights_content = {
    "NPA motif H-bond donor interactions with water":
        "The dual NPA asparagine residues (Asn112 and Asn224 in Aqy1) donate "
        "H-bonds to passing water molecules, establishing a bipolar orientation "
        "of water molecules within the channel. Subangstrom resolution enables "
        "direct visualization of these H-bond donor interactions through residual "
        "electron density from hydrogen omit maps.",

    "Selectivity filter tautomeric states":
        "The tautomeric states of the selectivity filter residues His212 "
        "and Arg227 were assigned from hydrogen omit maps. His212 N\u03b4 is "
        "protonated and donates an H-bond to the carbonyl oxygen of Leu208, "
        "while N\u03b5 is not protonated. Arg227 shows concentrated positive "
        "charge on N\u03b72 (closest to the water channel), maximizing "
        "electrostatic repulsion of hydronium ions.",

    "Four-site pair-wise water transport in the selectivity filter":
        "Four water positions (Wat1-Wat4) within the SF have complementary "
        "occupancies of 34% (Wat1/Wat3) and 66% (Wat2/Wat4) with 1.5 \u00c5 "
        "separation, too close for simultaneous occupation. This is analogous "
        "to the pair-wise ion transport through potassium channels, implying "
        "very little energy difference between configurations 1,3 and 2,4 "
        "for optimal water conduction.",

    "Correlated water movements prevent Grotthuss proton hopping":
        "MD simulations show strongly correlated movements of adjacent water "
        "molecules at the SF and NPA regions. The H-bond connectivity of water "
        "is significantly perturbed at both the NPA and SF regions, breaking "
        "the continuous H-bond network required for Grotthuss proton transport. "
        "This explains why mutation of SF residues disrupts proton exclusion.",

    "Evolutionary optimization of water channel geometry":
        "Subangstrom resolution reveals how evolution has fine-tuned water "
        "channel geometry: all four H-bond donor and acceptor interactions are "
        "filled as water moves through the SF, achieving exceptional water "
        "selectivity. Hydroxide ions suffer a geometric penalty (cannot "
        "simultaneously donate H-bonds to Ala221 and His212), while all "
        "H-bond interactions are distorted from ideal water geometry to avoid "
        "binding water too tightly.",

    "N-terminal gating mechanism":
        "Aqy1 has an extended N terminus (34 residues longer than AQP1) that "
        "folds into a tightly wound helical bundle on the cytoplasmic side of "
        "the tetramer. Tyr31 enters the water channel and forms H-bond "
        "interactions with a water molecule within the pore, thereby occluding "
        "the channel entrance. This represents a gating mechanism distinct "
        "from the D-loop gating observed in plant aquaporins.",

    "Dual regulation by phosphorylation and mechanosensitivity":
        "Water transport assays and molecular dynamics simulations suggest "
        "Aqy1 is regulated by a combination of phosphorylation at Ser107 and "
        "mechanosensitivity. The S107D mutation (mimicking phosphorylation) "
        "shows increased water transport. MD simulations with increased "
        "lateral pressure (10 bar) or membrane bending both induce spontaneous "
        "channel opening at the Tyr31 gate, involving local rearrangement of "
        "residues Leu189, Ala190, and Val191.",

    "Freeze tolerance function":
        "Aqy1 deletion causes a freeze-sensitive phenotype in P. pastoris. "
        "Overproduction of Aqy1 or the N-terminally truncated form "
        "(Aqy1\u0394N36) rescues freeze tolerance. However, the permanently "
        "open Aqy1\u0394N36 is detrimental when overproduced in wild-type "
        "strains, suggesting that gating balances water flux for optimal "
        "freeze survival.",
}

for bi in data.get("biological_insights", []):
    title = bi.get("title", "")
    if title in insights_content:
        bi["content"] = insights_content[title]
        print(f"  Fixed: {title}")

# Write back using yaml.dump
with open(path, "w") as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

print(f"Saved {path.name}")
