---
title: LH2 Light-Harvesting Complex (Rps. acidophila)
created: 2026-04-28
updated: 2026-04-28
type: protein
tags: [light-harvesting, photosynthesis, membrane-protein, xray-crystallography, pigment-protein]
sources: [doi/10.1016##S0022-2836(03)00024-X]
---
layout: default

# LH2 — Light-Harvesting Complex 2 from *Rhodopseudomonas acidophila*

## Overview

LH2 is a peripheral light-harvesting antenna complex from purple non-sulfur bacteria that traps solar energy. It consists of a nonameric ring of α- and β-peptides with bacteriochlorophyll (BChl) a and carotenoid pigments. This paper reports the 2.0 Å structure at 100 K with TLS refinement revealing functionally relevant pigment motions.

## Structure

- **Organism**: *Rhodopseudomonas acidophila* strain 10050
- **Resolution**: 2.0 Å at 100 K
- **PDB ID**: 1LHQ (implied from context; original 2.5 Å was 1KZU)
- **Symmetry**: C₉ nonameric ring
- **Data collection**: SRS wiggler beamline 9.6, Daresbury Laboratory; ADSC Quantum 4 CCD
- **Refinement**: REFMAC5 with TLS (translation, libration, screw) refinement

### Pigment Composition (per repeating unit)

- **2 BChl a molecules at 850 nm** (B850): 18 total in ring, arranged as 9 approximate dimers
- **1 BChl a molecule at 800 nm** (B800): 9 total
- **2 carotenoid molecules**: Rhodopin glucoside (RG1 and RG2)
- **Ligands**: B850 ligated to α-His31 and β-His30; B800 ligated to α-Met1 (carboxy-modified)

### Secondary Structure

- **α-peptide**: Transmembrane helix with short surface helices
- **β-peptide**: Transmembrane helix with greater thermal motion/freedom
- **18 BChl a molecules**: Ring near periplasmic surface between α and β peptides
- **9 B800 molecules**: Well-separated, near cytoplasmic surface between β peptides

### TLS Refinement Findings

- **48 TLS tensors** optimal (transmembrane helices divided into 4 segments)
- **B850 thermal motion**:
  - Mean Ueq = 0.4 Å²
  - Anisotropy E = 1.5
  - Largest libration: rotation about axis normal to membrane (~12 deg²)
  - Translational motion: along line between centers of different dimers
- **B800 thermal motion**:
  - Mean Ueq = 0.6 Å² (larger than B850)
  - Anisotropy E = 1.7
  - Pmax aligned along Qy transition dipole (150° relative to tangent)
  - Larger libration in membrane plane (12 deg²)
- **Phytyl chains**: Largest anisotropy at termini (up to 6 deg², Pmax = 1.79 Å²)
- **Inter-pigment displacements**: ~0.7 Å RMS, modulates pigment-pigment interaction energies by ~370 cm⁻¹ within dimers, ~280 cm⁻¹ between dimers

### Second Carotenoid

- **RG2**: Second rhodopin glucoside molecule observed
- **RG1**: Well-defined, TLS refined
- **RG2**: Partially disordered (glucoside head groups less defined than isoprene parts)

## Expression and Purification

**Note**: Methods refer to previous publications (McDermott et al., 1995; Papiz & Prince, 1996).

- **Detergent**: β-octyl glucoside (BOG) — used in complex preparation and crystallization
- **Crystallization**: Vapour diffusion against 2.3 M ammonium sulfate, pH 9.3
- **Cryoprotection**: Equilibration in K₂HPO₄, 350 mM NaCl, 0.5% BOG; dialysis against 3 M K₂HPO₄/Na (pH 10.5), 700 mM NaCl, 1% BOG:saturated sucrose
- **Data collection**: 100 K cryo-cooling

## Energy Transfer Implications

- **B850 coupling**: ~370 cm⁻¹ within dimers, ~280 cm⁻¹ between dimers
- **Disorder**: Off-diagonal energy disorder σ = 0.35V or σ = 0.19V (anti-correlated with site energy)
- **Dephasing times**: B850 ~130 ps at 4.2 K; B800 ~300 ps at 4.2 K
- **Energy transfer**: B800→B850 occurs in <1 ps; B850→LH1/RC in ~35 ps
- **TLS motions**: Time periods 3-7 ps (3-10 cm⁻¹ modes); may drive energy transfer

## Comparison with LH2 from Rs. molischianum

- **Symmetry**: C₈ (vs C₉ in Rps. acidophila)
- **B800 ligand**: α-Asp6 (vs α-Met1 in Rps. acidophila)
- **B800 orientation**: Tilted and rotated in membrane plane
- **Carotenoid**: Lycopene (vs rhodopin glucoside)

## Biological Significance

- **Photosynthesis**: First step in trapping solar energy in purple bacteria
- **Pigment organization**: Highly optimized for efficient energy transfer
- **Thermal motions**: Non-random, designed to optimize modulation of pigment energy interactions
- **Evolution**: Physical and dynamic properties selected for optimal energy transfer

## Related Complexes

- [rps-viridis-reaction-center](/proteins/rps-viridis-reaction-center/) — Reaction center from Rhodopseudomonas viridis
- [psi-lhci-supercomplex](/proteins/psi-lhci-supercomplex/) — PSI-LHCI Supercomplex from plants

## References

- Papiz et al. (2003) JMB 326:1523-1538 — LH2 structure at 2.0 Å with TLS refinement
- McDermott et al. (1995) Nature 374:517-521 — Original LH2 structure at 2.5 Å
- Koepke et al. (1996) Structure 4:581-597 — LH2 from Rs. molischianum