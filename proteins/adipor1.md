---
title: Adiponectin Receptor 1 (ADIPOR1)
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature21714]
verified: false
---

# Adiponectin Receptor 1 (ADIPOR1)

## Overview

Adiponectin receptor 1 (ADIPOR1) is an integral membrane protein that belongs to the progesterone and adipoQ receptor (PAQR) family. It has a seven-transmembrane (7TM) domain architecture with a zinc binding site within the transmembrane region, similar to ADIPOR2. ADIPOR1 also possesses intrinsic ceramidase activity that is sensitive to adiponectin. A revised crystal structure of ADIPOR1 reveals an open conformation with the catalytic site exposed to the inner membrane leaflet, distinct from the closed conformation of ADIPOR2.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature21714 | 5LXG | Not specified (revised from 3WXV) | Not specified | ADIPOR1 (residues 89-375, N-terminal Flag tag, revised structure from PDB 3WXV) | None observed |

## Expression and Purification

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Baculovirus expression in Sf9 insect cells (pFastBac system, ThermoFisher) | — | Not specified | N-terminally truncated ADIPOR1 construct (residues 89-375) with N-terminal Flag epitope tag |
| Cell lysis | Osmotic shock in 10 mM Tris-HCl pH 7.5, 1 mM EDTA, 2 mg/ml iodoacetamide | — | 10 mM Tris-HCl pH 7.5, 1 mM EDTA, 2 mg/ml iodoacetamide | Cells lysed by osmotic shock with protease inhibitors |
| Solubilization | Glass dounce tissue grinder in solubilization buffer | — | 20 mM HEPES pH 7.5, 100 mM NaCl, 1% DDM, 0.1% CHS, 2 mg/ml iodoacetamide | Stirred 1 h at 4 C |
| Detergent adjustment | Dilution to working concentration | — | 20 mM HEPES pH 7.4, 300 mM NaCl, 0.5% DDM, 0.05% CHS | Adjusted for anti-Flag affinity chromatography |
| Anti-Flag affinity chromatography | Anti-Flag M2 antibody resin (Sigma) | — | 20 mM HEPES pH 7.4, 300 mM NaCl, 0.5% DDM, 0.05% CHS | Gravity flow loading |
| Washing | Anti-Flag M2 resin wash | — | 20 mM HEPES pH 7.4, 200 mM NaCl, 0.025% DDM, 0.0001% CHS | Wash buffer 1 |
| Elution | Flag peptide elution | — | 20 mM HEPES pH 7.4, 200 mM NaCl, 0.025% DDM, 0.0001% CHS, 0.4 mg/ml Flag peptide | Bound receptor eluted with Flag peptide |
| Purity evaluation | SDS-PAGE and analytical SEC | — | Not specified | Purity and monodispersity evaluated |


## Crystallization

### doi/10.1038##nature21714

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Lipid | Monoolein |
| Temperature | Not specified |
| Notes | Revised ADIPOR1 structure (5LXG) from re-analysis of PDB 3WXV data. The revised structure shows a clear improvement in statistics. No FFA is observed in the structure. Large rearrangements of TM5 and intracellular loop 2 (ICL2) compared to ADIPOR2 structures. The zinc coordination sphere is similar to ADIPOR2.
 |


## Biological / Functional Insights

### Open conformation exposes catalytic site

The revised ADIPOR1 structure reveals an open conformation in which the putative catalytic site and substrate binding domain are exposed to the cytoplasm and fully accessible to the inner membrane leaflet. This is in stark contrast to the buried cavity of ADIPOR2. TM5 of ADIPOR1 is tilted by 20 degrees and translated 15 angstroms at the intracellular end compared to ADIPOR2. The largest structural shift is at residue M268 (TM5) of ADIPOR2 and R257 (TM5) of ADIPOR1, with a 17 angstrom shift.

### Intrinsic ceramidase activity

ADIPOR1 possesses intrinsic adiponectin-sensitive ceramidase activity, demonstrated using purified receptor preparations. The ceramidase activity of ADIPOR1 is inhibited by the H191R mutation (TM2) in the zinc binding domain, analogous to the H202R mutation in ADIPOR2.

### Conformational equilibrium model

The structural differences between ADIPOR1 (open) and ADIPOR2 (closed) suggest a dynamic equilibrium between open and closed conformations during the enzymatic process. The open conformation may allow substrate access from the inner membrane leaflet, while the closed conformation traps the substrate for catalysis and product release.


## Cross-References

- [Adiponectin Receptor 2 (ADIPOR2)](/xray-mp-wiki/proteins/adipor2/) — Homologous receptor with ceramidase activity, closed conformation
- [Adiponectin](/xray-mp-wiki/proteins/adiponectin/) — Hormone that activates ADIPOR1 and enhances ceramidase activity
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Primary lipid for LCP crystallization
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for solubilization and purification
- [Cholesteryl Hemisuccinate (CHS)](/xray-mp-wiki/reagents/lipids/cholesteryl-hemisuccinate/) — Lipid additive used with DDM for membrane protein stabilization
- [Ceramide](/xray-mp-wiki/reagents/lipids/ceramide/) — Substrate for ADIPOR1 ceramidase activity
- [Sphingosine](/xray-mp-wiki/reagents/lipids/sphingosine/) — Product of ADIPOR1 ceramidase-mediated ceramide hydrolysis
- [PAQR Family (Progesterone and AdipoQ Receptor Family)](/xray-mp-wiki/concepts/paqr-family/) — ADIPOR1 belongs to the PAQR protein family
