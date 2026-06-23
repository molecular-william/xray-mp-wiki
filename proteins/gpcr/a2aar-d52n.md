---
title: Human Adenosine A2A Receptor D52N Variant (A2AAR-D52N)
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2017.12.013]
verified: false
---

# Human Adenosine A2A Receptor D52N Variant (A2AAR-D52N)

## Overview

The human [A2AAR](/xray-mp-wiki/proteins/human-adenosine-a2a-receptor-a2ar) D52N variant (A2AAR-D52N) is a point mutant of the A2AR in which aspartate 52 (D52) in transmembrane helix II is replaced by asparagine. This mutation disrupts the allosteric sodium binding site and confers enhanced thermal stability, making it a valuable tool for GPCR crystallization and drug discovery. The structure reveals changes in the hydrogen bonding network near the activation microswitch NPxxY, providing structural insight into how sodium coordination regulates G-protein signaling.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2017.12.013 | 5WF5 | 2.60 A | P21 | A2AAR-T4L D52N variant truncated after residue 316, N-terminal FLAG tag, C-terminal His10 tag, K209-A221 replaced by cysteine-free [T4 Lysozyme](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme) (C54T, C97A) | [UK432097](/xray-mp-wiki/reagents/ligands/uk432097) |

## Expression and Purification

- **Expression system**: Sf9 insect cells ([Baculovirus Expression](/xray-mp-wiki/methods/expression-systems/baculovirus-expression))
- **Construct**: A2AAR-T4L D52N variant with N-terminal FLAG tag, C-terminal His10 tag, truncated after residue 316, K209-A221 replaced by cysteine-free [T4 Lysozyme](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme) (C54T, C97A)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| [Baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression) expression | Sf9 cell infection with high-titer recombinant [Baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression) | -- | ESF 921 media + -- | [Bac-to-Bac](/xray-mp-wiki/methods/expression-systems/bac-to-bac) system (Invitrogen) |
| Membrane preparation | Sf9 membrane harvest; membranes washed in hypotonic buffer then high osmotic buffer | -- | 10 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.0, 10 mM MgCl2, 20 mM KCl, protease inhibitors + -- | Membranes resuspended in buffer with [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide) and theophylline |
| Solubilization | Membranes solubilized with detergent in presence of ligand | -- | -- + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Solubilized with DDM in presence of 4 mM [Theophylline](/xray-mp-wiki/reagents/ligands/theophylline) |
| [IMAC](/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography) | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta) affinity purification using His10 tag | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta) | -- + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | His10 tag on C-terminus used for affinity capture |
| [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) for final polishing | -- | -- + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Final sample prepared for crystallization |


## Crystallization

### doi/10.1016##j.str.2017.12.013

| Parameter | Value |
|---|---|
| Method | [Lipidic Cubic Phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) (LCP) crystallization |
| Protein sample | A2AAR-T4L D52N in complex with [UK432097](/xray-mp-wiki/reagents/ligands/uk432097) (40% w/w protein solution) |
| Lipid | Monoolein (40% protein + 54% monoolein + 6% [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol)) |
| Protein-to-lipid ratio | 40:60 (w/w) |
| Temperature | 23 C |
| Growth time | Crystals appeared in ~1 hour, full size within one week |
| Cryoprotection | Flash frozen in liquid nitrogen |
| Notes | 24 crystals merged. Data collected on 23ID-D beamline at APS using Pilatus3-6M detector. 92.3% complete dataset at 2.6 A resolution. Solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement) using A2AAR-ZM241385 (PDB 3EML) as search model in Phaser. |


## Biological / Functional Insights

### Disruption of allosteric sodium binding site

The D52N mutation replaces the negatively charged aspartate at position 2.50 with a neutral asparagine, abolishing sodium coordination at the allosteric sodium site. This disrupts sodium-dependent G-protein signaling while maintaining ligand binding affinity. The D52N variant shows striking loss of G-protein signaling, confirming the critical role of D2.50 in sodium-mediated allosteric modulation of class A GPCRs.

### Enhanced thermal stability

The [A2AAR](/xray-mp-wiki/proteins/human-adenosine-a2a-receptor-a2ar)-D52N variant shows significantly increased thermal stability compared to wild-type A2AAR. Apo A2AAR-D52N showed a nearly 8 C increase in melting temperature compared to apo A2AAR. This enhanced stability is attributed to new hydrogen bonds formed by N52 with residues in helices II, III, and VII, which stabilize the receptor across a range of ligand complexes. The D52N mutation is proposed as a general strategy for stabilizing class A GPCRs for crystallization and drug discovery.

### Changes in NPxxY activation microswitch

Structural comparison reveals key changes in the hydrogen bonding network near the [NPxxY Motif](/xray-mp-wiki/concepts/npxxy-motif) in helix VII. The D52N mutation causes local conformational changes in the NPxxY motif that suggest coupling between the sodium site (D2.50) and the activation microswitch. These changes are consistent with the loss of G-protein signaling and provide structural insight into how sodium coordination regulates signal propagation from the orthosteric ligand binding site to the intracellular surface.

### Hydrogen bond network rearrangement

The D52N mutation introduces new hydrogen bonds between N52 and residues in helices II, III, and VII. These new interactions alter the interhelical packing near the activation microswitch. In contrast, the D52A mutation (aspartate to alanine) does not form these hydrogen bonds and shows markedly lower thermal stability, confirming that the asparagine side chain is critical for the stabilizing effect.


## Cross-References

- [Human Adenosine A2A Receptor (A2AR)](/xray-mp-wiki/proteins/gpcr/human-adenosine-a2a-receptor-a2ar/) — [A2AAR](/xray-mp-wiki/proteins/human-adenosine-a2a-receptor-a2ar)-D52N is a point mutant of the wild-type A2AR
- [Human Adenosine A2A Receptor S91A Variant (A2AAR-S91A)](/xray-mp-wiki/proteins/gpcr/a2aar-s91a/) — Another sodium-site variant solved in the same study
- [LJ-4517 (Compound 2)](/xray-mp-wiki/reagents/ligands/lj-4517/) — Nucleoside antagonist for comparison with nucleoside agonist [UK432097](/xray-mp-wiki/reagents/ligands/uk432097)
- [UK432097](/xray-mp-wiki/reagents/ligands/uk-432097/) — Full agonist co-crystallized with [A2AAR](/xray-mp-wiki/proteins/human-adenosine-a2a-receptor-a2ar)-D52N (PDB 5WF5)
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for solubilization and purification
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid component of [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) crystallization medium
- [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) — Added to [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) mixture for membrane protein stability
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method used for structure determination
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement) using Phaser
- [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression) — Expression system used for protein production
