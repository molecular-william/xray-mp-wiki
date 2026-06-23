---
title: "Bacillus halodurans YidC2 (BhYidC2)"
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein]
sources: [doi/10.1038##nature13167]
verified: false
---

# Bacillus halodurans YidC2 (BhYidC2)

## Overview

YidC is a conserved membrane protein insertase that inserts its substrates into the membrane, thereby facilitating membrane protein assembly in bacteria. The 2.4 Å crystal structure of Bacillus halodurans YidC2 reveals a novel fold with five conserved transmembrane helices forming a positively charged hydrophilic groove that is open towards both the lipid bilayer and the cytoplasm but closed on the extracellular side. The conserved arginine residue R72 in the groove is critical for substrate recognition and membrane protein insertion. YidC functions as both a Sec-independent insertase and a Sec-dependent membrane chaperone.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature13167 | 3W06 | 2.4 |  | B. halodurans YidC2 residues 27-266 | None |
| doi/10.1038##nature13167 | 3W07 | 2.4 |  | B. halodurans YidC2 residues 27-267 (with GFP tag) | None |

## Expression and Purification

- **Expression system**: Escherichia coli C41(DE3) + pRARE
- **Construct**: B. halodurans YidC2 residues 1-266 (or 1-267) with N-terminal His8 tag or GFP-His8 tag, cleaved by TEV protease

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane solubilization | Detergent solubilization | — | 300 mM NaCl, 20 mM Tris-HCl pH 8.0, 20 mM imidazole, 1% DDM, 0.1% CHS |  |
| Affinity purification | Ni-NTA affinity chromatography | Ni-NTA Superflow | 300 mM NaCl, 20 mM Tris-HCl pH 8.0, 20 mM imidazole, 0.1% DDM, 0.01% CHS |  |
| TEV cleavage | Protease cleavage and reverse Ni-NTA | — |  | His-tagged TEV protease used to cleave tags; flow-through collected |
| Gel filtration | Size-exclusion chromatography | Superdex 200 10/300 GL | 300 mM NaCl, 20 mM Tris-HCl pH 8.0 |  |


## Crystallization

### doi/10.1038##nature13167

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | Purified YidC in 300 mM NaCl, 20 mM Tris-HCl pH 8.0, mixed with monoolein (2:3 protein:lipid w/w) |
| Notes | Protein-lipid mixture (50 nl) overlaid with 800 nl precipitant solution. Crystals grown at 20°C. Structure determined by multi-wavelength anomalous diffraction using methyl-mercury-chloride-derivatized YidC (Y150C mutant). Diffraction data at SPring-8 BL32XU. |


## Biological / Functional Insights

### Hydrophilic groove mechanism for membrane protein insertion

YidC contains a positively charged hydrophilic groove (~2,000 Å³) formed by TM1-5. The groove contains conserved hydrophilic residues (T68, R72, Q82, Q142, Q187, N248, Q254) and is filled with ~20 water molecules. The conserved R72 creates a strong positive electrostatic potential. The groove is open to the cytoplasm and membrane interior but sealed on the extracellular side by a rigid hydrophobic core. Substrate proteins with acidic N-terminal extracellular regions are transiently captured in this groove.

### C1 region function

The C1 region (cytosolic domain between TM2 and TM3, containing CH1 and CH2 helices) is crucial for YidC-mediated membrane insertion of single-spanning membrane proteins like MifM. Deletion mutants of the C1 region substantially impair insertion activity.

### Substrate recognition via electrostatic interactions

The conserved arginine R72 in the groove interacts with acidic residues in the N-terminal extracellular tails of substrates such as MifM and Pf3 coat protein. In vivo photo-crosslinking using pBpa introduced at Q187 and W244 in the groove confirmed direct substrate binding at the groove.


## Cross-References
