---

title: A2A Adenosine Receptor
created: 2026-04-26
updated: 2026-04-27
type: protein
tags: [gpcr, membrane-protein, receptor]
sources: [doi/10.1002##anie.202115545, doi/10.1016##j.bbrc.2023.149393]

category: proteins
---
layout: default


# A2A Adenosine Receptor (A2AAR)

## Overview

The human A2A adenosine receptor is a class A GPCR that couples to Gs proteins and plays a pivotal role in immunological processes and neurodegenerative diseases. It is an important drug target in immuno-oncology and Parkinson's disease research.

## Structure Determination

- **Construct**: A2A-PSB1-bRIL (single S91³·³⁹K mutation, bRIL fusion in ICL3)
- **PDB IDs**: 7PX4 (PSB-2113 complex), 7PYR (PSB-2115 complex)
- **Resolutions**: 2.25 Å and 2.6 Å
- **Method**: [xray-crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/), sitting-drop [vapor-diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion/)
- **Stability**: Single point mutation (S91³·³⁹K) provides superior thermostability compared to 9-mutation A2A-StaR2

## Expression and Purification

- **Expression system**: [hek293-cells](/xray-mp-wiki/methods/expression-systems/hek293-cells/) (mammalian, stable expression)
- **Construct design**:
  - Single S91³·³⁹K mutation — lysine occupies the allosteric sodium binding site
  - bRIL (thermostabilized [bril](/xray-mp-wiki/reagents/protein-tags/bril/)) fused into ICL3
  - C-terminal truncation (long C-tail removed)
- **Detergent**: [ddm](/xray-mp-wiki/reagents/detergents/ddm/) (n-dodecyl-β-D-maltopyranoside) for membrane solubilization
- **Purification**: [affinity-chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) (His-tag on bRIL), followed by [size-exclusion-chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) (Superdex 200 increase 10/300)
- **SEC buffer**: 20 mM [hepes-buffer](/xray-mp-wiki/reagents/buffers/hepes-buffer/) pH 7.5, 150 mM [sodium-chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 0.05% [ddm](/xray-mp-wiki/reagents/detergents/ddm/), 1 μM ligand (PSB-2113 or PSB-2115)

## Crystallization

- **Method**: Sitting-drop [vapor-diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion/)
- **Reservoir**: 0.1 M sodium acetate pH 4.5, 18–20% [peg-400](/xray-mp-wiki/reagents/additives/peg-400/)
- **Drop composition**: 1 μL protein + 1 μL reservoir
- **Temperature**: 20 °C
- **Crystal growth**: 1–2 weeks
- **Space group**: P2₁2₁2₁

## Ligands Co-crystallized

- **PSB-2113**: PEGylated Preladenant [photoNECA](/xray-mp-wiki/reagents/ligands/photoNECA/) derivative
- **PSB-2115**: BODIPY-fluorophore-labeled Preladenant [photoNECA](/xray-mp-wiki/reagents/ligands/photoNECA/) derivative
- **Preladenant [photoNECA](/xray-mp-wiki/reagents/ligands/photoNECA/) (SCH-420814)**: Potent A2AAR antagonist (Ki < 1 nM), highly selective (>300-fold vs A2B)
- **MSX-2**: Standard xanthine antagonist (reference)
- **ZM241385**: Bicyclic A2AAR antagonist (reference, from PDB 4EIY)
- **[neca](/xray-mp-wiki/reagents/ligands/neca/)**: Adenosine agonist (binding abolished by S91K mutation)

## Key Construct Features

- **bRIL**: Thermostabilized apocytochrome b562RIL fusion protein replacing ICL3
- **S91³·³⁹K mutation**: Lysine occupies the allosteric sodium binding site, stabilizing inactive conformation
- **C-terminal truncation**: Long C-tail removed
- **No mutations in orthosteric ligand-binding pocket** (unlike A2A-StaR2 which has T88³·³⁶A and S277⁷·⁴²A)

## Binding Pocket Features

- PSB-2113 binds in the same orientation as ZM241385
- Key interactions: H-bond to N253⁶·⁵⁵ and E169ᴱᶜˡ² via furan oxygen and 5-amino group
- π-π stacking to F168ᴱᶜˡ²
- Hydrophobic contacts to L249⁶·⁵¹ and I274⁷·³⁹
- Displacement of "unhappy waters" from binding pocket contributes to high affinity
- Tricyclic core extends further toward helix II, displacing a structural water molecule

## Additional Constructs

- **A2A-StaR2**: Thermostabilized mutant expressed in [sf9-cells](/xray-mp-wiki/methods/expression-systems/sf9-cells/) with [fab-fragments](/xray-mp-wiki/reagents/antibodies/fab-fragments/) (Fab 35.1)
  - Used for agonist-bound structures (NECA complex, PDB 8WDT)
  - Crystallized with [fab-fragments](/xray-mp-wiki/reagents/antibodies/fab-fragments/) antibody fragment for conformational stabilization
  - [lipidic-cubic-phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) crystallization in dark/red light to prevent photoisomerization
- **A2AAR-Rag31-photoNECA**: Araya et al. (2024) — A2AAR-Rag31 with trans-photoNECA at 3.34 Å (PDB 8WDT)
  - Thermostabilized Rag31 mutant
  - SF9 insect cells, [baculovirus-expression](/xray-mp-wiki/methods/expression-systems/baculovirus-expression/)
  - LCP crystallization with trans-photoNECA in dark/red light
  - Fab fragment facilitator
  - PhotoNECA binding mode: NECA moiety in orthosteric site, photoswitching moiety in hydrophobic pocket (Ser67²·⁶⁵, Leu167ᴱᶜˡ², Leu267⁷·³², Tyr271⁷·³⁶)
  - Explains subtype selectivity: hydrophobic pocket in A2AAR vs. polar pocket in A1R
  - Data collection: BL32XU (391 datasets)

## Related Constructs

- [a2a-star2](/xray-mp-wiki/proteins/a2a-star2/) — 9-mutation thermostabilized construct (historical)
- [etb-receptor](/xray-mp-wiki/proteins/etb-receptor/) — ETB-Y5-T4L: 5 thermostabilizing mutations (R124Y, D154A, K270A, DS342A, I381A) + T4L fusion in ICL3
- A2A-PSB1-bRIL: Single S91K mutation, bRIL fusion (current gold standard)
- A2A-ΔC-bRIL: C-terminal truncation + bRIL fusion (no point mutations)

## Key Reagents Summary

|| Category | Reagent | Purpose |
|----------|---------|---------|
| Ligand | PSB-2113 | PEGylated Preladenant [photoNECA](/xray-mp-wiki/reagents/ligands/photoNECA/), co-crystallization |
| Ligand | PSB-2115 | BODIPY-labeled Preladenant [photoNECA](/xray-mp-wiki/reagents/ligands/photoNECA/), co-crystallization |
| Ligand | Preladenant [photoNECA](/xray-mp-wiki/reagents/ligands/photoNECA/) (SCH-420814) | Potent antagonist scaffold |
| Ligand | ZM241385 | Reference antagonist (bicyclic) |
| Ligand | MSX-2 | Reference xanthine antagonist |
| Ligand | [neca](/xray-mp-wiki/reagents/ligands/neca/) | Adenosine agonist (binding assay) |
| Fusion protein | [bril](/xray-mp-wiki/reagents/protein-tags/bril/) | ICL3 replacement for crystallization |
| Mutation | S91³·³⁹K | Allosteric stabilization |
| Detergent | [ddm](/xray-mp-wiki/reagents/detergents/ddm/) | Membrane solubilization |
| Precipitant | [peg-400](/xray-mp-wiki/reagents/additives/peg-400/) | Crystallization precipitant |

## Cross-References

- [a2a-star2](/xray-mp-wiki/proteins/a2a-star2/) — Thermostabilized precursor construct
- [etb-receptor](/xray-mp-wiki/proteins/etb-receptor/) — GPCR with [bril](/xray-mp-wiki/reagents/protein-tags/bril/) fusion and thermostabilization
- [p2y12-receptor](/xray-mp-wiki/proteins/p2y12-receptor/) — GPCR with BRIL fusion and LCP crystallization
- [5ht2b-receptor](/xray-mp-wiki/proteins/5ht2b-receptor/) — Serotonin GPCR with BRIL fusion and LCP
- [opsin-gpcr](/xray-mp-wiki/proteins/opsin-gpcr/) — Class A GPCR structural template
