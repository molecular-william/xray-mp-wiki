---
title: "Phosphatidylinositol Phosphate Synthase PgsA1 from Mycobacterium tuberculosis"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s42003-019-0427-1]
verified: false
---

# Phosphatidylinositol Phosphate Synthase PgsA1 from Mycobacterium tuberculosis

## Overview

Mycobacterium tuberculosis [Phosphatidylinositol](/xray-mp-wiki/reagents/lipids/phosphatidylinositol/) phosphate synthase (PgsA1)
is an integral membrane enzyme that catalyzes the formation of
[Phosphatidylinositol](/xray-mp-wiki/reagents/lipids/phosphatidylinositol/) phosphate (PIP) from CDP-diacylglycerol (CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag/)) and
[D-myo-Inositol-3-Phosphate](/xray-mp-wiki/reagents/ligands/d-myo-inositol-3-phosphate/) (ino-P). It belongs to the Class I
CDP-alcohol phosphotransferase (CDP-AP) family, which catalyzes
phosphodiester bond formation between a CDP-alcohol and a second alcohol,
releasing CMP. PgsA1 is essential for mycobacterial growth and
proliferation, as PIP is a precursor of [Phosphatidylinositol](/xray-mp-wiki/reagents/lipids/phosphatidylinositol/), which in
turn is the first building block in the biosynthesis of
[Phosphatidylinositol](/xray-mp-wiki/reagents/lipids/phosphatidylinositol/) mannosides, lipomannan, and lipoarabinomannan —
structurally complex constituents of the mycobacterial cell wall. PgsA1
is a potential drug target for novel anti-tuberculosis therapies due to
differences between eukaryotic and mycobacterial PI biosynthesis pathways.
This paper presents three crystal structures (apo at 2.9 Å, Mn-[Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/)
complex at 1.9 Å, and CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag/) complex at 1.8 Å) revealing atomic details
of substrate binding, metal coordination dynamics, and a refined catalytic
mechanism involving a substrate-induced [Carboxylate Shift](/xray-mp-wiki/concepts/structural-mechanisms/carboxylate-shift/).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s42003-019-0427-1 | 6H53 | 2.90 | P 21 21 21 | Full-length M. tuberculosis PgsA1 (Rv2612c) with TEV-cleavable N-terminal His-tag, homodimer | None (apo structure) |
| doi/10.1038##s42003-019-0427-1 | 6H5A | 1.88 | P 21 21 21 | Full-length M. tuberculosis PgsA1 (Rv2612c) with TEV-cleavable N-terminal His-tag, homodimer | Mn2+, [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) (Mn-[Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) complex) |
| doi/10.1038##s42003-019-0427-1 | 6H59 | 1.80 | P 21 21 2 | Full-length M. tuberculosis PgsA1 (Rv2612c) with TEV-cleavable N-terminal His-tag, homodimer | CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag/), Mg2+, sulfate |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Full-length M. tuberculosis PgsA1 (Rv2612c; UniProt P9WPG7) with N-terminal His-tag and TEV-protease cleavage site

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and membrane preparation | E. coli expression, cell lysis, membrane isolation | -- | -- + -- | Details described in Methods section |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA or similar | -- + n-Octyl-β-D-glucopyranoside (OG) or similar | His-tagged PgsA1 purified by IMAC |
| TEV protease cleavage | His-tagged TEV protease digestion | -- | -- + -- | His-tag removed by TEV protease |
| Reverse [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Second IMAC step | Ni-NTA | -- + -- | Cleaved protein collected in flowthrough |


## Crystallization

### doi/10.1038##s42003-019-0427-1

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | Purified PgsA1 in detergent solution |
| Temperature | 100 K (data collection) |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | Apo crystals obtained in one condition; Mn-[Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) complex from 100 mM [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/), 120 mM Mn2+ in crystallization solution; CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag/) complex from co-crystallization with CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag/) and Mg2+ in LCP. Data collected at Diamond Light Source beamline I24. |


## Biological / Functional Insights

### Drug target for tuberculosis



### Tight and relaxed states of metal site



### Inositol phosphate binding site



### Ordered substrate binding mechanism




## Cross-References

- [Phosphatidylglycerol Phosphate Synthase PgsA from Staphylococcus aureus](/xray-mp-wiki/proteins/enzymes/sa-pgsa/) — Homologous CDP-AP family enzyme; structural and mechanistic comparison
- [CDP-Alcohol Phosphotransferase Family](/xray-mp-wiki/concepts/protein-families/cdp-alcohol-phosphotransferase-family/) — PgsA1 belongs to the Class I CDP-alcohol phosphotransferase family
- [Cytidine Diphosphate Diacylglycerol (CDP-DAG)](/xray-mp-wiki/reagents/lipids/cytidine-diphosphate-diacylglycerol/) — One of two substrates; CDP-DAG binding mechanism revealed in this study
- [Lipidic Cubic Phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method used for substrate-bound PgsA1 structures
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Phasing method used to solve all three structures
- [Carboxylate Shift](/xray-mp-wiki/concepts/structural-mechanisms/carboxylate-shift/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Molecular Docking](/xray-mp-wiki/methods/structure-determination/molecular-docking/) — Method used in structure determination or purification
- [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) — Buffer component in purification or crystallization
- [D-myo-Inositol-3-Phosphate](/xray-mp-wiki/reagents/ligands/d-myo-inositol-3-phosphate/) — Related ligand or cofactor
