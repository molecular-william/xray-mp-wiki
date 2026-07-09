---
title: PreScission Protease
created: 2026-05-27
updated: 2026-06-22
type: reagent
category: reagents
layout: default
tags: [additive-ligand, subdirectory-additives]
sources: [doi/10.1016##j.immuni.2020.02.004, doi/10.1073##pnas.92.7.2658]
verified: false
---

# PreScission Protease

## Overview

PreScission protease is a genetically engineered fusion of Human Rhinovirus 3C protease (HRV 3C) and GST. It recognizes the sequence LEVLFQ-G-P and cleaves between Q and G residues. The GST tag enables easy removal from the digestion mixture by glutathione affinity chromatography after cleavage. It is active at 4°C (unlike the wild-type HRV 3C) and is commonly used for tag removal in membrane protein purification workflows. The enzyme is compatible with typical buffer conditions (50 mM Tris-HCl, 150 mM NaCl, 1 mM DTT, pH 7.0-8.0).


## Properties

- **Class**: site-specific protease

## Use in Membrane Protein Work

### Affinity tag removal

PreScission protease is used to cleave fusion tags from recombinant proteins after affinity purification. The LEVLFQGP recognition sequence is engineered between the tag and the target protein. After cleavage, the tag and protease (if also tagged) can be removed by passing the sample through affinity resin.


### Construct optimization

PreScission protease provides an alternative to TEV protease for tag cleavage, useful when the target protein contains TEV cleavage sites or when a different recognition sequence is preferred.


## Examples from This Wiki

| Protein | Concentration | Context | Result |
|---|---|---|---|
| Interleukin-17A ([IL-17A](/xray-mp-wiki/proteins/receptors-signaling/il-17a/)) | not specified | [IL-17A](/xray-mp-wiki/proteins/receptors-signaling/il-17a/) construct (residues 34-155) with N68D and C129S mutations expressed with CD33 signal peptide, APP6-tag, and PreScission recognition sequence (LEVLFQGP); tag cleavage to produce mature cytokine for biophysical studies
 | PreScission protease cleavage produced mature [IL-17A](/xray-mp-wiki/proteins/receptors-signaling/il-17a/) for [ITC](/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/) and [SEC-MALS](/xray-mp-wiki/methods/quality-assessment/sec-mals/) experiments
 |

## Advantages and Disadvantages

No advantages/disadvantages recorded.

## Comparison with Related Reagents

No comparison data available.

## Cross-References

- [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease/) — Alternative site-specific protease for tag cleavage
- [bRIL Fusion Protein](/xray-mp-wiki/reagents/protein-tags/bril/) — Fusion tag strategy that may require protease cleavage
- [Interleukin-17A (IL-17A)](/xray-mp-wiki/proteins/receptors-signaling/il-17a/) — IL-17A construct uses PreScission protease for tag removal
- [ITC](/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/) — Method used in structure determination or purification
- [SEC-MALS](/xray-mp-wiki/methods/quality-assessment/sec-mals/) — Method used in structure determination or purification
