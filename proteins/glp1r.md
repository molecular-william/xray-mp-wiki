---
title: Human Glucagon-Like Peptide-1 Receptor (GLP-1R)
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature22800]
verified: false
---

# Human Glucagon-Like Peptide-1 Receptor (GLP-1R)

## Overview

The human glucagon-like peptide-1 receptor (GLP-1R, UniProt P48684) is a class B G-protein-coupled receptor (GPCR) that binds the incretin hormone GLP-1 and mediates glucose-dependent insulin secretion from pancreatic beta cells. GLP-1R is expressed on pancreatic islets, as well as in the heart, gastrointestinal tract, and brain. It has a multi-domain architecture consisting of a large extracellular domain (ECD) required for binding the C-terminal portion of the GLP-1 peptide and a transmembrane domain (TMD) with seven transmembrane helices (TM1-TM7) that binds the N-terminal portion of the peptide. GLP-1R is a therapeutic target for type 2 diabetes, with several GLP-1 agonists approved for clinical use.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature22800 | 5NX2 | 3.7 | P3.21 | Full-length GLP-1R StaR (T207E, Q211A, D215R, L232F, G295A, T298A, C329A, P358A, G361A, H363V, V405A) bound to peptide 5 (truncated nonapeptide agonist)
 | peptide 5 |

## Expression and Purification

- **Expression system**: HEK293T cells
- **Construct**: Full-length human GLP-1R with thermostabilizing mutations (StaR: T207E, Q211A, D215R, L232F, G295A, T298A, C329A, P358A, G361A, H363V, V405A)

- **Notes**: Transient transfection. Residues 24-28 (N terminus) and 418-432 (C terminus) are not resolved in the crystal structure.


### Purification Workflow

- **Expression system**: HEK293T cells
- **Expression construct**: Full-length human GLP-1R StaR (T207E, Q211A, D215R, L232F, G295A, T298A, C329A, P358A, G361A, H363V, V405A)


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Transient transfection | -- | DMEM + 10% FBS + -- | HEK293T cells transfected and harvested after 48 h |
| Solubilization | Detergent solubilization | -- | 50 mM HEPES pH 7.5, 150 mM NaCl + 0.02% n-dodecyl-beta-D-maltopyranoside (DDM) | StaR generated using scanning mutagenesis approach. Solubilized in DDM supplemented with cholesteryl hemisuccinate (CHS)
 |


## Crystallization

### doi/10.1038##nature22800

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | GLP-1R StaR complexed with peptide 5 (truncated GLP-1 agonist nonapeptide)
 |
| Temperature | 20 |
| Growth time | Not specified |
| Notes | 8 crystals used. Space group P3.21. Cell dimensions: a=94.44, b=94.44, c=163.9 A; alpha=90, beta=90, gamma=120. Resolution 54.63-3.7 A (shell: 4.05-3.70). Rwork/Rfree: 0.285/0.334. 3,409 atoms (3,242 protein, 107 ligand, 60 others). Continuous electron density for all intra- and extracellular loops. Peptide 5 retains alpha-helical conformation deep within the receptor-binding pocket with contact surface area of 1,584 A^2. ECL1 forms a short helix-turn-helix and extends outward to contact the ECD. TM2 exhibits an extended helical structure. ECL2 is retracted. Arrangement of TMs reveals hallmarks of active conformation similar to class A receptors. |


## Biological / Functional Insights

### Active Conformation of Class B GPCR

The GLP-1R structure reveals hallmarks of an active conformation similar to that
observed in class A GPCRs. The extracellular ends of TM1, TM6, and TM7 are rotated
clockwise around the central TMD axis compared to GCGR (4.7, 5.1, and 3.4 A,
respectively) and CRF1R (7.4, 10.6, and 10.9 A). TM2 exhibits an extended helical
structure ending at residue S206, where the helix unwinds and then forms a short
alpha-helix between residues W214 and L217. This extended conformation of TM2
positions ECL1 upwards and further into the extracellular space where it interacts
with the ECD (residues E207-W214 of ECL1 and E127-R131 of the ECD). ECL2 is
retracted, adopting a conformation similar to CRF1R, in contrast to GCGR where
ECL2 stretches across the central axis mediating interactions from TM3 to TM6 and
TM7.

### Peptide Agonist Binding Pocket

Peptide 5 binds deep within the intra-helical cavity of GLP-1R with its N terminus
deepest in the binding pocket and C terminus directed towards the ECD. The peptide
retains an alpha-helical conformation. The contact surface area between peptide 5
and the receptor is 1,584 A^2. The amide of the Cap1 modification interacts with
E387(7.42b), which interacts with K383(7.38b). The gem-dimethyl group of Cap1
(substituting for A8) sits in a hydrophobic pocket lined by L384(7.39b) and
L388(7.43b). The C-linked tetrazolyl-Ala (C-tet-Ala) at position 9, the alpha-methyl-o-fluoro-Phe
at position 12 (X1), the 3-(4'-methoxy-2'-ethyl[1,1'-biphenyl]-4-yl)-L-alanine
at position 16 (X2), and the 5-(3,5-dimethylphenyl)-L-norvaline at position 17
(X3) form energetically favourable interactions with lipophilic hotspots on GLP-1R.
The X2 and X3 groups exit the binding site through the hydrophobic groove between
TM1 and TM2, providing a rationale for high affinity in the absence of ECD
interaction.

### Comparison to Related Class B GPCRs

Superposition of the TMD (TM1-TM7) of GLP-1R with GCGR (PDB 5EE7) and CRF1R
(PDB 4K5Y) yields RMSD values of 2.7 A and 3.4 A, respectively. Considerable
differences are observed between the extracellular surfaces of these three
receptors. The ECD of GLP-1R adopts the same fold as previously reported for the
isolated domain (PDB 3IOL) with an RMSD of 0.93 A for main-chain atoms, connected
to TM1 by a ten-residue linker. Unlike the glucagon receptor, no helical stalk
linking ECD and TMD is observed. The V-shaped central cavity is similar to other
class B GPCRs.


## Cross-References

- [Exendin-4](/xray-mp-wiki/reagents/ligands/exendin-4/) — Reference GLP-1R agonist used for binding assays and in vivo comparison
- [Human Glucagon Receptor (GCGR)](/xray-mp-wiki/proteins/gcgr/) — Related class B GPCR, structural comparison (PDB 5EE7)
- [Human CRF1R StaR-T4L](/xray-mp-wiki/proteins/crf1r-star-t4l/) — Related class B GPCR, structural comparison (PDB 4K5Y)
- [Protein Thermostabilization](/xray-mp-wiki/concepts/thermostabilization/) — StaR construct uses thermostabilization via scanning mutagenesis
- [GPCR Active Conformation](/xray-mp-wiki/concepts/gpcr-active-conformation/) — GLP-1R structure reveals hallmarks of active conformation
