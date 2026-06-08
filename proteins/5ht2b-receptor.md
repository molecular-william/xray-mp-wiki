---
title: Human 5-HT2B Receptor
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2016.12.033]
verified: false
---

# Human 5-HT2B Receptor

## Overview

The human serotonin 2B (5-HT2B) receptor is a class A GPCR that signals primarily through Gq/11 and beta-arrestin pathways. It is a target of several drugs and is the molecular target of the hallucinogen LSD. The crystal structure of the LSD-bound 5-HT2B receptor reveals an unexpected shallow binding mode for LSD in the orthosteric pocket and structural insights into its extremely slow dissociation kinetics.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2016.12.033 | 5TVN | 2.9 A | C2221 | Human 5-HT2B receptor, N-terminal residues 1-35 truncated, C-terminal residues 406-481 truncated, thermostabilizing M144W mutation, ICL3 replaced by BRIL fusion (A1-L106 of apocytochrome b562 RIL), N-terminal HA signal sequence and FLAG tag, C-terminal PreScission site and 10xHis tag | LSD |

## Expression and Purification

- **Expression system**: Sf9 insect cells
- **Construct**: Human 5-HT2B receptor, N-terminal residues 1-35 truncated, C-terminal residues 406-481 truncated, thermostabilizing M144W mutation, ICL3 replaced by BRIL fusion (A1-L106 of apocytochrome b562 RIL), N-terminal HA signal sequence and FLAG tag, C-terminal PreScission site and 10xHis tag

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and membrane preparation | Baculovirus expression in Sf9 insect cells | -- | 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl, 150 mM NaCl + -- | High-titer recombinant baculovirus used to infect Sf9 cells. Cells harvested 48 hr post-infection, washed in PBS, flash-frozen at -80C |
| Membrane solubilization | Detergent solubilization | -- | 10 mM HEPES pH 7.5, 150 mM NaCl + 1% DDM | LSD (50 uM) pre-incubated with membranes before solubilization. Iodoacetamide treatment for 30 min prior to solubilization |
| Affinity chromatography | Ni-NTA affinity chromatography | TALON IMAC resin | -- + DDM | His-tag on C-terminus used for affinity capture via TALON resin |
| Size-exclusion chromatography | Size-exclusion chromatography | SEC column | 10 mM HEPES pH 7.5, 150 mM NaCl + DDM | Final purification step to obtain monodisperse 5-HT2B-R-LSD-BRIL complex |


## Crystallization

### doi/10.1016##j.cell.2016.12.033

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase crystallization |
| Protein sample | 5-HT2B-R-LSD-BRIL complex at ~15 mg/ml |
| Temperature | 20 C |
| Growth time | not specified in main text |
| Cryoprotection | not specified in main text |
| Notes | LCP method with monoolein. Crystals diffracted to 2.9 A (space group C2221). Solved by molecular replacement using 5-HT2B-R/ERG (PDB: 4IB4) and BRIL (PDB: 1M6T) as search models |


## Biological / Functional Insights

### Unexpected shallow binding mode of LSD

LSD adopts a shallow binding mode in the 5-HT2B receptor orthosteric pocket, positioned higher and closer to EL2 compared to the deeper-binding ergotamine. The ergoline moiety of LSD forms a hydrogen bond between the basic amine and the conserved D135 residue at position 3.32, while the indole nitrogen hydrogen bonds with G221 at position 5.42 in helix V, rather than T140 at position 3.37 at the bottom of the pocket as seen with ergotamine. The diethylamide substituent does not interact with M218 at position 5.39, allowing this residue to flip upward and create more space for LSD shallower pose.

### Arrestin-biased conformational state

The LSD-bound 5-HT2B receptor adopts a conformation reminiscent of the ERG-bound structure, showing hallmarks of an arrestin-biased state. This includes a partially activated PIF motif, larger activation-related changes in helix VII and the NPxxY motif compared to helices V, VI, and the DRY motif. At 5-HT2B receptors, both LSD and ERG preferentially engage beta-arrestin-mediated over Gq-mediated signal transduction.

### EL2 lid and slow LSD dissociation kinetics

Molecular dynamics simulations reveal that extracellular loop 2 (EL2) residues 207-214 form a lid over the binding pocket. The lid residue L209 at EL2 acts as a latch through extensive hydrophobic contacts with LSD and surrounding TM residues. Mutation of L209 to alanine dramatically accelerates LSD off-rate (residence time decreases from 46 min to 4 min at 5-HT2B), selectively dampening beta-arrestin2 recruitment while leaving Gq signaling intact. This structural motif explains LSD extremely slow residence time at serotonin receptors, which likely contributes to its prolonged psychoactive effects.

### Diethylamide stereoselectivity

The conformation of LSD diethylamide moiety in the receptor-bound state differs from the free small-molecule crystal structure by approximately 60 degrees rotation. Sterically constrained analogs show that the (S,S)-azetidide (SSAz) conformation, which matches the receptor-bound LSD conformation, retains full potency and efficacy. In contrast, the (R,R)-azetidide (RRAz) analog, which resembles the free LSD conformation, has much reduced potency for beta-arrestin2 recruitment at both 5-HT2B and 5-HT2A receptors.


## Cross-References

- [LSD (Lysergic Acid Diethylamide)](/xray-mp-wiki/reagents/ligands/lsd/) — Primary co-crystallized ligand in PDB 5TVN
- [bRIL Fusion Protein](/xray-mp-wiki/reagents/protein-tags/bril/) — Replaces ICL3 for crystallization
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary solubilization detergent
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — LCP lipid matrix for crystallization
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer component in purification and crystallization
- [Cholesterol Hemisucinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Stabilizing lipid additive
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method used
- [Human 5-HT2A Receptor](/xray-mp-wiki/proteins/5ht2a-receptor/) — Homology model based on 5-HT2B-R/LSD structure; functional assays performed
