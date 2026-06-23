---
title: Adiponectin Receptor 2 (ADIPOR2)
created: 2026-06-03
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature21714, doi/10.1016##j.crmeth.2021.100102, doi/10.1038##s42003-020-01160-4]
verified: false
---

# Adiponectin Receptor 2 (ADIPOR2)

## Overview

[Adiponectin](/xray-mp-wiki/proteins/structural-adhesion/adiponectin/) receptor 2 (ADIPOR2) is an integral membrane protein that belongs to the progesterone and adipoQ receptor (PAQR) family. It has a seven-transmembrane (7TM) domain architecture with a zinc binding site within the transmembrane region. ADIPOR2 mediates cellular ceramidase activity that hydrolyses [Ceramide](/xray-mp-wiki/reagents/lipids/ceramide/) into [Sphingosine](/xray-mp-wiki/reagents/lipids/sphingosine/) and a free fatty acid (FFA), and this activity is enhanced by [Adiponectin](/xray-mp-wiki/proteins/structural-adhesion/adiponectin/) binding. The receptor was crystallized in complex with an scFv antibody fragment using lipidic cubic phase (LCP) crystallization. Additional structures were determined by serial synchrotron crystallography (SSX) using the automated CrystalDirect platform, enabling room-temperature and cryogenic structure comparisons.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature21714 | 5LX9 | 2.4 | P212121 | ADIPOR2-scFv complex (residues 100-386, N-terminal Flag tag, in complex with anti-ADIPOR scFv) | Oleic acid (FA C18:1) |
| doi/10.1038##nature21714 | 5LWY | 2.4 | P212121 | ADIPOR2-scFv complex (residues 100-386, N-terminal Flag tag, in complex with anti-ADIPOR scFv) | Oleic acid (FA C18:1) |
| doi/10.1038##nature21714 | 5LXA | 3.0 | P212121 | ADIPOR2-scFv complex (residues 100-386, N-terminal Flag tag, in complex with anti-ADIPOR scFv) | Oleic acid (FA C18:1) |
| doi/10.1016##j.crmeth.2021.100102 | 6YX9 | 2.4 | Not specified | ADIPOR2-scFv complex, cryogenic SSX structure, CrystalDirect platform | Oleic acid (FA C18:1) |
| doi/10.1016##j.crmeth.2021.100102 | 6YXD | 2.9 | Not specified | ADIPOR2-scFv complex, room temperature in situ SSX structure, CrystalDirect platform | Oleic acid (FA C18:1) |
| doi/10.1016##j.crmeth.2021.100102 | 6YXG | 3.0 | Not specified | ADIPOR2-scFv complex soaked with Tb-XO4 phasing agent | Tb-XO4 (crystallophore), Oleic acid |
| doi/10.1016##j.crmeth.2021.100102 | 6YXF | 3.0 | Not specified | ADIPOR2-scFv complex soaked with Gd-DO3 phasing agent | Gd-DO3, Oleic acid |
| doi/10.1038##s42003-020-01160-4 | 6KS1 | 2.4 | P21212 | ADIPOR2(D219) revised closed-form structure (residues 100-386, N-terminal Flag tag, in complex with anti-ADIPOR scFv), replaces PDB 3WXW | Oleic acid (FA C18:1) |

## Expression and Purification

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Baculovirus expression in Sf9 insect cells (pFastBac system, ThermoFisher) | — | Not specified | N-terminally truncated ADIPOR2 construct (residues 100-386) with N-terminal Flag epitope tag |
| Cell lysis | Osmotic shock in 10 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 1 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/), 2 mg/ml [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) | — | 10 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 1 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/), 2 mg/ml [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) | Cells lysed by osmotic shock with protease inhibitors |
| Solubilization | Glass dounce tissue grinder in solubilization buffer | — | 20 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 100 mM NaCl, 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.1% CHS, 2 mg/ml [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) | Stirred 1 h at 4 C |
| Detergent adjustment | Dilution to working concentration | — | 20 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.4, 300 mM NaCl, 0.5% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.05% CHS | Adjusted for anti-Flag affinity chromatography |
| Anti-Flag affinity chromatography | Anti-Flag M2 antibody resin (Sigma) | — | 20 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.4, 300 mM NaCl, 0.5% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.05% CHS | Gravity flow loading |
| Washing | Anti-Flag M2 resin wash | — | 20 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.4, 200 mM NaCl, 0.025% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.0001% CHS | Wash buffer 1 |
| Elution | Flag peptide elution | — | 20 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.4, 200 mM NaCl, 0.025% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.0001% CHS, 0.4 mg/ml Flag peptide | Bound receptor eluted with Flag peptide |
| Purity evaluation | SDS-PAGE and analytical SEC | — | Not specified | Purity and monodispersity evaluated |


## Crystallization

### doi/10.1038##nature21714

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Lipid | Monoolein |
| Temperature | Not specified |
| Notes | ADIPOR2-scFv complex crystallized in [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) LCP. Three structures solved: S1 (5LX9, 2.4 A), S2 (5LWY, 2.4 A), and S3 (5LXA, 3.0 A). Crystals grown in sandwich glass plates. |

### doi/10.1016##j.crmeth.2021.100102

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) in CrystalDirect plates |
| Protein sample | 15 mg/mL ADIPOR2-scFv in SEC buffer |
| Lipid | Monoolein:cholesterol (10:1) |
| Temperature | 20 C |
| Growth time | 5 days |
| Notes | LCP mesophase formed by coupled two-syringe method. Dispensed in CrystalDirect plates (30-50 nL bolus). Crystals approximately 30 x 20 x 5 um. Automated laser-based harvesting using CrystalDirect harvester. SSX data collected at cryogenic (SLS) and room temperature (PETRA III P14). Crystals stable for several weeks. |


## Biological / Functional Insights

### Intrinsic ceramidase activity

ADIPOR2 possesses intrinsic basal ceramidase activity that converts [Ceramide](/xray-mp-wiki/reagents/lipids/ceramide/) into [Sphingosine](/xray-mp-wiki/reagents/lipids/sphingosine/) and a free fatty acid. Michaelis-Menten kinetic analysis determined a Km of 15.6 uM and a kcat of 0.49 x 10^-3 s^-1. The activity is low but comparable to other intramembrane proteins such as [Gamma-Secretase Complex](/xray-mp-wiki/concepts/gamma-secretase/). ADIPOR2 shows preference for C18 [Ceramide](/xray-mp-wiki/reagents/lipids/ceramide/) substrate but can also hydrolyse C6 and C24 ceramides to a lesser extent.

### Adiponectin-enhanced ceramidase activity

[Adiponectin](/xray-mp-wiki/proteins/structural-adhesion/adiponectin/) increases the basal ADIPOR2 ceramidase activity approximately 20-fold. This suggests that [Adiponectin](/xray-mp-wiki/proteins/structural-adhesion/adiponectin/) binding to ADIPOR2 allosterically enhances its enzymatic function.

### Zinc-dependent catalytic mechanism

ADIPOR2 contains a zinc binding site within the 7TM domain close to the intracellular surface. The zinc is coordinated by residues including H202 (TM2), S168 (TM2), H348 (TM7), and H352 (TM7). Molecular dynamics simulations suggest a mechanism in which H348 acts as a general acid/base that promotes nucleophilic attack of a zinc-bound hydroxide ion onto the [Ceramide](/xray-mp-wiki/reagents/lipids/ceramide/) amide carbonyl. Residues R278 (TM5) and Y328 (TM6) serve as carbonyl-polarizing and oxyanion-stabilizing residues.

### Closed conformation with buried substrate binding pocket

The ADIPOR2 crystal structures reveal a closed conformation with a large internal cavity that is largely buried within the transmembrane domain. The [Ceramide](/xray-mp-wiki/reagents/lipids/ceramide/) binding pocket and zinc catalytic site are buried, accessible through a transmembrane opening and an intracellular opening. The fatty acid product remains bound in a hydrophobic pocket while the [Sphingosine](/xray-mp-wiki/reagents/lipids/sphingosine/) moiety would diffuse toward the cytoplasm through the intracellular cavity.

### Temperature-dependent conformational states of oleic acid product

Comparison of cryogenic (2.4 A) and room-temperature (2.9 A) ADIPOR2 structures from the CrystalDirect SSX platform revealed conformational differences in the bound oleic acid (OLA) product. MD simulations showed OLA rapidly adopting the RT conformation from the cryogenic starting model. TM5 opening of 4 A coincided with OLA displacement from the active-site zinc toward the lipid bilayer, capturing the product release mechanism. The RT structure also enabled capture of an open TM5 conformation resembling [ADIPOR1](/xray-mp-wiki/proteins/structural-adhesion/adipor1/).

### Revised AdipoR2 structure confirms closed conformation (6KS1)

The AdipoR2(D219) structure was reanalyzed with an improved model (PDB 6KS1, replacing 3WXW), including one oleic acid molecule. The revised structure confirms the closed conformation with 97.43% of residues in Ramachandran favored regions. The Rwork/Rfree values for the revised structure (6KS1) are 0.2256/0.2640.


## Cross-References

- [Adiponectin Receptor 1 (ADIPOR1)](/xray-mp-wiki/proteins/structural-adhesion/adipor1/) — Homologous receptor with ceramidase activity, distinct open conformation
- [Adiponectin](/xray-mp-wiki/proteins/structural-adhesion/adiponectin/) — Hormone that activates ADIPOR2 and enhances ceramidase activity
- [Alkaline Ceramidase 3 (ACER3)](/xray-mp-wiki/proteins/enzymes/acer3/) — Related PAQR family member; co-characterized in same CrystalDirect SSX study
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Primary lipid for LCP crystallization
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for solubilization and purification
- [Cholesteryl Hemisuccinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Lipid additive used with DDM for membrane protein stabilization
- [Ceramide](/xray-mp-wiki/reagents/lipids/ceramide/) — Substrate for ADIPOR2 ceramidase activity
- [PAQR Family (Progesterone and AdipoQ Receptor Family)](/xray-mp-wiki/concepts/paqr-family/) — ADIPOR2 belongs to the PAQR protein family
- [X-ray Crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/) — Method used in the study
- [PAQR Family (Progesterone and AdipoQ Receptor Family)](/xray-mp-wiki/concepts/paqr-family/) — Key concept related to this protein
