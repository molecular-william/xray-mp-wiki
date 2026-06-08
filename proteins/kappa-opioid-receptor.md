---
title: Kappa Opioid Receptor
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2017.12.011]
verified: false
---

# Kappa Opioid Receptor

## Overview

The human kappa opioid receptor (KOP) is a class A G-protein coupled receptor that mediates the actions of opioids with hallucinogenic, dysphoric, and analgesic activities. It is a promising target for the development of safer analgesics devoid of hallucinatory and dysphoric effects. This page covers the active-state crystal structure of KOP in complex with the epoxymorphinan agonist MP1104 and an active-state-stabilizing nanobody (Nb39), solved at 3.1 A resolution.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2017.12.011 | 6B73 | 3.10 | P21 | BRIL-fused KOP (truncated 7TM) | MP1104, Nb39 |

 - R-work 25.4%, R-free 27.5%; Atoms: 882 residues (307 KOP, 134 Nb39), 2 MP1104, 2 cholesterol; Data collection: APS GM/CA CAT 23ID-B/D, 1.033 A wavelength, Dectris Eiger-16m/Pilatus3-6m

## Expression and Purification

- **Expression system**: Sf9 cells (baculovirus expression system)
- **Construct**: BRIL-fused KOP (truncated 7TM) with C-terminal His-tag
- **Notes**: 10 uM naltrexone added to help receptor trafficking during expression

### Purification Workflow

- **Expression system**: Sf9 cells (baculovirus)
- **Expression construct**: BRIL-fused KOP with C-terminal His-tag
- **Tag info**: C-terminal hexa-His tag on BRIL

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell harvest | Centrifugation | — | Sf9 cells harvested 48 h post-infection, washed in 1x PBS, stored at -80 C | Final concentration of 10 uM naltrexone added to help receptor trafficking |
| Membrane preparation | Repeated centrifugation | — | 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl, 500 uM AEBSF, 1 uM E-64, 1 uM Leupeptin, 150 nM Aprotinin (low-salt); 1.0 M NaCl, 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl (high osmolarity) | 4 repeated centrifugations in high osmolarity buffer to remove soluble and membrane-associated proteins. Flash-frozen in liquid nitrogen. |
| Solubilization | Detergent solubilization | — | 10 mM HEPES pH 7.5, 100 mM NaCl, 0.05% DDM, 0.2 mg/mL CHS | Membranes resuspended and solubilized by gentle stirring |
| Affinity purification (TALON) | Cobalt affinity chromatography | TALON IMAC resin (Clontech) | 10 mM HEPES pH 7.5, 100 mM NaCl, 0.01% DDM, 20 mM imidazole (wash); 10 mM HEPES pH 7.5, 100 mM NaCl, 0.01% DDM, 250 mM imidazole (elution) | Supernatant incubated with TALON resin, washed, eluted with imidazole |
| TEV protease cleavage | Proteolytic cleavage | — | 10 mM HEPES pH 7.5, 100 mM NaCl, 0.01% DDM | TEV protease added overnight at 4 C to cleave His-tag from BRIL |
| Second TALON purification | Cobalt affinity chromatography | TALON IMAC resin (Clontech) | 10 mM HEPES pH 7.5, 100 mM NaCl, 0.01% DDM | Flow-through collected containing cleaved BRIL-KOP complex |
| Size exclusion chromatography | Size-exclusion chromatography | Superdex 200 Increase 10/300 GL | 10 mM HEPES pH 7.5, 100 mM NaCl, 0.01% DDM | Final purification step to isolate monodisperse complex |

**Final sample**: BRIL-KOP-MP1104-Nb39 complex, 10-15 mg/mL in 10 mM HEPES pH 7.5, 100 mM NaCl, 0.01% DDM, stored at -80 C with 10% glycerol


## Crystallization

### doi/10.1016##j.cell.2017.12.011

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | BRIL-KOP-MP1104-Nb39 complex at 10-15 mg/mL |
| Lipid | Monoolein |
| Protein-to-lipid ratio | 2:1 |
| Temperature | 20 |
| Growth time | 2-3 days |
| Cryoprotection | Crystals harvested and flash-frozen in liquid nitrogen |
| Notes | 21 crystals merged from beamline 23ID-B/D at APS GM/CA CAT. 2 complexes per asymmetric unit. Data collected at 1.033 A wavelength with 10 um microfocus beam. |


## Biological / Functional Insights

### MP1104 Binding Pocket and Hydrophobic Interactions

MP1104 binds in the orthosteric pocket of active-state KOP with its cyclopropylmethyl group extending into a hydrophobic pocket formed by W287^6.48, G319^7.42, and Y320^7.43. The iodobenzamide moiety forms a water-mediated hydrogen bond with Y312^7.35. Mutations W287^6.48L, G319^7.42L, and Y320^7.43L strongly reduce MP1104 potency for both G protein activation and beta-arrestin2 recruitment. The W287^6.48L mutant selectively reduces beta-arrestin2 recruitment, suggesting this pocket is a node linking binding pocket changes to transducer engagement.

### KOP Activation Mechanism and Signal Propagation

Activation-related conformational changes propagate from the orthosteric site through several key motifs: (1) The D^3.32YYNM^3.36 anchoring motif in TM3 rearranges upon agonist binding. (2) The CWxP motif residue W287^6.48 couples to the P^5.50-I^3.40-F^6.44 toggle switch microswitch, where P238^5.50 moves inward and I146^3.40 changes rotameric state, promoting F283^6.44 rotation. (3) This rotation drives TM6 outward displacement of ~10 A, opening the intracellular surface for transducer binding. (4) The sodium pocket between TM2/TM3/TM7 collapses upon activation, with D105^2.50 forming a new H-bond with S145^3.39. (5) The NPxxY motif and DRY motif undergo characteristic rearrangements.

### Subtype-Specific Structural Determinants and Biased Signaling

Position 7.35 differs between KOP (Y312^7.35) and MOP (W320^7.35), creating different receptor interactions for iodobenzamide ligands. The KOP Y312^7.35W mutant strongly reduces IBNtxA-mediated arrestin recruitment while having minimal effect on MP1104, demonstrating pathway-selective attenuation. MP1104 acts as a balanced full agonist in both KOP and MOP (bias factor ~0.6-1.6 toward G protein), while IBNtxA is G-protein-biased in MOP (bias factor 12) but balanced in KOP (bias factor 1.5). These findings provide structural insights for designing KOP-selective and biased ligands.


## Cross-References

- [MP1104](/xray-mp-wiki/reagents/ligands/mp1104/) — Co-crystallized epoxymorphinan agonist in PDB 6B73
- [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) — Fusion partner used in crystallization construct
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for solubilization and crystallization
- [Cholesterol hemisucinate](/xray-mp-wiki/reagents/lipids/cholesterol-hydrogen-succinate/) — Membrane protein stabilizer in solubilization buffer
