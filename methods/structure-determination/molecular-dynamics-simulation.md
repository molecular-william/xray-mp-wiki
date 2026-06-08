---
title: Molecular Dynamics Simulation
created: 2026-05-29
updated: 2026-05-29
type: method
category: methods
layout: default
tags: [structure-refinement, subdirectory-structure-determination]
sources: [doi/10.1038##nature09580, doi/10.1038##ncomms3465, doi/10.1038##nature22035]
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
- {'name': 'POPC lipid bilayer', 'purpose': 'Membrane environment'}

### Steps

1. {'step': 'System setup', 'method': 'Protein embedded in POPC lipid bilayer with explicit TIP3P water', 'notes': 'Periodic boundary conditions applied'}
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
| /xray-mp-wiki/proteins/vsglt/ | 2.7 | 3DH4, 3DH5 | 200 ns unrestrained MD simulation of galactose exit from vSGLT; N64A and N64S mutants studied to investigate Y263 rotamer gating |
| /xray-mp-wiki/proteins/navms/ | 2.9 | 3ZJZ | Coarse-grained MD simulations combined with DEER spectroscopy to model the flexible C-terminal domain of NavMs-pore + CTD; dynamic model of the linker and coiled-coil region informed by EPR distance distributions |
