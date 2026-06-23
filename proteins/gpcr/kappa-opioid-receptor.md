---
title: Kappa Opioid Receptor
created: 2026-05-27
updated: 2026-06-21
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature11111, doi/10.1016##j.cell.2017.12.011, doi/10.1038##s41467-020-14889-7, doi/10.1038##s41467-023-37041-7, doi/10.1038##nature10939]
verified: false
---

# Kappa Opioid Receptor

## Overview

The human kappa opioid receptor (KOP) is a class A G-protein coupled receptor (GPCR) that mediates the actions of opioids with hallucinogenic, dysphoric, and analgesic activities. Multiple crystal structures have been solved: the inactive-state structure with JDTic alone (PDB 4DJH, 2.9 A), the active-state structure with MP1104 and Nb39 (PDB 6B73, 3.1 A), the Nb6-stabilized inactive-state with JDTic, and the nalfurafine-bound structure with Nb39 (3.3 A).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature10939 | 4DJH | 2.9 | C2 | Kappa-OR-T4L fusion (T4L inserted at ICL3 between Gly261 and Arg263), N-terminal deletion Delta Glu2-Ala42, C-terminal deletion Delta Arg359-Val380, I135L point mutation | JDTic |
| doi/10.1016##j.cell.2017.12.011 | 6B73 | 3.1 | P21 | BRIL-fused KOP (truncated 7TM) | MP1104, Nb39 |
| doi/10.1038##s41467-023-37041-7 |  | 3.3 | — | BRIL-fused KOP (truncated 7TM) with S324C thermostabilizing mutation | Nalfurafine, Nb39 |

## Expression and Purification

- **Expression system**: Spodoptera frugiperda Sf9 insect cells
- **Construct**: Kappa-OR with N-terminal HA signal sequence, Flag tag, 10xHis tag, and TEV protease recognition site; T4L fused in ICL3; N-terminal Delta Glu2-Ala42 and C-terminal Delta Arg359-Val380 truncations; I135L mutation
- **Notes**: Baculovirus expression system used. 25 uM naltrexone (NTX) and 5% Protein Boost Additive added during expression.

### Purification Workflow

*Source: doi/10.1038##nature10939*

- **Expression system**: Sf9 insect cells (baculovirus)
- **Expression construct**: Kappa-OR-T4L with N-terminal HA-Flag-10xHis-TEV tag, N/C-terminal truncations, I135L mutation
- **Tag info**: N-terminal HA-Flag-10xHis tag, cleavable by TEV protease

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Centrifugation | — | Hypotonic buffer (10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl, protease inhibitors); high osmotic buffer (1.0 M NaCl, 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl, protease inhibitors) + — | Thawed in hypotonic buffer, washed 2-3x in hypotonic buffer, then 3-4x in high osmotic buffer |
| Alkylation and ligand incubation | Pre-incubation | — | 40 uM NTX, 2 mg/ml iodoacetamide, 150 mM NaCl, protease inhibitors + — | 1 h at 4 °C before solubilization |
| Solubilization | Detergent solubilization | — | 50 mM HEPES pH 7.5, 150 mM NaCl + 1% (w/v) detergent (DDM/CHS likely) | — |

### Purification Workflow

*Source: doi/10.1016##j.cell.2017.12.011*

- **Expression system**: Sf9 cells (baculovirus)
- **Expression construct**: BRIL-fused KOP with C-terminal His-tag
- **Tag info**: C-terminal hexa-His tag on BRIL

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell harvest | Centrifugation | — | — + — | Sf9 cells harvested 48 h post-infection, washed in 1x PBS, stored at -80 C. 10 uM naltrexone added to help receptor trafficking. |
| Membrane preparation | Repeated centrifugation | — | 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl, 500 uM AEBSF, 1 uM E-64, 1 uM leupeptin, 150 nM Aprotinin (low-salt); 1.0 M NaCl, 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl (high osmolarity) + — | 4 repeated centrifugations in high osmolarity buffer to remove soluble and membrane-associated proteins. |
| Solubilization | Detergent solubilization | — | 10 mM HEPES pH 7.5, 100 mM NaCl + 0.05% DDM, 0.2 mg/mL CHS | Membranes resuspended and solubilized by gentle stirring. |
| Affinity purification | Cobalt affinity chromatography | TALON IMAC resin (Clontech) | 10 mM HEPES pH 7.5, 100 mM NaCl, 20 mM imidazole (wash); 250 mM imidazole (elution) + 0.01% DDM | Supernatant incubated with TALON resin, washed, eluted with imidazole. |
| TEV protease cleavage | Proteolytic cleavage | — | 10 mM HEPES pH 7.5, 100 mM NaCl + 0.01% DDM | TEV protease added overnight at 4 C to cleave His-tag from BRIL. |
| Reverse TALON purification | Pass-through chromatography | TALON IMAC resin | 10 mM HEPES pH 7.5, 100 mM NaCl + 0.01% DDM | Flow-through collected containing cleaved BRIL-KOP complex. |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex 200 Increase 10/300 GL | 10 mM HEPES pH 7.5, 100 mM NaCl + 0.01% DDM | Final purification step to isolate monodisperse complex. |

**Final sample**: BRIL-KOP-MP1104-Nb39 complex, 10-15 mg/mL in 10 mM HEPES pH 7.5, 100 mM NaCl, 0.01% DDM, stored at -80 C with 10% glycerol

### Purification Workflow

*Source: doi/10.1038##s41467-023-37041-7*

- **Expression system**: Sf9 cells (baculovirus)
- **Expression construct**: BRIL-fused KOP (truncated 7TM) with S324C mutation, C-terminal His-tag
- **Tag info**: C-terminal hexa-His tag on BRIL

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and membrane preparation | Baculovirus infection of Sf9 cells | — | 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl, protease inhibitors; high-salt wash (1.0 M NaCl, 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl) + — | Cells harvested 48 h post-infection; membranes washed 4x in high-salt buffer. |
| Ligand incubation and alkylation | Pre-incubation with ligand | — | 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl, 150 mM NaCl, 50 uM nalfurafine, protease inhibitors + — | Incubated 1 h RT, then 30 min at 4 C; 2 mg/mL iodoacetamide added for 30 min alkylation. |
| Solubilization | Detergent solubilization | — | 10 mM HEPES pH 7.5, 150 mM NaCl, protease inhibitors + 1% DDM, 0.2% CHS | 2 h at 4 C; clarified at 150,000 x g for 30 min. |
| TALON IMAC affinity | Cobalt affinity chromatography | TALON IMAC resin (Clontech) | Wash I: 50 mM HEPES pH 7.5, 800 mM NaCl, 20 mM imidazole, 10% glycerol, 25 uM nalfurafine; Wash II: 25 mM HEPES pH 7.5, 150 mM NaCl, 10% glycerol, 25 uM nalfurafine + Wash I: 0.1% DDM, 0.02% CHS; Wash II: 0.05% DDM, 0.01% CHS | Resin incubated with supernatant overnight at 4 C; washed with 10 CV Wash I then 10 CV Wash II; eluted with 250 mM imidazole. |
| TEV protease cleavage | Proteolytic cleavage | — | 25 mM HEPES pH 7.5, 150 mM NaCl, 10% glycerol + 0.05% DDM, 0.01% CHS | His-tagged TEV protease added overnight at 4 C to remove N-terminal 10x His-tag. |
| Reverse TALON purification | Pass-through chromatography | TALON IMAC resin | 25 mM HEPES pH 7.5, 150 mM NaCl, 10% glycerol + 0.05% DDM, 0.01% CHS | Flow-through collected to remove TEV protease, cleaved His-tag, and uncleaved protein. |
| Nb39 complex formation | Complex formation | — | 25 mM HEPES pH 7.5, 150 mM NaCl, 10% glycerol + 0.05% DDM, 0.01% CHS | Incubated with excess Nb39 (KOR/Nb39 1:2 molar ratio) for 3 h; concentrated to ~30 mg/mL using 100 kDa MWCO concentrator. |

**Final sample**: KOR-nalfurafine-Nb39 complex at ~30 mg/mL in 25 mM HEPES pH 7.5, 150 mM NaCl, 0.05% DDM, 0.01% CHS, 10% glycerol


## Crystallization

### doi/10.1038##nature10939

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | Kappa-OR-T4L-JDTic complex |
| Lipid | Monoolein |
| Protein-to-lipid ratio | — |
| Temperature | — |
| Growth time | — |
| Cryoprotection | — |
| Notes | Crystallized using LCP method as described in Caffrey & Cherezov (2009). Data collected at APS. |

### doi/10.1016##j.cell.2017.12.011

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | BRIL-KOP-MP1104-Nb39 complex at 10-15 mg/mL |
| Lipid | Monoolein |
| Protein-to-lipid ratio | — |
| Temperature | — |
| Growth time | — |
| Cryoprotection | — |
| Notes | Crystals grown in LCP. Data collected at APS GM/CA CAT 23ID-B/D. |

### doi/10.1038##s41467-023-37041-7

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | KOR-nalfurafine-Nb39 complex at ~30 mg/mL |
| Lipid | Monoolein |
| Protein-to-lipid ratio | — |
| Temperature | — |
| Growth time | — |
| Cryoprotection | — |
| Notes | Crystals grown in LCP. |


## Biological / Functional Insights

### JDTic Binding and Subtype Selectivity

The crystal structure of KOR in complex with the selective antagonist JDTic (PDB 4DJH, 2.9 A) reveals the structural basis for high affinity and subtype selectivity. JDTic adopts a V-shaped conformation, anchoring via two amino groups to Asp1383.32. Four residues differing among opioid receptor subtypes contribute to selectivity: Val1082.53, Val1182.63, Ile2946.55, and Tyr3127.35. JDTic achieves >1000-fold selectivity for KOR via these residue differences, without requiring the 'address' interaction with Glu2976.58 utilized by morphinan-based antagonists.

### Salvinorin A Binding

Docking studies of the diterpene agonist salvinorin A analogue RB-64 into the KOR structure reveal that the thiocyanate group of RB-64 can react with Cys3157.38 to form covalent adducts, consistent with SCAM and SAR studies. SalA is unique among KOR ligands in lacking a charged nitrogen atom.

### MP1104 Binding Pocket and Hydrophobic Interactions

MP1104 binds in the orthosteric pocket of active-state KOP with its cyclopropylmethyl group extending into a hydrophobic pocket formed by W2876.48, G3197.42, and Y3207.43. The iodobenzamide moiety forms a water-mediated hydrogen bond with Y3127.35. Mutations W2876.48L, G3197.42L, and Y3207.43L strongly reduce MP1104 potency for both G protein activation and beta-arrestin2 recruitment.

### KOP Activation Mechanism and Signal Propagation

Activation-related conformational changes propagate from the orthosteric site: (1) The D3.32YYNM3.36 anchoring motif in TM3 rearranges. (2) The CWxP motif residue W2876.48 couples to the P5.50-I3.40-F6.44 toggle switch, promoting F2836.44 rotation. (3) TM6 outward displacement of ~10 A opens the intracellular surface. (4) The sodium pocket between TM2/TM3/TM7 collapses. (5) The NPxxY motif and DRY motif undergo characteristic rearrangements.

### Nb6 Stabilizes a Distinct Inactive State

The KOR-JDTic-Nb6 complex structure revealed Nb6 binds at the intracellular interface between TM5 and TM6. R102 in Nb6 forms ionic interactions with D2666.27 and R2706.31. Unlike beta2AR-Nb60, KOR uses R3.50 forming two H-bonds with T2.39 and T6.34 to stabilize the inactive conformation.

### Nalfurafine-Bound KOR Structure and Biased Signaling

The nalfurafine-bound KOR structure (3.3 A) revealed nalfurafine adopts a reversed V-shaped conformation. The furan ring extends into a crevice between TM1 and TM2. The S3247.47C mutation increased receptor stability. MD simulations identified three active-state conformations, including an occluded state that explains G protein bias.

### Ligand-Specific Determinants of Signaling Bias

Nalfurafine destabilizes the K2275.39-E2976.58 salt bridge. W2876.48A selectively reduces nalfurafine-mediated arrestin recruitment. TRUPATH profiling showed KOR activates multiple G protein subtypes (Gi1, Gi2, Gi3, GoA, GoB, Gz, Gustducin).


## Cross-References

- [JDTic](/xray-mp-wiki/reagents/ligands/jdtc/) — Selective antagonist co-crystallized with KOR in PDB 4DJH
- [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) — Fusion partner used in crystallization constructs
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for solubilization and crystallization
- [MP1104](/xray-mp-wiki/reagents/ligands/mp1104/) — Co-crystallized agonist in PDB 6B73
- [Nalfurafine](/xray-mp-wiki/reagents/ligands/nalfurafine/) — G protein-biased KOR agonist co-crystallized in the 2023 structure
- [GPCR Biased Signaling](/xray-mp-wiki/concepts/gpcr-biased-signaling/) — The occluded state mechanism explains G protein bias at KOR
- [NPxxY Motif](/xray-mp-wiki/concepts/structural-mechanisms/npxxy-motif/) — Important functional motif in KOR activation
- [Beta-Arrestin](/xray-mp-wiki/concepts/signaling-receptors/beta-arrestin/) — Key signaling pathway for KOR
- [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) — Expression system used for KOR production
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Purification method used for KOR
