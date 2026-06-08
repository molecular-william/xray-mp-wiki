---
title: ABCG8
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2022.167795]
verified: false
---

# ABCG8

## Overview

ABCG8 is a member of the ATP-binding cassette (ABC) G subfamily of transporter proteins. It functions as an obligate heterodimer with ABCG5 to form the ABCG5/G8 complex, which mediates selective sterol excretion by preferentially effluxing dietary plant sterols over cholesterol. The ABCG5/G8 heterodimer is localized on canalicular membranes of the bile ducts in the liver and the brush border of enterocytes in the small intestines, where it plays a critical role in reverse cholesterol transport and prevents abnormal accumulation of plant sterols (sitosterolemia) in the human body. In the ABCG5/G8 heterodimer, ABCG8 contributes key residues including T430 (which forms a hydrogen bond with cholesterol hydroxyl) and P415 (a landmark position at the end of the connecting helix). A conserved phenylalanine (F453) on transmembrane helix 2 is part of the phenylalanine highway motif.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2022.167795 | 8CUB | 4.051 A | I 2 2 2 | Human ABCG5/G8 heterodimer in complex with cholesterol | cholesterol |
| doi/10.1016##j.jmb.2022.167795 | 7JR7 | not specified | not specified | Human ABCG5/G8 heterodimer (cryo-EM structure used as molecular replacement model) | not specified |
| doi/10.1016##j.jmb.2022.167795 | 5DO7 | not specified | not specified | Human ABCG5/G8 heterodimer (apo state, cryo-EM structure) | None |

## Expression and Purification

- **Expression system**: Not specified
- **Construct**: Human ABCG8 (UniProt Q9UNQ0) with N-terminal His7-MBP tags followed by CBP tag. The CBP tag and N-linked glycans were cleaved by Endo H and HRV-3C protease.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Membrane preparation | -- | 20 mM HEPES pH 7.5, 150 mM NaCl, protease inhibitors (leupeptin, pepstatin A, PMSF) + -- | Insoluble membranes removed by ultracentrifugation |
| Solubilization | Detergent solubilization | -- | 20 mM HEPES pH 7.5, 150 mM NaCl, 0.1 mM TCEP + Not specified | Solubilized supernatant treated with 0.1 mM TCEP |
| Ni-affinity chromatography | Affinity chromatography (Ni-NTA) | 20-mL Ni-NTA column | Not specified + Not specified | Peak fractions from Ni-NTA eluates collected |
| Calmodulin-binding peptide (CBP) chromatography | Affinity chromatography (CBP) | 5-mL CBP column | 50 mM HEPES pH 7.5, 100 mM NaCl, 0.1% beta-DDM, 0.05% cholate, 0.01% CHS, 0.1 mM TCEP, 1 mM CaCl2, 1 mM MgCl2 + beta-DDM, cholate, CHS | Ni-NTA eluates mixed with CBP wash buffer and loaded onto CBP column |
| Detergent exchange | Affinity chromatography | CBP column | DMNG-containing buffer + DMNG | CBP column washed sequentially to exchange detergents to decyl maltose neopentyl glycol (DMNG) |
| Elution from CBP column | Affinity chromatography | CBP column | 50 mM HEPES pH 7.5, 300 mM NaCl, 2 mM EGTA, 0.1% DMNG, 0.05% cholate, 0.01% CHS, 1 mM TCEP + DMNG, cholate, CHS | ABCG5/G8 proteins eluted from CBP column |
| Tag cleavage | Protease digestion (Endo H and HRV-3C protease) | -- | Not specified + Not specified | N-linked glycans and CBP tag cleaved overnight at 4 C; Endo H (~0.2 mg per 10-15 mg protein) and HRV-3C protease (~2 mg per 10-15 mg protein) |
| Gel filtration chromatography | Size-exclusion chromatography | Superdex 200 30/100 GL column | 10 mM HEPES pH 7.5, 100 mM NaCl, 0.1% DMNG, 0.05% cholate, 0.01% CHS + DMNG, cholate, CHS | CBP tag-free proteins purified by SEC; peak fractions pooled |
| Reductive methylation and cysteine alkylation | Chemical modification | 2-mL Ni-NTA column | Not specified + Not specified | Methylated proteins relipidated with DOPC:DOPE (3:1, w/w), purified by Ni-NTA, treated with iodoacetamide |
| Cholesterol incubation | Ligand incubation | -- | Not specified + Not specified | Proteins incubated with cholesterol (prepared in isopropanol) overnight at 4 C |


## Crystallization

### doi/10.1016##j.jmb.2022.167795

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion with bicelles |
| Protein sample | Cholesterol-treated ABCG5/G8 reconstituted into 10% DMPC/CHAPSO bicelles (lipids:detergents 3:1 w/w, lipids containing 5 mol% cholesterol and 95 mol% DMPC), mixed 1:4 (v/v) with protein/bicelle stock, final protein concentration ~10 mg/ml |
| Reservoir | 1.8-2.0 M ammonium sulfate, 100 mM MES pH 6.5, 2-5% PEG400, 1 mM TCEP |
| Temperature | 20 C |
| Growth time | 1-2 weeks |
| Cryoprotection | 0.2 M sodium malonate |
| Notes | Crystals harvested by submersion in 0.2 M sodium malonate. Space group I 2 2 2. Solved by molecular replacement using PDB 7JR7. |


## Biological / Functional Insights

### Cholesterol hydrogen bonding with ABCG8_T430

In the cholesterol-bound ABCG5/G8 structure (PDB 8CUB), the cholesterol hydroxyl group forms a hydrogen bond with ABCG8_T430. The cholesterol extends across the interfacial space with its hydrocarbon tail remaining straight and in contact with hydrophobic residues on ABCG5 such as L516, L537, I562, F565, and F567. The sterol fits into an indented planar cleft within the upper region of the vestibule formed by the re-entry and transmembrane helices.

### Phenylalanine highway in ABCG8

ABCG8 contains a conserved phenylalanine F453 at position F1 of the phenylalanine highway (PH) on transmembrane helix 2. In ABCG8, F453 stacks underneath F576 (along with M577), which comprise the hydrophobic valve. The PH creates a highway-shaped open space at the TMD dimer interface, with aromatic side chains pointing inward, potentially serving as a molecular clamp for sterol transport.

### P415 landmark on ABCG8 connecting helix

Proline 415 (P415) in ABCG8 marks the end of the connecting helix that bridges the transmembrane domain to the nucleotide-binding domain. In wild-type ABCG5/G8, the cholesterol binding cloud stretches from P415 (ABCG8) to A540 (ABCG5), forming a continuous binding pattern. The A540F mutation introduces a break in this docking prediction, separating the two clusters.

### Asymmetric sterol binding on ABCG5/G8

Sterol docking poses on ABCG5/G8 are distributed asymmetrically at the opposing membrane-transporter interfaces. On the ABCG8-dominant side, sterol molecules orient in various but seemingly unspecific directions. Stigmasterol binds in two clusters partitioned between each monomer, while cholesterol binds in two separate pockets. The highest clusters of stigmasterol and cholesterol are located on opposite sides of the transporter-membrane interface.


## Cross-References

- [ABCG5](/xray-mp-wiki/proteins/abcg5/) — Obligate heterodimer partner; ABCG5/G8 heterodimer crystallized together in PDB 8CUB
- [ABCG1](/xray-mp-wiki/proteins/abcg1/) — Homodimeric ABCG sterol transporter; extensively compared for sterol binding patterns
- [ABCG2](/xray-mp-wiki/proteins/abcg2/) — Multidrug transporter ABCG member; shares hydrophobic valve and PH motif for comparison
- [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) — Central ligand; hydrogen bonds with ABCG8_T430; used in crystallization and incubation
- [Cholesteryl Hemisuccinate (CHS)](/xray-mp-wiki/reagents/additives/cholesterol-hydrogen-succinate/) — Cholesterol derivative used in purification and crystallization buffers (0.01% w/v)
- [Decyl Maltose Neopentyl Glycol (DMNG)](/xray-mp-wiki/reagents/detergents/dmng/) — Primary detergent used in final purification and crystallization sample buffer
- [MES Buffer](/xray-mp-wiki/reagents/buffers/mes/) — Crystallization buffer (100 mM, pH 6.5)
- [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/) — Crystallization precipitant (1.8-2.0 M)
