---
title: vSGLT N64A Mutant
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature09580]
verified: false
---

# vSGLT N64A Mutant

## Overview

[VSGLT](/xray-mp-wiki/proteins/slc-transporters/vsglt/) N64A is a point mutant of the Vibrio parahaemolyticus Sodium-Galactose Transporter in which asparagine at position 64 (located in transmembrane helix 1) is replaced with alanine. N64 is a key residue in the sodium ion coordination site and forms a hydrogen bond with galactose in the substrate-binding pocket. The N64A mutant was studied by molecular dynamics simulations to investigate the gating mechanism of [VSGLT](/xray-mp-wiki/proteins/slc-transporters/vsglt/), revealing that the mutation prevents the Y263 rotamer switch that is essential for galactose exit.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature09580 | 3DH4 | 2.7 | P212121 | [VSGLT](/xray-mp-wiki/proteins/slc-transporters/vsglt/) N64A mutant, residues 1-452 (full-length); studied by [Molecular Dynamics Simulation](/xray-mp-wiki/methods/structure-determination/molecular-dynamics-simulation/) | [D-Galactose](/xray-mp-wiki/reagents/ligands/d-galactose/), sodium ions |

## Expression and Purification

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: [VSGLT](/xray-mp-wiki/proteins/slc-transporters/vsglt/) N64A mutant (N64A point mutation); residues 1-452 without N-terminal His-tag

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Detergent solubilization from E. coli membrane fractions | Ni-NTA (His-tag affinity) | Buffer containing Tris | N64A studied by [Molecular Dynamics Simulation](/xray-mp-wiki/methods/structure-determination/molecular-dynamics-simulation/); not crystallized |


## Crystallization

### doi/10.1038##nature09580

| Parameter | Value |
|---|---|
| Method | [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) |
| Protein sample | [VSGLT](/xray-mp-wiki/proteins/slc-transporters/vsglt/) N64A mutant construct (inward-occluded conformation, PDB 3DH4) |
| Reservoir | [PEG](/xray-mp-wiki/reagents/additives/peg/) 3350, [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/) |
| Temperature | 20 |
| Growth time | Not specified |
| Notes | N64A studied primarily by molecular dynamics; crystal structure of inward-occluded state (3DH4) used as reference |


## Biological / Functional Insights

### Gate mechanism revealed by MD simulation

Molecular dynamics simulations of the N64A mutant show that the chi1 angle of Y263 in TM6 does not undergo a conformational change during the 100 ns simulation. This keeps the inner gate closed and prevents galactose from entering the intracellular space. In contrast to wild-type [VSGLT](/xray-mp-wiki/proteins/slc-transporters/vsglt/) where Y263 switches rotamer at 52 ns allowing galactose exit at 110 ns, the N64A mutant locks Y263 in the galactose-blocking state. This provides direct evidence for the role of N64 in gating and the Y263 rotamer switch mechanism.

### Sodium coordination and gating coupling

N64 is part of the sodium ion coordination network at the Na2 site, and its mutation to alanine disrupts both sodium binding and the gating mechanism. The N64A mutation prevents the Y263 rotamer switch, demonstrating that sodium coordination and the Y263 gate are mechanically coupled. The simulation shows that the N64A mutant maintains the original Y263 rotamer throughout the entire 100 ns simulation, keeping the inner gate permanently closed.


## Cross-References

- [V. parahaemolyticus Sodium-Galactose Transporter (vSGLT)](/xray-mp-wiki/proteins/slc-transporters/vsglt/) — N64A is a point mutant of vSGLT
- [vSGLT K294A Mutant](/xray-mp-wiki/proteins/slc-transporters/vsglt-k294a/) — Both are point mutants of vSGLT from the same study
- [Sodium Ion (Na+)](/xray-mp-wiki/reagents/ligands/sodium-ion/) — N64 coordinates the sodium ion at the Na2 site
- [D-Galactose](/xray-mp-wiki/reagents/ligands/d-galactose/) — Primary substrate of vSGLT
- [Molecular Dynamics Simulation](/xray-mp-wiki/methods/structure-determination/molecular-dynamics-simulation/) — MD simulations used to study N64A mutant gating mechanism
- [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) — Method used in structure determination or purification
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/) — Additive used in purification or crystallization buffers
