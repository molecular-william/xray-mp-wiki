---
title: Human D₂ Dopamine Receptor (DRD2)
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature25758]
verified: false
---

# Human D₂ Dopamine Receptor (DRD2)

## Overview

The human D₂ dopamine receptor (DRD2) is a class A G protein-coupled receptor that serves as the primary target for both typical and atypical antipsychotic drugs. DRD2 mediates dopamine's actions in reward, addiction, coordinated movement, metabolism, and hormonal secretion. Dysregulation of the dopaminergic system through DRD2 has been implicated in schizophrenia, Parkinson's disease, depression, and ADHD. This structure (PDB: 6C38, 2.9 A) represents the first high-resolution crystal structure of DRD2 in complex with the atypical antipsychotic risperidone, revealing a unique mode of antipsychotic drug binding and defining structural determinants essential for risperidone and related drugs at DRD2. The structure confirms the inactive state of DRD2, characterized by a maintained ionic lock between Arg3.50 and Glu6.30.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature25758 | 6C38 | 2.9 A | P2₁2₁2₁ | Human DRD2 long variant (D₂L) with N-terminal truncation (residues 1-34 deleted), T4 lysozyme (T4L, residues 12-161) fused into ICL3 (replacing residues 223-361), C-terminal truncation (residues unknown), thermostabilizing mutations I122^3.40A, L375^6.37A, L379^6.41A | Risperidone |

## Expression and Purification

### Purification Workflow

- **Expression system**: Sf9 insect cells (Spodoptera fragiperda, Expression Systems)
- **Expression construct**: DRD2-T4L fusion with N-terminal HA tag, Flag tag, 10xHis tag, TEV protease site; mutations I122A, L375A, L379A; N-terminal truncation (1-34); ICL3 replaced by T4L (12-161)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Baculovirus expression in Sf9 cells (Bac-to-Bac system, Invitrogen) | — | Not specified | 48 h expression; DRD2-T4L gene in modified pFastBac1 vector |
| Cell lysis and membrane preparation | Repeated washing and centrifugation with hypotonic and high salt buffers | — | Low salt: 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl; High salt: 1.0 M NaCl, 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl | Hypotonic wash (1x), high salt washes (3x) |
| Solubilization | DDM and CHS solubilization | — | 10 mM HEPES pH 7.5, 150 mM NaCl, 1% DDM, 0.2% CHS, 20 uM risperidone | 2 hr at 4°C; 10 uM risperidone included in all subsequent buffers |
| Affinity chromatography | TALON IMAC resin (Clontech) | — | 20 mM imidazole pH 7.5, 800 mM NaCl, 0.1% DDM, 0.02% CHS, 10 uM risperidone | Overnight incubation at 4°C; wash with Wash Buffer I and II |
| Elution | Imidazole elution from TALON resin | — | 50 mM HEPES pH 7.5, 500 mM NaCl, 250 mM imidazole, 50 uM risperidone, 10% glycerol, 0.05% DDM, 0.01% CHS | 3-4 column volumes |
| Imidazole removal | PD MiniTrap G-25 column (GE Healthcare) | — | Not specified | Imidazole removed before TEV protease treatment |
| Deglycosylation | PNGase treatment | — | Not specified | Overnight at 4°C; N-linked glycans removed |
| Tag cleavage | His-tagged TEV protease | — | Not specified | Overnight at 4°C; His6 tag cleaved |
| Final buffer exchange | PD MiniTrap G-25 column (GE Healthcare) | — | 20 mM HEPES pH 7.5, 150 mM NaCl, 0.05% DDM, 0.01% CHS | Final sample buffer |


## Crystallization

### doi/10.1038##nature25758

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | DRD2-T4L-risperidone complex at 12 mg/mL |
| Temperature | 20 C |
| Growth time | Not specified |
| Notes | 20 crystals used for data collection at APS GMCA-CAT 23ID-B/D (10 um microfocus beam). Space group P2₁2₁2₁. Unit cell: 50.98 x 72.52 x 151.31 A. Resolution range 30.00-2.90 A. R-work 22.6%, R-free 24.9%. 1948 DRD2 atoms, 1176 T4L atoms, 30 risperidone atoms, 82 lipid/other atoms.
 |


## Biological / Functional Insights

### Inactive-state conformation of DRD2

The DRD2-risperidone structure reveals an inactive-state conformation of the
D₂ dopamine receptor. Key features include: (1) no substantial outward movement
of the intracellular end of TM VI compared to inactive beta2 AR and A2A AR
structures; (2) the NPxxY motif Tyr7.53 and DRY motif Arg3.50 adopt positions
identical to homologous residues in inactive beta2 AR and A2A AR structures;
(3) the ionic lock salt bridge between Arg3.50 and Glu6.30 is maintained.
These findings are consistent with risperidone acting as an inverse agonist
that stabilizes the inactive state of DRD2.

### Risperidone binding mode and deep hydrophobic pocket

Risperidone displays a unique binding mode compared to substituted benzamides
eticlopride (DRD3) and nemonapride (DRD4). The benzisoxazole moiety extends
into a deep binding pocket defined by helices III, V, and VI, interacting
with Cys118^3.36, Thr119^3.37, Ser197^5.46, Phe198^5.47, Phe382^6.44,
Phe390^6.52, and Trp386^6.48. This deep hydrophobic subpocket lies below
the orthosteric site and is not engaged by eticlopride or nemonapride in
DRD3 or DRD4 structures. Additionally, a hydrophobic pocket above the
orthosteric site encloses risperidone's tetrahydropyridopyrimidinone moiety,
while Asp114^3.32 forms a salt bridge with risperidone's tertiary amine.
Alanine mutagenesis of contact residues reduces risperidone affinity by
more than tenfold.

### DRD2 extended binding pocket (DRD2-EBP)

Comparison of ligand binding pockets across D2-like receptors reveals a
unique extended binding pocket (DRD2-EBP) defined by four key residues:
Val/Phe^2.61, Trp^EL1, Phe/Leu^3.28, and Tyr/Val^7.35. The DRD2-EBP
extends toward the extracellular part of TM VII, consisting of EL1 and
the junction of helices I, II, and VII. This differs from the DRD3-EBP
(formed by EL1-EL2 junction and interface of helices II, III, VII) and
DRD4-EBP (deep cleft between TMs II and III, defined by Phe91^2.61/Leu111^3.28).
The DRD4-EBP structure enabled structure-based discovery of highly specific
agonists.

### Hydrophobic patch regulating risperidone binding kinetics

Trp100^EL1, Leu94^2.64, and Ile184^EL2 form a hydrophobic patch that
narrows the DRD2 binding pocket and regulates risperidone binding kinetics.
Trp100^EL1 side chain forms extensive hydrophobic contacts with Leu94^2.64
and Ile184^EL2. The W100^EL1A mutation reduces risperidone residence time
from 233 min to 28 min. The double mutant L94^2.64A/I184^EL2A reduces
residence time to 6 min. This patch also affects aripiprazole,
N-methylspiperone, and nemonapride dissociation kinetics.

### Structural comparison with DRD3 and DRD4

The DRD2-risperidone structure was compared with related D2-like receptor
structures: DRD3-eticlopride (PDB: 3PBL) and DRD4-nemonapride (PDB: 5WIU).
Striking differences were found around residues Val/Phe^2.61, Trp^EL1,
Phe/Leu^3.28, and Tyr/Val^7.35, defining the extended binding pocket
differences across the D2-like family. The structure also aligns with
inactive beta2 AR (PDB: 2RH1) and inactive A2A AR (PDB: 3REY), confirming
the inactive state of DRD2.


## Cross-References

- [T4 Lysozyme (T4L)](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) — T4L fusion into ICL3 enabled crystallization of DRD2
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for DRD2 solubilization and purification
- [Cholesteryl Hemisuccinate (CHS)](/xray-mp-wiki/reagents/lipids/cholesteryl-hemisuccinate/) — Lipid additive used with DDM for DRD2 stabilization
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer component in all DRD2 purification buffers
- [Risperidone](/xray-mp-wiki/reagents/ligands/risperidone/) — Atypical antipsychotic ligand co-crystallized with DRD2
- [Baculovirus Expression System in Sf9 Cells](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) — Expression system used for DRD2-T4L construct
- [Human Beta2-Adrenergic Receptor (beta2 AR)](/xray-mp-wiki/proteins/beta2-adrenergic-receptor/) — Structural comparison receptor for DRD2 inactive state confirmation
- [GPCR Inactive Conformation](/xray-mp-wiki/concepts/gpcr-inactive-conformation/) — DRD2 structure confirms inactive state with ionic lock intact
