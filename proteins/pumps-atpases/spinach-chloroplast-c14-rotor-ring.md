---
title: Spinach Chloroplast c14 Rotor Ring (CFo c14 Ring)
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [membrane-protein, xray-crystallography, pump]
sources: [doi/10.1074##jbc.m109.006916]
verified: false
---

# Spinach Chloroplast c14 Rotor Ring (CFo c14 Ring)

## Overview

The crystal structure of the membrane-integral c14 rotor ring of the proton translocating F1Fo ATP synthase from spinach (Spinacia oleracea) chloroplasts determined at 3.8 A resolution. The rotor ring consists of 14 identical c subunit protomers symmetrically arranged around a central pore. This is the first structure of an isolated c-ring rotor from a proton-driven ATPase. The conserved carboxylate Glu61, essential for proton transport, points toward the periphery of the ring where it is stabilized by hydrogen bonding with Tyr66 from the adjacent protomer. Comparisons with the c11 rotor of Ilyobacter tartaricus show conserved carboxylate spacing of 10.6-10.8 A despite different stoichiometries, suggesting a conserved gear distance in rotary ATPases.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1074##jbc.m109.006916 |  | 3.8 | C2 | Spinach chloroplast c14 ring (14 identical c subunit protomers, residues 3-79 resolved) | Glu61 (conserved proton-binding carboxylate) |

## Expression and Purification

- **Expression system**: Spinach plants (Spinacia oleracea) grown in local greenhouse
- **Construct**: Native CF1Fo purified from spinach thylakoid membranes; crystallization results in spontaneous loss of F1 subunits and subunits a, b, b', yielding isolated c14 ring

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Thylakoid membrane preparation | Washed in sodium pyrophosphate buffer pH 7.4 with [DTT](/xray-mp-wiki/reagents/additives/dtt/) and PMSF; precipitated by centrifugation at 3000 x g | -- | 20 mM sodium pyrophosphate pH 7.4, 2 mM [DTT](/xray-mp-wiki/reagents/additives/dtt/), 0.002% (w/v) PMSF + -- | Membranes resuspended in 400 mM [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/), 20 mM Tricine pH 7.4, 5 mM MgCl2, 0.002% PMSF, 50 mM [DTT](/xray-mp-wiki/reagents/additives/dtt/) |
| Solubilization of CF1Fo | Detergent extraction | -- | -- + 1% (w/v) [Sodium Cholate](/xray-mp-wiki/reagents/detergents/sodium-cholate/) + 2% (w/v) beta-[DDM](/xray-mp-wiki/reagents/detergents/ddm/) ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Suspension stirred on ice for 15 min and sonicated. Unsolubilized material removed by centrifugation at 100,000 x g |
| [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/) precipitation | 48% (w/v) [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/) precipitation | -- | 50 mM Tricine pH 8.0, 4% (w/v) [Glycine](/xray-mp-wiki/reagents/buffers/glycine/), 10% (v/v) [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 5 mM MgCl2, 5 mM [DTT](/xray-mp-wiki/reagents/additives/dtt/), 0.002% PMSF, 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Pellet dissolved in same buffer |
| [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/) gradient centrifugation | [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/) gradient (600 mM to 0 mM linear gradient) | -- | 50 mM Tricine pH 8.0, 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 5 mM [DTT](/xray-mp-wiki/reagents/additives/dtt/), 0.002% PMSF + 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Centrifuged 24 h at 75,000 x g at 4 C |
| Anion exchange chromatography | POROS HQ20 anion exchange | POROS HQ20 | 50 mM Tricine pH 8.0, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 4% [Glycine](/xray-mp-wiki/reagents/buffers/glycine/), 5 mM MgCl2 + 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Further purification step |


## Crystallization

### doi/10.1074##jbc.m109.006916

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | Purified CF1Fo (which spontaneously forms c14 ring crystals) |
| Reservoir | 100 mM sodium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) pH 4.6, 300 mM NaCl, 20% (v/v) 2-methyl-2,4-pentanediol ([MPD](/xray-mp-wiki/reagents/additives/mpd/)) |
| Temperature | 20 |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | Crystals obtained after spontaneous loss of F1 and peripheral F0 subunits during crystallization. Crystals contain only the c14 ring. Data collected at ESRF beamline ID14. Structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using tetradecameric models generated from I. tartaricus c11 monomer (1yce). Self-rotation function and AFM studies confirmed 14-fold symmetry. |


## Biological / Functional Insights

### Conserved carboxylate spacing across different c-ring stoichiometries

Despite different stoichiometries (c14 in spinach chloroplasts vs c11 in I. tartaricus), the conserved carboxylate residues involved in ion transport are 10.6-10.8 A apart in both rotor rings. This suggests a conserved gear distance in rotary ATPases, allowing calculation of c-ring diameter from stoichiometry or estimation of unknown stoichiometry from diameter.

### Proton binding site at Glu61

The conserved Glu61 (equivalent to Asp61 in E. coli) points toward the periphery of the c14 ring, stabilized by hydrogen bonding to Tyr66 of the adjacent protomer (O-epsilon-1...HO 2.5 A) and to the backbone carbonyl of Phe59 (O-epsilon-2...O 2.8 A) and Thr64 (O-epsilon-1...O-gamma-1 3.1 A). The structure reflects the protonated form of the c-ring. Upon deprotonation, Glu61 is proposed to change to another rotamer and become fully exposed to the periphery, where reprotonation by a conserved arginine in subunit a returns it to the initial conformation.

### Hydrophobic shell around proton-binding site

The proton-binding site in the chloroplast enzyme differs from the sodium-binding site in I. tartaricus. Residues adjacent to Glu61 (Leu57, Phe59, Ala62, Leu63) provide a hydrophobic shell, whereas Na+-translocating ATPases have polar residues (Ser/Thr) at equivalent positions. These differences likely determine ion specificity: Ala62 is found in all H+-translocating F-ATPases, while Na+-translocating enzymes have a polar serine or threonine. This substitution pattern explains the shift in ion specificity between proton- and sodium-driven ATPases.

### Structure comparison with other c-ring rotors

The chloroplast c14 ring has a barrel-shaped cylinder with less pronounced waist compared to I. tartaricus c11. External diameter: ~47 A (middle), compared to ~50 A (boundaries) and 40 A (middle waist) for I. tartaricus c11, ~34 A for yeast mitochondrial c10 at the conserved carboxylate, and 80/68 A for E. hirae V-type rotor (with 4-helix protomers). Backbone structure of yeast mitochondrial c10 shows only slight curvature, similar to the chloroplast ring.

### Proposed proton translocation pathway

Current models suggest that proton transport involves either a single access channel or two half-channels in subunit a. Modification studies of engineered cysteines in E. coli c-ring identified residues at positions 57, 58, 62, and 65 as involved in the pathway. All these residues are located at the periphery of the chloroplast c14 ring and are accessible from the external phase. None are charged or polar, suggesting that a water wire for proton transport is formed at least in part at the backbone of the c subunit. Gly51 and Leu57 backbone carbonyls may provide water-binding sites.


## Cross-References

- [Ilyobacter tartaricus c11 Rotor Ring](/xray-mp-wiki/proteins/pumps-atpases/ilyobacter-tartaricus-c-subunit/) — Na+-translocating c11 ring used as molecular replacement search model and key structural comparator
- [Spirulina platensis c15 Ring](/xray-mp-wiki/proteins/pumps-atpases/spirulina-platensis-c15-ring/) — Another c-ring rotor structure with different stoichiometry for comparison
- [Bacillus pseudofirmus OF4 c13 Ring](/xray-mp-wiki/proteins/pumps-atpases/bacillus-pseudofirmus-of4-c13-ring/) — Bacterial c-ring rotor for comparison of proton-translocating c-rings
- [Rotary ATPase Mechanism](/xray-mp-wiki/concepts/enzyme-mechanisms/rotary-atpase-mechanism/) — The c14 ring is the rotor component of the rotary ATP synthase mechanism
- [Proton Wire](/xray-mp-wiki/concepts/transport-mechanisms/proton-wire/) — Proposed involvement of backbone carbonyls and water wires in proton translocation through the c-ring
- [Common Drug-Binding Site on ATP Synthase c-Ring](/xray-mp-wiki/concepts/structural-mechanisms/common-drug-binding-site-atp-synthase-c-ring/) — Structural basis of c-ring as drug target
- [NCS](/xray-mp-wiki/concepts/structural-mechanisms/non-crystallographic-symmetry/) — Related biological concept
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/) — Additive used in purification or crystallization buffers
- [DTT](/xray-mp-wiki/reagents/additives/dtt/) — Additive used in purification or crystallization buffers
