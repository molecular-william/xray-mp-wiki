---
title: Human Angiotensin-Converting Enzyme 2 (hACE2)
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [enzyme, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2020.03.045]
verified: false
---

# Human Angiotensin-Converting Enzyme 2 (hACE2)

## Overview

Human angiotensin-converting enzyme 2 (hACE2) is a membrane-bound zinc metalloprotease that plays a key role in the renin-angiotensin system by converting angiotensin II to angiotensin-(1-7). It also serves as the cellular entry receptor for SARS-CoV and SARS-CoV-2 coronaviruses. The structure of hACE2 reveals an N-terminal peptidase domain that mediates viral spike protein binding.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2020.03.045 | 6LZG | 2.50 A | P41212 | hACE2 residues 19-615, N-terminal peptidase domain in complex with SARS-CoV-2 CTD | SARS-CoV-2 CTD (spike protein residues 319-541) |

## Expression and Purification

- **Expression system**: Sf9 insect cells (baculovirus)
- **Construct**: hACE2 residues 19-615, N-terminal gp67 signal peptide, C-terminal 6xHis tag

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Metal affinity chromatography | Ni-NTA affinity chromatography | HisTrap HP 5 mL column | Buffer not specified + -- | Soluble proteins from Hi5 cell supernatant purified by metal affinity chromatography |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex 200 column | 20 mM Tris-HCl pH 8.0, 150 mM NaCl | Final purification step; samples pooled and concentrated |


## Crystallization

### doi/10.1016##j.cell.2020.03.045

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | SARS-CoV-2 CTD/hACE2 complex, protein concentration 15 mg/ml |
| Reservoir | 0.1 M MES pH 6.5, 10% w/v PEG 5000 MME, 12% v/v 1-propanol |
| Temperature | 18 C |
| Growth time | not specified |
| Cryoprotection | Reservoir solution supplemented with 20% v/v glycerol before flash-cooling in liquid nitrogen |
| Notes | Diffraction data collected at SSRF BL17U (wavelength 0.97919 A) |


## Biological / Functional Insights

### Structural basis for SARS-CoV-2 receptor recognition

The crystal structure of the SARS-CoV-2 CTD in complex with hACE2 at 2.5 A resolution reveals the molecular basis for viral entry. hACE2 binds to the C-terminal domain of the SARS-CoV-2 spike protein via its N-terminal peptidase domain. The binding interface involves extensive hydrophobic contacts and hydrogen bonds between hACE2 residues (including F28, Y41, H34, D38, Y41) and SARS-CoV-2 CTD residues (including Y453, L455, F456, Y489, Q498). The SARS-CoV-2 CTD displays stronger affinity for hACE2 compared to SARS-RBD due to key residue substitutions that slightly strengthen the interaction.

### Comparison of SARS-CoV and SARS-CoV-2 receptor binding

Despite both SARS-CoV and SARS-CoV-2 utilizing hACE2 as their entry receptor, the atomic details at the binding interface demonstrate notable differences. SARS-CoV-2 CTD residue substitutions lead to higher affinity for receptor binding compared to SARS-RBD. The overall binding mode is similar, but key contacts differ at the residue level, explaining the higher infectivity of SARS-CoV-2. The SARS-CoV-2 CTD is antigenically distinct from SARS-RBD, as shown by the inability of SARS-CoV-directed monoclonal and polyclonal antibodies to bind SARS-CoV-2 spike protein.


## Cross-References

- [SARS-CoV-2 Spike Protein C-Terminal Domain](/xray-mp-wiki/proteins/sars-cov-2-ctd/) — Co-crystallized with hACE2 in PDB 6LZG
- [2-(N-Morpholino)ethanesulfonic Acid (MES)](/xray-mp-wiki/reagents/buffers/mes/) — Crystallization buffer at pH 6.5
- [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) — PEG 5000 MME used as crystallization precipitant
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Cryoprotectant (20% v/v) for flash-cooling crystals
- [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/) — 150 mM in SEC purification buffer
- [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) — 20 mM Tris-HCl pH 8.0 in SEC buffer
