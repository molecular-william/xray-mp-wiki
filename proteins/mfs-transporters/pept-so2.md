---
title: PepT_So2 Oligopeptide Transporter
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##embor.2013.107, doi/10.1038##nsmb.2860]
verified: false
---

# PepT_So2 Oligopeptide Transporter

## Overview

PepT_So2 is a proton-dependent oligopeptide transporter from Shewanella oneidensis. It belongs to the POT (proton-dependent oligopeptide transporter) family, a subgroup of the Major Facilitator Superfamily ([MFS](/xray-mp-wiki/concepts/protein-families/major-facilitator-superfamily/)). PepT_So2 uses a proton gradient to drive the uptake of di- and tri-peptides. The crystal structure reveals an inward open conformation with a central hydrophilic peptide-binding cavity and the first substrate-bound POT structure characterized. PepT_So2 uniquely forms a tetrameric assembly in detergent solution, distinguishing it from other POT family members.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##embor.2013.107 | not specified in paper | 3.2 A | P2_1 2_1 2_1 | Full-length PepT_So2 from Shewanella oneidensis, wild-type, inward open conformation, co-crystallized with [Alafosfalin](/xray-mp-wiki/reagents/ligands/alafosfalin/) | [Alafosfalin](/xray-mp-wiki/reagents/ligands/alafosfalin/) (peptidomimetic phosphonodipeptide) |
| doi/10.1038##embor.2013.107 | not specified in paper | 4.6 A | P3_1 2 1 | Full-length PepT_So2 from Shewanella oneidensis, wild-type, tetrameric assembly | none (crystal form without zinc, showing tetrameric arrangement) |
| doi/10.1038##nsmb.2860 | 4TPJ | 3.2 A | P2_1 2_1 2_1 | Full-length PepT_So2 from Shewanella oneidensis, wild-type, inward open conformation, co-crystallized with Ala-Ala-Ala ([AAA](/xray-mp-wiki/reagents/ligands/aaa/)) tripeptide | Ala-Ala-Ala ([AAA](/xray-mp-wiki/reagents/ligands/aaa/)) tripeptide |
| doi/10.1038##nsmb.2860 | 4TPG | 3.91 A | P2_1 2_1 2_1 | Full-length PepT_So2 from Shewanella oneidensis, wild-type, inward open conformation, co-crystallized with Ala-Tyr(L-3,5-diBr)-Ala (AY(Br)A) tripeptide | Ala-Tyr(L-3,5-diBr)-Ala (AY(Br)A) tripeptide |
| doi/10.1038##nsmb.2860 | 4TPH | 3.16 A | P2_1 2_1 2_1 | Full-length PepT_So2 from Shewanella oneidensis, wild-type, inward open conformation, co-crystallized with Ala-Tyr(L-3,5-diBr) (AY(Br)) dipeptide | Ala-Tyr(L-3,5-diBr) (AY(Br)) dipeptide |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Full-length PepT_So2 from Shewanella oneidensis (Q8EHE6), C-terminal His-tag with tobacco etch virus (TEV) cleavage site, cloned into pNIC-CTHF-vector

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Cell lysis and membrane fractionation | -- | -- + -- | Full-length PepT_So2 expressed in E. coli with C-terminal His-tag |
| Affinity purification | Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA | -- + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | His-tag purification with TEV cleavage site for tag removal |
| Size-exclusion chromatography | Size-exclusion chromatography | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | -- + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Tetrameric state confirmed by analytical gel filtration and Blue Native PAGE |


## Crystallization

### doi/10.1038##embor.2013.107

| Parameter | Value |
|---|---|
| Method | vapor diffusion, sitting drop |
| Notes | Native crystals grew in 40% [PEG](/xray-mp-wiki/reagents/additives/peg/) 300, 0.1 M phosphate [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) pH 4.5, 0.12 M ZnCl2 and 3% trimethylamine N-oxide dehydrate pH 11 at 20 C. Crystals appeared after 21 days with dimensions of approximately 100 x 50 x 10 um. PepT_So2 was incubated with 50 mM [Alafosfalin](/xray-mp-wiki/reagents/ligands/alafosfalin/) for 30 min at 4 C before crystallization. Seleno-[L-Methionine](/xray-mp-wiki/reagents/ligands/l-methionine/) crystals grew in 38% [PEG](/xray-mp-wiki/reagents/additives/peg/) 300, 0.1 M phosphate [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) pH 5.2 and 0.01 M ZnCl2. P3_1 2_1 crystal form grew in 0.1 M citric acid pH 4.2, 0.1 M sodium hydrogen phosphate and 40% [PEG](/xray-mp-wiki/reagents/additives/peg/) 300. |


## Biological / Functional Insights

### First substrate-bound POT structure

This is the first POT transporter structure solved in complex with a substrate.
[Alafosfalin](/xray-mp-wiki/reagents/ligands/alafosfalin/) binds in the central hydrophilic cavity with its N-terminal amine group
interacting with Asn151, Asn329 and Glu402, while its phosphonate moiety forms a
hydrogen bond with Tyr29 and a salt bridge with Arg25. The principle binding mode
is consistent with mutagenesis data on PEPT1, PepT_So, PepT_St, and two E. coli
transporters, indicating conserved substrate recognition across the POT family.

### Substrate-binding pocket architecture

The substrate-binding site is located in a hydrophilic cavity at the center of
the cytoplasmic crevice, formed by helices H1, H2, H4, H5 from the N-terminal
bundle and H7, H8, H10, H11 from the C-terminal bundle. A cluster of conserved
tyrosine residues (Tyr29, Tyr147, Tyr291) points toward the cavity center and
mediates interactions with peptide backbone CO- and NH-groups, enabling broad
substrate specificity. Arg25 and Glu402 are key residues for C-terminus
coordination, while Asn151, Asn329 and Tyr29 coordinate the N-terminus.

### Tetrameric assembly

Unlike other POT family members that are monomeric, PepT_So2 forms a homo-tetramer
in detergent solution as demonstrated by analytical gel filtration, Blue Native PAGE,
cross-linking, and negative stain electron microscopy. The tetramer has approximate
dimensions of 12.4 x 12.4 nm. The P3_1 2_1 crystal form shows a tetrameric
assembly in the crystal lattice, with TM12 mediating key interactions between
monomers. The P2_1 2_1 2_1 crystal form shows a dimer interface stabilized by
zinc ions, likely a crystal-packing artifact.

### Gating mechanism in inward open conformation

In the inward open conformation, the N- and C-terminal bundles interact tightly
at the periplasmic side, while a large central hydrophilic crevice faces the
intracellular side. The gating mechanism involves two conserved interaction
networks: a salt bridge between H2 and H7 (Asp47 and Arg304 in PepT_So2) and
a hydrogen bond network between H5 and H8 (Lys165, Asp166, Ser321). Tyr37
plays a key role in sealing the N- and C-terminal bundle on the periplasmic side.
The intracellular gate residue Met426 in helix H11 is displaced by approximately
6 A compared to the occluded state of PepT_So, opening the intracellular gate.

### Three peptide-binding pockets (P1, P2, P3)

The PepT_So2 substrate-binding site is divided into three pockets for peptide side
chain interactions. P1 is a small pocket formed by Ser154, Tyr29, Met158 and Pro330,
accommodating only small- to medium-sized residues. P2 is a hydrophobic pocket
dominated by Phe287, Phe288, Tyr291 and Ser406. P3 is an aromatic pocket formed by
Arg25, Tyr28, Trp54, Ile61, Tyr62, Pro65, Asn292, Phe430 and Asn437. The N-terminus
of bound peptides is clamped by Glu402, Asn151, Asn329 and Tyr147, while the C-terminus
extends into a positively charged patch (Arg25, Lys121). Dipeptides interact primarily
with Arg25, while tripeptides extend further to interact with Lys121.

### Peptide-bound crystal structures at high resolution

Three crystal structures of PepT_So2 in complex with different peptides were solved:
4TPJ ([AAA](/xray-mp-wiki/reagents/ligands/aaa/) tripeptide, 3.2 A), 4TPG (AY(Br)A tripeptide, 3.91 A), and 4TPH
(AY(Br) dipeptide, 3.16 A). All in P2_1 2_1 2_1 space group with two molecules per
asymmetric unit. Crystallization used 3% TMNO, phosphate [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) buffer pH 4.0-4.5,
36-46% [PEG](/xray-mp-wiki/reagents/additives/peg/) 300, and 0.12 M ZnCl2. The brominated tyrosine-containing peptides
provided strong anomalous densities for bromine atoms, confirming correct ligand
placement.


## Cross-References

- [POT Family (Proton-Dependent Oligopeptide Transporters)](/xray-mp-wiki/concepts/transport-mechanisms/pot-family/) — PepT_So2 is a member of the POT family within MFS
- [PepT_So Oligopeptide Transporter](/xray-mp-wiki/proteins/mfs-transporters/pept-so/) — POT family member from Shewanella oneidensis, occluded conformation
- [PepT_St Proton-Dependent Oligopeptide Transporter](/xray-mp-wiki/proteins/mfs-transporters/pept-st/) — POT family member from Streptococcus thermophilus, inward open conformation
- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) — PepT_So2 belongs to the MFS of secondary active transporters
- [Alafosfalin](/xray-mp-wiki/reagents/ligands/alafosfalin/) — Peptidomimetic phosphonodipeptide ligand co-crystallized with PepT_So2
- [Scissor-Switch Gating](/xray-mp-wiki/concepts/transport-mechanisms/scissor-switch-gating/) — POT-specific gating mechanism employed by PepT_So2
- [E. coli DtpA Peptide Transporter](/xray-mp-wiki/proteins/slc-transporters/dtpa/) — POT family member from Escherichia coli
- [E. coli YbgH Peptide Transporter](/xray-mp-wiki/proteins/mfs-transporters/ybgH/) — POT family member from Escherichia coli
- [Ala-Ala-Ala (AAA)](/xray-mp-wiki/reagents/ligands/aaa/) — Tripeptide ligand co-crystallized with PepT_So2 (PDB 4TPJ)
- [Ala-Tyr(L-3,5-diBr)-Ala (AY(Br)A)](/xray-mp-wiki/reagents/ligands/aybr-a/) — Brominated tripeptide ligand co-crystallized with PepT_So2 (PDB 4TPG)
- [Ala-Tyr(L-3,5-diBr) (AY(Br))](/xray-mp-wiki/reagents/ligands/aybr/) — Brominated dipeptide ligand co-crystallized with PepT_So2 (PDB 4TPH)
- [PepT_So2 Substrate-Binding Pockets (P1, P2, P3)](/xray-mp-wiki/concepts/structural-mechanisms/peptide-binding-pocket/) — Three pockets identified in PepT_So2 substrate-binding cavity for side chain recognition
