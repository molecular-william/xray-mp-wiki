---
title: Chicken BEST1 Bestrophin-1 Ca2+-activated Cl- channel
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature13913, doi/10.1073##pnas.1614688113]
verified: false
---

# Chicken BEST1 Bestrophin-1 Ca2+-activated Cl- channel

## Overview

Bestrophin-1 (BEST1) is a calcium-activated chloride channel (CaCC) that regulates the flow of chloride and other monovalent anions across cellular membranes in response to intracellular calcium levels. The X-ray structure of chicken BEST1-Fab complexes, determined at 2.85 A resolution, reveals a pentameric assembly of subunits forming a single ion pore approximately 95 A in length along the central axis. The pore contains at least 15 binding sites for anions. Subsequent electrophysiological studies of purified wild-type and mutant BEST1 channels, together with the X-ray structure of a constitutively active TripleA mutant (I76A/F80A/F84A), identified distinct regions controlling ion selectivity and Ca2+-dependent activation. The hydrophobic neck functions as a Ca2+-dependent gate, the Ca2+ clasp serves as the intracellular Ca2+ sensor, and the aperture acts as a size-selective filter that governs relative permeabilities among anions. Mutations in human BEST1 cause vitelliform macular dystrophy (Best's disease) and other retinopathies.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature13913 | unknown | 2.85 | unknown | Chicken BEST1 (N-terminal region, residues 1-390) crystallized as complex with Fab fragments | Ca2+, Cl-/Br- |
| doi/10.1073##pnas.1614688113 | not specified in paper text | not specified | unknown | Chicken BEST1 TripleA mutant (I76A/F80A/F84A) in complex with Fab 10-D10 | Ca2+ |

## Expression and Purification

- **Expression system**: Not specified in text (likely insect or mammalian expression)
- **Construct**: Chicken BEST1 N-terminal region (residues 1-390) sufficient for CaCC activity
- **Notes**: In the subsequent PNAS study, BEST1 was expressed recombinantly and purified for electrophysiology, flux assays, and crystallization studies.

### Purification Workflow

*Source: doi/10.1038##nature13913*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein purification | Not detailed in main text | -- | Not specified + Not specified | BEST1 was purified and reconstituted into liposomes for functional assays. BEST1-Fab complex was formed for crystallization. |

### Purification Workflow

*Source: doi/10.1073##pnas.1614688113*

- **Expression system**: Insect cells (likely Sf9 or High Five)
- **Expression construct**: Chicken BEST1 N-terminal region (residues 1-390)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Baculovirus expression system | — |  | Recombinant expression of chicken BEST1 for purification |
| Purification | Not detailed for protein alone | -- | Not specified | BEST1 was purified and reconstituted into liposomes for planar lipid bilayer recordings and flux assays. For crystallization, BEST1 was complexed with Fab 10-D10 at 1:1.2 molar ratio and purified by SEC on [Superdex 200 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200/) in buffer containing 10 mM [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 75 mM NaCl, 75 mM KCl, 0.5 mM CymaI-6 (Anatrace). |


## Crystallization

### doi/10.1038##nature13913

| Parameter | Value |
|---|---|
| Method | Not detailed in main text |
| Protein sample | BEST1-Fab complex with Ca2+ and permeant anions |
| Reservoir | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Crystals grown with different detergents showed subtle structural changes near the Ca2+ clasp correlated with changes in the neck diameter, suggesting conformational coupling between the Ca2+ sensor and the gate. |

### doi/10.1073##pnas.1614688113

| Parameter | Value |
|---|---|
| Method | Sitting drop vapor diffusion |
| Protein sample | BEST1 TripleA-Fab 10-D10 complex |
| Reservoir | 6% (wt/vol) [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) 4000, 50 mM sodium [Acetate Buffer (Sodium Acetate)](/xray-mp-wiki/reagents/buffers/acetate/) pH 4.0, 20% (vol/vol) [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |
| Temperature | 20°C |
| Growth time | 5-10 days |
| Cryoprotection | 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) in reservoir |
| Notes | Crystals harvested after 5-10 days and flash-cooled in liquid nitrogen. Data collected at 100 K. Phases determined by molecular replacement using BEST1 WT (PDB 4RDQ) as search model. |


## Biological / Functional Insights

### Pentameric channel architecture

BEST1 forms a pentamer of five subunits symmetrically arranged around a central axis. The channel is roughly barrel-shaped with dimensions of ~70 A across and ~95 A high. Each subunit crosses the membrane four times (segments S1-S4) as alpha-helices and extended conformations. The structure resolved the debate about bestrophin stoichiometry, confirming pentameric assembly.

### Ca2+ clasp gating mechanism

Intracellular Ca2+ binds to the Ca2+ clasp, a structure formed by the S1a-S1b helix-turn-helix element and the acidic cluster at the S4a-S4b junction. The Ca2+ ligands include Asp301 and Asp304. Conformational changes near the Ca2+ clasp are coupled to dilatation of the hydrophobic neck gate. The Fab fragment specifically binds the Ca2+-bound form, suggesting Ca2+-dependent gating involves long-range conformational changes.

### Anion binding and selectivity

The pore contains at least 15 anion binding sites with five-fold symmetry, organized as three rings (sites 1-3). Anions are stabilized at the N-terminal ends of alpha-helices by positive electrostatic potential from oriented peptide dipoles. Anion-pi interactions with Phe80 and Phe84 in the neck may contribute to anion selectivity. The permeability sequence is NO3- > Br- > Cl-.

### Disease mutations in the gating apparatus

Approximately 200 mutations in human BEST1 are associated with [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) degenerative disorders including vitelliform macular dystrophy (Best's disease). Disease-causing mutations are particularly prevalent in the Ca2+ clasp (e.g., Asp301, Asp304) and the neck of the pore (e.g., Phe80, Phe84), confirming these regions as critical components of the gating apparatus.

### Hydrophobic neck gate

The hydrophobic neck near the midpoint of the membrane, lined by Ile76, Phe80 and Phe84 from each of the five S2b helices, forms the channel gate. The narrowness of the neck, its sequence conservation, and its positioning nearest to the Ca2+ binding site suggest it acts as the gate. The gate is proposed to dilate when Ca2+ is bound and seal shut when Ca2+ is absent.

### Neck functions as gate, not selectivity filter (PNAS 2016)

Electrophysiological studies of purified BEST1 channels in planar lipid bilayers demonstrated that the hydrophobic neck is the Ca2+-dependent gate, not a major determinant of ion selectivity. TripleA mutations (I76A, F80A, F84A) that widen the neck from ~3.5 Å to ~9 Å produce constitutively active channels that conduct Cl- even in the absence of Ca2+. Despite this dramatic widening, anion-vs.-cation selectivity (PK/PCl ~0.05-0.09) and the lyotropic permeability sequence (SCN- > I- > Br- > Cl-) remain unchanged, ruling out the neck as a selectivity filter. The X-ray structure of BEST1 TripleA shows that the remainder of the channel is essentially unperturbed.

### Aperture as size-selective filter (PNAS 2016)

The cytosolic aperture, formed by a ring of V205 side chains (~3 Å diameter), functions as a size-selective filter that determines relative anion permeabilities. Mutation V205A abolishes the lyotropic permeability sequence, making SCN-, I-, Br-, and Cl- equally permeant, while retaining Ca2+ dependence and anion-vs.-cation selectivity. The V205A mutant also becomes permeable to [Acetate Buffer (Sodium Acetate)](/xray-mp-wiki/reagents/buffers/acetate/), which is not detectably permeant through wild-type BEST1. These data indicate the aperture discriminates on the basis of size, not charge, permitting passage of small dehydrated anions while excluding larger molecules.

### Ca2+ clasp confirmed as intracellular Ca2+ sensor (PNAS 2016)

The Ca2+ clasp, formed by the S1a-S1b helix-turn-helix element and the acidic cluster (D301, D304) at the S4a-S4b junction, was confirmed as the intracellular Ca2+ sensor. Mutation of D301A/D304A yields channels that are constitutively closed, unable to conduct ions even at elevated Ca2+ concentrations. Combined with the TripleA mutation (which opens the neck), the D301A/D304A/TripleA quintuple mutant can be rescued to constitutively active behavior, demonstrating that the Ca2+ clasp controls the neck gate through a long-range conformational coupling.


## Cross-References

- [nhTMEM16 lipid scramblase](/xray-mp-wiki/proteins/miscellaneous/nhtmem16/) — Another family of CaCCs (TMEM16 family), distinct from bestrophins
- [Gloeobacter violaceus Ligand-gated Ion Channel (GLIC)](/xray-mp-wiki/proteins/cys-loop-receptors/glic/) — Pentameric channel used for comparison of pore architecture
- [Anion-pi interactions](/xray-mp-wiki/concepts/anion-pi-interactions/) — Proposed mechanism for anion coordination in the BEST1 pore
- [Calcium-activated Channels](/xray-mp-wiki/concepts/calcium-activated-channels/) — BEST1 belongs to the CaCC family of ion channels
- [Chloride Ion](/xray-mp-wiki/reagents/ligands/chloride-ion/) — Primary permeant anion for BEST1
- [Calcium Ion](/xray-mp-wiki/reagents/ligands/calcium-ion/) — Intracellular Ca2+ regulates channel gating
- [KpBest Bestrophin Ion Channel](/xray-mp-wiki/proteins/other-ion-channels/kpbest/) — Prokaryotic bestrophin homolog with opposite ion selectivity (cation-selective), used for comparative structure-function analysis
- [GR (Halobacterium sp. GR Bacteriorhodopsin)](/xray-mp-wiki/proteins/rhodopsins/gr/) — Related protein structure
- [nhTMEM16 (TMEM16 Lipid Scramblase from Nectria haematococca)](/xray-mp-wiki/proteins/miscellaneous/nhtmem16/) — Related protein structure
- [GLIC (Gloeobacter violaceus Ion Channel)](/xray-mp-wiki/proteins/cys-loop-receptors/glic/) — Related protein structure
