---
title: Thermus thermophilus SecDF Protein Translocation Motor
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2018.01.002]
verified: false
---

# Thermus thermophilus SecDF Protein Translocation Motor

## Overview

SecDF is a membrane protein belonging to the resistance-nodulation-division (RND) superfamily that enhances protein translocation at the extracytoplasmic side of the bacterial membrane using a proton gradient. It operates as part of the Sec translocon complex, working alongside SecA ATPase and the SecYEG channel to drive protein export. SecDF is the smallest known motor protein of the RND family and consists of 12 transmembrane helices along with flexible extracytoplasmic domains (P1-base, P1-head, and P4). The protein undergoes dramatic conformational transitions between beta-sheet and beta-barrel architectures in its extracellular region, driven by remote coupling between the transmembrane proton transport pathway and the extracytoplasmic domains.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2018.01.002 | 5YHF | 2.8 A | P1 | Thermus thermophilus SecDF residues 1-735 with C-terminal His10 tag; expressed in E. coli BL21(DE3) | None |

## Expression and Purification

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: Thermus thermophilus SecDF(1-735)-His10 from plasmid pTV118N; based on NCBI Reference sequence Gene ID 3168575

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Ni-NTA affinity chromatography | Affinity chromatography (His-tag) | Ni-NTA Agarose | Not specified + DDM | His10-tagged SecDF purified from E. coli membrane fraction |
| Size-exclusion chromatography | Size-exclusion chromatography | Not specified | Tris buffer + 0.01% DDM | Final sample in 0.01% DDM for crystallization |


## Crystallization

### doi/10.1016##j.str.2018.01.002

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase crystallization |
| Protein sample | Purified SecDF mixed with monoolein at 1:1 ratio (w/w) |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Cryocooled to 100 K for X-ray data collection |
| Notes | 5YHF; Super F form; helical data collection at SPring-8 BL32XU; 1.0 A wavelength; space group P1; 44.1-2.8 A resolution (shell 2.9-2.8 A); Rwork/Rfree 0.202/0.236; 734 protein residues; 5790 non-hydrogen atoms; 132 ligand atoms; 27 solvent molecules |


## Biological / Functional Insights

### Super-membrane-facing (Super F) form reveals beta-barrel architecture

The crystal structure of SecDF (PDB 5YHF) reveals a novel conformation termed the Super-membrane-facing (Super F) form, in which the extracytoplasmic P1-base and P4 domains adopt a beta-barrel architecture instead of the beta-sheet structure seen in the previously reported F form (PDB 3AQP) and I form structures. This drastic structural transition represents the most extreme conformational change observed in SecDF to date. The beta-barrel form suggests that the extracellular domain undergoes large-scale rearrangements during the protein translocation cycle, providing a structural basis for understanding how SecDF pulls precursor proteins from the SecYEG translocon.

### Remote coupling mechanism links proton transport to conformational transitions

The Super F form structure reveals a conserved salt bridge between Asp340 in transmembrane helix 4 (TM4) and Arg671 in transmembrane helix 10 (TM10), with their C-alpha-C-alpha distance reduced from 12.9 A in the F form to 2.6 A in the Super F form. Both residues are essential for protein translocation and proton transport activities. Asp340 is proposed to regulate the proton transport pathway depending on its protonation state. The formation of this salt bridge strengthens the interaction between TM4 and TM10 in conserved regions D5 and F2, which in turn induces displacement of conserved regions D1 and F1 toward the transmembrane domain center. This sequential structural change pulls the P1-base and P4 domains toward the center of SecDF, ultimately provoking the beta-sheet to beta-barrel rearrangement. This remote coupling model demonstrates how proton influx through the transmembrane region drives functional extracytoplasmic conformational transitions.

### Conserved transmembrane regions D1, D5, F1, and F2 transmit structural changes

Comparison of the F form and Super F form structures reveals that highly conserved regions D1, D5, F1, and F2 (Eichler, 2003) play an important role in transmitting structural changes from the transmembrane region to the extracytoplasmic side. In the Super F form, the interaction between TM4 and TM10 strengthens in regions D5 and F2, while regions D1 and F1 undergo slight displacement toward the transmembrane domain. These conserved regions are present across the RND superfamily and likely represent a general mechanism for coupling ion transport to substrate translocation in multidrug efflux pumps and the SecDF protein translocation motor.


## Cross-References

- [Thermus thermophilus SecYEG Translocon Complex](/xray-mp-wiki/proteins/secyeg/) — SecDF operates at the extracytoplasmic side of the SecYEG channel to pull precursor proteins during translocation
- [RND Efflux Pumps](/xray-mp-wiki/concepts/rnd-efflux-pumps/) — SecDF belongs to the RND superfamily; this paper provides structural insight into the remote coupling mechanism of RND proteins
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Primary lipid used for LCP crystallization of SecDF (PDB 5YHF)
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method used for SecDF structure determination
