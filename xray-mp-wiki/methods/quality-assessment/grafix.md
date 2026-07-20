---
title: "GraFix (Glycerol-Glutaraldehyde Gradient Fixation)"
created: 2026-06-16
updated: 2026-06-16
type: method
category: methods
layout: default
tags: [quality-assessment, subdirectory-quality-assessment]
sources: [doi/10.1038##nature13205]
verified: regex
---

# GraFix (Glycerol-Glutaraldehyde Gradient Fixation)

## Overview

GraFix (Glycerol-Glutaraldehyde Gradient Fixation) is a sample preparation method for single-particle electron cryomicroscopy that combines a glycerol gradient for centrifugation with a low concentration of glutaraldehyde for mild crosslinking. It stabilizes macromolecular complexes by reducing conformational heterogeneity and preventing dissociation during grid preparation.

## Principle

GraFix uses a linear glycerol gradient (10-30% v/v) containing a low concentration of glutaraldehyde (0.15% v/v). As the protein complex sediments through the gradient by ultracentrifugation, it is gently crosslinked by the glutaraldehyde from the surrounding medium. This stabilizes fragile complexes and locks them into a single conformational state without introducing significant artifacts. The glycerol gradient also serves a preparative function, separating aggregated or damaged particles from well-behaved complexes.

## Protocol

### Reagents and Materials

- [Glutaraldehyde](/xray-mp-wiki/reagents/additives/glutaraldehyde/) (0.15% v/v)
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) (10-30% v/v)
- [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) buffer (50 mM, pH 7.5)
- [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/) (400 mM)
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) (0.03% w/v)

### Steps

1. {'step': 'Prepare gradient', 'method': 'Mix low-glycerol and high-glycerol buffers in a gradient maker', 'notes': 'Buffer 1: 50 mM HEPES pH 7.5, 400 mM NaCl, 0.03% DDM, 10% glycerol. Buffer 2: same + 30% glycerol, 0.15% glutaraldehyde'}
2. {'step': 'Load sample', 'method': 'Apply protein complex to top of gradient', 'notes': 'Typically 100 pmol of freshly prepared complex'}
3. {'step': 'Ultracentrifugation', 'method': 'Centrifuge at 111,845g for 18 h at 4 C', 'notes': 'SW60 rotor (Beckmann)'}
4. {'step': 'Fractionate gradient', 'method': 'Pump gradient out from bottom to top', 'notes': 'Collect 200 ul fractions at 4 C'}
5. {'step': 'Quench crosslinking', 'method': 'Add glycine (1 M, pH 7.5)', 'notes': 'Final concentration 80 mM glycine. Concentrate using Vivaspin (MWCO = 100 kDa).'}
6. {'step': 'Buffer exchange', 'method': 'Dilute and reconcentrate', 'notes': 'Reduce glycerol concentration. Flash freeze in liquid N2 and store at -80 C.'}

### Typical Conditions

- **glycerol_gradient**: 10-30% v/v
- **glutaraldehyde_concentration**: 0.15% v/v
- **centrifugation**: 111,845g, 4 C, 18 h
- **quench**: 80 mM glycine pH 7.5


## Advantages

- Stabilizes transient or fragile multiprotein complexes for cryo-EM
- Reduces conformational heterogeneity
- Prevents complex dissociation during grid preparation
- Separates aggregated particles from well-behaved complexes

## Disadvantages

- Chemical crosslinking may introduce minor conformational artifacts
- Requires gradient-making equipment
- Sample loss during fractionation and concentration steps

## Proteins Using This Method

| Protein | Resolution | PDB | Notes |
|---|---|---|---|
| [AcrAB-TolC multidrug efflux pump (E. coli)](/xray-mp-wiki/proteins/abc-transporters/acrb/) | 15-20 A (pseudo-atomic model) | Not deposited | AcrABZ-TolC complex prepared using GraFix for cryo-EM structural analysis |
