---
title: NavMs Sodium Channel
created: 2026-05-28
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.molcel.2020.12.048, doi/10.1038##ncomms2077, doi/10.1038##ncomms3465, doi/10.1038##ncomms14205]
verified: false
---

# NavMs Sodium Channel

## Overview

NavMs is a prokaryotic voltage-gated sodium channel (NaV) from Magnetococcus marinus. NavMs is a homotetramer where each subunit contains a voltage-sensing module (VSM, S0-S4) and a pore module (PM, S5-P-S6). It serves as a particularly good exemplar for human NaV pharmacology in terms of drug potency, mechanism of drug inhibition, and receptor site interactions. This paper reports the highest-resolution complete NavMs structure (2.45 A) in a fully open conformation, with all three domains — voltage sensor, pore, and C-terminal domain — visible simultaneously.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms2077 | 4F4L | 3.49 A | C2 | NavMs pore-only construct (transmembrane helices S5-P-S6, residues M130-H237); homotetramer; open-channel conformation with splayed S6 helices | None (apo structure); water molecules modeled at selectivity filter |
| doi/10.1038##ncomms3465 | 3ZJZ | 2.9 A | C2221 | NavMs pore with full-length CTD; homotetramer of VSM-PM subunits; open pore conformation; two crystallographically distinct tetramers in asymmetric unit | None (apo structure); 394 ligand/ion atoms in asymmetric unit |
| doi/10.1016##j.molcel.2020.12.048 | 6SX5 | 2.2 A | N/A | NavMs L F208L mutant (phenylalanine to leucine substitution at position 208); homotetramer of VSM-PM subunits; apo form | None (apo structure) |
| doi/10.1016##j.molcel.2020.12.048 | 6SXF | 2.2 A | N/A | NavMs L F208L mutant; homotetramer; complex with [Tamoxifen](/xray-mp-wiki/reagents/ligands/tamoxifen/) | [Tamoxifen](/xray-mp-wiki/reagents/ligands/tamoxifen/) (4 copies bound in inner and outer sites) |
| doi/10.1016##j.molcel.2020.12.048 | 6SXG | 2.2 A | N/A | NavMs L F208L mutant; homotetramer; complex with [4-Hydroxytamoxifen](/xray-mp-wiki/reagents/ligands/4-hydroxytamoxifen/) | [4-Hydroxytamoxifen](/xray-mp-wiki/reagents/ligands/4-hydroxytamoxifen/) (4 copies bound in inner and outer sites) |
| doi/10.1016##j.molcel.2020.12.048 | 6SXC | 2.2 A | N/A | NavMs L F208L mutant; homotetramer; complex with [4-Hydroxytamoxifen](/xray-mp-wiki/reagents/ligands/4-hydroxytamoxifen/) | [4-Hydroxytamoxifen](/xray-mp-wiki/reagents/ligands/4-hydroxytamoxifen/) (8 copies bound — inner and outer sites) |
| doi/10.1016##j.molcel.2020.12.048 | 6SXE | 2.2 A | N/A | NavMs L F208L mutant; homotetramer; complex with [N-Desmethyltamoxifen](/xray-mp-wiki/reagents/ligands/n-desmethyltamoxifen/) | [N-Desmethyltamoxifen](/xray-mp-wiki/reagents/ligands/n-desmethyltamoxifen/) (4 copies bound in inner and outer sites) |
| doi/10.1016##j.molcel.2020.12.048 | 6Z8C | 2.2 A | N/A | NavMs L F208L mutant; homotetramer; complex with [Endoxifen](/xray-mp-wiki/reagents/ligands/endoxifen/) | [Endoxifen](/xray-mp-wiki/reagents/ligands/endoxifen/) (4 copies bound in inner and outer sites) |
| doi/10.1016##j.molcel.2020.12.048 | 6SX7 | 2.2 A | N/A | NavMs L F208L mutant; homotetramer; complex with [Endoxifen](/xray-mp-wiki/reagents/ligands/endoxifen/) | [Endoxifen](/xray-mp-wiki/reagents/ligands/endoxifen/) (4 copies bound in inner and outer sites) |
| doi/10.1038##ncomms14205 | 5HVX | 2.45 A | I4122 | Full-length NavMs wild type; homotetramer of VS-S4-S5 linker-pore-CTD subunits; activated voltage sensor conformation; open selectivity filter with three sodium ions; open activation gate at intracellular membrane surface; complete structure with all three domains visible | Three sodium ions per subunit in selectivity filter |
| doi/10.1038##ncomms14205 | 5HVD | 2.60 A | I4122 | Full-length NavMs I218C mutant; homotetramer; activated voltage sensor conformation; open selectivity filter; open activation gate; used for comparison with [NAVAB](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) structure (I217C equivalent mutation) | Three sodium ions per subunit in selectivity filter |

## Expression and Purification

No purification described.

## Crystallization

No crystallization described.

## Biological / Functional Insights

### Novel gating hinge mechanism at Thr209 in S6

Comparison of the open NavMs pore structure (PDB 4F4L) with the closed [NAVAB](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) pore reveals a new gating mechanism for bacterial sodium channels. Opening is enabled by a simple rotation around the backbone angle of Thr209 in the middle of the S6 helix, which swings the lower half of S6 away from the central pore axis. This splaying opens the cytoplasmic activation gate to a diameter sufficient for hydrated sodium ions (~7.8 A) to pass through. Unlike the iris-like twist proposed for potassium channels and nicotinic [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine/) receptors, sodium channel gating involves a bending motion at a single residue, with minimal displacement of the S5 helices. The selectivity filter remains structurally unchanged between open and closed states, demonstrating that the activation gate is structurally uncoupled from the filter. Fenestrations in the transmembrane region are considerably larger in the open state, with implications for state-dependent drug binding.

### C-terminal domain structure and gating mechanism

The CTD of NavMs includes a flexible linker region (residues 222-239) connecting the transmembrane pore to a four-helix coiled-coil bundle (residues 240-270). The coiled-coil domain couples inactivation with channel opening and is enabled by negatively charged residues (E229, E230, E231) in the linker region. Deletion of the linker region (Delta223) slows inactivation ~7-fold and recovery from inactivation ~155-fold. EEE to QQQ mutation of the linker glutamates slows inactivation ~5-fold. The EPR-derived structure shows the CTD is dynamic but not fully disordered, consistent with the lack of defined density in the crystal electron density map of PDB 3ZJZ.

### Novel tamoxifen binding site at the intracellular gate

[Tamoxifen](/xray-mp-wiki/reagents/ligands/tamoxifen/) and its metabolites ([4-Hydroxytamoxifen](/xray-mp-wiki/reagents/ligands/4-hydroxytamoxifen/), [N-Desmethyltamoxifen](/xray-mp-wiki/reagents/ligands/n-desmethyltamoxifen/), [Endoxifen](/xray-mp-wiki/reagents/ligands/endoxifen/)) bind at the intracellular exit of the NavMs ion-conducting pore. Two distinct binding sites were identified: an "inner" site closer to the ion-conducting pathway and an "outer" site near the intracellular C-terminal portion. Up to eight copies of a drug can bind simultaneously (four inner and four outer, one per subunit). The inner site involves hydrogen bonds with M222 (intracellular gate residue), K226, and E227. Binding to the inner site narrows the pore radius from 2.3 A (open state) to 1.4 A.

### Conformational changes upon drug binding

Compared with the apo-NavMs open state, the C-terminal ends (starting at I224) of the S6 helices in drug-bound NavMs are displaced toward the center of the ion-conducting pathway (RMSD of 1.2 A). The S4 helices in the VSMs remain in the "up" position and the PMs adopt a narrow, non-conductive conformation. The drug-bound structures may represent either the "pre-open" or "inactivated" state.

### Structural similarity to estrogen receptor binding pocket

The [Tamoxifen](/xray-mp-wiki/reagents/ligands/tamoxifen/) binding pocket in NavMs shares geometric features with the estrogen receptor (ER) binding pocket. Both pockets feature hydrogen bonds with an aspartic acid at one end (D220 in NavMs, D351 in ER) and a glutamate at the other (E227 in NavMs, E353 in ER). This similarity may explain the off-target sodium channel effects of [Tamoxifen](/xray-mp-wiki/reagents/ligands/tamoxifen/) and its derivatives in cancer cells.

### Mechanism of sodium channel inhibition

[4-Hydroxytamoxifen](/xray-mp-wiki/reagents/ligands/4-hydroxytamoxifen/) inhibits sodium channels by stabilizing the non-conducting inactivated state rather than directly blocking the pore. The onset of inhibition (tau_on) and recovery (tau_off) were 16 and 765 times slower, respectively, than the pore-blocking metal ion cadmium. Recovery from inactivation showed a ~10-fold delay following drug treatment. Inhibition is use-dependent, requiring channel entry into the inactivated state.

### Conservation in human sodium channels

The [Tamoxifen](/xray-mp-wiki/reagents/ligands/tamoxifen/) receptor residues in NavMs (D220, E227, M222, K226) are conserved in domains III and IV of human Na_v1.2. The NavMs F208L mutant was examined because the equivalent residues in two domains of human NaVs are phenylalanine and in two domains are leucine, making NavMs_L a more representative model for human channel pharmacology.

### Activated open-state structure with complete domains

The 2.45 A resolution structure (5HVX) is the first complete NavMs structure with all three domains — voltage sensor, pore, and C-terminal domain — visible simultaneously. It displays a canonical activated conformation of the S4 voltage sensor helix, an open selectivity filter with three sodium ions, and an open activation gate formed by the S6 helices at the intracellular membrane surface. The structure was obtained from crystals formed under zero potential conditions consistent with an open-channel state. This is the highest-resolution sodium channel structure determined to date.

### S4-S5 linker as activation lever

The S4-S5 linker acts as a mechanical lever between the voltage sensor and pore domains. Activation of the voltage sensor produces a large shift in the C-terminal end of the linker where it meets the S5 helix of the pore domain. This lever action shifts the positions of S5 and S6 helices, thereby opening the gate. The interaction motif involving W77 of S3, the S4-S5 linker (R118, Q122), and the C-terminal EEE motif (E229, E230, E231) stabilizes the open state and regulates gate opening/closing.


## Cross-References

- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Solubilization detergent used for membrane extraction
- [Tris Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component in purification (20 mM Tris, pH 7.5)
- [NavAb Bacterial Voltage-Gated Sodium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) — Structural comparison between activated open and pre-activated states
- [NavAe1p Prokaryotic Sodium Channel Pore](/xray-mp-wiki/proteins/gpcr/navae1p-sodium-channel/) — Closed-state comparison for CTD domain analysis
- [NaChBac Bacterial Voltage-Gated Sodium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/nachbac/) — Founding member of voltage-gated sodium channel family
- [Sodium Channel Gating and Selectivity](/xray-mp-wiki/concepts/sodium-channel-gating/) — General voltage-gating mechanism overview
- [Sodium Channel Inactivation Gating](/xray-mp-wiki/concepts/sodium-channel-inactivation-gating/) — CTD-mediated inactivation mechanism in prokaryotic sodium channels
- [S4-S5 Linker Interaction Motif](/xray-mp-wiki/concepts/s4-s5-linker-interaction-motif/) — Central structural finding of this paper
- [4-Hydroxytamoxifen](/xray-mp-wiki/reagents/ligands/4-hydroxytamoxifen/) — Related ligand or cofactor
- [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine/) — Related ligand or cofactor
