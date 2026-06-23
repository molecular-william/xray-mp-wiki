---
title: Human Alpha-1B Adrenergic Receptor (alpha1B AR)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-021-27911-3]
verified: false
---

# Human Alpha-1B Adrenergic Receptor (alpha1B AR)

## Overview

The human alpha-1B adrenergic receptor (alpha1B AR, ADRA1B) is a class A G protein-coupled receptor that mediates physiological responses to the endogenous catecholamines [Epinephrine](/xray-mp-wiki/reagents/epinephrine/) and [Norepinephrine](/xray-mp-wiki/reagents/norepinephrine/). It plays key roles in cardiovascular function, CNS signaling, and immune regulation. The crystal structure of alpha1B AR bound to the inverse agonist (+)-cyclazosin was determined at 2.87 A resolution (anisotropy-corrected, PDB 7B6W), enabled by CHESS-based directed evolution for stabilization and a [Designed Ankyrin Repeat Protein (DARPin)](/xray-mp-wiki/reagents/protein-tags/darpin/) D12 crystallization chaperone. The structure revealed a canonical GPCR fold with two unique secondary binding pockets. Structural comparison with alpha2 ARs and construction of alpha1B-alpha2C chimeras identified residues 3.29 and 6.55 as key determinants of ligand selectivity. The structure provides a template for rational design of alpha1B AR-selective ligands and for understanding off-target binding of aminergic drugs.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-021-27911-3 | 7B6W | 2.87 A (anisotropy-corrected from 3.1 A) | Not specified in paper | Human alpha1B AR with 12 stabilizing mutations from CHESS directed evolution, N-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) (residues 1-34 deleted), ICL3 deletion (residues K249-L283 deleted), and C-terminal [Designed Ankyrin Repeat Protein (DARPin)](/xray-mp-wiki/reagents/protein-tags/darpin/) D12 crystallization chaperone fused via AEDLVEDWE linker; expressed in E. coli
 | (+)-Cyclazosin (inverse agonist) |

## Expression and Purification

- **Expression system**: E. coli (inner membranes)
- **Construct**: alpha1B AR_XTAL: N-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) M1-N34 deleted, ICL3 K249-L283 deleted, 12 stabilizing mutations from directed evolution, [Designed Ankyrin Repeat Protein (DARPin)](/xray-mp-wiki/reagents/protein-tags/darpin/) D12 fused at C-terminus via AEDLVEDWE linker


### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Cell lysis and membrane isolation | -- | Hypotonic buffer with protease inhibitors + -- | Cells harvested and lysed; membranes isolated by centrifugation |
| Solubilization and purification | Affinity chromatography | Ligand-affinity column (cleavable prazosin analog) | PBS-E (1.8 mM KH2PO4, 137 mM NaCl, 2.7 mM KCl, 1 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/), pH 7.4) + [DM](/xray-mp-wiki/reagents/detergents/dm/) (DM) / CHAPS / [DHPC](/xray-mp-wiki/reagents/detergents/dhpc/) | Receptor solubilized in [DM](/xray-mp-wiki/reagents/detergents/dm/)/CHAPS, incubated with QAPB fluorescent ligand, purified using cleavable ligand column strategy. Further details in Schuster et al. BBA Biomembr. 2020.
 |


## Crystallization

### doi/10.1038##s41467-021-27911-3

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) (inferred - standard for GPCR crystallography) |
| Protein sample | Purified alpha1B AR_XTAL in complex with (+)-cyclazosin |
| Temperature | Not specified in paper |
| Growth time | Not specified in paper |
| Cryoprotection | Not specified in paper |
| Notes | Structure determined at 3.1 A (processed to 2.87 A with STARANISO anisotropy correction). Data collected at synchrotron. Molecular replacement using turkey beta1 AR (PDB 6IBL) and [Designed Ankyrin Repeat Protein (DARPin)](/xray-mp-wiki/reagents/protein-tags/darpin/) D12 (PDB 5LW2) as search models.
 |


## Biological / Functional Insights

### Two unique secondary binding pockets identified

The (+)-cyclazosin ligand adopts an inverted L-shaped binding mode. The dimethoxyquinazoline moiety occupies the orthosteric binding site (OBS). The cis-decahydroquinoxaline moiety sits at the boundary between OBS and a secondary pocket defined by TM3 and ECL2. The furan-2-yl-methanone moiety is accommodated in secondary binding pockets proximal to the extracellular surface, making (+)-cyclazosin a bitopic ligand.

### Residues 3.29 and 6.55 as key determinants of ligand selectivity

Using structural comparison of alpha1B AR with alpha2 ARs and construction of alpha1B-alpha2C chimeras, residues A122(3.29) and L314(6.55) were identified as key determinants of ligand selectivity. The quadruple mutant alpha1B-alpha2C(YLLY) (W121Y, A122L, V197L, L314Y) showed nearly three orders of magnitude improved affinity for the alpha2-selective antagonist RS79948. Position 3.29 (Ala in alpha1, Leu in alpha2) modulates the distinct selectivity profiles of yohimbine and corynanthine. ECL2 in alpha2 ARs is postulated to sterically hinder binding of bulky piperazinyl quinazoline ligands.

### DARPin crystallization chaperone strategy

The receptor was stabilized using CHESS-based directed evolution in E. coli and fused to a [Designed Ankyrin Repeat Protein (DARPin)](/xray-mp-wiki/reagents/protein-tags/darpin/) D12 crystallization chaperone at the C-terminus replacing helix 8. This same strategy was previously used for NTSR1 structures. The [Designed Ankyrin Repeat Protein (DARPin)](/xray-mp-wiki/reagents/protein-tags/darpin/) was modified with N-terminal deletions and point mutations for optimized crystal packing. [Designed Ankyrin Repeat Protein (DARPin)](/xray-mp-wiki/reagents/protein-tags/darpin/) D12-mediated crystal contacts enabled structure determination of this previously recalcitrant GPCR.


## Cross-References

- [X-ray Crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/) — Method used in the study
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) — Key concept related to this protein
- [Designed Ankyrin Repeat Protein (DARPin)](/xray-mp-wiki/reagents/protein-tags/darpin/) — Key concept related to this protein
- [GR (Halobacterium sp. GR Bacteriorhodopsin)](/xray-mp-wiki/proteins/rhodopsins/gr/) — Related protein mentioned in the study
- [1,2-Dihexanoyl-sn-glycero-3-phosphocholine (DHPC)](/xray-mp-wiki/reagents/detergents/dhpc/) — Reagent used in the study
- [n-Octyl beta-D-glucopyranoside (OG)](/xray-mp-wiki/reagents/detergents/og/) — Detergent used in purification
- [n-Decyl-beta-D-Maltoside (DM)](/xray-mp-wiki/reagents/detergents/dm/) — Reagent used in the study
- [TES Buffer (N-Tris(hydroxymethyl)methyl-2-aminoethanesulfonic acid)](/xray-mp-wiki/reagents/buffers/tes/) — Reagent used in the study
- [Ethylenediaminetetraacetic Acid (EDTA)](/xray-mp-wiki/reagents/additives/edta/) — Reagent used in the study
- [Epinephrine](/xray-mp-wiki/reagents/epinephrine/) — Reagent used in the study
