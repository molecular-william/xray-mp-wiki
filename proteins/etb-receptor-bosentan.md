---
title: Human Endothelin ETB Receptor Bound to Bosentan
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.3450]
verified: false
---

# Human Endothelin ETB Receptor Bound to Bosentan

## Overview

The human endothelin ETB receptor is a class A G-protein-coupled receptor (GPCR) activated by vasoactive peptide hormones endothelins. This paper reports the crystal structures of the ETB receptor bound to the clinical dual ETA-ETB antagonist bosentan at 3.6-A resolution and to the ETB-selective analog K-8794 at 2.2-A resolution. The ETB receptor plays crucial roles in vascular control as a target for drugs treating pulmonary arterial hypertension and cancer progression. Bosentan is the first oral drug approved to treat PAH, with worldwide sales surpassing $1 billion per year. The structures reveal detailed interactions between the antagonists and the receptor, unexpected similarity between antagonist and agonist binding at the orthosteric site, and how bosentan sterically prevents the inward movement of transmembrane helix 6 (TM6), thereby exerting its antagonistic activity. The K-8794-bound structure at high resolution reveals a detailed water-mediated hydrogen-bonding network at the transmembrane core that accounts for weak negative allosteric modulation of ETB by sodium ions.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nsmb.3450 | 5X93 | 2.2 | C2221 | ETB-Y5-mT4L thermostabilized mutant with mT4L fusion in ICL3, C-terminal truncation after Ser407, C396A/C400A/C405A mutations, five thermostabilizing mutations, HA signal peptide, Flag tag, and 9-aa linker | K-8794 (ETB-selective antagonist, 10 uM throughout purification) |
| doi/10.1038##nsmb.3450 | 5XPR | 3.6 | P3221 | ETB-Y4-mT4L thermostabilized mutant (reverted Asp154Ala to Asp for bosentan crystallization), same core mutations as Y5 variant | Bosentan (clinical dual ETA-ETB antagonist, 10 uM throughout purification) |

## Expression and Purification

- **Expression system**: Sf9 insect cells using Bac-to-Bac baculovirus expression system (Invitrogen)
- **Construct**: ETB-Y5-mT4L or ETB-Y4-mT4L in modified pFastBac1 vector with TEV protease recognition sequence and EGFP-His10 tag. Infected at 4.0 x 10^6 cells/ml in Sf900 II medium, grown 48 h at 27 C.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Sonication and ultracentrifugation | -- | 20 mM Tris-HCl pH 7.5, 20% glycerol + -- | Harvested Sf9 cells disrupted by sonication; crude membrane fraction collected by ultracentrifugation at 180,000g for 1 h |
| Solubilization | Detergent solubilization | -- | 50 mM Tris-HCl pH 7.5, 200 mM NaCl, 0.5% DDM, 0.1% CHS, 2 mg/ml iodoacetamide + 0.5% DDM, 0.1% CHS | Solubilized for 2 h at 4 C; antagonists added to 10 uM final concentration |
| Affinity purification | Immobilized metal affinity chromatography | TALON resin (Clontech) | 20 mM Tris-HCl pH 7.5, 500 mM NaCl, 0.1% LMNG, 0.01% CHS, 20 mM imidazole (wash); 200 mM imidazole (elution) + LMNG, CHS | Incubated with resin for 30 min; eluted with 200 mM imidazole |
| Tag cleavage | Protease digestion and dialysis | -- | 20 mM Tris-HCl pH 7.5, 500 mM NaCl + -- | Eluate treated with TEV protease and dialyzed to remove imidazole |
| Tag removal | Immobilized metal affinity chromatography | Ni-NTA resin | 20 mM Tris-HCl pH 7.5, 500 mM NaCl + -- | Cleaved GFP-His10 tag and TEV protease removed with Ni-NTA resin |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex 200 10/300 Increase column | 10 mM HEPES-NaOH pH 7.5, 200 mM NaCl, 0.01% LMNG, 0.001% CHS + LMNG, CHS | Peak fractions concentrated to 40 mg/ml; antagonists added to 100 uM for crystallization |


## Crystallization

### doi/10.1038##nsmb.3450

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | ETB receptor at 40 mg/ml reconstituted into LCP of monoolein with cholesterol at 8:9:1 ratio |
| Temperature | Not specified |
| Growth time | Not specified |
| Notes | Crystals of ETB-Y5-mT4L-K-8794 in space group C2221 (2.2 A); ETB-Y4-mT4L-bosentan in space group P3221 (3.6 A). Molecular replacement used for structure determination. |


## Biological / Functional Insights

### Unexpected similarity between antagonist and agonist binding

Despite having little structural similarity to the endogenous agonist endothelin-1, bosentan occupies the bottom of the orthosteric site, corresponding to the binding site for the C-terminal tripeptide of ET-1 (Ile19, Ile20, Trp21). The pharmacophore of bosentan consists of: (1) a negatively charged sulfonamide group that forms ionic interactions with positively charged residues (Lys182, Lys273, Arg343); (2) a hydrophobic 4-t-butylphenyl group; and (3) a 2-methoxyphenoxy group. The 2-pyrimidyl group shows relatively poor interaction, consistent with SAR studies showing less influence on affinity.

### Antagonistic mechanism via steric prevention of TM6 inward movement

Bosentan does not induce the inward movement of TM6 and TM7 that characterizes agonist binding. The critical activation residues Arg343(6.55) and Trp336(6.48) are not repositioned upon bosentan binding. Unlike ET-1 which causes significant conformational changes in TM6 and TM7, bosentan's binding to the orthosteric pocket sterically prevents the conformational transitions required for receptor activation, explaining its antagonistic activity despite occupying the same binding site as the agonist.

### Water-mediated hydrogen-bonding network and Na+ allosteric modulation

The high-resolution K-8794-bound structure reveals a detailed water-mediated hydrogen-bonding network at the transmembrane core. A putative Na+-binding site is identified with conserved residues N1.50, D2.50, S3.35, T3.39, W6.48, N7.45, S7.46, N7.49 matching the canonical GPCR sodium binding motif. Competition binding assays show that ETB receptor is weakly negatively allosterically modulated by Na+ ions, as 2 M NaCl does not 50% inhibit [125I]ET-1 binding.


## Cross-References

- [DDM (N-Dodecyl-beta-D-maltoside)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary solubilization detergent (0.5%) for ETB membrane extraction
- [LMNG (Lauryl Maltose Neopentyl Glycol)](/xray-mp-wiki/reagents/detergents/lmng/) — Used in IMAC wash/elution (0.1-0.01%) and SEC (0.01%) buffers
- [Cholesterol Hemisuccinate (CHS)](/xray-mp-wiki/reagents/lipids/cholesterol-hemisuccinate/) — Added at 0.1% during solubilization and 0.001% in SEC for receptor stability
- [Tris Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Primary buffer (20-50 mM pH 7.5) for membrane prep and affinity purification
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Used at 10 mM pH 7.5 in SEC buffer
- [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/) — 200-500 mM NaCl in purification buffers
- [T4 Lysozyme (T4L) fusion](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) — mT4L fusion protein used in ICL3 for crystallization stabilization
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used for ETB receptor crystallization with monoolein
