---
title: Human Nav1.7 Voltage-Gated Sodium Channel
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.aac5464]
verified: false
---

# Human Nav1.7 Voltage-Gated Sodium Channel

## Overview

Nav1.7 (encoded by SCN9A) is a voltage-gated sodium channel isoform highly expressed in peripheral nervous system neurons, particularly in dorsal root ganglion and olfactory epithelium. It plays a central role in pain perception: gain-of-function mutations cause extreme pain disorders, while loss-of-function mutations cause congenital insensitivity to pain. Nav1.7 is a validated target for analgesic drug development. The first X-ray crystal structure of the Nav1.7 VSD4 (voltage-sensor domain IV) was determined as a chimera fused onto the bacterial [NAVAB](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) channel, revealing the binding mode of isoform-selective aryl sulfonamide antagonists that trap VSD4 in an activated conformation.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.aac5464 | N/A (not explicitly stated in paper) | 3.53 | — | Nav1.7 VSD4-[NAVAB](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) chimeric channel — human Nav1.7 VSD4 (S1-S4, residues 1525-1625) grafted onto bacterial [NAVAB](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) channel scaffold | [GX-936](/xray-mp-wiki/reagents/ligands/gx-936/) (aryl sulfonamide antagonist) |
| doi/10.1126##science.aac5464 | N/A (not explicitly stated in paper) | 3.85 | — | Nav1.7 VSD4-[NAVAB](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) with GX-629 (brominated analog for SAD phasing) | GX-629 |
| doi/10.1126##science.aac5464 | N/A (not explicitly stated in paper) | 4.35 | — | Nav1.7 VSD4-[NAVAB](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) (selenomethionine-incorporated, 5 Met landmarks) | [GX-936](/xray-mp-wiki/reagents/ligands/gx-936/) |

## Expression and Purification

- **Expression system**: HEK293 cells (mammalian expression)
- **Construct**: Nav1.7 VSD4-[NAVAB](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) chimera with grafted human Nav1.7 VSD4 residues (S1-S4, residues 1525-1625)
- **Notes**: Exploiting evolutionary relationship between human and bacterial Nav channels. The chimera preserved high-affinity antagonist binding as confirmed by radioligand binding and alanine-scanning mutagenesis.

### Purification Workflow

- **Expression system**: HEK293 cells
- **Expression construct**: Nav1.7 VSD4-[NAVAB](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) chimeric protein

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and expression | Transient transfection of HEK293 cells | — |  | Protein production for crystallization studies |
| Purification | Affinity and [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | Not specified in main text | Not specified in main text + Not specified in main text | Standard membrane protein purification protocol |


## Crystallization

### doi/10.1126##science.aac5464

| Parameter | Value |
|---|---|
| Method | [Bicelle Crystallization](/xray-mp-wiki/methods/crystallization/bicelle-crystallization/) |
| Protein sample | Nav1.7 VSD4-[NAVAB](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) chimera |
| Temperature | 4 |
| Cryoprotection | Not specified |
| Notes | Crystals grown from PC-based bicelle system. [GX-936](/xray-mp-wiki/reagents/ligands/gx-936/), GX-629, or GX-674 included for cocrystallization. Data collected at Br absorption edge (0.9199 A) for SAD phasing with GX-629. SeMet protein used for landmarking. |


## Biological / Functional Insights

### Aryl sulfonamides trap Nav1.7 VSD4 in activated state via voltage-sensor trapping mechanism

[GX-936](/xray-mp-wiki/reagents/ligands/gx-936/) and related aryl sulfonamide antagonists bind to VSD4 only when the voltage-sensor domain is in its activated conformation (depolarized membrane potential). The anionic aryl sulfonamide warhead directly engages the R4 gating charge (R1608) through a bidentate salt bridge, effectively trapping VSD4 in the activated state. This prevents VSD4 deactivation, stabilizes inactivated channel states, and thereby inhibits Nav1.7 with extreme state dependence (IC50 0.1 nM at -40 mV vs 240 nM at -120 mV).

### Isoform selectivity determined by S2 and S3 helix residues

Isoform selectivity of aryl sulfonamide inhibitors is achieved through interactions with nonconserved residues on the S2 and S3 helices of VSD4. Key selectivity motifs were identified: YWxxV on S2 (Y1537, W1538) and GMxxA on S3 (G1581, M1582, A1585). The selectivity pocket distinguishes Nav1.7 from other isoforms like Nav1.5 (cardiac) where GX-674 shows 100,000-fold selectivity.

### Phospholipids form a tripartite complex with antagonist and VSD4

Bound [Phosphatidylcholine](/xray-mp-wiki/reagents/lipids/phosphatidylcholine/) (PC) molecules were observed in the structure, with one lipid (PC2) directly buttressing the [GX-936](/xray-mp-wiki/reagents/ligands/gx-936/) binding site. This peripherally bound lipid covers ~200 A^2 of [GX-936](/xray-mp-wiki/reagents/ligands/gx-936/) surface and forms specific interactions with S2 and S3 helix residues (E1534 and D1586). The observation of a lipid-antagonist-VSD4 ternary complex suggests that membrane lipids can directly modulate the VSD4 receptor site.

### VSD chimeric engineering strategy for crystallography

A novel protein-engineering strategy was devised by exploiting the evolutionary relationship between human and bacterial Nav channels. The human Nav1.7 VSD4 (S1-S4) was grafted onto the bacterial [NAVAB](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) channel scaffold, creating a functional chimeric channel that preserved the antagonist binding site. This approach overcame the technical complexity of producing full-length human Nav channels for crystallographic studies.


## Cross-References

- [GX-936](/xray-mp-wiki/reagents/ligands/gx-936/) — Co-crystallized aryl sulfonamide antagonist that traps Nav1.7 VSD4 in activated state
- [Bicelle Crystallization](/xray-mp-wiki/methods/crystallization/bicelle-crystallization/) — Method used in structure determination or purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Method used in structure determination or purification
- [NAVAB](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) — Related protein structure
- [Phosphatidylcholine](/xray-mp-wiki/reagents/lipids/phosphatidylcholine/) — Additive used in purification or crystallization buffers
