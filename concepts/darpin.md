---
title: Designed Ankyrin Repeat Protein (DARPin)
created: 2026-05-27
updated: 2026-05-27
type: concept
category: concepts
layout: default
tags: [concept-construct-design]
sources: [doi/10.1016##j.jsb.2011.01.014]
verified: false
---

# Designed Ankyrin Repeat Protein (DARPin)

## Overview

Designed Ankyrin Repeat Proteins (DARPins) are modular protein scaffolds engineered through directed evolution for the specific binding of target proteins. Structurally, each DARPin repeat consists of an alpha-turn-alpha motif followed by a loop connecting to the next repeat, forming an overall L-shaped module. The lateral surfaces of repeats are hydrophobic, allowing modules to stack into elongated, stable proteins. DARPins are cysteine-free, characterized by extraordinary thermodynamic and chemical stability, and can be produced at high expression yields in bacteria.

DARPins have emerged as powerful crystallization chaperones for membrane proteins. By binding to flexible or difficult-to-crystallize targets, DARPins reduce conformational heterogeneity, stabilize specific conformational states, and provide additional crystal contact surfaces. This approach has proven especially valuable for membrane proteins, where the hydrophilic surface area available for crystal contacts is limited compared to soluble proteins.

## Mechanism/Details

A single DARPin repeat comprises an alpha-turn-alpha motif with a signature TPLH sequence containing a proline preceding the first helix, inducing a kink at the loop-to-helix transition. Internal repeats are based on a consensus sequence, with randomized positions in the complementarity-determining region (CDR) that contacts the target. In an N3C format (three internal repeats flanked by capping modules), randomization at position 26 (asparagine, tyrosine, or histidine) yields a theoretical diversity of 3.8 x 10^23.

DARPins are typically selected using ribosome display or phage display against the target protein. Ribosome display offers the advantage of maintaining the genotype-phenotype linkage without the need for transformation, enabling selection from libraries exceeding 10^12 variants. Selected binders can be further optimized for affinity and stability.

The DARPin binding interface typically involves 5-7 CDR residues contacting the target, burying approximately 400-500 A^2 of surface area. The hydrophobic core of the DARPin scaffold provides a stable framework that precisely positions the randomized CDR residues for optimal target contact.

DARPins as crystallization chaperones function through several mechanisms: (1) They reduce conformational heterogeneity by trapping specific conformational states of dynamic targets; (2) They provide additional hydrophilic surface area for crystal contacts; (3) They can shift thermodynamic equilibria toward a single conformation, analogous to ligand-induced stabilization.

## Examples in Membrane Protein Work

- **AcrB-DARPin complexes** (PDB 2JBS, 3NOC, 3NOG): DARPin binders selected by ribosome display against the E. coli multidrug efflux pump AcrB. Three crystal structures revealed that binders share a common epitope on the DC subdomain of the TolC docking domain. The DARPin-mediated crystal lattice provided equal contacts in all three dimensions, improving diffraction resolution to 2.54 A. Comparative analysis of three DARPin complexes showed that subtle differences in binding geometry significantly affect crystal quality, with resolution varying from 2.54 to 3.34 A despite identical crystal contact residues.

- **DARPin binding to membrane transporters**: DARPins have been selected against various membrane protein targets including RND efflux pumps, sodium-citrate symporter CitS, and the CC2-LZ domain of NEMO. These examples demonstrate the broad applicability of DARPins as crystallization chaperones across different membrane protein classes.

## Related Concepts

- Crystallization chaperone strategies using antibody fragments and other binding proteins
- Ribosome display and phage display for binder selection
- Protein engineering and directed evolution for scaffold optimization
- Conformational heterogeneity and its impact on crystallization

## Cross-References

- [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/acrB/) — Primary example of DARPin crystallization chaperone application; three crystal structures resolved (2JBS, 3NOC, 3NOG)
- [RND Efflux Pumps](/xray-mp-wiki/concepts/rnd-efflux-pumps/) — AcrB is an RND transporter; DARPin selection against RND transporters demonstrated binding plasticity
