---
title: L](/xray-mp-wiki/reagents/protein-tags/bril/
created: 2026-05-26
updated: 2026-05-26
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1002##anie.202115545]
verified: false
---

# L](/xray-mp-wiki/reagents/protein-tags/bril/

## Overview

The adenosine A2A receptor (A2AAR) is a class A  and important drug target for immuno-oncology and neurodegenerative diseases. The  construct combines C-terminal truncation, a single S91K(3,39) point mutation in the transmembrane domain, and intracellular loop 3 replacement with thermostabilized . This single-mutation design achieves superior thermostability over the previously used nine-mutation A2A-StaR2 construct while avoiding mutations in the orthosteric ligand-binding pocket. Crystal structures were solved with two [Preladenant(/xray-mp-wiki/reagents/ligands/preladenant/) derivatives ( and [PSB-2115(/xray-mp-wiki/reagents/ligands/preladenant/)), providing the first GPCR structures with [PEG(/xray-mp-wiki/reagents/additives/peg/)- and fluorophore-conjugated ligands.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1002##anie.202115545 | 7PX4 | 2.25 A | not specified | L(/xray-mp-wiki/reagents/protein-tags/bril/) (C-terminal truncation + S91K single mutation + [bRIL](/xray-mp-wiki/reagents/protein-tags/bril/) fusion in ICL3) |  (PEGylated [Preladenant(/xray-mp-wiki/reagents/ligands/preladenant/) derivative) |
| doi/10.1002##anie.202115545 | 7PYR | 2.6 A | not specified | L(/xray-mp-wiki/reagents/protein-tags/bril/) (C-terminal truncation + S91K single mutation + [bRIL](/xray-mp-wiki/reagents/protein-tags/bril/) fusion in ICL3) | PSB-2115 (Y fluorophore(/xray-mp-wiki/reagents/additives/bodipy/)-labeled [Preladenant](/xray-mp-wiki/reagents/ligands/preladenant/) derivative) |

## Expression and Purification

- **Expression system**: Sf9 insect cells (implied by binding assays)
- **Construct**: Human A2AAR with C-terminal truncation, S91K(3,39) mutation, [bRIL](/xray-mp-wiki/reagents/protein-tags/bril/) fusion in ICL3

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Detergent solubilization | -- | not specified | Membrane preparation from Sf9 cells |
| [Affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA affinity (His-tag) | Ni-NTA resin | not specified | [bRIL](/xray-mp-wiki/reagents/protein-tags/bril/) fusion provides His-tag for affinity capture |
| [Size-exclusion chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | SEC | not specified | not specified | Analytical SEC confirmed complex formation (Figure 5) |


## Crystallization

### doi/10.1002##anie.202115545

| Parameter | Value |
|---|---|
| Method | not specified (likely vapor diffusion) |
| Protein sample | L(/xray-mp-wiki/reagents/protein-tags/bril/) + [PSB-2113](/xray-mp-wiki/reagents/ligands/psb-2113/) |
| Reservoir | not specified |
| Temperature | not specified |
| Growth time | not specified |
| Notes | Crystals at 2.25 A resolution. [Preladenant](/xray-mp-wiki/reagents/ligands/preladenant/) derivative co-crystallized. |

| Parameter | Value |
|---|---|
| Method | not specified (likely vapor diffusion) |
| Protein sample | L(/xray-mp-wiki/reagents/protein-tags/bril/) + PSB-2115 |
| Reservoir | not specified |
| Temperature | not specified |
| Growth time | not specified |
| Notes | Crystals at 2.6 A resolution. -labeled [Preladenant(/xray-mp-wiki/reagents/ligands/preladenant/) derivative co-crystallized. |


## Biological / Functional Insights

### S91K mutation stabilizes inactive state

The S91K(3,39) mutation places a lysine in the allosteric sodium binding site, stabilizing the inactive conformation. This abolishes agonist binding ( pKi < 4.0) while preserving antagonist affinity ([PSB-2113(/xray-mp-wiki/reagents/ligands/psb-2113/) Ki = 19.6 nM). The mutation restrains key activation switches (W246(6,48), H250(6,52)) and helix III movements required for agonist accommodation. Thermal shift assays show superior stability compared to A2A-StaR2 (9 mutations) and A2A-DC-[bRIL](/xray-mp-wiki/reagents/protein-tags/bril/) (0 mutations).

### [Preladenant](/xray-mp-wiki/reagents/ligands/preladenant/) binding mode

 binds in the orthosteric pocket in the same orientation as [ZM241385(/xray-mp-wiki/reagents/ligands/zm241385/), with the tricyclic core displacing an "unhappy water" molecule from the binding pocket. Key interactions include hydrogen bonds to N253(6,55) and E169(ECL2) via furan oxygen and 5-amino group, pi-pi stacking to F168(ECL2), and hydrophobic contacts to L249(6,51) and I274(7,39). The phenylpiperazinylethyl moiety extends toward the extracellular surface, stabilized by pi-pi stacking to H264(ECL3). The  linker and [[BODIP(/xray-mp-wiki/reagents/additives/bodipy/)Y fluorophore](/xray-mp-wiki/reagents/additives/bodipy/) (PSB-2115) are disordered with no electron density, extending out of the binding pocket.


## Cross-References

- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Ni-NTA affinity purification using bRIL His-tag
- [Size-Exclusion Chromatography (SEC)](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Analytical SEC confirmed complex formation
- [BRIL Fusion Protein](/xray-mp-wiki/reagents/protein-tags/bril/) — ICL3 fusion partner for stabilization
- [Preladenant](/xray-mp-wiki/reagents/ligands/preladenant/) — Parent compound of co-crystallized ligands
- [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) — Linker in PSB-2113 conjugate
- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — Related neopentyl glycol detergent family
