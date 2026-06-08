---
title: Squid Rhodopsin (Primary Photochemical Reaction States)
created: 2026-05-26
updated: 2026-05-26
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2011.08.044, doi/10.1038##nature06925]
verified: false
---

# Squid Rhodopsin (Primary Photochemical Reaction States)

## Overview

Squid rhodopsin from Todarodes pacificus is an invertebrate visual pigment that interacts with Gq-type G-protein to activate the inositol 1,4,5-triphosphate signaling pathway. The crystal structures of the primary photoreaction intermediates bathorhodopsin (Batho) and isorhodopsin (Iso, 9-cis) revealed that light energy absorbed by the protein is converted into distortion energy of the retinal polyene chain: upon photoisomerization, the central moiety moves toward the cytoplasmic side while the ionone ring and Schiff base remain relatively fixed, creating a right-handed screwed configuration.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2011.08.044 | 3P1L | 2.8 A | P62 | C-terminally truncated [squid rhodopsin](/xray-mp-wiki/proteins/squid-rhodopsin/) (residues 1-372, cleaved at Glu373 by V8 protease); bathorhodopsin state (all-trans retinal) | all-trans retinal |
| doi/10.1016##j.jmb.2011.08.044 | 3P1K | 2.7 A | P62 | C-terminally truncated [squid rhodopsin](/xray-mp-wiki/proteins/squid-rhodopsin/) (residues 1-357, cleaved at Glu358 by V8 protease); isorhodopsin state (9-cis retinal) | 9-cis retinal |
| doi/10.1016##j.jmb.2011.08.044 | 2BRS | 2.7 A | P62 | C-terminally truncated [squid rhodopsin](/xray-mp-wiki/proteins/squid-rhodopsin/) (dark state, 11-cis) | 11-cis retinal |
| doi/10.1038##nature06925 | 2BRS | 2.5 A | P62 | C-terminally truncated [squid rhodopsin](/xray-mp-wiki/proteins/squid-rhodopsin/) (residues Glu9-Glu358, cleaved at Glu373 by V8 protease; dark state, 11-cis retinal) | 11-cis retinal |

## Expression and Purification

- **Expression system**: Loligo (Todarodes) pacificus (native retina)
- **Construct**: Native [squid rhodopsin](/xray-mp-wiki/proteins/squid-rhodopsin/) from microvillar membranes; C-terminus truncated by V8 protease cleavage at Glu373 or Glu358

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane extraction | Selective extraction from squid microvillar membranes | -- | Tris buffer with zinc [acetate](/xray-mp-wiki/reagents/buffers/acetate/) + n-octyl beta-D-glucopyranoside ([OG](/xray-mp-wiki/reagents/detergents/og/)) | Rhodopsin extracted selectively from microvillar membranes; all manipulations performed in dim red light (>640 nm) |


## Crystallization

### doi/10.1038##nature06925

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | C-terminally truncated squid rhodopsin solubilized in n-octyl beta-D-glucopyranoside (OG) |
| Reservoir | 3.2 M ammonium sulfate, 32 mM MES pH 6.4, 38 mM EDTA, 10 mM beta-mercaptoethanol |
| Temperature | 277 K |
| Growth time | >6 months |
| Cryoprotection | 20% sucrose, flash-frozen in liquid propane at 100 K |
| Notes | Hexagonal P62 crystals. Extracted from microvillar membranes with octylglucoside in presence of zinc acetate. V8-protease cleavage at Glu373. |

### doi/10.1016##j.jmb.2011.08.044

| Parameter | Value |
|---|---|
| Method | In meso crystallization (hexagonal P62 crystals) |
| Protein sample | Truncated [squid rhodopsin](/xray-mp-wiki/proteins/squid-rhodopsin/) solubilized in n-octyl beta-D-glucopyranoside ([OG](/xray-mp-wiki/reagents/detergents/og/)) |
| Reservoir | not specified |
| Temperature | 100 K (cryogenic) |
| Growth time | not specified |
| Cryoprotection | Cryocooled to 100 K; crystals handled in dim red light (>640 nm) |
| Notes | Hexagonal P62 crystals. Data collected at SPring-8 BL41XU using a 10-micrometer microbeam. Photoreaction states trapped by illumination at specific wavelengths: blue light (473 nm) for bathorhodopsin, yellow light (560 nm) for isorhodopsin, red light (635 nm) for dark-state rhodopsin. |


## Biological / Functional Insights

### Retinal distortion stores light energy in bathorhodopsin

The bathorhodopsin structure reveals that upon photoisomerization (11-cis to all-trans), the retinal central moiety moves largely toward the cytoplasmic side while the ionone ring and Schiff base undergo limited movement. The polyene chain takes on a right-handed screwed configuration with twisted C7=C8, C9=C10, and C11=C12 bonds. The C13 methyl pushes Ser187 into the E-II loop, and the C9 methyl pushes Phe188. This distortion stores approximately 35 kcal/mol of energy, conserved between vertebrate and invertebrate rhodopsins.

### Structural differences from [bovine rhodopsin](/xray-mp-wiki/proteins/bovine-rhodopsin/)

[Squid rhodopsin](/xray-mp-wiki/proteins/squid-rhodopsin/) differs from [bovine rhodopsin](/xray-mp-wiki/proteins/bovine-rhodopsin/) in the retinal-binding pocket: the beta-ionone ring is surrounded by aromatic residues (vs glutamate in bovine), and the retinal polyene chain associates with helix III backbone over three helical turns (vs polar residue Thr118 in bovine). The Schiff base H-bond partner is Asn87 or Tyr111 (vs Gly89 and Glu113 in bovine). These differences slow cis-trans isomerization in [squid rhodopsin](/xray-mp-wiki/proteins/squid-rhodopsin/) compared to bovine while maintaining similar bathorhodopsin energy levels.

### X-ray radiation damage in rhodopsin

Significant X-ray radiation damage was characterized: (1) retinal isomerization to an orange species (precursor of retro form) at approximately 4 x 10^14 photons/mm^2, (2) breakage of disulfide bond between Cys108 and Cys186, (3) loss of electron density at Asp80 (decarboxylation/radiolysis). These changes produce photochemically inactive products that can be distinguished from functional photointermediates. Data collection must account for approximately 50% protein damage at doses of 3 x 10^15 photons/mm^2.


## Cross-References

- [n-Octyl beta-D-glucopyranoside (OG)](/xray-mp-wiki/reagents/detergents/og/) — Primary detergent for squid rhodopsin extraction and crystallization
- [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/) — Crystallization precipitant at 3.2 M in sitting-drop vapor diffusion
- [MES (2-(N-Morpholino)ethanesulfonic Acid)](/xray-mp-wiki/reagents/buffers/mes/) — Crystallization buffer at 32 mM, pH 6.4
- [11-cis-Retinal](/xray-mp-wiki/reagents/ligands/11-cis-retinal/) — Chromophore covalently bound to Lys305 via protonated Schiff base in the dark state
- [Acetate Buffer (sodium acetate)](/xray-mp-wiki/reagents/buffers/acetate/) — Zinc acetate used in squid rhodopsin extraction buffer
- [Tris (Tris-HCl buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Used in extraction buffer for squid rhodopsin purification
- [Bovine Rhodopsin (Dark State)](/xray-mp-wiki/proteins/bovine-rhodopsin/) — Comparative vertebrate rhodopsin; key reference for retinal-binding pocket differences and structural comparison
- [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/) — Cryoprotectant at 20% used for flash-freezing squid rhodopsin crystals
