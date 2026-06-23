---
title: Cysteinyl Leukotriene Receptor 1 (CysLT1R)
created: 2019-10-09
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1126##sciadv.aax2518]
verified: false
---

# Cysteinyl Leukotriene Receptor 1 (CysLT1R)

## Overview

Cysteinyl leukotriene receptor type 1 (CysLT1R) is a class A G protein-coupled receptor (GPCR) that mediates inflammatory processes and plays a major role in asthma, allergic rhinitis, cardiovascular disease, and cancer. The crystal structures of CysLT1R bound to two chemically distinct antagonists, zafirlukast and pranlukast, were determined at 2.53 A and 2.7 A resolution, respectively, using both synchrotron and X-ray free-electron laser (XFEL) sources. The structures reveal unique ligand-binding modes including lateral ligand access to the orthosteric pocket between transmembrane helices TM4 and TM5, an atypical pattern of microswitches (FRC motif instead of DRY), and a distinct four-residue-coordinated sodium site with unusually high sodium affinity (Km 39 mM). CysLT1R belongs to the delta-branch of class A GPCRs and shares close structural similarity with P2Y1R.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##sciadv.aax2518 | 6RZ4 | 2.7 | P 1 21 1 | Human CysLT1R with [Bril](/xray-mp-wiki/reagents/protein-tags/bril/) fusion in ICL3, C-terminal [Truncation](/xray-mp-wiki/concepts/truncation/) after K311; complex with pranlukast | Pranlukast (antagonist) |
| doi/10.1126##sciadv.aax2518 | 6RZ5 | 2.53 | P 1 | Human CysLT1R with [Bril](/xray-mp-wiki/reagents/protein-tags/bril/) fusion in ICL3, C-terminal [Truncation](/xray-mp-wiki/concepts/truncation/) after K311; complex with zafirlukast (XFEL structure) | Zafirlukast (antagonist) |

## Expression and Purification

- **Expression system**: Spodoptera frugiperda Sf9 insect cells; Bac-to-Bac Baculovirus Expression System
- **Construct**: Human CysLT1R with [Bril](/xray-mp-wiki/reagents/protein-tags/bril/) fusion in intracellular loop 3, C-terminal [Truncation](/xray-mp-wiki/concepts/truncation/) after Lys311; 8 uM zafirlukast added during expression

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell harvest and membrane preparation | Hypotonic lysis and ultracentrifugation | Not specified | Hypotonic: 10 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 10 mM [Mgcl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/), 20 mM KCl, PIC; High-salt: 10 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 10 mM [Mgcl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/), 20 mM KCl, 1 M NaCl, PIC + Not specified | Membranes washed twice in hypotonic buffer, three times in high-salt buffer |
| Solubilization | Detergent extraction | Not specified | 25 uM antagonist (zafirlukast or pranlukast), [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) (2 mg/ml), PIC + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.2% CHS | Solubilization for 3.5 h at 4 C with continuous stirring |
| Affinity purification | Immobilized metal affinity chromatography (IMAC) | [Talon](/xray-mp-wiki/reagents/additives/talon/) IMAC resin (Clontech) | Wash 1: 100 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 250 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.02% CHS, 15 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), PIC, 10 mM [Mgcl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/), 8 mM [ATP](/xray-mp-wiki/reagents/ligands/atp/); Wash 2: 50 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 250 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% CHS, 30 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), PIC + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.01% CHS (after buffer exchange) | Overnight batch binding; 6 CV washes; elution performed after buffer exchange to lower [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |


## Crystallization

### doi/10.1126##sciadv.aax2518

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | Purified CysLT1R reconstituted into monoolein-based LCP |
| Temperature | 20 |
| Cryoprotection | Crystals harvested and flash-cooled in liquid nitrogen for synchrotron; XFEL data collected at room temperature using LCP injector |
| Notes | Synchrotron data collected at ESRF beamlines ID29 and ID23-1. XFEL data collected at LCLS. The zafirlukast complex structure (6RZ5) was determined by molecular replacement using CysLT1R-pran (6RZ4) as search model. The 6RZ4 structure was solved by molecular replacement using P2Y1R (PDB 4XNW) and [Bril](/xray-mp-wiki/reagents/protein-tags/bril/) from A2AAR (PDB 4EIY). |


## Biological / Functional Insights

### Lateral ligand access between TM4 and TM5

CysLT1R reveals a unique ligand-binding pocket that stretches from ECL2 across the receptor toward a gap between TM4 and TM5, providing a lateral ligand access route from the lipid bilayer into the orthosteric pocket. The zafirlukast-bound structure shows an open-gate conformation between TM4 and TM5, while the pranlukast-bound structure has a closed gate. Molecular dynamics simulations show the open-gate conformation collapses within ~200 ns after zafirlukast removal, indicating a low energy barrier for gate transitions.

### Atypical FRC microswitch motif

CysLT1R contains an atypical FRC motif (Phe119-Arg121-Cys122) instead of the canonical DRY motif at positions 3.49-3.51. This eliminates the common salt bridge between D3.49 and R3.50 found in inactive-state GPCRs. The R3.50 residue adopts different conformations in the two structures, conferring more flexibility. Mutation of the FR motif residues alters LTD4 signaling potency.

### Distinct four-residue sodium-binding site

CysLT1R contains a unique sodium-binding site coordinated by four residues (Asp69, Asn106, Ser110, Asn287) plus a water molecule, distinct from the canonical three-residue sodium site in other class A GPCRs. The N7.45 side chain directly coordinates Na+ instead of making water-mediated contact as in [PAR1](/xray-mp-wiki/proteins/gpcr/par1/). The sodium ion is tightly bound with high affinity (Km 39 +/- 11 mM) and stabilizes the receptor, increasing Tm by up to 8 C at physiological (150 mM) Na+ concentration.

### Delta-branch structural similarity despite different ligands

Despite sharing only 29% sequence identity with P2Y1R and binding completely different ligands (lipids vs nucleotides), CysLT1R shows remarkably high structural similarity to P2Y1R (Ca RMSD 1.1 A on 90% of 7TM residues). This level of structural similarity is typically observed within GPCR subfamilies, highlighting the delta-branch conservation pattern.

### Unique disulfide bond linking TM1 and TM7

The CysLT1R-pran structure reveals a new disulfide bond between C14 1.23 and C267 7.25, connecting the extracellular tips of TM1 and TM7. While disulfide bonds between the N terminus and TM7-ECL3 junction have been observed, a disulfide bond directly linking two transmembrane helices has not been previously reported in GPCRs. Alanine mutations of either cysteine resulted in 2-6 fold drop in LTD4 potency.

### Pre-activated P-I-F microswitch with inactive state stabilization

CysLT1R shows an unusual pattern where the P-I-F (Pro-Ile-Phe) microswitch appears pre-activated while the receptor is stabilized in the inactive state by a tightly bound sodium ion. This suggests a novel GPCR activation mechanism where the receptor is primed for activation but held in check by the sodium ion.


## Cross-References

- [P2Y1 Receptor](/xray-mp-wiki/proteins/gpcr/human-p2y1-receptor/) — Close structural homolog (Ca RMSD 1.1 A); delta-branch GPCR comparison
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for solubilization and purification
- [Lipidic Cubic Phase (In Meso) Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method used for CysLT1R structures
- [GPCR G Protein Coupling](/xray-mp-wiki/concepts/gpcr-g-protein-coupling/) — CysLT1R is a GPCR that signals through Gq/11 and Gi/o pathways
- [Cholesteryl Hemisuccinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Additive used in purification to stabilize the receptor
- [Bril](/xray-mp-wiki/reagents/protein-tags/bril/) — Referenced in the context of Bril
- [Truncation](/xray-mp-wiki/concepts/truncation/) — Referenced in the context of Truncation
- [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) — Referenced in the context of Hepes
- [Mgcl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/) — Referenced in the context of Mgcl2
- [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) — Referenced in the context of Iodoacetamide
