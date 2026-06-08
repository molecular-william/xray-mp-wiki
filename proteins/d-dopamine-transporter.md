---
title: Drosophila Dopamine Transporter (dDAT)
created: 2026-06-02
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature12863, doi/10.1038##NSMB.2894, doi/10.1038##nature12533, doi/10.1038##nature14431, doi/10.1038##nature17629]
verified: false
---

# Drosophila Dopamine Transporter (dDAT)

## Overview

The Drosophila melanogaster dopamine transporter (dDAT) is a eukaryotic member of the neurotransmitter/sodium symporter (NSS) family. It mediates the Na+/Cl--coupled reuptake of dopamine from the synaptic cleft, terminating dopaminergic signaling. Crystal structures of inhibitor-bound and substrate-bound dDAT provided the first high-resolution views of an eukaryotic NSS, confirming conservation of the LeuT-fold architecture and revealing molecular principles that distinguish substrates from inhibitors in biogenic amine transporters.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature12863 | not specified | 2.9 A | not specified | dDAT from D. melanogaster, inhibitor-bound outward-open state | antidepressant/psychostimulant inhibitor, Na+, Cl- |
| doi/10.1038##nature12533 | not specified | 2.96 A | P212121 | dDATcryst — N-terminal truncation (residues 1-20 deleted), EL2 truncation (residues 164-206 deleted), C-terminal thrombin site at position 602, thermostabilizing mutations V74A, V275A, V311A, L415A, G538L | nortriptyline, Na+, Cl-, cholesterol |
| doi/10.1038##nature14431 | not specified | not specified | not specified | dDAT_mfc — thermostabilizing mutations (V74A, L415A), N-terminal deletion (1-20), EL2 deletion (162-202), thrombin site replacing residues 602-607 | dopamine (DA) |
| doi/10.1038##nature14431 | not specified | not specified | not specified | dDAT_mfc — thermostabilizing mutations (V74A, L415A), N-terminal deletion (1-20), EL2 deletion (162-202), thrombin site replacing residues 602-607 | D-amphetamine |
| doi/10.1038##nature14431 | not specified | not specified | not specified | dDAT_mfc — thermostabilizing mutations (V74A, L415A), N-terminal deletion (1-20), EL2 deletion (162-202), thrombin site replacing residues 602-607 | (+)-methamphetamine |
| doi/10.1038##nature14431 | not specified | not specified | not specified | dDAT_mfc — thermostabilizing mutations (V74A, L415A), N-terminal deletion (1-20), EL2 deletion (162-202), thrombin site replacing residues 602-607 | 3,4-dichlorophenethylamine (DCP) |
| doi/10.1038##nature14431 | not specified | not specified | not specified | dDAT_mfc — thermostabilizing mutations (V74A, L415A), N-terminal deletion (1-20), EL2 deletion (162-202), thrombin site replacing residues 602-607 | cocaine |
| doi/10.1038##nature14431 | not specified | not specified | not specified | dDAT_mfc sub^B (D121G, S426M) — thermostabilizing mutations (V74A, L415A), N-terminal deletion (1-20), EL2 deletion (162-202), thrombin site replacing residues 602-607 | RTI-55 |
| doi/10.1038##nature14431 | not specified | not specified | not specified | ts^5 dDATcryst sub^B (D121G, S426M) — thermostabilizing mutations (V74A, V275A, V311A, L415A, G538L), N-terminal deletion (1-20), EL2 deletion (164-206), thrombin site replacing residues 602-607 | beta-CFT |

## Expression and Purification

### Purification Workflow

- **Expression system**: HEK293S GnT- cells
- **Expression construct**: C-terminal GFP-His8 fusion

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and infection | Baculovirus-mediated transduction | HEK293S GnT- cells | standard cell culture media | Membranes harvested post-infection |
| Membrane solubilization | Detergent solubilization | -- | 1x TBS (20 mM Tris pH 8.0, 100 mM NaCl) + 20 mM DDM, 4 mM CHS | Homogenization and solubilization of membranes |
| Affinity chromatography | Cobalt-charged metal affinity resin | Cobalt-charged metal affinity resin | 1x TBS + 1 mM DDM + 0.2 mM CHS + 80 mM imidazole pH 8.0 + 1 mM DDM | Elution with imidazole |
| Tag removal | Thrombin digestion | -- | 1x TBS | GFP-His8 tag removed |
| Size exclusion chromatography | Superdex 200 10/300 SEC | Superdex 200 10/300 column | 20 mM Tris pH 8.0, 300 mM NaCl, 4 mM decyl-beta-D-maltoside, 0.2 mM CHS, 0.001% POPE + 4 mM decyl-beta-D-maltoside | Peak fractions >0.5 mg/ml collected, ascorbic acid added for DA complex |


## Crystallization

### doi/10.1038##nature14431

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | dDAT_mfc in complex with DA |
| Reservoir | PEG 600 31%, Tris pH 8.0 (0.1M) |
| Notes | Outward-open conformation |

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | dDAT_mfc in complex with D-amphetamine |
| Reservoir | PEG 600 36%, MOPS pH 7.0 (0.1M) |
| Notes | Outward-open conformation |

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | dDAT_mfc in complex with (+)-methamphetamine |
| Reservoir | PEG 400 38%, Tris pH 8.0 (0.1M) |
| Notes | Outward-open conformation |

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | dDAT_mfc in complex with DCP |
| Reservoir | PEG 400 38%, Tris pH 8.0 (0.1M) |
| Notes | Partially occluded conformation |

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | dDAT_mfc in complex with cocaine |
| Reservoir | PEG 400 37%, Na MES pH 6.8 (0.1M) |
| Notes | Outward-open conformation |

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | dDAT_mfc sub^B in complex with RTI-55 |
| Reservoir | PEG 400 41%, Tris pH 8.0 (0.1M) |
| Notes | Outward-open conformation |

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | ts^5 dDATcryst sub^B in complex with beta-CFT |
| Reservoir | not specified |
| Notes | Outward-open conformation |


## Biological / Functional Insights

### Substrate-bound outward-open conformation

DA, D-amphetamine, and methamphetamine all bind to the central S1 site in an outward-open conformation. The amine group interacts with Asp46 (TM1b) in subsite A, while the aromatic group is stabilized by van der Waals interactions with a hydrophobic cleft formed by TMs 3, 6, and 8 in subsite B. Substrates require Phe325 to rotate inward to contract pocket size and maintain edge-to-face aromatic interactions.

### Dopamine-binding mode

DA occupies the central binding site surrounded by TMs 1, 3, 6, and 8. The amine group interacts with Asp46 at 3 A distance. The catechol group occupies subsite B cavity formed by Ala117, Val120, Asp121, Tyr124, Ser422, and Phe325. A water molecule observed 3.1 A from the amine group forms a hydrogen bond network linking DA to the Na1 sodium ion binding site.

### DCP-induced partial occlusion

3,4-dichlorophenethylamine (DCP) induces a partially occluded conformation through inward rotations of TM1b (5.6 degrees) and TM6a (7 degrees). Phe319 rotates inward to cover the ligand. This conformation is on the pathway to the fully occluded state seen in LeuT. Unlike the DA-bound state, no water molecule is associated with DCP, suggesting dehydration accompanies occlusion.

### Amphetamine substrate recognition

D-amphetamine and methamphetamine bind to the central site with amine groups interacting with Asp46. Despite being sterically smaller than dopamine, amphetamines act as substrates because their amino and aromatic groups can interact with both subsite A and subsite B simultaneously, without requiring catechol-like hydroxyl groups.

### Cocaine inhibition mechanism

Cocaine binds to the central site in an outward-open conformation. The tertiary amino group forms a salt bridge with Asp46. Inhibition is achieved by combining a free amine with bulky tropane and aromatic moieties that limit conformational movements of the transporter. The TM6a-6b linker contracts, allowing Phe325 to form edge-to-face aromatic interactions with the benzyl ring.

### Binding-site plasticity

The binding pocket accommodates ligands of varying sizes through conformational adjustments of TM6 and side chains of Phe319 and Phe325. Ligand recognition is bipartite: an amine group interacts with subsite A (Asp46 or Phe43/Phe319 carbonyls), while an aromatic group is stabilized in the hydrophobic subsite B cleft. Substrates with single phenyl rings cause Phe325 to rotate inward; tropane inhibitors with multiple aromatic rings require both Phe319 and Phe325 to splay outward.

### Cholesterol binding sites

Two cholesterol binding sites identified in dDAT. Site 1 corresponds to the conserved NSS cholesterol site. Site 2 is a novel site at the inner leaflet junction of TMs 2, 7, and 11 where cholesteryl hemisuccinate (CHS) was modeled. CHS enhances dDAT inhibitor affinity, suggesting cholesterol may stabilize DAT in an outward-open state in native membranes.

### Subsite B mutagenesis

D121G and S426M mutations in subsite B (TM3 and TM8) enhance dDAT binding affinity for cocaine and beta-CFT, mimicking mammalian DAT pharmacology. The negative electrostatic potential of subsite B in wild-type dDAT compared to mammalian DATs accounts for reduced cocaine affinity. Mutations abrogate dopamine transport activity.


## Cross-References

- [Human Serotonin Transporter (SERT)](/xray-mp-wiki/proteins/ssert/) — NSS family homolog; structural comparison between SERT and dDAT reveals conserved architecture and distinct EL6/EL2 regions
- [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/leut/) — NSS family prototype; dDAT structure confirms conserved LeuT-fold architecture
- [MhsT Multi-Hydrophobic Amino Acid Transporter from Bacillus halodurans](/xray-mp-wiki/proteins/mhst/) — NSS family member; dDAT shares 25% sequence identity with MhsT
- [Neurotransmitter/Sodium Symporter (NSS) Family](/xray-mp-wiki/concepts/nss-family/) — dDAT is a eukaryotic member of the NSS family
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — Core transport mechanism of NSS family; DCP-bound structure supports alternating access
- [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine/) — Endogenous substrate; cocrystal structure of dDAT_mfc-DA complex
- [Cocaine](/xray-mp-wiki/reagents/ligands/cocaine/) — Competitive inhibitor; cocrystal structure of dDAT_mfc-cocaine complex
- [D-Amphetamine](/xray-mp-wiki/reagents/ligands/d-amphetamine/) — Psychostimulant substrate; cocrystal structure of dDAT_mfc-D-amphetamine complex
- [3,4-Dichlorophenethylamine (DCP)](/xray-mp-wiki/reagents/ligands/3-4-dichlorophenethylamine/) — Stable dopamine analogue; cocrystal structure shows partial occlusion
