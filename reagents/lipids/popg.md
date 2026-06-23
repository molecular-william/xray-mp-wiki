---
title: 1-Palmitoyl-2-Oleoylphosphatidylglycerol (POPG)
created: 2026-06-03
updated: 2026-06-16
type: reagent
category: reagents
layout: default
tags: [lipid-diacyl, subdirectory-lipids]
sources: [doi/10.1016##j.jmb.2020.06.012, doi/10.1038##nature12484, doi/10.1038##nsmb.1531, doi/10.1038##417515a, doi/10.1016##j.bbamem.2021.183825, doi/10.1038##s41594-020-0464-y]
verified: false
---

# 1-Palmitoyl-2-Oleoylphosphatidylglycerol (POPG)

## Overview

1-Palmitoyl-2-oleoylphosphatidylglycerol (POPG) is a diacyl phospholipid with a palmitoyl (16:0) chain at the sn-1 position and an oleoyl (18:1) chain at the sn-2 position. POPG carries a net negative charge and is one of the most abundant anionic phospholipids in bacterial membranes. It is commonly used in structural biology to mimic the anionic lipid composition of bacterial membranes in molecular dynamics simulations. A POPG molecule was identified as an embedded lipid in the substrate-binding cavity of the LmrP multidrug transporter (PDB 6T1Z), where it is proposed to contribute to polyspecificity through conformational plasticity.


## Properties


## Use in Membrane Protein Work

### Molecular dynamics simulation of membrane protein in bacterial membrane mimic




## Examples from This Wiki

| Protein | Concentration | Context | Result |
|---|---|---|---|
| [Na+/H+ Antiporter NapA from Thermus thermophilus](/xray-mp-wiki/proteins/slc-transporters/nap-a/) | 25% (in 4:1 [POPE](/xray-mp-wiki/reagents/lipids/pope/):POPG mixture) | [Molecular Dynamics Simulation](/xray-mp-wiki/methods/structure-determination/molecular-dynamics-simulation/) of NapA dimer in mixed [POPE](/xray-mp-wiki/reagents/lipids/pope/)/POPG bilayer approximating E. coli membrane composition | NapA dimer stable in the mixed lipid bilayer; sodium ions spontaneously bound to Asp 157 at the bottom of the outward-facing cavity |
| /xray-mp-wiki/proteins/voltage-gated-channels/nak-channel/ | 2.5 mg/mL (in 3:1 [POPE](/xray-mp-wiki/reagents/lipids/pope/):POPG mixture) | Anionic lipid component for NaK channel reconstitution into liposomes for 86Rb flux assays | POPG (2.5 mg/mL) combined with [POPE](/xray-mp-wiki/reagents/lipids/pope/) (7.5 mg/mL) at protein/lipid ratio of 5-10 ug/mg; used with 10 mM DM for solubilization and dialysis-based detergent removal |
| /xray-mp-wiki/proteins/voltage-gated-channels/kcsa/ | 25% (in 3:1 [POPC](/xray-mp-wiki/reagents/lipids/popc/):POPG mixture) | Component of mixed lipid bilayer for [Molecular Dynamics Simulation](/xray-mp-wiki/methods/structure-determination/molecular-dynamics-simulation/) of open-gate [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) potassium channel with Ba2+ bound at site S4 | [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) with Ba2+ at S4 stable over 500-ns MD trajectory; RMSD of selectivity filter ~0.6 A |
| /xray-mp-wiki/proteins/mfs-transporters/lmrp/ | Embedded lipid in binding cavity | Crystal structure of LmrP (PDB 6T1Z) revealed POPG embedded in substrate-binding pocket adjacent to Hoechst 33342 | POPG stabilizes outward-open conformation through Arg14-Asp142 salt bridge; proposed to contribute to polyspecificity |

## Advantages and Disadvantages

No advantages/disadvantages recorded.

## Comparison with Related Reagents

No comparison data available.

## Cross-References

- [Molecular Dynamics Simulation](/xray-mp-wiki/methods/structure-determination/molecular-dynamics-simulation/) — Method used in structure determination or purification
- [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) — Related protein structure
- [Na+/H+ Antiporter NapA from Thermus thermophilus](/xray-mp-wiki/proteins/slc-transporters/nap-a/) — Related protein structure
- [Phosphatidylglycerol](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol/) — Additive used in purification or crystallization buffers
- [POPC](/xray-mp-wiki/reagents/lipids/popc/) — Additive used in purification or crystallization buffers
- [POPE](/xray-mp-wiki/reagents/lipids/pope/) — Additive used in purification or crystallization buffers
- [LmrP Multidrug Transporter](/xray-mp-wiki/proteins/mfs-transporters/lmrp/) — POPG embedded in the LmrP binding cavity (PDB 6T1Z)
