---
title: Palmitoyl-Oleoyl-Phosphatidylethanolamine (POPE)
created: 2026-06-02
updated: 2026-06-03
type: reagent
category: reagents
layout: default
tags: [lipid-diacyl, subdirectory-lipids]
sources: [doi/10.1038##nature08156, doi/10.1038##nature12484, doi/10.1038##ncomms11673]
verified: false
---

# Palmitoyl-Oleoyl-Phosphatidylethanolamine (POPE)

## Overview

Palmitoyl-oleoyl-phosphatidylethanolamine (POPE) is a diacyl phospholipid with a palmitoyl (16:0) chain at the sn-1 position and an oleoyl (18:1) chain at the sn-2 position. POPE is one of the most abundant phospholipids in bacterial cell membranes and is commonly used in structural biology to mimic biological lipid bilayers. It was used in molecular dynamics simulations to model membrane protein insertion into a phospholipid bilayer.


## Properties

- **Chemical name**: 1-palmitoyl-2-oleoyl-sn-glycero-3-phosphoethanolamine
- **Chemical formula**: C41H78NO8P
- **Molecular weight**: 716.05 g/mol
- **Class**: phosphatidylethanolamine

## Use in Membrane Protein Work

### Molecular dynamics simulation of SNARE complex in lipid bilayer

POPE lipids were chosen to mimic a simple membrane with a thickness of approximately 4.5-5.0 nm in short molecular dynamics simulations of the synaptic SNARE complex. Because PE head groups are highly abundant in animal membranes and PO is a relatively short tail group, POPE was used to model the position of the SNARE complex in a palmitoyl-oleoyl-phosphatidylethanolamine bilayer. The hydrophobic parts of the transmembrane regions of syntaxin-1A and synaptobrevin-2 were centered within the hydrophobic part of the bilayer.


### Molecular dynamics simulation of LeuT dimer in lipid bilayer

POPE lipids used to model the membrane bilayer for molecular dynamics simulations of the LeuT crystal dimer. The dimer was inserted into a POPE bilayer with at least 20 A of lipids surrounding it. The system was solvated with TIPS3P water and 0.2 M NaCl. Simulations used CHARMM36 force field for protein and lipids, with a 2 fs time step at 310 K. Total system contained ~130,000 atoms.


## Examples from This Wiki

| Protein | Concentration | Context | Result |
|---|---|---|---|
| SNARE complex (syntaxin-1A, SNAP-25A, synaptobrevin-2) | N/A | Molecular dynamics simulation of SNARE complex in POPE bilayer | Estimated position of four-helix bundle in phospholipid bilayer; hydrophilic head groups shown as balls, aliphatic chains as sticks |
| Na+/H+ Antiporter NapA from Thermus thermophilus | N/A (75% in 4:1 POPE:POPG mixture) | Molecular dynamics simulation of NapA dimer in mixed POPE/POPG bilayer approximating E. coli membrane composition | NapA dimer stable in the mixed lipid bilayer; sodium ions spontaneously bound to Asp 157 |
| LeuT Amino Acid Transporter from Aquifex aeolicus | N/A (pure POPE bilayer) | Molecular dynamics simulation of LeuT crystal dimer in pure POPE bilayer; dimer inserted with 20 A padding, solvated with TIPS3P water and 0.2 M NaCl; ~130,000 atoms total; CHARMM36 force field; 310 K; 2 fs time step; total simulation 1.2 microseconds | Simulations revealed Leu25 remains stably positioned in S1 substrate-binding site in Na+-free return state, preventing Na+ access to Na1 and Na2 sites |

## Advantages and Disadvantages

No advantages/disadvantages recorded.

## Comparison with Related Reagents

No comparison data available.

## Cross-References

- [Membrane Mimetics and Structural Biology](/xray-mp-wiki/concepts/membrane-mimetics/) — POPE used as membrane bilayer component in MD simulations
- [Syntaxin-1A](/xray-mp-wiki/proteins/syntaxin-1a/) — POPE bilayer used to model syntaxin-1A transmembrane region insertion
- [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/leut/) — POPE bilayer used for LeuT dimer MD simulations revealing return state mechanism
