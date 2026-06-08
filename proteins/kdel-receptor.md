---
title: 
created: 2026-05-26
updated: 2026-05-26
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.68380]
verified: false
---

# 

## Overview

The [KDEL receptor](/xray-mp-wiki/proteins/kdel-receptor/) is a seven-transmembrane protein that retrieves escaped ER luminal proteins from the Golgi apparatus. It captures cargo carrying C-terminal KDEL, HDEL, or RDEL retrieval signals in the mildly acidic pH of the Golgi. The receptor undergoes a pH-dependent conformational change: signal binding triggers closure around the retrieval signal and exposes a lysine motif recognized by the COPI coat complex for retrograde transport. In the neutral pH of the ER, signal release reverses the conformational change, burying the COPI motif and exposing a patch of aspartate/glutamate residues proposed to form a COPII-binding ER exit signal. The receptor cycles between ER and Golgi, capturing escaped ER proteins in a dynamic retrieval process.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.7554##eLife.68380 | 6Y7V | not specified | not specified | Chicken [KDEL receptor](/xray-mp-wiki/proteins/kdel-receptor/) R2 bound to HDEL peptide at pH 6.0 | HDEL retrieval signal peptide |
| doi/10.7554##eLife.68380 | 6ZXR | not specified | not specified | Chicken [KDEL receptor](/xray-mp-wiki/proteins/kdel-receptor/) R2 bound to RDEL peptide at pH 6.0 | RDEL retrieval signal peptide |

## Expression and Purification

- **Expression system**: not specified (likely mammalian expression systems for functional assays)
- **Construct**: Chicken [KDEL receptor](/xray-mp-wiki/proteins/kdel-receptor/) R2 (major variant)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Purification | not specified | -- | not specified | Purified for in vitro binding assays and crystallography |


## Crystallization

### doi/10.7554##eLife.68380

| Parameter | Value |
|---|---|
| Method | not specified |
| Protein sample | Chicken [KDEL receptor](/xray-mp-wiki/proteins/kdel-receptor/) R2 + HDEL peptide |
| Reservoir | not specified |
| Temperature | not specified |
| Growth time | not specified |
| Notes | Structure at pH 6.0 (mimicking Golgi pH) |

| Parameter | Value |
|---|---|
| Method | not specified |
| Protein sample | Chicken [KDEL receptor](/xray-mp-wiki/proteins/kdel-receptor/) R2 + RDEL peptide |
| Reservoir | not specified |
| Temperature | not specified |
| Growth time | not specified |
| Notes | Structure at pH 6.0 |


## Biological / Functional Insights

### Signal capture and proofreading mechanism

The [KDEL receptor](/xray-mp-wiki/proteins/kdel-receptor/) captures retrieval signals through a stepwise carboxyl-handover mechanism. The C-terminal carboxylate of the signal sequentially engages R169 (TM6), R5, and R47 (TM4) in a ladder of arginine residues. Gatekeeper residues D50 and E117 at the entrance of the binding pocket exclude ADEL and DDEL sequences. Affinity differences between HDEL (10-fold higher than KDEL) and KDEL are explained by interactions between the variable -4 position and W120.

### pH-dependent conformational cycling

At acidic pH (Golgi, ~pH 6.0), the receptor closes around the retrieval signal and exposes a lysine motif for COPI coat binding. At neutral pH (ER), signal release reverses the conformational change, burying the lysine motif and exposing a patch of aspartate and glutamate residues proposed to form a COPII-binding ER exit signal. This pH-dependent cycling enables efficient retrieval and recycling.

### Dynamic range of ER retrieval

The receptor binds HDEL with 10-fold higher affinity than KDEL, yet HDEL is less efficiently retained than KDEL or RDEL in cells. This prevents HDEL-bearing proteins from outcompeting KDEL/RDEL proteins for limited receptor. The total concentration of retrieval signals exceeds the receptor by at least two orders of magnitude, but the receptor does not need to be stoichiometric with ER proteins.


## Cross-References

- [11-cis-Retinal](/xray-mp-wiki/reagents/ligands/11-cis-retinal/) — Related ligand-binding study methodology
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Related protein purification method
