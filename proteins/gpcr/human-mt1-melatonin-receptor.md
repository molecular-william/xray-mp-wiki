---
title: "Human MT1 Melatonin Receptor"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41586-019-1141-3]
verified: false
---

# Human MT1 Melatonin Receptor

## Overview

The MT1 melatonin receptor (type 1A) is a class A G-protein-coupled receptor that binds the neurohormone melatonin (N-acetyl-5-methoxytryptamine) and maintains circadian rhythms. The receptor is a target for insomnia drugs such as ramelteon and the antidepressant agomelatine. High-resolution room-temperature XFEL and synchrotron structures of MT1 in complex with four agonists (ramelteon, 2-PMT, 2-iodomelatonin, and agomelatine) reveal an unusually compact binding pocket sealed from extracellular solvent by extracellular loop 2, with a narrow lateral channel between transmembrane helices IV and V that connects the binding site to the lipid bilayer.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41586-019-1141-3 | 6ME2 | 2.80 | P 4 2_1 2 | MT1-CC (PGS fusion, N-term trunc 11 aa, C-term trunc 25 aa, 9 point mutations) | ramelteon |
| doi/10.1038##s41586-019-1141-3 | 6ME3 | 2.90 | P 4 2_1 2 | MT1-CC (PGS fusion, N-term trunc 11 aa, C-term trunc 25 aa, 9 point mutations) | 2-PMT (2-phenylmelatonin) |
| doi/10.1038##s41586-019-1141-3 | 6ME4 | 3.20 | P 4 2_1 2 | MT1-CC (PGS fusion, N-term trunc 11 aa, C-term trunc 25 aa, 9 point mutations) | 2-iodomelatonin |
| doi/10.1038##s41586-019-1141-3 | 6ME5 | 3.20 | P 4 2_1 2 | MT1-CC (PGS fusion, N-term trunc 11 aa, C-term trunc 25 aa, 9 point mutations) | agomelatine |

## Expression and Purification

- **Expression system**: Spodoptera frugiperda (Sf9) insect cells
- **Construct**: MT1-CC (human MT1 with N-terminal 11 aa [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/), C-terminal 25 aa [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/), ICL3 residues 219-227 replaced with PGS fusion; 9 thermostabilizing point mutations)
- **Notes**: Bac-to-bac baculovirus expression system; MOI 5; harvested 48h post-infection at 27C

### Purification Workflow

- **Expression system**: Sf9 insect cells
- **Expression construct**: MT1-CC (PGS fusion with His10-Flag-HA-PSP tags)
- **Tag info**: N-terminal HA signal, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), 10x His tag, [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) removable

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Dounce homogenization and ultracentrifugation | — | 10 mM HEPES pH 7.5, 1 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/) | Membrane fraction isolated from 3L biomass; repeated homogenization and ultracentrifugation |
| Solubilization | Detergent extraction | — | 50 mM HEPES pH 7.5, 150 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) / 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) |  |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA / [TALON](/xray-mp-wiki/reagents/additives/talon/) | — |  | Standard immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) |
| Size-exclusion chromatography | SEC | — |  | Final polishing step |


## Crystallization

### doi/10.1038##s41586-019-1141-3

| Parameter | Value |
|---|---|
| Method | LCP (lipid cubic phase) |
| Protein sample | ~30 mg/mL MT1-CC in 50 mM HEPES pH 7.5, 150 mM NaCl, 0.05%/0.01% [DDM](/xray-mp-wiki/reagents/detergents/ddm/)/CHS, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) |
| Protein-to-lipid ratio | 2:3 (w/w) |
| Temperature | 20C |
| Growth time | 2-4 weeks |
| Cryoprotection | 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |
| Notes | Crystals appeared in LCP with P4 2_1 2 space group; ramelteon complex crystals used for XFEL data collection, 2-PMT complex crystals optimized for synchrotron |


## Biological / Functional Insights

### Lateral Ligand Access Channel

MT1 has a sealed extracellular binding pocket with a narrow lateral channel between TM4 and TM5 that connects the binding site to the lipid bilayer. This channel provides an atypical entry pathway for lipophilic ligands directly from the membrane, explaining how neutral lipophilic ligands like melatonin access the binding site without traversing the extracellular space. The channel entrance lies approximately 6.5-10.9 Å below the membrane boundary.

### YPYP Motif in Helix II

A unique YPYP motif (Y79-P80-Y81-P82) in helix II creates a bulge that shapes the ligand binding pocket. This motif is specific to melatonin receptors and GPR50, and is not found in any other human GPCR. Mutation of any residue in this motif reduces thermostability by 6-10°C and impairs receptor function.

### Compact Binding Site Architecture

The MT1 binding site is extremely compact (710 Å³ with ramelteon), among the smallest in class A GPCRs. Ligands interact primarily through aromatic stacking with F179^ECL2 and hydrogen bonds with N162^4.60 and Q181^ECL2. The small binding pocket and lateral channel impose constraints on ligand size and physicochemical properties, with 98% of high-affinity ligands being neutral at physiological pH.


## Cross-References

- [Human 5-HT2A Receptor](/xray-mp-wiki/proteins/gpcr/5ht2a-receptor/) — Comparison of melatonin vs serotonin receptor binding site evolution; agomelatine binds both receptors
- [Human 5-HT2C Receptor](/xray-mp-wiki/proteins/gpcr/5ht2c-receptor/) — Agomelatine acts as antagonist at 5-HT2C; structural comparison of binding modes
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Additive used in purification or crystallization buffers
- [EDTA](/xray-mp-wiki/reagents/additives/edta/) — Additive used in purification or crystallization buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) — Additive used in purification or crystallization buffers
- [TALON](/xray-mp-wiki/reagents/additives/talon/) — Additive used in purification or crystallization buffers
- [Human MT2 Melatonin Receptor](/xray-mp-wiki/proteins/gpcr/human-mt2-melatonin-receptor/) — Sister subtype; companion paper (10.1038/s41586-019-1144-0) describes MT2 structures revealing subtype selectivity
