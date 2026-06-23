---
title: Cytochrome b5
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2020.05.017, doi/10.1038##nature14549]
verified: false
---

# Cytochrome b5

## Overview

Cytochrome b5 is a membrane-embedded electron transfer protein consisting of a soluble cytosolic domain and a single C-terminal transmembrane helix. The soluble domain contains a b-type heme group ligated by two axial histidine residues. In the endoplasmic reticulum, cytochrome b5 serves as the intermediate electron carrier between cytochrome b5 reductase and various downstream enzymes including [STEAROYL-COA](/xray-mp-wiki/reagents/ligands/stearoyl-coa) desaturase 1 (SCD1). This paper reports the expression and purification of the soluble domain of mouse cytochrome b5 for in vitro electron transfer studies.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2020.05.017 | 2I96 | not specified in this paper | not specified | Soluble cytosolic domain of mouse cytochrome b5 | B-type heme (protoporphyrin IX with [IRON](/xray-mp-wiki/reagents/additives/iron)) |

## Expression and Purification

- **Expression system**: Escherichia coli (pET vector)
- **Construct**: Mouse cytochrome b5 soluble domain, C-terminally tagged with polyhistidine tag and TEV protease site

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell expression and lysis | E. coli expression in pET vector with sonication | -- | Buffer A (composition not fully specified) + -- | Cells supplemented with 0.5 mM delta-aminolevulinic acid, 5 uM FeCl3, and 1 uM hemin chloride for [HEME](/xray-mp-wiki/reagents/ligands/heme) biosynthesis |
| Affinity chromatography | Cobalt affinity chromatography | [TALON](/xray-mp-wiki/reagents/additives/talon) cobalt-based affinity resin | -- + -- | Polyhistidine tag captured on [TALON](/xray-mp-wiki/reagents/additives/talon) resin |
| Tag cleavage | TEV protease cleavage | [TALON](/xray-mp-wiki/reagents/additives/talon) resin | -- + -- | TEV protease cleaved His tag |
| Concentration | Concentration | -- | -- + -- | Concentrated using 10 kDa cutoff concentrators |


## Crystallization

No crystallization described.

## Biological / Functional Insights

### Electron transfer to SCD1

In the SCD1 electron transfer chain, reduced ferrous cytochrome b5 donates
electrons to SCD1, becoming oxidized. The oxidation of cyt b5 by SCD1 exhibits
a biphasic time course with rate constants k1 = 1.86 min-1 and k2 = 0.246 min-1,
as monitored by the decrease of the Soret peak at 423 nm. This interaction is
the rate-limiting step in the assembled electron transfer chain. The reaction
must be performed anaerobically to prevent auto-oxidation by molecular oxygen.

### Spectroscopic characterization

The soluble domain of cytochrome b5 exhibits characteristic spectroscopic
features confirming the presence of the b-type heme cofactor. The oxidized form
shows a Soret peak at 413 nm, which shifts to 423 nm upon reduction. Reduction
is achieved by cytochrome b5 reductase in the presence of [NADH](/xray-mp-wiki/reagents/cofactors/nadh). The heme is
ligated by two axial histidine residues, characteristic of b-type cytochromes.


## Cross-References

- [Mouse Stearoyl-CoA Desaturase 1 (mSCD1)](/xray-mp-wiki/proteins/enzymes/mouse-scd1/) — Direct electron acceptor; cyt b5 oxidized by SCD1
- [Cytochrome b5 Reductase](/xray-mp-wiki/proteins/enzymes/cytochrome-b5-reductase/) — Reduces cytochrome b5 using NADH as electron donor
- [NADH](/xray-mp-wiki/reagents/cofactors/nadh/) — Electron donor for cytochrome b5 reduction by b5R
- [NADH](/xray-mp-wiki/reagents/cofactors/nadh) — Reagent used in this study
- [TALON](/xray-mp-wiki/reagents/additives/talon) — Reagent used in this study
- [HEME](/xray-mp-wiki/reagents/ligands/heme) — Reagent used in this study
- [STEAROYL-COA](/xray-mp-wiki/reagents/ligands/stearoyl-coa) — Reagent used in this study
- [IRON](/xray-mp-wiki/reagents/additives/iron) — Reagent used in this study
