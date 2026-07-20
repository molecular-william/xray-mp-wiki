---
title: "Inside-Out Patch Clamp Electrophysiology"
created: 2026-06-16
updated: 2026-06-16
type: method
category: methods
layout: default
tags: [quality-assessment, subdirectory-quality-assessment]
sources: [doi/10.1038##nature10370]
verified: regex
---

# Inside-Out Patch Clamp Electrophysiology

## Overview

Inside-out patch clamp electrophysiology is a variant of the patch clamp technique in which a patch of membrane is excised from the cell, exposing the cytoplasmic face to the bath solution. This configuration allows precise control of the intracellular environment and was used to study PIP2 regulation of Kir2.2 channels, where PIP2 depletion causes channel 'run-down' and exogenous PIP2 restores channel activity.

## Principle

In the inside-out configuration, a gigaohm seal is formed with a micropipette on the cell surface, then the pipette is rapidly withdrawn to excise a patch of membrane. The cytoplasmic side of the membrane faces the bath solution, allowing application of test compounds (e.g., PIP2) to the intracellular face while recording ionic currents through channels in the patch.

## Protocol

### Reagents and Materials

- Xenopus laevis oocytes expressing Kir2.2 cRNA
- ND96 solution (96 mM NaCl, 2 mM KCl, 1.8 mM CaCl2, 1 mM MgCl2, 50 ug/mL gentamycin, pH 7.6 with NaOH)
- ND96 + 200 mM NaCl (for vitelline membrane removal)
- Short-chain (dioctanoyl) PIP2 (10 mM stock in water)

### Steps

1. {'step': '1. Oocyte preparation', 'method': 'Inject 50 nL of ~2 mg/mL Kir2.2 cRNA into Xenopus oocytes', 'notes': 'Incubate for 2-3 days before recording'}
2. {'step': '2. Vitelline membrane removal', 'method': 'Hyperosmotic treatment + mechanical removal', 'buffer': 'ND96 + 200 mM NaCl for 5-10 min'}
3. {'step': '3. Seal formation', 'method': 'On-cell patch clamp', 'notes': 'Pipette resistance 0.4-0.9 MOhm; large inside-out patches with currents 0.2-5 nA'}
4. {'step': '4. Patch excision', 'method': 'Rapid pipette withdrawal', 'notes': 'Inside-out configuration exposing cytoplasmic face to bath'}
5. {'step': '5. Current recording', 'method': 'Voltage ramp from -80 to +80 mV', 'notes': 'Macroscopic currents recorded immediately, during PIP2 depletion (run-down), and after adding short-chain PIP2 to bath'}

### Typical Conditions

- **temperature**: Room temperature
- **recording_solution**: Bath solution with variable PIP2 concentration
- **pipette_resistance**: 0.4-0.9 MOhm


## Proteins Using This Method

| Protein | Resolution | PDB | Notes |
|---|---|---|---|
| [Chicken Kir2.2](/xray-mp-wiki/proteins/voltage-gated-channels/kir2-2-channel/) | N/A (functional study) | 3SPI | Inside-out patch clamp was used to demonstrate PIP2-mediated activation of Kir2.2. Endogenous PIP2 depletion causes run-down; exogenous short-chain PIP2 restores activity in a dose-dependent manner. |
