---
title: "Human Claudin-4 (hCLDN-4)"
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.2024651118, doi/10.1126##science.1261833]
verified: false
---

# Human Claudin-4 (hCLDN-4)

## Overview

Human claudin-4 (hCLDN-4) is a 23-34 kDa tetraspanning tight junction membrane protein
belonging to the claudin family of 27 human isoforms. It is a critical component of
epithelial tight junctions, functioning primarily as a cation barrier to reduce paracellular
Na+ permeability. hCLDN-4 is upregulated in the large intestine and is a primary high-affinity
receptor for Clostridium perfringens enterotoxin (CpE) in humans. The crystal structure of
hCLDN-4 in complex with the C-terminal receptor-binding domain of CpE (cCpE) was solved at
3.37 A resolution (PDB 7KP4), revealing the NPLVA153 motif on extracellular segment 2 (ECS2)
as the key toxin-binding determinant. A leucine at position 3 of this motif (Leu153) imparts
high-affinity CpE binding (Kd = 2.5 nM), distinguishing hCLDN-4 as the primary human CpE
receptor, in contrast to mice where CLDN-3 and CLDN-8 serve this role.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.2024651118 | 7KP4 | 3.37 |  | hCLDN-4 residues 5-186 with C-terminal affinity tag, in complex with cCpE | cCpE (Clostridium perfringens enterotoxin C-terminal domain) |

## Expression and Purification

- **Expression system**: Sf9 insect cells via baculovirus
- **Construct**: Full-length human CLDN-4 with C-terminal tag
- **Notes**: Expressed using Bac-to-Bac baculovirus expression system

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Homogenization and centrifugation | — |  | Membranes collected from Sf9 cell pellets |
| Solubilization | Detergent solubilization | — | 1% n-undecyl-beta-D-maltopyranoside ([UDM](/xray-mp-wiki/reagents/detergents/udm/)) | Membrane proteins solubilized from Sf9 cell membranes |
| Complex formation | Incubation with cCpE | — |  | Purified hCLDN-4 mixed with cCpE to form complex |
| Gel filtration | Size-exclusion chromatography | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | 20 mM HEPES pH 7.5, 150 mM NaCl, 0.22 M [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | hCLDN-4/cCpE complex purified to homogeneity |


## Crystallization

### doi/10.1073##pnas.2024651118

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | hCLDN-4/cCpE complex |
| Notes | Data collected at ALS beamline 8.3.1. Structure determined by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/). Resolution 3.37 A. |


## Biological / Functional Insights

### NPLVA153 motif determines CpE binding affinity

The hCLDN-4 structure reveals that CpE targets the NPLVA153 motif on ECS2.
Position 3 (Leu153) is the critical determinant of binding affinity. A leucine
at this position provides extended hydrophobic side chain length that more deeply
penetrates a surface groove on cCpE, yielding high-affinity binding (Kd = 2.5 nM).
In contrast, hCLDN-3 has valine at this position (NPVVP152), resulting in 100-fold
lower affinity (Kd = 252 nM). Mutagenesis swapping Leu153 in hCLDN-4 to Val
(hCLDN-4 L151V/A153P) decreases cCpE affinity 5-fold, while swapping Val150 in
hCLDN-3 to Leu (hCLDN-3 V150L/P152A) increases affinity 12-fold. The dissociation
rate (koff) is the dominant kinetic parameter differentiating high- vs low-affinity
claudin-CpE complexes.

### hCLDN-4 as primary human CpE receptor

Based on correlation of binding affinities, kinetics, half-lives, and claudin
expression patterns in gut, hCLDN-4 is identified as the primary CpE receptor in
humans. High-affinity (<10 nM) CpE receptors in humans are CLDN-4, CLDN-6, and
CLDN-9. In contrast, the primary CpE receptors in mice are CLDN-3 and CLDN-8,
reflecting divergence in the NPLVA motif. hCLDN-4 has a complex half-life (t1/2)
of ~2 h with cCpE, allowing sustained toxin binding necessary for cytotoxicity.

### ECH1 structural plasticity upon CpE binding

The structure of hCLDN-4 lacks a fully formed ECH1 (extracellular helix 1) that
is present in unbound claudin structures such as mCLDN-15. ECH1 is involved in
claudin cis assembly. In hCLDN-4, the SLLALP74 region appears as a bulbous density
with helical phi/psi values, representing a helical remnant of ECH1 disrupted by
cCpE binding. CpE-induced structural plasticity of ECH1 may be how enterotoxin
disables claudin lateral (cis) assemblies, contributing to tight junction disassembly.

### hCLDN-4 ion selectivity: Lys65 as cation barrier determinant

hCLDN-4 functions as a cation barrier (reduces paracellular Na+ permeability)
due to Lys65 on beta-4 of ECS1. This lysine residue provides a positive charge
that repels cations, creating a cation-tight barrier. This contrasts with hCLDN-2
(Asp65, anion barrier/cation pore) and is shared with hCLDN-9 (Lys65).


## Cross-References

- [Human Claudin-9 (hCLDN-9)](/xray-mp-wiki/proteins/structural-adhesion/human-claudin-9/) — Related claudin-CpE complex structure; both show conserved claudin fold and NPLVA motif for CpE binding
- [Mouse Claudin-19 (mCldn19)](/xray-mp-wiki/proteins/structural-adhesion/claudin-19-mouse/) — Related claudin-C-CPE complex structure revealing shared CpE binding mode
- [C-CPE (Clostridium perfringens Enterotoxin)](/xray-mp-wiki/reagents/ligands/c-cpe/) — hCLDN-4 is the primary human CpE receptor; structure reveals NPLVA motif recognition
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) — Additive used in purification or crystallization buffers
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used in purification or crystallization
- [UDM](/xray-mp-wiki/reagents/detergents/udm/) — Detergent used in purification or crystallization
