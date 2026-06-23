---
title: Epithelial Calcium Channel TRPV6
created: 2026-06-10
updated: 2026-06-10
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature17975, doi/10.1038##s41598-017-10993-9, doi/10.1126##sciadv.abe1508]
verified: false
---

# Epithelial Calcium Channel TRPV6

## Overview

TRPV6 is a Ca2+-selective transient receptor potential vanilloid channel uniquely expressed in epithelial tissues where it mediates active Ca2+ absorption across the intestinal and other epithelial barriers. TRPV6 forms homo- or heteromeric tetrameric assemblies of four subunits, each containing a central K+ channel-like transmembrane domain flanked by intracellular N- and C-terminal domains. The channel is essential for calcium homeostasis and its overexpression has been implicated in various cancers. Structural studies have revealed the architecture of TRPV6, its Ca2+ selectivity and permeation mechanism, and the molecular basis of inhibition by (4-phenylcyclohexyl)piperazine derivatives (PCHPDs) that act as inactivation-mimicking pore blockers.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature17975 | 5IWK | 3.25 A | P4_12_12 | Rat TRPV6 crystallization construct (TRPV6_cryst), residues 1-668, mutations I62Y, L92N, M96Q, L495Q, C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) | [Desthiobiotin](/xray-mp-wiki/reagents/ligands/desthiobiotin/) (bound at intersubunit interface during affinity purification) |
| doi/10.1038##nature17975 | 5IWP | 3.85 A | P4_12_12 | Rat TRPV6 crystallization construct with Ba2+ | Ba2+ (10 mM BaCl2) |
| doi/10.1038##nature17975 | 5IWR | 3.65 A | P4_12_12 | Rat TRPV6 crystallization construct with Ca2+ | Ca2+ (10 mM CaCl2) |
| doi/10.1038##nature17975 | 5IWT | 3.80 A | P4_12_12 | Rat TRPV6 crystallization construct with Gd3+ | Gd3+ (1 mM GdCl3) |
| doi/10.1038##s41598-017-10993-9 | 5WO6 | 3.45 A | P42_12 | TRPV6_cryst (same as 5IWK), mutations I62Y, L92N, M96Q, L495Q | -- |
| doi/10.1038##s41598-017-10993-9 | 5WO7 | 3.25 A | P42_12 | TRPV6* (L495Q reverted to native L495), C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/), I62Y, L92N, M96Q | -- |
| doi/10.1038##s41598-017-10993-9 | 5WO8 | 3.40 A | P42_12 | TRPV6*-del1 (4 residues deleted in S4-S5 linker, 477-480) | -- |
| doi/10.1038##s41598-017-10993-9 | 5WO9 | 3.6 A | P42_12 | TRPV6_cryst with Ca2+, mutations I62Y, L92N, M96Q, L495Q | Ca2+ |
| doi/10.1038##s41598-017-10993-9 | 5WOA | 3.85 A | P42_12 | TRPV6_cryst with Gd3+, mutations I62Y, L92N, M96Q, L495Q | Gd3+ |

## Expression and Purification

- **Expression system**: HEK 293S cells (GnTI-), BacMam expression
- **Construct**: Rat TRPV6 (GenBank EDM15484.1), crystallization construct TRPV6_cryst comprising residues 1-668 with point mutations I62Y, L92N, M96Q, L495Q and C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/). C-terminal thrombin cleavage site (LVPRG) followed by eGFP and streptavidin affinity tag (WSHPQFEK). Expressed in [PEG](/xray-mp-wiki/reagents/additives/peg/) BacMam vector.
- **Notes**: For [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) studies, hTRPV6-FL (residues 1-725) and hTRPV6-CtD (residues 1-666, C-terminally truncated) constructs were used with C-terminal thrombin cleavage site followed by streptavidin affinity tag.

### Purification Workflow

- **Expression system**: HEK 293S (GnTI-)
- **Expression construct**: Rat TRPV6_cryst (residues 1-668, I62Y, L92N, M96Q, L495Q), C-terminal thrombin-eGFP-Strep tag
- **Tag info**: C-terminal streptavidin affinity tag (WSHPQFEK), removable by thrombin cleavage

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Sonication | -- | 150 mM NaCl, 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 1 mM [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/), 0.8 uM aprotinin, 2 ug/ml leupeptin, 2 mM pepstatin A, 1 mM PMSF + -- | Misonix Sonicator, 12 x 15 sec, power level 7 |
| Membrane collection | Ultracentrifugation | -- | -- + -- | Sorval centrifuge 7,500 rpm 15 min, then Beckman Ti45 rotor 40,000 RPM 1 h |
| Solubilization | Detergent solubilization | -- | 150 mM NaCl, 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 1 mM [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/), protease inhibitors + 20 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | 2-4 hours incubation |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Strep [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Streptavidin-linked resin | 150 mM NaCl, 20 mM Tris pH 8.0, 1 mM [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/) + 20 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Rotated 4-16 hours, eluted with 10 mM [Desthiobiotin](/xray-mp-wiki/reagents/ligands/desthiobiotin/) |
| Thrombin cleavage | Protease cleavage | -- | 150 mM NaCl, 20 mM Tris pH 8.0, 1 mM [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/) + 0.5 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Thrombin added at 1:50 ratio, 1.5 hours at 22C |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | SEC | Superose 6 column | 150 mM NaCl, 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 1 mM betaME + 0.5 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Tetrameric channel fractions collected, 10 mM TCEP added |

**Final sample**: Purified in 150 mM NaCl, 20 mM Tris pH 8.0, 1 mM betaME, 0.5 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/)


## Crystallization

### doi/10.1038##nature17975

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | TRPV6_cryst at 2.5-3.0 mg/ml in 150 mM NaCl, 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 1 mM betaME, 0.5 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Reservoir | 20-24% [PEG](/xray-mp-wiki/reagents/additives/peg/) 350 MME, 100 mM NaCl, 100 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0-8.5 |
| Mixing ratio | -- |
| Temperature | 20 C |
| Growth time | ~2 weeks |
| Cryoprotection | 33-36% [PEG](/xray-mp-wiki/reagents/additives/peg/) 350 MME, 100 mM NaCl, 100 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.2, 0.5 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 50 mM [Ammonium Formate](/xray-mp-wiki/reagents/additives/ammonium-formate/), flash frozen in liquid nitrogen |
| Notes | Crystals grew as thin plates (~400 um x ~120 um x ~20 um). 50 mM [Ammonium Formate](/xray-mp-wiki/reagents/additives/ammonium-formate/) added to protein before crystallization to increase crystal size. For co-crystallization with cations, protein was incubated with 10 mM CaCl2, 10 mM BaCl2, or 1 mM GdCl3 for 1 hour at 4C prior to crystallization. |

### doi/10.1038##s41598-017-10993-9

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | TRPV6* or TRPV6*-del1 at 2.5-3.0 mg/ml in 150 mM NaCl, 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 1 mM betaME, 0.5 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Reservoir | 20-24% [PEG](/xray-mp-wiki/reagents/additives/peg/) 350 MME, 50 mM NaCl, 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0-8.5 |
| Mixing ratio | -- |
| Temperature | 20 C |
| Cryoprotection | 100 mM NaCl, 100 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.2, 0.5 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 50 mM [Ammonium Formate](/xray-mp-wiki/reagents/additives/ammonium-formate/), 33-36% [PEG](/xray-mp-wiki/reagents/additives/peg/) 350 MME, flash frozen in liquid nitrogen |
| Notes | Protein subjected to ultracentrifugation (Ti100 rotor, 40000 rpm, 40 min, 4C) prior to crystallization to remove aggregates. For cation-bound structures, protein was incubated with 10 mM CaCl2 or 1 mM GdCl3 for 1 h at 4C prior to crystallization. |


## Biological / Functional Insights

### TRPV6 architecture and domain organization

TRPV6 forms a four-fold symmetrical tetramer with a central ion channel pore and a ~70 A tall intracellular skirt. Each subunit contains an ankyrin repeat domain (ARD) with six ankyrin repeats, a linker domain with beta-hairpin and helix-turn-helix motif, pre-S1 helix, and a K+ channel-like transmembrane domain (S1-S6 with P-loop). A unique non-swapped TM domain arrangement was observed where S1-S4 and pore domains of the same protomer pack against each other.

### Ca2+ selectivity and permeation mechanism

Ca2+ selectivity is determined by direct coordination of Ca2+ by a ring of aspartate side chains in the selectivity filter (sequence 538TIID541). D541 side chains protrude toward the pore central axis. A Ca2+ knock-off mechanism of permeation is proposed where Site 1 is constitutively occupied by Ca2+ due to charge repulsion between D541 side chains.

### Domain swapping governed by residue 495

TRPV6 can adopt either a domain-swapped or non-swapped transmembrane architecture depending on residue 495 in the S5 helix. The native leucine (L495) drives a domain-swapped fold. Mutation to glutamine (L495Q) converts to non-swapped. The S4-S5 linker length is also a critical determinant.

### Inactivation-mimicking pore block by PCHPDs

(4-Phenylcyclohexyl)piperazine derivatives (PCHPDs) are potent and selective TRPV6 inhibitors that act via two binding sites: (i) modulatory sites at lipid-binding site 2 (LBS-2) between S1-S4 and pore domains, and (ii) the main site in the ion channel pore at the intracellular entrance. At the pore site, PCHPDs plug the open pore, physically obstructing ion conductance, mimicking the action of calmodulin (CaM) which causes Ca2+-induced inactivation. The inhibitor binding at the pore mimics the tryptophan cage mechanism where K115 of CaM interacts with W583. This represents a unique inactivation-mimicking inhibition strategy unprecedented among TRP channels.

### Tryptophan cage mechanism for pore block

Four W583 residues from each TRPV6 subunit form a tight cubic cage (4.2 A between indole rings) that provides a unique environment for cation-pi interaction with the epsilon-amino group of CaM K115. PCHPDs exploit this same site, mimicking the inactivation mechanism. The W583F mutation dramatically reduces [cis-22a (PCHPD TRPV6 Inhibitor)](/xray-mp-wiki/reagents/ligands/cis-22a/) affinity (75-fold increase in IC50 from 0.083 to 6.19 uM), confirming the importance of this tryptophan cage for inhibition.


## Cross-References

- [Epithelial Calcium Channel TRPV5](/xray-mp-wiki/proteins/voltage-gated-channels/trpv5/) — Closely related Ca2+ channel (~75% sequence identity); CaM-dependent inactivation mechanism conserved
- [TRPV2](/xray-mp-wiki/proteins/voltage-gated-channels/trpv2/) — TRP channel family member; structural comparison of lipid-binding sites
- [C-type Inactivation](/xray-mp-wiki/concepts/structural-mechanisms/c-type-inactivation/) — PCHPD inhibition mimics Ca2+-induced inactivation mechanism; tryptophan cage at pore intracellular entrance
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary solubilization detergent (20 mM) for TRPV6 extraction from membranes
- [Desthiobiotin](/xray-mp-wiki/reagents/ligands/desthiobiotin/) — Elution agent for Strep affinity purification (10 mM); bound at intersubunit interface in crystal structure
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Method used in structure determination or purification
- [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) — Method used in structure determination or purification
- [Ammonium Formate](/xray-mp-wiki/reagents/additives/ammonium-formate/) — Additive used in purification or crystallization buffers
