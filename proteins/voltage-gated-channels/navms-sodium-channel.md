---
title: NavMs Sodium Channel from Magnetococcus marinus
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##NCOMMS3465]
verified: false
---

# NavMs Sodium Channel from Magnetococcus marinus

## Overview

[NAVMS](/xray-mp-wiki/proteins/voltage-gated-channels/navms/) is a prokaryotic voltage-gated sodium channel from Magnetococcus marinus that serves as a model system for understanding sodium channel structure, gating, and inactivation. The channel forms a homotetramer with each monomer consisting of a transmembrane domain containing the voltage sensor and pore functionalities, and a C-terminal domain (CTD) comprising a flexible linker region connected to a four-helix coiled-coil bundle. The 2.9 A crystal structure of the [NAVMS](/xray-mp-wiki/proteins/voltage-gated-channels/navms/) pore with its full-length CTD reveals a fully open pore conformation. Combined electron paramagnetic resonance (EPR) spectroscopy, molecular dynamics simulations, and electrophysiology demonstrate that the coiled-coil domain couples inactivation with channel opening, enabled by negatively charged residues in the linker region.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##NCOMMS3465 | 3ZJZ | 2.9 | C2221 | NavMs-pore + CTD (full-length C-terminal domain), residues 1-274 from Magnetococcus marinus | None |

## Expression and Purification

- **Expression system**: E. coli expression system (described in earlier NavMs-pore study, PDB 4F4L)
- **Construct**: NavMs-pore + CTD construct with full-length C-terminal domain

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Purification | HisTrap HP [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) followed by size-exclusion chromatography | HisTrap HP column, size exclusion column | Buffer A (composition not specified in raw paper) + Not specified | Untagged wild-type NavMs-pore + CTD concentrated to 14 mg/ml for crystallization |


## Crystallization

### doi/10.1038##NCOMMS3465

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | NavMs-pore + CTD at 14 mg/ml |
| Reservoir | 0.1 M trisodium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/), 0.1 M [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 34% v/v [PEG400](/xray-mp-wiki/reagents/additives/peg-400/) |
| Temperature | 4 |
| Cryoprotection | Not specified |
| Notes | Protein mixed in 2:1 ratio with reservoir solution for 150 nl sitting drops. Data collected at Diamond Light Source. Space group C2221, cell dimensions a=80.15, b=334.38, c=80.21 A. Structure determined by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using monomer A from NavMs-pore structure (PDB 4F4L). |


## Biological / Functional Insights

### C-terminal domain structure and dynamics

The CTD of [NAVMS](/xray-mp-wiki/proteins/voltage-gated-channels/navms/) consists of a flexible linker region (residues 222-239) connecting the transmembrane pore to a four-helix coiled-coil bundle (residues 240-270). EPR spectroscopy reveals the linker is flexible and dynamic but not fully disordered, while the coiled-coil region forms a stable tetrameric bundle. DEER distance measurements and molecular dynamics simulations show large motions in the CTD, explaining why this region is disordered in the crystal electron density map.

### Open pore conformation

The 2.9 A structure of NavMs-pore + CTD reveals a fully open pore conformation with all four monomers in their open state. The gating movement involves a change in the Psi angle of residue Thr84, producing an anticlockwise twisting motion of the lower end of the S6 helices (~4.5 A movement each). Both crystallographically distinct tetramers have true fourfold symmetry, with the distance between Met97 C-alpha atoms at the base of the pore being 21 A across both diagonals.

### Role of CTD in inactivation gating

Electrophysiology measurements show the CTD is necessary for inactivation gating and recovery, and for channel stability. The Delta223 [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation/) (removing the linker and coiled-coil) inactivates ~7 times slower than wild-type [NAVMS](/xray-mp-wiki/proteins/voltage-gated-channels/navms/) and recovers from inactivation ~155 times slower. The Delta239 [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation/) (removing only the coiled-coil) has normal inactivation kinetics but uncoupled voltage dependence. Mutation of three negatively charged glutamate residues (E229, E230, E231) to glutamine slows inactivation ~5-fold.

### Gating mechanism model

A mechanism for gating is proposed whereby splaying of the bottom of the pore is possible without requiring unravelling of the coiled-coil. The CTD acts like an oscillator composed of a spring (the flexible linker) tethered to a mass (the coiled-coil) that enables opening of the gate without dissociating the tetramers. The linker and coiled-coil C-terminal region enables opening of the gate and fast inactivation at the appropriate membrane potential.

### Conservation across prokaryotic sodium channels

The CTDs of all identified prokaryotic sodium channels exhibit similar flexible linker/coiled-coil motifs. Evolutionary differences in linker length and flexibility may account for different inactivation kinetics. For example, [NaChBac Bacterial Voltage-Gated Sodium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/nachbac/) (with a considerably shorter linker region) inactivates 12-19 times slower than [NAVMS](/xray-mp-wiki/proteins/voltage-gated-channels/navms/).


## Cross-References

- [KcsA Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) — Related tetrameric ion channel serving as structural model
- [Sitting Drop Vapor Diffusion Crystallization](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) — Crystallization method used for NavMs
- [Sodium Channel Gating](/xray-mp-wiki/concepts/sodium-channel-gating/) — NavMs provides insights into sodium channel gating mechanisms
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [NaChBac Bacterial Voltage-Gated Sodium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/nachbac/) — Related protein structure
- [NAVMS](/xray-mp-wiki/proteins/voltage-gated-channels/navms/) — Related protein structure
- [PEG400](/xray-mp-wiki/reagents/additives/peg-400/) — Additive used in purification or crystallization buffers
- [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) — Buffer component in purification or crystallization
