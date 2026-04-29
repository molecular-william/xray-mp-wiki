---

title: T4 Lysozyme
created: 2026-04-27
updated: 2026-04-27
type: reagent
tags: [additive-stabilizer, sample-preparation]
sources: [doi/10.1016##j.bbrc.2019.12.091]

category: reagents
---
layout: default


# T4 Lysozyme

## Overview

T4 lysozyme (T4L) is a 164-amino-acid enzyme from bacteriophage T4 that cleaves bacterial cell wall peptidoglycan. In structural biology, T4L has been extensively used as a fusion partner to facilitate crystallization of membrane proteins, particularly GPCRs.

## GPCR Crystallization Strategy

The T4L fusion strategy was pioneered by Brian Kobilka for the β₂-adrenergic receptor and has since been applied to numerous GPCRs:
- **Target site**: Intracellular loop 3 (ICL3), which is often flexible and disordered
- **Insertion**: T4L is inserted between specific residues in ICL3 (commonly between positions corresponding to 5.68 and 6.23 in Ballesteros-Weinstein numbering)
- **Rationale**: T4L provides a large, stable, well-folded domain that participates in crystal contacts, replacing the flexible ICL3

## Known T4L Fusion Sites in GPCRs

| GPCR | T4L Insertion Site | Reference |
|------|-------------------|-----------|
| β₂-adrenergic receptor | ICL3 (N127-E165) | Cherezov et al., Science 2007 |
| A₂A adenosine receptor | ICL3 (N162-R204) | Cao et al., Science 2007 |
| Adenosine A₁ receptor | ICL3 | Liu et al., Science 2012 |
| Dopamine D₃ receptor | ICL3 | Wu et al., Science 2012 |
| Endothelin ETB receptor | ICL3 (L303-L311) | Izume et al., BBRC 2020 |
| Neurotensin receptor 1 | ICL3 | Wang et al., Nature 2015 |

## ETB Receptor Fusion (ETB-Y5-T4L)

- **Insertion**: Between L303⁵·⁶⁸ and L311⁶·²³
- **Additional thermostabilizing mutations**: R124Y¹·⁵⁵, D154A²·⁵⁷, K270A⁵·³⁵, DS342A⁶·⁵⁴, I381A⁷·⁴⁸
- **Effect on structure**: T4L insertion affects conformations of TM5 and TM6, which must be considered when interpreting conformational states
- **C-terminal tag**: GFP-His₁₀ tag for purification (removed by TEV protease)

## Limitations

- T4L insertion may perturb native ICL3-mediated G-protein interactions
- Conformational changes induced by T4L (e.g., TM5 displacement) must be distinguished from ligand-induced changes
- Not all GPCRs tolerate T4L insertion; alternative strategies include nanobodies (Nb39, Nb80) or thermostabilizing mutations alone

## Related Stabilization Strategies

- **Nanobodies**: Active-state nanobodies (Nb39, NbAT110i1) bind intracellular side of GPCRs
- **BRIL fusion**: Apocytochrome b₅₆₂RIL (BRIL) replaces ICL3 in some GPCRs
- **Thermostabilizing mutations**: Point mutations that increase thermal stability without fusion proteins
- **Conformational restriction**: Disulfide bonds, small molecule stabilizers

## Related Reagents

- [nanobody](/reagents/antibodies/nanobody.html) — Synthetic active-state AT1R nanobody
- [cholesterol-hydrogen-succinate](/reagents/lipids/cholesterol-hydrogen-succinate.html) — CHS for membrane protein stabilization
- [lmng](/reagents/detergents/lmng.html) — Mild detergent for GPCR stabilization