---
title: Time-Resolved Serial Femtosecond Crystallography (TR-SFX)
created: 2026-06-03
updated: 2026-06-03
type: method
category: methods
layout: default
tags: [structure-xray, subdirectory-structure-determination]
sources: [doi/10.7554##eLife.62389, doi/10.1038##nature13453, doi/10.1038##nature21400]
verified: false
---

# Time-Resolved Serial Femtosecond Crystallography (TR-SFX)

## Overview

Time-resolved serial femtosecond crystallography (TR-SFX) is an X-ray crystallography technique that uses X-ray free electron lasers (XFELs) to capture structural changes in proteins at microsecond to millisecond timescales. Samples are delivered as microcrystals in a liquid jet, and a pump-probe scheme is used: a laser pulse triggers the reaction (pump), and an XFEL pulse diffracts the crystal (probe) at a defined delay time. The femtosecond X-ray pulse captures diffraction before radiation damage occurs, enabling time-resolved structural studies of light-sensitive proteins and other dynamic processes.

## Principle

TR-SFX exploits the diffraction-before-destruction principle of XFEL pulses. Each femtosecond X-ray pulse captures a complete diffraction pattern from a single microcrystal before radiation damage destroys the sample. By using a pump-probe scheme — where a laser pulse (pump) triggers a reaction and an XFEL pulse (probe) captures the structural state at a defined delay — TR-SFX can reconstruct the time evolution of structural changes. Room-temperature delivery via liquid jets, lipidic cubic phase injectors, or high viscosity extrusion injectors ensures continuous sample renewal.

## Protocol

### Reagents and Materials

- Microcrystals of target protein
- Delivery medium (water, cryo-protectant, or lipidic matrix)
- Pump laser (optical, IR, or UV) for triggering reaction
- XFEL pulse for diffraction

### Steps

1. Grow protein microcrystals (typically 0.1-10 µm)
2. Mix crystals with delivery medium and any triggering reagents
3. Load into injector (liquid jet, LCP, or high viscosity extrusion)
4. Deliver crystals to XFEL beam intersection point
5. Apply pump laser pulse to initiate reaction
6. After defined delay, fire XFEL pulse to capture diffraction pattern
7. Repeat for millions of crystals across different delay times
8. Index, integrate, and merge diffraction patterns
9. Solve structures at each time point by molecular replacement


## Advantages

- Captures transient intermediates inaccessible to conventional crystallography
- Room-temperature structures more physiologically relevant
- No radiation damage due to femtosecond pulse duration
- No need for cryocooling
- Can study light-sensitive proteins with optical pumping

## Disadvantages

- Requires XFEL facility access (limited availability)
- Large number of crystals needed (millions)
- Complex data processing and merging
- Limited to proteins that can form microcrystals
- Lower throughput than synchrotron methods

## Proteins Using This Method

| Protein | Resolution | PDB | Notes |
|---|---|---|---|
| [Channelrhodopsin C1C2](/xray-mp-wiki/proteins/Channelrhodopsin C1C2/) | 1.7-2.8 | 7E6X, 7E6Z, 7E70, 7E71 | TR-SFX at SACLA XFEL captured 6 time points (dark, 1 us, 50 us, 250 us, 1 ms, 4 ms) revealing early conformational changes in TM3 and TM7 |
| [Photosystem II](/xray-mp-wiki/proteins/Photosystem II/) | 5.0 | 4PBU | TR-SFX at LCLS CXI captured dark S1 state; gas focusing liquid injector at 10 °C; 120 Hz FEL |
| [Photosystem II](/xray-mp-wiki/proteins/Photosystem II/) | 5.5 | 4Q54 | TR-SFX at LCLS captured double-flash putative S3 state; revealed Mn4CaO5 elongation during S2-S3 transition |
| [Photosystem II](/xray-mp-wiki/proteins/Photosystem II/) | 2.35 | 5WS5, 5WS6 | TR-SFX at SACLA XFEL on T. vulcanus PSII at 2.35 A; pre-flashed with potassium ferricyanide; revealed O=O bond formation site (O6 near O5) |
