---
title: Diffractive Imaging of Imperfect Crystals
created: 2026-06-03
updated: 2026-06-03
type: method
category: methods
layout: default
tags: [structure-xray, subdirectory-structure-determination]
sources: [doi/10.1038##nature16949]
verified: false
---

# Diffractive Imaging of Imperfect Crystals

## Overview

Diffractive imaging of imperfect crystals is a macromolecular structure determination technique that exploits continuous diffraction patterns from lattice-disordered crystals to achieve resolution beyond the measurable Bragg peak limit. In imperfect crystals with translational disorder (rigid-body displacements of molecules from ideal lattice positions), the coherent Bragg interference breaks down beyond a resolution determined by the disorder length, while the incoherent sum of single- molecule diffraction (continuous diffraction) carries high-resolution structural information. By using the molecular envelope from a low-resolution Bragg solution as a real-space constraint, iterative phase retrieval algorithms can reconstruct the full-resolution structure from the continuous diffraction pattern.

## Protocol

### Reagents and Materials

- {'name': 'XFEL X-ray pulses (e.g. 40 fs at 9.48 keV)', 'role': 'X-ray source'}
- {'name': 'Gas dynamic virtual nozzle (GDVN) injector', 'role': 'Sample delivery'}
- {'name': 'Pixel array detector (e.g. CSPAD)', 'role': 'Diffraction detection'}
- {'name': 'CrystFEL software', 'role': 'Data processing and indexing'}
- {'name': 'Cheetah software', 'role': 'Hit finding and Bragg peak identification'}

### Steps

1. {'step': 'Data collection', 'description': 'Collect still snapshot diffraction patterns from microcrystals in random orientations using an X-ray free-electron laser (XFEL). Crystals are delivered via a liquid jet injector (e.g. GDVN) at room temperature. One diffraction frame is recorded per X-ray pulse.\n'}
2. {'step': 'Pattern indexing', 'description': 'Identify Bragg peaks in each diffraction pattern using automated hit-finding software (e.g. Cheetah). Index the lattice to determine crystal orientation and lattice parameters for each pattern using software such as CrystFEL.\n'}
3. {'step': '3D diffraction volume assembly', 'description': 'Use indexed crystal orientations to assemble individual snapshot diffraction patterns into a 3D reciprocal-space grid representing the full-pattern intensity distribution of the average disordered crystal.\n'}
4. {'step': 'Background subtraction', 'description': 'Subtract the featureless solvent background from each pattern. This is computed by summing counts along circles of constant q (scattering vector magnitude) after correcting for X-ray beam polarization, excluding very high and very low values to avoid Bragg peak influence.\n'}
5. {'step': 'Low-resolution phasing from Bragg data', 'description': 'Perform [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) phasing using Bragg peak intensities to obtain a low-resolution electron density map. Generate a binary molecular envelope mask from the smoothed electron density, dilated slightly to avoid over-constraining the phasing.\n'}
6. {'step': 'Scaling and interpolation', 'description': 'Scale the molecular transform calculated from phased Bragg intensities in magnitude and interpolate to match the merged continuous diffraction data. This is done empirically at an intermediate q range where both data types overlap.\n'}
7. {'step': 'Iterative phase retrieval', 'description': 'Phase the continuous diffraction using a difference-map algorithm. The algorithm iteratively enforces two constraints: first, Fourier magnitudes match the measured continuous diffraction intensities; second, electron density is zero outside the molecular envelope support. Low-resolution phases from [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) are preserved. Point-group symmetries are applied to Fourier magnitudes.\n'}
8. {'step': 'Structure averaging and refinement', 'description': 'Average solutions obtained over multiple random phase starts to produce a self-consistent electron density. Evaluate resolution using Fourier shell correlation (FSC) and phase retrieval transfer function (PRTF). Perform pseudo-crystallographic refinement of the resulting electron density map.\n'}

### Typical Conditions

- **temperature**: Room temperature
- **x_ray_pulse_duration**: 40 fs
- **photon_energy**: 9.48 keV
- **detector**: Cornell-SLAC Pixel Array Detector (CSPAD)
- **frame_rate**: 120 Hz
- **max_dose**: 275 MGy per crystal


## Advantages

- Achieves resolution beyond the Bragg peak limit in imperfect crystals
- Exploits commonly encountered disordered crystals rather than requiring perfect crystals
- Higher tolerable X-ray dose with XFEL (diffraction before destruction)
- Can measure data from hundreds of thousands of crystals and select the best
- Enables ab initio phasing using only the molecular envelope as a constraint
- Applicable to a range of macromolecular systems
- Demonstrated for membrane protein complexes ([Photosystem II](/xray-mp-wiki/proteins/photosynthesis/photosystem-ii/))

## Disadvantages

- Requires an XFEL facility (limited availability)
- Continuous diffraction data is noisy, requiring many patterns for convergence
- Limited by the accuracy of the molecular envelope support constraint
- Scaling between Bragg and continuous diffraction must be determined empirically
- Convergence depends on initial well-estimated support and low-resolution phases
- Currently demonstrated for a limited number of systems
