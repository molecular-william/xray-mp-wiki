---
title: Human Endothelin ETB Receptor in Complex with Sarafotoxin S6b
created: 2026-05-26
updated: 2026-05-26
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.bbrc.2019.12.091]
verified: false
---

# Human Endothelin ETB Receptor in Complex with Sarafotoxin S6b

## Overview

The human endothelin ETB receptor (ETBR) is a class A GPCR that binds endothelin peptides and sarafotoxins, regulating vascular tone through nitric oxide-mediated vasorelaxation. The crystal structure of the thermostabilized ETB receptor in complex with the non-selective sarafotoxin S6b at 3.0 A resolution reveals the binding mode of sarafotoxins and provides structural insight into their subtype selectivity. The S6b-bound receptor shows an outward displacement of the intracellular end of TM5, suggesting a more active conformation for G-protein coupling.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.bbrc.2019.12.091 | 6LRY | 3.0 A | not specified | ETB-Y5-T4L thermostabilized construct with T4 lysozyme inserted in ICL3, C-terminus truncated after S405, five thermostabilizing mutations (R124Y, D154A, K270A, DS342A, I381A), and three cysteine-to-alanine mutations (C396A, C400A, C405A) | Sarafotoxin S6b (SRTX-b) |

## Expression and Purification

- **Expression system**: Sf9 insect cells using Bac-to-Bac baculovirus expression system (Invitrogen)
- **Construct**: Hemagglutinin signal peptide, Flag epitope tag (DYKDDDDK) with nine-amino-acid linker at N-terminus, TEV protease recognition sequence between G57 and L66, C-terminus truncated after S405, thermostabilizing mutations R124Y, D154A, K270A, DS342A, I381A, cysteine-to-alanine mutations C396A, C400A, C405A, T4 lysozyme inserted in intracellular loop 3 between L303 and L311 (ETB-Y5-T4L), GFP-His10 tag at C-terminus

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and membrane preparation | Sf9 insect cell expression | -- | 20 mM Tris-HCl, pH 7.5, 20% glycerol + -- | Cells infected with recombinant baculovirus at 4.0 x 10^6 cells/mL in SF900 II medium, grown for 48 h at 27 C. Membranes harvested by ultracentrifugation at 180,000g for 1 h. |
| Solubilization | Membrane solubilization | -- | 20 mM Tris-HCl, pH 7.5, 200 mM [sodium-chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/) + 1% [ddm](/xray-mp-wiki/reagents/detergents/ddm/) + 0.2% [cholesterol-hydrogen-succinate](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) (CHS) + 2 mg/mL [iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) | Solubilized for 1 h at 4 C. Supernatant separated by ultracentrifugation at 180,000g for 20 min. |
| Affinity chromatography | [affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) on TALON resin | [TALON](/xray-mp-wiki/reagents/additives/talon/) cobalt affinity resin (Clontech) | 20 mM Tris-HCl, pH 7.5, 500 mM [sodium-chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/) + 0.1% [lmng](/xray-mp-wiki/reagents/detergents/lmng/) (wash) / 0.01% [lmng](/xray-mp-wiki/reagents/detergents/lmng/) (elution) + 0.01% CHS (wash) / 0.001% CHS (elution) | Incubated with TALON resin for 30 min. Washed with 10 column volumes. Eluted with 200 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/). |
| TEV protease cleavage and tag removal | TEV protease cleavage followed by [affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) depletion | [TALON](/xray-mp-wiki/reagents/additives/talon/) cobalt affinity resin (Clontech) | 20 mM Tris-HCl, pH 7.5, 500 mM [sodium-chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/) + -- | Eluate treated with [TEV protease](/xray-mp-wiki/reagents/protein-tags/tevp-protease/) and dialyzed. Cleaved GFP-His10 tag and TEV protease removed with TALON resin. |
| Size-exclusion chromatography | [Size-exclusion chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) on Superdex200 | [superdex-200](/xray-mp-wiki/reagents/additives/superdex-200/) | 20 mM Tris-HCl, pH 7.5, 150 mM [sodium-chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/) + 0.01% [lmng](/xray-mp-wiki/reagents/detergents/lmng/) + 0.001% [cholesterol-hydrogen-succinate](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Peak fractions pooled, concentrated to 40 mg/mL using 50 kDa MW cutoff centrifugal filter. S6b added during concentration. |


## Crystallization

### doi/10.1016##j.bbrc.2019.12.091

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | ETB-S6b complex at 40 mg/mL in 20 mM Tris-HCl, pH 7.5, 150 mM [sodium-chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 0.01% [lmng](/xray-mp-wiki/reagents/detergents/lmng/), 0.001% [cholesterol-hydrogen-succinate](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) |
| Reservoir | not specified in the available text |
| Temperature | not specified in the available text |
| Growth time | not specified in the available text |
| Cryoprotection | not specified in the available text |
| Notes | 32 datasets collected and merged by KAMO. Structure determined by molecular replacement using ET-3-bound receptor (PDB 6IGK). Space group not specified in main text. |


## Biological / Functional Insights

### S6b-bound ETB receptor shows outward displacement of intracellular TM5

The S6b-bound receptor shows a remarkable difference on the intracellular side compared to ET-1- and ET-3-bound receptors. The intracellular end of TM5 is opened up by 4 A, suggesting that TM5 adopts a more active conformation for G-protein coupling, similar to the NTSR1 receptor. While T4L insertion affects the conformations of TM5 and TM6, agonist binding may cause the outward displacement of TM5 in the ETB receptor.

### Sarafotoxin S6b binding disrupts the inactive-state hydrogen-bonding network

Agonist binding disrupts the hydrogen-bonding network between W336(6,48) and D147(2,50) that stabilizes the inactive conformation by connecting TMs 2, 3, 6, and 7 at the receptor core. In the S6b-bound receptor, W336(6,48) rotates inwardly and forms a hydrogen bond with N378(7,45). D147(2,50) forms hydrogen bonding interactions with N119(1,50) and T188(3,39), indicating rearrangement of the hydrogen-bonding interaction in the receptor core upon agonist binding.

### Sarafotoxin S6b structurally mimics endothelins despite sequence differences

S6b adopts a similar bicyclic architecture to endothelins, with four conserved cysteines forming intrachain disulfide bonds (C1-C15 and C3-C11). S6b superimposes well with ET-1 and ET-3 (R.M.S.D. values for Ca = 0.39 and 0.40 A, respectively). Despite 8 differing residues, S6b highly mimics the endothelins and activates the receptor through similar binding interactions.

### Structural basis for sarafotoxin subtype selectivity revealed by MD simulations

Molecular dynamics simulations based on the S6b-bound receptor reveal that K9 in S6b forms a salt bridge with D246(ECL2) in ETB, anchoring the alpha-helical region to ECL2. In contrast, S6c (with E9 instead of K9) is repelled by D246(ECL2), explaining the reduced affinity of S6c for the ET_A receptor. The hydrophobic residues L252(ECL2) and I254(ECL2) in ETB are replaced by polar residues H236(ECL2) and T238(ECL2) in ET_A, reducing hydrophobic interactions with the sarafotoxin alpha-helical region.

### Thermostabilized ETB-Y5-T4L construct enables crystallographic studies

The thermostabilizing mutations R124Y(1,55), D154A(2,57), K270A(5,35), DS342A(6,54), and I381A(7,48) combined with T4 lysozyme insertion in ICL3 enabled the determination of the ETB receptor structure. Cysteine-to-alanine mutations (C396A, C400A, C405A) avoided heterogeneous palmitoylation, and the TEV protease site enabled removal of the disordered N-terminus during purification.


## Cross-References

- [Human Endothelin ETB Receptor in Complex with Sarafotoxin S6b](/xray-mp-wiki/proteins/etb-s6b-complex/) — This is the current entity being reconstructed
- [Human Adenosine A2A Receptor (A2AR)](/xray-mp-wiki/proteins/human-adenosine-a2a-receptor-a2ar/) — Other class A GPCR in the database with similar thermostabilization approaches (T4 lysozyme, bRIL fusions)
- [bRIL Fusion Protein](/xray-mp-wiki/reagents/protein-tags/bril/) — Related thermostabilization strategy for GPCRs (T4 lysozyme used in ETB instead)
- [TEV Protease](/xray-mp-wiki/reagents/protein-tags/tevp-protease/) — Used to cleave the GFP-His10 tag during purification
- [LMNG (Lauryl Maltose Neopentyl Glycol)](/xray-mp-wiki/reagents/detergents/lmng/) — Primary detergent used in affinity chromatography wash/elution and SEC
- [Cholesterol Hemisuccinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Added to solubilization and purification buffers to stabilize the GPCR
- [DDM (N-Dodecyl-beta-D-maltoside)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used in initial membrane solubilization
- [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon/) — Used for His-tag affinity capture and tag removal
- [Superdex 200 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200/) — Size-exclusion chromatography resin for final polishing
- [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) — Added during solubilization (2 mg/mL) to prevent disulfide scrambling
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Used as eluent for TALON Ni-NTA affinity chromatography
- [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/) — Salt component in all purification buffers
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — TALON resin-based His-tag affinity purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Superdex200 SEC used for final purification and complex verification
- [GPCR Active Conformation](/xray-mp-wiki/concepts/gpcr-active-conformation/) — S6b-bound receptor shows outward displacement of TM5 consistent with active conformation
