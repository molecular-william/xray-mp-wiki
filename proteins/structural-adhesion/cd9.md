---
title: CD9 (Tetraspanin)
created: 2026-06-09
updated: 2026-06-09
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-020-15459-7]
verified: false
---

# CD9 (Tetraspanin)

## Overview

CD9 is a member of the tetraspanin family, a class of four-transmembrane domain proteins that play critical roles in cell adhesion, migration, fertilization, and viral infection. The crystal structure of human CD9 was determined at 2.7 A resolution using the SIRAS method from crystals grown in lipidic cubic phase. The structure reveals a reversed cone-like molecular shape with four transmembrane helices arranged in a teepee-like configuration, creating a large central cavity in the intramembranous region. A [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) structure of CD9 in complex with its partner protein EWI-2 at 7.3 A resolution reveals a 2:2 hetero-tetrameric stoichiometry, with the TM3-4 region of CD9 interacting with the membrane-spanning helix of EWI-2 through small residue contacts (Gly/Ala zipper motif). MD simulations show spontaneous transitions between open and closed conformations of the extracellular loops. The asymmetric molecular shape generates membrane curvature, explaining CD9 localization in microvilli and exosomes. Fertilization assays demonstrate that the large extracellular loop (LEL) is critical for sperm-egg fusion.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-020-15459-7 | Not deposited (crystal structure) | 2.7 A | — | Human CD9 with partial LEL deletion (Thr175-Lys179) and C-terminal tail deletion (Glu226-Val228) |  |
| doi/10.1038##s41467-020-15459-7 | Not deposited (cryo-EM structure) | 7.3 A | — | Full-length CD9 + EWI-2 + anti-CD9 Fab |  |

## Expression and Purification

- **Expression system**: HEK293S GnTI- (BacMam)
- **Construct**: Human wild-type CD9 with N-terminal His6-GFP tag and TEV cleavage site

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane solubilization | Detergent solubilization | — | 10 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.0, 150 mM NaCl + 1.5% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.3% (w/v) CHS | Membrane fractions solubilized for 1 h, insoluble material removed by ultracentrifugation |
| Affinity chromatography | Metal affinity chromatography | [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon/) Metal Affinity Resin | 10 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.0, 150 mM NaCl, 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.02% CHS, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (wash), 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (elution) | His6-GFP tag cleaved by TEV protease during dialysis |
| Reverse affinity chromatography | Ni-NTA subtractive step | Ni-NTA Superflow | 10 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.0, 150 mM NaCl, 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.02% CHS | Removes His6-GFP tag and TEV protease |
| Size-exclusion chromatography | Gel filtration | Superdex 200 Increase 10/300 GL | 10 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.0, 150 mM NaCl, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% CHS | Concentrated to ~15 mg/mL for crystallization |


## Crystallization

### doi/10.1038##s41467-020-15459-7

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | Purified CD9 at ~15 mg/ml mixed with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) (2:3 protein:lipid ratio) |
| Temperature | 20 C |
| Growth time | Up to 3 weeks |
| Notes | [Mercury (HgCl2) - Aquaporin Inhibitor](/xray-mp-wiki/reagents/additives/mercury/) derivative co-crystallized with 2 mM CH3HgCl for SIRAS phasing. Crystals collected and flash-cooled in liquid nitrogen. |


## Biological / Functional Insights

### Reversed cone-like molecular shape generates membrane curvature

CD9 adopts a reversed cone-like shape with the four TM helices bundled tightly at the intracellular side and loosely packed at the extracellular side, creating a large central cavity. This asymmetric shape generates membrane curvature in crystalline lipid layers of LCP, explaining CD9 localization in regions of high membrane curvature such as microvilli tips and exosomes.

### TM region and LEL provide multi-platform binding interface

The CD9-EWI-2 complex reveals that CD9 associates with partner proteins through two distinct interfaces: the TM3-4 region interacting with the EWI-2 membrane-spanning helix via small residue (Gly/Ala) contacts, and the large extracellular loop (LEL) which adopts an open conformation to contact the juxta-membrane Ig-like domain of EWI-2. Fertilization assays show that the LEL is critical for sperm-egg fusion, while the TM region is sufficient for EWI-2 association, demonstrating different functional dependencies for different partner proteins.

### Dynamic SEL-LEL gating

MD simulations (100 microsecond reconstructed trajectory) reveal spontaneous transitions between closed, semi-open, and open conformations of the short extracellular loop (SEL) and large extracellular loop (LEL). Unlike [Human CD81 Tetraspanin](/xray-mp-wiki/proteins/structural-adhesion/cd81/), CD9 transitions between conformations even in the absence of [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) binding, suggesting a more dynamic extracellular interface.

### Central cavity accommodates lipid molecules

The central cavity in the intramembranous region is rendered hydrophilic by conserved residues Asn18 and Glu103. An unassigned electron density within the cavity likely corresponds to [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) or endogenous lipid molecules, suggesting regulatory roles of lipids in CD9 function. The [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/)-binding residue Glu219 found in [Human CD81 Tetraspanin](/xray-mp-wiki/proteins/structural-adhesion/cd81/) is replaced by Gly210 in CD9.


## Cross-References

- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used for CD9 crystal structure determination
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Used for LCP crystallization of CD9
- [DDM (n-Dodecyl-beta-D-Maltopyranoside)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary solubilization and purification detergent
- [Cholesteryl Hemisuccinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Used as additive during purification for stability
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Used throughout purification and crystallization
- [GR (Halobacterium sp. GR Bacteriorhodopsin)](/xray-mp-wiki/proteins/rhodopsins/gr/) — Related protein structure
- [ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel)](/xray-mp-wiki/proteins/cys-loop-receptors/elic/) — Related protein structure
- [Human CD81 Tetraspanin](/xray-mp-wiki/proteins/structural-adhesion/cd81/) — Related protein structure
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid component
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Method used in the study
