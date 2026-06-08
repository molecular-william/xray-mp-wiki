---
title: Blastochloris viridis Photosynthetic Reaction Centre
created: 2026-06-04
updated: 2026-06-04
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms3911]
verified: false
---

# Blastochloris viridis Photosynthetic Reaction Centre

## Overview

The photosynthetic reaction centre from Blastochloris viridis (RC_vir) is a four-subunit integral membrane protein complex with a molecular weight of 135 kDa. It is responsible for the primary charge separation in bacterial photosynthesis, converting light energy into electrochemical potential. The complex contains multiple cofactors including bacteriochlorophylls, bacteriopheophytins, quinones, and heme groups that form two branches of electron transfer, with the L-branch being the active pathway.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms3911 | 4CAS | 3.5 | P2_12_12_1 | Full-length RC_vir | bacteriochlorophyll, bacteriopheophytin, menaquinone-7, heme |

## Expression and Purification

### Purification Workflow

- **Expression system**: Blastochloris viridis

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Fermentation | -- | 20 mM Tris-HCl pH 8.5, 1% LDAO + 1% LDAO | 250 ml POROS 50 micron HQ media packed in XK 50/20 column |
| Affinity chromatography | Ion-exchange chromatography | POROS 50 micron HQ | 20 mM Tris-HCl pH 8.5, 1% LDAO, 0-0.5 M NaCl gradient + 1% LDAO | Eluted with linear NaCl gradient |
| Size exclusion chromatography | Size-exclusion chromatography | HiPrep 26/60 Sephacryl S-300 | 10 mM Tris-HCl pH 8.5, 0.1% LDAO + 0.1% LDAO | 3 mg pure RC_vir per litre of cell culture |


## Crystallization

### doi/10.1038##ncomms3911

| Parameter | Value |
|---|---|
| Method | Liquid sponge phase crystallization |
| Protein sample | 25-35 mg/ml RC_vir |
| Temperature | room temperature |
| Growth time | microcrystals |
| Notes | Batch crystallization in septum-sealed glass vials; microcrystals injected as microjet |


## Biological / Functional Insights

### Serial femtosecond crystallography structure at 3.5 A resolution

The RC_vir SFX structure was determined to 3.5 A resolution using data from 1,175 microcrystals
(P2_12_12_1 space group; a=57.9 A, b=84.8 A, c=384.3 A). The R_work/R_free values were 0.294/0.327.
The electron density maps clearly resolved all cofactors including the special pair bacteriochlorophylls,
the L-branch bacteriopheophytin, and the menaquinone in the Q_A pocket. The multiplicity of 27 was
orders of magnitude lower than soluble protein SFX structures, yet the electron density quality was
striking due to multicrystal averaging.

### Absence of radiation damage at 33 MGy dose

Each microcrystal was exposed to a 42-fs X-ray pulse of 4x10^11 photons at 9.34 keV, depositing
33 MGy, which is approximately two orders of magnitude above the limit for room-temperature
crystallography. Despite approximately four primary photo-ionization events and 200 secondary
ionization events per RC_vir molecule, no signs of radiation damage were visible. The covalent
thioether bond linking the N-terminal cysteine of the tetrahaem cytochrome c subunit to a
diacylglycerol molecule remained intact, and all metal centres (Mg and Fe) emerged as strong
positive density in omit maps.


## Cross-References

- [Serial Femtosecond Crystallography](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/) — Primary structure determination method used
- [Lauryldimethylamine-oxide (LDAO)](/xray-mp-wiki/reagents/detergents/lDAO/) — Detergent used in purification and solubilization
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid used in LSP crystallization
- [Bacteriochlorophyll](/xray-mp-wiki/reagents/cofactors/bacteriochlorophyll/) — Cofactor in the special pair and electron transfer chain
- [Bacteriopheophytin](/xray-mp-wiki/reagents/cofactors/bacteriopheophytin/) — Electron acceptor cofactor in L-branch
- [Menaquinone-7](/xray-mp-wiki/reagents/cofactors/menaquinone-7/) — Quinone cofactor in Q_A pocket
- [X-Ray Radiation Damage in Crystallography](/xray-mp-wiki/concepts/x-ray-radiation-damage/) — Central finding, no damage at 33 MGy dose via SFX
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LSP is a liquid analogue of LCP crystallization
