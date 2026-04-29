---
title: scFv16
created: 2026-04-28
updated: 2026-04-28
type: reagent
tags: [additive-antibody]
sources: [doi/10.1016##j.cell.2020.01.008]
category: reagents
---
layout: default

# scFv16

## Overview

scFv16 is a designed single-chain variable fragment antibody used to stabilize GPCR-G(i) complexes for cryo-EM structure determination. It binds at the interface between the G(alpha)i alpha N helix and the G(beta) beta-propeller, locking the complex in a conformation suitable for single-particle cryo-EM.

## Structure and Binding

- **Binding interface**: G(alpha)i alpha N helix + G(beta) beta-propeller
- **Binding mode**: Similar interface to other GPCR-Gi-scFv complexes (Koehl et al., 2018)
- **Effect**: Stabilizes the active GPCR-Gi complex for cryo-EM data collection

## Expression and Purification

- **Expression**: Hi5 insect cells (Trichoplusia ni) via Bac-to-Bac Baculovirus Expression System
- **Vector**: Modified pFastBac1 with GP67 secretion signal at N terminus, 10xHis tag at C terminus
- **Secretion**: Expressed in secreted form (collected from supernatant)
- **IMAC purification**: Ni-NTA resin; wash with 20 mM HEPES pH 7.5, 100 mM NaCl, 10 mM imidazole; elute with 250 mM imidazole
- **Tag cleavage**: C-terminal 10xHis tag removed by human rhinovirus 3C protease
- **Dialysis**: Into 20 mM HEPES pH 7.5, 100 mM NaCl
- **Re-loading**: Flowthrough collected after 3C cleavage + Ni-NTA re-loading to remove cleaved tag
- **SEC**: Hiload Superdex 75 10/300 column for gel filtration; monomeric fractions pooled
- **Concentration**: Flash frozen at 4°C for storage

## Use in GPCR Structural Biology

- **CB2-Gi complex**: Used in CB2-AM12033-Gi-scFv16 cryo-EM (2.9 Å, PDB: 6KPF)
- **CB1-Gi complex**: Used in CB1-AM841-Gi-scFv16 cryo-EM (3.0 Å, PDB: 6KPG)
- **General role**: Enables cryo-EM structure determination of GPCR-Gi heterotrimeric complexes by stabilizing the active conformation

## Cross-References

- [cb1-receptor](//xray-mp-wiki/proteins/cb1-receptor/) — scFv16 used for CB1-Gi cryo-EM structure
- [cb2-receptor](//xray-mp-wiki/proteins/cb2-receptor/) — scFv16 used for CB2-Gi cryo-EM structure
- [bril-fusion](//xray-mp-wiki/concepts/bril-fusion/) — Alternative stabilization strategy (BRIL fusion instead of scFv)
- [cryoem](//xray-mp-wiki/methods/structure-determination/cryoem/) — Cryo-EM technique where scFv16 is applied
- [sf9-cells](//xray-mp-wiki/methods/expression-systems/sf9-cells/) — Sf9 cells used for GPCR-Gi co-expression (scFv16 from Hi5)