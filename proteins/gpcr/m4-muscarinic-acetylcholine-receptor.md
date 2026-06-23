---
title: Human M4 Muscarinic Acetylcholine Receptor
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature17188]
verified: false
---

# Human M4 Muscarinic Acetylcholine Receptor

## Overview

The human M4 muscarinic [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine/) receptor (M4 mAChR) is a class A G protein-coupled receptor that mediates inhibitory cholinergic neurotransmission in the central nervous system. It couples to Gi/Go family G proteins and is highly expressed in the striatum, where it plays a critical role in motor control and cognitive function. The M4 receptor has emerged as an attractive drug target for schizophrenia, as selective M4 positive allosteric modulators (PAMs) have demonstrated preclinical efficacy. The first crystal structure of the M4 receptor was solved in complex with the inverse agonist [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium/) at 2.6 A resolution, revealing the orthosteric binding site and a network of residues linking the orthosteric and allosteric sites.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature17188 | 5DSG | 2.6 A | P 1 21 1 | Human M4 muscarinic receptor, N-terminal FLAG epitope tag, N-terminus truncated (residues 1-21 removed), residues 226-389 of ICL3 replaced by minimal T4 lysozyme (mT4L), C-terminal 8x histidine tag
 | [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium/) |

## Expression and Purification

- **Expression system**: Sf9 insect cells (baculovirus expression vector system)
- **Construct**: Human M4 muscarinic [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine/) receptor with N-terminal FLAG epitope tag, N-terminus truncated (residues 1-21 removed by [HRV 3C Protease](/xray-mp-wiki/reagents/additives/hrv-3c-protease/) cleavage at engineered HRV 3C site), residues 226-389 of ICL3 replaced by minimal Cys-free T4 lysozyme fusion (mT4L), and C-terminal deca-histidine tag. Expressed using the Bac-to-Bac Baculovirus Expression System (Invitrogen) in Sf9 cells.


### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Sf9 cell expression | Baculovirus expression in Sf9 insect cells | -- | -- + -- | Cells infected at density of 4.0-5.0 x 10^6 cells/mL, treated with 10 uM [Atropine](/xray-mp-wiki/reagents/ligands/atropine/), harvested at 60 hours |
| Solubilization | Membrane solubilization in presence of [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium/) | -- | -- + -- | Receptor solubilized and purified in presence of [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium/) as previously described for M3 receptor |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA resin | -- + -- | First purification step via C-terminal His tag |
| FLAG [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | FLAG [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | FLAG affinity resin | -- + -- | Second purification step via N-terminal FLAG epitope tag |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | Size exclusion column | -- + -- | N-terminus cleaved with [HRV 3C Protease](/xray-mp-wiki/reagents/additives/hrv-3c-protease/) (2% w/w) during concentration prior to SEC (~2hr at 4 degrees C). Purified receptor concentrated to 85 AU (~50 mg/mL) and flash frozen in small aliquots using liquid nitrogen. |


## Crystallization

### doi/10.1038##nature17188

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | M4-mT4L bound to [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium/), reconstituted by mixing protein solution into 10:1 (w/w) [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/):[Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) in 1:1.5 parts w/w protein:lipid ratio using the two-syringe method. Sample volume 20-40 nL.
 |
| Temperature | 20 degrees Celsius |
| Growth time | Initial crystals formed after 24 hours |
| Cryoprotection | Crystals harvested using mesh grid loops and stored in liquid nitrogen |
| Notes | M4-mT4L crystallized in space group P 1 21 1. Data processed using XDS. Structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using inactive M2 structure (PDB: 3UON) and inactive M3-mT4L (PDB: 4U15) as search models for receptor and mT4L fusion domains respectively. Refinement carried out in Phenix with manual building in Coot. 64 crystals used. Final Rwork/Rfree: 22.7%/24.0%.
 |


## Biological / Functional Insights

### M4-specific rotameric change of D112 (3.32)

The M4 receptor exhibits a unique rotameric change of D112 (3.32) compared to M1, M2, and M3 structures. This residue is conserved throughout biogenic amine GPCRs and serves as the counter-ion for positively charged neurotransmitters. In the M4 structure, D112 (3.32) points away from [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium/) and is accompanied by slight movements of Y439 (7.39) and Y443 (7.43), allowing them to form a network of hydrogen bond interactions between D112 (3.32), S85 (2.57), W108 (3.28), Y439 (7.39), and Y443 (7.43). This hydrogen bond network is distinct from M1, M2, and M3 muscarinic receptor structures.

### Intact ionic lock in M4 receptor

The M4 receptor was crystallized with an intact ionic lock, a feature uncommonly seen in other GPCRs and not present in other muscarinic structures. Chain B of the M4 receptor shows R (3.50) forming hydrogen bonds with T (6.34) and E (6.30). This contrasts with the other muscarinic receptor structures where the ionic lock is disrupted.

### PEG 300 as allosteric modulator

[PEG](/xray-mp-wiki/reagents/additives/peg/) 300, a required precipitant for crystallization, was found to occupy the allosteric binding site of the inactive-state M4 receptor. Surrounding the [PEG](/xray-mp-wiki/reagents/additives/peg/) 300 molecule are residues forming the allosteric site from the top regions of TM2, TM3, and TMs 5-7. [PEG](/xray-mp-wiki/reagents/additives/peg/) 300 sits immediately above the aromatic cage composed of Y113 (3.33), Y416 (6.51), Y439 (7.39), and Y443 (7.43). [PEG](/xray-mp-wiki/reagents/additives/peg/) 300 was confirmed to act as an allosteric modulator through its ability to retard the dissociation of [3H][NMS](/xray-mp-wiki/reagents/ligands/n-methylscopolamine/) in a concentration-dependent manner with an apparent affinity of approximately 10 mM for the NMS-occupied M4 receptor.

### Allosteric network linking orthosteric and allosteric sites

A network of residues was identified that links the allosteric and orthosteric sites of the M4 receptor, involving the interface between TMs 2, 3, 6, and 7, and extending along the top of ECL2. This network was mapped through mutagenesis studies examining cooperativity between [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine/) and the PAM [LY2033298](/xray-mp-wiki/reagents/ligands/ly2033298/). Residues including W435 (7.35), F186 (ECL2), Y113 (3.33), Y416 (6.51), Y439 (7.39), Y89 (2.61), W108 (3.28), L109 (3.29), N423 (6.58), and others were found to significantly affect cooperativity upon mutation. The TM2/3/7 interface may act as a hinge mediating conformational rearrangements in the extracellular vestibule between inactive and active states.

### Comparison with M1-M3 receptor structures

The M4 structure is overall similar to M1, M2, and M3 with RMSD of 0.6-0.9 A (excluding [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) fusions). The M4 structure reveals differences in the allosteric vestibule that are strikingly divergent between subtypes, while the orthosteric site residues are highly conserved. The M4 structure, together with M1, M2, and M3 structures, provides a near complete view of the inactive state of the muscarinic receptor subfamily.


## Cross-References

- [M1 Muscarinic Acetylcholine Receptor](/xray-mp-wiki/proteins/gpcr/m1-muscarinic-acetylcholine-receptor/) — Related muscarinic receptor subtype; co-crystallized with tiotropium in same study
- [Human M2 Muscarinic Acetylcholine Receptor](/xray-mp-wiki/proteins/gpcr/m2-muscarinic-acetylcholine-receptor/) — Related muscarinic receptor subtype; used as search model for M4 structure determination (PDB 3UON)
- [M3 Muscarinic Acetylcholine Receptor](/xray-mp-wiki/proteins/gpcr/m3-muscarinic-acetylcholine-receptor/) — Related muscarinic receptor subtype; used as search model for mT4L fusion (PDB 4U15)
- [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium/) — Inverse agonist co-crystallized with M4 receptor (PDB 5DSG)
- [mT4L (Minimal T4 Lysozyme)](/xray-mp-wiki/proteins/gpcr/mt4l-lysozyme/) — Minimal T4 lysozyme fusion used to replace ICL3 for crystallization
- [Flag Epitope Tag (DYKDDDDK)](/xray-mp-wiki/reagents/protein-tags/flag-tag/) — N-terminal FLAG tag used for purification and as crystallization construct component
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — LCP lipid matrix used for M4 crystallization (10:1 monoolein:cholesterol)
- [Allosteric Regulation in Membrane Proteins](/xray-mp-wiki/concepts/allosteric-regulation/) — M4 receptor allosteric site and cooperativity network central to paper findings
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Method used in structure determination or purification
