---
title: MhsT Multi-Hydrophobic Amino Acid Transporter from Bacillus halodurans
created: 2026-06-02
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##NSMB.2894, doi/10.15252##embj.2020105164]
verified: false
---

# MhsT Multi-Hydrophobic Amino Acid Transporter from Bacillus halodurans

## Overview

MhsT is a multi-hydrophobic amino acid transporter from Bacillus halodurans belonging to the [Neurotransmitter/Sodium Symporter (NSS) Family](/xray-mp-wiki/concepts/nss-family/). It mediates the Na+-coupled uptake of hydrophobic amino acids including L-tryptophan, L-tyrosine, [L-Phenylalanine](/xray-mp-wiki/reagents/ligands/l-phenylalanine/), and [L-Leucine](/xray-mp-wiki/reagents/ligands/l-leucine/). Initial crystal structures of MhsT in occluded inward-facing states with bound Na+ ions and L-tryptophan revealed a novel mechanism involving TM5 unwinding at a conserved GlyX9Pro motif, providing a solvent pathway for intracellular Na+ release from the Na2 site. Subsequent structures with six different substrates (L-Tyr, L-4-F-Phe, L-Phe, L-Ile, L-Leu, L-Val) revealed how a Gly-Met-Gly (GMG) motif in the unwound region of TM6 tailors the binding site volume to accommodate substrates of different sizes. The GMG loop shifts inward by ~2 A for small aliphatic substrates, reducing binding pocket volume from ~230 A^3 to ~144 A^3. A conserved Glu66 residue maintains interaction with the GMG loop through water-mediated hydrogen bonds in all states.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##NSMB.2894 | not specified | 2.1 A | not specified | Full-length MhsT from B. halodurans, residues 1-453, His-tag cleaved | Na+ (2 ions), L-tryptophan |
| doi/10.1038##NSMB.2894 | not specified | 2.6 A | not specified | Full-length MhsT from B. halodurans, residues 1-453, His-tag cleaved, LCP crystal form | Na+ (2 ions), L-tryptophan |
| doi/10.15252##embj.2020105164 | 6YU7 | 2.3 A | P2 | Full-length MhsT, religipidated in [DOPC](/xray-mp-wiki/reagents/lipids/dopc/), crystallized in OG/NG | Na+, L-Tyrosine |
| doi/10.15252##embj.2020105164 | 6YU4 | 2.26 A | P2 | Full-length MhsT, religipidated in [DOPC](/xray-mp-wiki/reagents/lipids/dopc/) | Na+, L-4-Fluoro-Phenylalanine |
| doi/10.15252##embj.2020105164 | 6YU3 | 2.25 A | P2 | Full-length MhsT, religipidated in [DOPC](/xray-mp-wiki/reagents/lipids/dopc/) | Na+, [L-Phenylalanine](/xray-mp-wiki/reagents/ligands/l-phenylalanine/) |
| doi/10.15252##embj.2020105164 | 6YU2 | 2.3 A | P2_1 | Full-length MhsT, religipidated in [DOPC](/xray-mp-wiki/reagents/lipids/dopc/) | Na+, L-Isoleucine |
| doi/10.15252##embj.2020105164 | 6YU6 | 2.1 A | P2_1 | Full-length MhsT, religipidated in [DOPC](/xray-mp-wiki/reagents/lipids/dopc/) | Na+, [L-Leucine](/xray-mp-wiki/reagents/ligands/l-leucine/) |
| doi/10.15252##embj.2020105164 | 6YU5 | 2.1 A | P2_1 | Full-length MhsT, religipidated in [DOPC](/xray-mp-wiki/reagents/lipids/dopc/) | Na+, L-Valine |

## Expression and Purification

- **Expression system**: Lactococcus lactis NZ9000
- **Construct**: mhsT gene cloned into plasmid pNZ8048, N-terminal 10x histidine tag with TEV protease cleavage site

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane preparation | Cell lysis and membrane fractionation | -- | not specified + not specified | Expressed in Lactococcus lactis NZ9000, purified as previously described |
| Solubilization | Detergent solubilization | -- | not specified + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) (n-dodecyl-beta-D-maltopyranoside) | Membranes solubilized in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA affinity resin | not specified + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | His-tagged MhsT captured on Ni-NTA |
| Tag cleavage | TEV protease digestion | Ni-NTA affinity resin (second column) | [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | TEV protease used to remove N-terminal histidine tag, MhsT-containing flow-through collected |
| Second affinity purification | Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA affinity resin (Qiagen) | not specified + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Second Ni-NTA column to remove cleaved His-tag and TEV protease |


## Crystallization

### doi/10.1038##NSMB.2894

| Parameter | Value |
|---|---|
| Method | HiLiDe (hydrophobic interaction-driven crystallization) |
| Protein sample | MhsT at 7 mg/mL after TEV cleavage and second Ni-NTA purification, in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Reservoir | not specified |
| Temperature | not specified |
| Growth time | not specified |
| Notes | MhsT crystallized using HiLiDe method, yielding structure at 2.1 A resolution. Crystallographic dimer formed through intracellular half of helix 11 and intracellular loop 5. |

| Parameter | Value |
|---|---|
| Method | lipidic cubic phase (LCP) |
| Protein sample | MhsT in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Temperature | not specified |
| Growth time | not specified |
| Notes | MhsT crystallized using LCP method, yielding structure at 2.6 A resolution. Similar overall structure to HiLiDe form (0.65 A RMSD) but differs at TM5 region. |

### doi/10.15252##embj.2020105164

| Parameter | Value |
|---|---|
| Method | hanging-drop vapor diffusion |
| Protein sample | MhsT religipidated in [DOPC](/xray-mp-wiki/reagents/lipids/dopc/) at 9 mg/mL, 4CMC OG or NG detergent |
| Reservoir | 14-24% [PEG400](/xray-mp-wiki/reagents/additives/peg-400/), 0.3-0.5 M NaCl, 100 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) or HEPES-NaOH pH 7.0, 5-10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 5% TMANO |
| Temperature | 19 C |
| Growth time | not specified |
| Notes | Crystallized by vapor diffusion in hanging drops using immersion oil as sealing agent. Substrates included Tyr, 4F-Phe, Phe, Ile, Leu, Val. Diffraction data collected at Diamond Light Source (I24, I04) and Swiss Light Source (PXI). |


## Biological / Functional Insights

### Occluded inward-facing state with bound Na+ and substrate

Both MhsT crystal structures represent an occluded, inward-facing state with two bound Na+ ions and one L-tryptophan molecule. The extracellular side is sealed by a tight hydrophobic cluster of TMs 1b, 2, 6a, and 7, collapsing the extracellular vestibule. At the intracellular side, a water-access pathway reaches the Na2 site while the substrate and Na1 site remain inaccessible. This state is distinct from the inward-open apo conformation of [LEUT](/xray-mp-wiki/proteins/enzymes/leut/).

### TM5 unwinding via GlyX9Pro motif

The intracellular part of transmembrane helix 5 (TM5i) unwinds at a conserved GlyX9Pro motif, creating a solvent pathway from the cytoplasm to the Na2 site. This unwinding results from strain between the movement of the extracellular part of TM5 (TM5e) together with TM6a during closure of the extracellular vestibule around Trp33, while TM5i maintains coiled-coil interaction with TM1a through coordination with Na+ at the Na2 site. The GlyX9Pro motif is conserved across the NSS family and is predicted to promote unraveling of TM5i.

### Na2 site solvation and Na+ release mechanism

TM5 unwinding provides a cytoplasmic water molecule access to the Na2 site as a sixth ligand, completing octahedral coordination. TM8 is displaced relative to TM1, and the Ser323 side chain shifts to provide space. This solvation primes the Na2 site for intracellular Na+ release in the low-Na+ cytoplasmic environment. Release of Na+ from Na2 triggers TM1a to swing out, opening a wide intracellular pathway for substrate and Na1 release.

### Substrate recognition by the GMG motif

Six new substrate-bound structures (L-Tyr, L-4-F-Phe, L-Phe, L-Ile, L-Leu, L-Val) reveal a bimodal binding site that distinguishes between aliphatic and aromatic amino acids. The unwound region of TM6 containing a Gly-Met-Gly (GMG) motif shifts inward by ~2 A for small aliphatic substrates, reducing the binding pocket volume from ~230 A^3 (aromatic) to ~144 A^3 (valine). This is an induced-fit mechanism where the GMG loop compensates for smaller substrate side chains. Met236 undergoes rotamer changes to fine-tune the chemical environment for different substrates.

### Conserved Glu66 fulcrum

Glu66 on TM2 forms a conserved interaction with the unwound TM6 region through water-mediated hydrogen bonds. With aliphatic substrates, an additional ordered water molecule is recruited compared to aromatic substrates. This interaction is maintained throughout the transport cycle (as confirmed by comparison with various [LEUT](/xray-mp-wiki/proteins/enzymes/leut/) structures) and is critical for conformational transitions. Mutation of the equivalent glutamate in [SERT](/xray-mp-wiki/proteins/slc-transporters/ssert/), DAT, NET, and GAT1 diminishes transport activity without affecting substrate binding.

### M236F mutation alters substrate specificity

The M236F substitution (mimicking the AFG motif of human SLC6A18/SLC6A19) completely abolishes transport of aromatic amino acids (L-Trp, L-Phe, L-Tyr) while maintaining aliphatic amino acid (L-Leu, L-Val, L-Ile) transport. The Vmax for Leu is unchanged (3.23 vs 3.33 nmol/min/mg for WT vs M236F), while Trp uptake is undetectable. This explains why human SLC6A18/SLC6A19 (with AFG motif) preferentially transport aliphatic amino acids, despite sharing ~50% binding site conservation with MhsT.

### Substrate binding and selectivity

MhsT binds L-tryptophan with a Kd of 4.8 +/- 0.6 uM and a molar binding stoichiometry of 1.1 +/- 0.04. The substrate binding site is similar to the L-leucine-occupied S1 site in [LEUT](/xray-mp-wiki/proteins/enzymes/leut/). MhsT shows transport activity for L-tryptophan (Kt 1.7 +/- 0.3 uM), L-tyrosine, [L-Phenylalanine](/xray-mp-wiki/reagents/ligands/l-phenylalanine/), and [L-Leucine](/xray-mp-wiki/reagents/ligands/l-leucine/). The catalytic turnover number (kcat 0.8 +/- 0.03 s-1) is about two and three orders of magnitude faster than LeuT-mediated transport of [L-Alanine](/xray-mp-wiki/reagents/substrates/l-alanine/) and [L-Leucine](/xray-mp-wiki/reagents/ligands/l-leucine/), respectively. The bulky side chains of Phe259LeuT and Ile359LeuT (Met236MhsT and Leu328MhsT) cannot accommodate L-tryptophan, explaining substrate selectivity differences.

### Transport mechanism model for NSS family

A general model of NSS function: (1) Na+ and substrate binding in outward-open state initiates occlusion. (2) Occluded outward-facing state exposes hydrophobic vestibule, priming for extracellular closure around Trp33. (3) Transition to inward-facing state with TM5 unwinding providing solvation pathway for Na2 site. (4) Na+ release from Na2 triggers forward reaction. (5) TM1a swings out, TM5i reassociates with TM5e, releasing substrate and Na1 intracellularly. (6) Return to outward-open state through unknown occluded states.

### Comparison with LeuT functional states

MhsT occluded inward-facing state differs from [LEUT](/xray-mp-wiki/proteins/enzymes/leut/) inward-open apo conformation: the extracellular-closed conformation is not paired with an open intracellular side. Instead, the intracellular configuration resembles outward-facing states with the N-terminal tail sealing the cytoplasmic side and Trp12 plugging a hydrophobic pocket. However, TM5 unwinding creates a solvent pathway to the Na2 site that is absent in outward-facing [LEUT](/xray-mp-wiki/proteins/enzymes/leut/) structures. The MhsT structure shares 33% sequence identity with [LEUT](/xray-mp-wiki/proteins/enzymes/leut/) and 25% with dDAT.

### Conservation of GlyXnPro pattern in LeuT-fold transporters

Structural alignment of MhsT (NSS family) with [Mhp1 Benzyl-Hydantoin Transporter from Microbacterium liquefaciens](/xray-mp-wiki/proteins/slc-transporters/mhp1/) (NCS1 family, another LeuT-fold transporter) reveals a recurring GlyXnPro pattern in the intracellular part of TM5, suggesting that TM5 unwinding and cytoplasmic water access to the Na+-binding site may be a general mechanism exploited by other Na+-dependent LeuT-fold transporters. The GlyX9Pro motif is slightly shifted in eukaryotic NSSs relative to bacterial NSSs, potentially fine-tuning the TM5 deformation mechanism to species-specific conditions.


## Cross-References

- [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/enzymes/leut/) — NSS family prototype; MhsT shares 33% sequence identity with LeuT; LeuT structures 5JAE and 5JAF show return state mechanism with Leu25 rotation; compared with MhsT inward-facing state for NSS transport cycle model
- [Drosophila Dopamine Transporter (dDAT)](/xray-mp-wiki/proteins/slc-transporters/d-dopamine-transporter/) — Eukaryotic NSS homolog used for structural comparison; MhsT shares 25% sequence identity
- [Neurotransmitter/Sodium Symporter (NSS) Family](/xray-mp-wiki/concepts/nss-family/) — MhsT belongs to the NSS family
- [SLC6 Substrate Recognition by the GMG Motif](/xray-mp-wiki/concepts/slc6-substrate-recognition-gmg-motif/) — The GMG motif in TM6 mediates MhsT substrate recognition
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for MhsT solubilization, purification, and binding studies
- [TEV Protease](/xray-mp-wiki/reagents/protein-tags/tevp-protease/) — Used to cleave N-terminal histidine tag from MhsT
- [HiLiDe Crystallization](/xray-mp-wiki/methods/crystallization/hilide-crystallization/) — MhsT crystallized using HiLiDe method (2.1 A structure)
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — MhsT crystallized using LCP method (2.6 A structure)
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — Core transport mechanism of NSS family
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
