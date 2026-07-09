---
title: "De Novo Protein Design"
created: 2026-07-06
updated: 2026-07-06
type: concept
category: concepts
layout: default
tags: [concept-functional, subdirectory-methods-techniques]
sources: [doi/10.1038##nature19946, doi/10.1126##science.1259426]
verified: none
---

# De Novo Protein Design

## Overview
De novo protein design is the computational design of new proteins with sequences not found in nature, using physical and statistical principles to achieve a desired three-dimensional fold and function. Unlike protein engineering (which modifies existing natural proteins), de novo design starts from first principles, specifying the target backbone conformation and then searching for amino acid sequences that stabilize that conformation. Major milestones include the design of Top7 (a novel alpha/beta fold not found in nature), the computational design of enzymes for model reactions (e.g., the Kemp eliminase), and the design of transmembrane protein structures. For membrane proteins, de novo design has achieved the design of proton-conducting channels, small-molecule transporters, and signaling proteins. The Rosetta software suite (particularly RosettaDesign and RosettaCM) is the most widely used platform for de novo protein design, employing Monte Carlo sampling of rotameric states to optimize side-chain packing, hydrogen bond networks, and buried hydrophobic surface area. The field is advancing rapidly with the integration of deep learning methods (protein diffusion models, AlphaFold-based hallucination) that can generate novel protein backbones and sequences simultaneously.

## Mechanism/Details


## Examples in Membrane Protein Work
- Designed Proton Channel — A de novo designed four-helix bundle proton channel (PDB 4HD3) that conducts protons across lipid bilayers via a His- and Trp-containing pore, demonstrating the feasibility of designing membrane protein function from scratch.
- Designed Transmembrane Protein Fold — A designed transmembrane protein with a non-natural topology (PDB 6E3F) that folds and inserts into membranes, establishing that de novo design principles can generate stable, functional membrane protein structures.

## Related Concepts
- [Computational Protein Design](/xray-mp-wiki/concepts/methods-techniques/computational-protein-design/) — De novo design is a specialized branch of computational protein design
- [Rosetta Software Suite](/xray-mp-wiki/concepts/methods-techniques/rosetta-software-suite/) — Rosetta is the primary platform used for de novo protein design calculations

## Cross-References
- [Computational Protein Design](/xray-mp-wiki/concepts/methods-techniques/computational-protein-design/) — De novo design represents the most ambitious approach within computational protein design
