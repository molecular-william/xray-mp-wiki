---
title: Photosystem II
created: 2026-06-02
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [enzyme, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature04224, doi/10.1038##nature13453, doi/10.1038##nature16949, doi/10.1038##nature21400]
verified: false
---

# Photosystem II

## Overview

Photosystem II (PSII) from Thermosynechococcus elongatus is a homodimeric multisubunit protein-cofactor complex embedded in the thylakoid membrane that initiates oxygenic photosynthesis. It captures sunlight and powers the photo-induced oxidation of water to atmospheric oxygen. The 3.0 A structure reveals the arrangement of 20 protein subunits and 77 cofactors per monomer. Serial femtosecond crystallography (SFX) structures have been determined at 5.0 A (dark S1 state) and 5.5 A (double-flash putative S3 state). Additionally, diffractive imaging using continuous diffraction from imperfect microcrystals achieved a 3.5 A resolution structure, surpassing the 4.5 A Bragg peak limit through iterative phasing of the continuous diffraction pattern.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature04224 | 1K4C | 3.0 | P212121 | Photosystem II core complex from Thermosynechococcus elongatus, homodimer, 20 subunits per monomer (D1, D2, CP43, CP47, cytochrome b-559 alpha and beta chains, PsbO, PsbO2, PsbU, PsbV, PsbW, PsbX, PsbY, PsbZ, PsbT, PsbJ, PsbH, PsbI, and three unassigned transmembrane helices X1, X2, X3) | Chlorophyll a (35 per monomer), beta-carotene (11 per monomer), pheophytin a (2), plastoquinone (2), haem (2), bicarbonate, 14 lipids (4 DGDG, 6 MGDG, 3 SQDG, 1 PG), 3 beta-DM detergent molecules, Mn4Ca cluster, Fe2+, Ca2+ |
| doi/10.1038##nature13453 | 4PBU | 5.0 | P212121 | Photosystem II core dimer from Thermosynechococcus elongatus, dark S1 state, serial femtosecond crystallography | Chlorophyll a, beta-carotene, pheophytin a, plastoquinone (QA, QB), haem, bicarbonate, lipids, Mn4CaO5 cluster, non-haem iron, Ca2+ |
| doi/10.1038##nature13453 | 4Q54 | 5.5 | P212121 | Photosystem II core dimer from Thermosynechococcus elongatus, double-flash putative S3 state, serial femtosecond crystallography | Chlorophyll a, beta-carotene, pheophytin a, plastoquinone (QA, QB), haem, bicarbonate, lipids, Mn4CaO5 cluster, non-haem iron, Ca2+ |
| doi/10.1038##nature16949 |  | 3.5 | P212121 | Photosystem II core dimer (~700 kDa) from Thermosynechococcus elongatus, continuous diffraction structure determined at 3.5 A resolution by iterative phasing of continuous diffraction patterns from room-temperature microcrystals (2,848 patterns, 120 Hz, LCLS XFEL, CSPAD detector) | Chlorophyll a, beta-carotene, pheophytin a, plastoquinone (QA, QB), haem, bicarbonate, lipids, Mn4CaO5 cluster, non-haem iron, Ca2+ |
| doi/10.1038##nature21400 | 5WS5 | 2.35 | P212121 | Photosystem II core dimer from Thermosynechococcus vulcanus, pre-flashed dark-adapted S1 state, TR-SFX at SACLA XFEL, 27,497 images used for refinement | Chlorophyll a, beta-carotene, pheophytin a, plastoquinone (QA, QB), haem, bicarbonate, lipids, Mn4CaO5 cluster, non-haem iron, Ca2+, 4 waters (W542, W546, W567, W665) in O4-water chain, Glu189 of D1 |
| doi/10.1038##nature21400 | 5WS6 | 2.35 | P212121 | Photosystem II core dimer from Thermosynechococcus vulcanus, pre-flashed two-flash 2F state (putative S3, 46% population), TR-SFX at SACLA XFEL, 21,680 images used for refinement | Chlorophyll a, beta-carotene, pheophytin a, plastoquinone (QA, QB), haem, bicarbonate, lipids, Mn4CaO5 cluster, non-haem iron, Ca2+, newly inserted oxygen atom O6 near O5, water W665 displaced, W567 moved toward O4 |
| doi/10.1038##nature21400 | 5GTH | 2.50 | P212121 | Photosystem II core dimer from Thermosynechococcus vulcanus, non-pre-flashed dark-adapted S1 state, TR-SFX at SACLA XFEL, 22,341 images used for refinement | Chlorophyll a, beta-carotene, pheophytin a, plastoquinone (QA, QB), haem, bicarbonate, lipids, Mn4CaO5 cluster, non-haem iron, Ca2+, waters W542, W546, W567, W665 in O4-water chain |
| doi/10.1038##nature21400 | 5GTI | 2.50 | P212121 | Photosystem II core dimer from Thermosynechococcus vulcanus, non-pre-flashed two-flash 2F state, TR-SFX at SACLA XFEL, 23,903 images used for refinement | Chlorophyll a, beta-carotene, pheophytin a, plastoquinone (QA, QB), haem, bicarbonate, lipids, Mn4CaO5 cluster, non-haem iron, Ca2+, structural changes at QB/non-haem iron site, OEC water chain |

## Expression and Purification

- **Expression system**: Thermosynechococcus elongatus (native expression)
- **Construct**: Photosystem II core complex, wild-type, 20 subunits per monomer, no affinity tags

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Thylakoid membrane isolation | Cell disruption and differential centrifugation from Thermosynechococcus elongatus | -- | Not specified in paper + -- | Thylakoid membranes prepared from Thermosynechococcus elongatus cells grown photoautotrophically |
| PSII core complex solubilization | Detergent solubilization with n-dodecyl-beta-D-maltoside (beta-DM) | -- | 50 mM Tris-HCl pH 8.0, 200 mM NaCl, 10 mM CaCl2 + 0.08% n-dodecyl-beta-D-maltoside (beta-DM) | PSII core complexes (CP47-III) solubilized from thylakoid membranes with beta-DM |
| PSII core complex purification | Anion-exchange chromatography on DEAE-Sepharose | DEAE-Sepharose | 20 mM Tris-HCl pH 8.0, 20 mM NaCl, 10 mM CaCl2, 5 mM MgCl2, 0.004% beta-DM + 0.004% beta-DM | PSII core complexes purified by DEAE-Sepharose chromatography; eluted with linear NaCl gradient |


## Crystallization

### doi/10.1038##nature04224

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, hanging drop |
| Protein sample | PSII core complex at 7.5 mg/ml in 20 mM Tris-HCl pH 8.0, 20 mM NaCl, 10 mM CaCl2, 0.004% beta-DM |
| Reservoir | 20 mM Tris-HCl pH 8.0, 18-20% PEG 4000, 100 mM NaCl, 10 mM CaCl2, 10 mM MgCl2 |
| Temperature | 293 K |
| Growth time | 2-3 weeks |
| Cryoprotection | Cryocooled to 100 K in liquid nitrogen; mother liquor supplemented with 25% glycerol |
| Notes | Plate-like crystals grew in hanging drops by vapor diffusion. Space group P212121, unit cell dimensions a = 171.4, b = 234.2, c = 324.3 A. One dimer per asymmetric unit. Structure solved by molecular replacement using the 3.8 A structure as search model. Refinement to 3.0 A resolution with Rwork = 21.8% and Rfree = 26.1%. The model contains 20 protein subunits per monomer, 77 cofactors, 14 lipids, and 3 detergent molecules. |

### doi/10.1038##nature13453

| Parameter | Value |
|---|---|
| Method | Batch crystallization with free interface diffusion |
| Protein sample | PSII core complex in solubilization buffer: 100 mM PIPES pH 7.0, 5 mM CaCl2, 10 mM tocopherol, 0.03% beta-dodecylmaltsyl (DDM), chlorophyll 0.5 mM |
| Temperature | 10 °C |
| Growth time | 48 hours |
| Cryoprotection | Not specified; crystals delivered at 10 °C via gas focusing liquid injector |
| Notes | PSII microcrystals (~1 µm) grown by free interface diffusion enhanced sedimentation method. Slow addition of PEG 2000 precipitant at ~20 µl/s created a two-phase system. Crystals sedimented into precipitant layer forming a pellet. All steps performed in darkness or dim green light. Unit cell dimensions: dark S1 state a=133 A, b=226 A, c=307 A; double-flash S3 state a=137 A, b=228 A, c=309 A. Data collected at 120 Hz FEL frequency with alternating dark and double-flash patterns. |

### doi/10.1038##nature16949

| Parameter | Value |
|---|---|
| Method | Batch crystallization with free interface diffusion |
| Protein sample | PSII core complex in crystallization buffer |
| Temperature | Room temperature |
| Notes | PSII microcrystals grown by free interface diffusion centrifugation technique. Space group P212121 with only four crystal contacts per dimer and 64% solvent by volume. Bragg diffraction limit of 4.5 A caused by lattice disorder (r.m.s. displacement of 0.8 A per dimension). Continuous diffraction data collected at LCLS XFEL CXI end station using gas dynamic virtual nozzle (GDVN) injector, 40 fs X-ray pulses at 9.48 keV, CSPAD detector at 120 Hz. 1.24 million frames collected over 2.9 h; 25,585 indexed; 2,848 strongest patterns used for continuous diffraction phasing. Wilson B-factor 191.6 A^2. Maximum dose 275 MGy. |

### doi/10.1038##nature21400

| Parameter | Value |
|---|---|
| Method | Batch crystallization |
| Protein sample | PSII core dimer from Thermosynechococcus vulcanus at 2.3 mg chlorophyll per ml |
| Temperature | 20 °C |
| Growth time | A few hours |
| Cryoprotection | 22% glycerol, 9% PEG 1450, 9% PEG 5000 MME by stepwise replacement over 1.5 h; loaded into high viscosity micro-extrusion injector with Super Lube nuclear grade grease matrix |
| Notes | Highly active PSII isolated from Thermosynechococcus vulcanus. Optimal crystal size 100 µm max length, diffracting to 2.1 Å by SACLA XFEL pulse. Post-crystallization procedure critical for good diffraction. Pre-flashed samples: 10 mM potassium ferricyanide in mother liquid. Non-pre-flashed: 2 mM potassium ferricyanide. ~46% S3 state population upon 2F illumination confirmed by FTIR. Data collected at SACLA XFEL, space group P212121, R_iso=0.068 between pre-flashed dark and 2F states at 2.35 Å. |


## Biological / Functional Insights

### Electron transfer chain architecture

In PSII, excitation energy is transferred from the antenna system to the reaction centre, where the primary electron donor P680 formed by chlorophyll a molecules is excited to P680*, followed by release of an electron that travels along the electron transfer chain by means of pheophytin a (PheoD1) to the plastoquinone QA, forming P680+QA-. After two steps of reduction and protonation of the secondary plastoquinone QB, the plastoquinol PQH2 leaves the QB site and is replaced by new plastoquinone. The electrons are transferred from the Mn4Ca cluster through redox-active TyrZ to P680+, which is reduced to P680 for another photosynthetic cycle.

### Oxygen-evolving Mn4Ca cluster architecture

The electron density of the Mn4Ca cluster is best approximated by four Mn ions arranged as a hook-like structure resembling a Y-shaped arrangement. The Mn ions are numbered Mn1 to Mn4, starting from the highest electron density at the bend. Mn1 and Mn3 can attain either oxidation state III or IV in the S1 state. Mn4, ligated by Asp 170 of D1, is not oxidized during S0-S1-S2-S3 transitions. The Mn4Ca cluster architecture differs considerably from the previously postulated cubane-like model, with unequal Mn-Mn distances in the pyramid formed by three Mn and Ca2+, connected asymmetrically to Mn4.

### High-resolution structure from continuous diffraction

Diffractive imaging of PSII microcrystals at the LCLS XFEL achieved a 3.5 A resolution structure using continuous diffraction, surpassing the 4.5 A Bragg peak limit. Starting with a 4.5 A molecular replacement solution, a binary molecular envelope mask was generated and used as a real-space constraint for iterative phase retrieval on the continuous diffraction data covering 4.5-3.3 A. The difference-map algorithm converged within 100 iterations, retrieving over 30 million phases. Averaging solutions over multiple random starts produced a self-consistent electron density. Pseudo-crystallographic refinement of the continuous diffraction structure showed improved side-chain definition in helices and better model-to-density fit compared to Bragg-only refinement. The R-free factor at low resolution was notably improved by including continuous diffraction data.

### Light-induced structural changes and O=O bond formation site revealed by TR-SFX at SACLA

TR-SFX at SACLA XFEL at 2.35 Å resolution revealed two areas of structural changes between the two-flash (2F) and dark-adapted S1 states: around the QB/non-haem iron-binding site and the oxygen-evolving complex (OEC). At the QB site, the quinone head group rotated ~10° towards Ser264 and His215 of D1. Around the OEC, water molecule W665 disappeared upon 2F illumination, causing W567 to move closer to O4 (distance reduced to 2.32 Å), suggesting proton transfer. Critically, a new oxygen atom O6 was inserted near O5 (average distance 1.5 Å), providing a mechanism for O=O bond formation consistent with the Siegbahn model. Glu189 of D1 moved away from the cubane to accommodate O6. The S-state population was ~46% S3 upon 2F illumination.


## Cross-References

- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Beta-DM/DDM detergent used for PSII core complex solubilization and purification
- [Digalactosyl Diacylglycerol (DGDG)](/xray-mp-wiki/reagents/lipids/digalactosyl-diacylglycerol/) — One of four DGDG lipids integrally bound to PSII
- [Phosphatidylglycerol (PG)](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol/) — One of the lipids integrally bound to PSII
- [Heme](/xray-mp-wiki/reagents/ligands/heme/) — Two heme molecules per monomer in cytochrome b-559
- [Carotenoid](/xray-mp-wiki/reagents/ligands/carotenoid/) — Eleven beta-carotene molecules per monomer for photoprotection
- [Plastoquinone](/xray-mp-wiki/reagents/ligands/plastoquinone/) — Plastoquinone QA and QB are the primary and secondary electron acceptors in PSII
- [Potassium Ferricyanide](/xray-mp-wiki/reagents/additives/potassium-ferricyanide/) — Artificial electron acceptor used in TR-SFX experiments for pre-flashed PSII samples
- [Time-Resolved Serial Femtosecond Crystallography (TR-SFX)](/xray-mp-wiki/methods/structure-determination/time-resolved-serial-femtosecond-crystallography/) — TR-SFX at SACLA XFEL used for time-resolved study of PSII S-state transitions
