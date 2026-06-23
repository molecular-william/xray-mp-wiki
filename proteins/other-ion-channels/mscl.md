---
title: Mechanosensitive Channel of Large Conductance MscL (Mycobacterium tuberculosis)
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature13419]
verified: false
---

# Mechanosensitive Channel of Large Conductance MscL (Mycobacterium tuberculosis)

## Overview

MscL (mechanosensitive channel of large conductance) from Mycobacterium tuberculosis is a pentameric mechanosensitive ion channel with two transmembrane helices per subunit. MscL was found to bind lipids non-selectively, with all tested phospholipids imparting comparable stabilization. However, [[Phosphatidylinositol](/xray-mp-wiki/reagents/lipids/phosphatidylinositol) (PI)(/xray-mp-wiki/reagents/lipids/phosphatidylinositol/)] bound with higher avidity, conferring a large linear increase in stability. This is consistent with PI's proposed functional role in MscL mechanosensitivity. MscL demonstrates a broad lipid binding profile without regard to particular headgroup or chain length.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature13419 | not solved in this paper (PDB 2OAR referenced from Chang et al. 1998) | not solved in this paper | not solved in this paper | MscL-GFP fusion | Various phospholipids studied by IM-MS |

## Expression and Purification

- **Expression system**: E. coli BL21(DE3) Delta mscL::KanR (homologous recombination disrupted endogenous mscL)
- **Construct**: MscL-GFP fusion

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Microfluidizer cell lysis | -- | 300 mM [[Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride)], 20 mM [[TRIS](/xray-mp-wiki/reagents/buffers/tris)] (pH 7.4), protease inhibitor, 5 mM [[2-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol)] + -- | Cells lysed at 19,000 psi; membranes pelleted at 100,000g for 2 h; [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) omitted for MscL |
| Solubilization | Membrane solubilization | -- | 100 mM [[Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride)], 5 mM [[2-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol)], 20 mM [[TRIS](/xray-mp-wiki/reagents/buffers/tris)] (pH 7.4) + 1% [n-nonyl-beta-D-glucopyranoside (NGNG)] | Extracted overnight at 4 C |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta) [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | 5 mL HisTrap-HP column | 200 mM [[Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride)], 10% [[Glycerol](/xray-mp-wiki/reagents/additives/glycerol)], 20 mM [[Imidazole](/xray-mp-wiki/reagents/additives/imidazole)], 0.025% [[DDM](/xray-mp-wiki/reagents/detergents/ddm)], 50 mM [[TRIS](/xray-mp-wiki/reagents/buffers/tris)] (pH 7.4) + 0.025% [[DDM](/xray-mp-wiki/reagents/detergents/ddm)] | Washed with 1% [n-nonyl-beta-D-glucopyranoside (NGNG)]; eluted with 500 mM [[Imidazole](/xray-mp-wiki/reagents/additives/imidazole)] |


## Crystallization

No crystallization described.

## Biological / Functional Insights

### Non-selective lipid binding with PI as the most stabilizing lipid

IM-MS analysis revealed that MscL binds lipids non-selectively; all seven tested phospholipids and synthetic PCs with chain lengths C14-C22 imparted comparable stabilization. MscL avidly bound [Phosphatidylinositol](/xray-mp-wiki/reagents/lipids/phosphatidylinositol) (PI), greater than all other lipids, conferring a large linear increase in stability upon binding multiple PI molecules. This is consistent with PI's proposed functional role in Mycobacterium mechanosensitivity. MscL responds promiscuously to lipid composition.

### Gas-phase unfolding reveals cumulative lipid stabilization

Collision-induced unfolding experiments showed that apo MscL and lipid-bound forms (1-5 lipids) maintain pentameric state throughout unfolding. All lipid-bound states showed less unfolding as a function of lipid binding. Cumulative stabilization was observed for 1-2 bound lipid molecules. The equilibrium unfolding model identified four distinct intermediate states in the unfolding trajectories.


## Cross-References

- [Mechanosensitive Gating in Ion Channels](/xray-mp-wiki/concepts/mechanosensitive-gating/) — MscL is a mechanosensitive ion channel; lipid binding modulates its mechanosensitivity
- [Force-from-Lipid Principle in Mechanosensation](/xray-mp-wiki/concepts/force-from-lipid-principle/) — PI proposed as functional lipid in MscL mechanosensitivity via force-from-lipid mechanism
- [Phosphatidylinositol (PI)](/xray-mp-wiki/reagents/lipids/phosphatidylinositol/) — PI is the most stabilizing lipid for MscL; confers large linear increase in stability
- [Phosphatidylcholine (PC)](/xray-mp-wiki/reagents/lipids/phosphatidylcholine/) — Various PC species (DNPC, DEPC, DIPC, DOPC, DPPC, DMPC) tested with MscL
- [Octyltetraoxyethylene (C8E4)](/xray-mp-wiki/reagents/detergents/c8e4/) — Optimal detergent for maintaining intact MscL complexes in native MS
- [n-Nonyl-beta-D-Glucopyranoside (NGNG)](/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/) — Detergent used for MscL solubilization (1%)
- [Tris Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Buffer used in purification (20-50 mM, pH 7.4)
- [E. coli MscS (Mechanosensitive Channel of Small Conductance)](/xray-mp-wiki/proteins/voltage-gated-channels/mscs/) — Related mechanosensitive channel; different lipid selectivity profile
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) — Entity mentioned in text
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) — Entity mentioned in text
