---
title: AtPIP2;4 (Arabidopsis thaliana Plasma Membrane Intrinsic Protein 2;4)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.bbamem.2019.183065]
verified: false
---

# AtPIP2;4 (Arabidopsis thaliana Plasma Membrane Intrinsic Protein 2;4)

## Overview

AtPIP2;4 is a plasma membrane intrinsic protein (PIP) [Aquaporin](/xray-mp-wiki/concepts/aquaporin/) from Arabidopsis thaliana. It belongs to the PIP2 subfamily of plant [Aquaporin](/xray-mp-wiki/concepts/aquaporin/), which form homotetramers at the plasma membrane and function as water and hydrogen peroxide (H2O2) channels. AtPIP2;4 shares the conserved [Aquaporin](/xray-mp-wiki/concepts/aquaporin/) hourglass architecture with six transmembrane helices and two half-helices containing NPA motifs. The structure was determined at 3.7 Å resolution (PDB: 6QIM), revealing high structural similarity to SoPIP2;1 from spinach (75% sequence identity). Unlike SoPIP2;1, Cd2+ cation is not required to retain the closed conformation. AtPIP2;4 is an efficient transporter of both water and H2O2, with H2O2 transport capacity comparable to SoPIP2;1 and significantly higher than human [AQP1](/xray-mp-wiki/proteins/other-ion-channels/aqp1/).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.bbamem.2019.183065 | 6QIM | 3.7 | P 63 22 | Truncated AtPIP2;4(28-279) with 8xHis-tag, expressed in Pichia pastoris, purified in LDAO/OG micelles | None |

## Expression and Purification

- **Expression system**: Pichia pastoris (X-33Δ strain, aquaporin-deficient)
- **Construct**: Two constructs produced: Full-length AtPIP2;4-FL (1-291) and truncated AtPIP2;4(28-279), both with C-terminal TEV-8xHis tag. Codon-optimized gene, cloned into pPICZB vector.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Bead beating (12×30s with cooling) | -- | Breaking buffer (50 mM potassium phosphate pH 7.5, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 2 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/), 1 mM [Pmsf](/xray-mp-wiki/reagents/additives/pmsf/)) + -- | Glass beads (0.5 mm) used. Cell debris removed at 10,000g. |
| Membrane preparation | Ultracentrifugation and [Urea](/xray-mp-wiki/reagents/substrates/urea/) wash | -- | [Urea](/xray-mp-wiki/reagents/substrates/urea/) buffer (4 M [Urea](/xray-mp-wiki/reagents/substrates/urea/), 5 mM Tris·HCl pH 9.5, 2 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/), 2 mM [Egta](/xray-mp-wiki/reagents/additives/egta/)); Membrane wash buffer (20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 8, 20 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 2 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/), 1 mM [Pmsf](/xray-mp-wiki/reagents/additives/pmsf/)) + -- | Membranes collected at 200,000g for 90 min at 4°C. |
| Solubilization | Detergent solubilization screen | -- | 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 8, 200 mM NaCl + 2% [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) (n-Dodecyl-N,N-Dimethylamine-N-Oxide) | [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) selected as most efficient detergent after screening CHAPS, [DDM](/xray-mp-wiki/reagents/detergents/ddm/), [DM](/xray-mp-wiki/reagents/detergents/dm/), FC12, [LDAO](/xray-mp-wiki/reagents/detergents/ldao/), MNG, NG, β-OG. |
| Ni-NTA affinity chromatography | Immobilized metal affinity chromatography | Ni-NTA agarose (Qiagen) | Wash: 20 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 200 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.4% [LDAO](/xray-mp-wiki/reagents/detergents/ldao/), 50 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/); Elution: 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.4% [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) | 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) added before loading. 50 mg of AtPIP2;4-FL obtained from 90 g cells. |
| Size-exclusion chromatography | SEC for buffer exchange and polishing | Superdex200 Increase 10/300 GL (GE Healthcare) | 20 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 200 mM NaCl + 1% [OG](/xray-mp-wiki/reagents/detergents/og/) (n-Octyl-β-D-Glucopyranoside) or 0.145% OGNPG (Octyl [Glucose](/xray-mp-wiki/reagents/additives/glucose/) Neopentyl Glycol) | For crystallization, β-OG and OGNPG gave monodisperse peaks for FL. For truncated variant, β-OG, [DM](/xray-mp-wiki/reagents/detergents/dm/) and [DDM](/xray-mp-wiki/reagents/detergents/ddm/) gave monodisperse peaks. |


## Crystallization

### doi/10.1016##j.bbamem.2019.183065

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | AtPIP2;4(28-279) at 20 mg/mL in 1% [OG](/xray-mp-wiki/reagents/detergents/og/) |
| Reservoir | 1.5 M sodium formate, 0.05 M sodium [Cacodylate](/xray-mp-wiki/reagents/buffers/cacodylate/) pH 5.5, 30% [PEG400](/xray-mp-wiki/reagents/additives/peg-400/), 3% w/v 6-Aminohexanoic acid, 0.01 M Calcium chloride dihydrate |
| Temperature | 4 |
| Growth time | Few days |
| Cryoprotection | Flash frozen in liquid nitrogen |
| Notes | Crystals appeared after a few days. The tetramer shows a typical [Aquaporin](/xray-mp-wiki/concepts/aquaporin/) oligomer with four individual water pores. Two molecules in asymmetric unit. Data collected at ESRF beamline MASSIF-1 (ID30A-1). Molecular replacement with SoPIP2;1 (PDB: 4jc6). |


## Biological / Functional Insights

### AtPIP2;4 is an efficient H2O2 transporter

AtPIP2;4 transports hydrogen peroxide efficiently, as demonstrated by yeast growth assay (most significant growth defect among 12 AtPIP homologues at 3 mM H2O2), DCF fluorescence assay, and a novel proteoliposome assay. The plant [Aquaporin](/xray-mp-wiki/concepts/aquaporin/) (AtPIP2;4 and SoPIP2;1) are significantly more efficient at H2O2 transport than human [AQP1](/xray-mp-wiki/proteins/other-ion-channels/aqp1/), despite comparable water transport efficiencies. The H2O2 transport is protein-specific and can be inhibited by [Mercury](/xray-mp-wiki/reagents/additives/mercury/) (tested for hAQP1, which has Cys189 in the selectivity filter; plant [Aquaporin](/xray-mp-wiki/concepts/aquaporin/) have Thr at the corresponding position and are mercury-insensitive).

### Loop D conformation in AtPIP2;4 without divalent cation

The AtPIP2;4 structure reveals loop D in a conformation very similar to the closed conformation of SoPIP2;1, despite the absence of a Cd2+ cation. In SoPIP2;1, a divalent cation (Cd2+ in crystals, possibly Ca2+ in vivo) was critical for defining the closed structure by anchoring loop D. The observation that AtPIP2;4 adopts a similar closed conformation without the cation suggests variations in the molecular mechanisms for plant [Aquaporin](/xray-mp-wiki/concepts/aquaporin/) regulation, with possible additional fine-tuning involving loop regions.

### Comparison of transport specificities across aquaporin homologues

The pore-lining residues of hAQP1, SoPIP2;1 and AtPIP2;4 are almost identical. The selectivity filter residues (F87, H216, T225, R231 in AtPIP2;4) show no obvious difference in pore diameter despite T225 being a cysteine in hAQP1. Differences in H2O2 transport efficiency between plant and human [Aquaporin](/xray-mp-wiki/concepts/aquaporin/) cannot be explained by differences in the monomeric pore architecture. The structural determinants likely reside in the flexible loop regions outside the membrane core. Loop D, which is four residues shorter in hAQP1 and lacks the conserved Leu197 involved in PIP channel regulation, is a candidate for contributing to transport specificity differences.


## Cross-References

- [SoPIP2;1 (Spinach Plasma Membrane Aquaporin)](/xray-mp-wiki/proteins/other-ion-channels/so-pip2-1/) — Highly homologous plant aquaporin (75% sequence identity) used as molecular replacement model and for comparative functional analysis
- [Aquaporin Z](/xray-mp-wiki/proteins/other-ion-channels/aquaporin-z/) — Related bacterial aquaporin for comparative structural analysis
- [Pichia pastoris Expression System](/xray-mp-wiki/methods/expression-systems/pichia-pastoris/) — Expression system used for recombinant AtPIP2;4 production
- [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) — Method used for crystallization of AtPIP2;4
- [LDAO (n-Dodecyl-N,N-Dimethylamine-N-Oxide)](/xray-mp-wiki/reagents/detergents/ldao/) — Primary detergent for solubilization and purification
- [n-Octyl-beta-D-glucopyranoside (OG)](/xray-mp-wiki/reagents/detergents/og/) — Detergent used for crystallization and final SEC buffer
- [Aquaporin Family](/xray-mp-wiki/concepts/aquaporin/) — AtPIP2;4 is a member of the aquaporin family
- [AQP1](/xray-mp-wiki/proteins/other-ion-channels/aqp1/) — Referenced in the context of AQP1
- [Urea](/xray-mp-wiki/reagents/substrates/urea/) — Referenced in the context of Urea
- [Tris](/xray-mp-wiki/reagents/buffers/tris/) — Referenced in the context of Tris
