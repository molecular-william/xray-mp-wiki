---
title: Human Endothelin ETB Receptor Bound to Endothelin-1
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature19319]
verified: false
---

# Human Endothelin ETB Receptor Bound to Endothelin-1

## Overview

The human endothelin ETB receptor is a class A GPCR that binds the endogenous
  21-amino-acid peptide hormone endothelin-1 (ET-1) with sub-nanomolar affinity in
a virtually irreversible manner. Crystal structures of the thermostabilized ETB
receptor in the ligand-free form (PDB 5GLI) and in complex with ET-1 (PDB 5GLH,
  2.8 Å resolution) reveal the mechanism of isopeptide selectivity and
agonist-induced activation. ET-1 binds with an ~1,500 Å2 interaction surface -
the largest among peptide-activated GPCRs - with TM1, TM2, TM6, and TM7 enveloping
the entire peptide.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature19319 | 5GLH | 2.8 Å | Not specified | ETB-Y5-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) (thermostabilized with R124Y, D154A, K270A, S342A, I381A mutations; [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) inserted in ICL3; C396A/C400A/C405A; Flag-Nt-TEV site; C-terminus truncated after Ser407) | Endothelin-1 (ET-1) |
| doi/10.1038##nature19319 | 5GLI | Not specified | Not specified | ETB-Y5-mT4L (thermostabilized; mT4L in ICL3; C-terminal GFP-His10 tag) | None (ligand-free form) |

## Expression and Purification

- **Expression system**: Sf9 insect cells using Bac-to-Bac baculovirus expression system
- **Construct**: HA signal peptide-Flag tag-9aa linker-ETB-Y5-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) or -mT4L; TEV protease site between Gly57 and Leu66; C-terminus truncated after Ser407

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell disruption and membrane preparation | High-pressure homogenizer | -- | 10 mM HEPES-NaOH pH 7.5, 10 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/), 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1 mM PMSF + -- | Emulsiflex-C5 homogenization; membranes collected by ultracentrifugation |
| Solubilization | Detergent solubilization | -- | 10 mM HEPES-NaOH pH 7.5, 200 mM NaCl, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), protease inhibitors + 1% n-dodecyl-beta-D-maltoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) + 0.2% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Solubilized for 2 h at 4°C; ET-1 added during purification |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [TALON](/xray-mp-wiki/reagents/additives/talon/) cobalt affinity resin | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 500 mM NaCl + 0.1% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) + 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Bound for 30 min; washed with 10 CV; eluted with 200 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| TEV protease cleavage and tag removal | TEV cleavage and reverse IMAC | [TALON](/xray-mp-wiki/reagents/additives/talon/) resin | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 500 mM NaCl + -- | TEV protease (1:20 w/w) overnight; cleaved GFP-His10 tag removed by [TALON](/xray-mp-wiki/reagents/additives/talon/) resin |
| Size-exclusion chromatography | Size-exclusion chromatography | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 10/300 column | 10 mM HEPES-NaOH pH 7.5, 200 mM NaCl + 0.01% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) + 0.001% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Peak fractions concentrated to 40 mg/ml for crystallization |


## Crystallization

### doi/10.1038##nature19319

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | ETB-ET1 complex at 40 mg/ml in LCP ([Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/)/cholesterol 8:9:1) |
| Temperature | 20°C |
| Growth time | Not specified |
| Cryoprotection | Cryocooled for data collection |
| Notes | ET-1-bound structure determined at 2.8 Å resolution. Ligand-free structure from mT4L construct. |


## Biological / Functional Insights

### ET-1 binds with the largest interaction surface among peptide-activated GPCRs

Endothelin-1 binds to the ETB receptor with an ~1,500 Å2 interaction surface,
the largest observed among peptide-activated GPCRs. The 21-amino-acid bicyclic
peptide is completely enveloped by TM1, TM2, TM6, and TM7. The C-terminal
tripeptide (Ile19-Ile20-Trp21) penetrates deeply into the orthosteric pocket
in a manner similar to small-molecule drug agonists, explaining the virtually
irreversible binding (Kd in the sub-nanomolar range).

### Isopeptide selectivity between ET-1 and ET-3

Structural comparison and mutation analysis reveal the mechanism for isopeptide
selectivity between ET-1 and ET-3. The N-terminal region of the endothelin
peptides modulates interactions at the alpha-helical and C-terminal binding
interfaces. The ET-1-bound structure provides a foundation for understanding
the distinct pharmacological profiles of the three endothelin isopeptides.

### Conformational changes propagate to the G-protein coupling interface

ET-1 binding induces dramatic rearrangements: TM2, TM6, and TM7 move inward
by 2.6, 4.1, and 4.9 Å respectively, while TM1 moves outward by 4.4 Å.
The orthosteric pocket contracts into a compact closed configuration. The
N-terminal tail and ECL2 form a lid-like architecture. These changes propagate
to the receptor core, with TM7 transmitting signals to the cytoplasmic side,
while TM6 appears primed for G-protein engagement.


## Cross-References

- [Human Endothelin ETB Receptor Bound to Bosentan](/xray-mp-wiki/proteins/gpcr/etb-receptor-bosentan/) — Same ETB receptor bound to clinical antagonist for comparison
- [Human Endothelin ETB Receptor in Complex with Sarafotoxin S6b](/xray-mp-wiki/proteins/gpcr/etb-s6b-complex/) — Related ETB receptor structure with snake toxin agonist
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Primary solubilization detergent
- [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) — Detergent for IMAC wash and SEC buffers
- [Cholesterol Hemisuccinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Additive in purification buffers for receptor stability
- [T4 Lysozyme (T4L) fusion](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) — T4L insertion in ICL3 enabled crystallization
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used for ETB receptor crystallization
- [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) — Receptor expressed in Sf9 insect cells via Bac-to-Bac system
- [GPCR Active Conformation](/xray-mp-wiki/concepts/gpcr-active-conformation/) — ET-1 binding induces conformational changes characteristic of GPCR activation
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
