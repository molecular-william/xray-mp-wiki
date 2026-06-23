---
title: Computational Design of Multipass Transmembrane Proteins
created: 2026-06-08
updated: 2026-06-08
type: concept
category: concepts
layout: default
tags: [concept-construct-design, membrane-protein]
sources: [doi/10.1126##science.aaq1739]
verified: false
---

# Computational Design of Multipass Transmembrane Proteins

## Overview
A methodology for the de novo computational design of multipass transmembrane proteins using Rosetta and buried hydrogen bond networks. This approach enables the design of transmembrane monomers, homodimers, trimers, and tetramers with 76 to 860 total residues containing two to eight membrane-spanning helices. Crystal structures of designed proteins closely match the computational models, demonstrating the accuracy of the approach.


## Mechanism/Details
The design strategy repurposes hydrogen bond networks (serine- and glutamine-containing) from soluble four-helix bundles to provide structural specificity within the membrane environment. Key steps include:

1. Parametric generation of four-helix bundle backbones of varying lengths using parametric generating equations
2. Introduction of hydrogen bond network residues and neighboring packing residues
3. Sequence optimization using Rosetta Monte Carlo design calculations to obtain low-energy sequences
4. Building connecting loops between helices with Rosetta
5. Incorporation of a ring of amphipathic residues at the designed lipid-water boundary on the extracellular/periplasmic side to specify membrane orientation

A major challenge overcome by this approach is the degeneracy of nonpolar interactions in the membrane environment. In soluble proteins, secondary structure and topology are specified by hydrophobic and hydrophilic residue patterns, but the apolar membrane environment requires outward-facing residues to also be nonpolar. Buried hydrogen bonds between polar side chains overcome this degeneracy and provide the structural specificity needed for accurate design.

The approach was validated by experimental characterization of designed proteins including CD spectroscopy (thermostable to 95 degrees C), analytical ultracentrifugation (correct oligomerization state), confocal microscopy (plasma membrane localization in HEK293T and bacterial cells), single-molecule magnetic tweezer unfolding (thermodynamic stability of 2.0 kcal/mol per helix), and X-ray crystal structures of the dimer TMHC2_E (2.95 A, Calpha RMSD 0.7 A from design) and tetramer TMHC4_R (3.9 A, Calpha RMSD 1.2-1.8 A from design).

## Examples in Membrane Protein Work
- TMHC2_E — Designed transmembrane dimer with four membrane-spanning helices; crystal structure confirmed at 2.95 A resolution
- TMHC4_R — Designed transmembrane tetramer with eight membrane-spanning helices in a rocket-shaped structure; crystal structure at 3.9 A confirmed overall architecture

## Related Concepts
- [De novo protein design](/xray-mp-wiki/concepts/de-novo-protein-design/) — Foundational methodology for computational protein structure design
- [Hydrogen bond networks in membrane proteins](/xray-mp-wiki/concepts/hydrogen-bond-networks/) — Central to the design strategy for specifying transmembrane helix packing

## Cross-References

