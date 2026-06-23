---
title: Acetabularia Rhodopsin II
created: 2026-05-26
updated: 2026-05-26
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2011.06.028]
verified: false
---

# Acetabularia Rhodopsin II

## Overview

Acetabularia rhodopsin II (ARII) is a light-driven proton pump from the marine alga Acetabularia acetabulum, representing the first crystal structure of a eukaryotic member of the microbial rhodopsin family. The protein was expressed using an E. coli cell-free protein synthesis system and crystallized by the lipidic mesophase (in meso) method at 3.2 A resolution. ARII shares structural similarity with [bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) but exhibits a reversed proton uptake/release sequence and lacks dark-light adaptation.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2011.06.028 | 3AM6 | 3.2 A | P212121 | ARII opsin, 247 amino acid residues, N11-tag at N-terminus (not removed) | Retinal (all-trans), Cholesterol (8 molecules in asymmetric unit) |

## Expression and Purification

- **Expression system**: E. coli cell-free protein synthesis system (supplemented with 0.4% digitonin and 6.7 mg/ml phosphatidylcholine)
- **Construct**: N11-tag (modified histidine tag) at N-terminus, not removed after purification; 247 amino acid residues (gene truncated at position 229)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell-free synthesis | Cell-free protein synthesis | -- | Cell-free reaction mixture with 0.4% [digitonin](/xray-mp-wiki/reagents/detergents/digitonin/) and 6.7 mg/ml phosphatidylcholine + 0.4% digitonin | Yield of 4.5 mg from a 27-ml reaction. Synthesis performed in presence of both lipid and detergent, enabling high target protein content in liposomes. |
| Ni2+ chelating affinity chromatography | [Affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni2+ chelating resin | 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/)-HCl (pH 7.0), 400 mM [sodium chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/) | Modified N11-tag at N-terminus used for purification; tag not removed. |
| Gel filtration chromatography | [Size-exclusion chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | Gel filtration column | 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/)-HCl (pH 7.0), 400 mM [sodium chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 1 mM dithiothreitol, 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 0.01% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Final fractions concentrated to 45.4 mg/ml with a filter unit for crystallization. Absorption ratio at 280/532 nm was 1.34. |


## Crystallization

### doi/10.1016##j.jmb.2011.06.028

| Parameter | Value |
|---|---|
| Method | [Lipidic cubic phase crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) (in meso using monoolein) |
| Protein sample | 45.4 mg/ml ARII in 20 mM Tris-HCl (pH 7.0), 400 mM NaCl, 1 mM DTT, 10% glycerol, 0.01% DDM |
| Temperature | 20 °C |
| Growth time | 2 weeks |
| Cryoprotection | Crystals cryocooled for X-ray data collection at SPring-8 BL41XU beamline (10-µm microbeam, Mar MX-225HE detector) |
| Notes | Reddish-purple plate-like crystals grew to 100 µm × 100 µm × 10 µm. Crystals were very unstable under open-air conditions and easily damaged during handling. Four ARII monomers with eight [cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) molecules in the asymmetric unit. Cholesterol molecules located between helices A and G, stabilizing overlaid planar layers. No obvious electron densities for loops between helices A-B and E-F. |


## Biological / Functional Insights

### First eukaryotic microbial rhodopsin structure

ARII is the first crystal structure of a eukaryotic member of the microbial rhodopsin family, determined at 3.2 A resolution (PDB: 3AM6). The structure reveals seven transmembrane helices (A-G) and a retinal chromophore, with four monomers and eight cholesterol molecules in the asymmetric unit. The structure is highly similar to bacteriorhodopsin (Z score=28.9), N. pharaonis SRII (Z score=29.3), and Anabaena sensory rhodopsin (Z score=27.8).

### Reversed proton uptake/release sequence compared to bacteriorhodopsin

During the ARII photocycle, proton uptake from the cytoplasm occurs first, followed by release to the extracellular side. This is reversed relative to bacteriorhodopsin, where proton release precedes uptake at pH 7.0. The reversed sequence is attributed to the lack of Ser189 (corresponding to Glu194BR, the proton-releasing group in BR) and the different pKa of Glu199 (corresponding to Glu204BR) in ARII.

### Conserved proton transfer pathway residues

The cytoplasmic-to-extracellular proton transfer pathway in ARII consists of: Asp92 (corresponding to Asp96BR, proton donor), Schiff base at Lys211, Asp207 (Asp212BR), Asp81 (Asp85BR, proton acceptor), Arg78 (Arg82BR), Glu199 (Glu204BR), and Ser189 (Glu194BR). The Arg78 side chain orientation is opposite to Arg82 in BR but same as Arg72 in NpSRII, which is capable of proton transfer.

### Cys218 involvement in proton uptake from cytoplasm

The side chain of Cys218 in ARII (corresponding to Leu223 in BR) is positioned 3.0 A from the δ2 oxygen of Asp92, suggesting a low-barrier hydrogen bond that may promote proton uptake. ARII and NpSRII both contain a non-dissociable residue at this position and show late proton release, unlike BR which has a dissociable residue and shows fast proton release.

### Retinal isomer composition and lack of dark adaptation

Unlike BR which contains both all-trans and 13-cis retinal in the dark, ARII contains 95.5% all-trans and 4.5% 13-cis retinal in the dark, with no dark adaptation observed. This is similar to NpSRII, which also has only all-trans retinal. The relative positions of the protonated Schiff base and counterion are important for light-dark adaptation.

### Photocycle kinetics and intermediates

The ARII photocycle proceeds on a millisecond timescale, similar to a typical light-driven proton pump. M intermediate formation occurs earlier than in BR. The K intermediate decay almost immediately leads to M formation, and the L intermediate is difficult to observe. Both M and O intermediates are confirmed.

### Cholesterol-mediated crystal stabilization

Eight cholesterol molecules were observed in the asymmetric unit, located between helices A and G of one ARII molecule and helix A of the neighboring ARII molecule. These intermolecular contacts play important roles in stabilizing the overlaid planar layers of ARII in the thin plate-like crystal.


## Cross-References

- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — ARII structure compared to BR; conserved proton transfer pathway residues; reversed proton release/uptake sequence
- [Archaerhodopsin-2](/xray-mp-wiki/proteins/rhodopsins/archaerhodopsin-2/) — Another microbial rhodopsin with late proton release behavior
- [Cell-free Protein Synthesis](/xray-mp-wiki/methods/expression-systems/cell-free-protein-synthesis/) — ARII expressed using E. coli cell-free synthesis system supplemented with detergent and lipid
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — ARII crystallized by in meso method using monoolein
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Ni2+ chelating affinity chromatography used for N11-tagged ARII purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Gel filtration chromatography used for final purification step
- [N-Dodecyl-β-D-maltoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — 0.01% DDM used in gel filtration buffer for ARII purification
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Primary lipid used for in meso crystallization of ARII
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — 10% glycerol used in purification buffer
- [Tris (Tris-HCl buffer)](/xray-mp-wiki/reagents/buffers/tris/) — 20 mM Tris-HCl (pH 7.0) used in purification buffer
- [Rhodopsin Photocycle](/xray-mp-wiki/concepts/rhodopsin-mechanisms/rhodopsin-photocycle/) — ARII follows the BR-type photocycle with K, M, and O intermediates
- [Channelrhodopsin C1C2](/xray-mp-wiki/proteins/rhodopsins/channelrhodopsin-c1c2/) — Related microbial rhodopsin; ARII used in opto-neurophysiology applications
