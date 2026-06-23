---
title: Channelrhodopsin C1C2
created: 2026-05-26
updated: 2026-06-21
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.62389, doi/10.1038##ncomms8177, doi/10.1038##nature10870]
verified: false
---

# Channelrhodopsin C1C2

## Overview

Channelrhodopsin C1C2 is a chimeric construct between Chlamydomonas reinhardtii ChR1 and ChR2, designed as a light-gated cation channel for optogenetic applications. The original crystal structure was solved at 2.3 A resolution (PDB 3UG9) by Kato et al. (2012), revealing the essential molecular architecture of channelrhodopsins including the retinal-binding pocket, dimer interface, and cation conduction pathway. Time-resolved serial femtosecond crystallography (TR-SFX) using an X-ray free electron laser later revealed early conformational changes following photoactivation, including [Retinal](/xray-mp-wiki/reagents/ligands/retinal) isomerization-induced outward shift of TM3 and downward shift of TM7 - triggers for ion pore opening.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature10870 | 3UG9 | 2.3 A | not specified | C1C2 chimera (truncated, residues 1-342) | all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal) |
| doi/10.7554##eLife.62389 | 7C86 | 2.3 A | not specified | C1C2 chimera (dark state, synchrotron structure) | all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal) |
| doi/10.7554##eLife.62389 | 7E6Z | 2.5 A | not specified | C1C2 chimera (50 µs light-activated state) | isomerized [Retinal](/xray-mp-wiki/reagents/ligands/retinal) (twisted conformation) |
| doi/10.7554##eLife.62389 | 7E70 | 2.5 A | not specified | C1C2 chimera (250 µs light-activated state) | isomerized [Retinal](/xray-mp-wiki/reagents/ligands/retinal) |
| doi/10.7554##eLife.62389 | 7E71 | 2.5 A | not specified | C1C2 chimera (1 ms light-activated state) | isomerized [Retinal](/xray-mp-wiki/reagents/ligands/retinal) |
| doi/10.7554##eLife.62389 | 7E6X | 2.5 A | not specified | C1C2 chimera (4 ms light-activated state) | isomerized [Retinal](/xray-mp-wiki/reagents/ligands/retinal) |

## Expression and Purification

- **Expression system**: Spodoptera frugiperda Sf+ insect cells (baculovirus expression system)
- **Construct**: C1C2 chimera (residues 1-342) with C-terminal TEV-EGFP-His8 tag
- **Notes**: Cultured in Sf900II at 27°C for 24h, then 20°C. Cells harvested 72h post-infection.

### Purification Workflow

*Source: doi/10.1038##nature10870*

- **Expression system**: Sf+ insect cells (baculovirus)
- **Expression construct**: C1C2 chimera residues 1-342 with C-terminal TEV-EGFP-His8 tag
- **Tag info**: C-terminal EGFP-His8 (cleaved by TEV protease)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell disruption and membrane preparation | Microfluidizer (2 passes at 15,000 psi) | — | 300 mM NaCl, 50 mM Tris-HCl pH 8.0, 5% glycerol, 0.1 mM PMSF | Cell debris cleared at 10,000g for 40 min; crude membrane collected by ultracentrifugation at 43,000 rpm (Ti45) for 1h |
| Solubilization | Detergent solubilization | — | 300 mM NaCl, 50 mM Tris-HCl pH 8.0, 5% glycerol, 20 mM imidazole, 0.1 mM PMSF + 2.5% DDM, 0.5% cholesteryl hemisuccinate (CHS) | Insoluble material removed by ultracentrifugation at 45,000 rpm (Ti70) for 30 min |
| Ni-NTA affinity chromatography | Nickel affinity | Ni-NTA (QIAGEN) | 300 mM NaCl, 50 mM Tris-HCl pH 8.0, 5% glycerol, 0.1 mM PMSF + 0.05% DDM, 0.01% CHS | 1h binding; elution with 300 mM imidazole |
| TEV cleavage and reverse Ni-NTA | Tag removal | — |  | EGFP-His8 cleaved by His-tagged TEV protease; flow-through containing C1C2 collected after reloading on Ni-NTA |
| Size-exclusion chromatography | SEC | — | 150 mM NaCl, 50 mM Tris-HCl pH 8.0, 5% glycerol + 0.05% DDM, 0.01% CHS | Final purification step |

**Final sample**: Purified C1C2 in SEC buffer with DDM/CHS

### Purification Workflow

*Source: doi/10.7554##eLife.62389*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | Recombinant expression in Escherichia coli | -- | Not specified in paper + -- | C1C2 vector construction and protein production performed as previously reported (Kato et al., 2012) |
| Lysis and solubilization | Cell lysis and detergent solubilization | -- | 150 mM [sodium chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 50 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) (pH 8.0), 5% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 0.05% [n-dodecyl-beta-D-maltoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% [cholesteryl hydrogen succinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Protein solubilized in DDM/CHS mixture for membrane protein stability |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex 200 SEC column | 150 mM [sodium chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 50 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) (pH 8.0), 5% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Final purification step; protein concentrated to ~15 mg/ml for crystallization |


## Crystallization

### doi/10.1038##nature10870

| Parameter | Value |
|---|---|
| Method | [Lipidic cubic phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) (LCP) crystallization |
| Protein sample | Purified C1C2 in SEC buffer with DDM/CHS |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) |
| Protein-to-lipid ratio | 2:3 (w/w) |
| Temperature | 20°C |
| Growth time | 2-3 weeks in the dark |
| Cryoprotection | None (flash-cooled in liquid nitrogen without additional cryoprotectant) |
| Notes | Protein-LCP mixture dispensed by mosquito LCP robot (TTP LabTech). 100 nl protein-LCP aliquots overlaid with 1 ul precipitant on 96-well sandwich plates. Structure solved by MAD phasing using mercury-derivatized crystals. Data collected at SLS beamline X06SA and SPring-8 BL32XU. First example of MAD phasing for LCP-grown crystals. |

### doi/10.7554##eLife.62389

| Parameter | Value |
|---|---|
| Method | [Lipidic cubic phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) (LCP) crystallization |
| Protein sample | C1C2 chimera concentrated to ~15 mg/ml in 150 mM [sodium chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 50 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) (pH 8.0), 5% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) |
| Temperature | 20°C |
| Growth time | 2-3 weeks in the dark |
| Cryoprotection | Not specified; XFEL data collected at room temperature from LCP microjet |
| Notes | Protein mixed with [monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) at 2:3 protein-to-lipid ratio (w/w). High-density microcrystals (2-5 µm) formed, optimized for TR-SFX at SACLA XFEL. Dark state structure solved at 2.3 A resolution. Time-resolved structures at 50 µs, 250 µs, 1 ms, and 4 ms were collected using 470 nm pump laser pulses. |


## Biological / Functional Insights

### First crystal structure of a channelrhodopsin reveals essential molecular architecture

The 2.3 A structure of C1C2 (PDB 3UG9) revealed the seven-transmembrane helix architecture with an N-terminal extracellular domain (residues 24-83), the core TM1-TM7 helices, and a C-terminal intracellular domain. Two C1C2 protomers form a tightly associated dimer via N-domain, ECL1, TM3, and TM4 interactions, with three disulfide bonds (Cys66-Cys66, Cys73-Cys73, Cys75-Cys75) stabilizing the dimer interface. 6 lipids and 43 water molecules were observed per protomer.

### Structural comparison with bacteriorhodopsin reveals distinct features

C1C2 superimposes well on bacteriorhodopsin (PDB 1IW6) with conserved TM3-6 and protonated Schiff base position, but three distinct features differentiate it: (1) additional N-terminal and C-terminal domains (N-domain for dimerization, C-domain for subcellular localization), (2) TM7 protrudes ~18 A into the intracellular space, shifted 2.7 A toward the monomer central axis, and (3) the extracellular ends of TM1 and TM2 are tilted outward by 3.0 A and 4.1 A respectively, enlarging the cavity for cation translocation.

### Retinal-binding pocket and Schiff base counterion network

All-trans retinal is covalently bound to Lys296 (ChR2: 257) via a protonated Schiff base. The counterion complex includes Glu162 (ChR2: 123, corresponding to BR Asp85) and Asp292 (ChR2: 253, corresponding to BR Asp212). Distances from the Schiff base are 4.4 A (water), 3.4 A (Glu162), and 3.0 A (Asp292). Asp292 is proposed as the primary proton acceptor in C1C2, consistent with D292A mutants almost completely abolishing photocurrents. The Cys167-Asp195 DC-pair shows a distance of 4.4-4.6 A, with Cys167 associated with the retinal pi-electron system rather than Asp195.

### Electronegative cation-conduction pathway framed by TM1, TM2, TM3, and TM7

Electrostatic surface potential reveals an electronegative pore lined by 12 polar residues (Gln95, Thr98, Ser102, Glu122, Glu129, Lys132, Glu136, Glu140, Glu162, Thr285, Asp292, Asn297). Glu136 (ChR2: 97) is essential for cation conduction. Two constriction sites occlude the cytoplasmic side: (1) Ser102, Glu129, and Asn297 form the first gate, and (2) Tyr109 (ChR2: 70) forms the second gate. Mutations at these residues affect ion selectivity and kinetics.

### Extracellular vestibule and conserved residue cluster

An extracellular vestibule (~8 A diameter) is formed by the N domain and ECL1-3, with Lys154, Lys209, and Arg213 creating a slightly electropositive surface. Deeper within, Arg159, Tyr160, Glu274, and Ser284 (conserved in ChRs and BRs) form a water-mediated hydrogen-bond network fixing TM3, TM6, and TM7 positions. The R159A mutant does not produce photocurrent despite robust membrane expression, indicating this cluster is critical for creating the extracellular vestibule.

### Absorption spectrum blueshift explained by counterion proximity

The ChR absorption maximum (470 nm) is blueshifted compared to BR (568 nm). The C1C2 structure shows that Asp292 (the counterion) is ~1 A closer to the Schiff base than the corresponding BR residue, and negatively charged residues line the conducting pathway. These environments stabilize the ground state (S0), enlarging the S0-S1 energy gap and causing the blueshift.

### Retinal kink-induced outward shift of TM3 triggers channel opening

Time-resolved TR-SFX revealed that [Retinal](/xray-mp-wiki/reagents/ligands/retinal) isomerization induces a twisted, kinked conformation that shifts toward Cys167, causing an outward shift of TM3 originating at the Pro168 helix kink. This movement propagates to the intracellular segment where His173 forms ionic interactions with Arg307 in TM7 and Glu121/Glu122 in TM2, opening the inner gate. The outward shift of TM3 is not observed in the Cys167 mutant, indicating the critical role of the Cys residue in the TM3 shift.

### Downward shift of TM7 induced by retinal isomerization

The isomerization of retinal induces a downward shift of TM7 (Helix G) at the retinal-attached residue Lys296, which becomes most prominent at 4 ms. Positive densities along Lys296 and complementary difference densities around Trp299 indicate an overall downward shift of the middle portion of TM7. This shift is similar to the L-like intermediate of [Bacteriorhodopsin](/xray-mp-wiki/proteins/bacteriorhodopsin) and represents a conserved feature of rhodopsin proteins.

### Five glutamic acid residues and three constriction sites line the ion pore

The dark state structure reveals five glutamic acid residues (E1-E5) lining the putative ion pore, with two counterion residues (C11 and C12). Three constriction sites form the inner, central, and outer gates. The inner gate is formed by Glu121, Glu122, His173, and Arg307. Light-induced conformational changes at these gates precede ion conductance, with the inward gate destabilization likely triggering water influx and pore dilation.

### Photocycle intermediates P2 accumulates in crystals with hindered P3 transition

C1C2 crystals accumulate primarily the P2 intermediate (390 nm) with the transition from P2 to P3 hindered in the crystal lattice. The P2 intermediate shows prominent spectral increase at 390 nm, suggesting a deprotonated Schiff base state. This differs from solution behavior where P3 (530 nm) forms after P2. The P1 intermediate (520 nm) forms before 10 µs, and the P3 intermediate shows a delayed rise at 530 nm after 360 µs in solution.

### DC-pair residues (Cys167 and Asp195) are critical for channel gating

The aspartate-cysteine pair (DC-pair) Cys167 and Asp195 in the [Retinal](/xray-mp-wiki/reagents/ligands/retinal) binding pocket are critical for fast channel kinetics. Mutations of these residues result in step-function opsin (SFO) mutants with long-lasting photocurrents. FTIR and structural studies suggest Asp195 functions as the internal proton donor for the deprotonated Schiff base via an internal hydrated water molecule and Cys167. The hydrogen-bonding network involving the DC-pair affects the retinal conformation after isomerization.


## Cross-References

- [n-Dodecyl-beta-D-maltoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent (2.5% for solubilization, 0.05% for purification) used for membrane protein extraction and stabilization
- [Cholesteryl Hydrogen Succinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Stabilizing additive (0.5% for solubilization, 0.01% for purification) used to maintain C1C2 stability
- [Tris (Tris-HCl buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Buffer (50 mM, pH 8.0) used throughout purification and crystallization
- [2-(N-morpholino)ethanesulfonic acid (MES)](/xray-mp-wiki/reagents/buffers/mes/) — Buffer used in eLife 2021 crystallization reservoir
- [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/) — Salt (150-300 mM) used in purification and crystallization buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Stabilizer (5%) used in purification and crystallization buffers
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Host lipid for LCP crystallization matrix
- [All-trans retinal](/xray-mp-wiki/reagents/ligands/11-cis-retinal/) — Chromophore covalently bound to Lys296 via Schiff base linkage; essential for light sensitivity
- [Polyethylene glycol (PEG)](/xray-mp-wiki/reagents/additives/peg/) — Precipitant (PEG500DME) used in LCP crystallization
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used for both original and TR-SFX C1C2 crystal growth
- [Multi-wavelength Anomalous Diffraction (MAD)](/xray-mp-wiki/methods/structure-determination/mad-phasing/) — MAD phasing using mercury derivative was used to solve the original C1C2 structure - first application to LCP crystals
- [Rhodopsin Photocycle](/xray-mp-wiki/concepts/rhodopsin-photocycle/) — C1C2 photocycle intermediates (P1, P2, P3) characterized by flash photolysis
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — Archetypal microbial rhodopsin used for structural comparison
- [Channelrhodopsin 2 (ChR2)](/xray-mp-wiki/proteins/rhodopsins/channelrhodopsin-2/) — Parent protein of C1C2 chimera; C1C2 is a fusion of ChR1 and ChR2
