---
title: Human Ghrelin Receptor (GHSR)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-020-17554-1]
verified: true
---

# Human Ghrelin Receptor (GHSR)

## Overview

The human ghrelin receptor (GHSR, growth hormone secretagogue receptor) is a class A [GPCR](/xray-mp-wiki/concepts/signaling-receptors/gpcr/) that mediates the physiological effects of ghrelin, a gastric peptide hormone with important roles in appetite stimulation, growth hormone secretion, adiposity, energy homeostasis, and hippocampal neurogenesis. Ghrelin is uniquely modified by O-acyl-modification at Ser3, which is essential for its activity. The first high-resolution crystal structure of the ghrelin receptor bound to the neutral antagonist Compound 21 revealed a bifurcated ligand-binding pocket divided by a salt bridge between E124^3.33 and R283^6.55, and a hydrophobic gap (crevasse) between TM6 and TM7 rich in phenylalanine residues (F279^6.51, F286^6.58, F290^6.62, F309^7.39, F312^7.42). This gap is proposed to accommodate the acyl modification of ghrelin, explaining why acyl modification is essential for receptor activation.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-020-17554-1 |  |  |  | Engineered construct: N-terminal 28 residues replaced with thermostabilized apocytochrome b562RIL (bRIL), C-terminal 20 residues deleted. Mutations: T130K (thermostability), N188Q (glycosylation site removal). Fab 7881 fragment antibody added to facilitate crystallization. | Compound 21 (synthesized from YIL-781) |

## Expression and Purification

- **Expression system**: Baculovirus/Sf9 insect cells
- **Construct**: HA signal sequence + FLAG tag at N-terminus; HRV 3C protease site followed by eGFP and 8xHis tag at C-terminus. N-terminal 28 residues replaced with bRIL. C-terminal 20 residues deleted. Mutations: T130K, N188Q.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell harvest | Sf9 insect cells infected with baculovirus at MOI 1; harvested 48 h post-infection | — |  |  |
| Membrane preparation | Dounce homogenization in hypotonic buffer, ultracentrifugation, high salt wash | — |  |  |
| Solubilization | DDM with CHS | — |  |  |
| Affinity chromatography | Nickel IMAC for His-tag capture | — |  |  |
| Size-exclusion chromatography | SEC for purification of receptor-Fab-Compound 21 complex | — |  |  |


## Crystallization

### doi/10.1038##s41467-020-17554-1

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | Ghrelin receptor-Fab 7881-Compound 21 complex |
| Lipid | Monoolein:cholesterol (10:1) |
| Temperature | 20 C |
| Growth time | Up to 2 weeks |
| Notes | Data collected at SPring-8 BL32XU. Structure solved by molecular replacement using orexin receptor (PDB 4S0V), bRIL (PDB 1M6T), and Fab 7881 (PDB 6KS2) as search models. |


## Biological / Functional Insights

### Bifurcated ligand-binding pocket

The ghrelin receptor has a bifurcated ligand-binding pocket divided into two cavities (cavity I and cavity II) by a salt bridge between E124^3.33 and R283^6.55. This bifurcated pocket has not been observed in other solved beta-branch class A peptide hormone GPCRs. Mutagenesis of E124 or R283 completely abolished ghrelin-induced receptor function.

### Hydrophobic crevasse for acyl-modification recognition

A wide hydrophobic gap (crevasse) between TM6 and TM7 is formed by five phenylalanine residues (F279^6.51, F286^6.58, F290^6.62, F309^7.39, F312^7.42) and G282^6.54. The F279A and F312A mutations decreased Compound 21 binding and basal receptor activity. This crevasse is proposed to accommodate the acyl modification of ghrelin, explaining why acyl-modification at Ser3 is essential for receptor activation.

### Constitutive activity basis

The ghrelin receptor exhibits high constitutive (ligand-independent) activity. The aromatic amino acid cluster on TM6 and TM7, particularly the phenylalanine residues forming the crevasse, is thought to contribute to this high basal activity. The structure suggests the ghrelin receptor has properties of both peptide hormone GPCRs and lipid GPCRs.


## Cross-References

- [GPCR](/xray-mp-wiki/concepts/signaling-receptors/gpcr/) — Ghrelin receptor is a class A GPCR
