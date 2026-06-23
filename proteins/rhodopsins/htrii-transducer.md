---
title: HtrII Transducer (Sensory Rhodopsin II Transducer)
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##NATURE01109]
verified: false
---

# HtrII Transducer (Sensory Rhodopsin II Transducer)

## Overview

HtrII (Halobacterial transducer for sensory rhodopsin II) is the cognate
transmembrane transducer protein that forms a tight complex with sensory
rhodopsin II (NpSRII) from Natronobacterium pharaonis. HtrII mediates
phototaxis signal transduction by coupling light activation of SRII to a
downstream two-component signalling cascade homologous to eubacterial
chemotaxis. The transducer contains two transmembrane helices (TM1, TM2)
and a cytoplasmic domain that interacts with CheA-like histidine kinases.
A truncated construct comprising residues 1-114 (HtrII_114) retains the
two TM helices and a short cytoplasmic fragment and forms a functionally
unimpaired complex with SRII.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##NATURE01109 |  | 1.94 | Orthorhombic | HtrII_114 (residues 1-114, C-terminal truncated) in complex with NpSRII |  |

## Expression and Purification

- **Expression system**: Escherichia coli BL21 (DE3)
- **Construct**: C-terminal 7x His-tagged HtrII_114 (residues 1-114)
- **Notes**: Co-expressed and co-purified with NpSRII

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Affinity purification | Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | — | Imidazole-containing buffer | His-tagged HtrII_114 purified via C-terminal His tag |
| [Ion-Exchange Chromatography](/xray-mp-wiki/methods/purification/ion-exchange-chromatography/) | DEAE chromatography | — | Buffer with 2% n-octyl-beta-D-glucopyranoside | Imidazol removed by DEAE chromatography before complex formation |


## Crystallization

### doi/10.1038##NATURE01109

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | NpSRII-HtrII_114 complex (1:1 ratio) reconstituted into H. salinarum polar lipids |
| Lipid | Monovacccin |
| Temperature | 22°C |
| Growth time | Not specified |
| Notes | Thin orange orthorhombic crystals ~140 um. Complex solubilized in 2% n-octyl-beta-D-glucopyranoside, 150 mM NaCl, 25 mM Na/KPi pH 5.1. Data collected at ESRF beamline ID14-1. |


## Biological / Functional Insights

### SRII-HtrII complex structure reveals signal transduction interface

The 1.94 A structure of the NpSRII-HtrII_114 complex reveals how the
transducer TM1 and TM2 helices pack against receptor helices F and G.
The complex forms a dimer along a crystallographic two-fold axis with
TM1-TM2 TM1'-TM2' packing. The transducer extends ~3 helical turns
beyond the extracellular side (residues 44-59), a structural element
absent in HtrI but present in H. salinarum HtrII. High B-factors at
the cytoplasmic ends indicate conformational flexibility essential for
signal transduction. The structure supports a mechanism where light-
induced outward motion of SRII helix F triggers a clockwise rotation
of TM2, which propagates the signal to the downstream CheA/CheY
two-component cascade.


## Cross-References

- [Sensory Rhodopsin II (NpSRII)](/xray-mp-wiki/proteins/rhodopsins/sensory-rhodopsin-ii/) — HtrII forms a tight complex with NpSRII and mediates phototaxis signal transduction
- [Two-Component Signaling System (TCS) in Membrane Sensors](/xray-mp-wiki/concepts/two-component-signaling-system/) — HtrII links SRII photoactivation to the CheA/CheY two-component signalling cascade
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Ion-Exchange Chromatography](/xray-mp-wiki/methods/purification/ion-exchange-chromatography/) — Method used in structure determination or purification
