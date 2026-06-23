---
title: "ASBT-NM (Bacterial Homologue of the Bile Acid Sodium Symporter ASBT)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##NATURE10450]
verified: false
---

# ASBT-NM (Bacterial Homologue of the Bile Acid Sodium Symporter ASBT)

## Overview

ASBT-NM is a bacterial homologue of the apical sodium-dependent bile acid transporter (ASBT, SLC10A2) from Neisseria meningitidis. ASBT moves bile acids across the apical membrane of the ileum using the sodium ion gradient, making it a target for hypercholesterolaemia drugs. The structure reveals ten transmembrane helices organized as two inverted structural repeats (five helices each), forming a core domain of six helices and a panel-like domain of four helices. The architecture is remarkably similar to the sodium/proton antiporter NhaA despite no detectable sequence homology. The structure was captured in an inward-facing conformation with bound taurocholate and two sodium ions.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##NATURE10450 | 3ZUY | 2.2 | not specified | Full-length ASBT-NM (residues 1-? from N. meningitidis MC58; wild-type; C-terminal truncation | Taurocholate, two Na⁺ ions, five LDAOO molecules, two Peptide 5Tru [Ecoli Phospholipids](/xray-mp-wiki/reagents/lipids/ecoli-phospholipids/) |

## Expression and Purification

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Cell disruption and ultracentrifugation | — | 1× PBS, 150 mM NaCl, 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) | E. coli C43(DE3) expressing ASBT-NM-GFP-His8 fusion protein with T4L fusion |
| Solubilization | Detergent solubilization | — | 1× PBS, 150 mM NaCl, 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 1% DDM (dodecyl-β-D-maltopyranoside | Solubilized for 2 h at 4°C |
| Ni-NTA affinity | Ni-NTA affinity chromatography | Ni-NTA Superflow (Qiagen | 1× PBS, 0.1% DDM, 150 mM NaCl, 20 mM imidazole (wash); 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (elution) + 0.1% DDM | Washed with 20 CV of low-imidazole buffer, then 20 CV of 50 mM imidazole; eluted in 2 CV of 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Tag cleavage and buffer exchange | Dialysis and TEV cleavage | — | 20 mM Tris-HCl pH 7.5, 150 mM NaCl + Not specified | Dialysed overnight with His6-tagged TEV protease to remove GFP-His8 tag; subsequent Ni-NTA flow-through to remove cleaved tag and TEV protease |
| Size exclusion chromatography | SEC | Not specified | 20 mM Tris-HCl pH 7.5, 150 mM NaCl, 0.06% LDAO + 0.06% LDAO (n-dodecyl-N,N-dimethylamine-N-oxide | Final polishing step; ASBT-NM exchanged into LDAO for crystallization |


## Crystallization

### doi/10.1038##NATURE10450

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified ASBT-NM in 0.06% LDAO, 20 mM Tris-HCl pH 7.5, 150 mM NaCl |
| Reservoir | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Crystal dehydration using humidity controller HC1 device at 45% relative humidity for 5 min before freezing |
| Notes | Grown in presence of 10 mM taurocholate; dehydration necessary to obtain diffraction data; data collected at Diamond Light Source beamlines I02 and I03 |


## Biological / Functional Insights

### Inverted repeat architecture

ASBT-NM contains two inverted structural repeats of five helices each (TM1-TM5 and TM6-TM10), related by a pseudo-twofold axis in the membrane plane. Each repeat contains an N-terminal V-motif (TM1/TM2 or TM6/TM7) and a core of three helices (TM3-TM5 or TM8-TM10). The core motifs together form the core domain, while the V-motifs create a panel domain. TM4 and TM9 are broken (discontinuous helices that cross over at conserved motifs, a feature shared with NhaA.

### Sodium binding sites

Two sodium ions (Na1 and Na2) are located in the core domain, buried from bulk solvent. Na1 is octahedrally coordinated by S114, N115 (TM4b), T132, S128 (TM5), and E260 (TM9a). Na2 has a square pyramidal arrangement involving E260, V261, M263, Q264 (TM9) and Q77 (TM3). Na1 is located near the crossover of the discontinuous helices, suggesting it controls channel gating and conformational changes to drive panel domain movement.

### Substrate binding cavity

A large inward-facing cavity between the core and panel domains contains the taurocholate. The cavity extends over halfway through the membrane and is closed on the extracellular side. Only one direct hydrogen bond exists between ASBT-NM and taurocholate (N295 to the 7α hydroxyl group). The taurine moiety binds near TM1 and TM10. B-factors suggest weak taurocholate binding, consistent with the variety of compounds recognized by ASBT.

### Transport mechanism

An outward-facing model was generated by swapping the conformations of the N- and C-terminal repeats (analogous to the LeuT approach). Comparing the inward-facing conformation with the outward-facing model, the largest difference is the position of the panel domain relative to the core domain. This suggests that substrate binding controls conformational changes in the core domain, which drives panel domain movement to alter substrate accessibility - a rocker-switch type alternating access mechanism.


## Cross-References

- [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/enzymes/leut/) — Related protein structure; referenced in text
- [MalG (Escherichia coli Maltose Transporter Transmembrane Subunit)](/xray-mp-wiki/proteins/abc-transporters/malG/) — Related protein structure; referenced in text
- [Saccharomyces cerevisiae Niemann-Pick Type C-Related Protein 1 (NCR1)](/xray-mp-wiki/proteins/structural-adhesion/ncr1/) — Related protein structure; referenced in text
- [Bovine Rhodopsin (2.2 A Resolution, PDB 1U19)](/xray-mp-wiki/proteins/gpcr/rhodopsin-2-2a/) — Related protein structure; referenced in text
- [GLIC ECD (Extracellular Domain of Gloeobacter violaceus Ion Channel)](/xray-mp-wiki/proteins/cys-loop-receptors/glic-ecd/) — Related protein structure; referenced in text
- [Na+/H+ Antiporter NhaA from Escherichia coli](/xray-mp-wiki/proteins/slc-transporters/nhaa/) — Related protein structure; referenced in text
- [Chicken Kir2.2 Inward Rectifier K+ Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kir2-2-channel/) — Related protein structure; referenced in text
- [E. coli MscS (Mechanosensitive Channel of Small Conductance)](/xray-mp-wiki/proteins/voltage-gated-channels/mscs/) — Related protein structure; referenced in text
- [GLIC (Gloeobacter violaceus Ion Channel)](/xray-mp-wiki/proteins/cys-loop-receptors/glic/) — Related protein structure; referenced in text
- [MalF (Escherichia coli Maltose Transporter Transmembrane Subunit)](/xray-mp-wiki/proteins/abc-transporters/malF/) — Related protein structure; referenced in text
