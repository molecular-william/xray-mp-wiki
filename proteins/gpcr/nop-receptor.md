---
title: Nociceptin/Orphanin FQ Peptide Receptor (NOP)
created: 2026-06-08
updated: 2026-06-09
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2015.07.024, doi/10.1038##nature11085]
verified: false
---

# Nociceptin/Orphanin FQ Peptide Receptor (NOP)

## Overview

The nociceptin/orphanin FQ peptide receptor (NOP), also known as ORL-1, is a member of the opioid receptor subfamily of GPCRs. NOP is a key drug target due to its roles in pain transmission, drug addiction, anxiety, and locomotor and mood disorders. The first X-ray crystal structure of the human NOP receptor was determined at 3.0 A resolution in complex with the peptide mimetic antagonist C-24 (Thompson et al., Nature 2012, PDB 4EA3), revealing an antagonist-bound inactive conformation with a large solvent-exposed orthosteric binding pocket. The receptor was subsequently crystallized in complex with antagonists SB-612111 and C-35 using lipidic cubic phase (LCP) crystallization, also to 3.0 A resolution. A strong correlation between antagonist potency (pKB) and receptor thermostability (Tm) was demonstrated, providing a high-throughput strategy for identifying GPCR ligands for crystallization. Docking studies revealed that potent, stabilizing antagonists like SB-612111 favor a single binding orientation, while less potent ligands can adopt multiple binding modes, contributing to reduced receptor stabilization.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature11085 | 4EA3 | 3.0 | P21 | BRIL-ΔN-NOP-ΔC fusion with N-terminal [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) (apocytochrome b562 RIL), N-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation/) (ΔN), C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation/) (ΔC); expressed in Sf9 insect cells | C-24 (peptide mimetic antagonist; Banyu Compound-24) |
| doi/10.1016##j.str.2015.07.024 | 5DHH | 3.0 | P21 | Human NOP receptor with [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) fusion, in complex with SB-612111 | SB-612111 (piperidine-based antagonist) |
| doi/10.1016##j.str.2015.07.024 | 5DHG | 3.0 | P21 | Human NOP receptor with [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) fusion, in complex with C-35 | C-35 (dichlorophenyl-N-benzyl D-Pro antagonist) |

 - R-work 24.8%, R-free 28.8%; Atoms: 3946 protein atoms (molecule A: 2113, molecule B: 2081), 64 ligand atoms (32 per molecule), 59 lipid/water atoms; Data collection: Merged from 23 crystals at 3.0 A resolution; space group P21 with two molecules in asymmetric unit

## Expression and Purification

- **Expression system**: Spodoptera frugiperda (Sf9) insect cells; baculovirus expression system
- **Construct**: Human NOP receptor with N-terminal [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) fusion; N-terminal and C-terminal truncations for crystallogenesis

### Purification Workflow

*Source: doi/10.1038##nature11085*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | Baculovirus infection of Sf9 insect cells |  |  | BRIL-ΔN-NOP-ΔC construct expressed in Sf9 cells; harvested 48 h post-infection |
| Membrane preparation and solubilization | Homogenization and solubilization in detergent |  | 20 mM HEPES pH 7.5, 500 mM NaCl, 30% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 1.0% lauryl [Maltose](/xray-mp-wiki/reagents/additives/maltose/) neopentyl glycol (MNG), 0.3% [Sodium Cholate](/xray-mp-wiki/reagents/detergents/sodium-cholate/), 0.03% [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) hemisuccinate ([CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)) | [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) present during solubilization; [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) used for cysteine blocking |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [TALON](/xray-mp-wiki/reagents/additives/talon/) IMAC [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [TALON](/xray-mp-wiki/reagents/additives/talon/) IMAC resin | 20 mM HEPES pH 7.5, 500 mM NaCl, 0.1% MNG, 0.03% [Sodium Cholate](/xray-mp-wiki/reagents/detergents/sodium-cholate/), 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 0.1% MNG, 0.03% [Sodium Cholate](/xray-mp-wiki/reagents/detergents/sodium-cholate/), 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Eluted with 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |

### Purification Workflow

*Source: doi/10.1016##j.str.2015.07.024*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | Baculovirus infection of Sf9 insect cells |  | Not specified | Expressed from 5 L Sf9 insect cell biomass, concentrated to 40 mg/ml for crystallization |
| Purification | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) and [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) |  | Not specified | Receptor purity and monodispersity monitored via SDS-PAGE and analytic SEC throughout purification |


## Crystallization

### doi/10.1038##nature11085

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | Purified BRIL-NOP-ΔC construct in complex with C-24 |
| Temperature | 20 C |
| Notes | Crystals grown in LCP using [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/)/cholesterol mix. Structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/). 23 crystals merged for final dataset. Data collected at wavelength 1.0330 A. Two NOP molecules per asymmetric unit (antiparallel) with one [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) domain forming crystal lattice contacts with receptors from an adjacent layer. |

### doi/10.1016##j.str.2015.07.024

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | Purified NOP receptor at 40 mg/ml, reconstituted into LCP (40% protein, 54% [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/), 6% [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/)) |
| Temperature | 20 C |
| Growth time | ~20 days |
| Cryoprotection | Crystals flash frozen directly from LCP in liquid nitrogen |
| Notes | LCP drops: 40 nl protein-containing LCP + 0.8 ul precipitant. Crystals harvested using 50 um MiTeGen micromounts. Data collected at APS GM/CA CAT beamline 23ID-B/D using 10 um minibeam at 1.0330 A wavelength. Due to radiation damage, 10-20 degree wedges collected per crystal. 19-22 crystals used per dataset. [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) with Phaser-MR using NOP-C24 structure (PDB 4EA3) as search model. |


## Biological / Functional Insights

### First NOP receptor structure and antagonist binding

The first X-ray crystal structure of the NOP receptor (Thompson et al., Nature 2012) was determined at 3.0 A resolution in complex with the peptide mimetic antagonist C-24 (Banyu Compound-24). The structure reveals a canonical seven-transmembrane GPCR fold with a large, solvent-exposed orthosteric binding pocket characteristic of peptide-binding GPCRs. C-24 binds in the pocket with its piperidine nitrogen forming a salt bridge with D130(3.32), similar to the binding mode of morphinan antagonists in other opioid receptors.

### Correlation between antagonist potency and receptor thermostability

A strong positive correlation was found between antagonist potency (pKB, measured by BRET assay) and receptor thermal stability (Tm, measured by CPM assay) for the NOP receptor (linear regression r^2 = 0.97, P < 0.001). This correlation provides a high-throughput strategy for identifying GPCR ligands for crystallization using BRET assays on crude membrane preparations, which is more amenable to automation than purified protein Tm measurements.

### Single binding mode correlates with high Tm and successful crystallization

Docking studies showed that potent, stabilizing antagonists (SB-612111, C-35, C-24) strongly favor a single binding orientation, with a salt bridge between the piperidine nitrogen and D130(3.32) anchoring the ligand. Less potent ligands (J-113397, Trap-101, JTC-801) that lowered thermostability could adopt multiple binding modes. This suggests that degenerate ligand binding orientations divide the receptor population into sub-conformations, reducing the probability of isolating a single receptor-ligand pair via crystallization.

### Structural basis of antagonist binding to NOP

The NOP structures with SB-612111 and C-35 are highly similar to the previously determined NOP-C24 structure (RMSD 0.37 A and 0.45 A over C-alpha atoms, respectively). All three antagonists use a piperidine group whose protonated nitrogen forms a salt bridge with D130(3.32). The dichlorophenyl head group of both SB-612111 and C-35 is buried deep in a hydrophobic sub-pocket outlined by M134(3.36), F135(3.37), I219(5.42), and V283(6.55). A sodium ion and water cluster was observed in the NOP-SB-612111 structure near residues D97(2.50), N133(3.35), S137(3.39), and N311(7.45).

### Structural basis of opioid receptor subtype selectivity

The NOP receptor has low affinity for classical opioid alkaloids despite sharing ~67% transmembrane sequence identity with mu-, delta-, and kappa-opioid receptors. Comparison of the NOP-C24 structure with kappa-opioid receptor (PDB 4DJH) and [Human CXCR4 Chemokine Receptor](/xray-mp-wiki/proteins/gpcr/cxcr4/) (PDB 3ODU) reveals differences in extracellular loop conformations, particularly in the region around helices V, VI, and VII, which contribute to ligand selectivity. The NOP receptor shows a more constrained extracellular binding pocket entrance compared to classical opioid receptors.


## Cross-References

- [Delta Opioid Receptor](/xray-mp-wiki/proteins/gpcr/delta-opioid-receptor/) — Homologous opioid receptor subfamily member; shares conserved sodium binding pocket architecture
- [Mu Opioid Receptor](/xray-mp-wiki/proteins/gpcr/mu-opioid-receptor/) — Homologous opioid receptor subfamily member; NOP antagonists show >300-1000 fold selectivity over mu opioid receptor
- [Kappa Opioid Receptor](/xray-mp-wiki/proteins/gpcr/kappa-opioid-receptor/) — Homologous opioid receptor subfamily member; used for structural comparison of extracellular region conformations
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Major component of LCP (54% w/w) for NOP crystallization
- [Lipidic Cubic Phase (LCP) Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Method used for all NOP crystal structures
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [Human CXCR4 Chemokine Receptor](/xray-mp-wiki/proteins/gpcr/cxcr4/) — Related protein structure
