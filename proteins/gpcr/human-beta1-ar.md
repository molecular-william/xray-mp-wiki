---
title: "Human Beta-1 Adrenergic Receptor (beta1 AR)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41422-020-00424-2]
verified: false
---

# Human Beta-1 Adrenergic Receptor (beta1 AR)

## Overview

The beta-1 adrenergic receptor (beta1 AR) is a G protein-coupled receptor (GPCR) that mediates physiologic responses to the catecholamines [Epinephrine](/xray-mp-wiki/reagents/ligands/epinephrine/) and [Norepinephrine](/xray-mp-wiki/reagents/ligands/norepinephrine/) released by the sympathetic nervous system. It is highly expressed in the heart, where it plays a key role in regulating cardiac function. While beta1 AR and beta2 AR share identical catecholamine-binding pockets, beta1 AR has approximately tenfold higher affinity for [Norepinephrine](/xray-mp-wiki/reagents/ligands/norepinephrine/), contributing to distinct physiologic roles. This receptor activates Gs leading to adenyl cyclase activation and increased cAMP. Crystal structures of human beta1 AR in inactive (carazolol-bound) and active (BI-167107-, epinephrine-, and norepinephrine-bound) conformations were determined, revealing that the extracellular vestibule shape and electrostatic properties determine ligand association rates and selectivity.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41422-020-00424-2 | 7BVQ | 2.5 | Not specified in paper | T4L-beta1AR (T4 lysozyme fused to S54 with two alanine linkers, truncated at position 399, ICL3 removed, FLAG-tagged) | [Carazolol](/xray-mp-wiki/reagents/ligands/carazolol/) |
| doi/10.1038##s41422-020-00424-2 | 7BU7 | 2.8 | Not specified in paper | T4L-beta1AR + Nb6B9 [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) | [BI-167107](/xray-mp-wiki/reagents/ligands/bi-167107/) |
| doi/10.1038##s41422-020-00424-2 | 7BU6 | 3.1 | Not specified in paper | T4L-beta1AR + Nb6B9 [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) | [Norepinephrine](/xray-mp-wiki/reagents/ligands/norepinephrine/) |
| doi/10.1038##s41422-020-00424-2 | 7BTS | 2.8 | Not specified in paper | T4L-beta1AR + Nb6B9 [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) | [Epinephrine](/xray-mp-wiki/reagents/ligands/epinephrine/) |

## Expression and Purification

- **Expression system**: Sf9 insect cells (baculovirus expression)
- **Construct**: T4L-beta1AR with FLAG epitope at N-terminus, truncated at position 399, ICL3 (C261-L314) removed
- **Notes**: Expressed with recombinant baculovirus (Bac-to-Bac system) for 48 h at 27 C

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Solubilization | Membrane solubilization |  | 20 mM HEPES pH 7.5, 100 mM NaCl, 1% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.02% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 1% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) + 0.02% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | For inactive-state beta1 AR (carazolol-bound) |
| M1 Flag [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | M1 [FLAG](/xray-mp-wiki/reagents/protein-tags/flag-tag/) affinity resin (Sigma) | 20 mM HEPES pH 7.5, 100 mM NaCl, 0.01% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.0002% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 0.01% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.0002% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Purified with 10 uM [Carazolol](/xray-mp-wiki/reagents/ligands/carazolol/) for inactive state |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) column | 20 mM HEPES pH 7.5, 100 mM NaCl, 0.01% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.0002% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 0.01% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.0002% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Final buffer with 10 uM [Carazolol](/xray-mp-wiki/reagents/ligands/carazolol/) for inactive state |


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Solubilization and M1 Flag affinity | Same as inactive but with agonists | M1 [FLAG](/xray-mp-wiki/reagents/protein-tags/flag-tag/) affinity resin | 20 mM HEPES pH 7.5, 100 mM NaCl, 0.01% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.0002% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 0.01% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.0002% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Purified with target agonists (100 nM [BI-167107](/xray-mp-wiki/reagents/ligands/bi-167107/), 1 mM [Epinephrine](/xray-mp-wiki/reagents/ligands/epinephrine/), or 1 mM [Norepinephrine](/xray-mp-wiki/reagents/ligands/norepinephrine/)) |
| Nb6B9 incubation | Complex formation |  | Same as above + 0.01% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.0002% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Mixed with 1.2-fold molar excess of Nb6B9 overnight at 4 C |
| Nickel [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) (pull-down) | Nickel affinity resin | Same as above + 0.01% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.0002% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Pull-down of functional receptor-Nb6B9 complex via His-tagged Nb6B9 |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) column | 20 mM HEPES pH 7.5, 100 mM NaCl, 0.01% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.0002% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 0.01% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.0002% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Excess Nb6B9 removed; agonists maintained in buffer |


## Crystallization

### doi/10.1038##s41422-020-00424-2

| Parameter | Value |
|---|---|
| Method | [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) ([LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/)) |
| Protein sample | T4L-beta1AR-[Carazolol](/xray-mp-wiki/reagents/ligands/carazolol/) complex reconstituted in [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) with 10% [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) |
| Temperature | Not specified |
| Notes | Inactive state crystals; protein:lipid ratio 2:3 |

| Parameter | Value |
|---|---|
| Method | [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) ([LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/)) |
| Protein sample | T4L-beta1AR-Nb6B9-agonist complexes reconstituted in [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) with 10% [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) |
| Temperature | Not specified |
| Notes | Active state crystals ([BI-167107](/xray-mp-wiki/reagents/ligands/bi-167107/), [Norepinephrine](/xray-mp-wiki/reagents/ligands/norepinephrine/), and [Epinephrine](/xray-mp-wiki/reagents/ligands/epinephrine/) complexes); protein:lipid ratio 2:3 |


## Biological / Functional Insights

### Norepinephrine selectivity for beta1 AR is determined by the extracellular vestibule

Despite identical orthosteric catecholamine-binding pockets in beta1 AR and beta2 AR, [Norepinephrine](/xray-mp-wiki/reagents/ligands/norepinephrine/) is tenfold selective for beta1 AR. The selectivity arises from different association rates (on-rates), not dissociation rates. Metadynamics simulations revealed that [Norepinephrine](/xray-mp-wiki/reagents/ligands/norepinephrine/) takes different pathways to the orthosteric pocket in the two receptors, determined by differences in extracellular vestibule shape, electrostatic properties, and key residues including negatively charged pairs (D217/D356 in beta1 AR vs E180/D300 in beta2 AR) and aromatic gates (F218/F359 in beta1 AR vs F193/Y308 in beta2 AR).

### Active and inactive conformations of human beta1 AR

The inactive (carazolol-bound) and active (BI-167107-, norepinephrine-, and epinephrine-bound) beta1 AR structures display classical GPCR activation features including outward movement of TM5 and TM6 and inward displacement of TM3 and TM7 on the cytoplasmic side. The conserved PIF motif rearrangement (P236, I246, F333) and water-mediated hydrogen bonds characteristic of active-state stabilization were observed.

### Electrostatic differences distinguish norepinephrine and epinephrine binding

Although both catecholamines follow similar binding pathways in their respective receptors, [Epinephrine](/xray-mp-wiki/reagents/ligands/epinephrine/) has an additional methyl group on the primary amine that modifies the electron distribution, making the protonated nitrogen less positively charged than in [Norepinephrine](/xray-mp-wiki/reagents/ligands/norepinephrine/). This makes [Epinephrine](/xray-mp-wiki/reagents/ligands/epinephrine/) less sensitive to the electrostatic differences between the beta1 AR and beta2 AR extracellular vestibules, explaining why [Epinephrine](/xray-mp-wiki/reagents/ligands/epinephrine/) binds both receptors with equal affinity.


## Cross-References

- [Carazolol](/xray-mp-wiki/reagents/ligands/carazolol/) — Inverse agonist used for inactive state structure determination
- [BI-167107](/xray-mp-wiki/reagents/ligands/bi-167107/) — High-affinity agonist used for active state structure
- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — Primary detergent for solubilization and purification
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer used in all purification steps
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid used for LCP crystallization
- [Cholesteryl Hemisuccinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Stabilizing additive used with LMNG
- [T4 Lysozyme (T4L)](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) — Fusion partner for crystallization construct
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Method used in structure determination or purification
- [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/) — Additive used in purification or crystallization buffers
