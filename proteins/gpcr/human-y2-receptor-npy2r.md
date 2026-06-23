---
title: Human Neuropeptide Y Y2 Receptor (Y2R, NPY2R)
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-021-21030-9]
verified: false
---

# Human Neuropeptide Y Y2 Receptor (Y2R, NPY2R)

## Overview

The human neuropeptide Y (NPY) Y2 receptor (Y2R, NPY2R) is a class A G-protein-coupled receptor that plays essential roles in food intake, bone formation, and mood regulation. Y2R is widely distributed in the central and peripheral nervous systems and has been considered an important drug target for obesity and anxiety. The crystal structure of Y2R bound to a selective antagonist JNJ-31020028 at 2.8 Å resolution reveals molecular details of the ligand-binding mode. Combined with mutagenesis studies, the structure provides insights into key factors that define antagonistic activity of diverse antagonists and identifies receptor-ligand interactions that play different roles in modulating receptor activation and mediating ligand selectivity. Comparison with antagonist-bound Y1R structures deepens understanding of molecular mechanisms of ligand recognition and subtype specificity of NPY receptors, enabling structure-based drug design.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-021-21030-9 | 7DDZ | 2.8 | -- | Engineered human Y2R with N-terminal T4L fusion, C-terminal truncation (S354-V381), H149(3.51)Y and S280(6.47)C mutations, ICL3 (S251-N256) replacement with modified flavodoxin (P2A, Y98W), N-terminal HA signal sequence, C-terminal PreScission site and 10xHis tag plus Flag tag | JNJ-31020028 (selective antagonist) |

## Expression and Purification

- **Expression system**: Spodoptera frugiperda (Sf9) insect cells, Bac-to-Bac baculovirus expression system
- **Construct**: Engineered human Y2R with HA signal sequence, PreScission site, 10xHis tag and Flag tag at C terminus; H149(3.51)Y and S280(6.47)C mutations; C-terminal truncation of 28 amino acids (S354-V381); N-terminal T4L fusion; ICL3 replacement with modified flavodoxin

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane preparation | Dounce homogenization and ultracentrifugation | -- | Hypotonic buffer (10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl, protease inhibitor cocktail); High-osmotic buffer (10 mM HEPES pH 7.5, 1 M NaCl, 10 mM MgCl2, 20 mM KCl, protease inhibitor cocktail) + -- |  |
| Solubilization | Incubation with detergent | -- | 50 mM HEPES pH 7.5, 300 mM NaCl, 0.5% (w/v) DDM, 0.1% (w/v) CHS, 50 µM JNJ-31020028, 2 mg/ml iodoacetamide, protease inhibitor cocktail + n-dodecyl-beta-D-maltopyranoside (DDM), cholesterol hemisuccinate (CHS) |  |
| Affinity purification | TALON immobilized metal affinity chromatography | TALON IMAC resin (Clontech) | Wash: 25 mM HEPES pH 7.5, 300 mM NaCl, 0.05% (w/v) DDM, 0.01% (w/v) CHS, 10 mM imidazole pH 7.4; Elution: wash buffer with 200 mM imidazole + 0.05% DDM, 0.01% CHS |  |
| Size-exclusion chromatography | SEC | Superdex 200 increase 10/300 column | 25 mM HEPES pH 7.5, 300 mM NaCl, 0.05% (w/v) DDM, 0.01% (w/v) CHS, 10 µM JNJ-31020028 + 0.05% DDM, 0.01% CHS |  |

**Final sample**: Purified Y2R-JNJ-31020028 complex in SEC buffer


## Crystallization

No crystallization described.

## Biological / Functional Insights

### Ligand-binding mode of JNJ-31020028

The crystal structure of Y2R bound to JNJ-31020028 at 2.8 Å resolution reveals a binding pocket formed by residues from helices II, III, V, VI, VII, and ECL1. The phenylethyl and diethyl amide groups bind to a cavity shaped by ECL1 and helices II, III, and VII, making hydrophobic contacts with residues T107(2.61), Y110(2.64), T111(2.65), W116(ECL1), V126(3.28), F307(7.35), T308(7.36), and H311(7.39). The benzamide and pyridine groups sit in a subpocket bordered by helices III, V, and VI, interacting with V134(3.36), Y219(5.38), S220(5.39), S223(5.42), L224(5.43), L227(5.46), Y228(5.47), and H285(6.52). The carbonyl of the benzamide group and the pyridine nitrogen form a hydrogen bond network with S220(5.39), H285(6.52), and Q288(6.55).

### Receptor activation and antagonist mechanism

Mutagenesis studies showed that W281(6.48) and H285(6.52) exhibited the largest effect on antagonistic activity, with mutants showing 48-186-fold and 20-153-fold drops, respectively. These residues are consistent with the fact that helix VI exhibits the most profound conformational change during receptor activation, suggesting that antagonist interactions with these residues constrain helix VI rearrangement, stabilizing the receptor in an inactive state.

### Subtype selectivity determinants

Sequence alignment of NPY receptors identified seven residues in the ligand-binding pocket that differ among subtypes: V126(3.28), L183(4.60), S223(5.42), L227(5.46), H285(6.52), Q288(6.55), and T308(7.36). Mutagenesis swapping each to its Y1R counterpart revealed that V126(3.28)N, L227(5.46)Q, H285(6.52)T, and Q288(6.55)N decreased JNJ-31020028 antagonistic activity by 4-186-fold. L227(5.46) and Q288(6.55) were also implied to be important for selectivity of antagonist UR-MK299 in Y1R.


## Cross-References

- [Human NPY Y1 Receptor (Y1R, NPY1R)](/xray-mp-wiki/proteins/gpcr/human-y1-receptor-npy1r/) — Related NPY receptor subtype with previously determined antagonist-bound crystal structures
