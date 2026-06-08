---
title: E. coli MlaC Periplasmic Lipid-Binding Protein
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2017.03.019]
verified: false
---

# E. coli MlaC Periplasmic Lipid-Binding Protein

## Overview

MlaC is a soluble periplasmic lipid-binding protein from Escherichia coli that functions as a shuttle carrier for phospholipids in the Mla lipid transport system. MlaC binds lipid tails in a deep hydrophobic pocket with little head group specificity, allowing it to ferry a wide range of diacyl lipids between the inner membrane MlaFEDB transporter complex and the outer membrane MlaA-OmpC/OmpF complex. MlaC adopts a mixed alpha/beta fold with four beta strands and seven alpha helices. Its structure reveals a deep hydrophobic pocket that binds the two tails of a lipid molecule without interacting with the lipid head group.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2017.03.019 | 5UWA | 2.5 A | P212121 | Mature MlaC, signal peptide-cleaved, residues 22-211, with N-terminal 6xHis tag and TEV protease cleavage site | Phosphatidic acid |

## Expression and Purification

- **Expression system**: E. coli Rosetta2 DE3
- **Construct**: Mature MlaC (residues 22-211), signal peptide-cleaved, cloned into custom pET vector (pBE1092) with N-terminal 6xHis tag and TEV protease cleavage site

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Emulsiflex-C3 cell disruptor, centrifugation at 38,000g | -- | 50 mM Tris pH 8.0, 300 mM NaCl, 10 mM imidazole + -- | Clarified lysate from periplasmic fraction |
| Ni-NTA affinity chromatography | Metal affinity chromatography | Nickel-NTA agarose | 50 mM Tris pH 8.0, 300 mM NaCl, 10 mM imidazole (wash), 250 mM imidazole (elution) + -- | His-tagged MlaC purified from soluble periplasmic fraction |
| Gel filtration | Size-exclusion chromatography on Superdex 200 | Superdex 200 | 20 mM Tris pH 8.0, 150 mM NaCl + -- | Monomeric MlaC eluted as single peak |


## Crystallization

### doi/10.1016##j.cell.2017.03.019

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | MlaC (residues 22-211), concentrated to 10-60 mg/mL |
| Reservoir | 0.1 M citric acid pH 3.5, 1.6 M ammonium sulfate |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | Reservoir solution supplemented with 37.5% ethylene glycol |
| Notes | Phased by molecular replacement using MR-Rosetta homology model based on PDB 2QGU template. Two phosphatidic acid molecules built into electron density in the core of each MlaC monomer in the asymmetric unit. |


## Biological / Functional Insights

### Lipid tail binding pocket with head group independence

MlaC contains a deep hydrophobic pocket that binds the two acyl tails of a lipid
molecule without interacting with the lipid head group. This structural feature
allows MlaC to bind a wide range of diacyl lipids including phosphatidylglycerol
(PG), phosphatidylethanolamine (PE), and cardiolipin-like species. Mass spectrometry
analysis of co-purified lipids confirmed that MlaD, PqiB, and YebT each bind PG
and PE species. The lack of head group specificity supports a model where MlaC
functions as a general lipid shuttle.

### Periplasmic lipid shuttle between inner and outer membrane complexes

MlaC interacts directly with both the inner membrane MlaFEDB transporter complex
and the outer membrane MlaA-OmpC/OmpF complex, as demonstrated by biolayer interferometry
(Octet RED384). MlaC makes no significant interactions with lipid head groups,
suggesting it binds the hydrophobic tails of phospholipids extracted from the inner
membrane and delivers them to the outer membrane. This shuttle mechanism bridges
the periplasmic space between the IM and OM lipid transport complexes.

### MlaC homologs and structural conservation

Two MlaC homologs were previously deposited by the Northeast Structural Genomics
Consortium (NESG): PDB 2QGU from Ralstonia solanacearum (27% sequence identity)
and PDB 4FCZ (22% sequence identity). The 2QGU structure was crystallized with
a ligand modeled as phosphatidylethanolamine. Re-refinement of 4FCZ coordinates
revealed additional electron density in the hydrophobic pocket suggestive of a
tetra-acyl cardiolipin-like lipid. These homologs support the conservation of
MlaC as a lipid-binding protein across bacterial species.


## Cross-References

- [E. coli MlaD MCE Protein](/xray-mp-wiki/proteins/mlaD/) — MlaC ferries lipids between MlaD at the inner membrane and outer membrane complexes
- [E. coli MlaA Outer Membrane Lipoprotein](/xray-mp-wiki/proteins/mlaa/) — MlaC interacts directly with the MlaA-OmpC/OmpF outer membrane complex
- [E. coli YebT Tube-like MCE Protein](/xray-mp-wiki/proteins/yebT/) — YebT binds the same phospholipids (PG, PE) that MlaC shuttles
- [E. coli PqiB Syringe-like MCE Protein](/xray-mp-wiki/proteins/pqiB/) — PqiB binds the same phospholipids (PG, PE) that MlaC shuttles
- [Phosphatidylglycerol](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol/) — MlaC binds PG lipids as part of its lipid shuttle function
- [Phosphatidylethanolamine](/xray-mp-wiki/reagents/lipids/phosphatidylethanolamine/) — MlaC binds PE lipids as part of its lipid shuttle function
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Used for Ni-NTA affinity chromatography wash (10 mM) and elution (250 mM)
- [Citrate Buffer](/xray-mp-wiki/reagents/buffers/citrate/) — 0.1 M citric acid pH 3.5 used in crystallization reservoir
