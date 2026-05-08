---
title: hiGlpG (Haemophilus influenzae Rhomboid Protease)
created: 2026-05-07
updated: 2026-05-07
type: protein
category: proteins
layout: default
tags: [rhomboid, protease, membrane-protein, intramembrane-cleavage, serine-protease]
sources: [doi/10.1016##j.jmb.2011.01.046]
---

# hiGlpG (Haemophilus influenzae Rhomboid Protease)

## Overview

hiGlpG is the rhomboid intramembrane protease from Haemophilus influenzae, a 7-TM membrane protein belonging to the serine protease family. The structure (PDB 3ODJ) revealed disorder in loop 4, helix 5, and loop 5, identifying these as mobile elements of the substrate gate. Mutagenesis demonstrated that flexibility in loop 5 and helix 5 is required for substrate access, while loop 4 must remain relatively rigid. The structure supports a si-face cleavage mechanism for rhomboid proteases.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2011.01.046 | 3ODJ | 2.85 A | C2 | Native hiGlpG from H. influenzae (residues 1-164, missing 134-164 due to disorder) | None |

## Expression and Purification

- **Expression system**: Escherichia coli (Top10 cells)
- **Construct**: hiGlpG in pBAD-Myc-HisA vector with Myc-His tag

### Purification Workflow

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Crude membrane isolation | High-speed ultracentrifugation | -- | LB media with ampicillin | Membrane fraction isolated from induced cells |
| Solubilization | Detergent solubilization | -- | 1% dodecylmaltoside (DDM) | Solubilized in 1% DDM from Anatrace |
| Affinity purification | Ni-NTA chromatography | Ni-NTA | DDM-containing buffer | His-tag purification followed by thrombin cleavage (30 U/mg GlpG, 1 h, RT) |
| Gel filtration | Superdex 200 size-exclusion chromatography | Superdex 200 | 50 mM Tris, 200 mM NaCl, 0.005% AnaPOE C12E8, 20% glycerol, 0.5 mM EDTA (pH 8.0) | Final purification step; concentrated to 10-15 mg/ml using Millipore Amicon 30 kDa cutoff |


## Crystallization

### doi/10.1016##j.jmb.2011.01.046

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (hanging or sitting drop) |
| Protein sample | hiGlpG at 10-15 mg/ml in 50 mM Tris, 200 mM NaCl, 0.005% AnaPOE C12E8, 20% glycerol, 0.5 mM EDTA (pH 8.0) |
| Reservoir | not specified |
| Mixing ratio | not specified |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | not specified |
| Notes | Crystals diffracted to 2.85 A, space group C2. Disorder in residues 134-164 (loop 4, helix 5, loop 5) observed across multiple data sets (150+ crystals searched). Data collected at ALS beamline 8.3.1. |


## Biological / Functional Insights

### Substrate gating by loop 4, helix 5, and loop 5 flexibility

The hiGlpG structure revealed persistent disorder in loop 4 (L4), helix 5 (H5), and loop 5 (L5) across multiple crystal forms. Mutagenesis showed that L5 and H5 flexibility is essential for substrate access: F160A and M164A (L5) retained 46-60% activity, while L136A and F137A (L4) dropped to 5-22%. Disrupting H2-H5 hydrophobic contacts (W72A+F76A+F144A) increased activity 2.5-fold, suggesting the gate opens more readily. Loop 4 requires structural rigidity for proper substrate positioning.

### si-face cleavage mechanism

The structural evidence for substrate gating via helix 5 movements, combined with the active-site geometry, predicts that rhomboid cleavage occurs on the si-face of the scissile peptide bond (rather than the re-face typical of soluble serine proteases). The oxyanion hole is composed of the main-chain NH from Ser116 and the protonated N-epsilon from His65. This si-face mechanism is shared with other serine peptidases having a Ser-Lys catalytic dyad, including signal peptidase (SPase) and Lon protease.

### Comparison with ecGlpG gating

hiGlpG differs from E. coli GlpG (ecGlpG) in the intramolecular connections between helix 5 and helix 2: in hiGlpG, helix 5 is partially unwound and tilted, while in ecGlpG it runs parallel to helix 2. Despite these differences, both rhomboids show comparable gating mechanisms with subtle variations. The disorder in L4/H5/L5 is a common feature of the rhomboid family, indicating conserved substrate access dynamics.


## Cross-References

- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary solubilization detergent for hiGlpG membrane extraction
- [Rhomboid Protease Family](/xray-mp-wiki/concepts/rhomboid-protease/) — hiGlpG is a member of the rhomboid intramembrane protease family
- [Intramembrane Proteolysis](/xray-mp-wiki/concepts/intramembrane-proteolysis/) — hiGlpG cleaves transmembrane substrates within the lipid bilayer
- [Tris Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Primary buffer component (50 mM, pH 8.0) for purification and crystallization
