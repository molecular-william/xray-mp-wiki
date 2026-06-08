---
title: Guinea Pig Leukotriene B4 Receptor 1 (BLT1)
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nchembio.2547]
verified: false
---

# Guinea Pig Leukotriene B4 Receptor 1 (BLT1)

## Overview

The leukotriene B4 receptor 1 (BLT1) is a class A G protein-coupled receptor that mediates the biological effects of leukotriene B4 (LTB4), a potent inflammatory lipid mediator. BLT1 is primarily expressed on leukocytes and plays a central role in inflammatory and immune responses. The first crystal structure of BLT1 was determined for a thermostabilized guinea pig construct in complex with the antagonist BIIL260, revealing a novel sodium ion-mimicking mechanism by which the benzamidine moiety of BIIL260 stabilizes the inactive state of the receptor.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nchembio.2547 | 5X33 | 3.7 A | Not specified | Thermostabilized guinea pig BLT1 mutant lacking residues 1-14, with H83G/K88G/V212A/S309A mutations, fused with T4 lysozyme (T4L) at intracellular loop 3 (construct ICL3-10)
 | BIIL260 |

## Expression and Purification

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Pichia pastoris stable expression | — | BMGY medium (1% yeast extract, 2% peptone, 100 mM potassium phosphate pH 6.0, 1.34% yeast nitrogen base, 1% glycerol) at 30 C | BLT1-T4L construct expressed in P. pastoris (pPIC3.5K vector) |
| Induction | BMMY medium induction with methanol | — | BMMY medium (1% yeast extract, 2% peptone, 100 mM potassium phosphate pH 6.0, 1.34% yeast nitrogen base, 0.5% methanol) at 30 C | Induced expression for 18-20 h |
| Cell disruption | Bead beater with glass beads | — | 50 mM Tris pH 8.0, 1 M NaCl, 5% glycerol, protease inhibitor cocktail | 20 cycles of 1 min disruption and 2 min chilling |
| Membrane preparation | Differential ultracentrifugation | — | 50 mM Tris pH 8.0, 1 M NaCl, 5% glycerol | 3,500 x g for 5 min to remove debris, then 100,000 x g for 1 h |
| Membrane solubilization | Potter homogenizer with iodoacetamide | — | 50 mM Tris-Cl pH 8.0, 150 mM NaCl, 5% glycerol, 4 mg/ml iodoacetamide, protease inhibitor cocktail | Membrane pellet suspended and solubilized |


## Crystallization

### doi/10.1038##nchembio.2547

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Lipid | Monoolein |
| Temperature | Not specified |
| Notes | Thermostabilized BLT1-T4L fusion crystallized in complex with BIIL260 by the lipidic cubic phase method. Protein was mixed with monoolein at a 1:1 (w/w) ratio. The structure was determined at 3.7 A resolution.
 |


## Biological / Functional Insights

### First crystal structure of BLT1

The crystal structure of guinea pig BLT1 in complex with BIIL260 (PDB: 5X33, 3.7 A) represents the first structural view of the leukotriene B4 receptor. The thermostabilized mutant (H83G/K88G/V212A/S309A, lacking residues 1-14) with T4 lysozyme fusion at ICL3 enabled crystallization by the lipidic cubic phase method. The structure reveals canonical seven transmembrane helix architecture with the N-terminus on the extracellular side and C-terminus on the intracellular side.

### Benzamidine as sodium ion-mimicking ligand

The benzamidine moiety of BIIL260 occupies the conserved sodium ion-binding site in BLT1, interacting with D66 (2.50), V69 (2.53), S106 (3.39), W236 (6.48), and S276 (7.45). This mimics the entire sodium ion-centered water cluster found in other inactive-state class A GPCRs, stabilizing BLT1 in the inactive conformation. The benzamidine moiety is located outside the orthosteric binding site, adjacent to it.

### Sodium ion as negative allosteric modulator of BLT1

Biochemical assays demonstrated that sodium ions decrease LTB4 binding to BLT1 in a concentration-dependent manner, confirming that BLT1 is intrinsically sensitive to allosteric sodium modulation. BIIL260 competes with the sodium ion for binding, and higher NaCl concentrations can displace BIIL260 from the sodium ion-binding site, restoring LTB4 binding.

### Inactive-state conformation of BLT1

The intracellular side of the BLT1-BIIL260 complex shows features characteristic of the inactive GPCR state. An interhelical hydrogen bonding network is present among transmembrane helices 2, 3, 5, and 6 and ICL2. The DRY motif side chains (D116 3.49 and R117 3.50) do not form a salt bridge, consistent with the S2 inactive state with a broken ionic lock.

### Extracellular ligand access vestibule

BIIL260 binds deeply in the transmembrane helix bundle but does not contact the extracellular loops. The ligand-binding vestibule is open on the extracellular surface, allowing ligands including BIIL260 and LTB4 to enter and leave the binding site via the extracellular surface. This contrasts with other lipid-ligand GPCRs (GPR40, S1P1R, CB1, rhodopsin) where the vestibules are not open on the extracellular surface.


## Cross-References

- [BIIL260](/xray-mp-wiki/reagents/ligands/biil260/) — Primary antagonist ligand bound in the first BLT1 crystal structure (PDB 5X33)
- [Benzamidine](/xray-mp-wiki/reagents/ligands/benzamidine/) — Benzamidine moiety of BIIL260 mimics the sodium ion in BLT1
- [Leukotriene B4 (LTB4)](/xray-mp-wiki/reagents/ligands/ltb4/) — Endogenous agonist of BLT1
- [T4 Lysozyme (T4L)](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) — T4L fusion at ICL3 enabled BLT1 crystallization
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used for BLT1 crystallization
- [Protein Thermostabilization](/xray-mp-wiki/concepts/thermostabilization/) — H83G/K88G/V212A/S309A mutations used for BLT1 thermostabilization
- [Sodium Ion Allosteric Modulation in GPCRs](/xray-mp-wiki/concepts/sodium-allosteric-modulation/) — BLT1 is sensitive to allosteric sodium modulation
- [Pichia pastoris Expression System](/xray-mp-wiki/expression-systems/pichia-pastoris/) — BLT1-T4L expressed in Pichia pastoris
- [GPCR Inactive Conformation](/xray-mp-wiki/concepts/gpcr-inactive-conformation/) — BLT1-BIIL260 complex represents the inactive state
- [Inverse Agonism in GPCR Signaling](/xray-mp-wiki/concepts/inverse-agonism/) — BIIL260 acts as an inverse agonist for BLT1
- [Negative Allosteric Modulation](/xray-mp-wiki/concepts/negative-allosteric-modulation/) — Benzamidine moiety of BIIL260 serves as negative allosteric modulator
- [Extra-helical Binding Site in GPCRs](/xray-mp-wiki/concepts/extra-helical-binding-site/) — Benzamidine binding site is an extra-helical allosteric site
