---
title: Bovine Mitochondrial F-ATPase c8-Ring (F1-c-ring Complex)
created: 2026-06-21
updated: 2026-06-21
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1011099107]
verified: false
---

# Bovine Mitochondrial F-ATPase c8-Ring (F1-c-ring Complex)

## Overview

The bovine mitochondrial F-ATPase (ATP synthase) c8-ring is part of the membrane-embedded rotor of the enzyme that drives ATP synthesis using the transmembrane proton-motive force. The structure of the bovine F1-c-ring complex was determined at 3.5 A resolution, revealing that the c-ring contains 8 c-subunits (c8-ring). This is the first c-ring structure from a higher eukaryote, establishing that vertebrate F-ATPases contain c8-rings and require 2.7 protons per ATP synthesised (or 3.7 total including transport costs).

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1011099107 |  | 3.5 A | P2(1)2(1)2(1) | Bovine F1-c-ring subcomplex (F1 domain alpha3beta3gamma + c8-ring) | AMP-PNP, Mg2+ |

## Expression and Purification

- **Expression system**: Bovine heart mitochondria (native source)
- **Construct**: Native F1Fo-ATPase purified from bovine heart mitochondria; F1-c-ring subcomplex prepared by ion exchange chromatography

### Purification Workflow

- **Expression construct**: Native F1Fo-ATPase from bovine heart mitochondria
- **Tag info**: Purified via IF1(1-60) affinity column (residues 1-60 of F1-ATPase inhibitor protein IF1)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Purification of F1Fo-ATPase | Affinity chromatography | IF1(1-60) affinity column | 20 mM Tris-HCl pH 8.0, 10% glycerol, 1 mM ADP, 2 mM MgSO4, 0.02% NaN3 + 20 mM N-dodecyl-N,N-(dimethylammonio)butyrate | Purified from bovine heart mitochondria |
| F1-c-ring subcomplex preparation | Ion exchange chromatography | HiTrap Q HP | 20 mM Tris-HCl pH 8.0, 10% glycerol, 1 mM ADP, 2 mM MgSO4, 0.02% NaN3 + 0.95 mM n-tridecyl-beta-D-maltoside (TDM) | Eluted with 0-1 M NaCl gradient, complex eluted at 0.35-0.40 mM NaCl. Pooled fractions dialyzed against buffer with 0.95 mM TDM and concentrated to 22 mg/mL on Vivaspin Q mini H spin column. |

**Final sample**: 10 mg/mL in 20 mM Tris-HCl pH 8.0, 10% glycerol, 1 mM ADP, 2 mM MgSO4, 0.02% NaN3, 5.7 mM TDM, 1 mM AMP-PNP


## Crystallization

### doi/10.1073##pnas.1011099107

| Parameter | Value |
|---|---|
| Method | Microbatch under oil |
| Protein sample | Bovine F1-c-ring complex at 10 mg/mL with 5.7 mM TDM, 1 mM AMP-PNP |
| Reservoir | 14-16.5% PEG 4600, 100 mM Hepes pH 7.0, 50 mM K2HPO4 pH 7.0 |
| Mixing ratio | 2 uL protein + 2 uL reservoir |
| Temperature | 23 C |
| Growth time | 42 days |
| Cryoprotection | 50 mM Hepes pH 7.0, 25 mM K2HPO4 |
| Notes | Crystals harvested and analyzed by SDS-PAGE confirmed all subunits of F1-c-ring complex present and undegraded. Four crystals were harvested, washed three times in buffer, dissolved and analyzed. |


## Biological / Functional Insights

### c8-ring stoichiometry in vertebrates

The bovine F-ATPase c-ring contains 8 c-subunits, establishing the first c-ring structure from a higher eukaryote. This contrasts with fungal (c10 in S. cerevisiae), eubacterial (c10-c15 in I. tartaricus), and plant chloroplast (c14 in S. oleracea) rings. The c-subunit sequences are nearly identical across vertebrates and highly conserved in invertebrates, suggesting c8-rings are universal in ~50,000 vertebrate species and many of the ~2 million invertebrate species.

### Bioenergetic cost of ATP synthesis

With a c8-ring, each 360 degree rotation of the central stalk (producing 3 ATP) requires 8 protons (one per c-subunit glutamate). Therefore 8/3 = 2.67 protons per ATP. Including the electrogenic exchange of ATP for ADP by the ADP/ATP translocase (one charge) and the electroneutral phosphate/proton symport (one proton) adds one more proton, giving a total of 3.7 protons per ATP exported to the cytoplasm. The P/O ratio is 10/3.7 = 2.7 for NADH and 6/3.7 = 1.6 for succinate, close to experimental values of 2.5 and 1.5.

### Cardiolipin binding and c8-ring stabilization

The c8-ring has eight trimethylated Lys43 residues that likely mark binding sites for cardiolipin, an abundant inner mitochondrial membrane lipid with no head group. Unlike larger rings (c10+), the c8-ring outer ring has gaps between C-terminal alpha-helices that expose the inner ring to the lipid bilayer. Each bound cardiolipin with two acyl side chains could help strengthen the c8-ring by cross-linking adjacent c-subunits. The Lys43 trimethylation is conserved across Animalia.


## Cross-References

- [Bovine F1-ATPase](/xray-mp-wiki/proteins/pumps-atpases/bovine-f1-atpase/) — Catalytic domain of the same ATP synthase complex
- [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) — Cardiolipin binds c8-ring external surface and stabilizes the ring structure
- [F1-ATPase Rotary Catalytic Mechanism](/xray-mp-wiki/concepts/f1-atpase-rotary-mechanism/) — Rotary mechanism of ATP synthesis coupled to proton flow through c-ring
- [Symmetry Mismatch in Rotary Motors](/xray-mp-wiki/concepts/symmetry-mismatch-rotary-motor/) — Mismatch between c8-ring (8-fold) and catalytic domain (3-fold) symmetry
- [Rotary ATPase Mechanism](/xray-mp-wiki/concepts/rotary-atpase-mechanism/) — Broader rotary catalysis mechanism context
