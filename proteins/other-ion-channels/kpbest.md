---
title: "KpBest Bestrophin Ion Channel"
created: 2026-06-10
updated: 2026-06-10
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein]
sources: [doi/10.1126##science.1259723]
verified: false
---

# KpBest Bestrophin Ion Channel

## Overview

KpBest is a bestrophin ion channel from *Klebsiella pneumoniae* whose crystal structure was determined at 2.3 Å resolution by single-wavelength anomalous diffraction (SAD). KpBest forms a stable pentamer with four transmembrane helices per protomer and a long intracellular domain comprising five helices. The channel conducts monovalent cations (Na⁺ > K⁺ ≈ Cs⁺) and is not activated by Ca²⁺, in contrast to eukaryotic bestrophins which are Ca²⁺-activated Cl⁻ channels. The ion permeation pathway features two distinct restrictions: a hydrophobic five-helix transmembrane pore with three rings of residues (I62, I66, F70) and a second restriction at I180 that acts as an activation gate.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.1259723 | 4WD7 | 2.3 | — | KpBest with 11-residue C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) (residues 22-289) | Zn²⁺ |

## Expression and Purification

- **Expression system**: E. coli
- **Construct**: KpBest with C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/)

### Purification Workflow

- **Expression system**: E. coli
- **Expression construct**: KpBest with 11-residue C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/)

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Purification | Not specified in detail | — |  | Purified KpBest was reconstituted into planar lipid bilayers for functional studies |


## Crystallization

### doi/10.1126##science.1259723

| Parameter | Value |
|---|---|
| Method | [Sitting-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) |
| Protein sample | Purified KpBest |
| Notes | Crystals grown from zinc acetate solution; 2.9 Å initial resolution improved to 2.3 Å after C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/); five-fold noncrystallographic symmetry aided refinement |


## Biological / Functional Insights

### Pentameric architecture and novel fold

KpBest is the first bestrophin structure solved, revealing a pentameric assembly with four transmembrane helices per protomer and a large cytoplasmic domain. The transmembrane and cytoplasmic helical bundles represent novel folds with no close structural homologs in the PDB.

### Cation selectivity determined by a single residue

KpBest conducts Na⁺ while eukaryotic bestrophins conduct Cl⁻. A single residue difference at position 66 (I66 in KpBest vs. F80 in hBest1) determines the charge selectivity. Mutating KpBest I66F switches selectivity to Cl⁻, while hBest1 F80I reduces Cl⁻ permeability, demonstrating that a hydrophobic pore residue controls ion selectivity in bestrophin channels.

### Two distinct permeation restrictions

The ion permeation pathway has a flower-vase shape with two restrictions. The first restriction at the transmembrane pore (I62, I66, F70; radius < 2.0 Å) controls ion selectivity. The second restriction at I180 (radius 1.2 Å) at the base of the cytoplasmic cavity acts as an activation gate — I180A markedly enhances open probability without affecting selectivity.

### Relevance to human disease

Mutations at residues equivalent to KpBest I66 (hBest1 F80) and I180 (hBest1 I205) cause [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) disorders in humans. hBest1 I205T is a known disease-causing mutation with significantly decreased Cl⁻ conductance.


## Cross-References

- [Chicken BEST1 Bestrophin-1 Ca2+-activated Cl- channel](/xray-mp-wiki/proteins/other-ion-channels/chicken-bestrophin-1/) — Chicken BEST1 is a eukaryotic bestrophin homolog with opposite ion selectivity to KpBest
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) — Related biological concept
- [Sitting-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) — Method used in structure determination or purification
- [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) — Related ligand or cofactor
