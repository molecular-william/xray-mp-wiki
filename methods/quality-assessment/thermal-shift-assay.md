---
title: Thermal Shift Assay (Fluorescent CPM)
created: 2026-05-29
updated: 2026-05-29
type: method
category: methods
layout: default
tags: [quality-assessment, subdirectory-quality-assessment]
sources: [doi/10.1186##s12915-021-01102-4, doi/10.1038##s41467-021-27726-2, doi/10.1016##j.str.2017.12.013, doi/10.1016##j.str.2008.04.013, doi/10.1016##j.str.2018.01.005]
verified: false
---

# Thermal Shift Assay (Fluorescent CPM)

## Overview

Thermal shift assays (also known as differential scanning fluorescence or CPM assays) measure protein thermal stability by tracking the exposure of hydrophobic regions as the protein unfolds with increasing temperature. The fluorescent probe CPM (N-[4-(7-diethylamino-4-methyl-3-coumarinyl)phenyl]maleimide) binds to exposed cysteine residues, and the increase in fluorescence is monitored as a function of temperature to determine the melting temperature (Tm). This method is widely used for screening ligands that stabilize membrane proteins and for optimizing purification conditions.

## Principle

The CPM probe contains a maleimide group that reacts specifically with free cysteine thiols. In the folded state, few cysteines are accessible, resulting in low fluorescence. As temperature increases and the protein unfolds, hydrophobic regions and cysteine residues become exposed, increasing CPM binding and fluorescence. The midpoint of the fluorescence transition corresponds to the melting temperature (Tm), which reflects the thermal stability of the protein. Ligand binding that stabilizes the protein shifts the Tm to higher temperatures.

## Protocol

### Reagents and Materials

- CPM (N-[4-(7-diethylamino-4-methyl-3-coumarinyl)phenyl]maleimide)
- Dimethylformamide (DMF)
- HEPES buffer
- NaCl
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) detergent
- [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) hydrogen [Succinate (Succinic Acid)](/xray-mp-wiki/reagents/ligands/succinate/)
- Ligands for stabilization screening

### Steps

1. {'step': 'CPM stock preparation', 'method': 'Dissolve CPM at 4 mg/ml in dimethylformamide; further diluted 1:1000 v/v in sample buffer', 'notes': 'Sample buffer: 50 mM HEPES pH 7.0, 150 mM NaCl, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)'}
2. {'step': 'Protein-ligand incubation', 'method': 'Incubate protein with ligand on ice for 30 minutes', 'notes': 'Approximately 5 ug protein in 200 ul total volume; ligands prepared in appropriate stock solutions'}
3. {'step': 'Fluorescence measurement', 'method': 'Cary Eclipse spectrofluorometer with quartz cuvettes; temperature ramp from 20 C to 90 C at 2 C/min', 'notes': 'Excitation wavelength 384 nm, emission wavelength 470 nm'}
4. {'step': 'Data analysis', 'method': 'Normalize data and fit to Boltzmann sigmoidal function using Prism software', 'notes': 'Tm determined from midpoint of transition; experiments performed in triplicate'}


## Advantages

- Sensitive detection of protein unfolding transitions
- Requires small amounts of protein (approximately 5 ug)
- Can screen multiple ligands to identify stabilizers
- Works with membrane proteins in detergent solution
- Provides quantitative Tm values for comparing stability

## Disadvantages

- Requires accessible cysteine residues for CPM binding
- CPM probe may affect protein stability at high concentrations
- Detergent choice can affect fluorescence baseline
- Not suitable for proteins lacking free cysteines without engineering

## Proteins Using This Method

| Protein | Resolution | PDB | Notes |
|---|---|---|---|
| [A2AAR-S91A](/xray-mp-wiki/proteins/gpcr/a2aar-s91a/) | not applicable | 5WF6 | Thermal shift assays used to characterize stability of S91A variant with panel of pharmacological ligands |
| [PepT_St Proton-Dependent Oligopeptide Transporter](/xray-mp-wiki/proteins/PepT_St Proton-Dependent Oligopeptide Transporter/) | not applicable | -- | DSF used for peptide binding screen of 28 different di- and tripeptides; thermal stability peaked at pH 4.5; 100 mM HEPES pH 7.0, 150 mM NaCl, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) used in purification buffer; NM (nonylmaltoside) used for DSF to maximize peptide stabilization signal |
| [A2AAR-D52N](/xray-mp-wiki/proteins/gpcr/a2aar-d52n/) | not applicable | 5WF5 | Thermal shift assays used to compare stability of A2AR-D52N vs wild-type [A2AR](/xray-mp-wiki/proteins/gpcr/human-adenosine-a2a-receptor-a2ar/) across multiple ligands; apo [A2AAR-D52N](/xray-mp-wiki/proteins/gpcr/a2aar-d52n/) showed ~8 C increase in Tm over apo A2AAR |
