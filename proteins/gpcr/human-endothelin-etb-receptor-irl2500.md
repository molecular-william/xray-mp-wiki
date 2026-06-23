---
title: "Human Endothelin ETB Receptor in Complex with IRL2500"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s42003-019-0482-7]
verified: false
---

# Human Endothelin ETB Receptor in Complex with IRL2500

## Overview

The human endothelin ETB receptor (ETB) is a class A GPCR that binds the endogenous
peptide hormone endothelin-1 (ET-1). [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) is a peptide-mimetic of the C-terminal
tripeptide of ET-1 that functions as a potent ETB-selective inverse agonist. The
crystal structure of the thermostabilized ETB receptor (ETB-Y4-mT4L) in complex
with [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) was determined at 2.7 Å resolution. The structure reveals that the
biphenyl group of [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) penetrates into the transmembrane core proximal to
D[2.50], stabilizing the inactive conformation. [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) functions as an inverse
agonist, as demonstrated using a constitutively active ETB mutant (L192[3.43]Q).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s42003-019-0482-7 | 6K1Q | 2.7 | I422 | ETB-Y4-mT4L (thermostabilized ETB receptor with R124Y[1.55], K270A[5.35], S342A[6.54], I381A[7.48] mutations; mT4L inserted in ICL3 between K303[5.68] and L311[6.23]; C396A/C400A/C405A; N-terminal deletion G57-L66; C-terminus truncated after S407; C-terminal TEV-GFP-His10 tag) | [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) |

## Expression and Purification

- **Expression system**: Sf9 insect cells using Bac-to-Bac baculovirus expression system (Invitrogen)
- **Construct**: ETB-Y4-mT4L subcloned into modified pFastBac vector with C-terminal TEV cleavage site followed by GFP-His10 tag

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and infection | Baculovirus infection of Sf9 cells | — | Sf900 II medium | Infected at cell density of 4.0 x 10^6 cells per ml, grown for 48 h at 27°C |
| Cell disruption | Sonication | — | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) | Crude membrane fraction collected by ultracentrifugation at 180,000 g for 1 h |
| Solubilization | Detergent solubilization | — | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 200 mM NaCl, 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.2% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 10 μM [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/), 2 mg/ml [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) | Solubilized for 1 h at 4°C; supernatant clarified by ultracentrifugation at 180,000 g for 20 min |
| Immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) (IMAC) | [TALON](/xray-mp-wiki/reagents/additives/talon/) resin (Clontech) | [TALON](/xray-mp-wiki/reagents/additives/talon/) cobalt affinity resin | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 500 mM NaCl, 0.1% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 10 μM [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/), 15 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (wash); 200 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (elution) | Incubated with [TALON](/xray-mp-wiki/reagents/additives/talon/) resin for 30 min; washed with 10 column volumes; eluted with 200 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| TEV protease cleavage and tag removal | TEV cleavage and dialysis | — | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 500 mM NaCl, 10 μM [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) | TEV protease treatment during dialysis; cleaved GFP-His10 tag removed with Co2+-NTA resin |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex200 10/300 Increase column | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 150 mM NaCl, 0.01% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.001% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 10 μM [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) | Peak fractions pooled and concentrated to 40 mg/ml using centrifugal filter device (Millipore 50 kDa MW cutoff); [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) added to 100 μM final concentration during concentration |


## Crystallization

### doi/10.1038##s42003-019-0482-7

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | Purified ETB-Y4-mT4L-[IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) complex at 40 mg/ml |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) and [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) (10:1 by mass) |
| Temperature | 20°C |
| Notes | Protein-laden mesophase dispensed into 96-well glass plates in 30 nl drops overlaid with 800 nl precipitant solution by Gryphon LCP robot. Crystals harvested directly from LCP using micromounts or LithoLoops, frozen in liquid nitrogen without extra cryoprotectant. |


## Biological / Functional Insights

### IRL2500 binds in a distinct mode from ET-1 and bosentan

[IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) is designed to mimic the F14, I19, I20, and W21 residues of ET-1.
While the electrostatic interactions between the carboxylates and positively
charged residues are conserved between [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) and ET-1 binding, the biphenyl
group of [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) penetrates into the receptor core in an opposite manner to
the F14 and I20 of ET-1. The tryptophan of [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) superimposes with I20
of ET-1 rather than W21, while the dimethylbenzoyl group of [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/)
superimposes with W21 of ET-1.

### IRL2500 as an inverse agonist stabilizing the inactive conformation

[IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) functions as an inverse agonist for the ETB receptor. The biphenyl
group of [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) penetrates into the transmembrane core proximal to D147[2.50],
stabilizing the inactive conformation. This is analogous to other class A GPCR
inverse agonists such as ritanserin-bound 5-HT2CR and BIIL260-bound [Leukotriene B4 Receptor 1 (BLT1) — Guinea Pig and Human](/xray-mp-wiki/proteins/gpcr/blt1/),
which also interact near the sodium binding site.

### ETB-selectivity mechanism of IRL2500

ETB-selectivity of [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) is attributed to residues Y129[2.53] and F161[3.28]
in the ETA receptor, which specifically clash with [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/). The H150Y and V177F
mutations in ETA (corresponding to ETB residues) selectively reduce [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/)
potency without affecting bosentan potency. The S376T mutation in ETB increases
[IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) potency by 4-fold.

### Constitutively active ETB mutant L192[3.43]Q

The L192[3.43]Q mutation in ETB confers constitutive activity, as measured by
AP-TGFα shedding assay. Using this mutant, [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) was shown to reduce basal
signaling, confirming its inverse agonist activity. Bosentan, K-8794, and BQ-788
also showed inverse agonist activity in this assay.


## Cross-References

- [Human Endothelin ETB Receptor Bound to Endothelin-1](/xray-mp-wiki/proteins/gpcr/human-endothelin-etb-receptor-et1/) — Same ETB receptor bound to agonist ET-1 for comparison of binding modes
- [Human Endothelin ETB Receptor Bound to Bosentan](/xray-mp-wiki/proteins/gpcr/etb-receptor-bosentan/) — Same ETB receptor bound to clinical antagonist for comparison
- [Human Endothelin ETB Receptor in Complex with Sarafotoxin S6b](/xray-mp-wiki/proteins/gpcr/etb-s6b-complex/) — Related ETB receptor structure with snake toxin agonist
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for membrane solubilization
- [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) — Detergent used in IMAC wash and SEC buffers
- [T4 Lysozyme (T4L) fusion](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) — mT4L insertion in ICL3 enabled crystallization
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used for ETB receptor crystallization
- [GPCR Active Conformation](/xray-mp-wiki/concepts/signaling-receptors/gpcr-active-conformation/) — IRL2500 stabilizes the inactive conformation, relevant to GPCR activation mechanism
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Leukotriene B4 Receptor 1 (BLT1) — Guinea Pig and Human](/xray-mp-wiki/proteins/gpcr/blt1/) — Related protein structure
