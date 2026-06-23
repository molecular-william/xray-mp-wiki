---
title: Molecular Dynamics Simulation
created: 2026-05-29
updated: 2026-05-29
type: method
category: methods
layout: default
tags: [structure-refinement, subdirectory-structure-determination]
sources: [doi/10.1107##s205225252100213x, doi/10.1186##s12915-021-01102-4, doi/10.1126##science.aad3873, doi/10.1085##jgp.201411219, doi/10.1073##pnas.2009624117, doi/10.1038##s41467-021-27726-2, doi/10.1038##nature09580, doi/10.1038##ncomms3465, doi/10.1038##nature22035, doi/10.1073##pnas.2014896117, doi/10.1126##science.1243352, doi/10.1107##s2052252522001907, doi/10.1085##jgp.201711884, doi/10.1126##scisignal.ado8741, doi/10.1093##nar##gkad910, doi/10.3390##ijms21093110]
verified: false
---

# Molecular Dynamics Simulation

## Overview

Molecular dynamics (MD) simulation is a computational technique for studying the physical movements of atoms and molecules over time. In the context of membrane protein crystallography, MD simulations are used to explore conformational dynamics, validate crystal structures, study substrate transport mechanisms, and investigate the effects of mutations on protein function.

## Protocol

### Reagents and Materials

- {'name': 'GROMACS simulation engine', 'purpose': 'MD simulation'}
- {'name': 'CHARMM force field', 'purpose': 'Atomistic force field'}
- {'name': 'TIP3P water model', 'purpose': 'Explicit water model'}
- {'name': '[POPC](/xray-mp-wiki/reagents/lipids/popc/) lipid bilayer', 'purpose': 'Membrane environment'}

### Steps

1. {'step': 'System setup', 'method': 'Protein embedded in [POPC](/xray-mp-wiki/reagents/lipids/popc/) lipid bilayer with explicit TIP3P water', 'notes': 'Periodic boundary conditions applied'}
2. {'step': 'Energy minimization', 'method': 'Steepest descent minimization', 'notes': 'Remove steric clashes'}
3. {'step': 'Equilibration', 'method': 'NVT and NPT equilibration with position restraints', 'notes': 'Gradual release of restraints'}
4. {'step': 'Production simulation', 'method': 'Unrestrained or restrained MD simulation', 'notes': '100-200 ns simulation timescales for conformational sampling'}


## Advantages

- Provides atomic-level insights into conformational dynamics not accessible from static crystal structures
- Can simulate mutant effects on protein function and gating mechanisms
- Validates and extends structural observations from X-ray crystallography

## Disadvantages

- Limited to nanosecond-microsecond timescales, may not capture slow conformational transitions
- Force field accuracy affects reliability of results
- Computationally expensive for large membrane protein systems

## Proteins Using This Method

| Protein | Resolution | PDB | Notes |
|---|---|---|---|
| /xray-mp-wiki/proteins/slc-transporters/vsglt/ | 2.7 | 3DH4, 3DH5 | 200 ns unrestrained MD simulation of galactose exit from [VSGLT](/xray-mp-wiki/proteins/slc-transporters/vsglt/); N64A and N64S mutants studied to investigate Y263 rotamer gating |
| /xray-mp-wiki/proteins/voltage-gated-channels/navms/ | 2.9 | 3ZJZ | Coarse-grained MD simulations combined with DEER spectroscopy to model the flexible C-terminal domain of NavMs-pore + CTD; dynamic model of the linker and coiled-coil region informed by EPR distance distributions |
| /xray-mp-wiki/proteins/pumps-atpases/serca1a-e340a/ | 3.2 |  | 3 x 200 ns all-atom MD simulations of [SERCA1a (Sarcoplasmic Reticulum Ca2+-ATPase)](/xray-mp-wiki/proteins/pumps-atpases/serca1a/) E340A and wild-type in [POPC](/xray-mp-wiki/reagents/lipids/popc/) bilayers using CHARMM36 force field (GROMACS). Confirmed that the ~10 A downward headpiece rotation and loss of A-domain contacts persist in dynamic membrane environment. Revealed irreversible Arg822 swing-out and M1 helix rigidification in the mutant. |
| /xray-mp-wiki/proteins/enzymes/narq/ | 2.4 | 6YUE, 5IJI, 5JEQ | 7 all-atom MD simulations (880-1000 ns each) of [NARQ](/xray-mp-wiki/proteins/enzymes/narq/) sensor-TM-HAMP fragment (ligand-bound WT, ligand-free WT, ligand-free R50S mutant) in [POPG](/xray-mp-wiki/reagents/lipids/popg/)/POPE bilayer using CHARMM36 force field (GROMACS). Simulations showed that ligand removal from WT causes transition to ligand-free-like conformation with Gly47 helical rotation, diagonal scissoring of H1/H4 helices, restoration of continuous alpha-helix between TM1 and H1, and piston-like shifts of TM helices. R50S mutant MD simulations showed fast transition from crystal structure to ligand-free-like state, confirming crystallographic trapping. |
