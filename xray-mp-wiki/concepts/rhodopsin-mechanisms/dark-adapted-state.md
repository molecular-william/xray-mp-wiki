---
title: "Dark-Adapted State of Microbial Rhodopsins"
created: 2026-06-11
updated: 2026-06-11
type: concept
category: concepts
layout: default
tags: [concept-functional, concept-transport-mechanism, subdirectory-rhodopsin-mechanisms]
sources: [doi/10.1038##s41467-020-20596-0]
verified: regex
---

# Dark-Adapted State of Microbial Rhodopsins

## Overview
The dark-adapted (DA) state is a desensitized conformation of microbial rhodopsins established during prolonged absence of light. In this state, the retinal chromophore exists in a thermal equilibrium between all-trans and 13-cis isomers, unlike the light-adapted (LA) ground state which contains exclusively all-trans retinal. The DA state represents a distinct conformational ensemble where the protein environment permits thermal isomerization without energy input. This state is characterized by altered internal water networks around the Schiff base that reduce the activation energy for retinal isomerization, enabling the establishment of a cis-trans equilibrium at room temperature.

## Mechanism/Details
In the dark-adapted state, the retinal binding pocket of microbial rhodopsins permits thermal equilibration between all-trans and 13-cis retinal isomers. High-resolution structures of AR3 reveal that the DA state (PDB: 6GUX, 1.3 A) contains both isomers in a 70:30 ratio. QM/MM calculations show that the 13-cis isomer is energetically favored in the DA state (Delta G = -1.9 kcal/mol) with a lower activation barrier for interconversion (17.1 kcal/mol) compared to the LA state (21.5 kcal/mol). The key mechanism involves subtle changes in the Schiff base electronic environment: in the LA state, the SB nitrogen atom shifts 0.5 A, destabilizing a pentagonal H-bond network involving Wat402, Thr99, and Asp95. This destabilization in the DA state reduces the energy barrier for retinal isomerization. The water network in the DA state is more ordered, with Wat402 well-resolved and Asp95 in a single conformation, facilitating the thermal equilibrium between isomers. In contrast, the LA state shows disordered Wat402 and dual Asp95 conformations, locking the chromophore into the all-trans configuration.


## Examples in Membrane Protein Work
- [Archaerhodopsin-3](/xray-mp-wiki/proteins/rhodopsins/archaerhodopsin-3/) — DA state structure (PDB: 6GUX, 1.3 A) shows 13-cis/all-trans retinal ratio of 70:30, matching liquid chromatography studies of other photoreceptor homologs

## Related Concepts
- [Light-Adapted State](/xray-mp-wiki/concepts/rhodopsin-mechanisms/light-adapted-state/) — Opposite conformational state where all-trans retinal is exclusively favored
- [Retinal Isomerization](/xray-mp-wiki/concepts/rhodopsin-mechanisms/retinal-isomerization/) — Thermal cis-trans isomerization in DA state driven by water network dynamics
- [Rhodopsin Photocycle](/xray-mp-wiki/concepts/rhodopsin-mechanisms/rhodopsin-photocycle/) — DA state serves as starting point for the light-driven photocycle

## Cross-References
- [Archaerhodopsin-3 (AR3)](/xray-mp-wiki/proteins/rhodopsins/archaerhodopsin-3/) — High-resolution DA state structure (6GUX) provides structural basis for desensitization mechanism
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — DA state of bacteriorhodopsin (PDB: 1C3W) also shows 13-cis retinal isomer
- [All-trans retinal](/xray-mp-wiki/reagents/ligands/retinal/) — Chromophore present in both DA and LA states
- [Light-Adapted State](/xray-mp-wiki/concepts/rhodopsin-mechanisms/light-adapted-state/) — Complementary concept describing the ground state of microbial rhodopsins
