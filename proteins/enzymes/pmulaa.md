---
title: "Pasteurella multocida Ascorbate Transporter EIIC (pmUlaA)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1038##s41421-018-0037-y]
verified: false
---

# Pasteurella multocida Ascorbate Transporter EIIC (pmUlaA)

## Overview

pmUlaA is the EIIC component of the L-ascorbate (vitamin C) phosphoenolpyruvate-dependent phosphotransferase system (PTS) from Pasteurella multocida. It belongs to the ascorbate/galactitol (AG) superfamily of PTS transporters. The structure was solved in the inward-facing conformation at 3.35 Angstrom resolution, revealing a rigid-body [Elevator Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/elevator-mechanism/) where the substrate-binding core domain moves relative to the V motif domains to transport ascorbate across the membrane. pmUlaA shares 63% sequence identity with the E. coli homolog ecUlaA.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41421-018-0037-y | 5ZOV | 3.35 | — | Proteolyzed from wild-type pmUlaAB fusion, residues 37-460 | L-ascorbate (vitamin C) |

## Expression and Purification

- **Expression system**: E. coli C43 (DE3)
- **Construct**: Full-length pmUlaA with C-terminal His x 8 tag, expressed as pmUlaAB fusion (proteolyzed with [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/) to obtain pmUlaA)
- **Notes**: Cells disrupted by French Press at 15,000 p.s.i.
- **Induction**: 0.2 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at OD600 1.2
- **Media**: Luria broth

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane isolation | High-speed centrifugation | — |  | Membrane fraction pelleted from clarified lysate |
| Solubilization | Detergent extraction | — | 25 mM Tris-Cl pH 8.0, 150 mM NaCl, 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 2 mM ascorbic acid | Incubated for 1 h at 4 C |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA agarose | 25 mM Tris-Cl pH 8.0, 150 mM NaCl, 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 2 mM ascorbic acid, 0.56% NM | Eluted with [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) gradient, detergent exchanged from [DDM](/xray-mp-wiki/reagents/detergents/ddm/) to NM during elution |
| Size-exclusion chromatography | Gel filtration | — | 25 mM Tris-Cl pH 8.0, 150 mM NaCl, detergent, 2 mM ascorbic acid | Polishing step in buffer A with detergent |


## Crystallization

### doi/10.1038##s41421-018-0037-y

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Proteolyzed pmUlaA with bound L-ascorbate |
| Notes | Crystallized as a homodimer in the asymmetric unit. Best diffraction to 3.35 Angstrom. [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using ecUlaA core domain (PDB 4PR9) as search model. |


## Biological / Functional Insights

### Elevator mechanism of ascorbate transport

The inward-facing structure of pmUlaA completes the transport cycle of the PTS-AG family. Comparison of outward-open (ecUlaA, PDB 4PR9), occluded (ecUlaA), and inward-facing (pmUlaA, PDB 5ZOV) states reveals that ascorbate translocation occurs via a rigid-body movement of the substrate-binding core domain relative to the V motif domains. The core domain undergoes an 11.1 degree rotation and 6.68 Angstrom translocation relative to the V motif. TM2 and TM7 of the V motif domains act as pivots, with the C-terminus of TM7 swinging approximately 46.67 degrees around conserved Gly58 and Gly286 residues to accommodate core domain movement.

### Substrate coordination changes during transport

In the outward-facing state, vitamin C is entirely coordinated by core domain residues. As the core moves inward, Ser59 from V motif 1 contributes a hydrogen bond to the O3 atom of vitamin C in the occluded state. In the inward-facing state, Arg288 from V motif 2 forms a hydrogen bond with the O3 atom, stabilizing the substrate for phosphate transfer from UlaB.


## Cross-References

- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Used for membrane solubilization
- [Elevator Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/elevator-mechanism/) — Demonstrates elevator mechanism of ascorbate transport
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [IPTG](/xray-mp-wiki/reagents/additives/iptg/) — Additive used in purification or crystallization buffers
- [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/) — Additive used in purification or crystallization buffers
