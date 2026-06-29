---
title: "Human Adenosine A1 Receptor (A1AR)"
created: 2026-05-27
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2017.01.042, doi/10.1016##j.str.2017.06.012]
verified: false
---

# Human Adenosine A1 Receptor (A1AR)

## Overview

The human adenosine A1 receptor (A1AR) is a class A G protein-coupled receptor that plays a vital role in cardiac, renal, and neuronal processes. Structures have been solved for the A1AR bound to the selective covalent antagonist DU172 (3.2 A) and the thermostabilized A1R-StaR construct bound to the A1-selective xanthine antagonist PSB36 (3.3 A), revealing key determinants of ligand subtype selectivity.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2017.01.042 | 5UEN | 3.2 A | P1 | Human A1AR with M4 N-terminus insertion, BRIL fusion in ICL3, N159A mutation, C-terminal truncation after residue 311 with 3C protease site | DU172 |
| doi/10.1016##j.str.2017.06.012 | -- | 3.3 A | C22222 | Human A1R-StaR-Delta3-b562RIL thermostabilized mutant (A57L, T91A, Y205A, L236A, L240A, T277A) with C-terminal truncation, b562RIL fusion | PSB36 |

## Expression and Purification

- **Expression system**: Sf9 insect cells (baculovirus) for DU172 structure; Sf9 insect cells for StaR structure
- **Construct**: Human A1AR constructs: (1) A1AR with M4 N-terminus insertion, BRIL fusion in ICL3, N159A mutation, C-terminal truncation; (2) A1R-StaR-Delta3-b562RIL thermostabilized mutant with mutations A57L(2.52), T91A(3.36), Y205A(5.63), L236A(6.37), L240A(6.41), T277A(7.42)
- **Notes**: For DU172 structure: High-titer recombinant baculovirus used to infect Sf9 cells; cells harvested 48 hr post-infection; construct had 22 aa M4 muscarinic receptor N-terminus with N-glycosylation sites and 3C protease site; BRIL inserted in ICL3 between residues 211-220; N159A mutation; C-terminal truncation after residue 311 with 3C protease site

### Purification Workflow

#### Source: doi/10.1016##j.cell.2017.01.042


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression and membrane preparation | Baculovirus expression in Sf9 insect cells; cells harvested 48 hr post-infection, membranes prepared by homogenization and ultracentrifugation | — | 10 mM HEPES pH 7.5, 150 mM NaCl, protease inhibitors + -- | DU172 (0.2 uM) added to membranes before solubilization |
| Solubilization | Detergent solubilization | -- | 10 mM HEPES pH 7.5, 150 mM NaCl + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.2% sodium cholate, 0.2% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Solubilized for 2 hr at 4C in presence of 0.2 uM DU172 |
| TALON IMAC | Immobilized metal [affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [TALON](/xray-mp-wiki/reagents/additives/talon/) IMAC resin | 10 mM HEPES pH 7.5, 150 mM NaCl, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% sodium cholate, 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 50 mM imidazole + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% sodium cholate, 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Eluted with 200 mM imidazole; 0.2 uM DU172 present throughout |
| Anti-Flag M1 affinity | Anti-[FLAG](/xray-mp-wiki/reagents/protein-tags/flag-tag/) M1 [affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Anti-[FLAG](/xray-mp-wiki/reagents/protein-tags/flag-tag/) M1 affinity resin | 0.05% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) (detergent exchanged from [DDM](/xray-mp-wiki/reagents/detergents/ddm/)) + 0.05% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) | Detergent exchanged to [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) on resin |
| SEC | [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | 20 mM HEPES pH 7.5, 150 mM NaCl, 0.05% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.005% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 0.2 uM DU172 + 0.05% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.005% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Concentrated to ~50 mg/mL for [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) crystallization |

#### Source: doi/10.1016##j.str.2017.06.012


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | HEK293T cell expression; membranes prepared in 40 mM Tris-HCl pH 7.6, 1 mM EDTA with protease inhibitors | -- | 40 mM Tris-HCl pH 7.6, 1 mM EDTA + -- | Cells expressed in HEK293T; 0.6 mg/L yield |
| Solubilization | Membranes solubilized with 1.5% [DM](/xray-mp-wiki/reagents/detergents/dm/) for 1 hr at 4 C in presence of 10 uM PSB36 | -- | 40 mM Tris-HCl pH 7.6 + 1.5% [DM](/xray-mp-wiki/reagents/detergents/dm/) | Incubated 1 hr at room temperature with PSB36 before solubilization |
| Ni-NTA affinity chromatography | Batch binding to 5 ml [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta/) superflow cartridge; washed with 5 CV of 8 mM imidazole, 25 CV of 68 mM imidazole; eluted with 272 mM imidazole | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta/) superflow cartridge (Qiagen) | 40 mM Tris-HCl pH 7.4, 400 mM NaCl, 0.15% [DM](/xray-mp-wiki/reagents/detergents/dm/), 5 uM PSB36 (binding); 8 mM imidazole (wash); 272 mM imidazole (elution)
 + 0.15% [DM](/xray-mp-wiki/reagents/detergents/dm/) | All buffers contained 5 uM PSB36 |
| Size-exclusion chromatography | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 10/300 GL column | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 10/300 GL (GE Healthcare) | 40 mM Tris-HCl pH 7.4, 200 mM NaCl, 0.15% [DM](/xray-mp-wiki/reagents/detergents/dm/), 5 uM PSB36 + 0.15% [DM](/xray-mp-wiki/reagents/detergents/dm/) | Fractions concentrated to ~37 mg/mL |


## Crystallization

### doi/10.1016##j.cell.2017.01.042

| Parameter | Value |
|---|---|
| Method | [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) ([LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/)) crystallization |
| Protein sample | A1AR-[BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) fusion in complex with DU172 at ~50 mg/mL mixed with monoolein and cholesterol at 40:54:6 (w:w:w) ratio |
| Temperature | 20 C |
| Growth time | 2 wk |
| Notes | 29 crystals merged into single dataset at 3.2 A resolution, space group P1; two receptor copies per asymmetric unit; structure solved by molecular replacement; lipid cubic phase method |

### doi/10.1016##j.str.2017.06.012

| Parameter | Value |
|---|---|
| Method | [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) ([LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/)) [crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) |
| Protein sample | A1R-StaR-Delta3-b562RIL in complex with PSB36 at ~37 mg/mL mixed with monoolein and cholesterol at 40:54:6 (w:w:w) ratio |
| Temperature | 20 C |
| Growth time | 2 crystals merged |
| Cryoprotection | -- |
| Notes | Crystallized in [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) at Diamond Light Source. Data collected at 3.3 A resolution, space group C22222, 2 crystals merged. Structure solved by molecular replacement.
 |


## Biological / Functional Insights

### A1AR-DU172 structure reveals wider extracellular cavity

The 3.2 A crystal structure of human A1AR bound to the covalent antagonist DU172 (PDB 5UEN) reveals a strikingly wider extracellular cavity compared to the A2AR structure. Major differences were found in the ECL2 conformation and extracellular loop regions. The wider cavity accommodates both orthosteric and allosteric ligands, suggesting a structural basis for allosteric modulation. Drug selectivity between A1 and A2A receptor subtypes appears to be primarily determined by binding site shape/conformation rather than residue composition. The DU172 compound forms a covalent benzene-sulfonate linkage with Y271(7.36) in the binding pocket.

### Xanthine binding mode in A1AR

PSB36 occupies the orthosteric ligand binding pocket of A1AR with the xanthine core sandwiched between F171 and L250(6.51). Two hydrogen bonds form between PSB36 and N254(6.55). The butyl substituent at N1 points toward a hydrophobic pocket formed by V87(3.32), L88(3.33), A91(3.36), M180(5.38), W247(6.48), and H251(6.52). The noradamantyl group at C8 points toward the extracellular face, contacting L253(6.54), T257(6.58), T270(7.35), and E172.

### T270(7.35) gatekeeper residue

Threonine at position 7.35 in A1AR (vs methionine in A2AR) is the primary determinant of xanthine selectivity. M270T mutation in A2AR increases A1-selective ligand affinity, while T270M in A1AR decreases it. The bulky methionine in A2AR creates unfavorable steric interactions with the C8 noradamantyl group of PSB36.

### Narrower binding channel in A2AR

The channel accommodating the N1 butyl chain of PSB36 is narrower in A2AR than in A1AR, preventing deep binding of PSB36 in A2AR. This contributes to the submicromolar affinity of PSB36 for A2AR compared to subnanomolar affinity for A1AR.


## Cross-References

- [PSB36](/xray-mp-wiki/reagents/ligands/psb36/) — A1-selective xanthine antagonist used in crystallization (3.3 A structure)
- [DU172](/xray-mp-wiki/reagents/ligands/du172/) — Covalent antagonist used in prior A1AR structure (PDB 5UEN, 3.2 A)
- [DPCPX (8-Cyclopentyl-1,3-dipropylxanthine)](/xray-mp-wiki/reagents/ligands/dpcpx/) — A1-selective antagonist used in mutagenesis binding assays
- [Human Adenosine A2A Receptor (A2AR)](/xray-mp-wiki/proteins/gpcr/human-adenosine-a2a-receptor-a2ar/) — Comparison structure for selectivity determinants
- [Decylmaltoside (DM)](/xray-mp-wiki/reagents/detergents/dm/) — Detergent used for solubilization and purification at 0.15%
- [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Buffer used in purification and membrane preparation
- [BRIL Fusion Protein](/xray-mp-wiki/reagents/protein-tags/bril/) — b562RIL fusion partner used in StaR construct
