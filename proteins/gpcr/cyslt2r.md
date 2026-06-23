---
title: Cysteinyl Leukotriene Receptor 2 (CysLT2R)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-019-13348-2]
verified: false
---

# Cysteinyl Leukotriene Receptor 2 (CysLT2R)

## Overview

Cysteinyl leukotriene receptor type 2 (CysLT2R) is a class A G protein-coupled receptor (GPCR) that mediates pro-inflammatory responses to cysteinyl leukotrienes LTC4 and LTD4. Four crystal structures of CysLT2R were determined in complex with three dual CysLT1R/CysLT2R antagonists (ONO-2570366, ONO-2770372, and ONO-2080365) at resolutions of 2.4-2.7 A using lipidic cubic phase (LCP) crystallization. The structures, combined with comprehensive mutagenesis and computational modeling, reveal molecular determinants of ligand selectivity between [Cyslt1R](/xray-mp-wiki/proteins/gpcr/cyslt1r/) and CysLT2R subtypes and provide structural explanations for disease-associated single nucleotide variants including M201V (atopic asthma) and L129Q (uveal melanoma).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-019-13348-2 | 6RZ6 | 2.4 | P 21 21 21 | Human CysLT2R with [Bril](/xray-mp-wiki/reagents/protein-tags/bril/) fusion in ICL3, N- and C-terminal [Truncation](/xray-mp-wiki/concepts/methods-techniques/truncation/), W51V, D84N, F137Y mutations; complex with ONO-2570366 (cpd 11a) | ONO-2570366 (cpd 11a, antagonist) |
| doi/10.1038##s41467-019-13348-2 | 6RZ7 | 2.4 | Not specified | Human CysLT2R with [Bril](/xray-mp-wiki/reagents/protein-tags/bril/) fusion in ICL3, N- and C-terminal [Truncation](/xray-mp-wiki/concepts/methods-techniques/truncation/), W51V, D84N, F137Y mutations; complex with ONO-2570366 (cpd 11a) | ONO-2570366 (cpd 11a, antagonist) |
| doi/10.1038##s41467-019-13348-2 | 6RZ8 | 2.7 | Not specified | Human CysLT2R with [Bril](/xray-mp-wiki/reagents/protein-tags/bril/) fusion in ICL3, N- and C-terminal [Truncation](/xray-mp-wiki/concepts/methods-techniques/truncation/), W51V, D84N, F137Y mutations; complex with ONO-2770372 (cpd 11b) | ONO-2770372 (cpd 11b, antagonist) |
| doi/10.1038##s41467-019-13348-2 | 6RZ9 | 2.7 | Not specified | Human CysLT2R with [Bril](/xray-mp-wiki/reagents/protein-tags/bril/) fusion in ICL3, N- and C-terminal [Truncation](/xray-mp-wiki/concepts/methods-techniques/truncation/), W51V, D84N, F137Y mutations; complex with ONO-2080365 (cpd 11c) | ONO-2080365 (cpd 11c, antagonist) |

## Expression and Purification

- **Expression system**: Spodoptera frugiperda Sf9 insect cells
- **Construct**: Human CysLT2R (UniProt Q9NS75) with N-terminal HA-FLAG-10xHis-TEV, N-terminal [Truncation](/xray-mp-wiki/concepts/methods-techniques/truncation/) (1-16), C-terminal [Truncation](/xray-mp-wiki/concepts/methods-techniques/truncation/) (323-346), [Bril](/xray-mp-wiki/reagents/protein-tags/bril/) fusion in ICL3 (between E232 and V240), W51V/D84N/F137Y mutations
- **Notes**: Bac-to-Bac baculovirus expression system. Cells infected at MOI 5-10, harvested 48-50 h post-infection. 3 uM BayCysLT2 ligand added at infection.


### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Hypotonic lysis |  | 10 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 20 mM KCl, 10 mM [Mgcl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/) | Cells washed with hypotonic and high osmotic buffers with protease inhibitors |
| Membrane solubilization | Detergent extraction |  | 300 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 25 uM ligand, 2 mg/ml [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.2% CHS | Solubilization for 3.5 h at 4 C |
| Affinity chromatography | IMAC ([Talon](/xray-mp-wiki/reagents/additives/talon/)) | [Talon](/xray-mp-wiki/reagents/additives/talon/) IMAC resin | Wash 1 - 100 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 250 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 15 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 8 mM [ATP](/xray-mp-wiki/reagents/ligands/atp/) / Wash 2 - 50 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 250 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 30 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.02% CHS (wash 1) / 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.01% CHS (wash 2) | Overnight batch binding with 10 CV washes |
| Size-exclusion chromatography | Gel filtration | Superdex 200 | 25 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 150 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 25 uM ligand + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.01% CHS | Peak fractions pooled and concentrated |


## Crystallization

### doi/10.1038##s41467-019-13348-2

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | Purified CysLT2R in DDM/CHS, reconstituted into monoolein-based LCP |
| Lipid | Monoolein |
| Protein-to-lipid ratio | 2:3 (w/w) |
| Temperature | 20 |
| Growth time | Not specified |
| Cryoprotection | Crystals harvested and flash-cooled in liquid nitrogen |
| Notes | Four structures determined: CysLT2R-11a in two space groups (2.4 A each, PDB 6RZ6 and 6RZ7), CysLT2R-11b (2.7 A, PDB 6RZ8), and CysLT2R-11c (2.7 A, PDB 6RZ9). Structures solved by molecular replacement using CysLT1R-pranlukast as search model.
 |


## Biological / Functional Insights

### Ligand-binding pocket architecture

CysLT2R adopts the canonical seven-transmembrane helical bundle. All three antagonists share the same 3,4-dihydro-2H-1,4-benzoxazine scaffold and bind in similar conformations. Y119(3.33) is a key anchoring residue forming multiple polar contacts with the benzoxazine part, carboxylic group, and amide linker. The N-linked carboxypropyl moiety makes salt bridges with K37(1.31) and H284(7.32) that are specific to CysLT2R.

### Antagonist selectivity determinants between CysLTR subtypes

Docking of 18 scaffold derivatives revealed structural basis for selectivity. [Cyslt1R](/xray-mp-wiki/proteins/gpcr/cyslt1r/) has F150(4.52) which restricts the subpocket near TM4, while CysLT2R has L165(4.52) which creates a more open cleft. For the N-substituent, CysLT1R's Y26(1.35) forms a hydrogen bond with carboxyl groups (as in cpd 13e, 1800-fold selective for [Cyslt1R](/xray-mp-wiki/proteins/gpcr/cyslt1r/)), while CysLT2R has F41(1.35) which cannot form such interactions, explaining selectivity preferences.

### Atopic asthma-associated M201V polymorphism

M201(5.38) together with M172(4.59), L173(4.60), and L198(5.35) define the hydrophobic part of the ligand-binding pocket. The M201V variant (atopic asthma-associated) still responds to LTD4 stimulation but with significantly decreased potency and efficacy compared to wild-type. Substitution with alanine or leucine results in nonresponsive mutants, indicating the specific effect of the valine substitution.

### Oncogenic L129Q constitutive activation

L129(3.43)Q mutation is associated with uveal melanoma and blue nevi. This mutation displays constitutive activity for the Gq pathway with a fourfold increase in basal IP1 accumulation and is unresponsive to LTD4 stimulation. Position 3.43 mutations to R, K, A, E, or Q induce constitutive activation in several GPCRs.

### Intracellular helix H8 in CysLT receptors

CysLT2R displays a well-resolved intracellular helix H8, while [Cyslt1R](/xray-mp-wiki/proteins/gpcr/cyslt1r/) does not. The difference stems from [Cyslt1R](/xray-mp-wiki/proteins/gpcr/cyslt1r/) having a flexible GG(8.48) motif at the TM7-H8 junction, whereas CysLT2R has GE(8.48). This structural insight helps explain differences in receptor stability and signaling properties between the two subtypes.

### Mapping of disease-associated SNVs

Structural mapping of 117 missense SNV positions from the ExAC database revealed that 9 belong to the ligand-binding pocket, 7 are activation-related microswitches or in the sodium-binding site, and 9 reside on the G protein and beta-arrestin-binding interface. Most ExAC mutations are very rare (MAF < 10^-4), making disease association difficult.


## Cross-References

- [Cysteinyl Leukotriene Receptor 1 (CysLT1R)](/xray-mp-wiki/proteins/gpcr/cyslt1r/) — Closely related GPCR subtype; companion paper describes CysLT1R structures with zafirlukast and pranlukast
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for CysLT2R solubilization and purification
- [Lipidic Cubic Phase (In Meso) Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method used for all CysLT2R structures
- [Cholesteryl Hemisuccinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Additive used in purification to stabilize the receptor
- [GPCR G Protein Coupling](/xray-mp-wiki/concepts/signaling-receptors/gpcr-g-protein-coupling/) — CysLT2R is a GPCR that signals through Gq/11 pathway
- [Bril](/xray-mp-wiki/reagents/protein-tags/bril/) — Referenced in context related to Bril
- [Truncation](/xray-mp-wiki/concepts/methods-techniques/truncation/) — Referenced in context related to Truncation
- [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) — Referenced in context related to Hepes
- [Mgcl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/) — Referenced in context related to Mgcl2
- [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) — Referenced in context related to Iodoacetamide
