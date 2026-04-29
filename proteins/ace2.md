---
title: ACE2
created: 2026-04-28
updated: 2026-04-28
type: protein
tags: [enzyme, membrane-protein, receptor]
sources: [doi/10.1016##j.cell.2020.03.045]
---

# Angiotensin-Converting Enzyme 2 (ACE2)

## Overview

ACE2 (Angiotensin-Converting Enzyme 2) is a type II membrane protein and carboxypeptidase that serves as the functional receptor for SARS-CoV and SARS-CoV-2 viral entry. It is expressed on the surface of epithelial cells in the lungs, heart, kidneys, and intestines. ACE2 plays a key role in the renin-angiotensin system, converting angiotensin II to angiotensin-(1-7).

## Structure

### Wang et al. (Cell 2020) — SARS-CoV-2-CTD/hACE2 Complex

- **Resolution**: 2.5 Å
- **PDB ID**: 6LZG
- **Space group**: P41212
- **Unit cell**: a=104.45, b=104.45, c=229.79 Å
- **Refinement**: Rwork/Rfree = 0.1846/0.2142
- **Contents**: 6,461 protein atoms, 1 ligand/ion, 322 water molecules
- **B-factors**: Protein 44.1, ligand 38.3, water 40.4
- **Construct**: hACE2 residues 19–615 (full-length ectodomain)
- **Binding partner**: SARS-CoV-2 S protein CTD (residues 319–541)

## Binding Interface with SARS-CoV-2 Spike

Key hACE2 residues interacting with SARS-CoV-2-CTD:

| hACE2 residue | SARS-CoV-2-CTD contacts |
|--------------|------------------------|
| S19 | A475(3,1), G476(4) |
| Q24 | A475(4), G476(5), N487(15,1) |
| T27 | F456(5), Y473(1), A475(2), Y489(7) |
| F28 | Y489(7) |
| D30 | K417(4,1), L455(2), F456(4) |
| K31 | L455(2), F456(5), E484(1), Y489(6), F490(2), Q493(3) |
| H34 | Y453(5,1), L455(9), Q493(6) |
| E35 | Q493(8) |
| E37 | Y505(7) |
| D38 | Y449(9,1), G496(5), Q498(1) |
| Y41 | Q498(8), T500(7,1), N501(8,1) |
| Q42 | G446(4,1), Y449(4,1), Q498(8,3) |
| L45 | Q498(3), T500(1) |

## Comparison with SARS-RBD Binding

- SARS-CoV-2-CTD and SARS-RBD use a similar overall binding mode to hACE2
- Key residue substitutions in SARS-CoV-2-CTD slightly strengthen interaction with hACE2
- SARS-CoV-2-CTD shows higher affinity for hACE2 compared to SARS-RBD
- Antigenic differences: SARS-CoV-2-CTD is antigenically distinct from SARS-RBD

## Solubilization, Expression, and Purification

### Wang et al. (Cell 2020)

- **Expression system**: Sf9 insect cells (SFM adapted, Invitrogen)
- **Vector**: pFastbac1 baculovirus transfer vector
- **Construct**: hACE2 residues 19–615, N-terminal gp67 signal peptide, C-terminal 6xHis tag
- **Baculovirus production**: DH10Bac competent E. coli (Invitrogen)
- **Purification**: HisTrap HP 5 mL column (GE Healthcare) metal affinity chromatography
- **SEC**: Superdex 200 column (GE Healthcare)
- **SEC buffer**: 20 mM [[tris-buffer]]-HCl pH 8.0, 150 mM [[sodium-chloride]]
- **Concentration**: Concentrated for crystallization at 15 mg/mL

## Crystallization

### Wang et al. (Cell 2020)

- **Method**: Sitting-drop [[vapor-diffusion]]
- **Drop setup**: 0.8 µL protein + 0.8 µL reservoir solution at 18°C
- **Protein concentration**: 15 mg/mL SARS-CoV-2-CTD/hACE2 complex
- **Reservoir**: 0.1 M [[mes-buffer]] pH 6.5, 10% w/v [[peg-5000]] MME, 12% v/v 1-propanol
- **Cryoprotection**: 20% (v/v) [[glycerol]] in reservoir solution
- **Data collection**: Shanghai Synchrotron Radiation Facility (SSRF) BL17U, wavelength 0.97919 Å
- **Processing**: HKL2000 software
- **Phasing**: Molecular replacement with Phaser using SARS-RBD complex (PDB: 2AJF) as search model
- **Model building**: COOT
- **Refinement**: phenix.refine in Phenix
- **Stereochemistry**: MolProbity assessment

## Cross-References

- [[sars-cov-2-s-ctd]] — SARS-CoV-2 spike protein C-terminal domain (binding partner)
- [[peg-5000]] — PEG 5000 MME crystallization precipitant
- [[glycerol]] — Cryoprotectant for crystal freezing
- [[vapor-diffusion]] — Sitting-drop vapor diffusion crystallization method
- [[xray-crystallography]] — X-ray crystallography structure determination
- [[molecular-replacement]] — Phaser molecular replacement phasing
- [[superdex-columns]] — Superdex 200 SEC column
- [[imac]] — HisTrap HP affinity chromatography (implied by 6xHis tag purification)
- [[sf9-cells]] — Sf9 insect cell expression system
- [[tris-buffer]] — Tris-HCl buffer for SEC
- [[sodium-chloride]] — NaCl in purification buffer
- [[peg-6000]] — Related PEG crystallization precipitant