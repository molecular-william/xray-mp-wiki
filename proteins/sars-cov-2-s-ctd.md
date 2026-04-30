---
title: SARS-CoV-2 S Protein CTD
created: 2026-04-28
updated: 2026-04-28
type: protein
tags: [receptor, membrane-protein]
sources: [doi/10.1016##j.cell.2020.03.045]
category: proteins
layout: default
---


# SARS-CoV-2 Spike Protein CTD

## Overview

The C-terminal domain (CTD), also called the receptor-binding domain (RBD), is the portion of the SARS-CoV-2 spike (S) glycoprotein that directly binds to the host receptor ACE2. The S protein is a trimeric class I fusion protein embedded in the viral envelope. The CTD (residues 319–541) is a ~22 kDa domain that folds into a core subdomain and external subdomain, mediating viral attachment to host cells.

## Structure

### Wang et al. (Cell 2020) — SARS-CoV-2-CTD/hACE2 Complex

- **Resolution**: 2.5 Å
- **PDB ID**: 6LZG
- **Space group**: P41212
- **Domain organization**: Core subdomain (β strands labeled c1–c5) + external subdomain (β strands labeled 1'–5')
- **Disulfide bonds**: 4 cysteine pairs stabilizing the fold
- **N-glycosylation**: N343 glycan site visible in electron density
- **Binding partner**: hACE2 (residues 19–615)

## Secondary Structure

- **Core subdomain**: β strands βc1–βc5
- **External subdomain**: β strands β1'–β5'
- **Helices**: α1, α2 (short helices)
- **Loop regions**: Variable loop between βc4 and βc5 (unique to SARS-CoV-2)

## Comparison with SARS-RBD

- Overall similar receptor binding mode to SARS-CoV RBD
- Key residue substitutions in SARS-CoV-2-CTD strengthen hACE2 interaction
- Higher affinity for hACE2 than SARS-RBD
- Antigenically distinct: SARS-RBD-directed antibodies (mAbs B30A38, A50A1A1, C31A12, mAb1, mAb2, mAb3) do NOT bind SARS-CoV-2-CTD
- Divergent electrostatic surface potential despite similar protein fold

## Expression and Purification

### Wang et al. (Cell 2020)

- **Expression**: Sf9 insect cells (SFM adapted, Invitrogen) via Bac-to-Bac system
- **Construct**: SARS-CoV-2-CTD residues 319–541 fused to mouse Fc (mFc), accession EPI_ISL_402119
- **Vector**: pFastbac1 baculovirus transfer vector
- **Purification**: HiTrap HP 5 mL HisTrap column → Superdex 200 SEC
- **SEC buffer**: 20 mM [tris-buffer](/xray-mp-wiki/reagents/buffers/tris-buffer/)-HCl pH 8.0, 150 mM [sodium-chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/)
- **Alternative**: mFc-fusion proteins also expressed in HEK293T cells via pCAGGS plasmids, purified by rProtein A FF affinity chromatography

## Crystallization

### Wang et al. (Cell 2020)

- **Method**: Sitting-drop [vapor-diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion/)
- **Complex**: SARS-CoV-2-CTD-mFc + hACE2-His
- **Drop**: 0.8 µL protein + 0.8 µL reservoir at 18°C
- **Reservoir**: 0.1 M [mes-buffer](/xray-mp-wiki/reagents/buffers/mes-buffer/) pH 6.5, 10% w/v [peg-5000](/xray-mp-wiki/reagents/additives/peg-5000/) MME, 12% v/v 1-propanol
- **Protein concentration**: 15 mg/mL complex
- **Cryoprotection**: 20% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/) in reservoir
- **Data collection**: SSRF BL17U, 0.97919 Å wavelength
- **Phasing**: Molecular replacement with Phaser (PDB: 2AJF, SARS-RBD complex)
- **Refinement**: COOT + Phenix phenix.refine

## Key Residues in hACE2 Binding

The external subdomain of SARS-CoV-2-CTD contains key residues that contact hACE2:

- **Y453**: Contacts hACE2-H34
- **A475**: Contacts hACE2-S19, Q24, T27
- **F456**: Contacts hACE2-T27, D30, K31
- **Y473**: Contacts hACE2-T27
- **Y489**: Contacts hACE2-T27, F28, K31
- **N487**: Contacts hACE2-Q24
- **E484**: Contacts hACE2-K31
- **K417**: Contacts hACE2-D30
- **L455**: Contacts hACE2-D30, K31, H34
- **Q493**: Contacts hACE2-K31, H34, E35
- **Q498**: Contacts hACE2-Y41, Q42
- **T500**: Contacts hACE2-Y41
- **N501**: Contacts hACE2-Y41
- **Y505**: Contacts hACE2-E37
- **G496**: Contacts hACE2-D38
- **Y449**: Contacts hACE2-D38, Q42
- **G446**: Contacts hACE2-Q42
- **G476**: Contacts hACE2-S19, Q24

## Cross-References

- [ace2](/xray-mp-wiki/proteins/ace2/) — hACE2 receptor binding partner
- [peg-5000](/xray-mp-wiki/reagents/additives/peg-5000/) — PEG 5000 MME crystallization precipitant
- [mes-buffer](/xray-mp-wiki/reagents/buffers/mes-buffer/) — MES buffer for crystallization
- [glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Cryoprotectant
- [vapor-diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion/) — Sitting-drop vapor diffusion
- [xray-crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/) — X-ray crystallography
- [molecular-replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Phaser MR phasing
- [superdex-columns](/xray-mp-wiki/methods/purification/superdex-columns/) — Superdex 200 SEC
- [imac](/xray-mp-wiki/methods/purification/imac/) — HisTrap HP affinity purification
- [sf9-cells](/xray-mp-wiki/methods/expression-systems/sf9-cells/) — Sf9 insect cell expression
- [tris-buffer](/xray-mp-wiki/reagents/buffers/tris-buffer/) — Tris-HCl SEC buffer
- [sodium-chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/) — NaCl in SEC buffer
- sars-cov — SARS-CoV (structural comparison)