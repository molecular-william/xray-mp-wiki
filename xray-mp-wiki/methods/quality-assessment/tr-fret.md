---
title: "Time-Resolved Fluorescence Resonance Energy Transfer (TR-FRET)"
created: 2026-05-27
updated: 2026-05-27
type: method
category: methods
layout: default
tags: [quality-assessment, subdirectory-quality-assessment]
sources: [doi/10.1016##j.immuni.2020.02.004]
verified: regex
---

# Time-Resolved Fluorescence Resonance Energy Transfer (TR-FRET)

## Overview

Time-resolved fluorescence resonance energy transfer (TR-FRET) is a biophysical technique that monitors molecular interactions at nanomolar concentrations by measuring energy transfer between a lanthanide donor and a fluorescent acceptor. TR-FRET uses time-gated detection to eliminate background fluorescence, enabling sensitive measurement of binding events in complex mixtures. In membrane protein research, TR-FRET is used to monitor receptor-receptor and receptor-ligand interactions, determine binding stoichiometries, and compare the relative affinities of different ligands or receptor variants.

## Principle

A lanthanide donor (e.g., europium-streptavidin) is excited by a pulsed light source and emits at a characteristic wavelength after a time delay. If a fluorescent acceptor (e.g., Alexa Fluor 647) is within approximately 10 nm, energy transfer occurs and the acceptor emits at its characteristic wavelength. The TR-FRET ratio is calculated as the acceptor emission divided by the donor emission. The ratio is highly dependent on the distance between donor and acceptor, enabling detection of interactions at concentrations far below those required by other methods.

## Protocol

### Reagents and Materials

- {'donor': 'Europium-streptavidin (Perkin Elmer, cat# AD0062)', 'acceptor_label': 'Alexa Fluor 647 NHS Ester (Thermo Fisher, cat# A20006)', 'labeling_method': 'Biotinylation with EZ-link Sulfo NHS-LC-Biotin (Thermo Fisher, cat# 21338) for streptavidin-donor binding; Alexa Fluor 647 conjugation for acceptor\n'}

### Steps

1. {'step': 'Reagent preparation', 'description': 'Label one receptor with Alexa Fluor 647 and biotinylate the other receptor for streptavidin-donor binding\n'}
2. {'step': 'Binding reaction', 'description': 'Mix labeled receptors with cytokine at various concentrations\n'}
3. {'step': 'Signal detection', 'description': 'Measure TR-FRET signal as ratio of fluorescence at 665 nm to 615 nm multiplied by 1000\n'}
4. {'step': 'Data analysis', 'description': 'Plot TR-FRET ratio as function of cytokine concentration; error bars represent standard deviation of three replicates\n'}


## Advantages

- Sensitive enough to detect interactions at ~1000-fold lower concentrations than [SEC-MALS](/xray-mp-wiki/methods/quality-assessment/sec-mals/)
- Time-gated detection eliminates background fluorescence
- Homogeneous assay format (no separation steps required)
- Suitable for high-throughput screening
- Can monitor real-time binding kinetics

## Disadvantages

- Requires fluorescent labeling of one or both binding partners
- Labeling may affect binding properties
- Distance-dependent; requires close proximity (typically <10 nm)
- Limited to binary or ternary interaction analysis
