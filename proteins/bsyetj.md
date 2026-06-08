---
title: BsYetJ TMBIM Ca2+ Channel
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2014.03.045, doi/10.1016##j.str.2019.03.003]
verified: false
---

# BsYetJ TMBIM Ca2+ Channel

## Overview

BsYetJ is a transmembrane Bax inhibitor motif (TMBIM) protein from Bacillus subtilis that functions as a pH-sensitive Ca2+ leak channel. BsYetJ contains seven transmembrane helices (TMs) with the second TM (TM2) capable of lateral movement within the membrane bilayer to open and close the channel pore. A conserved aspartyl dyad (Asp171-Asp195) serves as the pH sensor that regulates Ca2+ flux through the channel. Protonation of Asp171 triggers Arg60 disengagement and TM2 rearrangement, leading to pore opening. BsYetJ mediates Ca2+ efflux from eukaryotic intracellular stores and is sensitive to protons, monovalent cations (Na+, K+, Li+), and lanthanide ions (Gd3+, Yb3+, Lu3+).

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2019.03.003 | 6NQ7 | 2.5 A | P21 | Wild-type BsYetJ (Delta5BsYetJ, N-terminal truncation of 5 residues), 7 transmembrane helices crystallized in lipidic cubic phase (LCP) with monoolein; closed conformation | Ca2+ binding site formed by Asp171-Asp195 dyad; Arg60 conformation latch |
| doi/10.1016##j.str.2019.03.003 | 6NQ8 | 3.1 A | C2 | D171E BsYetJ mutant (Asp171 to Glu), N-terminal truncation (Delta5BsYetJ), 7 transmembrane helices; open conformation with TM2 unlocked | D171E mutation disrupting pH-sensing dyad |
| doi/10.1016##j.str.2019.03.003 | 6NQ9 | 3.1 A | C2 | D195E BsYetJ mutant (Asp195 to Glu), N-terminal truncation (Delta5BsYetJ), 7 transmembrane helices; open conformation with TM2 unlocked | D195E mutation disrupting pH-sensing dyad |
| doi/10.1016##j.cell.2014.03.045 | 4PGR | 2.8 A | P212121 | Wild-type BsYetJ (C10E5BsYetJ), N-terminal truncation, 7 transmembrane helices crystallized in detergent C10E5; closed conformation | Ca2+ binding site formed by Asp171-Asp195 dyad |
| doi/10.1016##j.cell.2014.03.045 | 4PGS | 2.8 A | P212121 | Wild-type BsYetJ at pH 6 (C10E5BsYetJ), N-terminal truncation, 7 transmembrane helices; closed conformation | Protonated state of Asp171-Asp195 dyad at low pH |

## Expression and Purification

No purification described.

## Crystallization

No crystallization described.

## Biological / Functional Insights

### pH-dependent Ca2+ channel gating via Asp171-Asp195 dyad

The conserved aspartyl dyad (Asp171-Asp195) serves as the central pH sensor regulating Ca2+ flux through BsYetJ. In the closed state, Asp171 forms a strong salt bridge with Arg60, locking TM2 in place against TM6. Protonation of Asp171 at low pH disrupts this salt bridge, causing TM2 to move downward and away from TM6, opening the Ca2+ pore. The pH dependence of Ca2+ binding follows a bell-shaped curve with a peak at pH 7.46 +/- 0.01, as measured by scintillation proximity assay (SPA). The wild-type EC50 for Ca2+ binding is 65.4 +/- 0.9 uM at pH 7.5.

### Ion selectivity and cation sensitivity

BsYetJ Ca2+ binding is inhibited by monovalent cations (Na+, K+, Li+) at physiological concentrations, suggesting these ions may regulate basal channel activity. Divalent ions Mg2+ and Mn2+ show no apparent inhibition, indicating selectivity for Ca2+ based on ionic size. Lanthanide ions Gd3+, Yb3+, and Lu3+ inhibit Ca2+ binding, with Gd3+ having the strongest inhibitory potency (IC50 = 24.2 +/- 2.8 uM). The inhibitory effects of these lanthanides suggest they may act as Ca2+ surrogates of similar ionic radius, binding to the proposed Ca2+ binding site.

### Functional Ca2+ flux in mammalian cells

BsYetJ mediates Ca2+ efflux from the endoplasmic reticulum in permeabilized HeLa cells loaded with 45Ca2+. At 2.5 uM, BsYetJ releases Ca2+ from ER stores, demonstrating that the bacterial protein can function in a eukaryotic cellular context. This inter-kingdom functional complementation suggests that all TMBIM proteins likely possess Ca2+ flux activity and share a similar ion-recognition pattern.

### Molecular dynamics of the conformational latch mechanism

MD simulations reveal that in the Asp171-deprotonated state, Asp171 and protonated Asp195 form a stable dyad, and Asp171 persistently forms a strong salt bridge with Arg60. Protonation of Asp171 disrupts the Arg60-Asp171 salt bridge and alters the dyad conformation, causing TM2 to move downward and away from TM6 toward the open state. The D171E mutation, while retaining negative charge, results in a less optimal dyad with Asp195 and a slight TM2 rearrangement. The D171E mutant EC50 for Ca2+ binding is 1.2 +/- 0.1 mM, and D195E is 1.7 +/- 0.3 mM, both significantly reduced compared to wild-type.


## Cross-References

- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for BsYetJ solubilization and purification
- [Lauryldimethylamine N-oxide (LDAO)](/xray-mp-wiki/reagents/detergents/lDAO/) — Alternative detergent used for BsYetJ solubilization
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid matrix used for LCP crystallization of wild-type BsYetJ (6NQ7)
- [TEV Protease](/xray-mp-wiki/reagents/protein-tags/tevp-protease/) — Protease used for His-tag removal from BsYetJ construct
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used to crystallize BsYetJ in native-like lipid environment
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Phasing method used to solve BsYetJ structures
- [NavAb Bacterial Voltage-Gated Sodium Channel](/xray-mp-wiki/proteins/navab/) — Related bacterial ion channel with structural insights into ion selectivity
- [Channel Gating via Plug Domain Displacement](/xray-mp-wiki/concepts/channel-gating/) — BsYetJ pore opening mechanism involves TM2 rearrangement analogous to gating
