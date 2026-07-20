---
title: "Inward Rectification in Potassium Channels"
created: 2026-06-16
updated: 2026-06-16
type: concept
category: concepts
layout: default
tags: [concept-functional, membrane-protein, subdirectory-transport-mechanisms]
sources: [doi/10.1126##science.1180310, doi/10.1038##nrn727]
verified: none
---

# Inward Rectification in Potassium Channels

## Overview
Inward rectification is the property of certain potassium channels (Kir channels) to conduct K+ ions more efficiently into the cell than out of the cell, despite equal but opposite electrochemical driving forces. This diode-like behavior arises from voltage-dependent pore blockage by intracellular multivalent cations, especially Mg2+ and polyamines (spermidine, spermine, putrescine). Inward rectifiers are critical for setting the resting membrane potential in electrically excitable cells while preventing dissipation of the K+ gradient during action potentials.


## Mechanism/Details
The mechanism of inward rectification was elucidated through combined electrophysiological and structural studies, culminating in the Kir2.2 crystal structure (Science 2009).

**Voltage-dependent pore block.** At hyperpolarizing (negative) membrane potentials, intracellular blocking ions (Mg2+, polyamines) are cleared from the pore, allowing K+ to conduct. At depolarizing (positive) potentials, these blocking ions are driven into the pore from the cytoplasm, occluding the conduction pathway. This produces the characteristic diode-like current-voltage relationship.

**Ion binding sites.** The Kir2.2 structure (PDB 3JYC) revealed multiple ion binding sites on the intracellular side of the selectivity filter that can be occupied by conducting ions (K+, Rb+) but exhibit higher affinity for multivalent blocking ions (Mg2+, Sr2+, polyamines):

1. **The central cavity** (D173 in Kir2.2): A ring of four aspartate residues that attracts cations through strong electrostatic interactions. In strong rectifiers, these are Asp; in weak rectifiers (e.g., Kir1.1, Kir6.1), they are Asn.

2. **The upper ring of charges** (E225 and E300): Two concentric rings of acidic residues in the cytoplasmic domain, creating the most electronegative site. This site binds trivalent Eu3+ and shows the strongest Sr2+ peak.

3. **The lower ring of charges** (D256): Located at the entryway of the cytoplasmic pore, providing additional electrostatic attraction for blocking ions.

**Competition mechanism.** Conducting ions (K+) and blocking ions (Mg2+, polyamines) compete for these binding sites. High extracellular K+ favors occupation by conducting ions, shifting the voltage at which block occurs to more depolarized values. As blocking ions enter the pore from the intracellular side, displaced conducting ions must move through the selectivity filter to the extracellular side. This coupling generates the steep voltage dependence characteristic of strong rectifiers, as the blocking ion experiences not only its own charge moving through the membrane field but also the charge of displaced ions.

**Structural basis for strong vs. weak rectification.** Strong rectifiers (Kir2 subfamily) have Asp at the cavity position (D173) and maintain tight electrostatic interactions with blocking ions. Weak rectifiers (Kir1.1, Kir6.1) have Asn at this position, producing a weaker electrostatic sink. The Kir2.2 structure also revealed hydrophobic residues at positions I177 and M181 on the inner helices that form a hydrophobic seal, which may interact with the methylene groups of polyamine blockers to further stabilize the blocked state.

**Cooperativity between sites.** Mutagenesis studies have confirmed that mutations at D173, E225, E300, and D256 all affect Mg2+ and polyamine affinity. The multiple binding sites along the pore create a distributed electrostatic field that captures blocking ions entering from the cytoplasm and stabilizes them across the length of the pore.


## Examples in Membrane Protein Work
- [Kir2.2](/xray-mp-wiki/proteins/voltage-gated-channels/kir2-2-channel/) — Crystal structure revealed the structural basis for inward rectification with D173 in the cavity, E225/E300 at the upper ring, and D256 at the lower ring of charges
- [KirBac](/xray-mp-wiki/proteins/voltage-gated-channels/kirbac-potassium-channels/) — Prokaryotic Kir channels lack the specific amino acids that confer inward rectification in eukaryotic channels

## Related Concepts
- []() — The selectivity filter determines which ions enter the pore; inward rectification controls the direction of permitted flow
- []() — Inward rectification appears as voltage-dependent gating but is actually voltage-dependent block by intracellular cations

## Cross-References
- [Chicken Kir2.2 Inward Rectifier K+ Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kir2-2-channel/) — The crystal structure that revealed the structural basis for inward rectification
- [KirBac Potassium Channels](/xray-mp-wiki/proteins/voltage-gated-channels/kirbac-potassium-channels/) — Prokaryotic Kir channels used for structural comparison
