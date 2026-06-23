---
title: "KvAP voltage-dependent K+ channel from Aeropyrum pernix"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.0507651102]
verified: false
---

# KvAP voltage-dependent K+ channel from Aeropyrum pernix

## Overview

[KvAP Voltage-Dependent Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kvap/) is a voltage-dependent K+ channel from the hyperthermophilic archaeon Aeropyrum pernix and was the first Kv channel to have its crystal structure determined. This study presents two new structures: the [KvAP Voltage-Dependent Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kvap/)-Fv antibody fragment complex at 3.9 A resolution and an 8 A structure without antibody fragments. Together with disulfide cross-linking studies in lipid membranes and comparison with the eukaryotic Kv1.2 channel structure, the work demonstrates that (i) [KvAP Voltage-Dependent Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kvap/) is structurally similar to Kv1.2 with modest voltage sensor orientation differences, (ii) antibody fragments are not the source of non-native conformations, and (iii) [KvAP Voltage-Dependent Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kvap/) requires an intact lipid membrane to maintain native voltage sensor orientation because its voltage sensors and pore are loosely adherent domains. The voltage sensor paddle (helix-turn-helix formed by S3b and S4) functions at the protein-lipid interface, consistent with the original voltage-sensing paddle model.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.0507651102 | 2A0L | 3.9 A | Tetragonal | Truncated [KvAP Voltage-Dependent Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kvap/) (36 C-terminal amino acids deleted) | None |

## Expression and Purification

- **Expression system**: E. coli
- **Construct**: Truncated [KvAP Voltage-Dependent Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kvap/) (36 C-terminal residues deleted)

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression and purification | Standard recombinant expression and membrane protein purification | -- | -- + [DHPC](/xray-mp-wiki/reagents/detergents/dhpc/) (1,2-diheptanoyl-sn-glycero-3-phosphocholine) | [KvAP Voltage-Dependent Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kvap/) was purified in the detergent-like lipid [DHPC](/xray-mp-wiki/reagents/detergents/dhpc/) for crystallization |


## Crystallization

### doi/10.1073##pnas.0507651102

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified [KvAP Voltage-Dependent Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kvap/) in [DHPC](/xray-mp-wiki/reagents/detergents/dhpc/) |
| Reservoir | -- |
| Mixing ratio | -- |
| Temperature | -- |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | Two crystal forms: (1) [KvAP Voltage-Dependent Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kvap/)-33H1 Fv complex in tetragonal space group at 3.9 A, (2) [KvAP Voltage-Dependent Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kvap/) alone in triclinic space group at 8 A. [DHPC](/xray-mp-wiki/reagents/detergents/dhpc/) used as detergent-like lipid for both forms. Fv-mediated crystal contacts in the tetragonal form. |


## Biological / Functional Insights

### Voltage sensor orientation in membranes

The voltage sensors of [KvAP Voltage-Dependent Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kvap/) are loosely attached to the pore as self-contained structural domains. In detergent micelles, the sensors adopt non-native orientations, but in lipid membranes they assume their correct position. The S2-S3 turn contains five tyrosine residues that would be energetically driven to the lipid-water interface in a planar membrane, providing a mechanism for correct sensor positioning. This explains why [KvAP Voltage-Dependent Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kvap/) does not maintain a native conformation in crystals - the detergent micelle is an imperfect mimic of the lipid bilayer for proteins with loosely adherent domains.

### Voltage sensor paddle (helix-turn-helix)

The voltage sensor paddle (S3b-S4 helix-turn-helix) is a highly mobile element at the protein-lipid interface. EPR data show high lipid accessibility of S4 residues, and disulfide cross-linking studies confirm the paddle is near the extracellular end of S5 of a neighboring subunit. The four conserved arginine residues on S4 (gating charges) are near the extracellular surface in the open conformation, and they translate 15-20 A across the membrane during gating. This supports the original paddle model for voltage-dependent gating.

### Comparison with Kv1.2

The [KvAP Voltage-Dependent Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kvap/) model constructed from these data is quite similar to the eukaryotic Kv1.2 channel structure (PDB 2A79). The voltage sensor in [KvAP Voltage-Dependent Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kvap/) is rotated slightly about an axis perpendicular to the membrane plane relative to the pore, making S1 more buried and S4 more exposed to lipid, consistent with EPR accessibility data. The S6 inner helices have a wide diameter (~12 A) near the intracellular pore entryway, suggesting the pore is in an open conformation.

### S2-S3 turn as membrane interface anchor

The S2-S3 turn, not resolved in Kv1.2 but defined in several [KvAP Voltage-Dependent Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kvap/) crystal structures, contains a conserved salt-bridge pair and five tyrosine residues. This turn appears to serve as a membrane interface anchor and is intrinsically flexible, adopting different conformations in different crystal forms (1ORS, 1ORQ, 2A0L). This flexibility may allow the voltage sensor paddle to undergo the large movements required for voltage-dependent gating.


## Cross-References

- [Voltage Sensor Paddle Mechanism](/xray-mp-wiki/concepts/construct-design/voltage-sensor-paddle/) — KvAP is the prototype for the voltage-sensor paddle model of voltage-dependent gating
- [Voltage-Dependent Gating](/xray-mp-wiki/concepts/voltage-dependent-gating/) — KvAP is a voltage-dependent K+ channel that established the paddle mechanism for voltage sensing
- [Membrane Protein-Lipid Interface](/xray-mp-wiki/concepts/membrane-protein-lipid-interface/) — KvAP requires a planar lipid membrane to maintain native voltage sensor orientation, demonstrating the importance of the protein-lipid interface
- [X-ray Crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/) — Method used in the study
- [Voltage-Sensor Paddle](/xray-mp-wiki/concepts/construct-design/voltage-sensor-paddle/) — Key concept related to this protein
- [GR (Halobacterium sp. GR Bacteriorhodopsin)](/xray-mp-wiki/proteins/rhodopsins/gr/) — Related protein mentioned in the study
- [KvAP Voltage-Dependent Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kvap/) — Related protein mentioned in the study
- [ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel)](/xray-mp-wiki/proteins/cys-loop-receptors/elic/) — Related protein mentioned in the study
- [1,2-Dihexanoyl-sn-glycero-3-phosphocholine (DHPC)](/xray-mp-wiki/reagents/detergents/dhpc/) — Reagent used in the study
- [n-Octyl beta-D-glucopyranoside (OG)](/xray-mp-wiki/reagents/detergents/og/) — Detergent used in purification
