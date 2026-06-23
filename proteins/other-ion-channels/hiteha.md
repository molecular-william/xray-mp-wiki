---
title: HiTehA (TehA from Haemophilus influenzae)
created: 2026-06-02
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature09487, doi/10.1107##s139900471500423x]
verified: false
---

# HiTehA (TehA from Haemophilus influenzae)

## Overview

HiTehA is the [TEHA](/xray-mp-wiki/proteins/other-ion-channels/teha/) anion channel protein from Haemophilus influenzae. It is a bacterial
homologue of the plant SLOW ANION CHANNEL 1 ([SLAC1 (SLOW ANION CHANNEL 1 from Arabidopsis thaliana)](/xray-mp-wiki/proteins/other-ion-channels/slac1/)) and functions as an anion-selective
channel. HiTehA forms a symmetrical trimer, with each protomer containing ten transmembrane
helices arranged from five helical hairpin pairs to create a central five-helix transmembrane
pore. The pore is gated by a highly conserved phenylalanine residue (Phe 262). The structure
was originally solved by selenomethionyl (SeMet) SAD phasing at 1.20 A resolution from
cryocooled crystals. A subsequent room-temperature structure at 2.3 A resolution was
determined using in situ data collection from multiple crystals in vapour-diffusion plates,
demonstrating the first in situ membrane protein structure determination at a synchrotron.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature09487 | 3M7B | 1.20 | R3 | Full-length [TEHA](/xray-mp-wiki/proteins/other-ion-channels/teha/) from Haemophilus influenzae (residues 6-313) with Flag and deca-His tag, TEV cleavable | beta-octylglucoside |
| doi/10.1107##s139900471500423x | 4YCR | 2.30 | H3 | Full-length HiTehA (residues 1-313) expressed from pWaldoGFPe vector | beta-octylglucoside (OG) |

## Expression and Purification

- **Expression system**: Escherichia coli BL21(DE3) pLysS
- **Construct**: HiTehA cloned into pWaldoGFPe with C-terminal tag, purified in 20 mM Tris pH 7.5, 150 mM NaCl, 60 mM n-octyl-beta-D-glucopyranoside
- **Notes**: Overexpressed and purified as described by Drew et al. (2006)

### Purification Workflow

- **Expression system**: Escherichia coli BL21(DE3) pLysS
- **Expression construct**: HiTehA with Flag and deca-His tag, TEV cleavable
- **Tag info**: Flag and deca-His tag, cleavable by TEV protease

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Sonication | — | Buffer with [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |  |
| Metal affinity purification | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA | [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |  |
| Analytical SEC screening | Size-exclusion chromatography | Analytical SEC column | 12 different detergents tested |  |

**Final sample**: HiTehA exchanged into n-octyl-beta-D-glucopyranoside


## Crystallization

### doi/10.1107##s139900471500423x

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | HiTehA at 20 mg/mL in 20 mM Tris pH 7.5, 150 mM NaCl, 60 mM OG |
| Reservoir | 0.1 M NaCl, 120 mM Tris pH 9.4, 20% (v/v) [PEG](/xray-mp-wiki/reagents/additives/peg/) 400 |
| Mixing ratio | 1:1 (100 nL + 100 nL) |
| Temperature | 277 K (crystal growth), ambient for data collection |
| Growth time | 7-10 days |
| Notes | Crystals grown in 96-well sitting-drop plates (CrystalQuick X) using Mosquito robot. Data collected directly in-plate at room temperature on Diamond I24 with Pilatus3 6M detector. |

### doi/10.1038##nature09487

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | HiTehA in OG |
| Reservoir | [PEG 600](/xray-mp-wiki/reagents/additives/peg-600/) or [PEG](/xray-mp-wiki/reagents/additives/peg/) 400 |
| Temperature | 277 K |
| Notes | Original crystallization; crystals diffracted beyond 1.1 A. |


## Biological / Functional Insights

### Room-temperature in situ structure determination

The first membrane protein structure determined at room temperature using in situ data
collection at a synchrotron. Data from 56 crystals (63 partial wedges) were merged using
BLEND software after radiation damage assessment. The final dataset reached 2.3 A resolution
with R_meas = 0.107, R_p.i.m. = 0.044, completeness = 92.9%, and multiplicity = 4.9.
The room-temperature structure is very similar to the cryogenic structure (RMSD 0.66 A
for all atoms), with a notable loop shift in the TM6-TM7 connecting loop (max 2.9 A
at Ser192). The gating residue Phe262 remains in the same position and orientation.

### OG detergent binding in the channel cavity

The electron density from both room-temperature and 100 K data revealed one
octylglucoside (OG) detergent molecule inside the channel cavity on the cytoplasmic side,
which was not reported in the original 1.2 A structure. The hydrophobic alkyl tail of OG
reaches deep into the channel, surrounded by hydrophobic residues including Phe262, Ile203,
Leu18, Leu144.

### Trimeric organization of HiTehA

HiTehA forms tight trimers with three-fold axes aligned to the crystal lattice. Subunits
bury 8,947 A^2 of total surface area within trimer interfaces. The trimeric state was
confirmed both by size-exclusion multi-angle light-scattering ([SEC-MALS](/xray-mp-wiki/methods/quality-assessment/sec-mals/)) measurements
and by chemical cross-linking experiments.

### Novel ten-helix transmembrane fold

Each HiTehA protomer has ten transmembrane helices arranged from five tandemly repeated
helical hairpins with quasi-five-fold symmetry. An inner pentad of outwardly directed
odd-numbered transmembrane helices creates a pore through each protomer perpendicular to
the membrane plane. Even-numbered helices from the five hairpins surround the inner pore
as an outer layer.

### Phe 262 gate occluding the central pore

The central pore through each HiTehA protomer is occluded by the side chain of Phe 262
in the wild-type structure. The gating role of Phe 262 is conserved in [SLAC1 (SLOW ANION CHANNEL 1 from Arabidopsis thaliana)](/xray-mp-wiki/proteins/other-ion-channels/slac1/) as Phe 450.
The room-temperature structure confirms Phe262 is in the same position and orientation as
in the cryogenic structure.


## Cross-References

- [SLAC1 (SLOW ANION CHANNEL 1 from Arabidopsis thaliana)](/xray-mp-wiki/proteins/other-ion-channels/slac1/) — HiTehA is the bacterial homologue of plant SLAC1; structure used for homology modeling
- [Anion Channel Gating via Phenylalanine Gate](/xray-mp-wiki/concepts/anion-channel-gating/) — Phe 262 in HiTehA (Phe 450 in SLAC1) is the conserved gating residue
- [X-ray Crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/) — First in situ room-temperature synchrotron X-ray structure of a membrane protein
- [In situ Crystallography](/xray-mp-wiki/concepts/in-situ-crystallography/) — HiTehA was the first membrane protein structure determined by in situ data collection
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [SEC-MALS](/xray-mp-wiki/methods/quality-assessment/sec-mals/) — Method used in structure determination or purification
- [TEHA](/xray-mp-wiki/proteins/other-ion-channels/teha/) — Related protein structure
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [PEG 600](/xray-mp-wiki/reagents/additives/peg-600/) — Additive used in purification or crystallization buffers
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used in purification or crystallization
