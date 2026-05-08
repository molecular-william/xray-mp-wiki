---
title: Vp-ZntB Cytoplasmic Domain
created: 2026-05-05
updated: 2026-05-05
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1002##pro.215]
---

# Vp-ZntB Cytoplasmic Domain

## Overview

ZntB is a zinc/cadmium efflux transporter from the metal ion transporter (MIT) superfamily, a distant homolog of the CorA Mg2+ transporter. The crystal structure of the cytoplasmic domain of Vp-ZntB from Vibrio parahaemolyticus reveals a funnel-shaped homopentamer with two subdomains per monomer: an N-terminal alpha/beta/alpha sandwich and a C-terminal coiled-coil stalk. At 1.90 A resolution, 25 well-defined Cl- ions were identified binding along the central pore, creating strong negative electrostatic potential that enhances cation transport. No Zn2+ or Cd2+ binding sites were found despite crystallization buffer containing divalent cations.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1002##pro.215 | 3CK6 | 1.90 A | P21 | Vp-ZntB cytoplasmic domain, residues 1-203, homopentamer | 25 Cl- ions per pentamer (5 per monomer) |

## Expression and Purification

- **Expression system**: not specified
- **Construct**: Vp-ZntB cytoplasmic domain (residues 1-203) from Vibrio parahaemolyticus

### Purification Workflow

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression and purification | Not specified in paper | -- | -- | Cytoplasmic domain expressed and purified; SeMet derivative used for phasing |


## Crystallization

### doi/10.1002##pro.215

| Parameter | Value |
|---|---|
| Method | not specified |
| Protein sample | Vp-ZntB cytoplasmic domain |
| Reservoir | Crystallization buffer included 0.2 M [MgCl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/) |
| Temperature | not specified |
| Growth time | not specified |
| Notes | High-resolution structure at 1.90 A. Se-SAD phasing at Se absorption edge. Anomalous data at Zn and low energy (7 keV) confirmed Cl- binding. 25 Cl- ions per pentamer identified. |


## Biological / Functional Insights

### Pentamer formation determinants

The cytoplasmic domain alone is sufficient to assemble a homopentamer, with the coiled-coil subdomain (alpha4, alpha5, alpha6 stalk helices) exclusively contributing to pentamer formation. Monomer-monomer interface buried area is ~2100 A2 per contact with favorable Gibbs free energy of -8.6 kcal/mol. The alpha6 stalk helix is the primary contributor; truncation at the middle of alpha6 would disrupt stability. This contrasts with previously reported CorA intracellular domain dimers, which are likely artifacts of extensive truncation.

### Chloride ion binding and electrostatics

Five Cl- ions per monomer bind at distinct sites: Cl-(1) and Cl-(2) are the highest peaks (6.1-8.5 sigma), Cl-(3) sits at the N-terminal end of alpha3 helix interacting with R113 and A114 amides, Cl-(4) interacts with R35, and Cl-(5) is at the inner funnel surface near R192. The Cl- ring neutralizes positive charges and creates strong negative electrostatic potential along the central pore, making it highly attractive for divalent cations. Continuum electrostatics calculations show the pore affinity for cations depends strongly on Cl- presence, removing the energy barrier at Z = -60 A.

### Full-length model and pore architecture

Homology model built on Tm-CorA (2.9 A) shows Vp-ZntB full-length pore is more open than Tm-CorA, with three constriction sites: below membrane (D235, K238, R241, D242), and two in transmembrane domain (S263, F259, F252). The aspartate ring at D242 corresponds to D277 in Tm-CorA. Ion selectivity attributed to signature motif G[I,V]N (ZntB) vs YGMNFxxMPEL (CorA) located between TM helices.


## Cross-References

- [CorA Mg2+ Transporter](/xray-mp-wiki/concepts/cora-mg-transporter/) — Structural homolog and reference for full-length modeling
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — General purification technique referenced
- [Membrane Protein Structural Biology Concepts](/xray-mp-wiki/concepts/membrane-mimetics/) — Related MIT superfamily structural principles
