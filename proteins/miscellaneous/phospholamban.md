---
title: "Phospholamban (PLB)"
created: 2026-06-08
updated: 2026-06-21
type: protein
category: proteins
layout: default
tags: [membrane-protein, xray-crystallography, pump]
sources: [doi/10.1038##nature11900, doi/10.1074##jbc.M113.501585, doi/10.1126##science.aav7541, doi/10.1038##nature11899]
verified: false
---

# Phospholamban (PLB)

## Overview

Phospholamban (PLB, also known as PLN) is a small (~52 amino acid) membrane protein that regulates the sarcoplasmic reticulum Ca2+-ATPase (SERCA) by binding to it and lowering its apparent Ca2+ affinity. PLB is primarily expressed in heart muscle in humans, whereas [SLN](/xray-mp-wiki/proteins/pumps-atpases/sarcolipin/) ([SLN](/xray-mp-wiki/proteins/pumps-atpases/sarcolipin/)) predominates in skeletal muscle. PLB and [SLN](/xray-mp-wiki/proteins/pumps-atpases/sarcolipin/) are homologous regulators that bind SERCA in a similar fashion. Phosphorylation of PLB by protein kinase A or CaMKII relieves its inhibitory effect on SERCA, providing a key mechanism for beta-adrenergic regulation of cardiac contractility.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1074##jbc.M113.501585 | 4KYT | 2.83 | P2_1_2_1_2_1 | PLB4 (superinhibitory mutant N27A, L37A, I40A, L51A) bound to [SERCA1a (Sarcoplasmic Reticulum Ca2+-ATPase)](/xray-mp-wiki/proteins/pumps-atpases/serca1a/); E2-PLB state | None (Ca2+-free) |
| doi/10.1074##jbc.M113.501585 | 4Y3U | 3.51 | P2_1_2_1_2_1 | Wild-type PLB bound to [SERCA1a (Sarcoplasmic Reticulum Ca2+-ATPase)](/xray-mp-wiki/proteins/pumps-atpases/serca1a/) | None (Ca2+-free) |
| doi/10.1038##nature11900 | 4H1W | Low resolution (~20 A) | Not determined | PLB-SERCA complex observed by electron microscopy | Not determined |

## Expression and Purification

- **Expression system**: Mammalian heart muscle, native expression
- **Construct**: Native PLB from cardiac sarcoplasmic reticulum; no heterologous expression

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| PLB expression and purification | Anti-PLB monoclonal antibody (2D12) [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Anti-PLB 2D12 antibody affinity column | 20 mM MOPS (pH 7.2), 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 0.1% decyl maltoside or 0.01% dodecyl maltoside | WT-PLB and PLB4 expressed in Sf21 insect cells. Eluted PLB concentrated 100-fold with Amicon concentrator, then dialyzed against buffer with detergent. |


## Crystallization

### doi/10.1074##jbc.M113.501585

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (hanging drop) via co-crystallization |
| Protein sample | SERCA solubilized in 2% nonyl maltoside with 0.14 mg PLB4/mg SERCA; final buffer: 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 100 mM MOPS pH 7.0, 80 mM KCl, 3 mM MgCl2, 2.8 mM [EGTA](/xray-mp-wiki/reagents/additives/egta/) |
| Reservoir | 100 mM HEPES pH 7.0, 800 mM NaH2PO4/K2HPO4, 0.1% decyl maltoside, 100 mM NaCl, 1 mM [EGTA](/xray-mp-wiki/reagents/additives/egta/), 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |
| Temperature | 4 C |
| Growth time | Several days |
| Cryoprotection | 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |
| Notes | Novel alkyl mannoside detergent system. Crystals in space group P2_1_2_1_2_1. Diffraction data to 2.83 A. |


## Biological / Functional Insights

### Crystal structure of PLB-SERCA complex

The 2.83 A crystal structure of PLB4-SERCA (PDB 4KYT) reveals that PLB binds as a single transmembrane alpha-helix in a groove between M2, M4, M6, M9 of SERCA. The structure stabilizes the E2-PLB conformation with collapsed Ca2+ binding sites, explaining how dephosphorylated PLB decreases Ca2+ affinity.

### Asn34 is the key inhibitory residue

Asn34 of PLB forms hydrogen bonds with Gly801 (main chain carbonyl) and Thr805 (side chain) of SERCA M6. Mutation N34A completely disables PLB inhibition. Asn34 is positioned in a particularly hydrophobic context, enhancing its functional impact.

### PLB pentamer-monomer equilibrium

The crystal structure confirms that PLB monomer binds SERCA, while pentamer is the storage form. The PLB4 mutant (N27A, L37A, I40A, L51A) shows increased monomer population leading to superinhibition. The Leu/Ile zipper has dual faces: one for pentamerization and one for SERCA inhibition.

### PLB and SLN regulate SERCA by different mechanisms

Unlike [SLN](/xray-mp-wiki/proteins/pumps-atpases/sarcolipin/), PLB decreases Ca2+ affinity without uncoupling ATP hydrolysis from Ca2+ transport. PLB dissociates from SERCA in the presence of Ca2+, whereas [SLN](/xray-mp-wiki/proteins/pumps-atpases/sarcolipin/) continues to interact with SERCA even with Ca2+ bound. The unique C-terminal tail of [SLN](/xray-mp-wiki/proteins/pumps-atpases/sarcolipin/) (Arg27, Tyr31) is not present in PLB.

### Phosphorylation relieves PLB inhibition

Phosphorylation of PLB at Ser16 and Thr17 reverses the inhibitory effect by causing PLB to dissociate from SERCA. The E2-PLB structure provides the structural basis for understanding how cAMP-dependent phosphorylation regulates cardiac contractility.

### MD simulations reveal distinct rigid apolar and dynamic polar domains

Atomistic MD simulations of full-length PLN in a [POPC](/xray-mp-wiki/reagents/lipids/popc/) bilayer (starting from NMR model PDB 2KYV) showed that the C-terminal LxxIxxx-domain (residues 33-51) is tightly packed and very rigid (backbone RMSF 0.53 A), while the N-terminal TM sector is more dynamic (1.53 A) and becomes widely splayed, with water rushing into the bundle. This indicates that the apolar C-terminal domain plays the dominant role in pentamer stabilization, while polar N-terminal residues modulate functional dynamics rather than stability.


## Cross-References

- [SERCA1a (Sarcoplasmic Reticulum Ca2+-ATPase 1a)](/xray-mp-wiki/proteins/pumps-atpases/serca1a/) — Primary target of PLB regulation; PLB binds and inhibits SERCA
- [Sarcolipin (SLN)](/xray-mp-wiki/proteins/pumps-atpases/sarcolipin/) — Homologous regulator of SERCA; distinct mechanism from PLB
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — PLB modulates the alternating-access transport cycle of SERCA by stabilizing the E2 state
- [PL5 Designed Pentameric Transmembrane Protein](/xray-mp-wiki/proteins/miscellaneous/pl5-pentamer/) — PL5 is a designed variant derived from PLN's apolar C-terminal domain; revealed the steric packing code underlying PLN assembly
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [EGTA](/xray-mp-wiki/reagents/additives/egta/) — Additive used in purification or crystallization buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [POPC](/xray-mp-wiki/reagents/lipids/popc/) — Additive used in purification or crystallization buffers
