---
title: SaTRIC Channel from Sulfolobus acidocaldarius
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms15103]
verified: false
---

# SaTRIC Channel from Sulfolobus acidocaldarius

## Overview

SaTRIC is a Trimeric Intracellular Cation (TRIC) channel from the archaeon Sulfolobus acidocaldarius. It forms a homotrimeric complex with each monomer containing seven transmembrane helices arranged in a 3+3+1 topology. The channel is permeable to monovalent cations (K+, Na+) and divalent cations (Mg2+, Ca2+). Multiple crystal structures were solved in different ion-bound states, revealing ion-dependent conformational changes in the pore-forming helices and the structural basis for cation selectivity.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms15103 | not specified | 3.1 A | P321 | SaTRIC residues 1-207, L148M/L180M double mutant, Se-Met labeled | not specified |
| doi/10.1038##ncomms15103 | not specified | 1.6 A | P63 | SaTRIC residues 1-207, wild-type, Native | Na+ bound |
| doi/10.1038##ncomms15103 | not specified | 1.8 A | P63 | SaTRIC residues 1-207, wild-type, Native | Mg2+ bound |
| doi/10.1038##ncomms15103 | not specified | 2.4 A | R32 | SaTRIC residues 1-207, wild-type, Native | ion-free |

## Expression and Purification

- **Expression system**: not specified in supplementary tables
- **Construct**: SaTRIC from Sulfolobus acidocaldarius. The crystallization construct covers residues 1-207, encompassing the transmembrane domain. A double mutant L148M/L180M was also prepared for the Type 1 crystal form.


### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein solution | not specified | -- | HEPES 20 mM pH 7.5, NaCl 200 mM + n-DM (n-dodecyl-beta-D-maltoside) 4 mM | Protein solution for Type 1, Type 2a, Type 2b crystallization; for Type 2b RbCl 200 mM replaced NaCl; for Type 3 NaBr 200 mM replaced NaCl |


## Crystallization

### doi/10.1038##ncomms15103

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | SaTRIC residues 1-207 (WT or L148M/L180M mutant) in HEPES 20 mM pH 7.5, NaCl 200 mM, DM 4 mM |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | not specified |
| Notes | Type 1 crystal: Se-Met labeled L148M/L180M mutant. Wavelength 0.97853 A, space group P321, resolution ~3.1 A. |

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | SaTRIC residues 1-207 WT, Native, in HEPES 20 mM pH 7.5, NaCl 200 mM, DM 4 mM |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | not specified |
| Notes | Type 2a crystal: Wild-type, Native. Wavelength 0.97876 A, space group P63, resolution ~1.6 A. Na+ bound structure. |

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | SaTRIC residues 1-207 WT, Native, in HEPES 20 mM pH 7.5, RbCl 200 mM, DM 4 mM |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | not specified |
| Notes | Type 2b crystal: Wild-type, Native. Wavelength 0.81530 A (near Mg K-edge for anomalous), space group P63, resolution ~1.8 A. Mg2+ bound structure. |

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | SaTRIC residues 1-207 WT, Native, in HEPES 20 mM pH 7.5, NaBr 200 mM, DM 4 mM |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | not specified |
| Notes | Type 3 crystal: Wild-type, Native, ion-free. Wavelength 0.91532 A, space group R32, resolution ~2.4 A. Unmodelled density in ion-conducting pore observed. |


## Biological / Functional Insights

### Ion-dependent pore conformations

Four crystal structures of SaTRIC were solved in different ion-bound states, revealing ion-dependent conformational changes in the pore-forming helices. The Na+ bound structure (Type 2a, 1.6 A) shows a distinct conformation compared to the Mg2+ bound structure (Type 2b, 1.8 A) and the ion-free structure (Type 3, 2.4 A). Superposition of Type 2a onto Type 3 reveals r.m.s.d. of 1.67 A for 79 C-alpha atoms in the C-terminal helical bundle (C-THB) and 1.24 A for 78 C-alpha atoms in the N-terminal helical bundle (N-THB), indicating localized conformational changes near the ion binding sites.

### Pore helix re-orientation mechanism

Ion binding triggers re-orientation of the pore-forming helices (TM3/TM6). Comparison of Na+ bound SaTRIC (Type 2a) with Mg2+ bound (Type 2b) and ion-free (Type 3) structures reveals that the TM3 and TM6 helices shift their orientation depending on the bound ion. The ion-free structure shows unmodelled density in the ion-conducting pore, suggesting a partially occluded state. The structural comparison between Type 2a (P63) and Type 3 (R32) crystal forms highlights the flexibility of the pore helices in response to ion occupancy.

### Homotrimeric architecture with N-THB and C-THB domains

Each SaTRIC monomer contains an N-terminal helical bundle (N-THB, helices M1-M3) and a C-terminal helical bundle (C-THB, helices M4-M6), with a standalone M7 helix. The N-THB and C-THB domains show internal symmetry (r.m.s.d. 1.32 A/79 C-alpha in Type 2a; 1.17 A/79 C-alpha in Type 3), consistent with the 3+3+1 topology shared with TRIC-B channels. The trimeric assembly creates three independent ion permeation pathways, one per monomer.

### D99A mutant functional characterization

The SaTRIC D99A mutant was functionally characterized by single-channel electrophysiology. The mutant channel shows almost zero current at +20 mV, indicating that Asp99 plays a critical role in ion permeation. I-V plots for wild-type SaTRIC show ion selectivity preferences: K+ > Rb+ and rejection of divalent cations Ca2+ and Mg2+ in trans chamber assays (210 mM KCl cis vs. 210 mM NaCl/RbCl or 105 mM CaCl2/MgCl2 trans).


## Cross-References

- [CpTRIC Channel from Clostridium perfringens](/xray-mp-wiki/proteins/cp-tric/) — Homologous TRIC channel from C. perfringens; structural comparison between prokaryotic TRIC channels
- [C. elegans TRIC-B1 Channel](/xray-mp-wiki/proteins/tric-b1/) — Eukaryotic TRIC channel homolog; shared 7-TM hourglass architecture and PIP2-dependent gating
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — All four SaTRIC crystal structures solved by LCP method
- [TRIC Channel Gating Mechanism](/xray-mp-wiki/concepts/tric-channel-gating/) — SaTRIC belongs to the TRIC channel family with ion-dependent gating
- [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer component (20 mM, pH 7.5) used in protein solution and crystallization
- [Decylmaltoside (DM)](/xray-mp-wiki/reagents/detergents/decylmaltoside/) — Detergent (4 mM) used throughout SaTRIC protein solutions for stability
