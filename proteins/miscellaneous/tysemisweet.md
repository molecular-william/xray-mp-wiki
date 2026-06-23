---
title: "TySemiSWEET from Thermotoga yellowstonii"
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##cr.2014.144]
verified: false
---

# TySemiSWEET from Thermotoga yellowstonii

## Overview

TySemiSWEET is a bacterial sugar transporter from the [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/semisweet/) family found in Thermotoga yellowstonii. It is a dimeric three-helix bundle transporter that selectively transports disaccharides such as [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/). The structure reveals an elongated central pocket that accommodates a disaccharide ligand, providing structural insight into substrate selectivity within the [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/semisweet/) family.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##cr.2014.144 | 4RNG | 2.4 | P212121 | TySemiSWEET full-length | [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/) (tentative) |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: TySemiSWEET full-length

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Solubilization | Detergent solubilization | -- | -- + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Purified in detergent micelles; crystals in hanging-drop diffusion did not diffract beyond 10 A |


## Crystallization

### doi/10.1038##cr.2014.144

| Parameter | Value |
|---|---|
| Method | lipidic cubic phase |
| Protein sample | TySemiSWEET |
| Temperature | -- |
| Notes | Crystals diffracted beyond 2.4 A at BL32XU, SPring-8; structure determined by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using [LbSemiSWEET from Leptospira biflexa](/xray-mp-wiki/proteins/miscellaneous/lbsemisweet/) as search model |


## Biological / Functional Insights

### Dimeric assembly and interface

Six TySemiSWEET molecules arranged into three dimers in the asymmetric unit. Two dimers are arranged in parallel fashion, while the third is positioned in opposite orientation. Within each dimer, the two parallel protomers are related by 180-degree rotation around an axis perpendicular to the membrane plane. The dimer interface involves hydrogen bonds between Tyr57 of one protomer and Glu63 of the other, and between Trp54 and Thr19. An extensive H-bond network exists between the L1-2 linkers on the cytosolic side.

### Central pocket and substrate selectivity

The central pocket of TySemiSWEET is 18 A long with surface area of 463 A squared and volume of 613 A cubed. This elongated pocket can accommodate a disaccharide molecule such as [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/). The pocket size is determined by Met47, which leaves enough space compared to the corresponding Phe41 in [LbSemiSWEET from Leptospira biflexa](/xray-mp-wiki/proteins/miscellaneous/lbsemisweet/) that closes the pocket midway. All 16 residues in each protomer constituting the central pocket are highly conserved between TySemiSWEET and BjSemiSWEET1 (10 invariants), indicating similar pocket architecture in the [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/) transporter BjSemiSWEET1. In contrast, [LbSemiSWEET from Leptospira biflexa](/xray-mp-wiki/proteins/miscellaneous/lbsemisweet/) has a smaller pocket (11 A long, 424 A cubed volume) consistent with its function as a [Glucose](/xray-mp-wiki/reagents/additives/glucose/) transporter.

### Topology and transport mechanism

Each protomer contains three transmembrane helices (TM1, TM2, TM3) with TM3 positioned between TM1 and TM2. TM1 and TM2 are connected by an extended linker L1-2 enriched with positively charged residues. According to the positive-inside rule, L1-2 is located on the cytoplasmic side, leaving the N-terminus on the periplasmic side. The structure supports the alternating access mechanism, with the outward-open and occluded states captured. The inward-open structure remains to be determined.


## Cross-References

- [LbSemiSWEET from Leptospira biflexa](/xray-mp-wiki/proteins/miscellaneous/lbsemisweet/) — Close homologue used as molecular replacement search model; structural comparison reveals pocket size differences
- [SWEET Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/sweet-transporter/) — TySemiSWEET is a member of the SemiSWEET subfamily of sugar transporters
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — TySemiSWEET operates via alternating access with outward-open and occluded conformations captured
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — TySemiSWEET crystals obtained by LCP diffracted to 2.4 A at SPring-8
- [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/semisweet/) — Related biological concept
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [Glucose](/xray-mp-wiki/reagents/additives/glucose/) — Additive used in purification or crystallization buffers
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used in purification or crystallization
- [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/) — Related ligand or cofactor
