---
title: "Synechocystis Halorhodopsin (SyHR)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-022-34019-9]
verified: false
---

# Synechocystis Halorhodopsin (SyHR)

## Overview

Synechocystis [Halorhodopsin (HR) from Halobacterium salinarum](/xray-mp-wiki/proteins/rhodopsins/halorhodopsin/) (SyHR) is a light-driven anion pump from the cyanobacterium Synechocystis sp. PCC 7509. It belongs to a clade of cyanobacterial anion-pumping [Microbial Rhodopsins](/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/) characterized by the TSD motif (T74, S78, D85 in helix C). SyHR is the only known natural microbial rhodopsin proposed to pump divalent anions such as sulfate in addition to monovalent halides like chloride. The protein functions as an inward Cl- pump and has potential as a next-generation optogenetics tool due to its high chloride affinity (Kd 0.112 mM) and ability to pump against strong concentration gradients. SyHR forms trimers in lipid membranes and contains a [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore covalently bound to K205 via a Schiff base.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-022-34019-9 | 7ZOU | 1.57 | P 3 2 1 | Synechocystis [Halorhodopsin (HR) from Halobacterium salinarum](/xray-mp-wiki/proteins/rhodopsins/halorhodopsin/) (residues 1-225 of 234), C-terminal 6xHis tag | chloride ion in RSB region |
| doi/10.1038##s41467-022-34019-9 | 7ZOV | 1.57 | P 3 2 1 | Synechocystis [Halorhodopsin (HR) from Halobacterium salinarum](/xray-mp-wiki/proteins/rhodopsins/halorhodopsin/) (residues 1-225 of 234), C-terminal 6xHis tag | sulfate ion (surface-bound, not in RSB region) |
| doi/10.1038##s41467-022-34019-9 | 7ZOW | 1.7 | P 3 2 1 | Synechocystis [Halorhodopsin (HR) from Halobacterium salinarum](/xray-mp-wiki/proteins/rhodopsins/halorhodopsin/) (residues 1-225 of 234), C-terminal 6xHis tag | K-state intermediate ([Retinal](/xray-mp-wiki/reagents/ligands/retinal/) in 6-s-cis, 12-s-cis configuration) |
| doi/10.1038##s41467-022-34019-9 | 7ZOY | 1.6 | P 3 2 1 | Synechocystis [Halorhodopsin (HR) from Halobacterium salinarum](/xray-mp-wiki/proteins/rhodopsins/halorhodopsin/) (residues 1-225 of 234), C-terminal 6xHis tag | O-state intermediate (anion-free) |

## Expression and Purification

- **Expression system**: Escherichia coli C41
- **Construct**: Codon-optimized SyHR gene (accession WP_009632765) in pET system with C-terminal 6xHis tag
- **Notes**: Autoinducing ZYP-5052 medium; 10 uM all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) added when [Glucose](/xray-mp-wiki/reagents/additives/glucose/) dropped below 10 mg/L; incubated at 20 C overnight

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell disruption | High-pressure homogenization | not specified | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.5% Triton X-100, 50 mg/L DNase I + 0.5% Triton X-100 | Disrupted at 172.3 MPa; membrane fraction isolated by ultracentrifugation at 90,000g for 1h |
| Solubilization | Detergent solubilization | not specified | 50 mM NaH2PO4/Na2HPO4 pH 8.0, 0.1 M NaCl + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Stirred overnight; centrifuged at 90,000g for 1h |
| IMAC purification | Nickel-nitrilotriacetic acid [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA column (Qiagen) | 50 mM NaH2PO4/Na2HPO4 pH 7.5, 0.2 M NaCl, 0.5 M [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Eluted in imidazole-containing buffer |
| Size-exclusion chromatography | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) prep grade 125 mL column (GE Healthcare) | 50 mM NaH2PO4/Na2HPO4 pH 7.5, 0.2 M NaCl, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Protein-containing fractions pooled and concentrated to 60 mg/mL |


## Crystallization

### doi/10.1038##s41467-022-34019-9

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (in meso) |
| Protein sample | SyHR at 20 mg/mL in lipidic mesophase ([Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/)) |
| Temperature | 20 C |
| Notes | Hexagonal crystals grown over 2 months; reached 150 um in length and width. Red crystals cryoprotected in 1.6 M Ammonium Phosphate pH 4.6, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/). Violet crystals cryoprotected in 2.0 M [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/), 0.1 M HEPES pH 7.0, 15% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/). Flash-cooled in liquid nitrogen. |


## Biological / Functional Insights

### Unique retinal isomerization in K state

The K state intermediate of SyHR reveals a unique 6-s-cis, 12-s-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) configuration never previously observed in [Microbial Rhodopsins](/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/). This isomerization causes the polyene chain to rotate 180 degrees from atoms C7 to C12, shifting C20 by 1.7 A toward L82 and the beta-ionone ring by almost 2 A toward the cytoplasmic side. W75 rotates 10 degrees and L82 reorients to accommodate the cofactor. This suggests a unique primary photochemical reaction in SyHR.

### Chloride release pathway through H167

SyHR contains a unique histidine residue H167 in helix F, absent in archaeal HRs and bacterial Cl- pumps. Two internal cavities (IC1 and IC2) near H167 form the putative chloride release pathway to the cytoplasm. IC2 is unique to SyHR and is a compact hydrophilic cavity filled by two water molecules coordinated by N104, T137, and H167. The mutation of the corresponding histidine in MrHR (H166A) dramatically decelerates L and N state decay, confirming H167's role in ion release.

### Sulfate pumping mechanism

SyHR's unique ability to pump sulfate is attributed to a large extracellular cavity serving as an ion uptake vestibule. The cavity protrudes from the extracellular space through a pore to R71. The key determinant is T183 at the cavity entrance; in MrHR, the bulky E182 blocks sulfate access. Mutating E182 to T or A in MrHR enables sulfate pumping, with E182A pumping even more efficiently than SyHR-like E182T. The larger cavities in SyHR compared to MrHR near H167 also facilitate translocation of the bulky divalent sulfate anion.


## Cross-References

- [Microbial Rhodopsins](/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Halorhodopsin (HR) from Halobacterium salinarum](/xray-mp-wiki/proteins/rhodopsins/halorhodopsin/) — Related protein structure
- [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/) — Additive used in purification or crystallization buffers
- [Glucose](/xray-mp-wiki/reagents/additives/glucose/) — Additive used in purification or crystallization buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) — Additive used in purification or crystallization buffers
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component in purification or crystallization
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used in purification or crystallization
