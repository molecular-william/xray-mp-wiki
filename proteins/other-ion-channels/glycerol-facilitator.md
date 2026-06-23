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

[Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) Facilitator (GlpF) is a membrane transporter from Escherichia coli that facilitates rapid [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) transport across the cell membrane. The high-resolution X-ray crystal structure reveals a tetrameric channel with each monomer containing six transmembrane helices and two membrane-inserted non-membrane-spanning helices, sharing the same general topology as [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) water channels. The key structural difference from water-specific aquaporins is a wider, more hydrophobic constriction region that accommodates glycerol molecules, achieved by substituting glycine for the conserved histidine and phenylalanine for conserved cysteine found in the [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) constriction region.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.290.5497.481 | 1FX8 | 2.0 A | P43212 | Full-length E. coli [Glpf](/xray-mp-wiki/proteins/other-ion-channels/glpf/) | [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) molecules in the pore |
| doi/10.1038##414872a | 1FX8 | 2.0 A | P43212 | Full-length E. coli [Glpf](/xray-mp-wiki/proteins/other-ion-channels/glpf/) | -- |

## Expression and Purification

- **Expression system**: Not specified in this paper
- **Construct**: Full-length E. coli [Glpf](/xray-mp-wiki/proteins/other-ion-channels/glpf/)

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
| Protein sample | E. coli [Glpf](/xray-mp-wiki/proteins/other-ion-channels/glpf/) |
| Reservoir | Not specified in detail |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | -- |
| Notes | Crystals grown in the presence of [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) (cryoprotectant). Space group P43212, unit cell a = b = 89.6 A, c = 180.4 A. |


## Biological / Functional Insights

### Wider, more hydrophobic constriction region enables glycerol transport

The [Glpf](/xray-mp-wiki/proteins/other-ion-channels/glpf/) constriction region is nearly 1 A wider than that of water-specific [AQP1](/xray-mp-wiki/proteins/other-ion-channels/aqp1/). In GlpF, the conserved H182 of [AQP1](/xray-mp-wiki/proteins/other-ion-channels/aqp1/) is replaced by [Glycine](/xray-mp-wiki/reagents/buffers/glycine/), and C191 is replaced by phenylalanine. These substitutions increase the constriction size and hydrophobicity, allowing the larger [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) molecule to pass. The glycine substitution provides additional room, while the phenylalanine substitution makes the constriction more hydrophobic, both changes being critical for [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) permeability.

### Shared tetrameric architecture with aquaporins

[Glpf](/xray-mp-wiki/proteins/other-ion-channels/glpf/) shares the same general folding topology as aquaporins: six transmembrane helices, two membrane-inserted non-membrane-spanning helices, and an NPA motif in each half of the sequence. The tetrameric assembly is similar, with each monomer providing an independent transport pathway. This structural homology supports the classification of aquaporins and [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) facilitators within the same superfamily.

### Hydrophilic pore lining for solute coordination

A similar distribution of pore-lining carbonyl oxygens and asparagine amine groups as in [AQP1](/xray-mp-wiki/proteins/other-ion-channels/aqp1/) is found in GlpF. The short helices M3 and M7 are situated end-to-end with their positive helical dipole ends pointing inward toward the pore. This two-helix motif is found in both water- and [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/)-selective channels, suggesting it is a general structural feature rather than a selectivity determinant.


## Cross-References

- [Aquaporin-1 (AQP1)](/xray-mp-wiki/proteins/other-ion-channels/aqp1/) — Water-specific aquaporin used as structural comparison; AQP1 constriction region is narrower and more hydrophilic, excluding glycerol
- [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) — GlpF belongs to the aquaporin superfamily; shares conserved NPA motifs and general topology with water channels
- [Aquaporin Z (AqpZ)](/xray-mp-wiki/proteins/other-ion-channels/aquaporin-z/) — E. coli bacterial water channel homolog; shares common architecture with GlpF
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Referenced in glycerol-facilitator text
- [Glpf](/xray-mp-wiki/proteins/other-ion-channels/glpf/) — Referenced in glycerol-facilitator text
- [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) — Referenced in glycerol-facilitator text
