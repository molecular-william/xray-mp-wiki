---
title: Paddle-Chimaera Voltage-Dependent Potassium Channel
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein]
sources: [doi/10.1038##nature06265]
verified: false
---

# Paddle-Chimaera Voltage-Dependent Potassium Channel

## Overview

The paddle-chimaera channel is a chimeric voltage-dependent K+ (Kv) channel constructed by replacing the voltage-sensor paddle (S3b-S4 helix-turn-helix) of rat Kv1.2 with the corresponding region from rat Kv2.1. The structure was determined at 2.4 A resolution in a lipid membrane-like environment, with the pore and voltage sensors embedded in a bilayer-like arrangement of lipid molecules. This high-resolution structure revealed detailed atomic interactions of voltage sensors within a membrane environment, including charge stabilization by external and internal negative clusters, a phenylalanine gap separating the clusters, and the conformation of gating charges in the open state.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature06265 | not specified | 2.4 | P42(1)2 | Paddle-chimaera channel (Kv1.2 backbone with Kv2.1 paddle residues VAIIPYYVTIFLTESNKSVLQFQNVRRVVQIFRIMRILRIFK), co-expressed with rat beta2.1 subunit in Pichia pastoris | K+, NADP+ |

## Expression and Purification

### Purification Workflow

- **Expression system**: Pichia pastoris
- **Expression construct**: Paddle-chimaera channel with N-terminal His10 tag and thrombin cleavage site, co-expressed with rat beta2.1 subunit (residues 36-367)
- **Tag info**: N-terminal His10 tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Yeast transformation and expression | Pichia pastoris fermentation | — |  | Co-expression of paddle-chimaera channel and beta2.1 subunit |
| Cobalt affinity chromatography | Affinity chromatography | Cobalt affinity column | not specified | Protein concentrated to ~20 mg/ml after elution |
| Gel filtration | Size-exclusion chromatography | Superdex-200 | 150 mM KCl, 20 mM Tris-HCl pH 7.5, 1 mM EDTA, 2 mM TCEP, 10 mM DTT + 3 mM Cymal-6, 3 mM Cymal-7 | Lipids (3:1:1 POPC:POPE:POPG at 0.1 mg/ml) included in gel filtration buffer. Elution between 11-12 ml showed correct Kv1.2:beta2.1 ratio. |

**Final sample**: ~10 mg/ml in gel filtration buffer


## Crystallization

### doi/10.1038##nature06265

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | Paddle-chimaera channel at 10 mg/ml in gel filtration buffer |
| Reservoir | 28-36% PEG 400, 50 mM Tris-HCl pH 8.5 |
| Temperature | 20 |
| Growth time | 5 days |
| Notes | Crystals approximately 200 um in each dimension. Detergents Cymal-6, Cymal-7, and CHAPS present. Lipids POPC, POPE, POPG present. Space group P42(1)2. Data collected to 2.4 A at NSLS beamline X29. Structure solved by molecular replacement using Kv1.2 structure (PDB 2A79) as search model. |


## Biological / Functional Insights

### Voltage-sensor architecture in a membrane-like environment

The 2.4 A structure reveals the voltage sensor in atomic detail within a membrane-like arrangement of lipids. The voltage-sensor paddle (S3b-S4) is tilted away from the central axis of the voltage sensor, towards the lipid membrane, making minimal contact with the remainder of the channel. One entire face of the voltage-sensor paddle is exposed to the lipid membrane.

### Negative clusters and the phenylalanine gap

Negatively charged amino acids form two clusters: an external negative cluster (Glu183 in S1, Glu226 in S2) and an internal negative cluster (Glu154 in S0, Glu236 in S2, Asp259 in S3a), separated by approximately 15 A. Phe233, the single most conserved amino acid in Kv channels outside the selectivity filter, separates the two clusters in a 'phenylalanine gap' - a hydrophobic zone of roughly 10 A that may create an energy barrier for arginine side chains, preventing proton transfer and favoring a switch-like transition between closed and open conformations.

### Gating charge disposition in the open state

In the open conformation, positively charged residues on S4 are positioned such that R0, R1, and R2 are in or close to the extracellular solution. R3 and R4 form ionized hydrogen bonds with the external negative cluster. K5 and R6 form ionized hydrogen bonds with the internal negative cluster. The S4 helix adopts a 3_10-helix hydrogen-bonding pattern below position 296 (R3), stretching the helix and allowing the voltage-sensor paddle to reside closer to the extracellular side.

### Lipid interactions and bilayer-like arrangement

Multiple complete and/or partial lipid molecules surround the channel, with a bilayer-like arrangement near the protein surface. Lipids are most dense in the concave hemi-circles between voltage sensors. A displaced phospholipid molecule is wedged between the voltage sensor and the S4-S5 linker, a region that couples voltage-sensor motions to pore gating.

### Gating mechanism inferred from structure

The structure suggests that during closure, the voltage-sensor paddle moves relative to S1 and S2, translating S4 gating charges ~15 A towards the intracellular side. The 3_10-helical region may shift as a moving segment along S4 in a wave-like 'concertina effect', turning arginine residues away from the lipid membrane as they cross the hydrophobic core.


## Cross-References

- [Shaker Kv1.2 Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/shaker-kv1-2/) — Parent channel backbone for the paddle-chimaera construct
- [KvAP Voltage-Dependent Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kvap/) — Prokaryotic Kv channel used for structural comparison
- [Voltage-Sensor Paddle](/xray-mp-wiki/concepts/construct-design/voltage-sensor-paddle/) — The voltage-sensor paddle concept characterized by this structure
