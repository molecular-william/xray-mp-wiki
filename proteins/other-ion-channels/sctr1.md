---
title: sCtr1 (High-Affinity Copper Transporter from Salmo salar)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-019-09376-7]
verified: false
---

# sCtr1 (High-Affinity Copper Transporter from Salmo salar)

## Overview

Ctr1 is the evolutionarily conserved high-affinity Cu⁺ transporter crucial for dietary copper uptake and peripheral distribution. The X-ray crystal structures of Salmo salar Ctr1 (sCtr1) were determined in both Cu⁺-free and Cu⁺-bound states, revealing a homo-trimeric Cu⁺-selective ion channel-like architecture. Two layers of methionine triads (M146 and M150 in TM2) form a selectivity filter at the extracellular entrance, coordinating two bound Cu⁺ ions. A Zn²⁺ binding site comprised of E80 (TM1) and H135 (TM2) was also identified, with mutations at these positions increasing Cu⁺ transport rate. The C-terminal HCH motif potentially forms an intracellular gate.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-019-09376-7 | unknown | 3.0 | H32 | sCtr1_cryst (ΔN40, BRIL insertion) |  |
| doi/10.1038##s41467-019-09376-7 | unknown | 3.2 | H32 | sCtr1_cryst | Cu⁺ |

## Expression and Purification

- **Expression system**: [Pichia pastoris](/xray-mp-wiki/methods/expression-systems/pichia-pastoris/) SMD1163H
- **Construct**: sCtr1_cryst (N-terminal 40 residues deleted, intracellular loop 94–120 replaced by BRIL)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell disruption | Ball milling (Retsch MM400) | — | 50 mM [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, protease inhibitors |  |
| Solubilization | Detergent extraction | — | 50 mM [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl + 2% (w/v) [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) | 3 h at 4 °C |
| Cobalt affinity chromatography | Immobilized metal-affinity chromatography | Cobalt resin (Clontech) | 20 mM [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 30 mM imidazole, 4 mM [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) | C-terminal GFP tag removed by PreScission protease overnight at 4 °C |
| Size-exclusion chromatography | Gel filtration | Superose 6 (GE Healthcare) | 20 mM [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 5 mM [Dithiothreitol (DTT)](/xray-mp-wiki/reagents/additives/dtt/), 5 mM CYMAL-5 |  |


## Crystallization

### doi/10.1038##s41467-019-09376-7

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, hanging drop |
| Protein sample | ~7 mg/ml sCtr1_cryst |
| Reservoir | 26% [Polyethylene Glycol 400 (PEG 400)](/xray-mp-wiki/reagents/additives/peg-400/), 50 mM Zn(OAc)₂, 50 mM [Sodium Cacodylate](/xray-mp-wiki/reagents/buffers/cacodylate/) pH 5.9 |
| Temperature | 20 °C |
| Notes | Crystals appeared in 2 days, grew to full size within 2 weeks. Space group H32. |


## Biological / Functional Insights

### Selectivity filter

Two strictly conserved [methionine triads](/xray-mp-wiki/concepts/transport-mechanisms/selectivity-filter/) (M146 and M150 in TM2, MX₃M motif) form a Cu⁺ selectivity filter near the extracellular entrance. Each triad coordinates a single Cu⁺ ion through trigonal planar Cu-S coordination, conferring selectivity for Cu⁺ over Cu²⁺.

### Zinc binding and regulation

A Zn²⁺ binding site is formed by E80 (TM1) and H135 (TM2) from adjacent subunits. Mutations at corresponding positions in human Ctr1 (E84Q, H139R) increase Cu⁺ transport rate, suggesting Zn²⁺ negatively regulates Cu⁺ transport.


## Cross-References

- [Selectivity Filter](/xray-mp-wiki/concepts/transport-mechanisms/selectivity-filter/) — Two methionine triads form a Cu⁺ selectivity filter
- [Channel-Like Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/channel-like-mechanism/) — Ctr1 functions like an ion channel for Cu⁺ conduction
- [Intramembrane Ion Coordination](/xray-mp-wiki/concepts/membrane-mimetics/membrane-mimetics/membrane-mimetics/intramembrane-ion-coordination/) — Cu⁺ is coordinated by methionine S atoms in the selectivity filter
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — SEC was used as a final purification step
- [Hanging Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) — Crystals were grown by hanging drop vapor diffusion
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for solubilization at 2% (w/v)
- [Tris](/xray-mp-wiki/reagents/buffers/tris/) — Primary buffer component throughout purification
- [DTT](/xray-mp-wiki/reagents/additives/dtt/) — Reducing agent in SEC buffer
- [PEG 400](/xray-mp-wiki/reagents/additives/peg-400/) — Precipitant in crystallization conditions
- [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) — Fusion protein used in crystallization construct
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Used in cobalt affinity wash buffer
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Used as cryoprotectant
- [Pichia pastoris Expression System](/xray-mp-wiki/methods/expression-systems/pichia-pastoris/) — Used for recombinant expression of sCtr1
- [Sodium Cacodylate](/xray-mp-wiki/reagents/buffers/cacodylate/) — Buffer component in crystallization reservoir solution
