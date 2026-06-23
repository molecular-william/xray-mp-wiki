---
title: "AdeB Multidrug Efflux Transporter"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-021-27146-2]
verified: false
---

# AdeB Multidrug Efflux Transporter

## Overview

AdeB is a multidrug efflux transporter from the Gram-negative pathogen Acinetobacter baumannii, belonging to the Resistance-Nodulation-Division (RND) superfamily. It forms the inner membrane pump component of the AdeABC tripartite efflux complex, together with the periplasmic adaptor AdeA and the outer membrane channel AdeC. AdeB functions as a homotrimer, with each protomer cycling through different conformational states. Single-particle cryo-electron microscopy revealed the AdeB trimer predominantly adopts a symmetric OOO resting state (3.54-3.84 A) with all protomers in a conformation devoid of transport channels or antibiotic binding sites. A second conformation, L*OO (3.84 A), was observed in approximately 10% of protomers, where three transport channels (CH1-CH3) lead to the closed deep binding pocket (DBP). The L* conformation represents a novel state not described for the homologous E. coli [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/abc-transporters/acrb/) transporter. Mutagenesis studies comparing AdeB and [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/abc-transporters/acrb/) substrate binding in the DBP using co-structures with doxycycline (2.1 A), fusidic acid (2.3 A), and levofloxacin (2.7 A) reveal distinct drug binding mechanisms between the two homologous RND pumps.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-021-27146-2 | 7B8Q | 3.84 | -- | AdeB from A. baumannii, full-length, in L*OO conformation | -- |
| doi/10.1038##s41467-021-27146-2 | 7B8R | 3.54 | -- | AdeB from A. baumannii, full-length, in OOO conformation (C3-symmetric) | -- |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: A. baumannii AdeB with C-terminal His10-tag, expressed in E. coli C43(DE3) Delta acrAB

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Fermentation | -- | TB medium (12 g/L tryptone, 24 g/L yeast extract, 5 g/L [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 2.31 g/L KH2PO4, 12.54 g/L K2HPO4) + -- | E. coli C43(DE3) Delta acrAB harboring p7XC3H_adeB |
| Membrane preparation | Ultracentrifugation | -- | Resuspension buffer + -- | Membrane fraction collected by ultracentrifugation |
| Solubilization | Detergent solubilization | -- | 20 mM [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 300 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Membranes solubilized in 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) with 12 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Affinity chromatography | Ni-NTA | HisPur Ni-NTA (Thermo Scientific) | 20 mM [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 300 mM NaCl, 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Washed with 20 mM and 80 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), eluted with 400 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Size-exclusion chromatography | SEC | Superose 6 increase 10/300 GL | 20 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 150 mM NaCl, 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Trimeric protein fractions collected at ~13 mL elution volume |


## Crystallization

### doi/10.1038##s41467-021-27146-2

| Parameter | Value |
|---|---|
| Method | [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) (single-particle) |
| Protein sample | Purified AdeB in 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 20 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 150 mM NaCl |
| Reservoir | -- |
| Temperature | -- |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) data collected on Titan Krios, processed with Relion 3.0. Final maps at 3.54 A (OOO) and 3.84 A (L*OO). Initial model generated with Phyre2 using PDB 4DX5 as template. Model refined with Phenix real-space refinement and Coot, validated with Molprobity. |


## Biological / Functional Insights

### OOO resting state predominates in AdeB

The AdeB trimer adopts predominantly a symmetric OOO conformation (all protomers in the O/extrusion state), in contrast to the asymmetric LTO states of [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/abc-transporters/acrb/). This conformation lacks drug entry channels and binding sites, suggesting tight regulation of AdeB activity. The high prevalence of the OOO state is not an artifact, as similar symmetric conformations have been observed in C. jejuni [Campylobacter jejuni CmeB Multidrug Efflux Pump](/xray-mp-wiki/proteins/abc-transporters/cmeb/) and another AdeB [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) study.

### L*OO - a novel pre-binding conformation

Approximately 10% of AdeB protomers adopt the L* conformation, a previously undiscovered state. L* reveals three entry tunnels (CH1-CH3) leading to the closed DBP, analogous to [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/abc-transporters/acrb/) channels. The L* protomer most closely resembles the [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/abc-transporters/acrb/) T conformation (RMSD 0.68 A over C-alpha), but PN2 and PC1 subdomains differ significantly from both L and T states. The L* conformation may be the first state in the AdeB transport cycle, allowing initial substrate entry in the absence of drugs.

### Different drug binding mechanisms between AdeB and AcrB

Mutagenesis of 20 AdeB DBP variants and comparison with [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/abc-transporters/acrb/) reveals distinct substrate preferences. AdeB confers higher resistance to polyaromatic compounds, while [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/abc-transporters/acrb/) shows higher resistance to non-polyaromatic antibiotics. For AdeB, drug binding may proceed via induced fit (drug binds to AP first, inducing DBP opening), whereas [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/abc-transporters/acrb/) appears to use conformational selection. Removal of bulky Phe/Tyr residues in the AdeB DBP generally widens the binding pocket, affecting substrate specificity differently than equivalent substitutions in [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/abc-transporters/acrb/).


## Cross-References

- [AcrB Multidrug Efflux Transporter](/xray-mp-wiki/proteins/abc-transporters/acrb/) — Homologous RND efflux transporter from E. coli; detailed structural and functional comparison in this study
- [MexB Multidrug Efflux Transporter](/xray-mp-wiki/proteins/abc-transporters/mexb/) — Homologous RND transporter from P. aeruginosa with similar tripartite efflux pump architecture
- [Multidrug Resistance Mechanisms](/xray-mp-wiki/concepts/multidrug-resistance/) — AdeB is a key RND efflux pump contributing to multidrug resistance in A. baumannii
- [Single-Particle Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/single-particle-cryo-em/) — AdeB structures determined by single-particle cryo-EM
- [X-ray Crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/) — Method used in the study
- [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) — Method used in the study
- [GR (Halobacterium sp. GR Bacteriorhodopsin)](/xray-mp-wiki/proteins/rhodopsins/gr/) — Related protein mentioned in the study
- [MexB (Pseudomonas aeruginosa multidrug exporter)](/xray-mp-wiki/proteins/abc-transporters/mexB/) — Related protein mentioned in the study
- [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/abc-transporters/acrb/) — Related protein mentioned in the study
- [Campylobacter jejuni CmeB Multidrug Efflux Pump](/xray-mp-wiki/proteins/abc-transporters/cmeb/) — Related protein mentioned in the study
