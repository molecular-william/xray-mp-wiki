---
title: 
created: 2026-05-26
updated: 2026-05-26
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##J.MOLCEL.2011.10.020]
verified: false
---

# 

## Overview

Isoprenylcysteine carboxyl methyltransferase (ICMT) catalyzes the final step of CAAX processing, methylating the C-terminal prenylcysteine residue of proteins such as Ras and Rho GTPases. The structure of the prokaryotic ortholog from Methanosarcina acetivorans () reveals a markedly different architecture from conventional [SAM(/xray-mp-wiki/reagents/cofactors/sam/)-dependent methyltransferases.  comprises five transmembrane alpha helices and a C-terminal cytoplasmic alpha helix, with a cofactor-binding pocket enclosed within a conserved C-terminal catalytic subdomain. A substrate access tunnel links the [SAM(/xray-mp-wiki/reagents/cofactors/sam/)-binding pocket to the inner membrane, allowing recognition of both the hydrophilic [SAM](/xray-mp-wiki/reagents/cofactors/sam/) cofactor and the lipophilic prenyl lipid substrate.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##J.MOLCEL.2011.10.020 | 4A2N | 3.4 A | P6222 | [Ma-ICMT](/xray-mp-wiki/proteins/ma-icmt/) (MA2698) from Methanosarcina acetivorans; TEV-cleavable C-terminal GFP-His7 tag | SAH (S-adenosyl-L-homocysteine), endogenous lipid (C9 alkyl chain) |

## Expression and Purification

- **Expression system**: Escherichia coli strain C41(DE3)
- **Construct**: [Ma-ICMT](/xray-mp-wiki/proteins/ma-icmt/) (MA2698) cloned into pTriEX-based plasmid with TEV-cleavable C-terminal GFP-His7 tag (pOPIN-GFP)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Ni-NTA [affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA affinity | Ni-NTA | Lysis buffer with His7 tag elution | Initial purification via C-terminal His7 tag |
| Ion exchange chromatography | Ion exchange | -- | -- | Further purification |
| [Size-exclusion chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | [Size-exclusion chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | -- | 20 mM  pH 6.5, 200 mM NaCl, 10% [glycerol(/xray-mp-wiki/reagents/additives/glycerol/), 0.024% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Final purification step |


## Crystallization

### doi/10.1016##J.MOLCEL.2011.10.020

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample |  at 8 mg/ml in 20 mM [MES(/xray-mp-wiki/reagents/buffers/mes/) pH 6.5, 200 mM NaCl, 10% , 0.024% [DDM(/xray-mp-wiki/reagents/detergents/ddm/) |
| Reservoir | 5 mM SAH (S-adenosyl-L-homocysteine), 0.5 mg/ml polar lipids (Avanti Polar Lipids) |
| Mixing ratio | not specified |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | not specified |
| Notes | Crystals obtained only in presence of SAH cofactor, suggesting cofactor is required for conformational homogeneity |


## Biological / Functional Insights

### Unique integral membrane methyltransferase architecture

Unlike all known aqueous methyltransferases, ICMT is an integral membrane protein with five transmembrane helices. The [SAM](/xray-mp-wiki/reagents/cofactors/sam/) cofactor binding pocket is enclosed within a conserved C-terminal catalytic subdomain, and a substrate access tunnel connects the catalytic site to the inner membrane. The tunnel has a hydrophobic upper region within the membrane (for prenyl lipid access) and a hydrophilic lower region in the cytosol (for the polar protein substrate C terminus).


## Cross-References
