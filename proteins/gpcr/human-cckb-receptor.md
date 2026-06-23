---
title: Human Cholecystokinin B Receptor (CCKᴅR)
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein]
sources: [doi/10.1038##s41589-021-00866-8]
verified: false
---

# Human Cholecystokinin B Receptor (CCKᴅR)

## Overview

The human cholecystokinin B receptor (CCKᴅR) is a class A G-protein-coupled receptor (GPCR) that recognizes both sulfated cholecystokinin (CCK) and gastrin peptides with similar affinities. CCKᴅR is involved in satiety regulation, anxiety, memory, and drug addiction, and can activate both Gᵢ and G₉ signaling pathways. Cryo-electron microscopy structures of human CCKᴅR in complex with the endogenous peptide gastrin-17 and two different G proteins — Gᵢ₂ (3.1 Å resolution) and G₉ (3.3 Å resolution) — revealed the fully active receptor conformation and provided insights into G protein coupling selectivity.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41589-021-00866-8 | 7F8X | 3.10 |  | Human CCKᴅR with N-terminal HA signal and Flag tag, C-terminal PreScission-Strep tag, C-terminal truncation (419-447) | Gastrin-17 (endogenous peptide agonist) |
| doi/10.1038##s41589-021-00866-8 | 7F8Y | 3.30 |  | Human CCKᴅR with N-terminal HA signal and Flag tag, C-terminal PreScission-Strep tag, C-terminal truncation (419-447) | Gastrin-17 (endogenous peptide agonist) |

## Expression and Purification

- **Expression system**: High Five insect cells (Bac-to-Bac baculovirus expression system)
- **Construct**: Human CCKᴅR with N-terminal HA signal sequence and Flag tag, C-terminal PreScission protease site followed by 2× Strep-tag; C-terminal truncation of residues 419-447

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1. Membrane preparation and solubilization | Detergent extraction | — | 20 mM HEPES pH 7.5, 200 mM NaCl, 5 mM CaCl₂, 10 µM gastrin-17, 1% LMNG, 0.1% CHS | Co-expression with G proteins; solubilization for 2 h at 4°C |
| 2. G protein complex assembly | Nanobody 35 (Nb35) addition | — | 20 mM HEPES pH 7.5, 200 mM NaCl, 5 mM CaCl₂, 10 µM gastrin-17, 0.01% LMNG, 0.001% CHS | Nb35 added to stabilize G protein-receptor complex |
| 3. M1 anti-Flag affinity chromatography | Flag affinity purification | — | 20 mM HEPES pH 7.5, 200 mM NaCl, 5 mM CaCl₂, 10 µM gastrin-17, 0.01% LMNG, 0.001% CHS | Elution with Flag peptide |
| 4. Size-exclusion chromatography | Superose 6 10/300 GL | — | 20 mM HEPES pH 7.5, 200 mM NaCl, 5 mM CaCl₂, 10 µM gastrin-17, 0.00075% LMNG, 0.00025% CHS, 0.00025% GDN | Peak fractions collected for cryo-EM grid preparation |


## Crystallization

### doi/10.1038##s41589-021-00866-8

| Parameter | Value |
|---|---|
| Method | Cryo-electron microscopy (single particle) |
| Protein sample | CCKᴅR-gastrin-17-G protein-Nb35 complex |
| Notes | Data collected on Titan Krios with K3 detector. Processing in RELION3.1. Resolution: 3.1 Å (Gᵢ₂ complex) and 3.3 Å (G₉ complex). Local resolution estimation by ResMap. |


## Biological / Functional Insights

### G protein coupling promiscuity

CCKᴅR can activate both Gᵢ and G₉ signaling pathways. The cryo-EM structures with Gᵢ₂ and G₉ showed that both G proteins insert into the same binding pocket formed by helices II, III, VI, VII and the intracellular loops, but with an approximately 8° rotation of the G protein heterotrimer between the two complexes. Differences in ICL2 interactions with the G protein αN helix were observed: residues R163 and V164 in CCKᴅR form hydrophobic interactions with G₉ αN, while only V164 interacts with Gᵢ₂.

### ECL2 dynamics in peptide discrimination

Unlike CCKₐR (which has R197 in ECL2 forming a salt bridge with sulfated tyrosine), CCKᴅR has a valine at the equivalent position, removing the spatial hindrance that prevents gastrin binding to CCKₐR. Instead, W209 in CCKᴅR ECL2 pushes H207 toward gastrin for a hydrogen bond with the peptide backbone, enabling gastrin recognition.

### Active state conformation

The active CCKᴅR structures show an approximately 6 Å outward movement of helix VI, smaller than typical class A GPCR-G protein complexes (∼8-14 Å). An approximately 8° rotation between Gᵢ₂ and G₉ heterotrimers was observed, reflecting different binding modes of the two G proteins.


## Cross-References

- [Human Cholecystokinin A Receptor (CCKₐR)](/xray-mp-wiki/proteins/gpcr/human-ccka-receptor/) — Sister receptor with distinct peptide selectivity; structures from same study showing antagonist and agonist-bound states
- [Peptide Selectivity in Cholecystokinin Receptors](/xray-mp-wiki/concepts/cck-receptor-peptide-selectivity/) — Structural comparison reveals basis for differential peptide recognition between CCKₐR and CCKᴅR
- [Stepwise Activation of Cholecystokinin Receptors](/xray-mp-wiki/concepts/cck-receptor-stepwise-activation/) — Active CCKᴅR-G protein structures represent the fully active state in the stepwise activation model
