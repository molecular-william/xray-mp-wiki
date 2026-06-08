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

The human adenosine A2A receptor S91A variant (A2AAR-S91A) is a point mutant of the A2AR in which serine 91 (S91) in transmembrane helix III is replaced by alanine. This residue is one of two residues in the first sodium coordination shell of the allosteric sodium binding site. The structure reveals an overall active-like conformation with key changes in the activation motif NPxxY, providing structural insight into the role of sodium-coordinating residues in GPCR signaling.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2017.12.013 | 5WF6 | 2.90 A | P21 | A2AAR-T4L S91A variant truncated after residue 316, N-terminal FLAG tag, C-terminal His10 tag, K209-A221 replaced by cysteine-free T4 lysozyme (C54T, C97A) | UK432097 |

## Expression and Purification

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: A2AAR-T4L S91A variant with N-terminal FLAG tag, C-terminal His10 tag, truncated after residue 316, K209-A221 replaced by cysteine-free T4 lysozyme (C54T, C97A)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Baculovirus expression | Sf9 cell infection with high-titer recombinant baculovirus | -- | ESF 921 media + -- | Bac-to-Bac system (Invitrogen) |
| Membrane preparation | Sf9 membrane harvest; membranes washed in hypotonic buffer then high osmotic buffer | -- | 10 mM HEPES pH 7.0, 10 mM MgCl2, 20 mM KCl, protease inhibitors + -- | Membranes resuspended in buffer with iodoacetamide and theophylline |
| Solubilization | Membranes solubilized with detergent in presence of ligand | -- | -- + DDM | Solubilized with DDM in presence of 4 mM theophylline |
| Ni-NTA affinity chromatography | Ni-NTA affinity purification using His10 tag | Ni-NTA | -- + DDM | His10 tag on C-terminus used for affinity capture |
| Size-exclusion chromatography | SEC for final polishing | -- | -- + DDM | Final sample prepared for crystallization |


## Crystallization

### doi/10.1016##j.str.2017.12.013

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | A2AAR-T4L S91A in complex with UK432097 (40% w/w protein solution) |
| Lipid | Monoolein (40% protein + 54% monoolein + 6% cholesterol) |
| Protein-to-lipid ratio | 40:60 (w/w) |
| Temperature | 23 C |
| Growth time | Crystals appeared in ~1 hour, full size within one week |
| Cryoprotection | Flash frozen in liquid nitrogen |
| Notes | 25 crystals merged. Data collected on 23ID-D beamline at APS using Pilatus3-6M detector. 91.9% complete dataset at 2.9 A resolution. Solved by molecular replacement using A2AAR-ZM241385 (PDB 3EML) as search model in Phaser. |


## Biological / Functional Insights

### S91A variant in active-like conformation

The S91A mutation replaces serine 91 in the first sodium coordination shell with alanine. The resulting structure presents an overall active-like conformation with key changes in the activation motif NPxxY. The rotamer position of S281(7.46) differs from the D52N variant, and the electron density maps were more ambiguous in the NPxxY motif region compared to D52N.

### Comparison with D52N variant

The two most significant differences between the D52N and S91A structures are the rotamer position of S281(7.46) and differences in C-alpha positions of residues in the NPxxY motif. The S91A mutation also disrupts the allosteric sodium binding site but preserves partial G-protein signaling activity, unlike the D52N variant which shows striking loss of signaling.

### Role of S91 in sodium coordination

In the high-resolution antagonist-bound A2AAR structure, S91(3.39) and D52(2.50) were the only two residues observed to directly coordinate the sodium ion. The S91A mutation demonstrates that while S91 contributes to sodium coordination, its removal has a less severe effect on signaling than removal of D52, suggesting D52 plays a more critical role in sodium-mediated allosteric modulation.


## Cross-References

- [Human Adenosine A2A Receptor (A2AR)](/xray-mp-wiki/proteins/human-adenosine-a2a-receptor-a2ar/) — A2AAR-S91A is a point mutant of the wild-type A2AR
- [Human Adenosine A2A Receptor D52N Variant (A2AAR-D52N)](/xray-mp-wiki/proteins/a2aar-d52n/) — Sodium-site variant solved in the same study with PDB 5WF5
- [LJ-4517 (Compound 2)](/xray-mp-wiki/reagents/ligands/lj-4517/) — Nucleoside antagonist for comparison with nucleoside agonist UK432097
- [UK432097](/xray-mp-wiki/reagents/ligands/uk432097/) — Full agonist co-crystallized with A2AAR-S91A (PDB 5WF6)
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for solubilization and purification
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid component of LCP crystallization medium
- [Cholesterol](/xray-mp-wiki/reagents/additives/cholesterol/) — Added to LCP mixture for membrane protein stability
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method used for structure determination
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Structure solved by molecular replacement using Phaser
