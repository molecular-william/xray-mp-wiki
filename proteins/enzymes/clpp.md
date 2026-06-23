---
title: "ClpP Protease"
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2007.11.080, doi/10.1016##j.jmb.2006.05.063]
verified: false
---

# ClpP Protease

## Overview

ClpP is an ATP-dependent, general protease from bacterial cytoplasm that works with chaperones ClpA and ClpX to recognize, unfold, and cleave misfolded and transient proteins. ClpP forms a large circular assembly with an axial pore hole and contains 14 catalytic active sites utilizing a Ser/His/Asp catalytic triad mechanism. The structure shows a surprising fold similarity to the periplasmic Ser/Lys protease [SppA_EC](/xray-mp-wiki/proteins/enzymes/sppa-ec/) despite different catalytic mechanisms and oligomeric arrangements.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2006.05.063 | 2CLP | 1.9 A | -- | E. coli ClpP with peptide covalently bound | peptide inhibitor |
| doi/10.1016##j.jmb.2007.11.080 | 3BF0 | -- | -- | E. coli ClpP (structural comparison model) | -- |

## Expression and Purification

- **Expression system**: Not specified in source papers; ClpP is a native cytoplasmic protease
- **Construct**: Native E. coli ClpP; the structure in PDB 2CLP includes ClpP with a peptide covalently bound at the active site

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| ClpP purification | Not specified in detail; ClpP was purified for structural studies with covalently bound peptide inhibitor | -- | -- + -- | ClpP was crystallized with a peptide covalently bound at the active site. |


## Crystallization

### doi/10.1016##j.jmb.2006.05.063

| Parameter | Value |
|---|---|
| Method | -- |
| Protein sample | ClpP with peptide covalently bound at active site |
| Reservoir | -- |
| Temperature | -- |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | Structure solved at 1.9 A resolution; ClpP forms a 14-mer spherical assembly (two 7-mer oligomers). The axial hole is ~13.5 A in diameter. |


## Biological / Functional Insights

### 14-mer spherical assembly with axial pore

ClpP forms a large circular assembly composed of two heptameric rings (14-mer) creating a barrel-shaped structure with an axial pore hole of approximately 13.5 A in diameter. The major globular domain of each monomer forms the axial hole, with an internal sequence extension (the "handle") creating intercalating interactions between the two 7-mer halves. This is distinct from the bowl-shaped tetrameric assembly of SppA, where the extension domain forms the axial hole.

### Ser/His/Asp catalytic triad

Each ClpP monomer encodes a complete active site involving a Ser/His/Asp catalytic triad. This differs from SppA, which utilizes residues at the interface of its tandemly repeated domains to create a Ser/Lys catalytic dyad. Remarkably, when a ClpP monomer is superimposed on the C-terminal half of SppA, the catalytic atoms of the Ser/His/Asp triad superimpose with the catalytic atoms of the Ser/Lys dyad.

### ATP-dependent chaperone/protease complex

ClpP works with ATP-dependent chaperones ClpA and ClpX to form the ClpAP and ClpXP complexes. These chaperones recognize, unfold, and deliver misfolded and transient proteins from the bacterial cytoplasm to the ClpP protease chamber for degradation. This is analogous to how SppA may function in quality control of periplasmic and membrane-bound proteins.

### Structural similarity to SppA despite different mechanisms

Despite limited sequence identity (15.6-25% identity for 147-155 aligned residues), the N- and C-terminal regions of SppA monomers are similar in fold to ClpP monomers, with rmsd of 3.0 A and 1.8 A respectively. The oxyanion holes in both SppA and ClpP are unique among serine proteases in that they use a main-chain amide NH from the residue following the nucleophile. The internal surface of the ClpP complex is much more polar than the hydrophobic interior of the SppA bowl.


## Cross-References

- [Signal Peptide Peptidase A from Escherichia coli (SppA_EC)](/xray-mp-wiki/proteins/enzymes/sppa-ec/) — Primary structural comparison protein; SppA shows surprising fold similarity to ClpP despite different catalytic mechanisms; both are Ser proteases with similar oxyanion hole architecture
