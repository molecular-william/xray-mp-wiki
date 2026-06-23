---
title: "Mitochondrial Calcium Uniporter (MCU)"
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41586-018-0330-9]
verified: false
---

# Mitochondrial Calcium Uniporter (MCU)

## Overview

The mitochondrial calcium uniporter (MCU) is the pore-forming subunit of the mitochondrial Ca2+ channel that mediates rapid Ca2+ uptake into the mitochondrial matrix, critical for ATP production, intracellular Ca2+ signaling, and cell death. Crystal structures of MCU from the fungi Metarhizium acridum (MaMCU) and cryo-EM structures from Fusarium graminearum (FgMCU) reveal a tetrameric dimer-of-dimers architecture with a truncated pyramid shape, fundamentally different from the previously reported pentameric NMR structure of C. elegans MCU. Each protomer contains two transmembrane helices (TM1 and TM2), with TM2 lining the central ion conduction pore. The selectivity filter is formed by a conserved DXXE motif (Asp333-Glu336 in MaMCU) at the first helical turn of TM2, with Glu336 carboxylate groups coordinating Ca2+ at the pore centre. The structures reveal a new ion channel architecture and provide a structural framework for understanding mitochondrial calcium uniporter function, selectivity, and regulation.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41586-018-0330-9 | 5ID3 | 3.50 | P2_1_2_1_2 | MaMCU-Rub (Metarhizium acridum MCU residues 62-484 with rubredoxin fusion, truncations 62-98, 190-205, 427-484, mutations H327W, M330F) | Ca2+ |
| doi/10.1038##s41586-018-0330-9 | 5ID5 | 3.70 | C222_1 | MaMCU with nanobody | Ca2+ |
| doi/10.1038##s41586-018-0330-9 | 5IDG | 3.10 | C2 | MaMCU soluble domain (NTD only, residues 62-294 with TM domain deleted) | none |

## Expression and Purification

- **Expression system**: Escherichia coli BL21 (DE3)
- **Construct**: MaMCU (Metarhizium acridum MCU, residues 62-484, lacking mitochondrial signal peptide 1-61); engineered construct MaMCU-Rub added Clostridium pasteurianum rubredoxin fusion in NTD loop (S213-G214) plus point mutations H327W and M330F for improved crystallization
- **Notes**: Purified with N-terminal His6-GFPuv tag, cleaved by 3C protease; FgMCU construct also expressed in E. coli with similar vector

### Purification Workflow

- **Expression system**: E. coli BL21 (DE3)
- **Expression construct**: MaMCU (His6-GFPuv-3C-MaMCU)
- **Tag info**: N-terminal His6-GFPuv tag, cleaved by 3C protease

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Sonication | — | 50 mM Tris pH 8.0, 150 mM NaCl, 2 mM CaCl2, protease inhibitor cocktail |  |
| Membrane extraction | Detergent extraction | — | 2% DDM | 2 h at 4C |
| Affinity chromatography | Cobalt resin (TALON) | — |  | Batch binding 2 h at 4C; washed with 10-20 mM imidazole |
| Tag cleavage | 3C protease overnight | — |  | On-column cleavage |
| Size-exclusion chromatography | SEC (Superdex 200 Increase) | — | 20 mM Tris pH 8.0, 150 mM NaCl, 2 mM CaCl2, 0.03% DDM | Peak fractions concentrated to 10-15 mg/mL |


## Crystallization

### doi/10.1038##s41586-018-0330-9

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | 10-15 mg/mL MaMCU-Rub in 20 mM Tris pH 8.0, 150 mM NaCl, 2 mM CaCl2, 0.03% DDM |
| Reservoir | 100 mM Tris pH 8.0, 200 mM Li2SO4, 35% PEG 4000 |
| Temperature | 20C |
| Notes | Crystals diffracted to 3.5 A; P2_1_2_1_2 space group; also crystallized MaMCU-nanobody complex (C222_1 space group) and MaMCU soluble domain (C2 space group) |


## Biological / Functional Insights

### Dimer-of-Dimers Architecture

MCU forms a tetrameric channel with a dimer-of-dimers assembly, where two pairs of protomers assemble around a central ion conduction pore. This architecture was consistently observed by X-ray crystallography and cryo-EM across species (M. acridum and F. graminearum) and in multiple chemical environments (detergent, amphipol, nanodisc). The N-terminal domain (NTD) also forms a dimer-of-dimers arrangement, with a conserved interface matching human MCU NTD crystal forms.

### DXXE Selectivity Filter

The selectivity filter of MCU is formed by the conserved DXXE motif (Asp333-X-X-Glu336 in MaMCU) at the first helical turn of TM2. Glu336 carboxylate groups from all four subunits point to the pore centre and coordinate a bound Ca2+ ion. This high-affinity Ca2+ binding site is essential for the remarkable Ca2+ selectivity of MCU (which operates at sub-micromolar Ca2+ concentrations). The mechanism parallels Ca2+ channels like Orai and CavAb, using carboxylate rings for Ca2+ coordination.

### Truncated Pyramid Pore Architecture

Unlike conventional ion channels, MCU has a truncated pyramid shape with the wider base at the mitochondrial matrix side and the narrower apex at the intermembrane space. TM2 helices line the central pore with near four-fold symmetry. The pore is mostly hydrophilic and wider than typical channels, contributing to the relatively high conductance of MCU. The Asp333 residue at the intermembrane-space entrance likely recruits Ca2+ and is the site of ruthenium red inhibition.

### Conserved Architecture from Fungi to Humans

Although the N-terminal domain shows sequence conservation only among metazoans, the NTD fold is conserved between MaMCU and human MCU (r.m.s.d. 1.6 A despite no sequence similarity). The dimer interface of NTDs in MaMCU matches a crystal form of human MCU NTD, supporting a conserved tetrameric architecture from fungi to humans.


## Cross-References

- [Dimer-of-Dimers Architecture](/xray-mp-wiki/concepts/dimer-of-dimers/) — MCU represents a paradigm for this quaternary assembly in ion channels
- [Intramembrane Ion Coordination](/xray-mp-wiki/concepts/membrane-mimetics/intramembrane-ion-coordination/) — Glu336 ring provides a carboxylate-based Ca2+ selectivity mechanism shared with Orai and CavAb channels
