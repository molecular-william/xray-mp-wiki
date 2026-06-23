---
title: Human 5-HT2B Serotonin Receptor Bound to Ergotamine
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein]
sources: [doi/10.1126##science.1232808]
verified: false
---

# Human 5-HT2B Serotonin Receptor Bound to Ergotamine

## Overview

The 5-HT2B receptor is a class A G protein-coupled receptor (GPCR) for [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki/reagents/ligands/serotonin/) (5-hydroxytryptamine) involved in cardiovascular function, CNS signaling, and valvular heart disease pathogenesis. This crystal structure captures the receptor bound to [ERG](/xray-mp-wiki/reagents/ligands/ergotamine/) ([ERG](/xray-mp-wiki/reagents/ligands/ergotamine/)) in an active-like conformation, revealing structural features that govern functional selectivity (biased agonism) between G protein and beta-arrestin signaling pathways. The structure was solved at 2.7 Å resolution using lipidic cubic phase (LCP) crystallization and data merged from 17 crystals.


## Structure Determination

No structure determined.

## Expression and Purification

- **Expression system**: Spodoptera frugiperda (Sf9) insect cells
- **Construct**: Delta N(1-35)-5-HT2B-BRIL-Delta C(406-481); HA signal + [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) N-terminal; PreScission site + 10xHis C-terminal
- **Notes**: Bac-to-Bac baculovirus system, MOI 5, harvested 48h post-infection at 27C

### Purification Workflow

- **Expression system**: Spodoptera frugiperda (Sf9) insect cells
- **Expression construct**: Delta N-5-HT2B-BRIL-Delta C with N-terminal HA-FLAG and C-terminal PreScission-10xHis
- **Tag info**: C-terminal 10xHis tag removed by [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Hypotonic lysis and high-salt wash | — | 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl; high-salt wash: 1.0 M NaCl, 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl | EDTA-free protease inhibitors; washed 2x hypotonic, 4-5x high-salt |
| Ligand incubation | Incubation | — | 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl, 150 mM NaCl | 100 uM [ERG](/xray-mp-wiki/reagents/ligands/ergotamine/) for 1h at RT; 2 mg/ml [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) for 30 min at 4C |
| Solubilization | Detergent solubilization | — | 10 mM HEPES pH 7.5, 150 mM NaCl, 50 uM [ERG](/xray-mp-wiki/reagents/ligands/ergotamine/) + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.2% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | 2h at 4C; unsolubilized material removed at 150,000xg for 30 min |
| Immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [TALON](/xray-mp-wiki/reagents/additives/talon/) IMAC | [TALON](/xray-mp-wiki/reagents/additives/talon/) IMAC resin (Clontech) | Wash I: 50 mM HEPES pH 7.5, 800 mM NaCl, 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.02% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 50 uM [ERG](/xray-mp-wiki/reagents/ligands/ergotamine/); Wash II: 50 mM HEPES pH 7.5, 150 mM NaCl, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 50 uM [ERG](/xray-mp-wiki/reagents/ligands/ergotamine/) | Elution in Wash II + 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/); [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) removed via PD MiniTrap G-25 |
| Tag cleavage | [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) digestion | — |  | His-tagged PreScission; overnight; protease and uncleaved protein removed by second [TALON](/xray-mp-wiki/reagents/additives/talon/) IMAC |
| Concentration | Centrifugal concentration | — |  | 100 kDa MWCO Vivaspin; concentrated to ~50 mg/ml; purity >95% by SDS-PAGE |

**Final sample**: ~50 mg/ml in Wash Buffer II (without [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/))
**Purity**: >95% by SDS-PAGE; monodisperse by aSEC


## Crystallization

### doi/10.1126##science.1232808

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/)/cholesterol mixture (40%:54%:6%) |
| Protein-to-lipid ratio | 40% protein : 60% lipid |
| Temperature | 20 |
| Growth time | 3 days |
| Cryoprotection | Flash-frozen directly from LCP matrix |
| Notes | Crystals grown in 96-well glass sandwich plates; NT8-LCP robot; 40 nl LCP drops + 800 nl precipitant; crystals up to 100x30x20 um |


## Biological / Functional Insights

### Functional Selectivity at 5-HT2B

The 5-HT2B/ERG complex reveals that [ERG](/xray-mp-wiki/reagents/ligands/ergotamine/) induces beta-arrestin-biased signaling at the 5-HT2B receptor but not at the 5-HT1B receptor. The structural basis involves a unique kink in helix V of 5-HT2B that engages helix VI through S2225.43-N3446.45 hydrogen bonding and hydrophobic contacts mediated by the [ERG](/xray-mp-wiki/reagents/ligands/ergotamine/) phenyl moiety. This interaction selectively impairs G protein signaling while preserving beta-arrestin recruitment, providing a structural mechanism for biased agonism.

### Active-State Conformation

The 5-HT2B/ERG complex adopts an active-state conformation intermediate between inactive (Rho-R, A2AAR-R) and fully active (Ops-R*, A2AAR-R*) states. Helix VI shows outward displacement characteristic of active GPCRs, while helix VII adopts an intermediate active-state position. The D(E)/RY and NPxxY motifs show distinct activation features compared to both inactive and fully active receptors.

### Extended Ligand Binding Site

[ERG](/xray-mp-wiki/reagents/ligands/ergotamine/) occupies the orthosteric binding pocket with its ergoline core, while its tripeptide moiety extends into an extended binding site that differs between 5-HT1B and 5-HT2B receptors. This differential engagement contributes to the functional selectivity profiles of [ERG](/xray-mp-wiki/reagents/ligands/ergotamine/) and related ergolines.


## Cross-References

- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Additive used in purification or crystallization buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) — Additive used in purification or crystallization buffers
- [PEG400](/xray-mp-wiki/reagents/additives/peg-400/) — Additive used in purification or crystallization buffers
- [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) — Additive used in purification or crystallization buffers
- [TALON](/xray-mp-wiki/reagents/additives/talon/) — Additive used in purification or crystallization buffers
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used in purification or crystallization
- [ERG](/xray-mp-wiki/reagents/ligands/ergotamine/) — Related ligand or cofactor
