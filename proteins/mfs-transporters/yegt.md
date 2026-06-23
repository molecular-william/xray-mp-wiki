---
title: "YegT Nucleoside Proton Symporter from Escherichia coli"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jbc.2025.108357]
verified: false
---

# YegT Nucleoside Proton Symporter from Escherichia coli

## Overview

YegT is a member of the nucleoside proton symporter (NHS) family within the [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/protein-families/mfs-transporter/). Despite only 27% sequence identity with [NupG](/xray-mp-wiki/proteins/mfs-transporters/nupg/), YegT shares high structural conservation and a conserved GXXXD motif in TM10 that mediates proton-coupled substrate translocation.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jbc.2025.108357 | 8ZOJ | 3.1 | unknown | YegT K267A mutant from E. coli | none (apo state) |

## Expression and Purification

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane preparation | Cell lysis and membrane fractionation | — | 25 mM MES pH 6.0, 150 mM NaCl + 2% DDM | High-pressure homogenization at 800 bar |
| Affinity chromatography | Ni-NTA affinity chromatography | Ni-NTA affinity resin (Qiagen) | 25 mM MES pH 6.0, 150 mM NaCl, 25-300 mM imidazole + 0.02% DDM | Wash with 25 mM imidazole, eluted with 300 mM imidazole |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex 200 10/300 Increase (GE Healthcare) | 25 mM MES pH 6.0, 150 mM NaCl + 0.4% NG (n-octyl beta-D-glucoside) | Buffer exchanged to 0.4% NG for crystallization; concentrated to 30 mg/ml |


## Crystallization

### doi/10.1016##j.jbc.2025.108357

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP, in meso) |
| Protein sample | YegT K267A at 30 mg/ml, mixed with monoolein at 1:1.5 (w/w) |
| Temperature | 20°C |
| Notes | Crystals appeared within ~3 days; solved by molecular replacement at 3.1 Å |


## Biological / Functional Insights

### Conserved GXXXD motif for proton coupling

YegT contains a conserved GXXXD motif (Gly311–Asp315) in TM10, equivalent to NupG's Gly319–Asp323. The Asp315 serves as the protonation site with a calculated pKa of 7.96 (at crystallization pH 5.8, Asp315 is protonated). MD simulations showed deprotonation of Asp315 triggers TM10 helix destabilization and TM8 outward shift.

### Different substrate specificity from NupG

YegT shares only 27% sequence identity with NupG. The substrate-binding cavity residues differ significantly — residues Phe143, Tyr318, Phe322, and Asn228 in NupG (involved in uridine binding) are not conserved in YegT. ITC experiments showed no significant binding of uridine, adenosine, cytidine, or guanosine to YegT, suggesting a different physiological substrate.

### Structural conservation despite low sequence identity

Despite 27% sequence identity, YegT and NupG share a high structural similarity (RMSD 1.57 Å over 316 Cα atoms). The overall MFS fold, the GXXXD motif, and the protonation site architecture are fully conserved, indicating a shared proton-coupled release mechanism.


## Cross-References

- [NupG Nucleoside Proton Symporter](/xray-mp-wiki/proteins/mfs-transporters/nupg/) — Paralogs sharing the NHS family, conserved GXXXD motif, and proton-coupled mechanism
- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) — YegT belongs to the MFS family as an NHS member
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — YegT crystallized by LCP method with monoolein
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent for membrane solubilization of YegT
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid component of LCP crystallization matrix
- [2-(N-Morpholino)ethanesulfonic Acid (MES)](/xray-mp-wiki/reagents/buffers/mes/) — Buffer used throughout YegT purification
- [n-Octyl-beta-D-glucopyranoside (OG)](/xray-mp-wiki/reagents/detergents/og/) — Detergent used in size-exclusion chromatography for crystallization
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — Core transport mechanism shared by MFS transporters
