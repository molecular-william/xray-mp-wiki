---
title: "Merohedral Twinning in Protein Crystallography"
created: 2026-06-11
updated: 2026-06-16
type: concept
category: concepts
layout: default
tags: [concept-crystallography-principle, subdirectory-methods-techniques]
sources: [doi/10.1107##S0907444908017162, doi/10.1126##science.280.5371.1934]
verified: none
---

# Merohedral Twinning in Protein Crystallography

## Overview
Merohedral twinning is a crystal growth defect in which two or more crystal
domains are related by a crystallographic symmetry operation that is not part of
the crystal's own space group but belongs to the higher-symmetric Laue group. This
results in overlapping reflections from different domains, complicating structure
determination and refinement. In macromolecular crystallography, merohedral twinning
can sometimes be identified by statistical analysis of reflection intensities and
corrected during refinement by refining a twin fraction parameter.


## Mechanism/Details


## Examples in Membrane Protein Work
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — The 2.3 A structure of bacteriorhodopsin (Luecke et al., 1998) exhibits nearly perfect merohedral twinning. Crystals in space group P6_3 show pseudo-622 Laue symmetry, requiring detwinning during data processing using the twinning matrix [0 1 0; 1 0 0; 0 0 -1]. The twinning was identified via a Patterson self-rotation function showing strong two-fold peaks every 30 degrees in the a/b plane.
- [Rhodopsin N2C/D282C Mutant](/xray-mp-wiki/proteins/gpcr/rhodopsin-n2c-d282c-mutant/) — The rhodopsin mutant structure (PDB 2j4y) was found to be merohedrally twinned when refined in P6_4 space group, with a twin fraction of 0.02. The merohedral twinning was identified by referees of the original structure report.

## Related Concepts
- Non-crystallographic symmetry
- Space group assignment
- Crystal symmetry

## Cross-References
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — The 2.3 A bR structure is a textbook example of merohedral twinning in membrane protein crystallography
- [Bovine Rhodopsin](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/) — Rhodopsin structure where merohedral twinning was applied
- [X-ray Crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/) — Core crystallographic methodology
- [Rhodopsin N2C/D282C Mutant](/xray-mp-wiki/proteins/gpcr/rhodopsin-n2c-d282c-mutant/) — Related protein structure
