---
title: A2A-PSB1-bRIL Adenosine A2A Receptor
created: 2026-05-05
updated: 2026-05-05
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1002##anie.202115545]
---

# A2A-PSB1-bRIL Adenosine A2A Receptor

## Overview

The adenosine A2A receptor (A2AAR) is a class A GPCR and important drug target for immuno-oncology and neurodegenerative diseases. The A2A-PSB1-bRIL construct combines C-terminal truncation, a single S91K(3,39) point mutation in the transmembrane domain, and intracellular loop 3 replacement with thermostabilized bRIL. This single-mutation design achieves superior thermostability over the previously used nine-mutation A2A-StaR2 construct while avoiding mutations in the orthosteric ligand-binding pocket. Crystal structures were solved with two Preladenant derivatives (PSB-2113 and PSB-2115), providing the first GPCR structures with PEG- and fluorophore-conjugated ligands.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1002##anie.202115545 | 7PX4 | 2.25 A | not specified | A2A-PSB1-bRIL (C-terminal truncation + S91K single mutation + bRIL fusion in ICL3) | PSB-2113 (PEGylated Preladenant derivative) |
| doi/10.1002##anie.202115545 | 7PYR | 2.6 A | not specified | A2A-PSB1-bRIL (C-terminal truncation + S91K single mutation + bRIL fusion in ICL3) | PSB-2115 (BODIPY fluorophore-labeled Preladenant derivative) |

## Expression and Purification

- **Expression system**: Sf9 insect cells (implied by binding assays)
- **Construct**: Human A2AAR with C-terminal truncation, S91K(3,39) mutation, bRIL fusion in ICL3

### Purification Workflow

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Detergent solubilization | -- | not specified | Membrane preparation from Sf9 cells |
| Affinity chromatography | Ni-NTA affinity (His-tag) | Ni-NTA resin | not specified | bRIL fusion provides His-tag for affinity capture |
| Size-exclusion chromatography | SEC | not specified | not specified | Analytical SEC confirmed complex formation (Figure 5) |


## Crystallization

### doi/10.1002##anie.202115545

| Parameter | Value |
|---|---|
| Method | not specified (likely vapor diffusion) |
| Protein sample | A2A-PSB1-bRIL + PSB-2113 |
| Reservoir | not specified |
| Temperature | not specified |
| Growth time | not specified |
| Notes | Crystals at 2.25 A resolution. Preladenant derivative co-crystallized. |

| Parameter | Value |
|---|---|
| Method | not specified (likely vapor diffusion) |
| Protein sample | A2A-PSB1-bRIL + PSB-2115 |
| Reservoir | not specified |
| Temperature | not specified |
| Growth time | not specified |
| Notes | Crystals at 2.6 A resolution. BODIPY-labeled Preladenant derivative co-crystallized. |


## Biological / Functional Insights

### S91K mutation stabilizes inactive state

The S91K(3,39) mutation places a lysine in the allosteric sodium binding site, stabilizing the inactive conformation. This abolishes agonist binding (NECA pKi < 4.0) while preserving antagonist affinity (PSB-2113 Ki = 19.6 nM). The mutation restrains key activation switches (W246(6,48), H250(6,52)) and helix III movements required for agonist accommodation. Thermal shift assays show superior stability compared to A2A-StaR2 (9 mutations) and A2A-DC-bRIL (0 mutations).

### Preladenant binding mode

PSB-2113 binds in the orthosteric pocket in the same orientation as ZM241385, with the tricyclic core displacing an "unhappy water" molecule from the binding pocket. Key interactions include hydrogen bonds to N253(6,55) and E169(ECL2) via furan oxygen and 5-amino group, pi-pi stacking to F168(ECL2), and hydrophobic contacts to L249(6,51) and I274(7,39). The phenylpiperazinylethyl moiety extends toward the extracellular surface, stabilized by pi-pi stacking to H264(ECL3). The PEG linker and BODIPY fluorophore (PSB-2115) are disordered with no electron density, extending out of the binding pocket.


## Cross-References

- [BRIL Fusion Protein](/xray-mp-wiki/reagents/protein-tags/bril/) — ICL3 fusion partner for stabilization
- [Preladenant](/xray-mp-wiki/reagents/ligands/preladenant/) — Parent compound of co-crystallized ligands
- [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) — Linker in PSB-2113 conjugate
- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — Related neopentyl glycol detergent family
