---
title: TmCdsA CDP-DAG Synthetase
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms5244]
verified: false
---

# TmCdsA CDP-DAG Synthetase

## Overview

TmCdsA is the CDP-diacylglycerol (CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag/)) synthetase from Thermotoga maritima, an integral membrane enzyme that catalyses the formation of CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag/) from cytidine 5'-triphosphate (CTP) and [Phosphatidic Acid](/xray-mp-wiki/reagents/lipids/phosphatidic-acid/) (PA). CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag/) is a central liponucleotide intermediate essential for the biosynthesis of [Phosphatidylinositol](/xray-mp-wiki/reagents/lipids/phosphatidylinositol/), [Phosphatidylglycerol](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol/), and [Phosphatidylserine](/xray-mp-wiki/reagents/lipids/phosphatidylserine/). The 3.4 A resolution crystal structure reveals that TmCdsA forms a homodimer with each monomer containing nine transmembrane helices arranged into a novel fold with three domains (NTD, MD, CTD). A funnel-shaped cavity penetrates halfway into the membrane, enabling simultaneous access of hydrophilic CTP from the cytoplasm and hydrophobic PA from the lipid bilayer. A Mg2+-K+ hetero-di-metal centre coordinated by an Asp-Asp dyad (Asp219, Asp249) serves as the catalytic cofactor, suggesting a two-metal-ion catalytic mechanism for CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag/) synthesis at the membrane-cytoplasm interface.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms5244 | 4QDG | 3.4 A | P6522 | TmCdsA S200C/S223C double-cysteine mutant; homodimer; residues 4-270 per monomer; nine transmembrane helices arranged in NTD (M1), MD (M2-M5), and CTD (M6-M9); with Mg2+-K+ hetero-di-metal centre | Mg2+ and K+ ions at the active site; [Methylmercury Chloride](/xray-mp-wiki/reagents/additives/methylmercury-chloride/) bound at engineered cysteine sites for phasing |
| doi/10.1038##ncomms5244 | 4QDH | 3.5 A | P6522 | TmCdsA S200C/S258C double-cysteine mutant; homodimer; alternative crystallization construct for structural comparison | Mg2+ and K+ ions |

## Expression and Purification

- **Expression system**: Escherichia coli C41(DE3)
- **Construct**: Full-length TmCdsA (residues 1-270) with N-terminal [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/) in pET15b vector; S200C/S223C and S200C/S258C double-cysteine mutants for crystallization; wild-type for functional studies

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane extraction | Sonication and detergent solubilization | — | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) (pH 7.5), 300 mM NaCl, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 1.5% decyl-beta-D-maltopyranoside (DM) | Cell suspension stirred on ice; 1.5g DM per 100 mL cell suspension; sonication at 80% power, 1s on/5s off for 2 min total |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA resin gravity column | Ni-NTA agarose (1 mL per 50 mL supernatant) | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) (pH 7.5), 300 mM NaCl, 20-300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) gradient, 0.5% DM + 0.5% decyl-beta-D-maltopyranoside (DM) | Pre-equilibrated with buffer A (25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/), 300 mM NaCl, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 0.5% DM, pH 7.5); washed with 5 column volumes; eluted with [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) gradient |
| Size-exclusion chromatography | Gel filtration | — | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) (pH 7.5), 100 mM NaCl, 0.3% DM | Purified protein concentrated to ~10 mg/mL for crystallization |


## Crystallization

### doi/10.1038##ncomms5244

| Parameter | Value |
|---|---|
| Method | [Sitting-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) |
| Protein sample | S200C/S223C or S200C/S258C TmCdsA at ~10 mg/mL in 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) (pH 7.5), 100 mM NaCl, 0.3% DM, with 1 mM [Methylmercury Chloride](/xray-mp-wiki/reagents/additives/methylmercury-chloride/) |
| Reservoir | 100 mM HEPES (pH 7.5), 200 mM [Ammonium Acetate](/xray-mp-wiki/reagents/buffers/ammonium-acetate/), 25% [PEG](/xray-mp-wiki/reagents/additives/peg/) 3350 |
| Temperature | 20 C |
| Growth time | 1-2 weeks |
| Notes | Crystals grew in space group P6522 with one dimer per asymmetric unit; methylmercury was essential for crystallization of the double-cysteine mutants |


## Biological / Functional Insights

### Novel three-domain fold for CDP-DAG synthesis

TmCdsA adopts a previously uncharacterized fold with nine transmembrane helices (M1-M9) organized into three domains: N-terminal domain (NTD, M1), middle domain (MD, M2-M5) at the dimerization interface, and C-terminal domain (CTD, M6-M9). The CTD has the highest degree of sequence conservation among prokaryotic Cds homologues. The dimer interface is formed primarily by the MD domains, with the two active sites facing opposite sides of the dimer.

### Funnel-shaped dual-opening cavity for dual substrates

Each TmCdsA monomer contains a funnel-shaped cavity that indents halfway into the membrane from the cytoplasmic side. The cavity has two openings: a cytoplasmic opening that allows the water-soluble substrate CTP/dCTP to enter and the pyrophosphate by-product to exit, and a lateral opening exposed to the inner leaflet of the lipid bilayer that allows the hydrophobic substrate [Phosphatidic Acid](/xray-mp-wiki/reagents/lipids/phosphatidic-acid/) (PA) to access the active site. The M1 helix shows relatively high B-factors, suggesting it may act as a lateral gate controlling PA access and CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag/) release.

### Mg2+-K+ hetero-di-metal catalytic centre

TmCdsA contains a non-canonical Mg2+-K+ hetero-di-metal centre at the bottom of the funnel-shaped cavity. The Mg2+ site is coordinated by Asp219 and Asp249 (the Asp-Asp dyad) and is absolutely required for activity. The K+ site is coordinated by Glu222 and is stimulated by monovalent cations (K+ > Rb+ > NH4+ > Na+). K+ at 50-200 mM stimulates activity ~30-fold over Mg2+ alone. This represents a unique integral membrane enzyme with a hetero-di-metal catalytic centre, analogous to the two-metal-ion mechanism of DNA polymerases but with Mg2+ activating the PA substrate and K+ facilitating pyrophosphate dissociation.

### Accessory charged residues in the active site

Mutagenesis analysis identified several essential charged residues around the di-metal centre. Asp144, Asp246, Lys167, and Lys226 each lost >98% activity when mutated to Ala, comparable to the Asp-Asp dyad mutants. These residues contribute to substrate binding, intermediate formation, or product release. Arg166, located more distantly, lost only 30% activity upon mutation.


## Cross-References

- [Phosphatidic Acid (PA)](/xray-mp-wiki/reagents/lipids/phosphatidic-acid/) — Hydrophobic substrate of TmCdsA
- [Cytidine-Diphosphate Diacylglycerol (CDP-DAG)](/xray-mp-wiki/reagents/cytidine-diphosphate-diacylglycerol/) — Product of TmCdsA enzymatic reaction
- [CDP-Alcohol Phosphotransferase Family](/xray-mp-wiki/concepts/cdp-alcohol-phosphotransferase-family/) — Related enzyme family also utilizing CDP-activated substrates for phospholipid biosynthesis
- [Sitting-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) — Method used in structure determination or purification
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [Methylmercury Chloride](/xray-mp-wiki/reagents/additives/methylmercury-chloride/) — Additive used in purification or crystallization buffers
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [Ammonium Acetate](/xray-mp-wiki/reagents/buffers/ammonium-acetate/) — Buffer component in purification or crystallization
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component in purification or crystallization
