---
title: Human Aquaporin 1 (hAQP1)
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1107##s2053230x14024558]
verified: false
---

# Human Aquaporin 1 (hAQP1)

## Overview

Human [Aquaporin Family](/xray-mp-wiki/concepts/aquaporin/) 1 (hAQP1) is the archetypal water-selective channel from the
[Aquaporin Family](/xray-mp-wiki/concepts/aquaporin/), originally discovered in red blood cells and renal proximal
tubules. It forms homotetrameric channels that transport water bidirectionally
in response to osmotic gradients, strictly excluding ions including protons.
hAQP1 is a key factor in cell migration and angiogenesis and constitutes a
possible target for anticancer compounds and glaucoma treatment. A
preliminary crystallographic analysis at 3.28 A resolution was obtained from
protein expressed in Sf9 insect cells (the first recombinant hAQP1
structure). Crystals belong to the tetragonal space group I422 with
unit-cell parameters a = b = 89.28, c = 174.9 A and one monomer per
asymmetric unit; the biological tetramer is generated via the
crystallographic fourfold axis. This extends previous electron
crystallographic studies of hAQP1 from human red blood cells which were
limited to approximately 3.8 A resolution. A 2.2 A crystal structure of the
closely related bovine [Aquaporin Family](/xray-mp-wiki/concepts/aquaporin/) 1 (bAQP1, PDB 1j4n) had previously been
solved from bovine red blood cells.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1107##s2053230x14024558 | -- | 3.28 | I422 | Full-length human [AQP1](/xray-mp-wiki/proteins/other-ion-channels/aqp1/) (residues 1-269) with N-terminal 6xHis tag and TEV cleavage site, expressed in Sf9 insect cells |  |

## Expression and Purification

- **Expression system**: Spodoptera frugiperda Sf9 insect cells (baculovirus expression system)
- **Construct**: hAQP1 gene cloned into pFB-Lic-Bse vector with N-terminal 6xHis tag and TEV protease cleavage site
- **Notes**: Early passage virus (P0 amplified to P2). MOI 2-3, 27 C, 56 h, 140 rpm. 21 log-phase culture (3x10^6 cells/mL).

### Purification Workflow

- **Expression system**: S. frugiperda Sf9
- **Expression construct**: 6xHis-tagged hAQP1 with TEV cleavage site
- **Tag info**: N-terminal 6xHis tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell harvest | Centrifugation | — |  | 1500g for 30 min; pellet washed twice with PBS |
| Cell lysis | Sonication | — | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8, 300 mM NaCl, 2 mM [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), cOmplete protease inhibitor cocktail, benzonase, 2% OG | 10 min sonication |
| Membrane solubilization | Solubilization | — | 2% n-octyl-beta-D-glucopyranoside (OG) | Insoluble material removed by centrifugation |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | — |  | His-tagged hAQP1 purified by Ni-NTA |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | SEC | — |  | hAQP1 elutes at 72 mL corresponding to homotetramer |

**Final sample**: Purified tetrameric hAQP1 in OG


## Crystallization

### doi/10.1107##s2053230x14024558

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (hanging drop) |
| Protein sample | Purified hAQP1 tetramer in OG |
| Temperature | 293 K (room temperature) |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Tetragonal-shaped crystals. Anisotropic diffraction - strong to 3.3 A along c*, weak beyond 6 A in perpendicular directions. Significant diffuse scattering observed. Space group I422. Data collected at PXIII, SLS-PSI, PILATUS 2M detector, 110 K, 410 mm crystal-to-detector distance. 120 total rotation, 1 per image, 4 s exposure per image. |


## Biological / Functional Insights

### First recombinant hAQP1 crystal structure

This work reports the first crystal structure of human [Aquaporin Family](/xray-mp-wiki/concepts/aquaporin/) 1 obtained from recombinant protein expressed in Sf9 insect cells, extending previous electron crystallographic studies (limited to ~3.8 A) that used native hAQP1 extracted from human red blood cells. The recombinant expression system enables mutagenesis studies and structure-based drug discovery targeting hAQP1.

### Comparison of hAQP1 and bAQP1 crystal packing

The crucial difference between hAQP1 and bAQP1 (bovine [AQP1](/xray-mp-wiki/proteins/other-ion-channels/aqp1/), PDB 1j4n) lattices is the presence of an additional ~400 A2 packing interface in bAQP1 established between the N-terminal region of one tetramer and the C-terminal region of a dyad-related tetramer, stabilized by six hydrogen bonds. This interface is absent in hAQP1 due to disorder of the C-terminal polypeptide chain, leading to a slight tilt of the hAQP1 tetramer compared to bAQP1. The hAQP1 tetramer is formed via crystallographic fourfold axis. Contacts between head-to-tail tetramers are limited to arginine-rich loops 158-162 brought into proximity via a crystallographic dyad.


## Cross-References

- [Aquaporin Family](/xray-mp-wiki/concepts/aquaporin/) — hAQP1 is the founding member of the aquaporin water channel family
- [Aquaporin Z (AqpZ)](/xray-mp-wiki/proteins/other-ion-channels/aquaporin-z/) — Bacterial homolog of hAQP1; structural comparison for water selectivity
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Method used in structure determination or purification
- [AQP1](/xray-mp-wiki/proteins/other-ion-channels/aqp1/) — Related protein structure
- [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/) — Additive used in purification or crystallization buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component in purification or crystallization
