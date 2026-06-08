---
title: 
created: 2026-05-26
updated: 2026-05-26
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.bbabio.2023.148986]
verified: false
---

# 

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

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Thylakoid membrane isolation | Thylakoid membrane isolation | -- | Slightly acidic buffer, pH 6.5, low ionic strength + -- | PSI-LHCI supercomplexes purified from thylakoid membranes of C. reinhardtii. Mild, column-free isolation. |
| Membrane solubilization | Membrane solubilization | -- | pH 6.5 buffer + n-dodecyl-beta-D-maltopyranoside (M(/xray-mp-wiki/reagents/detergents/ddm/)) | Solubilization by M(/xray-mp-wiki/reagents/detergents/ddm/) from thylakoid membranes. |
| Sucrose density gradient ultracentrifugation | Sucrose density gradient ultracentrifugation | Sucrose gradient | pH 6.5 buffer + M(/xray-mp-wiki/reagents/detergents/ddm/) | Purification by sucrose density gradient ultracentrifugation yielded PSI-8LHCI supercomplexes. |
| Detergent exchange | Detergent exchange (cryo-EM sample) | Sucrose density gradient | pH 6.5 buffer + [glyco-diosgenin](/xray-mp-wiki/reagents/detergents/glyco-diosgenin/) (GDN) | For cryo-EM sample preparation, M(/xray-mp-wiki/reagents/detergents/ddm/) exchanged to GDN by second sucrose density gradient. |


## Crystallization

### 10.1016##j.bbabio.2023.148986

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Temperature | Room temperature |
| Notes | Initial crystals appeared after 3 days, grew to 0.3 mm over 3-4 weeks. One PSI-LHCI molecule per asymmetric unit. |

| Parameter | Value |
|---|---|
| Method | Cryoprotection soaking |
| Temperature | 277 K (soaking), 100 K (data collection) |
| Notes | Cryoprotected crystals diffracted to 3.2 A. Space group P21, a=94.6 A, b=98.1 A, c=210.1 A, gamma=94.6 deg. PDB TBD. Data at SPring-8 BL44XU. |


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

- [Lithium Sulfate](/xray-mp-wiki/reagents/additives/lithium-sulfate/) — Crystallization buffer component (50 mM Li2SO4)
- [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) — Crystallization precipitant (PEG 400, PEG 6000)
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for solubilization and cryoprotection
- [Tris Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Crystallization buffer (50 mM Tris-HCl pH 7.0)
- [Membrane Protein Structural Biology Concepts](/xray-mp-wiki/concepts/membrane-mimetics/) — Photosystem is a large multisubunit membrane protein complex
