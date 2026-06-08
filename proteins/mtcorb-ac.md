---
title: MtCorB Delta-C from Methanoculleus thermophilus
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-021-24282-7]
verified: false
---

# MtCorB Delta-C from Methanoculleus thermophilus

## Overview

MtCorB Delta-C is a CNNM/CorB family magnesium transporter from the thermophilic archaeon *Methanoculleus thermophilus*. CNNM/CorB proteins are a broadly conserved family of integral membrane proteins implicated in Mg2+ homeostasis and divalent cation transport, with mutations in human CNNM proteins linked to genetic diseases including hypomagnesemia and Jalili syndrome. This archaeal ortholog shares 26% sequence identity to the conserved core of human CNNM2. The structure was determined in two conformations: an Mg2+-ATP bound state and an apo state (via a disease-mimicking R235L mutant homologous to the human CNNM4 Jalili syndrome mutant R407L). The transmembrane domain exists in an inward-facing conformation with a negatively charged cavity and a conserved pi-helical turn that coordinates a Mg2+ ion. The CBS-pair domain undergoes major conformational rearrangements upon Mg2+-ATP binding, switching from an elongated dimeric configuration to a disc-like dimeric form. Functional liposome-based assays demonstrated direct Mg2+ transport by CorB proteins through an electroneutral antiporter mechanism.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-021-24282-7 | 7MSU | 1.60 | P 1 21 1 | MtCorB CBS-pair domain (residues 199-322) in complex with Mg2+-ATP | Mg2+-ATP |
| doi/10.1038##s41467-021-24282-7 | 7M1T | 3.25 | C 1 21 1 | MtCorB Delta-C Delta-loop (residues 5-322) in complex with Mg2+-ATP | Mg2+-ATP, UDM |
| doi/10.1038##s41467-021-24282-7 | 7M1U | 3.80 | P 1 21 1 | MtCorB Delta-C R235L mutant (residues 5-322) in apo state | none |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: MtCorB Delta-C (residues 1-322, C-terminal CorC domain deletion) with internal loop deletion
- **Notes**: Codon-optimized cDNA subcloned into pET29a vector with C-terminal His6-tag. Expressed in E. coli and purified in DDM, optimized to UDM for crystallization.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1 | Cell lysis by sonication | — | 50 mM Tris-HCl pH 7.0, 0.5 mM Na-EDTA, 1 mM MgCl2 + DDM | Membrane fraction collected by ultracentrifugation |
| 2 | Affinity chromatography (Ni-NTA) | Ni-NTA Superflow (Qiagen) | 50 mM Tris-HCl pH 7.0, 300 mM NaCl, 250 mM imidazole + 0.05% UDM | His6-tag purification |
| 3 | Size-exclusion chromatography | — | 20 mM HEPES pH 7.5, 150 mM NaCl + 0.05% UDM | Final purification step for crystallization |


## Crystallization

### doi/10.1038##s41467-021-24282-7

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, sitting drop |
| Protein sample | 20 mg/mL MtCorB Delta-C Delta-loop in 20 mM HEPES pH 7.5, 150 mM NaCl, 0.05% UDM, 5 mM Mg2+-ATP |
| Reservoir | 0.1 M sodium citrate pH 5.5, 0.1 M Li2SO4, 0.1 M NaCl, 20 mM MgCl2, 34% PEG400, 5 mM ATP |
| Temperature | 293 |
| Notes | Crystals of 7M1T obtained after construct and detergent optimization |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, sitting drop |
| Protein sample | 20 mg/mL MtCorB Delta-C R235L mutant in 20 mM HEPES pH 7.5, 150 mM NaCl, 0.05% UDM |
| Reservoir | 0.1 M sodium citrate pH 5.5, 50 mM Li2SO4, 11% PEG4000, 10 mM MgSO4 |
| Temperature | 293 |
| Notes | Apo state captured via disease-mimicking R235L mutant |


## Biological / Functional Insights

### Mg2+-ATP sensing and transport mechanism

MtCorB demonstrates a rocker-switch transport mechanism. In the apo state, the CBS-pair domain adopts an elongated dimeric configuration and the acidic helical bundle (AHB) dissociates, forming a CBS-TMD contact that locks the transmembrane domain in the inward-facing conformation, inactivating the transporter. Upon Mg2+-ATP binding, the CBS-pair domain switches to a disc-like dimeric configuration, disrupting the CBS-TMD contact and allowing the transporter to transition to other conformational states required for Mg2+ transport. The Mg2+ ion in the transmembrane cavity is coordinated by Ser21, Ser25, Ser71, Glu111, and main-chain carbonyls of Ser21 and Gly110. A conserved pi-helical turn in TM3 (involving Pro114) is essential for transport activity.

### Direct Mg2+ transport by CorB proteins

Liposome-based Mg2+ transport assays with mag-fura-2 demonstrated that CorB proteins mediate direct Mg2+ transport, resolving a longstanding debate in the field. The transport occurs through an electroneutral antiporter mechanism, as shown by the lack of valinomycin-sensitive enhancement (unlike the electrogenic CorA channel). Mutations near the pi-helical turn (S117A, E118A, P121G, K122A) consistently reduced transport activity, while mutations in the Mg2+ binding site (S26A, S30A, N76A) increased activity.


## Cross-References
