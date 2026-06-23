---
title: "GLUT5 Fructose Transporter"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature14909]
verified: false
---

# GLUT5 Fructose Transporter

## Overview

GLUT5 is a fructose-specific facilitated-diffusion transporter belonging to the solute carrier 2 (SLC2) family and the major facilitator superfamily (MFS). It is primarily expressed in the small intestine but also found in brain, adipose tissue, kidney, testes, and skeletal muscle. GLUT5 is the only member of the GLUT family specific to fructose, and its altered activity has been linked to metabolic disorders such as type 2 diabetes and obesity. GLUT5 is also overexpressed in certain tumour cells, making it a potential drug target. This paper describes the crystal structures of Rattus norvegicus GLUT5 (rGLUT5) in an open outward-facing conformation at 3.27 A resolution and Bos taurus GLUT5 (bGLUT5) in an open inward-facing conformation at 3.0 A resolution, providing mechanistic insights into fructose transport via a gated-pore mechanism.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature14909 | -- | 3.27 | P2_1 | Rat GLUT5 (full-length, N50Y deglycosylation mutant) in complex with 4D111Fv fragment (VL and VH chains) | -- |
| doi/10.1038##nature14909 | -- | 3.0 | P2_12_12_1 | Bovine GLUT5 (residues 1-473, N51A deglycosylation mutant) | -- |

## Expression and Purification

- **Expression system**: Saccharomyces cerevisiae FGY217
- **Construct**: Full-length GLUT5 with C-terminal His6 tag and TEV cleavage site (pDDGFP2 vector, GAL1 inducible)
- **Notes**: GLUT5 homologues screened using fluorescence-based methods. Rat GLUT5 N50Y and bovine GLUT5 N51A mutants were used for deglycosylation.

### Purification Workflow

- **Expression system**: S. cerevisiae FGY217
- **Expression construct**: Full-length GLUT5 with C-terminal His6 tag, TEV cleavable

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Yeast fermentation | -- | -- + -- | 10 ml S. cerevisiae culture; overexpression as described previously |
| Membrane preparation | Cell lysis and ultracentrifugation | -- | 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 150 mM NaCl + -- | -- |
| Solubilization and purification | Affinity chromatography and SEC | -- | 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 150 mM NaCl + 0.03% n-dodecyl-beta-D-maltopyranoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Purified in [DDM](/xray-mp-wiki/reagents/detergents/ddm/); monodisperse peak assessed by gel filtration |

**Final sample**: 0.06 mg/ml in purification buffer (20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 150 mM NaCl, 0.03% DDM)


## Crystallization

### doi/10.1038##nature14909

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | rGLUT5-Fv complex in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Reservoir | 33-35% [Peg](/xray-mp-wiki/reagents/additives/peg/) 400, 0.12 M CaCl2 |
| Temperature | 20 C |
| Cryoprotection | -- |
| Notes | Rat GLUT5 crystallized in complex with 4D111Fv fragment in the open outward-facing conformation |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | bGLUT5 in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Reservoir | -- |
| Temperature | 20 C |
| Cryoprotection | -- |
| Notes | Bovine GLUT5 crystallized in the open inward-facing conformation; data showed severe anisotropy (resolutions along a*/b*/c* of 4.0/3.0/4.0 A) |


## Biological / Functional Insights

### Gated-pore transport mechanism in GLUT5

Comparison of the open outward-facing (rGLUT5) and open inward-facing (bGLUT5) structures reveals that in addition to a global [Rocker](/xray-mp-wiki/proteins/miscellaneous/rocker/)-switch-like reorientation of the N- and C-terminal 6-TM bundles (~15 degree rotation), local asymmetric rearrangements of C-terminal bundle helices TM7 and TM10 form substrate-induced gates. TM7 gates the extracellular side while TM10 gates the intracellular side, supporting a gated-pore transport mechanism for MFS monosaccharide transporters.

### Substrate specificity switch via single point mutation

Substitution of Gln166 (TM5) with glutamate (the equivalent residue in GLUT7) switches substrate preference from fructose to [Glucose](/xray-mp-wiki/reagents/additives/glucose/). The Q166E mutant shows robust D-[Glucose](/xray-mp-wiki/reagents/additives/glucose/) binding with a Kd of ~4 mM, whereas wild-type GLUT5 binds only [D Fructose](/xray-mp-wiki/reagents/ligands/d-fructose/) (Kd ~6-9 mM). This demonstrates that a single residue can determine substrate specificity among GLUT isoforms.

### Inter-bundle salt bridge network in conformational states

In the outward-facing conformation, conserved salt bridges form between the N- and C-terminal bundles (Glu400-Arg158 and Glu151-Arg407), which break apart in the inward-facing state (~7 A and 13 A separation, respectively). An additional salt bridge linking Glu336 (TM8) to Arg340 connects to this inter-bundle network. Substitution of Glu151 or Glu400 to alanine significantly reduces [D Fructose](/xray-mp-wiki/reagents/ligands/d-fructose/) binding, showing coupling between salt bridge integrity and substrate binding. The intracellular helical domain (ICH1-ICH5) provides additional stabilization of the outward-facing conformation.


## Cross-References

- [MFS Transporter](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) — GLUT5 belongs to the Major Facilitator Superfamily
- [Sugar Porter Family](/xray-mp-wiki/concepts/protein-families/sugar-porter-family/) — GLUT5 is a member of the sugar porter subfamily of MFS transporters
- [GLUT1](/xray-mp-wiki/proteins/mfs-transporters/glut1/) — Comparison with hGLUT1 inward-facing structure shows conservation of substrate-binding residues
- [D-Fructose](/xray-mp-wiki/reagents/ligands/d-fructose/) — Primary substrate of GLUT5
- [Tris](/xray-mp-wiki/reagents/buffers/tris/) — Referenced in glut5 text
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Referenced in glut5 text
- [Peg](/xray-mp-wiki/reagents/additives/peg/) — Referenced in glut5 text
- [Rocker](/xray-mp-wiki/proteins/miscellaneous/rocker/) — Referenced in glut5 text
- [Glucose](/xray-mp-wiki/reagents/additives/glucose/) — Referenced in glut5 text
- [D Fructose](/xray-mp-wiki/reagents/ligands/d-fructose/) — Referenced in glut5 text
