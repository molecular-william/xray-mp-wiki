---
title: Single-Crystal Microspectrophotometry
created: 2026-05-29
updated: 2026-05-29
type: method
category: methods
layout: default
tags: [structure-xray, subdirectory-structure-determination]
sources: [doi/10.1038##44623]
verified: false
---

# Single-Crystal Microspectrophotometry

## Overview

Single-crystal microspectrophotometry is a technique for recording absorption spectra of individual protein crystals at controlled temperatures. It enables characterization of the photochemical state of light-sensitive membrane proteins (such as bacteriorhodopsin) in the crystalline state before and during X-ray data collection, ensuring that the crystal has reached the desired photointermediate.

## Principle

A portable microspectrophotometer directs a light beam through a single crystal and measures the transmitted intensity across a wavelength range. By comparing spectra at different temperatures or illumination states, researchers can determine the optical density, photostationary state composition, and photochemical behavior of the crystal under study. This information guides the selection of illumination conditions for time-resolved or intermediate-trapping crystallography experiments.

## Protocol

### Reagents and Materials

- 532 nm laser diode (100 mW) for crystal illumination
- Liquid nitrogen for cryocooling
- Portable microspectrophotometer (http://www.4dx.se)

### Steps

1. Light-adapt the protein in the crystalline state by exposure to bright white light for several minutes
2. Mount crystals in cryo-loops and flash-freeze in liquid nitrogen
3. Record spectra at various temperatures (92-280 K) from a measurement area of 25 um diameter
4. Measure optical density of crystals (typically 0.7-1.5 at 570 nm and 0.5-1.2 at 532 nm for pump wavelength)

### Typical Conditions

- **temperature_range**: 92-280 K
- **measurement_area**: 25 um diameter
- **cryocooling_temperature**: 110 K (liquid nitrogen)
- **laser_wavelength**: 532 nm
- **laser_power**: 100 mW


## Advantages

- Provides direct measurement of photochemical state in the exact crystal to be studied
- Enables optimization of illumination conditions for intermediate trapping
- Non-destructive and compatible with cryogenic temperatures
- Can be used to verify the photostationary state before X-ray data collection

## Disadvantages

- Requires specialized portable microspectrophotometer equipment
- Limited to crystals with sufficient optical density for measurement
- Measures bulk crystal spectrum, not individual molecule behavior

## Proteins Using This Method

| Protein | Resolution | PDB | Notes |
|---|---|---|---|
| [bacteriorhodopsin](/xray-mp-wiki/proteins/bacteriorhodopsin/) | 1.9 A | 1Qhj (ground state) | Microspectrophotometry used to characterize bacteriorhodopsin crystals before photoexcitation and X-ray data collection at 110 K |
