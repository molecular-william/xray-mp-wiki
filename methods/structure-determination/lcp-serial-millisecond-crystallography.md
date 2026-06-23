---
title: LCP Serial Millisecond Crystallography (LCP-SMX)
created: 2026-06-08
updated: 2026-06-08
type: method
category: methods
layout: default
tags: [structure-xray, subdirectory-structure-determination]
sources: [doi/10.1107##S2052252514026487]
verified: false
---

# LCP Serial Millisecond Crystallography (LCP-SMX)

## Overview

LCP serial millisecond crystallography (LCP-SMX) is a serial crystallography technique that adapts the lipidic cubic phase (LCP) injector, originally developed for [Serial Femtosecond Crystallography](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/) (SFX) at X-ray free-electron lasers (XFELs), to more widely available synchrotron microfocus beamlines. The LCP injector extrudes a 20-50 um diameter stream of LCP containing microcrystals, enabling data collection at room temperature with 10-50 ms exposure times and a sample consumption of less than 1 mg of protein. Compared with conventional microcrystallography, LCP-SMX eliminates the need for difficult handling of individual crystals and allows for efficient screening of thousands of crystals. The method was demonstrated by solving the structure of [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) (bR) at 2.4 A resolution at the ESRF ID13 beamline, with 0.8 mg of protein in 200 ul of LCP yielding a complete dataset over 3 days (Nogly et al., 2015, PDB 4x31). A comparison cryo-structure was also collected from a single bR crystal at the SLS PXI beamline to 1.9 A resolution (PDB 4x32).

## Principle

LCP-SMX exploits the high viscosity of the lipidic cubic phase to extrude a slow-moving stream (0.05-0.15 um/ms) of microcrystals across a synchrotron microfocus X-ray beam. The slow stream velocity allows 10-100 ms exposure times, enabling efficient use of the sample. Each crystal is exposed for only a single diffraction pattern before the stream carries it away, distributing the radiation dose across thousands of crystals. Per-crystal doses remain below the Henderson- Garman safe dose limit of 1 MGy at room temperature (approximately 0.7 MGy in the bR demonstration), minimizing radiation damage. Room-temperature data collection avoids cryocooling artifacts.

## Protocol

### Reagents and Materials

- Microcrystals of target protein in LCP matrix (monoolein-based)
- [MAG](/xray-mp-wiki/reagents/lipids/mag/) 7.9 (optional, to prevent phase transition during injection)
- Paraffin oil (optional, to support smooth flow)

### Steps

1. Grow protein microcrystals in LCP (typically 5-50 um)
2. Remove excess crystallization buffer via syringe coupler
3. Add [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) to achieve homogeneous transparent LCP mesophase
4. Optionally supplement with 5% [MAG](/xray-mp-wiki/reagents/lipids/mag/) 7.9 and 5% paraffin oil
5. Homogenize crystal distribution using 3-way syringe coupler
6. Load sample into LCP injector with 20-50 um diameter nozzle
7. Set flow rate to 0.05-0.15 um/ms (1-300 nl/min)
8. Align LCP stream onto synchrotron microfocus X-ray beam
9. Collect diffraction patterns at 10-17 Hz with 10-50 ms exposure
10. Process with Cheetah (hit finding) and CrystFEL (indexing, integration, merging)


## Advantages

- Room-temperature data collection (no cryocooling artifacts)
- No difficult crystal handling or mounting
- Less than 1 mg of protein sufficient for complete dataset
- Widely available synchrotron microfocus beamlines
- Suitable for time-resolved studies on microsecond to millisecond timescale
- Eliminates pre-exposure, handling and centring of crystals

## Disadvantages

- Lower hit rate (~1%) compared to XFEL-SFX
- Lower data acquisition rate (10-17 Hz vs 120 Hz at XFEL)
- Background scattering from LCP stream at ~4.5 A resolution
- Requires microfocus beamline (not available at all synchrotrons)
- Large number of crystals needed (thousands to millions)

## Proteins Using This Method

| Protein | Resolution | PDB | Notes |
|---|---|---|---|
| [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) | 2.4 | 4X31 | First demonstration of LCP-SMX at synchrotron. bR from Halobacterium salinarum crystallized in monoolein-based LCP. Data collected at ESRF ID13 (2x3 um beam, 0.954 A wavelength) with Rayonix MX-170 CCD detector. 0.8 mg protein, 200 ul LCP, 3 days. 1,343,092 images collected, 12,982 hits, 5,691 indexed. Space group P63, a=b=62.8, c=109.7 A. Room temperature structure at 2.4 A resolution. Used CrystFEL for data processing and Phaser + Phenix for [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) (using sensory rhodopsin II, PDB 1h68, as search model). |
| [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) | 1.9 | 4X32 | Conventional cryo-crystallography comparison dataset. Single crystal of bR (50x50x10 um) data collected at SLS PXI-X06SA, 100 K, 0.1 degree oscillation, 150 ms exposure. PILATUS 6M detector. 2532 images. Space group P63, a=b=60.5, c=101.5 A. Resolution 1.9 A. Phased with Phaser using bR (PDB 2ntu) as search model. Refined with Refmac5. |
