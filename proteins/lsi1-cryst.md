---
title: Rice silicon channel Lsi1 crystallization construct
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-021-26535-x]
verified: false
---

# Rice silicon channel Lsi1 crystallization construct

## Overview

Lsi1 is the Low silicon rice 1 channel, a silicon (Si) uptake transporter from rice (*Oryza sativa*) that belongs to the Nodulin 26-like intrinsic protein (NIP) subfamily of aquaporins. Silicon is the most abundant mineral element in the earth's crust and is especially essential for high and stable rice production, helping plants overcome biotic and abiotic stresses. Lsi1 shows remarkably high selectivity for silicic acid Si(OH)4 over smaller molecules like glycerol. The crystal structure at 1.8 Angstrom resolution reveals unique transmembrane helical orientations, a widely opened hydrophilic selectivity filter composed of five residues (Thr65_TM1/Gly88_TM2/Ser207_TM5/Gly216_LE1/Arg222_LE2), and two Thr residues (Thr65_TM1 and Thr181) that create two polar faces in the channel. Molecular dynamics simulations of silicic acid permeation showed that water molecules Wat3 and Wat9 act as part of the channel lumen, narrowing the channel and strictly selecting the orientation of silicic acid during transport. The structure provides a blueprint for rational design of transgenic crops that specifically take up silicic acid but not carcinogenic arsenite.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-021-26535-x | 7CJS | 1.80 | P 21 21 21 | Lsi1 crystallization construct (residues 47-264) with mutations K50R, C66A, T93V, C139A, K232R, T253V, K264R | none |

## Expression and Purification

- **Expression system**: Sf9 insect cells
- **Construct**: Lsi1 crystallization construct (residues 47-264) with TEV protease cleavage site and octa-His tag, cloned into pFastBac1 vector
- **Notes**: Baculovirus expression system. Functionally active construct discovered by screening N- and C-terminal deletion constructs, point mutations, and Si-permeable AQPs from other organisms.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1 | Cell lysis by sonication | — | 25 mM Tris-HCl pH 8.0, 150 mM NaCl + DDM | Sf9 insect cell membranes solubilized in DDM |
| 2 | Affinity chromatography (Ni-NTA) | Ni-NTA resin | 25 mM Tris-HCl pH 8.0, 150 mM NaCl, 250 mM imidazole + DDM | Octa-His tag purification |
| 3 | Size-exclusion chromatography | — | 20 mM HEPES pH 7.5, 150 mM NaCl + DDM | Final polishing step for crystallization |


## Crystallization

### doi/10.1038##s41467-021-26535-x

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, sitting drop |
| Protein sample | Lsi1_cryst at ~10 mg/mL in 20 mM HEPES pH 7.5, 150 mM NaCl, 0.05% DDM |
| Reservoir | 0.1 M sodium citrate pH 5.5, 0.1 M Li2SO4, 0.1 M NaCl, 20 mM MgCl2, 34% PEG400, 5 mM ATP |
| Temperature | 293 |
| Notes | Crystals diffracted to 1.6 Angstrom but suffered from lattice-translocation defects. X-ray intensities corrected using Wang et al. approach. Structure solved at 1.8 Angstrom resolution. |


## Biological / Functional Insights

### Unique selectivity filter for silicic acid

The Lsi1 selectivity filter (SF) is the widest and most hydrophilic among characterized aquaporins, composed of five residues including a unique fifth residue Thr65_TM1. In canonical aquaporins, a bulky hydrophobic residue in TM2 (Phe in AQP1, Trp in GlpF) shields the equivalent position. In Lsi1, Gly88_TM2 exposes Thr65_TM1 to the channel, creating a wide hydrophilic SF. The two polar faces formed by water molecules Wat3 and Wat9 hydrogen-bonded to Thr65_TM1 provide an energetically preferable environment for the tetrahedral silicic acid molecule. Mutagenesis studies showed that Thr65_TM1 substitutions to Ala, Gly, or Ser were unaffected, but substitutions to Val, Ile, or Cys substantially decreased or abolished transport activity.

### Silicic acid transport mechanism and MD simulations

Molecular dynamics simulations of silicic acid permeation through Lsi1 revealed three structural bottlenecks in the channel, two in the SF region and one near Thr181. Water molecules Wat3, Wat9, and Wat17 stably exist within cavities at these bottlenecks. During silicic acid permeation, Wat3 and Wat9 act as part of the channel lumen, narrowing the channel and strictly selecting the orientation of silicic acid. Wat9 remained bound to its site independently of Si(OH)4 movement (94% occupancy, average exchange time tau = 1.5 ns), while Wat3 (60% occupancy, tau ~ 0.3 ns) and Wat17 (44% occupancy, tau ~ 0.3 ns) were displaced during permeation. The modeled Si2 position in the SF showed all four hydroxyl groups forming hydrogen bonds with channel carbonyls, waters, Ser207_TM5, and Arg222_LE2, compensating for the energetic cost of dehydration.


## Cross-References
