---
title: "BsYetJ TMBIM Ca2+ Channel"
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2014.03.045, doi/10.1016##j.str.2019.03.003, doi/10.1126##science.1252043]
verified: false
---

# BsYetJ TMBIM Ca2+ Channel

## Overview

BsYetJ is a transmembrane Bax inhibitor motif (TMBIM) protein from Bacillus subtilis that functions as a pH-sensitive Ca2+ leak channel. BsYetJ contains seven transmembrane helices (TMs) with the second TM (TM2) capable of lateral movement within the membrane bilayer to open and close the channel pore. A conserved aspartyl dyad (Asp171-Asp195) serves as the pH sensor that regulates Ca2+ flux through the channel. Protonation of Asp171 triggers Arg60 disengagement and TM2 rearrangement, leading to pore opening. BsYetJ mediates Ca2+ efflux from eukaryotic intracellular stores and is sensitive to protons, monovalent cations (Na+, K+, Li+), and lanthanide ions (Gd3+, Yb3+, Lu3+).

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2019.03.003 | 6NQ7 | 2.5 A | P21 | Wild-type BsYetJ (Delta5BsYetJ, N-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) of 5 residues), 7 transmembrane helices crystallized in lipidic cubic phase (LCP) with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/); closed conformation | Ca2+ binding site formed by Asp171-Asp195 dyad; Arg60 conformation latch |
| doi/10.1016##j.str.2019.03.003 | 6NQ8 | 3.1 A | C2 | D171E BsYetJ mutant (Asp171 to Glu), N-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) (Delta5BsYetJ), 7 transmembrane helices; open conformation with TM2 unlocked | D171E mutation disrupting pH-sensing dyad |
| doi/10.1016##j.str.2019.03.003 | 6NQ9 | 3.1 A | C2 | D195E BsYetJ mutant (Asp195 to Glu), N-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) (Delta5BsYetJ), 7 transmembrane helices; open conformation with TM2 unlocked | D195E mutation disrupting pH-sensing dyad |
| doi/10.1016##j.cell.2014.03.045 | 4PGR | 2.8 A | P212121 | Wild-type BsYetJ (C10E5BsYetJ), N-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/), 7 transmembrane helices crystallized in detergent C10E5; closed conformation | Ca2+ binding site formed by Asp171-Asp195 dyad |
| doi/10.1016##j.cell.2014.03.045 | 4PGS | 2.8 A | P212121 | Wild-type BsYetJ at pH 6 (C10E5BsYetJ), N-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/), 7 transmembrane helices; closed conformation | Protonated state of Asp171-Asp195 dyad at low pH |
| doi/10.1126##science.1252043 | 4PGR | 2.50 | P6,22 | Full-length BsYetJ, form-1 hexagonal crystals grown at pH 8. Closed conformation. Intracrystalline transition by soaking at pH 6 opens the pore. Reversible back-soaking to pH 8 recloses. | Di-aspartyl pH sensor Asp171-Asp195; Arg60 latch |
| doi/10.1126##science.1252043 | 4PGR | Not specified | C222,1 | Full-length BsYetJ, form-2 orthorhombic crystals grown at pH 6. Open conformation with TM2 displaced 13.5 A. | Protonated Asp171, disrupted Arg60-Asp171 salt bridge |
| doi/10.1126##science.1252043 | 4PGR | Not specified | P6,22 | Full-length BsYetJ at pH 7 (back-soaked from pH 6 to pH 7). Mixed 60:40 closed:open conformation. TM2 modeled in two alternative conformations. | Equilibrium state with 60% closed, 40% open conformation |

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

### Reversible pH-driven conformational transition

The BsYetJ pore can be reversibly opened and closed by pH changes in crystallo. Form-1 crystals (pH 8, closed, space group P6,22, c ~289 A) shrink upon soaking at pH 6 (c ~276 A), opening the pore. Back-soaking to pH 8 restores the original closed conformation (c ~293 A). At pH 7, a mixed 60:40 closed:open equilibrium is observed, with the apparent pKa of the transition estimated slightly below pH 7. This reversible pH-driven gating is intrinsic to the BsYetJ protein, as demonstrated by pH-dependent Ca2+ influx in pure proteoliposome systems.

### Seven-transmembrane triple-helix sandwich fold

BsYetJ adopts a novel 7-TM fold distinct from GPCRs and CAAX proteases. The structure comprises two triple-helix sandwich substructures (TM1-3 and TM4-6) wrapped around a central C-terminal helix (TM7). TM1-3 and TM4-6 are superimposable when inverted by pseudo-twofold symmetry, despite no detectable sequence similarity. TM7 occupies the central position (analogous to TM3 in GPCRs) and forms extensive interactions with other helices, including the conserved di-aspartyl pH sensor. Short side-chain hydrophobic residues at the sticky patches enable close TM1-TM3 and TM4-TM6 clamping contacts.

### pH-sensitive calcium leak in proteoliposomes

Purified BsYetJ reconstituted into proteoliposomes shows pH-dependent calcium influx measured by Fura-2 fluorescence. Steady-state calcium influx is maximal at near-neutral pH (7.0-7.4) and substantially lower at pH 6.5 or pH 7.9. The bell-shaped pH dependence correlates with the conformational equilibrium: at low pH, the di-aspartyl sensor is protonated and the pore is open but less electronegative; at high pH, the pore is closed. The maximal activity at physiological pH supports a model where TMBIM proteins function as Ca2+ leak channels that maintain calcium homeostasis in intracellular stores.


## Cross-References

- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for BsYetJ solubilization and purification
- [Lauryldimethylamine N-oxide (LDAO)](/xray-mp-wiki/reagents/detergents/ldao/) — Alternative detergent used for BsYetJ solubilization
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid matrix used for LCP crystallization of wild-type BsYetJ (6NQ7)
- [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease/) — Protease used for His-tag removal from BsYetJ construct
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used to crystallize BsYetJ in native-like lipid environment
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Phasing method used to solve BsYetJ structures
- [NavAb Bacterial Voltage-Gated Sodium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) — Related bacterial ion channel with structural insights into ion selectivity
- [Channel Gating via Plug Domain Displacement](/xray-mp-wiki/concepts/transport-mechanisms/channel-gating/) — BsYetJ pore opening mechanism involves TM2 rearrangement analogous to gating
- [GR (Halobacterium sp. GR Bacteriorhodopsin)](/xray-mp-wiki/proteins/rhodopsins/gr/) — Related protein structure
- [NavAb Bacterial Voltage-Gated Sodium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) — Related protein structure
