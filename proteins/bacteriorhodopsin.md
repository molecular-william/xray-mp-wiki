---
title: Bacteriorhodopsin (Ground State)
created: 2026-05-07
updated: 2026-05-07
type: protein
category: proteins
layout: default
tags: [rhodopsin, membrane-protein, proton-pump, microbial-rhodopsin, seven-tm]
sources: [doi/10.1016##j.jmb.2011.04.038]
---

# Bacteriorhodopsin (Ground State)

## Overview

Bacteriorhodopsin (bR) is a light-driven proton pump from the halophilic archaeon Halobacterium salinarum. It consists of seven transmembrane alpha-helices (A-G) with all-trans retinal covalently bound to Lys216 via a protonated Schiff base in the ground state. The high-resolution crystallographic study (1.65-1.78 A) revealed that X-ray radiation during data collection induces structural changes that can mimic functional photointermediate states, including retinal all-trans to 13-cis isomerization, decarboxylation of Asp85, and loss of key water molecules (W401, W402, W406).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2011.04.038 | 1C3W | 1.78 A | P63 | Native bacteriorhodopsin from Halobacterium salinarum | all-trans retinal (covalently bound to Lys216 via protonated Schiff base) |

## Expression and Purification

- **Expression system**: Halobacterium salinarum (native purple membrane)
- **Construct**: Native bR holoprotein

### Purification Workflow

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Purple membrane isolation | Differential centrifugation | -- | not specified | Standard purification from H. salinarum purple membrane |


## Crystallization

### doi/10.1016##j.jmb.2011.04.038

| Parameter | Value |
|---|---|
| Method | In meso crystallization (lipidic mesophase) |
| Protein sample | bR solubilized in lipidic phase |
| Reservoir | not specified |
| Mixing ratio | not specified |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | Cryocooled to 100 K for X-ray data collection |
| Notes | Flat, hexagonally shaped crystals (150-300 micrometers plane, 10-40 micrometers thickness) grown in monoolein lipidic phase. Crystals separated from mesophase using 3 M sodium phosphate buffer, pH 5.6, with 0.1% octylglucoside. |


## Biological / Functional Insights

### X-ray radiation damage mimics functional intermediates

High-resolution analysis revealed that X-ray doses accumulated during standard data collection (0.3-0.4 MGy per dataset) induce structural changes in bR: (1) all-trans to 13-cis retinal isomerization, (2) disappearance of water molecules W401, W402, W406 from the active site, (3) decarboxylation of Asp85, (4) radiolysis of Asp212, (5) backbone movement of the C-helix (residues 82-85) and Lys216. These changes closely mimic the L-intermediate state structural features, potentially corrupting published intermediate-state structures that accumulated 0.7-1.1 MGy of radiation.

### Proton transport mechanism

bR pumps protons from cytoplasmic to extracellular side upon light absorption. The photocycle involves retinal isomerization (all-trans to 13-cis), followed by formation of intermediates K, L, M, N, and O. Key residues include Asp85 (proton acceptor), Asp96 (proton donor), Arg82 (proton release group), Glu194/Glu204 (extracellular proton release), and Asp212. The protonated Schiff base at Lys216 is the central proton donor.


## Cross-References

- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid component of the in meso crystallization matrix
- [n-Octyl beta-D-glucopyranoside (OG)](/xray-mp-wiki/reagents/detergents/og/) — Used at 0.1% for separating crystals from lipidic mesophase
- [Sodium Phosphate](/xray-mp-wiki/reagents/buffers/sodium-phosphate/) — 3 M sodium phosphate buffer (pH 5.6) used for crystal handling
- [11-cis-Retinal](/xray-mp-wiki/reagents/ligands/11-cis-retinal/) — Related chromophore; bR uses all-trans retinal
- [Rhodopsin Photocycle](/xray-mp-wiki/concepts/rhodopsin-photocycle/) — bR is the archetypal microbial rhodopsin photocycle
