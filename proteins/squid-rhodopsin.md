---
title: Squid Rhodopsin (Photoreaction States)
created: 2026-05-07
updated: 2026-05-07
type: protein
category: proteins
layout: default
tags: [rhodopsin, membrane-protein, gpcr, visual-pigment, seven-tm, invertebrate]
sources: [doi/10.1016##j.jmb.2011.08.044]
---

# Squid Rhodopsin (Photoreaction States)

## Overview

Squid rhodopsin from Todarodes pacificus is an invertebrate visual pigment that interacts with Gq-type G-protein to activate the inositol 1,4,5-triphosphate signaling pathway. The 448-residue protein contains 11-cis retinal bound to Lys305 via a protonated Schiff base. Crystal structures of the primary photoreaction intermediates bathorhodopsin (Batho) and isorhodopsin (Iso, 9-cis) revealed that retinal isomerization stores energy as distortion of the polyene chain: the central moiety moves toward the cytoplasmic side while the ionone ring and Schiff base remain relatively fixed, creating a right-handed screwed configuration. Significant X-ray radiation damage was also characterized.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2011.08.044 | 3P1L | 2.8 A | P62 | C-terminally truncated squid rhodopsin (residues 1-372 or 1-357, cleaved at Glu373/Glu358 by V8 protease) | all-trans retinal (in Batho), 9-cis retinal (in Iso) |
| doi/10.1016##j.jmb.2011.08.044 | 3P1K | 2.7 A | P62 | C-terminally truncated squid rhodopsin (Iso state) | 9-cis retinal |
| doi/10.1016##j.jmb.2011.08.044 | 2BRS | 2.7 A | P62 | Native squid rhodopsin (dark state, 11-cis) | 11-cis retinal |

## Expression and Purification

- **Expression system**: Loligo (Todarodes) pacificus (native retina)
- **Construct**: Native squid rhodopsin from microvillar membranes

### Purification Workflow

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane extraction | Selective extraction from microvillar membranes | -- | Octylglucoside with zinc acetate | Rhodopsin extracted from squid microvillar membranes using octylglucoside in presence of zinc acetate |


## Crystallization

### doi/10.1016##j.jmb.2011.08.044

| Parameter | Value |
|---|---|
| Method | In meso crystallization (hexagonal P62 crystals) |
| Protein sample | Squid rhodopsin in octylglucoside |
| Reservoir | not specified |
| Mixing ratio | not specified |
| Temperature | Cryogenic (100 K) |
| Growth time | not specified |
| Cryoprotection | Cryocooled to 100 K; crystals handled in dim red light (>640 nm) |
| Notes | Hexagonal P62 crystals. Data collected at SPring-8 BL41XU using 10-micrometer microbeam. Photoreaction states trapped by illumination at specific wavelengths (blue 473 nm for Batho, yellow 560 nm for Iso, red 635 nm for Rhod). |


## Biological / Functional Insights

### Retinal distortion stores light energy in Batho

The Batho structure reveals that upon photoisomerization (11-cis to all-trans), the retinal central moiety moves largely toward the cytoplasmic side while the ionone ring and Schiff base undergo limited movement. The polyene chain takes on a right-handed screwed configuration with twisted C7=C8, C9=C10, and C11=C12 bonds. The C13 methyl pushes Ser187 into the E-II loop, and the C9 methyl pushes Phe188. This distortion stores ~35 kcal/mol of energy, conserved between vertebrate and invertebrate rhodopsins.

### Structural differences from bovine rhodopsin

Squid rhodopsin differs from bovine rhodopsin in the retinal-binding pocket: the beta-ionone ring is surrounded by aromatic residues (vs glutamate in bovine), and the retinal polyene chain associates with helix III backbone over three helical turns (vs polar residue Thr118 in bovine). The Schiff base H-bond partner is Asn87 or Tyr111 (vs Gly89 and Glu113 in bovine). These differences slow cis-trans isomerization in squid rhodopsin (vs bovine) while maintaining similar Batho energy.

### X-ray radiation damage in rhodopsin

Significant X-ray radiation damage was characterized: (1) retinal isomerization to orange species (precursor of retro form) at ~4 x 10^14 photons/mm^2, (2) breakage of disulfide bond between Cys108 and Cys186, (3) loss of electron density at Asp80 (decarboxylation/radiolysis). These changes produce photochemically inactive products that can be distinguished from functional photointermediates. Data collection must account for ~50% protein damage at doses of 3 x 10^15 photons/mm^2.


## Cross-References

- [n-Octyl beta-D-glucopyranoside (OG)](/xray-mp-wiki/reagents/detergents/og/) — Primary detergent for squid rhodopsin extraction and crystallization
- [Tris Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Used in oocyte buffer for electrophysiological studies (10 mM Hepes/Tris, pH 7.5)
- [Bovine Rhodopsin (Dark State)](/xray-mp-wiki/proteins/bovine-rhodopsin/) — Comparative vertebrate rhodopsin; key reference for retinal-binding pocket differences
- [Bovine Rhodopsin](/xray-mp-wiki/proteins/bovine-rhodopsin/) — Structural comparison; similar Batho energy but different isomerization dynamics
