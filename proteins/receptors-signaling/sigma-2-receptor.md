---
title: "Human Sigma-2 Receptor (TMEM97)"
created: 2026-06-09
updated: 2026-06-09
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41586-021-04175-x]
verified: false
---

# Human Sigma-2 Receptor (TMEM97)

## Overview

The human sigma-2 receptor (σ2 receptor, encoded by TMEM97) is an orphan transmembrane protein
that is highly expressed in the central nervous system and various cancer cell lines. It has been
a long-standing target for neuropathic pain treatment and cancer diagnostics, though its endogenous
ligand and native function remain unknown. The first X-ray crystal structures of the sigma-2
receptor, determined in complex with three different ligands (PB28, Roluperidone, and [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/)),
revealed a novel membrane protein fold consisting of a four-helix bundle with an intramembrane
ligand-binding pocket. The structures enabled large-scale docking-based virtual screening that
identified potent sigma-2 ligands with efficacy in animal models of neuropathic pain, including
several with activity comparable to gabapentinoids.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41586-021-04175-x | 7M93 | 2.7 A | Not stated in raw paper | Human sigma-2 receptor (TMEM97) expressed in Sf9 insect cells | PB28 (sigma-2 agonist) |
| doi/10.1038##s41586-021-04175-x | 7M93 | 3.3 A | Not stated in raw paper | Human sigma-2 receptor (TMEM97) expressed in Sf9 insect cells | Roluperidone (sigma-2 antagonist) |
| doi/10.1038##s41586-021-04175-x | 7M93 | 3.2 A | Not stated in raw paper | Human sigma-2 receptor (TMEM97) expressed in Sf9 insect cells | [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) |

## Expression and Purification

- **Expression system**: Baculovirus expression in Sf9 insect cells
- **Construct**: Human sigma-2 receptor (TMEM97) with N-terminal purification tag

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Baculovirus expression in Sf9 insect cells | — | Not specified | Expressed using baculovirus system |
| Solubilization | Detergent solubilization | — | Buffer containing [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) and [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Protein solubilized in [LMNG](/xray-mp-wiki/reagents/detergents/lmng/)/CHS mixed micelles |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Affinity purification | — | Standard purification buffer with [LMNG](/xray-mp-wiki/reagents/detergents/lmng/)/CHS | Purified via affinity tag, followed by size-exclusion chromatography |
| Size-exclusion chromatography | SEC | — | SEC buffer with [LMNG](/xray-mp-wiki/reagents/detergents/lmng/)/CHS | Final purification step; protein concentrated for crystallization |


## Crystallization

### doi/10.1038##s41586-021-04175-x

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | Purified sigma-2 receptor in [LMNG](/xray-mp-wiki/reagents/detergents/lmng/)/CHS |
| Temperature | 20 C |
| Notes | Structures determined by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/). Three distinct structures obtained
with different ligands: PB28 (agonist), Roluperidone (antagonist), and [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/).
The structures enabled large-scale docking-based virtual screening that identified
novel sigma-2 ligands with nanomolar potency.
 |


## Biological / Functional Insights

### Novel four-helix bundle architecture

The sigma-2 receptor adopts a novel four-helix bundle fold with an intramembrane
ligand-binding pocket, distinct from any previously characterized GPCR or
membrane protein fold. The binding pocket is completely buried within the
transmembrane region.

### Ligand recognition and docking-based discovery

The three structures reveal how diverse ligands (agonists, antagonists, and
[Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/)) bind to the sigma-2 receptor. The structures enabled successful
retrospective docking validation followed by prospective virtual screening of
a large compound library, yielding potent and selective sigma-2 ligands that
showed efficacy in a mouse model of neuropathic pain.


## Cross-References

- [Human Sigma-1 Receptor (SIGMAR1)](/xray-mp-wiki/proteins/receptors-signaling/sigma-1-receptor/) — Related sigma receptor family member with distinct pharmacology and fold
- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — Primary detergent for solubilization and purification
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Additive used in purification or crystallization buffers
- [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) — Additive used in purification or crystallization buffers
