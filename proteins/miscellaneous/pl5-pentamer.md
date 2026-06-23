---
title: PL5 Designed Pentameric Transmembrane Protein
created: 2026-06-10
updated: 2026-06-10
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.aav7541]
verified: false
---

# PL5 Designed Pentameric Transmembrane Protein

## Overview

PL5 is a designed homopentameric transmembrane helical bundle based on the apolar C-terminal domain of [PLB](/xray-mp-wiki/proteins/miscellaneous/phospholamban/) (PLN). It was designed to test whether apolar side-chain packing alone is sufficient to drive membrane protein folding and assembly. PL5 retains PLN's C-terminal LxxIxxx motif but replaces polar N-terminal residues (Asn, Ser, Cys) with fully hydrophobic isosteric residues (EtGly, Leu, Phe). The designed protein forms stable pentamers confirmed by MD simulation, analytical ultracentrifugation, SDS-PAGE thermal stability assays, and X-ray crystallography (PDB 6MQU, 1.75-Å resolution). The structure reveals knobs-into-holes packing at the d/e and a/g interfaces, defining a steric packing code for transmembrane helix assembly.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.aav7541 | 6MQU | 1.75 | TBD | PL5; designed pentameric transmembrane helical bundle based on PLN C-terminal domain with polar-to-apolar mutations | None (all apolar side chains) |

## Expression and Purification

- **Expression system**: Synthetic peptide (solid-phase synthesis)
- **Construct**: PL5, PL5_EtG, PL5_EtG3 variants

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Solid-phase peptide synthesis | Chemical synthesis | — |  | Synthesized with C-terminal amidation. EtGly residues incorporated as S-C-alpha-ethyl-Gly for fully hydrophobic isosteres. |
| Reconstitution in micelles | Detergent solubilization | — |  | Peptides reconstituted in myristyl sulfobetaine micelles or OG/LDS for characterization. |


## Crystallization

### doi/10.1126##science.aav7541

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Temperature | 20 |
| Notes | Crystals obtained from detergent solution. Structure solved at 1.75 A resolution. |


## Biological / Functional Insights

### Apolar packing alone drives pentameric assembly

PL5 forms stable pentamers stabilized entirely by van der Waals interactions between apolar side chains, with no interhelical hydrogen bonds. The pentamer is resistant to heating at 95 C in 2% LDS, 8 M [UREA](/xray-mp-wiki/reagents/substrates/urea/), demonstrating extreme thermostability. Analytical ultracentrifugation confirms the pentameric oligomeric state (apparent MW 18 kDa, expected 19 +/- 1.5 kDa).

### Knobs-into-holes packing code

The crystal structure reveals two distinct packing interfaces: d/e interface and a/g interface (using heptad repeat notation abcdefg). At the d/e interface, beta-branched amino acids (Ile, Val) pack tightly with their C-beta-C-gamma bonds directed inward. At the a/g interface, non-beta-branched residues are preferred because beta-branched residues would create steric clashes. This defines a steric packing code for transmembrane five-helix bundle assembly.

### Stringent steric complementarity requirement

Single conservative mutations (e.g., Leu-to-Ile at a g position) can entirely destabilize the pentamer. This demonstrates an unexpectedly stringent requirement for steric complementarity in membrane protein folding, where the hydrophobic effect is negligible unlike in soluble protein folding.


## Cross-References

- [Phospholamban (PLB)](/xray-mp-wiki/proteins/miscellaneous/phospholamban/) — PL5 is derived from the apolar C-terminal domain of PLN; the design revealed the steric packing code underlying PLN assembly
- [Computational Design of Multipass Transmembrane Proteins](/xray-mp-wiki/concepts/membrane-mimetics/computational-transmembrane-protein-design/) — Complementary approach to computational TM protein design using apolar packing rather than hydrogen bond networks
- [UREA](/xray-mp-wiki/reagents/substrates/urea/) — Entity mentioned in text
