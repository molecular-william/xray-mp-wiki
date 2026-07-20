---
title: "Solid-Supported Membrane Electrophysiology"
created: 2026-06-11
updated: 2026-06-11
type: method
category: methods
layout: default
tags: [quality-assessment, subdirectory-quality-assessment]
sources: [doi/10.1073##pnas.2403273121]
verified: regex
---

# Solid-Supported Membrane Electrophysiology

## Overview

Solid-supported membrane (SSM) electrophysiology is a technique for measuring
electrogenic transport activity of membrane proteins reconstituted into
proteoliposomes. Proteoliposomes are adsorbed onto a solid-supported membrane
(a lipid monolayer deposited on a gold electrode or other solid support), and
substrate solutions are rapidly perfused over the surface. Substrate binding
and transport by the reconstituted protein generates capacitive currents that
are recorded as a function of time. The technique provides direct, real-time
measurement of transport kinetics without the need for radioactive substrates
or fluorescent indicators.

## Protocol

### Steps

1. {'step': 'Reconstitution', 'description': 'Purified membrane protein is reconstituted into proteoliposomes at defined protein:lipid ratios via detergent removal (dialysis or Bio-Beads). For SSM measurements, higher protein:lipid ratios (~40 ug protein/mg lipid) are typically used.\n'}
2. {'step': 'Sensor preparation', 'description': 'A gold electrode or other solid support is coated with a lipid monolayer (typically a thiol-modified lipid or alkanethiol) to form the solid-supported membrane.\n'}
3. {'step': 'Proteoliposome adsorption', 'description': 'Proteoliposomes are adsorbed onto the SSM surface by incubating in the measurement chamber. The proteoliposomes fuse with the supported membrane, forming a continuous layer.\n'}
4. {'step': 'Perfusion and recording', 'description': 'Substrate-containing solutions are rapidly exchanged over the SSM surface using a fast perfusion system. Substrate-induced currents are recorded at sub-millisecond resolution. Both the amplitude and kinetics of the current report on the transport mechanism.\n'}
5. {'step': 'Data analysis', 'description': 'Current amplitudes are plotted against substrate concentration and fit to the Michaelis-Menten equation to derive apparent Km and Vmax values. The capacitive currents reflect electrogenic transport (net charge movement across the membrane per transport cycle).\n'}


## Advantages

- Direct measurement of transport activity without radioactive or fluorescent labels
- High temporal resolution (millisecond range)
- Compatible with a wide range of substrates
- Quantitative kinetic parameters (Km, Vmax)
- Small sample requirements

## Disadvantages

- Requires reconstitution into proteoliposomes
- Non-specific substrate-membrane interactions can produce background currents
- Only detects electrogenic transport (net charge movement)
- Substrate hydrophobicity can interfere with measurements
- Limited throughput compared to fluorescent assays
