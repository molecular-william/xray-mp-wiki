---
title: "Coccomyxa subellipsoidea Rhodopsin (CsR)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1126##scisignal.aav4203]
verified: false
---

# Coccomyxa subellipsoidea Rhodopsin (CsR)

## Overview

Coccomyxa subellipsoidea rhodopsin (CsR) is a light-driven proton pump from the polar freshwater alga C. subellipsoidea (Trebouxiophyceae). The crystal structure of wild-type CsR (CsR-WT) was determined at 2.0-Å resolution, revealing seven transmembrane helices (TM1-TM7) with an all-trans-retinal chromophore covalently bound to Lys215 via a protonated Schiff base. A specific hydrogen bond between the highly conserved Arg83 and a nonconserved Tyr14 guided the structure-based transformation of CsR into an operational light-gated proton channel (CySeR, Y14E mutant) designed for potential optogenetic applications. CsR exhibits a BR-like pentameric counterion complex involving Asp86, Asp211, and three well-ordered water molecules, with a proton release complex including Glu193 and Glu203.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##scisignal.aav4203 | 6GYH | 2.0 | H3 | Wild-type CsR (residues 2-226) from Coccomyxa subellipsoidea expressed in Pichia pastoris, with C-terminal 8xHis tag
 | all-trans-retinal (covalently bound via Schiff base to Lys215) |

## Expression and Purification

- **Expression system**: Pichia pastoris
- **Construct**: CsR gene (residues 2-226) with C-terminal 8xHis tag, codon-optimized for P. pastoris expression

- **Notes**: Expressed in P. pastoris under control of AOX1 promoter. Cells disrupted by bead milling, membranes collected by ultracentrifugation, solubilized in 1% n-dodecyl-beta-D-maltopyranoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)).


### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Bead milling and ultracentrifugation | — | Lysis buffer (not specified in paper) | P. pastoris cells disrupted by bead milling, membranes collected by ultracentrifugation |
| Solubilization | Detergent solubilization | — | Buffer containing 150 mM NaCl, 20 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 7.0 + 1% n-dodecyl-beta-D-maltopyranoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Membranes solubilized at 4°C for 1 h with rotation |
| Ni-NTA affinity | Immobilized metal affinity chromatography | Ni-NTA agarose | 20 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 7.0, 150 mM NaCl, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | C-terminal 8xHis tag used for purification |
| Size-exclusion chromatography | Size-exclusion chromatography | HiLoad 16/600 Superdex 200 pg | 20 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 7.0, 150 mM NaCl, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Purified CsR concentrated to 35 mg/ml for crystallization |


## Crystallization

### doi/10.1126##scisignal.aav4203

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | 35 mg/ml CsR in 20 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 7.0, 150 mM NaCl, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/)
 |
| Temperature | 20 |
| Growth time | 10-14 days |
| Cryoprotection | Crystals picked from mesophase and flash-frozen in liquid nitrogen without additional cryoprotectant
 |
| Notes | CsR mixed with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) containing 10% [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) in 1:1 (w/w) ratio. Rhombohedral crystals (space group H3) with one monomer per asymmetric unit. >100 crystals screened at ESRF (ID23-2) and BESSY II. Cell dimensions: a=b=78.08, c=143.97 A.
 |


## Biological / Functional Insights

### Proton pump architecture and extracellular half-channel

CsR shares the canonical seven-transmembrane fold of microbial rhodopsins. The extracellular half-channel features a BR-like pentameric counterion complex (Asp86, Asp211, three water molecules) and a hydrogen-bond network connecting the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) Schiff base to the extracellular side via Arg83 and six water molecules. A unique feature is the hydrogen bond between Arg83 and Tyr14 (TM1), stabilized by a hydrophobic cage formed by Tyr57, Met60, Ala204, Tyr80, and Ile6.

### Conversion of pump to light-gated proton channel (CySeR)

Substitution of Tyr14 with glutamate (Y14E) transformed CsR from a unidirectional proton pump into a light-gated proton channel (CySeR). The Glu14-Arg83 interaction reshapes the extracellular half-channel, creating a more open configuration that permits passive proton conductance. CySeR shows symmetric photocurrents at neutral pH, with residual pump activity under acidic conditions due to pH-dependent protonation of Glu14.

### Distinguishing pump vs channel currents

Time-resolved electrophysiological and spectroscopic measurements showed that pump and channel currents can coexist in a single protein. Arg83 mobility is essential as a dynamic extracellular barrier to prevent passive conductance. The findings demonstrate that molecular constraints distinguishing active and passive ion transport are structurally more confined than previously expected, located in the extracellular half-channel near the Arg83-Tyr14 interaction.

### Photocycle kinetics

CsR-WT exhibits a BR-like photocycle with K, M, and O intermediates. Deprotonation of the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) Schiff base occurs within ~1.8 microseconds. CySeR retains similar early photocycle kinetics at neutral pH but shows impaired K-to-M transition at pH 9.0. Late photocycle steps coincide with passive conductance, suggesting structural rearrangements open a transient water channel on the cytoplasmic side.


## Cross-References

- [Acetabularia Rhodopsin II](/xray-mp-wiki/proteins/rhodopsins/acetabularia-rhodopsin-ii/) — ARII used as molecular replacement search model (PDB 3AM6)
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — Reference proton pump for structural and mechanistic comparison
- [Archaerhodopsin-3](/xray-mp-wiki/proteins/rhodopsins/archaerhodopsin-3/) — Compared pump-channel dichotomy with CsR findings
- [Rhodopsin Photocycle](/xray-mp-wiki/concepts/rhodopsin-mechanisms/rhodopsin-photocycle/) — CsR follows BR-type photocycle with K, M, O intermediates
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — CsR crystallized in monoolein LCP with cholesterol
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Matrix lipid for LCP crystallization of CsR
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for CsR solubilization and purification
- [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) — Chromophore covalently bound to Lys215 via Schiff base
- [Proton Release Complex](/xray-mp-wiki/concepts/rhodopsin-mechanisms/proton-release-complex/) — CsR features Glu193-Glu203 proton release complex
- [Channel Gating](/xray-mp-wiki/concepts/transport-mechanisms/channel-gating/) — CySeR engineering demonstrates pump-channel conversion mechanism
