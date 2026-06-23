---
title: Rat Kynurenine 3-Monooxygenase (Rat KMO)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s42003-021-01666-5]
verified: false
---

# Rat Kynurenine 3-Monooxygenase (Rat KMO)

## Overview

Rat Kynurenine 3-monooxygenase (KMO) from Rattus norvegicus is a class A flavoprotein
monooxygenase and a single-pass transmembrane mitochondrial enzyme that catalyses
the hydroxylation of L-kynurenine to 3-hydroxykynurenine (3-HK) in the eukaryotic
tryptophan catabolic (kynurenine) pathway. Despite predictions suggesting two
transmembrane domains, the full-length crystal structure revealed KMO is actually
a single-pass transmembrane protein, with the other predicted transmembrane domain
lying laterally along the membrane where it forms part of the ligand-binding pocket.
KMO functions as a dimer and is linked to various neurological disorders including
Huntington's disease, pain, and neurodegenerative conditions. The structure was
determined in its membrane-embedded form using [Lipidic Cubic Phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/)
(in meso) crystallization, complexed with potent inhibitors identified through
medicinal chemistry and DNA-encoded chemical library screening.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s42003-021-01666-5 | Not explicitly stated in raw paper | 3.0 | C 1 2 1 | Full-length Rat KMO (residues 1-478), N-terminal GST-tag with thrombin cleavage site, C-terminal TEV site followed by FLAG tag | Compound 3 (KMO inhibitor) and FAD cofactor |
| doi/10.1038##s42003-021-01666-5 | Not explicitly stated in raw paper | 3.0 | C 1 2 1 | Full-length Rat KMO (residues 1-478), N-terminal GST-tag with thrombin cleavage site, C-terminal TEV site followed by FLAG tag | Compound 4 (KMO inhibitor from DNA-encoded chemical library) and FAD cofactor |

## Expression and Purification

- **Expression system**: Spodoptera frugiperda Sf9 cells (Bac-to-Bac Baculovirus Expression System)
- **Construct**: Full-length KMO (1-478) with N-terminal GST-tag (thrombin-cleavable) and
C-terminal TEV-FLAG tag

- **Notes**: Sf9 cells infected at 2-3 x 10^6 cells/mL with baculovirus MOI of 0.1,
grown at 27°C, collected 2 days post-infection


### Purification Workflow

- **Expression system**: Sf9 insect cells (Bac-to-Bac baculovirus)
- **Expression construct**: GST-thrombin-KMO-TEV-FLAG (full-length 1-478)
- **Tag info**: N-terminal GST (thrombin-cleavable), C-terminal FLAG (TEV-cleavable)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell disruption and solubilization | Sonication | -- | 20 mM potassium phosphate pH 7.5, 10% glycerol, 300 mM NaCl, 7 mM 2-mercaptoethanol, 50 µM FAD, protease inhibitors + 0.5% n-dodecyl β-D-maltoside (DDM) | Cells disrupted by sonication in lysis buffer; insoluble debris removed by centrifugation |
| Glutathione affinity chromatography | Batch purification | Glutathione Sepharose 4 Fast Flow (GE Healthcare) | 20 mM potassium phosphate pH 7.5, 10% glycerol, 300 mM NaCl + 0.012% DDM | Resin washed with same buffer; eluted with 33 mM glutathione |
| Buffer exchange and concentration | Ultrafiltration | AmiconUltra-15 Centrifugal Filters 50k (Millipore) | 20 mM potassium phosphate pH 7.5, 10% glycerol, 300 mM NaCl + 0.012% DDM | Concentrated, then desalted via PD-10 (GE Healthcare) to remove glutathione |
| Thrombin digestion | Proteolytic tag removal | -- | Not specified + Not specified | Digested with thrombin (Novagen) at 10 U/mg at 4°C to remove GST tag |


## Crystallization

### doi/10.1038##s42003-021-01666-5

| Parameter | Value |
|---|---|
| Method | [Lipidic Cubic Phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) (in meso) crystallization |
| Protein sample | Purified Rat KMO after thrombin cleavage, in complex with compound 3 |
| Lipid | Monoolein |
| Protein-to-lipid ratio | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Structure determined at 3.0 A resolution. Space group C 1 2 1, cell dimensions: a=160.97, b=63.43, c=152.42 A, beta=113.5 deg. Two structures solved: complex with compound 3 and complex with compound 4. |

| Parameter | Value |
|---|---|
| Method | [Lipidic Cubic Phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) (in meso) crystallization |
| Protein sample | Purified Rat KMO after thrombin cleavage, in complex with compound 4 |
| Lipid | Monoolein |
| Protein-to-lipid ratio | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Structure determined at 3.0 A resolution. Space group C 1 2 1, cell dimensions: a=161.51, b=63.42, c=152.66 A, beta=113.4 deg. |


## Biological / Functional Insights

### Single-pass transmembrane architecture

Despite computational predictions suggesting two transmembrane domains, the
crystal structure revealed that KMO is a single-pass transmembrane protein.
The second predicted transmembrane segment (alpha-12) lies laterally along the
membrane surface and forms part of the ligand-binding pocket. Electrostatic
potential and hydrophobicity analysis confirmed the non-polar surface of the
alpha-12 helix is partially embedded in the membrane.

### KMO functions as a physiological dimer

The crystal structure reveals a dimeric arrangement with 10 inter-beta-sheet
hydrogen bonds linking protomers. NanoBRET measurements in HEK293T cells
confirmed dimerization of human KMO at the cellular level. Mutations at the
dimer interface (D184A, Y185P, Q187A) significantly reduced BRET signal and
abolished catalytic activity, confirming the functional unit of KMO is a dimer.

### Ligand-binding pocket architecture

The ligand-binding pocket features a polar side (interacting with R85) and a
hydrophobic side. The carboxylic acid moiety of inhibitors fits into the polar
side, while hydrophobic regions engage the opposite side. The alpha-12 helix
contributes to the binding pocket. Compound 4 binding induced a conformational
change in Y398, which flips to accommodate the methyl group and isoindoline
ring of compound 4.

### Brain-penetrant inhibitor design

Replacing the carboxylic acid moiety of compound 3 yielded compound 5, which
showed significantly improved brain penetration (Kp,brain = 0.80) compared to
compound 1 (Kp,brain = 0.029). Compound 5 achieved 6025 ng/g in brain tissue
versus 7560 ng/mL in plasma. This bioisosteric approach enables targeting of
KMO for neurological indications where blood-brain barrier penetration is critical.


## Cross-References

- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — KMO was crystallized in meso (lipidic cubic phase) for structure determination
- [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) — KMO was expressed in Sf9 insect cells using the Bac-to-Bac baculovirus system
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — DDM used for membrane protein solubilization and throughout purification
- [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) — C-terminal FLAG tag used in KMO expression construct
- [TEV Protease](/xray-mp-wiki/reagents/protein-tags/tevp-protease/) — TEV cleavage site included between KMO and C-terminal FLAG tag
