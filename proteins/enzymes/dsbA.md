---
title: "DsbA"
created: 2026-05-27
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2006.10.034, doi/10.1016##j.febslet.2008.07.063]
verified: false
---

# DsbA

## Overview

DsbA is a periplasmic dithiol oxidase from Escherichia coli belonging to the thioredoxin-like protein family. It is the primary enzyme responsible for introducing disulfide bonds into folding secretory and periplasmic proteins by disulfide exchange. DsbA contains a highly reactive, catalytically unstable disulfide bond between Cys27 and Cys29 (numbering of the E. coli protein) that rapidly oxidizes substrate proteins. Reduced DsbA is then reoxidized by the inner membrane quinone reductase [DSBB](/xray-mp-wiki/proteins/dsbB), completing the oxidative protein folding pathway in the E. coli periplasm.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2006.10.034 | 2HI7 | 3.7 | P4(2)2(1)2 | DsbB(Cys130Ser)-DsbA(Cys33Ala) complex, a stable reaction intermediate mimic held together by a Cys30(DsbA)-Cys104(DsbB) intermolecular disulfide bond | [UBIQUINONE](/xray-mp-wiki/reagents/cofactors/ubiquinone) Q8 (bound to DsbB, not directly to DsbA) |
| doi/10.1016##j.febslet.2008.07.063 | 3E9J | Not explicitly stated | Not available | DsbA(Cys33Ala) single-cysteine variant covalently bound to wtDsbB via intermolecular disulfide bond between Cys30 of DsbA and Cys104 of [DSBB](/xray-mp-wiki/proteins/dsbB). The Cys33Ala mutation was introduced to prevent formation of an incorrect disulfide bond during complex formation. | [UBIQUINONE](/xray-mp-wiki/reagents/cofactors/ubiquinone) Q8 (bound to DsbB, not directly to DsbA) |

## Expression and Purification

- **Expression system**: E. coli
- **Construct**: DsbA(Cys33Ala) variant expressed and purified from E. coli. Purified according to an improved protocol compared to the previously described procedure.

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression and purification | Expression and purification | -- | -- + -- | DsbA(Cys33Ala) purified according to an improved protocol. Detailed protocol available in supplementary data. |
| Complex formation | In vitro complex formation | -- | -- + -- | Purified DsbA(Cys33Ala) mixed with wtDsbB-Q8-enriched membrane suspension to form the mixed disulfide complex |


## Crystallization

### doi/10.1016##j.febslet.2008.07.063

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | wtDsbB-DsbA(Cys33Ala)-Q8 complex in nonylmaltoside |
| Reservoir | Not explicitly stated |
| Temperature | Not explicitly stated |
| Growth time | Not explicitly stated |
| Cryoprotection | None; crystals mounted in cryoloops and cryocooled by immersion into liquid nitrogen without additional cryoprotectant |
| Notes | Crystals grown and cryocooled without cryoprotectant. Crystallographic data collection, structure solution and refinement described in supplementary data. Resolution same as the [DSBB](/xray-mp-wiki/proteins/dsbB)(Cys130Ser)-DsbA(Cys33Ala)-Q8 complex structure. |


## Biological / Functional Insights

### Disulfide exchange mechanism with DsbB

DsbA forms an intermolecular disulfide bond with [DSBB](/xray-mp-wiki/proteins/dsbB) during the reoxidation cycle. In the mixed disulfide complex, DsbA(Cys30) forms a disulfide bond with DsbB(Cys104). When wild-type DsbA reacts with wtDsbB, Cys33 of DsbA attacks the intermolecular DsbA(Cys30)-(Cys104)DsbB disulfide bond, regenerating oxidized DsbA and producing semi-reduced DsbB. This semi-reduced state has an inter-loop disulfide exchange that creates the reduced Cys41/Cys44 pair and the Cys104-Cys130 disulfide bond.

### Cys33Ala variant for trapping the charge-transfer intermediate

The DsbA(Cys33Ala) single-cysteine variant was used to trap the charge-transfer intermediate between [DSBB](/xray-mp-wiki/proteins/dsbB) and Q8. The Cys33Ala mutation prevents formation of an incorrect disulfide bond, allowing the formation of a stable ternary complex between wtDsbB, Q8, and DsbA covalently bound via a single intermolecular disulfide bond. This variant enabled crystallization of the charge-transfer complex.

### Oxidative protein folding pathway

DsbA is the central oxidant in the E. coli periplasmic oxidative protein folding pathway. It introduces disulfide bonds into folding polypeptides by disulfide exchange, becoming reduced in the process. The reduced DsbA is then reoxidized by DsbB, which transfers electrons to [UBIQUINONE](/xray-mp-wiki/reagents/cofactors/ubiquinone) Q8 in the inner membrane. This pathway is essential for proper folding of many secretory proteins in Gram-negative bacteria.


## Cross-References

- [DsbB](/xray-mp-wiki/proteins/enzymes/dsbB/) — DsbB is the inner membrane quinone reductase that reoxidizes reduced DsbA, completing the oxidative protein folding cycle
- [Ubiquinone](/xray-mp-wiki/reagents/cofactors/ubiquinone/) — Terminal electron acceptor in the DsbA-DsbB oxidative folding pathway
- [Nonylmaltoside](/xray-mp-wiki/reagents/detergents/nonylmaltoside/) — Detergent used for solubilization of the DsbB-DsbA complex
- [UBIQUINONE](/xray-mp-wiki/reagents/cofactors/ubiquinone) — Reagent used in this study
