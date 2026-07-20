---
title: "Two-Electrode Voltage Clamp (TEVC)"
created: 2026-06-16
updated: 2026-06-16
type: method
category: methods
layout: default
tags: [quality-assessment, subdirectory-quality-assessment]
sources: [doi/10.1016##j.celrep.2015.12.087, doi/10.1021##acs.biochem.9b00971]
verified: regex
---

# Two-Electrode Voltage Clamp (TEVC)

## Overview

Two-electrode voltage clamp (TEVC) is an electrophysiological technique used to measure ion currents across the cell membrane of large cells such as Xenopus oocytes. Two microelectrodes are inserted: one measures membrane potential, and the other injects current to maintain a clamped voltage. This technique was used to characterize the functional properties of AmP2X and mutant P2X receptors. TEVC was also used to measure the inhibitory activity of spiro-adamantyl amine against the M2 V27A mutant and WT M2 proton channels expressed in Xenopus oocytes.

## Principle

In TEVC, a voltage-sensing electrode measures the membrane potential while a current-passing electrode injects current to hold the membrane at a user-defined command voltage. The injected current is equal and opposite to the ionic current flowing through channels in the membrane, providing a direct measure of channel activity.

## Protocol

### Reagents and Materials

- Xenopus laevis oocytes
- ND96 solution (96 mM NaCl, 2 mM KCl, 1.8 mM CaCl₂, 1 mM MgCl₂, 5 mM HEPES, pH 7.4)
- Gentamicin (50 μg/ml)
- Bath solution (100 mM NaCl, 5 mM HEPES, 2 mM MgCl₂, pH 7.3, with or without ATP)

### Steps

1. {'step': '1. Inject cRNA or cDNA into Xenopus oocytes', 'method': 'Microinjection'}
2. {'step': '2. Incubate oocytes for 4-7 days at appropriate temperature', 'method': 'Incubation in ND96 supplemented with gentamicin'}
3. {'step': '3. Impale oocyte with two microelectrodes', 'method': 'Micromanipulator-guided insertion'}
4. {'step': '4. Clamp membrane potential at holding voltage (e.g., −70 mV)', 'method': 'Voltage clamp amplifier (e.g., OC-725C, Warner)'}
5. {'step': '5. Apply agonist (e.g., ATP) and record macroscopic currents', 'method': 'Perfusion system'}

### Typical Conditions

- **temperature**: Room temperature (20-22 °C)
- **holding_potential**: −70 mV
- **recording_solution**: 100 mM NaCl, 5 mM HEPES, 2 mM MgCl₂ (pH 7.3)


## Proteins Using This Method

| Protein | Resolution | PDB | Notes |
|---|---|---|---|
| [AmP2X](/xray-mp-wiki/proteins/other-ion-channels/amp2x/) | 2.80 | 5F1C |  |
| [Influenza A M2 Proton Channel](/xray-mp-wiki/proteins/other-ion-channels/influenza-a-m2-proton-channel/) | 2.50 | 6NV1 |  |
