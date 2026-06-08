---
title: TEV Protease (Tobacco Etch Virus Protease)
created: 2026-06-08
updated: 2026-06-08
type: reagent
category: reagents
layout: default
tags: [enzyme, protease, protein-tag, subdirectory-protein-tags]
sources: [doi/10.7554##eLife.60724, doi/10.1002##1873-3468.14136, doi/10.1016##j.cell.2015.04.011, doi/10.1038##nature06325, doi/10.1038##nature08650, doi/10.1038##ncomms7112, doi/10.1038##nsmb.1788, doi/10.1038##nsmb.3049]
verified: false
---

# TEV Protease (Tobacco Etch Virus Protease)

## Overview

TEV protease (tobacco etch virus protease) is a highly specific cysteine protease used for cleaving affinity tags (His-tag, MBP, GST, SUMO) from recombinant proteins. TEV protease recognizes a specific 8-residue sequence (ENLYFQ/S) and cleaves between the glutamine and serine/glycine residues. It functions optimally at 4-25C and is widely used in membrane protein purification workflows where gentle tag removal is required.


## Properties

- **Chemical name**: Tobacco Etch Virus (TEV) protease
- **Class**: cysteine protease

## Use in Membrane Protein Work

### Cleavage of affinity tags from recombinant proteins

TEV protease cleaves His-tag, MBP, GST, and other affinity tags from recombinant proteins after purification. Recognizes the sequence ENLYFQ↓(S/G) and cleaves between glutamine and serine/glycine, producing a native amino acid sequence at the junction.


### Removal of fusion partners after protein purification

Used to cleave fusion partners such as MBP from target proteins. In the Vps45-Tlg2 study, TEV protease cleaved His7-MBP tags from multiple Tlg2 and SNARE constructs after Ni-affinity chromatography.


### Generation of native protein sequences for structural studies

TEV protease generates proteins with native N-termini, important for structural studies where tag presence could interfere with crystallization or biological activity.


## Examples from This Wiki

| Protein | Concentration | Context | Result |
|---|---|---|---|
| [Tlg2](/xray-mp-wiki/proteins/tlg2/) | not specified | TEV protease cleaved His7-MBP tags from C. thermophilum Tlg2 constructs including MBP-Tlg2(1-327), MBP-Tlg2(258-327), and other SNARE motifs after Ni-affinity chromatography
 | Tags removed overnight at 4C; cleaved tags retained on His60 Ni Superflow resin |
| MBP-Snc2, MBP-Tlg1, MBP-Vti1 | not specified | TEV protease used to cleave MBP tags from C. thermophilum SNARE motifs (Snc2 R-SNARE, Tlg1 Qc-SNARE, Vti1 Qb-SNARE) for oligomerization assays
 | Released SNARE motifs used in size-exclusion chromatography |
| M3 Muscarinic Acetylcholine Receptor | not specified | TEV protease cleaved N-terminal extracellular tail of M3-crys construct (rat M3 receptor with FLAG tag, glycosylation mutants, TEV site at residues 50-56, T4L fusion in ICL3). Cleavage did not significantly affect ligand binding affinities (M3-crys [3H]NMS Kd: 337 +/- 9 pM; M3-crys-cleaved: 469 +/- 110 pM).
 | TEV cleavage produced construct with similar binding properties, enabling structural studies with reduced flexibility |

## Advantages and Disadvantages

No advantages/disadvantages recorded.

## Comparison with Related Reagents

No comparison data available.

## Cross-References

- [BRIL Fusion Protein](/xray-mp-wiki/reagents/protein-tags/bril/) — Related protein tag system using cleavable linkers
- [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/at1r/) — His-tagged TEV protease used to cleave FLAG/His tags from BRIL-AT1R
