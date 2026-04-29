---


title: Sf9 Insect Cells
created: 2026-04-27
updated: 2026-04-27
type: reagent
tags: [membrane-protein, sample-preparation]
sources: [doi/10.1016##j.bbrc.2019.12.091]


---
layout: default



# Sf9 Insect Cells

## Overview

Sf9 cells are a line of insect cells derived from *Spodoptera frugiperda* (fall armyworm) ovary tissue. They are widely used for recombinant protein expression using [[baculovirus-expression]] expression vectors, particularly for membrane proteins and GPCRs that require post-translational modifications (glycosylation, palmitoylation) not provided by bacterial systems.

## Baculovirus Expression System

The Bac-to-Bac system (Invitrogen/Thermo Fisher) enables rapid generation of recombinant baculovirus:
1. **Transfer vector**: Contains gene of interest flanked by baculovirus insertion sequences
2. **Transformation**: Into *E. coli* with bacmid containing viral genome
3. **Transposition**: Gene of interest transfers to bacmid via transposon
4. **Bacmid transfection**: Into Sf9 cells produces recombinant baculovirus
5. **Amplification**: Virus amplified through multiple passages
6. **Protein expression**: Sf9 cells infected with high-titer virus

## Advantages for Membrane Protein Expression

- **Eukaryotic post-translational modifications**: Proper folding, disulfide bond formation, glycosylation
- **Higher expression levels** than mammalian cells for many targets
- **Scalability**: Large volume cultures feasible
- **Reduced toxicity**: Baculovirus infection is less cytotoxic than viral infections in mammalian cells

## Use in ETB Receptor Expression

- **Cell line**: Sf9 insect cells
- **Medium**: SF900 II medium
- **Infection density**: 4.0 × 10⁶ cells/mL
- **Growth**: 48 hours at 27°C post-infection
- **Harvest**: Cells disrupted by sonication
- **Membrane preparation**: Ultra[[centrifugation]] at 180,000g for 1 hr

## Comparison with Other Expression Systems

| System | Expression Level | PTMs | Typical Use |
|--------|-----------------|------|-------------|
| *E. coli* | Very high | None (no disulfides in cytoplasm) | Soluble proteins, inclusion bodies |
| *Pichia pastoris* | High | Glycosylation (hypermannosylated) | GPCRs, transporters |
| Sf9 insect cells | Moderate-High | Mammalian-like glycosylation | GPCRs, large complexes |
| HEK293 mammalian | Low-Moderate | Full mammalian PTMs | Functional assays, native GPCRs |

## Related Expression Systems

- [[pichia-pastoris]] — Yeast expression system for eukaryotic membrane proteins
- [[hek293-cells]] — HEK293 mammalian cells for GPCR functional assays