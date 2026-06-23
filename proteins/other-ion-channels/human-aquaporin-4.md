---
title: Human Aquaporin 4 (hAQP4)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein]
sources: [doi/10.1073##pnas.0902725106]
verified: false
---

# Human Aquaporin 4 (hAQP4)

## Overview

Human [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) 4 (hAQP4) is the predominant water channel in the mammalian brain, expressed at the blood-brain and brain-cerebrospinal fluid interfaces of glial cells. The 1.8 Å crystal structure reveals the molecular basis for water selectivity and proton exclusion in the [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.0902725106 | — | 1.8 | P42_12 | Full-length hAQP4 (M1 isoform) | [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |

## Expression and Purification

- **Expression system**: Likely E. coli or insect cell expression (SI Materials and Methods referenced, not detailed in main text)

- **Construct**: Full-length hAQP4
- **Notes**: Full details in SI Materials and Methods


### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein purification | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) and SEC | — |  | Details in SI |


## Crystallization

### doi/10.1073##pnas.0902725106

| Parameter | Value |
|---|---|
| Method | Vapor diffusion / capillary microbatch (trials) |
| Temperature | — |
| Notes | Crystals obtained by drop-volume ratio trials and capillary microbatch. Full-length crystallization trials yielded 8 Å resolution; the 1.8 Å structure was from a truncated construct.
 |


## Biological / Functional Insights

### Water selectivity mechanism

The selectivity filter residues Arg-216 and His-201 create a
narrow constriction. Arg-216 is neutralized by hydrogen bonds
from 3 protein acceptors, with 2 donors to waters in transit,
enabling high-efficiency water conductance while excluding
protons.

### Dual NPA motif variant

Unlike AqpZ and [AQP1](/xray-mp-wiki/proteins/other-ion-channels/aqp1/) where the two NPA asparagines hydrogen
bond to the same central water, in hAQP4 the asparagines bond
to two different water molecules. MD simulations suggest the
central water transitions through a position accepting bonds
from both asparagines, contributing to proton exclusion.

### C loop flexibility

The C loop does not adopt the 3_10 helix seen in rat AQP4
electron diffraction structures, suggesting the 3_10 helix is
induced by crystal packing, not a physiological cell-adhesion
mechanism.

### Inhibitor testing

[TEA](/xray-mp-wiki/reagents/ligands/tetraethylammonium/) ([TEA](/xray-mp-wiki/reagents/ligands/tetraethylammonium/)), [Acetazolamide](/xray-mp-wiki/reagents/additives/acetazolamide/), and [Rizatriptan](/xray-mp-wiki/reagents/additives/rizatriptan/) were
tested. [TEA](/xray-mp-wiki/reagents/ligands/tetraethylammonium/) showed no inhibition up to 10 mM. [Acetazolamide](/xray-mp-wiki/reagents/additives/acetazolamide/) and
[Rizatriptan](/xray-mp-wiki/reagents/additives/rizatriptan/) showed only millimolar IC50 (~3 mM and ~1 mM
respectively) in proteoliposome assays, calling into question
earlier reports of micromolar inhibition.


## Cross-References

- [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) — hAQP4 is a member of the aquaporin family
- [Aquaporin Z (AqpZ)](/xray-mp-wiki/proteins/other-ion-channels/aquaporin-z/) — Comparative structural analysis with AqpZ
- [Glycerol Facilitator (GlpF)](/xray-mp-wiki/proteins/other-ion-channels/glycerol-facilitator/) — Comparative analysis of water/glycerol selectivity
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Used in crystallization; bound in extracellular vestibule
- [Tetraethylammonium](/xray-mp-wiki/reagents/tetraethylammonium/) — Tested as AQP4 inhibitor
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Used for phasing with rat AQP4 (2D57) as search model
- [Molecular Dynamics Simulation](/xray-mp-wiki/methods/molecular-dynamics-simulation/) — MD simulations of water dynamics in the NPA region
- [Selectivity Filter](/xray-mp-wiki/concepts/transport-mechanisms/selectivity-filter/) — Arg-216 and His-201 form the selectivity filter
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [AQP1](/xray-mp-wiki/proteins/other-ion-channels/aqp1/) — Related protein structure
