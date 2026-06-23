---
title: "YeeE Thiosulfate Transporter from Shewanella thermophila"
created: 2026-06-10
updated: 2026-06-10
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1126##sciadv.aba7637]
verified: false
---

# YeeE Thiosulfate Transporter from Shewanella thermophila

## Overview

YeeE is a bacterial membrane protein that mediates thiosulfate uptake for use as an inorganic sulfur source in cysteine synthesis. The crystal structure of YeeE from Shewanella thermophila at 2.5 Å resolution reveals an unprecedented hourglass-like architecture with an intramolecular pseudo 222 symmetry fold. YeeE is composed of 13 helices including 9 transmembrane α helices, with four characteristic loops (LA-LD) buried toward the center forming a constricted pathway. Three conserved cysteine residues (C22, C91, C293) along the pathway are essential for thiosulfate transport activity.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##sciadv.aba7637 | 6LEO | 2.52 | C2221 | StYeeE(1-328)-GSSGENLYFQFTS-H8 (WT) | Thiosulfate |
| doi/10.1126##sciadv.aba7637 | 6LEP | 2.60 | C2221 | StYeeE(1-328)-GSSGENLYFQFTS-H8 (C91A mutant) | — |

## Expression and Purification

- **Expression system**: E. coli C41 (DE3) heterologous expression

- **Construct**: Full-length StYeeE(1-328) with C-terminal GSSGENLYFQFTS-H8 tag, in modified pCGFP-BC vector (pKK550)

- **Induction**: 1 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at OD600=0.8, 37°C for 15 hours

- **Media**: LB Broth (Lennox) with 50 μg/ml [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/)


### Purification Workflow

- **Expression system**: E. coli C41 (DE3)
- **Expression construct**: StYeeE(1-328)-GSSGENLYFQFTS-H8
- **Tag info**: C-terminal H8 tag, removed by TEV(S219V) protease cleavage

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell harvesting and lysis | Microfluidizer | — | 10 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 1 mM EDTA-Na pH 8.0, 0.1 mM PMSF | Three passes at 15,000 psi |
| Membrane isolation | Differential centrifugation | — |  | 22,500g for 30 min (remove debris), then 140,000g for 60 min (pellet membranes) |
| Membrane solubilization | Detergent extraction | — | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 300 mM NaCl, 0.1 mM PMSF, 1 mM β-ME, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) pH 8.0 + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Resuspend and rotate for 45 min at 4°C, then ultracentrifuge at 140,000g for 30 min |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA | Ni-NTA agarose (Qiagen) | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 300 mM NaCl, 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Equilibrate with 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), wash with 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), stepwise elution with 40, 60, 100, 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Tag cleavage | TEV protease digestion | — | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 300 mM NaCl + 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | TEV(S219V) protease at 10:1 molar ratio (YeeE:TEV), dialysis against cleavage buffer |

**Final sample**: Purified YeeE in 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 300 mM NaCl, 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/)


## Crystallization

### doi/10.1126##sciadv.aba7637

| Parameter | Value |
|---|---|
| Method | — |
| Temperature | — |
| Growth time | — |
| Notes | Crystal structure determined at 2.5 Å resolution using SIRAS phasing with SeMet-substituted protein from 326 merged crystals. Data collected at SPring-8 BL32XU. Native structure from 515 merged crystals. C91A mutant from 93 merged crystals. Structure shows alternative conformations from oxidized/reduced forms between C22 and C91.
 |


## Biological / Functional Insights

### Intramolecular pseudo 222 symmetry fold

YeeE adopts a previously unknown fold with 13 helices (H1-H13) including 9 transmembrane α helices. The structure exhibits intramolecular pseudo 222 symmetry with four elements (H1-H3, H4-H6, H8-H10, H11-H13) assembled around three orthogonal pseudo dyad axes. Four characteristic loops (LA-LD) are buried toward the center of YeeE and form the central constricted region surrounded by the nine helices.

### Thiosulfate binding and transport mechanism

A thiosulfate ion is bound at position I on the positively charged periplasmic concave side, coordinated by hydrogen bonds to E241, K67, and C293. Three conserved cysteine residues (C22 in LA, C91 in LB, C293 in LD) are linearly located at ~7 Å intervals along the transport pathway. MD simulations suggest thiosulfate is transferred from position I to positions II and III via S-H-S hydrogen bonds between thiosulfate sulfur and cysteine thiol groups. The mechanism does not require large conformational changes in transmembrane helices, unlike rocking bundle or alternating access mechanisms.

### Thiosulfate versus sulfate selectivity

YeeE transports thiosulfate (S2O3^2-) but not sulfate (SO4^2-). The selectivity is explained by the S-H-S hydrogen bond relay mechanism requiring an exposed sulfur atom on the substrate. Sulfate's sulfur atom is shielded by four oxygen atoms, preventing interaction with the conserved cysteine residues. This selectivity makes thiosulfate a preferred sulfur source for cysteine synthesis.


## Cross-References

- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [IPTG](/xray-mp-wiki/reagents/additives/iptg/) — Additive used in purification or crystallization buffers
- [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/) — Antibiotic used in selection
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component in purification or crystallization
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used in purification or crystallization
