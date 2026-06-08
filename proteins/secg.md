---
title: Thermus thermophilus SecG Accessory Subunit
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.celrep.2015.10.025]
verified: false
---

# Thermus thermophilus SecG Accessory Subunit

## Overview

SecG is an accessory subunit of the bacterial Sec translocon that comprises two transmembrane helices (TM1 and TM2) connected by a large cytoplasmic loop. The high-resolution structure of the full SecYEG complex reveals that SecG is peripherally located and tightly bound to SecY through hydrophobic interactions. The TM regions of SecG have low B factors compared to SecY, indicating they are not flexible. The cytoplasmic loop of SecG covers the channel at the pore ring level, contributing to sealing the cytoplasmic side of the protein-conducting channel. This finding was confirmed by disulfide bond formation analysis and molecular dynamics simulations.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.celrep.2015.10.025 | 5AWW | 2.7 A | I222 | Thermus thermophilus SecG; part of full-length SecYEG heterotrimer; expressed in E. coli BL21(DE3) | None |

## Expression and Purification

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: Thermus thermophilus SecG; co-expressed with SecY(R252G)-His6 and SecE from dual plasmid system (pAK22 encodes two copies of SecG; pAK24 encodes SecY-R252G-His6, SecE, and SecG)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane fraction preparation | Differential centrifugation | -- | Not specified + -- | Total membrane fraction from E. coli BL21(DE3) cells co-expressing SecYEG |
| Solubilization | Detergent solubilization | -- | 20 mM Tris-HCl pH 8.0, 300 mM NaCl, 5% glycerol, 0.1 mM PMSF + 2% n-dodecyl-beta-D-maltoside (DDM) | 1 hr at 4 C; ultracentrifugation at 138,000 x g for 30 min |
| Ni-NTA affinity chromatography | Affinity chromatography (His-tag on SecY) | Ni-NTA agarose | 20 mM Tris-HCl pH 8.0, 300 mM NaCl, 0.1% DDM, 5% glycerol + 0.1% DDM | Co-purification of SecG with His-tagged SecY; equilibration with 20 mM imidazole; wash with 40 mM imidazole; elution with 300 mM imidazole |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex 200 10/300 GL column | 20 mM Tris-HCl pH 8.0, 300 mM NaCl, 0.1% DDM, 5% glycerol + 0.1% DDM | SecG co-elutes with SecY and SecE as a stable heterotrimeric complex |
| Ion-exchange chromatography | Ion-exchange chromatography | HiTrap SP HP column | 20 mM Tris-HCl pH 8.0, 0.25% n-decyl-beta-D-maltoside (DM), 5% glycerol + 0.25% DM | SecYEG heterotrimer eluted with linear gradient of 0-100% elution buffer (1 M NaCl, 20 mM Tris-HCl pH 8.0, 0.25% DM, 5% glycerol) |


## Crystallization

No crystallization described.

## Biological / Functional Insights

### Cytoplasmic loop covers the protein-conducting channel

The cytoplasmic loop of SecG covers the hourglass-shaped SecY channel exactly over the pore ring, contributing to channel sealing on the cytoplasmic side. The C4 loop of SecY and the cytoplasmic loop of SecG are in close proximity; L35 of SecG is located near I272 of SecY, with a C-alpha-C-alpha distance of approximately 4.5 A. Disulfide bond crosslinking between SecY(I272C) and SecG(L35C) confirmed this proximity in the membrane. This arrangement prevents uncontrolled ion flux across the membrane while allowing regulated protein translocation. The proposed topology inversion of SecG during translocation of its hydrophilic cytoplasmic loop across the hydrophobic membrane (Nishiyama et al., 1996) does not appear to occur based on the crystal structure.

### Transmembrane helices tightly bound to SecY

SecG comprises TM1 and TM2 connected by a cytoplasmic loop. The TMs of SecG are tightly bound to SecY through hydrophobic interactions, with an interaction area involving TM3, TM4, C2, and C3 of SecY that accounts for approximately 30% of the SecG surface. The B factors of SecG TM regions are low compared to those of SecY, indicating that these transmembrane regions are not flexible. Disulfide bond formation analysis confirmed the interaction between SecG and SecY (Satoh et al., 2003).


## Cross-References

- [Thermus thermophilus SecYEG Translocon Complex](/xray-mp-wiki/proteins/secyeg/) — SecG is the accessory subunit that covers the cytoplasmic side of the SecYEG channel
- [Thermus thermophilus SecY Core Channel Subunit](/xray-mp-wiki/proteins/secy/) — SecG binds to SecY and covers the cytoplasmic side of the SecY channel
- [Thermus thermophilus SecE Accessory Subunit](/xray-mp-wiki/proteins/sece/) — SecE and SecG are both accessory subunits of the SecYEG translocon
