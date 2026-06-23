---
title: Chrimson Channelrhodopsin
created: 2018-09-26
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-018-06421-9]
verified: false
---

# Chrimson Channelrhodopsin

## Overview

Chrimson is a red light-activated channelrhodopsin from the algae *Chlamydomonas noctigama* that represents the most red-shifted channelrhodopsin identified to date, with a peak absorption at 590 nm. The crystal structure was determined at 2.6 A resolution (PDB 5ZIH) (Oda et al., 2018), revealing a unique counterion configuration with protonated Glu165, polar residue distribution biased toward the beta-ionone ring, and tight retinal binding pocket packing. Chrimson resembles prokaryotic proton pumps in the retinal binding pocket while sharing similarity with other channelrhodopsins in the ion-conducting pore. Based on the structural insights, the ChrimsonSA mutant (S169A) was engineered with further red-shifted absorption beyond 605 nm, reduced blue-light sensitivity, and accelerated closing kinetics, making it a useful tool for dual-color optogenetic applications.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-018-06421-9 | 5ZIH | 2.6 A | C 1 2 1 | C1Chrimson (Chlamydomonas noctigama Chrimson with N-terminal 79 residues replaced by CrChR1 residues 1-76), C-terminal TEV-EGFP-FLAG tag, expressed in Sf9 insect cells | all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal) (covalently bound via Schiff base to Lys283) |

## Expression and Purification

- **Expression system**: [Sf9](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) insect cells ([Baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) expression system)
- **Construct**: C1Chrimson (N-terminal 1-79 swapped with CrChR1 1-76), C-terminal TEV-EGFP-FLAG tag

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | [Baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) infection of [Sf9](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) cells (Sf900II medium, 27 C, 48 h); 100 uM all-trans [retinal](/xray-mp-wiki/reagents/ligands/retinal/) added at 24 h post-infection | -- | 150 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 50 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.0, 5% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.1 mM [PMSF](/xray-mp-wiki/reagents/additives/pmsf/) + -- | Cells harvested 48 h post-infection; pellets disrupted by sonication; cell debris cleared at 10,000 x g; crude membrane collected by ultracentrifugation at 215,000 x g |
| Solubilization | Detergent solubilization | -- | 150 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 50 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.0, 5% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.1 mM [PMSF](/xray-mp-wiki/reagents/additives/pmsf/) + 2.5% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.5% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Insoluble material removed by ultracentrifugation at 208,000 x g |
| FLAG affinity purification | [ANTI-FLAG M2 Agarose](/xray-mp-wiki/reagents/additives/flag-tag/) affinity chromatography | ANTI-FLAG M2 Agarose Affinity Gel (Sigma) | 150 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 50 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.0, 5% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Binding for 1.5 h; EGFP-FLAG tag cleaved by [TEV protease](/xray-mp-wiki/reagents/additives/tev-protease/) (homemade) on resin |
| Size-exclusion chromatography | [Size-exclusion chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | Not specified | 150 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 50 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.0, 5% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Peak fractions pooled and concentrated to 7.0 mg/ml for crystallization |


## Crystallization

### doi/10.1038##s41467-018-06421-9

| Parameter | Value |
|---|---|
| Method | [Lipidic cubic phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) (LCP) crystallization |
| Protein sample | C1Chrimson at 7.0 mg/ml in 150 mM NaCl, 50 mM HEPES pH 7.0, 5% glycerol, 0.05% DDM, 0.01% CHS |
| Temperature | 20 C |
| Growth time | 4 weeks in the dark |
| Cryoprotection | No additional cryoprotectant needed (high PEG concentration); flash-cooled in liquid nitrogen |
| Notes | Protein mixed with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) at 2:3 protein-to-lipid ratio (w/w). 50 nl protein-LCP mixture per well, overlaid with 800 ul precipitant solution. Crystals harvested using microworms. Data collected at SPring-8 BL32XU; merged from multiple crystals using KAMO. |


## Biological / Functional Insights

### Unique counterion configuration enables red-shifted absorption

Chrimson's red-shifted absorption is partly due to protonation of the counterion residue Glu165, which weakens the stabilization of the protonated retinal Schiff base (PSB). Glu165 is in 3.0 A proximity to the PSB, while Asp295 is at 3.6 A. The two counterion residues are only 3.3 A apart, suggesting the Glu165 proton may be partly shared by both residues via hydrogen bond interactions. This configuration is similar to the acidic form of bacteriorhodopsin (BR605).

### Chrimson resembles prokaryotic proton pumps in the retinal binding pocket

About half of the residues constituting the retinal binding pocket are substituted in Chrimson compared to C1C2. Chrimson resembles bacteriorhodopsin rather than C1C2 in the residues surrounding the polyene chain and beta-ionone ring. Polar residues (Ser223, Tyr231) near the beta-ionone ring create biased polarity distribution, stabilizing the light-excited intermediate and contributing to the red-shifted absorption.

### Tight retinal packing by Met201 controls kinetics and absorption

The bulky side chain of Met201 tightly packs against the polyene chain of retinal. The M201T mutation causes a large blue-shift (50-80 nm) and extremely slow closing kinetics with photocurrents sustained for minutes, indicating that structural rigidity around the beta-ionone ring is crucial for proper photocycle kinetics. This is reminiscent of the step-function opsin (SFO) mutants in CrChRs.

### Outer gate and proton selectivity

The extracellular ion pore of Chrimson is occluded by an outer gate formed by Arg162 and Asn287, which separates a buried cluster of carboxylate residues (Glu132, Glu139, Glu300) from the extracellular solvent. Mutations destabilizing the outer gate (R162H, N287E, E139Q) cause largely blue-shifted activation spectra and altered ion permeability. The R162H mutant becomes permeable to guanidinium, suggesting Arg162 is part of the ion selectivity filter.

### Three constriction sites form the ion pore gates

Chrimson's ion-conducting pore is formed by TM2, TM3, TM6, and TM7, lined by five glutamic acid residues (Glu124-E5). Three constriction sites restrict ion permeation in the dark state: the inner gate (Lys176, Arg310), the central gate adjacent to the retinal Schiff base (Ser102, Glu129, Glu132), and the outer gate (Arg162, Asn287). The inner gate lacks the histidine-mediated ionic interaction seen in C1C2 and CrChR2.

### ChrimsonSA (S169A) engineered for dual-color optogenetics

Based on structural insights, the ChrimsonSA mutant (S169A) was engineered with peak absorption shifted beyond 605 nm, significantly reduced blue-light sensitivity, and accelerated closing kinetics. ChrimsonSA expressed well in hippocampal neurons and allowed spiking with red light while reducing blue-light-evoked action potentials, making it a useful tool for dual-color optogenetic applications.


## Cross-References

- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent (2.5% solubilization, 0.05% purification) for membrane protein isolation
- [Cholesteryl Hemisuccinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Stabilizing additive (0.5% solubilization, 0.01% purification) used with DDM
- [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer (50 mM, pH 7.0) used throughout purification and crystallization
- [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/) — Salt (150 mM) included in purification and SEC buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Stabilizer (5%) used in purification buffers
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid used for LCP crystallization matrix (2:3 protein-to-lipid ratio)
- [All-trans Retinal](/xray-mp-wiki/reagents/ligands/retinal/) — Chromophore covalently bound to Lys283 via Schiff base
- [Lipidic Cubic Phase (LCP) Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used for Chrimson crystallization
- [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) — Protein expressed in Sf9 cells using baculovirus system
- [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) — Expression host for recombinant Chrimson production
- [Channelrhodopsin C1C2](/xray-mp-wiki/proteins/rhodopsins/channelrhodopsin-c1c2/) — Chimeric channelrhodopsin used for structural comparison with Chrimson
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — Chrimson resembles BR in retinal binding pocket architecture
- [FLAG Tag](/xray-mp-wiki/reagents/additives/flag-tag/) — FLAG tag used for affinity purification via ANTI-FLAG M2 Agarose
- [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease/) — Used to cleave EGFP-FLAG tag during purification
- [Phenylmethylsulfonyl Fluoride (PMSF)](/xray-mp-wiki/reagents/additives/pmsf/) — Protease inhibitor (0.1 mM) included in purification buffers
