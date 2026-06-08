---
title: Lactose Permease of Escherichia coli (LacY)
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1088196, doi/10.1038##SJ.EMBOJ.7601028, doi/10.1073##pnas.1105687108, doi/10.1073##pnas.1324141111, doi/10.1073##pnas.1509854112, doi/10.1073##pnas.1615414113, doi/10.1073##pnas.1801774115]
verified: false
---

# Lactose Permease of Escherichia coli (LacY)

## Overview

Lactose permease (LacY) from Escherichia coli is a galactoside/H+ symporter and the paradigm member of the Major Facilitator Superfamily (MFS) of transporters. LacY catalyzes the coupled stoichiometric translocation of a D-galactopyranoside with an H+, utilizing the free energy released from downhill translocation of H+ to drive accumulation of galactopyranosides against a concentration gradient. The protein consists of 12 transmembrane helices organized in two pseudo-symmetrical alpha-helical bundles, with the N- and C-terminal six-helix domains forming a large internal cavity open to the cytoplasm. LacY has been one of the most intensively studied membrane transport proteins, serving as a structural template for understanding the entire MFS family and ion-coupled secondary transport mechanisms.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.1088196 | 2JHL | 3.5 A | P21 | Wild-type LacY, C154G mutant | not specified (outward-facing conformation) |
| doi/10.1038##SJ.EMBOJ.7601028 | not specified | 2.95 A | P43212 | Wild-type LacY, ligand-free | none (outward-facing, pH 6.5) |
| doi/10.1038##SJ.EMBOJ.7601028 | not specified | 3.3 A | P43212 | Wild-type LacY, ligand-free | none (outward-facing, pH 5.6) |
| doi/10.1038##SJ.EMBOJ.7601028 | 1PV7 | 2.2 A | not specified | Wild-type LacY | TDG (thiodigalactoside) |
| doi/10.1073##pnas.1105687108 | 3F6D | 2.8 A | not specified | C117S, C148A, C154V, C176S, C234S, C333S, C353A, C355A LacY | o-NPG (o-nitrophenyl-alpha-D-galactopyranoside) |
| doi/10.1073##pnas.1324141111 | 3B80 | 2.8 A | not specified | LacY G46W/G262W double-Trp mutant | o-NPG (o-nitrophenyl-alpha-D-galactopyranoside) |
| doi/10.1073##pnas.1509854112 | not specified | not specified | not specified | LacY G46W/G262W double-Trp mutant | alpha-NPG (alpha-nitrophenyl-alpha-D-galactopyranoside) |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: LacY from E. coli, heterologously expressed in various strains including C43(DE3)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Cell lysis and membrane fractionation | not specified | not specified + not specified | Expression and purification carried out as described (Abramson et al, 2003) |
| Solubilization | Detergent solubilization | not specified | not specified + DDM | Solubilization modified by increasing detergent:protein ratio to 2.5:1.0 (wt/wt); 10 mg protein/ml |
| Purification | Affinity chromatography | not specified | not specified + DDM | As described (Abramson et al, 2003) |


## Crystallization

### doi/10.1038##SJ.EMBOJ.7601028

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | Wild-type LacY in detergent |
| Reservoir | not specified (same conditions as orthorhombic crystals from Abramson et al, 2003) |
| Temperature | not specified |
| Growth time | not specified |
| Notes | Tetragonal crystal form (P43212) obtained at late equilibrium stage. pH 6.5 structure at 2.95 A resolution. |

| Parameter | Value |
|---|---|
| Method | Crystal soaking for cryoprotection |
| Protein sample | Wild-type LacY tetragonal crystals |
| Reservoir | 100 mM MES (pH 5.6)/36% PEG 400/200 mM CaCl2/3% 1,6-hexanediol/8 mM CHAPSO |
| Temperature | 100 K (frozen) |
| Growth time | not specified (crystals soaked for 2 min before freezing) |
| Notes | pH 5.6 structure at 3.3 A resolution. Diffraction data collected at Swiss Light Source beam-line X06SA. |

### doi/10.1073##pnas.1105687108

| Parameter | Value |
|---|---|
| Method | Vapor diffusion crystallization |
| Protein sample | Cysteine-less LacY (C117S, C148A, C154V, C176S, C234S, C333S, C353A, C355A) |
| Reservoir | not specified |
| Temperature | not specified |
| Growth time | not specified |
| Notes | Structure with affinity inactivator o-NPG. PDB 3F6D. |


## Biological / Functional Insights

### Induced fit mechanism for sugar binding

The ligand-free LacY structures reveal that the sugar-binding site is not in the correct configuration to bind galactopyranosides in the absence of substrate. Arg144 (helix V) forms a salt bridge with Glu126 (helix IV) instead of interacting with Glu269 (helix VIII). Helix VIII is slightly displaced from the cavity. Upon sugar binding, a rearrangement occurs: Trp151 (helix V) initially recognizes the galactopyranosyl ring through hydrophobic stacking, which orients the sugar for recognition by Arg144, Glu126, and Glu269. Arg144 then moves to form a bi-dentate H-bond with the O4 and O3 groups of the galactopyranosyl ring. Glu269 moves out of a hydrophobic environment, deprotonates, and forms a salt bridge with Arg144 while interacting with the sugar. This induced fit mechanism means that substrate binding drives the formation of the binding site and the initial step in H+ translocation.

### Glu269 as the primary protonation site

Glu269 (helix VIII) is the key residue coupling sugar binding to H+ translocation. In the ligand-free conformation, Glu269 is located in a relatively hydrophobic environment surrounded by Cys148, Trp151, Asn272, and Met323, suggesting it is protonated. Substrate binding drives the deprotonation of Glu269 as the initial step in H+ translocation. The H+ released from Glu269 may be delivered to His322 (helix X) through a tightly bound water molecule on the O3 group of the galactopyranosyl moiety or bound to His322. This mechanism establishes that protonation precedes ligand binding and that sugar binding triggers the deprotonation event.

### H+ translocation pathway

The residues involved in H+ translocation (Glu126, Glu269, His322, Arg302, His325) are aligned parallel to the plane of the membrane at a level similar to the sugar-binding site. At pH 5.6, Glu325 moves from a hydrophobic environment and becomes closer to His322, Tyr236, and Arg302, forming a salt bridge with His322. This H-bond/salt bridge network suggests that protonated His322 may transfer H+ directly to Glu325. H+ translocation through LacY does not involve a pathway through the molecule as in bacteriorhodopsin; rather, H+ can be released directly into either the inward- or outward-facing cavity, explaining how lactose-driven H+ translocation can occur in both directions across the membrane via the same residues.

### Six essential residues for ligand binding and H+ translocation

Only six amino acyl side chains are irreplaceable in LacY. Arg144 (helix V) and Glu126 (helix IV) are essential for ligand binding, while Glu269 (helix VIII), Arg302 (helix IX), His322, and Glu325 (helix X) are essential for H+ translocation. Arg144 forms a bi-dentate H-bond with the O4 and O3 atoms of the galactopyranosyl ring. These residues define the functional core of the MFS transporter mechanism.


## Cross-References

- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/mfs-transporter/) — LacY is the paradigm member of the MFS family of transporters
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — LacY operates by alternating access between inward- and outward-facing conformations
- [Rocker-Switch Mechanism in MFS Transporters](/xray-mp-wiki/concepts/rocker-switch-mechanism/) — MFS-specific variant of alternating access mechanism
- [Substrate-Protonation Coupling in MFS Symporters](/xray-mp-wiki/concepts/substrate-protonation-coupling/) — LacY couples galactoside binding to H+ translocation
- [Conformational Dynamics in MFS Transporters](/xray-mp-wiki/concepts/conformational-dynamics-mfs/) — LacY exhibits multiple conformational states during transport cycle
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for LacY purification and crystallization
- [2-(N-Morpholino)ethanesulfonic Acid (MES)](/xray-mp-wiki/reagents/buffers/mes/) — Buffer used for pH 5.6 crystal preparation
- [PEG 400 (Polyethylene Glycol 400)](/xray-mp-wiki/reagents/additives/peg-400/) — Crystallization precipitant used in LacY crystal soaking
