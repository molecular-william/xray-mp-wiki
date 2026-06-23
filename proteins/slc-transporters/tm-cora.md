---
title: "Thermotoga maritima CorA (TmCorA) Magnesium Channel"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein]
sources: [doi/10.1073##pnas.1209018109]
verified: false
---

# Thermotoga maritima CorA (TmCorA) Magnesium Channel

## Overview

CorA from Thermotoga maritima (TmCorA) is a homopentameric magnesium ion channel belonging to the CorA-Mrs2-Alr1 superfamily of Mg2+ transport proteins. It is the primary Mg2+ uptake system in Bacteria and Archaea. The structures reported here include a TmCorA-ΔNcc mutant in both Mg2+-bound (locked, symmetric) and Mg2+-free (unlocked, asymmetric) conformations. A hydrated Mg2+ ion binds to the periplasmic Gly-Met-Asn (GMN) motif, revealing clues to ion selectivity.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1209018109 | 4EEB | not specified | — | TmCorA-ΔNcc mutant (N-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/)) in presence of Mg2+ | Mg2+ |
| doi/10.1073##pnas.1209018109 | 4EEB | not specified | — | TmCorA-ΔNcc mutant in absence of Mg2+ | Cs+ |

## Expression and Purification

- **Expression system**: Expressed in Escherichia coli strain BW25113


### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | E. coli transformation | — |  | Expression plasmids for WT and mutant TmCorA transformed into BW25113 |
| Purification | Not detailed in main text | — |  | Referenced to SI Methods |


## Crystallization

### doi/10.1073##pnas.1209018109

| Parameter | Value |
|---|---|
| Method | X-ray crystallography |
| Notes | Data collected at Canadian Macromolecular Crystallography Facility and Canadian Light Source; structures determined in presence and absence of divalent ions |


## Biological / Functional Insights

### Sequential allosteric regulation of Mg2+ transport

At high intracellular Mg2+ concentrations, divalent ions bind to regulatory sites (M1 and M2) at the protomer-protomer interface of the cytosolic domain, locking TmCorA in a symmetric, transport-incompetent state. Loss of intracellular Mg2+ causes asymmetric rigid-body motions (lateral tilt, radial tilt, z rotation of protomers) that lead to bending of the central pore-lining α7 helix (bell-bending motion). This asymmetric state is potentially influx-competent. Molecular dynamics simulations confirm that without Mg2+, the pore becomes hydrated and the pentamer transitions from symmetric to asymmetric.

### GMN motif as selectivity filter

The universally conserved Gly-Met-Asn (GMN) motif at the periplasmic mouth of the CorA pore is only accessible in the asymmetric state. A hydrated Mg2+ ion was observed bound to the GMN motif, suggesting that Mg2+ ions with their first hydration shell intact are selected over other ions by CorA. This contrasts with K+ channels, where dehydrated ions are coordinated by carbonyl oxygens.

### Protease susceptibility confirms Mg2+-dependent conformational states

[Trypsin](/xray-mp-wiki/reagents/additives/trypsin/) digestion assays show that at Mg2+ concentrations >0.5 mM, the channel is protease-resistant (locked state). Below 0.5 mM Mg2+, the α5-α6 loop becomes exposed and cleaved at R202/K205. The D253K mutant, which replaces a regulatory Mg2+ site with a permanent salt bridge, abolishes Mg2+-dependent protection.


## Cross-References

- [Sequential Allosteric Regulation](/xray-mp-wiki/concepts/structural-mechanisms/sequential-allosteric-regulation/) — TmCorA exemplifies sequential allosteric regulation through asymmetric protomer motions
- [CorA-Mrs2-Alr1 Superfamily](/xray-mp-wiki/concepts/transport-mechanisms/cora-mrs2-alr1-superfamily/) — TmCorA is the founding member of this Mg2+ channel superfamily
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) — Related biological concept
- [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/) — Additive used in purification or crystallization buffers
