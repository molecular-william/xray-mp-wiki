---
title: Human Apelin Receptor (APJR)
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2017.04.008]
verified: true
---

# Human Apelin Receptor (APJR)

## Overview

The human apelin receptor (APJR), also known as angiotensin receptor-like 1 (AGTRL1) or angiotensin II type J receptor, is a class A G protein-coupled receptor (GPCR) that plays a key role in cardiovascular regulation. APJR is activated by two endogenous peptide ligands, apelin and elabela/toddler, and is involved in angiogenesis, vasoconstriction, heart muscle contractility, energy metabolism regulation, and fluid homeostasis. Polymorphisms in the APJR gene have been associated with increased risks of hypertension and coronary artery disease.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2017.04.008 | 5VBL | 2.6 | P 21 21 21 | Residues 19-330 with ICL3 (residues 230-242) replaced by rubredoxin (M1-E54). Mutations: C325L, C326M (palmitoylation site removal), T177N (glycosylation site removal), V117A, W261K. | AMG3054 |

## Expression and Purification

- **Expression system**: Baculovirus/Sf9 insect cells
- **Construct**: N-terminal HA signal sequence + Flag tag; C-terminal ppase site + 10x His tag. Residues 1-6 deleted, residues 331-380 truncated. ICL3 replaced with rubredoxin (M1-E54). Mutations: C325L, C326M, T177N, V117A, W261K.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell harvest | Sf9 cell culture infected with baculovirus at MOI 5; harvested after 48 h | — |  |  |
| Membrane preparation | Hypotonic lysis (10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl, protease inhibitor cocktail), centrifugation, high salt wash | — |  |  |
| Solubilization | DDM (N-Dodecyl-B-D-Maltoside, Anatrace D310) with CHS (Cholesteryl hemisuccinate, Sigma C6512) | — |  |  |
| Affinity chromatography | TALON IMAC resin (Clontech 635507) for His-tag capture | — |  |  |
| Size-exclusion chromatography | SEC in DDM/CHS buffer | — |  |  |
| Concentration | Concentrated for co-crystallization with AMG3054 | — |  |  |


## Crystallization

### doi/10.1016##j.str.2017.04.008

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Lipid | Monoolein (Sigma M7765) |
| Temperature | 20 C |


## Biological / Functional Insights

### Two-Site Peptide Binding Mode

The crystal structure of APJR in complex with AMG3054 revealed a novel two-site
peptide ligand binding mode, where the C-terminal end of the peptide binds deeply
into the canonical orthosteric pocket (site 1) and the N-terminal half extends to
a surface groove (site 2). This binding mode has not been observed in any other
solved class A GPCR structure.
Key binding residues at site 1 include Y35 (1.39), W85 (2.60), and R168 (ECL2),
whose mutation to alanine completely abolished apelin binding. Y264 (6.51) and
K268 (6.55) mutations reduced binding affinity but did not eliminate it. At site 2,
D23 (N-terminus) and D284 (7.28) are critical for peptide recognition.
The structure provides a mechanistic framework for understanding how endogenous
peptide ligands with high conformational flexibility may bind and modulate class A
peptide GPCRs through a similar two-site mechanism.


## Cross-References

- [AMG3054](/xray-mp-wiki/reagents/ligands/amg3054/) — Designed 17-mer apelin mimetic peptide agonist used in structure determination (PDB 5VBL)
- [Kappa Opioid Receptor](/xray-mp-wiki/proteins/kappa-opioid-receptor/) — Class A GPCR with endogenous peptide ligand; two-site binding model proposed via MD
- [Apelin-13](/xray-mp-wiki/reagents/ligands/apelin-13/) — Endogenous peptide agonist of APJR; binding analyzed by mutation and MD simulation
- [Apelin-17](/xray-mp-wiki/reagents/ligands/apelin-17/) — Endogenous peptide ligand; AMG3054 is a constrained analog of apelin-17
- [Two-Site Binding Mode](/xray-mp-wiki/concepts/two-site-binding-mode/) — Novel binding mechanism revealed by APJR-AMG3054 crystal structure
