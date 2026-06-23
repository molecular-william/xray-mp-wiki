---
title: "Ci-VSD Voltage-Sensing Domain"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.2768]
verified: false
---

# Ci-VSD Voltage-Sensing Domain

## Overview

Ci-VSD is the isolated voltage-sensing domain from the Ciona intestinalis voltage-sensing phosphatase (Ci-VSP). It contains the S1-S4 transmembrane segments that form the voltage-sensing module responsible for detecting changes in membrane potential. Crystal structures of both wild-type Ci-VSD (3.6 A) and the R217E mutant (2.5 A) reveal the structural basis of voltage-dependent gating, including the rotameric reorientation of gating arginine residues. The structures were refined using extended Molecular Dynamics Flexible Fitting (xMDFF), a method that integrates X-ray crystallography with molecular dynamics simulations to improve low-resolution structures. Ci-VSD was co-crystallized with Fab fragments and contains [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) detergent molecules at the S3-S4 loop region.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nsmb.2768 | 4G7V | 2.5 | P6_5 2 2 | Ci-VSD R217E mutant in complex with Fab fragment 33F12_4, 12 complexes (6 homodimers) in unit cell | [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) (3 molecules), succinic acid (1 molecule) |
| doi/10.1038##nsmb.2768 | 4G7V | 3.6 | P1 | Ci-VSD wild-type (residues 1-260) in complex with Fab fragment 39D10_18, 4 complexes (2 dimers) per asymmetric unit | none (apo structure) |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Ci-VSD (residues 1-260) from Ciona intestinalis, expressed with Fab co-expression for crystallization

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Complex purification | Co-purification with Fab fragments | Not specified | Not specified + [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) | Ci-VSD co-expressed and co-purified with Fab fragments 33F12_4 (R217E) or 39D10_18 (WT) |


## Crystallization

### doi/10.1038##nsmb.2768

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Notes | Ci-VSD R217E+33F12_4 complex crystallized in space group P6_5 2 2 at 2.5 A resolution. Ci-VSD WT+39D10_18 complex crystallized in space group P1 at 3.6 A resolution with 4 complexes per asymmetric unit. [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) detergent molecules and succinic acid resolved around the S3-S4 loop region of the R217E structure. |


## Biological / Functional Insights

### Gating arginine rotameric reorientation

The four gating arginine residues (R223, R226, R229, R232) in Ci-VSD show a distinct span of rotamer orientations. R229 lies horizontally inside the hydrophobic gasket, separating the intracellular and extracellular sides electrically. R223 and R226 point straight up above the electric field, while R232 points down below the electrical field. This rotameric reorientation mechanism is also observed in other VSDs ([KvAP Voltage-Dependent Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kvap/), Kv1.2-2.1 chimera, NavAb) and may be an additional contributor to total gating charge translocation in VSDs.

### xMDFF refinement methodology

Extended Molecular Dynamics Flexible Fitting (xMDFF) was developed as a method to iteratively refine atomic models into low-resolution electron density maps. The method cycles between X-ray crystallography refinement (using PHENIX) and MDFF fitting, using steering forces derived from the X-ray electron density. xMDFF was benchmarked on six low-resolution X-ray structures (4-4.5 A resolution: 1AV1, 1YE1, 1JL4, 1AOS, 1XDV, 1Y15) and showed significant improvements in R-free values, MolProbity scores, and Ramachandran favored conformations.

### S4 helix conformation and gating model

The S4 helix in the Ci-VSD WT structure is well resolved, including the gating arginines and the S4-phosphatase linker. The electron density supports the conformation observed rather than a hypothetical "two-click down" model (shifting S4 3 residues downward) or an "up-conformation" model (shifting S4 upward). The S3-S4 loop length and linker density are consistent with the resting/down conformation of the voltage sensor.

### Hydrophobic gasket and counter-charge interactions

The hydrophobic gasket residues and counter-charge residues (E205, F199) form a conserved interaction network around the gating arginines. F199 and Y200 are part of the hydrophobic constriction site that separates intracellular and extracellular compartments in the voltage sensor.


## Cross-References

- [Voltage-Sensor Paddle](/xray-mp-wiki/concepts/construct-design/voltage-sensor-paddle/) — Ci-VSD contains the conserved voltage-sensor paddle motif (S3b-S4)
- [KvAP Voltage-Dependent Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kvap/) — KvAP voltage sensor compared to Ci-VSD for rotamer analysis
- [NavAb Bacterial Voltage-Gated Sodium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) — NavAb structure compared to Ci-VSD for gating charge translocation
- [GR (Halobacterium sp. GR Bacteriorhodopsin)](/xray-mp-wiki/proteins/rhodopsins/gr/) — Related protein structure
- [KvAP Voltage-Dependent Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kvap/) — Related protein structure
- [NavAb Bacterial Voltage-Gated Sodium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) — Related protein structure
- [RibU (ECF-Type Riboflavin Transporter S Component from Staphylococcus aureus)](/xray-mp-wiki/proteins/pumps-atpases/ribu/) — Related protein structure
- [X-ray Crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/) — Method used in the study
- [Voltage-Sensor Paddle](/xray-mp-wiki/concepts/construct-design/voltage-sensor-paddle/) — Related concept
- [Lauryldimethylamine N-oxide (LDAO)](/xray-mp-wiki/reagents/detergents/ldao/) — Reagent used in the study
