---
title: Human 5-HT2B Receptor
created: 2026-05-27
updated: 2026-06-21
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2016.12.033, doi/10.1038##s41594-018-0116-7, doi/10.1126##science.1244142]
verified: false
---

# Human 5-HT2B Receptor

## Overview

The human serotonin 2B (5-HT2B) receptor is a class A GPCR that signals primarily through Gq/11 and [Beta-Arrestin](/xray-mp-wiki/concepts/beta-arrestin) pathways. It is a target of several drugs and is the molecular target of the hallucinogen LSD. Multiple crystal structures have been determined revealing structural determinants of receptor activation and biased agonism, including complexes with ergotamine, LSD, methylergonovine, methysergide, lisuride, and LY266097.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2016.12.033 | 5TVN | 2.9 A | C2221 | Human 5-HT2B receptor, N-terminal residues 1-35 truncated, C-terminal residues 406-481 truncated, thermostabilizing M144W mutation, ICL3 replaced by BRIL fusion (A1-L106 of apocytochrome b562 RIL), N-terminal HA signal sequence and [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag), C-terminal PreScission site and 10xHis tag | [LSD](/xray-mp-wiki/reagents/ligands/lsd) |

## Expression and Purification

- **Expression system**: [Sf9 Cells](/xray-mp-wiki/methods/expression-systems/sf9-insect-cells)
- **Construct**: Human 5-HT2B receptor, N-terminal residues 1-35 truncated, C-terminal residues 406-481 truncated, thermostabilizing M144W mutation, ICL3 replaced by BRIL fusion (A1-L106 of apocytochrome b562 RIL), N-terminal HA signal sequence and [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag), C-terminal PreScission site and 10xHis tag

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and membrane preparation | Baculovirus expression in [Sf9 Cells](/xray-mp-wiki/methods/expression-systems/sf9-insect-cells) | -- | 10 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 10 mM MgCl2, 20 mM KCl, 150 mM NaCl + -- | High-titer recombinant [Baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression) used to infect Sf9 cells. Cells harvested 48 hr post-infection, washed in PBS, flash-frozen at -80C |
| Membrane solubilization | Detergent solubilization | -- | 10 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 150 mM NaCl + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm) | LSD (50 uM) pre-incubated with membranes before solubilization. [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide) treatment for 30 min prior to solubilization |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | [IMAC](/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography) | [TALON](/xray-mp-wiki/reagents/additives/talon) IMAC resin | -- + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | [His Tag](/xray-mp-wiki/reagents/protein-tags/his-tag) on C-terminus used for affinity capture via TALON resin |
| [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) column | 10 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 150 mM NaCl + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Final purification step to obtain monodisperse 5-HT2B-R-LSD-[BRIL](/xray-mp-wiki/reagents/protein-tags/bril) complex |


## Crystallization

### doi/10.1016##j.cell.2016.12.033

| Parameter | Value |
|---|---|
| Method | [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) crystallization |
| Protein sample | 5-HT2B-R-LSD-[BRIL](/xray-mp-wiki/reagents/protein-tags/bril) complex at ~15 mg/ml |
| Temperature | 20 C |
| Growth time | not specified in main text |
| Cryoprotection | not specified in main text |
| Notes | LCP method with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein). Crystals diffracted to 2.9 A (space group C2221). Solved by molecular replacement using 5-HT2B-R/ERG (PDB: 4IB4) and BRIL (PDB: 1M6T) as search models |

### doi/10.1126##science.1244142

| Parameter | Value |
|---|---|
| Method | [LCP-SFX](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography) |
| Protein sample | 5-HT2B-R-ergotamine-[BRIL](/xray-mp-wiki/reagents/protein-tags/bril) complex in LCP at ~3 mg/ml (300 ug total) |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) |
| Protein-to-lipid ratio | 40:60 (w/w) |
| Temperature | 21 C (room temperature) |
| Notes | LCP-grown microcrystals (5x5x5 um) delivered via LCP injector at LCLS CXI. Co-axial He/N2 gas stabilization at 20-30 bar. 4,217,508 diffraction patterns collected in 10 hours at 120 Hz, 50 fs pulses, 9.5 keV. 152,651 crystal hits (3.6%), 32,819 indexed (21.5%). Structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement) at 2.8 A resolution. Rwork/Rfree = 22.7/27.0%. Space group C2221. First room-temperature GPCR structure obtained by SFX. |


## Biological / Functional Insights

### Unexpected shallow binding mode of LSD

LSD adopts a shallow binding mode in the 5-HT2B receptor orthosteric pocket, positioned higher and closer to EL2 compared to the deeper-binding [Ergotamine](/xray-mp-wiki/reagents/ligands/ergotamine). The ergoline moiety of LSD forms a hydrogen bond between the basic amine and the conserved D135 residue at position 3.32, while the indole nitrogen hydrogen bonds with G221 at position 5.42 in helix V, rather than T140 at position 3.37 at the bottom of the pocket as seen with ergotamine. The diethylamide substituent does not interact with M218 at position 5.39, allowing this residue to flip upward and create more space for LSD shallower pose.

### Arrestin-biased conformational state

The LSD-bound 5-HT2B receptor adopts a conformation reminiscent of the ERG-bound structure, showing hallmarks of an arrestin-biased state. This includes a partially activated PIF motif, larger activation-related changes in helix VII and the NPxxY motif compared to helices V, VI, and the DRY motif. At 5-HT2B receptors, both LSD and ERG preferentially engage [Beta-Arrestin](/xray-mp-wiki/concepts/beta-arrestin)-mediated over Gq-mediated signal transduction.

### EL2 lid and slow LSD dissociation kinetics

Molecular dynamics simulations reveal that extracellular loop 2 (EL2) residues 207-214 form a lid over the binding pocket. The lid residue L209 at EL2 acts as a latch through extensive hydrophobic contacts with LSD and surrounding TM residues. Mutation of L209 to alanine dramatically accelerates LSD off-rate (residence time decreases from 46 min to 4 min at 5-HT2B), selectively dampening [Beta-Arrestin](/xray-mp-wiki/concepts/beta-arrestin)2 recruitment while leaving Gq signaling intact. This structural motif explains LSD extremely slow residence time at serotonin receptors, which likely contributes to its prolonged psychoactive effects.

### Room-temperature SFX structure reveals native conformational ensemble

The 5-HT2B-XFEL structure (2.8 A) was the first room-temperature GPCR structure determined by [Serial Femtosecond Crystallography](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography) (SFX). Comparison with the cryo-cooled synchrotron structure (PDB 4IB4, 2.7 A) revealed that the room-temperature structure has a 2.1% larger unit cell volume and a 2.5 degree rotation of the [BRIL](/xray-mp-wiki/reagents/protein-tags/bril) fusion domain. The average B-factor was 21 A^2 higher (88.4 vs 67.2 A^2), consistent with greater thermal motions. A salt bridge between Glu319 and Lys247, well-defined in the room-temperature structure, appeared broken in the cryo structure, suggesting it plays a role in receptor function. Helix II adopted a regular alpha-helix at room temperature vs a water-stabilized kink in the cryo structure. These findings demonstrate that SFX provides a more accurate representation of the native conformational ensemble of GPCRs.

### Diethylamide stereoselectivity

The conformation of LSD diethylamide moiety in the receptor-bound state differs from the free small-molecule crystal structure by approximately 60 degrees rotation. Sterically constrained analogs show that the (S,S)-azetidide (SSAz) conformation, which matches the receptor-bound LSD conformation, retains full potency and efficacy. In contrast, the (R,R)-azetidide (RRAz) analog, which resembles the free LSD conformation, has much reduced potency for [Beta-Arrestin](/xray-mp-wiki/concepts/beta-arrestin)2 recruitment at both 5-HT2B and 5-HT2A receptors.

### Orthosteric binding pocket (OBP) vs extended binding pocket (EBP) mutations in biased agonism

Systematic mutagenesis of the 5-HT2B receptor reveals that the orthosteric binding pocket (OBP) residue T140^3.37 and the extended binding pocket (EBP) residue A225^5.46 play distinct roles in biased agonism. OBP mutation T140A reduces Gq potency more than beta-arrestin2 recruitment, while EBP mutation A225G enhances Gq potency and converts methysergide from antagonist to full agonist. These results demonstrate that ligand-receptor interactions at different depths in the binding pocket contribute differentially to G protein versus arrestin signaling.

### OBP toggle switch residue L362^7.35

The residue L362^7.35 at the bottom of the orthosteric binding pocket acts as a toggle switch for biased signaling. Mutation to smaller residues (L362A, L362N) or aromatic residues (L362F, L362Y) differentially affects LSD-mediated beta-arrestin2 recruitment. The L362F mutation converts lisuride from a balanced agonist to a Gq-biased ligand, suggesting that steric interactions at the base of the binding pocket control signaling bias through the intracellular cavity.


## Cross-References

- [LSD (Lysergic Acid Diethylamide)](/xray-mp-wiki/reagents/ligands/lsd) — Primary co-crystallized ligand in PDB 5TVN
- [bRIL Fusion Protein](/xray-mp-wiki/reagents/protein-tags/bril) — Replaces ICL3 for crystallization
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm) — Primary solubilization detergent
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) — [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) lipid matrix for crystallization
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes) — Buffer component in purification and crystallization
- [Cholesterol Hemisucinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate) — Stabilizing lipid additive
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) — Crystallization method used
- [Human 5-HT2A Receptor](/xray-mp-wiki/proteins/5ht2a-receptor) — Homology model based on 5-HT2B-R/LSD structure; functional assays performed
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) — Purification method used in protein preparation
- [Baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression) — Expression system used for protein production
- [Serial Femtosecond Crystallography](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography) — SFX method used to obtain room-temperature 2.8 A structure of 5-HT2B-ergotamine complex
