---
title: PsbA3-PSII dimer from Thermosynechococcus elongatus
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jbc.2022.102668]
verified: false
---

# PsbA3-PSII dimer from Thermosynechococcus elongatus

## Overview

The photosystem II (PSII) dimer from the thermophilic cyanobacterium Thermosynechococcus elongatus expressing only the psbA3 gene, which encodes the D1-3 variant (PsbA3). This structure was solved at 1.90 A resolution to reveal how the D1-3 isoform differs from the canonical D1-1 (PsbA1) and the microaerobic-inducible D1-2 (PsbA2). Key structural differences include a strengthened hydrogen bond between PheoD1 and D1-E130, loss of hydrogen bonding between SQDG and D1-Ala270 near the QB binding site, and enhanced QB exchange efficiency in PsbA3-PSII compared to the other variants.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jbc.2022.102668 | 7YQ7 | 1.90 A | P212121 | PSII dimer expressing only psbA3 gene (pABA3 strain, lacking psbA1 and psbA2) | Chlorophyll a, pheophytin a, plastoquinone, heme, nonheme iron, Mn4CaO5 cluster, bicarbonate, chloride ions, SQDG, DGDG, MGDG, carotenoids |

## Expression and Purification

- **Expression system**: Thermosynechococcus elongatus (thermophilic cyanobacterium)
- **Construct**: PSII dimer from mutant strain lacking psbA1 and psbA2 genes, expressing only psbA3 gene

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell growth and harvest | Cultivation of psbA3-only mutant strain | -- | -- + -- | Cells cultured with 20 umol photons m-2 s-1 red LED illumination, then diluted and grown with increasing light intensity over 7-8 days. |
| Thylakoid membrane isolation | Cell disruption and membrane isolation | -- | -- + -- | Cells harvested and broken to isolate thylakoid membranes. |
| Thylakoid solubilization | Detergent solubilization | -- | -- + 0.25% lauryl dimethylamine-n-oxide (LDAO) | Solubilization of thylakoid membranes with LDAO. |
| Secondary solubilization | Detergent exchange | -- | -- + n-dodecyl-beta-D-maltoside (DDM) | Exchange to DDM for PSII dimer stability. |
| PSII dimer purification | Anion-exchange chromatography | Anion-exchange column | -- + DDM | Purification of PSII dimers using anion-exchange column chromatography. |


## Crystallization

### doi/10.1016##j.jbc.2022.102668

| Parameter | Value |
|---|---|
| Method | Oil batch method |
| Protein sample | PsbA3-PSII dimer |
| Reservoir | Buffer conditions as reported previously |
| Temperature | 100 K (cryocooled) |
| Growth time | Crystals grew to approximately 1.0 x 0.4 x 0.2 mm |
| Cryoprotection | Cryoprotectant solution with buffer conditions as reported previously; flash-frozen in nitrogen gas stream at 100 K |
| Notes | Crystals diffracted to 1.90 A resolution. Space group P212121. Unit cell dimensions a=122.8, b=228.5, c=286.9 A. Data collected at SPring-8 BL41XU with 0.9 A wavelength. |


## Biological / Functional Insights

### Stronger hydrogen bond between PheoD1 and D1-E130

The replacement of D1-Gln130 with glutamate (D1-Q130E) in PsbA3 strengthens the hydrogen bond between PheoD1 and the 13(1)-keto group. This accounts for the observed increase in the redox potential of PheoD1 in PsbA3-PSII, shifting from -522 mV in PsbA1-PSII to -505 mV. The hydrogen bond distance between the 13(1)-keto group of PheoD1 and D1-E130 was shortened in both PsbA2 and PsbA3 compared to PsbA1.

### Loss of SQDG hydrogen bond with D1-Ala270

D1-Ser270 in PsbA1 and PsbA2 forms hydrogen bonds with the sulfoquinovosyl diacylglycerol (SQDG) molecule near the QB binding site. In PsbA3, this residue is replaced by alanine (D1-S270A), causing loss of this hydrogen bond. The SQDG head group shifts closer to D1-Asn267, resulting in shorter hydrogen bond distances between SQDG and D1-Asn267 (0.3 A shorter than PsbA1, 0.4 A shorter than PsbA2). This may result in easier exchange of bound QB with free plastoquinone, enhancing oxygen evolution efficiency in PsbA3-PSII.

### Enhanced QB binding stability in PsbA3

The main chain nitrogen of D1-Phe265 is hydrogen bonded to the carbonyl group of the QB head region, with distances 0.2 A shorter in PsbA2 and PsbA3 than in PsbA1. D1-Ser264 is also hydrogen bonded to QB, with distances 0.2 to 0.3 A shorter in PsbA2 and PsbA3. The B-factor of D1-Ser264 decreased to 51.8 A2 for PsbA3 compared to 59.8 A2 for PsbA1 and 60.1 A2 for PsbA2. The QB head region B-factor also decreased in PsbA3, resulting in more clearly defined density maps. These changes suggest more stable QB binding in PsbA3.


## Cross-References

- [PSI-LHCI supercomplex from Chlamydomonas reinhardtii](/xray-mp-wiki/proteins/psi-lhci-chlamydomonas/) — Another photosystem complex from photosynthetic organisms solved by X-ray crystallography
- [N-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for PSII dimer purification and stabilization
- [Lauryl dimethylamine-n-oxide (LDAO)](/xray-mp-wiki/reagents/detergents/lDAO/) — Initial solubilization detergent for thylakoid membranes
