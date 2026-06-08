---
title: Human Histamine H3 Receptor (H3R)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-022-33880-y]
verified: false
---

# Human Histamine H3 Receptor (H3R)

## Overview

The human histamine H3 receptor (H3R) is a G protein-coupled receptor (GPCR) belonging to the aminergic GPCR subfamily. It is expressed mainly in the central nervous system, where it acts as an auto- or hetero-receptor to regulate histamine release and modulate the release of various neurotransmitters including dopamine, GABA, and acetylcholine. H3R is associated with physiological processes such as sleep-wake cycles, learning, memory, feeding, and cerebral ischemia, making it a potential drug target for neurological and psychiatric disorders including sleep disorders, Parkinson's disease, schizophrenia, and Alzheimer's disease. The crystal structure of H3R in complex with the non-imidazole antagonist PF-03654746 reveals the molecular basis for ligand recognition and allosteric cholesterol binding.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-022-33880-y | not specified | 2.6 | not specified | Human H3R (residues 27-432), with N-terminal truncation (1-26), ICL3 truncation (242-346), C-terminal truncation (433-445), S121K mutation, and N-terminal BRIL fusion (M7W, H102I, R106L) | PF-03654746 |

## Expression and Purification

- **Expression system**: Spodoptera frugiperda (Sf9) insect cells
- **Construct**: Codon-optimized human H3R gene cloned into modified pFastBacI vector with N-terminal HA signal sequence, FLAG tag, 10x His tag, and TEV protease cleavage site
- **Notes**: Bac-to-Bac Baculovirus Expression System; infected at 2-3 x 10^6 cells/ml, harvested 48h post-infection

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Cell lysis and membrane fractionation | not specified | 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl (hypotonic); 10 mM HEPES pH 7.5, 1.0 M NaCl, 10 mM MgCl2, 20 mM KCl (high-osmotic) + not specified | Cells washed with hypotonic buffer then high-osmotic buffer; purified membranes resuspended with 2 mg/mL iodoacetamide |
| Solubilization | Detergent solubilization | not specified | 50 mM HEPES pH 7.5, 800 mM NaCl, 10% glycerol + 0.5% DDM, 0.1% CHS | Solubilized for 3h at 4 C; centrifuged at 58,000xg for 1h |
| IMAC purification | Immobilized metal affinity chromatography | TALON IMAC resin (TaKaRa) | 50 mM HEPES pH 7.5, 800 mM NaCl, 10% glycerol, 0.1% LMNG, 0.01% CHS, 20 mM imidazole (wash I); 20 mM HEPES pH 7.5, 500 mM NaCl, 5% glycerol, 0.05% LMNG, 0.005% CHS, 40 mM imidazole (wash II); 10 mM HEPES pH 7.5, 500 mM NaCl, 5% glycerol, 0.05% LMNG, 0.005% CHS, 250 mM imidazole (elution) + LMNG, CHS | Incubated overnight at 4 C; eluted in 3 column volumes |


## Crystallization

### doi/10.1038##s41467-022-33880-y

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | H3R-PF-03654746 complex in 0.05% LMNG, 0.005% CHS |
| Temperature | not specified |
| Notes | Crystals formed within 1 week; collected with 50 um micro-loops and flash-frozen in liquid nitrogen |


## Biological / Functional Insights

### Extended binding pocket (EBP) in H3R

The H3R structure reveals an extended binding pocket (EBP) around TMs2/7 and ECL2 compared to other aminergic receptors. This EBP accommodates the aromatic moieties of H3R antagonists through pi-pi stacking and OH/pi hydrogen bonds with aromatic residues including Y91 and Y189. Functional assays showed Y91A and Y189A mutations significantly decreased inhibition of several antagonists, confirming the EBP's importance for ligand binding and efficacy.

### Allosteric cholesterol binding

A cholesterol molecule was observed binding at the extrahelical pocket between TM1 and TM7 of H3R, forming extensive hydrophobic interactions with F29, L37, M41, L40, L44, T396, Y393, and W399. The beta-3-hydroxy head group of cholesterol forms a hydrogen bond with E395, which also participates in polar interactions with PF-03654746. Molecular dynamics simulations showed cholesterol stabilizes the TM1-TM7-N-term contacts, potentially affecting antagonist binding through an allosteric mechanism.

### Inactive state conformation

Compared to inactive H1R, H3R shows inward movement of TM6 and TM7 extracellular tips by 2.3 and 3.5 A, respectively, and an outward movement of TM6 by 2.8 A at the intracellular side (vs 12 A in active H1R). The D131-R132 salt bridge (instead of D-R-Y motif) is a key feature of the inactive state. ECL2 shifts 11 A toward TM3, creating space for the antagonist.


## Cross-References
