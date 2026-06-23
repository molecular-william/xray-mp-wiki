---
title: "AtTPC1 - Arabidopsis thaliana Two-pore Channel 1"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein]
sources: [doi/10.1073##pnas.1616191114]
verified: false
---

# AtTPC1 - Arabidopsis thaliana Two-pore Channel 1

## Overview

AtTPC1 (Arabidopsis thaliana Two-pore Channel 1) is a plant vacuolar cation channel belonging to the two-pore channel (TPC) family. Each TPC subunit contains two homologous Shaker-like six-transmembrane (6-TM) domains and functions as a homodimer. AtTPC1 is permeable to various cations with a relative permeability sequence of Ca2+ > Na+ ≈ Li+ ≈ K+ > Rb+ > Cs+. It is selective for Ca2+ over Na+ (PCa/PNa ~5) but nonselective among monovalent cations. Structural studies guided the conversion of AtTPC1 to a Na+-selective channel by mimicking the selectivity filter of human TPC2, revealing key residues (Val/Asn pair in filter II) that define Na+ selectivity.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1616191114 | 5TUA |  |  | At2HsTPC2 mutant (AtTPC1 with S265A, M629V, G630N mutations in the selectivity filter to mimic HsTPC2) | Na+, Rb+, or Cs+ (soaked) |

## Expression and Purification

- **Expression system**: HEK293 cells
- **Construct**: Full-length AtTPC1 and mutants including AtTPC1ΔCai (D240A/D454A/E528A for Ca2+ current measurements), and At2HsTPC2 (S265A/M629V/G630N for structural studies)
- **Notes**: AtTPC1 mutants were overexpressed in HEK293 [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) for [Solid Supported Membrane Electrophysiology](/xray-mp-wiki/methods/quality-assessment/solid-supported-membrane-electrophysiology/); At2HsTPC2 was expressed and purified for X-ray crystallography

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| purification | Detailed in SI Materials and Methods | — |  | purification details for At2HsTPC2 used for crystallization |


## Crystallization

### doi/10.1073##pnas.1616191114

| Parameter | Value |
|---|---|
| Method | Not specified in main text |
| Protein sample | At2HsTPC2 |
| Notes | Crystals were soaked with Rb+ or Cs+ for SAD phasing experiments |


## Biological / Functional Insights

### Filter II Val/Asn pair defines Na+ selectivity in TPC channels

Systematic mutagenesis and [Solid Supported Membrane Electrophysiology](/xray-mp-wiki/methods/quality-assessment/solid-supported-membrane-electrophysiology/) identified that a Val/Asn pair
in filter II of TPC channels is essential for Na+ [Claudin Paracellular Ion Selectivity](/xray-mp-wiki/concepts/miscellaneous/claudin-paracellular-ion-selectivity/).
AtTPC1 residues Met629→Val and Gly630→Asn (the At2HsTPC2 mutant)
converted the nonselective [VIT1](/xray-mp-wiki/proteins/pumps-atpases/vit1/) channel to a Na+-selective channel with
PNa/PK of 41.1. The structure of At2HsTPC2 (PDB 5TUA) revealed
that Asn630 creates a constriction in the ion channel (~4.8 A) and
coordinates Na+ through its side chain carbonyl groups, while the Asn630/Asn631
pair creates steric hindrance for larger monovalent cations (Rb+, Cs+).

### Structural basis of TPC ion selectivity

Comparison of AtTPC1 and At2HsTPC2 filter structures shows that the
M629V mutation causes local rearrangements in the filter,
stabilizing a narrow conformation. The Asn630 side chain is
coordinated by [Proton Wire](/xray-mp-wiki/concepts/transport-mechanisms/proton-wire/) with backbone carbonyls of Thr264 and Ala265
from filter I. The resulting filter explains how mammalian TPCs
achieve Na+ Selectivity while [VIT1](/xray-mp-wiki/proteins/pumps-atpases/vit1/) TPC1 remains nonselective.


## Cross-References

- [Bovine F1-ATPase (azide-inhibited form)](/xray-mp-wiki/proteins/pumps-atpases/bovine-f1-atpase/) — Related protein structure; referenced in text
- [Human Angiotensin-Converting Enzyme 2 (hACE2)](/xray-mp-wiki/proteins/slc-transporters/hace2/) — Related protein structure; referenced in text
- [NTSR1-LF Mutant](/xray-mp-wiki/proteins/gpcr/ntsr1-lf/) — Related protein structure; referenced in text
- [Bovine Mitochondrial F1-ATPase-Stator Complex (Membrane Extrinsic Region)](/xray-mp-wiki/proteins/pumps-atpases/bovine-f1-atpase-stator-complex/) — Related protein structure; referenced in text
- [GluA2 AMPA Receptor — Structures with Antagonists, NAMs, and Allosteric Modulators](/xray-mp-wiki/proteins/other-ion-channels/glua2-ampa-receptor/) — Related protein structure; referenced in text
- [Plant Vacuolar Iron Transporter 1 (VIT1)](/xray-mp-wiki/proteins/pumps-atpases/vit1/) — Related protein structure; referenced in text
- [Claudin-Mediated Paracellular Ion Selectivity](/xray-mp-wiki/concepts/miscellaneous/claudin-paracellular-ion-selectivity/) — Related concept; referenced in text
- [Membrane Mimetics and Structural Biology](/xray-mp-wiki/concepts/membrane-mimetics/membrane-mimetics/) — Related concept; referenced in text
- [Proton Wire (Chain of Hydrogen Bonds)](/xray-mp-wiki/concepts/transport-mechanisms/proton-wire/) — Related concept; referenced in text
- [Oxygen Ladder in Selectivity Filters](/xray-mp-wiki/concepts/transport-mechanisms/oxygen-ladder-selectivity-filter/) — Related concept; referenced in text
