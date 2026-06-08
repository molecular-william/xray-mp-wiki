---
title: Murine Mu-Opioid Receptor
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature14886]
verified: false
---

# Murine Mu-Opioid Receptor

## Overview

The murine mu-opioid receptor (muOR, MOP) is a class A G-protein-coupled receptor that mediates the analgesic and addictive properties of opiate alkaloids. This page covers the active-state crystal structure of muOR solved at 2.1 A resolution in complex with the morphinan agonist BU72 and the G-protein mimetic nanobody Nb39. The structure reveals conformational changes associated with receptor activation, including a 10 A outward displacement of transmembrane helix 6 and rearrangement of the conserved core triad (F6.44, P5.50, I3.40).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature14886 | TBD | 2.1 | I212121 | Full-length murine muOR with N-term Flag tag, C-term 6xHis tag, TEV site after residue 51, 3C site before residue 359 | BU72, Nb39 |

 - R-work 18.53%, R-free 22.15%; Atoms: 3278 protein atoms, 32 ligand (BU72) atoms, 208 lipid/water/other atoms; Data collection: Merged from four crystals at 2.1 A resolution

## Expression and Purification

- **Expression system**: Sf9 insect cells (baculovirus expression system, BestBac)
- **Construct**: Full-length murine muOR with N-terminal Flag epitope tag, C-terminal 6xHis tag, TEV protease site after residue 51, rhinovirus 3C protease site before residue 359

### Purification Workflow

- **Expression system**: Sf9 insect cells (baculovirus)
- **Expression construct**: Full-length murine muOR with N-term Flag, C-term 6xHis, TEV and 3C protease sites

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and infection | Baculovirus infection | — | Sf9 cells infected at 3 x 10^6 cells/mL | Infected with baculovirus encoding muOR at 27 deg.C for 48-60 h |
| Membrane solubilization | Detergent solubilization | — | 25 mM HEPES pH 7.4, 100 mM NaCl + 0.01% MNG, 0.001% CHS | Receptor solubilized and purified in final buffer |


## Crystallization

### doi/10.1038##nature14886

| Parameter | Value |
|---|---|
| Method | Lipidic mesophase (LCP) |
| Protein sample | muOR-BU72-Nb39 complex |
| Lipid | Monoolein |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Data collected by merging diffraction from four crystals |
| Notes | Complete data set to 2.1 A obtained by merging from four crystals. Nb39 mediates majority of packing interactions between lipidic layers. Parallel dimeric packing via TM1-TM2-ECL1-H8 with 460 A^2 buried surface area. |


## Biological / Functional Insights

### Active-State Conformational Changes

Upon activation, muOR undergoes a 10 A outward displacement of TM6 and smaller inward movements of TM5 and TM7. The extracellular domain shows minimal changes except at the proximal N terminus. The conserved E/DRY motif rearranges: in the inactive state, R165^3.50 forms a hydrogen bond with T279^6.34; in the active state, R3.50 forms a hydrogen bond with Y5.58^5.58, stabilizing inward movement of TM5. A parallel dimer interface involving TM1, TM2, ECL1, and H8 is observed in both inactive and active states with 460 A^2 buried surface area.

### Ligand-Binding Pocket and Polar Interactions

BU72 binds in the orthosteric pocket with its morphinan core interacting with hydrophobic residues I296^6.51, V300^6.55 in TM6 and W318^7.35, I322^7.39 in TM7. The phenolic hydroxyl engages in a water-mediated interaction with H297^6.52. The tertiary amine forms an ionic interaction with D147^3.32. An unexpected interaction between BU72 and the amino terminus (H54) was observed, with H54 positioned 2.6 A from the BU72 secondary amine, though this is unlikely physiologically relevant.

### Conserved Core Triad Rearrangement

A triad of conserved amino acids F6.44, P5.50, and I3.40 (the conserved core triad) undergoes rearrangement upon activation. In the active state, the morphinan scaffold of BU72 adopts a pose sterically incompatible with the inactive position of TM3, causing TM3 residues D147^3.32 and M151^3.36 to shift 1.5 A toward TM2. W293^6.48 serves as a link between the ligand-binding pocket and the triad, with its rotameric state stabilized by agonist binding.

### Polar Network in Signal Propagation

An extensive polar network connects the orthosteric binding pocket to the G-protein-coupling interface. In the active state, the sodium-binding site (coordinated by D2.50, N3.35, S3.39, and W6.48) collapses and rearranges to preclude sodium binding. The NPxxY motif in TM7 moves inward toward TM5, with N332^7.49 and Y336^7.53 participating in a hydrogen-bond network involving Y252^5.58 and backbone carbonyls of L158^3.43 and V285^6.40.


## Cross-References

- [BU72](/xray-mp-wiki/reagents/ligands/bu72/) — Co-crystallized agonist ligand in active muOR structure
- [BU74](/xray-mp-wiki/reagents/ligands/bu74/) — Antagonist counterpart used in MD simulations to demonstrate instability in active state
- [beta-FNA](/xray-mp-wiki/reagents/ligands/beta-fna/) — Covalent antagonist co-crystallized with inactive muOR structure
- [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) — Nb39 nanobody used as G-protein mimetic for active-state stabilization
- [Human Beta2-Adrenergic Receptor](/xray-mp-wiki/proteins/beta2-adrenergic-receptor/) — Comparative analysis of activation mechanism
- [Human Delta-Opioid Receptor](/xray-mp-wiki/proteins/delta-opioid-receptor/) — High-resolution inactive structure used for polar network comparison
- [Kappa Opioid Receptor](/xray-mp-wiki/proteins/kappa-opioid-receptor/) — Related classical opioid GPCR
- [Conserved Core Triad](/xray-mp-wiki/concepts/conserved-core-triad/) — Key mechanistic concept from muOR activation studies
