---
title: "Orphan GPR52 (G Protein-Coupled Receptor 52)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41586-020-2019-0]
verified: false
---

# Orphan GPR52 (G Protein-Coupled Receptor 52)

## Overview

GPR52 is a class-A orphan G-protein-coupled receptor (GPCR) highly expressed in the brain, representing a promising therapeutic target for Huntington’s disease and psychiatric disorders. Unlike most GPCRs, GPR52 exhibits intrinsically high constitutive activity through a unique self-activation mechanism where extracellular loop 2 (ECL2) occupies the orthosteric binding pocket and operates as a built-in agonist. This study presents high-resolution structures of human GPR52 in three states: ligand-free (apo), Gs-coupled (fully active), and bound to the allosteric surrogate agonist c17. The receptor features a novel side pocket for ligand binding.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41586-020-2019-0 | 6LII | 2.90 A | P 21 21 21 | GPR52-Rub-apo ([Rubredoxin](/xray-mp-wiki/reagents/protein-tags/rubredoxin/) fusion in ICL3, residues 17-340, 7 stabilizing mutations) | none (apo) |
| doi/10.1038##s41586-020-2019-0 | 6LI2 | 3.20 A | I 41 | GPR52-Fla-apo (flavodoxin fusion in ICL3, residues 17-340, 7 stabilizing mutations) | none (apo) |
| doi/10.1038##s41586-020-2019-0 | 6LI0 | 2.80 A | P 21 21 21 | GPR52-c17 ([Rubredoxin](/xray-mp-wiki/reagents/protein-tags/rubredoxin/) fusion, ligand-bound) | c17 (allosteric surrogate agonist) |
| doi/10.1038##s41586-020-2019-0 | 6LI3 | 3.30 A | none (cryo-EM) | GPR52-mini-Gs-[Nb35](/xray-mp-wiki/reagents/antibodies/nb35/) complex | mini-Gs heterotrimer, [Nb35](/xray-mp-wiki/reagents/antibodies/nb35/) [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) |

## Expression and Purification

- **Expression system**: Baculovirus/Sf9 insect cells (Bac-to-Bac system, Invitrogen)
- **Construct**: Human GPR52 residues 17-340. N-terminal HA signal peptide + Flag tag + [Bril](/xray-mp-wiki/reagents/protein-tags/bril/), TEV site, C-terminal 10xHis tag (3C-protease-removable). ICL3 replaced with [Rubredoxin](/xray-mp-wiki/reagents/protein-tags/rubredoxin/) (residues 235-263) or flavodoxin (residues 236-261). 7 stabilizing mutations: A130W, A264L, W278Q, C314P, S318A, N321D, V323T.

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and infection | Sf9 cells infected with baculovirus at 2x10^6 cells/ml, grown at 27C, harvested 48 h post-infection | — |  | Used Bac-to-Bac system |
| Membrane preparation | Low-salt wash (10 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 20 mM KCl, 10 mM [Mgcl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/), protease inhibitors) followed by high-salt wash (10 mM HEPES pH 7.5, 1 M NaCl, 20 mM KCl, 10 mM [Mgcl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/), protease inhibitors) | — |  | For c17 cocrystallization, membranes incubated with 20 uM c17 for 3 h, then 2 mg/ml [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) |
| Solubilization | 100 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/), 800 mM NaCl, 1.0% DDM + 0.2% CHS, stirred 2.5 h at 4C | — |  | c17 (20 uM) added for ligand-bound sample |
| Affinity chromatography | [Talon](/xray-mp-wiki/reagents/additives/talon/) IMAC resin (Clontech), overnight batch binding at 4C | [Talon](/xray-mp-wiki/reagents/additives/talon/) IMAC resin | 50 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 800 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.05% DDM, 0.01% CHS, 10 mM MgCl2, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 20 uM c17 | Washed with 15 CV buffer I, eluted with buffer II (40 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/)) |
| Size-exclusion chromatography | SEC for complex formation and final purification using Superdex 200 10/300 column | Superdex 200 10/300 | 20 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 100 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1 mM MgCl2, 1 uM GDP, 0.1 mM TCEP | GPR52 mixed with 1.2x mini-Gs and 1.5x [Nb35](/xray-mp-wiki/reagents/antibodies/nb35/); peak fractions pooled and concentrated |


## Crystallization

### doi/10.1038##s41586-020-2019-0

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | Purified GPR52 (apo or with c17 ligand), ~30 mg/ml |
| Temperature | 20 C |
| Notes | GPR52-Rub-apo, GPR52-Fla-apo, and GPR52-c17 crystals grown in LCP |

| Parameter | Value |
|---|---|
| Method | [Cryo Em](/xray-mp-wiki/methods/structure-determination/cryo-em/) single-particle analysis |
| Protein sample | GPR52-mini-Gs-[Nb35](/xray-mp-wiki/reagents/antibodies/nb35/) complex, ~2.5 mg/ml |
| Temperature | 4 C (blotting) |
| Notes | Data collected on FEI Titan Krios at 300 kV with Falcon III detector. 7,287 movies; 651,456 particles; nominal global resolution 3.3 A. Processed with RELION-3. |


## Biological / Functional Insights

### ECL2 functions as a built-in agonist (self-activation mechanism)

GPR52s 22-residue ECL2 folds into a small module occupying the orthosteric binding pocket, functioning as a built-in agonist. The second segment (residues 182-190) adopts an extended conformation with a short 3_10 helix that fits into the large hydrophobic cavity. Tyr185 packs against an aromatic cluster (Tyr281, Tyr284, Phe285 of TM6). A salt bridge between Lys182 and Asp188 stabilizes this conformation. This confers intrinsically high basal activity (~90% of maximal) without an external agonist.

### Gs-coupled active state and G-protein coupling interface

The [Cryo Em](/xray-mp-wiki/methods/structure-determination/cryo-em/) structure of GPR52-mini-Gs-Nb35 at 3.3 A reveals the fully active state. TM6 moves outward by ~6 A vs the apo structure. The interface involves TM3, TM5-TM7 and the Ras-like domain of G-alpha-s. The DRY motif (Asp138-Arg139-Tyr317) rearranges: Arg139 stacks with Tyr391 of G-alpha-s, and Tyr317 rotates to lock TM6 in the active position.

### Novel allosteric ligand-binding side pocket

GPR52s orthosteric site is occupied by ECL2. The surrogate agonist c17 binds in a newly identified side pocket between ECL2 and TM1, TM2, and TM7, closer to TM4-TM6. This side pocket is less conserved than the orthosteric pocket. The unique position of Pro214(5.50) in TM5 prevents use of the consensus PIF motif for activation.

### Structural basis for orphan receptor understanding

GPR52 is the closest homologue of GPR21 (71% sequence identity). ECL2 is highly conserved between them, suggesting GPR21 may also self-activate. The structures enable modeling of other orphan receptors and provide a foundation for drug discovery targeting GPR52 for Huntingtons disease and psychiatric disorders.


## Cross-References

- [G Protein-Coupled Receptor (GPCR)](/xray-mp-wiki/concepts/signaling-receptors/gpcr/) — GPR52 is a class-A orphan GPCR
- [n-Dodecyl-beta-D-Maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for membrane protein solubilization
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — LCP matrix lipid for crystallization
- [Lipidic Cubic Phase (LCP) Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used for GPR52 crystallization
- [Rubredoxin](/xray-mp-wiki/reagents/protein-tags/rubredoxin/) — Referenced in gpr52 text
- [Nb35](/xray-mp-wiki/reagents/antibodies/nb35/) — Referenced in gpr52 text
- [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) — Referenced in gpr52 text
- [Bril](/xray-mp-wiki/reagents/protein-tags/bril/) — Referenced in gpr52 text
- [Mgcl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/) — Referenced in gpr52 text
- [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) — Referenced in gpr52 text
