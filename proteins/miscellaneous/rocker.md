---
title: Rocker — De Novo Designed Zn²⁺ Transporter
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1261172]
verified: false
---

# Rocker — De Novo Designed Zn²⁺ Transporter

## Overview

Rocker is a de novo designed membrane-spanning four-helical bundle that
transports first-row transition metal ions Zn²⁺ and Co²⁺, but not Ca²⁺,
across membranes. The conduction path was designed to contain two di-metal
binding sites that bind with negative cooperativity. The overall helical
bundle is formed from two tightly interacting pairs of helices, which form
individual domains that interact weakly along a more dynamic interface.
Rocker functions as a Zn²⁺/H⁺ antiporter, using a Zn²⁺ gradient to drive
reverse proton transport. This work represents the first high-resolution
structure of a designed membrane protein, demonstrating the feasibility of
designing membrane proteins with predefined structural and dynamic properties.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.1261172 | Not deposited | 2.7-2.8 | Multiple non-isomorphous | Zn²⁺-free Rocker four-helix bundle | None (apo form) |

## Expression and Purification

- **Expression system**: Not specified
- **Construct**: De novo designed four-helix bundle with 4Glu-2His di-Zn²⁺-binding sites, ExxH motifs
- **Notes**: Designed computationally. Contains tight and loose helix-helix interfaces. Tight interface stabilized by Ala-rich packing. Loose interface packed by large Phe residues.

### Purification Workflow

- **Expression system**: Not specified
- **Expression construct**: Rocker four-helix bundle with designed metal-binding sites

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Solubilization | Detergent solubilization | — | [DPC](/xray-mp-wiki/reagents/detergents/dpc/) ([DPC](/xray-mp-wiki/reagents/detergents/dodecylphosphocholine/)) for AUC and solution NMR; [DMPC](/xray-mp-wiki/reagents/lipids/dmpc/) bilayers for SSNMR; [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) for LCP crystallization | Rocker was solubilized in micelles for solution studies and reconstituted in phospholipid bilayers for SSNMR. X-ray structures obtained from both micelle and [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) LCP conditions. |


## Crystallization

### doi/10.1126##science.1261172

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (from micelles) and lipidic cubic phase ([Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/)) |
| Protein sample | Zn²⁺-free Rocker |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) (for LCP crystallization) |
| Notes | Three non-isomorphous space groups obtained. Data extended between 2.7 and 2.8 Å. Structures solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/). Dimers composed of straight alpha helices interacting along the tight interface. |


## Biological / Functional Insights

### De novo design of functional membrane protein

Rocker is the first designed membrane protein whose structure has been
experimentally determined at high resolution. The design combines
traditional computational design with biophysically motivated
conformational ensemble-based reasoning. The design achieved
function without high-throughput screening or directed evolution.

### Designed tight and loose helix-helix interfaces

The dimer of dimers architecture has two non-equivalent interfaces:
a "tight interface" with small interhelical distance (8.9 Å)
stabilized by Ala-rich packing (alanine coil motif), and a "loose
interface" with larger interhelical distance (12.0 Å) packed by
large Phe residues. The loose interface is thermodynamically less
stable and geometrically more flexible, facilitating ion motion.

### Negative cooperativity between metal-binding sites

Solution NMR titration showed two Zn²⁺ ions bind per tetramer at
high affinity, followed by much weaker association at a second
binding site. This negative cooperativity between the two di-Zn²⁺
binding sites is consistent with the design strategy inspired by
the [Alternating Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) of natural transporters.

### Zn²⁺/H⁺ antiport activity

Rocker transports Zn²⁺ with Michaelis-Menten kinetics (KM = 280 ±
90 µM for Zn²⁺). A Zn²⁺ gradient drives uphill proton transport
with a stoichiometry of 3-4 H⁺ per Zn²⁺. Co²⁺ is also transported
(KM = 1400 ± 200 µM, Vmax = 470 ± 40 min⁻¹). Ca²⁺ is not
transported. Proton-Zn²⁺ coupling is linked through displacement
of protons upon Zn²⁺ binding to the Glu/His ligands.


## Cross-References

- [Dodecylphosphocholine (DPC)](/xray-mp-wiki/reagents/detergents/dodecylphosphocholine/) — Primary micelle-forming detergent for AUC and solution NMR characterization
- [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Buffer used in purification and sample preparation
- [Alternating Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — Related biological concept
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [DPC](/xray-mp-wiki/reagents/detergents/dpc/) — Detergent used in purification or crystallization
- [DMPC](/xray-mp-wiki/reagents/lipids/dmpc/) — Additive used in purification or crystallization buffers
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Additive used in purification or crystallization buffers
