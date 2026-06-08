---
title: SMO-FLA Fusion Construct (SMO-Flavodoxin)
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

The SMO-FLA fusion construct is an engineered human smoothened (SMO) receptor with Flavodoxin (FLA, 16 kDa) fused to the intracellular loop 3 (ICL3) between residues P434 and S443. This construct was designed to enhance crystallizability by providing a stable, well-folded crystallization chaperone in the intracellular region. The construct includes N- and C-terminal truncations and a single point mutation E194M in the hinge domain.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms15383 | 5V56 | 2.90 | P21 | SMO-FLA fusion (residues 53-558 with E194M mutation, FLA fused to ICL3 at P434-S443, N-term HA-FLAG-10xHis-TEV, C-term 10xHis) | TC114 |
| doi/10.1038##ncomms15383 | 5V57 | 3.00 | P21 | SMO-FLA fusion (residues 53-558, FLA fused to ICL3 at P434-S443, N-term HA-FLAG-10xHis-TEV, C-term 10xHis, N-term further truncated by 5 residues for synchrotron) | TC114 |

## Expression and Purification

- **Expression system**: HEK293F cells (human embryonic kidney 293F, suspended culture)
- **Construct**: SMO-FLA fusion: N-terminus residues 1-52 truncated, C-terminus residues 559-747 truncated, E194M point mutation in hinge domain. N-terminal fusion: HA signal sequence, FLAG tag, 10xHis tag, TEV protease recognition site. Flavodoxin (FLA, 16 kDa) fused to ICL3 between P434 and S443 via overlapping PCR. C-terminal 10xHis tag.


### Purification Workflow

- **Expression system**: HEK293F cells
- **Expression construct**: SMO-FLA fusion (residues 53-558, E194M, FLA fused to ICL3)
- **Tag info**: HA signal, FLAG tag, 10xHis tag at N-terminus (cleaved by TEV), 10xHis tag at C-terminus

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and transfection | Transient transfection | — |  | HEK293F cells transfected with PEI:DNA at 2:1 ratio, cultured at 37 C, collected 48 h post-transfection. 5 uM vismodegib present during expression. |
| Membrane preparation | Cell lysis and membrane fractionation | — | 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl, EDTA-free protease inhibitor cocktail | Hypotonic buffer wash; repeated centrifugation (3x) in high salt buffer (1.0 M NaCl) |
| Ligand incubation | Ligand binding | — | 30 uM TC114, 2 mg/ml iodoacetamide | Membranes incubated with TC114 and iodoacetamide on rocker at 4 C for 1 h |
| Solubilization | Solubilization | — | 50 mM HEPES pH 7.5, 200 mM NaCl + 1% (w/v) DDM, 0.2% (w/v) CHS | 2.5 h at 4 C |
| IMAC (first capture) | Immobilized metal ion affinity chromatography | TALON IMAC resin (Clontech) | 50 mM HEPES pH 7.5, 200 mM NaCl, 20 mM imidazole, 1.0 M NaCl + DDM, CHS | Overnight binding at 4 C |
| Wash and detergent exchange | Immobilized metal ion affinity chromatography | — | 50 mM HEPES pH 7.5, 800 mM NaCl, 10% glycerol, 0.5% LMNG, 0.1% CHS, 20 mM imidazole, 10 mM MgCl2, 6 mM ATP, 30 uM TC114 + LMNG, CHS | Wash I buffer; 2 h rocker incubation for complete detergent exchange |
| Wash II | Immobilized metal ion affinity chromatography | — | 25 mM HEPES pH 7.5, 500 mM NaCl, 10% glycerol, 0.03% LMNG, 0.006% CHS, 40 mM imidazole, 50 uM TC114 + LMNG, CHS | Six-column volume wash |
| Elution and TEV cleavage | Immobilized metal ion affinity chromatography | — | 25 mM HEPES pH 7.5, 500 mM NaCl, 0.03% LMNG, 0.006% CHS, 250 mM imidazole, 50 uM TC114 | Eluted with high imidazole; TEV protease cleavage of N-terminal tags |

**Final sample**: 25 mM HEPES pH 7.5, 500 mM NaCl, 0.03% LMNG, 0.006% CHS, 50 uM TC114


## Crystallization

### doi/10.1038##ncomms15383

| Parameter | Value |
|---|---|
| Method | Serial femtosecond crystallography (XFEL) |
| Protein sample | SMO-FLA-TC114 complex |
| Temperature | 20 |
| Notes | XFEL data collection at LCLS (Linac Coherent Light Source, SLAC). Room temperature (20 C). Space group P21. Cell dimensions: a=40.6, b=349.5, c=61.8, beta=101.1 deg. 13,583,207 reflections measured, 37,101 unique. Rsplit=13.3 (280 in outer shell). CC*=0.9986. Cryoprotection: not applicable (XFEL at room temperature).
 |

| Parameter | Value |
|---|---|
| Method | Synchrotron X-ray crystallography |
| Protein sample | SMO-FLA-TC114 complex |
| Temperature | -196 |
| Notes | Synchrotron data collection at BL41XU, SPring-8. Cryo-cooled (-196 C). Space group P21. Cell dimensions: a=40.1, b=356.4, c=59.1, beta=102.8 deg. 109,498 reflections measured, 29,571 unique. Rmerge=11.7 (39.3 in outer shell).
 |


## Biological / Functional Insights

### Flavodoxin Fusion for GPCR Crystallization

Flavodoxin (FLA, 16 kDa) was fused to the intracellular loop 3 (ICL3) of the human SMO receptor between residues P434 and S443. This fusion strategy provides a stable, well-folded protein domain on the intracellular side of the receptor, which enhances crystallizability by reducing conformational flexibility in the intracellular region. The SMO-FLA construct enabled the first XFEL structure determination of a multi-domain SMO receptor.

### Multi-domain Architecture of SMO

The SMO-FLA structure reveals the complete three-domain architecture of SMO: a seven-transmembrane helices domain (TMD), a hinge domain (HD), and an intact extracellular cysteine-rich domain (CRD). This multi-domain arrangement enables allosteric interactions between the CRD and TMD that are critical for ligand recognition and receptor activation. The structure demonstrates that the CRD adopts a 'closed' conformation regardless of sterol binding when in the context of the full-length receptor.

### Activation Mechanism of Multi-domain GPCRs

The SMO-FLA structure combined with HDX analysis and MD simulations reveals a unique GPCR activation mechanism distinct from other multi-domain GPCRs. Transmembrane helix VI, extracellular loop 3 (ECL3), and the hinge domain (HD) play a central role in signal transmission. Agonist binding to the CRD triggers a small tilt of the CRD, which pushes helix VI and ECL3 outward, leading to amplified conformational changes and downward movement of the HD, transmitting the signal to the TMD.


## Cross-References

- [Human Smoothened Receptor (SMO)](/xray-mp-wiki/proteins/smoothened/) — Parent receptor protein for the SMO-FLA fusion construct
- [TC114](/xray-mp-wiki/reagents/ligands/tc114/) — Stabilizing ligand used for SMO-FLA crystallization
- [Serial Femtosecond Crystallography](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/) — XFEL method used for SMO-FLA structure determination (PDB 5V56)
- [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) — Detergent used in SMO-FLA purification and sample preparation
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used in initial SMO-FLA membrane solubilization
