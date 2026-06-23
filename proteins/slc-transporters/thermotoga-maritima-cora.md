---
title: Thermotoga maritima CorA Mg2+ Transporter
created: 2026-06-10
updated: 2026-06-10
type: protein
category: proteins
layout: default
tags: [transporter, ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature04642, doi/10.1126##science.1127121]
verified: false
---

# Thermotoga maritima CorA Mg2+ Transporter

## Overview

The [CorA Magnesium Transporter from Thermotoga maritima](/xray-mp-wiki/proteins/slc-transporters/tmcora-thermotoga-maritima/) is the founding structural model for the CorA/MRS2 family of Mg2+ transporters, which constitute the primary Mg2+ uptake system in most prokaryotes and functional homologues of the eukaryotic mitochondrial magnesium transporter. The structure was determined as a full-length protein in an apparent closed state at 3.9 A resolution (Nature 2006) and subsequently at 2.9 A resolution (Science 2006). The transporter is a funnel-shaped homopentamer with two transmembrane helices per monomer. The channel pore is formed by five inner helices and putatively gated by bulky hydrophobic residues. The cytoplasmic domain forms a large funnel with metal-binding regulatory sites (M1, M2) that sense intracellular Mg2+ concentration.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature04642 | 2BBJ | 1.85 | Not specified | N-terminal soluble domain of T. maritima CorA (residues 1-266) | Mg2+, Na+ |
| doi/10.1038##nature04642 | 2IUB | 3.9 | Not specified | Full-length T. maritima CorA | Putative Mg2+ |
| doi/10.1126##science.1127121 | 2IUB | 2.9 | Not specified | Full-length T. maritima CorA | Mg2+, Co2+ (soak), Cl- |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Full-length Thermotoga maritima CorA

### Purification Workflow

*Source: doi/10.1038##nature04642*

- **Expression system**: Escherichia coli
- **Expression construct**: Full-length T. maritima CorA and N-terminal domain (residues 1-266) as fusions to N-terminal six-histidine tag in modified T7 polymerase expression vector

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane isolation | Centrifugation | — | 50 mM HEPES pH 7.5, 500 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 1% n-dodecyl-beta-D-maltopyranoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Protease inhibitors added to lysis buffer |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Nickel [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA | 50 mM HEPES pH 7.5, 500 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |  |

### Purification Workflow

*Source: doi/10.1126##science.1127121*

- **Expression system**: Escherichia coli
- **Expression construct**: Full-length T. maritima CorA

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | E. coli expression | — |  | Expression and purification of full-length TmCorA |


## Crystallization

### doi/10.1038##nature04642

| Parameter | Value |
|---|---|
| Method | [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) |
| Protein sample | Full-length T. maritima CorA |
| Reservoir | 20% (w/v) [PEG 2000](/xray-mp-wiki/reagents/additives/peg2000/), 0.3 M Mg(NO3)2, 0.1 M Tris pH 8.0 |
| Temperature | Room temperature |
| Notes | Crystals of full-length CorA diffracted to 3.9 A |

| Parameter | Value |
|---|---|
| Method | [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) |
| Protein sample | Soluble N-terminal domain (residues 1-266) |
| Reservoir | 35% (w/v) [PEG](/xray-mp-wiki/reagents/additives/peg/) 3350, 0.2 M MgCl2, 0.1 M Tris pH 8.5 |
| Temperature | Room temperature |
| Notes | Soluble domain crystallized to 1.85 A |

### doi/10.1126##science.1127121

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Full-length T. maritima CorA |
| Notes | 100 mM MgCl2 present during crystallization. Crystals diffracted to 2.9 A resolution. |


## Biological / Functional Insights

### Funnel-shaped homopentameric architecture

The CorA transporter is a homopentamer with five-fold symmetry about a central pore. The pore is narrowest at three rings formed by Met291, Leu294, and Met302. At the cytosolic side, the pore diameter rapidly increases around Asp277, leading to a funnel-shaped cavity formed by the N-terminal domain. The conserved GMN sequence (residues 312-314) occurs just after the first TM segment on the periplasmic side.

### Two regulatory metal-binding sites (M1 and M2)

Two metal-binding sites were identified at 2.9 A resolution using anomalous scattering from Co2+ soaks. M1 is directly coordinated by Asp89 and Asp253 (distances ~2.2 A), with a second coordination sphere of hydrogen-bonding residues (Asn92, Gln95, Glu100, Asp256, His257). M2 is located ~7 A from M1, surrounded by Leu12, Glu88, Asp175, and Asp253, likely binding a hydrated metal ion with water-mediated coordination. These metal-binding sites are conserved in class II CorAs and likely regulate transport activity.

### Aspartate ring at the pore entrance

A ring formed by five symmetry-related Asp277 residues at the entrance of the pore shows significant residual density (~4.5 sigma in Fo-Fc maps), attributed to bound Mg2+ ions. This aspartate ring is highly conserved among class II CorAs and may determine selectivity or form a binding site for inhibitory cations, analogous to the aspartate ring in the TolC transport system.

### Unique pore architecture

The CorA pore differs from other cation channels, with extensive hydrophobic interactions in the interior and few polar groups (Ser284, Thr287, Thr305). The pore has several narrow regions lacking appropriate polar groups for cation interactions along more than two-thirds of its ~60 A length, suggesting that gating and transport mechanisms may differ from previously studied cation-transport systems.


## Cross-References

- [KvAP Voltage-Dependent Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kvap/) — Both are prokaryotic membrane protein structures solved at similar resolutions
- [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) — Method used in structure determination or purification
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [CorA Magnesium Transporter from Thermotoga maritima](/xray-mp-wiki/proteins/slc-transporters/tmcora-thermotoga-maritima/) — Related protein structure
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [PEG 2000](/xray-mp-wiki/reagents/additives/peg2000/) — Additive used in purification or crystallization buffers
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used in purification or crystallization
