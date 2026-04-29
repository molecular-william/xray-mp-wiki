---

title: 5-HT2B Receptor (Serotonin Receptor 2B)
created: 2026-04-26
updated: 2026-04-27
type: protein
tags: [gpcr, membrane-protein, receptor]
sources: [doi/10.1016##j.cell.2016.12.033]

category: proteins
---
layout: default


# 5-HT2B Receptor

## Overview

The 5-HT2B receptor is a serotonin GPCR that mediates the effects of LSD and other hallucinogens. It is implicated in cardiac valvulopathy (FDA black box warning), appetite regulation, and has potential in psychedelic-assisted therapy research.

## Structure Determination

- **PDB ID**: 5TVN
- **Resolution**: 2.9 Å (29.2–2.9 Å range)
- **Method**: [xray-crystallography](//xray-mp-wiki/methods/structure-determination/xray-crystallography/), [lipidic-cubic-phase](//xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) (LCP)
- **Construct**: 5-HT2B-ΔN/ΔICL3_BRIL/ΔC (N-terminal truncation, [bril](//xray-mp-wiki/reagents/protein-tags/bril/) fusion in ICL3, C-terminal truncation)
- **Ligand**: LSD (lysergic acid diethylamide)
- **Space group**: C222₁
- **Data collection**: APS GMCA/CAT 23ID-B/D, 10-μm microfocus beam
- **Total reflections**: 46,859; Unique reflections: 12,568
- **R-work/R-free**: 22.5%/26.6%

## Expression and Purification

- **Expression system**: [hek293-cells](//xray-mp-wiki/methods/expression-systems/hek293-cells/) (mammalian, transient transfection)
- **Construct design**:
  - N-terminal truncation (ΔN)
  - [bril](//xray-mp-wiki/reagents/protein-tags/bril/) (thermostabilized apocytochrome b562RIL) fused into ICL3
  - C-terminal truncation (ΔC)
- **Detergent**: [mng-detergent](//xray-mp-wiki/reagents/detergents/mng-detergent/) for solubilization and purification
- **Purification**: [affinity-chromatography](//xray-mp-wiki/methods/purification/affinity-chromatography/) (His-tag on [bril](//xray-mp-wiki/reagents/protein-tags/bril/)), followed by [size-exclusion-chromatography](//xray-mp-wiki/methods/purification/size-exclusion-chromatography/)

## Crystallization

- **Method**: [lipidic-cubic-phase](//xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — [monoolein](//xray-mp-wiki/methods/crystallization/monoolein/)-based mesophase
- **Lipid**: [monoolein](//xray-mp-wiki/methods/crystallization/monoolein/) (Sigma M8410)
- **Protein-to-lipid ratio**: 1:2 (w/w)
- **Precipitant**: 0.2 M MgCl₂, 0.1 M [hepes-buffer](//xray-mp-wiki/reagents/buffers/hepes-buffer/) pH 7.0, 20–24% [peg-400](//xray-mp-wiki/reagents/additives/peg-400/)
- **Temperature**: 20 °C
- **Crystal growth**: 1–2 weeks

## LSD Binding Mode

- LSD shows **unexpected binding configuration** in the orthosteric site
- Conformational rearrangements accommodate the diethylamide moiety
- Extracellular loop 2 (EL2) forms a "lid" at the entrance to the binding pocket
- LSD dissociates exceptionally slowly from both 5-HT2B and 5-HT2A receptors
- Molecular dynamics suggest the EL2 lid restricts LSD binding/unbinding kinetics
- Mutation predicted to increase lid mobility accelerates LSD kinetics and selectively dampens β-arrestin2 recruitment

## Pharmacological Significance

- LSD has a complex pharmacology affecting essentially all aminergic GPCRs
- Long-lasting effects (6–15 hours) correlate with slow dissociation kinetics
- Potential applications in substance abuse, cluster headaches, and anxiety disorders
- Therapeutic potential under renewed scientific interest

|## Related Serotonin Receptors
|
|- [a2a-adenosine-receptor](//xray-mp-wiki/proteins/a2a-adenosine-receptor/) — GPCR with extensive structural biology
|- [opsin-gpcr](//xray-mp-wiki/proteins/opsin-gpcr/) — Class A GPCR structural template
|- [etb-receptor](//xray-mp-wiki/proteins/etb-receptor/) — Endothelin GPCR with [bril](//xray-mp-wiki/reagents/protein-tags/bril/) fusion
|- [kappa-opioid-receptor](//xray-mp-wiki/proteins/kappa-opioid-receptor/) — Opioid GPCR with nanobody
