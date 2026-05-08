---
title: NtMATE2 Nicotine Transporter
created: 2026-05-05
updated: 2026-05-05
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1002##1873-3468.14136]
---

# NtMATE2 Nicotine Transporter

## Overview

NtMATE2 is a multidrug and toxic compound extrusion (MATE) family transporter from Nicotiana tabacum (tobacco) that mediates vacuolar sequestration of nicotine, a specialized alkaloid. As one of three nicotine MATE transporters in tobacco roots, NtMATE2 transports nicotine from the cytosol into the vacuolar lumen in exchange for protons, protecting the plant from its own toxic metabolite. The crystal structures reveal two outward-facing conformations with unprecedented TM7 movement distinct from other eukaryotic MATE proteins.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1002##1873-3468.14136 | 7DQK | 3.5 A | P212121 | NtMATE2-EFPGENLYFQGQF-eGFP(3-239)-H8, residues 18-493 (Mol-A), 15-493 (Mol-B) | unidentified molecule in Mol-B C-lobe cavity (possibly partial nicotine mimic) |

## Expression and Purification

- **Expression system**: Pichia pastoris yeast strain SMD1168
- **Construct**: C-terminal GFP-His8-tagged NtMATE2, induced with 0.5% methanol in BMMY medium at 20 C for 72 h

### Purification Workflow

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Microfluidizer (M-110EH, Microfluidics) | -- | 300 mM NaCl, 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/)-HCl pH 8.0, 10% glycerol; 5 passes at 22,000 p.s.i. | Membrane fraction separated by centrifugation |
| Solubilization | Detergent solubilization | -- | 300 mM NaCl, 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/)-HCl pH 8.0, 10% glycerol, 2% [DDM](/xray-mp-wiki/reagents/detergents/ddm/); 2 h incubation | 130,000 g for 30 min, supernatant collected |
| Affinity chromatography | TALON cobalt affinity resin | TALON (Clontech) | Equilibration: 300 mM NaCl, 50 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/)-Na pH 7.0, 5% glycerol, 0.05% DDM, 0.005% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 20 mM imidazole pH 8.0 | His-tagged NtMATE2 bound |
| Wash | Affinity wash | TALON | 300 mM NaCl, 50 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/)-Na pH 7.0, 5% glycerol, 0.03% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.003% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 20-40 mM imidazole pH 8.0 | -- |
| Elution | Affinity elution | TALON | 300 mM NaCl, 50 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/)-Na pH 7.0, 5% glycerol, 0.03% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.003% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 200 mM imidazole pH 8.0 | -- |
| Concentration | Ultrafiltration | -- | 300 mM NaCl, 50 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/)-Na pH 7.0, 1% glycerol, 0.03% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.003% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Amicon Ultra 100K filter (Merck Millipore) |
| Size-exclusion chromatography | [Size-exclusion chromatography (SEC)](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | Superdex 200 Increase 10/30 GL (GE Healthcare) | 300 mM NaCl, 50 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/)-Na pH 7.0, 1% glycerol, 0.03% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.003% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | GFP-His8 tag removed with [TEV](/xray-mp-wiki/methods/purification/tev-protease/) protease at 4 C for 16 h before SEC |


## Crystallization

### doi/10.1002##1873-3468.14136

| Parameter | Value |
|---|---|
| Method | [Lipidic cubic phase (LCP)](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) |
| Protein sample | NtMATE2 + 2.5 mM [nicotine](/xray-mp-wiki/reagents/ligands/nicotine/) |
| Lipid | [monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) (NU-CHEK-PREP / Sigma-Aldrich) |
| Protein-to-lipid ratio | 1:1 (twin-syringe mixing) |
| Temperature | not specified |
| Growth time | not specified |
| Notes | 30 nL LCP mixed with 1 uL reservoir in glass sandwich plates. Two outward-facing forms (Mol-A, Mol-B) in asymmetric unit. Phased by molecular replacement with CasMATE (PDB 5YCK). Rwork/Rfree = 0.265/0.313. SPring-8 BL32XU beamline. |


## Biological / Functional Insights

### TM7 conformational transitions

Comparing Mol-A and Mol-B, TM7 shows the highest RMSD among all transmembrane helices (1.671 A). Unlike CasMATE and AtDTX14 where TM7 bends around G255-P257, NtMATE2 TM7 undergoes an overall arrangement change without alpha-helix bending. Mol-B (outward-releasing form) has an elongated electron density near N316/TM8 and E285/TM7, suggesting a substrate-binding pocket surrounded by Y288, F289, F320, Y430, and W453. The conserved Asp in TM10 of CasMATE/AtDTX14 is replaced by Asn403 in NtMATE2, which may form a hydrogen bond with E285.

### C-lobe substrate binding pocket

The negatively charged C-lobe cavity provides a binding site for positively charged alkaloid molecules like nicotine. In Mol-B, an unidentified electron density near E285/TM7 and N316/TM8 may partially mimic nicotine. The phosphate ion observed in Mol-A N-lobe cavity (between TM1 and TM2) is likely derived from the crystallization buffer.


## Cross-References

- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Primary crystallization method
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Initial solubilization detergent
- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — Maintenance detergent during purification
- [BRIL Fusion Protein](/xray-mp-wiki/reagents/protein-tags/bril/) — Related thermostabilization strategy for GPCRs
