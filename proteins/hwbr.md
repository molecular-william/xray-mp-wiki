---
title: HwBR (Halomonas Water Bacteriorhodopsin)
created: 2026-06-05
updated: 2026-06-05
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms8177]
verified: false
---

# HwBR (Halomonas Water Bacteriorhodopsin)

## Overview

HwBR (Halomonas water bacteriorhodopsin) is a light-driven proton pump from a Halomonas species. It shares high sequence similarity with archaerhodopsin-3 (AR3) and was used as a model system for rational design of blue-shifted AR3 mutants. The wild-type HwBR exhibits a characteristic absorption maximum typical of bacteriorhodopsins. Rational design mutations at positions equivalent to C1C2 residues 198 and 202 (positions 128 and 132 in HwBR/AR3 numbering) were introduced to create blue-shifted variants. HwBR was expressed in E. coli BL21(DE3) and purified using standard membrane protein purification protocols.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms8177 | 1C3W | not specified for HwBR in this paper | not specified | HsBR (Halobacterium salinarum bacteriorhodopsin) used as structural model for HwBR | all-trans retinal |

## Expression and Purification

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: HwBR expression plasmid constructed as previously described
- **Notes**: Transformed E. coli BL21(DE3) cells grown at 18 C overnight in LB medium containing ampicillin (50 ug/ml) and 5 uM all-trans retinal. L-arabinose induction used for AR3 and HwBR expression (as opposed to IPTG for GR).
- **Induction**: 0.1% L-arabinose (for AR3 and HwBR)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Cell disruption and membrane fractionation | -- | 50 mM MES (pH 6.5) containing 1 M NaCl + -- | Cells harvested by centrifugation at 4 C, disrupted by sonication or French press passage |
| Solubilization | Detergent solubilization | -- | 50 mM MES (pH 6.5), 1 M NaCl + n-dodecyl-beta-D-maltoside (DDM) | Cell membranes solubilized by DDM |
| Affinity chromatography | Ni2+ affinity chromatography | Ni2+ affinity column (GE Healthcare) | Not specified + DDM | Purified by chromatography on Ni2+ affinity column |
| Concentration and buffer exchange | Ultrafiltration concentration | -- | 1 M NaCl, 50 mM Tris-Cl (pH 7.0) + 0.05% DDM | Purified sample concentrated using Amicon Ultra filter |


## Crystallization

No crystallization described.

## Biological / Functional Insights

### HwBR as model for blue-shifted AR3 design

HwBR shares high sequence similarity with AR3 and was used as a model system for rational design of blue-shifted AR3 mutants. The HsBR crystal structure (PDB 1C3W) served as the structural template for QM/MM simulations to predict the effects of mutations at positions 128 and 132 (equivalent to positions 198 and 202 in C1C2) on the retinal chromophore conformation. The design principle was validated by creating blue-shifted HwBR variants with significantly altered absorption spectra.

### Blue-shifted HwBR variants created by rational design

HwBR was engineered with mutations at positions 128 and 132 (equivalent to C1C2 positions 198 and 202) to create blue-shifted variants. These mutations induce rotation of the beta-ionone ring of the retinal chromophore, producing blue-shifted absorption spectra. The design principle established with C1C2 was shown to be transferable to HwBR, demonstrating the generality of the atomistic design approach.


## Cross-References

- [Archaerhodopsin-2](/xray-mp-wiki/proteins/archaerhodopsin-2/) — AR3 shares high sequence similarity with HwBR; HsBR used as structural model for both
- [C1C2GA (C1C2 T198G/G202A)](/xray-mp-wiki/proteins/c1c2ga/) — HwBR was engineered using the same design principle as C1C2GA (mutations at equivalent positions 128/132)
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/bacteriorhodopsin/) — HwBR is a bacteriorhodopsin; HsBR (PDB 1C3W) used as structural model
- [n-Dodecyl-beta-D-maltoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for membrane solubilization and protein purification
- [2-(N-morpholino)ethanesulfonic acid (MES)](/xray-mp-wiki/reagents/buffers/mes/) — Buffer (50 mM, pH 6.5) used in cell lysis and membrane preparation
- [All-trans retinal](/xray-mp-wiki/reagents/ligands/all-trans-retinal/) — Chromophore covalently bound to conserved lysine via protonated Schiff base
