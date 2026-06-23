---
title: "Leptosphaeria Rhodopsin (LR/Mac)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s42003-021-02326-4]
verified: false
---

# Leptosphaeria Rhodopsin (LR/Mac)

## Overview

Leptosphaeria rhodopsin (LR), also referred to as LR (Mac), is a light-driven
proton pump from the pathogenic fungus Leptosphaeria maculans (a major pathogen
of Brassica napus, oilseed rape). LR is a microbial (type 1) rhodopsin belonging
to the heptahelical transmembrane (7TM) protein family that covalently binds
an all-trans-retinal chromophore. The first high-resolution structure of a
fungal rhodopsin was determined at 2.2 A resolution using [Lipidic Cubic Phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/)
(in meso) crystallization. The structure revealed striking similarity of its
membrane core to archaeal rhodopsins (particularly [bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/))
rather than bacterial rhodopsins. An unusually long N-terminal region stabilizes
the protein through direct interaction with extracellular loop 2 (ECL2).
Structure-based phylogenetic analysis of all available light-driven proton pump
structures supports an archaeal origin of eukaryotic proton-pumping rhodopsins.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s42003-021-02326-4 | Not explicitly stated in raw paper | 2.2 | P 21 21 21 | Full-length LR (residues 1-313) from Leptosphaeria maculans, C-terminal polyhistidine tag (H6/H9), expressed in Leishmania tarentolae | all-trans-retinal (covalently bound via Schiff base) |

## Expression and Purification

- **Expression system**: Leishmania tarentolae (LEXSY expression system)
- **Construct**: LR 1-313 (full-length) and LR 49-313 (N-terminally truncated) with
C-terminal polyhistidine tags (H6 and H9), in pLEXSY_I-blecherry3 vector

- **Notes**: Genes synthesized de novo, codon-optimized for Leishmania tarentolae expression.
Cells grown at 26°C in Brain-Heart-Infusion Broth, induced with tetracycline.
10 µM all-trans-retinal added for LR 1-313 construct. Average yield: 20 mg/L
for LR 1-313, 10 mg/L for LR 49-313.


### Purification Workflow

- **Expression system**: Leishmania tarentolae (LEXSY)
- **Expression construct**: Full-length LR 1-313 with C-terminal H6/H9 tag; truncated LR 49-313
- **Tag info**: C-terminal polyhistidine tag (H6 and H9)

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell disruption | Microfluidizer (M-110P Lab Homogenizer) | -- | 50 mM NaH2PO4/Na2HPO4 pH 7.6, 0.1 M NaCl, 10% glycerol, 1 mM EDTA, 2 mM 6-aminohexanoic acid, 50 mg/L DNase I, cOmplete protease inhibitor cocktail + -- | Cells disrupted at 10,000 psi |
| Membrane isolation | Ultracentrifugation | -- | Same buffer without DNase I + -- | 120,000 x g for 1 h at 4°C, repeated once after resuspension |
| Solubilization | Detergent solubilization | -- | 20 mM HEPES pH 8.0, 0.2 M NaCl, cOmplete protease inhibitor + 1% n-dodecyl β-D-maltoside (DDM) | Membranes stirred overnight at 4°C; 20 µM all-trans-retinal added for LR 1-313, 5 µM for LR 49-313; insoluble fraction removed by ultracentrifugation |
| Ni-NTA affinity chromatography | Immobilized metal affinity chromatography | Ni-NTA resin (Cube Biotech) | 20 mM HEPES pH 7.5, 0.2 M NaCl, 0.25 M L-Histidine, 0.1 mM PMSF, 2 mM 6-aminohexanoic acid, cOmplete + 0.1% DDM | Eluted with L-Histidine-containing buffer |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex 200 Increase 10/300 GL (GE Healthcare) | 10 mM NaH2PO4/Na2HPO4 pH 6.5, 0.2 M NaCl, 1 mM EDTA, 2 mM 6-aminohexanoic acid, 0.1 mM PMSF, cOmplete + 0.05% DDM | A280/A540 absorbance ratio ~1.5; concentrated to 30-40 mg/ml for crystallization |


## Crystallization

### doi/10.1038##s42003-021-02326-4

| Parameter | Value |
|---|---|
| Method | [Lipidic Cubic Phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) (in meso) crystallization |
| Protein sample | Purified LR at 30-40 mg/ml in 10 mM NaH2PO4/Na2HPO4 pH 6.5, 0.2 M NaCl, 0.05% DDM |
| Lipid | Monoolein |
| Protein-to-lipid ratio | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Crystals grown using in meso approach. Structure determined at 2.2 A resolution. Space group P 21 21 21, cell dimensions: a=63.54, b=70.78, c=148.02 A. Data collected at ESRF synchrotron beamlines. Rwork/Rfree = 23.8/28.5%. |


## Biological / Functional Insights

### Structural similarity to archaeal rhodopsins

The membrane core of LR is strikingly similar to bacteriorhodopsin (HsBR)
and other archaeal proton-pumping rhodopsins, supporting a common archaeal
ancestor for eukaryotic proton pumps. Key functional regions including the
retinal binding pocket, proton release, and proton uptake regions are highly
conserved. In contrast, bacterial proton pumps (e.g., GR) form a distinct
structural cluster.

### N-terminal domain stabilizes the extracellular side

LR features an unusually long N-terminal region (residues 42-48) that forms
a beta-strand and directly interacts with extracellular loop 2 (ECL2) through
seven hydrogen bonds. Nano-DSF thermal stability measurements showed the
full-length protein (LR 1-313) has a single melting temperature of 66.5°C,
while the N-terminally truncated construct (LR 49-313) shows two inflection
points at 49.3°C and 64.8°C, indicating significant destabilization upon
N-terminal truncation.

### Trimeric oligomeric state

Glutaraldehyde cross-linking and size-exclusion chromatography in DDM
micelles indicate LR exists predominantly as a trimer, with stoichiometry
of 3 and lower. The calculated molar mass from SEC (99 kDa for LR 1-313,
73 kDa for LR 49-313) is consistent with trimeric and monomeric forms.
Template-based modeling using archaeorhodopsin-2 (PDB: 3WQJ) predicts a
trimer with monomer-monomer interface area of 1799 A^2. Truncation of the
N-terminus dramatically shifts the monomer:trimer ratio from ~2:5 to ~40:1.

### Proton translocation and photocycle

LR functions as a light-driven outward proton pump. Key regions involved in
proton transport include the retinal Schiff base (RSB), proton acceptor,
proton release group, and proton uptake region. Spectroscopic characterization
reveals a photocycle with five intermediates. Proton-pumping experiments in
POPC:POPS proteoliposomes showed full-length LR achieves higher proton-pumping
activity (0.3 pH units) than the truncated construct (0.1 pH units) at pH 6.5.

### Structure-based evolution of rhodopsins

Structure-based phylogenetic analysis using 16 available proton pump
structures from the PDB demonstrates that archaeal and eukaryotic proton
pumps cluster together, while bacterial proton pumps form a separate cluster.
This structural evidence, combined with functional similarities (pH dependence
of photocycle, intermediate states), provides strong support for an archaeal
origin of eukaryotic proton-pumping rhodopsins, likely inherited from the
archaeal ancestors of eukaryotes.


## Cross-References

- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — LR shows striking structural similarity to archaeal HsBR in membrane core architecture
- [Coccomyxa subellipsoidea Rhodopsin (CsR)](/xray-mp-wiki/proteins/rhodopsins/coccomyxa-rhodopsin/) — CsR is another eukaryotic proton pump rhodopsin with known structure
- [Acetabularia Rhodopsin II](/xray-mp-wiki/proteins/rhodopsins/acetabularia-rhodopsin-ii/) — ARII is a characterized eukaryotic rhodopsin used for structural comparison
- [Archaerhodopsin-1](/xray-mp-wiki/proteins/rhodopsins/archaerhodopsin-1/) — Archaeal proton pump used as reference in phylogenetic analysis
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LR was crystallized using in meso approach
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — DDM used for solubilization and purification of LR
- [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) — All-trans-retinal is the chromophore covalently bound to LR
- [Rhodopsin Photocycle](/xray-mp-wiki/concepts/rhodopsin-mechanisms/rhodopsin-photocycle/) — LR exhibits a characteristic rhodopsin photocycle with five intermediates
