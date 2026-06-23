---
title: "C1C2GA (C1C2 T198G/G202A)"
created: 2026-06-05
updated: 2026-06-05
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms8177]
verified: false
---

# C1C2GA (C1C2 T198G/G202A)

## Overview

C1C2GA is a blue-shifted mutant of the channelrhodopsin chimera C1C2, created by double mutation T198G/G202A. The mutant exhibits a 21 [NM](/xray-mp-wiki/reagents/detergents/nm/) blue shift in absorption maximum (from 476 [NM](/xray-mp-wiki/reagents/detergents/nm/) to 455 nm) compared to wild-type C1C2. The crystal structure at 2.5 A resolution (space group C2221) revealed that the mutations induce rotation of the beta-ionone ring of the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore to a 6-s-cis twisted conformation, shrinking the pi-conjugated system. The N-terminal 10 residues (PDYVFHRAHE) form a short helix not seen in the C1C2WT structure, and a putative Zn2+ ion coordinated by Asp40, His44, His47, and Asp142 was found bound to the extracellular side of the protein. C1C2GA maintains functional ion channel activity in HEK293 cells and mouse neurons.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms8177 | 4YZI | 2.5 A | C2221 | C1C2 T198G/G202A mutant (C1C2GA) | all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) (twisted 6-s-cis conformation) |

## Expression and Purification

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: C1C2 T198G/G202A mutant, [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg/) induction, [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/) selection
- **Notes**: Transformed E. coli BL21(DE3) cells grown at 18 C overnight in LB medium containing [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/) (50 ug/ml) and 5 uM all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal/). [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg/) induction used for [GR (Halobacterium sp. GR Bacteriorhodopsin)](/xray-mp-wiki/proteins/rhodopsins/gr/) expression.

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Cell disruption and membrane fractionation | -- | 50 mM [MES](/xray-mp-wiki/reagents/buffers/mes/) (pH 6.5) containing 1 M NaCl + -- | Cells harvested by centrifugation at 4 C, resuspended in buffer, disrupted by sonication or French press passage |
| Solubilization | Detergent solubilization | -- | 50 mM [MES](/xray-mp-wiki/reagents/buffers/mes/) (pH 6.5), 1 M NaCl + n-dodecyl-beta-D-maltoside (DDM) | Cell membranes solubilized by [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Affinity chromatography | Ni2+ affinity chromatography | Ni2+ affinity column (GE Healthcare) | Not specified + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Purified by chromatography on Ni2+ affinity column |
| Concentration and buffer exchange | Ultrafiltration concentration | -- | 1 M NaCl, 50 mM [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/)-Cl (pH 7.0) + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Purified sample concentrated and buffer exchanged using Amicon Ultra filter (Millipore) |


## Crystallization

### doi/10.1038##ncomms8177

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | C1C2GA mutant protein in buffer containing 1 M NaCl, 50 mM [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/)-Cl (pH 7.0), 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Lipid | Lipidic cubic phase (MOS/DCG or similar LCP medium) |
| Protein-to-lipid ratio | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Yellow crystals obtained in lipidic cubic phase under neutral pH conditions (pH 7.0). Structure determined by molecular replacement method using C1C2WT (PDB 3UG9) as template. Overall structure at pH 7.0 nearly identical to C1C2WT at pH 6.0 (RMSD 0.66 A over all Ca atoms). |


## Biological / Functional Insights

### Beta-ionone ring rotation induces blue-shifted absorption

The T198G/G202A mutations create space in the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) binding pocket, allowing the beta-ionone ring of the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore to rotate from the all-trans planar conformation to a twisted 6-s-cis conformation with C6-C7 bond torsion of -27.7 degrees. This rotation shrinks the pi-conjugated system of the chromophore, producing a 21 [NM](/xray-mp-wiki/reagents/detergents/nm/) blue shift (476 to 455 nm). The twisted 6-s-cis conformation is thermodynamically more stable by -1.1 kcal/mol than the planar 6-s-trans form in the C1C2GA mutant.

### First evidence of Zn2+ binding to channelrhodopsin

The crystal structure revealed a putative endogenous Zn2+ ion bound at the N-terminal segment of C1C2GA, which was disordered in the C1C2WT structure. The N-terminal 10 residues (PDYVFHRAHE) form a short helix on the extracellular side of transmembrane helix 2 and extracellular loop 1. The Zn2+ ion is coordinated tetrahedrally by Asp40, His44, and His47 on the N-terminal helix, together with Asp142 on ECL1. This represents the first evidence of a Zn2+ ion bound to the extracellular side of a channelrhodopsin.

### Disappearance of vibrational fine structure in absorption spectrum

The C1C2GA absorption spectrum lacks the spectral shoulder at ~447 [NM](/xray-mp-wiki/reagents/detergents/nm/) present in C1C2WT, which represents vibrational fine structure. The beta-ionone ring rotation eliminates this fine structure by broadening the Franck-Condon vibrational distribution in the excited state and separating the energy levels of the S1 and S2 states through vibronic coupling.

### C1C2GA maintains functional ion channel activity

Despite the large blue shift in absorption, C1C2GA retains functional ion channel activity. Photocurrent measurements in HEK293 cells showed that C1C2GA produces inward currents upon blue light illumination (475 nm), comparable to wild-type C1C2. The mutant was also functional in mouse neurons, demonstrating its utility as a blue-shifted optogenetic tool for dual-light activation experiments.


## Cross-References

- [Channelrhodopsin C1C2](/xray-mp-wiki/proteins/rhodopsins/channelrhodopsin-c1c2/) — C1C2GA is the T198G/G202A mutant of C1C2; C1C2WT structure (PDB 3UG9) used as template for C1C2GA crystal structure determination
- [Archaerhodopsin-2](/xray-mp-wiki/proteins/rhodopsins/archaerhodopsin-2/) — AR3 was also engineered with the same design principle (M128A/G132V/A225T) to produce a 100 nm blue shift (552 to 454 nm)
- [n-Dodecyl-beta-D-maltoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for membrane solubilization and protein purification
- [All-trans retinal](/xray-mp-wiki/reagents/lipids/all-trans-retinal/) — Chromophore covalently bound to conserved lysine via protonated Schiff base; adopts twisted 6-s-cis conformation in C1C2GA
- [2-(N-morpholino)ethanesulfonic acid (MES)](/xray-mp-wiki/reagents/buffers/mes/) — Buffer (50 mM, pH 6.5) used in cell lysis and membrane preparation
- [Tris (Tris-HCl buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Buffer (50 mM, pH 7.0) used in final purification buffer
- [Cholesterol Hydrogen Succinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — CHS (0.01%) used in C1C2 absorption spectrum measurements
- [Isopropyl-beta-D-thiogalactoside (IPTG)](/xray-mp-wiki/reagents/additives/iptg/) — IPTG induction used for GR expression in E. coli
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used to grow C1C2GA crystals at pH 7.0
- [Rhodopsin Photocycle](/xray-mp-wiki/concepts/rhodopsin-mechanisms/rhodopsin-photocycle/) — C1C2GA retains photocycle functionality; blue-shifted variant for optogenetics
- [Zinc Chloride](/xray-mp-wiki/reagents/additives/zinc-chloride/) — Putative Zn2+ ion bound to N-terminal helix of C1C2GA (first evidence of Zn2+ binding to channelrhodopsin)
