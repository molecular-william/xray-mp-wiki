---
title: Channelrhodopsin C1C2 (ChR1/ChR2 Chimera)
created: 2026-05-07
updated: 2026-05-07
type: protein
category: proteins
layout: default
tags: [light-gated-ion-channel, microbial-opsin, xray-crystallography, tr-sfx, optogenetics]
sources: [doi/10.7554##eLife.62389]
---

# Channelrhodopsin C1C2 (ChR1/ChR2 Chimera)

## Overview

Channelrhodopsin C1C2 is a chimeric construct between Chlamydomonas reinhardtii ChR1 and ChR2, designed as a light-gated cation channel for optogenetic applications. C1C2 retains normal ChR1 photocycle properties while forming high-density microcrystals suitable for time-resolved serial femtosecond crystallography (TR-SFX) using an X-ray free electron laser (XFEL). The TR-SFX analysis revealed early conformational changes following photoactivation, including retinal isomerization-induced downward shift of TM7, outward shift of TM3, and local deformation in TM7 - all triggers for ion pore opening. The DC-pair (Asp292-Cys294) in the retinal binding pocket is critical for photocycle transitions.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.7554##eLife.62389 | 7E6X | 2.3 A | not specified | C1C2 chimera (4 ms light-activated state) | all-trans retinal |
| doi/10.7554##eLife.62389 | 7E6Z | 2.5 A | not specified | C1C2 chimera (50 µs light-activated state) | isomerized retinal (twisted conformation) |
| doi/10.7554##eLife.62389 | 7E70 | 2.5 A | not specified | C1C2 chimera (250 µs light-activated state) | isomerized retinal |
| doi/10.7554##eLife.62389 | 7E71 | 2.5 A | not specified | C1C2 chimera (1 ms light-activated state) | isomerized retinal |
| doi/10.7554##eLife.62389 | 3UG9 | not specified | not specified | C1C2 chimera (dark state, synchrotron structure) | all-trans retinal |

## Expression and Purification

- **Expression system**: not specified (likely mammalian HEK293 cells for functional assays)
- **Construct**: ChR1/ChR2 chimera (C1C2) between Chlamydomonas reinhardtii ChR1 and ChR2

### Purification Workflow

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Crystal growth | Lipidic cubic phase ([LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/)) | -- | 50 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/)-HCl pH 8.0, 150 mM NaCl, 5% glycerol, 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | High-density microcrystals (2-5 um) formed in LCP optimized for TR-SFX |
| Reconstitution for spectroscopy | Lipid reconstitution | -- | POPE/POPG (1:50 protein/lipid molar ratio), 150 mM NaCl, 50 mM Tris-HCl pH 8.0, 5% glycerol, 0.01% CHS | For flash photolysis and photocurrent measurements |


## Crystallization

### doi/10.7554##eLife.62389

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | C1C2 chimera |
| Temperature | not specified |
| Growth time | not specified |
| Notes | Microcrystals 2-5 um, optimized for TR-SFX at SACLA XFEL. Dark state structure determined at 2.3 A. |


## Biological / Functional Insights

### Early conformational changes in channel gating

Time-resolved TR-SFX revealed that retinal isomerization induces a twisted conformation and shifts toward putative internal proton donor residues (Asp292), causing a downward shift of TM7 and an outward shift of TM3. These early conformational changes in the pore-forming helices are triggers for ion pore opening. The DC-pair (Asp292-Cys294) in the retinal binding pocket mediates photocycle transitions.

### Five glutamic acid residues line the ion pore

The dark state structure reveals five glutamic acid residues (E1-E5) lining the putative ion pore, with two counterion residues (C11 and C12). Three constriction sites form the inner, central, and outer gates. Light-induced conformational changes at these gates precede ion conductance.

### Photocycle intermediates in crystals

C1C2 crystals accumulate primarily the P2 intermediate (390 nm) with the transition from P2 to P3 hindered in the crystal lattice. The P2 intermediate shows prominent spectral increase at 390 nm, suggesting a deprotonated Schiff base state. This differs from solution behavior where P3 (530 nm) forms after P2.


## Cross-References

- [11-cis-Retinal](/xray-mp-wiki/reagents/ligands/11-cis-retinal/) — Chromophore bound to conserved lysine via Schiff base linkage
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for flash photolysis measurements
- [Cholesterol Hydrogen Succinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — CHS (0.01%) used in crystallization and spectroscopy buffers
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used to grow C1C2 microcrystals for TR-SFX
- [Tris Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Tris-HCl pH 8.0 used in crystallization and spectroscopy buffers
