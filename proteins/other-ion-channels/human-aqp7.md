---
title: "Human Aquaporin 7 (AQP7)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2019.11.011]
verified: false
---

# Human Aquaporin 7 (AQP7)

## Overview

Human [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) 7 (AQP7) is an aquaglyceroporin highly expressed in adipocytes that facilitates [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) efflux and is crucial for lipid metabolism. Two X-ray structures of human AQP7 were determined at 1.9 A (PDB 6QZI) and 2.2 A (PDB 6QZJ) resolution. The structures reveal a tetrameric channel with five [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) molecules (G1-G5) in the conducting pore spanning the ar/R selectivity filter, NPA motifs, and cytoplasmic vestibule. Combined with molecular dynamics simulations, the study shows that AQP7 is highly permeable to water (Pf = 4.8 x 10^-14 cm^3/s) but [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) binding reduces water permeability by a factor of 2-4. [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) is conducted via a partly rotating movement, with the NPA region serving as a transition point.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2019.11.011 | 6QZI | 1.9 A | I4 | Human AQP7 (residues 33-279) with N-terminal 6xHis-tag, expressed in Pichia pastoris | [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) (5 molecules per monomer, G1-G5) |
| doi/10.1016##j.str.2019.11.011 | 6QZJ | 2.2 A | I4 | Human AQP7 (residues 33-279) with N-terminal 6xHis-tag, expressed in Pichia pastoris | [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) (5 molecules per monomer) |

## Expression and Purification

- **Expression system**: Pichia pastoris (yeast expression system)
- **Construct**: Human AQP7 residues 33-279 (full-length excluding N-terminal cytoplasmic domain) with N-terminal 6xHis-tag

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane preparation | High-pressure homogenization and ultracentrifugation | -- | 20 mM [Sodium Phosphate](/xray-mp-wiki/reagents/buffers/sodium-phosphate/) pH 8.0, 300 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1 mM [DTT](/xray-mp-wiki/reagents/additives/dtt/) + -- | Cells disrupted by high-pressure homogenization; membranes isolated by centrifugation at 145,000g for 90 min at 4 C |
| Solubilization | Detergent solubilization | -- | 20 mM [Sodium Phosphate](/xray-mp-wiki/reagents/buffers/sodium-phosphate/) pH 8.0, 300 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1 mM [DTT](/xray-mp-wiki/reagents/additives/dtt/) + 1% n-dodecyl-beta-D-maltopyranoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Membranes solubilized for 2 h at 4 C under gentle stirring |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA agarose | Buffer A: 20 mM [Sodium Phosphate](/xray-mp-wiki/reagents/buffers/sodium-phosphate/) pH 8.0, 300 mM NaCl, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.07% [OGNG](/xray-mp-wiki/reagents/detergents/ogng/). Wash: 10 mM then 30 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/). Elution: 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.07% [OGNG](/xray-mp-wiki/reagents/detergents/ogng/) (octyl [Glucose](/xray-mp-wiki/reagents/additives/glucose/) neopentyl glycol) | Protein loaded overnight in presence of 5 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/); eluted with 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Size-exclusion chromatography | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) Increase 10/300 GL | 20 mM [Sodium Phosphate](/xray-mp-wiki/reagents/buffers/sodium-phosphate/) pH 7.5, 100 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.07% [OGNG](/xray-mp-wiki/reagents/detergents/ogng/) + 0.07% [OGNG](/xray-mp-wiki/reagents/detergents/ogng/) | Final polishing step; purity assessed by SDS-PAGE |


## Crystallization

### doi/10.1016##j.str.2019.11.011

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | Purified AQP7 at 9 mg/mL in 0.07% [OGNG](/xray-mp-wiki/reagents/detergents/ogng/) |
| Reservoir | 85 mM Tris pH 8.0, 37% v/v [PEG](/xray-mp-wiki/reagents/additives/peg/) 200, 0.80% v/v n-octyl-beta-D-glucopyranoside |
| Temperature | 4 C |
| Growth time | Not specified |
| Cryoprotection | Crystal 1 (1.9 A): gradient increase of [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) to 20% in 5% increments before plunge freezing. Crystal 2 (2.2 A): 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) in mother liquor before plunge freezing |
| Notes | Two crystals from the same drop were used for data collection at the P13 beamline at PETRA III, EMBL Hamburg. Crystal 1 was subjected to crude dehydration via [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) gradient. Both structures solved by molecular replacement. [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) molecules were modeled in the conducting pore, with G4 occupying two alternative positions (G4a, G4b) at the NPA region. |


## Biological / Functional Insights

### Glycerol conduction via rotating movement

The high-resolution AQP7 structures reveal five [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) molecules (G1-G5) in the pore. At the NPA region, [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) G4 adopts two alternative positions (G4a and G4b, refined to 45% and 55% occupancy), suggesting the NPA area serves as a transition point. The rotation of [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) molecules facilitates breaking of hydrogen bonds to allow movement along the pore, indicating a partly rotating conducting mechanism.

### Glycerol reduces water permeability

MD simulations showed that water permeability (Pf) of AQP7 is 4.8 x 10^-14 cm3/s in the absence of [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), similar to orthodox aquaporins. In the presence of [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), water permeability is reduced 2-4 fold (1.3-2.4 x 10^-14 cm3/s) due to competition for hydrogen-bonding sites. This explains the lower water permeability of AQP7 observed in cellular assays where [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) is present.

### AQP7 selectivity filter architecture

The ar/R selectivity filter of AQP7 has a diameter of 3.3 A, formed by Phe74, Tyr223, Gly222, and His92. Unlike other aquaglyceroporins ([GLPF](/xray-mp-wiki/proteins/other-ion-channels/glpf/), PfAQP), the Tyr223 hydroxyl group provides a hydrogen bond donor that orientates [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) uniquely. This structural feature contributes to AQP7 specificity for [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) over water. The PMF for [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) shows a maximum barrier of ~8 kJ/mol, lower than [GLPF](/xray-mp-wiki/proteins/other-ion-channels/glpf/), consistent with efficient permeation.

### Structural differences between AQP7 and AQP10

Comparison of AQP7 (pore diameter 3.3 A at selectivity filter) with AQP10 (pore diameter ~5 A at selectivity filter) reveals significant differences. AQP10 has a narrowing on the intracellular side that blocks [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) but permits water, and is regulated by pH-dependent gating via His80. In contrast, AQP7 has a narrower selectivity filter but constitutively open intracellular vestibule, explaining their different [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) transport activities.


## Cross-References

- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary solubilization detergent for AQP7
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Substrate of AQP7; used as cryoprotectant and present in crystallization
- [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) — AQP7 belongs to the aquaglyceroporin subfamily
- [Pichia pastoris Expression System](/xray-mp-wiki/methods/expression-systems/pichia-pastoris-expression/) — AQP7 expressed in Pichia pastoris
- [Molecular Dynamics Simulation](/xray-mp-wiki/methods/structure-determination/molecular-dynamics-simulation/) — MD simulations used to study water and glycerol permeation
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [GLPF](/xray-mp-wiki/proteins/other-ion-channels/glpf/) — Related protein structure
- [DTT](/xray-mp-wiki/reagents/additives/dtt/) — Additive used in purification or crystallization buffers
- [Glucose](/xray-mp-wiki/reagents/additives/glucose/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
