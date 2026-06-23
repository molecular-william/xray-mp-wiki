---
title: "ABCG2"
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2022.167795]
verified: false
---

# ABCG2

## Overview

ABCG2 (breast cancer resistance protein, BCRP) is the sole multidrug transporter (MDR) of the ABCG subfamily. Unlike other ABCG members that function as lipid floppases, ABCG2 exports a broad spectrum of structurally diverse substrates including drugs, toxins, and endogenous compounds. ABCG2 functions as a homodimer and shares the characteristic ABCG structural fold including the hydrophobic valve (di-leucine valve/gate) and phenylalanine highway (PH) motif. The di-leucine valve at the TMD interface and the PH on TMH2 form a conserved structural framework shared among ABCG transporters. ABCG2 has been implicated in cancer multidrug resistance, porphyria cutanea tarda, and inflammatory bowel disease.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2022.167795 | 6VXI | not specified | not specified | Human ABCG2 homodimer | None |
| doi/10.1016##j.jmb.2022.167795 | 6VXF | not specified | not specified | Human ABCG2 homodimer | None |
| doi/10.1016##j.jmb.2022.167795 | 6VXJ | not specified | not specified | Human ABCG2 homodimer | None |
| doi/10.1016##j.jmb.2022.167795 | 6FFC | not specified | not specified | Human ABCG2 homodimer | Not specified |
| doi/10.1016##j.jmb.2022.167795 | 6VXH | not specified | not specified | Human ABCG2 homodimer | Not specified |
| doi/10.1016##j.jmb.2022.167795 | 6HBU | not specified | not specified | Human ABCG2 E211Q mutant ([ATP](/xray-mp-wiki/reagents/ligands/atp)-bound) | [ATP](/xray-mp-wiki/reagents/ligands/atp) |

## Expression and Purification

- **Expression system**: Not specified
- **Construct**: Human ABCG2 homodimer; AlphaFold2 predictions and PDB structures used for modeling

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Not specified | Not specified | -- | Not specified + Not specified | ABCG2 structures from PDB used for molecular docking analysis; purification details not reported in this paper |


## Crystallization

No crystallization described.

## Biological / Functional Insights

### Hydrophobic valve and phenylalanine highway in ABCG2

ABCG2 contains a di-leucine valve/gate at the TMD interface, distinct from the hydrophobic valve found in ABCG1/ABCG4/ABCG5/G8. The phenylalanine highway on TMH2 includes F439 (F1 position), which is critical for substrate binding. The F439A mutation downregulates drug efflux, while F439Y and F439W substitutions do not hamper efflux function, emphasizing the importance of aromatic residues in contributing to a substrate-binding route from the inner leaflet of the membranes.

### Drug substrate binding

ABCG2 transports a broad spectrum of structurally diverse substrates including topotecan, [Mitoxantrone](/xray-mp-wiki/reagents/additives/mitoxantrone), and imatinib. Molecular docking validation was performed by redocking these drugs to reproduce their complexes with ABCG2 structures (PDB 6FFC, 6VXH, 6VXJ). The F431 (PH's F1) in ABCG2 has been shown to engage in drug-protein interactions with ABCG2 inhibitors, highlighting the role of the PH in drug binding.

### Comparison with ABCG sterol transporters

ABCG2 differs from ABCG1, ABCG4, ABCG5, and [ABCG8](/xray-mp-wiki/proteins/abcg8) in its substrate specificity, functioning as a multidrug transporter rather than a lipid floppase. The substrate specificity among ABCG transporters may result from differences in hydrophobic valve composition between ABCG2 and the lipid transporters. ABCG2's relaxed approach to substrate efflux contrasts with the selective sterol transport of ABCG5/G8.


## Cross-References

- [ABCG5](/xray-mp-wiki/proteins/abcg5) — ABCG5/G8 heterodimer; PH motif and hydrophobic valve comparison
- [ABCG1](/xray-mp-wiki/proteins/abcg1) — ABCG sterol transporter; hydrophobic valve composition comparison
- [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) — Endogenous ligand that modulates ABCG2 function
- [Imatinib](/xray-mp-wiki/reagents/additives/imatinib) — ABCG2 drug substrate used in docking validation
- [Topotecan](/xray-mp-wiki/reagents/additives/topotecan) — ABCG2 drug substrate used in docking validation
- [Mitoxantrone](/xray-mp-wiki/reagents/additives/mitoxantrone) — ABCG2 drug substrate used in docking validation
- [Stigmasterol](/xray-mp-wiki/reagents/lipids/stigmasterol) — Plant sterol; docked on ABCG sterol transporters for selectivity comparison
- [Abcg8](/xray-mp-wiki/proteins/abcg8) — Related membrane protein structure
- [Atp](/xray-mp-wiki/reagents/ligands/atp) — Ligand used in structure determination
