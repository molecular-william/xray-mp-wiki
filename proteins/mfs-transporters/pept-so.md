---
title: PepT_So Oligopeptide Transporter
created: 2026-05-26
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##EMBOJ.2010.309, doi/10.1016##j.str.2014.12.012, doi/10.1016##j.str.2011.04.028]
verified: false
---

# PepT_So Oligopeptide Transporter

## Overview

PepT_So is a proton-coupled oligopeptide transporter from Shewanella oneidensis. It belongs to the POT (proton-dependent oligopeptide transporter) family, a subgroup of the Major Facilitator Superfamily ([MFS](/xray-mp-wiki/concepts/major-facilitator-superfamily/)). PepT_So uses a proton gradient to drive the uptake of di- and tri-peptides and serves as a model system for understanding mammalian peptide transporters PepT1 and PepT2. The crystal structure reveals a ligand-bound occluded conformation with a central hydrophilic peptide-binding cavity and His61 as a key residue in the proton-coupling machinery.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##EMBOJ.2010.309 | 3B97 | 3.6 A | P3_2 | PepT_So from Shewanella oneidensis, wild-type, occluded conformation | unidentified dipeptide-sized ligand in central cavity |
| doi/10.1016##j.str.2014.12.012 | 4UVM | 3.0 A | P4_1 2_1 2 | PepT_So from Shewanella oneidensis, wild-type, inward-open conformation | none (apo-like) |
| doi/10.1016##j.str.2011.04.028 | 2XUT | 3.0 A | not specified | PepT_So from Shewanella oneidensis, wild-type, inward-occluded conformation | dipeptide substrate |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: PepT_So from Shewanella oneidensis, wild-type

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Cell lysis and membrane fractionation | -- | -- + -- | Wild-type PepT_So purified as described in Newstead et al., 2011 |


## Crystallization

### doi/10.1038##EMBOJ.2010.309

| Parameter | Value |
|---|---|
| Method | vapor diffusion |
| Notes | Structure solved by [MIRAS](/xray-mp-wiki/methods/structure-determination/miras/) using [Mercury (HgCl2) - Aquaporin Inhibitor](/xray-mp-wiki/reagents/additives/mercury/) derivative crystals and seleno-[L-Methionine](/xray-mp-wiki/reagents/ligands/l-methionine/) incorporated protein. Three PepT_So molecules in asymmetric unit. R-factor 27.8%, R-free 29.6%. |


## Biological / Functional Insights

### Ligand-bound occluded state of MFS transporter

The PepT_So structure captures a ligand-bound occluded conformation of an [MFS](/xray-mp-wiki/concepts/major-facilitator-superfamily/)
transporter, where both the extracellular and intracellular gates are closed,
isolating the bound peptide within a central hydrophilic cavity. This represents
a key intermediate in the [Alternating Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/), bridging the outward-facing
and inward-facing states.

### Central hydrophilic peptide-binding cavity

The peptide-binding site is located in a central hydrophilic cavity with
approximate dimensions of 13 x 12 x 11 A, sufficient to accommodate di- and
tri-peptides. The binding site is formed by residues from helices H1, H2, H4,
H5 (N-terminal bundle) and H7, H8, H10, H11 (C-terminal bundle). Conserved
positively charged residues (Arg25, Arg32, Lys127) extend into the cavity on the
N-terminal side, while Glu419 and Ser423 are located on the C-terminal side.
Hydrophobic residues (Ile157, Trp312, Phe315, Trp446) provide pockets for
peptide side chains.

### Proton-coupling machinery

His61, located near the extracellular gate of the central cavity, is proposed as
a key residue in proton-substrate coupling. Mutation of His61 to cysteine
inactivates the transporter. In the vicinity, Asp316 sits at the top of the
central cavity and interacts with Arg32 in the ligand-binding site. The
arrangement of charged residues near the extracellular gate suggests a mechanism
where protonation/deprotonation drives conformational changes.

### Asymmetric rocking motion in MFS transport

The occluded PepT_So structure suggests an asymmetric rocking motion between the
N- and C-terminal six-helix bundles, rather than a symmetrical rigid body motion.
The N-terminal helix bundle is less dynamic and more involved in peptide binding,
while the C-terminal helix bundle contains the mobile gates, likely driven by the
proton electrochemical gradient.


## Cross-References

- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/mfs-transporter/) — PepT_So belongs to the MFS of secondary active transporters
- [POT Family (Proton-Dependent Oligopeptide Transporters)](/xray-mp-wiki/concepts/pot-family/) — PepT_So is a member of the POT family within MFS
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — PepT_So captures an occluded intermediate of the alternating access cycle
- [PepT_St Proton-Dependent Oligopeptide Transporter](/xray-mp-wiki/proteins/mfs-transporters/pept-st/) — POT family member from Streptococcus thermophilus, 8 crystal structures
- [PepT_So2 Oligopeptide Transporter](/xray-mp-wiki/proteins/mfs-transporters/pept-so2/) — POT family member from Shewanella oneidensis, inward open conformation with substrate
- [MFS](/xray-mp-wiki/concepts/major-facilitator-superfamily/) — Related biological concept
- [MIRAS](/xray-mp-wiki/methods/structure-determination/miras/) — Method used in structure determination or purification
- [Mercury (HgCl2) - Aquaporin Inhibitor](/xray-mp-wiki/reagents/additives/mercury/) — Additive used in purification or crystallization buffers
- [L-Methionine](/xray-mp-wiki/reagents/ligands/l-methionine/) — Related ligand or cofactor
