---
title: DAP12
created: 2026-04-28
updated: 2026-04-28
type: protein
tags: [membrane-protein, immunoreceptor, signaling]
sources: [doi/10.1016##j.celrep.2015.04.045]
---
layout: default

# DAP12 (DNAX-Activating Protein 12 kDa)

## Overview

DAP12 is a 12 kDa immunoreceptor signaling module that associates with various activating receptors on immune cells (NK cells, macrophages, dendritic cells). It has no structured ectodomain and forms both homo- and hetero-oligomeric interfaces through its transmembrane (TM) domain. DAP12 contains two extracellular cysteines that form disulfide-linked dimers, and its TM domain mediates assembly with client receptors via a polar aspartic acid/threonine motif.

## Structure

### Knoblich et al. (Cell Reports 2015) — DAP12-TM Trimer

- **Resolution**: 1.77 Å
- **PDB ID**: 4WOL
- **Construct**: DAP12-TM peptide (residues 2–34 of mature protein): CSTVSPGVLAGIVVGDLVLTVLIALAVYFLGRL
- **Assembly**: Right-handed trimeric coiled coil, 3 parallel α helices
- **Space group**: Not explicitly stated (LCP crystallization)
- **Key feature**: Polar core of Asp23/Thr27 from all 3 chains with coordinated K+ ion
- **Monoolein**: 4 well-ordered lipid molecules in electron density

### Knoblich et al. (Cell Reports 2015) — DAP12-TM Tetramer

- **Resolution**: 2.14 Å
- **PDB ID**: 4WO1
- **Assembly**: 4 parallel α helices
- **Key feature**: Polar core of Asp23/Thr27 from all 4 chains with coordinated Ca2+ ions (2 overlapping sites, pentagonal bipyramidal geometry)
- **Monoolein**: Structured lipid molecules in electron density

## Transmembrane Domain Sequence

Human DAP12 TM peptide (33 aa, crystallized construct):
```
CSTVSPGVLAGIVVGDLVLTVLIALAVYFLGRL
         ^^^^^^^^^^^^ ^^^^^^^^
         Gly zipper   Asp/Thr motifs
```

- **Glycine zipper**: GxxxGxxxG motif (helical periodicity) on exterior surface
- **Polar core**: Asp23 and Thr27 residues oriented toward trimer/tetramer center
- **Disulfide**: N-terminal cysteine forms disulfide-linked dimer before crystallization

## Ion Coordination

### Trimer (4WOL) — Potassium Ion

- **Coordinated by**: Asp23 (bidentate from chain A, monodentate from B and C) + Thr27 (monodentate from all 3 chains)
- **Distances**: 2.7–3.1 Å from K+ center
- **Charge state**: Most stable with 1 ionized Asp (1 Asp⁻), as predicted by MD simulations
- **Source**: Potassium thiocyanate in precipitant solution

### Tetramer (4WO1) — Calcium Ions

- **Coordination**: 2 overlapping Ca2+ sites with pentagonal bipyramidal geometry
- **Occupancy**: 50% each
- **Additional**: Network of water molecules in coordination sphere
- **Source**: Calcium chloride in precipitant solution

## Expression and Purification

### Knoblich et al. (Cell Reports 2015)

- **Expression**: E. coli, trpLE fusion protein
- **Disulfide formation**: Disulfide-linked through N-terminal cysteine
- **Cleavage**: Cyanogen bromide (CB) digestion to release TM peptide
- **Purification**: HPLC (high-performance liquid chromatography)
- **Verification**: HPLC, mass spectrometry, SDS-PAGE confirmed pure disulfide-linked dimer
- **Storage**: Lyophilized product

## Crystallization

### Knoblich et al. (Cell Reports 2015)

- **Method**: [lipidic-cubic-phase](/methods/crystallization/lipidic-cubic-phase/) (LCP) in monoolein
- **Reconstitution**: Co-dissolution in hexafluoroisopropanol (HFIP), solvent removal under vacuum, mixing with monoolein
- **SAXS**: Confirmed gyroid cubic, diamond cubic, and fluid lamellar phases

#### Trimer Crystal Conditions
- 10% cholesterol, 12.4% (w/v) PEG 3350, 0.149 M potassium thiocyanate
- Small oval discs after 5–7 days

#### Tetramer Crystal Conditions
- 0.1 M bis-tris propane chloride (pH 6.07), 19.7% (w/v) PEG 3350, 0.269 M calcium chloride
- Star-like clusters after 1–3 days

- **Phasing**: Molecular replacement with Phaser using Glycophorin A (PDB: 1AFO) as search model
- **Tetramer solution**: Chain A from DAP12 trimer used as MR model

## Biological Role

- **Assembly**: Forms disulfide-linked homodimers; higher-order oligomers (trimers, tetramers) also form in ER
- **Receptor assembly**: Hetero-oligomerizes with client receptors (e.g., KIR2DS2, NKG2D) via TM domain interactions
- **Central TM lysine**: Key feature of DAP12-associated receptors
- **Competition**: DAP12 homotrimers compete with DAP12-receptor heterotrimer assembly in ER
- **Glycophorin A**: Reference TM dimer structure (PDB: 1AFO) used for molecular replacement

## Cross-References

- [monoolein](/methods/crystallization/monoolein/) — Lipid matrix for LCP crystallization
- [lipidic-cubic-phase](/methods/crystallization/lipidic-cubic-phase/) — LCP crystallization method
- [molecular-replacement](/methods/structure-determination/molecular-replacement/) — Phaser MR (PDB: 1AFO, Glycophorin A)
- [sodium-chloride](/reagents/additives/sodium-chloride/) — Common buffer salt
- [peg-3350](/reagents/additives/peg-3350/) — PEG 3350 crystallization precipitant (used in both crystal forms)
- [cholesterol-lipid](/reagents/lipids/cholesterol-lipid/) — Cholesterol in trimer crystallization
- [[glycophorin-a]] — Glycophorin A (PDB: 1AFO, reference TM dimer)