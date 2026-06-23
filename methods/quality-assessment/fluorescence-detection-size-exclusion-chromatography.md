---
title: Fluorescence-Detection Size-Exclusion Chromatography (FSEC)
created: 2026-06-16
updated: 2026-06-16
type: method
category: methods
layout: default
tags: [purification-size-exclusion, quality-assessment, subdirectory-quality-assessment]
sources: [doi/10.1016##j.celrep.2015.12.087]
verified: false
---

# Fluorescence-Detection Size-Exclusion Chromatography (FSEC)

## Overview

Fluorescence-detection size-exclusion chromatography (FSEC) is a screening technique that uses GFP-fused membrane proteins to rapidly assess expression level, monodispersity, and oligomeric state without purification. FSEC profiles on a Superdex 200 column were used to evaluate AmP2X and its crystallization construct AmP2Xcryst compared to zfP2X4.

## Principle

A GFP tag is fused to the target membrane protein. Crude cell lysate or detergent-solubilized membrane fractions are loaded onto a size-exclusion column, and fluorescence of the eluting GFP (488 nm excitation, 510 nm emission) is monitored. Sharp, symmetrical peaks indicate well-behaved, monodisperse samples suitable for crystallization.

## Protocol

### Reagents and Materials

- EGFP-fused membrane protein expressing cells
- Solubilization buffer with detergent (e.g., DDM)
- Superdex 200 10/300 GL column (GE Healthcare)

### Steps

1. {'step': '1. Express GFP-fused membrane protein in mammalian cells (e.g., HEK293T)', 'method': 'Transient transfection or stable cell line'}
2. {'step': '2. Solubilize membrane fraction with detergent', 'method': 'Detergent solubilization'}
3. {'step': '3. Centrifuge to remove insoluble material', 'method': 'Ultracentrifugation'}
4. {'step': '4. Inject supernatant onto Superdex 200 column', 'method': 'ÄKTA FPLC system with fluorescence detector'}
5. {'step': '5. Monitor fluorescence signal (ex. 488 nm, em. 510 nm)', 'method': 'In-line fluorescence detection'}

### Typical Conditions

- **column**: Superdex 200 10/300 GL
- **flow_rate**: 0.5 mL/min
- **detection**: Fluorescence (488 nm excitation, 510 nm emission)


## Proteins Using This Method

| Protein | Resolution | PDB | Notes |
|---|---|---|---|
| [AmP2X](/xray-mp-wiki/proteins/AmP2X/) | 2.80 | 5F1C |  |
