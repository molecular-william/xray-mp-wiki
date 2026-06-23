---
title: "CCR5 Chemokine Receptor (C-C Chemokine Receptor Type 5)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1241475]
verified: false
---

# CCR5 Chemokine Receptor (C-C Chemokine Receptor Type 5)

## Overview

CCR5 (C-C chemokine receptor type 5) is a class A G protein-coupled receptor (GPCR) that functions as a chemokine receptor and is a major co-receptor for HIV-1 entry. The crystal structure of CCR5 bound to [Maraviroc](/xray-mp-wiki/reagents/ligands/maraviroc/), an allosteric inverse agonist and HIV entry inhibitor, was determined by X-ray crystallography. CCR5 is structurally similar to the chemokine receptor [Human CXCR4 Chemokine Receptor](/xray-mp-wiki/proteins/gpcr/cxcr4/) (Calpha RMSD of 1.8 Å within the 7TM bundle at 34% sequence identity) but differs in several key regions. ECL2 forms a beta-hairpin structure stabilized by disulfide bonds (Cys101(3.25)-Cys178 in ECL2 and Cys20-Cys269(7.25)). CCR5 features a short alpha helix VIII (absent in CXCR4), a tilted helix IV with a shorter intracellular portion, and a two-turn alpha helix in ICL2 that runs parallel to the membrane. [Maraviroc](/xray-mp-wiki/reagents/ligands/maraviroc/) binds in a deep pocket defined by residues from helices I, II, III, V, VI, and VII, making no contacts with the extracellular loops, and functions as an allosteric inverse agonist by stabilizing CCR5 in an inactive conformation.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.1241475 | 4MBS | 2.7 | — | CCR5-[Maraviroc](/xray-mp-wiki/reagents/ligands/maraviroc/) complex | [Maraviroc](/xray-mp-wiki/reagents/ligands/maraviroc/) |

## Expression and Purification

- **Expression system**: Insect cell expression (Sf9 or High Five cells)
- **Construct**: CCR5 with T4 lysozyme fusion (BRIL) for crystallization
- **Notes**: Detailed expression protocol described in supplementary materials

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation and solubilization | Standard membrane protein solubilization | — |  | Methods described in supplementary materials |
| Purification | Affinity chromatography and size-exclusion chromatography | — |  | Details in supplementary materials |


## Crystallization

### doi/10.1126##science.1241475

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) or vapor diffusion |
| Protein sample | CCR5-[Maraviroc](/xray-mp-wiki/reagents/ligands/maraviroc/) complex |
| Notes | Structure determined in complex with [Maraviroc](/xray-mp-wiki/reagents/ligands/maraviroc/). Detailed crystallization conditions in supplementary materials. |


## Biological / Functional Insights

### Maraviroc binding mode and allosteric inverse agonism

[Maraviroc](/xray-mp-wiki/reagents/ligands/maraviroc/) occupies the bottom of the CCR5 ligand-binding pocket, defined by residues from helices I, II, III, V, VI, and VII. Key interactions include: (1) salt bridge between the protonated tropane nitrogen and Glu283(7.39); (2) hydrogen bond between the carboxamide nitrogen and Tyr251(6.51); (3) hydrogen bonds between the triazole amine and Tyr37(1.39) and a water molecule; (4) hydrogen bonds between a fluorine of the cyclohexane ring and Thr195(5.39) and Thr259(6.59); and (5) hydrophobic interactions between the phenyl group and five aromatic residues (Tyr108(3.32), Phe109(3.33), Phe112(3.36), Trp248(6.48), Tyr251(6.51)). The length of the carbon chain between the tropane and carboxamide nitrogens correlates with anti-HIV activity. [Maraviroc](/xray-mp-wiki/reagents/ligands/maraviroc/) acts as an allosteric inverse agonist by stabilizing CCR5 in an inactive conformation, reducing chemokine and gp120 binding.

### Structural basis for HIV-1 co-receptor selectivity between CCR5 and CXCR4

The ligand-binding pockets of CCR5 and [Human CXCR4 Chemokine Receptor](/xray-mp-wiki/proteins/gpcr/cxcr4/) differ substantially in charge distribution. In [Human CXCR4 Chemokine Receptor](/xray-mp-wiki/proteins/gpcr/cxcr4/), acidic residues (Asp97(2.63), Asp171(4.60), Asp187 in ECL2, Asp193(5.32), Asp262(6.58)) are critical for ligand binding and HIV-1 infectivity. In CCR5, these are substituted by uncharged residues (Tyr89(2.63), Gly163(4.60), Ser179, Gln188(5.32), Asn258(6.58)). Moreover, the [Human CXCR4 Chemokine Receptor](/xray-mp-wiki/proteins/gpcr/cxcr4/) N terminus contains nine acidic residues while CCR5 has only three. These differences correlate with the different charge distributions in the V3 loops of X4-tropic versus R5-tropic HIV-1 viruses. Models of CCR5-R5-V3 and [Human CXCR4 Chemokine Receptor](/xray-mp-wiki/proteins/gpcr/cxcr4/)-X4-V3 complexes suggest that differential charge distribution and steric hindrances from residue substitutions are major determinants of HIV-1 co-receptor selectivity.

### Structural differences between CCR5 and CXCR4

Beyond the binding pocket, CCR5 and [Human CXCR4 Chemokine Receptor](/xray-mp-wiki/proteins/gpcr/cxcr4/) differ in several structural features: (1) CCR5 has a short helix VIII at the C terminus with a conserved F(RK)xx(FL)xxx(LF) motif, while [Human CXCR4 Chemokine Receptor](/xray-mp-wiki/proteins/gpcr/cxcr4/) has an extended disordered C terminus; (2) helix IV in CCR5 is tilted ~15 degrees relative to [Human CXCR4 Chemokine Receptor](/xray-mp-wiki/proteins/gpcr/cxcr4/), with its intracellular portion 1.5 turns shorter; (3) ICL2 in CCR5 contains a two-turn alpha helix running parallel to the membrane, stabilized by hydrophobic interactions (Phe135, Ala136 with Leu128(3.53) and Ala129(3.54)), while ICL2 is unstructured in [Human CXCR4 Chemokine Receptor](/xray-mp-wiki/proteins/gpcr/cxcr4/); (4) the extracellular end of helix VII shifts ~3 Å away from the central axis in CCR5 versus [Human CXCR4 Chemokine Receptor](/xray-mp-wiki/proteins/gpcr/cxcr4/).


## Cross-References

- [Human Beta2-Adrenergic Receptor (beta2 AR)](/xray-mp-wiki/proteins/gpcr/beta2-adrenergic-receptor/) — Class A GPCR for structural comparison of 7TM architecture
- [Maraviroc](/xray-mp-wiki/reagents/ligands/maraviroc/) — Co-crystallized allosteric inverse agonist and HIV entry inhibitor bound to CCR5 in the structure
- [GR (Halobacterium sp. GR Bacteriorhodopsin)](/xray-mp-wiki/proteins/rhodopsins/gr/) — Related protein structure
- [Human Beta2-Adrenergic Receptor (beta2 AR)](/xray-mp-wiki/proteins/gpcr/beta2-adrenergic-receptor/) — Related protein structure
- [Human CXCR4 Chemokine Receptor](/xray-mp-wiki/proteins/gpcr/cxcr4/) — Related protein structure
- [ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel)](/xray-mp-wiki/proteins/cys-loop-receptors/elic/) — Related protein structure
- [RibU (ECF-Type Riboflavin Transporter S Component from Staphylococcus aureus)](/xray-mp-wiki/proteins/pumps-atpases/ribu/) — Related protein structure
- [X-ray Crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/) — Method used in the study
- [Maraviroc](/xray-mp-wiki/reagents/ligands/maraviroc/) — Reagent used in the study
- [n-Octyl beta-D-glucopyranoside (OG)](/xray-mp-wiki/reagents/detergents/og/) — Detergent used in the study
