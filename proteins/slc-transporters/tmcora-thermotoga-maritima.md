---
title: CorA Magnesium Transporter from Thermotoga maritima
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##sj.emboj.7601269]
verified: false
---

# CorA Magnesium Transporter from Thermotoga maritima

## Overview

CorA from Thermotoga maritima (TmCorA) is the primary Mg2+ uptake system in prokaryotes, belonging to the CorA superfamily of divalent cation transporters. The structure reveals a funnel-shaped pentameric assembly with a ~55 Å long pore, featuring a cytoplasmic funnel domain and a transmembrane domain. This work provides a structural basis for Mg2+ homeostasis, including a divalent cation sensor mechanism, and proposes an open state model for the CorA translocation cycle.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##sj.emboj.7601269 | 2BBJ | 3.7 | P21212 | TmCorA1-351 | Ca2+ |
| doi/10.1038##sj.emboj.7601269 | 2BBH | 1.85 | P41212 | TmCorA_SGC-266 | none |

## Expression and Purification

- **Expression system**: Escherichia coli

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein purification | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | — | 20 mM Tris pH 8.0, 100 mM NaCl, 1 mM TCEP + 0.026% n-dodecyl-beta-D-maltoside |  |


## Crystallization

### doi/10.1038##sj.emboj.7601269

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Reservoir | 200 mM CaCl2, 100 mM HEPES pH 7.5, 30% [PEG](/xray-mp-wiki/reagents/additives/peg/) 400 |
| Temperature | 20 |
| Notes | Crystals obtained in the presence of 200 mM CaCl2 |


## Biological / Functional Insights

### Global Divalent Cation Sensor

Ten metal-binding sites within the cytoplasmic funnel domain function
as a physiologically tuned divalent cation sensor. The sensor acts as
a Mg2+-specific homeostatic molecular switch, responding to intracellular
Mg2+ concentrations centered around ~0.5 mM. The Asp253-to-Lys253 mutant
(DK) locks the transporter in a protected conformation even in the absence
of Mg2+, confirming the sensor mechanism.

### Open State Model and Translocation Cycle

A major conformational change is observed between the soluble AfCorA1-263
domain structure and full-length TmCorA, revealing a two-state mechanism.
The CorA elbow (alpha5-alpha6 loop) and the swivel helix (alpha6) mediate
a ~105 degree rotation around alpha7, opening the pore. The open state
model explains how low intracellular Mg2+ promotes transport.

### Selectivity Filter and Pore Architecture

The CorA pore is ~55 Å long with a sparingly polar character. A hydrated
metal at Site A near the GMN motif sits ~10 Å into the membrane and
represents the selectivity filter. The hydrophobic girdle (Leu294) and
hydrophobic belt (Thr305/Met302) create constrictions that require
substrate dehydration. A "linked-beads" translocation model is proposed
where cations move in discrete steps along the pore.


## Cross-References

- [Escherichia coli CorA Mg2+ Channel (Cytoplasmic Domain)](/xray-mp-wiki/proteins/abc-transporters/ec-cor-a/) — Homologous CorA protein from E. coli
- [Tris](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component in purification
- [n-Dodecyl-beta-D-Maltoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for solubilization
- [TCEP](/xray-mp-wiki/reagents/additives/tcep/) — Reducing agent in purification buffer
- [Sodium Chloride](/xray-mp-wiki/reagents/sodium-chloride/) — Salt component in purification buffer
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
