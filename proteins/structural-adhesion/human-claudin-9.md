---
title: "Human Claudin-9 (hCLDN-9)"
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1908929116, doi/10.1126##science.1261833]
verified: false
---

# Human Claudin-9 (hCLDN-9)

## Overview

Human claudin-9 (hCLDN-9) is a tetraspanning tight junction membrane protein belonging
to the claudin family of 27 human isoforms. It is the highest-expressing claudin in
the inner ear and is essential for hearing, acting as a cation barrier to reduce
Na+ and K+ permeability in the endolymphatic system. hCLDN-9 also serves as an entry
coreceptor for hepatitis C virus (HCV) and is a high-affinity receptor for Clostridium
perfringens enterotoxin (CpE). Crystal structures of hCLDN-9 in complex with the
C-terminal receptor-binding domain of CpE (cCpE) were solved at 3.2 and 3.3 A
resolution, revealing the complete claudin structure with two distinct conformations
(closed and open) that show how CpE binding disrupts claudin self-assembly and tight
junction integrity.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1908929116 | 6OV2 | 3.2 | P2(1)2(1)2(1) | Full-length human CLDN-9 with C-terminal His6 tag, in complex with cCpE (closed conformer) | cCpE |
| doi/10.1073##pnas.1908929116 | 6OV2 | 3.3 | P2(1)2(1)2(1) | Full-length human CLDN-9 with C-terminal His6 tag, in complex with cCpE (open conformer) | cCpE |

## Expression and Purification

- **Expression system**: Sf9 insect cells via baculovirus
- **Construct**: Full-length human CLDN-9 with C-terminal His10 tag
- **Notes**: Expressed using Bac-to-Bac baculovirus expression system

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Homogenization and centrifugation | — |  | Membranes collected from Sf9 cell pellets |
| Solubilization | Detergent solubilization | — | 20 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Membrane proteins solubilized for 2 h at 4 C |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA affinity | Ni-NTA |  | His10-tagged hCLDN-9 purified by nickel affinity |
| Complex formation | Incubation with cCpE | — |  | Purified hCLDN-9 mixed with cCpE at 1:1.5 molar ratio |
| Gel filtration | Size-exclusion chromatography | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | 20 mM HEPES pH 7.5, 150 mM NaCl, 0.22 M [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | hCLDN-9/cCpE complex purified to homogeneity |


## Crystallization

### doi/10.1073##pnas.1908929116

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | hCLDN-9/cCpE complex |
| Reservoir | 150 mM Na(C2H5COO), NaO2As(CH3)2, Bis-Tris propane pH 4.5, 25% [PEG](/xray-mp-wiki/reagents/additives/peg/) 1500 |
| Notes | Crystals cryoprotected and flash-frozen in liquid nitrogen. Data collected at ALS beamline 8.3.1. Structures determined by MR using homology model of hCLDN-9 and cCpE. Two distinct conformers captured: closed (cCpE deep in palm) and open (cCpE rocked outward). |


## Biological / Functional Insights

### Complete claudin structure with left-handed 4-TM bundle

hCLDN-9 reveals a left-handed four-transmembrane-helix bundle. The extracellular
domain consists of a five-stranded beta-sheet (four from ECS1, one from ECS2)
forming a hand-like epitope. ECS1 is fortified by a Cys54-Cys64 disulfide bond.
An additional Cys25-Cys84 disulfide links TM1 to TM2. The improved resolution
allows visualization of all nonterminal residues, resulting in the most complete
claudin structure to date.

### hCLDN-9 ion selectivity: Lys65 as cation barrier determinant

hCLDN-9 functions as a cation barrier. Sequence and structure comparison with
hCLDN-2 (anion barrier, Asp65) and hCLDN-4 (cation barrier, Lys65) identifies
hCLDN-9 Lys65 as a key residue for ion selectivity. Lys65 lies below the Cys54-Cys64
disulfide bond on beta-4. Residues at positions 31, 48, 53, and 65 on beta-1 to
beta-4 align on the same plane and could create a single-sided half-pore.

### CpE-induced claudin self-assembly disruption via lever mechanism

The cCpE-bound hCLDN-9 structures reveal two conformers: a closed form where
cCpE sits deep in the claudin palm, and an open form where cCpE rocks outward
via a rigid-body lever-like motion. Both conformers disrupt the two epitopes
known to enable claudin cis self-assembly. In the closed form, cCpE binding
breaks 80% (4 of 5) of the interatomic bonds at the cis interaction epitope.
In the open form, all cis interactions are abolished. CpE binding to the NPLVA153
motif on ECS2 also disrupts trans interactions. These mechanisms explain how CpE
dissociates tight junctions in gut epithelium.

### hCLDN-9 is a high-affinity CpE receptor

Biolayer interferometry (BLI) measurements show that hCLDN-9 binds CpE with a
Kd of 5.1 nM and cCpE with a Kd of 3.6 nM, comparable to the well-characterized
CpE receptors hCLDN-3 and hCLDN-4. CpE is cytotoxic to hCLDN-9-expressing Sf9
cells (59.2% decrease in viability), while cCpE (lacking the cytotoxic domain)
is not. This demonstrates that hCLDN-9 is a functional CpE receptor.


## Cross-References

- [Mouse Claudin-19 (mCldn19)](/xray-mp-wiki/proteins/structural-adhesion/claudin-19-mouse/) — Related claudin structure in complex with C-CPE; both show conserved claudin fold and CpE binding mode
- [C-CPE (Clostridium perfringens Enterotoxin)](/xray-mp-wiki/reagents/ligands/c-cpe/) — hCLDN-9 is a high-affinity CpE receptor; structures reveal mechanisms of CpE-induced TJ disassembly
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) — Additive used in purification or crystallization buffers
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used in purification or crystallization
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used in purification or crystallization
