---
title: Differential Static Light Scattering (DSLS)
created: 2026-06-16
updated: 2026-06-16
type: method
category: methods
layout: default
tags: [quality-assessment, xray-crystallography]
sources: [doi/10.1021##acs.jmedchem.5b00330]
verified: false
---

# Differential Static Light Scattering (DSLS)

## Overview

Differential static light scattering (DSLS) is a biophysical screening method used to detect ligand-induced shifts in the temperature-dependent aggregation of proteins. It serves as a thermal stability assay to identify protein-ligand complexes most likely to crystallize. DSLS is particularly effective for integral membrane proteins due to its general lack of sensitivity to the presence of detergent.

## Principle

DSLS (implemented in instruments such as the Stargazer-384 from Harbinger Biotech) monitors the aggregation of a protein sample as a function of temperature by measuring static light scattering. The aggregation temperature (Tagg) is defined as the temperature at which protein aggregation begins. Ligand binding typically stabilizes a protein, shifting the aggregation temperature to a higher value. A larger shift correlates with increased thermal stabilization and, for membrane protein crystallography, a greater likelihood of successful crystallization.

## Protocol

### Reagents and Materials

- Purified membrane protein in detergent solution
- Ligand/inhibitor compound
- Assay buffer (detergent-containing GF buffer)

### Steps

1. Dilute purified protein to ~0.2 mg/mL in appropriate buffer (e.g., GF buffer for mPGES-1)
2. Add ligand/inhibitor at appropriate concentration (e.g., 100 microM for mPGES-1 inhibitors)
3. Transfer 35 microL sample to a 384-well clear bottom plate
4. Apply temperature gradient from 25.0 to 85.0 degrees Celsius at a ramp rate of 1.0 degree Celsius/min
5. Monitor static light scattering throughout the temperature ramp
6. Calculate aggregation temperatures using instrument software (e.g., Bioactive software from Harbinger Biotech)
7. Compare Tagg values between apo and ligand-bound samples to determine stabilization


## Proteins Using This Method

| Protein | Resolution | PDB | Notes |
|---|---|---|---|
| [mPGES-1](/xray-mp-wiki/proteins/mPGES-1/) | 1.41 | 4YK5 | DSLS used to prioritize mPGES-1/inhibitor complexes for crystallization. Compounds 5, 63, 30, and 3 imparted shifts of 7.8, 10.4, 5.4, and 7.3 degrees Celsius, respectively. All four yielded crystal structures. |
