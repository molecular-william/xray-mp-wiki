---
title: ABCG8
created: 2026-05-27
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2022.167795, doi/10.1038##nature17666]
verified: false
---

# ABCG8

## Overview

ABCG8 is a member of the ATP-binding cassette (ABC) G subfamily of transporter proteins. It functions as an obligate heterodimer with ABCG5 to form the ABCG5/G8 complex, which mediates selective sterol excretion by preferentially effluxing dietary plant sterols over [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol). The ABCG5/G8 heterodimer is localized on canalicular membranes of the bile ducts in the liver and the brush border of enterocytes in the small intestines, where it plays a critical role in reverse cholesterol transport and prevents abnormal accumulation of plant sterols (sitosterolemia) in the human body.
The first X-ray crystal structure of human ABCG5/G8 was determined at 3.9 Å resolution (PDB 5DO7) using bicelle crystallization. In the ABCG5/G8 heterodimer, ABCG8 contributes key residues including T430 (which forms a hydrogen bond with cholesterol hydroxyl) and P415 (a landmark position at the end of the connecting helix). A conserved phenylalanine (F453) on transmembrane helix 2 is part of the phenylalanine highway motif. ABCG8 contains the catalytically active ATPase site (NBS2), with G8 Signature motif contributing to nucleotide binding and hydrolysis. 

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature17666 | 5DO7 | 3.9 | I 2 2 2 | Human ABCG5/G8 heterodimer, nucleotide-free inward-facing state (bicelle crystallization) | Cholesterol (putative, in sterol vestibules) |
| doi/10.1016##j.jmb.2022.167795 | 8CUB | 4.051 | I 2 2 2 | Human ABCG5/G8 heterodimer in complex with [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) | [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) |
| doi/10.1016##j.jmb.2022.167795 | 7JR7 | not specified | not specified | Human ABCG5/G8 heterodimer (cryo-EM structure used as [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement) model) | not specified |

## Expression and Purification

- **Expression system**: Pichia pastoris (yeast)
- **Construct**: Human ABCG8 (UniProt Q9UNQ0) with C-terminal calmodulin-binding peptide (CBP) tag; coexpressed with ABCG5 (C-terminal His₁₂ tag). CBP tag and N-linked glycans cleaved by Endo H and HRV-3C protease. Protein treated by reductive methylation and cysteine alkylation before crystallization.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Membrane preparation | -- | 20 mM HEPES pH 7.5, 150 mM NaCl, protease inhibitors ([Leupeptin](/xray-mp-wiki/reagents/additives/leupeptin), pepstatin A, PMSF) + -- | Insoluble membranes removed by ultracentrifugation |
| Solubilization | Detergent solubilization | -- | 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 150 mM NaCl, 0.1 mM TCEP + Not specified | Solubilized supernatant treated with 0.1 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep) |
| Ni-[Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) (Ni-NTA) | 20-mL [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta) column | Not specified + Not specified | Peak fractions from [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta) eluates collected |
| Calmodulin-binding peptide (CBP) chromatography | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) (CBP) | 5-mL CBP column | 50 mM HEPES pH 7.5, 100 mM NaCl, 0.1% beta-DDM, 0.05% [Cholate](/xray-mp-wiki/reagents/detergents/cholate), 0.01% CHS, 0.1 mM TCEP, 1 mM CaCl2, 1 mM MgCl2 + beta-DDM, [Cholate](/xray-mp-wiki/reagents/detergents/cholate), CHS | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta) eluates mixed with CBP wash buffer and loaded onto CBP column |
| Detergent exchange | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | CBP column | [DMNG](/xray-mp-wiki/reagents/detergents/dmng)-containing buffer + [DMNG](/xray-mp-wiki/reagents/detergents/dmng) | CBP column washed sequentially to exchange detergents to decyl [Maltose](/xray-mp-wiki/reagents/additives/maltose) neopentyl glycol (DMNG) |
| Elution from CBP column | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | CBP column | 50 mM HEPES pH 7.5, 300 mM NaCl, 2 mM EGTA, 0.1% DMNG, 0.05% [Cholate](/xray-mp-wiki/reagents/detergents/cholate), 0.01% CHS, 1 mM TCEP + DMNG, [Cholate](/xray-mp-wiki/reagents/detergents/cholate), CHS | [ABCG5/G8](/xray-mp-wiki/proteins/abcg5) proteins eluted from CBP column |
| Tag cleavage | Protease digestion (Endo H and HRV-3C protease) | -- | Not specified + Not specified | N-linked glycans and CBP tag cleaved overnight at 4 C; Endo H (~0.2 mg per 10-15 mg protein) and HRV-3C protease (~2 mg per 10-15 mg protein) |
| Gel filtration chromatography | [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200) 30/100 GL column | 10 mM HEPES pH 7.5, 100 mM NaCl, 0.1% DMNG, 0.05% [Cholate](/xray-mp-wiki/reagents/detergents/cholate), 0.01% CHS + DMNG, [Cholate](/xray-mp-wiki/reagents/detergents/cholate), CHS | CBP tag-free proteins purified by [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography); peak fractions pooled |
| Reductive methylation and cysteine alkylation | Chemical modification | 2-mL [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta) column | Not specified + Not specified | Methylated proteins relipidated with DOPC:DOPE (3:1, w/w), purified by Ni-NTA, treated with [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide) |
| [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) incubation | Ligand incubation | -- | Not specified + Not specified | Proteins incubated with [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) (prepared in isopropanol) overnight at 4 C |


## Crystallization

### doi/10.1038##nature17666

| Parameter | Value |
|---|---|
| Method | Bicelle crystallization (vapor diffusion, hanging drop) |
| Protein sample | G5G8 heterodimers coexpressed in P. pastoris, purified by tandem affinity chromatography (Ni-NTA + CBP), treated by reductive methylation and cysteine alkylation, reconstituted into DMPC bicelles (10% bicelle stock, lipids containing 5 mol% cholesterol and 95 mol% DMPC), ATP added at 10 mM before mixing, final protein concentration 5-10 mg ml⁻¹, protein/bicelle mixed 1:4 (v/v) |
| Reservoir | 1.7-2.0 M ammonium sulfate, 100 mM MES pH 6.5 (or HEPES pH 7.0), 2-5% PEG400 (or PEG350 MME), 1 mM TCEP |
| Temperature | 20-22 °C |
| Growth time | 3 days to 2 weeks; maximum size 75-150 × 40-60 × 10-20 μm in 1-2 months |
| Cryoprotection | 25% glycerol, 2 M (NH₄)₂SO₄, 100 mM MES pH 6.5, 2-4% PEG400 |
| Notes | Crystals only diffracted to 3.9 Å when cholesterol was present in bicelles. Two heterodimers in asymmetric unit. Tungsten SAD phasing using sodium phosphotungstate derivative. Native data merged from 19 crystals to 3.9 Å resolution. Space group I 2 2 2. Structure refined to R/Rfree = 0.242/0.328. |

### doi/10.1016##j.jmb.2022.167795

| Parameter | Value |
|---|---|
| Method | [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) with bicelles |
| Protein sample | [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol)-treated ABCG5/G8 reconstituted into 10% DMPC/CHAPSO bicelles (lipids:detergents 3:1 w/w, lipids containing 5 mol% cholesterol and 95 mol% DMPC), mixed 1:4 (v/v) with protein/bicelle stock, final protein concentration ~10 mg/ml |
| Reservoir | 1.8-2.0 M [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate), 100 mM MES pH 6.5, 2-5% PEG400, 1 mM TCEP |
| Temperature | 20 C |
| Growth time | 1-2 weeks |
| Cryoprotection | 0.2 M sodium malonate |
| Notes | Crystals harvested by submersion in 0.2 M sodium malonate. Space group I 2 2 2. Solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement) using PDB 7JR7. |


## Biological / Functional Insights

### ABCG8 contributes the catalytically active NBS2

ABCG8 contains the catalytically active Signature motif that contributes to NBS2, which binds and hydrolyses ATP. In contrast, ABCG5 contains an inactive Signature motif (NBS1) that binds but does not hydrolyse ATP. The three-helix bundle (CnH/CpH/E-helix) of G8 exhibits greater flexibility and transitions between different conformations, linking ATP hydrolysis to sterol transport via allosteric communication.

### Cholesterol hydrogen bonding with ABCG8_T430

In the [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol)-bound ABCG5/G8 structure (PDB 8CUB), the cholesterol hydroxyl group forms a hydrogen bond with ABCG8_T430. The cholesterol extends across the interfacial space with its hydrocarbon tail remaining straight and in contact with hydrophobic residues on ABCG5 such as L516, L537, I562, F565, and F567. The sterol fits into an indented planar cleft within the upper region of the vestibule formed by the re-entry and transmembrane helices.

### Phenylalanine highway in ABCG8

ABCG8 contains a conserved phenylalanine F453 at position F1 of the phenylalanine highway (PH) on transmembrane helix 2. In ABCG8, F453 stacks underneath F576 (along with M577), which comprise the hydrophobic valve. The PH creates a highway-shaped open space at the TMD dimer interface, with aromatic side chains pointing inward, potentially serving as a molecular clamp for sterol transport.

### P415 landmark on ABCG8 connecting helix

Proline 415 (P415) in ABCG8 marks the end of the connecting helix that bridges the transmembrane domain to the nucleotide-binding domain. In wild-type ABCG5/G8, the [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) binding cloud stretches from P415 (ABCG8) to A540 (ABCG5), forming a continuous binding pattern. The A540F mutation introduces a break in this docking prediction, separating the two clusters.

### Asymmetric sterol binding on ABCG5/G8

Sterol docking poses on ABCG5/G8 are distributed asymmetrically at the opposing membrane-transporter interfaces. On the ABCG8-dominant side, sterol molecules orient in various but seemingly unspecific directions. [Stigmasterol](/xray-mp-wiki/reagents/lipids/stigmasterol) binds in two clusters partitioned between each monomer, while cholesterol binds in two separate pockets. The highest clusters of stigmasterol and cholesterol are located on opposite sides of the transporter-membrane interface.


## Cross-References

- [ABCG5](/xray-mp-wiki/proteins/abc-transporters/abcg5/) — Obligate heterodimer partner; [ABCG5/G8](/xray-mp-wiki/proteins/abcg5) heterodimer crystallized together in PDB 5DO7 (first ABC sterol transporter structure) and PDB 8CUB
- [ABCG1](/xray-mp-wiki/proteins/abc-transporters/abcg1/) — Homodimeric ABCG sterol transporter; extensively compared for sterol binding patterns
- [ABCG2](/xray-mp-wiki/proteins/abc-transporters/abcg2/) — Multidrug transporter ABCG member; shares hydrophobic valve and PH motif for comparison
- [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) — Central ligand; hydrogen bonds with ABCG8_T430; used in crystallization and incubation
- [Cholesteryl Hemisuccinate (CHS)](/xray-mp-wiki/reagents/additives/cholesterol-hydrogen-succinate/) — [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) derivative used in purification and crystallization buffers (0.01% w/v)
- [Decyl Maltose Neopentyl Glycol (DMNG)](/xray-mp-wiki/reagents/detergents/dmng/) — Primary detergent used in final purification and crystallization sample buffer
- [MES Buffer](/xray-mp-wiki/reagents/buffers/mes/) — Crystallization buffer (100 mM, pH 6.5)
- [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/) — Crystallization precipitant (1.8-2.0 M)
- [Bicelle Crystallization](/xray-mp-wiki/methods/crystallization/bicelle-crystallization/) — G5G8 was crystallized using bicelle crystallization with DMPC/cholesterol bicelles
- [ABC Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/) — G5G8 is an ABCG subfamily member; the 2016 structure defined the ABC2 exporter superfamily fold
