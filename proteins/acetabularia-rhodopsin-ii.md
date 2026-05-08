---
title: Acetabularia Rhodopsin II (ARII)
created: 2026-05-07
updated: 2026-05-07
type: protein
category: proteins
layout: default
tags: [rhodopsin, membrane-protein, proton-pump, microbial-rhodopsin, seven-tm, eukaryotic]
sources: [doi/10.1016##j.jmb.2011.06.028]
---

# Acetabularia Rhodopsin II (ARII)

## Overview

Acetabularia rhodopsin II (ARII) is a light-driven proton pump from the marine alga Acetabularia acetabulum, representing the first eukaryotic member of the microbial rhodopsin family. ARII is a 247-residue protein with seven transmembrane helices and an all-trans retinal chromophore bound to Lys211. The structure (PDB 3AM6) at 3.2 A resolution reveals a proton transfer pathway with reversed proton release/uptake timing compared to bacteriorhodopsin: proton uptake from the cytoplasmic side occurs first, followed by release to the extracellular side. Key residues include Asp81 (proton acceptor), Asp92 (proton donor), Arg78, Glu199, and Ser189 (non-dissociable, causing late proton release).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2011.06.028 | 3AM6 | 3.2 A | P212121 | ARII from Acetabularia acetabulum (247 residues, N11-tagged, tag not removed) | all-trans retinal, 8 cholesterol molecules (4 per monomer, intermolecular) |

## Expression and Purification

- **Expression system**: E. coli cell-free protein synthesis system
- **Construct**: ARII synthesized in presence of 0.4% digitonin and 6.7 mg/ml phosphatidylcholine

### Purification Workflow

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Ni2+ chelating affinity chromatography | Ni2+ affinity | Ni2+ chelating resin | 20 mM Tris-HCl (pH 7.0), 400 mM NaCl, 1 mM DTT, 10% glycerol, 0.01% DDM | N11-tagged ARII purified; tag not removed |
| Gel filtration | Size-exclusion chromatography | Not specified | 20 mM Tris-HCl (pH 7.0), 400 mM NaCl, 1 mM DTT, 10% glycerol, 0.01% DDM | Final concentration to 45.4 mg/ml using filter unit |


## Crystallization

### doi/10.1016##j.jmb.2011.06.028

| Parameter | Value |
|---|---|
| Method | In meso crystallization (lipidic mesophase) |
| Protein sample | ARII at 45.4 mg/ml |
| Reservoir | not specified |
| Mixing ratio | not specified |
| Temperature | 20 C |
| Growth time | 2 weeks |
| Cryoprotection | not specified |
| Notes | Reddish-purple plate-like crystals (100 x 100 x 10 micrometers) grew within 2 weeks at 20 C. Four ARII monomers with eight cholesterol molecules in asymmetric unit. Cholesterol molecules located between helices A and G of adjacent monomers, stabilizing overlaid planar layers. |


## Biological / Functional Insights

### Reversed proton release/uptake sequence

Unlike bacteriorhodopsin (release then uptake), ARII exhibits reversed proton transfer: proton uptake from the cytoplasmic side occurs first, followed by release to the extracellular side. This is evidenced by ITO transparent electrode measurements showing downward voltage shift (proton uptake) preceding the upward shift (release). The proton uptake occurs with O intermediate formation, and release with O intermediate decay. The reversed sequence is attributed to Ser189 (vs Glu194 in BR, which serves as the proton-releasing group) and different pKa of Glu199 (vs Glu204 in BR).

### Cys218 role in proton uptake

The side chain of Cys218 in ARII (corresponding to Leu223 in BR, Ser217 in ASR) is positioned near Asp92 and may form a low-barrier hydrogen bond with it. This interaction is proposed to facilitate proton uptake from the cytoplasmic side. Mutant studies of Cys218 indicate its involvement with the proton-donor residue Asp92.

### Eukaryotic microbial rhodopsin

ARII is the first crystal structure of a eukaryotic microbial rhodopsin. It shares 33% sequence identity with bacteriorhodopsin and 56% with ARI (the other opsin from the same organism). ARII lacks light-dark adaptation (unlike BR), maintaining predominantly all-trans retinal in the dark. The structure is highly similar to BR (Dali Z-score 28.9), with conserved proton transfer residues: Asp81 (Asp85BR), Asp92 (Asp96BR), Arg78 (Arg82BR), Glu199 (Glu204BR), and Asp207 (Asp212BR).


## Cross-References

- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Primary lipid for in meso crystallization
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Used at 0.01% during purification and 0.05% in spectroscopic assays
- [Tris Buffer](/xray-mp-wiki/reagents/buffers/tris/) — 20 mM Tris-HCl (pH 7.0) used for purification and cell-free synthesis
- [Rhodopsin Photocycle](/xray-mp-wiki/concepts/rhodopsin-photocycle/) — ARII follows the BR-type photocycle (K, L, M, N, O intermediates)
