---
title: On-Chip Crystallization for Serial Crystallography
created: 2026-06-11
updated: 2026-06-11
type: method
category: methods
layout: default
tags: [crystallization-vapor-diffusion, subdirectory-crystallization]
sources: [doi/10.1107##s2052252519007395]
verified: false
---

# On-Chip Crystallization for Serial Crystallography

## Overview

On-chip crystallization is a method for growing protein crystals directly on micro-patterned silicon chips (Roadrunner chips) for fixed-target serial crystallography experiments. Crystals are grown by sitting-drop vapor diffusion, allowing established crystallization conditions to be directly transferred from conventional hanging-drop or sitting-drop setups. The method eliminates crystal harvesting steps, making it particularly suitable for fragile crystals. After crystal growth, excess mother liquor is blotted away, leaving 'naked' crystals on the chip for in-situ diffraction measurements with very low background scattering. The chips are compatible with both synchrotron and XFEL beamlines, and the exposed crystals are highly accessible for ligand-soaking experiments. Two chip designs exist: Roadrunner I (1.5 x 1.5 mm membrane, 2-3 ul sample) for cryo and room-temperature work, and Roadrunner II (larger, ~100 ul sample) for high-throughput serial data collection.

## Proteins Using This Method

| Protein | Resolution | PDB | Notes |
|---|---|---|---|
| Human [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) 2 ([AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/)) | 3.70 | 6qf5 | On-chip crystallized on Roadrunner II chip, room-temperature SFX at LCLS. 3377 hits from 137476 frames, 2.5% hit rate, data merged from 2903 indexed patterns. |
| [Proteinase K](/xray-mp-wiki/proteins/Proteinase K/) | 1.74 | 6qf1 | On-chip crystallized on Roadrunner I chip, room-temperature data at synchrotron. Data merged from 3 crystals. |
| [Thermolysin](/xray-mp-wiki/reagents/additives/thermolysin/) | 1.73 | 6qf2 | On-chip crystallized on Roadrunner I chip, cryogenic data at PETRA III P11. Data merged from 3 crystals. |
| [Thermolysin-aspartate complex](/xray-mp-wiki/reagents/additives/thermolysin/) | 1.52 | 6qf3 | On-chip crystallized and soaked with 200 mM sodium aspartate on Roadrunner I chip. Data merged from 5 crystals. |
| DRAK2 (human serine/threonine kinase 17B)-ADP complex | 2.50 | 6qf4 | Batch crystallized, then soaked with ATP on Roadrunner I chip. ATP hydrolyzed to ADP during incubation. Data merged from 4 crystals. |

## Related Methods

- [Serial Femtosecond Crystallography](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/) — On-chip crystallization is a sample preparation method for SFX experiments
- [Sitting-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) — On-chip crystallization uses sitting-drop vapor diffusion for crystal growth
- [In Situ X-ray Crystallography](/xray-mp-wiki/concepts/methods-techniques/in-situ-crystallography/) — On-chip crystallization is an in situ crystallography approach
