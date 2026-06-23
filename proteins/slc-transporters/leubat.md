---
title: LeuBAT (LeuT Engineered for Antidepressant Pharmacology)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature12648]
verified: false
---

# LeuBAT (LeuT Engineered for Antidepressant Pharmacology)

## Overview

LeuBAT is an engineered mutant of the bacterial leucine transporter [LEUT](/xray-mp-wiki/proteins/enzymes/leut/) from Aquifex aeolicus that harbours human biogenic amine transporter (BAT)-like pharmacology. By introducing 13 mutations around the primary binding pocket, LeuBAT binds the SSRI [Sertraline](/xray-mp-wiki/reagents/ligands/sertraline/) with a Kd of 18 nM and displays high-affinity binding to a range of SSRIs, SNRIs, and TCAs. Twelve crystal structures of LeuBAT in complex with four classes of antidepressants reveal that chemically diverse inhibitors share a remarkably similar binding mode in which they straddle transmembrane helix 3, wedge between TM3/TM8 and TM1/TM6, and lock the transporter in a sodium- and chloride-bound outward-facing open conformation.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature12648 |  |  |  | LeuBAT Delta13 mutant with BAT-like pharmacology in complex with antidepressants | [Sertraline](/xray-mp-wiki/reagents/ligands/sertraline/), [Paroxetine](/xray-mp-wiki/reagents/ligands/paroxetine/), [Fluoxetine](/xray-mp-wiki/reagents/ligands/fluoxetine/), [Fluvoxamine](/xray-mp-wiki/reagents/ligands/fluvoxamine/), [Duloxetine](/xray-mp-wiki/reagents/ligands/duloxetine/), [Desvenlafaxine](/xray-mp-wiki/reagents/ligands/desvenlafaxine/), [CMI](/xray-mp-wiki/reagents/ligands/clomipramine/), [Mazindol](/xray-mp-wiki/reagents/ligands/mazindol/) |

## Expression and Purification

- **Expression system**: E. coli, LeuBAT mutants expressed and purified as for wild-type [LEUT](/xray-mp-wiki/proteins/enzymes/leut/)
- **Construct**: Delta13 LeuBAT with 13 mutations: L9S, I17A, L25A, A50S, V33I, N21S, A22S, T254S, S256G, I359G, Q250L, A53D, W6L (and other mutations enabling BAT-like pharmacology)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane solubilization | Detergent solubilization | IMAC | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0 250 mM NaCl + 1% Lauryl [Maltose](/xray-mp-wiki/reagents/additives/maltose/) Neopentyl Glycol (MNG-3) | Cell membranes solubilized; protein purified by IMAC in 0.02% MNG-3 |
| Size-exclusion chromatography | SEC | -- | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0 150 mM NaCl 40 mM [OG](/xray-mp-wiki/reagents/detergents/og/) + 40 mM [OG](/xray-mp-wiki/reagents/detergents/og/) | Buffer exchanged into [OG](/xray-mp-wiki/reagents/detergents/og/) for crystallization |


## Crystallization

### doi/10.1038##nature12648

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | LeuBAT at 2.5 mg/ml with saturating [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki/reagents/ligands/serotonin/) or [Mazindol](/xray-mp-wiki/reagents/ligands/mazindol/) |
| Reservoir | 100 mM NaPi pH 7.0 100 mM NaCl 32-34% [PEG300](/xray-mp-wiki/reagents/additives/peg300/); or 100 mM [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) pH 9.4 0.1 M Li2SO4 29-31% [PEG400](/xray-mp-wiki/reagents/additives/peg-400/) |
| Temperature | 20 |
| Notes | Crystals grown in presence of [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki/reagents/ligands/serotonin/) soaked for 1 h in crystallization solution containing antidepressants; 12 crystal structures determined; [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using LeuT-Trp (PDB 3F3A) as search probe |


## Biological / Functional Insights

### Shared binding mode for diverse antidepressants

Despite chemical diversity, all SSRIs ([Sertraline](/xray-mp-wiki/reagents/ligands/sertraline/), [Paroxetine](/xray-mp-wiki/reagents/ligands/paroxetine/), [Fluoxetine](/xray-mp-wiki/reagents/ligands/fluoxetine/), [Fluvoxamine](/xray-mp-wiki/reagents/ligands/fluvoxamine/)), SNRIs ([Duloxetine](/xray-mp-wiki/reagents/ligands/duloxetine/), [Desvenlafaxine](/xray-mp-wiki/reagents/ligands/desvenlafaxine/)), and TCAs ([CMI](/xray-mp-wiki/reagents/ligands/clomipramine/)) bind to the primary orthosteric pocket in a similar orientation. The amine groups are proximal to the carboxyl group of Asp24 and form hydrogen bonds with main-chain carbonyls of Tyr21, Ala22, and Phe253. The halogenated aromatic rings insert into a hydrophobic groove formed by Pro101, Val104, Ala105, Ser356, and Gly359. This common binding mode defines three subsites (A, B, C) within the primary pocket.

### Outward-facing open conformation

All 12 LeuBAT-antidepressant structures adopt an outward-facing open conformation with sodium and chloride ions bound. This contrasts with the LeuT-TCA structures where TCAs bind in the extracellular vestibule. The inhibitors lock the transporter in this conformation, explaining their competitive inhibition mechanism at human BATs versus the non-competitive mechanism seen in wild-type [LEUT](/xray-mp-wiki/proteins/enzymes/leut/).

### Pharmacological validation

LeuBAT was validated as a model for human [SERT](/xray-mp-wiki/proteins/slc-transporters/ssert/) by mutational analysis. Mutations Y21A, D24E, F259Y, and S355T in LeuBAT showed similar effects on [Sertraline](/xray-mp-wiki/reagents/ligands/sertraline/) binding as the homologous mutations (Y95A, D98E, F341Y, S438T) in human [SERT](/xray-mp-wiki/proteins/slc-transporters/ssert/), demonstrated by a linear logKd vs logKi relationship. The pharmacological profile of LeuBAT is a hybrid of human DAT, NET, and [SERT](/xray-mp-wiki/proteins/slc-transporters/ssert/) properties.

### Chloride binding site

The outward-facing open conformation of LeuBAT includes a chloride ion binding site. This is consistent with the chloride dependence of human monoamine transporters and explains why chloride is required for high-affinity inhibitor binding in [SERT](/xray-mp-wiki/proteins/slc-transporters/ssert/).


## Cross-References

- [Drosophila Dopamine Transporter (dDAT)](/xray-mp-wiki/proteins/slc-transporters/d-dat/) — Related biogenic amine transporter for comparison
- [Sertraline](/xray-mp-wiki/reagents/ligands/sertraline/) — SSRI co-crystallized with LeuBAT
- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — Detergent used for solubilization and purification
- [GPCR Active Conformation](/xray-mp-wiki/concepts/gpcr-active-conformation/) — LeuBAT represents outward-facing open conformation relevant to transporter mechanism
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [LEUT](/xray-mp-wiki/proteins/enzymes/leut/) — Related protein structure
- [SERT](/xray-mp-wiki/proteins/slc-transporters/ssert/) — Related protein structure
- [Maltose](/xray-mp-wiki/reagents/additives/maltose/) — Additive used in purification or crystallization buffers
- [PEG300](/xray-mp-wiki/reagents/additives/peg300/) — Additive used in purification or crystallization buffers
- [PEG400](/xray-mp-wiki/reagents/additives/peg-400/) — Additive used in purification or crystallization buffers
