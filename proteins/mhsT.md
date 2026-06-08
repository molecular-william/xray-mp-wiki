---
title: MhsT Multi-Hydrophobic Amino Acid Transporter from Bacillus halodurans
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##NSMB.2894]
verified: false
---

# MhsT Multi-Hydrophobic Amino Acid Transporter from Bacillus halodurans

## Overview

MhsT is a multi-hydrophobic amino acid transporter from Bacillus halodurans belonging to the neurotransmitter/sodium symporter (NSS) family. It mediates the Na+-coupled uptake of hydrophobic amino acids including L-tryptophan, L-tyrosine, L-phenylalanine, and L-leucine. Two crystal structures of MhsT in occluded inward-facing states with bound Na+ ions and L-tryptophan revealed a novel mechanism involving TM5 unwinding at a conserved GlyX9Pro motif, providing a solvent pathway for intracellular Na+ release from the Na2 site.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##NSMB.2894 | not specified | 2.1 A | not specified | Full-length MhsT from B. halodurans, residues 1-453, His-tag cleaved | Na+ (2 ions), L-tryptophan |
| doi/10.1038##NSMB.2894 | not specified | 2.6 A | not specified | Full-length MhsT from B. halodurans, residues 1-453, His-tag cleaved, LCP crystal form | Na+ (2 ions), L-tryptophan |

## Expression and Purification

- **Expression system**: Lactococcus lactis NZ9000
- **Construct**: mhsT gene cloned into plasmid pNZ8048, N-terminal 10x histidine tag with TEV protease cleavage site

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane preparation | Cell lysis and membrane fractionation | -- | not specified + not specified | Expressed in Lactococcus lactis NZ9000, purified as previously described |
| Solubilization | Detergent solubilization | -- | not specified + DDM (n-dodecyl-beta-D-maltopyranoside) | Membranes solubilized in DDM |
| Affinity chromatography | Ni-NTA affinity chromatography | Ni-NTA affinity resin | not specified + DDM | His-tagged MhsT captured on Ni-NTA |
| Tag cleavage | TEV protease digestion | Ni-NTA affinity resin (second column) | DDM | TEV protease used to remove N-terminal histidine tag, MhsT-containing flow-through collected |
| Second affinity purification | Ni-NTA affinity chromatography | Ni-NTA affinity resin (Qiagen) | not specified + DDM | Second Ni-NTA column to remove cleaved His-tag and TEV protease |


## Crystallization

### doi/10.1038##NSMB.2894

| Parameter | Value |
|---|---|
| Method | HiLiDe (hydrophobic interaction-driven crystallization) |
| Protein sample | MhsT at 7 mg/mL after TEV cleavage and second Ni-NTA purification, in DDM |
| Reservoir | not specified |
| Temperature | not specified |
| Growth time | not specified |
| Notes | MhsT crystallized using HiLiDe method, yielding structure at 2.1 A resolution. Crystallographic dimer formed through intracellular half of helix 11 and intracellular loop 5. |

| Parameter | Value |
|---|---|
| Method | lipidic cubic phase (LCP) |
| Protein sample | MhsT in DDM |
| Temperature | not specified |
| Growth time | not specified |
| Notes | MhsT crystallized using LCP method, yielding structure at 2.6 A resolution. Similar overall structure to HiLiDe form (0.65 A RMSD) but differs at TM5 region. |


## Biological / Functional Insights

### Occluded inward-facing state with bound Na+ and substrate

Both MhsT crystal structures represent an occluded, inward-facing state with two bound Na+ ions and one L-tryptophan molecule. The extracellular side is sealed by a tight hydrophobic cluster of TMs 1b, 2, 6a, and 7, collapsing the extracellular vestibule. At the intracellular side, a water-access pathway reaches the Na2 site while the substrate and Na1 site remain inaccessible. This state is distinct from the inward-open apo conformation of LeuT.

### TM5 unwinding via GlyX9Pro motif

The intracellular part of transmembrane helix 5 (TM5i) unwinds at a conserved GlyX9Pro motif, creating a solvent pathway from the cytoplasm to the Na2 site. This unwinding results from strain between the movement of the extracellular part of TM5 (TM5e) together with TM6a during closure of the extracellular vestibule around Trp33, while TM5i maintains coiled-coil interaction with TM1a through coordination with Na+ at the Na2 site. The GlyX9Pro motif is conserved across the NSS family and is predicted to promote unraveling of TM5i.

### Na2 site solvation and Na+ release mechanism

TM5 unwinding provides a cytoplasmic water molecule access to the Na2 site as a sixth ligand, completing octahedral coordination. TM8 is displaced relative to TM1, and the Ser323 side chain shifts to provide space. This solvation primes the Na2 site for intracellular Na+ release in the low-Na+ cytoplasmic environment. Release of Na+ from Na2 triggers TM1a to swing out, opening a wide intracellular pathway for substrate and Na1 release.

### Substrate binding and selectivity

MhsT binds L-tryptophan with a Kd of 4.8 +/- 0.6 uM and a molar binding stoichiometry of 1.1 +/- 0.04. The substrate binding site is similar to the L-leucine-occupied S1 site in LeuT. MhsT shows transport activity for L-tryptophan (Kt 1.7 +/- 0.3 uM), L-tyrosine, L-phenylalanine, and L-leucine. The catalytic turnover number (kcat 0.8 +/- 0.03 s-1) is about two and three orders of magnitude faster than LeuT-mediated transport of L-alanine and L-leucine, respectively. The bulky side chains of Phe259LeuT and Ile359LeuT (Met236MhsT and Leu328MhsT) cannot accommodate L-tryptophan, explaining substrate selectivity differences.

### Transport mechanism model for NSS family

A general model of NSS function: (1) Na+ and substrate binding in outward-open state initiates occlusion. (2) Occluded outward-facing state exposes hydrophobic vestibule, priming for extracellular closure around Trp33. (3) Transition to inward-facing state with TM5 unwinding providing solvation pathway for Na2 site. (4) Na+ release from Na2 triggers forward reaction. (5) TM1a swings out, TM5i reassociates with TM5e, releasing substrate and Na1 intracellularly. (6) Return to outward-open state through unknown occluded states.

### Comparison with LeuT functional states

MhsT occluded inward-facing state differs from LeuT inward-open apo conformation: the extracellular-closed conformation is not paired with an open intracellular side. Instead, the intracellular configuration resembles outward-facing states with the N-terminal tail sealing the cytoplasmic side and Trp12 plugging a hydrophobic pocket. However, TM5 unwinding creates a solvent pathway to the Na2 site that is absent in outward-facing LeuT structures. The MhsT structure shares 33% sequence identity with LeuT and 25% with dDAT.

### Conservation of GlyXnPro pattern in LeuT-fold transporters

Structural alignment of MhsT (NSS family) with Mhp1 (NCS1 family, another LeuT-fold transporter) reveals a recurring GlyXnPro pattern in the intracellular part of TM5, suggesting that TM5 unwinding and cytoplasmic water access to the Na+-binding site may be a general mechanism exploited by other Na+-dependent LeuT-fold transporters. The GlyX9Pro motif is slightly shifted in eukaryotic NSSs relative to bacterial NSSs, potentially fine-tuning the TM5 deformation mechanism to species-specific conditions.


## Cross-References

- [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/leut/) — NSS family prototype; MhsT shares 33% sequence identity with LeuT; LeuT structures 5JAE and 5JAF show return state mechanism with Leu25 rotation; compared with MhsT inward-facing state for NSS transport cycle model
- [Drosophila Dopamine Transporter (dDAT)](/xray-mp-wiki/proteins/d-dopamine-transporter/) — Eukaryotic NSS homolog used for structural comparison; MhsT shares 25% sequence identity
- [Neurotransmitter/Sodium Symporter (NSS) Family](/xray-mp-wiki/concepts/nss-family/) — MhsT belongs to the NSS family
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for MhsT solubilization, purification, and binding studies
- [TEV Protease](/xray-mp-wiki/reagents/protein-tags/tevp-protease/) — Used to cleave N-terminal histidine tag from MhsT
- [HiLiDe Crystallization](/xray-mp-wiki/methods/crystallization/hilide-crystallization/) — MhsT crystallized using HiLiDe method (2.1 A structure)
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — MhsT crystallized using LCP method (2.6 A structure)
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — Core transport mechanism of NSS family
