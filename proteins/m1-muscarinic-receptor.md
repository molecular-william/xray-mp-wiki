---
title: M1 Muscarinic Acetylcholine Receptor
created: 2026-04-28
updated: 2026-04-28
type: protein
tags: [gpcr, membrane-protein, receptor]
sources: [doi/10.1016##j.cell.2021.11.001]
category: proteins
---
layout: default

# M1 Muscarinic Acetylcholine Receptor (M1-AR)

## Overview

The M1 muscarinic acetylcholine receptor (M1-AR) is a Class A GPCR that couples primarily to G(q)/G(11) proteins. It is widely expressed in the central nervous system (hippocampus, cortex) and is a key mediator of cognitive function, learning, and memory. M1-AR is a therapeutic target for Alzheimer's disease. It is one of five muscarinic receptor subtypes (M1–M5) with high sequence similarity in the orthosteric binding site.

## Structure

### Brown et al. (Cell 2021) — M1-StaR-T4L with 77-LH-28-1

- **Resolution**: 2.17 Å
- **PDB ID**: 6ZG8
- **Construct**: M1-StaR-T4L (thermostabilized M1 with T4-lysozyme fusion in ICL3)
- **Ligand**: 77-LH-28-1 (agonist, piperidine-based)
- **Space group**: Not explicitly stated
- **Key feature**: Agonist-bound conformation with disrupted "tyrosine cage"

### Brown et al. (Cell 2021) — M1-StaR-T4L with HTL9936

- **Resolution**: 2.4 Å
- **PDB ID**: 6ZG9
- **Ligand**: HTL9936 (selective M1 partial agonist, EC50 32 nM)
- **Key feature**: Extended orthosteric ligand with carbamate and amide groups forming water-mediated polar networks

### Brown et al. (Cell 2021) — M1-StaR-T4L with GSK1034702

- **Resolution**: 2.5 Å
- **PDB ID**: 6ZG9
- **Ligand**: GSK1034702 (bitopic M1 agonist, reached clinical development but withdrawn due to M2/M3 side effects)
- **Key feature**: Benzimidazol-2-one group interacting with Y82, I180, Y381

## M1-StaR Construct Design

The thermostabilized M1 receptor (M1-StaR) enabled crystallization:

- **Hybrid construct**: Residues 1–95 of human M4 fused to residues 88–438 of M1
- **12 thermostabilizing mutations** (γ12.1): F27A(1.34), T32A(1.39), V46L(1.53), L64A(2.43), T95A, W101A(3.28), S112A(3.39), A143L(4.43), A196T(5.46), K362A(6.32), A364L(6.34), S411A(7.46)
- **W101A(3.28)**: Key mutation enabling direct access of small molecule agonists to orthosteric site
- **T4-lysozyme fusion**: Residues R220–F355 in ICL3 replaced with T4L
- **N-terminal**: GP64 signal sequence (residues 1–27 removed)
- **C-terminal**: Deca-histidine tag (residues 439–460 removed)
- **Expression**: Sf21 insect cells, Bac-to-Bac system, ESF 921 medium

## Ligand Binding Site Architecture

### Amine Pocket (central)
- **Key residues**: D105(3.32), S109(3.36), W378(6.48), Y381(6.51), Y404(7.39), C407(7.42), Y408(7.43)
- **Interaction**: Protonated amine of agonists forms charge-charge interaction with D105(3.32)

### Major Pocket
- **Key residues**: Y106(3.33), N110(3.37), W157(4.56), A(5.43), T196(5.46), N382(6.52)

### Minor Pocket
- **Key residues**: F77(2.56), L81(2.60), Y282(2.61), A/W101(3.28), L102(3.29)

### Extracellular Vestibule
- **Key residues**: Y85(2.64), W91(2.50), C178(4.50), I180(4.52)

### Tyrosine Cage
- **Residues**: Y82(2.61), Y104(3.33), Y381(6.51), Y403(6.51), Y404(7.39), Y426(7.39)
- **Agonist binding**: Disrupts the tyrosine cage seen in antagonist structures
- **HTL9936 effect**: Piperidine nitrogen contacts Y404(7.39), causing rotation of Y381(6.51)

## Solubilization, Expression, and Purification

### Brown et al. (Cell 2021)

- **Expression system**: Sf21 insect cells (Spodoptera frugiperda)
- **Vector**: Bac-to-Bac Expression System (Invitrogen)
- **Medium**: ESF 921 + 10% FBS + 1% Pen/Strep
- **Infection**: 3.5 × 10^6 cells/mL, MOI ~2, 48 h at 27°C
- **Cell disruption**: Microfluidizer at ~15,000 psi
- **Membrane prep**: Ultracentrifugation at 200,000 g for 50 min
- **High salt wash**: PBS + 1 M NaCl + protease inhibitor
- **Detergent**: 1.5% (w/v) [ddm](/reagents/detergents/ddm/) (n-Dodecyl-β-D-maltopyranoside, Anatrace) for solubilization
- **Affinity chromatography**: Ni-NTA Superflow resin (QIAGEN), gradient 10–60 mM [imidazole](/reagents/additives/imidazole/)
- **Imidazole wash**: 40 mM Tris-HCl pH 7.6, 500 mM NaCl, 0.05% DDM, 70 mM imidazole
- **Elution**: 40 mM Tris-HCl pH 7.6, 500 mM NaCl, 0.05% DDM, 245 mM imidazole + ligand (20–40 μM)
- **SEC**: [superdex-columns](/methods/purification/superdex-columns/) 200 (GE Healthcare)
- **SEC buffer**: 40 mM Tris-HCl pH 7.6, 150 mM NaCl, 0.03% DDM + 40 μM ligand
- **Concentration**: ~60 mg/mL using 100 kDa cut-off membrane

## Crystallization

### Brown et al. (Cell 2021)

- **Method**: [lipidic-cubic-phase](/methods/crystallization/lipidic-cubic-phase/) (LCP)
- **Lipid**: Monoolein
- **Protein concentration**: ~60 mg/mL
- **Ligand**: 40 μM agonist (77-LH-28-1, HTL9936, or GSK1034702) present throughout purification and crystallization
- **Phasing**: Molecular replacement with Phaser using β1-adrenergic receptor:cyanopindolol (PDB: 2VT4) as search model
- **Refinement**: BUSTER

## MD Simulations

- Comparative MD simulations of M1-StaR with 77-LH-28-1, HTL9936, and GSK1034702
- HTL9936 forms stable water-mediated polar interaction networks with Y106(3.33), T196(5.46), Y381(6.51), N382(6.52) via carbamate moiety
- HTL9936 amide group interacts with C178(4.50) and Y404(7.39)
- HTL9936 binding site volume closer to antagonist tiotropium than full agonist iperoxo

## Pharmacology

- **HTL9936**: M1 EC50 32 nM, M2 > 20 μM, M3 > 20 μM, M4 EC50 398 nM — highly selective M1 partial agonist
- **77-LH-28-1**: Primary agonist used for hit identification and structure determination
- **GSK1034702**: Bitopic M1 agonist with significant M2 activity (EC50 26 nM at M2) — responsible for dose-limiting cardiovascular/GI side effects in clinical trials

## Cross-References

- [t4-lysozyme](/reagents/protein-tags/t4-lysozyme/) — T4L fusion in ICL3 for crystallization
- [ddm](/reagents/detergents/ddm/) — DDM detergent for solubilization
- [superdex-columns](/methods/purification/superdex-columns/) — Superdex 200 SEC
- [lipidic-cubic-phase](/methods/crystallization/lipidic-cubic-phase/) — LCP crystallization
- [molecular-replacement](/methods/structure-determination/molecular-replacement/) — Phaser MR (PDB: 2VT4)
- [imidazole](/reagents/additives/imidazole/) — Imidazole for Ni-NTA elution
- [htl9936](/reagents/ligands/htl9936/) — Selective M1 partial agonist (drug candidate for AD)
- [77-lh-28-1](/77-lh-28-1) — Agonist used for initial structure determination
- [gsk1034702](/gsk1034702) — Bitopic M1 agonist (clinical candidate, withdrawn)
- [gpcr](/gpcr) — Class A GPCR
- [microfluidizer](/methods/cell-lysis/microfluidizer/) — Cell disruption method