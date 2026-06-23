---
title: "Human Dermcidin (DCD) Antimicrobial Channel"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein]
sources: [doi/10.1073##pnas.1214739110]
verified: false
---

# Human Dermcidin (DCD) Antimicrobial Channel

## Overview

Dermcidin (DCD) is a human antimicrobial host-defense peptide that forms transmembrane channels to disrupt bacterial membranes. Its X-ray crystal structure reveals a hexameric channel architecture composed of zinc-connected trimers of antiparallel helix pairs. The channel has a unique barrel-stave-like architecture with six lateral openings (eyelets) that allow ions to enter sideways. DCD channels exhibit a conductance of ~80-110 pS and are anion-selective. The structure and functional mechanism were elucidated through a combination of X-ray crystallography, solid-state NMR spectroscopy, electrophysiology, and molecular dynamics simulations, providing a foundation for structure-based design of peptide antibiotics.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1214739110 | not in raw text | not specified | — | Full-length DCD peptide (synthetic) | Zn2+ |

## Expression and Purification

- **Expression system**: Chemically synthesized peptide (>97% purity, Peptide2.0)


### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Peptide synthesis | Chemical synthesis | — |  | DCD peptide synthesized by Peptide2.0 at >97% purity |
| Preparation for crystallization | Dissolved in buffer | — | 10 mM HEPES | 50 mg/mL (~10 mM) peptide in 10 mM HEPES |


## Crystallization

### doi/10.1073##pnas.1214739110

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | DCD peptide at 50 mg/mL in 10 mM HEPES |
| Reservoir | 0.2 M Zn(ac)2, 0.1 M Na-[Cacodylate (Sodium Dimethylarsenate)](/xray-mp-wiki/reagents/buffers/cacodylate/), 18% PEG8000, pH 6.5 |
| Mixing ratio | 1:1 (400 nL peptide + 400 nL reservoir) |
| Temperature | 100 K (cryo) |
| Cryoprotection | None (flash-frozen from mother liquor) |
| Notes | Crystallized in absence of detergents or lipids; crystals flash-frozen in liquid nitrogen without cryoprotectant |


## Biological / Functional Insights

### Zn2+-dependent channel formation

Zinc ions are essential for DCD channel formation. The structure
reveals Zn2+ ions coordinated by Glu5, Glu9, His38', and Asp42' at
the dimer interfaces. Zn2+ neutralizes the anionic charge of DCD
peptides (from -12e to neutral) and stabilizes the hexameric
assembly. MD simulations show that removal of Zn2+ compromises the
membrane-channel character. Electrophysiology confirms that H38A
mutation abolishes channel formation.

### Unique ion permeation pathway through lateral eyelets

DCD exhibits an unusual ion-permeation pathway. Through channel tilt
(~30° from membrane normal), ions enter sideways through six lateral
openings (eyelets, ~1 nm diameter) at the trimeric interfaces. This
shortens the ion pathway across the channel and exploits increased
ion concentration at lipid head groups. Anion traversal involves
single-ion "hopping" in the inner pore and multi-ion "knock-on"
effects at channel termini, expelling clusters of 3-4 anions.

### Barrel-stave mechanism for antimicrobial action

DCD represents a structurally characterized barrel-stave-like
antimicrobial channel. Unlike the carpet or toroidal pore models
proposed for many AMPs, DCD forms a defined hexameric channel with
high conductance (~80-110 pS). A single channel can dissipate the
bacterial transmembrane potential on a time scale of ~10^-4 s.
The structure provides the first comprehensive atomic-level
mechanism for membrane perturbation by a human antimicrobial peptide.

### DCD adopts multiple states depending on environment

DCD exists in a complex equilibrium of states: monomers and
oligomers in solution, monomers or small oligomers lying parallel to
the membrane surface, and transmembrane channels. Transmembrane
voltage and Zn2+ favor the membrane-spanning oligomeric state.
Solid-state NMR shows that the majority of DCD aligns in-plane with
the membrane in the absence of voltage, while electrophysiology
captures the minor but functionally relevant channel-forming
population.


## Cross-References

- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Used for DCD peptide preparation (10 mM HEPES)
- [Cacodylate (Sodium Dimethylarsenate)](/xray-mp-wiki/reagents/buffers/cacodylate/) — Used in crystallization reservoir (0.1 M Na-cacodylate, pH 6.5)
