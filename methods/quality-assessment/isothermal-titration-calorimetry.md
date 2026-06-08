---
title: Isothermal Titration Calorimetry (ITC)
created: 2026-05-27
updated: 2026-05-27
type: method
category: methods
layout: default
tags: [quality-assessment, subdirectory-quality-assessment]
sources: [doi/10.1016##j.immuni.2020.02.004]
verified: false
---

# Isothermal Titration Calorimetry (ITC)

## Overview

Isothermal titration calorimetry (ITC) directly measures the heat released or absorbed during molecular binding interactions. It provides complete thermodynamic characterization of protein-protein interactions, including binding affinity (Kd), stoichiometry (N), enthalpy (Delta H), and entropy (Delta S) in a single experiment. In membrane protein research, ITC is used to quantify binding affinities between receptors and ligands, compare binding thermodynamics of mutant variants, and determine binding stoichiometry independently of labeling or immobilization.

## Principle

A solution of one binding partner is titrated into a solution of the other in an isothermal calorimeter. Each injection produces a heat signal proportional to the amount of complex formed. The integrated heat per injection is plotted against the molar ratio to produce a binding isotherm. Fitting this curve to an appropriate binding model yields Kd, N, Delta H, and Delta S. The Gibbs free energy is calculated as Delta G = Delta H - T*Delta S.

## Protocol

### Reagents and Materials

- {'calorimeter': 'MicroCal Auto-ITC200 (Malvern Instruments)', 'buffer': 'PBS pH 7.4, 1 mM EDTA', 'cytokine_concentrations': '200 uM IL-17F, 275 uM IL-17A homodimer, 185 uM IL-17A/F heterodimer', 'receptor_concentrations': '36-42 uM IL-17RC or 25-35 uM IL-17RA'}

### Steps

1. {'step': 'Protein dialysis', 'description': 'All proteins dialyzed overnight against PBS pH 7.4, 1 mM EDTA\n'}
2. {'step': 'Protein quantification', 'description': 'Protein concentration quantified by HPLC using UV absorbance at 210 nm\n'}
3. {'step': 'Titration', 'description': '26 successive 3 s injections of 1.5 uL cytokine into 400 uL receptor solution with 180 s interval between successive injections\n'}
4. {'step': 'Delay', 'description': 'Initial delay of 60 s applied before first injection\n'}
5. {'step': 'Data fitting', 'description': 'Binding isotherms fitted to single-site binding model with MicroCal PEAQ-ITC software (version 1.21, Malvern)\n'}


## Advantages

- Label-free measurement of binding interactions
- Provides complete thermodynamic profile (Kd, N, Delta H, Delta S)
- Determines binding stoichiometry directly
- No immobilization or labeling required
- Works with complex mixtures

## Disadvantages

- Requires relatively large amounts of protein
- Low throughput compared to surface-based methods
- Heat signals from dilution must be accounted for
- Weak interactions (Kd > 100 uM) may be difficult to measure
