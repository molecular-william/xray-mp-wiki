---
title: Channelrhodopsin C1C2
created: 2026-05-26
updated: 2026-05-26
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.62389, doi/10.1038##ncomms8177]
verified: false
---

# Channelrhodopsin C1C2

## Overview

Channelrhodopsin C1C2 is a chimeric construct between Chlamydomonas reinhardtii ChR1 and ChR2, designed as a light-gated cation channel for optogenetic applications. Time-resolved serial femtosecond crystallography (TR-SFX) using an X-ray free electron laser revealed early conformational changes following photoactivation, including retinal isomerization-induced outward shift of TM3 and downward shift of TM7 - triggers for ion pore opening. The dark state structure was solved at 2.3 A resolution.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.7554##eLife.62389 | 7C86 | 2.3 A | not specified | C1C2 chimera (dark state, synchrotron structure) | all-trans retinal |
| doi/10.7554##eLife.62389 | 7E6Z | 2.5 A | not specified | C1C2 chimera (50 µs light-activated state) | isomerized retinal (twisted conformation) |
| doi/10.7554##eLife.62389 | 7E70 | 2.5 A | not specified | C1C2 chimera (250 µs light-activated state) | isomerized retinal |
| doi/10.7554##eLife.62389 | 7E71 | 2.5 A | not specified | C1C2 chimera (1 ms light-activated state) | isomerized retinal |
| doi/10.7554##eLife.62389 | 7E6X | 2.5 A | not specified | C1C2 chimera (4 ms light-activated state) | isomerized retinal |

## Expression and Purification

- **Expression system**: Escherichia coli (recombinant expression)
- **Construct**: C1C2 chimera between Chlamydomonas reinhardtii ChR1 and ChR2, His-tag for purification

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | Recombinant expression in Escherichia coli | -- | Not specified in paper + -- | C1C2 vector construction and protein production performed as previously reported (Kato et al., 2012) |
| Lysis and solubilization | Cell lysis and detergent solubilization | -- | 150 mM [sodium chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 50 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) (pH 8.0), 5% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 0.05% [n-dodecyl-beta-D-maltoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% [cholesteryl hydrogen succinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Protein solubilized in DDM/CHS mixture for membrane protein stability |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex 200 SEC column | 150 mM [sodium chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 50 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) (pH 8.0), 5% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Final purification step; protein concentrated to ~15 mg/ml for crystallization |


## Crystallization

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

### Retinal kink-induced outward shift of TM3 triggers channel opening

Time-resolved TR-SFX revealed that retinal isomerization induces a twisted, kinked conformation that shifts toward Cys167, causing an outward shift of TM3 originating at the Pro168 helix kink. This movement propagates to the intracellular segment where His173 forms ionic interactions with Arg307 in TM7 and Glu121/Glu122 in TM2, opening the inner gate. The outward shift of TM3 is not observed in the Cys167 mutant, indicating the critical role of the Cys residue in the TM3 shift.

### Downward shift of TM7 induced by retinal isomerization

The isomerization of retinal induces a downward shift of TM7 (Helix G) at the retinal-attached residue Lys296, which becomes most prominent at 4 ms. Positive densities along Lys296 and complementary difference densities around Trp299 indicate an overall downward shift of the middle portion of TM7. This shift is similar to the L-like intermediate of bacteriorhodopsin and represents a conserved feature of rhodopsin proteins.

### Five glutamic acid residues and three constriction sites line the ion pore

The dark state structure reveals five glutamic acid residues (E1-E5) lining the putative ion pore, with two counterion residues (C11 and C12). Three constriction sites form the inner, central, and outer gates. The inner gate is formed by Glu121, Glu122, His173, and Arg307. Light-induced conformational changes at these gates precede ion conductance, with the inward gate destabilization likely triggering water influx and pore dilation.

### Photocycle intermediates P2 accumulates in crystals with hindered P3 transition

C1C2 crystals accumulate primarily the P2 intermediate (390 nm) with the transition from P2 to P3 hindered in the crystal lattice. The P2 intermediate shows prominent spectral increase at 390 nm, suggesting a deprotonated Schiff base state. This differs from solution behavior where P3 (530 nm) forms after P2. The P1 intermediate (520 nm) forms before 10 µs, and the P3 intermediate shows a delayed rise at 530 nm after 360 µs in solution.

### DC-pair residues (Cys167 and Asp195) are critical for channel gating

The aspartate-cysteine pair (DC-pair) Cys167 and Asp195 in the retinal binding pocket are critical for fast channel kinetics. Mutations of these residues result in step-function opsin (SFO) mutants with long-lasting photocurrents. FTIR and structural studies suggest Asp195 functions as the internal proton donor for the deprotonated Schiff base via an internal hydrated water molecule and Cys167. The hydrogen-bonding network involving the DC-pair affects the retinal conformation after isomerization.


## Cross-References

- [n-Dodecyl-beta-D-maltoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent (0.05%) used for protein solubilization and purification
- [Cholesteryl Hydrogen Succinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Stabilizing additive (0.01%) used in purification and crystallization buffers
- [Tris (Tris-HCl buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Buffer (50 mM, pH 8.0) used in purification, crystallization, and spectroscopy
- [2-(N-morpholino)ethanesulfonic acid (MES)](/xray-mp-wiki/reagents/buffers/mes/) — Buffer (100 mM, pH 6.9) used in crystallization reservoir
- [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/) — Salt (150 mM) used in purification and crystallization buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Cryoprotectant/stabilizer (5%) used in purification buffer
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid component of the lipidic cubic phase (LCP) crystallization matrix
- [All-trans retinal](/xray-mp-wiki/reagents/ligands/11-cis-retinal/) — Chromophore covalently bound to conserved lysine (Lys296) via Schiff base linkage
- [Polyethylene glycol (PEG)](/xray-mp-wiki/reagents/additives/peg/) — Precipitant (PEG500DM, 30%) used in crystallization reservoir
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used to grow C1C2 microcrystals (2-5 µm) for TR-SFX
- [Time-Resolved Serial Femtosecond Crystallography (TR-SFX)](/xray-mp-wiki/methods/structure-determination/time-resolved-serial-femtosecond-crystallography/) — TR-SFX at SACLA XFEL used to capture 5 time-resolved structures of C1C2
- [Rhodopsin Photocycle](/xray-mp-wiki/concepts/rhodopsin-photocycle/) — C1C2 photocycle intermediates (P1, P2, P3) characterized by flash photolysis
- [GPCR Active Conformation](/xray-mp-wiki/concepts/gpcr-active-conformation/) — Light-induced conformational changes in TM3 and TM7 analogous to GPCR activation
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/bacteriorhodopsin/) — Archetypal microbial rhodopsin; C1C2 TM7 shift similar to BR L-intermediate
- [Channelrhodopsin C1C2](/xray-mp-wiki/proteins/channelrhodopsin-c1c2/) — Chimeric construct between ChR1 and ChR2 from Chlamydomonas reinhardtii
