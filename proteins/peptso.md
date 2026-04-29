---
title: PepTSo (Proton-Coupled Oligopeptide Transporter)
created: 2026-04-28
updated: 2026-04-28
type: protein
tags: [transporter, mfs-transporter, membrane-protein, xray-crystallography, alternating-access]
sources: [doi/10.1016##J.STR.2014.12.012]
category: proteins
---
layout: default

# PepTSo — Proton-Coupled Oligopeptide Transporter from Shewanella oneidensis

## Overview

PepTSo is a proton-coupled oligopeptide transporter from the POT (Peptide Transporter) family, belonging to the Major Facilitator Superfamily (MFS). It mediates H+-coupled uptake of di/tripeptides across the bacterial membrane. This paper reports an improved inward-facing structure and uses molecular dynamics, DEER spectroscopy, and repeat-swapping to elucidate the gating mechanism.

## Structure

- **Protein**: PepTSo from *Shewanella oneidensis*
- **Resolution**: 3.0 Å
- **PDB ID**: 4UVM
- **Space group**: P4₁2₁2
- **Cell dimensions**: a=86.83, b=86.83, c=219.82 Å
- **Data collection**: Diamond Light Source I24 beamline
- **Refinement**: Rwork/Rfree not explicitly stated (see Table 1)

### MFS Architecture

- **12 transmembrane helices** organized as two inverted-topology 6-helix repeats
- **N-terminal repeat**: H1-H6
- **C-terminal repeat**: H7-H12
- **Conformation**: Inward-facing (cytoplasmic gate open)
- **SAH binding**: S-adenosyl-L-homocysteine molecule observed in structure

### Gating Mechanism — Double Scissor-Switch Model

- **Periplasmic gate**: H1, H2, H7, H8
- **Cytoplasmic gate**: H4, H5, H10, H11
- **Scaffold helices**: H3, H6, H9, H12 (less mobile, provide platform)
- **Alternating access**: Concerted scissoring movement of N- and C-terminal halves

### Key Structural Features

- **Salt bridges stabilizing outward-facing**:
  - D136-K439 (H4-H11): conserved in mammalian POT family
  - K84-D79 (H3-H2): potential in PepTSt
  - R52-D328 (periplasmic side): reduces transport when mutated
- **Proline kinks in H8**: P345 and P353 essential for transport
  - P345A: reduces transport
  - P353A: abolishes active transport
  - P345A/P353A double mutant: no detectable activity
- **DEER spectroscopy**: Confirms conformational dynamics in detergent

## Expression and Purification

**Note**: Methods refer to previous publications (Newstead et al., 2011; Lyons et al., 2014).

- **Expression**: *E. coli* (standard for POT family transporters)
- **Purification**: To homogeneity (Newstead et al., 2011)
- **Detergent**: Not specified in this paper; see reference papers
- **Crystallization**: As described in Lyons et al., 2014

## Functional Assays

- **Reconstitution**: Into *E. coli* total lipids with egg PC liposomes
- **Transport assay**: Proton-driven system (Solcan et al., 2012)
- **DEER spectroscopy**: MTSL spin labels at specific positions to measure distances between helices

## Molecular Dynamics Simulations

- **Starting structure**: Apo PepTSo (PDB 2XUT)
- **Simulations**: As described by Newstead et al., 2011
- **Findings**: Both proteins sample inward-facing, occluded, and outward-facing conformations
- **C-terminal half**: More dynamic than N-terminal half

## Comparison with PepTSt

- **PepTSt**: From *Sulfolobus tokodaii* (archaeal homolog)
- **Structural differences**: C-terminal half more dynamic in PepTSt
- **Salt bridges**: Only K84-D79 potential in PepTSt (D136-K439 not conserved)
- **Proline mutations**: Similar effects in both transporters

## Biological Significance

- **POT family**: Includes mammalian PEPT1/PEPT2 (intestinal/renal peptide uptake)
- **Drug delivery**: Proton-coupled transporters exploited for peptide-mimetic prodrugs
- **Antibiotic uptake**: Some antibiotics use POT family transporters for bacterial uptake

## Related Transporters

- [sotb](/xray-mp-wiki/proteins/sotb/) — E. coli antiporter (MFS family)
- [mmpL3](/xray-mp-wiki/proteins/mmpL3/) — Mycobacterial drug transporter
- [adenine-nucleotide-transporter](/xray-mp-wiki/proteins/adenine-nucleotide-transporter/) — ANT (nucleotide transporter)

## References

- Fowler et al. (2015) Structure 23:290-301 — Gating topology of PepTSo
- Newstead et al. (2011) — PepTSo structure and dynamics
- Lyons et al. (2014) EMBO Rep. 15:886-893 — Polyspecificity in POT family
- Solcan et al. (2012) — PepTSt structure