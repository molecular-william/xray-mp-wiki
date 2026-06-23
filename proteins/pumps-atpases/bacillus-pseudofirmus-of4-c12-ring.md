---
title: "Bacillus pseudofirmus OF4 ATP Synthase A16/20G c12 Ring"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein]
sources: [doi/10.1073##pnas.1303333110]
verified: false
---

# Bacillus pseudofirmus OF4 ATP Synthase A16/20G c12 Ring

## Overview

The [ATP](/xray-mp-wiki/reagents/ligands/atp/) synthase c-ring from the extreme alkaliphile *Bacillus pseudofirmus* OF4 assembles as an oligomeric ring of c-subunits that determines the ion-to-ATP ratio during [ATP](/xray-mp-wiki/reagents/ligands/atp/) synthesis. The wild-type c-ring has a stoichiometry of c13, enabled by an AxAxAxA motif (replacing the canonical GxGxGxG) that tightens c-subunit packing. The A16/20G double mutant forms a smaller c12 ring, solved by X-ray crystallography at 4.1-Å resolution (PDB: 3zo6). The alanine motif is an evolutionary adaptation to support [ATP](/xray-mp-wiki/reagents/ligands/atp/) synthesis at the low proton motive force (pmf) of alkaline environments.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1303333110 | 3zo6 | 4.1 | — | A16/20G mutant c-ring with C-terminal extension |  |

## Expression and Purification

- **Expression system**: E. coli
- **Construct**: C-terminal extension (5 amino acids) on c-subunit; A16/20G mutations

### Purification Workflow

- **Expression system**: E. coli

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Purification | Affinity chromatography / standard c-ring purification | — | n-dodecyl-beta-D-maltoside |  |


## Crystallization

### doi/10.1073##pnas.1303333110

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (hanging drop) |
| Reservoir | 0.1 M [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 9.0, 23% (v/v) [Peg](/xray-mp-wiki/reagents/additives/peg/) 400 |
| Temperature | 20 |
| Growth time | 24 hours |
| Cryoprotection | 0.1 M [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 9.0, 30% (v/v) [Peg](/xray-mp-wiki/reagents/additives/peg/) 400, 2% (w/v) alpha-nonyl-maltoside |


## Biological / Functional Insights

### Alanine Motif Determines c-Ring Stoichiometry

The AxAxAxA motif (residues 16-22) in the B. pseudofirmus OF4 c-subunit replaces the canonical GxGxGxG motif found in neutralophilic Bacillus species. The alanine methyl side chains form an extensive hydrophobic interaction network, with A16 making five interaction partners including four on the adjacent c-subunit. Alanine-to-glycine mutations (A16G and A16/20G) disrupt these packing interactions, leading to smaller c-ring stoichiometries (c12 vs. c13).

### Altered Stoichiometry Impacts Cell Physiology

The A16/20G mutant with c12 stoichiometry exhibited a molar growth yield only 56% of wild-type c13 at pH 10.5 on limiting malate. This demonstrates that larger c-ring stoichiometry (higher ion-to-ATP ratio) is advantageous at low pmf in alkaliphiles. The c13 stoichiometry is a key adaptation for [ATP](/xray-mp-wiki/reagents/ligands/atp/) synthesis at high pH, where the proton gradient is reduced.

### Variable Stoichiometry Observed by AFM

AFM imaging of 270 individual c-rings revealed that the wild-type C-terminal extension construct produced variable stoichiometries ranging from c11 to c16, with c13 dominating (77.2%). The A16/20G mutant showed a shift toward c12 (61.3%) and c13 (34.7%), confirming that the alanine mutations bias assembly toward smaller rings but do not enforce a single stoichiometry.


## Cross-References

- [Rotary ATPase Mechanism](/xray-mp-wiki/concepts/enzyme-mechanisms/rotary-atpase-mechanism/) — ATP synthase c-ring is a key component of the rotary ATPase mechanism
- [Binding Change Mechanism](/xray-mp-wiki/concepts/enzyme-mechanisms/binding-change-mechanism/) — c-ring stoichiometry determines the ion-to-ATP ratio in the binding change mechanism
- [ATP](/xray-mp-wiki/reagents/ligands/atp/) — Referenced in the context of ATP
- [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) — Referenced in the context of Tris Hcl
- [Peg](/xray-mp-wiki/reagents/additives/peg/) — Referenced in the context of Peg
