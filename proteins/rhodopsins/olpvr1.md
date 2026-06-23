---
title: "OLPVR1"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-020-19457-7]
verified: false
---

# OLPVR1

## Overview

OLPVR1 is a viral channelrhodopsin from the VR1 group, encoded by the Organic Lake phycodnavirus (OLPV), a nucleocytoplasmic large DNA virus that infects marine phytoplankton. It is a light-gated Na+/K+-selective cation channel that is uniquely impermeable to Ca2+ ions. The 1.4 A resolution crystal structure reveals remarkable differences from known channelrhodopsins, including a unique ion-conducting pathway with intracellular pore formation and absence of prominent extracellular cavities. OLPVR1 represents a distinct group of light-gated channels with potential optogenetic applications due to its lack of Ca2+ permeability.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-020-19457-7 | 7AKX | 1.4 A | P1 | OLPVR1 from Organic Lake phycodnavirus, full-length viral channelrhodopsin | all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal) |
| doi/10.1038##s41467-020-19457-7 | 7AKW | 1.4 A | P21212 | OLPVR1 from Organic Lake phycodnavirus, full-length viral channelrhodopsin | all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal) |
| doi/10.1038##s41467-020-19457-7 | 7AKY | 1.6 A | not specified | OLPVR1 O1O2 mutant | all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal) |

## Expression and Purification

- **Expression system**: Human embryonic kidney (HEK) cells
- **Construct**: Human codon-optimized OLPVR1 gene cloned into pcDNA3.1(-) vector with P2A self-cleavage peptide and fluorescent tag

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | Transfection of HEK cells with codon-optimized OLPVR1 plasmid | -- | Not specified + -- | Codon-optimized OLPVR1 synthesized commercially (Eurofins), cloned into pcDNA3.1(-) vector with P2A self-cleavage peptide and Katushka fluorescent protein at C-terminus |


## Crystallization

### doi/10.1038##s41467-020-19457-7

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | OLPVR1 at 20 mg/ml with 10 mM CaCl2, 10 mM [MGCL2](/xray-mp-wiki/reagents/additives/mgcl2) |
| Temperature | 22 C |
| Growth time | 1 to 4 weeks |
| Cryoprotection | Crystals incubated in precipitant solution for 5 min before data collection |
| Notes | Best crystals obtained with 20 mg/ml protein. Data collected at ESRF beamlines ID30b and ID23-1 using PILATUS 6M detector. Structures solved by molecular replacement using 6SQG structure as search model. |


## Biological / Functional Insights

### Unique ion-conducting pathway with intracellular pore

Unlike other channelrhodopsins, OLPVR1 lacks prominent cavities in the extracellular part. Instead, it has a pore in the intracellular part that ends with a relatively large hydrophilic cavity near the [Retinal](/xray-mp-wiki/reagents/ligands/retinal). The cavity is filled with four water molecules and surrounded by polar residues E44, T87, T88, and W178. Three constriction sites form the putative ion-conductive pathway: intracellular (E44), central (S-E-N triad at E51), and extracellular (R73, E132, K192, N193, N197).

### Ca2+ impermeability distinguishes viral channelrhodopsins

VirChR1 (61% sequence similarity to OLPVR1) is completely impermeable to Ca2+ cations, in contrast to the high Ca2+ conductivity of CrChR2. This Ca2+ impermeability is an important feature that separates VirChR1s from direct competition with chlorophyte channelrhodopsins in optogenetic applications, as it avoids Ca2+-induced noxious side effects.

### Photocycle intermediates lack detectable M-state

Transient absorption measurements revealed three distinct intermediate states: an early decaying K-like state (540 nm), followed by major accumulation of L-like (460 nm) and N-like (560 nm) states lasting about 1.5 s. Unlike other channelrhodopsins, OLPVR1 lacks a detectable M-state that is generally associated with the ion-conducting state. The equilibrium between L-like and N-like states is the major candidate for the ion-conducting state.


## Cross-References

- [Channelrhodopsin C1C2](/xray-mp-wiki/proteins/rhodopsins/channelrhodopsin-c1c2/) — Reference channelrhodopsin structure for comparison of ion-conducting pathway and constriction sites
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — Archetypal microbial rhodopsin; OLPVR1 architecture resembles PR family with different ion pathway
- [All-trans retinal](/xray-mp-wiki/reagents/ligands/retinal/) — Chromophore covalently bound to conserved Lys204 via Schiff base linkage
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid component of the lipidic cubic phase crystallization matrix
- [Tris (Tris-HCl buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Buffer (100 mM, pH 8.2) used in crystallization reservoir
- [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/) — Salt used in electrophysiology experiments to measure Na+ conductivity
- [Calcium Chloride (CaCl2)](/xray-mp-wiki/reagents/additives/calcium-chloride/) — Used in crystallization (10 mM) and to test Ca2+ impermeability in electrophysiology
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used to grow OLPVR1 crystals at 22 C
- [Retinal](/xray-mp-wiki/reagents/ligands/retinal) — Entity mentioned in text
- [PEG](/xray-mp-wiki/reagents/additives/peg) — Entity mentioned in text
