---

title: BRIL (Apocytochrome b562RIL)
created: 2026-04-27
updated: 2026-04-27
type: reagent
tags: [additive-stabilizer, sample-preparation]
sources: [doi/10.1016##j.cell.2015.04.011, doi/10.1016##j.cell.2018.12.006]

category: reagents
---
layout: default


# BRIL (Apocytochrome b562RIL)

## Overview

BRIL is a thermostabilized mutant of apocytochrome b562 from *Escherichia coli* (M7W, H102I, R106L mutations). It has been developed as a fusion partner toolchest for the stabilization and crystallization of G protein-coupled receptors (GPCRs).

## Thermostabilization

BRIL contains three point mutations relative to wild-type apocytochrome b562:
- **M7W**: Methionine → Tryptophan at position 7
- **H102I**: Histidine → Isoleucine at position 102
- **R106L**: Arginine → Leucine at position 106

These mutations increase thermal stability and solubility, making BRIL an ideal fusion partner for membrane protein crystallization.

## GPCR Fusion Strategy

BRIL can be fused to either the N-terminus or intracellular loops of GPCRs:

### N-terminal Fusion
- Used for AT1R (Angiotensin II type 1 receptor): BRIL fused to N-terminus
- Construct: HA signal peptide + FLAG tag + 10× His tag + TEV site + BRIL + AT1R
- Truncations: AT1R residues 1, 7–16, 320–359 deleted

### Intracellular Loop 3 (ICL3) Fusion
- Used for AT1R (active-state): BRIL inserted into ICL3 (residues 226–227)
- Construct: I320 truncated to stop; BRIL in ICL3 instead of N-terminus
- **Result**: 2-fold higher AngII affinity than wild-type; retained nanobody binding

## Known GPCR-BRIL Fusions

| GPCR | Fusion Site | Reference |
|------|------------|-----------|
| AT1R | N-terminus | Zhang et al., Cell 2015 (PDB: 4YAY) |
| AT1R | ICL3 (226–227) | Wingler et al., Cell 2019 (PDB: 6DO1) |
| β₂-adrenergic receptor | ICL3 | Cherezov et al., Science 2007 |
| A₂A adenosine receptor | ICL3 | Cao et al., Science 2007 |
| 5-HT₁B receptor | N-terminus | Wu et al., Science 2012 |
| 5-HT₁AR | ICL3 | Wang et al., Nature 2013 |
| Adenosine A₁ receptor | ICL3 | Liu et al., Science 2012 |

## Comparison with T4 Lysozyme

| Feature | BRIL | T4 Lysozyme |
|---------|------|-------------|
| Size | ~12 kDa (110 aa) | ~18.5 kDa (164 aa) |
| Fusion sites | N-terminus or ICL3 | ICL3 only |
| Crystal contacts | Yes | Yes |
| GPCR compatibility | Broader (N-term + ICL3) | ICL3 only |
| First used | 2012 (Chun et al.) | 2007 (Cherezov et al.) |

## Related Stabilization Strategies

- [t4-lysozyme](//xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) — T4 lysozyme fusion in ICL3 for GPCR crystallization
- [nanobody](//xray-mp-wiki/reagents/antibodies/nanobody/) — Active-state nanobody for GPCR stabilization
- [cholesterol-hydrogen-succinate](//xray-mp-wiki/reagents/lipids/cholesterol-hydrogen-succinate/) — CHS for membrane protein stabilization
- [lmng](//xray-mp-wiki/reagents/detergents/lmng/) — Mild detergent for GPCR stabilization

## References

- Chun et al. (2012) Structure 20:967–976 — BRIL fusion toolchest