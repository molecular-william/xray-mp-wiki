---
title: Benzamidine
created: 2026-06-08
updated: 2026-06-08
type: reagent
category: reagents
layout: default
tags: [ligand, subdirectory-ligands]
sources: [doi/10.1038##NATURE13293, doi/10.1038##nchembio.2547]
verified: false
---

# Benzamidine

## Overview

Benzamidine is a carboximidamide compound with diverse pharmacological properties. Classically, it is known as a highly potent serine-protease inhibitor, with derivatives in clinical trials for blood clotting prevention. In membrane protein structural biology, benzamidine has been used as an agonist for the GABA_A R-β3 homopentamer and as a crystallization additive. Additionally, the benzamidine moiety serves as a sodium ion-mimicking pharmacophore in GPCR ligands, where it occupies the conserved sodium ion-binding site and stabilizes the inactive receptor conformation.


## Properties

- **Chemical name**: benzamidine
- **Chemical formula**: C7H8N2
- **Molecular weight**: 120.15 g/mol
- **Class**: carboximidamide

## Use in Membrane Protein Work

### GABA_A receptor agonist

Benzamidine acts as an agonist of the human GABA_A receptor beta-3 homopentamer, inducing desensitization at micromolar concentrations. EC50 = 61 +/- 12 uM in whole-cell patch-clamp recordings from HEK293S-GnTI- cells. EC50 = 370 +/- 180 uM in [Protein Thermostabilization](/xray-mp-wiki/concepts/construct-design/thermostabilization/) assays, comparable to histamine (400 +/- 150 uM). Benzamidine binds at the orthosteric neurotransmitter pocket between subunits, with its benzyl ring stacked between Phe 200 and Tyr 62, and its amidinium group forming hydrogen bonds with Glu 155, Ser 156, and Tyr 157, plus cation-pi interactions with Tyr 157 and Tyr 205.


### Crystallization additive for GABA_A R

Benzamidine (2% v/v) was used as a crystallization additive in sitting-drop vapor diffusion experiments, enabling the formation of high-resolution diffracting crystals of GABA_A R-β3 at 3.0 A resolution. Five benzamidine molecules were observed bound in the five neurotransmitter-binding sites per pentamer.


### Sodium ion-mimicking pharmacophore in GPCR ligands

The benzamidine moiety serves as a sodium ion-mimicking pharmacophore in [Leukotriene B4 Receptor 1 (BLT1) — Guinea Pig and Human](/xray-mp-wiki/proteins/gpcr/blt1/) ligands. In the BLT1-[BIIL260](/xray-mp-wiki/reagents/ligands/biil260/) crystal structure, the positively charged protonated amide group of the benzamidine moiety occupies the position of the structurally bound sodium ion in the conserved sodium-binding site (coordinated by D66 2.50, V69 2.53, S106 3.39, W236 6.48, S276 7.45). This mimics the entire sodium ion-centered water cluster, stabilizing [Leukotriene B4 Receptor 1 (BLT1) — Guinea Pig and Human](/xray-mp-wiki/proteins/gpcr/blt1/) in the inactive state. Free benzamidine at 30 mM can compete with [BIIL260](/xray-mp-wiki/reagents/ligands/biil260/) for this site, demonstrating that the benzamidine moiety alone can serve as a negative allosteric modulator for [Leukotriene B4 Receptor 1 (BLT1) — Guinea Pig and Human](/xray-mp-wiki/proteins/gpcr/blt1/).


## Examples from This Wiki

| Protein | Concentration | Context | Result |
|---|---|---|---|
| Human GABA_A Receptor Beta-3 Subunit | 2% (v/v) | Crystallization additive in sitting-drop vapor diffusion at 4 C | Enabled high-resolution crystal growth (PDB 4COF, 3.0 A) |
| Human GABA_A Receptor Beta-3 Subunit | 61 uM (EC50) | Agonist activity measured by whole-cell patch-clamp electrophysiology | Induced desensitization currents in HEK293S-GnTI- cells |
| Human GABA_A Receptor Beta-3 Subunit | 370 uM (EC50) | [Protein Thermostabilization](/xray-mp-wiki/concepts/construct-design/thermostabilization/) in detergent micelles measured by SEC | Stabilized receptor at high temperature, comparable to histamine |
| Guinea Pig Leukotriene B4 Receptor 1 ([Leukotriene B4 Receptor 1 (BLT1) — Guinea Pig and Human](/xray-mp-wiki/proteins/gpcr/blt1/)) | 30 mM (free benzamidine) | Free benzamidine competes with [BIIL260](/xray-mp-wiki/reagents/ligands/biil260/) for the sodium ion-binding site of [Leukotriene B4 Receptor 1 (BLT1) — Guinea Pig and Human](/xray-mp-wiki/proteins/gpcr/blt1/). In competition binding assays with [3H][LTB4](/xray-mp-wiki/reagents/ligands/ltb4/), 30 mM benzamidine displaced [BIIL260](/xray-mp-wiki/reagents/ligands/biil260/) from the allosteric site, demonstrating that the benzamidine moiety alone can serve as a negative allosteric modulator.
 | Benzamidine acts as a negative allosteric modulator of [Leukotriene B4 Receptor 1 (BLT1) — Guinea Pig and Human](/xray-mp-wiki/proteins/gpcr/blt1/), competing with [BIIL260](/xray-mp-wiki/reagents/ligands/biil260/) for the conserved sodium ion-binding site
 |

## Advantages and Disadvantages

No advantages/disadvantages recorded.

## Comparison with Related Reagents

No comparison data available.

## Cross-References

- [Human GABA_A Receptor Beta-3 Subunit](/xray-mp-wiki/proteins/cys-loop-receptors/gabar-b3/) — Primary target protein; benzamidine is the bound agonist in PDB 4COF
- [GABA (Gamma-Aminobutyric Acid)](/xray-mp-wiki/reagents/ligands/gaba/) — Natural neurotransmitter agonist of GABA_A receptors
- [Histamine](/xray-mp-wiki/reagents/ligands/histamine/) — Related GABA_A R agonist; EC50 = 400 uM in thermostabilization
- [Etomidate](/xray-mp-wiki/reagents/ligands/etomidate/) — Intravenous anaesthetic that binds to GABA_A R transmembrane pocket
- [Propofol](/xray-mp-wiki/reagents/ligands/propofol/) — Intravenous anaesthetic that binds to GABA_A R transmembrane pocket
- [Fipronil](/xray-mp-wiki/reagents/additives/fipronil/) — Channel blocker used in electrophysiology with benzamidine agonist
- [Picrotoxin](/xray-mp-wiki/reagents/additives/picrotoxin/) — Convulsant channel blocker used in electrophysiology with benzamidine
- [Guinea Pig Leukotriene B4 Receptor 1 (BLT1)](/xray-mp-wiki/proteins/gpcr/blt1/) — Benzamidine moiety of BIIL260 mimics sodium ion in BLT1 structure
- [Protein Thermostabilization](/xray-mp-wiki/concepts/construct-design/thermostabilization/) — Related biological concept
- [BIIL260](/xray-mp-wiki/reagents/ligands/biil260/) — Related ligand or cofactor
