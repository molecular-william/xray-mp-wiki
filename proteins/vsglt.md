---
title: V. parahaemolyticus Sodium-Galactose Transporter (vSGLT)
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature09580]
verified: false
---

# V. parahaemolyticus Sodium-Galactose Transporter (vSGLT)

## Overview

V. parahaemolyticus Sodium-Galactose Transporter (vSGLT) is a secondary active transporter from the bacterium Vibrio parahaemolyticus that couples the electrochemical gradient of sodium ions to the active transport of galactose across the cell membrane. vSGLT belongs to the Major Facilitator Superfamily (MFS) and shares structural homology with the bacterial amino acid transporter LeuT. The crystal structures of vSGLT in both inward-occluded and outward-open conformations provided the first direct structural evidence for the alternating-access mechanism in an MFS transporter, revealing a sodium-dependent rocker-switch mechanism.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature09580 | 3DH4 | 2.7 | P212121 | vSGLT residues 1-452 (full-length) without N-terminal His-tag | D-galactose, sodium ions |
| doi/10.1038##nature09580 | 3DH5 | 2.7 | P212121 | vSGLT residues 1-452 (full-length) without N-terminal His-tag | D-galactose, sodium ions |

## Expression and Purification

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: vSGLT residues 1-452 with N-terminal His-tag; selenomethionine-substituted variant for SAD phasing

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Detergent solubilization from E. coli membrane fractions | Ni-NTA (His-tag affinity) | Buffer containing Tris | Selenomethionine-substituted protein for SAD phasing |


## Crystallization

### doi/10.1038##nature09580

| Parameter | Value |
|---|---|
| Method | Hanging drop vapor diffusion |
| Protein sample | Selenomethionine-substituted vSGLT construct |
| Reservoir | PEG 3350, sodium chloride |
| Temperature | 20 |
| Growth time | Not specified |
| Notes | Space group P212121; SAD phasing with selenium sites; two structures reported: inward-occluded (3DH4, galactose-bound) and outward-open (3DH5) |


## Biological / Functional Insights

### Outward-open conformation structure

The 3DH5 structure reveals vSGLT in an outward-open conformation with galactose and sodium ions bound in the substrate-binding pocket. The sodium ion is coordinated by the side chains of N64, N343, T350, S365, and K294, forming a coordination network that locks galactose in place. Key residues N64, N343, and W251 form hydrogen bonds with galactose, while Y263 adopts a rotamer conformation that opens the extracellular pathway. This structure provides the first high-resolution view of an MFS transporter in the outward-open state.

### Alternating-access mechanism

Superposition of the inward-occluded (3DH4) and outward-open (3DH5) structures reveals a rocker-switch mechanism involving rigid-body movement of the extracellular domain (ECD) relative to the transmembrane domain (TMD). The transition involves significant conformational changes in transmembrane helices 1, 5, 6, 7, and 10, while the hash motif (TMs 3, 4, 8, 9) and sugar bundle (TMs 2, 6, 7) remain relatively rigid. This provides direct structural evidence for the alternating-access mechanism in MFS transporters.

### Sodium-dependent gating mechanism

The sodium ion coordination site is critical for substrate binding and gating. In the outward-open conformation, the sodium ion stabilizes the binding pocket, and its absence allows the Y263 rotamer to switch and block substrate release. Molecular dynamics simulations show that sodium departure from the binding site triggers conformational changes that allow galactose to exit. The Y263 residue in TM6 acts as a gate, switching rotamer conformations to control substrate access.

### Inward-open conformation stabilization

The inward-open conformation is partially stabilized by a hydrogen bond between E68 (on the unwound segment of TM1) and S365 (a sodium-coordinating residue). This interaction helps lock the intracellular gate in the open state. The hash motif formed from TMs 3, 4, 8, and 9 provides structural stability during the conformational transition.


## Cross-References

- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — vSGLT crystal structures provide direct evidence for alternating access
- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/mfs-transporter/) — vSGLT is a member of the MFS transporter family
- [D-Galactose](/xray-mp-wiki/reagents/ligands/d-galactose/) — Primary substrate of the vSGLT transporter
- [Sodium Ion (Na+)](/xray-mp-wiki/reagents/ligands/sodium-ion/) — Essential co-transport ion for vSGLT function
- [vSGLT K294A Mutant](/xray-mp-wiki/proteins/vsglt-k294a/) — Crystallized variant of vSGLT from same study
- [vSGLT N64A Mutant](/xray-mp-wiki/proteins/vsglt-n64a/) — Gate mutant studied by molecular dynamics in same study
- [Molecular Dynamics Simulation](/xray-mp-wiki/methods/structure-determination/molecular-dynamics-simulation/) — MD simulations used to study galactose exit mechanism
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for membrane protein solubilization
