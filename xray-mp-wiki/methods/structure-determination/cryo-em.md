---
title: Cryo-Electron Microscopy
created: 2026-06-08
updated: 2026-06-09
type: method
category: methods
layout: default
tags: [structure-cryoem, subdirectory-structure-determination]
sources: [doi/10.1016##j.cell.2019.06.031, doi/10.1016##j.cell.2020.01.008, doi/10.1038##nature17679, doi/10.1038##ncomms8947, doi/10.1016##jsb.2004.09.003, doi/10.15252##embj.2021108341, doi/10.1126##scisignal.ado8741]
verified: false
---

# Cryo-Electron Microscopy

## Overview

Cryo-electron microscopy (cryo-EM) is a high-resolution structure determination technique for membrane proteins and macromolecular complexes. Samples are flash-frozen in vitreous ice, preserving native conformation without crystallization. Single particle analysis enables 3D reconstruction from thousands of particle images, achieving near-atomic resolution for suitably sized complexes. Cryo-EM has been used to solve structures of intact heterotetrameric GluN1b-GluN2B NMDA receptors at multiple conformational states (active, non-active1, non-active2) in the presence of [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) and [L-Glutamate](/xray-mp-wiki/reagents/substrates/l-glutamate/) without allosteric inhibitors.

## Principle

Purified protein is applied to a grid, blotted to form a thin film, and rapidly frozen in liquid ethane to create vitreous (non-crystalline) ice. Individual particles are imaged by transmission electron microscopy at cryogenic temperatures. Thousands of 2D projection images are computationally aligned, classified, and combined to reconstruct a 3D density map. Resolution is assessed by the gold standard Fourier shell correlation (FSC) 0.143 criterion.

## Protocol

### Reagents and Materials

- [Digitonin](/xray-mp-wiki/reagents/detergents/digitonin/) or other suitable detergent for membrane protein solubilization
- Buffer components (Tris, NaCl, etc.)
- Grid preparation materials (quantifoil grids, glow discharge)
- C-flat 1.2/1.3 Cu 400 mesh grids (Protochips)

### Steps

1. {'step': 'Sample preparation', 'description': 'Purify membrane protein in appropriate detergent (e.g., [Digitonin](/xray-mp-wiki/reagents/detergents/digitonin/) for cryo-EM). Concentrate to suitable density (typically 0.5-3 mg/ml).'}
2. {'step': 'Grid application', 'description': 'Apply 3-4 ul of sample to glow-discharged grid. Blot and plunge-freeze in liquid ethane.'}
3. {'step': 'Data collection', 'description': 'Collect images on cryo-EM (e.g., Tecnai G2 F20) at 200-300 keV. Use automatic data collection software for high-throughput acquisition.'}
4. {'step': 'Motion correction', 'description': 'Correct for beam-induced motion using software such as MotionCor2.'}
5. {'step': 'CTF estimation', 'description': 'Estimate contrast transfer function parameters for each micrograph.'}
6. {'step': 'Particle picking', 'description': 'Automatically or manually pick particle images from micrographs.'}
7. {'step': '2D classification', 'description': 'Classify particle images into 2D averages to remove bad particles and identify representative views.'}
8. {'step': '3D reconstruction', 'description': 'Perform initial reference-free 3D classification, then refine with selected particles.'}
9. {'step': 'Model building', 'description': 'Dock existing crystal structures into density map or rebuild atomic model de novo using Coot and Phenix.'}
10. {'step': 'Grid preparation', 'description': 'Purified protein placed on C-flat grids subjected to glow discharge for 45 s at 15 mA.'}
11. {'step': 'Vitrification', 'description': 'Plunge-frozen using FEI Vitrobot Mark 2 with 3 s blot time at 85-95% relative humidity.'}
12. {'step': 'Image processing', 'description': 'Super-resolution movie frames corrected for magnification distortion, downsampled, motion-corrected and exposure filtered using Unblur. CTF determined using CTFFIND4. 3D classification into classes with highest resolution at FSC 0.143 cut-off.'}


## Advantages

- No crystallization required
- Can capture multiple conformational states
- Suitable for large complexes and membrane proteins
- Resolution approaching X-ray crystallography for well-behaved samples

## Disadvantages

- Requires specialized, expensive equipment
- Lower resolution than X-ray for small proteins (<100 kDa)
- Sample preparation can be challenging
- Requires significant computational resources
