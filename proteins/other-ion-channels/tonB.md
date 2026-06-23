---
title: TonB (E. coli)
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature19757]
verified: false
---

# TonB (E. coli)

## Overview

TonB is an integral polytopic membrane protein from Escherichia coli that serves as the energy transducer connecting the inner membrane [Ton Complex](/xray-mp-wiki/concepts/ton-complex/) (ExbB-[ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/)) to TonB-dependent transporters (TBDTs) at the outer membrane. TonB contains a single N-terminal transmembrane helix that anchors a large C-terminal periplasmic domain. The periplasmic domain contains a conserved 5-7 residue TonB box that interacts with TBDTs upon ligand binding. TonB exchanges for one [ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/) monomer during energy transduction, and its interaction with [ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/) triggers conformational changes that lead to ligand uptake by TBDTs at the outer membrane.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature19757 | 5FQ7 | 2.6 A | P63 | ExbB-ExbD-TonB fully assembled complex | calcium ion |
| doi/10.1038##nature19757 | 5FQ6 | 3.5 A | P212121 | ExbB-ExbD-TonB fully assembled complex | calcium ion |

## Expression and Purification

- **Expression system**: E. coli K-12 BL21(DE3) cells
- **Construct**: TonB cloned into pACYCDUET-1 vector with N-terminal 10xHis tag followed by TEV protease site; TonB C18A mutant also prepared

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Emulsiflex-C3 high-pressure homogenization | -- | TBS + -- | Cells resuspended with 100 uM AEBSF, 100 uM DNase, 50 ug/ml lysozyme; disrupted at ~15,000 p.s.i. |
| Membrane isolation | Ultracentrifugation | -- | TBS + -- | Pelleted at 200,000g for 1 h at 4 C; membranes resuspended with dounce homogenizer |
| Solubilization | Membrane solubilization | -- | TBS + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Solubilized by addition of [DDM](/xray-mp-wiki/reagents/detergents/ddm/) to 1% final concentration |
| Affinity purification | His-tag [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | -- | TBS + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Purified using N-terminal 10xHis tag on TonB; co-expression with [ExbB (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbB/) and [ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/) for [Ton Complex](/xray-mp-wiki/concepts/ton-complex/) |


## Crystallization

### doi/10.1038##nature19757

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | ExbB-ExbD-TonB fully assembled complex |
| Reservoir | Not specified in paper |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | The fully assembled [Ton Complex](/xray-mp-wiki/concepts/ton-complex/) was characterized by electron microscopy, crosslinking, and DEER spectroscopy. Only a single TMH of TonB can fit within the [ExbB (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbB/) pentamer pore. DEER on the fully assembled complex (TonB C18A-[ExbB (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbB/) C25S-[ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/) N78C) showed distance distributions nearly identical to the subcomplex, confirming [ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/) remains dimeric in the presence of TonB. |


## Biological / Functional Insights

### Stoichiometry of the fully assembled Ton complex

The fully assembled [Ton Complex](/xray-mp-wiki/concepts/ton-complex/) consists of a pentamer of [ExbB (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbB/), a dimer of [ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/), and at least one TonB. Association of TonB does not notably affect the structure or stoichiometry of [ExbB (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbB/) or [ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/). The interaction of TonB with [ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/) leads to a functional [Ton Complex](/xray-mp-wiki/concepts/ton-complex/) that triggers energy production and transduction in the form of conformational changes in TonB, which lead to ligand uptake by the TBDT at the outer membrane.

### TonB-ExbD interaction and energy transduction

Previous studies indicated that TonB may exchange for one of the [ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/) monomers during energy transduction. The second [ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/) copy is located outside the [ExbB (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbB/) pentamer, hypothesized to be mediated by its periplasmic domain. The interaction of TonB with [ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/) leads to a functional [Ton Complex](/xray-mp-wiki/concepts/ton-complex/), triggering energy production and transduction. This mechanism couples the proton motive force at the inner membrane to ligand transport across the outer membrane.

### DEER validation of complex assembly

DEER spectroscopy on the fully assembled [Ton Complex](/xray-mp-wiki/concepts/ton-complex/) (TonB C18A-[ExbB (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbB/) C25S-[ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/) N78C, labeled with MTSL) showed distance distributions for the labels on [ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/) nearly identical to those of the subcomplex, confirming that [ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/) remains a dimer in both the absence and presence of TonB. This confirms the proposed model of a pentamer of [ExbB (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbB/), dimer of [ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/), and at least one TonB.


## Cross-References

- [ExbB (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbB/) — TonB interacts with the ExbB pentamer as part of the fully assembled Ton complex
- [ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/) — TonB interacts directly with ExbD; TonB may exchange for one ExbD monomer during energy transduction
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for solubilization of the fully assembled Ton complex (1% DDM)
- [His6 Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) — N-terminal 10xHis tag used for TonB purification
- [DEER Spectroscopy](/xray-mp-wiki/methods/quality-assessment/deer-spectroscopy/) — DEER performed on the fully assembled Ton complex (TonB C18A-ExbB C25S-ExbD N78C) to validate stoichiometry
- [Circular Dichroism Spectroscopy](/xray-mp-wiki/methods/quality-assessment/circular-dichroism-spectroscopy/) — Circular dichroism used to assess secondary structure and thermal stability of the Ton subcomplex
- [Ton Complex](/xray-mp-wiki/concepts/ton-complex/) — TonB is a core component of the Ton complex; the concept page describes the functional complex and energy transduction mechanism
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
