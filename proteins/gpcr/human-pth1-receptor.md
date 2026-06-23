---
title: Human Parathyroid Hormone 1 Receptor (PTH1R)
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41594-018-0151-4]
verified: false
---

# Human Parathyroid Hormone 1 Receptor (PTH1R)

## Overview

The human parathyroid hormone 1 receptor (PTH1R) is a class B G-protein-coupled receptor that mediates the actions of parathyroid hormone (PTH) and parathyroid hormone-related protein (PTHrP), playing a central role in calcium homeostasis and bone metabolism. PTH1R is a major drug target for osteoporosis and hypoparathyroidism. The high-resolution crystal structure of the engineered PTH1R (PTH1R_XTAL) in complex with an engineered peptide agonist (ePTH) was determined, revealing the detailed interactions between the receptor and its ligand. The construct included deletions in the extracellular domain (ECD) and C-terminus, a PGS fusion replacing ICL3, and 10 thermostabilizing mutations from directed yeast evolution.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41594-018-0151-4 | 6HX0 | 3.00 | P 2_1 2_1 2_1 | PTH1R_XTAL (ECD-PTH1R_S-PGS fusion) with N-terminal HA signal, FLAG tag, His10 tag, 3C cleavage site; ECD deletion (61-104), C-term deletion (481-593), ICL3 (389-397) replaced by PGS fusion; 10 thermostabilising mutations from yeast evolution | ePTH (engineered PTH peptide agonist) |

## Expression and Purification

- **Expression system**: Spodoptera frugiperda Sf9 insect cells (baculovirus) and HEK293T cells
- **Construct**: PTH1R_XTAL — melittin signal peptide, FLAG epitope, His10 tag, 3C protease cleavage site, ECD-PTH1R_S-PGS with ECD deletion (61-104), C-term deletion (481-593), ICL3 (389-397) replaced by PGS
- **Notes**: Directed evolution in S. cerevisiae followed by additional thermostabilising mutations

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Baculovirus infection of Sf9 cells | — |  | Receptor expressed in Sf9 insect cells |
| Membrane preparation | Homogenization and ultracentrifugation | — |  |  |
| Solubilization | Detergent extraction | — |  |  |
| Affinity chromatography | Ni-NTA / TALON immobilized metal affinity chromatography | — |  | His10 tag purification |
| Size-exclusion chromatography | SEC | — |  | Final polishing step in LCP-compatible buffer |


## Crystallization

### doi/10.1038##s41594-018-0151-4

| Parameter | Value |
|---|---|
| Method | LCP (lipid cubic phase) |
| Protein sample | PTH1R_XTAL-ePTH complex in buffer |
| Temperature | 20 C |
| Growth time | 3-7 days |
| Notes | Crystals grew in lipidic cubic phase (monoolein-based); P2_1_2_1_2_1 space group; diffraction to ~3.0 A resolution |


## Biological / Functional Insights

### ePTH binding mode and peptide-receptor interactions

The crystal structure reveals that ePTH binds to PTH1R in a two-domain mode typical of class B GPCRs: the C-terminal helical region of ePTH (residues 15-34) interacts with the N-terminal extracellular domain (ECD), while the N-terminal region of ePTH (residues 1-14) inserts into the transmembrane helical bundle. Key interactions include hydrogen bonds between ePTH residues (Ac5c1, Aib3, E4, Hrg11, N16) and PTH1R residues (Q364^5.40, Y429^ECL3, M441^7.39, E444^7.42, Y195^1.47, R233^2.60, F288^3.36, N448^7.46), as well as hydrophobic contacts mediated by I5, L7, M8, W14, and V21. The engineered substitutions in ePTH (Ac5c1, Aib3, Q10, Hrg11, A12, W14, Nle18, Y34) increase peptide stability and binding affinity.

### Conserved W352 in ECL2 adopts distinct orientation

In the PTH1R-ePTH complex, the conserved tryptophan W352 in extracellular loop 2 (ECL2) adopts a distinct orientation compared to other class B GPCR structures (GCGR, GLP1R). Instead of positioning between TM3 and TM4, W352 packs against the peptide ligand, contributing to the orthosteric binding pocket. This unique orientation is defined by clear side chain electron density and contributes to ligand binding specificity.

### R440 stabilising mutation reduces receptor activation

The stabilising mutation R440^7.38 (Q440 in wild-type PTH1R) forms an extended hydrogen bonding network that includes E444^7.42 and the backbone oxygen of F424^6.56 at the extracellular end of helix VI. This additional hydrogen bond stabilises the top of helix VI in an inactive-like state, explaining why the Q440R mutation strongly reduces receptor activation while largely retaining ligand binding. This provides structural insight into the activation mechanism requiring conformational rearrangements at the extracellular end of helix VI.

### Jansen Metaphyseal Chondrodysplasia mutations affect HETX motif

Jansen's metaphyseal chondrodysplasia is caused by constitutively activating mutations in PTH1R. The conserved class B HETX motif (H409^6.41, E410^6.42, T411^6.43, X412^6.44) is located at the cytoplasmic end of helix VI. In the active state, T^6.42 is removed from the network due to rearrangements in TM6. The thermostabilising mutation I458^7.56A together with disease-associated I458^7.56R face toward S409^6.41 near the HETX motif. The bulky arginine sidechain of I458R clashes with helix VI in the inactive state, providing a structural rationale for constitutive activation.

### Glycosylation at N161 near the peptide binding site

The crystal structure resolved glycosylation (GlcNAc and fucose) at residue N161 of the PTH1R ECD, located in close proximity to the ePTH C-terminus. The amidated C-terminus of Y34 forms hydrogen bonds with T163 of PTH1R, rationalizing the increased binding affinity of C-terminally amidated PTH peptides. The N161D mutation showed similar binding to wild-type PTH1R (IC50 11.0 vs 13.0 nM), indicating that glycosylation at this site is not essential for ligand binding.


## Cross-References

- [Polar Network in GPCR Activation](/xray-mp-wiki/concepts/signaling-receptors/polar-network-gpcr-activation/) — The HETX motif is a conserved polar network in class B GPCRs critical for activation
- [Constitutive Active GPCR Mutations](/xray-mp-wiki/concepts/signaling-receptors/constitutive-active-gpcr-mutations/) — Jansen metaphyseal chondrodysplasia mutations cause constitutive PTH1R activation
- [GPCR Active Conformation](/xray-mp-wiki/concepts/signaling-receptors/gpcr-active-conformation/) — PTH1R-ePTH complex represents an active-state class B GPCR
- [Thermostabilization](/xray-mp-wiki/concepts/construct-design/thermostabilization/) — Directed yeast evolution and additional mutations stabilized PTH1R for crystallization
