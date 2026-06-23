---
title: "Human Histamine H1 Receptor (H1R)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature10236]
verified: false
---

# Human Histamine H1 Receptor (H1R)

## Overview

The human histamine H1 receptor (H1R) is a [G Protein](/xray-mp-wiki/concepts/signaling-receptors/g-protein/)-coupled receptor ([GPCR](/xray-mp-wiki/concepts/signaling-receptors/gpcr/)) belonging to the aminergic receptor subfamily of class A GPCRs. H1R is expressed in various human tissues including airway, intestinal, and vascular smooth muscle and brain, where it mediates the effects of histamine in type I hypersensitivity allergic reactions and inflammation. The first X-ray crystal structure of H1R was determined at 3.1 A resolution in complex with the first-generation antagonist [Doxepin](/xray-mp-wiki/reagents/ligands/doxepin) (Shimamura et al., 2011, PDB 3RZE). The structure reveals that doxepin sits deep in the ligand-binding pocket, directly interacting with Trp428^6.48, a highly conserved key residue in GPCR activation. A unique anion-binding region occupied by a phosphate ion was observed at the entrance to the binding pocket, coordinated by Lys179^ECL2, Lys191^5.39, Tyr431^6.51, and His450^7.35. H1R is structurally most similar to the beta2-adrenergic receptor, beta1-adrenergic receptor, and dopamine D3 receptor among known GPCR structures. The structure provides a molecular basis for understanding H1R antagonist specificity.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature10236 | 3RZE | 3.1 | I 4 2 2 | Human H1R with N-terminal 19-residue deletion, T4 lysozyme inserted into ICL3 (C54T, C97A), C-terminal TEV cleavage site, yeast-enhanced GFP, and octa-histidine tag | Doxepin (E isomer), phosphate ion |

 - R-work 0.2145%, R-free 0.2486%; Data collection: Complete data set to 3.1 A resolution

## Expression and Purification

- **Expression system**: [Pichia pastoris](/xray-mp-wiki/methods/expression-systems/pichia-pastoris)
- **Construct**: Codon-optimized human H1R with N-terminal 19-residue deletion, T4L in ICL3, TEV cleavage site, yeast-enhanced GFP, octa-histidine tag; cloned into pPIC9K vector
- **Notes**: Expressed in P. pastoris SMD1163 under methanol-inducible AOX1 promoter; induced with 0.5% methanol + 2.5% v/v DMSO at 30 C for 20-24 h

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Glass bead disruption | not specified | 50 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 120 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride), 5% v/v [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 2 mM EDTA, protease inhibitor cocktail + not specified | Yeast cells disrupted with 0.5 mm glass beads; membranes collected by ultracentrifugation at 100,000g; washed with high-salt buffer (1 M NaCl) |
| Membrane solubilization | Detergent solubilization | not specified | not specified + 1% w/v [DDM](/xray-mp-wiki/reagents/detergents/ddm), 0.2% w/v [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate) | Solubilized from P. pastoris membranes |
| [IMAC](/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography) purification | Immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | Ni-NTA [IMAC](/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography) | not specified + [DDM](/xray-mp-wiki/reagents/detergents/ddm), [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate) | C-terminal GFP tag cleaved by [TEV Protease](/xray-mp-wiki/reagents/protein-tags/tev-protease); reverse [IMAC](/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography) to remove cleaved His-tagged GFP and [TEV Protease](/xray-mp-wiki/reagents/protein-tags/tev-protease) |


## Crystallization

### doi/10.1038##nature10236

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase ([LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase)) |
| Protein sample | H1R-doxepin complex in [DDM](/xray-mp-wiki/reagents/detergents/ddm)/[CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate) |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) |
| Temperature | 20 |
| Growth time | Not specified |
| Cryoprotection | Crystals collected and flash-frozen in liquid nitrogen |
| Notes | Protein-LCP mixture: 40% w/w receptor solution, 54% w/w [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein), 6% w/w [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol). The phosphate ion in the reservoir (300 mM ammonium phosphate) was found bound at the entrance to the ligand-binding pocket and acts as a positive modulator of ligand binding. |


## Biological / Functional Insights

### Deep Ligand Binding and Trp428^6.48 Interaction

Doxepin sits approximately 5 A deeper in the binding pocket than ligands in other non-rhodopsin GPCR structures. The tricyclic dibenzo[b,e]oxepin ring makes extensive hydrophobic interactions with Trp428^6.48 (the conserved CWxP motif), which is unique among known non-rhodopsin GPCR structures. This interaction likely stabilizes the hydrophobic packing around helix VI and contributes to the inverse agonist activity of doxepin by locking H1R in an inactive conformation. The highly conserved binding pocket, composed mainly of residues including Ile115^3.40, Phe424^6.44, Trp428^6.48, and Phe432^6.52, explains the low selectivity of first-generation H1R antagonists.

### Anion-Binding Region at Pocket Entrance

A phosphate ion from the crystallization buffer (300 mM ammonium phosphate) was observed coordinated by Lys179^ECL2, Lys191^5.39, Tyr431^6.51, and His450^7.35 at the entrance to the ligand-binding pocket. Except for Tyr431^6.51, these residues are unique to H1R among aminergic receptors. The phosphate ion may act as a positive modulator of ligand binding, as thermostability and ligand affinity increased in the presence of phosphate. The second-generation zwitterionic H1R antagonists (cetirizine, acrivastine, fexofenadine) interact with Lys191^5.39 and/or Lys179^ECL2, providing a structural basis for their enhanced H1R selectivity.

### ECL2 Structure and Ligand Specificity

ECL2 of H1R contains 7 amino acids between the conserved disulfide bridge (Cys100^3.25-Cys180) and helix V, compared to 5 in beta2-AR and 4 in D3R. The extra length is accommodated by increased distance between the extracellular ends of helices III and V (1.5 A vs beta2-AR, 3.1 A vs D3R), creating more space in the ligand-binding pocket for larger second-generation antagonists. Seven residues (Phe168-Val174) before the disulfide were disordered. Doxepin does not interact with ECL2, contributing to its low selectivity.

### H1R Inactivation Mechanism

H1R antagonists act as highly effective inverse agonists, reducing basal receptor activity by up to 78%. The mechanism involves blocking both (1) the activation-related contraction of the extracellular binding pocket (histamine is much smaller than bulky H1R antagonists) and (2) the Trp428^6.48 switch, which in rhodopsin and A2AAR participates in activation-related conformational changes. The extensive interaction between doxepin and Trp428^6.48 is a key feature of H1R inactivation.


## Cross-References

- [G Protein](/xray-mp-wiki/concepts/signaling-receptors/g-protein/) — Related entity
- [GPCR](/xray-mp-wiki/concepts/signaling-receptors/gpcr/) — H1R is a class A GPCR
- [Human Beta2-Adrenergic Receptor](/xray-mp-wiki/proteins/gpcr/beta2-adrenergic-receptor/) — Comparative structural analysis with aminergic GPCR
- [Human Beta-2 Adrenergic Receptor](/xray-mp-wiki/proteins/gpcr/human-beta-2-adrenergic-receptor/) — Comparative structural analysis
- [Human Histamine H3 Receptor](/xray-mp-wiki/proteins/gpcr/human-histamine-h3-receptor/) — Related histamine receptor subtype
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method
- [Pichia Pastoris](/xray-mp-wiki/methods/expression-systems/pichia-pastoris/) — Expression host
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Purification method
- [Immobilized Metal Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Purification method
- [Doxepin](/xray-mp-wiki/reagents/ligands/doxepin/) — Co-crystallized antagonist in H1R structure
