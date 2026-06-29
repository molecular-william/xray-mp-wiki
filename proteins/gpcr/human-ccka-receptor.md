---
title: "Human Cholecystokinin A Receptor (CCKₐR)"
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein]
sources: [doi/10.1038##s41589-021-00866-8]
verified: false
---

# Human Cholecystokinin A Receptor (CCKₐR)

## Overview

The human cholecystokinin A receptor (CCKₐR) is a class A G-protein-coupled receptor (GPCR) that preferentially binds sulfated cholecystokinin (CCK) peptides. CCKₐR plays vital roles in food intake regulation, pancreatic enzyme secretion, and gall bladder contraction. Crystal structures of human CCKₐR have been determined in complex with two small-molecule antagonists (devazepide at 2.5 Å, PDB 7F8W; lintitript at 2.8 Å, PDB 7F8V) and one peptide agonist analog (NN9056 at 3.0 Å, PDB 7F8W — the same PDB code covers multiple structures). The structures revealed an ECL3 forming a two-turn α-helical conformation (never before observed in class A GPCRs) and a β-hairpin in ECL2 typical of peptide receptors. The agonist-bound structure showed an inward shift of helix VI in the ligand-binding region as an early step toward activation.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41589-021-00866-8 | 7F8W | 2.50 | P2₁2₁2 | Human CCKₐR with T4L fusion in ICL3 (between I240 and A302), C-terminal truncation (G407-Q428), mutation D87²·⁵⁰N for inactive state stabilization | Devazepide (antagonist) |
| doi/10.1038##s41589-021-00866-8 | 7F8V | 2.80 | P2₁2₁2 | Human CCKₐR with T4L fusion in ICL3, C-terminal truncation, D87²·⁵⁰N mutation | Lintitript (antagonist) |
| doi/10.1038##s41589-021-00866-8 | 7F8W | 3.00 | P2₁2₁2 | Human CCKₐR with T4L fusion in ICL3, C-terminal truncation, F130³·⁴⁰W mutation | NN9056 (peptide agonist analog) |

## Expression and Purification

- **Expression system**: Spodoptera frugiperda (Sf9) insect cells (Bac-to-Bac baculovirus expression system)
- **Construct**: Human CCKₐR with HA signal sequence, Flag tag, N-terminal tag, PreScission protease site, 10× His tag at C-terminus; T4L inserted at ICL3 (I240-A302) with C-terminal truncation (G407-Q428)

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1. Membrane preparation and solubilization | Detergent extraction | — | 50 mM HEPES pH 7.5, 500 mM NaCl, 10% glycerol, 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.1% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 10 μM ligand | Sf9 cell membranes solubilized for 2 h at 4°C |
| 2. Ni-NTA affinity chromatography | Immobilized metal [affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | — | 50 mM HEPES pH 7.5, 500 mM NaCl, 10% glycerol, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.005% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 20 mM imidazole | Protein eluted with 200 mM imidazole |
| 3. PreScission protease cleavage | Protease treatment | — | 50 mM HEPES pH 7.5, 500 mM NaCl, 10% glycerol, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.005% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Overnight cleavage at 4°C to remove N-terminal tag |
| 4. Size-exclusion chromatography | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 10/300 GL | — | 25 mM HEPES pH 7.5, 150 mM NaCl, 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.002% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 10 μM ligand | Peak fractions concentrated to 20 mg/ml for crystallization |


## Crystallization

### doi/10.1038##s41589-021-00866-8

| Parameter | Value |
|---|---|
| Method | [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) (LCP) |
| Protein sample | CCKₐR-T4L at ~20 mg/ml in 25 mM HEPES pH 7.5, 150 mM NaCl, 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.002% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) |
| Temperature | 20°C |
| Growth time | 3-7 days |
| Notes | Data collected at SPring-8 beamline BL41XU. Structures solved by molecular replacement using T4L and a GPCR template. Diffraction data from [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/)-grown crystals with space group P2₁2₁2. |


## Biological / Functional Insights

### Unique ECL3 α-helical conformation in CCKₐR

The third extracellular loop (ECL3) of CCKₐR adopts a two-turn α-helical conformation that has never been observed before in other class A GPCR structures. This unusual ECL3 architecture may play a role in ligand recognition and receptor activation.

### ECL2 β-hairpin and peptide recognition

ECL2 of CCKₐR forms a β-hairpin structure similar to other peptide-activated GPCRs. Key residue R197 in ECL2 forms a salt bridge with the sulfated tyrosine of CCK peptides, which is critical for high-affinity binding. Mutation R197A greatly diminishes CCK-8 binding.

### Helix VI movement in partial activation

Upon binding the agonist NN9056, an approximately 1 Å inward shift of helix VI in the ligand-binding region was observed compared to antagonist-bound structures. This represents an early conformational change toward receptor activation, though the full active state requires G protein coupling.


## Cross-References

- [Human Cholecystokinin B Receptor (CCKᴅR)](/xray-mp-wiki/proteins/gpcr/human-cckb-receptor/) — Sister receptor with distinct peptide selectivity; complementary structures from same study
- [Peptide Selectivity in Cholecystokinin Receptors](/xray-mp-wiki/concepts/signaling-receptors/cck-receptor-peptide-selectivity/) — Structural basis for CCKₐR preference for sulfated CCK over gastrin
- [Stepwise Activation of Cholecystokinin Receptors](/xray-mp-wiki/concepts/signaling-receptors/cck-receptor-stepwise-activation/) — The CCKₐR structures in antagonist, agonist, and G protein-bound states reveal a stepwise activation mechanism
