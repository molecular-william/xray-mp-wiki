---
title: HiTehA (TehA from Haemophilus influenzae)
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature09487]
verified: false
---

# HiTehA (TehA from Haemophilus influenzae)

## Overview

HiTehA is the TehA anion channel protein from Haemophilus influenzae. It is a bacterial homologue of the plant SLOW ANION CHANNEL 1 (SLAC1) and functions as an anion-selective channel. HiTehA forms a symmetrical trimer, with each protomer containing ten transmembrane helices arranged from five helical hairpin pairs to create a central five-helix transmembrane pore. The pore is gated by a highly conserved phenylalanine residue (Phe 262). The structure was solved by selenomethionyl (SeMet) single-wavelength anomalous dispersion (SAD) phrasing at 1.20 Å resolution, providing key insights into anion channel gating, selectivity, and the structural basis of the SLAC1 superfamily.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature09487 | Not specified in paper text | 1.20 A | R3 | Full-length TehA from Haemophilus influenzae (residues 6-313) | 4 detergent molecules (beta-octylglucoside) |

## Expression and Purification

- **Expression system**: Escherichia coli BL21(DE3) plysB
- **Construct**: Flag and deca-histidine (His6) tag fusion at C terminus, cleavable by TEV protease
- **Notes**: High-throughput format (0.6 ml in deep-well block); expressed from genomic DNA PCR clones

### Purification Workflow

- **Expression system**: Escherichia coli BL21(DE3) plysB
- **Expression construct**: Flag and deca-histidine tag fusion at C terminus
- **Tag info**: Flag and His6 tags, cleavable by TEV protease

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Sonication | — | N-dodecyl-beta-D-maltopyranoside (DDM) + 0.02% DDM | Metal affinity purification in buffer containing DDM |
| Analytical SEC screening | Size-exclusion chromatography | Analytical SEC column | 12 different detergent-containing mobile phases | Screened across 12 detergents to find stable conditions |

**Final sample**: HiTehA in beta-octylglucoside


## Crystallization

### doi/10.1038##nature09487

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | HiTehA in beta-octylglucoside |
| Reservoir | PEG600 or PEG400 as precipitant |
| Temperature | 4 C |
| Growth time | Not specified |
| Notes | Crystals diffracted beyond 1.1 A spacings; solved by SeMet SAD phrasing |


## Biological / Functional Insights

### Trimeric organization of HiTehA

HiTehA forms tight trimers with three-fold axes aligned to the crystal lattice. Subunits bury 8,947 A^2 of total surface area within trimer interfaces. The trimeric state was confirmed both by size-exclusion multi-angle light-scattering (SEC-MALS) measurements and by chemical cross-linking experiments. The electrostatic potential surface is largely negative on the extracellular surface and largely positive on the cytoplasmic surface, which likely contributes to anion efflux.

### Novel ten-helix transmembrane fold

Each HiTehA protomer has ten transmembrane helices arranged from five tandemly repeated helical hairpins with quasi-five-fold symmetry. Extracellular inter-helix loops are short (2-5 residues), whereas intracellular inter-helix connections are longer, including a nine-residue helix H2,3 between transmembrane helix 2 and helix 3. An inner pentad of outwardly directed odd-numbered transmembrane helices creates a pore through each protomer perpendicular to the membrane plane. Even-numbered helices from the five hairpins surround the inner pore as an outer layer.

### Phe 262 gate occluding the central pore

The central pore through each HiTehA protomer is occluded by the side chain of Phe 262 in the wild-type structure, which blocks ion conductance. The phenyl ring is in a high-energy conformation (chi1/chi2 at -160 degrees/-4 degrees), restricted by contacts with Val 210 and Leu 18. In the F262A mutant, the pore opens with a relatively uniform diameter of approximately 5 A across approximately 30 A through the membrane. The gating role of Phe 262 is conserved in SLAC1 as Phe 450.

### Proline kinks in pore helices

Four of the five HiTehA inner helices have centrally located proline residues that generate kinks, maintaining a relatively constant pore diameter across the membrane. TM9 is kinked at a backbone-coordinated water molecule. Proline replaces Gly 263 in all SF1A and SF1B relatives, including Pro 451 of AtSLAC1. Centrally located proline residues also prevail in TM3, TM5, and TM7 across SLAC1 superfamily proteins. The outer helices are longer and straighter but more inclined.

### Homology between HiTehA and AtSLAC1

Arabidopsis SLAC1 (AtSLAC1) is substantially similar to HiTehA with 19% sequence identity in the transmembrane domain (PSI-BLAST E-value 3 x 10^-22). All HiTehA transmembrane helices align to predicted SLAC1 transmembrane helices. SLAC1 shares 76% identity with rice SLAC1, 41% with Arabidopsis SLAH1, and lower identities with fungal homologues (11% with S. cerevisiae Ssu1, 9% with S. pombe Mae1). The HiTehA structure was used to build a homology model of AtSLAC1 that guided mutational analysis.


## Cross-References

- [SLAC1 (SLOW ANION CHANNEL 1 from Arabidopsis thaliana)](/xray-mp-wiki/proteins/slac1/) — HiTehA is the bacterial homologue of plant SLAC1; structure used for homology modeling
- [Anion Channel Gating via Phenylalanine Gate](/xray-mp-wiki/concepts/anion-channel-gating/) — Phe 262 in HiTehA (Phe 450 in SLAC1) is the conserved gating residue
- [n-Octyl beta-D-glucopyranoside (OG)](/xray-mp-wiki/reagents/detergents/og/) — Detergent used for HiTehA solubilization and crystallization
- [PEG 600](/xray-mp-wiki/reagents/additives/peg-600/) — Crystallization precipitant used for HiTehA
