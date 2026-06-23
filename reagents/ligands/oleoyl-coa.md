---
title: Oleoyl-CoA
created: 2026-05-27
updated: 2026-05-27
type: reagent
category: reagents
layout: default
tags: [ligand, subdirectory-ligands]
sources: [doi/10.1016##j.jmb.2020.05.017]
verified: false
---

# Oleoyl-CoA

## Overview

Oleoyl-CoA (18:1-CoA) is the monounsaturated product of the [Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/) desaturase 1 (SCD1) reaction. It is an 18-carbon fatty acyl chain with a cis-9 double bond, linked to coenzyme A via a thioester bond. Oleoyl-CoA is both a physiological product of SCD1 and the endogenous ligand found tightly bound in the substrate tunnel of both zinc-containing and iron-containing SCD1 crystal structures. The double bond confers a different acyl chain conformation compared to [Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/) (18:0-CoA), which may contribute to product inhibition.


## Properties

- **Chemical name**: (Z)-octadec-9-enoyl-CoA
- **Chemical formula**: C27H46N7O17P3S
- **Molecular weight**: 868 g/mol
- **Class**: Acyl-CoA derivative

## Use in Membrane Protein Work

### Product of SCD1 desaturation reaction

Oleoyl-CoA is the primary product of the SCD1-catalyzed conversion of [Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/) (18:0-CoA) to a monounsaturated fatty acyl-CoA. In vitro assays using purified SCD1, [Cytochrome b5](/xray-mp-wiki/proteins/enzymes/cytochrome-b5/), [Cytochrome b5 Reductase](/xray-mp-wiki/proteins/enzymes/cytochrome-b5-reductase/), and NADH show de novo synthesis of oleoyl-CoA from [Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/). The reaction exhibits Michaelis-Menten kinetics with Km = 6.3 +/- 1.2 uM and kcat = 2.78 +/- 0.59 min-1. Product inhibition is observed after approximately 10 minutes of turnover.


### Endogenous ligand in SCD1 crystal structures

Oleoyl-CoA is tightly bound to SCD1 and was identified in both the iron-containing structure (PDB 6WF2) and the zinc-containing structure (PDB 4YMK). The molar ratio of oleoyl-CoA to protein is approximately 1:1. The CoA moiety is recognized by the protein surface while the acyl chain accommodates a V-shaped tunnel inside the protein. The Delta9 carbon is approximately 3 A from the water bound to Fe2 in the active site.


## Examples from This Wiki

| Protein | Concentration | Context | Result |
|---|---|---|---|
| Mouse [Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/) Desaturase 1 (mSCD1) | Approximately 1:1 molar ratio to protein | Endogenous ligand in crystal structure of iron-containing mSCD1 (PDB 6WF2, 3.5 A) | Oleoyl-CoA bound in V-shaped tunnel; Delta9 carbon 3 A from Fe2-bound water |
| Mouse [Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/) Desaturase 1 (mSCD1) | Approximately 1:1 molar ratio to protein | Endogenous ligand in zinc-containing mSCD1 structure (PDB 4YMK) | Refinement with oleoyl-CoA (18:1) fits better at Delta9/Delta10 positions than previously modeled [Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/) (18:0) |
| Mouse [Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/) Desaturase 1 (mSCD1) | Product of reaction | In vitro desaturation assay with SCD1, cyt b5, b5R, [Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/), and NADH | De novo synthesis of oleoyl-CoA confirmed by HPLC; initial rate used for Michaelis-Menten kinetics |

## Advantages and Disadvantages

No advantages/disadvantages recorded.

## Comparison with Related Reagents

No comparison data available.

## Cross-References

- [Mouse Stearoyl-CoA Desaturase 1 (mSCD1)](/xray-mp-wiki/proteins/enzymes/mouse-scd1/) — Endogenous bound ligand and product of SCD1 reaction
- [Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/) — Substrate of SCD1; precursor to oleoyl-CoA
- [Cytochrome b5 Reductase](/xray-mp-wiki/proteins/enzymes/cytochrome-b5-reductase/) — Related protein structure
- [Cytochrome b5](/xray-mp-wiki/proteins/enzymes/cytochrome-b5/) — Related protein structure
- [Oleic Acid](/xray-mp-wiki/reagents/lipids/oleic-acid/) — Additive used in purification or crystallization buffers
