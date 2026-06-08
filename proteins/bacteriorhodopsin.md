---
title: Bacteriorhodopsin
created: 2026-05-26
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1016##S0969-2126(99)80118-X, doi/10.1016##j.jbc.2022.101722, doi/10.1038##44623]
verified: false
---

# Bacteriorhodopsin

## Overview

Bacteriorhodopsin (bR) from Halobacterium salinarum is a light-driven proton pump that converts the energy of light into a proton gradient used to drive ATP synthesis. The protein comprises seven transmembrane helices and is covalently bound to [retinal](/xray-mp-wiki/reagents/ligands/retinal/) via a Schiff base at Lys216. The high-resolution 1.9 A structure solved from crystals grown in [lipidic cubic phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) reveals the complete proton translocation pathway, including a continuous hydrogen-bond network of well-ordered water molecules and charged residues from the Schiff base to the extracellular surface.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##S0969-2126(99)80118-X | 1C3W | 1.9 A | P63 | Bacteriorhodopsin from Halobacterium salinarum, wild-type, seven transmembrane helices | all-trans retinal (covalently bound via Schiff base to Lys216) |

## Expression and Purification

- **Expression system**: Halobacterium salinarum (native expression in purple membrane)
- **Construct**: Wild-type bacteriorhodopsin, seven transmembrane helices, no affinity tags

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Purple membrane isolation | Differential centrifugation from Halobacterium salinarum cell pellets | -- | Not specified in paper + -- | bR is naturally expressed at high levels in Halobacterium salinarum, forming purple membrane patches that are 75% protein by mass. The purple membrane is organized into stable two-dimensional protein-lipid crystalline arrays with bR trimers. |


## Crystallization

### doi/10.1016##S0969-2126(99)80118-X

| Parameter | Value |
|---|---|
| Method | [Lipidic cubic phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) crystallization |
| Protein sample | Detergent-solubilized bR from purple membrane, incorporated into [monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) cubic phase |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Cryocooled to 100 K for X-ray data collection |
| Notes | Hexagonal plate-like crystals with sizes up to 80 x 8 micrometers. The structure was solved at 1.9 A resolution with R = 22.3% and R_free = 24.5%. Cell parameters: a = 60.80, b = 60.80, c = 110.52 A. The packing arrangement in the ab plane is indistinguishable from that in the native purple membrane. Stacking along the c axis is due to polar interactions between the cytosolic and extracellular loops of adjacent layers. |

### doi/10.1038##44623

| Parameter | Value |
|---|---|
| Method | [Lipidic cubic phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) crystallization with lipase liquefaction |
| Protein sample | Detergent-solubilized bacteriorhodopsin in monoolein lipidic cubic phase matrix |
| Temperature | 110 K (cryocooled) |
| Growth time | Not specified |
| Cryoprotection | Flash frozen in liquid nitrogen; crystals mounted in cryo-loops |
| Notes | Hexagonal plate crystals approximately 70 micrometers across and 5-10 micrometers thick. Ground state data: resolution 1.9 A, space group P63, unit cell 60.80, 60.80, 110.52 A, 17996 unique reflections, 99.5% completeness, R_sym 4.6%. Excited state data collected at 110 K with continuous 532 nm laser illumination during X-ray diffraction. |


## Biological / Functional Insights

### Proton transport mechanism

Upon absorption of a photon, retinal isomerizes from all-trans to 13-cis,15-anti configuration, initiating the photocycle. A proton is transferred from the Schiff base (Lys216) to Asp85 (primary proton acceptor), followed by proton release into the extracellular medium and reprotonation from the cytoplasmic side. Key residues include Asp96 (cytoplasmic proton donor), Arg82 (proton release group), and Glu194/Glu204 (extracellular proton release). The reprotonation step from the cytoplasmic side requires a rearrangement of the helices.

### Hydrogen-bond network in proton translocation pathway

Eight well-ordered water molecules in the extracellular half form a continuous hydrogen-bond network from the Schiff-base nitrogen at Lys216 to Glu194 and Glu204, including residues Asp85, Asp212, and Arg82. Arg82 is solvated by four water molecules and Glu194 by two. This network is involved both in proton translocation during the photocycle and in stabilizing the structure of the ground state by preventing premature proton transfer from the Schiff base to Asp85.

### Native lipids maintain purple membrane integrity

Nine lipid phytanyl moieties were modeled in the 1.9 A structure (numbered 500-508), with four in the cytoplasmic half and five in the extracellular half. Lipids 502, 503, 507, and 508 form van der Waals contacts with symmetry-related bR trimers, accounting for purple membrane integrity. MALDI-MS identified four charged lipid species in crystals: phosphatidylglycerol sulfate (PGS), phosphatidylglycerol phosphate methylester (PGP-Me), triglycosyldiether (TGD), and sulfated triglycoside lipid (S-TGA-1). Archaeal lipids bind strongly to the protein and remain during detergent solubilization.

### Cytoplasmic side flexibility

The cytoplasmic and extracellular parts exhibit different B-factor distributions. Extracellular B factors are systematically smaller than cytoplasmic ones, except for helix A. Helices B, C, E, and F show the largest deviations (up to 11.7 A^2 difference). This flexibility on the cytoplasmic side is consistent with conformational changes needed for reprotonation of the Schiff base (via Asp96 on helix C) during the M to N transition in the photocycle.

### High-resolution ground-state structure in native lipid environment

The structure of bR in the ground state was solved to 1.9 A resolution from non-twinned crystals grown in a lipidic cubic phase. The model contains a single bR monomer per asymmetric unit with R = 22.3% and R_free = 24.5%. The structure reveals the complete protein, lipid, and water organization in the crystals, representing the functional entity of bR in the purple membrane of the bacteria at atomic resolution. The crystals are built up of layers of native-like membranes stacked in a well-ordered array.

### Early photocycle structural changes at the K_LT intermediate

Photoexcitation at 110 K triggers retinal photoisomerization from all-trans,15-anti to 13-cis,15-anti configuration. This forces C20 towards the cytoplasmic side, contacting Trp 182. Movements of Lys 216 and its peptide backbone in helix G partially disrupt a hydrogen-bonding network, weakening the helix. Water molecule W402 is displaced from between the Schiff base and the carboxylates of Asp 85 and Asp 212, and these carboxylates mutually approach, creating an electrostatic environment for proton transfer from the Schiff base to Asp 85. The K_LT intermediate population was estimated at approximately 35% by both X-ray crystallography and microspectrophotometry.


## Cross-References

- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid component of the lipidic cubic phase crystallization matrix
- [Sodium Phosphate](/xray-mp-wiki/reagents/buffers/sodium-phosphate/) — Buffer used in crystal handling and purification
- [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) — Chromophore covalently bound to Lys216 via Schiff base
- [Rhodopsin Photocycle](/xray-mp-wiki/concepts/rhodopsin-photocycle/) — bR is the archetypal microbial rhodopsin photocycle
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — bR crystallized in monoolein LCP at 1.9 A resolution
- [K_LT Intermediate](/xray-mp-wiki/concepts/k-lt-intermediate/) — Low-temperature photointermediate characterized in this paper
- [Single-Crystal Microspectrophotometry](/xray-mp-wiki/methods/structure-determination/single-crystal-microspectrophotometry/) — Method used to characterize bacteriorhodopsin crystals before photoexcitation
