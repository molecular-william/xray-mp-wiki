---
title: "Human Oxytocin Receptor (OTR)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1126##sciadv.abb5419]
verified: false
---

# Human Oxytocin Receptor (OTR)

## Overview

The human oxytocin receptor (OTR) is a class A G protein-coupled receptor (GPCR) that mediates the physiological effects of the neuropeptide hormone oxytocin, including regulation of parturition, lactation, and socioemotional behaviors. OTR belongs to the neurohypophyseal receptor family along with the vasopressin receptors (V1aR, V1bR, V2R). The receptor exhibits strong dependence on allosteric modulators including [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) and Mg2+ for proper function. The first crystal structure of OTR was determined in complex with the nonpeptidic antagonist [Retosiban](/xray-mp-wiki/reagents/additives/retosiban/) at 3.2-A resolution using lipidic cubic phase (LCP) crystallization.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##sciadv.abb5419 | 6TPK | 3.2 |  | OTR_XTAL (PGS fusion, D153A/S224A, C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/)) | [Retosiban](/xray-mp-wiki/reagents/additives/retosiban/) (antagonist), [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/), Mg2+ coordination site identified |

## Expression and Purification

- **Expression system**: Spodoptera frugiperda (Sf9) insect cells
- **Construct**: OTR crystallization construct (OTR_XTAL) with PGS fusion in ICL3 (residues R232-L265 replaced), C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) (residues 360-389), and D153A/S224A thermostabilizing mutations
- **Notes**: SNAP tag and octahistidine affinity tag at N-terminus (removed by 3C protease and PNGase F after purification). Codon-optimized for Sf9.

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Solubilization | 1% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.2% (w/v) [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) in 30 mM Hepes pH 7.5, 500 mM NaCl, 10 mM KCl, 5 mM MgCl2 | — | 30 mM Hepes pH 7.5, 500 mM NaCl, 10 mM KCl, 5 mM MgCl2 | Membranes solubilized for 2.5 h at 4 C with 100 uM [Retosiban](/xray-mp-wiki/reagents/additives/retosiban/) and [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [TALON](/xray-mp-wiki/reagents/additives/talon/) IMAC resin | — | Wash I: 50 mM Hepes pH 7.5, 500 mM NaCl, 10 mM MgCl2, 5 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.2% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 8 mM ATP, 50 uM [Retosiban](/xray-mp-wiki/reagents/additives/retosiban/). Wash II: 50 mM Hepes pH 7.5, 500 mM NaCl, 15 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 50 uM [Retosiban](/xray-mp-wiki/reagents/additives/retosiban/) | Elution: 50 mM Hepes pH 7.5, 500 mM NaCl, 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 100 uM [Retosiban](/xray-mp-wiki/reagents/additives/retosiban/) |
| Desalting / tag removal | PD MiniTrap G-25 column | — | 50 mM Hepes pH 7.5, 500 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.006% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 100 uM [Retosiban](/xray-mp-wiki/reagents/additives/retosiban/) | [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) removed, then treated with His-tagged 3C protease and PNGase F overnight to remove affinity tags and deglycosylate. Cleaved receptor collected as Ni-NTA flow-through. |
| Concentration | 100-kDa MWCO Vivaspin 2 concentrator | — | Same as G25 buffer | Concentrated to ~70 mg/ml; typical yield ~0.8 mg per liter of expression volume |


## Crystallization

### doi/10.1126##sciadv.abb5419

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Temperature | 16 |
| Notes | OTR:[Retosiban](/xray-mp-wiki/reagents/additives/retosiban/) complex (~70 mg/ml) mixed with molten [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) for LCP reconstitution. Strong electron density for [Retosiban](/xray-mp-wiki/reagents/additives/retosiban/), [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/), and key interaction residues. |


## Biological / Functional Insights

### Enlarged binding pocket

The OTR binding pocket is approximately 25% larger than other non-peptide antagonist-bound neuropeptide GPCRs and ~50% larger than the agonist-bound NTS1R. The enlarged pocket likely accommodates the cyclic nonapeptide agonist oxytocin.

### Retosiban binding mode

[Retosiban](/xray-mp-wiki/reagents/additives/retosiban/) adopts an upright, elongated conformation in the binding pocket with its 2,5-diketopiperazine (DKP) core. The binding interface features a polar hemisphere (helices II-IV, residues Q119, Q171, K116) and a hydrophobic hemisphere (helices V-VII). Key polar interactions include hydrogen bonds between Q171^4.60 and the DKP 2-keto oxygen, and between Q119^3.32 and the DKP N1.

### Extrahelical cholesterol binding site

A [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) molecule binds in a previously undescribed extrahelical location between helices IV and V, capped by ECL2. Key interactions involve Y200^5.38 and W203^5.41 on helix V, and P170^4.59, I174^4.63, and ECL2 residues. [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) binding stabilizes the receptor through direct contact with ECL2 and by orienting Y200^5.38 to form a hydrogen bond with Q171^4.60, thereby coordinating the polar network of the binding pocket.

### Divalent cation coordination site

Two acidic residues, E42^1.35 and D100^2.65, at the extracellular tips of helices I and II form a highly conserved Mg2+ binding site. Mg2+ acts as a positive allosteric modulator for agonist binding. This represents the first identification of a distinct, solvent-exposed divalent cation coordination site in a GPCR.


## Cross-References

- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Used as the LCP matrix for OTR crystallization
- [GPCR Active State and High-Affinity Agonist Binding](/xray-mp-wiki/concepts/signaling-receptors/gpcr-active-state-high-affinity-agonist-binding/) — OTR is a class A GPCR with allosteric modulation by cholesterol and Mg2+
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Additive used in purification or crystallization buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) — Additive used in purification or crystallization buffers
- [Retosiban](/xray-mp-wiki/reagents/additives/retosiban/) — Additive used in purification or crystallization buffers
- [TALON](/xray-mp-wiki/reagents/additives/talon/) — Additive used in purification or crystallization buffers
