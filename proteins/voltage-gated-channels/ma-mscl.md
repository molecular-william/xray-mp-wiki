---
title: "MaMscL (Methanosarcina acetivorans Mechanosensitive Channel of Large Conductance)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1503202112]
verified: false
---

# MaMscL (Methanosarcina acetivorans Mechanosensitive Channel of Large Conductance)

## Overview

[MSCL](/xray-mp-wiki/proteins/other-ion-channels/mscl/) (mechanosensitive channel of large conductance) from Methanosarcina acetivorans (MaMscL) is a prokaryotic pressure-relief valve that protects cells from lysis during acute osmotic downshock. MaMscL forms a homo-pentameric channel that responds to membrane tension by opening a non-selective pore of ~30 Å width with a unitary conductance of ~3 nS. Structures of MaMscL were solved in closed and expanded intermediate states using a fusion protein strategy with [Riboflavin (Vitamin B2)](/xray-mp-wiki/reagents/cofactors/riboflavin/) synthase (MjRS) from Methanocaldococcus jannaschii to enhance crystallizability.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1503202112 | 4Y7K |  |  | MaMscL-MjRS fusion (full-length MaMscL with C-terminal MjRS fusion) |  |
| doi/10.1073##pnas.1503202112 | 4Y7K |  |  | MaMscL-MjRS fusion (full-length MaMscL with C-terminal MjRS fusion) |  |

## Expression and Purification

- **Expression system**: E. coli BL21(DE3)
- **Construct**: MaMscL-MjRS fusion (C-terminal fusion with Methanocaldococcus jannaschii [Riboflavin (Vitamin B2)](/xray-mp-wiki/reagents/cofactors/riboflavin/) synthase)
- **Notes**: Fusion protein enhances crystallizability by providing a large hydrophilic scaffold

### Purification Workflow

- **Expression system**: E. coli
- **Expression construct**: MaMscL-MjRS fusion

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Fermentation |  |  |  |
| Purification | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) |  |  | Purified in two different detergent types for distinct crystal forms |


## Crystallization

### doi/10.1073##pnas.1503202112

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | MaMscL-MjRS fusion in detergent type 1 |
| Notes | Form 1 crystals - closed state, different space group |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | MaMscL-MjRS fusion in detergent type 2 |
| Notes | Form 2 crystals - expanded intermediate state, different space group |


## Biological / Functional Insights

### Helix-Pivoting Gating Mechanism

During the transition from closed to expanded state, TM1 and TM2 helices undergo large tilting movements (TM1: 37°→58°, TM2: 24°→42°), consistent with the helix-pivoting model. The transmembrane domain thins from 44Å to 30Å as the periplasmic surface expands from 50Å to 66Å width (ΔA ~1,457 Å²).

### N-Helix as Membrane-Anchored Stopper

The N-terminal helix undergoes significant rotation and horizontal sliding coupled to TM1/TM2 tilting. The N-helix serves as a membrane-anchored stopper that limits TM1/TM2 tilt during gating. The relationship follows: r(cosη₁ - cosη₂) = Δh = n(cosψ₁ - cosψ₂), where η and ψ are TM1 and N-helix tilt angles.

### Periplasmic Loop Reorganization

The periplasmic loop transforms from a folded structure containing an ω-shaped loop (residues Pro50-Ala57, motif PGGGWETA) and a short β-hairpin to an extended and partly disordered conformation. The ω-loop motif is involved in regulating the mechanosensitivity of [MSCL](/xray-mp-wiki/proteins/other-ion-channels/mscl/), with deletion of Gly51-Thr56 abolishing channel function.

### Mechanical Coupling of Channel Domains

The intersubunit coupling between the N-helix and TM1-TM2 pairs drives coordinated movement during channel expansion. The TM2 behaves like an umbrella stretcher and the N-helix like a rib that is pushed open. This provides a mechanism for force transmission across the pentameric channel.


## Cross-References

- [Mechanosensitive Channel of Large Conductance MscL (Mycobacterium tuberculosis)](/xray-mp-wiki/proteins/other-ion-channels/mscl/) — MaMscL structure compared with closed-state MtMscL
- [Staphylococcus aureus MscL](/xray-mp-wiki/proteins/voltage-gated-channels/sa-mscl/) — MaMscL expanded state compared with SaMscL-CΔ26 expanded intermediate
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Riboflavin (Vitamin B2)](/xray-mp-wiki/reagents/cofactors/riboflavin/) — Related ligand or cofactor
