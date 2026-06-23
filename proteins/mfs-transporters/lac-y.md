---
title: Lactose Permease of Escherichia coli (LacY)
created: 2026-06-02
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1088196, doi/10.1038##SJ.EMBOJ.7601028, doi/10.1073##pnas.1105687108, doi/10.1073##pnas.1324141111, doi/10.1073##pnas.1509854112, doi/10.1073##pnas.1615414113, doi/10.1073##pnas.1801774115, doi/10.1073##pnas.0707688104]
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
| doi/10.1073##pnas.0707688104 | not specified | 3.6 A | P2_12_12_1 | Wild-type LacY | none (apo, inward-facing conformation) |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: LacY from E. coli, heterologously expressed in various strains including C43(DE3)

### Purification Workflow

*Source: doi/10.1038##SJ.EMBOJ.7601028*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Cell lysis and membrane fractionation | not specified | not specified + not specified | Expression and purification carried out as described (Abramson et al, 2003) |
| Solubilization | Detergent solubilization | not specified | not specified + DDM | Solubilization modified by increasing detergent:protein ratio to 2.5:1.0 (wt/wt); 10 mg protein/ml |
| Purification | Affinity chromatography | not specified | not specified + DDM | As described (Abramson et al, 2003) |

### Purification Workflow

*Source: doi/10.1073##pnas.0707688104*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Aggregate removal | Ultracentrifugation | -- | Not specified + -- | Protein samples centrifuged at 327,205 x g for 1 h to remove aggregates |
| Crystallization setup | Hanging drop vapor diffusion | -- | [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 8.0 + [CHAPS](/xray-mp-wiki/reagents/detergents/chapso/) | Mixed with reservoir (HEPES pH 8.0, ammonium sulfate, PEG 400) plus CHAPS and 1,6-hexanediol; phospholipid content manipulated for crystallization |


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

### doi/10.1073##pnas.0707688104

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | Wild-type LacY (centrifuged to remove aggregates) |
| Reservoir | 0.1 M [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 8.0, 0.1 M ammonium sulfate, 29-31% [PEG 400](/xray-mp-wiki/reagents/additives/peg-400/), 8 mM [CHAPS](/xray-mp-wiki/reagents/detergents/chapso/), 1% 1,6-hexanediol |
| Mixing ratio | 1:1 (protein:reservoir mix) |
| Temperature | 23 C |
| Growth time | 3-4 days |
| Cryoprotection | Direct freezing in liquid nitrogen |
| Notes | Phospholipid content adjusted during crystallization to enable wild-type LacY crystallization. Data collected at ALS BL8.2.1 and Swiss Light Source. Space group P2_12_12_1. Structure solved by molecular replacement using 1PV7. Also contains 5 mM TDG (ligand) in crystallization drop, though no clear sugar density observed.
 |


## Biological / Functional Insights

### Induced fit mechanism for sugar binding

The ligand-free LacY structures reveal that the sugar-binding site is not in the correct configuration to bind galactopyranosides in the absence of substrate. Arg144 (helix V) forms a salt bridge with Glu126 (helix IV) instead of interacting with Glu269 (helix VIII). Helix VIII is slightly displaced from the cavity. Upon sugar binding, a rearrangement occurs: Trp151 (helix V) initially recognizes the galactopyranosyl ring through hydrophobic stacking, which orients the sugar for recognition by Arg144, Glu126, and Glu269. Arg144 then moves to form a bi-dentate H-bond with the O4 and O3 groups of the galactopyranosyl ring. Glu269 moves out of a hydrophobic environment, deprotonates, and forms a salt bridge with Arg144 while interacting with the sugar. This induced fit mechanism means that substrate binding drives the formation of the binding site and the initial step in H+ translocation.

### Glu269 as the primary protonation site

Glu269 (helix VIII) is the key residue coupling sugar binding to H+ translocation. In the ligand-free conformation, Glu269 is located in a relatively hydrophobic environment surrounded by Cys148, Trp151, Asn272, and Met323, suggesting it is protonated. Substrate binding drives the deprotonation of Glu269 as the initial step in H+ translocation. The H+ released from Glu269 may be delivered to His322 (helix X) through a tightly bound water molecule on the O3 group of the galactopyranosyl moiety or bound to His322. This mechanism establishes that protonation precedes ligand binding and that sugar binding triggers the deprotonation event.

### H+ translocation pathway

The residues involved in H+ translocation (Glu126, Glu269, His322, Arg302, His325) are aligned parallel to the plane of the membrane at a level similar to the sugar-binding site. At pH 5.6, Glu325 moves from a hydrophobic environment and becomes closer to His322, Tyr236, and Arg302, forming a salt bridge with His322. This H-bond/salt bridge network suggests that protonated His322 may transfer H+ directly to Glu325. H+ translocation through LacY does not involve a pathway through the molecule as in bacteriorhodopsin; rather, H+ can be released directly into either the inward- or outward-facing cavity, explaining how lactose-driven H+ translocation can occur in both directions across the membrane via the same residues.

### Six essential residues for ligand binding and H+ translocation

Only six amino acyl side chains are irreplaceable in LacY. Arg144 (helix V) and Glu126 (helix IV) are essential for ligand binding, while Glu269 (helix VIII), Arg302 (helix IX), His322, and Glu325 (helix X) are essential for H+ translocation. Arg144 forms a bi-dentate H-bond with the O4 and O3 atoms of the galactopyranosyl ring. These residues define the functional core of the MFS transporter mechanism.

### Wild-type LacY structure reveals inward-facing conformation

The crystal structure of wild-type LacY at 3.6 A resolution reveals the same global fold as the C154G mutant — organized into two six-helix bundles with twofold pseudosymmetry separated by a large interior hydrophilic cavity open only to the cytoplasmic side. The sugar-binding residues (Glu126, Arg144, Trp151, Glu269) and H+ translocation residues (Tyr236, Arg302, His322, Glu325) face the internal cavity. The inward-facing conformation represents the lowest free-energy state, suggesting that the rate-limiting step for transport is the conformational change leading to the outward-facing conformation.

### Cys-154 role in helix I-helix V interaction

In wild-type LacY, the sulfur atom of Cys-154 (helix V) forms two hydrogen bonds with the carbonyl oxygens of Phe-21 and Gly-24 (helix I), respectively. In the C154G mutant, this space is empty, suggesting less intimate contact between helices I and V. Cys-154 is located below the sugar-binding residues (Arg144, Cys-148, Trp151) and above the periplasmic gateway (Pro28, Pro31, Ile32, His35 on helix I; Gln241, Gln242, Ala244, Asn245, Thr248 on helix VII). The mutation to glycine (C154G) severely impairs sugar translocation without affecting ligand binding, confirming that the C154G mutation locks LacY in an intermediate state.

### Periplasmic gateway in wild-type LacY

The wild-type LacY structure identified a periplasmic gateway formed by residues on helix I (Pro28, Pro31, Ile32, His35) and helix VII (Gln241, Gln242, Ala244, Asn245, Thr248). Ile32 (helix I) is close to Asn245 (helix VII), closing the periplasmic side. This gateway must open for the outward-facing conformation to form. The inward-facing conformation observed in the wild-type structure is consistent with the alternating access model, where the sugar-binding site is alternately accessible to either side of the membrane.

### Phospholipid content as key to membrane protein crystallization

Crystallization of wild-type LacY required manipulation of phospholipid (PL) content. This was accomplished by adding CHAPS and 1,6-hexanediol to the crystallization drop. The intrinsic hydrophobic properties of membrane proteins and the difficulty of maintaining homogeneous protein-detergent-PL complexes represent a bottleneck to crystallization. This strategy of adjusting PL content may be broadly applicable to other membrane protein crystallization efforts.


## Cross-References

- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) — LacY is the paradigm member of the MFS family of transporters
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — LacY operates by alternating access between inward- and outward-facing conformations
- [Rocker-Switch Mechanism in MFS Transporters](/xray-mp-wiki/concepts/structural-mechanisms/rocker-switch-mechanism/) — MFS-specific variant of alternating access mechanism
- [Substrate-Protonation Coupling in MFS Symporters](/xray-mp-wiki/concepts/transport-mechanisms/substrate-protonation-coupling/) — LacY couples galactoside binding to H+ translocation
- [Conformational Dynamics in MFS Transporters](/xray-mp-wiki/concepts/transport-mechanisms/conformational-dynamics-mfs/) — LacY exhibits multiple conformational states during transport cycle
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for LacY purification and crystallization
- [2-(N-Morpholino)ethanesulfonic Acid (MES)](/xray-mp-wiki/reagents/buffers/mes/) — Buffer used for pH 5.6 crystal preparation
- [PEG 400 (Polyethylene Glycol 400)](/xray-mp-wiki/reagents/additives/peg-400/) — Crystallization precipitant used in LacY crystal soaking
