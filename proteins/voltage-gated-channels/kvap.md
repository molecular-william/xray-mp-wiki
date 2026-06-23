---
title: KvAP Voltage-Dependent Potassium Channel
created: 2026-06-10
updated: 2026-06-10
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature01580, doi/10.1073##pnas.1314356110]
verified: false
---

# KvAP Voltage-Dependent Potassium Channel

## Overview

KvAP is a voltage-dependent potassium channel from the thermophilic archaebacterium Aeropyrum pernix. It serves as a model system for understanding voltage-gated potassium channel structure and gating mechanisms. The channel forms a homotetramer with a central ion-conduction pore lined by the conserved TVGYG selectivity filter motif, surrounded by four voltage-sensor domains. The structure revealed the voltage-sensor paddle architecture and provided the first high-resolution view of a full-length voltage-gated potassium channel.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature01580 | not specified (full-length KvAP-Fab) | 3.2 | I422 | Full-length KvAP from A. pernix (residues 18-240) with Fab 6E1 | K+, Cd2+ |
| doi/10.1038##nature01580 | not specified (isolated VSD-Fab) | 1.9 | C2 | Isolated voltage-sensor domain (Met 1 to Lys 147) with Fab 33H1 | -- |

## Expression and Purification

- **Expression system**: E. coli XL1-Blue
- **Construct**: KvAP full-length (residues 18-240) and isolated voltage-sensor domain (Met 1 to Lys 147) from Aeropyrum pernix, cloned into pQE69 with thrombin cleavage site and C-terminal hexahistidine tag
- **Notes**: Cells grown at 37 C to OD600 ~1.0, induced with 0.4 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) for 4 hours. Also expressed in E. coli for in vivo nonsense suppression of Y199-ester mutant.

### Purification Workflow

*Source: doi/10.1038##nature01580*

- **Expression system**: E. coli XL1-Blue
- **Expression construct**: KvAP full-length (residues 18-240) with C-terminal hexahistidine tag
- **Tag info**: C-terminal hexahistidine, thrombin cleavable

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Chemical lysis with protease inhibitors | — | 50 mM Tris pH 8.0, 100 mM KCl, leupeptin, pepstatin, aprotinin, PMSF |  |
| Membrane extraction | Detergent solubilization | — | 50 mM Tris pH 8.0, 100 mM KCl + 40 mM [DM](/xray-mp-wiki/reagents/detergents/dm/) (DM) | 3 hour extraction at room temperature |
| Affinity purification | [TALON](/xray-mp-wiki/reagents/additives/talon/) Co2+ [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [TALON](/xray-mp-wiki/reagents/additives/talon/) Co2+ affinity resin (Clontech) | 20 mM Tris pH 8.0, 100 mM KCl + 5 mM DM | Eluted with 300-400 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Tag cleavage | [Thrombin Protease](/xray-mp-wiki/reagents/protein-tags/thrombin-protease/) cleavage | — | 20 mM Tris pH 8.0, 100 mM KCl + 5 mM DM | Overnight at room temperature (21 C), 1 unit thrombin per 2 mg protein |
| Size-exclusion chromatography | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) (10/30) (Pharmacia) | 30 mM n-octyl glucoside |  |

### Purification Workflow

*Source: doi/10.1073##pnas.1314356110*

- **Expression system**: E. coli
- **Expression construct**: KvAP with Y199-ester substitution (amber suppression at position 199)
- **Tag info**: Unnatural amino acid (HPLA) incorporated at Y199 via orthogonal tRNA/tRNA synthetase pair

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | In vivo nonsense suppression | — |  | Y199 in KvAP selectivity filter (equivalent to Y78 in [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/), Y445 in Shaker B) replaced with HPLA using amber suppression |
| Purification and reconstitution | Planar lipid bilayer reconstitution | — |  | KvAP Y199-ester mutant incorporated into planar lipid bilayers for single-channel and macroscopic current recordings |


## Crystallization

### doi/10.1038##nature01580

| Parameter | Value |
|---|---|
| Method | Co-crystallization with Fab |
| Protein sample | Full-length KvAP in DM + Fab 6E1 |
| Notes | Full-length KvAP-Fab 6E1 complex in I422. Also isolated VSD-Fab 33H1 in C2. |


## Biological / Functional Insights

### Voltage-sensor paddle architecture

The voltage sensor features a novel helix-turn-helix structure called the voltage-sensor paddle, composed of S3b and N-terminal half of S4. The paddle is located at the protein-lipid interface. Conserved S4 arginines carry most of the gating charge.

### S2 site occupancy regulates C-type inactivation

An ester substitution at the 2' amide bond in the KvAP selectivity filter (Y199-ester, equivalent to Y78 in [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/)) dramatically slows C-type inactivation, similar to the effect in [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/). Single-channel conductance is reduced from 136 pS (WT) to 18 pS (Y199-ester) in 150 mM K+ at +100 mV. Recovery from inactivation is also affected. These results demonstrate that the S2-dependent inactivation mechanism is conserved across K+ channels.

### S4-S5 linker as flexible coupling element

The S4-S5 linker connects the voltage-sensor paddle to the pore-lining S5 helix. It is poorly conserved with many hydrophilic residues and [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) break points.

### Glycine-gating hinge mechanism

The S6 inner helices contain a conserved [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) that acts as a gating hinge, allowing the inner helices to open like a camera aperture.


## Cross-References

- [KcsA Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) — Selectivity filter structure essentially identical; glycine-gating hinge mechanism first identified in KcsA-MthK comparison
- [Decylmaltoside (DM)](/xray-mp-wiki/reagents/detergents/dm/) — Primary detergent (40 mM) for membrane extraction and 5 mM for purification
- [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Main buffer component (50 mM, pH 8.0) throughout purification
- [Potassium Chloride (KCl)](/xray-mp-wiki/reagents/additives/potassium-chloride-kcl/) — 100 mM KCl in lysis buffer; 6 K+ ions in selectivity filter
- [C-type Inactivation](/xray-mp-wiki/concepts/c-type-inactivation/) — Y199-ester mutation slows C-type inactivation in KvAP, linking S2 occupancy to inactivation
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Elution agent (300-400 mM) for TALON Co2+ affinity chromatography
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [IPTG](/xray-mp-wiki/reagents/additives/iptg/) — Additive used in purification or crystallization buffers
- [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) — Additive used in purification or crystallization buffers
- [TALON](/xray-mp-wiki/reagents/additives/talon/) — Additive used in purification or crystallization buffers
