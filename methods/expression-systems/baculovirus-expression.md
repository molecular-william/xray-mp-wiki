---


title: Baculovirus Expression
created: 2026-04-27
updated: 2026-04-27
type: method
tags: [expression-system]
sources: [doi/10.1016##j.bbrc.2019.12.091]


category: methods
---
layout: default



# Baculovirus Expression System

## Overview

The [baculovirus-expression](//xray-mp-wiki/methods/expression-systems/baculovirus-expression/) vector system (BEVS) uses recombinant baculoviruses to express proteins in insect cells. It combines the high expression capacity of viral infection with the eukaryotic protein processing machinery of insect cells.

## Bac-to-Bac System

The Bac-to-Bac system (Invitrogen/Thermo Fisher) streamlines recombinant baculovirus generation:
1. **Transfer plasmid**: Contains gene of interest with baculovirus polyhedrin promoter and flanking IS1 elements
2. **E. coli transformation**: With bacmid (large plasmid containing baculovirus genome)
3. **Transposon-mediated transposition**: Gene of interest transfers from transfer plasmid to bacmid
4. **Bacmid purification**: From positive E. coli colonies
5. **Sf9 cell transfection**: Bacmid DNA transfected into Sf9 cells produces recombinant baculovirus
6. **Virus amplification**: P0 virus amplifies to P1, P2, P3 generations
7. **Protein expression**: Sf9 cells infected with P3 virus at optimal density

## Protocol for GPCR Expression

1. **Sf9 cell culture**: 4.0 × 10⁶ cells/mL in SF900 II medium
2. **Virus infection**: At optimal cell density
3. **Incubation**: 48 hours at 27°C
4. **Harvest**: Centrifugation, cell pellet flash-frozen
5. **Membrane preparation**: Cell lysis (sonication), ultracentrifugation at 180,000g for 1 hr
6. **Solubilization**: Detergent extraction from crude membranes

## Advantages for GPCR Crystallization

- **Eukaryotic folding**: Proper disulfide bond formation, membrane protein folding
- **Post-translational modifications**: Mammalian-like glycosylation, palmitoylation
- **High expression**: Typically 10–100× higher than mammalian expression
- **Scalability**: Can produce liters of infected cell culture
- **Flexibility**: Easy to co-express multiple subunits or fusion partners

## Disadvantages

- **Glycosylation**: Insect cells add high-mannose glycans (not fully mammalian)
- **Palmitoylation**: May differ from mammalian patterns
- **Time**: 2–3 weeks from gene to protein
- **Cost**: More expensive than bacterial expression

## Related Systems

- [pichia-pastoris](//xray-mp-wiki/methods/expression-systems/pichia-pastoris/) — Yeast expression system
- [hek293-cells](//xray-mp-wiki/methods/expression-systems/hek293-cells/) — Mammalian expression system
- [sf9-cells](//xray-mp-wiki/methods/expression-systems/sf9-cells/) — Sf9 insect cell line