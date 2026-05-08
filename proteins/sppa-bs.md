---
title: Signal Peptide Peptidase A from Bacillus subtilis (SppA_BS)
created: 2026-05-07
updated: 2026-05-07
type: protein
category: proteins
layout: default
tags: [membrane-protease, serine-protease, oligomeric-protease, gram-positive]
sources: [doi/10.1016##j.jmb.2012.03.020]
---

# Signal Peptide Peptidase A from Bacillus subtilis (SppA_BS)

## Overview

Signal Peptide Peptidase A from Bacillus subtilis (SppA_BS) is a membrane-bound self-compartmentalized serine protease that functions to cleave remnant signal peptides left behind after protein secretion. The catalytic domain assembles into a dome-shaped octameric complex with eight separate active sites, each formed at the interface between neighboring protomers. The catalytic mechanism involves a Ser147 nucleophile and Lys199 general base that come into proximity only upon octamer assembly.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2012.03.020 | NOT_DEPOSITED | 2.4 A | P2_12_12_1 | SppA_BS Delta1-25 K199A with thermolysin-resistant fragment (residues 57-295) | -- |

## Expression and Purification

- **Expression system**: E. coli Tuner (DE3)
- **Construct**: SppA_BS Delta1-25 K199A in pET28b+ with N-terminal 6xHis tag and thrombin site (MGSSHHHHHHSSGLVPRGSH)

### Purification Workflow

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell disruption | Sonication and cell homogenization | -- | 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/)-HCl pH 8.0, 150 mM NaCl | Membrane fractions collected by ultracentrifugation at 30,000g for 35 min |
| Affinity chromatography | Metal affinity chromatography (Ni-NTA) | Ni-NTA | 20 mM Tris-HCl pH 8.0, 150 mM NaCl, 100-600 mM imidazole gradient | Washed with 50 and 75 mM imidazole; eluted with 100-600 mM imidazole |
| Dialysis | Dialysis | -- | 20 mM Tris-HCl pH 8.0, 150 mM NaCl | Overnight at 4 C to remove imidazole |
| Concentration | Ultrafiltration | -- | 20 mM Tris-HCl pH 8.0, 150 mM NaCl | Concentrated to 10 mg/mL using Amicon 10-kDa cutoff filter |


## Crystallization

No crystallization described.

## Biological / Functional Insights

### Octameric dome structure

SppA_BS catalytic domain forms a dome-shaped octameric complex with eight separate active sites, each formed at the protein-protein interface. Three neighboring protomers are required to assemble one complete catalytic unit. The catalytic Ser147 nucleophile arrives from one protomer and the Lys199 general base from an adjacent protomer.

### Ser/Lys catalytic dyad

The catalytic mechanism involves Ser147 as the nucleophile and Lys199 as the general base. These residues are more than 29 A apart in the monomer but come within hydrogen bonding distance upon octamer assembly. The oxyanion hole is formed by Gly114 and Gly148, and Ser169 helps coordinate the lysine general base.


## Cross-References

- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Crystallization detergent (0.1% final)
- [2-Methyl-2,4-pentanediol (MPD)](/xray-mp-wiki/reagents/additives/mpd/) — Cryoprotectant and crystallization additive (5% in reservoir, 20% in cryosolvent)
- [Limited Proteolysis](/xray-mp-wiki/methods/limited-proteolysis/) — Used to generate proteolytically resistant fragment for crystallization
