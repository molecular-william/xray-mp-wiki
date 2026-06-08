---
title: Drosophila melanogaster Dopamine Transporter
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.3029, doi/10.1038##nsmb.1662]
verified: false
---

# Drosophila melanogaster Dopamine Transporter

## Overview

The Drosophila melanogaster dopamine transporter (dDAT) is a Na+/Cl--coupled biogenic amine transporter that clears dopamine, norepinephrine, and tyramine from synaptic spaces. dDAT is widely used as a model system for mammalian biogenic amine transporters because it lacks a dedicated norepinephrine transporter (NET) in Drosophila, making dDAT the primary catecholamine reuptake mechanism. Despite preferring dopamine over norepinephrine, dDAT exhibits pharmacological properties closest to mammalian NETs, making it an excellent model for structure-based studies of NET-specific antidepressant inhibitors.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nsmb.3029 | 4XNU | 3.0 |  | dDAT_cryst | nisoxetine |
| doi/10.1038##nsmb.3029 | 4XNX | 3.0 |  | dDAT_mfc | reboxetine |

## Expression and Purification

- **Expression system**: HEK-293S GnTI- cells (baculovirus-mediated transduction)
- **Construct**: C-terminal GFP-His8 fusion; thermostabilized variants with EL2 truncation and thrombin cleavage site

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1 | membrane solubilization |  | 1x TBS (20 mM Tris pH 8.0, 150 mM NaCl) + 20 mM DDM | Membranes homogenized in TBS and solubilized with 20 mM DDM |
| 2 | cobalt-affinity chromatography | cobalt-charged metal-affinity resin | 1x TBS with 1 mM DDM, 0.2 mM CHS, 100 mM imidazole, pH 8.0 + 1 mM DDM | GFP-His8 tag captured on cobalt resin and eluted with imidazole |
| 3 | thrombin cleavage |  | 1x TBS with 1 mM DDM, 0.2 mM CHS + 1 mM DDM | GFP-His8 tag removed by overnight thrombin digestion at 4 C |
| 4 | size-exclusion chromatography | Superdex 200 10/300 column | 20 mM Tris pH 8.0, 300 mM NaCl, 4 mM decyl-beta-D-maltoside, 0.2 mM CHS, 0.001% POPE + 4 mM decyl-beta-D-maltoside | Peak fractions pooled; all procedures at 4 C |


## Crystallization

### doi/10.1038##nsmb.3029

| Parameter | Value |
|---|---|
| Method | hanging-drop vapor diffusion |
| Protein sample | Fab-DAT complex at 3-4 mg/ml with 1 mM nisoxetine or (R,R)-reboxetine |
| Reservoir | 0.1 M glycine pH 9, 38% PEG 350 monomethyl ether |
| Temperature | 4 C |
| Notes | Crystals of dDAT_mfc obtained by streak seeding 7 d after drop setup |


## Biological / Functional Insights

### Outward-open conformation stabilized by antidepressants

Both nisoxetine and reboxetine bind in the central substrate-binding site (S1), locking dDAT in an outward-open conformation. The inhibitors occupy subsites A, B, and C. The secondary amine groups extend into subsite A, forming interactions with Phe43. The bulky morpholine ring of reboxetine sterically prevents inward movements of transmembrane helices 1b and 6a, gating the extracellular vestibule.

### Molecular basis of NET-specific inhibitor selectivity

The bilobed aromatic moieties and extended amine groups of antidepressants generate high-affinity binding. Substituents on the aromatic rings encode selectivity between biogenic amine transporters. The phenoxy ring substitution pattern (ortho vs. para) distinguishes hNET from hSERT inhibitors based on subsite B environment. Residues at subsite B differ between insect (Asp121, Ser426 in dDAT) and mammalian DAT/NET (Gly, Met), and mutating these to hNET residues enhanced nisoxetine binding affinity three-fold.


## Cross-References

- [N-Dodecyl-Beta-D-Maltoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary solubilization detergent used throughout purification
- [Polyethylene Glycol (PEG)](/xray-mp-wiki/reagents/additives/peg/) — PEG 350 monomethyl ether used as crystallization precipitant
- [Superdex 200 SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200/) — Size-exclusion chromatography resin used for final purification
- [Glycine Buffer](/xray-mp-wiki/reagents/additives/glycine/) — Crystallization reservoir buffer (0.1 M, pH 9)
- [Nisoxetine](/xray-mp-wiki/reagents/ligands/nisoxetine/) — NET-specific inhibitor co-crystallized with dDAT_cryst (PDB 4XNU)
- [Reboxetine](/xray-mp-wiki/reagents/ligands/reboxetine/) — NET-specific inhibitor co-crystallized with dDAT_mfc (PDB 4XNX)
- [Fab 9D5](/xray-mp-wiki/reagents/antibodies/fab-9d5/) — Antibody fragment used to complex with dDAT for crystallization
- [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) — Crystallization method used to grow dDAT-Fab complexes
