---
title: BbFPN — Putative Bacterial Ferroportin Homologue from Bdellovibrio bacteriovorus
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms9545]
verified: false
---

# BbFPN — Putative Bacterial Ferroportin Homologue from Bdellovibrio bacteriovorus

## Overview

BbFPN is a putative bacterial homologue of ferroportin (FPN/SLC40A1) from Bdellovibrio bacteriovorus (formerly Bd2019). It is a divalent transition-metal cation transporter selective for Fe2+, Co2+, Mn2+, and Ni2+, and functions as a uniporter. Despite undetectable sequence similarity, BbFPN adopts the major facilitator superfamily (MFS) fold with 12 transmembrane helices divided into N-lobe (TM1-TM6) and C-lobe (TM7-TM12). Crystal structures were determined in both outward-facing (2.2 Å) and inward-facing (3.3 Å) conformations, capturing two extreme states of the MFS transport cycle. BbFPN serves as a structural model for understanding ferroportin-mediated [Iron](/xray-mp-wiki/reagents/additives/iron/) export and hepcidin-mediated regulation in humans.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms9545 | 5AYN | 2.2 A | P2,2,2,1 | BbFPNΔC (C-terminal 8 residues deleted), full-length BbFPN residues | K+ (outward-facing state) |
| doi/10.1038##ncomms9545 | 5AYM | 3.0 A | P2,2,2,1 | BbFPNΔC, Fe2+-soaked outward-facing state | Fe2+ (anomalous scattering) |
| doi/10.1038##ncomms9545 | 5AYO | 3.3 A | P2,2,2,1 | BbFPNΔC (C-terminal 8 residues deleted) | none (inward-facing state) |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Full-length BbFPN (Bd2019) and BbFPNΔC (C-terminal 8 residues deleted for crystallization)

### Purification Workflow

- **Expression system**: E. coli
- **Expression construct**: BbFPN with affinity tag (protocol A and protocol B)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Purification | Affinity chromatography (protocol A and protocol B) | — | 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 500 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.004% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) (protocol B final buffer) + 0.004% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) (protocol B) | Two purification protocols used (A and B); protocol A for Hg-derivatized crystals, protocol B for form I and form II crystals |

**Final sample**: 2.5-2.9 mg/ml in 20 mM Tris pH 8.0, 500 mM NaCl, 10% glycerol, 0.004% LMNG


## Crystallization

### doi/10.1038##ncomms9545

| Parameter | Value |
|---|---|
| Method | Lipidic Cubic Phase (LCP) |
| Protein sample | Purified BbFPNΔC in 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 500 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.004% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) |
| Lipid | monoolein |
| Protein-to-lipid ratio | 2:3 (wt/wt) |
| Temperature | 20 C |
| Notes | Three crystal forms obtained. Hg-derivative/Fe2+-soaked crystals (Form I-like): 100 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 50-200 mM K-formate, 50-100 mM (NH4)2HPO4, 26-32% PEG550MME. Hg-derivative: 1 mM CH3HgCl, 2.5 h soak. Fe2+-soaked: 5 mM FeSO4, 12 h soak. Form I: 100 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 8.5, 100 mM NaK-tartrate, 100 mM KNO3, 30% PEG550MME. Form II: 100 mM Na-acetate pH 4.0, 200-300 mM K-formate, 10 mM ZnSO4, 10-20 mM ZnCl2, 27-30% PEG550MME. |


## Biological / Functional Insights

### MFS fold of a transition-metal transporter

BbFPN adopts the canonical MFS fold with 12 TM helices organized into N-lobe (TM1-TM6) and C-lobe (TM7-TM12) connected by a long cytoplasmic loop. This is the first MFS transporter shown to mediate cation transport. Despite low sequence homology, the structural fold is conserved, demonstrating that the FPN family shares common topology with MFS transporters.

### Outward- and inward-facing conformational states

Comparison of the outward-facing (2.2 Å) and inward-facing (3.3 Å) structures reveals intra-domain conformational rearrangements during the transport cycle. The intracellular side of the N-lobe is flexible while the C-lobe is rigid; induced fit of the flexible N-lobe to the rigid C-lobe facilitates intracellular gate formation during the outward-to-inward transition. On the extracellular side, the C-lobe is flexible while the N-lobe is rigid.

### Metal-binding site

A substrate metal-binding site was identified based on structural and mutational analyses. Fe2+ coordination involves residues including Asp24, Asn196, and likely utilizes cation-π interactions with Phe200. The binding site is located in the central cavity between the N- and C-lobes. Isothermal titration calorimetry confirmed Co2+ binding affinity.

### Structural model for hepcidin-ferroportin interaction

A homology model of human ferroportin (hFPN) was constructed based on the BbFPN outward-facing structure. The model suggests that hepcidin-binding residues (Phe324, Cys326, Tyr333, Asp504, His507) cluster inside the central cavity, not on the extracellular loop as previously thought. This suggests hepcidin enters the central cavity between N and C lobes to interact with hFPN, providing new insights into hepcidin-mediated downregulation.


## Cross-References

- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) — BbFPN adopts the MFS fold despite undetectable sequence similarity
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — BbFPN structures capture outward- and inward-facing states of the transport cycle
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid used for LCP crystallization of BbFPN
- [Lipidic Cubic Phase (LCP) Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Method used for all BbFPN crystal forms
- [PEG550MME](/xray-mp-wiki/reagents/additives/peg550mme/) — Precipitant in all BbFPN crystallization conditions
- [Tris Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Buffer used in purification and crystallization of BbFPN
- [LMNG (Lauryldimaltoside Neopentyl Glycol)](/xray-mp-wiki/reagents/detergents/lmng/) — Detergent used in final purification buffer for BbFPN
- [Acetate Buffer](/xray-mp-wiki/reagents/buffers/acetate/) — Buffer component in Form II crystallization condition (Na-acetate pH 4.0)
- [Iron](/xray-mp-wiki/reagents/additives/iron/) — Referenced in the context of Iron
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Referenced in the context of Glycerol
