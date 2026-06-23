---
title: Lysophosphatidic Acid Receptor 1 (LPA1)
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2015.06.002]
verified: false
---

# Lysophosphatidic Acid Receptor 1 (LPA1)

## Overview

Lysophosphatidic acid receptor 1 (LPA1, also known as LPAR1 or EDG2) is a class A G protein-coupled receptor that binds lysophosphatidic acid (LPA), a bioactive lysophospholipid signaling molecule. LPA1 couples to multiple G protein pathways (Gq, Gi, G12/13) and mediates diverse physiological responses including cell proliferation, migration, and survival. Dysregulation of LPA1 signaling has been linked to cancer progression, hydrocephalus, and neuropathic pain. The first crystal structure of LPA1 revealed a spherical binding pocket and an extracellular ligand access pathway distinct from the related [Sphingosine](/xray-mp-wiki/reagents/lipids/sphingosine)-1-phosphate receptor [S1P1](/xray-mp-wiki/proteins/s1p1).

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2015.06.002 | 4Z34 | 3.0 | P212121 | Human LPA1 with bRIL fusion in ICL3 (R233, R247 positions), C-terminus truncated (38 residues removed), antagonist-bound | ONO-9780307 |
| doi/10.1016##j.cell.2015.06.002 | 4Z35 | 2.9 | P212121 | Human LPA1 with bRIL fusion in ICL3 (R233, R247 positions), C-terminus truncated (38 residues removed), antagonist-bound | ONO-9910539 |
| doi/10.1016##j.cell.2015.06.002 | 4Z36 | 2.9 | P212121 | Human LPA1 with engineered disulfide bond (D204A-V282C), mbRIL fusion in ICL3, C-terminus truncated, antagonist-bound | ONO-3080573 |

## Expression and Purification

- **Expression system**: Sf9 insect cells
- **Construct**: Human LPA1 with bRIL (b562RIL) fusion in ICL3 at Ballesteros positions 5.66 (R233) and 6.24 (R247), C-terminal truncation removing 38 residues. For ONO-3080573: dsLPA1-mbRIL with engineered disulfide between D204A and V282C, mbRIL with modified disordered loop (short linker)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and membrane preparation | Sf9 insect cell expression | -- | -- + -- | LPA1-[BRIL Fusion Protein](/xray-mp-wiki/reagents/protein-tags/bril) construct expressed in Sf9 insect cells; membranes harvested for stability assays and purification |
| Affinity chromatography | Ni-NTA affinity chromatography | Ni-NTA | -- | His-tag on [BRIL Fusion Protein](/xray-mp-wiki/reagents/protein-tags/bril) fusion partner used for affinity capture |
| Size-exclusion chromatography | [Size-exclusion chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | SEC column | -- | Analytical SEC used for stability screening in place of CPM assay; SEC stability assays guided compound selection |


## Crystallization

### doi/10.1016##j.cell.2015.06.002

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | LPA1-[BRIL Fusion Protein](/xray-mp-wiki/reagents/protein-tags/bril) co-crystallized with [ONO-9780307](/xray-mp-wiki/reagents/ligands/ono-9780307) or [ONO-9910539](/xray-mp-wiki/reagents/ligands/ono-9910539) |
| Temperature | not specified in main text |
| Growth time | not specified in main text |
| Cryoprotection | not specified in main text |
| Notes | Crystals grown in [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein)-[Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) LCP mixture. [ONO-9780307](/xray-mp-wiki/reagents/ligands/ono-9780307): 86 crystals, 3.0 A resolution. [ONO-9910539](/xray-mp-wiki/reagents/ligands/ono-9910539): 53 crystals, 2.9 A resolution. P212121 space group. |

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | dsLPA1-mbRIL co-crystallized with [ONO-3080573](/xray-mp-wiki/reagents/ligands/ono-3080573) |
| Temperature | not specified in main text |
| Growth time | not specified in main text |
| Cryoprotection | not specified in main text |
| Notes | Disulfide-engineered construct (D204A-V282C) with modified mbRIL fusion. 39 crystals, 2.9 A resolution. P212121 space group. |


## Biological / Functional Insights

### Spherical binding pocket with extracellular ligand access

The LPA1 binding pocket is spherical in nature, contrasting with the more linear binding pocket of [S1P1](/xray-mp-wiki/proteins/s1p1). The position of TM1 in LPA1 is shifted 3 A closer to TM7 compared to [S1P1](/xray-mp-wiki/proteins/s1p1), closing the gap that was postulated to enable membrane-embedded ligand access for [S1P1](/xray-mp-wiki/proteins/s1p1). Molecular dynamics simulations over 100 ns confirmed that the distance between TM1 and TM7 is consistently smaller and less variable in LPA1 than in [S1P1](/xray-mp-wiki/proteins/s1p1), with a difference of approximately 7 A at the extracellular tip in the absence of ligand. This structural feature suggests LPA1 preferentially receives ligands from the extracellular milieu rather than via the membrane, consistent with the biological existence of albumin-bound LPA and the delivery of LPA by autotaxin.

### Key binding pocket residues and antagonist interactions

The carboxylic acid of [ONO-9780307](/xray-mp-wiki/reagents/ligands/ono-9780307) interacts through polar and ionic bonds with His40, Lys39, and Tyr34 on the N-terminal capping helix and ECL0 loop. Arg124(3.28) and Gln125(3.29) on TM3 form ionic and polar interactions with the carboxylic acid and chiral hydroxyl group. Glu293(7.35) from TM7 stabilizes Lys39. The enhanced polar environment on TM3 and TM5 includes Asp129(3.33) on TM3 and Trp210(5.43) on TM5, which presents its indole nitrogen for hydrogen bonding. His40 is unique to LPA1 among the LPA receptor family and may be important for high-affinity antagonist binding. Calculations show protonated His40 increases binding affinity by more than 1 kcal/mol.

### Torsionally strained bioactive ligand conformation

The bioactive conformation of [ONO-9780307](/xray-mp-wiki/reagents/ligands/ono-9780307) requires a strained eclipsed torsion angle on the bond adjacent to the indane ring, with a difference of 9.6 kcal/mol between the observed conformation and the local energy minimum. The ligand positions its branching aromatic indane and dimethoxy phenyl rings adjacent to each other in the spherical binding pocket. The local energy minimum conformation is not able to bind due to projected clashes with TM6. This torsional strain was alleviated in [ONO-3080573](/xray-mp-wiki/reagents/ligands/ono-3080573) by replacing the methylene linker with an ether linkage.

### Ligand access path divergence between LPA1 and S1P1

Three key amino acid differences between LPA1 and [S1P1](/xray-mp-wiki/proteins/s1p1) account for the distinct pocket shapes: position 3.33 is aspartate in LPA1 versus phenylalanine in [S1P1](/xray-mp-wiki/proteins/s1p1); position 5.43 is tryptophan in LPA1 versus cysteine in [S1P1](/xray-mp-wiki/proteins/s1p1); position 6.51 is [Glycine](/xray-mp-wiki/reagents/buffers/glycine) in LPA1 versus leucine in [S1P1](/xray-mp-wiki/proteins/s1p1). The reduction in side chain bulk at position 6.51 opens a sub-pocket occupied by the indane ring of the antagonist series. The configuration of the extracellular region in LPA1 is constrained by two intraloop disulfide bonds in ECL2 and ECL3, and a disulfide bond connecting ECL2 with the N terminus.

### Promiscuous recognition of phosphorylated endocannabinoids

Molecular modeling predicted that the LPA1 binding pocket can accommodate phosphorylated endocannabinoids 2-ALPA (2-arachidonoyl-LPA) and pAEA (phosphorylated anandamide), which are generated through enzymatic action from endogenous cannabinoids. Cell-based assays confirmed that all phosphorylated ligands produced robust signaling via calcium response and cAMP inhibition in LPA1-expressing cells. A neurite retraction assay showed robust activation by pAEA, involving Rho GTPase activation and F-actin stress fiber formation. This links the LPA and cannabinoid receptor systems through metabolically related ligands with potential functional and therapeutic implications.

### Structure-based design of improved antagonists

Three antagonists were designed through structure-based approaches. [ONO-9910539](/xray-mp-wiki/reagents/ligands/ono-9910539) features an acetyl group in the para position of the phenyl ring for enhanced polar interactions with Trp210(5.43) and reduced lipophilicity. [ONO-3080573](/xray-mp-wiki/reagents/ligands/ono-3080573) replaced the methylene linker with an ether linkage to reduce torsional strain and substituted the metabolically labile pyrrole ring with a phenyl ring for improved metabolic stability, differentially positioning the carboxylic acid to gain interaction with Lys294(7.36) while breaking interactions with Arg124(3.28), His40, and Tyr34.


## Cross-References

- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Primary lipid component for LCP crystallization matrix
- [bRIL Fusion Protein](/xray-mp-wiki/reagents/protein-tags/bril/) — bRIL fusion in ICL3 used for crystallization of LPA1
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used for all three LPA1 structures
- [Sphingosine-1-Phosphate Receptor 1 (S1P1)](/xray-mp-wiki/proteins/gpcr/s1p1/) — Closest structural and functional homolog, major comparison throughout the paper
- [ONO-9780307](/xray-mp-wiki/reagents/ligands/ono-9780307/) — Co-crystallized antagonist for PDB 4Z34
- [ONO-9910539](/xray-mp-wiki/reagents/ligands/ono-9910539/) — Co-crystallized antagonist for PDB 4Z35
- [ONO-3080573](/xray-mp-wiki/reagents/ligands/ono-3080573/) — Co-crystallized antagonist for PDB 4Z36
- [2-AG (2-Arachidonoylglycerol)](/xray-mp-wiki/reagents/ligands/2-ag/) — Endogenous cannabinoid agonist; phosphorylated form 2-ALPA activates LPA1
- [Sphingosine](/xray-mp-wiki/reagents/lipids/sphingosine/) — Lipid component used in crystallization or solubilization
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid component used in crystallization or solubilization
