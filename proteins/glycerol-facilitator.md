---
title: Glycerol Facilitator (GlpF)
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##414872a, doi/10.1126##science.290.5497.481]
verified: false
---

# Glycerol Facilitator (GlpF)

## Overview

Glycerol Facilitator (GlpF) is a membrane transporter from Escherichia coli that facilitates rapid glycerol transport across the cell membrane. The high-resolution X-ray crystal structure reveals a tetrameric channel with each monomer containing six transmembrane helices and two membrane-inserted non-membrane-spanning helices, sharing the same general topology as aquaporin water channels. The key structural difference from water-specific aquaporins is a wider, more hydrophobic constriction region that accommodates glycerol molecules, achieved by substituting glycine for the conserved histidine and phenylalanine for conserved cysteine found in the aquaporin constriction region.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.290.5497.481 | 1FX8 | 2.0 A | P43212 | Full-length E. coli GlpF | Glycerol molecules in the pore |
| doi/10.1038##414872a | 1FX8 | 2.0 A | P43212 | Full-length E. coli GlpF | -- |

## Expression and Purification

- **Expression system**: Not specified in this paper
- **Construct**: Full-length E. coli GlpF

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Solubilization | Membrane solubilization | -- | -- + -- | Details described in reference (Fu et al. 2000) |


## Crystallization

### doi/10.1126##science.290.5497.481

| Parameter | Value |
|---|---|
| Method | Crystallization |
| Protein sample | E. coli GlpF |
| Reservoir | Not specified in detail |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | -- |
| Notes | Crystals grown in the presence of glycerol (cryoprotectant). Space group P43212, unit cell a = b = 89.6 A, c = 180.4 A. |


## Biological / Functional Insights

### Wider, more hydrophobic constriction region enables glycerol transport

The GlpF constriction region is nearly 1 A wider than that of water-specific AQP1. In GlpF, the conserved H182 of AQP1 is replaced by glycine, and C191 is replaced by phenylalanine. These substitutions increase the constriction size and hydrophobicity, allowing the larger glycerol molecule to pass. The glycine substitution provides additional room, while the phenylalanine substitution makes the constriction more hydrophobic, both changes being critical for glycerol permeability.

### Shared tetrameric architecture with aquaporins

GlpF shares the same general folding topology as aquaporins: six transmembrane helices, two membrane-inserted non-membrane-spanning helices, and an NPA motif in each half of the sequence. The tetrameric assembly is similar, with each monomer providing an independent transport pathway. This structural homology supports the classification of aquaporins and glycerol facilitators within the same superfamily.

### Hydrophilic pore lining for solute coordination

A similar distribution of pore-lining carbonyl oxygens and asparagine amine groups as in AQP1 is found in GlpF. The short helices M3 and M7 are situated end-to-end with their positive helical dipole ends pointing inward toward the pore. This two-helix motif is found in both water- and glycerol-selective channels, suggesting it is a general structural feature rather than a selectivity determinant.


## Cross-References

- [Aquaporin-1 (AQP1)](/xray-mp-wiki/proteins/aqp1/) — Water-specific aquaporin used as structural comparison; AQP1 constriction region is narrower and more hydrophilic, excluding glycerol
- [Aquaporin Family](/xray-mp-wiki/concepts/aquaporin/) — GlpF belongs to the aquaporin superfamily; shares conserved NPA motifs and general topology with water channels
- [Aquaporin Z (AqpZ)](/xray-mp-wiki/proteins/aquaporin-z/) — E. coli bacterial water channel homolog; shares common architecture with GlpF
