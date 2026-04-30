---
title: 5-HT2B Serotonin Receptor
created: 2026-04-26
updated: 2026-04-30
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, receptor]
sources: [doi/10.1016##j.cell.2016.12.033]
---

# 5-HT2B Serotonin Receptor

## Overview

The human 5-HT2B receptor is a class A GPCR that mediates the effects of LSD and other hallucinogens. It is implicated in cardiac valvulopathy (FDA black box warning), appetite regulation, and has potential in psychedelic-assisted therapy research.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| Wacker et al. (Cell 2017) | 5TVN | 29.2–2.9 Å | C222₁ | 5-HT2B-ΔN/ΔICL3_BRIL/ΔC (ΔN1–35, ΔC406–481, M144W³·⁴¹, BRIL fusion in ICL3) | LSD |

- **Refinement**: R-work 22.5%, R-free 26.6%
- **Atoms**: 2,218 (5-HT2B R), 721 (BRIL), 24 (LSD), 60 (lipid/other)
- **Data collection**: APS GMCA/CAT 23ID-B/D, 10-μm microfocus beam

## Expression and Purification

- **Expression system**: Sf9 (insect, baculovirus)
- **Construct**: 5-HT2B-ΔN/ΔICL3_BRIL/ΔC
  - N-terminal residues 1–35 deleted
  - C-terminal residues 406–481 deleted
  - M144W³·⁴¹ thermostabilizing mutation
  - [bril](/xray-mp-wiki/reagents/protein-tags/bril/) (A1–L106 of thermostabilized apocytochrome b562RIL: M7W, H102I, R106L) replaces ICL3 residues Y249–S312
  - HA signal sequence at N-terminus, FLAG tag, PreScission protease site, 10× His tag at C-terminus

### Purification Workflow

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1. Cell lysis | Thawing | — | 10 mM [hepes-buffer](/xray-mp-wiki/reagents/buffers/hepes-buffer/) pH 7.5, 10 mM MgCl₂, 20 mM KCl, protease inhibitors (500 μM AEBSF, 1 μM E-64, 1 μM Leupeptin, 150 nM Aprotinin) | Frozen Sf9 cell pellets |
| 2. Membrane prep | Centrifugation | — | 1.0 M [sodium-chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10 mM HEPES pH 7.5, 10 mM MgCl₂, 20 mM KCl | Repeated centrifugation to remove soluble proteins |
| 3. LSD incubation | Mixing | — | 10 mM HEPES pH 7.5, 150 mM NaCl, 10 mM MgCl₂, 20 mM KCl, 50 μM LSD | Room temperature, 1 hr |
| 4. Alkylation | Iodoacetamide | — | Same as step 3 + 2 mg/ml iodoacetamide | 30 min |
| 5. Solubilization | Detergent | — | 10 mM HEPES pH 7.5, 150 mM NaCl, 1% [ddm](/xray-mp-wiki/reagents/detergents/ddm/) | — |
| 6. Affinity | His-tag IMAC | TALON IMAC resin (Clontech) | — | Elution with imidazole |
| 7. Dialysis | Dialysis | — | 20 mM HEPES pH 7.5, 150 mM NaCl, 0.02% DDM, 10 μM LSD | Overnight |
| 8. SEC | Size-exclusion | Superdex 200 increase 10/300 GL | 20 mM HEPES pH 7.5, 150 mM NaCl, 0.02% DDM, 10 μM LSD | — |

**Final sample**: 5-HT2B-ΔN/ΔICL3_BRIL/ΔC in 20 mM HEPES pH 7.5, 150 mM NaCl, 0.02% DDM, 10 μM LSD

## Crystallization

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | 5-HT2B-ΔN/ΔICL3_BRIL/ΔC + LSD in 20 mM HEPES pH 7.5, 150 mM NaCl, 0.02% DDM |
| Lipid | [monoolein](/xray-mp-wiki/methods/crystallization/monoolein/) (Sigma M7765) |
| Protein-to-lipid ratio | 1:2 (w/w) |
| Reservoir | 0.2 M magnesium chloride, 100 mM HEPES pH 7.0, 18–20% [peg-400](/xray-mp-wiki/reagents/additives/peg-400/) |
| Temperature | 20 °C |
| Growth time | 1–2 weeks |
| Cryoprotection | Mother liquor + additional PEG 400, flash-cooled in liquid nitrogen |

## Biological / Functional Insights

### LSD Binding Mode

- LSD shows **unexpected binding configuration** in the orthosteric site — shallow binding mode, closer to EL2 and extracellular space
- Ergoline moiety located higher in pocket compared to ergotamine (ERG), which binds deeper
- Indole nitrogen of LSD hydrogen bonds with G221⁵·⁴² (helix V) backbone oxygen, NOT with T140³·³⁷ in helix III (as ERG does)
- Basic nitrogen forms salt bridge with D135³·³²
- M218⁵·³⁹ side chain flips up to accommodate LSD (vs. pushed down by ERG's phenyl moiety)
- Binding pocket volume: 2,068.4 Å³ (28.6% smaller than ERG-bound at 2,898.7 Å³)
- Conformational changes in T114²·⁶⁴, E363⁷·³⁶, and M218⁵·³⁹ rotamer states between LSD- and ERG-bound structures

### EL2 Lid and LSD Residence Time

- EL2 residues 207–214 form a "lid" that covers the binding pocket entrance
- L209ᴱˡ² acts as a latch — extensive hydrophobic contacts with LSD and TMs III, IV, V
- Wild-type 5-HT2B: LSD residence time 46 min (k_off = 0.022 min⁻¹)
- L209Aᴱˡ² mutant: residence time drops to 4 min (k_off = 0.236 min⁻¹) — 10-fold faster dissociation
- L209Aᴱˡ² mutation selectively dampens β-arrestin2 recruitment, minimally affects Gq signaling
- MD simulations: lid occludes binding pocket most of the time, occasionally moves aside

### Diethylamide Stereoselectivity

- LSD's diethylamide moiety adopts a constrained conformation in binding site (~60° rotation vs. receptor-free crystal structure)
- (S,S)-Azetidide (SSAz) — matches LSD's crystallographic conformation, high potency
- (R,R)-Azetidide (RRAz) — different orientation, much reduced β-arrestin2 recruitment potency
- Supports hypothesis that specific diethylamide conformation is key to LSD's potency and activity

## Cross-References

- [a2a-adenosine-receptor](/xray-mp-wiki/proteins/a2a-adenosine-receptor/) — GPCR with BRIL fusion, similar thermostabilization strategy
- [etb-receptor](/xray-mp-wiki/proteins/etb-receptor/) — GPCR with BRIL fusion and LCP crystallization
- [kappa-opioid-receptor](/xray-mp-wiki/proteins/kappa-opioid-receptor/) — GPCR crystallized with nanobody
- [bril](/xray-mp-wiki/reagents/protein-tags/bril/) — Thermostabilized apocytochrome b562RIL fusion partner
- [monoolein](/xray-mp-wiki/methods/crystallization/monoolein/) — Lipid used in LCP crystallization
- [ddm](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent for solubilization and purification
- [sf9-cells](/xray-mp-wiki/methods/expression-systems/sf9-cells/) — Sf9 insect cell expression system
- [lipidic-cubic-phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP crystallization method