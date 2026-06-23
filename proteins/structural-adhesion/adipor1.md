---
title: Adiponectin Receptor 1 (ADIPOR1)
created: 2026-06-03
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature21714, doi/10.1038##s42003-020-01160-4]
verified: false
---

# Adiponectin Receptor 1 (ADIPOR1)

## Overview

[Adiponectin](/xray-mp-wiki/proteins/adiponectin) receptor 1 (ADIPOR1) is an integral membrane protein that belongs to the progesterone and adipoQ receptor (PAQR) family. It has a seven-transmembrane (7TM) domain architecture with a zinc binding site within the transmembrane region, similar to ADIPOR2. ADIPOR1 also possesses intrinsic ceramidase activity that is sensitive to adiponectin. Crystal structures of the D208A variant (fully active for AMPK signaling) reveal that ADIPOR1 can adopt both closed and open conformations. In the open form, helices IV and V are tilted with their intracellular ends shifted by about 4 and 11 Å, respectively, creating large openings in the internal cavity. Wild-type ADIPOR1 exists as a 44:56 mixture of closed and open forms, suggesting a dynamic equilibrium relevant to signaling.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature21714 | 5LXG | Not specified (revised from 3WXV) | Not specified | ADIPOR1 (residues 89-375, N-terminal [FLAG Epitope Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag), revised structure from PDB 3WXV) | None observed |
| doi/10.1038##s42003-020-01160-4 | 6KRZ | 3.1 | P212121 | AdipoR1(A208) variant (residues 89-375, D208A mutation, in complex with Fv fragment of monoclonal antibody) | Oleic acid (molecule A), Monoolein (molecule C) |
| doi/10.1038##s42003-020-01160-4 | 6KS0 | 2.8 | C2221 | AdipoR1(D208) wild-type (residues 89-375, Fv complex), reanalyzed as dual closed (44%) and open (56%) conformation | None specified |

## Expression and Purification

### Purification Workflow

*Source: unknown*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Baculovirus expression in [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/sf9-insect-cells) (pFastBac system, ThermoFisher) | — | Not specified | N-terminally truncated ADIPOR1 construct (residues 89-375) with N-terminal Flag epitope tag |
| Cell lysis | Osmotic shock in 10 mM Tris-HCl pH 7.5, 1 mM EDTA, 2 mg/ml [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide) | — | 10 mM Tris-HCl pH 7.5, 1 mM EDTA, 2 mg/ml [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide) | Cells lysed by osmotic shock with protease inhibitors |
| Solubilization | Glass dounce tissue grinder in solubilization buffer | — | 20 mM HEPES pH 7.5, 100 mM NaCl, 1% DDM, 0.1% CHS, 2 mg/ml [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide) | Stirred 1 h at 4 C |
| Detergent adjustment | Dilution to working concentration | — | 20 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes) pH 7.4, 300 mM NaCl, 0.5% DDM, 0.05% CHS | Adjusted for anti-Flag [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) |
| Anti-Flag [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | Anti-Flag M2 antibody resin (Sigma) | — | 20 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes) pH 7.4, 300 mM NaCl, 0.5% DDM, 0.05% CHS | Gravity flow loading |
| Washing | Anti-Flag M2 resin wash | — | 20 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes) pH 7.4, 200 mM NaCl, 0.025% DDM, 0.0001% CHS | Wash buffer 1 |
| Elution | Flag peptide elution | — | 20 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes) pH 7.4, 200 mM NaCl, 0.025% DDM, 0.0001% CHS, 0.4 mg/ml Flag peptide | Bound receptor eluted with Flag peptide |
| Purity evaluation | SDS-PAGE and analytical [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | — | Not specified | Purity and monodispersity evaluated |

### Purification Workflow

*Source: doi/10.1038##s42003-020-01160-4*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Transient expression in FreeStyle 293-F cells | — | Not specified | AdipoR1(A208) residues 89-375 expressed as Fv fragment complex |
| Purification as Fv complex | Affinity purification with anti-ADIPOR1 monoclonal antibody Fv fragment | — | Not specified in available text | Purified as a complex with the Fv fragment of a monoclonal antibody |


## Crystallization

### doi/10.1038##nature21714

| Parameter | Value |
|---|---|
| Method | [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) (LCP) |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) |
| Temperature | Not specified |
| Notes | Revised ADIPOR1 structure (5LXG) from re-analysis of PDB 3WXV data. The revised structure shows a clear improvement in statistics. No FFA is observed in the structure. Large rearrangements of TM5 and intracellular loop 2 (ICL2) compared to [Adiponectin Receptor 2 (ADIPOR2)](/xray-mp-wiki/proteins/adipor2) structures. The zinc coordination sphere is similar to ADIPOR2.
 |

### doi/10.1038##s42003-020-01160-4

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | AdipoR1(A208)-Fv complex |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) |
| Temperature | Not specified |
| Notes | Crystallized by the lipidic mesophase method with monoolein. X-ray diffraction data collected at SPring-8 beamline BL32XU. The asymmetric unit contains three molecules: two in the closed form (A, B) and one in the open form (C). Data collected at 3.1 Å resolution with space group P212121.
 |


## Biological / Functional Insights

### Open conformation exposes catalytic site

The revised ADIPOR1 structure reveals an open conformation in which the putative catalytic site and substrate binding domain are exposed to the cytoplasm and fully accessible to the inner membrane leaflet. This is in stark contrast to the buried cavity of [Adiponectin Receptor 2 (ADIPOR2)](/xray-mp-wiki/proteins/adipor2). TM5 of ADIPOR1 is tilted by 20 degrees and translated 15 angstroms at the intracellular end compared to ADIPOR2. The largest structural shift is at residue M268 (TM5) of ADIPOR2 and R257 (TM5) of ADIPOR1, with a 17 angstrom shift.

### Intrinsic ceramidase activity

ADIPOR1 possesses intrinsic [Adiponectin](/xray-mp-wiki/proteins/adiponectin)-sensitive ceramidase activity, demonstrated using purified receptor preparations. The ceramidase activity of ADIPOR1 is inhibited by the H191R mutation (TM2) in the zinc binding domain, analogous to the H202R mutation in ADIPOR2.

### Conformational equilibrium model

The structural differences between ADIPOR1 (open) and [Adiponectin Receptor 2 (ADIPOR2)](/xray-mp-wiki/proteins/adipor2) (closed) suggest a dynamic equilibrium between open and closed conformations during the enzymatic process. The open conformation may allow substrate access from the inner membrane leaflet, while the closed conformation traps the substrate for catalysis and product release.

### Closed and open forms confirmed by D208A variant structure

The crystal structure of the fully active D208A variant (PDB 6KRZ) at 3.1 Å resolution revealed both closed and open forms in the asymmetric unit (two closed, one open). In the open form, helices IV and V are tilted with their intracellular ends shifted by approximately 4 and 11 Å, respectively. The cytoplasmic (CP) and lipid-bilayer (LB) openings of the major cavity are drastically enlarged in the open form.

### Wild-type AdipoR1 exists as a 44:56 closed-open mixture

Reanalysis of previous wild-type AdipoR1(D208) diffraction data (PDB 6KS0) using the authentic closed and open structures from the D208A variant revealed a dual conformation consisting of 44% closed form and 56% open form. The electron densities corresponding to both forms were unambiguously observed, confirming that AdipoR1 adopts both conformations in equilibrium.

### ICL2 conformational change relevant to downstream signaling

The position of ICL2 (Trp255-His263), which connects helices IV and V, differs by up to 13.5 Å between the closed and open forms. In the open form, ICL2 protrudes from the cytoplasmic surface and is more exposed. The positively charged residues Arg257, Lys262, and His263 in AdipoR1 ICL2 (distinct from the uncharged counterparts in AdipoR2) are oriented outward in the open form, potentially explaining the distinct downstream signaling pathways between AdipoR1 (AMPK) and AdipoR2 (PPAR-α).

### Zinc coordination stabilizes receptor structure

The zinc ion exhibits tetrahedral coordination with His191, His337, and His341 in both closed and open forms. Single mutations of these residues or D208A do not affect AMPK activation, suggesting the zinc coordination stabilizes the overall structure rather than being directly catalytic for the major signaling pathway.


## Cross-References

- [Adiponectin Receptor 2 (ADIPOR2)](/xray-mp-wiki/proteins/enzymes/adipor2/) — Homologous receptor with ceramidase activity, closed conformation
- [Adiponectin](/xray-mp-wiki/proteins/structural-adhesion/adiponectin/) — Hormone that activates ADIPOR1 and enhances ceramidase activity
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Primary lipid for LCP crystallization
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for solubilization and purification
- [Cholesteryl Hemisuccinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Lipid additive used with DDM for membrane protein stabilization
- [Ceramide](/xray-mp-wiki/reagents/lipids/ceramide/) — Substrate for ADIPOR1 ceramidase activity
- [Sphingosine](/xray-mp-wiki/reagents/lipids/sphingosine/) — Product of ADIPOR1 ceramidase-mediated ceramide hydrolysis
- [PAQR Family (Progesterone and AdipoQ Receptor Family)](/xray-mp-wiki/concepts/signaling-receptors/paqr-family/) — ADIPOR1 belongs to the PAQR protein family
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) — Purification method used in protein preparation
- [Size-Exclusion Chromatography (SEC)](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) — Purification method used in protein preparation
