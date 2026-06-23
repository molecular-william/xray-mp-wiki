---
title: "Human Gonadotropin-Releasing Hormone Receptor (GnRH1R)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-020-19109-w]
verified: true
---

# Human Gonadotropin-Releasing Hormone Receptor (GnRH1R)

## Overview

The human gonadotropin-releasing hormone receptor (GnRH1R, also known as luteinizing hormone-releasing hormone receptor) is a class A [GPCR](/xray-mp-wiki/concepts/signaling-receptors/gpcr/) that serves as the central regulator of the reproductive system. Activated by the decapeptide GnRH via the G_q signaling pathway, GnRH1R initiates the reproductive hormone cascade and releases gonadotropins (FSH and LH). The crystal structure of GnRH1R bound to the FDA-approved small-molecule antagonist drug elagolix at 2.8 Å resolution reveals an enlarged orthosteric binding pocket co-occupied by elagolix and the receptor N-terminus. Uniquely among class A GPCRs, GnRH1R lacks a cytoplasmic C-terminal helix and exhibits distinct microswitch structural features including a special N^2.50-D^7.49 pair and a hydrophobic Y^6.51-Y^6.52-W^6.48-F^6.44 motif in TM6 critical for signal transmission.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-020-19109-w | 7BR3 | 2.8 |  | Engineered construct: ICL3 (residues 243-256) replaced with thermostable Pyrococcus abyssi glycogen synthase (PGS) domain. Mutation: P128^3.39K for improved homogeneity. | Elagolix (NBI-56418) |

## Expression and Purification

- **Expression system**: Baculovirus/Sf9 insect cells
- **Construct**: HA signal sequence + FLAG tag at N-terminus; 10x His tag at C-terminus. ICL3 replaced with PGS domain. Mutation: P128^3.39K.

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell harvest | Sf9 insect cells infected with baculovirus; harvested 48 h post-infection | — |  |  |
| Membrane preparation | Homogenization and ultracentrifugation | — |  |  |
| Solubilization | DDM with CHS | — |  |  |
| Affinity chromatography | Nickel IMAC for His-tag capture | — |  |  |
| Size-exclusion chromatography | SEC in DDM/CHS buffer | — |  |  |
| Concentration | Concentrated with elagolix for crystallization | — |  |  |


## Crystallization

### doi/10.1038##s41467-020-19109-w

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | GnRH1R-PGS-elagolix complex |
| Temperature | 20 C |
| Notes | Data collected at Shanghai Synchrotron Radiation Facility (SSRF) BL17U. Structure solved by molecular replacement using PGS domain as search model. |


## Biological / Functional Insights

### Unusual N-terminus co-occupancy of orthosteric pocket

The N-terminus of GnRH1R inserts into the enlarged orthosteric binding pocket and co-occupies it together with elagolix. Residues L23 and M24 of the N-terminus pack alongside the ligand. The N-terminus is not involved in agonist GnRH binding but participates in small-molecule antagonist binding. The M24A mutation caused almost complete loss of elagolix inhibition of GnRH-induced response.

### Shallow antagonist binding site

Unlike other beta-branch GPCRs where ligands extend deeply into the orthosteric pocket and contact the toggle switch W^6.48, elagolix sits close to the top of the classical pocket and contacts Y283^6.51. Y283^6.51 together with Y284^6.52 and M125^3.36 form the bottom wall of the orthosteric pocket, decreasing ligand-binding cavity depth and blocking access to the toggle switch area. This shallow binding mode was further validated by docking of relugolix and sufugolix.

### Distinct microswitch features

GnRH1R lacks the conserved D^2.50 (replaced by N^2.50) and lacks a cytoplasmic C-terminal helix. The N^2.50-D^7.49 pair forms direct polar interactions and is critical for receptor activation. The hydrophobic Y^6.51-Y^6.52-W^6.48-F^6.44 motif in TM6 is critical for signal transmission upon extracellular stimuli. The Y283^6.51, Y284^6.52, and W280^6.48 residues greatly contribute to GnRH1R activation.


## Cross-References

- [GPCR](/xray-mp-wiki/concepts/signaling-receptors/gpcr/) — GnRH1R is a class A GPCR
