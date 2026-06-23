---
title: Photosystem I from Thermosynechococcus elongatus
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41598-021-00236-3]
verified: false
---

# Photosystem I from Thermosynechococcus elongatus

## Overview

Photosystem I (PS I) from the thermophilic cyanobacterium Thermosynechococcus elongatus is a large multisubunit pigment-protein complex that performs light-driven electron transfer across the thylakoid membrane. It consists of two large membrane intrinsic subunits (PsaA and PsaB) with 11 transmembrane helices each, surrounded by smaller membrane intrinsic subunits (PsaF, PsaI, PsaJ, PsaK, PsaL, PsaM, PsaX) and three membrane extrinsic subunits (PsaC, PsaD, PsaE) on the stromal side. The complex forms a trimer (~1 MDa) in cyanobacteria. Room temperature XFEL structures revealed an expansion along the membrane plane compared to cryogenic structures, and conformational differences around the phylloquinone cofactors PhQA and PhQB that may contribute to unidirectional electron transfer.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41598-021-00236-3 | 7M75 | 2.75 | P63 | Trimeric PS I from Thermosynechococcus elongatus; data merged from LCLS/MFX and SwissFEL/Bernina; 143,459 lattices merged; 2.75 A resolution |  |
| doi/10.1038##s41598-021-00236-3 | 7M78 | 3.00 | P63 | Trimeric PS I from T. elongatus; data collected at SACLA/BL2; 22,560 lattices merged; 3.0 A resolution |  |
| doi/10.1038##s41598-021-00236-3 | 7M76 | 3.00 | P63 | Trimeric PS I from T. elongatus; data collected at PAL-XFEL/NCI in presence of ascorbic acid; 5,901 lattices merged; 3.0 A resolution |  |

## Expression and Purification

No purification described.

## Crystallization

### doi/10.1038##s41598-021-00236-3

| Parameter | Value |
|---|---|
| Method | Microcrystal preparation for SFX |
| Protein sample | Trimeric PS I from T. elongatus |
| Temperature | Room temperature for data collection |
| Growth time | Crystals harvested and delivered via DOT (Drop-on-Tape) setup |
| Cryoprotection | No cryoprotection needed (room temperature SFX) |
| Notes | Microcrystals of 15-25 um trimeric PS I were delivered using the Drop-on-Tape (DOT) setup at LCLS/MFX and SwissFEL/Bernina. XFEL data collected at RT using fs X-ray pulses to obtain damage-free structures. Additional data collected at SACLA/BL2 and PAL-XFEL/NCI. LCLS/SwissFEL data merged for the highest quality 2.75 A structure. |


## Biological / Functional Insights

### Membrane plane expansion at room temperature

The room temperature PS I structure shows a clear expansion of the entire protein complex in the membrane plane direction (~0.2 A average) compared to the cryogenic structure (PDB 1JB0). This anisotropic expansion was consistently observed across three independent datasets collected at LCLS, SwissFEL, SACLA, and PAL-XFEL. The expansion is attributed to increased thermal mobility of aliphatic chains (chlorophyll isoprenoid tails, quinone chains, detergent/lipid fatty acids) at RT versus cryogenic temperatures, similar to observations in PS II. Perpendicular to the membrane, changes were minimal and symmetrically distributed.

### Phylloquinone environment asymmetry

At room temperature, the pi-stacked phenylalanine residues adjacent to the phylloquinones (PsaA-Phe689 and PsaB-Phe669) adopt different orientations. PsaA-Phe689 rotates to a more parallel orientation (13 +/- 8 degrees) relative to PhQA, increasing off-center pi-stacking at 3.9 A distance. In contrast, PsaB-Phe669 rotates to an almost perpendicular orientation (73 +/- 6 degrees) relative to PhQB. The symmetry-breaking PsaB-Trp673 also rotates by 15 degrees and moves further from PhQA (7.0 A vs 6.6 A in cryo structure). These temperature-dependent conformational changes may contribute to the preferential directionality of electron transfer along the A branch.

### Conserved room temperature features across XFEL sources

The same structural features (membrane plane expansion and phylloquinone asymmetry) were observed in independent datasets from four different XFEL facilities (LCLS, SwissFEL, SACLA, PAL-XFEL), using crystals from different preparations. Data collected in the presence of ascorbic acid (dark/reduced conditions at PAL-XFEL) did not show specific differences from the untreated dark state structure, confirming the robustness of the observations.


## Cross-References

- [Photosystem II Core Dimer](/xray-mp-wiki/proteins/photosynthesis/photosystem-ii-core-dimer/) — Comparison of membrane plane expansion between PS I and PS II at RT
- [PSI-LHCI supercomplex from pea](/xray-mp-wiki/proteins/photosynthesis/psi-lhci-pea/) — Related PS I structure from higher plants at cryogenic temperature
- [Serial Femtosecond Crystallography (SFX)](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/) — Method used for room temperature structure determination
- [X-ray Radiation Damage](/xray-mp-wiki/concepts/methods-techniques/x-ray-radiation-damage/) — SFX enables damage-free room temperature structures
- [Serial Femtosecond Crystallography](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/) — Method used in structure determination or purification
