---
title: PSI-LHCI supercomplex from Chlamydomonas reinhardtii
created: 2026-05-26
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.bbabio.2023.148986]
verified: false
---

# PSI-LHCI supercomplex from Chlamydomonas reinhardtii

## Overview

The photosystem I–light-harvesting complex I (PSI-LHCI) supercomplex from the green alga Chlamydomonas reinhardtii. Three distinct structures were determined by X-ray crystallography and single particle [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/), revealing a resting state of PSI-8LHCI with reduced chlorophyll content, electron donors docked in waiting positions on the luminal side, and regulatory binding partners at the stromal electron acceptor site. Binding of oxidized ferredoxin triggers a conformational change that activates the complex for electron transfer.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.bbabio.2023.148986 | 7WYI | 3.98 A | C1 (single particle cryo-EM) | PSI-8LHCI Form B ([Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) resting state structure) | Chlorophyll a, carotenoids, iron-sulfur clusters (Fx, Fa, Fb), unidentified stromal binding partners (sigma1, sigma2, sigma3) |
| doi/10.1016##j.bbabio.2023.148986 | 7WZN | 4.94 A | C1 (single particle cryo-EM) | PSI-8LHCI with gallium-substituted ferredoxin (Fd_Ga) Form C ([Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) active state structure) | Chlorophyll a, carotenoids, iron-sulfur clusters, gallium-ferredoxin (GaFd) |
| doi/10.1016##j.bbabio.2023.148986 | 6JO5 | 3.0 A | P21 (X-ray crystal structure) | PSI-8LHCI Form A (X-ray crystal structure) | Chlorophyll a, carotenoids, iron-sulfur clusters (Fx, Fa, Fb) |

## Expression and Purification

- **Expression system**: Chlamydomonas reinhardtii (green alga)
- **Construct**: PSI-8LHCI supercomplex purified directly from thylakoid membranes

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Thylakoid membrane isolation | Cell disruption and membrane isolation | -- | Slightly acidic buffer, pH 6.5, low ionic strength + -- | PSI-LHCI supercomplexes purified from thylakoid membranes of C. reinhardtii. Mild, column-free isolation procedure. |
| Membrane solubilization | Detergent solubilization | -- | pH 6.5 buffer + n-dodecyl-beta-D-maltopyranoside (beta-[DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Solubilization by beta-[DDM](/xray-mp-wiki/reagents/detergents/ddm/) from thylakoid membranes. Mild detergent used for preserving supercomplex integrity. |
| [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/) density gradient ultracentrifugation | [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/) density gradient ultracentrifugation | [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/) gradient | pH 6.5 buffer + beta-[DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Purification by [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/) density gradient ultracentrifugation yielded PSI-8LHCI supercomplexes suitable for crystallography and [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/). |
| Detergent exchange for [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) | Detergent exchange | [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/) density gradient | pH 6.5 buffer + [GDN](/xray-mp-wiki/reagents/detergents/glyco-diosgenin/) ([GDN](/xray-mp-wiki/reagents/detergents/glyco-diosgenin/)) | For [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) sample preparation, beta-[DDM](/xray-mp-wiki/reagents/detergents/ddm/) exchanged to [GDN](/xray-mp-wiki/reagents/detergents/glyco-diosgenin/) ([GDN](/xray-mp-wiki/reagents/detergents/glyco-diosgenin/)) by second [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/) density gradient ultracentrifugation. |


## Crystallization

### doi/10.1016##j.bbabio.2023.148986

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | PSI-8LHCI supercomplex at 3 mg/mL in pH 6.5 buffer |
| Reservoir | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) (pH 7.0), 50 mM Li2SO4, 4.5-7.0% (w/v) [PEG](/xray-mp-wiki/reagents/additives/peg/) 6000 |
| Temperature | Room temperature |
| Growth time | Initial crystals appeared after 3 days; grew to 0.3 mm over 3-4 weeks |
| Cryoprotection | Crystals soaked in crystallization buffer with 0.05% beta-[DDM](/xray-mp-wiki/reagents/detergents/ddm/), then gradually increased [PEG](/xray-mp-wiki/reagents/additives/peg/) 6000 and Li2SO4 to 8% and 100 mM respectively, followed by [PEG](/xray-mp-wiki/reagents/additives/peg/) 400 (17.5% v/v) and triethylene glycol (TEG, 17.5% v/v) |
| Notes | One PSI-LHCI molecule per asymmetric unit. Crystals diffracted to 3.2 A resolution. Space group P21, a=94.6 A, b=98.1 A, c=210.1 A, gamma=94.6 deg. Data collected at SPring-8 BL44XU at 100 K. |


## Biological / Functional Insights

### Resting state of PSI-LHCI

The PSI-LHCI supercomplex exists in a resting state with reduced chlorophyll content (six bridging chlorophylls absent from the luminal LHCI belt), electron donors (plastocyanin) docked in waiting positions on the luminal side, and regulatory binding partners (sigma1, sigma2, sigma3) positioned at the stromal electron acceptor site. This resting state avoids undesirable electron injection from plastocyanin or cytochrome c6 while allowing rapid productive binding for electron donation when needed.

### Ferredoxin-induced activation

Binding of oxidized ferredoxin to the PsaC electron acceptor site triggers dissociation of stromal regulatory binding partners (sigma1, sigma2, sigma3) and causes luminal electron donors to leave their waiting positions. This activates the PSI-LHCI complex for productive electron transfer. The edge-to-edge distance between the FB cluster and the Fe2S2 cluster of ferredoxin is approximately 9 Angstroms, close enough for efficient electron tunneling.

### Chlorophyll loss from LHCI belt

The Form A X-ray structure reveals absence of six chlorophylls from the luminal side of the LHCI belts. These bridging chlorophylls are normally found in previous [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) structures and their absence may significantly influence excitation energy transfer between light harvesting complexes and the PSI core.


## Cross-References

- [N-Dodecyl-beta-D-maltopyranoside (beta-DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for solubilization of thylakoid membranes and purification of PSI-8LHCI supercomplex
- [Glyco-diosgenin (GDN)](/xray-mp-wiki/reagents/detergents/glyco-diosgenin/) — Used for detergent exchange for cryo-EM sample preparation
- [Tris (Tris-HCl buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Crystallization buffer component (50 mM Tris-HCl, pH 7.0)
- [Lithium Sulfate](/xray-mp-wiki/reagents/additives/lithium-sulfate/) — Crystallization precipitant component (50-100 mM Li2SO4)
- [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) — Crystallization precipitant (4.5-7.0% PEG 6000) and cryoprotectant component (PEG 400)
- [Membrane Protein Structural Biology Concepts](/xray-mp-wiki/concepts/membrane-mimetics/) — PSI-LHCI is a large multisubunit membrane protein complex embedded in the thylakoid membrane
- [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) — Method used in structure determination or purification
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component in purification or crystallization
- [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/) — Related ligand or cofactor
