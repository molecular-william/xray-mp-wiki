---
title: Mouse Stearoyl-CoA Desaturase 1 (mSCD1)
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2020.05.017, doi/10.1038##nature14549]
verified: false
---

# Mouse Stearoyl-CoA Desaturase 1 (mSCD1)

## Overview

Mouse [Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/) desaturase 1 (SCD1) is a membrane-embedded diiron enzyme embedded in the endoplasmic reticulum membrane that catalyzes the formation of a cis-double bond at the Delta9 position of saturated acyl-CoAs, converting them to monounsaturated acyl-CoAs. This paper reports the first crystal structure of iron-containing mouse SCD1 (PDB 6WF2) solved at 3.5 A resolution by X-ray crystallography, revealing a unique all-histidine-coordinated diiron center and a tightly bound [Oleoyl-CoA](/xray-mp-wiki/reagents/ligands/oleoyl-coa/) ligand. The structure was expressed in HEK293 cells using a novel [IRON](/xray-mp-wiki/reagents/additives/iron/) incorporation protocol, overcoming the zinc misincorporation problem that plagued previous SCD1 structures.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2020.05.017 | 6WF2 | 3.5 A | P212121 | mDeltaSCD1 (residues 41-361), N-terminal 2-23 deletion, iron-containing diiron center | [Oleoyl-CoA](/xray-mp-wiki/reagents/ligands/oleoyl-coa/) |
| doi/10.1038##nature14549 | 4YMK | 2.6 A | P212121 | Mouse SCD1 Delta2-23 (residues 24-355), N-terminal 2-23 [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/), zinc-containing dimetal center | [Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/) |

## Expression and Purification

- **Expression system**: HEK293S GnTI- suspension cells (BacMam expression)
- **Construct**: Mouse SCD1 gene with deletion of residues 2-23 at N-terminus (mDeltaSCD1), codon-optimized for human cell expression, C-terminally tagged with GFP and TEV protease site

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and membrane preparation | HEK293S GnTI- suspension cell expression with BacMam vector | -- | 20 mM HEPES pH 7.5, 150 mM NaCl, 1 mM PMSF, 5 mM MgCl2, DNase I + -- | Cells infected with 10% P3 virus, supplemented with 5 mg/L iron-saturated transferrin and 5 uM FeCl3. Induced with 10 mM [Sodium Butyrate](/xray-mp-wiki/reagents/additives/sodium-butyrate/), 30 C for 48 h |
| Membrane solubilization | Detergent solubilization | -- | 20 mM HEPES pH 7.5, 150 mM NaCl + 40 mM [DM](/xray-mp-wiki/reagents/detergents/dm/) (DM) | 40 mM DM added to membranes, 4 C for 2 h under gentle agitation. Centrifuged at 55,000g for 45 min at 4 C |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) (GFP [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/)) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | CNBR-activated Sepharose coupled to GFP [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) (GFPnb) | 20 mM HEPES pH 7.5, 150 mM NaCl, 4 mM DM + 4 mM DM | 1 h incubation at 4 C, washed with 20 column volumes of buffer B |
| Tag cleavage | TEV protease cleavage | GFP [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) resin | Room temperature + 4 mM DM | TEV protease cleaved GFP tag at room temperature for 1 h |
| Secondary affinity cleanup | Cobalt [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [TALON](/xray-mp-wiki/reagents/additives/talon/) cobalt-based affinity resin | -- + -- | Removed His-tagged TEV protease |
| Size-exclusion chromatography | Size-exclusion chromatography | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 10/300 GL | 20 mM HEPES pH 7.5, 150 mM NaCl, 4 mM DM + 4 mM DM | Peak fractions collected and analyzed by SDS-PAGE |


## Crystallization

### doi/10.1016##j.jmb.2020.05.017

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | 30-50 mg/ml mDeltaSCD1 in [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) + 10% [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) (w/w) |
| Temperature | 20 C |
| Growth time | not specified |
| Cryoprotection | None; crystals flash frozen in liquid nitrogen directly |
| Notes | Protein mixed with molten [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) doped with 10% [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) at 1:1.5 (v/w) ratio using coupled syringe device. 50 nl deposited over 800 nl precipitant using Gryphon LCP robot. Data collected at 24-ID (NE-CAT), APS, Argonne. Wavelength 0.9791 A, resolution 3.51 A. R/Rfree 21.9%/27.6%. Model includes residues 41-361, two [IRON](/xray-mp-wiki/reagents/additives/iron/) ions, and one [Oleoyl-CoA](/xray-mp-wiki/reagents/ligands/oleoyl-coa/) |


## Biological / Functional Insights

### Unique all-histidine-coordinated diiron center

The diiron center in SCD1 is coordinated by nine highly conserved histidine
residues that segregate into four histidine-rich motifs distant in the primary
sequence. Fe1 is coordinated by five histidine residues, while Fe2 is coordinated
by four histidines and a putative water molecule. The two [IRON](/xray-mp-wiki/reagents/additives/iron/) ions are separated
by approximately 6.4 A. Unlike other diiron enzymes, there is no oxo-bridge
between the [IRON](/xray-mp-wiki/reagents/additives/iron/) ions, and the coordination geometry and inter-ionic distance
exceed the range for known reaction intermediates such as cis-mu-1,2-peroxo or
diferryl species. This suggests a novel oxygen activation mechanism in SCD1.

### Tightly bound endogenous oleoyl-CoA ligand

A single [Oleoyl-CoA](/xray-mp-wiki/reagents/ligands/oleoyl-coa/) molecule is tightly bound to SCD1 even in the non-functional
zinc-containing structure (PDB 4YMK). The CoA moiety is recognized by the protein
surface while the 18:1 acyl chain accommodates a V-shaped tunnel. The Delta9 and
Delta10 carbons are positioned at the inflection point of the V-shape, close to
the diiron center. The Delta9 carbon on [Oleoyl-CoA](/xray-mp-wiki/reagents/ligands/oleoyl-coa/) is approximately 3 A from the
water bound to Fe2. The double bond in [Oleoyl-CoA](/xray-mp-wiki/reagents/ligands/oleoyl-coa/) causes a different zigzag
conformation of the acyl chain compared to [Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/), which may contribute
to product inhibition.

### Diiron center structure and iron incorporation protocol

Previous SCD1 structures (PDB 4YMK and 5J45) contained zinc ions instead of [IRON](/xray-mp-wiki/reagents/additives/iron/),
an artifact of heterologous expression in insect cells. Zinc served as a structural
surrogate (0.88 A vs 0.92 A ionic radius) but rendered the enzyme inactive. This
paper developed a protocol for [IRON](/xray-mp-wiki/reagents/additives/iron/) incorporation using HEK293 cells supplemented
with iron-saturated transferrin and FeCl3, achieving >90% [IRON](/xray-mp-wiki/reagents/additives/iron/) occupancy by ICP-MS.
The iron-containing structure is nearly identical to the zinc-containing form
(RMSD 0.3 A for backbone atoms), confirming zinc's suitability as a structural
surrogate.

### In vitro reconstituted electron transfer chain

The complete electron transfer chain was assembled in vitro using purified mouse
SCD1, soluble domains of [Cytochrome b5](/xray-mp-wiki/proteins/enzymes/cytochrome-b5/) and [Cytochrome b5 Reductase](/xray-mp-wiki/proteins/enzymes/cytochrome-b5-reductase/), and
[Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/) as substrate. NADH served as the electron donor. Michaelis-Menten
kinetics yielded a Km of 6.3 +/- 1.2 uM and kcat of 2.78 +/- 0.59 min-1 for
[Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/). The rate-limiting step is the interaction between [Cytochrome b5](/xray-mp-wiki/proteins/enzymes/cytochrome-b5/)
and SCD1 (k1 = 1.86 min-1), comparable to the steady-state rate. Product
inhibition was observed after approximately 10 minutes, with a turnover number
of 7.52 +/- 0.047, likely due to limited detergent micelle capacity.


## Cross-References

- [Cytochrome b5](/xray-mp-wiki/proteins/enzymes/cytochrome-b5/) — Direct electron transfer partner; forms electron transport pair with SCD1
- [Cytochrome b5 Reductase](/xray-mp-wiki/proteins/enzymes/cytochrome-b5-reductase/) — Electron donor to cytochrome b5 in the SCD1 electron transport chain
- [Oleoyl-CoA](/xray-mp-wiki/reagents/ligands/oleoyl-coa/) — Endogenous bound ligand in crystal structure and product of SCD1 reaction
- [Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/) — Substrate of SCD1 desaturation reaction
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used to crystallize iron-containing mSCD1 (PDB 6WF2)
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Primary lipid component of LCP crystallization matrix
- [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) — Precipitant (PEG400) used in LCP crystallization of mSCD1
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer used in purification (20 mM, pH 7.5)
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
