---
title: SERCA1a E340A Mutant
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.2014896117]
verified: false
---

# SERCA1a E340A Mutant

## Overview

The [SERCA1a (Sarcoplasmic Reticulum Ca2+-ATPase)](/xray-mp-wiki/proteins/pumps-atpases/serca1a/) E340A mutant is a point mutant of the sarco(endo)plasmic reticulum
Ca2+-ATPase in which Glu340 (a conserved residue in the P1 helix at the interface
between the phosphorylation domain and transmembrane segments) is replaced by
alanine. Glu340 is strictly conserved among P-type ATPases and mediates interdomain
communication that guides Ca2+ transport. The crystal structure at 3.2 A resolution
reveals a rotated headpiece displaced ~10 A downward toward the membrane surface,
altered connectivity between the A and N domains, and loss of the electrostatic
interaction between Glu340 and Arg822 in the L6-7 loop. MD simulations support
stabilization of a more occluded Ca2+ state. The mutant displays ~25% WT ATPase
activity and ~3-fold slower Ca2+-binding kinetics due to delayed conformational
changes associated with the E2 to Ca2E1 transition.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.2014896117 |  | 3.2 | P2_1_2_1_2 | Rabbit [SERCA1a (Sarcoplasmic Reticulum Ca2+-ATPase)](/xray-mp-wiki/proteins/pumps-atpases/serca1a/) E340A mutant, Ca2E1 form with bound ATP analog ([AMPPCP](/xray-mp-wiki/reagents/ligands/amppcp/)) | 2 Ca2+ ions, [AMPPCP](/xray-mp-wiki/reagents/ligands/amppcp/), Mg2+ |

## Expression and Purification

- **Expression system**: Saccharomyces cerevisiae (yeast)
- **Construct**: [SERCA1a (Sarcoplasmic Reticulum Ca2+-ATPase)](/xray-mp-wiki/proteins/pumps-atpases/serca1a/) E340A mutant, 994 residues, with biotin acceptor domain linked to C-terminus by thrombin cleavage site
- **Notes**: Biotinylated in vivo in yeast; enables biotin-based affinity purification

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Biotin-based affinity purification | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) (biotin-streptavidin) | Streptavidin resin | 100 mM MOPS/Tris pH 6.8, 80 mM KCl, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1 mM CaCl2, 1 mM MgCl2 + [C12E8](/xray-mp-wiki/reagents/detergents/c12e8/) (octaethylene glycol dodecylether) | Same purification protocol as for wild-type [SERCA1a (Sarcoplasmic Reticulum Ca2+-ATPase)](/xray-mp-wiki/proteins/pumps-atpases/serca1a/) expressed in yeast |

**Final sample**: 8-10 mg/mL SERCA E340A in buffer with 10 mM CaCl2, 3 mM MgCl2, 1 mM [AMPPCP](/xray-mp-wiki/reagents/ligands/amppcp/)


## Crystallization

### doi/10.1073##pnas.2014896117

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | 8-10 mg/mL SERCA E340A supplemented with 10 mM CaCl2, 3 mM MgCl2, 1 mM [AMPPCP](/xray-mp-wiki/reagents/ligands/amppcp/), relipidated with [DOPC](/xray-mp-wiki/reagents/lipids/dopc/), solubilized in [C12E8](/xray-mp-wiki/reagents/detergents/c12e8/) |
| Reservoir | 200 mM lithium acetate, 18-22% PEG6K, 6-9% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 3% [tert-Butanol](/xray-mp-wiki/reagents/additives/tert-butanol/) |
| Mixing ratio | 1:1 |
| Temperature | 4 °C |
| Growth time | Not specified |
| Cryoprotection | [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) (6-9% in reservoir) |
| Notes | Crystals displayed rectangular stick morphology, markedly different from diamond-shaped WT crystals. Space group P2_1_2_1_2 with unit cell parameters (126 A, 232 A, 50 A; 90°, 90°, 90°). Data collected at ESRF microfocus beam line ID23-2. Resolution 3.2 A. Phased by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using Ca2E1-[AMPPCP](/xray-mp-wiki/reagents/ligands/amppcp/) structure (1T5S).
 |


## Biological / Functional Insights

### Glu340 is a key mediator of interdomain communication in SERCA

Glu340 is located centrally in the P1 helix (Pro337-Cys344) at the interface
between the phosphorylation domain and the cytosolic ends of M3 through M7.
It is almost universally conserved throughout the P-type ATPase superfamily.
The E340A mutation causes a stabilization of the Ca2+ sites in a more occluded
state, displaying slowed dynamics. The mutated residue disrupts communication
between the headpiece and the Ca2+-binding transmembrane region.

### E340A causes global domain rearrangements with rotated headpiece

The crystal structure of E340A (3.2 A) shows a pronounced ~10 A downward
rotation of the cytosolic headpiece toward the membrane surface compared to
WT (PDB 3N8G). The A domain loses >50% of its contacts with the N domain.
The P1 helix moves closer to M3, and the hydrogen bond network around residue
340 is completely altered — the electrostatic interaction between Glu340 and
Arg822 (L6-7 loop) is lost, replaced by hydrophobic contacts (Ala340 to
Leu249, Pro337 to Thr247 methyl group, Thr341 to Pro248). MD simulations
at 200 ns in [POPC](/xray-mp-wiki/reagents/lipids/popc/) bilayers confirm these structural changes persist in a
dynamic membrane environment.

### MD simulations reveal altered dynamics and stabilization of occluded Ca2+ state

All-atom MD simulations (3 x 200 ns) of WT, E340A, and in silico E340A_is
in [POPC](/xray-mp-wiki/reagents/lipids/popc/) bilayers revealed: (1) E340A maintains a more acute headpiece angle
(142° vs 146° for WT); (2) the P1 helix stays closer to M3 tip (Leu249);
(3) Arg822 swings out irreversibly from the wedge between P1 and M3 to a
stable "out" position, allowing Leu249 to close in; (4) the M1 helix becomes
rigidly kinked (less flexible than WT), consistent with a shift toward a more
occluded state. The rigidification of the M1 kink and narrow clustering of
phosphorylation site geometry around catalytically competent values support
stabilization of a more occluded conformation.

### Functional impairment arises from slowed Ca2+-binding kinetics

The E340A mutant displays ~25% WT ATPase activity (0.86 vs 3.45 umol
ATP/mg/min). The Ca2+-binding transition (H_nE2 -> E1 -> Ca2E1) monitored
by tryptophan fluorescence is ~3-fold slower (t1/2 = 4.5 s for E340A vs
1.6 s for WT, P = 0.0023). The slowing is attributed to inhibition of the
actual Ca2+-binding step rather than earlier E2-E1 equilibrium shifts,
consistent with previous COS cell studies showing no effect on vanadate
affinity. The mutation does not significantly affect other partial reactions
(phosphorylation, Ca2E1P -> E2P transition, or E2P dephosphorylation).

### M1 helix rigidification and link to Ca2+ occlusion

MD simulations show a rigidly kinked M1 helix in E340A compared to WT,
where the kink at Leu60 permits Phe57 to engage in a hydrophobic cluster
that shields Ca2+-binding sites for ion occlusion. A straight M1 helix is
associated with unoccluded Ca2E1 states. The rigidification correlates with
narrow clustering of phosphorylation site geometry (Asp351, ATP gamma-phosphate,
Mg2+) around catalytically competent values, consistent with stabilization
of a conformation resembling the occluded transition state.


## Cross-References

- [SERCA1a (Sarcoplasmic Reticulum Ca2+-ATPase)](/xray-mp-wiki/proteins/pumps-atpases/serca1a/) — Wild-type parent protein; structural and functional comparison
- [SERCA1a E309Q Mutant](/xray-mp-wiki/proteins/pumps-atpases/serca1a-e309q/) — Related SERCA1a point mutant; comparison of domain rearrangement effects
- [P-type ATPase Mechanism](/xray-mp-wiki/concepts/p-type-atpase-mechanism/) — E340A mutation reveals critical role of Glu340 in interdomain communication within the P-type ATPase transport cycle
- [Large Domain Motion in P-type ATPases](/xray-mp-wiki/concepts/large-domain-motion-in-p-type-atpases/) — E340A structure visualizes altered headpiece positioning and A-domain displacement
- [Phosphoenzyme E2P State](/xray-mp-wiki/concepts/phosphoenzyme-e2p-state/) — Glu340 is located at P-domain interface near phosphorylation site Asp351
- [AMPPCP](/xray-mp-wiki/reagents/ligands/amppcp/) — ATP analog used during crystallization and functional assays
- [Calcium Chloride](/xray-mp-wiki/reagents/additives/calcium-chloride/) — Essential substrate; two Ca2+ ions bound in transmembrane domain
- [Magnesium Chloride](/xray-mp-wiki/reagents/additives/magnesium-chloride/) — Cofactor; Mg2+ required for ATP binding and crystallization
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — E340A mutation alters the E2 to Ca2E1 transition kinetics
- [Molecular Dynamics Simulation](/xray-mp-wiki/methods/structure-determination/molecular-dynamics-simulation/) — MD simulations (3 x 200 ns in POPC bilayers) confirmed structural observations and revealed altered dynamics
