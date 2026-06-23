---
title: iC++ (Designed Anion Channelrhodopsin)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41586-018-0504-5]
verified: false
---

# iC++ (Designed Anion Channelrhodopsin)

## Overview

iC++ is a designed anion-conducting channelrhodopsin (dACR) created by structure-guided engineering of the C1C2 chimeric cation channelrhodopsin (CCR) through 10 mutations in transmembrane helices 1, 2, 3, and 7. Crystal structures were determined at pH 8.5 (3.2 A resolution) and pH 6.5 (3.2 A resolution), revealing the molecular basis for anion selectivity, pH dependence, and channel gating in both designed (dACRs) and natural (nACRs) anion channelrhodopsins. Comparison with the natural ACR [GtACR1 Anion Channelrhodopsin from Guillardia theta](/xray-mp-wiki/proteins/rhodopsins/gtacr1/) showed that iC++ extracellular vestibule shapes are more similar to nACRs than to its CCR parent C1C2. Structure-guided engineering of [GtACR1 Anion Channelrhodopsin from Guillardia theta](/xray-mp-wiki/proteins/rhodopsins/gtacr1/) led to FLASH (fast, light-activated anion-selective rhodopsin), integrating large photocurrents with fast kinetics. The structures provide insights into pore-surface electrostatics as the primary determinant of ion selectivity in channelrhodopsins.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41586-018-0504-5 | 6CSN | 3.2 A | not specified | iC++ with N61Q mutation, N-terminal [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) and C-terminal EGFP-His10 tag (pH 8.5, dark state) | all-trans-[Retinal](/xray-mp-wiki/reagents/ligands/retinal/) |
| doi/10.1038##s41586-018-0504-5 | 6CSO | 3.2 A | not specified | iC++ with N61Q mutation, N-terminal [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) and C-terminal EGFP-His10 tag (pH 6.5, dark state) | all-trans-[Retinal](/xray-mp-wiki/reagents/ligands/retinal/) |

## Expression and Purification

- **Expression system**: Spodoptera frugiperda Sf9 insect cells (baculovirus expression system)
- **Construct**: iC++ with N61Q mutation, N-terminal [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) (3C protease site), C-terminal EGFP-His10 tag (3C site)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Hypotonic lysis | — | 20 mM HEPES pH 7.5, 1 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/), protease inhibitors |  |
| Solubilization | Detergent solubilization | — | 20 mM HEPES pH 7.5, 500 mM NaCl, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), protease inhibitors + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.06% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) |  |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA agarose | 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 20 mM HEPES pH 7.5, 500 mM NaCl, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |  |
| Anti-FLAG [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Anti-FLAG M1 resin | 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 20 mM HEPES pH 7.5, 300 mM NaCl, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 2 mM CaCl2 | Supplemented Ni-NTA eluent with 2 mM CaCl2 before loading |


## Crystallization

### doi/10.1038##s41586-018-0504-5

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein-to-lipid ratio | 2:3 |
| Temperature | 20°C |

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Temperature | 20°C |


## Biological / Functional Insights

### Structural basis of anion selectivity

Both iC++ and [GtACR1 Anion Channelrhodopsin from Guillardia theta](/xray-mp-wiki/proteins/rhodopsins/gtacr1/) structures revealed that anion selectivity is governed by pore-surface electrostatics rather than specific residue interactions. Positively charged residues lining the extracellular and intracellular surfaces create an electropositive pore that favors anion conduction. Reverse engineering of [GtACR1 Anion Channelrhodopsin from Guillardia theta](/xray-mp-wiki/proteins/rhodopsins/gtacr1/) to conduct cations confirmed this model.

### pH-dependent chromophore occupancy

iC++ exhibited reduced all-trans-[Retinal](/xray-mp-wiki/reagents/ligands/retinal/) occupancy at alkaline pH (8.5) compared to pH 6.5. The Schiff base is deprotonated and ATR is hydrolyzed at pH values above 7.5, consistent with reduced dACR activity at alkaline pH. The E129Q and E162S mutations destabilize the Schiff base, enabling ATR hydrolysis.

### Extracellular constriction sites

Two extracellular vestibules (EV1 and EV2) with constriction sites (ECS1 and ECS2) regulate ion access to the central pore. In iC++, the E140S mutation breaks a hydrogen bond with Gln95, allowing EV1 to extend to the central constriction site (CCS), while EV2 is occluded at ECS2 by Arg156-Arg281 interactions.

### Design of FLASH (fast light-activated anion-selective rhodopsin)

Structure-guided engineering of [GtACR1 Anion Channelrhodopsin from Guillardia theta](/xray-mp-wiki/proteins/rhodopsins/gtacr1/) produced FLASH ([GtACR1 Anion Channelrhodopsin from Guillardia theta](/xray-mp-wiki/proteins/rhodopsins/gtacr1/)(R83Q/N239Q)), which combines large photocurrents with fast kinetics for optogenetic single-spike inhibition. FLASH showed more efficient net inhibition of spontaneous spiking than ZipACR in vivo in mouse hippocampus and thalamus.


## Cross-References

- [Channelrhodopsin C1C2](/xray-mp-wiki/proteins/rhodopsins/channelrhodopsin-c1c2/) — iC++ is derived from C1C2 via 10 structure-guided mutations
- [Channelrhodopsin Photocycle](/xray-mp-wiki/concepts/channelrhodopsin-photocycle/) — iC++ photocycle includes K, M, and O intermediates
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [GtACR1 Anion Channelrhodopsin from Guillardia theta](/xray-mp-wiki/proteins/rhodopsins/gtacr1/) — Related protein structure
- [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Additive used in purification or crystallization buffers
- [EDTA](/xray-mp-wiki/reagents/additives/edta/) — Additive used in purification or crystallization buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [Sodium Phosphate](/xray-mp-wiki/reagents/buffers/sodium-phosphate/) — Buffer component in purification or crystallization
