---
title: Human ABCB10 Mitochondrial ATP-Binding Cassette Transporter
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1073##pnas.1217042110]
verified: false
---

# Human ABCB10 Mitochondrial ATP-Binding Cassette Transporter

## Overview

ABCB10 is a human [ATP](/xray-mp-wiki/reagents/ligands/atp/)-binding cassette (ABC) transporter found in the inner mitochondrial membrane. It is a homodimeric half transporter essential for erythropoiesis and protection against mitochondrial oxidative stress. ABCB10 adopts an exporter fold with six transmembrane helices per monomer and a C-terminal nucleotide-binding domain (NBD). Its crystal structures in apo- and nucleotide-bound states reveal an unexpected open-inwards conformation with bound [ATP](/xray-mp-wiki/reagents/ligands/atp/) analogs, suggesting that nucleotide binding can occur before transport substrate binding.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1217042110 |  | 2.90 |  | ABCB10 with N-terminal mitochondrial targeting presequence removed (N-terminal 151 residues or residues 6-126 deleted) | [AMPPCP (Adenosine 5'-[beta,gamma-methylene]triphosphate)](/xray-mp-wiki/reagents/amppcp/) |
| doi/10.1073##pnas.1217042110 |  | 3.30 |  | ABCB10 with N-terminal mTP removed | AMPPNP |
| doi/10.1073##pnas.1217042110 |  |  |  | ABCB10 apo |  |

## Expression and Purification

- **Expression system**: Sf9 insect cells (baculovirus); ABCB10 expressed with both N- and C-terminal His-tags, with mitochondrial targeting presequence removed (deletion of N-terminal 151 residues or residues 6-126)


### Purification Workflow

- **Expression system**: Sf9 insect cells (baculovirus)
- **Expression construct**: ABCB10 with mTP removed, N- and C-terminal His-tags
- **Tag info**: N- and C-terminal His-tags

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Extraction | Detergent extraction | — | 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) (dodecyl maltoside) | Purified in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) with addition of either CHS (cholesteryl-hemisuccinate) or CDL (cardiolipin) |
| Affinity chromatography | Cobalt affinity | Cobalt affinity resin |  | Standard immobilized metal affinity chromatography |
| Size-exclusion chromatography | SEC | — |  | Final polishing step in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) with CHS or CDL |


## Crystallization

### doi/10.1073##pnas.1217042110

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (sitting drop) |
| Protein sample | ABCB10 purified in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + CHS or [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + CDL |
| Temperature | 20 |
| Notes | Plate-form crystals grown with AMPPNP; rod-form crystals grown with [AMPPCP (Adenosine 5'-[beta,gamma-methylene]triphosphate)](/xray-mp-wiki/reagents/amppcp/) from protein purified with CDL. Diffraction data collected at Diamond Light Source beamline I24. |


## Biological / Functional Insights

### Open-inwards conformation with bound nucleotide

Unlike other ABC transporters that adopt open-outwards conformations when bound to [ATP](/xray-mp-wiki/reagents/ligands/atp/) analogs, ABCB10 remains in an open-inwards conformation with separated NBDs. Four structures (apo, AMPPNP-bound, two [AMPPCP (Adenosine 5'-[beta,gamma-methylene]triphosphate)](/xray-mp-wiki/reagents/amppcp/)-bound) all show inward-facing states with varying degrees of NBD separation. Refinement confirms 80-100% nucleotide occupancy in both nucleotide binding sites, demonstrating that [ATP](/xray-mp-wiki/reagents/ligands/atp/) can bind to both NBDs without triggering the conformational change to open-outwards state.

### Portal between TMH1 and TMH2 for substrate entry

The ABCB10 structures reveal a portal between transmembrane helices TMH1 and TMH2 that connects the central cavity to the membrane environment. This portal is occupied by [Cardiolipin](/xray-mp-wiki/reagents/cardiolipin/) in rod-form crystals and is partially open or closed depending on crystal form. The portal may serve as an entry route for amphipathic transport substrates into the substrate-binding cavity.

### Implications for ABC transporter mechanism

The ABCB10 structures support an adaptation of the [ATP](/xray-mp-wiki/reagents/ligands/atp/) switch model where either nucleotide or transport substrate can bind first to the open-inwards conformation. Binding of transport substrate likely promotes NBD closure and transition to the open-outwards conformation, explaining the stimulation of ATPase activity by substrates. The basal ATPase activity of ABCB10 (Km_app ~0.2 mM) is consistent with nucleotide binding occurring in the absence of transport substrate.


## Cross-References

- [Mouse P-glycoprotein (Pgp, ABCB1)](/xray-mp-wiki/proteins/abc-transporters/mouse-p-glycoprotein/) — Homologous ABC exporter with similar fold; comparison of open-inwards vs open-outwards conformations
- [Sav1866 Multidrug ABC Transporter](/xray-mp-wiki/proteins/abc-transporters/sav1866/) — Bacterial ABC exporter in open-outwards conformation; key structural comparator
- [TM287/288 (ABC Exporter from Thermotoga maritima)](/xray-mp-wiki/proteins/abc-transporters/tm287-288/) — ABC exporter with intermediate open-inwards and AMPPNP-bound conformations
- [Aquaporin Family](/xray-mp-wiki/concepts/aquaporin/) — Key concept related to this protein
- [GR (Halobacterium sp. GR Bacteriorhodopsin)](/xray-mp-wiki/proteins/rhodopsins/gr/) — Related protein mentioned in the study
- [Mouse P-glycoprotein](/xray-mp-wiki/proteins/abc-transporters/mouse-p-glycoprotein/) — Related protein mentioned in the study
- [Sav1866 Multidrug ABC Transporter](/xray-mp-wiki/proteins/abc-transporters/sav1866/) — Related protein mentioned in the study
- [TM287/288 Heterodimeric ABC Exporter from Thermotoga maritima](/xray-mp-wiki/proteins/abc-transporters/tm287-288/) — Related protein mentioned in the study
- [ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel)](/xray-mp-wiki/proteins/cys-loop-receptors/elic/) — Related protein mentioned in the study
- [Cardiolipin](/xray-mp-wiki/reagents/cardiolipin/) — Lipid additive for stabilization
