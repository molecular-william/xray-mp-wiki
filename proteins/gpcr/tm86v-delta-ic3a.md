---
title: NTSR1 TM86V-ΔIC3A Mutant
created: 2026-06-05
updated: 2026-06-05
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1073##PNAS.1317903111]
verified: false
---

# NTSR1 TM86V-ΔIC3A Mutant

## Overview

[NTSR1](/xray-mp-wiki/proteins/gpcr/neurotensin-receptor-1/) TM86V-ΔIC3A is a directed evolution-selected mutant of the [Neurotensin](/xray-mp-wiki/reagents/ligands/neurotensin/) receptor 1 ([NTSR1](/xray-mp-wiki/proteins/gpcr/neurotensin-receptor-1/)) that was optimized for crystallization through a directed evolution approach in E. coli. The construct contains 11 point mutations (A86L, H103D, H105Y, A161V, R167L, R213L, V234L, I253A, H305R, F358V, S362A) that confer high expression and thermostability, and a deletion of most of the third intracellular loop (ΔIC3A). Unlike fusion protein-based GPCR structures, TM86V-ΔIC3A was crystallized without bulky modifications at the cytoplasmic face, retaining signaling competence including G protein coupling to Gi and β-arrestin-dependent internalization. The structure reveals a canonical inactive state at the cytosolic side with a stable amphipathic helix 8 (H8), distinct from the GW5-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) structure which lacks H8. The ligand binding pocket shows a single α-helical turn in ECL3 with a salt bridge between D336 and R9 of [Neurotensin](/xray-mp-wiki/reagents/ligands/neurotensin/).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##PNAS.1317903111 | Not specified (see main paper) | 3.26 A | Not specified | NTR1-TM86V-ΔIC3A: 11 point mutations (A86L, H103D, H105Y, A161V, R167L, R213L, V234L, I253A, H305R, F358V, S362A), ΔIC3A deletion of ICL3 and C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation/) after G390, expressed in E. coli
 | [Neurotensin](/xray-mp-wiki/reagents/ligands/neurotensin/) |
| doi/10.1073##PNAS.1317903111 | Not specified (see main paper) | 2.75 A | Not specified | NTR1-TM86V-ΔIC3B: 11 point mutations, ΔIC3B deletion of ICL3, expressed in E. coli
 | [Neurotensin](/xray-mp-wiki/reagents/ligands/neurotensin/) |

## Expression and Purification

- **Expression system**: E. coli (isopropyl-β-D-thiogalactopyranoside-inducible pBR322-derived vector)
- **Construct**: N- and C-terminally truncated at G50 and G390, linked via human rhinovirus 3C protease sites to maltose-binding protein (N-terminal) and thioredoxin (C-terminal)


No purification described.

## Crystallization

No crystallization described.

## Biological / Functional Insights

### Inactive conformation at intracellular side

The TM86V-ΔIC3A mutant adopts an apparent inactive receptor conformation at the intracellular side, lacking the outward movement of TM6 seen in active GPCRs. TM7 does not unwind as seen in NTSR1-ELF. The F376(8.50) residue is partially inserted into the pocket between TM1, TM2 and TM7, unlike in NTSR1-ELF where it is rotated outward.

### Comparison with active-like NTSR1 structures

The structure is similar to active-like [NTSR1](/xray-mp-wiki/proteins/gpcr/neurotensin-receptor-1/) structures in the extracellular half (ligand-binding region) but dissimilar in the intracellular half. The D113(2.50) side chain is in contact with neighbouring residues, but the interactions differ from those in NTSR1-GW5, [NTSR1-LF Mutant](/xray-mp-wiki/proteins/gpcr/ntsr1-lf/), and NTSR1-ELF. S362(7.46) is mutated to alanine in TM86V-ΔIC3A.

### Improved interhelical surface complementarity

Comparison of NTR1-TM86V with its precursor NTR1-D03 (which lacks A86L, I253A, and F358V) reveals that three hydrophobic-to-hydrophobic mutations significantly improve thermostability. I253A and F358V remove steric clashes with neighboring helices, while A86L adds favorable van der Waals contacts between TM1 and TM2. These changes suggest that improved interhelical surface complementarity, not increased polarity, drives [Protein Thermostabilization](/xray-mp-wiki/concepts/thermostabilization/).

### Helix 8 forms a canonical amphipathic structure

Unlike the GW5-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) structure, TM86V-ΔIC3B exhibits a canonical amphipathic helix 8. The H8 stability is reduced compared to [A2AR](/xray-mp-wiki/proteins/gpcr/human-adenosine-a2a-receptor-a2ar/) due to weaker interactions: F8.50 only partially inserts into the hydrophobic pocket, F8.54 clashes with N7.54, IC1 is longer and disordered, and the buried surface area is smaller (222 A2 vs 303 A2 in [A2AR](/xray-mp-wiki/proteins/gpcr/human-adenosine-a2a-receptor-a2ar/)). The occupancy of the canonical H8 position may depend on palmitoylation state.


## Cross-References

- [NTSR1-ELF Mutant](/xray-mp-wiki/proteins/gpcr/ntsr1-el/) — Active-like NTSR1 structure compared with inactive TM86V-ΔIC3A mutant
- [NTSR1-LF Mutant](/xray-mp-wiki/proteins/gpcr/ntsr1-lf/) — Active-like NTSR1 structure compared with inactive TM86V-ΔIC3A mutant
- [Protein Thermostabilization](/xray-mp-wiki/concepts/thermostabilization/) — Related biological concept
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation/) — Related biological concept
- [A2AR](/xray-mp-wiki/proteins/gpcr/human-adenosine-a2a-receptor-a2ar/) — Related protein structure
- [NTSR1](/xray-mp-wiki/proteins/gpcr/neurotensin-receptor-1/) — Related protein structure
- [Neurotensin](/xray-mp-wiki/reagents/ligands/neurotensin/) — Related ligand or cofactor
- [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) — Fusion tag for crystallization or purification
