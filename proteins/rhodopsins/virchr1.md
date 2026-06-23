---
title: VirChR1
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-020-19457-7]
verified: false
---

# VirChR1

## Overview

VirChR1 is a viral channelrhodopsin from the VR1 group, encoded by TARA-146-SRF-0.22-3-C376786_1, a nucleocytoplasmic large DNA virus infecting marine algae. It is a light-gated Na+/K+-selective cation channel that is uniquely impermeable to Ca2+ ions, distinguishing it from all known channelrhodopsins. VirChR1 shares 61% sequence similarity with [OLPVR1](/xray-mp-wiki/proteins/rhodopsins/olpvr1/) and was functionally characterized in HEK293S and SH-SY5Y cells. Upon illumination, VirChR1 depolarizes cell membranes to drive neural firing, making it a promising optogenetic tool for remote control of Ca2+-dependent processes without Ca2+-induced noxious side effects.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-020-19457-7 | not solved (functional characterization only) | not solved | not solved | Human codon-optimized VirChR1 with P2A self-cleavage peptide and Katushka fluorescent protein | all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) |

## Expression and Purification

- **Expression system**: Human embryonic kidney (HEK293S) and SH-SY5Y human neuroblastoma cells
- **Construct**: Human codon-optimized VirChR1 gene cloned into pcDNA3.1(-) vector with P2A self-cleavage peptide and Katushka fluorescent protein at C-terminus, N-terminal Hemagglutinin and [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | Transfection of HEK293S cells with pcDNA3.1_VirChR1_TS_P2A_Katushka plasmid | -- | Not specified + -- | Cells cultured at 37 C with 5% CO2. Electrophysiological experiments performed 16-24 h after transfection |


## Crystallization

### doi/10.1038##s41467-020-19457-7

| Parameter | Value |
|---|---|
| Method | Not crystallized (functional characterization only) |
| Protein sample | Not applicable |
| Reservoir | Not applicable |
| Temperature | Not applicable |
| Notes | VirChR1 was not crystallized; functional characterization performed via electrophysiology in SH-SY5Y cells. The 1.4 A structure of [OLPVR1](/xray-mp-wiki/proteins/rhodopsins/olpvr1/) (61% sequence similarity) was used as structural model. |


## Biological / Functional Insights

### Na+/K+-selective cation channel impermeable to Ca2+

Whole-cell patch-clamp recordings revealed that VirChR1 conducts Na+ and K+ ions with PK+ approximately 0.5 times PNa+. It is completely impermeable to Ca2+ — replacing 110 mM NaCl with 80 mM CaCl2 completely abolished the photocurrent. The reversal potential was 25 +/- 6 mV, confirming passive cation conductance. Action spectrum showed maximum sensitivity near 500 nm. Tau-off was 155 +/- 5 ms.

### Light-driven neural firing in neurons

VirChR1 expressed in primary hippocampal neurons enabled light-driven neural spiking. 80 ms light pulses at 1 Hz elicited action potentials with median latency of approximately 10 ms. This demonstrates that VirChR1 can depolarize neuronal membranes sufficiently to drive action potentials, establishing its utility as an optogenetic tool.

### Distinct photocycle intermediates

[OLPVR1](/xray-mp-wiki/proteins/rhodopsins/olpvr1/) (61% similar to VirChR1) shows three distinct photocycle intermediates: K-like (540 nm, early decaying), L-like (460 nm), and N-like (560 nm, lasting about 1.5 s). Unlike other channelrhodopsins, [OLPVR1](/xray-mp-wiki/proteins/rhodopsins/olpvr1/) lacks a detectable M-state. The equilibrium between L-like and N-like states is the major candidate for the ion-conducting state. This unique photocycle is characteristic of VR1 group viral channelrhodopsins.


## Cross-References

- [Channelrhodopsin C1C2](/xray-mp-wiki/proteins/rhodopsins/channelrhodopsin-c1c2/) — Reference channelrhodopsin for comparison of ion selectivity and photocycle
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — Archetypal microbial rhodopsin; VirChR1/OLPVR1 are distinct channelrhodopsins not pumps
- [All-trans retinal](/xray-mp-wiki/reagents/ligands/retinal/) — Chromophore required for photoactivation of VirChR1
- [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer (10 mM, pH 7.4) used in electrophysiology bath solution
- [EGTA](/xray-mp-wiki/reagents/additives/egta/) — Calcium chelator (10 mM) used in electrophysiology pipette solution
- [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/) — Salt (110 mM) in standard bath solution for electrophysiology
- [Calcium Chloride (CaCl2)](/xray-mp-wiki/reagents/additives/calcium-chloride/) — Used to demonstrate Ca2+ impermeability (80 mM CaCl2 abolished photocurrent)
- [Whole-Cell Patch-Clamp Recording](/xray-mp-wiki/methods/structure-determination/two-electrode-voltage-clamp/) — Electrophysiology method used to characterize VirChR1 ion channeling activity
- [OLPVR1](/xray-mp-wiki/proteins/rhodopsins/olpvr1/) — Related protein structure
- [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) — Related ligand or cofactor
