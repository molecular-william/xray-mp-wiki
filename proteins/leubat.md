---
title: LeuBAT Engineered Biogenic Amine Transporter Homologue
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature12648]
verified: false
---

# LeuBAT Engineered Biogenic Amine Transporter Homologue

## Overview

LeuBAT is an engineered mutant of the bacterial amino acid transporter LeuT from Aquifex aeolicus, designed to harbour human biogenic amine transporter (BAT)-like pharmacology. By introducing targeted mutations around the primary binding pocket, LeuBAT binds selective serotonin reuptake inhibitors (SSRIs), serotonin-noradrenaline reuptake inhibitors (SNRIs), and tricyclic antidepressants (TCAs) with high affinity, recapitulating the pharmacological properties of eukaryotic BATs. The final LeuBAT mutant (Delta13 LeuBAT) binds the SSRI sertraline with a Kd of 18 nM. Twelve crystal structures of LeuBAT in complex with antidepressants reveal a common binding mode in which inhibitors lock the transporter in a sodium- and chloride-bound outward-facing open conformation.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature12648 | not specified | not specified | not specified | Delta13 LeuBAT (13 mutations in LeuT to confer BAT-like pharmacology), outward-facing open conformation | Sertraline |
| doi/10.1038##nature12648 | not specified | not specified | not specified | Delta13 LeuBAT, outward-facing open conformation | Paroxetine |
| doi/10.1038##nature12648 | not specified | not specified | not specified | Delta13 LeuBAT, outward-facing open conformation | Fluoxetine |
| doi/10.1038##nature12648 | not specified | not specified | not specified | Delta13 LeuBAT, outward-facing open conformation | Fluvoxamine |
| doi/10.1038##nature12648 | not specified | not specified | not specified | Delta13 LeuBAT, outward-facing open conformation | Duloxetine |
| doi/10.1038##nature12648 | not specified | not specified | not specified | Delta13 LeuBAT, outward-facing open conformation | Desvenlafaxine |
| doi/10.1038##nature12648 | not specified | not specified | not specified | Delta13 LeuBAT, outward-facing open conformation | Clomipramine (CMI) |
| doi/10.1038##nature12648 | not specified | not specified | not specified | Delta6 LeuBAT, outward-facing open conformation | Mazindol |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: LeuT from A. aeolicus with 13 mutations (Delta13) to confer human BAT-like pharmacology

### Purification Workflow

- **Expression system**: Escherichia coli
- **Expression construct**: Delta13 LeuBAT mutant

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell membrane solubilization | Detergent solubilization | -- | 25 mM Tris-HCl pH 8.0, 250 mM NaCl, 1% MNG-3 + MNG-3 (lauryl maltose neopentyl glycol) | Cell membranes solubilized with MNG-3 instead of C12 |
| Immobilized-metal affinity chromatography | IMAC | IMAC resin | 25 mM Tris-HCl pH 8.0, 250 mM NaCl, 0.02% MNG-3 + 0.02% MNG-3 | Purified by IMAC in the presence of 0.02% MNG-3 |
| Size-exclusion chromatography | SEC | Size-exclusion column | 25 mM Tris-HCl pH 8.0, 150 mM NaCl, 40 mM n-octyl-beta-D-glucoside + 40 mM n-octyl-beta-D-glucoside | For crystallization, LeuBAT purified by SEC in n-octyl-beta-D-glucoside; concentrated to 2.5 mg/ml and supplemented with saturating serotonin or mazindol |

**Final sample**: 2.5 mg/ml in 25 mM Tris-HCl pH 8.0, 150 mM NaCl, 40 mM n-octyl-beta-D-glucoside


## Crystallization

### doi/10.1038##nature12648

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | Delta13 LeuBAT at 2.5 mg/ml supplemented with saturating serotonin or mazindol |
| Reservoir | 100 mM NaPi pH 7.0, 100 mM NaCl, 32-34% PEG300 |
| Temperature | 20 C |
| Growth time | not specified |
| Cryoprotection | Crystals flash frozen in liquid nitrogen after soaking |
| Notes | Crystals soaked for 1 h in crystallization solution containing antidepressants (4 mM paroxetine, 20 mM desvenlafaxine, 3.7 mM sertraline, 3.7 mM fluoxetine, 3 mM duloxetine, 3 mM fluvoxamine, or 10 mM CMI) |

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | Delta13 LeuBAT at 2.5 mg/ml supplemented with saturating serotonin or mazindol |
| Reservoir | 100 mM glycine pH 9.4, 0.1 M Li2SO4, 29-31% PEG400 |
| Temperature | 20 C |
| Growth time | not specified |
| Cryoprotection | Crystals flash frozen in liquid nitrogen after soaking |
| Notes | Alternative crystallization condition; crystals soaked for 1 h in antidepressant-containing solution |


## Biological / Functional Insights

### Engineered BAT-like pharmacology in bacterial transporter

LeuBAT was engineered by introducing ~20 residues around the primary binding pocket of LeuT that are divergent from human SERT. The final Delta13 LeuBAT mutant binds the SSRI sertraline with a Kd of 18 nM, paroxetine with Kd = 431 +/- 24 nM, and mazindol with Kd = 112 +/- 18 nM. The mazindol Kd is similar to that of human SERT (103 +/- 4.7 nM). LeuBAT displays high-affinity binding to a range of SSRIs, SNRIs, and TCAs, recapitulating the pharmacological properties of eukaryotic BATs. Although uptake experiments show the constructs are not active in transporting serotonin or dopamine, LeuBAT serves as a structural paradigm for understanding antidepressant binding to BATs.

### Common binding mode of chemically diverse antidepressants

Twelve crystal structures of LeuBAT in complex with four classes of antidepressants (SSRIs, SNRIs, TCAs, and the stimulant mazindol) reveal a remarkably similar mode of binding. The chemically diverse inhibitors straddle transmembrane helix 3, wedge between TM3/TM8 and TM1/TM6, and lock the transporter in a sodium- and chloride-bound outward-facing open conformation. The amine groups of all inhibitors interact with the carboxyl group of Asp24, forming salt bridges. Hydrophobic/aromatic moieties insert into a groove formed by residues including Tyr21, Val104, Tyr108, Phe253, and Phe259.

### Subsite architecture of the primary drug binding pocket

The primary orthosteric binding site of LeuBAT is organized into subsites A, B, and C. Subsite A contains residues Tyr21, Ala22, Asp24, and Ser355/Ser356. Subsite B is defined by residues Val104, Pro101, Ala105, Tyr107, and Phe259. Subsite C includes Phe253, Tyr108, and Asp404. Mutational studies (Y21A, D24E, F259Y, S355T) in LeuBAT show similar effects to homologous SERT mutants (Y95A, D98E, F341Y, S438T), confirming that LeuBAT is a reliable model for BAT-inhibitor complexes.

### Outward-facing open conformation locked by antidepressants

All LeuBAT-antidepressant complexes adopt an outward-facing open conformation with bound sodium and chloride ions. The antidepressants wedge between TM3/TM8 and TM1/TM6, locking the transporter in this conformation and preventing the transition to inward-facing states. This mechanism explains the competitive inhibition of biogenic amine transport by SSRIs, SNRIs, and TCAs in eukaryotic BATs.


## Cross-References

- [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/leut/) — LeuBAT is an engineered mutant of LeuT with 13 mutations conferring BAT-like pharmacology
- [Drosophila Dopamine Transporter (dDAT)](/xray-mp-wiki/proteins/d-dopamine-transporter/) — Eukaryotic NSS family member; LeuBAT pharmacology compared with human DAT
- [Neurotransmitter/Sodium Symporter (NSS) Family](/xray-mp-wiki/concepts/nss-family/) — LeuBAT models eukaryotic NSS transporters (SERT, DAT, NET)
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — Antidepressants lock LeuBAT in outward-facing state, blocking transport cycle
- [Rocking-Bundle Mechanism](/xray-mp-wiki/concepts/rocking-bundle-mechanism/) — Mechanism of ion-coupled solute flux by NSS transporters
- [Sertraline](/xray-mp-wiki/reagents/ligands/sertraline/) — SSRI with Kd = 18 nM for LeuBAT; highest affinity ligand studied
- [Paroxetine](/xray-mp-wiki/reagents/ligands/paroxetine/) — SSRI used for binding competition assays (Kd = 431 nM for LeuBAT)
- [Lauryl Maltose Neopentyl Glycol (MNG-3)](/xray-mp-wiki/reagents/detergents/mng-3/) — Amphipol used for LeuBAT solubilization and purification
