---
title: PspR (DTG Rhodopsin from Pseudomonas putida)
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jbc.2022.101722]
verified: false
---

# PspR (DTG Rhodopsin from Pseudomonas putida)

## Overview

PspR is a light-driven outward proton-pumping microbial rhodopsin from Pseudomonas putida, belonging to the DTG/DTS rhodopsin family. Unlike other light-driven proton pumps, PspR lacks a cytoplasmic proton donor residue (Asp/Glu homologous to BR Asp96), instead using a DTG motif. The protein comprises seven transmembrane helices and is covalently bound to [retinal](/xray-mp-wiki/reagents/ligands/retinal/) via a protonated Schiff base. The 2.84 A structure reveals large hydrophilic cytoplasmic cavities that enable direct proton uptake from the cytoplasmic solvent without a specialized donor residue.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jbc.2022.101722 | 7W74 | 2.84 A | Not specified in paper | PspR (DTG rhodopsin) from Pseudomonas putida, full-length, seven transmembrane helices | all-trans retinal (covalently bound via protonated Schiff base to Lys210) |

## Expression and Purification

- **Expression system**: Escherichia coli (heterologous expression)
- **Construct**: PspR from Pseudomonas putida, full-length, seven transmembrane helices, with His-tag for affinity purification

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell disruption | Sonication | -- | 50 mM Tris-HCl pH 8.0, 5 mM MgCl2 + -- | Harvested cells sonicated with Ultrasonic Homogenizer VP-300N; membrane fraction collected by ultracentrifugation at 142,000g for 1 h |
| Membrane solubilization | Detergent solubilization | -- | 50 mM MES-NaOH pH 6.5, 300 mM NaCl, 5 mM imidazole, 5 mM MgCl2 + 3% n-dodecyl-beta-D-maltopyranoside (DDM) | Insoluble fractions removed by ultracentrifugation at 142,000g for 1 h |
| Affinity purification | Co-NTA affinity chromatography | HiTrap TALON crude | 50 mM Tris-HCl pH 7.0, 300 mM NaCl, 300 mM imidazole, 5 mM MgCl2, 0.1% DDM + 0.1% DDM | Wash with 50 mM MES-NaOH pH 6.5, 300 mM NaCl, 50 mM imidazole, 0.1% DDM; elution with 300 mM imidazole |
| Dialysis | Dialysis | -- | 20 mM Hepes-NaOH pH 7.0, 100 mM NaCl, 0.05% DDM + 0.05% DDM | Dialysis to remove imidazole; final concentration 34 mg/ml protein for crystallization |


## Crystallization

### doi/10.1016##j.jbc.2022.101722

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | 34 mg/ml PspR mixed with monoolein at 2:3 protein-to-lipid ratio (v/v) |
| Temperature | 23 C |
| Growth time | Not specified |
| Cryoprotection | Crystals flash-cooled and stored in liquid nitrogen |
| Notes | Sample dispensed using Mosquito LCP robot (TTP Labtech); crystals harvested directly from LCP bolus |


## Biological / Functional Insights

### Absence of cytoplasmic proton donor residue

PspR lacks a cytoplasmic proton donor residue homologous to BR Asp96 (position 96 in BR corresponds to Gly84 in PspR). Instead, it has a DTG/DTS motif (Asp-Thr-Gly or Asp-Thr-Ser) important for its function. Proton directly binds from the cytoplasmic solvent to the retinal Schiff base (RSB) without a specialized donor residue. This represents a fundamentally different proton uptake mechanism compared to other light-driven proton pumps.

### Large cytoplasmic cavities enable direct proton uptake

The cytoplasmic side of TM7 (Ala212-Arg222) moves away from TM1, creating large hydrophilic cytoplasmic cavities not present in BR. These cavities increase water accessibility from the cytoplasmic milieu to the RSB region. The cytoplasmic region of the interhelical pathway consists of hydrophilic residues (His33, His37, Tyr91, Tyr213, Ser217), in contrast to the more tightly packed hydrophobic cytoplasmic region of BR. This structural rearrangement enables direct H+ transfer from cytoplasmic solvent to RSB.

### Extracellular proton release mechanism differs from BR

In BR, Glu194 and Glu204 form the proton-release group (PRG) with water molecules. In PspR, Glu204 is substituted with Thr198, and the homologous Glu188 forms a different hydrogen bond network with Arg70, Tyr71, and a water molecule. The E188A and E188Q mutants retained only 35-40% of WT pumping activity, confirming Glu188 significance in the proton release process.

### Photocycle intermediates and mutation effects

The PspR L81A mutant showed 1.9-fold higher activity than WT due to accumulation of a long-lived O-like intermediate that shortcuts the photocycle via photo-induced conversion. The Y213F mutant had similar decay of the M2 intermediate but significantly slower M2 decay, suggesting Tyr213 contributes to accelerating H+ uptake. The G84E mutant showed less pH-dependent photocycle with faster turnover at pH >= 7, as the introduced Glu partially functions as a proton donor.


## Cross-References

- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — Comparison reference; archetypal proton-pumping rhodopsin with cytoplasmic donor
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid component of LCP crystallization matrix
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for membrane solubilization and purification
- [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) — Chromophore covalently bound to Lys210 via protonated Schiff base
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — PspR crystallized by LCP method at 2.84 A resolution
- [Rhodopsin Photocycle](/xray-mp-wiki/concepts/rhodopsin-photocycle/) — PspR photocycle intermediates (M, O, L) characterized by laser flash photolysis
