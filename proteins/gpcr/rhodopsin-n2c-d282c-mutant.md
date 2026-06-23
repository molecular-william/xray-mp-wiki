---
title: "Rhodopsin N2C/D282C Mutant"
created: 2026-05-26
updated: 2026-05-26
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1016##J.JMB.2007.03.007]
verified: false
---

# Rhodopsin N2C/D282C Mutant

## Overview

The N2C/D282C mutant of rhodopsin is a thermally stabilized recombinant form with an engineered disulfide bond between Cys2 and Cys282, enabling handling of [OPSIN](/xray-mp-wiki/proteins/gpcr/opsin/) in detergent solution and increasing thermal stability by 10 deg.C. This structure, solved at 3.4 A resolution, was the first crystal structure of a recombinantly produced GPCR and opened the way for structural investigation of GPCR mutants expressed heterologously in cultured mammalian cells.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##J.JMB.2007.03.007 | 2J4Y | 3.4 A | P31 | Rhodopsin N2C/D282C mutant, residues 1-326 of 348; 326 of 348 residues in refined structure; two monomers (A and B) in asymmetric unit; post-translational modifications include acetylation of N-terminus, N-linked glycosylation at Asn15, and [11-cis-Retinal](/xray-mp-wiki/reagents/ligands/11-cis-retinal/) bound via Schiff base to Lys296 | [11-cis-Retinal](/xray-mp-wiki/reagents/ligands/11-cis-retinal/) (covalently bound to Lys296 via protonated Schiff base) |

## Expression and Purification

- **Expression system**: COS-1 mammalian cells (heterologous transient expression)
- **Construct**: Rhodopsin N2C/D282C double mutant with engineered disulfide bond between introduced Cys residues at positions 2 and 282; replaces hydrogen bond between Asn2 and Asp282 without changing overall fold; also screened N2C/N15D/D282C triple mutant for full deglycosylation

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell harvest and membrane preparation | Transient expression in COS-1 cells; membrane isolation from 50 plates (15 cm) of 5x10^5 cells per plate | -- | not specified (extraction from transfected COS cells) | ~5x10^5 COS-1 cells per 15 cm plate; 50 plates per preparation; expression level about 50% of wild-type |
| Solubilization | Detergent solubilization from membrane preparation | -- | not specified + 0.02% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm/) (N-Dodecyl-beta-D-maltopyranoside) | [11-cis-Retinal](/xray-mp-wiki/reagents/ligands/11-cis-retinal/) supplied exogenously before solubilization to form stable holoprotein ([OPSIN](/xray-mp-wiki/proteins/gpcr/opsin/) apoprotein is unstable in detergent) |
| Immunoaffinity chromatography | 1D4 immunoaffinity chromatography | 1D4 antibody | not specified + 0.02% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm/) (N-Dodecyl-beta-D-maltopyranoside) | Primary purification step using 1D4 antibody column; final yield ~0.6 mg of rhodopsin per preparation; protein/chromophore ratio (A280/A500) of 1.65 |
| Detergent exchange | Size-exclusion chromatography on Sephadex G50 | Sephadex G50 | not specified + 0.2% (w/v) [C8E4](/xray-mp-wiki/reagents/detergents/c8e4/) (Octyltetraoxyethylene), exchanged from 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Detergent exchange immediately before crystallization trials or thermal stability experiments |


## Crystallization

### doi/10.1016##J.JMB.2007.03.007

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | 10 mg/ml N2C/D282C rhodopsin in 0.2% [C8E4](/xray-mp-wiki/reagents/detergents/c8e4/) (Octyltetraoxyethylene); concentrated with Centricon 30 and Microcon 30 (Millipore); N,N-dimethyldodecylamine-N-oxide added to 0.05% |
| Reservoir | 1.2-1.7 M [Lithium Sulfate](/xray-mp-wiki/reagents/additives/lithium-sulfate/), 0.1 M HEPES (pH 7.5); 1 µl protein + 1 µl mother liquor sitting drops |
| Temperature | not specified (room temperature implied) |
| Growth time | crystals appeared within two weeks |
| Cryoprotection | 20% (v/v) [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) in mother liquor; crystals picked into cryoloops under infrared illumination |
| Notes | Needle-like crystals up to 100 µm long; unit cell a=b=109.3 A, c=77.7 A; diffracted to ~3.5 A after 15 s exposure; microcrystallography with 5 µm X-ray beam at ID13 beamline, ESRF Grenoble |


## Biological / Functional Insights

### First recombinant GPCR structure

The N2C/D282C mutant structure represents the first crystal structure of any recombinantly produced G protein-coupled receptor (GPCR). This demonstrates that heterologous expression in mammalian cells combined with protein stabilization strategies can yield sufficient quantities of functional GPCR for structure determination. The yield with recombinant rhodopsin was about 10% compared to about 1% with native rhodopsin from bovine retina.

### Engineered disulfide bond increases thermal stability

The N2C/D282C double mutant was designed to form a disulfide bond between introduced Cys residues at positions 2 and 282, replacing the native hydrogen bond between Asn2 and Asp282. This mutation increases the thermal stability of [OPSIN](/xray-mp-wiki/proteins/gpcr/opsin/) in detergent solution by 10 deg.C. The disulfide fixes the N-terminal cap permanently over the beta-sheet lid of the ligand-binding pocket, anchoring it at two locations on opposite sides of the domain, which likely explains the increased stability.

### Minimal structural impact of engineered disulfide

The overall Ca rms difference between the N2C/D282C mutant and the native [Bovine Rhodopsin](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/) structure (1GZM) is only 0.745 A. The extracellular domain, where the engineered disulfide is located, shows the smallest difference (Ca rms of 0.599 A). The immediate mutation sites (positions 2 and 282) have a Ca-Ca distance of 4.8 A versus 5.2 A in the native structure. The disulfide introduces only minor backbone changes in the E3 loop and N terminus, confirming the design preserved the overall fold.

### N-linked glycosylation at Asn15 observed in structure

Despite the N2C mutation removing one glycosylation site (Asn2), the second oligosaccharide chain at Asn15 is clearly evident in the electron density map, with strong density for the first sugar residue and partial density for the second. The N15D mutation (in the triple mutant) was designed to remove all N-linked glycosylation but did not improve crystal quality, likely due to unusual hydrophobic packing of carbohydrate chains in the P31 crystal form.

### Microcrystallography enables structure from nanogram quantities

Only 0.6 mg of crystallization-competent protein was obtained from one preparation. Microcrystals (5x5x90 µm needles) required a 5 µm X-ray beam at the ESRF ID13 microfocus beamline. Data were collected from 15 wedges along a single crystal, with progressive translation of the crystalline needle to avoid radiation damage. This approach yielded a complete dataset from a single crystal containing about 2.6x10^8 rhodopsin molecules.

### Retinitis pigmentosa disease mutation mechanism

Mutations at Asn15 that disrupt glycosylation are not tolerated and cause autosomal dominant retinitis pigmentosa in humans. The N15D mutation alone causes misfolding and failure to bind [11-cis-Retinal](/xray-mp-wiki/reagents/ligands/11-cis-retinal/). However, in the context of the stabilizing N2C/D282C disulfide, the N2C/N15D/D282C triple mutant expresses reasonably well (~50% of wild-type), displays wild-type absorption spectrum, and has specific activity for light-dependent transducin activation indistinguishable from the N2C/D282C mutant.


## Cross-References

- [Bovine Rhodopsin](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/) — Wild-type structure (1GZM) used as search model for molecular replacement; structural comparison shows 0.745 A rms difference
- [11-cis-Retinal](/xray-mp-wiki/reagents/ligands/11-cis-retinal/) — Chromophore covalently bound to Lys296 via protonated Schiff base; supplied exogenously before solubilization for holoprotein formation
- [DDM (N-Dodecyl-beta-D-maltopyranoside)](/xray-mp-wiki/reagents/detergents/ddm/) — Initial detergent used for solubilization at 0.02% (w/v); exchanged to C8E4 before crystallization
- [Octyltetraoxyethylene (C8E4)](/xray-mp-wiki/reagents/detergents/c8e4/) — Primary detergent for crystallization at 0.2% (w/v); provides enhanced thermal stability for the N2C/D282C mutant
- [Lithium Sulfate](/xray-mp-wiki/reagents/additives/lithium-sulfate/) — Primary precipitant in crystallization reservoir at 1.2-1.7 M concentration
- [HEPES (4-(2-hydroxyethyl)-1-piperazineethanesulfonic acid)](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer component in crystallization mother liquor at 0.1 M, pH 7.5
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Cryoprotectant at 20% (v/v) used for harvesting microcrystals
- [Magnesium Chloride (MgCl2)](/xray-mp-wiki/reagents/additives/magnesium-chloride/) — Component of thermal stability assay buffer (2 mM MgCl2)
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — 1D4 immunoaffinity chromatography used as primary purification method
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Sephadex G50 column used for detergent exchange from DDM to C8E4
