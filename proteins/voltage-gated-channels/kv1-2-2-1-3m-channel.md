---
title: Kv1.2-2.1-3m Chimeric Channel (C-type Inactivated State)
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1126##sciadv.abm8804]
verified: false
---

# Kv1.2-2.1-3m Chimeric Channel (C-type Inactivated State)

## Overview

The Kv1.2-2.1-3m channel is a triple mutant (W362F, S367T, V377T) of the Kv1.2-2.1 chimeric voltage-gated K+ channel that exhibits a ~2000-fold increase in the rate of C-type inactivation at high (100 mM) external K+. The crystal structure was determined at 3.35 A resolution (PDB 7SIT) and reveals the selectivity filter in a C-type inactivated state. The structure shows dilation of the selectivity filter at the S1 and S2 ion binding sites, caused by reorientation of the conserved Tyr373 and Asp375 side chains, which creates a widened vestibule. The S3 and S4 sites remain intact. Structural changes propagate to the extracellular mouth and turret regions. The structure supports the dilation model for C-type inactivation and provides a mechanism for the effect of extracellular K+ on inactivation.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##sciadv.abm8804 | 7SIT | 3.35 | P4 2_1 2 | Kv1.2-2.1 chimera with W362F, S367T, V377T mutations, co-expressed with rat Kv beta2 subunit | K+ |

## Expression and Purification

- **Expression system**: Pichia pastoris (co-expression with rat Kv beta2 subunit)
- **Construct**: Kv1.2-2.1 chimera with W362F, S367T, V377T mutations, N207Q, co-expressed with rat Kv beta2 subunit
- **Notes**: The Kv1.2-2.1 chimera substitutes residues 267-302 in the S3-S4 loop of Kv1.2 with residues 274-305 of Kv2.1 for improved crystallographic properties.

### Purification Workflow

- **Expression system**: Pichia pastoris
- **Expression construct**: Kv1.2-2.1-3m (W362F/S367T/V377T) with beta2 subunit, cloned into pPicZ-C vector

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Cryogenic milling | -- | 50 mM Tris-HCl pH 7.5, 150 mM KCl, 2 mM TCEP, 10 mM beta-mercaptoethanol, DNase I, protease inhibitors + -- | Six cycles of milling at 25 Hz for 3 min; cells kept cold with liquid nitrogen between cycles |
| Membrane solubilization | Detergent solubilization | -- | 50 mM Tris-HCl pH 7.5, 150 mM KCl, 2 mM TCEP, 10 mM beta-mercaptoethanol + 1.5% (w/v) n-dodecyl-beta-D-maltopyranoside (DDM) | Solubilized for 3 h at room temperature; unsolubilized material removed by ultracentrifugation (100,000g, 50 min) |
| Affinity chromatography | Cobalt affinity | Cobalt resin | 50 mM Tris-HCl pH 7.5, 150 mM KCl, 2 mM TCEP, 10 mM beta-mercaptoethanol, 5 mM DDM + 5 mM DDM | Incubated overnight at 4°C with gentle rotation; washed with 20 volumes of column buffer containing lipids (0.1 mg/ml POPC:POPE:POPG 3:1:1) and 20 mM imidazole; eluted with 400 mM imidazole |
| Size-exclusion chromatography | SEC | Superdex S200 | 20 mM Tris-HCl pH 7.5, 150 mM KCl, 2 mM TCEP, 10 mM DTT, 1 mM EDTA, lipids (0.1 mg/ml) (3:1:1 POPC:POPE:POPG) + 3 mM Cymal-6, 3 mM Cymal-7 | Eluted protein supplemented with 10 mM DTT, concentrated using Millipore Amicon Ultra 100K device |

**Final sample**: Kv1.2-2.1-3m-beta2 complex in lipid/detergent mixture with reducing agents


## Crystallization

### doi/10.1126##sciadv.abm8804

| Parameter | Value |
|---|---|
| Method | Hanging drop vapor diffusion |
| Protein sample | Kv1.2-2.1-3m-beta2 complex in buffer with 8 mM CHAPS, 150 mM K+ |
| Reservoir | 100 mM Tris-HCl pH 8.2-8.8, 26-36% PEG 400 |
| Temperature | Room temperature |
| Growth time | 4-5 days |
| Cryoprotection | PEG 400 concentration increased to 35% in well solution for 24 h, then frozen in liquid N2 |
| Notes | Protein-to-reservoir ratio 1:1. Rod-shaped crystals. Data collected at APS (beamlines 23ID-B and 23ID-D). Multiple crystals combined for complete dataset. |


## Biological / Functional Insights

### Selectivity filter dilation in C-type inactivated state

The structure reveals that C-type inactivation involves a dilation of the selectivity filter at the S1 and S2 ion binding sites. The conserved Tyr373 reorients from facing the channel interior to facing the extracellular solution. Asp375 undergoes a corresponding conformational change. Together these changes widen the selectivity filter, disrupting the S1 and S2 K+ binding sites. The S3 and S4 sites remain intact with K+ bound. This is consistent with the dilation model for C-type inactivation proposed by Hoshi and Armstrong.

### Mechanism for external K+ effect on inactivation

The disruption of S1 and S2 sites provides a mechanism for the effect of extracellular K+ on C-type inactivation. When external K+ is high, occupancy of S1 and S2 sites increases, which slows the structural changes at these sites and thereby slows inactivation. This explains why elevated external K+ slows C-type inactivation.

### Propagation of structural changes to extracellular mouth

Changes at the selectivity filter propagate to the loop region linking the filter to TM6. The repositioning of Asp375 leads to increased surface exposure of residues 376-378 (equivalent to Shaker positions 448-450), consistent with previous studies showing enhanced modification rates of Cys substitutions at these positions in the inactivated state.

### Intersubunit Asp375-Thr377 interaction stabilizes inactivated state

The V377T substitution creates a new intersubunit hydrogen bond between Asp375 and Thr377 that stabilizes the selectivity filter in the C-type inactivated conformation. The Kv1.2-2.1-2m construct (W362F, S367T without V377T) shows slow inactivation similar to wild type, and its crystal structure (PDB 7SIZ) shows a conductive selectivity filter, confirming the importance of the Asp375-Thr377 interaction.

### E346-S6 loop coupling

The V377T substitution also affects the interaction of E346 in the S4-S5 linker with the pore-S6 loop region. In the inactivated structure, E346 forms a new H-bond with the protein backbone of Thr379, breaking previous H-bond interactions with Thr379 backbone and Thr380 side chain.


## Cross-References

- [Shaker Kv1.2 Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/shaker-kv1-2/) — Parent channel; wild-type Kv1.2-2.1 structure (PDB 2R9R) used as molecular replacement model
- [Kv1.2-2.1 V406W Mutant Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kv1-2-2-1-v406w/) — Previously proposed C-type inactivated state structure; comparison of filter dilation magnitude
- [C-type Inactivation](/xray-mp-wiki/concepts/c-type-inactivation/) — Primary structural evidence for selectivity filter dilation in C-type inactivation
- [KcsA Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) — KcsA inactivation mechanism shares similarity with C-type inactivation in Kv channels
