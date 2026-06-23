---
title: Uric acid/xanthine H+ symporter UapA from Aspergillus nidulans
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms11336]
verified: false
---

# Uric acid/xanthine H+ symporter UapA from Aspergillus nidulans

## Overview

UapA from Aspergillus nidulans is a high-affinity purine/H+ symporter specific for xanthine and uric acid, belonging to the nucleobase/ascorbate transporter (NAT) family. The crystal structure of a thermostabilized construct (UapA-G411VΔ1-11) in complex with xanthine was determined at 3.7 A resolution. UapA forms a homodimer in the crystals with dimer interactions formed exclusively through the gate domain. The structure reveals UapA in an inward-facing conformation with xanthine bound to residues in the core domain. Molecular dynamics simulations suggest that Arg481 from the opposing monomer approaches the central binding cavity, creating a specificity barrier and contributing to fine-tuning substrate selectivity. Dominant negative mutant analysis is consistent with dimerization playing a key role in transport. UapA is postulated to function by an [Elevator Mechanism](/xray-mp-wiki/concepts/elevator-mechanism/) shared with other structurally homologous transporters including anion exchangers and prestin.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms11336 | 5I6C | 3.7 A | P2_1 | UapA-G411VΔ1-11 thermostabilized construct (G411V substitution, N-terminal 11 residues deleted) from A. nidulans, expressed in S. cerevisiae with C-terminal TEV-GFP-His8 tag; in complex with xanthine | xanthine |

## Expression and Purification

- **Expression system**: Saccharomyces cerevisiae
- **Construct**: UapA-G411VΔ1-11 (G411V, Δ1-11) cloned into pDDGFP vector with C-terminal TEV cleavage site followed by GFP-His8 tag; expressed in S. cerevisiae FGY217 strain under galactose induction

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane preparation | Cell disruption and membrane ultracentrifugation | not specified | not specified + not specified | S. cerevisiae cells harvested after 22 h of galactose induction. Membranes prepared by ultracentrifugation. |
| Solubilization and affinity purification | Detergent solubilization and Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | not specified | not specified + not specified | Protein solubilized from membranes and purified via GFP-His8 tag. |
| Tag cleavage and final purification | TEV protease cleavage and [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | Superdex unspecified | not specified + not specified | GFP-His8 tag removed by TEV protease cleavage before SEC. Xanthine (or 8-bromoxanthine for derivative preparation) was included throughout purification. |


## Crystallization

### doi/10.1038##ncomms11336

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | Purified UapA-G411VΔ1-11 with xanthine bound, TEV-cleaved; initial screening with MemSys/MemStart screens |
| Reservoir | 0.1% MES pH 6.5, 30% [PEG300](/xray-mp-wiki/reagents/additives/peg300/), 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 1% n-hexyl-beta-D-glucopyranoside |
| Temperature | 20 C |
| Growth time | overnight |
| Notes | Crystals showed anisotropic diffraction; best crystals diffracted to 3.5 A in strongest direction. Space group P2_1 with two molecules per asymmetric unit. Initial phases by SIRAS using TaBr-soaked crystals (overnight soak with saturating TaBr). Data collected at Diamond Light Source. Phasing with SHELX and SHARP. Refinement with PHENIX including DEN refinement, Rosetta refinement, [NCS](/xray-mp-wiki/concepts/non-crystallographic-symmetry/) averaging, and B-factor sharpening. Final R = 29.6%, Rfree = 32.7%. 8-bromoxanthine derivative used for anomalous phasing. |


## Biological / Functional Insights

### UapA structure reveals homodimer formation

UapA contains 14 transmembrane domains (TMs) organized into a 7+7 TM fold divided into a core domain (TMs 1-4 and 8-11) and a gate domain (TMs 5-7 and 12-14), similar to [Uracil:Proton Symporter UraA from Escherichia coli](/xray-mp-wiki/proteins/slc-transporters/uraA/). Unlike [Uracil:Proton Symporter UraA from Escherichia coli](/xray-mp-wiki/proteins/slc-transporters/uraA/) which was observed as a monomer, UapA forms a dimer in the crystals with interactions exclusively through the gate domain. The extracellular loop between TMs 3 and 4 contains a disulphide bond (Cys174-Cys185) highly conserved in fungi; mutation of either residue causes marked reduction in expression and membrane sorting.

### Substrate binding site

Xanthine binds to residues in the core domain. The binding site involves Glu356, Gln408, Ala407, Phe155, Val153, and Phe406. Key contacts include the amide N of Phe155 with N9 of xanthine, Glu356 with N7-H, Gln408 with N1-H and C2=O, and the amide N of Ala407 with C6=O. Phe155 and Phe406 provide aromatic packing around the xanthine.

### Arg481 from opposing monomer contributes to specificity

Molecular dynamics simulations suggest that Arg481 from the opposite monomer approaches the central binding cavity, creating a specificity barrier on the pathway to the cytoplasm. Arg481 is the most commonly mutated residue in genetic selection experiments that alter substrate specificity. The simulations show xanthine forms transient H-bond and pi-pi stacking interactions with Arg481 before moving to the cytosol.

### Dominant negative mutations support functional dimerization

Co-expression of wild-type UapA with transport-deficient mutants (G411V, Q408P, N409D, Q408E) results in dominant negative effects, reducing xanthine uptake compared to wild-type alone. This suggests that one subunit influences the transport function of the other, consistent with dimerization playing a direct role in transport rather than just trafficking.

### Postulated elevator transport mechanism

Based on structural homology with [Uracil:Proton Symporter UraA from Escherichia coli](/xray-mp-wiki/proteins/slc-transporters/uraA/), anion exchanger 1 (AE1), and SLC26 transporters, UapA is proposed to function by an [Elevator Mechanism](/xray-mp-wiki/concepts/elevator-mechanism/). The core domain containing the substrate-binding site moves relative to the fixed gate domain, effectively carrying xanthine across the membrane. The G411V mutation (which sterically hinders core domain sliding) retains binding but abolishes transport, consistent with this mechanism.


## Cross-References

- [Uracil:Proton Symporter UraA from Escherichia coli](/xray-mp-wiki/proteins/slc-transporters/uraA/) — Homologous NAT/NCS2 family transporter with the same 7+7 TM fold
- [Elevator Mechanism](/xray-mp-wiki/concepts/elevator-mechanism/) — UapA proposed to function via elevator mechanism based on structural homology
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — Elevator mechanism is a specific variant of alternating access
- [Rocker-Switch Mechanism](/xray-mp-wiki/concepts/rocker-switch-mechanism/) — Related alternating-access mechanism; gate domain motions contribute to transport
- [NCS](/xray-mp-wiki/concepts/non-crystallographic-symmetry/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Method used in structure determination or purification
- [PEG300](/xray-mp-wiki/reagents/additives/peg300/) — Additive used in purification or crystallization buffers
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used in purification or crystallization
