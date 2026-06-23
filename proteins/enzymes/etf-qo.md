---
title: "Electron Transfer Flavoprotein-Ubiquinone Oxidoreductase (ETF-QO)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.0604567103]
verified: false
---

# Electron Transfer Flavoprotein-Ubiquinone Oxidoreductase (ETF-QO)

## Overview

ETF-QO (Electron Transfer Flavoprotein- Oxidoreductase) is a 4Fe4S flavoprotein located in the inner mitochondrial membrane. It catalyzes  (UQ) reduction by ETF, linking the oxidation of fatty acids and some amino acids to the mitochondrial respiratory chain. The crystal structure of porcine ETF-QO was determined at 2.5 A resolution with bound UQ and at 2.7 A resolution in the UQ-free form. The molecule forms a single structural domain with three functional regions binding [FAD](/xray-mp-wiki/reagents/additives/flavin-adenine-dinucleotide/), the 4Fe4S cluster, and UQ, which are closely packed and share structural elements. The UQ-binding pocket consists mainly of hydrophobic residues, and the flavin-to-UQ distance (8.5 A) is significantly shorter than the cluster-to-UQ distance (18.8 A), suggesting that the flavin, not the cluster, is the direct electron donor to UQ.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.0604567103 | 2GMH | 2.5 A | P42(1)2 | Native porcine ETF-QO (full-length, residues 1-584) | [FAD](/xray-mp-wiki/reagents/additives/flavin-adenine-dinucleotide/), 4Fe4S cluster,  (UQ) |
| doi/10.1073##pnas.0604567103 | 2GMH | 2.7 A | P42(1)2 | Native porcine ETF-QO (UQ-free form, same construct) | [FAD](/xray-mp-wiki/reagents/additives/flavin-adenine-dinucleotide/), 4Fe4S cluster |

## Expression and Purification

- **Expression system**: Native tissue (porcine liver or kidney)
- **Construct**: Native full-length ETF-QO purified from porcine tissue

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Purification | Purification from porcine tissue | Not specified | 20 mM  (pH 7.5) + 0.2% beta-octyl-D-glucopyranoside | Protein purified from porcine tissue at 17 mg/ml concentration for crystallization |


## Crystallization

### doi/10.1073##pnas.0604567103

| Parameter | Value |
|---|---|
| Method | Vapor Diffusion Crystallization |
| Protein sample | Porcine ETF-QO at 17 mg/ml in 20 mM  pH 7.5, 0.2% beta-octyl-D-glucopyranoside |
| Reservoir | 12% (vol/vol) tertiary butanol, 3.5%  400, 0.1 M CaCl2, 0.1 M  pH 7.5 (UQ-free); similar conditions with UQ for the complex |
| Temperature | 4 C |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | UQ-bound crystals obtained by adding 10-fold molar excess of UQ. Space group P42(1)2 with cell dimensions a = b = 154.8 A, c = 130.2 A. Structure solved by /MAD methods. Data collected at BioCARS beamline at Advanced Photon Source (UQ-bound, 2.5 A) and Rigaku RU200 (UQ-free, 2.7 A). |


## Biological / Functional Insights

### Flavin is the direct electron donor to ubiquinone

The structure reveals that the flavin ring and  ring are in close proximity (8.5 A between C6 of FAD and O3 of UQ), while the 4Fe4S cluster is 18.8 A from UQ. This strongly suggests that the flavin, not the cluster, transfers electrons to UQ. The long cluster-UQ distance makes intraprotein electron transfer from cluster to UQ problematic, which cannot be overcome by conformational changes given the closely packed domain architecture, nor by dimer formation or a second UQ site.

### Three functional domains in a single structural domain

ETF-QO contains three functional regions - [FAD](/xray-mp-wiki/reagents/additives/flavin-adenine-dinucleotide/) domain, 4Fe4S cluster domain, and UQ-binding domain - that are closely packed and share structural elements, forming a single structural domain with no discrete, isolatable domains. The UQ domain is structurally similar to the p-hydroxylbenzoate hydroxylase fold, while the 4Fe4S domain core resembles Clostridium acidurici ferredoxin.

### Redox poising mechanism

When ETF-QO is reduced by ETF, the flavin is reduced to semiquinone and the cluster is also reduced. Electrons from ETF rapidly equilibrate between [FAD](/xray-mp-wiki/reagents/additives/flavin-adenine-dinucleotide/) and the cluster. When a second electron arrives, both centers are in a one-electron reduced state, priming the enzyme for two-electron reduction of UQ to ubiquinol. The cluster thus has a redox-poising effect on the flavin.

### Membrane association

The putative membrane-binding surface contains an alpha-helix and a beta-hairpin forming a hydrophobic plateau. Conserved basic residues (R113, R268, H269, H313, R423, K454) likely interact with phospholipid head groups. The UQ benzoquinone head group penetrates approximately 8 A into the matrix side of the mitochondria.

### Conserved catalytic architecture

The UQ-binding mode in ETF-QO differs from other UQ-binding proteins. Only one of the two carbonyl oxygen atoms in the benzoquinone ring is hydrogen-bonded to the polypeptide (to backbone of G272 and G273). The rest of the UQ molecule is surrounded by hydrophobic residues making van der Waals contacts. Residue S82 forms a hydrogen bond with the flavin ring that may influence the redox potential of bound [FAD](/xray-mp-wiki/reagents/additives/flavin-adenine-dinucleotide/).


## Cross-References

- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Referenced in purification methods
- [Ubiquinone](/xray-mp-wiki/reagents/cofactors/ubiquinone/) — Referenced in etf-qo text
- [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) — Referenced in etf-qo text
- [Peg](/xray-mp-wiki/reagents/additives/peg/) — Referenced in etf-qo text
- [MIRAS](/xray-mp-wiki/methods/structure-determination/miras/) — Referenced in etf-qo text
- [FAD](/xray-mp-wiki/reagents/additives/flavin-adenine-dinucleotide/) — Referenced in etf-qo text
