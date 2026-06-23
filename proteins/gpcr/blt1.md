---
title: Leukotriene B4 Receptor 1 (BLT1) — Guinea Pig and Human
created: 2026-06-03
updated: 2026-06-09
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nchembio.2547, doi/10.1038##s41467-021-23149-1]
verified: false
---

# Leukotriene B4 Receptor 1 (BLT1) — Guinea Pig and Human

## Overview

The leukotriene B4 receptor 1 (BLT1) is a class A G protein-coupled receptor that mediates the biological effects of leukotriene B4 (LTB4), a potent inflammatory lipid mediator. BLT1 is primarily expressed on leukocytes and plays a central role in inflammatory and immune responses. The first crystal structure of BLT1 was determined for a thermostabilized guinea pig construct in complex with the antagonist BIIL260 (PDB 5X33, 3.7 A), revealing a novel sodium ion-mimicking mechanism by which the [Benzamidine](/xray-mp-wiki/reagents/additives/benzamidine) moiety of BIIL260 stabilizes the inactive state of the receptor. Subsequently, the human BLT1 (hBLT1) crystal structure was determined in complex with the selective antagonist MK-D-046 (PDB 7K15, 2.9 A), developed for the treatment of type 2 diabetes and other inflammatory conditions. The hBLT1 structure, combined with site-directed mutagenesis, structure-activity relationship (SAR) analysis, and docking studies, revealed molecular determinants of ligand binding and selectivity toward different BLT receptor subtypes and across species, and identified a putative membrane-buried ligand access channel. 

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nchembio.2547 | 5X33 | 3.7 A | Not specified | Thermostabilized guinea pig BLT1 mutant lacking residues 1-14, with H83G/K88G/V212A/S309A mutations, fused with [T4 Lysozyme](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme) (T4L) at intracellular loop 3 (construct ICL3-10)  | [BIIL260](/xray-mp-wiki/reagents/ligands/biil260) |
| doi/10.1038##s41467-021-23149-1 | 7K15 | 2.9 A | P 21 2 21 | Human BLT1 (hBLT1) with N-terminal residues 1-4 and C-terminal residues 311-352 truncated, flavodoxin fusion in ICL3 between residues 212 and 213, and five thermostabilizing point mutations (L1063.41W, S1163.51Y, A1965.53I, C2877.55F, S310A) | [MK-D-046](/xray-mp-wiki/reagents/ligands/mk-d-046) (selective antagonist) |

## Expression and Purification

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | [Pichia pastoris](/xray-mp-wiki/organisms/pichia-pastoris) stable expression | — | BMGY medium (1% yeast extract, 2% peptone, 100 mM potassium phosphate pH 6.0, 1.34% yeast nitrogen base, 1% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol)) at 30 C | BLT1-T4L construct expressed in P. pastoris (pPIC3.5K vector) |
| Induction | BMMY medium induction with [Methanol](/xray-mp-wiki/reagents/additives/methanol) | — | BMMY medium (1% yeast extract, 2% peptone, 100 mM potassium phosphate pH 6.0, 1.34% yeast nitrogen base, 0.5% [Methanol](/xray-mp-wiki/reagents/additives/methanol)) at 30 C | Induced expression for 18-20 h |
| Cell disruption | Bead beater with glass beads | — | 50 mM Tris pH 8.0, 1 M NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), protease inhibitor cocktail | 20 cycles of 1 min disruption and 2 min chilling |
| Membrane preparation | Differential ultracentrifugation | — | 50 mM Tris pH 8.0, 1 M NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) | 3,500 x g for 5 min to remove debris, then 100,000 x g for 1 h |
| Membrane solubilization | Potter homogenizer with [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide) | — | 50 mM Tris-Cl pH 8.0, 150 mM NaCl, 5% glycerol, 4 mg/ml [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide), protease inhibitor cocktail | Membrane pellet suspended and solubilized |


## Crystallization

### doi/10.1038##nchembio.2547

| Parameter | Value |
|---|---|
| Method | [Lipidic Cubic Phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) (LCP) |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) |
| Temperature | Not specified |
| Notes | Thermostabilized BLT1-T4L fusion crystallized in complex with BIIL260 by the [Lipidic Cubic Phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) method. Protein was mixed with monoolein at a 1:1 (w/w) ratio. The structure was determined at 3.7 A resolution.  |

### doi/10.1038##s41467-021-23149-1

| Parameter | Value |
|---|---|
| Method | [Lipidic Cubic Phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) (LCP) |
| Protein sample | hBLT1-CC at ~30 mg/mL in 50 mM HEPES pH 7.5, 200 mM NaCl, 0.2% DDM, 0.02% CHS, 100 µM MK-D-046 |
| Temperature | 20 |
| Growth time | 1-14 days |
| Cryoprotection | Crystals flash-frozen in liquid nitrogen directly from LCP |
| Notes | hBLT1-CC crystallized in LCP using NT8-LCP robot. Crystals appeared 24-48 h after incubation at 20 C and continued to grow up to 2 weeks. Average crystal size was 40 x 15 x 8 µm. Data collected from 32 crystals at APS GM/CA 231D-B beamline. Structure solved by molecular replacement using gpBLT1 (PDB 5X33) and flavodoxin (PDB 1I10) as search models. Anisotropic truncation: 2.9 A x 2.9 A x 3.6 A by STARANISO.  |


## Biological / Functional Insights

### First crystal structure of BLT1 (guinea pig)

The crystal structure of guinea pig BLT1 in complex with BIIL260 (PDB: 5X33, 3.7 A) represents the first structural view of the leukotriene B4 receptor. The thermostabilized mutant (H83G/K88G/V212A/S309A, lacking residues 1-14) with T4 lysozyme fusion at ICL3 enabled crystallization by the [Lipidic Cubic Phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) method. The structure reveals canonical seven transmembrane helix architecture with the N-terminus on the extracellular side and C-terminus on the intracellular side. 

### Benzamidine as sodium ion-mimicking ligand

The [Benzamidine](/xray-mp-wiki/reagents/additives/benzamidine) moiety of BIIL260 occupies the conserved sodium ion-binding site in BLT1, interacting with D66 (2.50), V69 (2.53), S106 (3.39), W236 (6.48), and S276 (7.45). This mimics the entire sodium ion-centered water cluster found in other inactive-state class A GPCRs, stabilizing BLT1 in the inactive conformation. The benzamidine moiety is located outside the orthosteric binding site, adjacent to it. 

### Sodium ion as negative allosteric modulator of BLT1

Biochemical assays demonstrated that sodium ions decrease LTB4 binding to BLT1 in a concentration-dependent manner, confirming that BLT1 is intrinsically sensitive to allosteric sodium modulation. [BIIL260](/xray-mp-wiki/reagents/ligands/biil260) competes with the sodium ion for binding, and higher NaCl concentrations can displace BIIL260 from the sodium ion-binding site, restoring LTB4 binding.

### Inactive-state conformation of BLT1

The intracellular side of the BLT1-BIIL260 complex shows features characteristic of the inactive GPCR state. An interhelical hydrogen bonding network is present among transmembrane helices 2, 3, 5, and 6 and ICL2. The [DRY Motif](/xray-mp-wiki/concepts/dry-motif) side chains (D116 3.49 and R117 3.50) do not form a salt bridge, consistent with the S2 inactive state with a broken ionic lock. 

### Extracellular ligand access vestibule

[BIIL260](/xray-mp-wiki/reagents/ligands/biil260) binds deeply in the transmembrane helix bundle but does not contact the extracellular loops. The ligand-binding vestibule is open on the extracellular surface, allowing ligands including BIIL260 and LTB4 to enter and leave the binding site via the extracellular surface. This contrasts with other lipid-ligand GPCRs (GPR40, S1P1R, CB1, rhodopsin) where the vestibules are not open on the extracellular surface. 

### Human BLT1 structure reveals ligand recognition determinants

The 2.9 A crystal structure of hBLT1 in complex with MK-D-046 revealed the molecular details of antagonist binding. MK-D-046 occupies the orthosteric binding pocket, anchored by polar interactions with H94(3.29) and R156(4.64), and hydrophobic contacts with F74(2.60), Y102(3.37), I271(7.39), and F275(7.43). The selectivity of MK-D-046 for hBLT1 over gpBLT1 is explained by four non-conserved residues: F169(ECL2)/L171, P170(ECL2)/A172, S264(7.32)/R263, and N268(7.36)/K267. The structure also revealed a putative membrane-buried ligand access channel between TM4 and TM5, supported by mutagenesis showing that H181(5.38)W mutation decreases LTB4 potency ~20-fold. 

### Putative membrane channel for lipid agonist access

The hBLT1 structure revealed a channel extending into the lipid bilayer between TM4 and TM5 that may serve as an access route for the lipid chemoattractant LTB4. Docking of LTB4 into the inactive hBLT1 structure suggested two possible binding conformations: one with the LTB4 tail occupying the membrane channel (conformation 1), and another with LTB4 extending deeper toward the sodium site (conformation 2). Mutagenesis of H181(5.38)W, which blocks the membrane channel entrance, decreased LTB4 potency ~20-fold without affecting MK-D-046 potency, supporting a membrane access route for LTB4. 

### Structural basis for species selectivity

Comparison of hBLT1 and gpBLT1 structures revealed that four non-conserved residues near the extracellular side of the binding pocket (F169ECL2/L171ECL2, P170ECL2/A172ECL2, S2647.32/R2637.32, N2687.36/K2677.36) contribute to species differences in ligand potency. However, residues outside the binding pocket appeared to play a larger role. Conserved residues such as H94(3.29), R156(4.64), and I271(7.39) differed in conformation between the two structures due to interactions with chemically distinct co-crystallized ligands. The hBLT1 structure proved more suitable for docking than gpBLT1, and serves as a better template for future drug design. 


## Cross-References

- [BIIL260](/xray-mp-wiki/reagents/ligands/biil260/) — Primary antagonist ligand bound in the first gpBLT1 crystal structure (PDB 5X33)
- [MK-D-046](/xray-mp-wiki/reagents/ligands/mk-d-046/) — Selective antagonist co-crystallized with hBLT1 (PDB 7K15)
- [Benzamidine](/xray-mp-wiki/reagents/ligands/benzamidine/) — [Benzamidine](/xray-mp-wiki/reagents/additives/benzamidine) moiety of BIIL260 mimics the sodium ion in BLT1
- [Leukotriene B4 (LTB4)](/xray-mp-wiki/reagents/ligands/ltb4/) — Endogenous agonist of BLT1
- [T4 Lysozyme (T4L)](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) — T4L fusion at ICL3 enabled gpBLT1 crystallization
- [Flavodoxin](/xray-mp-wiki/reagents/protein-tags/flavodoxin/) — Flavodoxin fusion at ICL3 enabled hBLT1 crystallization
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) method used for both BLT1 structures
- [Protein Thermostabilization](/xray-mp-wiki/concepts/construct-design/thermostabilization/) — Mutations used for both gpBLT1 and hBLT1 thermostabilization
- [Sodium Ion Allosteric Modulation in GPCRs](/xray-mp-wiki/concepts/signaling-receptors/sodium-allosteric-modulation/) — BLT1 is sensitive to allosteric sodium modulation
- [Pichia pastoris Expression System](/xray-mp-wiki/expression-systems/pichia-pastoris/) — gpBLT1-T4L expressed in [Pichia pastoris](/xray-mp-wiki/organisms/pichia-pastoris)
- [Insect Cell Expression System](/xray-mp-wiki/expression-systems/insect-cell-expression/) — hBLT1 expressed using baculovirus in insect cells
- [GPCR Inactive Conformation](/xray-mp-wiki/concepts/signaling-receptors/gpcr-inactive-conformation/) — Both BLT1 structures represent the inactive state
- [Inverse Agonism in GPCR Signaling](/xray-mp-wiki/concepts/signaling-receptors/inverse-agonism/) — [BIIL260](/xray-mp-wiki/reagents/ligands/biil260) acts as an inverse agonist for BLT1
- [Negative Allosteric Modulation](/xray-mp-wiki/concepts/signaling-receptors/negative-allosteric-modulation/) — [Benzamidine](/xray-mp-wiki/reagents/additives/benzamidine) moiety of BIIL260 serves as negative allosteric modulator
- [Extra-helical Binding Site in GPCRs](/xray-mp-wiki/concepts/signaling-receptors/extra-helical-binding-site/) — [Benzamidine](/xray-mp-wiki/reagents/additives/benzamidine) binding site is an extra-helical allosteric site
- [Membrane Access Channel in GPCRs](/xray-mp-wiki/concepts/membrane-access-channel/) — hBLT1 structure revealed a putative membrane-buried ligand access channel between TM4 and TM5
