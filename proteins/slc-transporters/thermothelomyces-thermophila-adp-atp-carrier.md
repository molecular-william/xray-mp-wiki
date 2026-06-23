---
title: Thermothelomyces thermophila ADP/ATP Carrier
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2018.11.025]
verified: false
---

# Thermothelomyces thermophila ADP/ATP Carrier

## Overview

The Thermothelomyces thermophila ADP/ATP carrier (TtAac) is a mitochondrial inner membrane transporter. The thermostabilized Q302K mutant was crystallized in the matrix-open state locked by [Bongkrekic Acid](/xray-mp-wiki/reagents/ligands/bongkrekic-acid/), revealing the transport mechanism involving rotation of three domains about a central substrate-binding site.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2018.11.025 | 6GJ2 | 3.3 A | P3221 | TtAac residues 4-315 with Q302K mutation, N-terminal MetSer tag, complex with [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) | [Bongkrekic Acid](/xray-mp-wiki/reagents/ligands/bongkrekic-acid/) (BKA); tetraoleoyl [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/); [PEG](/xray-mp-wiki/reagents/additives/peg/) |
| doi/10.1016##j.cell.2018.11.025 | 6GJ3 | 3.6 A | P212121 | TtAac residues 8-311 with Q302K mutation, N-terminal His8 tag with Factor Xa cleavage site | [Bongkrekic Acid](/xray-mp-wiki/reagents/ligands/bongkrekic-acid/) (BKA); tetraoleoyl [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) |

## Expression and Purification

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Mitochondria isolation | Cell disruption and differential centrifugation | -- | 0.1 M MES pH 6.5, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) | Saccharomyces cerevisiae WB-12 strain, grown in YEPG at 30 C for 72 h |
| BKA inhibition | Inhibitor pre-incubation | -- | 100 mM Tris pH 7.4, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 2 umol BKA per mg mitochondrial protein, 250 uM ADP | Inhibited at room temperature for 30 min before solubilization |
| Solubilization | Detergent solubilization | -- | 2% 10-MNG, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 150 mM NaCl, 5 uM BKA | Solubilized for 1 h at 4 C, clarified by ultracentrifugation at 200,000g |
| Ni-NTA affinity purification | Immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni Sepharose High Performance | 100 mM Tris pH 7.4, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 150 mM NaCl, 5 uM BKA | Washed with buffer containing 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) complex formation | Complex incubation | Ni Sepharose High Performance | Buffer C with [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/), [HEGA-10](/xray-mp-wiki/reagents/detergents/hega-10/), BKA | His-tagged [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) added, incubated 30 min at 4 C, then overnight with Ni Sepharose |
| Factor Xa cleavage | Protease cleavage | -- | Buffer D with CaCl2, [HEGA-10](/xray-mp-wiki/reagents/detergents/hega-10/), BKA | Slurry supplemented with 30 ug Factor Xa protease, incubated at 10 C for 2 h |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | Gel filtration | Sephadex G75 | 10 mM Tris pH 7.4, 50 mM NaCl, 0.35% [HEGA-10](/xray-mp-wiki/reagents/detergents/hega-10/), 10 uM BKA | TtAac-Nb complex eluted in volume fractions 0.5-1.5 mL |


## Crystallization

### doi/10.1016##j.cell.2018.11.025

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | TtAac-Nb complex at A280 8-10 |
| Reservoir | 0.1 M HEPES pH 7.5, 3% 3-methyl-3-pentanol, 18% [PEG400](/xray-mp-wiki/reagents/additives/peg-400/) OR 0.1 M MES pH 6.5, 1% 3-methyl-3-pentanol, 22% [PEG400](/xray-mp-wiki/reagents/additives/peg-400/) |
| Temperature | 4 C |
| Growth time | 3 days |
| Cryoprotection | PFO cryo oil or LV cryo oil, flash-frozen in liquid nitrogen |
| Notes | Crystals grown at 4 C, appeared within 3 days. Also solved without [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) (6GJ3, P212121, 3.6 A) confirming structure not affected by [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/). |


## Biological / Functional Insights

### Matrix-open state structure reveals transport mechanism

The BKA-inhibited m-state structure shows the carrier with a central cavity open to the mitochondrial matrix side, with matrix helices rotated outward. The cytoplasmic side is closed by conserved hydrophobic residues and a salt bridge network braced by tyrosines. The carrier switches between states by rotation of its three domains about a fulcrum provided by the substrate-binding site, a mechanism likely applicable to the whole mitochondrial carrier family.

### Bongkrekic acid as conformation-specific competitive inhibitor

BKA binds deeply and asymmetrically within the central cavity, mimicking the dicarboxylate end of ATP phosphate groups and the polyunsaturated backbone mimicking the adenine ring. BKA forms electrostatic interactions with K30, R88, R197, hydrogen bonds to Y196, N96, and Y89. The steric bulk of BKA polyunsaturated backbone prevents substrate binding, locking the carrier in an abortive m-state.

### Cytoplasmic gate and salt bridge networks

The cytoplasmic gate is formed by hydrophobic residues (F97, F201, L295), the cytoplasmic salt bridge network (D101, K104, D205, K208, D299, K302), and tyrosine braces (Y100, Y204, Y298). These elements are highly conserved across the mitochondrial carrier family. Mutations of the strongest network links (R100, K104, K208) have the greatest effect on transport and thermal stability.

### Alternating access mechanism with domain rotation

The transport mechanism involves rigid-body rotation of core elements with approximately 15 degree rocking motion coupled with inward movement of gate elements. The substrate-binding site acts as a fulcrum. Core elements comprise odd-numbered helices, matrix helices, linkers, and one-third of even-numbered helices. Gate elements are the C-terminal portions of even-numbered helices beyond the contact points (R88, G192, R287).


## Cross-References

- [Bongkrekic Acid](/xray-mp-wiki/reagents/ligands/bongkrekic-acid/) — BKA inhibitor co-crystallized with TtAac, locks m-state conformation
- [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) — Tetraoleoyl cardiolipin binds at inter-domain interfaces via helix dipole interactions
- [Decyl Maltose Neopentyl Glycol (10-MNG)](/xray-mp-wiki/reagents/detergents/lmng/) — Primary solubilization detergent at 2% for mitochondrial carrier extraction
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — PEG400 and PEG600 used as crystallization precipitants
- [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) — Crystallization buffer at 0.1 M pH 7.5
- [MES](/xray-mp-wiki/reagents/buffers/mes/) — Alternative crystallization buffer at 0.1 M pH 6.5
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Elution agent for Ni-NTA affinity purification
- [Bovine ADP/ATP Carrier](/xray-mp-wiki/proteins/slc-transporters/bovine-adp-atp-carrier/) — Homologous mitochondrial carrier; ScAac2 CATR-inhibited c-state used for comparison
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Method used in structure determination or purification
