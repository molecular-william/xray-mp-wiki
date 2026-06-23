---
title: Tubulin-DARPin Complex (TD1)
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-017-00630-4]
verified: false
---

# Tubulin-DARPin Complex (TD1)

## Overview

The Tubulin-DARPin complex (TD1) is a model system for studying ligand binding to the colchicine site of tubulin. The complex consists of αβ-tubulin heterodimers bound to a designed ankyrin repeat protein (DARPin), which stabilizes the complex for crystallization. TD1 was used as a test case for serial millisecond crystallography (SMX) at room temperature, demonstrating ligand soaking with colchicine and rapid data convergence for structure-based drug design applications. Structures were determined for both the apo (TD1_apo) and colchicine-bound (TD1_col) forms.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-017-00630-4 | 5NM2 | 2.6 | Not specified | αβ-tubulin with DARPin. Colchicine-free (apo) form. Crystallized from 22% PEG 3350, 0.2 M ammonium sulfate, 0.1 M Bis-Tris methane pH 5.5. | None |
| doi/10.1038##s41467-017-00630-4 | 5NM4 | 2.8 | Not specified | αβ-tubulin with DARPin. Colchicine-soaked form. Crystals incubated 2 hours with 3.7 mM colchicine and 3.7% DMSO before data collection. | [Colchicine](/xray-mp-wiki/reagents/ligands/colchicine/) |

## Expression and Purification

- **Expression system**: Not specified
- **Construct**: αβ-tubulin with DARPin
- **Notes**: Source materials and expression details can be found in the original publication and its references.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein preparation | Not specified | — |  | TD1 complex was prepared as described in referenced methods. Crystallization: 22% PEG 3350, 0.2 M ammonium sulfate, 0.1 M Bis-Tris methane pH 5.5. |


## Crystallization

### doi/10.1038##s41467-017-00630-4

| Parameter | Value |
|---|---|
| Method | Not specified |
| Protein sample | TD1 complex |
| Reservoir | 22% PEG 3350, 0.2 M ammonium sulfate, 0.1 M Bis-Tris methane pH 5.5 |
| Temperature | Not specified |
| Growth time | Not specified |
| Notes | For colchicine soaking: 6 µL 100 mM colchicine in 100% DMSO, 6 µL crystallization buffer, 18 µL monoolein mixed to make 20 mM colchicine/20% DMSO. 5 µL ligand mixture mixed 100× with 22 µL crystals in LCP, final 3.7 mM colchicine/3.7% DMSO. 2 h incubation. |


## Biological / Functional Insights

### SMX enables rapid ligand soaking and detection for fragment screening

The TD1-colchicine experiment showed that SMX can detect bound ligands within minutes of data collection. Data convergence reached 90% of the final SA-omit map cross-correlation with just 3–35 minutes of data collection (3,000– 20,000 diffraction patterns). This makes SMX particularly well-suited for automated fragment screening and structure-based drug design.

### Room temperature reveals distinct protein dynamics

Comparison of room-temperature (SMX) and cryo-structures of TD1 revealed conformational differences in loop mobility patterns. The T7 loop of β-tubulin (which shields ligands at the colchicine site) is more flexible at room temperature, while the T5 loop of α-tubulin is more rigid. The reverse pattern was observed in cryo-structures, suggesting that cryo-cooling may alter conformational ensembles in ways relevant to understanding ligand binding.


## Cross-References

- [Serial Millisecond Crystallography (SMX)](/xray-mp-wiki/concepts/serial-millisecond-crystallography/) — SMX method used for room-temperature data collection and ligand soaking experiments.
- [Colchicine](/xray-mp-wiki/reagents/ligands/colchicine/) — Ligand soaked into TD1 crystals for the colchicine-bound structure.
