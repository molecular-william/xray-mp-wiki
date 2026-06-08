---
title: Human Adenosine A2A Receptor A2A-StaR2-S277-bRIL (PDB 8CU6)
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1021##acs.jmedchem.2c00462]
verified: false
---

# Human Adenosine A2A Receptor A2A-StaR2-S277-bRIL (PDB 8CU6)

## Overview

The A2A-StaR2-S277-bRIL construct is an engineered human adenosine A2A receptor with the S277A point mutation in addition to the nine StaR2 thermostabilizing mutations (A54L, T88A, R107A, K122A, N154A, L202A, L235A, V239A, S277A), N-terminal deletion, C-terminal truncation after residue 315 with a His10 tag, and apocytochrome b562 RIL (bRIL) fused into the third intracellular loop. The S277A mutation prevents hydrogen bonding with His278(7.43), which is critical for agonist-induced activation, making this construct ideal for studying nucleoside antagonist binding. The crystal structure (PDB 8CU6, 2.80 A) was solved in complex with the nucleoside antagonist LJ-4517 (compound 2).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1021##acs.jmedchem.2c00462 | 8CU6 | 2.80 A | not specified | A2A-StaR2-S277-bRIL: human A2AR with StaR2 mutations including S277A, N-terminal deletion, C-terminal truncation after L315 with His10 tag, bRIL fused into ICL3 (L208-G218)
 | LJ-4517 (compound 2) |

## Expression and Purification

- **Expression system**: CHO cells
- **Construct**: A2A-StaR2-S277-bRIL: human adenosine A2A receptor with StaR2 mutations including S277A, N-terminal deletion, C-terminal truncation after L315 with His10 tag, bRIL fusion in ICL3


### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and membrane preparation | CHO cell expression; membranes harvested and washed in hypertonic buffers (10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl, 1 M NaCl) | -- | 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl, 1 M NaCl + -- | Membranes washed three times in hypertonic buffer; incubated in hypotonic buffer with 2 mg/mL iodoacetamide and 2 mM theophylline for 20 min at 4 C |
| Solubilization | Membranes solubilized with 2x solubilization buffer containing DDM and CHS for 2.5 h | -- | 100 mM HEPES pH 7.5, 250 mM NaCl, 0.5% DDM, 0.05% CHS + 0.5% DDM, 0.05% CHS | Solubilization for 2.5 h; unsolubilized membranes removed by centrifugation at 60,000g for 50 min at 4 C |
| IMAC affinity chromatography | Incubated overnight with Talon (IMAC) resin in presence of 150 mM NaCl and 20 mM imidazole | Talon (IMAC) resin | 50 mM HEPES pH 7.5, 150 mM NaCl, 20 mM imidazole + 0.05% DDM, 0.01% CHS | Overnight incubation at 4 C with 1 mL Talon resin |
| Column wash and elution | Gravity column wash with wash buffer 1 (800 mM NaCl, 25 mM imidazole) and wash buffer 2 (150 mM NaCl, 50 mM imidazole), eluted with 250 mM imidazole | Talon (IMAC) | 50 mM HEPES pH 7.5, 150 mM NaCl, 250 mM imidazole + 0.025% DDM, 0.005% CHS | Washed with 10 cv wash buffer 1, 5 cv wash buffer 2, eluted in 3 cv elution buffer; concentrated to 20 uL using 100 kDa Amicon filter |


## Crystallization

### doi/10.1021##acs.jmedchem.2c00462

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | A2A-StaR2-S277-bRIL in complex with LJ-4517 (30 mg/mL) |
| Lipid | Monoolein/cholesterol (9:1 w/w) |
| Protein-to-lipid ratio | 2:3 (v/v) protein to lipid |
| Temperature | not specified |
| Growth time | Crystals appeared within 2 days, maximum size 15 x 10 x 2 um |
| Cryoprotection | Flash-frozen in liquid nitrogen |
| Notes | Crystals harvested directly from LCP using 50 um microcounts (MiTeGen) and flash-frozen. Data collected at 23ID-B beamline of the Advanced Photon Source, Argonne, IL, equipped with Dectris Eiger 16M detector.
 |


## Biological / Functional Insights

### S277A mutation enables nucleoside antagonist binding

The S277A mutation prevents the ribose-like moiety of nucleoside ligands from forming a stable hydrogen bond with His278(7.43). In the presence of the C8-thiophene group on LJ-4517, this mutation restricts receptor conformational rearrangements required for activation, converting the nucleoside from an agonist to an antagonist. Direct hydrogen bonding between the ligand and His278(7.43) occurs in only ~5% of MD simulation time points, with water-mediated bonding in ~41% of snapshots.

### Thiophene exosite extension

The n-hexynyl group of LJ-4517 extends into an A2AAR exosite, while the C8-thiophene group occupies a hydrophobic subpocket in the bottom part of the ligand-binding site. This exosite remains open in the S277-bRIL construct, unlike the ZM241385-bound structure where Tyr271(7.36) switches conformation to close the exosite.

### Structural comparison with agonist-bound A2AAR

The ribose-like moiety conformation in antagonist 2 is altered by steric hindrance from the thiophene group, preventing engagement with both Ser277(7.42) and His278(7.43). This contrasts with the agonist NECA (PDB 2YDV), where the ribose forms stable hydrogen bonds with both residues, enabling activation-related helical rearrangements.


## Cross-References

- [Human Adenosine A2A Receptor A2A-StaR2-bRIL (PDB 7ARO)](/xray-mp-wiki/proteins/a2ar-star2-bril/) — Parent construct without S277A mutation, same bRIL fusion design
- [Human Adenosine A2A Receptor (A2AR)](/xray-mp-wiki/proteins/human-adenosine-a2a-receptor-a2ar/) — A2A-StaR2-S277-bRIL is an engineered mutant of the human A2AR
- [LJ-4517 (Compound 2)](/xray-mp-wiki/reagents/ligands/lj-4517/) — Co-crystallized nucleoside antagonist ligand in PDB 8CU6
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for solubilization and purification
- [Cholesterol Hemisuccinate (CHS)](/xray-mp-wiki/reagents/lipids/cholesterol-hemisuccinate/) — Lipid additive in solubilization and crystallization buffers
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid component of LCP crystallization medium
- [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer used in purification and crystallization
- [Sodium Thiocyanate (NaSCN)](/xray-mp-wiki/reagents/additives/sodium-thiocyanate/) — Crystallization additive in the reservoir solution
