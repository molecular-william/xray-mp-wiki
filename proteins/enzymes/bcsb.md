---
title: "BcsB from Rhodobacter sphaeroides (Cellulose Synthase Periplasmic Subunit)"
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature11744]
verified: false
---

# BcsB from Rhodobacter sphaeroides (Cellulose Synthase Periplasmic Subunit)

## Overview

BcsB is a periplasmic protein that associates with the catalytic [Bcsa](/xray-mp-wiki/proteins/enzymes/bcsa/) subunit to form the bacterial cellulose synthase complex from Rhodobacter sphaeroides. BcsB is anchored to the inner membrane via a single C-terminal transmembrane helix and contains two periplasmic carbohydrate binding domains (CBD1 and CBD2) connected by a conserved disulphide bond, and two flavodoxin-like domains (FD1 and FD2). The CBD domains interact with the translocating glucan chain as it exits the [Bcsa](/xray-mp-wiki/proteins/enzymes/bcsa/) transmembrane channel, while the conserved residues at the tip of CBD1 likely play a role in glucan binding. [Bcsa](/xray-mp-wiki/proteins/enzymes/bcsa/) and BcsB can be fused as a single polypeptide in some species, supporting the genetic observation that BcsB is essential for cellulose synthesis.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature11744 | 4HG6 | 4.5 A |  | BcsA-BcsB complex from Rhodobacter sphaeroides; BcsB residues 21-725 with N-terminal PelB signal sequence (generates additional Met-Gly dipeptide after cleavage) | Translocating glucan (18 [Glucose](/xray-mp-wiki/reagents/additives/glucose/) units visible in electron density) |

## Expression and Purification

- **Expression system**: E. coli Rosetta 2 cells
- **Construct**: BcsB residues 21-725 cloned into pETDuet vector with N-terminal PelB signal sequence; amplified without native N-terminal signal sequence

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Co-expression and membrane preparation | Auto-induction culture | -- | ZYP-5052 auto-induction medium + -- | [Bcsa](/xray-mp-wiki/proteins/enzymes/bcsa/) and BcsB co-expressed in E. coli Rosetta 2 cells; cells grown at 37 C in ZYP-5052 auto-induction medium |
| Membrane solubilization | Detergent solubilization | -- | 20 mM sodium phosphate pH 7.2, 0.3 M NaCl, 5 mM [Cellobiose](/xray-mp-wiki/reagents/additives/cellobiose/), 5 mM [Mgcl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/), 40 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 2% Triton X-100 | Crude membranes solubilized for 60 min at 4 C |
| Affinity chromatography | Ni-NTA affinity chromatography | Ni-NTA agarose (Qiagen) | RB2 buffer with 40 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 2% Triton X-100 | Batch incubation with Ni-NTA agarose; [Bcsa](/xray-mp-wiki/proteins/enzymes/bcsa/) carries C-terminal His12 tag for purification of the complex |


## Crystallization

### doi/10.1038##nature11744

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified BcsA-BcsB complex |
| Reservoir | 30% [PEG200](/xray-mp-wiki/reagents/additives/peg200/), 0.1 M [MES](/xray-mp-wiki/reagents/buffers/mes/) pH 6.5, 50 mM NaCl |
| Temperature | 4 C |
| Growth time | approximately 7 days for initial crystals |
| Cryoprotection | -- |
| Notes | Crystals of selenomethionine-derivatized BcsA-BcsB complex grown at 4 C; diffraction to 4.5 A |


## Biological / Functional Insights

### Periplasmic domain architecture

The periplasmic region of BcsB is primarily formed by two carbohydrate binding domains (CBD1 and CBD2) connected by a disulphide bond between conserved Cys 163 and Cys 430. These are linked to two compact alpha/beta domains (FD1: amino acids 192-303; FD2: amino acids 457-529 and 598-666) that resemble a flavodoxin fold. The repeating structural motif of BcsB therefore contains a CBD linked to an FD domain.

### Membrane anchoring and interface helices

BcsB is anchored to the inner membrane via a single C-terminal transmembrane helix (amino acids 695-720). At the water-lipid interface, BcsB forms two amphipathic helices: IF4 (amino acids 569-592) interacts with the periplasmic termini of BcsA's TM2, TM6, and TM8, while IF5 (amino acids 679-693) directly precedes BcsB's membrane anchor and contacts BcsA's TM1 and the 1/2 loop.

### Conserved residues in CBD1 and glucan interaction

A cluster of conserved residues including His 159, Arg 160, Ile 161, Leu 171, and Trp 172 is located at the tip of CBD1, close to its disulphide bond with CBD2 and above the periplasmic exit of the glucan channel. Comparison of CBD1 with the bacterial carbohydrate binding module family 35 (CBM35) in complex with a glucuronic acid disaccharide localizes disaccharide binding to this cluster of conserved residues, indicating that CBD1 interacts with the translocating glucan.

### BcsA-BcsB complex interface

[Bcsa](/xray-mp-wiki/proteins/enzymes/bcsa/) and BcsB form an elongated complex. BcsB's transmembrane anchor packs against one side of the cuboid arrangement of BcsA's transmembrane helices. BcsA's TM2 and TM3, as well as its 5/6 loop, account for almost 30% of the complex interface with BcsB. The periplasmic exit of the glucan channel is between BcsA's 5/6 and 7/8 loops at the BcsA-BcsB interface, where the glucan kinks to protrude from the complex sideways.


## Cross-References

- [BcsA from Rhodobacter sphaeroides](/xray-mp-wiki/proteins/enzymes/bcsa/) — Catalytic partner; BcsA-BcsB complex solved by X-ray crystallography at 4.5 A
- [Triton X-100](/xray-mp-wiki/reagents/detergents/triton-x-100/) — Nonionic detergent used for solubilization of BcsA-BcsB complex from membranes
- [Sodium Phosphate Buffer](/xray-mp-wiki/reagents/buffers/sodium-phosphate/) — Buffer component in purification buffers
- [Cellobiose](/xray-mp-wiki/reagents/additives/cellobiose/) — Additive (5 mM) in purification buffers for BcsA-BcsB complex
- [Magnesium Chloride (MgCl2)](/xray-mp-wiki/reagents/additives/magnesium-chloride/) — Additive (5 mM) in solubilization buffer
- [GT-A Fold (Glycosyltransferase A Fold)](/xray-mp-wiki/concepts/structural-mechanisms/gt-a-fold/) — Structural domain of partner protein BcsA
- [PilZ Domain](/xray-mp-wiki/concepts/structural-mechanisms/pilz-domain/) — Cyclic-di-GMP binding domain of partner protein BcsA
- [Glucose](/xray-mp-wiki/reagents/additives/glucose/) — Referenced in the context of Glucose
- [Mgcl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/) — Referenced in the context of Mgcl2
- [PEG200](/xray-mp-wiki/reagents/additives/peg200/) — Referenced in the context of PEG200
