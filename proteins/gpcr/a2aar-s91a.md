---
title: Human Adenosine A2A Receptor S91A Variant (A2AAR-S91A)
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2017.12.013]
verified: false
---

# Human Adenosine A2A Receptor S91A Variant (A2AAR-S91A)

## Overview

The human [A2AAR](/xray-mp-wiki/proteins/human-adenosine-a2a-receptor-a2ar) S91A variant (A2AAR-S91A) is a point mutant of the A2AR in which serine 91 (S91) in transmembrane helix III is replaced by alanine. This residue is one of two residues in the first sodium coordination shell of the allosteric sodium binding site. The structure reveals an overall active-like conformation with key changes in the activation motif NPxxY, providing structural insight into the role of sodium-coordinating residues in GPCR signaling.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2017.12.013 | 5WF6 | 2.90 A | P21 | A2AAR-T4L S91A variant truncated after residue 316, N-terminal FLAG tag, C-terminal His10 tag, K209-A221 replaced by cysteine-free [T4 Lysozyme](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme) (C54T, C97A) | [UK432097](/xray-mp-wiki/reagents/ligands/uk432097) |

## Expression and Purification

- **Expression system**: Sf9 insect cells ([Baculovirus Expression](/xray-mp-wiki/methods/expression-systems/baculovirus-expression))
- **Construct**: A2AAR-T4L S91A variant with N-terminal FLAG tag, C-terminal His10 tag, truncated after residue 316, K209-A221 replaced by cysteine-free [T4 Lysozyme](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme) (C54T, C97A)

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
| Protein sample | A2AAR-T4L S91A in complex with [UK432097](/xray-mp-wiki/reagents/ligands/uk432097) (40% w/w protein solution) |
| Lipid | Monoolein (40% protein + 54% monoolein + 6% [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol)) |
| Protein-to-lipid ratio | 40:60 (w/w) |
| Temperature | 23 C |
| Growth time | Crystals appeared in ~1 hour, full size within one week |
| Cryoprotection | Flash frozen in liquid nitrogen |
| Notes | 25 crystals merged. Data collected on 23ID-D beamline at APS using Pilatus3-6M detector. 91.9% complete dataset at 2.9 A resolution. Solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement) using A2AAR-ZM241385 (PDB 3EML) as search model in Phaser. |


## Biological / Functional Insights

### S91A variant in active-like conformation

The S91A mutation replaces serine 91 in the first sodium coordination shell with alanine. The resulting structure presents an overall active-like conformation with key changes in the activation motif NPxxY. The rotamer position of S281(7.46) differs from the D52N variant, and the electron density maps were more ambiguous in the [NPxxY Motif](/xray-mp-wiki/concepts/npxxy-motif) region compared to D52N.

### Comparison with D52N variant

The two most significant differences between the D52N and S91A structures are the rotamer position of S281(7.46) and differences in C-alpha positions of residues in the [NPxxY Motif](/xray-mp-wiki/concepts/npxxy-motif). The S91A mutation also disrupts the allosteric sodium binding site but preserves partial G-protein signaling activity, unlike the D52N variant which shows striking loss of signaling.

### Role of S91 in sodium coordination

In the high-resolution antagonist-bound [A2AAR](/xray-mp-wiki/proteins/human-adenosine-a2a-receptor-a2ar) structure, S91(3.39) and D52(2.50) were the only two residues observed to directly coordinate the sodium ion. The S91A mutation demonstrates that while S91 contributes to sodium coordination, its removal has a less severe effect on signaling than removal of D52, suggesting D52 plays a more critical role in sodium-mediated allosteric modulation.


## Cross-References

- [Human Adenosine A2A Receptor (A2AR)](/xray-mp-wiki/proteins/gpcr/human-adenosine-a2a-receptor-a2ar/) — [A2AAR](/xray-mp-wiki/proteins/human-adenosine-a2a-receptor-a2ar)-S91A is a point mutant of the wild-type A2AR
- [Human Adenosine A2A Receptor D52N Variant (A2AAR-D52N)](/xray-mp-wiki/proteins/gpcr/a2aar-d52n/) — Sodium-site variant solved in the same study with PDB 5WF5
- [LJ-4517 (Compound 2)](/xray-mp-wiki/reagents/ligands/lj-4517/) — Nucleoside antagonist for comparison with nucleoside agonist [UK432097](/xray-mp-wiki/reagents/ligands/uk432097)
- [UK432097](/xray-mp-wiki/reagents/ligands/uk-432097/) — Full agonist co-crystallized with [A2AAR](/xray-mp-wiki/proteins/human-adenosine-a2a-receptor-a2ar)-S91A (PDB 5WF6)
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for solubilization and purification
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid component of [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) crystallization medium
- [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) — Added to [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) mixture for membrane protein stability
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method used for structure determination
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement) using Phaser
- [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression) — Expression system used for protein production
