---
title: "Yarrowia lipolytica F1Fo-ATP Synthase"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##J.MOLCEL.2016.05.037]
verified: false
---

# Yarrowia lipolytica F1Fo-ATP Synthase

## Overview

The F1Fo-ATP synthase from the strictly aerobic yeast Yarrowia lipolytica is a rotary ATP synthase that produces most of the cellular ATP. The complete, dimeric structure was determined by a combination of [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) and X-ray crystallography. The X-ray structure of the inhibitor-free F1c10 subcomplex (PDB 5FL7) was solved at 3.5 A resolution, revealing the three conformational states of the alpha/beta heterodimers with bound nucleotides. The [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) structure of the full 58-subunit dimer at 6.2-7.8 A resolution provided insights into the arrangement of the Fo stator subunits and the structural basis of cristae formation.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##J.MOLCEL.2016.05.037 | 5FL7 | 3.5 A | P2_12_12 | Yarrowia lipolytica F1c10 subcomplex (inhibitor-free) | Mg-ATP, Mg-ADP |

## Expression and Purification

- **Expression system**: Yarrowia lipolytica (yeast)
- **Construct**: Full F1Fo-ATP synthase (dimer) and F1c10 subcomplex

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| ATP synthase dimer purification | [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) gradient centrifugation, anion exchange, and gel filtration | -- | Not specified + Not specified | ATP synthase dimers fully competent for oligomycin-sensitive ATP hydrolysis were purified from Y. lipolytica cultures. Crystals of the F1c10 subcomplex were grown from concentrated samples of the monomer. |


## Crystallization

### doi/10.1016##J.MOLCEL.2016.05.037

| Parameter | Value |
|---|---|
| Method | Crystallization of F1c10 subcomplex |
| Protein sample | Concentrated Y. lipolytica F1c10 |
| Reservoir | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | X-ray data collected at Swiss Light Source beamline PX-II X10SA. Structure determined by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) with a model based on S. cerevisiae F1c10 complex (PDB 2XOK). Resolution 3.5 A, space group P2_12_12 with cell dimensions 169.5, 182.2, 193.0 A. Rwork/Rfree = 27.39/30.54%. The structure contains 30,123 atoms (29,954 protein, 152 ligands, 17 water). RMSD bond lengths 0.006 A, bond angles 0.883 degrees. |


## Biological / Functional Insights

### Rotational states of F1 reveal post-hydrolysis conformation

The three conformational states of the alpha/beta heterodimers are very similar to S. cerevisiae F1 (RMSD below 1.7 A). The gamma subunit is in a post-hydrolysis position, consistent with the presence of bound Mg-ADP in the catalytic beta_DP and beta_TP sites. The beta_E site is empty. The ADP in the Y. lipolytica beta_DP at this late hydrolysis stage without nucleotide-stabilizing azide is surprising, indicating a higher nucleotide affinity of this site.

### Peripheral stalk architecture and stator arrangement

The peripheral stalk consists of subunits b, d, h, and OSCP. The overall curvature differs from the bovine crystal structure but resembles the [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) map of the monomeric bovine complex. The N terminus of the alpha_DP subunit forms a previously unrecognized four-helix bundle with b, h, and the C terminus of OSCP, bonding the F1 head to the peripheral stalk.

### Fo stator subunit assignment

Six vertical transmembrane helices and four horizontal helices were assigned to stator subunits a, b, f, i, and 8. Subunit a contains a long horizontal hairpin (aH5/aH6, ~70 A) in contact with 3-4 c-ring subunits, and a distal hairpin (aH3/aH4, ~45 and ~35 A). The conserved Arg182 in aH5 is essential for proton translocation. Subunit 8 (A6L in human) derives from a bacterial b subunit ancestor. Subunit f mediates direct protein contact between the two monomers on the IMS side.

### Subunits e and g induce membrane curvature for cristae formation

Comparison of the dimer map with the monomer map (which lacks subunits e, g, and k) revealed that subunits e and g occupy a triangular density at the dimer interface. They induce a ~100 degree membrane bend that is the structural basis of cristae formation. In the monomer without e and g, the detergent belt is straight. In the bovine monomer (which has e and g), the bend is ~50 degrees. This demonstrates that e and g are chiefly responsible for the membrane curvature that results in mitochondrial cristae morphology.

### Aqueous half-channels for proton translocation

Two aqueous half-channels at the subunit a/c-ring interface conduct protons to and from the c-ring protonation sites. The conserved charged and polar residues of aH5 (starting with Glu168, four helix turns upstream of Arg182) create a hydrophilic environment. The lumenal half-channel near the hairpin loop and the matrix half-channel at the C terminus of subunit a are laterally offset. The essential Arg182 allows only deprotonated c subunit glutamate side chains to pass.


## Cross-References

- [Rotary ATPase Mechanism](/xray-mp-wiki/concepts/enzyme-mechanisms/rotary-atpase-mechanism/) — ATP synthase operates by rotary catalysis
- [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) — Primary structure determination method for the full dimer; combined with X-ray crystallography
- [ATP](/xray-mp-wiki/reagents/ligands/atp/) — Main product of the ATP synthase
- [ADP](/xray-mp-wiki/reagents/ligands/adp/) — Substrate for ATP synthesis; found in the X-ray structure
- [Magnesium Chloride](/xray-mp-wiki/reagents/additives/magnesium-chloride/) — Mg2+ ions coordinated with bound nucleotides
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
