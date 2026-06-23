---
title: "Human Aquaporin 5 (AQP5)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.0801466105]
verified: false
---

# Human Aquaporin 5 (AQP5)

## Overview

Human Aquaporin 5 (HsAQP5) is a water-selective channel protein belonging to the aquaporin family of major intrinsic proteins (MIPs). AQP5 is primarily expressed in salivary glands, lacrimal glands, lungs, and sweat glands, where it facilitates water transport across epithelial cell membranes. The high-resolution X-ray structure of HsAQP5 was determined at 2.0 A resolution, revealing a tetrameric assembly with each protomer forming an independent water channel. The structure was solved in the presence of near-perfect pseudomerohedral twinning (46.3% twin fraction), requiring specialized refinement using SHELXL. The structure displays the canonical aquaporin fold with six transmembrane helices and two half-helices containing the conserved NPA (Asn-Pro-Ala) motifs, and reveals a short C-terminal helix that shows conformational flexibility between protomers. Potential phosphorylation sites in loop B, loop D, and the C-terminal region suggest mechanisms for channel regulation.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.0801466105 | 3D9S | 2.0 | P2(1)2(1)2(1) (non-tagged construct); P312 (His-tagged construct) | Full-length human AQP5 expressed in Pichia pastoris without affinity tag; His-tagged construct also produced for validation | Water molecules; NG (n-nonyl-beta-D-glucopyranoside) detergent |

## Expression and Purification

- **Expression system**: Pichia pastoris
- **Construct**: Full-length HsAQP5 (cDNA from IMAGE clone 5269384) subcloned into pPICZB via EcoRI/NotI with extra serine after start codon; amino acid numbering starts with Met-0
- **Notes**: Expressed in buffered glycerol complex medium, induced with buffered methanol complex medium at OD600=1; 0.5% methanol added every 24 h for 75 h

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Bead beating and ultracentrifugation | -- | Breaking buffer (50 mM NaH2PO4, 1 mM EDTA, 5% glycerol, 1 mM PMSF) + -- | Cells broken with Bead Beater (Bio Spec) using 200 ml glass beads (0.5 mm diameter), 12 x 30 s runs with 30 s cooling. Debris removed by 2 x 30 min at 1400 x g; membranes pelleted at 186,000 x g for 2 h. ~400 mg crude membrane protein/L culture recovered. |
| Urea/alkali wash | Peripheral protein removal | -- | Buffer A (20 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/)-NaOH pH 7.8, 50 mM NaCl, 10% glycerol, 2 mM [beta-mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/)) + -- | Urea/alkali wash according to Fotiadis et al. (2001); centrifugation extended to 1.5 h; pellet briefly washed with ddH2O after NaOH treatment |
| Solubilization | Detergent solubilization | -- | 20 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.8, 50 mM NaCl, 10% glycerol, 2 mM beta-MeOH + 6% [NG (n-nonyl-beta-D-glucopyranoside)](/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/) | Solubilization screen identified NG and OTG (n-octyl-beta-D-thioglucopyranoside) as suitable detergents. Membranes (~30 mg protein) diluted dropwise with equal volume of solubilization buffer, stirred 1 h at RT. Nonsolubilized material removed at 140,000 x g for 30 min at 4 C. |
| Cation exchange chromatography | Ion exchange chromatography | Resource S (GE Healthcare) | 20 mM [MES](/xray-mp-wiki/reagents/buffers/mes/) pH 6.0, 15-500 mM NaCl gradient + 0.4% NG | Supernatant diluted 1:3 with 20 mM MES pH 6.0, 10% glycerol, 2 mM beta-MeOH, 0.4% NG; pH adjusted to 6.0. Applied to Resource S column equilibrated with 20 mM MES pH 6.0, 15 mM NaCl, 0.4% NG. Eluted with gradient 15-500 mM NaCl at 1 ml/min. Fractions concentrated to <0.5 ml using Vivaspin 20 concentrator. |


## Crystallization

### doi/10.1073##pnas.0801466105

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | Purified HsAQP5 in detergent (non-tagged construct for P2(1)2(1)2(1) crystals; His-tagged construct for P312 crystals) |
| Reservoir | Not specified in available raw text (crystallization conditions in main text not available) |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified in available text |
| Notes | Non-tagged HsAQP5 crystallized in space group P2(1)2(1)2(1); His-tagged HsAQP5 crystallized in space group P312. Structure exhibited near-perfect pseudomerohedral twinning (46.3% twin fraction) with twin operator (0 1 0 1 0 0 0 0 -1) swapping a and b axes. Refinement performed using SHELXL. 3.0 A partially twinned data (twin fraction 13%) from His-tagged crystals used for validation. Data collected at 2.0 A (twinned). Full omit maps calculated using CNS model_map.twin script. |


## Biological / Functional Insights

### Tetrameric water channel architecture conserved in human AQP5

HsAQP5 forms a tetramer with each protomer containing an independent water channel. The structure displays the canonical aquaporin fold of six transmembrane helices and two half-helices (the NPA motif regions) forming the water-selective pore. The tetrameric assembly is typical of the aquaporin family. HOLE calculations of pore radii for the four protomers show similar profiles compared with BtAQP1.

### Short C-terminal helix exhibits conformational flexibility

A notable feature of HsAQP5 is a short C-terminal helix that shows conformational differences between protomers in the tetramer. This flexibility may be functionally relevant for channel regulation, as the C-terminal region contains potential phosphorylation sites (cAMP/cGMP-dependent protein kinase A sites, protein kinase C sites, and casein kinase II sites) identified by PROSCAN/PROSITE searches. The C-terminal helix of AQP5 differs in length and angle compared to BtAQP1 and OaAQP0.

### Potential phosphorylation sites in regulatory loops

Sequence analysis of HsAQP5 reveals potential phosphorylation sites in loop B, loop D, and the C-terminal region. These include cAMP- and cGMP-dependent protein kinase A sites (RKX[ST] motif), protein kinase C sites ([ST]X[RK] motif), and casein kinase II sites ([ST]XX[DE] motif). Phosphorylation of corresponding sites in the plant aquaporin SoPIP2;1 and mouse AQP4 has been shown to regulate channel gating, suggesting that similar regulatory mechanisms may operate in HsAQP5.

### Pseudomerohedral twinning in AQP5 crystals

The HsAQP5 structure was refined from crystals exhibiting near-perfect pseudomerohedral twinning (twin fraction 46.3%) with the twin operator swapping the a and b axes. Specialized refinement using SHELXL was employed, with test reflections selected in thin resolution shells to avoid biasing Rfree. A full omit map procedure (Artymiuk et al.) was developed to produce less biased electron density maps, involving dividing the asymmetric unit into boxes, omitting each in turn for detwinning and map calculation, then merging.

### Functional water transport and mercury inhibition

HsAQP5 reconstituted into proteoliposomes demonstrates water transport activity by stopped-flow light scattering. Rate constants of 21.32 s-1 (LPR 65) and 14.10 s-1 (LPR 130) were measured, compared to 9.14 s-1 for control liposomes. Water transport was inhibited by HgCl2 with an IC50 of 30 uM, and inhibition was reversed by 0.5 mM beta-mercaptoethanol.


## Cross-References

- [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) — AQP5 is a member of the water-specific aquaporin subfamily; the structure reveals conserved aquaporin features including NPA motifs and tetrameric assembly
- [Aquaporin 0 (AQP0)](/xray-mp-wiki/proteins/other-ion-channels/aqp0/) — Related aquaporin for structural comparison of tetramer architecture and water selectivity
- [Aquaporin-1 (AQP1)](/xray-mp-wiki/proteins/other-ion-channels/aqp1/) — Archetypal water-specific aquaporin with similar pore architecture used for HOLE pore radius comparison
- [n-Nonyl-beta-D-glucopyranoside (NG)](/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/) — Primary detergent used for solubilization and purification of HsAQP5
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — HEPES-NaOH pH 7.8 used in membrane preparation buffer A and solubilization buffer
- [MES Buffer](/xray-mp-wiki/reagents/buffers/mes/) — MES pH 6.0 used as cation exchange column equilibration and binding buffer
- [Ion Exchange Chromatography](/xray-mp-wiki/methods/purification/ion-exchange-chromatography/) — Resource S cation exchange used as the main purification step for AQP5
- [Pseudomerohedral Twinning](/xray-mp-wiki/concepts/pseudomerohedral-twinning/) — HsAQP5 structure refined from crystals with near-perfect pseudomerohedral twinning (46.3%) using SHELXL
