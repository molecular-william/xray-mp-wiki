---
title: "SMO-FLA Fusion Construct (SMO-Flavodoxin)"
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms15383]
verified: false
---

# SMO-FLA Fusion Construct (SMO-Flavodoxin)

## Overview

The SMO-FLA fusion construct is an engineered human [SMO](/xray-mp-wiki/proteins/gpcr/smoothened/) ([SMO](/xray-mp-wiki/proteins/gpcr/smoothened/)) receptor with Flavodoxin (FLA, 16 kDa) fused to the intracellular loop 3 (ICL3) between residues P434 and S443. This construct was designed to enhance crystallizability by providing a stable, well-folded crystallization chaperone in the intracellular region. The construct includes N- and C-terminal truncations and a single point mutation E194M in the hinge domain.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms15383 | 5V56 | 2.90 | P21 | SMO-FLA fusion (residues 53-558 with E194M mutation, FLA fused to ICL3 at P434-S443, N-term HA-FLAG-10xHis-TEV, C-term 10xHis) | [TC114 (SMO Ligand)](/xray-mp-wiki/reagents/ligands/tc114/) |
| doi/10.1038##ncomms15383 | 5V57 | 3.00 | P21 | SMO-FLA fusion (residues 53-558, FLA fused to ICL3 at P434-S443, N-term HA-FLAG-10xHis-TEV, C-term 10xHis, N-term further truncated by 5 residues for synchrotron) | [TC114 (SMO Ligand)](/xray-mp-wiki/reagents/ligands/tc114/) |

## Expression and Purification

- **Expression system**: HEK293F cells (human embryonic kidney 293F, suspended culture)
- **Construct**: SMO-FLA fusion: N-terminus residues 1-52 truncated, C-terminus residues 559-747 truncated, E194M point mutation in hinge domain. N-terminal fusion: HA signal sequence, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), 10xHis tag, TEV protease recognition site. Flavodoxin (FLA, 16 kDa) fused to ICL3 between P434 and S443 via overlapping PCR. C-terminal 10xHis tag.


### Purification Workflow

- **Expression system**: HEK293F cells
- **Expression construct**: SMO-FLA fusion (residues 53-558, E194M, FLA fused to ICL3)
- **Tag info**: HA signal, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), 10xHis tag at N-terminus (cleaved by TEV), 10xHis tag at C-terminus

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and transfection | Transient transfection | — |  | HEK293F cells transfected with PEI:DNA at 2:1 ratio, cultured at 37 C, collected 48 h post-transfection. 5 uM [GDC-0449](/xray-mp-wiki/reagents/ligands/vismodegib/) present during expression. |
| Membrane preparation | Cell lysis and membrane fractionation | — | 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl, EDTA-free protease inhibitor cocktail | Hypotonic buffer wash; repeated centrifugation (3x) in high salt buffer (1.0 M NaCl) |
| Ligand incubation | Ligand binding | — | 30 uM [TC114 (SMO Ligand)](/xray-mp-wiki/reagents/ligands/tc114/), 2 mg/ml [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) | Membranes incubated with [TC114 (SMO Ligand)](/xray-mp-wiki/reagents/ligands/tc114/) and [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) on [ROCKER](/xray-mp-wiki/proteins/miscellaneous/rocker/) at 4 C for 1 h |
| Solubilization | Solubilization | — | 50 mM HEPES pH 7.5, 200 mM NaCl + 1% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.2% (w/v) [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | 2.5 h at 4 C |
| IMAC (first capture) | Immobilized metal ion [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [TALON](/xray-mp-wiki/reagents/additives/talon/) IMAC resin (Clontech) | 50 mM HEPES pH 7.5, 200 mM NaCl, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 1.0 M NaCl + [DDM](/xray-mp-wiki/reagents/detergents/ddm/), [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Overnight binding at 4 C |
| Wash and detergent exchange | Immobilized metal ion [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | — | 50 mM HEPES pH 7.5, 800 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.5% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.1% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 10 mM MgCl2, 6 mM ATP, 30 uM [TC114 (SMO Ligand)](/xray-mp-wiki/reagents/ligands/tc114/) + [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Wash I buffer; 2 h [ROCKER](/xray-mp-wiki/proteins/miscellaneous/rocker/) incubation for complete detergent exchange |
| Wash II | Immobilized metal ion [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | — | 25 mM HEPES pH 7.5, 500 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.03% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.006% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 40 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 50 uM [TC114 (SMO Ligand)](/xray-mp-wiki/reagents/ligands/tc114/) + [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Six-column volume wash |
| Elution and TEV cleavage | Immobilized metal ion [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | — | 25 mM HEPES pH 7.5, 500 mM NaCl, 0.03% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.006% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 50 uM [TC114 (SMO Ligand)](/xray-mp-wiki/reagents/ligands/tc114/) | Eluted with high [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/); TEV protease cleavage of N-terminal tags |

**Final sample**: 25 mM HEPES pH 7.5, 500 mM NaCl, 0.03% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.006% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 50 uM [TC114 (SMO Ligand)](/xray-mp-wiki/reagents/ligands/tc114/)


## Crystallization

### doi/10.1038##ncomms15383

| Parameter | Value |
|---|---|
| Method | [Serial Femtosecond Crystallography](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/) (XFEL) |
| Protein sample | SMO-FLA-[TC114 (SMO Ligand)](/xray-mp-wiki/reagents/ligands/tc114/) complex |
| Temperature | 20 |
| Notes | XFEL data collection at LCLS (Linac Coherent Light Source, SLAC). Room temperature (20 C). Space group P21. Cell dimensions: a=40.6, b=349.5, c=61.8, beta=101.1 deg. 13,583,207 reflections measured, 37,101 unique. Rsplit=13.3 (280 in outer shell). CC*=0.9986. Cryoprotection: not applicable (XFEL at room temperature).
 |

| Parameter | Value |
|---|---|
| Method | Synchrotron X-ray crystallography |
| Protein sample | SMO-FLA-[TC114 (SMO Ligand)](/xray-mp-wiki/reagents/ligands/tc114/) complex |
| Temperature | -196 |
| Notes | Synchrotron data collection at BL41XU, SPring-8. Cryo-cooled (-196 C). Space group P21. Cell dimensions: a=40.1, b=356.4, c=59.1, beta=102.8 deg. 109,498 reflections measured, 29,571 unique. Rmerge=11.7 (39.3 in outer shell).
 |


## Biological / Functional Insights

### Flavodoxin Fusion for GPCR Crystallization

Flavodoxin (FLA, 16 kDa) was fused to the intracellular loop 3 (ICL3) of the human [SMO](/xray-mp-wiki/proteins/gpcr/smoothened/) receptor between residues P434 and S443. This fusion strategy provides a stable, well-folded protein domain on the intracellular side of the receptor, which enhances crystallizability by reducing conformational flexibility in the intracellular region. The SMO-FLA construct enabled the first XFEL structure determination of a multi-domain [SMO](/xray-mp-wiki/proteins/gpcr/smoothened/) receptor.

### Multi-domain Architecture of SMO

The SMO-FLA structure reveals the complete three-domain architecture of [SMO](/xray-mp-wiki/proteins/gpcr/smoothened/): a seven-transmembrane helices domain (TMD), a hinge domain (HD), and an intact extracellular cysteine-rich domain (CRD). This multi-domain arrangement enables allosteric interactions between the CRD and TMD that are critical for ligand recognition and receptor activation. The structure demonstrates that the CRD adopts a 'closed' conformation regardless of sterol binding when in the context of the full-length receptor.

### Activation Mechanism of Multi-domain GPCRs

The SMO-FLA structure combined with HDX analysis and MD simulations reveals a unique GPCR activation mechanism distinct from other multi-domain GPCRs. Transmembrane helix VI, extracellular loop 3 (ECL3), and the hinge domain (HD) play a central role in signal transmission. Agonist binding to the CRD triggers a small tilt of the CRD, which pushes helix VI and ECL3 outward, leading to amplified conformational changes and downward movement of the HD, transmitting the signal to the TMD.


## Cross-References

- [Human Smoothened Receptor (SMO)](/xray-mp-wiki/proteins/gpcr/smoothened/) — Parent receptor protein for the SMO-FLA fusion construct
- [TC114](/xray-mp-wiki/reagents/ligands/tc114/) — Stabilizing ligand used for SMO-FLA crystallization
- [Serial Femtosecond Crystallography](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/) — XFEL method used for SMO-FLA structure determination (PDB 5V56)
- [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) — Detergent used in SMO-FLA purification and sample preparation
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used in initial SMO-FLA membrane solubilization
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [ROCKER](/xray-mp-wiki/proteins/miscellaneous/rocker/) — Related protein structure
- [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Additive used in purification or crystallization buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
