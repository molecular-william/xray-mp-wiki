---
title: MCE Proteins — Lipid Transport Systems
created: 2026-04-28
updated: 2026-04-28
type: protein
tags: [membrane-protein, lipid-transport, mce-family, outer-membrane, bacterial-transport]
sources: [doi/10.1016##j.cell.2017.03.019]
---

# MCE Proteins — Lipid Transport Systems for Bacterial Outer Membrane

## Overview

MCE (Mycobacterium Smegmatis Cell Envelope) proteins form diverse architectures for lipid trafficking between the inner and outer membranes in double-membraned bacteria. This paper reports structures of multiple MCE family components revealing conserved hexameric ring modules that assemble into tube- and syringe-like architectures with central channels.

## Protein Complexes

### Mla System (Integrity Lipid Asymmetry)

- **MlaFEDB complex**: Inner membrane ABC transporter
  - MlaF: Transmembrane permease (de novo model from co-evolving residues)
  - MlaD: Periplasmic adaptor protein (hexameric ring)
  - MlaE: Outer membrane permease component (de novo model)
  - MlaB: ATPase component
  - Architecture: ~10 Å resolution cryo-EM density map
  - Detergent: DDM for solubilization

- **MlaC**: Periplasmic lipid shuttle protein
  - Structure: Mixed α/β fold, 4 β strands + 7 α helices
  - Lipid binding: Deep hydrophobic pocket, binds two "tails" of lipid (no head group interaction)
  - Function: Shuttles lipids between IM MlaFEDB and OM MlaA-OmpF complexes
  - PDB: Deposited by NESG (Northeast Structural Genomics Consortium)

- **MlaA-OmpF complex**: Outer membrane lipid transfer
  - MlaA: OM protein interacting with OmpF porin
  - Function: Receives lipids from MlaC for OM insertion

### YebT System

- **Architecture**: Tall stack of 7 rings forming elongated tube-like barrel
  - Dimensions: ~230 Å long, ~90 Å diameter
  - Resembles: Proteasome, ClpXP, GroEL (small globular domains assemble into rings)
  - Additional density: Fuzzy density at one end of barrel

### PqiB System

- **Architecture**: Tube/syringe-like with central channel
  - Final MCE domain: Six-helix coiled coil needle (~35 Å diameter, 15–20 Å lumen)
  - Needle continuous with channel through PqiB barrel

## Expression and Purification

### MlaD
- **Construct**: MlaD(32–183) or MlaD(32–140) truncated constructs
- **Expression**: E. coli
- **Selenomethionine**: Site-directed mutagenesis (12 Leu→Met targets, 5 expressed at near WT levels)
- **Detergent**: DDM for solubilization

### MlaFEDB Complex
- **Operon**: Complete mlaFEDCB from MG1655 genome
- **Vector**: Custom pET vector (pDCE587), Gibson assembly
- **Tag**: C-terminal 6xHis on MlaD
- **Expression strain**: Rosetta 2 (DE3)
- **Induction**: IPTG to 1 mM from overnight culture (OD600 ~0.9)

### MlaC
- **Expression**: E. coli
- **Concentration**: 10–60 mg/ml for crystallization

### MlaA-OmpF Complex
- **Expression**: E. coli
- **Purification**: Co-purification of MlaA with OmpF

### YebT
- **Operon**: yebST from MG1655 genome
- **Vector**: pBAD-His (bicistronic YebS-YebT co-expression)
- **Tag**: C-terminal 6xHis on YebT
- **Expression strain**: Rosetta 2 (DE3)

### PqiB
- **Expression**: E. coli
- **Purification**: As described for YebT

## Crystallization

### MlaC
- **Method**: Sitting drop, vapor diffusion
- **Screens**: JCSG Core I–IV (QIAGEN)
- **Conditions**: 0.1 M citric acid pH 3.5, 1.6 M ammonium sulfate
- **Cryoprotection**: 37.5% ethylene glycol
- **Data collection**: Native diffraction data collected

### MlaD
- **Method**: Crystallization and structure determination (detailed methods in supplemental)
- **Screening**: Selenomethionine derivatives screened for diffraction-quality crystals

## Biological Significance

- **Lipid asymmetry**: Mla system maintains outer membrane lipid asymmetry in Gram-negative bacteria
- **Conserved building block**: Hexameric ring module used across diverse MCE family architectures
- **Periplasm-spanning**: Multiple architectures (tube, syringe, barrel) for lipid trafficking
- **Co-evolution**: MlaD TM helices co-evolve with MlaE membrane-spanning region