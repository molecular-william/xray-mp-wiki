---
title: Human M5 Muscarinic Acetylcholine Receptor
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1914446116]
verified: false
---

# Human M5 Muscarinic Acetylcholine Receptor

## Overview

The human M5 muscarinic [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine/) receptor (M5 mAChR) is a class A G protein-coupled receptor that preferentially couples to Gq/11 proteins. It represents less than 2% of total muscarinic receptor expression in the brain but is found predominantly in the central nervous system, where it has recently emerged as an exciting therapeutic target for treating disorders including drug addiction. The first high-resolution crystal structure of the M5 mAChR was determined bound to the clinically used inverse agonist [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium/) at 3.4 A resolution, using a T4 lysozyme ([T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/)) fusion construct with the thermostabilizing S117(3.39)R mutation. This structure enabled complete structural comparison across all five mAChR family members (M1-M5), revealing differences in extracellular loop (ECL) regions that mediate orthosteric and allosteric ligand selectivity. A ternary complex structure with the bis-ammonium alkane modulator 4B-C7/3-phth was also determined at 2.55 A. Chimeric swaps between M2 and M5 ECL regions provided structural insight into kinetic selectivity, where ligands show differential residency times between related family members.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1914446116 | 6OL9 | 3.4 A | Not specified | Human M5 muscarinic receptor with T4 lysozyme fusion (residues 225-430 of ICL3 replaced by [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/)), S117(3.39)R thermostabilizing mutation, N-terminal 20 amino acids cleaved by TEV protease site, bound to [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium/)
 | [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium/) |
| doi/10.1073##pnas.1914446116 | Not specified | 2.55 A | Not specified | Human M5 muscarinic receptor with T4 lysozyme fusion, S117(3.39)R mutation, ternary complex with [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium/) and bis-ammonium alkane modulator 4B-C7/3-phth
 | [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium/), 4B-C7/3-phth |

## Expression and Purification

- **Expression system**: Not specified in source paper (standard baculovirus/Sf9 insect cell system as previously described for M3-M4 receptors)
- **Construct**: M5-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) with S117(3.39)R mutation. ICL3 residues 225-430 removed and replaced with T4 lysozyme fusion. N-terminal TEV protease site for removal of first 20 amino acids.


### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Receptor expression and purification | M5-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) with S117(3.39)R purified similarly to previous methods for M3 receptor | Not specified | Not specified + Not specified | S117(3.39)R mutation increased receptor yields during purification and resulted in crystals diffracting to 3.4 A. |


## Crystallization

### doi/10.1073##pnas.1914446116

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | M5-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) S117(3.39)R bound to [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium/), reconstituted into 10:1 (wt/wt) [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/):[Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) in 1:1.5 wt/wt protein:lipid ratio
 |
| Temperature | 20 degrees Celsius |
| Growth time | Crystals appeared within 24 hours and grew to full size in 1-2 days |
| Cryoprotection | Whole drops harvested using mesh grid loops and flash-frozen in liquid nitrogen |
| Notes | For allosteric modulator cocrystallization, 2.5 mM modulator was added to purified protein and incubated on ice for 3 hours before LCP reconstitution. The ternary complex with 4B-C7/3-phth yielded crystals that grew to much larger size and diffracted to 2.55 A. Data collected at SPring-8 beamline BL32XU and Australian Synchrotron MX2 beamline. Structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using M5-mTAL (PDB 4U15) as search model for receptor and [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) ensemble for T4 lysozyme. Refinement performed with Phenix.
 |


## Biological / Functional Insights

### Complete structural comparison of all five mAChR subtypes

The M5 structure completed the structural coverage of all five muscarinic receptor subtypes (M1-M5). The orthosteric binding pocket residues are absolutely conserved across all five subtypes. However, subtle differences in the extracellular loops (ECL2 and ECL3) are observed, with ECL2 showing a 1.8 A difference beginning at the first nonconserved residue. The ECL2 3-10 helix motif moves inward by 2.8 A in M5 compared to M1, and the conserved ECL3 disulphide bond is displaced inward by 3.1 A for M3 and M5. These ECL differences are the major determinants of subtype selectivity for both orthosteric and allosteric ligands.

### Kinetic selectivity through ECL chimeric swaps

The M2 receptor has a shorter half-life for [3H][NMS](/xray-mp-wiki/reagents/ligands/n-methylscopolamine/) dissociation than M5. Chimeric swaps of ECL1, ECL2, and ECL3 between M2 and M5 receptors revealed that ECL1 has the largest effect on dissociation kinetics. R95(ECL1) in M5 is a conserved Tyr in M1-M4 subtypes and can form an ionic bond with M5 ECL2 residue D181(-2), potentially tethering ECL1 and ECL2 and limiting dynamics to reduce orthosteric ligand dissociation rates. The bis-ammonium alkane allosteric modulators (ML375, 4P-C7/3-phth) showed differential effects on [NMS](/xray-mp-wiki/reagents/ligands/n-methylscopolamine/) dissociation across the chimeras.

### Extracellular vestibule differences between M2 and M5

Comparison of the M2 and M5 extracellular vestibules (ECV) revealed major differences in nonconserved residues lining the top of TM6 starting from S465(6.58) across ECL3 and down to H478(7.36) in TM7. In the M5 receptor, these residues are bulkier and point more inwardly, constricting the overall size of the ECV. The allosteric modulator binding site at the ECV shows subtype-specific features that can be exploited for selective drug design.


## Cross-References

- [M1 Muscarinic Acetylcholine Receptor](/xray-mp-wiki/proteins/gpcr/m1-muscarinic-acetylcholine-receptor/) — Related muscarinic receptor subtype; compared in M5 structural study
- [Human M2 Muscarinic Acetylcholine Receptor](/xray-mp-wiki/proteins/gpcr/m2-muscarinic-acetylcholine-receptor/) — Related muscarinic receptor subtype; used for ECL chimeric swaps and kinetic selectivity studies
- [M3 Muscarinic Acetylcholine Receptor](/xray-mp-wiki/proteins/gpcr/m3-muscarinic-acetylcholine-receptor/) — Related muscarinic receptor subtype; M5 structure solved using M3-mTAL (PDB 4U15) as molecular replacement search model
- [Human M4 Muscarinic Acetylcholine Receptor](/xray-mp-wiki/proteins/gpcr/m4-muscarinic-acetylcholine-receptor/) — Related muscarinic receptor subtype; compared in M5 structural study
- [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium/) — Inverse agonist co-crystallized with M5 receptor (PDB 6OL9)
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method for M5 structure determination
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [Ammonium Tartrate](/xray-mp-wiki/reagents/additives/ammonium-tartrate/) — Additive used in purification or crystallization buffers
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine/) — Related ligand or cofactor
