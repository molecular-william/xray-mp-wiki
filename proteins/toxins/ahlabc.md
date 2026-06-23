---
title: AhlABC Tripartite Alpha-Pore Forming Toxin from Aeromonas hydrophila
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-019-10777-x]
verified: false
---

# AhlABC Tripartite Alpha-Pore Forming Toxin from Aeromonas hydrophila

## Overview

AhlABC is a tripartite alpha-pore forming toxin (alpha-PFT) from the Gram-negative pathogen Aeromonas hydrophila. The system consists of three components (AhlA, AhlB, and AhlC) that assemble to form a transmembrane pore. All three components are required for maximal cell lysis. AhlB is the pore-forming component containing a hydrophobic beta-tongue that undergoes a bi-fold hinge mechanism to transition from soluble to pore form. AhlC inserts into a single membrane leaflet to initiate pore assembly, and AhlA is proposed to provide the hydrophilic pore lining. The structures of AhlB in soluble and pore forms and AhlC in soluble tetrameric form have been determined by X-ray crystallography.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-019-10777-x | 6GRK | Not specified | C2 | Soluble AhlB |  |
| doi/10.1038##s41467-019-10777-x | 6GRJ | Not specified | C2 | AhlB pore (SeMet), Type 1/Type 2 conformations |  |
| doi/10.1038##s41467-019-10777-x | 6H2F | Not specified | C222(1) | AhlB pore Form 2 |  |
| doi/10.1038##s41467-019-10777-x | Not deposited separately | 2.35 | P6(2)2 | AhlC soluble tetramer Form 1 |  |
| doi/10.1038##s41467-019-10777-x | Not deposited separately | Not specified | P2(1) | AhlC soluble tetramer Form 2 |  |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Full-length AhlA, AhlB, and AhlC individually cloned and expressed
- **Notes**: Each component expressed and purified separately

### Purification Workflow

- **Expression system**: E. coli

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Bacterial culture |  | Not specified | Each Ahl component expressed individually in E. coli |
| Purification | Not specified in detail | Not specified | Not specified | Proteins purified to homogeneity |


## Crystallization

### doi/10.1038##s41467-019-10777-x

| Parameter | Value |
|---|---|
| Method | Sitting drop vapor diffusion |
| Protein sample | Purified AhlB |
| Temperature | Not specified |
| Notes | AhlB soluble form crystallized in space group C2. AhlB pore forms crystallized in space groups C2 and C222(1). Data collected on Diamond Light Source beamlines I02, I03, I04. Structures solved by Se-Met SAD. |

| Parameter | Value |
|---|---|
| Method | Sitting drop vapor diffusion |
| Protein sample | Purified AhlC at 40 mg/ml in 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8, 100 mM NaCl |
| Reservoir | 0.2 M [Magnesium Chloride (MgCl₂)](/xray-mp-wiki/reagents/additives/magnesium-chloride/), 0.1 M [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.0, 10% (w/v) [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) 10,000 |
| Temperature | 16 |
| Growth time | 1 week |
| Cryoprotection | Mother liquor with additional 20% (v/v) ethylene glycol |
| Notes | AhlC Form 1 in space group P6(2)2. AhlC Form 2 in space group P2(1). Se-Met SAD for phasing. |


## Biological / Functional Insights

### Bi-fold hinge mechanism for soluble-to-pore transition in AhlB

AhlB undergoes a dramatic conformational change from the soluble form to the pore form. The beta-tongue of soluble AhlB undergoes two 180-degree rotations (bi-fold hinge mechanism) to expose its hydrophobic head and form the membrane-spanning region. Two conformations (Type 1 and Type 2) are observed in the AhlB pore structure, with Type 2 being the fully extended form. Five Type 1/Type 2 dimers assemble into a decameric pore.

### AhlC tetramer hides hydrophobic heads

Unlike AhlB which uses conformational change, AhlC employs a tetrameric assembly to bury its hydrophobic alpha3-alpha4 heads. Within the tetramer, leucine zipper interactions between hydrophobic head residues and tail domains of symmetry-related subunits occlude the membrane-insertion region. Tetramer disassembly is required for membrane binding, supported by cross-linking experiments that abolish lytic activity.

### Tripartite pore assembly mechanism

The AhlABC pore assembles through a stepwise mechanism: (1) AhlC tetramer disassembles and monomers insert into a single membrane leaflet; (2) AhlB is recruited to the membrane and undergoes the bi-fold hinge conformational change; (3) AhlA binds to form the active hydrophilic-lined pore. Each component carries a separate role: AhlC provides initial membrane attachment, AhlB forms the hydrophobic pore, and AhlA provides the hydrophilic pore lining.


## Cross-References

- [Pore-Forming Toxins](/xray-mp-wiki/concepts/structural-mechanisms/pore-forming-toxins/) — AhlABC is an alpha-pore forming toxin in the ClyA family
- [ClyA Cytotoxin from Escherichia coli](/xray-mp-wiki/proteins/toxins/clyA/) — ClyA is the prototypical single-component alpha-PFT; AhlABC components have structural similarity to ClyA
- [X-ray Crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/) — Method used in the study
- [Pore-Forming Toxins](/xray-mp-wiki/concepts/structural-mechanisms/pore-forming-toxins/) — Key concept related to this protein
- [GR (Halobacterium sp. GR Bacteriorhodopsin)](/xray-mp-wiki/proteins/rhodopsins/gr/) — Related protein mentioned in the study
- [ClyA Cytotoxin from Escherichia coli](/xray-mp-wiki/proteins/toxins/clyA/) — Related protein mentioned in the study
- [n-Octyl beta-D-glucopyranoside (OG)](/xray-mp-wiki/reagents/detergents/og/) — Detergent used in purification
- [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) — Reagent used in the study
- [TES Buffer (N-Tris(hydroxymethyl)methyl-2-aminoethanesulfonic acid)](/xray-mp-wiki/reagents/buffers/tes/) — Reagent used in the study
- [Magnesium Chloride (MgCl₂)](/xray-mp-wiki/reagents/additives/magnesium-chloride/) — Reagent used in the study
