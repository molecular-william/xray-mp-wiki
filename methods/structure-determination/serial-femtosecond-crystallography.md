---


title: Serial Femtosecond Crystallography (SFX)
created: 2026-04-27
updated: 2026-04-27
type: method
tags: [structure-xray, structure-refinement]
sources: [doi/10.1016##j.cell.2015.04.011]


category: methods
---
layout: default



# Serial Femtosecond Crystallography (SFX)

## Overview

Serial femtosecond crystallography (SFX) is a method for determining macromolecular structures using X-ray free-electron lasers (XFELs). Unlike conventional crystallography that uses large crystals at synchrotrons, SFX uses microcrystals (often too small for synchrotron diffraction) delivered as a continuous stream into femtosecond X-ray pulses.

## Principle

1. **Microcrystal delivery**: Microcrystals (typically 1–10 μm) are injected into the XFEL beam as a liquid jet or via lipidic cubic phase (LCP)
2. **Femtosecond X-ray pulses**: XFEL delivers X-ray pulses of ~10–50 femtoseconds duration
3. **Diffraction before destruction**: The pulse is so short that diffraction data is collected before the crystal is destroyed by radiation damage ("diffraction before destruction")
4. **Serial data collection**: Thousands to millions of microcrystals are exposed, each contributing a diffraction pattern
5. **Data merging**: Patterns from many crystals are merged to produce a complete dataset

## LCP-SFX Method

For membrane proteins, the **LCP-SFX** (lipidic cubic phase [serial-femtosecond-crystallography](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/)) method was developed:
- Microcrystals are grown and suspended in LCP ([monoolein](/xray-mp-wiki/methods/crystallization/monoolein/)-based mesophase)
- LCP containing microcrystals is injected into the XFEL beam via a specialized injector
- The LCP serves as both the crystallization matrix and the delivery medium
- This method has been particularly successful for GPCR structure determination

## Advantages

- **No crystal size requirement**: Works with microcrystals too small for synchrotron diffraction
- **Room-temperature structures**: Data collected at physiological temperatures, capturing native conformations
- **Radiation damage avoidance**: Femtosecond pulses collect data before radiation damage occurs
- **Time-resolved studies**: Potential for capturing intermediate states in reaction cycles

## Disadvantages

- **XFEL access**: Requires access to XFEL facilities (limited beamtime)
- **Data complexity**: Millions of diffraction patterns require specialized processing software
- **Sample consumption**: Large amounts of protein needed for continuous injection
- **Indexing challenges**: Overlapping patterns and variable crystal orientations

## Notable SFX Structures

| Protein | Resolution | XFEL Facility | PDB |
|---------|-----------|---------------|-----|
| AT1R-ZD7155 | 2.9 Å | LCLS (SLAC) | 4YAY |
| Photosystem II | 1.95 Å | SACLA | Various |
| Myoglobin | 2.0 Å | LCLS | Various |

## Comparison with Synchrotron Crystallography

| Feature | Synchrotron | SFX/XFEL |
|---------|------------|----------|
| Crystal size | Large (≥50 μm) | Micro (1–10 μm) |
| Temperature | Typically 100 K (cryo) | Room temperature |
| Radiation damage | Significant | Avoided (femtosecond pulse) |
| Data collection time | Hours | Minutes |
| Beamline access | More available | Limited |

## Data Processing Software

- **CrystFEL**: Software suite for snapshot serial crystallography
- **cctbx.xfel**: X-ray free-electron laser processing tools
- **KAMO**: Automated data collection and processing system

## Related Methods

- [xray-crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/) — X-ray crystallography overview
- [lipidic-cubic-phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP crystallization method
- [cryoem](/xray-mp-wiki/methods/structure-determination/cryoem/) — Cryo-EM alternative for challenging targets