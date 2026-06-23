---
title: "Transient Receptor Potential Vanilloid 2 (TRPV2)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41594-018-0059-z]
verified: false
---

# Transient Receptor Potential Vanilloid 2 (TRPV2)

## Overview

TRPV2 is a transient receptor potential vanilloid channel belonging to the TRPV subfamily of TRP channels. Unlike the highly Ca²⁺-selective [Epithelial Calcium Channel TRPV5](/xray-mp-wiki/proteins/voltage-gated-channels/trpv5/)/TRPV6, TRPV2 is a non-selective cation channel that is activated by heat, cannabinoids, and 2-aminoethoxydiphenyl borate (2-APB). TRPV2 forms a domain-swapped homotetramer where each subunit comprises six transmembrane helices (S1-S6) with the voltage-sensor-like domain (S1-S4) interacting with the pore domain (S5-S6) of the neighboring protomer. The channel possesses two activation gates: one at the selectivity filter (SF gate) and another at the S6 helical bundle crossing (common gate). Crystal structures of rabbit TRPV2 reveal that [Resiniferatoxin (RTx)](/xray-mp-wiki/reagents/ligands/resiniferatoxin/) binding induces a two-fold symmetric opening of the selectivity filter gate wide enough for permeation of large organic cations.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41594-018-0059-z | 6BWJ | 3.1 A | P 2 2_1 2_1 | Rabbit miTRPV2_QM (minimal TRPV2 construct with quadruple mutations F470S, L505M, L508T, Q528E), residues 57-561 and 583-722, C-terminal FLAG affinity tag | [Resiniferatoxin (RTx)](/xray-mp-wiki/reagents/ligands/resiniferatoxin/) and Ca²⁺ |
| doi/10.1038##s41594-018-0059-z | 6BWM | 3.9 A | P 2 2_1 2_1 | Rabbit miTRPV2 (minimal construct), residues 57-561 and 583-722, C-terminal [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) | Ca²⁺ |

## Expression and Purification

- **Expression system**: Sf9 insect cells, Bac-to-Bac baculovirus system
- **Construct**: Codon-optimized gene for full-length rabbit TRPV2. Minimal construct miTRPV2 (residues 57-561 and 583-722) cloned into pFastBac vector with C-terminal FLAG affinity tag. Quadruple mutant miTRPV2_QM (F470S, L505M, L508T, Q528E) used for RTx-sensitive crystallization. Selenomethionine-labeled protein expressed in ESF 921 Delta Series methionine-deficient Sf9 media.


### Purification Workflow

- **Expression system**: Sf9 insect cells
- **Expression construct**: miTRPV2, C-terminal [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/)
- **Tag info**: [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), removed by [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/)

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Sonication | -- | 50 mM TRIS pH 8, 150 mM NaCl, 2 mM CaCl₂, 1 µg/ml leupeptin, 1.5 µg/ml pepstatin, 0.84 µg/ml aprotinin, 0.3 mM PMSF, 14.3 mM β-mercaptoethanol, DNAseI + -- | 3 × 30 pulses |
| Solubilization | Detergent extraction | -- | Buffer A supplemented with 40 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) and 4 mM [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 40 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 4 mM [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | 1 hour at 4°C. Insoluble material removed by centrifugation (8,000g, 30 min). |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Anti-FLAG resin | Anti-FLAG resin | Buffer B (50 mM TRIS pH 8, 150 mM NaCl, 2 mM CaCl₂, 0.1 mM [DMNG](/xray-mp-wiki/reagents/detergents/dmng/), 0.1 mM [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 0.1 mg/ml [DMPC](/xray-mp-wiki/reagents/lipids/dmpc/), 10 mM [DTT](/xray-mp-wiki/reagents/additives/dtt/)) + 0.1 mM [DMNG](/xray-mp-wiki/reagents/detergents/dmng/), 0.1 mM [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Wash with Buffer B, elute with Buffer C containing 0.1 mg/ml FLAG peptide |
| Tag cleavage | [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) cleavage | -- | 50 mM TRIS pH 8, 150 mM NaCl, 2 mM CaCl₂, 0.1 mM [DMNG](/xray-mp-wiki/reagents/detergents/dmng/), 0.1 mM [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 0.1 mg/ml [DMPC](/xray-mp-wiki/reagents/lipids/dmpc/), 10 mM [DTT](/xray-mp-wiki/reagents/additives/dtt/), 3 mM TCEP + 0.1 mM [DMNG](/xray-mp-wiki/reagents/detergents/dmng/), 0.1 mM [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Overnight incubation at 4°C with [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) and 3 mM TCEP |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | SEC | Superose 6 column (GE Healthcare) | -- + -- | Protein peak collected and concentrated to 8-10 mg/ml |


## Crystallization

### doi/10.1038##s41594-018-0059-z

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | miTRPV2 at 8-10 mg/ml in buffer supplemented with 5 mM TCEP |
| Reservoir | 200-400 mM CaCl₂, 15-25% [PEG400](/xray-mp-wiki/reagents/additives/peg-400/), pH 7-9 |
| Temperature | 17 |
| Growth time | Up to 2 weeks |
| Cryoprotection | -- |
| Notes | Crystals obtained in many conditions. Best diffracting crystals grew in 200-400 mM CaCl₂, 15-25% [PEG400](/xray-mp-wiki/reagents/additives/peg-400/) at pH 7-9. miTRPV2_QM+RTx protein was supplemented with 300 µM RTx and 5 mM TCEP before crystallization. Data from multiple crystals merged using BLEND. |

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | miTRPV2_QM at 8-10 mg/ml supplemented with 300 µM RTx and 5 mM TCEP |
| Reservoir | 200-400 mM CaCl₂, 15-25% [PEG400](/xray-mp-wiki/reagents/additives/peg-400/), pH 7-9 |
| Temperature | 17 |
| Growth time | Up to 2 weeks |
| Cryoprotection | -- |
| Notes | miTRPV2_QM extracted with 20 mM [OGNG](/xray-mp-wiki/reagents/detergents/ogng/) and 2 mM [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) in presence of 2 µM RTx. Purified in buffers containing 2 mM [OGNG](/xray-mp-wiki/reagents/detergents/ogng/), 0.2 mM [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 0.1 mg/ml [DMPC](/xray-mp-wiki/reagents/lipids/dmpc/), 2 µM RTx. |


## Biological / Functional Insights

### Two-fold symmetric selectivity filter gate opening

The TRPV2 channel can adopt a two-fold (C2) symmetric arrangement of subunits,
in contrast to the canonical four-fold (C4) symmetric arrangement observed in
most TRP channel structures. In the RTx- and Ca²⁺-bound state (6BWJ), two
diagonally positioned subunits (A and C) are widened while the other two (B and D)
are contracted, producing a two-fold symmetric pore conformation. The distance
between Ile603 carbonyls across the selectivity filter increases to 12.3 Å in
the widened subunits, compared to 5.2 Å in the closed state, creating an
opening large enough for permeation of large organic cations such as YO-PRO-1
(376 Da). This represents the first structural capture of a fully open SF gate
in a TRPV channel.

### Role of π-helix in S4-S5 linker mediated gating

A π-helix between the S4-S5 linker and S5 (termed π-hinge_S4-S5) determines
the quaternary structural arrangement of TRPV2 subunits. In the Ca²⁺-bound
structure (6BWM), two distinct π-helix positions (beginning at Asp534 vs
Ile531) produce different angles between the S4-S5 linker and S5, resulting
in different degrees of subunit rotation and the two-fold symmetric
rearrangement. RTx binding pushes down on the base of S5 via the π-hinge,
forcing the S4-S5 linker into a different conformation, leading to subunit
rotation and SF gate widening.

### Ca²⁺ coordination in the selectivity filter

In the contracted subunits of the RTx-bound structure, Ca²⁺ ions are
coordinated in the selectivity filter through a novel mechanism involving
helical dipole utilization. Two pore helices align so that carbonyls of
Phe601, Thr602, and Ile603 at the C-termini of the pore helices make
water-mediated coordination of Ca²⁺. In the Ca²⁺-bound structure (6BWM),
a putative Ca²⁺ ion is coordinated in the SF gate, with Ile603 carbonyls
coordinating via water molecules.

### Hydrogen bond triad in pore helix gating

A hydrogen bond triad consisting of Tyr542 (S5), Thr602 (pore helix), and
Tyr627 (S6) stabilizes the contracted subunit conformation. This triad is
broken in the widened subunits, allowing the pore helix to adopt a different
angle. Mutagenesis of Thr602Ala or Tyr542Ala significantly reduces YO-PRO-1
uptake while preserving Na⁺ conductance, demonstrating that the hydrogen bond
network is critical for large organic cation permeation through the SF gate.
The equivalent Thr641Ala mutation in TRPV1 produces a similar phenotype.


## Cross-References

- [Epithelial Calcium Channel TRPV6](/xray-mp-wiki/proteins/voltage-gated-channels/trpv6/) — TRPV family member, structural comparison of selectivity filter gating
- [Epithelial Calcium Channel TRPV5](/xray-mp-wiki/proteins/voltage-gated-channels/trpv5/) — TRPV family member, structural comparison
- [Resiniferatoxin (RTx)](/xray-mp-wiki/reagents/ligands/resiniferatoxin/) — Vanilloid toxin that binds TRPV2 and induces SF gate opening
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary solubilization detergent (40 mM) for miTRPV2 extraction
- [Decyl Maltoside Neopentyl Glycol (DMNG)](/xray-mp-wiki/reagents/detergents/dmng/) — Detergent (0.1 mM) used in buffers during purification
- [Octyl Glucose Neopentyl Glycol (OGNG)](/xray-mp-wiki/reagents/detergents/og/) — Detergent (20 mM) used for miTRPV2_QM extraction with RTx
- [Cholesteryl Hemisuccinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Lipid additive (4 mM/0.1-0.2 mM) used in detergent extraction and purification buffers
- [1,2-Dimyristoyl-sn-glycero-3-phosphocholine (DMPC)](/xray-mp-wiki/reagents/lipids/dmpc/) — Lipid (0.1 mg/ml) added to purification buffers
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Method used in structure determination or purification
