---
title: Human CC Chemokine Receptor 7 (CCR7)
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2019.07.028]
verified: false
---

# Human CC Chemokine Receptor 7 (CCR7)

## Overview

The CC chemokine receptor 7 (CCR7) is a class A G protein-coupled receptor (GPCR)
that balances immunity and tolerance by homeostatic trafficking of immune cells.
CCR7 mediates responses to chemokines CCL19 and CCL21, guiding B cells, T cells,
and antigen-presenting dendritic cells to lymph nodes. In cancer, CCR7-mediated
trafficking promotes lymph node metastasis, making the receptor a promising
therapeutic target. The crystal structure of human CCR7 was determined at 2.1 A
resolution using a Sialidase NanA fusion protein for crystallization. The structure
reveals the ligand Cmp2105 bound to an intracellular allosteric binding pocket
located between transmembrane helix 7 and helix 8 (TM7-H8 turn), a conserved
pharmacological hotspot among chemokine receptors. Cmp2105 contains a
thiadiazole-dioxide core motif and acts as an intracellular allosteric antagonist
that stabilizes an inactive CCR7 conformation, interfering with G protein and
arrestin binding. A computational screen identified additional CCR7 modulators
including Navarixin (a CXCR1/CXCR2 phase II antagonist), CS-1, and CS-2,
demonstrating that the TM7-H8 allosteric pocket can be targeted by diverse
chemotypes with selectivity across chemokine receptor subtypes.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2019.07.028 | 6QZH | 2.1 | P212121 | Human CCR7-Sialidase NanA fusion with L145W mutation, HRV 3C cleavage sites, deletion of ICL3 residues 248-256 (replaced by NanA residues 1-470) | Cmp2105 |

## Expression and Purification

- **Expression system**: Spodoptera frugiperda (Sf9) insect cells using Bac-to-Bac baculovirus system
- **Construct**: CCR7-Sialidase NanA fusion: N-terminal decahistidine tag, two HRV 3C protease cleavage sites (between residues 36-43 and 352-359), deletion of Arg248-Phe256 (ICL3) replaced by Sialidase NanA (residues 1-470, PDB: 2YA4) flanked by GS linkers, L145W thermostabilizing mutation
- **Notes**: Expressed in 10 L Wave Bioreactors at 27 C, 19 rocks/min, 40% oxygen. Infection at 2x10^6 cells/mL, harvested at 72 h post-infection.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane preparation | Dounce homogenization and ultracentrifugation | — | 10 mM HEPES/NaOH pH 7.5, 10 mM MgCl2, 20 mM KCl, Roche protease inhibitors | Membranes washed extensively with low salt buffer, high salt buffer (1 M NaCl), and low salt buffer. |
| Membrane solubilization | Detergent solubilization | — | 50 mM HEPES/NaOH pH 7.5, 300 mM NaCl, 20 mM imidazole/HCl pH 7.5, 23 uM Cmp2105, protease inhibitors + 1% (w/v) DDM, 0.2% (w/v) CHS | Membranes pre-treated with 23 uM Cmp2105 and 2 mg/mL iodoacetamide for 1 h at 4 C before solubilization. |
| Affinity purification | TALON metal affinity chromatography | — |  | Decahistidine-tagged CCR7-NanA fusion purified using TALON Superflow resin. |
| Size-exclusion chromatography | SEC | — |  | Final polishing step. |


## Crystallization

### doi/10.1016##j.cell.2019.07.028

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | Purified CCR7-Sialidase NanA complex with Cmp2105 in DDM/CHS buffer |
| Temperature | 20 C |
| Growth time | -- (not specified) |
| Cryoprotection | -- (not specified) |
| Notes | LCP crystallization in meso. Data collected at X06SA (PXI) beamline, Swiss Light Source. 5x5 um collimated beam. Data from 11 crystals merged. |


## Biological / Functional Insights

### Intracellular allosteric binding pocket in CCR7

Cmp2105 binds to an intracellular allosteric pocket located between TM1, TM2,
TM3, TM6, and the TM7-H8 turn. The thiadiazole-dioxide core motif positions
the sulfonamide group to interact with a conserved patch of residues at the
TM7-H8 turn (Tyr326, Gly330, Val331, Lys332, Phe333). This binding site
spatially overlaps with the Gi protein binding site, allowing Cmp2105 to
function as an intracellular allosteric antagonist.

### TM7-H8 turn as a pharmacological hotspot for chemokine receptors

The TM7-H8 turn is a conserved structural motif among CC and CXC chemokine
receptors. The Gly330 residue at the end of TM8 is conserved among most human
chemokine receptors and enables the tight interhelical joint that forms the
allosteric pocket. Multiple chemokine receptor ligands (CCR2-RA-[R] in CCR2,
Vercirnon in CCR9, Cmp2105 in CCR7) bind this motif, suggesting it is a
promising hotspot for multi-target drug design against chemokine receptors.

### Cross-reactivity of Navarixin at CCR7

Navarixin (SCH-527123 / MK-7123), a clinical phase II antagonist for CXCR1
and CXCR2, was identified as a CCR7 modulator by 3D shape similarity screening.
Its cyclobutene-dione core motif is almost identical to the thiadiazole-dioxide
of Cmp2105 in overall geometry. Navarixin suppresses arrestin recruitment in
response to CCL19 (IC50 33.9 uM) and stabilizes CCR7 (EC50 13.38 uM). This
finding suggests that part of Navarixin's anticancer effects may involve
silencing CCR7 in addition to CXCR1/CXCR2.

### Structural comparison with other chemokine receptors

CCR7 shares the canonical 7TM GPCR fold with Ca RMSD of 1.28-1.97 A to CCR2,
CCR5, CCR9, and CXCR4 at 29.9-39.1% sequence identity. Sequence and structural
differences between receptors are higher in the orthosteric chemokine binding
pocket (extracellular half) than in the intracellular side, which opens upon
activation. Cmp2105 stabilizes an inactive CCR7 conformation, confirmed by a
putative sodium ion in a conserved site between TM2, TM3, TM6, and TM7.

### Thermofluor-based drug discovery approach

An automated thermofluor (CPM thermal shift) screening methodology was used to
identify CCR7-binding compounds from a focused library of 293 compounds
selected by 3D shape similarity search from Roche's 2.3 million compound
repository. This approach detected both novel (CS-1, CS-2) and clinically
relevant (Navarixin) CCR7 modulators, demonstrating the utility of combining
structural data with thermal stability screening for GPCR drug discovery.


## Cross-References

- [CCR5 Chemokine Receptor](/xray-mp-wiki/proteins/gpcr/ccr5/) — Related human CC chemokine receptor for structural comparison
- [US28 Viral Chemokine Receptor](/xray-mp-wiki/proteins/gpcr/us28/) — Viral chemokine receptor for comparison of active/inactive conformations
- [Human Beta2-Adrenergic Receptor (beta2 AR)](/xray-mp-wiki/proteins/gpcr/beta2-adrenergic-receptor/) — Class A GPCR for comparison of intracellular allosteric binding
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used for CCR7 crystallization
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — MR method used with homology model of CCR7 and Sialidase NanA (PDB 2YA4)
- [Single-Wavelength Anomalous Diffraction (SAD)](/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/) — Native SAD used in combination with MR for structure determination
- [Molecular Docking](/xray-mp-wiki/methods/structure-determination/molecular-docking/) — Docking of CS-1 and Navarixin into CCR7 allosteric pocket using GOLD
- [Thermal Shift Assay](/xray-mp-wiki/methods/quality-assessment/thermal-shift-assay/) — CPM-based thermofluor assay used to validate ligand binding to CCR7
