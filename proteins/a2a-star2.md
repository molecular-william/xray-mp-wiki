---
title: A2A-STAR2
created: 2026-04-27
updated: 2026-04-28
type: protein
tags: [gpcr, receptor]
sources: [doi/10.1002##anie.202115545]
---
layout: default

# A2A-STAR2

## Overview

A2A-STAR2 is a 9-mutation thermostabilized construct of the human adenosine A2A receptor (A2AR). It was the dominant crystallization construct for GPCRs before the advent of BRIL fusion partners, enabling numerous high-resolution structures of antagonists bound to the inactive state.

## Structure Determination

- **PDB IDs**: 4EIY (ZM241385 complex), 4EBM (SCH-442416 complex), 8WDT (NECA complex with Fab 35.1)
- **Resolutions**: 2.4 Å (4EIY), 2.7 Å (4EBM), 2.9 Å (8WDT)
- **Method**: X-ray crystallography — vapor diffusion (4EIY, 4EBM) and LCP (8WDT)
- **Construct**: A2A-StaR2 (9 point mutations) + bRIL fusion in ICL3 (for most structures)

## Mutations

The STAR (Stabilization Through Allosteric Restriction) strategy introduces 9 point mutations to lock the receptor in the inactive conformation:

| Mutation | Position | Effect |
|----------|----------|--------|
| T88A | 3.36 | Reduces agonist affinity |
| N89D | 3.37 | Stabilizes inactive network |
| S91K | 3.39 | Occupies allosteric sodium pocket |
| F93W | 3.43 | Fills hydrophobic pocket |
| A105T | 3.51 | Restricts TM3 movement |
| F109W | 3.55 | Stabilizes TM3/TM4 packing |
| Y170F | ECL2 | Reduces flexibility |
| S277A | 7.42 | Removes steric clash with ligands |
| I316W | 8.46 | Stabilizes helix 8 |

**Note**: T88³·³⁶A and S277⁷·⁴²A are located inside the orthosteric ligand-binding pocket, which can interfere with agonist binding. This motivated the development of the single-mutation A2A-PSB1-bRIL construct.

## Expression and Purification

- **Expression system**: Sf9 insect cells (baculovirus expression)
- **Construct**: A2A-StaR2 with bRIL fusion in ICL3
- **Detergent**: DDM (n-dodecyl-β-D-maltopyranoside) for membrane solubilization
- **Purification**: Anti-FLAG affinity chromatography (N-terminal FLAG tag), followed by size-exclusion chromatography
- **SEC buffer**: 20 mM HEPES pH 7.5, 150 mM NaCl, 0.05% DDM

## Crystallization

### Antagonist-bound structures (4EIY, 4EBM)
- **Method**: Sitting-drop vapor diffusion
- **Precipitant**: 0.1 M sodium acetate pH 4.5, 18-20% PEG 400
- **Temperature**: 20 °C

### Agonist-bound structure with Fab 35.1 (8WDT)
- **Method**: Lipidic cubic phase (LCP) crystallization
- **Lipid**: Monoolein-based mesophase
- **Crystal growth**: Performed in dark/red light to prevent photoisomerization of agonist ligands
- **Stabilizer**: Fab 35.1 antibody fragment fused to extracellular side for conformational stabilization

## Key Uses

- Enabled the first high-resolution structures of A2AR with diverse antagonist scaffolds
- PDB 4EIY (ZM241385 complex) was a landmark structure for structure-based drug design
- Served as the primary template for developing Preladenant derivatives (PSB-2113, PSB-2115)
- PDB 8WDT (NECA-Fab complex) captured an agonist-bound state

## Relation to A2A-PSB1-bRIL

A2A-StaR2 was superseded by A2A-PSB1-bRIL (single S91K mutation), which:
- Has only 1 mutation instead of 9
- Avoids mutations in the orthosteric ligand-binding pocket (no T88A, no S277A)
- Provides superior thermostability
- Became the new gold standard for A2AR structural biology

## Related Proteins

- [a2a-adenosine-receptor](/proteins/a2a-adenosine-receptor/) — A2A-PSB1-bRIL construct (current gold standard)
- [bril](/reagents/protein-tags/bril/) — bRIL fusion partner used with A2A-StaR2
- [sf9-cells](/methods/expression-systems/sf9-cells/) — Insect cell expression system
- [fab-fragments](/reagents/antibodies/fab-fragments/) — Fab 35.1 used for agonist-bound structure (PDB 8WDT)
- [ddm](/reagents/detergents/ddm/) — Solubilization detergent
- [monoolein](/methods/crystallization/monoolein/) — LCP lipid for agonist-bound structure