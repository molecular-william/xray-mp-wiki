---
title: "Static Light Scattering"
created: 2026-06-02
updated: 2026-06-16
type: method
category: methods
layout: default
tags: [quality-assessment, subdirectory-quality-assessment]
sources: [doi/10.1021##acs.jmedchem.5b00330, doi/10.1038##cr.2017.83]
verified: regex
---

# Static Light Scattering

## Overview

Static light scattering (SLS) is a biophysical technique used to determine the molecular weight and oligomerization state of proteins in solution. By measuring the intensity of light scattered by a protein solution at zero angle, SLS provides an absolute measurement of the weight-average molecular weight independent of elution volume or shape assumptions. SLS is commonly coupled with size exclusion chromatography (SEC-LS) to analyze the oligomeric state of membrane proteins in detergent solution.

## Protocol

### Reagents and Materials

- {'protein_sample': 'Purified protein at approximately 1 mg/ml concentration.'}
- {'buffer': 'Buffer matching the protein sample, typically containing the detergent used for protein solubilization.'}

### Steps

1. {'step': 'Sample preparation', 'description': 'Purify protein and concentrate to approximately 1 mg/ml. Ensure sample is monodisperse by SEC prior to SLS analysis.'}
2. {'step': 'SEC separation', 'description': 'Inject 100 ul of protein sample onto a gel filtration column (e.g., WTC-030S5). Elute isocratically at 0.5 ml/min in buffer containing the appropriate detergent.'}
3. {'step': 'Light scattering detection', 'description': 'Detect scattered light using a light scattering instrument (e.g., Wyatt Tri Star Mini Dawn) coupled with UV detection. Data collected at 0.5 ml/min flow rate.'}
4. {'step': 'Data analysis', 'description': 'Analyze scattering data to determine molecular weight of each elution peak. Compare to theoretical monomer and dimer molecular weights to determine oligomeric state.'}


## Advantages

- Provides absolute molecular weight independent of shape
- Can detect multiple oligomeric states in equilibrium
- Non-destructive, reversible measurement
- Compatible with detergent-containing buffers

## Disadvantages

- Requires specialized equipment (light scattering detector)
- Sensitive to dust and aggregates
- Requires relatively concentrated samples
- Signal can be affected by detergent micelles

## Proteins Using This Method

| Protein | Resolution | PDB | Notes |
|---|---|---|---|
| [Uracil:Proton Symporter UraA](/xray-mp-wiki/proteins/slc-transporters/uraA/) | not applicable | not applicable | SLS used to demonstrate that wild-type UraA exists in monomer-dimer equilibrium in detergent micelles. Constitutive monomeric mutants (M1, M2) showed monomeric molecular weight, while constitutive dimer showed dimeric molecular weight. |
| [mPGES-1](/xray-mp-wiki/proteins/enzymes/mpges-1/) | 1.41 | 4YK5 | DSLS used to prioritize mPGES-1/inhibitor complexes for crystallization. Compounds 5, 63, 30, and 3 imparted shifts of 7.8, 10.4, 5.4, and 7.3 degrees Celsius, respectively. All four yielded crystal structures. |

## Related Methods

- [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — SLS is commonly coupled with SEC for oligomerization analysis
- [Thermal Shift Assay](/xray-mp-wiki/methods/quality-assessment/thermal-shift-assay/) — Complementary method for assessing protein stability and oligomerization

## Related Reagents

- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Commonly used detergent for SLS analysis of membrane proteins
