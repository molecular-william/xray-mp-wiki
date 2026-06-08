---
title: Human 5-HT2A Receptor
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2016.12.033]
verified: false
---

# Human 5-HT2A Receptor

## Overview

The human serotonin 2A (5-HT2A) receptor is a class A GPCR and the primary molecular target for the hallucinogenic effects of LSD and related compounds. While no crystal structure exists, a homology model was built based on the 5-HT2B-R/LSD crystal structure (PDB: 5TVN). The model recapitulates the LSD binding mode and was validated through ligand enrichment docking studies. Functional assays at 5-HT2A reveal extremely slow LSD dissociation kinetics (residence time 221 min), which are selectively disrupted by EL2 mutations.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2016.12.033 | none (homology model) | N/A | N/A | Homology model of human 5-HT2A receptor built using MODELER-9v15 based on 5-HT2B-R/LSD crystal structure (PDB: 5TVN) as template. LSD retained in modeling process to ensure ligand-competent orthosteric site. | LSD (docked pose) |

## Expression and Purification

- **Expression system**: HEK293T cells (Flp-In T-Rex system)
- **Construct**: Human 5-HT2A receptor with L229A^EL2 mutant. Stable cell lines generated using Flp-In 293 T-Rex tetracycline inducible system (Invitrogen). Tetracycline-induced expression.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and functional assays | Tetracycline-inducible HEK293T expression | -- | DMEM with 1% dialyzed FBS + -- | Stable cell lines for 5-HT2A-R used for calcium flux assays, BRET arrestin recruitment assays, and ligand binding assays |


## Crystallization

No crystallization described.

## Biological / Functional Insights

### LSD binding mode in 5-HT2A homology model

Homology modeling of 5-HT2A based on 5-HT2B-R/LSD crystal structure shows that LSD binding mode is recapitulated in the 5-HT2A receptor. Key interactions include a salt bridge between the basic amine and D138^3.32, and a hydrogen bond between the indole nitrogen and S242^5.42 (versus G221^5.42 in 5-HT2B). Docking of LSD and its derivatives (SSAz, RRAz, LSA) into the 5-HT2A model confirms that the crystallographic 5-HT2B binding mode is conserved. The rigidified substituent of SSAz adopts an almost identical orientation to LSD in receptor-bound form, while RRAz and LSA show different orientations with reduced receptor engagement.

### Extremely slow LSD dissociation kinetics at 5-HT2A

LSD dissociates exceptionally slowly from 5-HT2A receptors with a residence time of approximately 221 minutes at 37 degrees C. The EL2 lid residue L229 at position EL2 (equivalent to L209^EL2 in 5-HT2B) forms a structural latch. Mutation of L229A^EL2 decreases LSD residence time to 50 minutes, a 4.4-fold acceleration. This accelerated kinetics selectively disrupts beta-arrestin2 recruitment while leaving Gq function intact, mirroring the phenotype observed at 5-HT2B receptors.

### Time-dependent augmentation of signaling

At wild-type 5-HT2A receptors, LSD potency and efficacy for beta-arrestin2 recruitment increase with longer compound stimulation, exhibiting time-dependent augmentation. This is abrogated by the L229A^EL2 mutation, which results in weak LSD potency and efficacy that does not change over time. Gq-mediated IP accumulation shows time-dependent augmentation at wild-type but is not substantially affected by the EL2 mutation. This indicates that EL2-mediated residence time selectively controls the time-dependency of beta-arrestin2 translocation.


## Cross-References

- [Human 5-HT2B Receptor](/xray-mp-wiki/proteins/5ht2b-receptor/) — Template for homology model; co-crystallized structure PDB 5TVN
- [LSD (Lysergic Acid Diethylamide)](/xray-mp-wiki/reagents/ligands/lsd/) — Primary ligand studied; extremely slow off-rate at 5-HT2A
- [Ergotamine](/xray-mp-wiki/reagents/ligands/ergotamine/) — Related ergoline ligand compared in functional assays
- [(S,S)-Azetidide (SSAz)](/xray-mp-wiki/reagents/ligands/ssaaz/) — LSD analog tested at 5-HT2A for stereoselectivity
- [Lysergamide (LSA)](/xray-mp-wiki/reagents/ligands/lysergamide/) — LSD parent compound tested at 5-HT2A
