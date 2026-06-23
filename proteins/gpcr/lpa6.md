---
title: Lysophosphatidic Acid Receptor 6 (LPA6/P2Y5)
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature23448]
verified: false
---

# Lysophosphatidic Acid Receptor 6 (LPA6/P2Y5)

## Overview

Lysophosphatidic acid receptor 6 (LPA6, also known as P2Y5 or LPAR6) is a class A G protein-coupled receptor that belongs to the phylogenetically distant non-EDG family of LPA receptors (LPA4-LPA6). LPA6 is activated by lysophosphatidic acid (LPA), a bioactive lipid composed of a phosphate group, a glycerol backbone, and a single acyl chain. Unlike the EDG family LPA receptors (LPA1-LPA3), the non-EDG family shares sequence similarity with the P2Y family of nucleotide receptors. LPA6 regulates hair follicle formation, and null mutations in LPAR6 or the upstream LPA-producing enzyme PA-PLA1alpha (LIPH) cause autosomal recessive wooly hair/hypotrichosis, a congenital hair disease. LPA6 is also involved in cancer progression. The 3.2 A crystal structure of zebrafish LPA6a revealed a laterally open ligand-binding pocket towards the membrane and provided insights into the LPA recognition mechanism of non-EDG family LPA receptors.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature23448 | 5XSZ | 3.20 | P2_12_12_1 | Zebrafish LPA6a (Uniprot Q08BG4) with C-terminal truncation (residues 313-357 removed) and T4L insertion in ICL3 between V227 and L233; monoolein-bound; inactive state | Monoolein (MO1-MO3) |

## Expression and Purification

- **Expression system**: Sf9 insect cells (Bac-to-Bac baculovirus expression system)
- **Construct**: Zebrafish LPA6a (Uniprot Q08BG4) with N-terminal HA signal + Flag tag + TEV site; C-terminal TEV site + eGFP-His6 tag; C-terminal truncation (residues 313-357 removed); T4L inserted in ICL3 between V227 and L233 for crystallization
- **Notes**: Sf9 cells infected at 3 x 10^5 cells/mL, incubated 48 h at 27 C. Cells collected by centrifugation, resuspended in 50 mM Na-citrate pH 5.0, 150 mM NaCl, 10% glycerol with protease inhibitors.

### Purification Workflow

- **Expression system**: Sf9 insect cells
- **Expression construct**: Zebrafish LPA6a with N-term HA-Flag-TEV and C-term TEV-eGFP-His6 tags; C-terminal truncation (313-357); T4L fusion in ICL3
- **Tag info**: HA signal + Flag epitope (N-term), eGFP-His6 tag (C-term)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Sonication |  | 50 mM Na-citrate pH 5.0, 150 mM NaCl, 10% glycerol, 0.1 mM PMSF, 1.0 ug/mL aprotinin, 0.4 ug/mL leupeptin | Cells disrupted by sonication; membrane fraction collected by ultracentrifugation at 125,000g for 1 h at 4 C |
| Membrane solubilization | Detergent solubilization |  | 50 mM Na-citrate pH 5.0, 150 mM NaCl, 10% glycerol, 0.1 mM PMSF, 1.0 ug/mL aprotinin, 0.4 ug/mL leupeptin, 2 mg/mL iodoacetamide + 1% DDM + 0.2% CHS | Solubilization for 2 h at 4 C; insoluble material removed by ultracentrifugation at 125,000g for 30 min |
| Ni Sepharose affinity chromatography | Immobilized metal affinity chromatography | Ni Sepharose excel resin (GE Healthcare) | 50 mM Na-citrate pH 5.0, 150 mM NaCl, 10% glycerol, 0.1 mM PMSF, 1.0 ug/mL aprotinin, 0.4 ug/mL leupeptin, 20 mM imidazole + 0.1% DDM + 0.02% CHS | Batch incubation for 1.5 h at 4 C; washed with 10 column volumes; eluted with 300 mM imidazole |


## Crystallization

### doi/10.1038##nature23448

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | Purified LPA6-T4L fusion protein (after TEV cleavage to remove eGFP-His6 tag) |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) (90% w/w) + [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) (10% w/w) |
| Protein-to-lipid ratio | 2:3 (protein:lipid) |
| Temperature | 20 C |
| Growth time | 3-4 wk |
| Notes | 241 crystals merged into single dataset for 3.2 A resolution structure. Data collected at SPring-8 BL32XU beamline using 10 um minibeam. Rastering used to find best diffracting crystal regions. |


## Biological / Functional Insights

### Laterally open ligand-binding pocket of LPA6

The LPA6 structure reveals a unique laterally open ligand-binding pocket where a hydrophobic vertical cleft between TM4 and TM5 remains half-exposed to the lipid bilayer. This cleft accommodates the acyl chain of LPA, extending from the middle of the lipid bilayer. The central cavity includes aromatic and aliphatic residues creating a hydrophobic environment suitable for lipidic ligands. This "open" architecture differs from the sealed binding pockets of most class A GPCRs and allows LPA6 to laterally receive membrane-embedded LPA molecules produced by PA-PLA1alpha.

### Conserved positively charged residues recognize LPA phosphate

Five conserved positively charged residues (K26^1.31, R83^2.60, K188^5.32, R267^6.62, R281^7.32) are located at the periphery of the central cavity and mediate recognition of the negatively charged phosphate head group of LPA. Mutagenesis confirmed that K26^1.31, R83^2.60, R267^6.62 and R281^7.32 are critical for phosphate recognition, as alanine or glutamate mutations caused large reductions in receptor activity and LPA binding.

### TM6/TM7 inward shift mechanism for receptor activation

Docking simulations combined with mutagenesis suggest that LPA binding induces an inward shift of TM6 and TM7, bringing the positively charged residues on these helices (R267^6.62 and R281^7.32) into the central cavity to fully recognize the phosphate group. This inward shift mechanism is analogous to that observed in the evolutionarily related P2Y12 ADP receptor, where agonist binding induces TM6/TM7 closure. The motion of TM6 is crucial for coupling agonist binding to cytoplasmic G protein activation.

### Acyl chain binding and vertical cleft interactions

The acyl chain of LPA binds in the hydrophobic vertical cleft between TM4 and TM5, positioned between G157^4.56 and I198^5.42, with the chain terminus near L115^3.41, L153^4.52 and V201^5.45. Residues I198^5.42, V195^5.39, G157^4.56 and T161^4.60 are critical for acyl chain binding. LPA6 exhibits highest preference for LPA species with the linoleoyl (18:2) acyl chain. The synthetic potent agonist 2-alkyl-OMPT-(R), a stable analogue of 2-acyl LPA, was used for sensitive activity measurements.

### Structural similarity with P2Y family receptors

The LPA6 structure shows unexpected similarity to P2Y family ADP receptors. The pocket formed by TM3, TM4 and TM5 is a common structural feature among the P2Y family receptors and non-EDG family LPA receptors. In P2Y12, the adenine ring of ADP inserts into the same region as the LPA acyl chain in LPA6, indicating that both receptors use the same region to accommodate the "non-phosphate" moiety of their endogenous ligands. Other P2Y-related lipid receptors, such as lysophosphatidylserine receptors, may also use this pocket for acyl chain recognition.


## Cross-References

- [Lysophosphatidic Acid Receptor 1 (LPA1)](/xray-mp-wiki/proteins/lpa1) — LPA1 is an EDG-family LPA receptor with distinct binding pocket architecture; sequenced and structurally compared
- [P2Y12 Receptor](/xray-mp-wiki/proteins/p2y12-receptor) — Evolutionarily related P2Y family receptor sharing similar TM6/TM7 inward shift activation mechanism
