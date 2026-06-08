---
title: KvAP Voltage-Dependent Potassium Channel
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature01580]
verified: false
---

# KvAP Voltage-Dependent Potassium Channel

## Overview

KvAP is a voltage-dependent potassium channel from the thermophilic archaebacterium Aeropyrum pernix. It serves as a model system for understanding voltage-gated potassium channel structure and gating mechanisms. The channel forms a homotetramer with a central ion-conduction pore lined by the conserved TVGYG selectivity filter motif, surrounded by four voltage-sensor domains. This structure revealed the novel voltage-sensor paddle architecture and provided the first high-resolution view of a full-length voltage-gated potassium channel, fundamentally changing the understanding of voltage sensing in these channels.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature01580 | Not specified (PDB ID to be determined) | 3.2 | I422 | Full-length KvAP from Aeropyrum pernix (residues 18-240) in complex with monoclonal Fab fragment 6E1 | K+ (6 ions), Cd2+ (7 ions), H2O (6 molecules) |
| doi/10.1038##nature01580 | Not specified (PDB ID to be determined) | 1.9 | C2 | Isolated voltage-sensor domain of KvAP (Met 1 to Lys 147) in complex with monoclonal Fab fragment 33H1 | H2O (403 molecules) |

## Expression and Purification

- **Expression system**: E. coli XL1-Blue
- **Construct**: KvAP full-length (residues 18-240) and isolated voltage-sensor domain (Met 1 to Lys 147) from Aeropyrum pernix, cloned into pQE69 expression vector between NcoI and BglII sites with a thrombin cleavage site followed by a C-terminal hexahistidine tag. The first five N-terminal residues were replaced by a single leucine during expression. Cells grown at 37 C to OD600 ~1.0 and induced with 0.4 mM IPTG for 4 hours.


### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Chemical lysis with protease inhibitors | -- | 50 mM Tris (pH 8.0), 100 mM KCl, Leupeptin, Pepstatin, Aprotinin, PMSF + -- | Cells harvested and lysed in Tris/KCl buffer with protease inhibitors |
| Membrane extraction | Detergent solubilization | -- | 50 mM Tris (pH 8.0), 100 mM KCl + 40 mM decylmaltoside (DM) | 3 hour extraction at room temperature |
| Affinity purification | Talon Co2+ affinity chromatography | TALON Co2+ affinity resin (Clontech) | 5 mM DM, 20 mM Tris (pH 8.0), 100 mM KCl + 5 mM DM | Eluted with 300-400 mM imidazole |
| Tag cleavage | Thrombin protease cleavage | -- | 5 mM DM, 20 mM Tris (pH 8.0), 100 mM KCl + 5 mM DM | Overnight incubation at room temperature (21 C) with 1 unit thrombin per 2 mg protein |
| Size-exclusion chromatography | Superdex-200 SEC | Superdex-200 (10/30) column (Pharmacia) | 30 mM n-octyl glucoside + 30 mM n-octyl glucoside | Final purification step |


## Crystallization

### doi/10.1038##nature01580

| Parameter | Value |
|---|---|
| Method | Co-crystallization with Fab fragment 6E1 |
| Protein sample | Full-length KvAP in DM |
| Reservoir | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Full-length KvAP-Fab 6E1 complex crystallized in space group I422. Structure solved by molecular replacement using Fab search model. Rwork/Rfree = 25.6%/29.9% at 3.2 A resolution. 22,476 unique reflections. Contains 5,046 protein atoms, 6 H2O, 6 K+, 7 Cd2+. Crystal packing interactions pull outer helices away from pore axis, suggesting open pore conformation. |

| Parameter | Value |
|---|---|
| Method | Co-crystallization with Fab fragment 33H1 |
| Protein sample | Isolated voltage-sensor domain (Met 1 to Lys 147) |
| Reservoir | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Isolated voltage-sensor domain-Fab 33H1 complex crystallized in space group C2. Structure solved by molecular replacement using Fab search model. Rwork/Rfree = 23.1%/25.1% at 1.9 A resolution. 56,778 unique reflections. Contains 4,365 protein atoms and 403 H2O. Fab 33H1 and Fab 6E1 bind the same epitope at the tip of the voltage-sensor paddle. |


## Biological / Functional Insights

### Voltage-sensor paddle architecture

The voltage sensor features a novel helix-turn-helix structure called the voltage-sensor paddle, composed of S3b and the N-terminal half of S4. The paddle is located at the channel's outer perimeter at the protein-lipid interface. It is mainly hydrophobic in composition, with the important exception of conserved S4 arginine residues (positions 117, 120, 123, and 126) that are exposed to solvent. These arginines carry most of the gating charge in voltage-dependent K+ channels. The paddle is flexibly attached to the main channel body through an S3 loop, allowing it to move relative to the pore in response to membrane voltage changes.

### S4-S5 linker as a flexible coupling element

The S4-S5 linker connects the voltage-sensor paddle to the pore-lining S5 helix. It is poorly conserved, contains many hydrophilic amino acids, and is sprinkled with glycine residues that serve as break points. In the full-length channel structure, S4 bends at a glycine residue just after the paddle to redirect into S5, whereas in the isolated voltage sensor, S4 continues as a straight helix. The hydrophilic character of the linker suggests it is well suited to the water interface on the intracellular side of the membrane. Movements of the paddle are coupled to pore opening through this flexible linker.

### Glycine-gating hinge mechanism

The S6 inner helices of KvAP contain a conserved glycine residue that acts as a gating hinge. Bending at this position allows the inner helices to open like the aperture of a camera, similar to the mechanism observed in KcsA and MthK channels. The KvAP channel has a wider open pore than the closed KcsA channel, nearly as wide as the opened MthK channel. The S6-S5 helices maintain an approximately antiparallel relationship, suggesting they move together as a single unit during gating.

### Voltage-sensor conformational flexibility

Comparison of the full-length channel and isolated voltage sensor structures reveals significant conformational differences. In the full-length channel, the voltage sensor is constrained by its attachment to the pore, while in the isolated domain, S1 is folded back and S4 is straight. The relative positions of S2 and the voltage-sensor paddle differ between the two structures, with salt bridges broken in the full-length form. This flexibility, enabled by the S3 loop and S4-S5 linker, suggests the voltage sensor floats inside the membrane as a mobile domain.


## Cross-References

- [KcsA Potassium Channel](/xray-mp-wiki/proteins/kcsa/) — Selectivity filter structure is essentially identical to KcsA; glycine-gating hinge mechanism first identified in KcsA-MthK comparison
- [MthK (Methanobacterium thermoautotrophicum K+ Channel)](/xray-mp-wiki/proteins/mthk/) — KvAP open pore is nearly as wide as opened MthK; glycine-gating hinge mechanism shared
- [Decylmaltoside (DM)](/xray-mp-wiki/reagents/detergents/decylmaltoside/) — Primary detergent (40 mM) for membrane extraction and 5 mM for purification
- [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Main buffer component (50 mM, pH 8.0) used throughout purification and crystallization
- [Potassium Chloride (KCl)](/xray-mp-wiki/reagents/additives/potassium-chloride-kcl/) — 100 mM KCl in lysis buffer; 6 K+ ions observed in selectivity filter
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Elution agent (300-400 mM) for TALon Co2+ affinity chromatography
- [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon/) — TALon Co2+ affinity resin used for His-tag purification
- [Superdex 200 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200/) — Superdex-200 (10/30) column used for final size-exclusion purification
