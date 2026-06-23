---
title: "LpCopA (Copper-Transporting P-type ATPase from Legionella pneumophila)"
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature10191, doi/10.1038##NSMB.2721]
verified: false
---

# LpCopA (Copper-Transporting P-type ATPase from Legionella pneumophila)

## Overview

LpCopA is a copper-transporting P_IB-type ATPase from the bacterium Legionella pneumophila. It is a primary active transporter that exports copper ions from the cytoplasm using ATP hydrolysis, playing a critical role in copper homeostasis and bacterial virulence. LpCopA consists of a single polypeptide chain with eight transmembrane helices and three cytoplasmic domains (A, N, and P). The paper reveals a unique ion-release pathway involving conserved proline residues (Pro94 and Pro710) that enable a proline-dependent opening mechanism for copper egress, distinguishing P_IB ATPases from other P-type ATPases.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature10191 | 3RFU | 3.2 | P1 and P2_12_12_1 | Full-length LpCopA from Legionella pneumophila (residues 79-731) in E2.Pi state trapped with AlF4- | AlF4- (aluminum fluoride) phosphate analog, Mg2+ |
| doi/10.1038##NSMB.2721 | 3RFU | 2.0 A | C2 | Full-length LpCopA from Legionella pneumophila in E2.Pi state trapped with AlF4- | AlF4- (aluminum fluoride) phosphate analog, Mg2+, Cu+ transport site |
| doi/10.1038##NSMB.2721 | 3B9B | 2.0 A | P2_12_12_1 | Full-length LpCopA from Legionella pneumophila in E2P state trapped with BeF3- | BeF3- (beryllium fluoride) phosphate analog, Mg2+ |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Full-length LpCopA from Legionella pneumophila

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Solubilization | Detergent solubilization | -- | -- + -- | LpCopA solubilized from cell membranes |


## Crystallization

### doi/10.1038##NSMB.2721

| Parameter | Value |
|---|---|
| Method | HiLiDe (Hydrophobic Interaction-Driven) crystallization |
| Protein sample | LpCopA in E2-BeF3- state |
| Reservoir | -- |
| Temperature | -- |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | Two crystal forms obtained: C2 (high-resolution) and P2_12_12_1 (lower resolution). Proteins arranged as stacked bilayers held together by hydrophobic interactions between membrane-spanning regions, characteristic of the HiLiDe method.
 |


## Biological / Functional Insights

### Unique ion-release pathway with proline-dependent opening mechanism

LpCopA utilizes a unique ion-release pathway that involves two conserved proline residues, Pro94 and Pro710, which act as hinges enabling a proline-dependent opening mechanism. Molecular dynamics simulations reveal that the release pathway includes an internal water network connecting the transmembrane copper-binding site to the extracellular side. Glu189 plays a key role in the release pathway, with water molecules showing prolonged residency times near this residue during the E2.Pi state simulation. Mutations of Pro94 to Ala (P94A) or Pro710 to Ala (P710A) alter the hydration patterns and pore radius of the release pathway, suggesting that the proline kinks are essential for pathway opening.

### Structural comparison with SERCA reveals conserved domain rearrangements

Structural comparison of LpCopA with [SERCA1a (Sarcoplasmic Reticulum Ca2+-ATPase)](/xray-mp-wiki/proteins/pumps-atpases/serca1a/) in the E2P and E2.Pi states reveals conserved large-scale domain rearrangements. In both proteins, the A-domain shifts relative to the P-domain between the E2P and E2.Pi conformations. The catalytic aspartate (Asp426 in LpCopA, Asp351 in SERCA) is coordinated by Mg2+ and the phosphate analog (BeF3- or AlF4-) in the phosphorylation site. The overall domain arrangement in the E2P state is highly similar between LpCopA and SERCA, but the transmembrane ion-release pathway is unique to P_IB ATPases.

### Functional analysis of release pathway mutants

In vitro ATPase assays and in vivo copper susceptibility assays were performed on various LpCopA mutants. The D426N mutation (catalytic aspartate to asparagine) abolishes ATPase activity, confirming its essential role. Release pathway mutants P94A, P710A, M717V, M711L, A714T, E189N, and E189Q show reduced but not abolished activity, suggesting they affect the ion-release step rather than the catalytic cycle itself. The M717V mutation (high-affinity copper coordinator) retains some activity. The in vivo copper susceptibility assay shows that wild-type LpCopA confers copper resistance, while D426N and release pathway mutants exhibit increased sensitivity to copper in the growth medium.

### P_IB-ATPase sequence conservation across subfamilies

Sequence and secondary structure conservation analysis of P_IB-1 (CopA), P_IB-2 (ZntA), and P_IB-4 (CtpD) ATPases reveals conserved structural features across subfamilies. The N-terminal segment containing helices MA and MB shows weak sequence conservation but conserved secondary structure. Pro94 position is conserved across P_IB ATPases, supporting its functional importance. The transmembrane copper-binding site residues (including Met717, Met711, Ala714) are conserved in copper-transporting P_IB ATPases.


## Cross-References

- [SERCA1a (Sarcoplasmic Reticulum Ca2+-ATPase 1a)](/xray-mp-wiki/proteins/pumps-atpases/serca1a/) — Structural comparison of E2P and E2.Pi states between LpCopA and SERCA1a
- [P-type ATPase Family](/xray-mp-wiki/concepts/protein-families/p-type-atpase/) — LpCopA is a member of the P_IB subfamily of P-type ATPases
- [Phosphoenzyme E2P State](/xray-mp-wiki/concepts/enzyme-mechanisms/phosphoenzyme-e2p-state/) — LpCopA E2P and E2.Pi states captured with BeF3- and AlF4- phosphate analogs
- [Large Domain Motion in P-type ATPases](/xray-mp-wiki/concepts/structural-mechanisms/large-domain-motion-in-p-type-atpases/) — A-domain movement relative to P-domain conserved between LpCopA and SERCA
- [Molecular Dynamics Simulation](/xray-mp-wiki/methods/structure-determination/molecular-dynamics-simulation/) — MD simulations used to analyze release pathway dynamics and hydration patterns
- [AlF4 (Aluminum Fluoride)](/xray-mp-wiki/reagents/ligands/alf4/) — Phosphate analog used to trap E2.Pi state
- [BeF3 (Beryllium Fluoride)](/xray-mp-wiki/reagents/ligands/bef3/) — Phosphate analog used to trap E2P state
- [HiLiDe Crystallization](/xray-mp-wiki/methods/crystallization/hilide-crystallization/) — Crystallization method used for LpCopA structures
- [MIRAS](/xray-mp-wiki/methods/structure-determination/miras/) — Method used in structure determination or purification
