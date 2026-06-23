---
title: "C. elegans P-glycoprotein (P-gp)"
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature11448]
verified: false
---

# C. elegans P-glycoprotein (P-gp)

## Overview

P-glycoprotein (P-gp) from Caenorhabditis elegans is an [ATP](/xray-mp-wiki/reagents/ligands/atp/)-binding cassette (ABC) transporter that functions as a multidrug efflux pump. It belongs to the P-gp/MDR subfamily of ABC transporters and confers cellular resistance to a wide range of cytotoxic drugs including actinomycin D, [Paclitaxel](/xray-mp-wiki/reagents/ligands/paclitaxel/), and [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil/). P-gp is a primary active transporter that uses [ATP](/xray-mp-wiki/reagents/ligands/atp/) hydrolysis to extrude hydrophobic compounds from cells, playing a critical role in multidrug resistance. The C. elegans P-gp structure was solved by X-ray crystallography at 3.4 A resolution, providing the first high-resolution view of an ABC transporter in a nucleotide-free conformation. The protein is N-glycosylated at residue N125 and expresses as a functional full-length protein when produced in Sf9 insect cells.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature11448 | 4MQ1 | 3.4 | P212121 | C. elegans P-glycoprotein, full-length, N125 glycosylated | None (nucleotide-free) |

## Expression and Purification

- **Expression system**: Baculovirus expression in Sf9 insect cells
- **Construct**: Full-length C. elegans P-glycoprotein with GFP tag on C-terminus for expression monitoring

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Baculovirus expression in Sf9 cells | -- | Not specified + Not specified | P-gp expression monitored by GFP fluorescence fused to C-terminus |
| Solubilization | Detergent solubilization | -- | Not specified + Not specified | Not specified in supplementary information |
| Purification | GFP affinity chromatography | GFP-Trap | Not specified + Not specified | GFP-tagged P-gp purified using GFP-Trap beads |
| Size-exclusion chromatography | Size-exclusion chromatography (SEC) | -- | Not specified + Not specified | Final polishing step; SEC used for sample homogeneity assessment |


## Crystallization

### doi/10.1038##nature11448

| Parameter | Value |
|---|---|
| Method | Not specified |
| Protein sample | C. elegans P-glycoprotein, nucleotide-free |
| Reservoir | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Notes | Space group P212121, unit cell a=96.8, b=155.3, c=162.4 Angstroms. Structure determined by SeMet SAD and Hg anomalous diffraction. Resolution 3.4 A, Rwork/Rfree 24.9/28.2. |


## Biological / Functional Insights

### Drug resistance function

C. elegans P-gp confers cellular resistance to cytotoxic drugs. Sf9 cells expressing P-gp show protection from drug-induced cytotoxicity by actinomycin D (12 hours exposure) and [Paclitaxel](/xray-mp-wiki/reagents/ligands/paclitaxel/) (48 hours exposure), correlated with P-gp membrane expression monitored by GFP fluorescence. The protein functions as a broad-spectrum multidrug efflux pump.

### ATPase activity and drug stimulation

P-gp exhibits basal ATPase activity that is stimulated by drug substrates. Multiple compounds including [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil/), [Valinomycin](/xray-mp-wiki/reagents/ligands/valinomycin/), and trifluoperazine stimulate ATPase activity in detergent-solubilized P-gp, confirming their role as P-gp substrates. The drug concentration dependence of ATPase stimulation provides functional evidence for drug transport activity.

### N-glycosylation site resolved by anomalous diffraction

The N-glycosylation site at residue N125 was resolved using anomalous difference Fourier maps. [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) and [Mercury (HgCl2) - Aquaporin Inhibitor](/xray-mp-wiki/reagents/additives/mercury/) anomalous diffraction data (contoured at 4 sigma) enabled direct visualization of the attached oligosaccharide, confirming the glycosylation state of the crystallized protein.

### Transmembrane register shifts vs. mouse P-gp

Comparison with mouse P-gp (PDB 3G5U) reveals register shifts in transmembrane helices TM3, TM4, and TM5. Region of TM3 (residues 184-200) shifted by one amino acid, entire TM4 helix (residues 217-251) shifted by four amino acids, and TM5 shifted by three amino acids. These shifts highlight sequence divergence between C. elegans and mouse P-gp despite structural conservation.

### N-terminal truncation mutant

A [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) mutant lacking the N-terminal 56 residues (Delta56) confers cellular resistance to actinomycin D and [Paclitaxel](/xray-mp-wiki/reagents/ligands/paclitaxel/) similarly to full-length P-gp, indicating the N-terminus is not essential for drug transport function. However, the [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) mutant shows reduced maximum drug-stimulated ATPase activity in detergent, suggesting the N-terminus modulates the enzymatic activity of the transporter.


## Cross-References

- [ABCG2](/xray-mp-wiki/proteins/abc-transporters/abcg2/) — ABC transporter G subfamily; multidrug efflux pump with similar drug resistance function
- [ABCG1](/xray-mp-wiki/proteins/abc-transporters/abcg1/) — ABC transporter G subfamily member; lipid transporter with structural similarities
- [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/abc-transporters/acrb/) — Multidrug efflux pump from E. coli; functional comparison with P-gp
- [ABC Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/) — P-gp is a member of the ABC (ATP-binding cassette) superfamily of transporters
- [Actinomycin D](/xray-mp-wiki/reagents/antibiotics/actinomycin-d/) — P-gp substrate; tested for cellular resistance in P-gp-expressing cells
- [Paclitaxel](/xray-mp-wiki/reagents/ligands/paclitaxel/) — P-gp substrate; antimitotic drug whose cellular toxicity is reversed by P-gp
- [GR (Halobacterium sp. GR Bacteriorhodopsin)](/xray-mp-wiki/proteins/rhodopsins/gr/) — Related protein structure
- [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/abc-transporters/acrb/) — Related protein structure
- [ABCG2](/xray-mp-wiki/proteins/abc-transporters/abcg2/) — Related protein structure
- [ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel)](/xray-mp-wiki/proteins/cys-loop-receptors/elic/) — Related protein structure
