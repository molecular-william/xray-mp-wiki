---
title: "Blue-Shifted Rhodopsin Design Principle"
created: 2026-06-05
updated: 2026-06-05
type: concept
category: concepts
layout: default
tags: [concept-functional, concept-construct-design, subdirectory-rhodopsin-mechanisms]
sources: [doi/10.1038##ncomms8177]
verified: regex
---

# Blue-Shifted Rhodopsin Design Principle

## Overview
The blue-shifted rhodopsin design principle uses atomistic rational design to create color variants of microbial opsins with large spectral shifts. By introducing targeted point mutations in the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) binding pocket, the beta-ionone ring of the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore can be rotated to a twisted 6-s-cis conformation, shrinking its pi-conjugated system and producing blue shifts of up to 100 nm in absorption maximum. This approach, verified by QM/MM simulations and X-ray crystallography, represents a powerful and generalizable strategy for developing optogenetics tools with custom spectral properties.

## Mechanism/Details
The atomistic design principle for creating blue-shifted microbial rhodopsin optogenetics tools relies on rational point mutations that induce controlled conformational changes of the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore. The key insight is that mutations at specific positions in the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) binding pocket can shrink the pi-conjugated system of the chromophore by rotating the beta-ionone ring out of plane to a 6-s-cis conformation. In [Channelrhodopsin C1C2](/xray-mp-wiki/proteins/rhodopsins/channelrhodopsin-c1c2/), the double mutation T198G/G202A creates space by replacing the bulky Thr198 side chain with a smaller Gly, and the smaller Ala202 residue. This allows the beta-ionone ring to rotate with C6-C7 bond torsion of -27.7 degrees, producing a 21 nm blue shift. In [AR3](/xray-mp-wiki/proteins/rhodopsins/archaerhodopsin-3/) ([AR3](/xray-mp-wiki/proteins/rhodopsins/archaerhodopsin-3/)), the triple mutation M128A/G132V/A225T produces an even larger 100 nm blue shift (552 to 454 nm) through a similar mechanism with C6-C7 torsion of -45.1 degrees. The design requires simultaneous mutations at paired positions (128/132 in [AR3](/xray-mp-wiki/proteins/rhodopsins/archaerhodopsin-3/), 198/202 in C1C2) for controlled ring rotation rather than uncontrolled structural changes. The principle is applicable to other microbial opsins and explains the naturally occurring blue-shifted spectra of PsChR and TcChR from marine microalgae.

## Examples in Membrane Protein Work


## Related Concepts


## Cross-References
- [C1C2GA (C1C2 T198G/G202A)](/xray-mp-wiki/proteins/rhodopsins/c1c2ga/) — Prototype blue-shifted mutant designed using this principle; 21 nm blue shift (476 to 455 nm)
- [Archaerhodopsin-2](/xray-mp-wiki/proteins/rhodopsins/archaerhodopsin-2/) — AR3 M128A/G132V/A225T mutant designed using same principle; 100 nm blue shift (552 to 454 nm)
- [Channelrhodopsin C1C2](/xray-mp-wiki/proteins/rhodopsins/channelrhodopsin-c1c2/) — Wild-type C1C2 serves as the scaffold for rational design of C1C2GA blue-shifted mutant
- [Retinal Chromophore Conformation](/xray-mp-wiki/concepts/structural-mechanisms/retinal-chromophore-conformation/) — Beta-ionone ring rotation to 6-s-cis conformation is the key structural change enabling blue shifts
- [Rhodopsin Photocycle](/xray-mp-wiki/concepts/rhodopsin-mechanisms/rhodopsin-photocycle/) — Blue-shifted variants maintain photocycle functionality while shifting absorption maximum
- [AR3](/xray-mp-wiki/proteins/rhodopsins/archaerhodopsin-3/) — Related protein structure
- [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) — Related ligand or cofactor
