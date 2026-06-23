---
title: Interleukin-17A (IL-17A)
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.immuni.2020.02.004]
verified: false
---

# Interleukin-17A (IL-17A)

## Overview

IL-17A is a secreted cytokine and the best-studied member of the IL-17 cytokine family. It forms homodimers and plays a key role in innate and adaptive immune responses as well as in a broad range of chronic inflammatory and autoimmune disorders. IL-17A signals through a heteromeric receptor complex comprising [IL-17RA](/xray-mp-wiki/proteins/receptors-signaling/il-17ra/) and [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/). Unlike [IL-17F](/xray-mp-wiki/proteins/receptors-signaling/il-17f/), IL-17A readily drives formation of the heteromeric [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/):[IL-17RA](/xray-mp-wiki/proteins/receptors-signaling/il-17ra/):IL-17A complex at nanomolar concentrations. IL-17A can also form heterodimers with [IL-17F](/xray-mp-wiki/proteins/receptors-signaling/il-17f/) (IL-17A/F), which has intermediate ability to assemble the heteromeric complex.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.immuni.2020.02.004 | 5L9F | not specified | not specified | Human IL-17A, residues 34-155 of UniProt entry Q16552, with two point mutations (N68D and C129S) reported by Liu et al., 2013; fused to CD33 signal peptide, APP6-tag, and PreScission recognition sequence (LEVLFQGP)
 | -- |
| doi/10.1016##j.immuni.2020.02.004 | not specified | not specified | not specified | IL-17A homodimer in complex with [IL-17RA](/xray-mp-wiki/proteins/receptors-signaling/il-17ra/) and [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) (heteromeric 1:1:1 complex analyzed by [SEC-MALS](/xray-mp-wiki/methods/quality-assessment/sec-mals/) and [TR-FRET](/xray-mp-wiki/methods/quality-assessment/tr-fret/))
 | [IL-17RA](/xray-mp-wiki/proteins/receptors-signaling/il-17ra/) and [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) |

## Expression and Purification

- **Expression system**: HEK293S cells (human embryonic kidney cells deficient in N-acetylglucosaminyl-transferase I)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | Transient co-expression in HEK293S cells | -- | V3 medium (Novartis medium, patent WO 2011/134920 A1) + -- | Co-expression of IL-17A and [IL-17F](/xray-mp-wiki/proteins/receptors-signaling/il-17f/) led to production of IL-17A, [IL-17F](/xray-mp-wiki/proteins/receptors-signaling/il-17f/), and IL-17A/F heterodimer; cells grown to 3 x 10^6 cells/mL
 |
| Purification | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) and SEC | -- | -- + -- | IL-17A purified from supernatant; used for [ITC](/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/) and [SEC-MALS](/xray-mp-wiki/methods/quality-assessment/sec-mals/) experiments
 |


## Crystallization

No crystallization described.

## Biological / Functional Insights

### IL-17A efficiently drives heteromeric complex formation

In the presence of both [IL-17RA](/xray-mp-wiki/proteins/receptors-signaling/il-17ra/) and [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/), IL-17A readily drives formation of the heteromeric [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/):[IL-17RA](/xray-mp-wiki/proteins/receptors-signaling/il-17ra/):IL-17A complex at approximately 12.5 nM concentration in [TR-FRET](/xray-mp-wiki/methods/quality-assessment/tr-fret/) assays. This is significantly more efficient than [IL-17F](/xray-mp-wiki/proteins/receptors-signaling/il-17f/), which requires approximately 250-fold higher concentrations to achieve a similar signal.

### IL-17A forms the expected 1:1:1 heteromeric complex

SEC-HPLC and [SEC-MALS](/xray-mp-wiki/methods/quality-assessment/sec-mals/) analysis showed that IL-17A forms the expected 1:1:1 heteromeric complex with [IL-17RA](/xray-mp-wiki/proteins/receptors-signaling/il-17ra/) and [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/). A clear shift of the SEC peak to higher apparent molecular weight was observed upon addition of [IL-17RA](/xray-mp-wiki/proteins/receptors-signaling/il-17ra/). The MW deduced by MALS analysis was 165 kDa, above the calculated value of 130 kDa, suggesting possible higher-order oligomeric species.

### IL-17A contributes to angiogenesis and inflammation

IL-17A-induced angiogenesis through the [Phosphatidylinositol](/xray-mp-wiki/reagents/lipids/phosphatidylinositol/) 3-kinase (PI3K)-AKT pathway appears to be primarily mediated by [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/). In human synoviocytes, blockade of either [IL-17RA](/xray-mp-wiki/proteins/receptors-signaling/il-17ra/) or [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) alone was sufficient to downregulate IL-17A-induced IL-6 and CCL-20 secretion.


## Cross-References

- [Interleukin-17 Receptor C (IL-17RC)](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) — Co-receptor that forms heteromeric complex with IL-17A
- [Interleukin-17 Receptor A (IL-17RA)](/xray-mp-wiki/proteins/receptors-signaling/il-17ra/) — Shared co-receptor that forms heteromeric complex with IL-17A
- [Interleukin-17F (IL-17F)](/xray-mp-wiki/proteins/receptors-signaling/il-17f/) — Related cytokine; can form heterodimer with IL-17A
- [Competitive Receptor Binding](/xray-mp-wiki/concepts/competitive-receptor-binding/) — IL-17A efficiently assembles heteromeric complex unlike IL-17F
- [SEC-MALS](/xray-mp-wiki/methods/quality-assessment/size-exclusion-chromatography-mals/) — Used to analyze IL-17A receptor complex stoichiometry
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [ITC](/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/) — Method used in structure determination or purification
- [SEC-MALS](/xray-mp-wiki/methods/quality-assessment/sec-mals/) — Method used in structure determination or purification
- [TR-FRET](/xray-mp-wiki/methods/quality-assessment/tr-fret/) — Method used in structure determination or purification
- [Phosphatidylinositol](/xray-mp-wiki/reagents/lipids/phosphatidylinositol/) — Additive used in purification or crystallization buffers
