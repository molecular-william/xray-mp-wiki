---
title: "Time-Resolved Serial Synchrotron Crystallography (TR-SMX)"
created: 2026-06-08
updated: 2026-06-08
type: method
category: methods
layout: default
tags: [structure-xray, subdirectory-structure-determination]
sources: [doi/10.1107##s2059798322004144, doi/10.1126##science.aaw8634]
verified: regex
---

# Time-Resolved Serial Synchrotron Crystallography (TR-SMX)

## Overview

Time-resolved serial synchrotron crystallography (TR-SMX) adapts injector-based serial crystallography methods originally developed at XFELs to widely available synchrotron sources for time-resolved measurements in the millisecond range. Using a high-viscosity injector to deliver microcrystals and a pump-probe scheme with a laser diode synchronized to a fast photon-counting detector, TR-SMX captures structural changes in light-activated proteins over 200 ms with 5-ms timepoints. The method achieves results comparable to XFEL-based time-resolved studies while consuming less than 20 ul of microcrystal slurry, substantially lowering the entry barrier for time-resolved crystallographic studies.

## Principle

TR-SMX uses a pump-probe scheme at a synchrotron beamline. Microcrystals embedded in a high-viscosity medium (e.g., lipidic cubic phase) are extruded through a nozzle and intersect a monochromatic synchrotron X-ray beam. A laser diode activated by a delay generator triggers the photoreaction (pump), and the synchrotron X-rays capture diffraction (probe) after a defined delay. A fast detector operating at 200 Hz collects consecutive frames (5 ms each) to track the evolution of structural intermediates over time. The slow extrusion rate minimizes sample consumption to <20 ul, and the stable monochromatic beam and photon-counting detector provide high data quality. The method can achieve resolutions of ~2.3 A, limited primarily by available photon flux rather than crystal quality.

## Protocol

### Reagents and Materials

- Microcrystals of target protein in lipidic cubic phase or other high-viscosity carrier
- Laser diode (e.g., class 3R) for photoactivation

### Steps

1. Grow protein microcrystals (typically 5-50 um)
2. Load crystal slurry into high-viscosity injector syringe
3. Extrude crystals through nozzle at slow flow rate
4. Synchronize laser and detector via delay generator
5. Expose crystals to laser for 5 ms during first detector frame
6. Collect 40 consecutive frames (5 ms each) to track reaction over 200 ms
7. Index, integrate, and merge diffraction patterns using software like CrystFEL
8. Refine occupancies of structural intermediates against time-resolved data


## Advantages

- Accessible at widely available synchrotron sources (not limited to XFELs)
- Very low sample consumption (<20 ul microcrystal slurry vs. milliliters for XFELs)
- Stable monochromatic beam and photon-counting detector improve data quality
- High activation levels from millisecond laser exposure
- Can track complete reaction cycles (200 ms+) in single experiment

## Disadvantages

- Limited time resolution (~5 ms per timepoint, microsecond range with further development)
- Resolution limited by available synchrotron photon flux
- Requires fast detectors (200 Hz or faster)
- Limited to photoactivatable or mixable reactions

## Proteins Using This Method

| Protein | Resolution | PDB | Notes |
|---|---|---|---|
| [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) | 2.3 |  | TR-SMX at Swiss Light Source captured structural changes in bR over 200 ms with 5 ms timepoints. Revealed open-state conformation with helix F movement of 9 A and water chain formation for reprotonation. ~13,000 indexable diffraction patterns per timepoint. |
