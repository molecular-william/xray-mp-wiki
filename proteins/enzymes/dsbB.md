---
title: DsbB (Disulfide Bond Formation Protein B)
created: 2026-06-08
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2006.10.034, doi/10.1038##emboj.2009.21, doi/10.1126##sciadv.abe3717]
verified: false
---

# DsbB (Disulfide Bond Formation Protein B)

## Overview

DsbB is an integral membrane protein from Escherichia coli that functions as the
central oxidase in the bacterial disulfide bond formation pathway. Together with
the periplasmic protein [Dsba](/xray-mp-wiki/proteins/enzymes/dsbA/), DsbB catalyzes the de novo generation of disulfide
bonds in substrate proteins. DsbB spans the cytoplasmic membrane with four
transmembrane helices and contains two periplasmic loops (P1 and P2) that harbor
essential cysteine residues (Cys41-Cys44 in P1 and Cys104-Cys130 in P2). The
enzyme uses bound [Ubiquinone](/xray-mp-wiki/reagents/cofactors/ubiquinone/) (UQ) as an electron acceptor to generate disulfide
bonds and transfer them to [Dsba](/xray-mp-wiki/proteins/enzymes/dsbA/). DsbB undergoes elaborate conformational
transitions during catalysis, driven by the sequential relocation of its active-site
cysteines, which is regulated by a membrane-associated amphiphilic "horizontal
helix" in the P2 loop.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##emboj.2009.21 |  | 3.4 | C2 | DsbB(Cys41Ser) mutant in complex with Fab antibody fragment | [Ubiquinone](/xray-mp-wiki/reagents/cofactors/ubiquinone/) (UQ) |
| doi/10.1038##emboj.2009.21 | 2HI7 | 3.7 | P4(2)2(1)2 | DsbB(Cys130Ser) in disulfide-linked complex with DsbA(Cys33Ala) | [Ubiquinone](/xray-mp-wiki/reagents/cofactors/ubiquinone/) (UQ) |
| doi/10.1126##sciadv.abe3717 | 6WVF | 2.9 |  | DsbB with termini restrained by split sfGFP | [Ubiquinone](/xray-mp-wiki/reagents/cofactors/ubiquinone/) (UQ) |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Full-length DsbB with His6-myc tag; Cys41Ser mutant and Cys130Ser mutant variants

### Purification Workflow

- **Expression system**: E. coli SS141 (dsbB::kan5)
- **Expression construct**: His6-myc tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Complex formation | Size-exclusion chromatography | -- | -- + -- | DsbB-Fab complex of 1:1 stoichiometry prepared by size-exclusion chromatography |
| Crystal growth | Sitting-drop vapor diffusion | -- | 0.1 M [Mops](/xray-mp-wiki/reagents/buffers/mops/) pH 7.0 + -- | Crystallized in 15% PEG3350, 0.1 M magnesium formate, 0.1 M [Mops](/xray-mp-wiki/reagents/buffers/mops/) (pH 7.0) |


## Crystallization

### doi/10.1038##emboj.2009.21

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | DsbB(Cys41Ser)-Fab complex |
| Reservoir | 15% PEG3350, 0.1 M magnesium formate, 0.1 M [Mops](/xray-mp-wiki/reagents/buffers/mops/) (pH 7.0) |
| Temperature | Not specified |
| Growth time | 10 days |
| Cryoprotection | 27% PEG3350, 0.1 M magnesium formate, 0.1 M [Mops](/xray-mp-wiki/reagents/buffers/mops/) pH 7.0, 0.1% [DHPC](/xray-mp-wiki/reagents/detergents/dhpc/) |
| Notes | Co-crystallization with monoclonal Fab antibody fragment was essential for obtaining diffracting crystals. Wild-type DsbB was conformationally heterogeneous; the Cys41Ser mutant provided homogeneous initial-state conformation. |


## Biological / Functional Insights

### Cys104-Cys130 disulfide is the initial-state substrate for DsbA

The 3.4 A structure of DsbB(Cys41Ser)-Fab directly visualizes the Cys104-Cys130 disulfide bond that is ready to interact with reduced [Dsba](/xray-mp-wiki/proteins/enzymes/dsbA/). This represents the initial state of DsbB before [Dsba](/xray-mp-wiki/proteins/enzymes/dsbA/) binding, confirming the 'cysteine relocation' mechanism proposed previously. Upon [Dsba](/xray-mp-wiki/proteins/enzymes/dsbA/) binding, Cys104 is pulled into the hydrophobic groove of [Dsba](/xray-mp-wiki/proteins/enzymes/dsbA/), separating it from Cys130.

### Amphiphilic horizontal helix regulates DsbB activity

The P2 loop of DsbB contains a membrane-parallel amphiphilic alpha-helix (horizontal helix, residues 116-120) that associates peripherally with the cytoplasmic membrane through hydrophobic side chains. Systematic mutagenesis showed that disrupting this membrane association with charged or helix-breaking residues severely impaired [Dsba](/xray-mp-wiki/proteins/enzymes/dsbA/) oxidation activity. The horizontal helix acts as a membrane tether that restricts movement of the catalytically essential P2 cysteines, functioning as a ratchet for thiol-disulfide exchange.

### Conformational transitions during DsbB catalysis

Comparison of three DsbB states - the initial state (DsbB(Cys41Ser)-Fab), the DsbA-bound state (DsbB(Cys130Ser)-DsbA(Cys33Ala)), and the NMR structure of DsbB[CSSC] - reveals sequential cysteine relocations. In the initial state, Cys104-Cys130 are paired. Upon [Dsba](/xray-mp-wiki/proteins/enzymes/dsbA/) binding, Cys104 separates from Cys130 and forms an intermolecular disulfide with [Dsba](/xray-mp-wiki/proteins/enzymes/dsbA/) Cys30. After [Dsba](/xray-mp-wiki/proteins/enzymes/dsbA/) release, the Cys130-containing loop moves to approach Cys41 in P1, enabling the next catalytic cycle.

### Charge-transfer complex between Cys44 and ubiquinone

The 3.4 A structure provides direct evidence of a charge-transfer complex between Cys44 of DsbB and bound [Ubiquinone](/xray-mp-wiki/reagents/cofactors/ubiquinone/) (UQ), with the sulfur atom of Cys44 only 3.1 A from the C1 atom of the UQ ring. Arg48 forms a hydrogen bond with the thiolate form of Cys44, stabilizing the complex. This supports the proposed mechanism of de novo disulfide bond generation on DsbB using the oxidizing equivalents of quinone species.

### Catalytic triad mechanism revealed by high-resolution structure

The 2.9 A structure of termini-restrained DsbB (PDB 6WVF) reveals that the thiol oxidoreductase is activated through a catalytic triad (Arg48, His91, Glu47), similar to cysteine proteases. Arg48 and His91 form hydrogen bonds with the two carbonyl oxygens of the bound ubiquinone, stabilizing the charge-transfer complex and facilitating its formation through induced polarization of the quinone ring. Glu47 is positioned to maintain the correct orientation of Arg48. Arg48 and His91 are among the most conserved residues in DsbB homologs, and mutations of these residues show accumulation of DsbB-DsbA complex and reduced quinone binding, confirming impaired Cys44 reactivity.


## Cross-References

- [DsbA](/xray-mp-wiki/proteins/enzymes/dsbA/) — Direct functional partner in periplasmic disulfide bond formation
- [Disulfide Bond Formation](/xray-mp-wiki/concepts/disulfide-bond-formation/) — DsbB is the central enzyme in the bacterial disulfide bond formation pathway
- [Termini Restraining](/xray-mp-wiki/concepts/termini-restraining/) — High-resolution DsbB structure (6WVF) was determined using termini-restraining approach with split sfGFP
- [DHPC](/xray-mp-wiki/reagents/detergents/dhpc/) — Detergent used in cryoprotection during crystallization
- [Sitting Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion-sitting-drop/) — Crystallization method used for DsbB-Fab complex
- [Ubiquinone](/xray-mp-wiki/reagents/cofactors/ubiquinone/) — Referenced in context related to Ubiquinone
- [Mops](/xray-mp-wiki/reagents/buffers/mops/) — Referenced in context related to Mops
