---
title: Turkey Beta1-Adrenergic Receptor (beta1AR)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1100185108, doi/10.1126##science.aau5595]
verified: false
---

# Turkey Beta1-Adrenergic Receptor (beta1AR)

## Overview

The turkey beta1-adrenergic receptor (beta1AR) is a class A G-protein-coupled receptor (GPCR) that mediates physiological effects of catecholamines such as adrenaline and noradrenaline. Crystal structures have been determined for both inactive and active states, including the thermostabilized beta36-M23 construct bound to antagonists and active-state structures bound to agonists in complex with conformation-specific nanobodies. Comparison of inactive and active states bound to the same ligands reveals that the orthosteric binding site contracts by 24-42% upon activation, with shorter hydrogen bonds and up to 30% more atomic contacts between receptor and ligand, explaining the higher agonist affinity of the active state.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1100185108 | 2VT4 | 2.7 | — | beta36-M23 (deletions at N-term, C-term, and CL3; 6 thermostabilizing mutations) | [Cyanopindolol](/xray-mp-wiki/reagents/ligands/cyanopindolol/) |
| doi/10.1126##science.aau5595 | 6H7J | 3.0 | — | beta1AR with Nb80 or Nb6B9 [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) | [Isoprenaline](/xray-mp-wiki/reagents/ligands/isoprenaline/) |
| doi/10.1126##science.aau5595 | 6H7L | 3.2 | — | beta1AR with Nb80 or Nb6B9 [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) | [Dobutamine](/xray-mp-wiki/reagents/ligands/dobutamine/) |
| doi/10.1126##science.aau5595 | 6H7M | 3.1 | — | beta1AR with Nb80 or Nb6B9 [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) | [Salbutamol](/xray-mp-wiki/reagents/ligands/salbutamol/) |
| doi/10.1126##science.aau5595 | 6H7O | 3.0 | — | beta1AR with Nb80 or Nb6B9 [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) | [Cyanopindolol](/xray-mp-wiki/reagents/ligands/cyanopindolol/) |

## Expression and Purification

- **Expression system**: Baculovirus expression in Sf9 insect cells
- **Construct**: beta36-M23 (thermostabilized) or wild-type beta1AR for active-state structures
- **Notes**: The beta36 construct has deletions in flexible regions at N and C termini and cytoplasmic loop 3 (CL3). Six thermostabilizing mutations (M23) introduced for tolerance to short-chain detergents.

### Purification Workflow

*Source: doi/10.1073##pnas.1100185108*

- **Expression system**: Sf9 insect cells (baculovirus)
- **Expression construct**: beta1AR36-M23
- **Tag info**: His-tag (Ni2+-affinity)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Solubilization | Detergent extraction | — | beta-decylmaltoside | Receptor solubilized from membranes |
| Affinity chromatography | Ni2+-affinity | Ni-NTA |  | First purification step |
| Ligand affinity chromatography | [Alprenolol](/xray-mp-wiki/reagents/ligands/alprenolol/) sepharose affinity | — | [OTG](/xray-mp-wiki/reagents/detergents/octylthioglucoside/) (0.35%) | Detergent exchange to [OTG](/xray-mp-wiki/reagents/detergents/octylthioglucoside/) performed on the ligand affinity column. For carazolol-bound crystals, detergent was exchanged to [HEGA-10](/xray-mp-wiki/reagents/detergents/hega-10/) (0.35%) and receptor eluted with 50 microM [Carazolol](/xray-mp-wiki/reagents/ligands/carazolol/). |

**Final sample**: 5.5-9 mg/mL in crystallization buffer

### Purification Workflow

*Source: doi/10.1126##science.aau5595*

- **Expression system**: Sf9 insect cells (baculovirus)
- **Expression construct**: beta1AR (wild-type or modified for nanobody complex formation)
- **Tag info**: His-tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation and solubilization | Detergent extraction | — |  | Standard membrane protein solubilization procedures |
| Purification | Affinity chromatography and size-exclusion chromatography | — |  | Purified in complex with Nb80 or Nb6B9 nanobodies and respective agonist ligands |

**Final sample**: beta1AR-nanobody-agonist complex for crystallization


## Crystallization

### doi/10.1073##pnas.1100185108

| Parameter | Value |
|---|---|
| Method | Sitting drop vapor diffusion |
| Protein sample | 5.5 mg/mL (cyanopindolol/iodocyanopindolol) or 9 mg/mL ([Carazolol](/xray-mp-wiki/reagents/ligands/carazolol/)) |
| Reservoir | 0.1 M N-(2-acetamido)iminodiacetate-NaOH pH 6.9-7.3, 29-33% [Peg](/xray-mp-wiki/reagents/additives/peg/) 600 ([Cyanopindolol](/xray-mp-wiki/reagents/ligands/cyanopindolol/)); or 0.1 M [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 8.1, 40% [Peg](/xray-mp-wiki/reagents/additives/peg/) 400 ([Carazolol](/xray-mp-wiki/reagents/ligands/carazolol/)) |
| Temperature | 293 |
| Cryoprotection | 60% [Peg600](/xray-mp-wiki/reagents/additives/peg-600/) (t148), 40% [PEG400](/xray-mp-wiki/reagents/additives/peg-400/) (t1118), or 35% [Peg600](/xray-mp-wiki/reagents/additives/peg-600/) + 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) (t468). No additional cryoprotectant for t756. |
| Notes | Crystals grew in space groups P21 ([Carazolol](/xray-mp-wiki/reagents/ligands/carazolol/)) or C2 (cyanopindolol/iodocyanopindolol). Data collected at ESRF ID23-2 and SLS X06SA. |

### doi/10.1126##science.aau5595

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | beta1AR-nanobody-agonist complex |
| Temperature | 293 |
| Notes | Four crystal structures determined with resolutions between 3.0-3.2 A. Data collected at ESRF (beamlines ID23-2, ID30-A3, ID29, ID30B, MASSIF-1) and Diamond Light Source (beamline I24). |


## Biological / Functional Insights

### Two conformations of helix 6 in beta1AR

Eight new structures of beta1AR-M23 from four different crystals with three different antagonists reveal only two distinct conformations of the cytoplasmic end of helix 6: bent and straight. In the bent conformation, the Arg139-Glu285 salt bridge (ionic lock) is present, similar to dark-state rhodopsin. In the straight conformation, the ends of helices 3 and 6 are too far apart for the ionic lock to form.

### Ionic lock distance correlates with basal activity

In the bent conformation, the R3.50-E6.30 distance is 3.7-3.9 A, significantly longer than in rhodopsin (2.8-3.2 A), suggesting a weaker interaction that could explain the higher basal activity of beta1AR compared to rhodopsin.

### HKAL sequence as conformational switch

The His286-Lys287-Ala288-Leu289 (HKAL) sequence at the cytoplasmic end of H6 acts as a conformational switch. The bent conformation shows a marked kink at Ala288/Lys287, while the straight conformation has an extended helix. Mutations in this region are associated with constitutive activity in various GPCRs and human diseases.

### Orthosteric binding site contraction upon activation

Comparison of inactive and active state structures of beta1AR bound to the identical ligands ([Isoprenaline](/xray-mp-wiki/reagents/ligands/isoprenaline/), [Salbutamol](/xray-mp-wiki/reagents/ligands/salbutamol/), [Dobutamine](/xray-mp-wiki/reagents/ligands/dobutamine/), [Cyanopindolol](/xray-mp-wiki/reagents/ligands/cyanopindolol/)) reveals that the orthosteric binding site volume decreases by 24-42% upon activation. Potential hydrogen bonds become shorter, and there is up to a 30% increase in the number of atomic contacts between receptor and ligand. These changes explain the increase in agonist affinity of GPCRs in the active state.

### Partial occlusion of the orthosteric binding pocket entrance

In beta2AR, Tyr308(7.35) makes van der Waals contact with Phe193(ECL2) to occlude the binding pocket entrance. In beta1AR, the equivalent residues are Phe201(ECL2) and Phe325(7.35), which are not in van der Waals contact. The F325Y mutation in beta1AR slows the rate of ligand association, but does not significantly affect agonist affinity for the high-affinity state, suggesting that occlusion of the binding pocket entrance is not the primary determinant of increased agonist affinity in the active state.

### Active state of beta1AR is virtually identical to agonist-bound beta2AR active state

The overall structure of the beta1AR-nanobody complexes bound to agonists is virtually identical to the agonist-bound Nb6B9-beta2AR complex (0.5 A RMSD of 1601 atoms). This suggests a conserved mechanism of activation across related GPCRs.


## Cross-References

- [Human Beta2-Adrenergic Receptor (beta2 AR)](/xray-mp-wiki/proteins/gpcr/beta2-adrenergic-receptor/) — Close structural homolog for comparison of GPCR active and inactive states
- [GPCR Active State High-Affinity Agonist Binding](/xray-mp-wiki/concepts/signaling-receptors/gpcr-active-state-high-affinity-agonist-binding/) — Concept explaining the structural basis for increased agonist affinity in the active state
- [Cyanopindolol](/xray-mp-wiki/reagents/ligands/cyanopindolol/) — Referenced in the context of Cyanopindolol
- [Carazolol](/xray-mp-wiki/reagents/ligands/carazolol/) — Referenced in the context of Carazolol
- [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) — Referenced in the context of Nanobody
- [Isoprenaline](/xray-mp-wiki/reagents/ligands/isoprenaline/) — Referenced in the context of Isoprenaline
- [Dobutamine](/xray-mp-wiki/reagents/ligands/dobutamine/) — Referenced in the context of Dobutamine
- [Salbutamol](/xray-mp-wiki/reagents/ligands/salbutamol/) — Referenced in the context of Salbutamol
- [Alprenolol](/xray-mp-wiki/reagents/ligands/alprenolol/) — Referenced in the context of Alprenolol
- [OTG](/xray-mp-wiki/reagents/detergents/octylthioglucoside/) — Referenced in the context of OTG
