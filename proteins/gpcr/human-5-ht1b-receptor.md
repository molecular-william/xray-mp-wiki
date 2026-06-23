---
title: "Human 5-HT1B Serotonin Receptor"
created: 2026-06-21
updated: 2026-06-21
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1232807]
verified: false
---

# Human 5-HT1B Serotonin Receptor

## Overview

The human 5-HT1B receptor is a class A G protein-coupled receptor for serotonin (5-hydroxytryptamine, 5-HT). It couples preferentially to Gi proteins and is widely expressed in the central nervous system. 5-HT1B receptors are therapeutic targets for migraine treatment (triptan class drugs) and are implicated in mood disorders. Crystal structures of 5-HT1B in complex with ergotamine (ERG) and dihydroergotamine (DHE) were determined using BRIL fusion constructs and LCP crystallization, revealing the molecular basis for ligand recognition and selectivity across serotonin receptor subtypes.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.1232807 | 4IAR | 2.7 | C2 | Human 5-HT1B-BRIL fusion (ICL3 residues L240-M305 replaced by BRIL; N-terminal truncation at N32; L138³·⁴¹W thermostabilizing mutation), in complex with ergotamine (ERG) | Ergotamine (ERG) |
| doi/10.1126##science.1232807 | 4IAR | 2.8 | C222 | Human 5-HT1B-BRIL fusion (5-HT1B-2 construct, ICL3 residues L240-K303 replaced by BRIL; N-terminal truncation at N32; L138³·⁴¹W mutation), in complex with dihydroergotamine (DHE) | Dihydroergotamine (DHE) |

## Expression and Purification

- **Expression system**: Spodoptera frugiperda (Sf9) insect cells via baculovirus
- **Construct**: Human 5-HT1B with BRIL fusion replacing ICL3; N-terminal HA signal sequence + Flag tag + 10×His tag + TEV protease site; N32 truncation; L138³·⁴¹W thermostabilizing mutation

### Purification Workflow

- **Expression system**: Spodoptera frugiperda Sf9 insect cells
- **Expression construct**: 5-HT1B-BRIL fusion (ICL3 replacement) with N-terminal HA-Flag-10×His-TEV tag
- **Tag info**: 10×His tag + Flag tag, cleaved by AcTEV protease

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and expression | Baculovirus infection (P2, MOI 5) | -- | Sf9 cells in suspension + -- | 48 h post-infection at 27 °C |
| Membrane preparation | Hypotonic lysis and high-salt wash | -- | 10 mM HEPES pH 7.5, 10 mM MgCl₂, 20 mM KCl + protease inhibitors; then 1.0 M NaCl, 10 mM HEPES pH 7.5, 10 mM MgCl₂, 20 mM KCl + -- | Washed membranes resuspended in buffer with 50 µM ligand (ERG or DHE) + 2 mg/ml iodoacetamide |
| Solubilization | Detergent extraction | -- | 50 mM HEPES pH 7.5, 200 mM NaCl, 20 mM imidazole + 1% (w/v) DDM, 0.2% (w/v) CHS | 4 °C, 1 h incubation; supernatant clarified at 160,000×g for 30 min |
| Immobilized metal affinity chromatography | TALON IMAC | TALON IMAC resin (Clontech) | Wash I: 50 mM HEPES pH 7.5, 800 mM NaCl, 50 µM ligand, 20 mM imidazole, 10% glycerol, 0.1% DDM, 0.02% CHS, 10 mM ATP, 10 mM MgCl₂; Wash II: 50 mM HEPES pH 7.5, 500 mM NaCl, 50 mM imidazole, 50 µM ligand, 10% glycerol, 0.05% DDM, 0.01% CHS + 0.1% DDM / 0.02% CHS (Wash I); 0.05% DDM / 0.01% CHS (Wash II) | Eluted with 250 mM imidazole in 50 mM HEPES pH 7.5, 500 mM NaCl, 50 µM ligand, 10% glycerol, 0.05% DDM, 0.01% CHS |
| Buffer exchange | PD MiniTrap G-25 desalting | PD MiniTrap G-25 (GE Healthcare) | 50 mM HEPES pH 7.5, 500 mM NaCl, 50 µM ligand, 10% glycerol, 0.05% DDM, 0.01% CHS + 0.05% DDM, 0.01% CHS | Removes imidazole |
| Tag cleavage | AcTEV protease treatment | -- | 50 mM HEPES pH 7.5, 500 mM NaCl, 50 µM ligand, 10% glycerol, 0.05% DDM, 0.01% CHS + 0.05% DDM, 0.01% CHS | Overnight at 4 °C; His-tagged AcTEV and cleaved fragment removed by second TALON IMAC incubation |
| Concentration | Centrifugal concentration | -- | 50 mM HEPES pH 7.5, 500 mM NaCl, 50 µM ligand, 10% glycerol, 0.05% DDM, 0.01% CHS + 0.05% DDM, 0.01% CHS | Concentrated to 50-80 mg/ml using 100 kDa MWCO Vivaspin; purity >95% by SDS-PAGE; single peak by aSEC |

**Final sample**: 50-80 mg/ml in 50 mM HEPES pH 7.5, 500 mM NaCl, 50 µM ligand (ERG or DHE), 10% glycerol, 0.05% DDM, 0.01% CHS
**Yield**: --
**Purity**: >95% by SDS-PAGE; monodisperse by aSEC


## Crystallization

### doi/10.1126##science.1232807

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | 5-HT1B-1/ERG complex (construct 5-HT1B-1) |
| Lipid | Monoolein (54% w/w) + cholesterol (6% w/w) |
| Protein-to-lipid ratio | 40% (w/w) protein solution, 54% monoolein, 6% cholesterol |
| Temperature | 20 °C |
| Growth time | 2-3 days |
| Cryoprotection | Crystals harvested from LCP matrix; flash frozen in liquid nitrogen |
| Notes | Crystals grew to 20-50 µm; 40 nL protein-lipid overlaid with 800 nL precipitant; 96-well glass sandwich plates |

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | 5-HT1B-2/DHE complex (construct 5-HT1B-2) |
| Lipid | Monoolein (54% w/w) + cholesterol (6% w/w) |
| Protein-to-lipid ratio | 40% (w/w) protein solution, 54% monoolein, 6% cholesterol |
| Temperature | 20 °C |
| Growth time | 2-3 days |
| Cryoprotection | Crystals harvested from LCP matrix; flash frozen in liquid nitrogen |
| Notes | Crystals grew to 20-50 µm; data from 56 crystals merged for 2.8 Å structure |


## Biological / Functional Insights

### Extended binding pocket differs between 5-HT1B and 5-HT2B

Comparison of the 5-HT1B/ERG and 5-HT2B/ERG structures reveals that the orthosteric binding pocket is conserved, but the extended binding site differs significantly between the two receptors. The tripeptide moiety of ERG and DHE extends into an extended binding pocket created by extracellular loop 2 (ECL2), where sequence divergence between 5-HT1B and 5-HT2B accounts for differences in ligand selectivity. This extended pocket is a key determinant of triptan drug selectivity for 5-HT1B/1D over 5-HT2B receptors.

### Membrane-embedded ligand entry via TM5-TM6 gap

Like the S1P1 receptor, 5-HT1B shows a gap between the extracellular ends of TM5 and TM6 that may provide a membrane-embedded access route for ligands. The N-terminal cap and ECL2 restrict direct access from the extracellular milieu, suggesting that lipophilic ergolines and triptans access the binding pocket through the lipid bilayer.

### BRIL fusion strategy for GPCR crystallization

The 5-HT1B structures used BRIL (thermostabilized apocytochrome b₅₆₂ RIL mutant) replacing ICL3, enabling LCP crystallization. Two different BRIL junction sites were tested (5-HT1B-1: L240-M305 replaced; 5-HT1B-2: L240-K303 replaced), with the L138³·⁴¹W mutation further stabilizing the receptor. Both constructs showed ligand binding properties similar to wild type, validating the fusion approach.


## Cross-References

- [Human 5-HT2B Receptor](/xray-mp-wiki/proteins/gpcr/human-5-ht2b-receptor/) — Closely related serotonin receptor; structural comparison for ligand selectivity
- [Ergotamine (ERG)](/xray-mp-wiki/reagents/ligands/ergotamine/) — Ligand used for 5-HT1B-1 structure determination
- [BRIL (Thermostabilized apocytochrome b562 RIL)](/xray-mp-wiki/reagents/protein-tags/bril/) — Fusion protein used for crystallization
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for solubilization and purification
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used for 5-HT1B crystallization
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Primary lipid for LCP matrix
