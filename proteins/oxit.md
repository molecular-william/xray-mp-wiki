---
title: Oxalate Transporter OxIT from Oxalobacter formigenes
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-023-36883-5]
verified: false
---

# Oxalate Transporter OxIT from Oxalobacter formigenes

## Overview

Oxalate transporter OxIT is an oxalate:formate antiporter (OFA) from the gut bacterium Oxalobacter formigenes. It belongs to the Major Facilitator Superfamily (MFS) and catalyzes the strict antiport of oxalate for formate across the cell membrane with high substrate specificity optimized for the C2 dicarboxylate oxalate. OxIT selectively discriminates oxalate from larger C4 dicarboxylates such as succinate and oxaloacetate, preventing unwanted uptake of metabolic intermediates. The transporter has a high turnover rate (over 1000/s) and serves as a virtual proton pump that creates a proton motive force for bacterial ATP synthesis. OxIT is essential for the oxalate-degrading capability of O. formigenes, which reduces kidney stone risk in host animals.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-023-36883-5 | 8HPK | 3.0 | not specified | OxIT from O. formigenes in complex with D5901Fab antibody fragment | oxalate |
| doi/10.1038##s41467-023-36883-5 | 8HPJ | 3.3 | not specified | OxIT from O. formigenes in complex with 20D033Fv antibody fragment | ligand-free |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: OxIT with N-terminal Strep-II tag and C-terminal His8 tag
- **Notes**: Expressed from pRSF-OxIT vector; induced by IPTG with all-trans retinal

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Cell lysis and membrane fractionation | not specified | 50 mM Tris-HCl pH 8.0, 200 mM potassium acetate, 1 mM EDTA, 1 mM PMSF, 5 mM MgCl2, 20 ug/mL DNase I, 0.23 mg/mL lysozyme + not specified | Cells disrupted with Emulsiflex C-5; debris removed by centrifugation at 9,600xg for 30min; membranes collected at 185,000xg for 1h |
| Solubilization | Detergent solubilization | not specified | 20 mM HEPES-KOH pH 8.0, 200 mM potassium acetate, 10 mM potassium oxalate, 20% glycerol + 40 mM DDM | Membrane fraction solubilized in buffer A with DDM |
| Affinity purification | Ni-NTA affinity chromatography | Ni-NTA Superflow (QIAGEN) or HisTrap FF crude (GE Healthcare) | 20 mM HEPES-KOH pH 8.0, 200 mM potassium acetate, 10 mM potassium oxalate, 20% glycerol, 1 mM DDM, 30-50 mM imidazole (wash); 250 mM imidazole (elution) + DDM | Column washed with 1 mM DDM and 30-50 mM imidazole; eluted with 250 mM imidazole |


## Crystallization

### doi/10.1038##s41467-023-36883-5

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | OxIT-D5901Fab complex at 10 mg/mL in 20 mM MES-KOH pH 6.2, 200 mM potassium acetate, 10 mM potassium oxalate, 20% glycerol, 0.51 mM DDM |
| Reservoir | 0.1 M sodium citrate pH 5.5, 0.05 M NaCl, 26% PEG400 |
| Temperature | 20 C |
| Notes | Grown overnight at 4 C; crystals flash-frozen in liquid nitrogen |

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (in meso) |
| Protein sample | OxIT-20D033Fv complex in lipidic mesophase (50% protein, 45% monoolein, 5% cholesterol) |
| Temperature | 20 C |
| Notes | Crystals obtained in 1 week using NT8-LCP crystallization robot; harvested from lipidic mesophase using Mesh Litholoops |


## Biological / Functional Insights

### Substrate-specific discrimination mechanism

The ligand-binding pocket contains basic residues (Q34, Y35, R272, Y328, K355) that form salt bridges with oxalate while preventing conformational switch to the occluded state without an acidic substrate. The pocket accommodates oxalate but excludes larger C4 dicarboxylates. In the ligand-free outward-facing state, charge repulsion between Arg272 and Lys355 at the empty binding site stabilizes the open conformation, preventing transition to the occluded form. This ensures OxIT functions as an antiporter where conformational switching without substrate is disallowed.

### Gln34 latch mechanism

Gln34, along with the hydrogen bond between Thr38 and Val240, functions as a periplasmic gate latch that prevents transition from the occluded to outward-facing conformation. MD simulations revealed a single side-chain flip of Gln34 triggers opening to the outside, breaking the Thr38-Val240 hydrogen bond. The Q34A mutant showed partial loss of binding and transport activity. This latch mechanism ensures the transport cycle proceeds in the correct direction.

### Rocker-switch motion with domain bending

The transition between occluded and outward-facing states involves a rocker-switch motion of N- and C-terminal domains, but unlike other MFS proteins, it is accompanied by conspicuous bending at TM1, 2, 4, 7, 8, and 11. The C-alpha RMSD between conformations is 2.6-2.7 A overall, with 1.5-1.6 A for individual domains. Bending at glycine residues and tilting of surrounding helices enables the conformational change.


## Cross-References
