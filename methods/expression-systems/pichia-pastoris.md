---
created: 2026-05-19
updated: 2026-05-22
title: Pichia pastoris Expression System
type: method
category: methods
layout: default
tags: [expression-system]
sources: [doi/10.1016/j.bbapap.2015.02.008]
---

# Pichia pastoris Expression System

## Overview

Pichia pastoris (now reclassified as *Komagataella phaffii*) is a methylotrophic yeast widely used for heterologous protein expression, particularly for membrane proteins requiring proper folding and post-translational modifications. The system is driven by the AOX1 (alcohol oxidase 1) promoter, which is tightly regulated by carbon source availability: repressed by glucose, glycerol, or ethanol, and strongly induced by methanol. This methanol-inducible system enables controlled, high-level expression of recombinant proteins.

## Principle

The AOX1 promoter is one of the most powerful inducible promoters known, capable of driving expression levels up to 30% of total cellular protein. When cells are grown on glycerol or glucose, the AOX1 promoter is fully repressed. Addition of methanol derepresses and strongly induces transcription. The system uses the *aox1* gene locus for integration, and selection is typically performed using geneticin (G418) resistance or histidine auxotrophy complementation.

## Protocol

### Reagents

- **Media**: BMGY (buffered glycerol-complex medium) for cell growth; BMMY (buffered methanol-complex medium) for induction
- **Inducer**: Methanol (final concentration 0.5–1% v/v), added every 24–48 hours
- **Selection agent**: G418 (geneticin) at 1–200 µg/mL depending on copy number
- **Buffer salts**: Potassium phosphate buffer (pH 5.0–6.0) for media preparation

### Steps

1. **Transformation**: Linearize expression plasmid and transform into P. pastoris strain (e.g., SMD1168, GS115) via electroporation
2. **Selection**: Plate on YPD agar with appropriate selection agent (G418 for *arg4* integrants, histidine for *his4* integrants)
3. **Screening**: Colony PCR or growth tests to identify positive transformants
4. **Pre-culture**: Inoculate single colony into BMGY; grow at 30°C, 250 rpm until OD600 ≈ 2–6
5. **Induction**: Centrifuge cells, resuspend in BMMY; induce with methanol at 0.5–1% (v/v) every 24–48 hours
6. **Expression**: Typically 48–96 hours at reduced temperature (18–20°C) for improved folding
7. **Harvest**: Centrifuge at 3,000–5,000 × g for 15 min at 4°C; collect cell pellet or supernatant depending on secretion strategy

### Conditions

- **Pre-induction temperature**: 30°C
- **Induction temperature**: 18–20°C (for improved protein folding and solubility)
- **Induction duration**: 48–96 hours
- **Methanol feeding**: Every 24–48 hours at 0.5–1% (v/v)
- **Culture density**: OD600 2–6 at induction start

## Advantages

- **High expression levels**: AOX1 promoter can drive very high protein yields
- **Proper folding**: Eukaryotic folding machinery with disulfide bond formation capability
- **Post-translational modifications**: Glycosylation (though hypermannosylation can be an issue)
- **Scalability**: Easily scalable from shake flasks to fermenters
- **Secretion**: Proteins can be secreted into the medium, simplifying purification
- **Methanol regulation**: Tight control with minimal basal expression

## Disadvantages

- **Methanol toxicity**: Methanol is cytotoxic at high concentrations; careful feeding required
- **Glycosylation**: Hypermannosylation of N-glycans may interfere with crystallization
- **Proteolysis**: Secreted proteins may be degraded by yeast proteases
- **Slow growth**: Slower than E. coli, requiring longer expression times
- **Biosafety**: Methanol handling requires appropriate safety measures

## Proteins Using This Method

| Protein | Resolution | PDB | Notes |
|---|---|---|---|
| [NtMATE2](/xray-mp-wiki/proteins/ntmate2/) | 3.5 A | 7DQK | C-terminal GFP-His8 tagged; induced with 0.5% methanol at 20°C for 72 h in SMD1168 strain |

## Related Methods

- [Cell-Free Protein Synthesis](/xray-mp-wiki/methods/expression-systems/cell-free-protein-synthesis/) — Alternative expression system avoiding cellular constraints

## Related Reagents

- [Methanol](/xray-mp-wiki/reagents/additives/methanol/) — Primary inducer for AOX1 promoter system
- [G418 (Geneticin)](/xray-mp-wiki/reagents/additives/g418/) — Selection agent for yeast transformants
- [Glucose](/xray-mp-wiki/reagents/additives/glucose/) — Carbon source that represses AOX1 promoter
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Non-repressive carbon source for pre-induction growth
