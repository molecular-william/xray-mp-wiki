---
title: "BcXeR (Xenorhodopsin from Bacillus coahuilensis)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41594-023-01020-9]
verified: false
---

# BcXeR (Xenorhodopsin from Bacillus coahuilensis)

## Overview

BcXeR is a light-driven inward proton pump (xenorhodopsin) from Bacillus coahuilensis, belonging to the bacterial xenorhodopsin (XeR) clade of microbial rhodopsins. It is the only alternative optogenetic tool to channelrhodopsins for neuronal activation, functioning as an inwardly directed proton pump. This comprehensive function-structure study presents true-atomic-resolution structures (1.6-1.7 A) of BcXeR in the ground, L intermediate, and M intermediate states, captured by cryotrapping and time-resolved serial crystallography at a synchrotron source with sub-millisecond resolution (500 us to 250 ms). The structures reveal that inward proton translocation is based on proton wires regulated by internal gates. A water-mediated hydrogen-bond chain (proton wire) connects the retinal Schiff base (RSB) to the cytoplasmic proton transfer group (PTG, comprising D214, E34, and T88) in the L state. The M state shows RSB deprotonation, sodium dissociation from the PTG, and restoration of the hydrophobic gate, enabling unidirectional proton translocation to the cytoplasm. The extracellular side features a separate proton wire for RSB reprotonation from the extracellular bulk. The results establish a general concept of proton translocation through microbial rhodopsins, with sequential gate opening distinguishing inward pumps from channelrhodopsins where all gates open simultaneously.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41594-023-01020-9 | 7ZMY | 1.6 | P212121 | Ground state at pH 8.2 (100 K) | all-trans [retinal](/xray-mp-wiki/reagents/ligands/retinal/) |
| doi/10.1038##s41594-023-01020-9 | 7ZN3 | 1.6 | P212121 | L intermediate state at pH 8.2 (100 K, cryotrapped) | 13-cis retinal |
| doi/10.1038##s41594-023-01020-9 | 7ZN0 | 1.7 | P212121 | M intermediate state at pH 8.2 (100 K, cryotrapped) | 13-cis retinal (deprotonated RSB) |
| doi/10.1038##s41594-023-01020-9 | 7ZN8 | 1.6 | P212121 | Ground state at pH 7.0 (100 K) | all-trans retinal |
| doi/10.1038##s41594-023-01020-9 | 7ZN9 | 1.6 | P212121 | M state at pH 7.0 (100 K) | 13-cis retinal (deprotonated RSB) |
| doi/10.1038##s41594-023-01020-9 | 7ZNA | 1.7 | P212121 | Ground state at pH 5.2 (100 K) | all-trans retinal |
| doi/10.1038##s41594-023-01020-9 | 7ZNB | 1.7 | P212121 | M state at pH 5.2 (100 K) | 13-cis retinal (deprotonated RSB) |
| doi/10.1038##s41594-023-01020-9 | 7ZNC | 1.7 | P212121 | Ground state at pH 7.6, no sodium (100 K) | all-trans retinal |
| doi/10.1038##s41594-023-01020-9 | 7ZND | 1.7 | P212121 | M state at pH 7.6, no sodium (100 K) | 13-cis retinal (deprotonated RSB) |
| doi/10.1038##s41594-023-01020-9 | 7ZNE | 2.1 | P212121 | Ground state at pH 8.2 (293 K, 7.5-ms exposure, serial crystallography) | all-trans retinal |
| doi/10.1038##s41594-023-01020-9 | 7ZNI | 2.2 | P212121 | M state at pH 8.2 (293 K, 7.5-15-ms snapshot, serial crystallography) | 13-cis retinal (deprotonated RSB) |
| doi/10.1038##s41594-023-01020-9 | 7ZNG | 2.3 | P212121 | Ground state at pH 8.2 (293 K, 500-us exposure, serial crystallography) | all-trans retinal |
| doi/10.1038##s41594-023-01020-9 | 7ZNH | 2.3 | P212121 | L state at pH 8.2 (293 K, 250-750-us snapshot, serial crystallography) | 13-cis retinal |

## Expression and Purification

- **Expression system**: Escherichia coli (codon-optimized gene)
- **Construct**: BcXeR with C-terminal 6xHis tag in pET15b

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell growth and membrane preparation | E. coli cells transformed with pET15b-BcXeR, grown in autoinducing medium ZYP-5052 at 37 C with 10 mg/L ampicillin. Induced at OD600 0.6-0.7 with 1 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/). 10 uM all-trans retinal added. Cells disrupted in M-110P Lab Homogenizer at 25,000 psi in lysis buffer. Membrane fraction isolated by ultracentrifugation at 125,000g for 1 hr at 4 C. | -- | 20 mM [Tris-HCl](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 5% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.5% Triton X-100, 50 mg/L DNase I + 0.5% Triton X-100 | Cells grown in shaking baffled flasks. Membranes collected by ultracentrifugation |
| Solubilization | Membrane pellet resuspended in solubilization buffer and stirred overnight at 4 C. Insoluble fraction removed by ultracentrifugation at 125,000g for 1 hr at 4 C. | -- | 50 mM NaH2PO4/Na2HPO4 pH 7.5, 0.15 M [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Solubilized overnight for complete extraction |
| [Affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Supernatant loaded on Ni-NTA column, washed, eluted with 0.4 M imidazole | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta/) (Qiagen) | 50 mM NaH2PO4/Na2HPO4 pH 7.5, 0.15 M [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 0.4 M [imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Eluted with imidazole gradient |
| [Size-exclusion chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | Eluate subjected to SEC on 125-ml [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) PG column | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) PG (GE Healthcare) | 50 mM NaH2PO4/Na2HPO4 pH 7.5, 0.15 M [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Final purification step |


## Crystallization

### doi/10.1038##s41594-023-01020-9

| Parameter | Value |
|---|---|
| Method | [Lipidic cubic phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) (LCP) crystallization |
| Protein sample | 20 mg/mL BcXeR (in water part of mesophase) mixed with [monoolein](/xray-mp-wiki/reagents/lipids/monoolein/)-based LCP |
| Temperature | 22 C |
| Growth time | ~2 months |
| Cryoprotection | Crystals collected using micromounts, flash-cooled and stored in liquid nitrogen |
| Notes | Crystals grown in 96-well LCP glass sandwich plates. Best crystals obtained with 0.8 M Na/K-Pi pH 8.2. For pH 5.2 structures, crystals soaked 24 hr in 1.2 M Na/K-Pi pH 5.2 (buffer exchanged 3 times). For time-resolved serial crystallography, crystals grown in PCR tubes, reaching 30 x 20 x 5 um3. Space group P212121 for all structures. Unit cell: a ~68.2-69.1, b ~109.4-111.9, c ~118.5-119.6 A. Data collected at PETRAIII P14 beamline. Structures solved by molecular replacement using Anabaena sensory rhodopsin (PDB 1XIO) as search model. |


## Biological / Functional Insights

### Proton wire mechanism for inward translocation

In BcXeR, inward proton translocation proceeds via two proton wires (water-mediated H-bond chains) on opposite sides of the retinal Schiff base (RSB). In the L state, a cytoplasmic proton wire forms between the RSB and the proton transfer group (PTG, residues D214, E34, T88) via three water molecules (Wat501, Wat503, Wat504). The PTG acts as a proton storage site, with E34 reorienting toward the cytoplasm in the M state as sodium dissociates. A separate extracellular proton wire connects the RSB to a water-filled concavity exposed to the extracellular bulk for RSB reprotonation. Proton wires serve as both selectivity filters and translocation pathways.

### Sequential gate opening enables unidirectional transport

BcXeR employs a cavity-gate-cavity-gate architecture with two gates that open sequentially to ensure unidirectional transport. In the ground state, a hydrophobic gate (between L81 and F210) blocks the cytoplasmic pathway. In the L state, this gate opens as L81 reorients, allowing water molecules to enter and form the proton wire. The extracellular gate near Y49 weakens in the M state, permitting RSB reprotonation. Unlike channelrhodopsins where all gates open simultaneously (producing a channel), BcXeR gates open sequentially, enabling proton pumping against the concentration gradient.

### Structural rearrangements in the photocycle

The BcXeR photocycle involves: (1) Ground-to-L transition: retinal isomerization from all-trans to 13-cis, 180-degree flip of W173 to avoid steric clash with C20, L136 reorientation toward the lipid membrane, and formation of the cytoplasmic proton wire as L81 reorients. (2) L-to-M transition: RSB deprotonation, hydrophobic gate restoration (L81 returns to ground position), sodium dissociation from the PTG, E34 reorientation toward cytoplasm. The extracellular side shows minor rearrangements with two water molecules (Wat402, Wat403) appearing in the M state to establish a continuous H-bond chain for RSB reprotonation.

### Sodium binding at the proton transfer group

The PTG binds a sodium ion in the ground and L states at cryogenic temperatures, coordinated by D214, E34, T88, and the carbonyl oxygen of A84 (mean Na-O distance 2.4 A). This sodium-bound conformation reflects the deprotonated state of the PTG. In the M state, sodium dissociates, E34 flips toward the cytoplasm, and an additional water molecule appears. The sodium-free PTG conformation may represent either the protonated or deprotonated form, as they are structurally indistinguishable at 2 A resolution.

### Time-resolved serial crystallography at a synchrotron

This study demonstrates the use of time-resolved serial crystallography at a synchrotron (PETRAIII P14) with sub-millisecond resolution (500 us) for rhodopsin studies. L state and M state intermediates were captured at room temperature in 250-750 us and 7.5-15 ms snapshots, respectively. The data reveal the evolution of structural rearrangements during the photocycle. Cryotrapped intermediate structures at 100 K provide complementary higher-resolution (1.6-1.7 A) models. This opens the door for time-resolved structural studies of other rhodopsins at synchrotron sources.

### The proton-wire mechanism is fundamental to microbial rhodopsins

Comparison with bacteriorhodopsin (HsBR) reveals that both outward and inward proton pumps use proton wires as core mechanisms. In BcXeR, only minor reorganization of proton wires with sequential gate opening is sufficient for inward proton translocation. Phylogenetic analysis suggests the proton-wire mechanism is characteristic not only of bacterial xenorhodopsins but also of archaeal rhodopsins. Mutational analysis confirms that residues in the proton wire and gates are critical for function, providing a framework for engineering faster XeR variants for optogenetic applications.


## Cross-References

- [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) — Chromophore covalently bound to the protein via Schiff base
- [Rhodopsin Photocycle](/xray-mp-wiki/concepts/rhodopsin-mechanisms/rhodopsin-photocycle/) — BcXeR exhibits a photocycle with K, L, and M intermediate states
- [Retinal Chromophore Conformation](/xray-mp-wiki/concepts/structural-mechanisms/retinal-chromophore-conformation/) — Retinal isomerization from all-trans to 13-cis drives the photocycle
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — BcXeR crystallized in monoolein-based LCP
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid used for LCP crystallization matrix
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for BcXeR purification
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Used via Ni-NTA for purification
- [Nickel-NTA](/xray-mp-wiki/reagents/additives/nickel-nta/) — Affinity resin for His-tag purification
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Used for elution in affinity chromatography
- [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/) — Salt used in purification buffers
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Buffer used in membrane preparation
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Used in purification buffers as stabilizer
- [IPTG](/xray-mp-wiki/reagents/additives/iptg/) — Used for induction of protein expression
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Final polishing step in purification
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — Archetypal outward proton pump for comparison of proton wire mechanisms
