---
title: Molecular Dynamics Simulations for Membrane Proteins
created: 2026-06-16
updated: 2026-06-16
type: method
category: methods
layout: default
tags: [structure-xray, subdirectory-structure-determination]
sources: [doi/10.1016##j.bbamem.2021.183825, doi/10.1016##j.str.2012.12.018, doi/10.1021##acs.biochem.9b00971]
verified: false
---

# Molecular Dynamics Simulations for Membrane Proteins

## Overview

Molecular dynamics (MD) simulations are computational methods that simulate the time-dependent behavior of molecular systems. In the TmYidC study, 4 µs of all-atom MD simulations using the CHARMM36m force field in GROMACS were performed to study the orientation and dynamics of the N-terminal amphipathic helix and C1 region of YidC embedded in a POPE:POPG (3:1) bilayer. In a comprehensive study of bacteriorhodopsin (bR), 60 independent MD simulations using the Amber force field (ff99SB) were performed across eight crystal structures of bR photointermediates to investigate how D96 deprotonation controls opening of the cytoplasmic proton uptake pathway. For the M2 V27A mutant, a 300 ns MD simulation of the M2(22-46) V27A-spiro-adamantyl amine complex in a POPC bilayer was performed, predicting with accuracy the position of the ligands and waters inside the pore as validated by X-ray crystallography.

## Principle

MD simulations solve Newton's equations of motion for a system of atoms interacting via a molecular mechanics force field, allowing observation of protein dynamics, conformational changes, and interactions with the lipid bilayer at atomic resolution.

## Protocol

### Reagents and Materials

- POPE:POPG (3:1) lipid bilayer
- TIP3P water model
- 150 mM NaCl

### Steps

1. {'step': '1. Align crystal structure to membrane normal using OPM database', 'method': 'Orientation of Proteins in Membranes (OPM)'}
2. {'step': '2. Embed protein in POPE:POPG (3:1) bilayer', 'method': 'CHARMM-GUI webserver'}
3. {'step': '3. Solvate system with TIP3P water and add 150 mM NaCl', 'method': 'CHARMM-GUI'}
4. {'step': '4. Multi-step equilibration with gradual release of restraints', 'method': 'CHARMM-GUI scripts'}
5. {'step': '5. Unrestrained equilibration for 30 ns', 'method': 'GROMACS'}
6. {'step': '6. Production runs (10 independent simulations, 4 µs total)', 'method': 'GROMACS 2020.3 with CHARMM36m force field'}

### Typical Conditions

- **force_field**: CHARMM36m
- **temperature**: 310 K
- **timestep**: 2 fs
- **constraints**: LINCS algorithm (4th order)
- **cutoff**: 1.2 nm for short-range interactions
- **electrostatics**: PME (Particle Mesh Ewald)


## Advantages

- Provides atomic-level insight into protein dynamics and lipid interactions
- Can capture conformational transitions not accessible by crystallography
- Validates and extends structural observations from crystallography

## Disadvantages

- Limited by force field accuracy and timescale (microseconds)
- Computationally intensive
- Cannot observe slow conformational changes (e.g., insertase-to-chaperone switch)

## Proteins Using This Method

| Protein | Resolution | PDB | Notes |
|---|---|---|---|
| [TmYidC](/xray-mp-wiki/proteins/TmYidC/) | 3.4 | 6Y86 | MD simulations validated N-AH orientation (15° tilt on membrane surface) and revealed C1 region flexibility |
| [Bacteriorhodopsin](/xray-mp-wiki/proteins/Bacteriorhodopsin/) | 2.65 | 4FPD | 60 independent MD simulations using Amber ff99SB force field across 8 crystal structures (bR ground state, K, L, M1, M2, N, N') revealed D96 protonation state controls opening of the cytoplasmic half-channel. Simulations used the D96G/F171C/F219L triple mutant structure (4FPD) with residues restored to wild-type. Simulations with deprotonated D96 showed channel opening; protonated D96 maintained a closed channel. |
| [Influenza A M2 Proton Channel](/xray-mp-wiki/proteins/Influenza A M2 Proton Channel/) | 2.50 | 6NV1 | 300 ns MD simulation of M2(22-46) V27A-spiro-adamantyl amine complex in a hydrated POPC bilayer (CHARMM36 force field, OPLS3e for ligand). Simulation accurately predicted ligand position (RMSD <1 A between MD and crystal structure) and the formation of two ordered water layers (Ala30 and Gly34 layers) between the inhibitor ammonium and His37 gate. The ligand shifted ~2 A toward the N-terminus within the first 50 ns. Chloride ion bound near Trp41 at the channel C-terminus. |
