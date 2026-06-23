---
title: Human Glucose Transporter 1 (hGLUT1)
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1073##pnas.1603735113]
verified: false
---

# Human Glucose Transporter 1 (hGLUT1)

## Overview

Human [Glucose](/xray-mp-wiki/reagents/additives/glucose/) transporter 1 ([hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/), [SLC2A1](/xray-mp-wiki/proteins/mfs-transporters/glut1/)) is a ubiquitously
expressed facilitated-diffusion [Glucose](/xray-mp-wiki/reagents/additives/glucose/) uniporter belonging to the
major facilitator superfamily ([MFS](/xray-mp-wiki/concepts/protein-families/major-facilitator-superfamily/)). It transports [Glucose](/xray-mp-wiki/reagents/additives/glucose/) from the
extracellular space into cells and is essential for cell viability.
[hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/) is significantly up-regulated in numerous cancer types due to
the increased glycolytic demand of tumor cells (Warburg effect),
making it an important prognostic indicator and therapeutic target.
This paper reports the first inhibitor-bound crystal structures of
wild-type [hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/), determined in complex with cytochalasin B and two
novel phenylalanine amide inhibitors (GLUT-i1 and GLUT-i2), all in
inward-open conformations.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1603735113 |  | 3.00 | — | Full-length WT [hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/) (residues 1-455, with residues 1-8 and 456-504 disordered) | cytochalasin B |
| doi/10.1073##pnas.1603735113 |  | 2.90 | — | Full-length WT [hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/) (residues 1-455, with residues 1-8 and 456-504 disordered) | GLUT-i1 |
| doi/10.1073##pnas.1603735113 |  | 3.00 | — | Full-length WT [hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/) (residues 1-455, with residues 1-8 and 456-504 disordered) | GLUT-i2 |

## Expression and Purification

- **Expression system**: Saccharomyces cerevisiae (full-length [hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/) with thrombin-cleavable C-terminal 10x His tag)

- **Construct**: Full-length [hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/) (residues 1-504) with C-terminal 10x His tag

### Purification Workflow

- **Expression system**: Saccharomyces cerevisiae
- **Expression construct**: Full-length [hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/) with C-terminal 10x His tag
- **Tag info**: C-terminal 10x His tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA | Ni-NTA (GE Biosciences, 1 mL column) | not specified + n-dodecyl-beta-D-maltopyranoside (beta-[DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Protein was not glycosylated at N45 despite known glycosylation site |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | SEC | — |  | Used for buffer exchange into crystallization buffer |

**Final sample**: [hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/) in buffer with beta-[DDM](/xray-mp-wiki/reagents/detergents/ddm/) at concentration for crystallization


## Crystallization

### doi/10.1073##pnas.1603735113

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | WT-[hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/) with inhibitor (cytochalasin B, GLUT-i1, or GLUT-i2) |
| Notes | Crystals obtained for all three inhibitor complexes; space group not specified; structures determined by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using 4PYP (apo-[hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/)) as search model |


## Biological / Functional Insights

### Inhibitor binding site overlaps glucose-binding site in inward-open conformation

All three inhibitors (cytochalasin B, GLUT-i1, and GLUT-i2) bind in the central cavity of the inward-open conformation of [hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/), overlapping the glucose-binding site. The binding site involves conserved residues including Trp388, Trp412, Asn411, Phe379, Thr137, and His160. Despite very different chemical backbones (cytochalasin B is a macrocyclic fungal metabolite; GLUT-i1/i2 are phenylalanine amides), all three compounds interact with the same pocket.

### Structural basis for isoform selectivity across hGLUT1-4

IC50 values against hGLUT1-4 show that all three compounds are sub-micromolar inhibitors of [hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/) and hGLUT4, but 10-100 fold weaker against hGLUT2, with intermediate potency against [hGLUT3 (Human Glucose Transporter 3)](/xray-mp-wiki/proteins/mfs-transporters/hglut3/). Homology models of hGLUT2-4 based on the [hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/) inhibitor-bound structures reveal that sequence differences in the binding pocket, particularly at residues corresponding to positions lining the central cavity, explain the differential isoform selectivity.

### Trp388 as a key binding determinant and conformational sensor

Trp388 (TM10) is a key binding determinant for all three inhibitors, forming pi-pi stacking interactions with the inhibitor rings. In the glucose-bound occluded state of [hGLUT3 (Human Glucose Transporter 3)](/xray-mp-wiki/proteins/mfs-transporters/hglut3/), the equivalent tryptophan rotates into the channel and hydrogen bonds to [Glucose](/xray-mp-wiki/reagents/additives/glucose/). Inhibitors likely block the inward-to-occluded conformational transition by preventing Trp388 movement, thus inhibiting [Glucose](/xray-mp-wiki/reagents/additives/glucose/) transport via an alternate-access mechanism.


## Cross-References

- [n-Dodecyl-beta-D-maltopyranoside (beta-DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for hGLUT1 purification and crystallization
- [MFS](/xray-mp-wiki/concepts/protein-families/major-facilitator-superfamily/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [SLC2A1](/xray-mp-wiki/proteins/mfs-transporters/glut1/) — Related protein structure
- [hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/) — Related protein structure
- [hGLUT3 (Human Glucose Transporter 3)](/xray-mp-wiki/proteins/mfs-transporters/hglut3/) — Related protein structure
- [Glucose](/xray-mp-wiki/reagents/additives/glucose/) — Additive used in purification or crystallization buffers
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used in purification or crystallization
