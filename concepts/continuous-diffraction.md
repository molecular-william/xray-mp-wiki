---
title: Continuous Diffraction in Macromolecular Crystallography
created: 2026-06-08
updated: 2026-06-08
type: concept
category: concepts
layout: default
tags: [concept-crystallography-principle, xray-crystallography]
sources: [doi/10.1038##nature16949]
verified: false
---

# Continuous Diffraction in Macromolecular Crystallography

## Overview
Continuous diffraction refers to the incoherent sum of Fraunhofer diffraction patterns from individual macromolecular units in a crystal that has suffered translational disorder. In a perfect crystal, molecules are positioned at exact lattice points, producing sharp Bragg peaks through coherent constructive interference. When molecules undergo rigid-body random displacements from their ideal lattice positions (with root-mean-square displacement sigma), the coherent Bragg interference breaks down beyond a resolution of d = 2pi*sigma, giving rise to a continuous diffraction pattern. This continuous signal contains high-resolution structural information equal to the molecular transform of the individual asymmetric unit(s), which can be exploited for structure determination beyond the Bragg peak limit.


## Mechanism/Details
When a crystal molecule is displaced from its ideal lattice position by an amount s, the phase of the diffracted wave from this unit is changed by 2*pi*s/d at scattering angle 2theta corresponding to resolution d, leading to destructive interference when s = d/2. If all units are displaced randomly with r.m.s. displacement sigma, Bragg intensities diminish at resolution d = 2*pi*sigma according to the Debye-Waller factor exp(-4*pi^2*q^2*sigma^2), where q = 1/d. Beyond this resolution, the diffraction becomes proportional to the continuous diffraction pattern of the rigid structural unit |F_a(q)|^2. The continuous diffraction pattern appears as speckles in reciprocal space — randomly modulated intensity features associated with the crystal rather than solvent scattering. The size of the rigid structural unit can be estimated from the autocorrelation of the diffracting object (the 3D pair-distribution function), obtained by Fourier transform of the continuous diffraction intensities. In the diffractive imaging approach, the molecular envelope from a low-resolution Bragg solution serves as a real-space constraint for iterative phase retrieval on the continuous diffraction data, enabling reconstruction of the full-resolution structure.


## Examples in Membrane Protein Work
- Photosystem II (PSII): The most prominent demonstration of continuous
  diffraction-based structure determination. PSII microcrystals (~700 kDa
  dimer) from Thermosynechococcus elongatus showed a Bragg peak limit of
  4.5 A due to lattice disorder (r.m.s. displacement 0.8 A per dimension,
  Wilson B-factor 191.6 A^2). Using the molecular envelope from the 4.5 A
  Bragg solution as a constraint, iterative phasing of continuous diffraction
  data achieved a 3.5 A resolution structure. The 3D autocorrelation of the
  continuous diffraction confirmed the rigid structural unit as the PSII
  dimer. Data were collected at the LCLS XFEL using a gas dynamic virtual
  nozzle injector and CSPAD detector.
- Wilson statistics in continuous diffraction: The merged continuous
  intensities follow Wilson statistics — above a background level of around
  one photon per pixel per pulse, the logarithm of the intensity histogram
  follows a linear trend with negative slope, characteristic of the
  exponential distribution predicted by Wilson statistics. This confirms
  that the continuous signal arises from diffraction of a rigid object
  in crystallographic orientations.


## Related Concepts
- [Serial Femtosecond Crystallography](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/) — SFX technique used to collect continuous diffraction data from microcrystals - [Non-Crystallographic Symmetry](/xray-mp-wiki/concepts/non-crystallographic-symmetry/) — related crystallographic principle involving symmetry in macromolecular structures - [Epitaxial Twinning](/xray-mp-wiki/concepts/epitaxial-twinning/) — related crystallographic disorder phenomenon - [X-Ray Radiation Damage](/xray-mp-wiki/concepts/x-ray-radiation-damage/) — radiation damage limits data quality in crystallographic experiments - [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — phasing method used to generate initial molecular envelope for continuous diffraction phasing


## Cross-References

