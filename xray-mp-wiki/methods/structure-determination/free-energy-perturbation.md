---
title: Free Energy Perturbation
created: 2026-05-27
updated: 2026-05-27
type: method
category: methods
layout: default
tags: [structure-refinement, subdirectory-structure-determination]
sources: [doi/10.1016##j.jmb.2020.06.012]
verified: false
---

# Free Energy Perturbation

## Overview

Free energy perturbation (FEP) is a computational method for calculating free energy differences between two states of a system using alchemical transformations. In membrane protein research, FEP is used to compute relative binding affinities, ion selectivity, and the thermodynamic impact of mutations. The method works by gradually transforming one molecular species into another through a non-physical pathway parameterized by a coupling parameter lambda (lambda), which interpolates between the initial and final states.

## Principle

FEP calculates the free energy difference between two states A and B using the Zwanzig equation: Delta_G = -kT * ln(exp(-Delta_U/kT)), where Delta_U is the energy difference between the two states sampled from state A. In practice, the transformation is performed through a series of intermediate lambda windows, where the potential function linearly interpolates between the two end states: U(lambda) = (1-lambda)*U_A + lambda*U_B. Each lambda window is simulated independently, and the free energy differences between adjacent windows are summed to obtain the total free energy change. The ParseFEP method or BAR/TI analysis is used to extract free energies from the simulation data.

## Protocol

### Reagents and Materials

- Protein structure with ion/ligand bound (PDB or MD model)
- Force field parameters (e.g., CHARMM C36, Drude polarizable)
- Simulation software (e.g., NAMD, GROMACS, AMBER)
- Alchemical transformation parameters (lambda schedule, restraints)
- Analysis tools (ParseFEP, WHAM, BAR)

### Steps

1. {'step': 'Define transformation', 'description': 'Identify the two states to be transformed (e.g., K+ vs Na+ at a specific binding site). Define the alchemical pathway using a coupling parameter lambda varying from 0 (state A) to 1 (state B).'}
2. {'step': 'Set up lambda windows', 'description': 'Create a series of evenly spaced lambda windows (typically 11-21 windows) between 0 and 1. Each window has a mixed potential function interpolating between the two end states.'}
3. {'step': 'Equilibrate each window', 'description': 'For each lambda window, perform energy minimization followed by equilibration (typically 1 ns). Apply restraints to keep ions in their respective binding sites (e.g., flat-bottom planar harmonic restraints with force constant of 100 kcal/mol/A^2/A^2).'}
4. {'step': 'Run production simulations', 'description': 'Run production simulations for each lambda window (typically 10 ns per window). Save trajectories for analysis. Use the same force field and simulation conditions for all windows.'}
5. {'step': 'Analyze free energy', 'description': 'Use ParseFEP or WHAM to analyze the simulation data and extract free energy differences. The free energy of replacing K+ by Na+ at a binding site is calculated relative to the same substitution in bulk water, giving the selectivity free energy Delta_Delta_G.'}

### Typical Conditions

- **temperature**: 298 K
- **pressure**: 1 atm (NPT ensemble)
- **lambda_windows**: 11 evenly spaced values from 0 to 1
- **equilibration_time**: 1 ns per lambda window
- **sampling_time**: 10 ns per lambda window
- **restraints**: Flat-bottom planar harmonic, force constant 100 kcal/mol/A^2/A^2


## Advantages

- Provides quantitative free energy differences for ion selectivity
- Can compute selectivity at individual binding sites within the filter
- Alchemical approach avoids sampling conformational changes
- Compatible with both additive and polarizable force fields
- Direct comparison to electrophysiological measurements

## Disadvantages

- Computationally expensive (multiple lambda windows, each requiring long simulations)
- Requires careful setup of restraints and lambda schedule
- Convergence can be slow for complex transformations
- Force field accuracy limits quantitative predictions
- Results depend on initial ion configurations
