---
title: Multiphoton Effects in Time-Resolved Serial Femtosecond Crystallography
created: 2026-06-16
updated: 2026-06-16
type: concept
category: concepts
layout: default
tags: [concept-crystallography-principle, concept-functional, membrane-protein]
sources: [doi/10.1038##s41467-019-10758-0, doi/10.1063##1.3553377]
verified: false
---

# Multiphoton Effects in Time-Resolved Serial Femtosecond Crystallography

## Overview
Time-resolved serial femtosecond crystallography (TR-SFX) at X-ray free-electron
lasers (XFELs) requires high-intensity optical pump laser pulses to photoexcite
protein crystals. Due to the significantly higher protein concentrations in
crystals versus solutions, pump laser intensities of 360-500 GW/cm^2 are
typically used, which results in far more than one photon per chromophore.
This leads to multiphoton excitation effects that can alter the observed
structural dynamics compared to the biologically relevant single-photon regime.
Sequential two-photon absorption was demonstrated in bacteriorhodopsin (bR),
where excitation of a tryptophan residue (Trp86) flanking the retinal
chromophore occurs at intensities above 30 GW/cm^2. These multiphoton effects
are non-productive for photoisomerization and reduce the quantum yield,
complicating the interpretation of TR-SFX data.


## Mechanism/Details
Multiphoton effects in TR-SFX arise from the need for high intermediate state
occupancy in crystallography compared to spectroscopy. In bR (Nature Communications
2019, Nass Kovacs et al.), a power titration from 12 to 180 GW/cm^2 identified
three excitation regimes:

1. **Single-photon regime (<30 GW/cm^2):** Linear photoproduct yield;
   no detectable tryptophan excitation. The excited state evolves through
   the canonical I-J-K photocycle intermediates.

2. **Sequential two-photon regime (30-180 GW/cm^2):** The first photon excites
   retinal S1. Within the excited state lifetime (~0.5 ps), a second photon is
   absorbed, populating higher excited states (S_n) of retinal and charge-transfer
   (CT) states involving Trp86 and Tyr185. The excited Trp86 state decays with
   ~20 ps timescale. This process is non-productive for isomerization.

3. **Multiphoton ionization regime (>180 GW/cm^2):** At the highest intensities,
   additional sub-ps decay of excited-state retinal C=C stretching indicates
   ultrafast multiphoton effects including possible ionization of chromophore
   or water molecules.

Quantum chemistry (XMCQDPT2-CASSCF) showed that the sequential two-photon
process involves excitation from the retinal S1 state to higher S3 state
(2.03 eV) or from the CT(Y185) state to excited Trp86 D2 state (2.29 eV),
both with large transition dipole moments. The excited Trp86 state is
strongly coupled to the retinal CT state, explaining the efficient energy
transfer observed spectroscopically.

The practical implication is that power-dependent studies are essential
to establish the linear range of pump intensity for any TR-SFX experiment.
Data collected in the multiphoton regime can still provide qualitative
structural information but may not reflect the true single-photon dynamics.


## Examples in Membrane Protein Work
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — Archetypal example where TR-SFX data were collected in the multiphoton regime (500 GW/cm^2). Power titration revealed Trp86 excitation via sequential two-photon absorption. Despite multiphoton effects, the characteristic sub-ps isomerization and quasi-static K-bR difference spectra were observed.
- [Channelrhodopsin](/xray-mp-wiki/proteins/rhodopsins/channelrhodopsin-c1c2/) — Other microbial rhodopsins studied by TR-SFX face similar multiphoton challenges; power-dependent studies are needed to validate observations.

## Related Concepts
- [Bacteriorhodopsin Photocycle](/xray-mp-wiki/concepts/bacteriorhodopsin-photocycle/) — The photocycle intermediates (I, J, K, L, M) were observed in TR-SFX experiments, though under multiphoton conditions
- [Time-Resolved Serial Femtosecond Crystallography]() — TR-SFX is the method that requires the high laser intensities leading to multiphoton effects
- [Retinal Isomerization](/xray-mp-wiki/concepts/retinal-isomerization/) — The isomerization yield is affected by multiphoton excitation, with reduced quantum yield at high intensities
- [Light-Adapted State](/xray-mp-wiki/concepts/light-adapted-state/) — Light adaptation and pre-illumination protocols are critical for ensuring consistent retinal isomer composition in TR-SFX experiments

## Cross-References
- [Bacteriorhodopsin (bR)](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — The TR-SFX study of bR provides the most detailed characterization of multiphoton effects in a membrane protein
- [Bacteriorhodopsin Photocycle](/xray-mp-wiki/concepts/bacteriorhodopsin-photocycle/) — Multiphoton effects alter the photocycle dynamics compared to single-photon excitation
- [Retinal Isomerization](/xray-mp-wiki/concepts/retinal-isomerization/) — Multiphoton excitation reduces the isomerization quantum yield
