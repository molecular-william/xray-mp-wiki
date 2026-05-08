---
title: AcrB Efflux Pump
created: 2026-05-05
updated: 2026-05-05
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1007##s10969-013-9154-x]
---

# AcrB Efflux Pump

## Overview

AcrB (Acriflavine resistance protein B) is the inner membrane component of the AcrAB-TolC tripartite multidrug efflux system in Escherichia coli. It functions as a proton/drug antiporter that extrudes a wide variety of cytotoxic substances including antibiotics, organic solvents, dyes, and detergents from the cell. AcrB is the most well-studied resistance-nodulation-division (RND) family efflux pump and plays a central role in multidrug resistance in Gram-negative bacteria. The protein forms a symmetric trimer with each protomer containing 12 transmembrane helices and two periplasmic domains (porter and TolC-binding domains).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1007##s10969-013-9154-x | 4K7Q | 3.5 A | R32 | Wild-type AcrB with C-terminal polyhistidine tag | Linezolid |

## Expression and Purification

- **Expression system**: E. coli JM109
- **Construct**: Wild-type AcrB with C-terminal polyhistidine tag (pAcBH plasmid)

### Purification Workflow

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell disruption | Microfluidizer | -- | not specified | Membrane fractions collected by ultracentrifugation at 150,000g for 90 min |
| Solubilization | Detergent solubilization | -- | 50 mM Tris-HCl pH 7.0, 10% glycerol, 2% DDM | Lipids and debris removed by ultracentrifugation at 170,000g for 60 min |
| Affinity chromatography | Metal affinity chromatography (Ni-NTA) | Ni-NTA | 20 mM Tris-HCl pH 7.5, 0.3 M NaCl, 10% glycerol, 0.2% DDM | Washed with 25 and 100 mM imidazole; eluted with 300 mM imidazole; imidazole removed by concentration-dilution |
| Concentration | Ultrafiltration | -- | 20 mM sodium phosphate pH 6.2, 10% glycerol, 0.2% DDM | Concentrated to 28 mg/mL; frozen in liquid nitrogen |


## Crystallization

### doi/10.1007##s10969-013-9154-x

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | AcrB in 20 mM sodium phosphate pH 6.2, 10% glycerol, 0.2% DDM at 28 mg/mL |
| Reservoir | 0.1 M NaCl, Na-phosphate pH 6.2, 8% PEG 4000 |
| Cryoprotection | Cryosolvent with crystallization reagents plus 25% glycerol; crystals soaked with 6 mM Linezolid for 10 min at 21 C before flash cooling at 100 K |
| Notes | Apo-AcrB crystals soaked with Linezolid (30 mM stock in water, 6 mM final) prior to data collection |


## Biological / Functional Insights

### Linezolid binding site

Each protomer of the symmetric AcrB trimer binds one Linezolid molecule on the wall of the upper portion of the central cavity near residues A385 and F386. The three rings of the Linezolid molecule lie approximately parallel to the F386 binding loop, allowing maximum hydrophobic contact. The binding interface buries approximately 140 A^2 of Linezolid surface. This binding mode is the same as observed for ethidium, nafcillin, and ampicillin in earlier AcrB structures.

### Conformational change upon ligand binding

A significant local conformational difference at residues 670-675 was observed compared to apo-AcrB structure. These residues reside in a loop lining the bottom of the cleft in the porter domain, thought to be important for substrate transport and AcrA binding. Backbone position differs by up to 4 A in this region while overall RMSD is only 0.4 A.


## Cross-References

- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary solubilization detergent at 2% for membrane extraction
- [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) — Crystallization precipitant (PEG 4000) in sitting-drop vapor diffusion
- [Linezolid](/xray-mp-wiki/reagents/ligands/linezolid/) — Co-crystallized ligand bound to A385/F386 loop
