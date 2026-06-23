---
title: Human Thromboxane A2 Receptor (TP)
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41589-018-0170-9]
verified: false
---

# Human Thromboxane A2 Receptor (TP)

## Overview

The human thromboxane A2 receptor (TP) is a class A G-protein-coupled receptor that mediates the physiological actions of thromboxane A2 (TXA2), an endogenous arachidonic acid metabolite. TP plays a pivotal role in cardiovascular homeostasis and is considered an important drug target for cardiovascular disease. Two splice variants have been identified (TPα and TPβ) that share the same N-terminal 328 residues but differ in their C-terminal tails. Crystal structures of TP bound to the nonprostanoid antagonists ramatroban (2.5 A, PDB 6IIU) and daltroban (3.0 A, PDB 6IIV) revealed a ligand-binding pocket capped by two layers of extracellular loops stabilized by two disulfide bonds (C11-C102 and C105-C183), limiting ligand access from the extracellular milieu. The structures provide a detailed picture of ligand recognition, with the carboxylic acid group of antagonists forming salt bridges with H89(2.65) and R295(7.40) and a hydrogen bond with S181. The benzenesulfonamide moiety occupies a subpocket shaped by helices II, III, VI and VII, with hydrogen bonds to T81(2.57) and Q301(7.46). Molecular docking of prostanoid-like ligands SQ-29548 and U46619, combined with mutagenesis and functional assays, suggests a shared prostanoid binding mode across prostanoid receptors.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41589-018-0170-9 | 6IIU | 2.5 A | P 1 2 1 | TPα with bRIL fused at N terminus and rubredoxin fused in ICL3; C-terminal truncation (S324-Q343); L247(6.37) mutation; expressed in Sf9 insect cells via baculovirus | Ramatroban |
| doi/10.1038##s41589-018-0170-9 | 6IIV | 3.0 A | P 1 2 1 | TPα with bRIL fused at N terminus and rubredoxin fused in ICL3; C-terminal truncation (S324-Q343); L247(6.37) mutation; expressed in Sf9 insect cells via baculovirus | Daltroban |

## Expression and Purification

- **Expression system**: Spodoptera frugiperda (Sf9) insect cells via Bac-to-Bac baculovirus expression system
- **Construct**: Codon-optimized human TPα with N-terminal HA signal sequence and Flag tag, C-terminal PreScission site and 10xHis tag; bRIL fusion at N terminus; rubredoxin fusion in ICL3; C-terminal truncation of 20 residues (S324-Q343); L247(6.37) point mutation

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Hypotonic lysis and centrifugation | — | 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl, protease inhibitors | Washed with high-salt buffer (1 M NaCl) to remove membrane-associated proteins |
| Solubilization | DDM solubilization | — | 50 mM HEPES pH 7.5, 150 mM NaCl, 0.5% DDM, 0.1% CHS | Incubated 3 h at 4°C with 100 uM ramatroban or daltroban |
| Affinity chromatography | TALON IMAC | TALON IMAC resin (Clontech) | 20 mM HEPES pH 7.5, 150 mM NaCl, 10% glycerol, 0.05% DDM, 0.01% CHS, 30 mM imidazole | Washed with 30 column volumes; eluted with 200-300 mM imidazole |
| Final purification | Size-exclusion chromatography | Superdex 200 Increase 10/300 GL | 25 mM HEPES pH 7.5, 150 mM NaCl, 10% glycerol, 0.05% DDM, 0.01% CHS | Peak fractions pooled and concentrated |


## Crystallization

### doi/10.1038##s41589-018-0170-9

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | TP-ramatroban complex at ~25 mg/mL |
| Temperature | 20\u00B0C |
| Growth time | 3-4 weeks |
| Cryoprotection | PEG 400 as cryoprotectant (by LCP method) |
| Notes | Crystals grew in LCP with monoolein (9.5 A/0.9 A); data collected from 16 crystals for ramatroban, 49 crystals for daltroban |


## Biological / Functional Insights

### Two-layer extracellular cap with unique disulfide bonds

The TP structures reveal a unique double-layer extracellular lid formed by two disulfide bonds: the conserved C105(3.25)-C183 bridge between helix III and ECL2, and a novel C11-C102(3.22) bond connecting the N terminus and the extracellular tip of helix III. This two-layer cover constrains ligand access from the extracellular milieu, suggesting ligands enter through the lipid bilayer via a gap between helices I and VII.

### Conserved prostanoid carboxylate-binding motif

The carboxylic acid group of both ramatroban and daltroban forms critical polar interactions with residues H89(2.65), S181 (ECL2), and R295(7.40). This binding mode is conserved across prostanoid receptors, explaining previous mutagenesis data showing that mutations at R(7.40) abolish ligand binding. The residue S181 is conserved across the prostanoid receptor subfamily (except DP2).

### Prostanoid binding mode revealed by docking

Molecular docking of prostanoid-like ligands SQ-29548 and U46619 into the TP structure reveals a V-shaped binding pose. The central ring orients toward helix I, with the alpha-chain (containing the heptenoic acid group) contacting helices II, III, VII and ECL2, and the omega-chain overlapping with the benzenesulfonamide tail of nonprostanoid antagonists. Mutagenesis confirmed the importance of T81(2.57), H89(2.65), S181, R295(7.40), and Q301(7.46) for ligand binding.

### Selectivity determinants across prostanoid receptors

Sequence alignment reveals that residues predicted to interact with the central ring of prostanoids are less conserved between different prostanoid receptors compared to residues forming contacts with the two side tails. This provides new insights into prostanoid receptor selectivity, suggesting the central ring configuration determines receptor specificity as previously proposed from pharmacological classification.


## Cross-References

- [Prostanoid Receptor Family](/xray-mp-wiki/concepts/prostanoid-receptor-family/) — TP is a member of the prostanoid receptor family; structures provide first atomic-level view of TP ligand recognition
- [GPCR Inactive Conformation](/xray-mp-wiki/concepts/gpcr-inactive-conformation/) — TP-ramatroban and TP-daltroban structures represent antagonist-bound inactive state of a prostanoid receptor
- [CRTH2 (DP2)](/xray-mp-wiki/proteins/gpcr/crth2/) — Another prostanoid receptor with distinct ligand-binding mode; comparison highlights diversity in prostanoid receptor ligand recognition
- [Disulfide Bond Formation](/xray-mp-wiki/concepts/disulfide-bond-formation/) — Unique C11-C102 disulfide bond in extracellular region stabilizes the two-layer lid over the ligand-binding pocket
