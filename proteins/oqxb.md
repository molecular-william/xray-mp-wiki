---
title: OqxB efflux pump from Klebsiella pneumoniae
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-021-25679-0]
verified: false
---

# OqxB efflux pump from Klebsiella pneumoniae

## Overview

OqxB is a Resistance-Nodulation-Division (RND) efflux pump from *Klebsiella pneumoniae* that contributes to multidrug antibiotic resistance. OqxB underwent horizontal gene transfer and is now found in other Gram-negative bacterial pathogens including *Escherichia coli*, *Enterobacter cloacae*, and *Salmonella* spp. It confers resistance against fluoroquinolones, nitrofurantoin, quinoxalines, tigecycline, and chloramphenicol. The crystal structure at 1.85 Angstrom resolution reveals a symmetric trimer wherein all three protomers adopt a binding/tight conformation, unlike the asymmetric trimers observed in other RND pumps (AcrB, MexB). Each protomer contains two bound DDM molecules in the substrate-binding pocket. A unique charged arginine residue R157 in the substrate-binding pocket, absent in AcrB and MexB, forms hydrogen bonds with substrates and is critical for fluoroquinolone binding and efflux. The longer gate loop (g-loop) with two proline residues and a unique phenylalanine cage architecture distinguish OqxB from related pumps. Functional complementation assays demonstrated 8- to 16-fold increased MIC for fluoroquinolones upon OqxB expression, and the R157A mutant showed 4- to 8-fold improved MIC, validating the structural predictions.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-021-25679-0 | 7L0Q | 1.85 | P 65 2 2 | OqxB (residues 1-977) symmetric trimer | DDM (2 molecules per protomer) |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: OqxB (residues 1-977) with C-terminal hexa-histidine tag, cloned into modified pET-22b vector
- **Notes**: Expressed in E. coli C43(DE3) at 25 C for 8 hours with 0.1 mM IPTG induction at A600nm of 0.6

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1 | Cell lysis by Microfluidizer | — | 50 mM Tris-HCl pH 7.0, 0.5 mM Na-EDTA, 1 mM MgCl2 | 3 passes at 15,000 psi. Membrane fraction collected by ultracentrifugation |
| 2 | Solubilization | — | 50 mM Tris-HCl pH 7.0, 300 mM NaCl + DDM | Solubilized from membrane fraction |
| 3 | Affinity chromatography (Ni-NTA) | Ni-NTA Superflow (Qiagen) | 50 mM Tris-HCl pH 7.0, 300 mM NaCl, 250 mM imidazole + DDM | His6-tag purification |
| 4 | Size-exclusion chromatography | — | 20 mM HEPES pH 7.5, 150 mM NaCl + DDM | Final polishing step for crystallization |


## Crystallization

### doi/10.1038##s41467-021-25679-0

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, sitting drop |
| Protein sample | OqxB purified in DDM at ~10 mg/mL |
| Reservoir | 0.1 M sodium citrate pH 5.5, 0.1 M Li2SO4, 0.1 M NaCl, 20 mM MgCl2, 34% PEG400, 5 mM ATP |
| Temperature | 293 |
| Notes | Symmetric trimer structure with DDM molecules bound in substrate pocket |


## Biological / Functional Insights

### Unique charged residue R157 in substrate-binding pocket

R157 is a unique positively charged arginine residue in the OqxB substrate-binding pocket that is absent in related pumps AcrB and MexB (which have a small hydrophilic serine at the equivalent position). R157 forms hydrogen bond interactions with the DDM molecule and is proposed to interact with zwitterionic fluoroquinolone antibiotics through its guanidino side chain. Molecular docking and MD simulations showed that ciprofloxacin interacts with R157, forming stable hydrogen bonds (>80% occupancy) between the fluoroquinolone carboxyl and carbonyl groups. The R157A mutation reduced efflux liability for fluoroquinolones by 4- to 8-fold, confirming its critical role in drug binding and efflux.

### Extended gate loop and phenylalanine cage

The OqxB gate loop (g-loop) is longer by two residues (16 vs. 14) than AcrB and MexB, containing two proline residues (P619 and P630) on either side of the loop. The conserved phenylalanine residues (F615 and F617) in AcrB and MexB g-loops are replaced with L621 and A623 in OqxB. This is compensated by F626, which swings back toward the substrate-binding pocket, contributing to the unique phenylalanine cage architecture. These structural differences are responsible for the distinct binding mode of DDM molecules in OqxB compared to MexB.


## Cross-References
