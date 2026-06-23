---
title: "Xanthorhodopsin"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.0807162105]
verified: false
---

# Xanthorhodopsin

## Overview

Xanthorhodopsin is a light-driven proton pump from the eubacterium Salinibacter ruber that contains a dual chromophore system: a [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore and a noncovalently bound [Carotenoid](/xray-mp-wiki/reagents/ligands/carotenoid/) ([Salinixanthin](/xray-mp-wiki/reagents/ligands/salinixanthin/)) antenna. The 1.9 Å crystal structure reveals 7 transmembrane helices similar to [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) and archaerhodopsin, but with considerably different architecture. The structure introduces novel structural motifs for proton transfer during the photocycle, particularly a His-62–Asp-96 complex for regulating the pKa of the primary proton acceptor, and a dramatically different proton release mechanism compared to archaeal pumps. The close approach of the [Salinixanthin](/xray-mp-wiki/reagents/ligands/salinixanthin/) and [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) polyenes (center-to-center distance 11.7 Å, 46° angle) explains the ~45% efficiency of excited-state energy transfer from the [Carotenoid](/xray-mp-wiki/reagents/ligands/carotenoid/) antenna to [Retinal](/xray-mp-wiki/reagents/ligands/retinal/). This structure defines the geometry of the dual chromophore system and provides a model for eubacterial proton pump mechanisms.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.0807162105 | 3DDL | 1.9 A | P1 | Full-length xanthorhodopsin from Salinibacter ruber | [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) and [Salinixanthin](/xray-mp-wiki/reagents/ligands/salinixanthin/) ([Carotenoid](/xray-mp-wiki/reagents/ligands/carotenoid/) antenna) |

## Expression and Purification

- **Expression system**: Salinibacter ruber (native source)
- **Construct**: Native xanthorhodopsin

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell disruption and membrane preparation | French press | -- | 100 mM NaCl, 5 mM bicine (pH 8.0) + 0.01% dodecyl maltoside | Cells broken and membranes washed with buffer containing 0.01% dodecyl maltoside |
| Membrane resuspension | Centrifugation | -- | 30 mM phosphate (pH 5.6), 1 mM sodium azide + -- | Membrane fraction resuspended to 5 mg/ml xanthorhodopsin |
| Solubilization in bicelle medium | Bicelle solubilization | -- | -- + 16.7% (wt/wt) [DMPC](/xray-mp-wiki/reagents/lipids/dmpc/) in 20% nonyl maltoside | One volume of [DMPC](/xray-mp-wiki/reagents/lipids/dmpc/)/nonyl maltoside bicelle mixture added to 3 volumes of xanthorhodopsin preparation, vortexed, incubated overnight at 4°C |


## Crystallization

### doi/10.1073##pnas.0807162105

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | Solubilized xanthorhodopsin in bicelle medium (5 mg/ml) |
| Reservoir | 2.5-3 M [Sodium Phosphate](/xray-mp-wiki/reagents/buffers/sodium-phosphate/) (pH 5.6) |
| Temperature | 22°C |
| Growth time | 4-5 months |
| Cryoprotection | Stepwise equilibration with 5%, 10%, then 15% [Ethylene Glycol](/xray-mp-wiki/reagents/additives/ethylene-glycol/) |
| Notes | Crystals grown in sitting drops containing 10 µL solubilized xanthorhodopsin, 3 µL of 3 M [Sodium Phosphate](/xray-mp-wiki/reagents/buffers/sodium-phosphate/) (pH 5.6), and 2 µL of 2.5 mM sodium azide. Crystals approximately 30 × 30 × 150 µm. Data collected at 100 K on SSRL beamline 9.1. |


## Biological / Functional Insights

### Dual chromophore system with carotenoid antenna

Xanthorhodopsin contains both [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) and the [Carotenoid](/xray-mp-wiki/reagents/ligands/carotenoid/) [Salinixanthin](/xray-mp-wiki/reagents/ligands/salinixanthin/) as a light-harvesting antenna. The center-to-center distance between the two chromophores is 11.7 Å, with ring moieties within 5 Å of each other. The 46° angle between chromophore axes represents a compromise between optimal capture of light of all polarization angles and efficient excited-state energy transfer (~45% efficiency). The [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) β-ionone ring forms part of the [Carotenoid](/xray-mp-wiki/reagents/ligands/carotenoid/) binding site, explaining the dependence of the [Carotenoid](/xray-mp-wiki/reagents/ligands/carotenoid/) spectrum on [Retinal](/xray-mp-wiki/reagents/ligands/retinal/).

### Asp-His counterion complex for pKa regulation

Unlike [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) (pKa ~2.5), eubacterial proton pumps have a primary proton acceptor with pKa near 7. In xanthorhodopsin, His-62 ND1 forms a very short hydrogen bond (2.42-2.55 Å) with Asp-96 OD1, creating a shared-proton complex that acts as the Schiff base counterion. This Asp-His complex raises the effective pKa relative to aspartate alone and is conserved in proteorhodopsins, making it a general feature of eubacterial pumps.

### Reversed proton release sequence

Unlike [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/), xanthorhodopsin does not release a proton at the time of Schiff base deprotonation. Instead, proton uptake from the cytoplasm occurs first (via Glu-107 after it reprotonates the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) Schiff base), and proton release to the extracellular surface is delayed until the final photocycle step. The carboxylate of Asp-96 is severely rotated, and the hydrogen-bonded aqueous network for proton release in BR is replaced by hydrogen-bonded residues more resistant to rearrangement.

### Dramatically different architecture from archaeal rhodopsins

The main chain of xanthorhodopsin differs more from [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) than any other crystallized microbial rhodopsin. Helices A and G are longer (by 4 and 9 residues respectively), and their tilt and rotation differ considerably. The B-C loop reorients dramatically, displacing its tip by 30 Å toward the periphery and creating a large cleft that brings functional residues near the aqueous interface.


## Cross-References

- [Salinixanthin](/xray-mp-wiki/reagents/ligands/salinixanthin/) — Carotenoid antenna chromophore bound to xanthorhodopsin
- [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) — Primary chromophore of xanthorhodopsin
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — Archaeal homolog with different proton release mechanism
- [Proton Release Complex](/xray-mp-wiki/concepts/rhodopsin-mechanisms/proton-release-complex/) — Xanthorhodopsin lacks the canonical proton release complex found in BR
- [Evolution of Rhodopsins](/xray-mp-wiki/concepts/rhodopsin-mechanisms/evolution-of-rhodopsins/) — Xanthorhodopsin reveals evolutionary divergence between archaeal and eubacterial proton pumps
- [Bicelle Crystallization](/xray-mp-wiki/methods/crystallization/bicelle-crystallization/) — Structure was solved from crystals grown in bicelle medium
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [Anabaena Sensory Rhodopsin](/xray-mp-wiki/proteins/rhodopsins/anabaena-sensory-rhodopsin/) — Related protein structure
- [Ethylene Glycol](/xray-mp-wiki/reagents/additives/ethylene-glycol/) — Additive used in purification or crystallization buffers
- [Sodium Phosphate](/xray-mp-wiki/reagents/buffers/sodium-phosphate/) — Buffer component in purification or crystallization
