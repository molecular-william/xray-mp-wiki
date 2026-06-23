---
title: "M3 Muscarinic Acetylcholine Receptor"
created: 2026-05-28
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2014.08.022, doi/10.1038##nature11114, doi/10.1038##nature10867, doi/10.1038##nature17188]
verified: false
---

# M3 Muscarinic Acetylcholine Receptor

## Overview

The M3 muscarinic [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine) receptor (M3 mAChR) is a class A G protein-coupled receptor that mediates smooth muscle contraction, glandular secretion, and neuronal signaling through Gq/11-coupled pathways. It is a major therapeutic target for conditions including overactive bladder, chronic obstructive pulmonary disease, and hyperhidrosis. Multiple crystal structures of the rat M3 receptor have been solved using T4 lysozyme (T4L) fusion constructs in the third intracellular loop, revealing the binding modes of antagonists including [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium) and [NMS](/xray-mp-wiki/reagents/ligands/n-methylscopolamine) at resolutions up to 2.8 A.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature10867 | 4DAJ | 3.4 A | P 1 | Rat M3 muscarinic receptor, N-terminal FLAG tag, N-glycosylation mutants (4 asparagine to glutamine at positions N6, N15, N41, N48), TEV protease site at residues 50-56, ICL3 replaced by T4 lysozyme (residues 259-482), C-terminal His tag (6His)
 | Tiotropium |
| doi/10.1016##j.str.2014.08.022 | 4U14 | 3.6 A | P41212 | Rat M3 muscarinic receptor, N-terminal FLAG tag, N-glycosylation mutants (4 asparagine to glutamine), TEV protease site at residues 50-56, ICL3 replaced by T4 lysozyme (residues 259-482), C-terminal His tag
 | Tiotropium |
| doi/10.1016##j.str.2014.08.022 | 4U15 | 2.8 A | C2 | Rat M3 muscarinic receptor, N-terminal FLAG tag, N-glycosylation mutants, TEV protease site at residues 50-56, ICL3 replaced by mT4L (minimal T4 lysozyme with GGSGG linker), C-terminal truncation at residue 569, His tag
 | Tiotropium |
| doi/10.1016##j.str.2014.08.022 | 4U16 | 3.7 A | C2 | Rat M3 muscarinic receptor, N-terminal FLAG tag, N-glycosylation mutants, TEV protease site at residues 50-56, ICL3 replaced by mT4L (minimal T4 lysozyme with GGSGG linker), C-terminal truncation at residue 569, His tag
 | N-methylscopolamine |

 - R-work 25.1%, R-free 30.3%; Data collection: 76 crystals merged. Cell dimensions: a=54.8, b=61.3, c=176.9 A, alpha=85.9, beta=89.9, gamma=84.9 degrees. Anisotropic diffraction with superior quality along a* and b* axes compared to c*. Completeness decreases with resolution from 90.6% overall to 85.9% in highest shell.


## Expression and Purification

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: Rat M3 muscarinic receptor with N-terminal FLAG epitope tag, cleavable signal sequence, four N-glycosylation site asparagine mutations (to glutamine), TEV protease site at residues 50-56, ICL3 replaced by T4 lysozyme variant (dsT4L or mT4L) between residues 259 and 482, C-terminal truncation at residue 569, His tag (6 or 8 histidines depending on construct)


### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Sf9 cell expression | Baculovirus expression in Sf9 insect cells | -- | -- + -- | Membranes prepared from transfected COS-7 cells for binding assays; Sf9 cells for purification |
| Solubilization | Membrane solubilization | -- | -- + -- | -- |
| Nickel NTA affinity chromatography | Nickel NTA affinity chromatography | Nickel NTA resin | -- + -- | First affinity purification step via C-terminal His tag |
| Anti-FLAG affinity chromatography | Anti-FLAG affinity chromatography | Anti-FLAG resin | -- + -- | Second affinity purification step via N-terminal FLAG epitope tag |
| TEV protease cleavage | TEV protease cleavage | -- | -- + -- | TEV protease cleaved N-terminal extracellular tail; cleaved constructs retained similar ligand binding affinity |
| Size exclusion chromatography | Size exclusion chromatography | Size exclusion column | -- + -- | Final purification step; monodispersity confirmed by analytical SEC |


## Crystallization

### doi/10.1016##j.str.2014.08.022

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase crystallization |
| Protein sample | M3-dsT4L bound to [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium) |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | not specified |
| Notes | M3-dsT4L crystallized in higher symmetry space group P41212 compared to P1 for original M3-wtT4L (4DAJ). Crystals were not twinned. Resolution 3.6 A, lower than original P1 structure (3.4 A). Solved by molecular replacement using wtT4L (PDB 4LZM) as search model.
 |

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase crystallization |
| Protein sample | M3-mT4L bound to [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium) |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | not specified |
| Notes | Crystals in space group C2 with block-like morphology, strongly birefringent. Data collected to 2.8 A resolution. 37 crystals used. Rwork/Rfree 23.0/26.1%. Solved by molecular replacement using M3 structure from 4DAJ and wtT4L (PDB 4LZM) or triple cysteine T4L (PDB 152L) as search models.
 |

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase crystallization |
| Protein sample | M3-mT4L bound to [NMS](/xray-mp-wiki/reagents/ligands/n-methylscopolamine) (NMS) |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | not specified |
| Notes | Same crystallization condition as [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium)-bound M3-mT4L. 12 crystals used. Resolution 3.7 A (space group C2). Rwork/Rfree 23.9/28.5%. Binding pocket interactions nearly identical to [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium)-bound structure.
 |


## Biological / Functional Insights

### T4L fusion variant optimization for GPCR crystallization

The M3 receptor was used to demonstrate that modified T4 lysozyme variants can improve crystal quality compared to wild-type T4L. The original M3-wtT4L fusion produced twinned crystals (P1 space group) requiring 70 crystals to yield a 3.4 A structure. Replacing wtT4L with dsT4L (disulfide-stabilized) yielded untwinned crystals in higher symmetry P41212 space group at 3.6 A. Replacing wtT4L with mT4L (minimal, N-terminal lobe deleted) yielded untwinned C2 crystals at 2.8 A resolution, an improvement over the wtT4L construct. The mT4L variant eliminated epitaxial twinning by providing only one T4L packing arrangement instead of two.

### Tiotropium binding mode at M3 receptor

[Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium) binds to the orthosteric pocket of the M3 muscarinic receptor with nearly identical binding mode across all three crystal structures (M3-wtT4L, M3-dsT4L, M3-mT4L). The tropane moiety occupies the central binding pocket while the tropic acid ester extends toward the extracellular side. The binding mode is conserved between [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium) and [NMS](/xray-mp-wiki/reagents/ligands/n-methylscopolamine) bound structures, confirming the orthosteric binding site.

### Crystal packing and twinning mechanism

M3-wtT4L crystals exhibit epitaxial twinning due to two different T4L packing arrangements that alternate in successive layers. The M3 receptor forms antiparallel dimers in all three constructs. In M3-wtT4L, four molecules occupy the asymmetric unit with two distinct T4L orientations. M3-dsT4L has one molecule per asymmetric unit with single T4L packing. M3-mT4L has two molecules per asymmetric unit with the receptor forming two oligomerization interfaces, positioning receptors in a linear arrangement. The smaller interface is mediated by helices 1 and 2, while a second antiparallel interface forms between helices 4 and 5.

### Molecular dynamics reveals receptor-specific dynamics

Molecular dynamics simulations comparing M2 and M3 receptors bound to [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium) revealed several key differences. Extracellular loop 2 (ECL2) is significantly more mobile in the M2 receptor than in M3, as shown by broader RMSD distributions in M2. This difference may contribute to [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium)'s slower off-rate from the M3 receptor. TM5 is more mobile in the M3 simulation, fluctuating between conformations similar to both the M3 and M2 crystal structures. [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium) loses approximately half of its hydration shell as it enters the extracellular vestibule, with similar behavior observed in both M2 and M3 simulations.

### G protein coupling interface residues

Mutagenesis studies identified key residues involved in M3-Gq coupling. S493 (6.38) is conserved in M1, M3, and M5 but not M2/M4, and forms a hydrogen bond with Y250 (5.58) in TM5. Mutation of S493 to arginine or [Glycine](/xray-mp-wiki/reagents/buffers/glycine) severely interfered with G protein signaling without affecting ligand binding. L173 in ICL2 was identified as a critical M3/Gq contact site. Homology modeling of the M3-Gq complex using the beta2AR-Gs structure as template suggests L173 binds a hydrophobic pocket on Gqalpha similar to the F139-Galphas interaction in the beta2AR complex.


## Cross-References

- [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium/) — Co-crystallized antagonist in PDB 4U14 and 4U15
- [N-methylscopolamine (NMS)](/xray-mp-wiki/reagents/ligands/n-methylscopolamine/) — Co-crystallized antagonist in PDB 4U16
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — LCP lipid matrix used for all M3 structures
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method for all M3-T4L structures
- [M1 Muscarinic Acetylcholine Receptor](/xray-mp-wiki/proteins/gpcr/m1-muscarinic-acetylcholine-receptor/) — Related muscarinic receptor GPCR; M1 and M4 structures solved in same study (Thal et al., 2016)
- [Human M2 Muscarinic Acetylcholine Receptor](/xray-mp-wiki/proteins/gpcr/m2-muscarinic-acetylcholine-receptor/) — Related muscarinic receptor GPCR; compared via MD simulations
- [Human M4 Muscarinic Acetylcholine Receptor](/xray-mp-wiki/proteins/gpcr/m4-muscarinic-acetylcholine-receptor/) — Related muscarinic receptor subtype; M4 structure solved in same study as M1 (Thal et al., 2016)
- [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine/) — Endogenous agonist tested in competition binding assays
- [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) — Buffer component used in purification
- [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) — Buffer component used in purification
