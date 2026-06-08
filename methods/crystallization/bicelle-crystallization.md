---
title: Bicelle Crystallization
created: 2026-05-27
updated: 2026-06-03
type: method
category: methods
layout: default
tags: [crystallization-vapor-diffusion, solubilization-bicelle, subdirectory-crystallization]
sources: [doi/10.1016##j.jmb.2022.167795, doi/10.1038##nature12232]
verified: false
---

# Bicelle Crystallization

## Overview

Bicelle crystallization is a membrane protein crystallization technique where the protein is reconstituted into bicelles — small, disk-like lipid-detergent assemblies that mimic the native lipid bilayer environment. Bicelles consist of a mixture of long-chain phospholipids (forming the flat bilayer region) and short-chain detergents (forming the curved rim). The protein-bicelle mixture is combined with precipitant solution in a vapor diffusion setup, and crystals grow as water diffuses and the bicelle composition shifts toward the bilayer-forming regime. Bicelle crystallization has proven effective for ABCG transporter structures.

## Protocol

### Reagents and Materials

- DMPC (1,2-dimyristoyl-sn-glycero-3-phosphocholine) — long-chain phospholipid for bicelle bilayer
- CHAPSO (3-[(3-cholamidopropyl)dimethylammonio]-2-hydroxy-1-propanesulfonate) — zwitterionic detergent for bicelle rim
- Cholesterol — membrane lipid component (5 mol% of lipids)
- Ammonium sulfate — crystallization precipitant
- MES (2-(N-morpholino)ethanesulfonic acid) — buffer
- PEG400 — crystallization additive
- TCEP (tris(2-carboxyethyl)phosphine) — reducing agent

### Steps

1. {'step': 'Bicelle preparation', 'description': 'Reconstitute membrane protein into 10% DMPC/CHAPSO bicelles with lipids and detergents in a 3:1 (w/w) ratio. Include 5 mol% cholesterol and 95 mol% DMPC in the lipid component. The bicelle composition is adjusted by the q-value (ratio of long-chain lipid to detergent).\n'}
2. {'step': 'Protein-bicelle mixing', 'description': 'Mix protein-bicelle stock with precipitant solution in a defined ratio (e.g., 1:4 v/v), resulting in final protein concentration of ~10 mg/ml.\n'}
3. {'step': 'Hanging-drop vapor diffusion', 'description': 'Set up hanging-drop vapor diffusion by mixing protein/bicelle preparation with equal-volume crystallization reservoir solution. Incubate at controlled temperature (e.g., 20 C).\n'}
4. {'step': 'Crystal growth', 'description': 'Crystals typically grow within 1-2 weeks of incubation. Harvest by submerging crystals in cryoprotectant solution.\n'}

### Typical Conditions

- **temperature**: 20 C
- **incubation_time**: 1-2 weeks


## Advantages

- Provides a near-native lipid environment for membrane protein crystallization
- Bicelles are more stable than detergent-only solutions, facilitating crystal growth
- The lipid composition can be tuned by adjusting the q-value and lipid/detergent ratio
- Effective for ABC transporter crystallization

## Disadvantages

- Bicelle composition must be carefully optimized for each protein
- Limited number of successful bicelle crystallization reports compared to LCP or vapor diffusion
- Requires precise control of the q-value and lipid/detergent ratios

## Proteins Using This Method

| Protein | Resolution | PDB | Notes |
|---|---|---|---|
| [Maltose Transporter (MalFGK2)](/xray-mp-wiki/proteins/maltose-transporter/) | 3.9 A | not specified | EIIA^Glc-MalFGK2 complex crystallized in 35% DMPC/CHAPSO bicelles (q-value not specified) at 22 C; EIIA^Glc and MalFGK2 mixed at 2.5:1 molar ratio; structure solved by molecular replacement using PDB 1F3G (EIIA^Glc) and 3FH6 (resting MalFGK2) |
| [ABCG5/G8](/xray-mp-wiki/proteins/abcg5/) | 4.051 A | 8CUB | ABCG5/G8 crystallized in 10% DMPC/CHAPSO bicelles (3:1 w/w) with 5 mol% cholesterol; space group I 2 2 2; solved by molecular replacement using cryo-EM structure PDB 7JR7 |

## Related Methods

- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Another membrane protein crystallization method using lipidic environments
- [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) — Bicelle crystallization uses hanging-drop vapor diffusion setup

## Related Reagents

- [DMPC (1,2-Dimyristoyl-sn-glycero-3-phosphocholine)](/xray-mp-wiki/reagents/lipids/dmpc/) — Long-chain phospholipid component of bicelles
- [CHAPSO](/xray-mp-wiki/reagents/detergents/chapso/) — Zwitterionic detergent forming the curved rim of bicelles
- [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/) — Primary precipitant in bicelle crystallization reservoir
- [MES Buffer](/xray-mp-wiki/reagents/buffers/mes/) — Crystallization buffer (100 mM, pH 6.5)
