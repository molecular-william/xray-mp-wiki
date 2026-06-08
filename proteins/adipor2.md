---
title: Adiponectin Receptor 2 (ADIPOR2)
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature21714]
verified: false
---

# Adiponectin Receptor 2 (ADIPOR2)

## Overview

Adiponectin receptor 2 (ADIPOR2) is an integral membrane protein that belongs to the progesterone and adipoQ receptor (PAQR) family. It has a seven-transmembrane (7TM) domain architecture with a zinc binding site within the transmembrane region. ADIPOR2 mediates cellular ceramidase activity that hydrolyses ceramide into sphingosine and a free fatty acid (FFA), and this activity is enhanced by adiponectin binding. The receptor was crystallized in complex with an scFv antibody fragment using lipidic cubic phase (LCP) crystallization.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature21714 | 5LX9 | 2.4 A | P212121 | ADIPOR2-scFv complex (residues 100-386, N-terminal Flag tag, in complex with anti-ADIPOR scFv) | Oleic acid (FA C18:1) |
| doi/10.1038##nature21714 | 5LWY | 2.4 A | P212121 | ADIPOR2-scFv complex (residues 100-386, N-terminal Flag tag, in complex with anti-ADIPOR scFv) | Oleic acid (FA C18:1) |
| doi/10.1038##nature21714 | 5LXA | 3.0 A | P212121 | ADIPOR2-scFv complex (residues 100-386, N-terminal Flag tag, in complex with anti-ADIPOR scFv) | Oleic acid (FA C18:1) |

## Expression and Purification

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Baculovirus expression in Sf9 insect cells (pFastBac system, ThermoFisher) | — | Not specified | N-terminally truncated ADIPOR2 construct (residues 100-386) with N-terminal Flag epitope tag |
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
| Notes | ADIPOR2-scFv complex crystallized in monoolein LCP. Three structures solved: S1 (5LX9, 2.4 A), S2 (5LWY, 2.4 A), and S3 (5LXA, 3.0 A). Crystals grown without or with ceramide-doped lipidic cubic phase. Oleic acid observed bound in a hydrophobic cavity within the transmembrane domain.
 |


## Biological / Functional Insights

### Intrinsic ceramidase activity

ADIPOR2 possesses intrinsic basal ceramidase activity that converts ceramide into sphingosine and a free fatty acid. Michaelis-Menten kinetic analysis determined a Km of 15.6 uM and a kcat of 0.49 x 10^-3 s^-1. The activity is low but comparable to other intramembrane proteins such as gamma-secretase. ADIPOR2 shows preference for C18 ceramide substrate but can also hydrolyse C6 and C24 ceramides to a lesser extent.

### Adiponectin-enhanced ceramidase activity

Adiponectin increases the basal ADIPOR2 ceramidase activity approximately 20-fold. This suggests that adiponectin binding to ADIPOR2 allosterically enhances its enzymatic function.

### Zinc-dependent catalytic mechanism

ADIPOR2 contains a zinc binding site within the 7TM domain close to the intracellular surface. The zinc is coordinated by residues including H202 (TM2), S168 (TM2), H348 (TM7), and H352 (TM7). Molecular dynamics simulations suggest a mechanism in which H348 acts as a general acid/base that promotes nucleophilic attack of a zinc-bound hydroxide ion onto the ceramide amide carbonyl. Residues R278 (TM5) and Y328 (TM6) serve as carbonyl-polarizing and oxyanion-stabilizing residues.

### Closed conformation with buried substrate binding pocket

The ADIPOR2 crystal structures reveal a closed conformation with a large internal cavity that is largely buried within the transmembrane domain. The ceramide binding pocket and zinc catalytic site are buried, accessible through a transmembrane opening and an intracellular opening. The fatty acid product remains bound in a hydrophobic pocket while the sphingosine moiety would diffuse toward the cytoplasm through the intracellular cavity.


## Cross-References

- [Adiponectin Receptor 1 (ADIPOR1)](/xray-mp-wiki/proteins/adipor1/) — Homologous receptor with ceramidase activity, distinct open conformation
- [Adiponectin](/xray-mp-wiki/proteins/adiponectin/) — Hormone that activates ADIPOR2 and enhances ceramidase activity
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Primary lipid for LCP crystallization of ADIPOR2-scFv complex
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for solubilization and purification
- [Cholesteryl Hemisuccinate (CHS)](/xray-mp-wiki/reagents/lipids/cholesteryl-hemisuccinate/) — Lipid additive used with DDM for membrane protein stabilization
- [Ceramide](/xray-mp-wiki/reagents/lipids/ceramide/) — Substrate for ADIPOR2 ceramidase activity
- [Sphingosine](/xray-mp-wiki/reagents/lipids/sphingosine/) — Product of ADIPOR2 ceramidase-mediated ceramide hydrolysis
- [PAQR Family (Progesterone and AdipoQ Receptor Family)](/xray-mp-wiki/concepts/paqr-family/) — ADIPOR2 belongs to the PAQR protein family
