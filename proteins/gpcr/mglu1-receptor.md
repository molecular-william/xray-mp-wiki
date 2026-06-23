---
title: "Human mGlu1 Receptor 7TM Domain (Metabotropic Glutamate Receptor 1)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1249489]
verified: false
---

# Human mGlu1 Receptor 7TM Domain (Metabotropic Glutamate Receptor 1)

## Overview

The human mGlu1 (metabotropic glutamate receptor 1) is a class C G protein-coupled receptor that mediates the actions of glutamate, the major excitatory neurotransmitter in the central nervous system. Group I mGlu receptors (mGlu1 and mGlu5) are coupled to Gq/11 and activate phospholipase Cβ, inducing intracellular calcium mobilization and activating protein kinase C. The crystal structure of the mGlu1 7TM domain bound to the negative allosteric modulator (NAM) FITM at 2.8 Å resolution provides a three-dimensional framework for understanding molecular recognition by class C GPCRs. The mGlu1 7TM domain crystallized as a parallel dimer mediated by helix I and [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) molecules, with a restricted NAM-binding pocket formed by ECL2 and helices II, III, V, VI, and VII. This structure reveals major differences from class A, B, and F GPCRs in helix positioning and proline-induced kink distribution, and identifies subtype selectivity determinants for allosteric modulator design.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.1249489 | 4OR2 | 2.80 | -- | Human mGlu1 7TM domain (residues 581-860) with [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) N-terminal fusion | FITM (4-fluoro-N-(4-(6-(isopropylamino)pyrimidin-4-yl)thiazol-2-yl)-N-methylbenzamide) — negative allosteric modulator |

## Expression and Purification

- **Expression system**: Not specified in raw text (see supplementary materials)
- **Construct**: Human mGlu1 7TM domain (residues 581-860) with thermostabilized apocytochrome b562 RIL ([BRIL](/xray-mp-wiki/reagents/protein-tags/bril/)) N-terminal fusion

### Purification Workflow

- **Expression system**: Not specified in raw text
- **Expression construct**: mGlu1 7TM domain (581-860) with [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) fusion

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Purification | Not detailed in main text (see supplementary materials) | -- | Not detailed in main text + See supplementary materials | The truncated construct was verified to bind FITM and be functional in G protein coupling |

**Final sample**: Purified mGlu1 7TM-[BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) fusion protein


## Crystallization

### doi/10.1126##science.1249489

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | Purified mGlu1 7TM-[BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) fusion protein complexed with FITM |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) (likely, standard LCP lipid) |
| Temperature | Not specified |
| Cryoprotection | Not specified |
| Notes | Structure solved at 2.8 A from native data collected from 14 crystals. Initial phases obtained from a 4.0 A SAD data set from a single crystal soaked with tantalum bromide cluster. The asymmetric unit contains a parallel dimer of mGlu1 7TM domains, mediated mainly through helix I, with six well-resolved [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) molecules at the dimer interface. |


## Biological / Functional Insights

### Class C GPCR 7TM domain architecture

The mGlu1 7TM domain adopts the canonical GPCR fold despite less than 15% sequence identity with class A receptors. Unlike class A GPCRs which have proline-induced kinks at positions 5.50, 6.50, and 7.50, mGlu1 has nonproline residues at these positions. Instead, Pro833^{7.56} at the intracellular end of helix VII induces a distinct kink. Helices I-IV overlay well with other GPCRs, but helices V-VII show significant differences: helix V is shifted inward, and the extracellular end of helix VII is also shifted inward, restricting access to the NAM-binding cavity. No helix VIII is observed.

### FITM binding pocket and subtype selectivity

FITM, a negative allosteric modulator with IC50 = 5 nM, binds in a long narrow pocket formed by ECL2 and helices II, III, V, VI, and VII, partially overlapping with orthosteric sites of class A GPCRs. Most interactions are hydrophobic except for a hydrogen bond between the pyrimidine-amine group and Thr815^{7.38}. The p-fluorophenyl moiety contacts Trp798^{6.48}, which adopts an outward conformation (unlike the inward-pointing rotamer in most class A GPCRs). Four residues differ between mGlu1 and mGlu5 in the binding pocket: Val664^{3.32}, Ser668^{3.36}, Thr815^{7.38}, and Ala818^{7.41}. Thr815^{7.38}Met mutation reduces FITM affinity by ~6-fold, identifying it as a key selectivity determinant.

### Inactive conformation with closed intracellular crevice

The NAM-bound mGlu1 structure adopts an inactive conformation similar to class A GPCRs with antagonists. The intracellular crevice for G protein binding is in a closed state, with a hydrogen bond network stabilizing the receptor in its inactive conformation. Comparison with active and inactive class A GPCRs (β2AR) shows that the intracellular end of helix VI would need to move outward during receptor activation, analogous to the conserved activation mechanism across the GPCR superfamily.


## Cross-References

- [Metabotropic Glutamate Receptor 5 (mGlu5)](/xray-mp-wiki/proteins/gpcr/metabotropic-glutamate-receptor-5/) — mGlu1 is closely related to mGlu5; both are group I mGlu receptors. The paper compares the FITM binding pocket and selectivity determinants between mGlu1 and mGlu5.
- [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) — Additive used in purification or crystallization buffers
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Additive used in purification or crystallization buffers
- [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) — Fusion tag for crystallization or purification
