---
title: NupG Nucleoside Proton Symporter from Escherichia coli
created: 2026-05-27
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jbc.2021.100479, doi/10.1016##j.jbc.2025.108357]
verified: false
---

# NupG Nucleoside Proton Symporter from Escherichia coli

## Overview

NupG is a nucleoside proton symporter from [Escherichia coli](/xray-mp-wiki/proteins/escherichia-coli-aqpz/) belonging to the nucleoside proton symporter (NHS) family within the [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/mfs-transporter/). It mediates the transport of nucleosides across the bacterial inner membrane via a proton-coupled mechanism. The first crystal structure of an NHS transporter was solved in this work, revealing an inward-open conformation with 12 transmembrane helices.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jbc.2021.100479 | unknown | 3.0 | P21 | Full-length NupG from E. coli K12, wild-type | none (apo state) |
| doi/10.1016##j.jbc.2021.100479 | unknown | 3.0 | P1 | Full-length NupG from E. coli K12, D323A mutant | none (apo state, no visible uridine) |
| doi/10.1016##j.jbc.2025.108357 | 8ZOJ | 3.1 | unknown | YegT K267A mutant from E. coli | none (apo state) |

## Expression and Purification

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane preparation | Cell lysis and membrane fractionation | — | 25 mM MES pH 6.0, 150 mM NaCl + 2% DDM | Membranes incubated 2 h with 2% DDM at 4°C |
| Affinity chromatography | Ni-NTA affinity chromatography | Ni-NTA affinity resin (Qiagen) | 25 mM MES pH 6.0, 150 mM NaCl, 20-250 mM imidazole + 0.02% DDM (wash), 0.4% NG (elution) | Eluted with 250 mM imidazole in 0.4% NG |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex 200 10/300 Increase (GE Healthcare) | 25 mM MES pH 6.0, 150 mM NaCl + 0.4% NG | Peak fractions concentrated to 30 mg/ml for crystallization |


## Crystallization

### doi/10.1016##j.jbc.2021.100479

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP, in meso) |
| Protein sample | WT NupG at 30 mg/ml, mixed with monoolein at 1:1.5 (w/w) |
| Temperature | not specified |
| Notes | P21 crystal form, diffraction to 3.8 Å, solved by molecular replacement |

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP, in meso) |
| Protein sample | NupG D323A at 30 mg/ml, mixed with monoolein at 1:1.5 (w/w) |
| Temperature | not specified |
| Notes | P1 crystal form, two molecules in asymmetric unit, solved at 3.0 Å |


## Biological / Functional Insights

### Uridine binding site residues

The uridine binding site is constituted by R136, T140, F143, Q225, N228, Q261, E264, Y318, and F322. Mutagenesis showed N228A and E264A reduced binding while F143A, F322A abolished binding.

### D323A mutation enhances uridine binding

The D323A mutant bound uridine with Kd 9.67 ± 2.87 µM, a 20-fold increase over WT (Kd 199.67 ± 15.01 µM). D323 does not directly contact uridine but is important for proton coupling.

### Substrate selectivity profile

NupG binds nucleosides: guanosine (Kd 46.67 µM) > adenosine (Kd 99.67 µM) > cytidine (Kd 143.67 µM) > thymidine (Kd 162.5 µM) > uridine (Kd 199.67 µM).

### Inward-open conformation of NHS transporter

Both WT and D323A NupG structures reveal identical inward-open conformations, consistent with MFS alternating-access mechanism.

### Proton-coupled substrate release mechanism via GXXXD motif

Asp323 in NupG (or Asp315 in YegT) serves as the protonation site within a conserved GXXXD motif in TM10. Deprotonation triggers local conformational changes including TM10 helix destabilization and TM8 outward shift, facilitating substrate release. MD simulations showed proton transfer from Asp323 to Glu264 reduces substrate binding affinity.

### Structural conservation between YegT and NupG

Despite only 27% sequence identity, YegT and NupG share high structural conservation (RMSD 1.57 Å over 316 Cα atoms). The GXXXD motif and protonation sites are fully conserved, suggesting a shared proton-coupled release mechanism.


## Cross-References

- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/mfs-transporter/) — NupG belongs to the MFS family, specifically the NHS family
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — Core transport mechanism shared by MFS transporters
- [Rocker-Switch Mechanism](/xray-mp-wiki/concepts/rocker-switch-mechanism/) — MFS-specific variant of alternating access mechanism
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — NupG and YegT both crystallized by LCP method with monoolein
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for membrane solubilization of NupG
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Primary lipid component of LCP crystallization matrix
- [2-(N-Morpholino)ethanesulfonic Acid (MES)](/xray-mp-wiki/reagents/buffers/mes/) — Buffer used throughout NupG purification at pH 6.0
- [YegT Nucleoside Proton Symporter](/xray-mp-wiki/proteins/mfs-transporters/yegt/) — Paralogs sharing the same NHS family and proton-coupled mechanism
