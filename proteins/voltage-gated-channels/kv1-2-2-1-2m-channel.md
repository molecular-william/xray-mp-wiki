---
title: Kv1.2-2.1-2m Chimeric Channel (W362F, S367T)
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1126##sciadv.abm8804]
verified: false
---

# Kv1.2-2.1-2m Chimeric Channel (W362F, S367T)

## Overview

The Kv1.2-2.1-2m channel is a double mutant (W362F, S367T) of the Kv1.2-2.1 chimeric voltage-gated K+ channel. Unlike the Kv1.2-2.1-3m channel (which additionally contains V377T), this construct shows inactivation properties similar to wild type. The crystal structure at 150 mM K+ (PDB 7SIZ) shows the selectivity filter in a conductive conformation, confirming that the V377T substitution is essential for stabilizing the C-type inactivated state by enabling the intersubunit Asp375-Thr377 interaction.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##sciadv.abm8804 | 7SIZ | Not specified (∼3.5 A range) | — | Kv1.2-2.1 chimera with W362F, S367T, co-expressed with rat Kv beta2 subunit | K+ |

## Expression and Purification

- **Expression system**: Pichia pastoris
- **Construct**: Kv1.2-2.1 chimera with W362F, S367T mutations, co-expressed with rat Kv beta2 subunit

### Purification Workflow

- **Expression system**: Pichia pastoris
- **Expression construct**: Kv1.2-2.1-2m (W362F/S367T) with beta2 subunit

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein production | Pichia pastoris expression | — |  | Similar protocol to Kv1.2-2.1-3m channel |


## Crystallization

### doi/10.1126##sciadv.abm8804

| Parameter | Value |
|---|---|
| Method | Hanging drop vapor diffusion |
| Protein sample | Kv1.2-2.1-2m-beta2 complex, 150 mM K+ |
| Reservoir | 100 mM Tris-HCl, 26-36% PEG 400 |
| Temperature | Room temperature |
| Growth time | Not specified |
| Notes | Protein-to-reservoir ratio 2:1. Structure determined at 150 mM K+. |


## Biological / Functional Insights

### V377T substitution stabilizes C-type inactivated state

The Kv1.2-2.1-2m (without V377T) shows slow inactivation similar to wild type. Comparison with the Kv1.2-2.1-3m structure demonstrates that the V377T substitution creates an intersubunit Asp375-Thr377 interaction that stabilizes the selectivity filter in the dilated, C-type inactivated conformation. The equivalent position in Shaker (T449) is a well-known locus for C-type inactivation; substitution with Val produces a noninactivating phenotype.


## Cross-References

- [Kv1.2-2.1-3m Chimeric Channel (C-type Inactivated State)](/xray-mp-wiki/proteins/voltage-gated-channels/kv1-2-2-1-3m-channel/) — Triple mutant (W362F, S367T, V377T) showing rapid C-type inactivation; 3m includes V377T which stabilizes inactivated state
- [Shaker Kv1.2 Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/shaker-kv1-2/) — Parent channel used as basis for chimera
- [C-type Inactivation](/xray-mp-wiki/concepts/c-type-inactivation/) — Demonstrates role of Thr at position 377 (Shaker T449) in C-type inactivation
