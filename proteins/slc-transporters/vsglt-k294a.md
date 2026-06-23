---
title: vSGLT K294A Mutant
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature09580]
verified: false
---

# vSGLT K294A Mutant

## Overview

[VSGLT](/xray-mp-wiki/proteins/slc-transporters/vsglt/) K294A is a point mutant of the Vibrio parahaemolyticus Sodium-Galactose Transporter in which lysine at position 294 (located in transmembrane helix 6) is replaced with alanine. This mutation disrupts the sodium ion coordination site at the Na2 position, abolishing transport activity. The crystal structure of the K294A mutant provides direct structural evidence for the role of K294 in sodium-dependent substrate binding and the alternating-access mechanism.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature09580 | 3DH5 | 2.7 | P212121 | [VSGLT](/xray-mp-wiki/proteins/slc-transporters/vsglt/) K294A mutant, residues 1-452 (full-length) without N-terminal His-tag | [D-Galactose](/xray-mp-wiki/reagents/ligands/d-galactose/), sodium ions |

## Expression and Purification

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: [VSGLT](/xray-mp-wiki/proteins/slc-transporters/vsglt/) K294A mutant (K294A point mutation); residues 1-452 without N-terminal His-tag

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Detergent solubilization from E. coli membrane fractions | Ni-NTA (His-tag affinity) | Buffer containing Tris | Data from four crystals were merged for the K294A structure |


## Crystallization

### doi/10.1038##nature09580

| Parameter | Value |
|---|---|
| Method | [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) |
| Protein sample | [VSGLT](/xray-mp-wiki/proteins/slc-transporters/vsglt/) K294A mutant construct |
| Reservoir | [PEG](/xray-mp-wiki/reagents/additives/peg/) 3350, [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/) |
| Temperature | 20 |
| Growth time | Not specified |
| Notes | Space group P212121; unit cell a=85.3, b=112.7, c=238.8 A; alpha=beta=gamma=90 degrees; data from four crystals merged; Rwork/Rfree = 25.1/27.4; 8064 protein atoms, 26 ligand/ion atoms, 5 water atoms |


## Biological / Functional Insights

### Sodium coordination site disruption

The K294A mutation replaces a key sodium-coordinating residue (K294 in TM6) with alanine, disrupting the sodium ion binding site. The crystal structure at 2.7 A resolution (PDB 3DH5) shows the outward-open conformation of the mutant, providing structural evidence that K294 is essential for sodium ion coordination. This mutation abolishes transport activity while retaining the overall structural framework of the transporter.

### Structural refinement statistics

The K294A mutant structure was refined at 2.7 A resolution with Rwork/Rfree of 25.1/27.4. The unit cell dimensions are a=85.3, b=112.7, c=238.8 A in space group P212121. The model contains 8064 protein atoms, 26 ligand/ion atoms, and 5 water molecules. Data collection statistics: completeness 98.9%, redundancy 7.5, I/sigma(I) = 14.6.


## Cross-References

- [V. parahaemolyticus Sodium-Galactose Transporter (vSGLT)](/xray-mp-wiki/proteins/slc-transporters/vsglt/) — K294A is a point mutant of vSGLT
- [Sodium Ion (Na+)](/xray-mp-wiki/reagents/ligands/sodium-ion/) — K294 coordinates the sodium ion at the Na2 site
- [D-Galactose](/xray-mp-wiki/reagents/ligands/d-galactose/) — Primary substrate of vSGLT
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — K294A mutation provides evidence for sodium-dependent gating
- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/mfs-transporter/) — vSGLT is a member of the MFS transporter family
- [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) — Method used in structure determination or purification
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/) — Additive used in purification or crystallization buffers
