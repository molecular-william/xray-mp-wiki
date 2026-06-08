---
title: ScaDMT Divalent Metal-Ion Transporter
created: 2026-06-05
updated: 2026-06-05
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.2904]
verified: false
---

# ScaDMT Divalent Metal-Ion Transporter

## Overview

ScaDMT is a divalent metal-ion transporter from Staphylococcus capitis belonging to the SLC11 (NRAMP) family. It catalyzes the proton-coupled transport of transition-metal ions including Mn2+, Fe2+, Cd2+, Co2+, Ni2+, and Pb2+ across cellular membranes. The protein adopts an inward-facing conformation with a LeuT-fold architecture and a substrate-binding site at the center of the transporter. ScaDMT is highly homologous to human DMT1 (SLC11A2), sharing 37% identical and 59% homologous residues. It contains 448 amino acids and is monomeric in detergent solution as determined by multiangle light scattering.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nsmb.2904 | not specified in paper | 6.5 A | P3_2 2 1 | Full-length ScaDMT from Staphylococcus capitis, wild-type, 448 amino acids, inward-facing conformation | none (full-length crystal form, lower resolution) |
| doi/10.1038##nsmb.2904 | not specified in paper | 3.1 A | P3_1 2 1 | ScaDMT^tru (truncated construct lacking 41 N-terminal residues including 17 residues of first predicted TM helix) co-crystallized with nanobody, inward-facing conformation | none (apo complex with nanobody) |
| doi/10.1038##nsmb.2904 | not specified in paper | 3.4 A | P3_1 2 1 | ScaDMT^tru-nanobody complex with Mn2+ bound, inward-facing conformation | Mn2+ (coordinated by Asp49, Asn52, Met226, and backbone of Ala223) |
| doi/10.1038##nsmb.2904 | not specified in paper | 3.6 A | P3_1 2 1 | Selenomethionine-labeled ScaDMT^tru-nanobody complex | SeMet (for structural determination by X-ray crystallography) |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: ScaDMT from S. capitis DSM 20326 (448 aa), C-terminal His10 tag separated by HRV 3C protease cleavage site, cloned into pBXC3H vector

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane preparation | Cell disruption with custom-made cell disruptor; ultracentrifugation to harvest membranes | -- | 50 mM potassium phosphate pH 7.5, 150 mM NaCl + DM (1-2% w/v) | Membrane vesicles extracted with 10% glycerol and 1-2% DM |
| Affinity purification | Immobilized metal affinity chromatography (IMAC) | Ni-NTA | DM-containing buffer + DM | His10-tagged protein purified; HRV 3C protease cleavage during dialysis |
| Tag cleavage and SEC | HRV 3C protease cleavage followed by size-exclusion chromatography | Superdex S200 | 10 mM HEPES pH 7.5, 150 mM NaCl, 0.25% DM + DM | Cleaved protein concentrated and pooled for experiments |


## Crystallization

### doi/10.1038##nsmb.2904

| Parameter | Value |
|---|---|
| Method | Nanobody co-crystallization, vapor diffusion |
| Notes | Full-length ScaDMT crystals grew to 6.5 A resolution in P3_2 2 1. ScaDMT^tru co-crystallized with nanobody in PEG 600/650 precipitants yielding 3.1 A structures in P3_1 2 1. Mn2+ complexes obtained by soaking. SeMet-labeled crystals used for structural determination. |


## Biological / Functional Insights

### Conserved transition-metal ion binding site

The ion-binding site is located at the center of the transporter and is composed of
conserved residues Asp49 and Asn52 from the unwound region of alpha-helix 1, and
Met226 from alpha-helix 6a. The coordinating atoms form an approximately planar
geometry with predominantly hard oxygen ligands and a soft thioether sulfur ligand
from Met226. This binding mode is conserved across the SLC11 family including human
DMT1, as demonstrated by equivalent mutations (D86A, N89A, M265A) in human DMT1
showing similar loss of ion binding and transport activity.

### Ion selectivity mechanism

ScaDMT selectively transports transition-metal ions (Mn2+, Fe2+, Cd2+, Co2+, Ni2+,
Pb2+) while excluding alkaline earth metal ions (Ca2+, Mg2+, Sr2+, Ba2+). The binding
site chemistry reflects this selectivity: the planar coordination geometry with
oxygen and sulfur ligands favors transition metals over alkaline earth metals. The
conserved DPGN motif in the unwound region of alpha-helix 1 serves as a family
signature. Cu2+ binds at the same site with shifted position, while Zn2+ binds in
the aqueous vestibule interacting with His233.

### Alternating-access transport mechanism

ScaDMT operates via an alternating-access mechanism. Binding of a proton and a
transition-metal ion to the extracellular-accessible site triggers conformational
changes in alpha-helices 1 and 6 around a hinge at the ion-binding region. This
closes the extracellular pathway and opens the intracellular pathway, releasing
both substrates into the cytoplasm. The empty transporter returns to its
outward-facing state.


## Cross-References

- [SLC11 (NRAMP) Family](/xray-mp-wiki/concepts/slc11-nramp-family/) — ScaDMT is a member of the SLC11/NRAMP family of divalent metal-ion transporters
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — ScaDMT transports ions via the alternating-access mechanism
- [Inward-Facing Conformation](/xray-mp-wiki/concepts/inward-facing-conformation/) — ScaDMT structures adopt inward-facing conformation
- [LeuT Return-State Mechanism](/xray-mp-wiki/concepts/leut-return-state-mechanism/) — ScaDMT shares the LeuT-fold architecture with amino acid permeases
- [Decylmaltoside](/xray-mp-wiki/reagents/detergents/decylmaltoside/) — DM used for solubilization and purification of ScaDMT
