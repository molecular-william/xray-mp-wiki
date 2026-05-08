---
title: PSI-LHCI from Chlamydomonas reinhardtii
created: 2026-05-07
updated: 2026-05-07
type: protein
category: proteins
layout: default
tags: [membrane-protein, xray-crystallography, cryo-em, photosynthesis]
sources: [doi/10.1016##j.bbabio.2023.148986]
verified: true
---

# PSI-LHCI from Chlamydomonas reinhardtii

## Overview

The photosystem I-light harvesting complex I (PSI-LHCI) supercomplex from the green alga
Chlamydomonas reinhardtii. This study reports three distinct structures of the PSI-8LHCI
supercomplex determined by X-ray crystallography and single particle cryo-EM. The structures
reveal a resting state of PSI-LHCI with reduced chlorophyll content, electron donors docked
in waiting positions on the luminal side, and regulatory binding partners positioned at the
electron acceptor site on the stromal side. Binding of oxidized ferredoxin triggers a
conformational change that activates the complex for electron transfer.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.bbabio.2023.148986 | 7WYI | 3.2 A | P21 | PSI-8LHCI Form A (X-ray crystal structure) | Chlorophyll a, carotenoids, Fe-S clusters (Fx, Fa, Fb) |
| doi/10.1016##j.bbabio.2023.148986 | 7WZN | 4.94 A | C1 (single particle) | PSI-8LHCI + Ga-ferredoxin Form C (cryo-EM) | Chlorophyll a, carotenoids, Fe-S clusters, gallium-ferredoxin |
| doi/10.1016##j.bbabio.2023.148986 | 7WZQ | 3.98 A | C1 (single particle) | PSI-8LHCI Form B (cryo-EM resting state) | Chlorophyll a, carotenoids, Fe-S clusters, unidentified stromal binding partners |

## Expression and Purification

- **Expression system**: Chlamydomonas reinhardtii (green alga)
- **Construct**: PSI-8LHCI supercomplex purified from thylakoid membranes

No purification described.

## Crystallization

### doi/10.1016##j.bbabio.2023.148986

| Parameter | Value |
|---|---|
| Method | Hanging drop vapor diffusion |
| Protein sample | PSI-8LHCI purified by sucrose density gradient |
| Reservoir | 50 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/)-HCl (pH 7.0), 50 mM [Li2SO4](/xray-mp-wiki/reagents/additives/lithium-sulfate/), 4.5-7.0% [PEG 6000](/xray-mp-wiki/reagents/additives/peg/) |
| Mixing ratio | 1:1 (protein sample to reservoir) |
| Temperature | 277 K |
| Growth time | 3-4 weeks |
| Cryoprotection | 17.5% [PEG 400](/xray-mp-wiki/reagents/additives/peg/), 17.5% TEG, 8% [PEG 6000](/xray-mp-wiki/reagents/additives/peg/), 50 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/)-HCl pH 7.0, 100 mM [Li2SO4](/xray-mp-wiki/reagents/additives/lithium-sulfate/), 0.05% beta-[DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Notes | Initial crystals appeared in 3 days, grew to 0.3 mm in longest dimension. Data collected at SPring-8 BL44XU. |


## Biological / Functional Insights

### Resting state of PSI-LHCI

The PSI-LHCI supercomplex exists in a resting state with reduced chlorophyll content
(six bridging chlorophylls absent from the luminal LHCI belt), electron donors (plastocyanin)
docked in waiting positions on the luminal side, and regulatory binding partners at the
stromal electron acceptor site. This resting state avoids undesirable electron injection
from plastocyanin or cytochrome c6 while allowing rapid productive binding for electron
donation when needed.

### Ferredoxin-induced activation

Binding of oxidized ferredoxin to the PsaC electron acceptor site triggers dissociation
of stromal regulatory binding partners (sigma1, sigma2, sigma3) and causes luminal electron
donors to leave their waiting positions. This activates the PSI-LHCI complex for productive
electron transfer. The edge-to-edge distance between the FB cluster and the Fe2S2 cluster
of ferredoxin is approximately 9 Angstroms, close enough for efficient electron tunneling.

### Chlorophyll loss from LHCI belt

The Form A X-ray structure reveals absence of six chlorophylls from the luminal side of
the LHCI belts. These bridging chlorophylls are normally found in previous cryo-EM structures
and their absence may significantly influence excitation energy transfer between light
harvesting complexes and the PSI core.


## Cross-References

- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for solubilization and cryoprotection
- [Membrane Protein Structural Biology Concepts](/xray-mp-wiki/concepts/membrane-mimetics/) — Photosystem is a large multisubunit membrane protein complex
