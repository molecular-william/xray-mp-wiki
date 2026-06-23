---
title: Somatostatin Receptor 2 (SSTR2)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41422-022-00679-x]
verified: false
---

# Somatostatin Receptor 2 (SSTR2)

## Overview

Somatostatin receptor 2 (SSTR2) is a class A G protein-coupled receptor that is the best characterized member of the somatostatin receptor family. SSTR2 plays versatile roles in inhibiting secretion of multiple hormones including growth hormone and thyroid-stimulating hormone, and is the most common SSTR subtype expressed in human neuroendocrine tumors (NETs). It is a validated target for diagnosis and therapy of NETs and acromegaly. Crystal structures of SSTR2 bound to a selective peptide antagonist CYN 154806 (2.65 A) and a non-peptide agonist L-054,522 (2.6 A) were determined using LCP crystallization, revealing the molecular basis of ligand recognition, subtype selectivity, receptor activation, and G protein coupling.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41422-022-00679-x | 7XNA | 2.65 | Not specified | SSTR2 with C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) (T359), xylanase insertion in ICL3 (S238-G243 replaced), D89N, V106E, S316D mutations | CYN 154806 (peptide antagonist) |
| doi/10.1038##s41422-022-00679-x | 7XN9 | 2.6 | Not specified | SSTR2 with C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) (T359), xylanase insertion in ICL3 (I240-V242 junction), V106E, S316D mutations (D89 restored to WT) | L-054,522 (non-peptide agonist) |
| doi/10.1038##s41422-022-00679-x | 7XMR | 3.1 | C1 | SSTR2 WT with C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) (T359) | SST-14 (endogenous ligand) |

## Expression and Purification

- **Expression system**: Sf9 insect cells (baculovirus expression, Bac-to-Bac system)
- **Construct**: SSTR2 with HA signal peptide, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) at N-terminus, [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) site, 10xHis tag at C-terminus (for crystallization); or twin-strep tag at C-terminus (for [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/))
- **Notes**: High-titer recombinant viruses at MOI of 5; cells collected 48 h post-infection

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Cell collection and membrane isolation |  | Lysis buffer with protease inhibitors | Sf9 cells collected 48 h post-infection |


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| LCP crystallization | [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) |  | Not specified in paper | Crystals grown in [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) lipid phase; determined at 2.65 A and 2.6 A |


## Crystallization

### doi/10.1038##s41422-022-00679-x

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | Purified SSTR2-CYN 154806 complex in [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) |
| Temperature | Not specified |
| Notes | SSTR2 with xylanase fusion in ICL3; D89N, V106E, S316D mutations |

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | Purified SSTR2-L-054,522 complex in [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) |
| Temperature | Not specified |
| Notes | SSTR2 with xylanase in ICL3; D89 restored to WT; V106E, S316D mutations |


## Biological / Functional Insights

### Ligand recognition by SSTR2

The endogenous ligand SST-14 binds SSTR2 with its key pharmacophore (F7-W8-K9-T10) located at the bottom of the binding pocket. K9 forms a salt bridge with D122(3.32), a conserved interaction in SSTRs. The hydrophobic pocket formed by helix VI, ECL3 and helix VII is a major determinant of ligand selectivity for SSTR2. CYN 154806 occupies a similar binding pocket to SST-14 but with a 70-degree counterclockwise rotation of the d-W8-K9 pair, leading to antagonist effects. L-054,522, a non-peptide agonist, binds with its 2-oxo-3H-benzimidazole group extending into the hydrophobic cavity formed by helix VI, ECL3 and helix VII.

### Activation mechanism of SSTR2

Agonist binding to SSTR2 induces a contraction of the helical bundle, rearrangement of the "NPxxY" motif, and release of the ionic lock between D139(3.49) and R140(3.50). The antagonist CYN 154806, through chirality inversion of specific residues, induces outward movement of extracellular tips of helices II, VI and VII, expanding the ligand-binding pocket and preventing receptor activation.


## Cross-References

- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid used for LCP crystallization
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Method used for crystal growth
- [T4 Lysozyme (T4L)](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) — Reference fusion protein (xylanase used as alternative crystallization fusion partner)
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) — Related biological concept
- [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) — Additive used in purification or crystallization buffers
- [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) — Fusion tag for crystallization or purification
