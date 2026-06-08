---
title: Epithelial Calcium Channel TRPV6
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature17975]
verified: false
---

# Epithelial Calcium Channel TRPV6

## Overview

TRPV6 is a Ca²⁺-selective transient receptor potential vanilloid channel uniquely expressed in epithelial tissues where it mediates active Ca²⁺ absorption across the intestinal and other epithelial barriers. TRPV6 forms homo- or heteromeric tetrameric assemblies of four subunits, each containing a central K⁺ channel-like transmembrane domain flanked by intracellular N- and C-terminal domains. The channel is essential for calcium homeostasis and its overexpression has been implicated in various cancers. The crystal structure of rat TRPV6 reveals a unique non-swapped TM domain arrangement and identifies a Ca²⁺ knock-off permeation mechanism mediated by multiple cation binding sites within the pore.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature17975 | 5IWK | 3.25 A | P4₁2₁2 | Rat TRPV6 crystallization construct (TRPV6_cryst), residues 1-668, mutations I62Y, L92N, M96Q, L495Q, C-terminal truncation | Desthiobiotin (bound at intersubunit interface during affinity purification) |
| doi/10.1038##nature17975 | 5IWP | 3.85 A | P4₁2₁2 | Rat TRPV6 crystallization construct with Ba²⁺ | Ba²⁺ (10 mM BaCl₂) |
| doi/10.1038##nature17975 | 5IWR | 3.65 A | P4₁2₁2 | Rat TRPV6 crystallization construct with Ca²⁺ | Ca²⁺ (10 mM CaCl₂) |
| doi/10.1038##nature17975 | 5IWT | 3.80 A | P4₁2₁2 | Rat TRPV6 crystallization construct with Gd³⁺ | Gd³⁺ (1 mM GdCl₃) |

## Expression and Purification

- **Expression system**: HEK 293S cells (GnTI⁻), BacMam expression
- **Construct**: Rat TRPV6 (GenBank EDM15484.1), crystallization construct TRPV6_cryst comprising residues 1-668 with point mutations I62Y, L92N, M96Q, L495Q and C-terminal truncation. C-terminal thrombin cleavage site (LVPRG) followed by eGFP and streptavidin affinity tag (WSHPQFEK). Expressed in pEG BacMam vector.


### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Sonication | -- | 150 mM NaCl, 20 mM Tris-HCl pH 8.0, 1 mM β-mercaptoethanol, 0.8 µM aprotinin, 2 µg/ml leupeptin, 2 mM pepstatin A, 1 mM PMSF + -- | Misonix Sonicator, 12 × 15 sec, power level 7 |
| Membrane collection | Ultracentrifugation | -- | -- + -- | Sorval centrifuge 7,500 rpm 15 min, then Beckman Ti45 rotor 40,000 RPM 1 h |
| Solubilization | Detergent solubilization | -- | 150 mM NaCl, 20 mM Tris-HCl pH 8.0, 1 mM β-mercaptoethanol, 20 mM n-dodecyl-β-D-maltopyranoside (DDM), protease inhibitors + 20 mM DDM | 2-4 hours incubation |
| Affinity chromatography | Strep affinity chromatography | Streptavidin-linked resin | 150 mM NaCl, 20 mM Tris pH 8.0, 1 mM β-mercaptoethanol, 20 mM DDM + 20 mM DDM | Rotated 4-16 hours, eluted with 10 mM desthiobiotin |
| Thrombin cleavage | Protease cleavage | -- | 150 mM NaCl, 20 mM Tris pH 8.0, 1 mM β-mercaptoethanol, 0.5 mM DDM + 0.5 mM DDM | Thrombin added at 1:50 ratio, 1.5 hours at 22°C |
| Size exclusion chromatography | SEC | Superose 6 column | 150 mM NaCl, 20 mM Tris-HCl pH 8.0, 1 mM βME, 0.5 mM DDM + 0.5 mM DDM | Tetrameric channel fractions collected, 10 mM TCEP added |


## Crystallization

### doi/10.1038##nature17975

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | TRPV6_cryst at 2.5-3.0 mg/ml in 150 mM NaCl, 20 mM Tris-HCl pH 8.0, 1 mM βME, 0.5 mM DDM |
| Reservoir | 20-24% PEG 350 MME, 100 mM NaCl, 100 mM Tris-HCl pH 8.0-8.5 |
| Temperature | 20 |
| Growth time | ~2 weeks |
| Cryoprotection | 33-36% PEG 350 MME, 100 mM NaCl, 100 mM Tris-HCl pH 8.2, 0.5 mM DDM, 50 mM ammonium formate, flash frozen in liquid nitrogen |
| Notes | Crystals grew as thin plates (~400 µm x ~120 µm x ~20 µm). 50 mM ammonium formate added to protein before crystallization to increase crystal size. For co-crystallization with cations, protein was incubated with 10 mM CaCl₂, 10 mM BaCl₂, or 1 mM GdCl₃ for 1 hour at 4°C prior to crystallization. |


## Biological / Functional Insights

### TRPV6 architecture and domain organization

TRPV6 forms a four-fold symmetrical tetramer with a central ion channel pore and a ~70 Å tall intracellular skirt. Each subunit contains an ankyrin repeat domain (ARD) with six ankyrin repeats, a linker domain with β-hairpin and helix-turn-helix motif, pre-S1 helix, and a K⁺ channel-like transmembrane domain (S1-S6 with P-loop). A unique non-swapped TM domain arrangement was observed where S1-S4 and pore domains of the same protomer pack against each other. The S6-TRP helix linker is unstructured, unlike other TRP channels. An amphipathic TRP helix runs parallel to the membrane and interacts with intracellular soluble domains.

### Ca²⁺ selectivity mechanism

Ca²⁺ selectivity is determined by direct coordination of Ca²⁺ by a ring of aspartate side chains in the selectivity filter (sequence ⁵³⁸TIID⁵⁴¹). D541 side chains protrude toward the pore central axis producing a minimum interatomic distance of 4.6 Å, large enough to accommodate a dehydrated Ca²⁺ ion (typical Ca²⁺-oxygen distance ~2.4 Å). Three conserved phenylalanine residues (F530, F533, F536) in the pore helix restrict selectivity filter dynamics, contributing to the static outer pore domain.

### Multiple cation binding sites in the pore

Four types of cation binding sites were identified. Site 1 at the selectivity filter (D541 plane) is the main high-affinity Ca²⁺ binding site. Site 2, 6-8 Å below Site 1, coordinates cations through hydration shell by T538 backbone carbonyls and sidechain hydroxyls. Site 3 in the hydrophobic cavity at M569 level coordinates cations via ordered water molecules. Recruitment sites in the electronegative outer vestibule (near D517, E518, D547) recruit cations toward the extracellular vestibule.

### Knock-off Ca²⁺ permeation mechanism

A Ca²⁺ knock-off mechanism of permeation is proposed. Site 1 is constitutively occupied by Ca²⁺ due to charge repulsion between D541 side chains. New Ca²⁺ ions must knock off the bound ion, necessitating high local Ca²⁺ concentration. After knock-off from Site 1, Ca²⁺ moves to Site 2 (coordinated via hydration shell by T538), then to Site 3 where it is poised to enter the cell. Ba²⁺ shows higher affinity for Site 2 compared to Site 1, suggesting different permeation kinetics. Gd³⁺ blocks divalent permeation through strong binding at Site 1.

### Intracellular skirt assembly and allosteric regulation

Intracellular domains engage in extensive inter- and intrasubunit interactions forming a skirt with a ~50 Å × 50 Å cavity. The N-terminal helix acts as a hub for domain interactions, stabilized by hydrogen bonds and salt bridges involving D34. Desthiobiotin was observed bound at the intersubunit interface near the ATP-binding site conserved in TRPV1, TRPV3, and TRPV4 ankyrin repeats. This site may be targeted by endogenous or exogenous factors for allosteric modulation.


## Cross-References

- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/n-dodecyl-beta-d-maltopyranoside/) — Primary solubilization detergent (20 mM) for TRPV6 extraction from membranes
- [Polyethylene Glycol 350 Monomethyl Ether (PEG 350 MME)](/xray-mp-wiki/reagents/additives/peg-350-mme/) — Main crystallization precipitant (20-24%)
- [Ammonium Formate](/xray-mp-wiki/reagents/additives/ammonium-formate/) — Added to protein before crystallization (50 mM) to increase crystal size
- [Desthiobiotin](/xray-mp-wiki/reagents/ligands/desthiobiotin/) — Elution agent for Strep affinity purification (10 mM) and bound at intersubunit interface
- [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/) — Reducing agent (1 mM) used throughout purification
- [Tris-(2-carboxyethyl)phosphine (TCEP)](/xray-mp-wiki/reagents/additives/tcep/) — Reducing agent (10 mM) added to purified protein fractions
- [Epithelial Calcium Channel TRPV5](/xray-mp-wiki/proteins/trpv5/) — Closely related Ca²⁺ channel (~75% sequence identity), structural comparison
- [Transient Receptor Potential Vanilloid 1 (TRPV1)](/xray-mp-wiki/proteins/trpv1/) — TRP channel family member used for structural comparison (PDB entry 3J5P)
