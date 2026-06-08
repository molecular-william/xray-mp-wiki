---
title: Opsin (Retinal-Free Rhodopsin Apoprotein)
created: 2026-05-26
updated: 2026-05-26
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1002##anie.201302374]
verified: false
---

# Opsin (Retinal-Free Rhodopsin Apoprotein)

## Overview

Opsin is the apoprotein form of rhodopsin, the G-protein-coupled receptor responsible for vision in vertebrate retinal rod cells. This crystal structure represents the active Ops* conformation (retinal-free rhodopsin) in complex with a synthetic G-protein peptide (GalphaCT2) and a molecule of [og](/xray-mp-wiki/reagents/detergents/og/) bound deep within the orthosteric ligand-binding pocket. The structure serves as the best available structural template for homology modeling of olfactory receptors (ORs), which comprise over half of all GPCRs.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1002##anie.201302374 | 4GZM | 2.65 A | not specified in paper | Ops* conformation (retinal-free rhodopsin apoprotein) in complex with synthetic G protein peptide GalphaCT2 | Octyl glucoside (OG) in retinal-binding pocket; synthetic G protein peptide GalphaCT2 |

## Expression and Purification

- **Expression system**: Vertebrate retinal rod cells (disc membrane)
- **Construct**: Native opsin apoprotein (retinal-free rhodopsin), solubilized in [og](/xray-mp-wiki/reagents/detergents/og/) detergent

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Disc membrane solubilization | Solubilization in [og](/xray-mp-wiki/reagents/detergents/og/) detergent | -- | not specified + Octyl glucoside (OG) | Opsin was solubilized from disc membranes of vertebrate retinal rod cells using OG, which favors the active Ops* conformation |


## Crystallization

### doi/10.1002##anie.201302374

| Parameter | Value |
|---|---|
| Method | X-ray crystallography (sitting-drop or vapor diffusion not specified) |
| Protein sample | Ops* in complex with synthetic G protein peptide GalphaCT2 and OG in [og](/xray-mp-wiki/reagents/detergents/og/) detergent |
| Reservoir | pH 5.6 crystallization conditions |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | not specified |
| Notes | Crystallization at low pH (5.6) in OG detergent promotes formation of the active Ops* conformation. The well-defined hydrogen-bond network holds OG in the retinal-binding pocket. Active Ops* conformation stabilized by OG in the ligand-binding pocket. |


## Biological / Functional Insights

### Ops* conformation stabilized by OG in ligand-binding pocket

A molecule of [og](/xray-mp-wiki/reagents/detergents/og/) was identified in the
retinal-binding pocket of the active Ops* conformation, replacing retinal and stabilizing the
G-protein-interacting state. This was confirmed by the crystal structure of Ops* in complex with
the synthetic G protein peptide GalphaCT2, derived from the key GPCR binding site on the C-terminal
region of the G-alpha subunit.

### Structural homology between opsin and olfactory receptors

Opsin shares key features expected for olfactory receptors (ORs): a deep hydrophobic ligand-binding
pocket accessible from the lipid bilayer, a hydrogen-bond network for ligand recognition, and
conformational flexibility between active and inactive states. The hydrogen-bond pattern holding OG
in the pocket is reminiscent of the dynamic hydrogen-bond pattern proposed for OR-odorant interactions,
in which the receptor offers changing side chains for bonding.

### Detergent chain-length-dependent pocket occupancy

Various detergents ([decylmaltoside (DM)](/xray-mp-wiki/reagents/detergents/decylmaltoside/), OG,
[nonylglucoside (NG)](/xray-mp-wiki/reagents/detergents/nonylglucoside/), and
[heptylglucoside (HpG)](/xray-mp-wiki/reagents/detergents/heptylglucoside/)) can occupy the binding
pocket in a chain-length-dependent manner, providing a model for how hydrophobic odorants enter ORs.
The neopentyl glycol detergents ([lauryl maltose neopentyl glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/),
octyl glucose neopentyl glycol) showed only small inhibitory effects, suggesting they block the
openings rather than entering the pocket.

### Opsin as structural template for OR homology modeling

Opsin can host not only various artificial hydrophobic retinal analogues and naturally occurring
hydroxy analogues, but also chemically distinct molecules like detergents containing multiple hydroxy
groups. The present Ops* structure illustrates how hydrophobic odorants, after partitioning into the
membrane, can enter from the lipid bilayer into the 7TM scaffold. Taken together, Ops* may serve as
the best currently available structural template for homology modeling of ORs and improved binding-site
prediction for hydrophobic odorants.


## Cross-References

- [Bovine Rhodopsin (Dark State)](/xray-mp-wiki/proteins/bovine-rhodopsin/) — Same protein in dark state with 11-cis-retinal bound (PDB 1GZM); structural basis for comparison to active Ops* state
- [Octyl Glucoside (OG)](/xray-mp-wiki/reagents/detergents/og/) — Detergent found bound in orthosteric ligand-binding pocket of Ops*, stabilizing active conformation
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent tested for reconstitution compatibility with opsin
- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — Neopentyl glycol detergent family, tested for pocket access in reconstitution experiments
- [Decylmaltoside (DM)](/xray-mp-wiki/reagents/detergents/decylmaltoside/) — Shows strong concentration-dependent inhibition of rhodopsin reconstitution, fitting best into retinal-binding pocket
- [Nonylglucoside (NG)](/xray-mp-wiki/reagents/detergents/nonylglucoside/) — Tested for reconstitution inhibition, shows chain-length-dependent pocket occupancy
- [Heptylglucoside (HpG)](/xray-mp-wiki/reagents/detergents/heptylglucoside/) — Tested for reconstitution inhibition, shows chain-length-dependent pocket occupancy
- [11-cis-Retinal](/xray-mp-wiki/reagents/ligands/11-cis-retinal/) — Natural chromophore ligand of rhodopsin; replaced by OG in the Ops* crystal structure
