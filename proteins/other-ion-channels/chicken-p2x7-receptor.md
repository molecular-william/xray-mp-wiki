---
title: Chicken P2X7 Receptor (ckP2X7)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-017-00887-9]
verified: false
---

# Chicken P2X7 Receptor (ckP2X7)

## Overview

The P2X7 receptor is an [ATP](/xray-mp-wiki/reagents/ligands/atp/)-gated non-selective cation channel belonging to the P2X receptor family, which plays a crucial role in the immune and nervous systems. It is mainly expressed in immune cells including macrophages and lymphocytes, where its activation stimulates the release of proinflammatory cytokines. The chicken P2X7 receptor (ckP2X7) structure was determined in complex with the competitive antagonist TNP-[ATP](/xray-mp-wiki/reagents/ligands/atp/), revealing an expanded, incompletely activated conformation distinct from both the apo closed and [ATP](/xray-mp-wiki/reagents/ligands/atp/)-bound open states. TNP-[ATP](/xray-mp-wiki/reagents/ligands/atp/) acts as a wedge, with its trinitrophenyl group inserted between the head and dorsal fin domains to prevent the complete cleft closure motion required for channel activation. The structure provides mechanistic insights into competitive antagonist action and facilitates interpretation of disease-associated SNPs in the human P2X7 receptor.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-017-00887-9 | 5XW6 | 3.1 | P4(1)2(1)2 | Chicken P2X7 crystallization construct (ckP2X7_cryst) with N-terminal GFP-His8 tag (removed by TEV cleavage) and Endo H deglycosylation, in complex with TNP-[ATP](/xray-mp-wiki/reagents/ligands/atp/) | TNP-[ATP](/xray-mp-wiki/reagents/ligands/atp/) |

## Expression and Purification

- **Expression system**: HEK293S GnTI(-)
- **Construct**: Chicken P2X7 (NCBI XP_001235163) expressed in HEK293S GnTI- cells via [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) BacMam vector with N-terminal GFP-His8 tag, TEV cleavage site, and GSGS linker

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Sonication | -- | 50 mM [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl + -- | Supplemented with aprotinin, leupeptin, and pepstatin A |
| Membrane collection | Ultracentrifugation | -- | -- + -- | 138,000 x g, 1 h, 4°C |
| Membrane solubilization | Detergent solubilization | -- | 50 mM [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 2 mM CaCl2, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 2% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | 1 h at 4°C; 0.2 U/mL apyrase added |
| Affinity purification | [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon/) metal affinity chromatography | [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon/) (Co2+) | 50 mM [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Washed with 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), eluted with 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Tag removal and deglycosylation | Enzymatic digestion | -- | -- + -- | TEV protease digestion and Endo H treatment |
| Size-exclusion chromatography | SEC | Superdex 200 Increase 10/300 GL | 20 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.0, 100 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Final purification step |


## Crystallization

### doi/10.1038##s41467-017-00887-9

| Parameter | Value |
|---|---|
| Method | Co-crystallization |
| Protein sample | Purified ckP2X7_cryst in 20 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.0, 100 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Reservoir | 20% [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) 3350, 0.2 M sodium-potassium phosphate, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |
| Temperature | 20 |
| Growth time | -- |
| Cryoprotection | Crystals flash-cooled in liquid nitrogen |
| Notes | Co-crystallized with TNP-[ATP](/xray-mp-wiki/reagents/ligands/atp/). X-ray data collected at 100 K at beamline X06SA-PXI (SLS). Structure solved by molecular replacement using the amP2X structure (PDB 4DW0) as search model. |


## Biological / Functional Insights

### TNP-ATP wedge mechanism of competitive inhibition

The TNP-[ATP](/xray-mp-wiki/reagents/ligands/atp/)-bound ckP2X7 structure reveals an incompletely activated conformation where the trinitrophenyl group of TNP-[ATP](/xray-mp-wiki/reagents/ligands/atp/) inserts between the head and dorsal fin domains, acting as a wedge that prevents the complete cleft closure motion required for channel activation. Molecular dynamics simulations showed that removal of the trinitrophenyl group allowed the head domain to undergo the downward movement characteristic of [ATP](/xray-mp-wiki/reagents/ligands/atp/)-dependent activation. This wedge mechanism explains how TNP-[ATP](/xray-mp-wiki/reagents/ligands/atp/) acts as a competitive antagonist — it occupies the [ATP](/xray-mp-wiki/reagents/ligands/atp/) binding pocket and sterically blocks the conformational changes needed for channel opening, with the phosphate groups adopting a fully extended conformation that forms unique interactions with Lys236 and Lys298.

### Structural mapping of disease-associated P2X7 SNPs

Mapping of human P2X7 receptor SNPs onto the ckP2X7 structure revealed that loss-of-function substitutions are located exclusively in the extracellular domain and cluster within secondary structure regions, suggesting they affect the structural integrity of the inactivated state. Gain-of-function substitutions are observed in both extracellular and transmembrane domains. Notably, substitution Leu196Pro (human; corresponding to ckPhe179) associated with affective mood disorder maps to the TNP-[ATP](/xray-mp-wiki/reagents/ligands/atp/) binding pocket without forming direct hydrogen bonds, while Ala348Thr (toxoplasmosis) and Thr357Ser (bipolar disorder) map near the pore constriction site in the transmembrane domain.


## Cross-References

- [TNP-ATP](/xray-mp-wiki/reagents/ligands/tnp-atp/) — Competitive antagonist co-crystallized with ckP2X7; key to understanding inhibition mechanism
- [Zebrafish P2X4 Receptor (zfP2X4)](/xray-mp-wiki/proteins/other-ion-channels/zfp2x4/) — Related P2X family receptor structure used for comparison
- [Human P2X3 Receptor (hP2X3)](/xray-mp-wiki/proteins/other-ion-channels/human-p2x3-receptor/) — TNP-ATP-bound hP2X3 structure compared with ckP2X7; different binding modes
- [P2X Receptor Family](/xray-mp-wiki/concepts/signaling-receptors/p2x-receptor-family/) — ckP2X7 belongs to the P2X receptor family of ATP-gated ion channels
- [Dodecylmaltoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for solubilization and purification
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — 20 mM HEPES pH 7.0 used in SEC and crystallization buffers
- [Tris Buffer](/xray-mp-wiki/reagents/buffers/tris/) — 50 mM Tris pH 8.0 used in solubilization and affinity purification buffers
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Phasing method for structure determination using amP2X model
- [GR (Halobacterium sp. GR Bacteriorhodopsin)](/xray-mp-wiki/proteins/rhodopsins/gr/) — Related protein structure
- [Zebrafish P2X4 Receptor (zfP2X4)](/xray-mp-wiki/proteins/other-ion-channels/zfp2x4/) — Related protein structure
