---
title: Cell-Free Protein Synthesis for Membrane Proteins
created: 2026-05-18
updated: 2026-05-22
type: method
category: methods
layout: default
tags: [expression-system, membrane-protein]
sources: [doi/10.1016##j.jmb.2011.06.028]
---

# Cell-Free Protein Synthesis for Membrane Proteins

## Overview

Cell-free protein synthesis (CFPS) systems can be supplemented with both lipid and detergent to produce functional membrane proteins directly in a membrane-like environment. This approach eliminates the need for cellular expression and avoids the challenges of heterologous expression in living cells. The system produces protein that is co-translationally incorporated into lipid-detergent micelles or liposomes, enabling direct purification and crystallization without harsh solubilization steps. This is particularly valuable for membrane proteins that are difficult to express in E. coli or other expression hosts.

## Principle

Cell-free systems use cell extracts containing ribosomes, tRNAs, amino acids, and translation factors to synthesize proteins from added DNA templates. For membrane proteins, the extract is supplemented with lipid vesicles or detergent-lipid mixtures that provide a hydrophobic environment for the nascent transmembrane domains to insert into during translation. This co-translational insertion mimics the natural membrane insertion process, improving folding and functional yield.

## Protocol

### Reagents
- **Cell-free extract**: E. coli S30 extract or wheat germ extract
- **DNA template**: Plasmid or linear DNA with T7 promoter
- **Membrane mimetic**: Detergent (e.g., DDM, LDAO) plus lipid (e.g., POPC, monoolein)
- **Energy regenerating system**: Creatine phosphate/creatine kinase or phosphoenolpyruvate/pyruvate kinase
- **Amino acids**: Standard 20 amino acids plus any non-standard amino acids
- **Translation factors**: EF-Tu, EF-G, RF1/RF2, RF3

### Steps
1. Prepare cell-free extract (commercial or in-house prepared S30 extract)
2. Add DNA template (10-100 ng/µL) encoding the target membrane protein
3. Supplement with detergent and lipid at appropriate ratios (typically 0.05-0.5% detergent, 0.1-1% lipid)
4. Add energy regenerating system and amino acids
5. Incubate at 25-30°C for 2-24 hours
6. Harvest the reaction mixture containing membrane protein in lipid-detergent micelles

### Conditions
- **Temperature**: 25-30°C (optimal for folding)
- **Duration**: 2-24 hours depending on protein
- **Detergent**: DDM 0.1%, LDAO 0.05-0.1%, or other mild detergents
- **Lipid**: POPC 0.5-1%, or mixed lipid/detergent nanodisc components

## Advantages

- **No cellular toxicity**: Membrane protein expression does not kill the host cell
- **Co-translational insertion**: Protein inserts during synthesis, improving folding
- **Flexibility**: Easy to incorporate non-standard amino acids or isotopic labels
- **Speed**: Expression in hours rather than days
- **Scalability**: Can be scaled from microliters to liters
- **Control**: Reaction conditions easily tunable

## Disadvantages

- **Cost**: Cell-free reagents are more expensive than cellular expression
- **Yield**: Lower yields than optimized cellular expression systems
- **Complexity**: Requires optimization of detergent-lipid ratios
- **Limited volume**: Standard reactions are small (50-500 µL)

## Proteins Using This Method

| Protein | Resolution | PDB | Notes |
|---|---|---|---|
| [GlpG Rhomboid Intramembrane Protease (E. coli)](/xray-mp-wiki/proteins/glpg/) | 2.3 A | 3K6H | Cell-free synthesis with lipid-detergent supplement |
| [Human Adenosine A2A Receptor (A2AR)](/xray-mp-wiki/proteins/human-adenosine-a2a-receptor-a2ar/) | N/A | N/A | Used for functional studies and ligand binding |

## Related Methods

- [Pichia pastoris Expression System](/xray-mp-wiki/methods/expression-systems/pichia-pastoris/) — Eukaryotic expression for proper folding
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Purification from cell-free reactions

## Related Reagents

- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent for membrane protein solubilization
- [Phosphatidylcholine (POPC)](/xray-mp-wiki/reagents/lipids/popc/) — Lipid component for membrane mimetic

## Cross-References

- [GlpG Rhomboid Intramembrane Protease (E. coli)](/xray-mp-wiki/proteins/glpg/) — Rhomboid protease expressed via cell-free synthesis
- [Pichia pastoris Expression System](/xray-mp-wiki/methods/expression-systems/pichia-pastoris/) — Alternative expression system for membrane proteins
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used in cell-free membrane protein synthesis
