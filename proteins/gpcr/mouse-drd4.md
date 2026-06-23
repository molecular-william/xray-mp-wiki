---
title: Mouse Dopamine Receptor D4 (DRD4)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.48822]
verified: false
---

# Mouse Dopamine Receptor D4 (DRD4)

## Overview

Mouse [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine/) receptor D4 ([DRD4](/xray-mp-wiki/proteins/gpcr/d4-dopamine-receptor/)) is a G-protein-coupled receptor (GPCR) belonging to the D2-like subfamily of [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine/) receptors. It is expressed in the frontal cortex and amygdala and plays roles in cognition and emotions. [DRD4](/xray-mp-wiki/proteins/gpcr/d4-dopamine-receptor/) is coupled to Gi/o proteins and downregulates adenylyl cyclase activity. The 3.5-angstrom crystal structure of mouse [DRD4](/xray-mp-wiki/proteins/gpcr/d4-dopamine-receptor/) complexed with the subtype-selective antagonist [L745870](/xray-mp-wiki/reagents/ligands/l745870/) reveals an extended ligand-binding pocket specific for [DRD4](/xray-mp-wiki/proteins/gpcr/d4-dopamine-receptor/), located between transmembrane helices 2 and 3.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.7554##eLife.48822 | 6IQL | 3.5 | P1 | Mouse [DRD4](/xray-mp-wiki/proteins/gpcr/d4-dopamine-receptor/) (N22 [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/), ICL3 replaced with [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/), F121W/P201I/P317A/C181R) with [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), complexed with [L745870](/xray-mp-wiki/reagents/ligands/l745870/) | [L745870](/xray-mp-wiki/reagents/ligands/l745870/) |

## Expression and Purification

- **Expression system**: Bac-to-Bac Baculovirus Expression System in High5 (Spodoptera frugiperda) cells
- **Construct**: Mouse [DRD4](/xray-mp-wiki/proteins/gpcr/d4-dopamine-receptor/) (GenBank BC051421.1) with N22 [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/), HA signal sequence and [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) at N-terminus, [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) (residues A1-L106 with M7W/H102I/R106L) replacing ICL3 (A220-A302), [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) site, C-terminal EGFP-10xHis tag. Mutations: F121W, P201I, P317A, C181R
- **Notes**: Expressed for 48 hr. Cells flash-frozen in liquid nitrogen and stored at -80 C

### Purification Workflow

- **Expression system**: High5 insect cells via Bac-to-Bac Baculovirus
- **Expression construct**: Mouse DRD4-[BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) chimera with [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), EGFP-His10, mutations F121W/P201I/P317A/C181R
- **Tag info**: N-terminal [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), C-terminal 10xHis-tag, PreScission-cleavable EGFP

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Dounce homogenization | — | 25 mM HEPES pH 7.4, 150 mM NaCl | Cells homogenized, membranes collected and washed |
| Membrane incubation | Ligand stabilization | — | 25 mM HEPES pH 7.4, 150 mM NaCl, 30 uM [L745870](/xray-mp-wiki/reagents/ligands/l745870/), 0.2% w/v [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) | Membranes incubated at 4 C for 1 hr with [L745870](/xray-mp-wiki/reagents/ligands/l745870/) antagonist |
| Solubilization | Detergent extraction | — | [DDM](/xray-mp-wiki/reagents/detergents/ddm/), [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Membranes solubilized in [DDM](/xray-mp-wiki/reagents/detergents/ddm/)/CHS for membrane protein extraction |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | IMAC | [TALON](/xray-mp-wiki/reagents/additives/talon/) cobalt resin | [DDM](/xray-mp-wiki/reagents/detergents/ddm/), [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | His10-tag purification |
| Tag cleavage | [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) digestion | — |  | EGFP-His10 tag removed by [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) |
| Size-exclusion chromatography | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | 25 mM HEPES pH 7.4, 150 mM NaCl + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.015% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Purified protein concentrated for crystallization |

**Final sample**: Purified DRD4-[BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) in 25 mM HEPES pH 7.4, 150 mM NaCl, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.015% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) with [L745870](/xray-mp-wiki/reagents/ligands/l745870/)


## Crystallization

### doi/10.7554##eLife.48822

| Parameter | Value |
|---|---|
| Method | LCP (lipidic cubic phase) |
| Protein sample | Purified DRD4-[BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) with [L745870](/xray-mp-wiki/reagents/ligands/l745870/) in buffer containing 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.015% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) |
| Temperature | 4 |
| Notes | Crystals grew within one week. Harvested from LCP matrix using 50 um micromounts and flash-frozen in liquid nitrogen. Data collected at SPring-8 beamline 41XU |


## Biological / Functional Insights

### Extended binding pocket (EBP) for subtype selectivity

The crystal structure reveals a secondary binding pocket extending from
the orthosteric binding pocket to a DRD4-specific crevice located between
transmembrane helices 2 and 3. This extended pocket is formed by residues
S91(2.64), L94(2.67), L108(3.28), and G110(3.30) that are unique to
[DRD4](/xray-mp-wiki/proteins/gpcr/d4-dopamine-receptor/) within the D2-like subfamily. [L745870](/xray-mp-wiki/reagents/ligands/l745870/) inserts a bulky 4-chlorophenyl
group into this crevice, providing the structural basis for its
DRD4-selective antagonism.

### Antagonist mechanism through TM2-TM3 immobilization

[L745870](/xray-mp-wiki/reagents/ligands/l745870/) blocks [DRD4](/xray-mp-wiki/proteins/gpcr/d4-dopamine-receptor/) activation by reducing the moving freedom of
transmembrane helix 3 (TM3). The bulky chemical group inserted into the
TM2-TM3 crevice prevents the relative movement between these helices
required for full activation of class-A GPCRs. Mutagenesis studies showed
that small-to-large mutations S91L and L108F dramatically reduced the
inhibitory effects of [L745870](/xray-mp-wiki/reagents/ligands/l745870/), and S91F abolished dopamine-induced
activity entirely.

### Non-symmetric homodimer

The crystal structure revealed a non-symmetrical homodimer interface
between TM1-3 of Mol-A and TM5-6 of Mol-B, burying 1600 square angstroms
of solvent-accessible surface. This is stabilized by hydrogen bonds and
hydrophobic packing, including polar interactions between S101(A3.21) and
D186(B5.37) extracellularly, and intracellular hydrogen bonds between
A57(1.58)/T135(3.55) and S58(1.59)/G213(5.64). Cross-linking experiments
confirmed [DRD4](/xray-mp-wiki/proteins/gpcr/d4-dopamine-receptor/) dimerization also occurs in solution.


## Cross-References

- [Human D2 Dopamine Receptor (DRD2)](/xray-mp-wiki/proteins/gpcr/drd2/) — Related D2-like dopamine receptor; comparison of extended binding pocket determinants
- [L745870](/xray-mp-wiki/reagents/ligands/l745870/) — Subtype-selective DRD4 antagonist bound in the 6IQL structure
- [n-Dodecyl-beta-D-maltoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for purification and crystallization
- [HEPES (HEPES-KOH Buffer)](/xray-mp-wiki/reagents/buffers/hepes/) — 25 mM HEPES pH 7.4 used throughout purification
- [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Used in cross-linking and SEC buffers
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [DRD4](/xray-mp-wiki/proteins/gpcr/d4-dopamine-receptor/) — Related protein structure
- [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Additive used in purification or crystallization buffers
- [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) — Additive used in purification or crystallization buffers
