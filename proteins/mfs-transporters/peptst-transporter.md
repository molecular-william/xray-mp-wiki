---
title: PepTSt Peptide Transporter from Streptococcus thermophilus
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1371##journal.pone.0173126]
verified: false
---

# PepTSt Peptide Transporter from Streptococcus thermophilus

## Overview

PepTSt is a proton-dependent oligopeptide transporter (POT) from the Major Facilitator Superfamily (MFS) found in Streptococcus thermophilus. It mediates the uptake of di- and tripeptides and is a bacterial homolog of the human intestinal peptide transporters PepT1 and PepT2. Crystal structures have been determined in three different crystal forms (P2_12_12_1, C222_1, and P3_121), all capturing inward facing conformations. The P3_121 form reported here was crystallized using the short-chain detergent n-Nonyl-β-D-maltopyranoside (NM) and the MIRAS phasing method, revealing a monomeric inward facing state with the TM10-TM11 lobe bent toward the central pore, suggesting an inward facing occluded or intermediate conformation. PepTSt consists of 14 transmembrane helices (TM1-TM12 forming the canonical MFS N- and C-domains, plus TM-A and TM-B in the linker region).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1371##journal.pone.0173126 | 5MMT | 3.4 A | P3_1_21 | C-terminally hexahistidine-tagged wild-type PepTSt (Ce27) from Streptococcus thermophilus. Expressed in E. coli C41. Purified in NM (n-Nonyl-β-D-maltopyranoside) detergent. | Penicillin G (present in protein sample, not identified in electron density) |
| doi/10.1371##journal.pone.0173126 | 4APS | 3.3 A | P2_1_2_1_2_1 | C-terminally hexahistidine-tagged PepTSt |  |
| doi/10.1371##journal.pone.0173126 | 4D2C | 2.3 A | C222_1 | C-terminally hexahistidine-tagged PepTSt | Dipeptide |
| doi/10.1371##journal.pone.0173126 | 4D2B |  | C222_1 | C-terminally hexahistidine-tagged PepTSt |  |
| doi/10.1371##journal.pone.0173126 | 4D2D |  | C222_1 | C-terminally hexahistidine-tagged PepTSt | Tripeptide |
| doi/10.1371##journal.pone.0173126 | 5D58 |  | C222_1 | C-terminally hexahistidine-tagged PepTSt | Dipeptide |
| doi/10.1371##journal.pone.0173126 | 5D59 |  | C222_1 | C-terminally hexahistidine-tagged PepTSt | Dipeptide |

 - R-work 26.5%, R-free 28.6%

## Expression and Purification

- **Expression system**: [E. coli C41](/xray-mp-wiki/methods/expression-systems/e-coli-expression)
- **Construct**: C-terminally hexahistidine-tagged wild-type PepTSt (Ce27)
- **Notes**: Protein expressed in E. coli C41 cells. For SeMet labeling, protein was expressed in minimal medium supplemented with SeMet according to established protocols. Two mutant variants were prepared for phasing: L226M and F338M.

### Purification Workflow

- **Expression system**: E. coli C41
- **Expression construct**: C-terminally hexahistidine-tagged PepTSt (Ce27)
- **Tag info**: C-terminal 6xHis tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane solubilization | Detergent solubilization | -- | Buffer with 1% detergent + DDM, DM, or NM at 1% | Four detergents tested: LMNG, DDM, DM, NM. For NM, protein was purified in DM up to IMAC step, then exchanged to NM in SEC step. |
| [IMAC](/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | IMAC resin | Buffer with appropriate detergent + DDM (0.03%), DM (0.2%), NM (0.4%), or LMNG (0.01%) | Elution by passing TEV protease over beads to cleave His tag |
| [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | SEC column | Buffer with appropriate detergent + As above | Final purification step to obtain monodisperse PepTSt |


## Crystallization

### doi/10.1371##journal.pone.0173126

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion (in surfo) |
| Protein sample | PepTSt at 5-10 mg/mL purified in NM |
| Reservoir | 0.05 M HEPES pH 8.0, 30% PEG550 MME, 1.2% Fos-Choline 10 |
| Temperature | 277 K (4 C) |
| Growth time | Not specified |
| Cryoprotection | Crystals flash frozen in liquid nitrogen without prior cryobuffer soaking |
| Notes | Initial hits in 96-well sitting-drop plates. Scaling up to 24-well format was not found beneficial. Fos-Choline-10 additive significantly improved diffraction. Native crystals diffracted to 3.4 A maximum resolution with severe anisotropy. Data truncated and scaled anisotropically. MIRAS phasing using SeMet (F338M mutant) and KAu(CN)2 derivative. |


## Biological / Functional Insights

### MFS transporter with 14 transmembrane helices

PepTSt contains 14 transmembrane helices in total. TM1-TM6 form the N-terminal MFS domain (N-domain), TM7-TM12 form the C-terminal MFS domain (C-domain), and the last two helices (TM-A and TM-B) are found in the linker region between the two domains, adopting a V-shaped arrangement. This architecture is characteristic of bacterial PepT/POT transporters.

### P3_121 crystal form revealed monomeric inward facing state

The P3_121 crystal form of PepTSt (PDB 5MMT) was crystallized in NM detergent, which disrupts the dimeric form observed in longer-chain detergents like DDM and LMNG. The protein adopts an inward facing conformation where lobe TM10-TM11 is markedly bent toward the central pore, likely occluding the binding site. The extent of occlusion could not be determined due to disorder at the apex of the lobe. The structure reveals a monomeric state, important for future spectroscopic studies where dimeric forms would complicate data interpretation.

### A-motif and TM-A/TM-B functional roles

The A-motif in PepTSt (found in loop TM2-TM3) differs from the consensus MFS sequence by having an extra residue inserted prior to the second conserved glycine and often missing one or more basic residues. The salt bridge normally found between the second basic residue and the acidic residue in TM4 is absent in PepTSt, suggesting that regulated bending of TM4 may not take place in this transporter. Instead, bending of lobe TM10-TM11 appears to be the primary mechanism for forming the inward facing occluded state, possibly in combination with domain rotation and changes in TM4-TM5 and TM-A/TM-B.

### Crystal packing and diffraction anisotropy

The P3_121 and P2_12_12_1 crystal forms both exhibit ordered end-to-end packing through periplasmic-periplasmic and cytoplasmic-cytoplasmic interactions, with a complete lack of ordered lateral contacts. This manifests as severe diffraction anisotropy, with the directions of reflection intensity falloff correlating with directions where ordered packing interactions are missing. The C222_1 form, crystallized in meso, encompasses tight lateral interactions and diffracted to much better resolution (2.3 A isotropic).


## Cross-References

- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/protein-families/major-facilitator-superfamily/) — PepTSt is a member of the MFS transporter family
- [Conformational Dynamics in MFS Transporters](/xray-mp-wiki/concepts/transport-mechanisms/conformational-dynamics-mfs/) — PepTSt exhibits inward facing conformations relevant to MFS transport dynamics
- [Inward Facing Occluded State in MFS Transporters](/xray-mp-wiki/concepts/transport-mechanisms/inward-facing-occluded-mfs-state/) — The P3_121 form represents a potential inward facing occluded state
- [Rocker-Switch Mechanism](/xray-mp-wiki/concepts/structural-mechanisms/rocker-switch-mechanism/) — Canonical transport mechanism for MFS transporters
- [Cork-in-Bottle Occlusion](/xray-mp-wiki/concepts/structural-mechanisms/cork-in-bottle-occlusion/) — Alternative occlusion mechanism for membrane transporters
