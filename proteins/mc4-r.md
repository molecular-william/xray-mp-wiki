---
title: Human Melanocortin 4 Receptor (MC4-R)
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1021##acs.jmedchem.3c01822, doi/10.1021##acs.jmedchem.0c01620]
verified: false
---

# Human Melanocortin 4 Receptor (MC4-R)

## Overview

The human melanocortin 4 receptor (MC4-R) is a class A G protein-coupled receptor (GPCR) that plays a central role in regulating energy homeostasis and feeding behavior. MC4-R is highly expressed in the hypothalamus, brainstem, and limbic system, where it couples to Gs proteins to activate adenylyl cyclase and produce cAMP. Activation of MC4-R-expressing neurons by alpha-MSH reduces food intake and increases energy expenditure, while inhibition by agouti-related protein (AgRP) increases hunger. MC4-R is a major drug target for treating metabolic and eating disorders including obesity, anorexia nervosa, and cancer cachexia.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1021##acs.jmedchem.3c01822 | 8WKY | 2.90 | N/A | Human MC4-R with thermostabilizing mutations E49^1.37V, N97^2.57L, S99^2.59F, S131^3.34A, D298^7.49N; 15 N-terminal and 12 C-terminal amino acid truncations; PGS (Pyrococcus abyssi glycogen synthase catalytic domain G218-S413) fusion in ICL3 between H222 and R236; co-crystallized with PG-934 peptide antagonist | PG-934 |
| doi/10.1021##acs.jmedchem.3c01822 | 8WKZ | 3.30 | N/A | Human MC4-R with thermostabilizing mutations E49^1.37V, N97^2.57L, S99^2.59F, S131^3.34A, D298^7.49N; 15 N-terminal and 12 C-terminal amino acid truncations; PGS fusion in ICL3 between H222 and R236; co-crystallized with SBL-MC-31 peptide antagonist | SBL-MC-31 |
| doi/10.1021##acs.jmedchem.0c01620 | 6W25 | 2.50 | N/A | Human MC4-R with thermostabilizing mutations and PGS fusion; co-crystallized with SHU9119 peptide antagonist | SHU9119 |

## Expression and Purification

- **Expression system**: Spodoptera frugiperda (Sf9) cells using Bac-to-Bac baculovirus expression system
- **Construct**: Codon-optimized human MC4-R in pFastBac1 vector with HA signal sequence, N-terminal FLAG tag, PreScission protease recognition site (Leu-Glu-Val-Leu-Phe-Gln/Gly-Pro), and C-terminal 10x His tag. Thermostabilizing mutations: E49^1.37V, N97^2.57L, S99^2.59F, S131^3.34A, D298^7.49N. 15 N-terminal and 12 C-terminal truncations. PGS fusion in ICL3 between H222 and R236.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell membrane preparation | Sf9 cell harvest, hypotonic lysis buffer (10 mM HEPES pH 7.0, 10 mM MgCl2, 20 mM KCl, EDTA-free protease inhibitor), centrifugation at 60,000xg for 30 min | -- | 10 mM HEPES pH 7.0, 10 mM MgCl2, 20 mM KCl + -- | Cell membranes prepared from Sf9 cells infected at 2x10^6 cells/mL, MOI 5, grown 48 h at 27 C |
| Protein extraction | Membrane solubilization by incubation 3 h at 4 C with gentle mixing | -- | 50 mM HEPES pH 7.0, 800 mM NaCl + 1.0% DDM, 0.2% CHS | Extracted from membranes in 50 mM HEPES pH 7.0, 800 mM NaCl, 1.0% DDM, 0.2% CHS |
| IMAC purification | Incubation with TALON IMAC resin overnight at 4 C with 30 mM imidazole | TALON IMAC resin | 50 mM HEPES pH 7.0, 800 mM NaCl, 10% glycerol, 10 mM MgCl2, 0.05% DDM, 0.01% CHS, 30 mM imidazole, 8 mM ATP + 0.05% DDM, 0.01% CHS (wash); 0.01% DDM, 0.002% CHS (elution) | Washed with wash buffer 1 (800 mM NaCl, 10% glycerol, 10 mM MgCl2, 0.05% DDM, 0.01% CHS, 30 mM imidazole, 8 mM ATP, 50 uM test peptides) and wash buffer 2 (without MgCl2 and ATP); eluted with 220 mM imidazole, 100 uM test peptides |
| Deglycosylation | Incubation with EndoH overnight at 4 C | -- | 50 mM HEPES pH 7.0, 800 mM NaCl, 0.01% DDM, 0.002% CHS + 0.01% DDM | EndoH in-house production; removed N-glycosylation |
| Concentration | Concentrated to 35-45 mg/mL using 100 kDa cutoff concentrator | -- | 50 mM HEPES pH 7.0, 800 mM NaCl, 0.01% DDM, 0.002% CHS + 0.01% DDM | Sartorius concentrator, Göttingen, Germany |


## Crystallization

No crystallization described.

## Biological / Functional Insights

### Two discrete binding sub-pockets at TM7-TM1-TM2 interfaces

The MC4-R:PG-934 and MC4-R:SBL-MC-31 structures revealed two discrete binding sub-pockets delimited by residues from TM2, TM1, TM7, and the N-terminal domain. The first sub-pocket is occupied by the SHU9119 His6 side chain and is formed by E100^2.60, T101^2.61, I104^2.64 on TM2, F51^1.39 on TM1, and N285^7.36 on TM7. The second sub-pocket is delineated by TM7 residues F284^7.35 and L288^7.39, plus the N-terminal Q43. N285^7.36 forms a distinctive ridge separating the two sub-pockets. This structural insight enabled rational design of peptide analogs with enhanced MC4-R over MC1-R selectivity up to 132-fold.

### Ca2+ coordination network stabilizes ligand binding

Ca2+ is coordinated by three receptor acidic residues (E100^2.60, D122^3.25, D126^3.29) and the backbone carbonyl oxygens of Asp5 and DNal(2')7 from the peptide ligands. This coordination network is conserved across all melanocortin receptor subtypes and both agonist and antagonist ligands. Ca2+ binding "primes" the receptor in a sub-active state. E100A and D122A mutations cause modest 2-5 fold decreases in MT-II potency but 68-121 fold decreases in setmelanotide potency, while D126A has profound effects on both.

### Biased signaling through MC4-R:Kir7.1 coupling

MC4-R couples to the inwardly rectifying K+ channel Kir7.1 through a G protein-independent mechanism. Alpha-MSH and agonists induce channel closure (decreased K+ conductance, depolarization, increased firing), while AgRP and some antagonists induce channel opening (increased K+ conductance, hyperpolarization, decreased firing). This biased signaling modality allows targeting of MC4-R:Kir7.1 complex independently of G protein signaling, potentially avoiding G protein-associated side effects.


## Cross-References

- [PG-934](/xray-mp-wiki/reagents/ligands/pg-934/) — Novel co-crystallized peptide antagonist, PDB 8WKY
- [SBL-MC-31](/xray-mp-wiki/reagents/ligands/sbl-mc-31/) — Novel co-crystallized peptide antagonist, PDB 8WKZ
- [SHU9119](/xray-mp-wiki/reagents/ligands/shu9119/) — Reference peptide antagonist, previously crystallized PDB 6W25
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for MC4-R solubilization and purification
- [Cholesterol Hydrogen Succinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Lipid additive used in MC4-R solubilization buffer
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Primary lipid component of LCP crystallization matrix
- [Calcium Chloride (CaCl2)](/xray-mp-wiki/reagents/additives/calcium-chloride/) — Crystallization additive (50-100 mM) and Ca2+ coordination cofactor
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method used for MC4-R:PG-934 and MC4-R:SBL-MC-31
