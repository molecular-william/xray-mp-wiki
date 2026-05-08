---
title: Rhodopsin N2C/D282C Mutant
created: 2026-05-07
updated: 2026-05-07
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography, visual-pigment, mutant]
sources: [doi/10.1016##J.JMB.2007.03.007]
---

# Rhodopsin N2C/D282C Mutant

## Overview

The N2C/D282C mutant of bovine rhodopsin is a thermally stabilized recombinant form with an engineered disulfide bond between Cys2 and Cys282, connecting the N-terminal cap domain to the E3 extracellular loop. This mutant was the first recombinantly produced GPCR to have its crystal structure determined. Expressed in COS mammalian cells, the mutant shows ~10 deg.C increased thermal stability compared to wild-type opsin and enabled crystallization of fully deglycosylated rhodopsin (N2C/N15D/D282C triple mutant). The disulfide fixes the N-terminal cap over the beta-sheet lid covering the ligand-binding pocket, explaining the increased stability. The structure was solved by molecular replacement from the native rhodopsin 1GZM structure using microcrystallography at the ESRF ID13 beamline with a 5 um X-ray beam.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##J.JMB.2007.03.007 | 2J4Y | 3.4 A | P31 | N2C/D282C rhodopsin mutant (326 of 348 residues); expressed in COS cells | 11-cis-retinal (covalently bound to Lys296); N-linked glycosylation at Asn15 |

## Expression and Purification

- **Expression system**: COS-1 mammalian cells (heterologous expression)
- **Construct**: N2C/D282C rhodopsin mutant; N2C/N15D/D282C triple mutant for crystallization

### Purification Workflow

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Transient transfection of COS cells | -- | not specified | ~50 plates (15 cm) yielded ~0.6 mg rhodopsin; expression level ~50% of wild-type |
| Immunoaffinity chromatography | 1D4 immunoaffinity chromatography | 1D4 antibody | not specified | Purification using 1D4 antibody column |
| Detergent exchange | Sephadex G50 column | Sephadex G50 | Exchange from 0.02% DDM to 0.2% C8E4 | Protein/detergent exchange before crystallization |


## Crystallization

### doi/10.1016##J.JMB.2007.03.007

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | N2C/D282C rhodopsin at 10 mg/mL (concentrated with Centricon 30/Microcon 30) |
| Reservoir | 1.2-1.7 M lithium sulfate, 0.1 M Hepes pH 7.5 |
| Mixing ratio | 1 ul protein + 1 ul mother liquor |
| Temperature | not specified |
| Growth time | ~2 weeks |
| Cryoprotection | Mother liquor with 20% glycerol; flash-frozen in nitrogen at 100 K |
| Notes | Needle-like crystals up to 100 um long. Data collected at ESRF ID13 microfocus beamline (5 um beam) from microcrystals. |


## Biological / Functional Insights

### Engineered disulfide stabilizes N-terminal cap

The N2C/D282C disulfide bond covalently crosslinks the N-terminal cap domain to the E3 loop, anchoring it at two locations on opposite sides of the domain. This fixes the N-terminal cap permanently over the beta-sheet lid of the ligand-binding pocket, increasing thermal stability by ~10 deg.C. The C-alpha to C-alpha distance in the mutant (4.8 A) is slightly closer than in 1GZM (5.2 A). The disulfide introduces only minor backbone changes but significantly increases the reproducibility of crystallization.

### Microcrystallography for GPCR structure determination

The small crystal size (5 x 5 x 90 um) required microdiffractometry at ESRF ID13. A 5 um X-ray beam with 10^11 photons/s flux was used, with progressive translation along the needle to avoid radiation damage. 13 wedges of 5-15 degrees rotation from a single crystal were collected and merged. This approach enabled structure determination from recombinant GPCRs where milligram quantities are not available.


## Cross-References

- [Bovine Rhodopsin (Dark State)](/xray-mp-wiki/proteins/bovine-rhodopsin/) — Wild-type structure (1GZM) used as search model for molecular replacement
- [Octyltetraoxyethylene (C8E4)](/xray-mp-wiki/reagents/detergents/c8e4/) — Primary crystallization detergent at 0.2%
- [Lauryldimethylamine N-oxide (LDAO)](/xray-mp-wiki/reagents/detergents/lDAO/) — Added at 0.05% for crystallization
- [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) — Key component of crystallization reservoir buffer (0.1 M, pH 7.5) with lithium sulfate
- [11-cis-Retinal](/xray-mp-wiki/reagents/ligands/11-cis-retinal/) — Chromophore covalently bound to Lys296; supplied exogenously before solubilization for holoprotein formation
