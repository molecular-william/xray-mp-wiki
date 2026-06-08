---
title: LPCAT3 (Lysophosphatidylcholine Acyltransferase 3)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein]
sources: [doi/10.1038##s41467-021-27244-1]
verified: false
---

# LPCAT3 (Lysophosphatidylcholine Acyltransferase 3)

## Overview

LPCAT3 (Lysophosphatidylcholine Acyltransferase 3), also known as MBOAT5, is a multi-pass membrane protein belonging to the membrane-bound O-acyltransferase (MBOAT) family. It catalyzes the re-acylation step of Lands' cycle, preferentially introducing polyunsaturated acyl chains (particularly arachidonoyl, 20:4) onto the sn-2 position of lysophosphatidylcholine (LPC). LPCAT3 is the main isoform expressed in major metabolic tissues including liver, small intestine, skeletal muscle, macrophage, and adipocyte. It plays critical roles in lipoprotein production, membrane fluidity regulation, and has been implicated in metabolic disorders such as hyperlipidemia and atherosclerosis.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-021-27244-1 | 7EWT | 1.9 | not specified | Trypsin-digested chicken LPCAT3 core | apo |
| doi/10.1038##s41467-021-27244-1 | 7F3X | 3.49 | C2 | Chicken LPCAT3 dimer with arachidonoyl-CoA | arachidonoyl-CoA |
| doi/10.1038##s41467-021-27244-1 | 7F40 | 3.57 | C2 | Chicken LPCAT3 dimer with 12:0-LPC | 1-dodecanoyl-sn-glycero-3-phosphocholine |

## Expression and Purification

- **Expression system**: Expi293 mammalian cells
- **Construct**: Chicken LPCAT3 (cLPCAT3), trypsin-digested core for crystallization
- **Notes**: Human and chicken LPCAT3 share 69% protein sequence identity. Trypsin digestion used to generate crystallizable core construct.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane solubilization | Detergent extraction | not specified | not specified + LMNG (Lauryl Maltose Neopentyl Glycol) | LMNG used for solubilization; enables dimer formation unlike DDM |
| Size-exclusion chromatography | Size-exclusion chromatography | not specified | GDN supplemented with 0.2 mM arachidonoyl-CoA + GDN (Glyco-Diosgenin) | Separates oligomeric LPCAT3 from monomers; 0.2 mM arachidonoyl-CoA added to stabilize substrate-bound state |


## Crystallization

### doi/10.1038##s41467-021-27244-1

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Trypsin-digested cLPCAT3 core, 14-28 days |
| Reservoir | 50 mM Magnesium acetate, 100 mM MES pH 6.0, 25% (v/v) PEG 400, 1% (v/v) Formamide |
| Temperature | 16 |
| Notes | Crystals harvested by flash freezing in liquid nitrogen. Cryoprotectant: 32% PEG 400, 100 mM MES pH 6.0, 50 mM magnesium acetate |


## Biological / Functional Insights

### T-shaped reaction chamber with lateral gate

LPCAT3 features a T-shaped reaction chamber with a lateral gate formed by TM1 and TM6 helices. The chamber comprises a horizontal tunnel for the acyl acceptor (LPC) and a vertical tunnel for the acyl donor (acyl-CoA), connected near the catalytic center. A side pocket extends from the vertical tunnel to accommodate the bulky polyunsaturated acyl chain of arachidonoyl-CoA.

### Substrate preference mechanism

The side pocket's near-to-90 degree bending routine from the vertical tunnel favors polyunsaturated acyl chains (e.g., 20:4) which adopt a ring-shape structure fitting the pocket well. Saturated acyl chains in all-trans configuration suffer from steric hindrance, explaining LPCAT3's preference for polyunsaturated over saturated fatty acids.

### Catalytic mechanism

The catalytic residues H388 and N352 are positioned near the junction of the horizontal and vertical tunnels. N352 is implied to act as a protonation reagent for the thioester bond. The catalytic chamber allows both substrates (LPC and arachidonoyl-CoA) to bind simultaneously, with the acyl chain positioned for transfer.


## Cross-References
