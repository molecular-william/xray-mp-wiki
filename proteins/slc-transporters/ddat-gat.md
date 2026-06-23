---
title: dDAT_GAT (GAT1-Engineered Drosophila Dopamine Transporter)
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography, transporter]
sources: [doi/10.15252##embj.2022110735]
verified: false
---

# dDAT_GAT (GAT1-Engineered Drosophila Dopamine Transporter)

## Overview

dDAT_GAT is an engineered construct of the Drosophila melanogaster dopamine transporter (dDAT) in which 11 residues in the primary binding site were substituted to mimic the binding pocket of the human GABA transporter 1 (hGAT1, SLC6A1). The construct was built on a thermostabilized dDAT scaffold (ts2-L415A, V74A) and includes mutations F43Y, D46G, V120A, D121N, F325L, S422Q, G425T, S426V, Y124F (TM3), I113V (TM3), and E384S (EL4). Although dDAT_GAT lacks GABA transport activity, it binds GAT1-specific inhibitors including NO711 (KD ~10 µM) and SKF89976a (KD ~34 µM) as measured by microscale thermophoresis, enabling the first X-ray structures of GAT1 inhibitors bound to an NSS family member. The substrate-free structure (3.2 Å, PDB 7WGD) reveals an outward-open conformation with altered subsite architecture compared to wild-type dDAT.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.15252##embj.2022110735 | 7WGD | 3.2 A | not specified | dDAT_GAT — ts2-L415A, V74A with 11 GAT1-like substitutions (F43Y, D46G, V120A, D121N, F325L, S422Q, G425T, S426V, Y124F, I113V, E384S) | substrate-free (water molecules modeled in binding site) |
| doi/10.15252##embj.2022110735 | not specified | not specified | not specified | dDAT_GAT — as above | [NO711](/xray-mp-wiki/reagents/ligands/no711) |
| doi/10.15252##embj.2022110735 | not specified | not specified | not specified | dDAT_GAT — as above | [SKF89976a](/xray-mp-wiki/reagents/ligands/skf89976a) (primary site + allosteric site) |

## Expression and Purification

### Purification Workflow

- **Expression system**: HEK293S GnTI- cells
- **Expression construct**: dDAT_GAT with C-terminal GFP-His8 fusion
- **Tag info**: GFP-His8

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | Baculovirus-mediated transduction (BacMam) | — |  | HEK293S GnTI- cells transduced with P2 virus |
| Membrane solubilization | Detergent solubilization | — | 20 mM DDM + 4 mM CHS in TBS (20 mM Tris pH 8.0, 100 mM NaCl) |  |
| Affinity chromatography | Cobalt-charged metal affinity resin | — |  | Batch binding with cobalt resin |
| Tag removal | Thrombin digestion | — |  | GFP-His8 tag removed |
| Size exclusion chromatography | Superdex 200 Increase 10/300 | — | 20 mM Tris pH 8.0, 300 mM NaCl, 4 mM decyl-β-D-maltoside, 0.2 mM CHS, 0.001% POPE |  |


## Crystallization

No crystallization described.

## Biological / Functional Insights

### Altered subsite architecture for GAT1 inhibitor recognition

The GAT1-like substitutions in subsites A and B reorganize the binding pocket. Subsite A loses the conserved Asp46 (substituted to Gly63-like) to accommodate the carboxylate group of GAT1 inhibitors, which coordinates Na+ at site 1. Subsite B is occluded by a hydrogen bond network (Asn121-Gln422, Gln422-Thr425, Asn121-Thr425, Asn121-Asn125) that minimizes the accessible cavity. A new subsite C' is created, replacing the conventional trilobed subsite architecture of biogenic amine transporters.

### TM6 linker as a selectivity determinant

The F325L substitution (Leu300 in GAT1) at the TM6 linker is critical for GAT1 inhibitor binding. In biogenic amine transporters the larger phenylalanine side chain restricts access, whereas the leucine in GATs allows accommodation of the diaryl groups of tiagabine analogs by widening the TM6 linker. Mutation of L300W in GAT1 nearly abolishes GABA transport, confirming the gatekeeper role of this residue.

### Allosteric binding site for SKF89976a

SKF89976a binds not only at the primary S1 site but also at an allosteric site in the extracellular vestibule, near EL4 (E384S substitution, Ser359 in GAT1). This dual binding mode provides a structural rationale for SKF89976a's ability to display both competitive and noncompetitive inhibition characteristics in GAT1. The allosteric site involves interactions with residues in TM10 and EL4, analogous to the (S)-citalopram secondary binding site in SERT.


## Cross-References

- [Drosophila Dopamine Transporter (dDAT)](/xray-mp-wiki/proteins/slc-transporters/d-dopamine-transporter/) — Parent construct; dDAT_GAT is derived from dDAT with 11 GAT1-like substitutions
- [Neurotransmitter/Sodium Symporter (NSS) Family](/xray-mp-wiki/concepts/nss-family/) — dDAT_GAT is an engineered NSS family member
- [GABA Transporters (GATs)](/xray-mp-wiki/concepts/gaba-transporters-gats/) — dDAT_GAT was engineered to mimic the GAT1 binding site
- [Allosteric Site in NSS Transporters](/xray-mp-wiki/concepts/allosteric-site-in-nss-transporters/) — SKF89976a binds the allosteric site in the extracellular vestibule of dDAT_GAT
- [NO711](/xray-mp-wiki/reagents/ligands/no711/) — GAT1 inhibitor co-crystallized with dDAT_GAT at primary binding site
- [SKF89976a](/xray-mp-wiki/reagents/ligands/skf89976a/) — GAT1 inhibitor bound at both primary and allosteric sites
