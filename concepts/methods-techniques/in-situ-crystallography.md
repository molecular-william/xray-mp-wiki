---
title: In situ X-ray Crystallography
created: 2026-06-11
updated: 2026-06-11
type: concept
category: concepts
layout: default
tags: [concept-crystallography-principle, subdirectory-concepts]
sources: [doi/10.1107##s139900471500423x, doi/10.1107##S1399004715005210, doi/10.1016##j.str.2018.10.027, doi/10.1107##s2052252519007395]
verified: false
---

# In situ X-ray Crystallography

## Overview
In situ X-ray crystallography is a technique where X-ray diffraction data are collected
directly from crystals in their crystallization plates or on their growth supports,
eliminating the need for manual crystal harvesting, cryoprotection, and cryocooling.
This approach is particularly valuable for membrane proteins, whose crystals are often
small, fragile, and sensitive to handling. By recording data from many crystals at room
temperature and merging the partial datasets using specialized software such as BLEND,
sufficient completeness can be achieved for structure determination. The first
demonstration of in situ membrane protein structure determination at a synchrotron was
the 2.3 A structure of Haemophilus influenzae [TEHA](/xray-mp-wiki/proteins/other-ion-channels/teha/) ([HITEHA](/xray-mp-wiki/proteins/other-ion-channels/hiteha/), PDB 4ycr) using 63 partial
datasets from 56 crystals, with data collected on Diamond Light Source beamline I24.
Related approaches include IMISX (in meso in situ) for crystals grown in lipidic cubic
phase, and on-chip crystallization on silicon chips for fixed-target serial
crystallography (Lieske et al., 2019).


## Mechanism/Details


## Examples in Membrane Protein Work
- [HITEHA](/xray-mp-wiki/proteins/other-ion-channels/hiteha/) (Haemophilus influenzae [TEHA](/xray-mp-wiki/proteins/other-ion-channels/teha/)) — First membrane protein structure determined by in situ data collection at a synchrotron. 56 crystals grown in sitting-drop vapour-diffusion plates. 63 partial datasets (30-50 images of 0.2 deg each at 25 frames/s) were recorded in less than 3 h on Diamond I24. Data merged using BLEND to 2.3 A resolution (PDB 4ycr).
- CC Chemokine Receptor 2A ([CCR2A](/xray-mp-wiki/proteins/gpcr/ccr2a/)) — IMISX approach: crystals grown in LCP in glass sandwich plates with 64 um spacer. Entire drop cut out and plunge-frozen. Serial data collection from 77 crystals at SLS gave 2.7 A structure (PDB 6GPX).
- Human [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) 2 (hAQP2) — On-chip crystallization on micro-patterned silicon chips (Roadrunner II). Crystals grown by sitting-drop vapor diffusion directly on chip. Room-temperature SFX at LCLS with 3377 hits from 137476 frames; structure at 3.7 A resolution (PDB 6qf5).
- Proteinase K — On-chip crystallization on Roadrunner I chip by sitting-drop vapor diffusion. Room-temperature data collection at synchrotron yielded 1.74 A structure (PDB 6qf1).
- [Thermolysin](/xray-mp-wiki/reagents/additives/thermolysin/) — On-chip crystallization on Roadrunner I chip; on-chip ligand soaking with 200 mM sodium aspartate. Cryogenic data collection gave 1.52 A structure of the thermolysin-aspartate complex (PDB 6qf3).

## Related Concepts
- [Serial Femtosecond Crystallography](/xray-mp-wiki/concepts/serial-femtosecond-crystallography/) — Related approach using XFELs for room-temperature data collection; in situ methods provide an alternative at synchrotron sources
- [Fixed-Target Serial Crystallography](/xray-mp-wiki/methods/crystallography/fixed-target-serial-crystallography/) — On-chip crystallization provides fixed-target sample holders for serial data collection

## Cross-References
- [HiTehA — Haemophilus influenzae TehA](/xray-mp-wiki/proteins/other-ion-channels/hiteha/) — First membrane protein structure by in situ data collection
- [IMISX In-Situ Serial Crystallography](/xray-mp-wiki/methods/imisx-in-situ-crystallization/) — Related in situ method using LCP crystallization and serial data collection
- [X-ray Crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/) — In situ crystallography is a variant of X-ray crystallography
- [On-Chip Crystallization](/xray-mp-wiki/methods/on-chip-crystallization/) — Method for growing crystals directly on silicon chips for in-situ serial crystallography
- [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) — Related biological concept
- [CCR2A](/xray-mp-wiki/proteins/gpcr/ccr2a/) — Related protein structure
- [TEHA](/xray-mp-wiki/proteins/other-ion-channels/teha/) — Related protein structure
- [Thermolysin](/xray-mp-wiki/reagents/additives/thermolysin/) — Additive used in purification or crystallization buffers
