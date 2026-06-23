---
title: Drosophila melanogaster Dopamine Transporter
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.3029, doi/10.1038##nsmb.1662, doi/10.1038##s41467-021-22385-9]
verified: false
---

# Drosophila melanogaster Dopamine Transporter

## Overview

The Drosophila melanogaster [DOPAMINE](/xray-mp-wiki/reagents/ligands/dopamine) transporter (dDAT) is a Na+/Cl--coupled biogenic amine transporter that clears [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine), norepinephrine, and tyramine from synaptic spaces. dDAT is widely used as a model system for mammalian biogenic amine transporters because it lacks a dedicated norepinephrine transporter (NET) in Drosophila, making dDAT the primary catecholamine reuptake mechanism. Despite preferring [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine) over norepinephrine, dDAT exhibits pharmacological properties closest to mammalian NETs, making it an excellent model for structure-based studies of NET-specific antidepressant inhibitors.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nsmb.3029 | 4XNU | 3.0 |  | dDAT_cryst | [NISOXETINE](/xray-mp-wiki/reagents/ligands/nisoxetine) |
| doi/10.1038##nsmb.3029 | 4XNX | 3.0 |  | dDAT_mfc | [REBOXETINE](/xray-mp-wiki/reagents/ligands/reboxetine) |
| doi/10.1038##s41467-021-22385-9 | 7M2E | 3.3 |  | dDAT_subB (hNET-like mutations D121G/S426M in subsite B), substrate-free | None (Na+ and Cl- bound at respective sites) |
| doi/10.1038##s41467-021-22385-9 | 7M2F | 2.8 |  | dDAT_mfc with norepinephrine bound | Norepinephrine |
| doi/10.1038##s41467-021-22385-9 | 7M2G | 3.3 |  | dDAT_subB (hNET-like mutations D121G/S426M) with [DULOXETINE](/xray-mp-wiki/reagents/ligands/duloxetine) bound | [DULOXETINE](/xray-mp-wiki/reagents/ligands/duloxetine) |
| doi/10.1038##s41467-021-22385-9 | 7M2H | 3.0 |  | dDAT_NET with milnacipran bound | Milnacipran |
| doi/10.1038##s41467-021-22385-9 | 7M2I | 2.8 |  | dDAT_NET with tramadol bound | Tramadol |

## Expression and Purification

- **Expression system**: HEK-293S GnTI- cells (baculovirus-mediated transduction)
- **Construct**: C-terminal GFP-His8 fusion; thermostabilized variants with EL2 [TRUNCATION](/xray-mp-wiki/concepts/truncation) and thrombin cleavage site

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1 | membrane solubilization |  | 1x TBS (20 mM [TRIS](/xray-mp-wiki/reagents/buffers/tris) pH 8.0, 150 mM NaCl) + 20 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Membranes homogenized in TBS and solubilized with 20 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm) |
| 2 | cobalt-affinity chromatography | cobalt-charged metal-affinity resin | 1x TBS with 1 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm), 0.2 mM CHS, 100 mM [IMIDAZOLE](/xray-mp-wiki/reagents/additives/imidazole), pH 8.0 + 1 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm) | GFP-His8 tag captured on cobalt resin and eluted with [IMIDAZOLE](/xray-mp-wiki/reagents/additives/imidazole) |
| 3 | thrombin cleavage |  | 1x TBS with 1 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm), 0.2 mM CHS + 1 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm) | GFP-His8 tag removed by overnight thrombin digestion at 4 C |
| 4 | size-exclusion chromatography | Superdex 200 10/300 column | 20 mM [TRIS](/xray-mp-wiki/reagents/buffers/tris) pH 8.0, 300 mM NaCl, 4 mM decyl-beta-D-maltoside, 0.2 mM CHS, 0.001% [POPE](/xray-mp-wiki/reagents/lipids/pope) + 4 mM decyl-beta-D-maltoside | Peak fractions pooled; all procedures at 4 C |


## Crystallization

### doi/10.1038##nsmb.3029

| Parameter | Value |
|---|---|
| Method | hanging-drop vapor diffusion |
| Protein sample | Fab-DAT complex at 3-4 mg/ml with 1 mM [Nisoxetine](/xray-mp-wiki/reagents/ligands/nisoxetine) or (R,R)-[REBOXETINE](/xray-mp-wiki/reagents/ligands/reboxetine) |
| Reservoir | 0.1 M [GLYCINE](/xray-mp-wiki/reagents/buffers/glycine) pH 9, 38% [PEG](/xray-mp-wiki/reagents/additives/peg) 350 monomethyl ether |
| Temperature | 4 C |
| Notes | Crystals of dDAT_mfc obtained by streak seeding 7 d after drop setup |


## Biological / Functional Insights

### Norepinephrine binds in a different pose than dopamine

Norepinephrine binds in subsite C of the primary binding site, oriented more towards subsite C relative to [DOPAMINE](/xray-mp-wiki/reagents/ligands/dopamine) which binds closer to subsite B. The beta-OH group in NE restricts catechol rotation with an energy barrier of 9-12 kcal/mol, compared to 0.3-0.6 kcal/mol for DA. This difference translates to DAT and NET having greater propensity to interact with DA compared to NE, consistent with higher Ki values for NE competition (19 uM vs 2.0 uM for DA).

### Subsite C determines NET-specific inhibitor selectivity

SNRIs [DULOXETINE](/xray-mp-wiki/reagents/ligands/duloxetine), milnacipran, and tramadol all interact with subsite C through aromatic groups. hDAT-like mutations in subsite C (A117S, A428S) in dDAT cause maximal loss of affinity for these inhibitors, demonstrating that subsite C residues are key determinants of NET specificity. Non-specific inhibitors like [Cocaine](/xray-mp-wiki/reagents/ligands/cocaine) primarily interact with subsite B, while NET-specific inhibitors engage subsite C.

### Tramadol binds primarily at subsite C

Tramadol's methoxyphenyl ring interacts with Y124 by aromatic edge-to-face interactions and fits into the hydrophobic pocket lined by A117, V120, A428, and F325 of subsite C. Unlike [COCAINE](/xray-mp-wiki/reagents/ligands/cocaine) which wedges its benzoyl group into subsite B, tramadol's lack of interaction at subsite B compromises affinity but retains NET specificity over DAT.


## Cross-References

- [N-Dodecyl-Beta-D-Maltoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary solubilization detergent used throughout purification
- [Polyethylene Glycol (PEG)](/xray-mp-wiki/reagents/additives/peg/) — PEG 350 monomethyl ether used as crystallization precipitant
- [Superdex 200 SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200/) — Size-exclusion chromatography resin used for final purification
- [Glycine Buffer](/xray-mp-wiki/reagents/additives/glycine/) — Crystallization reservoir buffer (0.1 M, pH 9)
- [Nisoxetine](/xray-mp-wiki/reagents/ligands/nisoxetine/) — NET-specific inhibitor co-crystallized with dDAT_cryst (PDB 4XNU)
- [Reboxetine](/xray-mp-wiki/reagents/ligands/reboxetine/) — NET-specific inhibitor co-crystallized with dDAT_mfc (PDB 4XNX)
- [Fab 9D5](/xray-mp-wiki/reagents/antibodies/fab-9d5/) — Antibody fragment used to complex with dDAT for crystallization
- [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) — Crystallization method used to grow dDAT-Fab complexes
- [Duloxetine](/xray-mp-wiki/reagents/ligands/duloxetine/) — SNRI inhibitor co-crystallized with dDAT_subB (PDB 7M2G)
- [Milnacipran](/xray-mp-wiki/reagents/ligands/milnacipran/) — SNRI inhibitor co-crystallized with dDAT_NET (PDB 7M2H)
- [Tramadol](/xray-mp-wiki/reagents/ligands/tramadol/) — Synthetic opioid co-crystallized with dDAT_NET (PDB 7M2I)
- [MOPS Buffer](/xray-mp-wiki/reagents/buffers/mops/) — Buffer (0.1 M, pH 6.5-7.0) used in crystallization reservoir
- [Polyethylene glycol 600 (PEG 600)](/xray-mp-wiki/reagents/additives/peg-600/) — Precipitant (30-32%) used in crystallization reservoir
