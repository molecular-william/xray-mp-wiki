---
title: "Cytochrome b5 Reductase"
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2020.05.017]
verified: false
---

# Cytochrome b5 Reductase

## Overview

Cytochrome b5 reductase (b5R) is a membrane-embedded flavoprotein that catalyzes the transfer of electrons from [NADH](/xray-mp-wiki/reagents/cofactors/nadh) or NADPH to cytochrome b5. It consists of a single N-terminal transmembrane helix anchoring it to the endoplasmic reticulum membrane and a large soluble cytosolic domain composed of an N-terminal FAD-binding half and a C-terminal NAD(P)H-binding half. This paper reports the expression and purification of the soluble domain of mouse b5R for reconstitution of the SCD1 electron transfer chain in vitro.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2020.05.017 | 1UMK | not specified in this paper | not specified | Soluble cytosolic domain of mouse cytochrome b5 reductase | FAD (flavin adenine dinucleotide) |

## Expression and Purification

- **Expression system**: Escherichia coli (pET vector)
- **Construct**: Mouse cytochrome b5 reductase soluble domain, N-terminally tagged with polyhistidine tag and TEV protease site

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell expression and lysis | E. coli expression in pET vector with sonication | -- | Buffer A (composition not fully specified) + -- | Cells supplemented with 100 uM FAD in media for flavin cofactor incorporation |
| Affinity chromatography | Cobalt affinity chromatography | [TALON](/xray-mp-wiki/reagents/additives/talon) cobalt-based affinity resin | -- + -- | Polyhistidine tag captured on [TALON](/xray-mp-wiki/reagents/additives/talon) resin |
| Tag cleavage | TEV protease cleavage | [TALON](/xray-mp-wiki/reagents/additives/talon) resin | -- + -- | TEV protease cleaved His tag |
| Concentration | Concentration | -- | -- + -- | Concentrated using 10 kDa cutoff concentrators |


## Crystallization

No crystallization described.

## Biological / Functional Insights

### Electron donor to cytochrome b5

Cytochrome b5 reductase reduces the heme group of cytochrome b5 using [NADH](/xray-mp-wiki/reagents/cofactors/nadh) or
NADPH as the electron donor. The NAD(P)H binds to the C-terminal half of the
soluble domain while FAD binds to the N-terminal half. Electron flow proceeds
from NAD(P)H to FAD to the b-type heme of cytochrome b5. In the SCD1 electron
transfer chain, b5R reduces cyt b5, which then donates electrons to SCD1 for
the desaturation reaction.

### In vitro reconstituted electron transfer chain

The soluble domains of b5R and cyt b5, together with SCD1 and NADH, form a
complete in vitro electron transfer chain capable of catalyzing the conversion
of [STEAROYL-COA](/xray-mp-wiki/reagents/ligands/stearoyl-coa) to oleoyl-CoA. The initial rate of oleoyl-CoA production yielded
Km = 6.3 +/- 1.2 uM and kcat = 2.78 +/- 0.59 min-1 for stearoyl-CoA. The rate
limiting step is the interaction between cyt b5 and SCD1.


## Cross-References

- [Mouse Stearoyl-CoA Desaturase 1 (mSCD1)](/xray-mp-wiki/proteins/enzymes/mouse-scd1/) — Terminal electron acceptor in the reconstituted electron transfer chain
- [Cytochrome b5](/xray-mp-wiki/proteins/enzymes/cytochrome-b5/) — Direct electron acceptor from b5R; intermediate carrier to SCD1
- [NADH](/xray-mp-wiki/reagents/cofactors/nadh/) — Primary electron donor for b5R
- [STEAROYL-COA](/xray-mp-wiki/reagents/ligands/stearoyl-coa) — Reagent used in this study
- [NADH](/xray-mp-wiki/reagents/cofactors/nadh) — Reagent used in this study
- [TALON](/xray-mp-wiki/reagents/additives/talon) — Reagent used in this study
