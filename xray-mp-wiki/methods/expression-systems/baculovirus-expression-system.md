---
title: "Baculovirus Expression System in Sf9 Cells"
created: 2026-05-29
updated: 2026-06-22
type: method
category: methods
layout: default
tags: [expression-system, subdirectory-expression-systems]
sources: [doi/10.1021##acs.jmedchem.0c01620, doi/10.1021##acs.jmedchem.3c01822, doi/10.1021##acs.jmedchem.5b00892, doi/10.1038##nature08650, doi/10.1038##nature10753, doi/10.1038##nature13306]
verified: regex
---

# Baculovirus Expression System in Sf9 Cells

## Overview

The baculovirus expression system using Spodoptera frugiperda (Sf9) insect cells is a widely used eukaryotic expression platform for membrane proteins, particularly GPCRs. The Bac-to-Bac system enables rapid generation of recombinant baculovirus through bacterial transformation of a bacmid containing the gene of interest. Sf9 cells are infected at a controlled multiplicity of infection (MOI), and protein expression occurs over 48-72 hours. The system supports proper folding, post-translational modifications, and membrane insertion of complex eukaryotic proteins.

## Principle

The Bac-to-Bac system uses a modified Autographa californica multiple nucleopolyhedrovirus (AcMNPV) bacmid DNA. The gene of interest is cloned into a donor vector containing baculovirus transposon sequences (mini-Tn7), which is then co-transformed with the bacmid into E. coli DH10Bac cells. Transposition places the gene of interest under control of the strong baculovirus polyhedrin promoter. Recombinant bacmid DNA is extracted and transfected into Sf9 insect cells, producing recombinant baculovirus particles. These are used to infect fresh Sf9 cells at a controlled MOI for protein expression. The insect cell system supports proper eukaryotic post-translational modifications including glycosylation, disulfide bond formation, and membrane protein insertion.

## Protocol

### Reagents and Materials

- Sf9 insect cells (Invitrogen)
- Bac-to-Bac Baculovirus Expression System kit (Thermo Fisher Scientific)
- pFastBac1 donor vector
- DH10Bac competent E. coli cells
- TC-100 insect medium or Grace's medium with 10% fetal bovine serum
- Gentamicin antibiotic
- Kanamycin for bacmid selection
- Tn7 transposon mixture

### Steps

1. Clone gene of interest into pFastBac1 donor vector with appropriate promoter and tag
2. Co-transform pFastBac1-donor with Tn7 transposon mixture into DH10Bac competent cells
3. Select recombinant bacmid on kanamycin/gentamicin plates; verify by colony PCR
4. Extract recombinant bacmid DNA and transfect into Sf9 cells to generate Bac1 viral stock
5. Infect Sf9 cells at 2x10^6 cells/mL with MOI 5; grow 48 h at 27 C
6. Harvest cells by centrifugation and store at -80 C
7. Prepare cell membranes in hypotonic buffer (10 mM HEPES pH 7.0, 10 mM MgCl2, 20 mM KCl)
8. Solubilize membrane fraction with detergent (e.g., 1.0% DDM, 0.2% CHS) for 3 h at 4 C
9. Purify by IMAC (TALON resin) with wash and elution buffers containing test peptides
10. Remove glycosylation with EndoH overnight at 4 C
11. Concentrate protein for downstream applications

### Typical Conditions

- **Cell growth temperature**: 27 C
- **Infection time**: 48 h
- **Cell density at infection**: 2 x 10^6 cells/mL
- **Multiplicity of infection (MOI)**: 5


## Advantages

- Supports proper folding and post-translational modifications of complex eukaryotic proteins
- High expression levels achievable with strong polyhedrin promoter
- Scalable from small cultures to large bioreactors
- Suitable for multi-pass transmembrane proteins including GPCRs
- Compatible with fusion partners (BRIL, T4L, PGS) and thermostabilizing mutations

## Disadvantages

- Insect cell glycosylation differs from mammalian N-glycosylation (paucimannosyl vs. complex)
- Lower expression levels compared to some bacterial systems
- Longer timeline (2-3 weeks) compared to bacterial expression
- Risk of viral contamination in continuous cell cultures
- May require optimization of infection conditions for each protein

## Proteins Using This Method

| Protein | Resolution | PDB | Notes |
|---|---|---|---|
| [Human Glucose Transporter GLUT1 (SLC2A1)](/xray-mp-wiki/proteins/mfs-transporters/glut1/) | 3.2 | unknown | Full-length human GLUT1 (residues 1-492, N45T, E329Q, C-terminal 10x His) expressed in High Five insect cells using pFastBac baculovirus system; harvested 48 h post-infection |
| [Human Melanocortin 4 Receptor (MC4-R)](/xray-mp-wiki/proteins/gpcr/mc4-r/) | 2.90 | 8WKY | MC4-R-PGS construct with thermostabilizing mutations; expressed in Sf9 via Bac-to-Bac system; DDM/CHS solubilized; purified by TALON IMAC; crystallized by LCP at 2.9 A |
| [Human Melanocortin 4 Receptor (MC4-R)](/xray-mp-wiki/proteins/gpcr/mc4-r/) | 3.30 | 8WKZ | Same MC4-R-PGS construct; co-crystallized with SBL-MC-31 at 3.3 A |

## Related Methods

- [Pichia pastoris Expression System](/xray-mp-wiki/methods/expression-systems/pichia-pastoris/) — Alternative eukaryotic expression system for membrane proteins

## Related Reagents

- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for solubilizing membrane proteins from Sf9 cell membranes
- [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon/) — IMAC resin used for His-tag purification of Sf9-expressed proteins
