---
title: SoPIP2;1 (Spinach Plasma Membrane Aquaporin)
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature04316]
verified: false
---

# SoPIP2;1 (Spinach Plasma Membrane Aquaporin)

## Overview

SoPIP2;1 is a plasma membrane intrinsic protein (PIP) from spinach (Spinacia oleracea) that functions as a water-selective channel in the cell plasma membrane. It is one of 13 well-conserved PIPs in the model plant Arabidopsis thaliana and belongs to the PIP2 subfamily. SoPIP2;1 forms tetramers with each monomer containing six transmembrane helices and two membrane-inserted non-membrane-spanning helices, following the conserved aquaporin hourglass architecture. The channel is regulated by phosphorylation and pH-dependent gating, where loop D acts as a hydrophobic gate that can cap or open the cytoplasmic pore entrance. This gating mechanism appears conserved throughout all plant plasma membrane aquaporins and enables plants to rapidly respond to environmental water stress.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature04316 | Pending | 2.1 A | I4 | Full-length SoPIP2;1 from Spinacia oleracea, expressed in Pichia pastoris | Cadmium ion (Cd2+) in closed conformation; no bound ligand in open conformation |
| doi/10.1038##nature04316 | Pending | 3.9 A | P21212 | His-tagged SoPIP2;1 from Spinacia oleracea, expressed in Pichia pastoris | No bound ligand |

## Expression and Purification

- **Expression system**: Pichia pastoris (methylotrophic yeast)
- **Construct**: Full-length SoPIP2;1; both His-tagged and non-tagged versions used

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Heterologous overexpression in Pichia pastoris | -- | -- + -- | Functional SoPIP2;1 overproduced as both His-tagged and non-tagged protein; reference 37 provides details |
| Purification | Purification and concentration (details in Supplementary Information) | -- | -- + -- | Purification protocol detailed in Supplementary Information of the source paper |


## Crystallization

### doi/10.1038##nature04316

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | Non-tagged SoPIP2;1 |
| Reservoir | 0.1 M Tris-HCl pH 8.0, 30% PEG 400, 0.1 M NaCl |
| Temperature | 4 C |
| Growth time | Few days |
| Cryoprotection | 0.1 M CdCl2 added to drop in 1:10 ratio |
| Notes | Closed conformation crystals; two molecules in asymmetric unit; Cd2+ added to improve crystal quality |

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | His-tagged SoPIP2;1 |
| Reservoir | 0.1 M sodium citrate pH 5.6, 30% PEG 400, 0.1 M NaCl |
| Temperature | 4 C |
| Growth time | Six months |
| Cryoprotection | Not specified |
| Notes | Open conformation crystals; four molecules in asymmetric unit; His-tagged protein showed significant water transport activity |


## Biological / Functional Insights

### Loop D hydrophobic gate mechanism in plant aquaporin gating

The most striking structural feature of SoPIP2;1 is the extended loop D, which is four to seven residues longer in PIP subfamily members compared to other aquaporin homologues. In the closed conformation, this extended loop folds underneath the aquaporin and caps the water pore from the cytosol. A key residue is the fully conserved Leu 197 of loop D, which inserts into a cavity near the channel entrance. Combined with His 99, Val 104, and Leu 108, Leu 197 creates a hydrophobic barrier blocking the pore. HOLE calculations establish that in the closed conformation, the pore narrows to a diameter of about 1.4 A at Leu 197 and further narrows to 0.8 A near Pro 195 and Val 194, severely restricting water passage. Two water molecules separated by 6.4 A are visible on either side of this hydrophobic gate. In the open conformation, loop D is displaced up to 16 A, and the N terminus of helix 5 extends an additional half-turn into the cytoplasm, displacing Leu 197, Pro 195, and Val 194 by 8.4, 13.9, and 15.0 A respectively. This movement opens the pore to more than 4 A diameter, allowing water flux.

### Phosphorylation-dependent gating via Ser 115 and Ser 274

SoPIP2;1 channel closure is triggered by dephosphorylation of two conserved serine residues. Ser 115 is located in the cytosolic loop B and is conserved as Ser in 12 of 13 Arabidopsis PIPs (Thr in one). Ser 274 is in the carboxy-terminal region and is fully conserved in all eight Arabidopsis PIP2s. Both residues are situated in consensus phosphorylation sites. In the closed conformation, Ser 115 forms a hydrogen bond to Glu 31, which ligates a divalent cation (Cd2+ in crystals, proposed Ca2+ in vivo). The simultaneous closure of all Arabidopsis PIPs upon anoxia depends on dephosphorylation of these residues. Molecular dynamics simulations of the phosphorylated protein showed a significant rearrangement in the conformation of amino acids coordinating the Ca2+ ion within 15 ns, with a partial opening of the gate mediated through displacement of loop D after phosphorylation of Ser 115 and Ser 274.

### pH-dependent gating via His 193 protonation

Protonation of a strictly conserved histidine residue in loop D (His 193 in SoPIP2;1) triggers channel closure following a drop in cytoplasmic pH due to anoxia during flooding. In the closed structure, His 193 adopts a specific conformation. At low pH when His 193 is protonated, a simple rotation of the histidine side chain would enable it to form a salt bridge to Asp 28 (conserved in PIPs as Asp or Glu). This would recover the hydrogen-bond-mediated anchor for loop D onto the N terminus that is lost when Ser 115 is phosphorylated. The structure of Ser 115-phosphorylated SoPIP2;1 at low pH is therefore expected to be similar to the closed conformation, with loop D capping the cytoplasmic side and Leu 197, Pro 195, and Val 194 effectively blocking the water channel.

### Divalent cation binding site anchors loop D in closed conformation

A divalent cation binding site was observed near loop D in the closed conformation structure. A heavy metal was assigned as Cd2+ based on anomalous difference density, and the addition of this ion improved crystal quality. A search for similar structural motifs revealed 13 PDB entries containing Ca2+, suggesting this site binds Ca2+ in vivo. The divalent cation is implicated in regulation because it anchors loop D through a network involving ionic interactions and hydrogen bonds onto a short alpha-helix of the N terminus, and is critical for defining the closed conformation. Specifically, Arg 190 and Asp 191 of loop D connect to Arg 118 (strictly conserved in PIPs) and Gly 30 through a hydrogen-bond network containing three water molecules. Arg 118 forms hydrogen bonds to Glu 31 (strictly conserved in PIPs), which ligates the cation. The divalent cation site coordinates residues including Asp 28, Glu 31, and Ser 115.

### Conservation of gating mechanism across plant plasma membrane aquaporins

The gating mechanism revealed by SoPIP2;1 structures appears conserved throughout all plant plasma membrane aquaporins. Tyr 149 of AQP0, which has been suggested to gate AQP0, overlays almost exactly with Leu 197 of SoPIP2;1. However, for AQP0 only one amino-acid residue blocks the pore, whereas several residues of loop D cap the channel in SoPIP2;1. The PIP subfamily members have a loop D that is typically four to seven residues longer than other aquaporin homologues, providing the extended gating apparatus. The conserved residues involved in gating include Ser 115, Ser 274, His 193, Leu 197, Arg 118, Glu 31, Asp 28, and Asp 191, which are all strictly or near-strictly conserved in PIPs.


## Cross-References

- [Aquaporin Family](/xray-mp-wiki/concepts/aquaporin/) — SoPIP2;1 is a plant plasma membrane aquaporin; shares the conserved hourglass architecture and NPA motif with all aquaporins
- [Aquaporin-1 (AQP1)](/xray-mp-wiki/proteins/aqp1/) — Bovine AQP1 used as molecular replacement model for SoPIP2;1 structure; structural comparison between animal and plant aquaporins
- [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) — Used for crystallizing both closed and open conformations of SoPIP2;1
- [Pichia pastoris Expression System](/xray-mp-wiki/methods/expression-systems/pichia-pastoris/) — SoPIP2;1 was heterologously expressed and overproduced in Pichia pastoris
- [Molecular Dynamics Simulation](/xray-mp-wiki/methods/structure-determination/molecular-dynamics-simulation/) — MD simulations of 15 ns duration performed on phosphorylated, non-phosphorylated, and induced open SoPIP2;1 tetramers embedded in POPE bilayer
- [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Tris-HCl pH 8.0 used as reservoir buffer for closed conformation crystallization
- [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) — Sodium citrate pH 5.6 used as reservoir buffer for open conformation crystallization
- [PEG 400 (Polyethylene Glycol 400)](/xray-mp-wiki/reagents/additives/peg-400/) — PEG 400 used as precipitant in both closed and open conformation crystallization
