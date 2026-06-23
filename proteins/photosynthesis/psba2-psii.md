---
title: "PsbA2-PSII dimer from Thermosynechococcus elongatus"
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jbc.2022.102668]
verified: false
---

# PsbA2-PSII dimer from Thermosynechococcus elongatus

## Overview

The [Photosystem II](/xray-mp-wiki/proteins/photosynthesis/photosystem-ii/) (PSII) dimer from the thermophilic cyanobacterium Thermosynechococcus elongatus expressing only the psbA2 gene, which encodes the D1-2 variant (PsbA2). This structure was solved to reveal how the D1-2 isoform differs from the canonical D1-1 (PsbA1) and the stress-induced D1-3 (PsbA3) in terms of hydrogen bonding networks around the pheophytin cofactor, water/proton channels near the oxygen-evolving complex, and the QB binding site. The PsbA2 variant is activated under microaerobic conditions and shows altered S-state transition kinetics.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jbc.2022.102668 | 7YQ2 | 1.90 A | P212121 | PSII dimer expressing only psbA2 gene (pABA2 strain, lacking psbA1 and psbA3) | Chlorophyll a, pheophytin a, [Plastoquinone](/xray-mp-wiki/reagents/ligands/plastoquinone/), [HEME](/xray-mp-wiki/reagents/ligands/heme/), nonheme [IRON](/xray-mp-wiki/reagents/additives/iron/), Mn4CaO5 cluster, bicarbonate, chloride ions, [SQDG](/xray-mp-wiki/reagents/lipids/sulfoquinovosyl-diacylglycerol/), DGDG, [MGDG](/xray-mp-wiki/reagents/lipids/monogalactosyl-diacylglycerol/), carotenoids |

## Expression and Purification

- **Expression system**: Thermosynechococcus elongatus (thermophilic cyanobacterium)
- **Construct**: PSII dimer from mutant strain lacking psbA1 and psbA3 genes, expressing only psbA2 gene

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell growth and harvest | Cultivation of psbA2-only mutant strain | -- | -- + -- | Cells cultured with 20 umol photons m-2 s-1 red LED illumination, then diluted and grown with increasing light intensity over 7-8 days. |
| Thylakoid membrane isolation | Cell disruption and membrane isolation | -- | -- + -- | Cells harvested and broken to isolate thylakoid membranes. |
| Thylakoid solubilization | Detergent solubilization | -- | -- + 0.25% lauryl dimethylamine-n-oxide ([LDAO](/xray-mp-wiki/reagents/detergents/ldao/)) | Solubilization of thylakoid membranes with [LDAO](/xray-mp-wiki/reagents/detergents/ldao/). |
| Secondary solubilization | Detergent exchange | -- | -- + n-dodecyl-beta-D-maltoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Exchange to [DDM](/xray-mp-wiki/reagents/detergents/ddm/) for PSII dimer stability. |
| PSII dimer purification | Anion-exchange chromatography | Anion-exchange column | -- + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Purification of PSII dimers using anion-exchange column chromatography. |


## Crystallization

### doi/10.1016##j.jbc.2022.102668

| Parameter | Value |
|---|---|
| Method | Oil batch method |
| Protein sample | PsbA2-PSII dimer |
| Reservoir | Buffer conditions as reported previously |
| Temperature | 100 K (cryocooled) |
| Growth time | Crystals grew to approximately 1.0 x 0.4 x 0.2 mm |
| Cryoprotection | Cryoprotectant solution with buffer conditions as reported previously; flash-frozen in nitrogen gas stream at 100 K |
| Notes | Crystals diffracted to 1.90 A resolution. Space group P212121. Unit cell dimensions a=122.1, b=228.2, c=286.7 A. Data collected at SPring-8 BL41XU with 1.0 A wavelength. |


## Biological / Functional Insights

### Stronger hydrogen bond between PheoD1 and D1-E130

The replacement of D1-Gln130 with glutamate (D1-Q130E) in PsbA2 strengthens the hydrogen bond between PheoD1 and the 13(1)-keto group. This is consistent with FTIR spectroscopy measurements and partially explains the altered redox potential of PheoD1 observed in [PsbA3-PSII dimer from Thermosynechococcus elongatus](/xray-mp-wiki/proteins/photosynthesis/psba3-psii/) (increasing from -522 mV in PsbA1 to -505 mV). The hydrogen bond distance between the 13(1)-keto group of PheoD1 and D1-E130 was shortened in PsbA2 compared to PsbA1.

### Loss of hydrogen bond between PheoD1 and D1-F147 in PsbA2

In PsbA1 and PsbA3, D1-Tyr147 forms a hydrogen bond with the ester group of PheoD1. In PsbA2, this residue is replaced by phenylalanine (D1-Y147F), which loses this hydrogen bond, making PheoD1 in PsbA2 the most structurally unstable among the three D1 variants. This breakage may be necessary to avoid conformational changes of transmembrane helix C caused by the D1-Pro144 substitution (Pro in PsbA2 vs Cys in PsbA1/PsbA3), which disrupts the TMH C main chain and causes a flip of D1-F147.

### Narrowing of Cl-1 channel in PsbA2

The D1-Pro173 to methionine substitution (D1-P173M) in PsbA2 causes two water molecules (W568 and W572) in the Cl-1 channel to become invisible due to the larger side chain of methionine. The average diameter of the channel region around D1-173 is approximately 0.9 A narrower in PsbA2-PSII, with the narrowest region around 2.8 A. This may limit proton egress via Grotthus-type transfer, explaining the slower reduction of P680+ by TyrZ in the S2 and S3 states observed spectroscopically.


## Cross-References

- [PSI-LHCI supercomplex from Chlamydomonas reinhardtii](/xray-mp-wiki/proteins/photosynthesis/psi-lhci-chlamydomonas/) — Another photosystem complex from photosynthetic organisms solved by X-ray crystallography
- [N-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for PSII dimer purification and stabilization
- [Lauryl dimethylamine-n-oxide (LDAO)](/xray-mp-wiki/reagents/detergents/ldao/) — Initial solubilization detergent for thylakoid membranes
- [Photosystem II](/xray-mp-wiki/proteins/photosynthesis/photosystem-ii/) — Related protein structure
- [PsbA3-PSII dimer from Thermosynechococcus elongatus](/xray-mp-wiki/proteins/photosynthesis/psba3-psii/) — Related protein structure
- [IRON](/xray-mp-wiki/reagents/additives/iron/) — Additive used in purification or crystallization buffers
- [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) — Detergent used in purification or crystallization
- [HEME](/xray-mp-wiki/reagents/ligands/heme/) — Related ligand or cofactor
- [Plastoquinone](/xray-mp-wiki/reagents/ligands/plastoquinone/) — Related ligand or cofactor
- [MGDG](/xray-mp-wiki/reagents/lipids/monogalactosyl-diacylglycerol/) — Additive used in purification or crystallization buffers
