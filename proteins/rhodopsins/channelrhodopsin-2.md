---
title: "Channelrhodopsin 2 (ChR2) from Chlamydomonas reinhardtii"
created: 2026-06-10
updated: 2026-06-10
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.aan8862]
verified: false
---

# Channelrhodopsin 2 (ChR2) from Chlamydomonas reinhardtii

## Overview

Channelrhodopsin 2 (ChR2) is a light-gated cation channel from the green alga
Chlamydomonas reinhardtii. It is the most widely used optogenetic tool for
remote control of neural activity with high spatiotemporal resolution. ChR2
belongs to the microbial rhodopsin family, a group of seven-transmembrane helix
proteins that bind a [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore via a protonated Schiff base. Photon
absorption triggers all-trans to 13-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) isomerization, initiating a
photocycle that opens the ion pore. The 2.4 Å crystal structure of wild-type
ChR2 and the 2.7 Å structure of the C128T slow mutant reveal the molecular
basis for ion conduction and gating regulation.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.aan8862 | 6EID | 2.4 | — | Wild-type ChR2 (residues 1-315, C-terminal truncation) |  |
| doi/10.1126##science.aan8862 | 6EID | 2.7 | — | C128T mutant ChR2 (residues 1-315, C-terminal truncation) |  |

## Expression and Purification

- **Expression system**: LEXSY (Leishmania tarentolae expression system)
- **Construct**: Full-length ChR2 with C-terminal polyhistidine tag
- **Notes**: Expressed in LEXSY T7-TR cells for structural studies

### Purification Workflow

- **Expression system**: LEXSY (Leishmania tarentolae)
- **Expression construct**: C-terminal polyhistidine tag

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Affinity chromatography | Ni-NTA / HisPur Cobalt Resin | — | 50 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 0.2 M NaCl, 0.2 M L-Histidine, 2 mM 6-aminohexanoic acid, cOmplete protease inhibitor + 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |  |
| Size-exclusion chromatography | SEC on Superdex 200 Increase 10/300 GL | — | 50 mM NaH2PO4/Na2HPO4 pH 5.2, 0.2 M NaCl, 1 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/), 2 mM 6-aminohexanoic acid, cOmplete + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Fractions with A280/A470 absorbance ratio ~1.8 were pooled |

**Final sample**: 40 mg/ml in SEC buffer


## Crystallization

### doi/10.1126##science.aan8862

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Lipid | Monoolein |
| Protein-to-lipid ratio | 1:1 (v/v) |
| Temperature | 22°C |
| Growth time | 2-6 months |
| Cryoprotection | 2.4 M KH2PO4/Na2HPO4, pH 5.2-5.6, 20% (w/v) [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |
| Notes | 300 nl protein-mesophase mixture overlaid with 500 nl precipitant. Hexagonal and rod-shaped crystals grew to 30-150 um. |


## Biological / Functional Insights

### Ion conduction pathway with four cavities and three gates

The ChR2 structure reveals an ion conduction pathway comprising four cavities
(EC1, EC2, IC1, IC2) separated by three gates (ECG, CG, ICG). The [Retinal](/xray-mp-wiki/reagents/ligands/retinal/)
Schiff base (RSB) at the central gate controls and synchronizes all three
gates through an extended hydrogen-bonding network involving water molecules
and side-chain residues. Arginines R120 and R268 form the cores of the ECG
and ICG, respectively.

### DC gate controls gating lifetime

The DC gate, named after D156 (TM4) and C128 (TM3), comprises a water-mediated
bond separate from the main ion pore but directly interacting with the RSB.
This gate controls channel open lifetime. The C128T mutant, with a prolonged
open-state lifetime, disrupts the water-mediated hydrogen bond network,
replacing it with a direct hydrogen bond between T128 and D156, affecting
the Schiff base environment and gating kinetics.

### Structural comparison reveals differences from C1C2 chimera

Comparison with the C1C2 chimera structure (PDB 3UG9) shows considerable
differences. In ChR2, E90 is a key determinant of ion selectivity and is
hydrogen-bonded to the proton acceptor D253, enabling direct influence by
[Retinal](/xray-mp-wiki/reagents/ligands/retinal/) isomerization and subsequent D253 protonation. In C1C2, the
corresponding E129 is not hydrogen-bonded to D292, explaining distinct
FTIR spectroscopy responses between the two proteins.


## Cross-References

- [Channelrhodopsin C1C2](/xray-mp-wiki/proteins/rhodopsins/channelrhodopsin-c1c2/) — Chimeric construct used for comparison; shows distinct structural and functional differences from native ChR2
- [Channelrhodopsin Photocycle](/xray-mp-wiki/concepts/transport-mechanisms/channelrhodopsin-photocycle/) — ChR2 structures provide molecular basis for understanding the photocycle and gating mechanism
- [n-Dodecyl-beta-D-maltoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Used throughout purification (0.1% for affinity, 0.05% for SEC)
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Used as LCP host lipid for in meso crystallization
- [LEXSY Leishmania tarentolae Expression System](/xray-mp-wiki/methods/expression-systems/lexsy-expression-system/) — Expression system used for ChR2 production
- [GR (Halobacterium sp. GR Bacteriorhodopsin)](/xray-mp-wiki/proteins/rhodopsins/gr/) — Related protein structure
- [Opsin (Retinal-Free Rhodopsin Apoprotein)](/xray-mp-wiki/proteins/gpcr/opsin/) — Related protein structure
- [Channelrhodopsin C1C2](/xray-mp-wiki/proteins/rhodopsins/channelrhodopsin-c1c2/) — Related protein structure
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid component
- [X-ray Crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/) — Method used in the study
