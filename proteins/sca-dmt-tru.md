---
title: ScaDMT^tru Truncated Divalent Metal-Ion Transporter
created: 2026-06-05
updated: 2026-06-05
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.2904]
verified: false
---

# ScaDMT^tru Truncated Divalent Metal-Ion Transporter

## Overview

ScaDMT^tru is a truncated construct of ScaDMT from Staphylococcus capitis, lacking 41 amino acids at the N terminus including 17 residues of the first predicted transmembrane helix. This construct was identified through systematic truncation of both termini in increments of four residues. ScaDMT^tru retains wild-type-like Cd2+ binding affinity (Kd = 37 +/- 8 uM) and transports both Cd2+ and Mn2+, making it suitable for crystallization. It was co-crystallized with a nanobody to obtain high-resolution structures at 3.1 A and 3.4 A resolution.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nsmb.2904 | not specified in paper | 3.1 A | P3_1 2 1 | ScaDMT^tru (lacking 41 N-terminal residues) co-crystallized with llama-derived nanobody, inward-facing conformation, apo complex | none (nanobody-bound apo complex) |
| doi/10.1038##nsmb.2904 | not specified in paper | 3.4 A | P3_1 2 1 | ScaDMT^tru-nanobody complex with Mn2+ bound, inward-facing conformation | Mn2+ (anomalous density confirmed at binding site; coordinated by Asp49, Asn52, Met226, and Ala223 backbone) |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: ScaDMT^tru (truncated S. capitis ScaDMT lacking 41 N-terminal residues), C-terminal His10 tag with HRV 3C protease cleavage site, cloned into pBXC3H vector

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane preparation | Cell disruption with custom-made cell disruptor; ultracentrifugation | -- | 50 mM potassium phosphate pH 7.5, 150 mM NaCl + DM (1-2% w/v) | Membrane vesicles extracted with 10% glycerol and DM |
| Affinity purification | Immobilized metal affinity chromatography (IMAC) | Ni-NTA | DM-containing buffer + DM | His10-tag purification with HRV 3C protease cleavage during dialysis |
| Size-exclusion chromatography | SEC on Superdex S200 | Superdex S200 | 10 mM HEPES pH 7.5, 150 mM NaCl, 0.25% DM + DM | Peak fractions pooled for complex formation and crystallization |


## Crystallization

### doi/10.1038##nsmb.2904

| Parameter | Value |
|---|---|
| Method | Nanobody co-crystallization, vapor diffusion |
| Notes | ScaDMT^tru co-crystallized with SEC-purified nanobody. PEG 600/650 used as precipitants. Mn2+ complex obtained by soaking crystals in Mn2+ solution. SeMet-labeled crystals used for structural determination. |


## Biological / Functional Insights

### Truncation enables high-resolution crystallization

Systematic truncation of ScaDMT termini in four-residue increments identified
ScaDMT^tru as the shortest well-behaved construct. Removal of 41 N-terminal residues
(including 17 residues of the first predicted TM helix) stabilized the protein for
crystallization while retaining transport activity and ion-binding affinity comparable
to wild-type ScaDMT.

### Nanobody enables high-resolution structure determination

Co-crystallization of ScaDMT^tru with a llama-derived nanobody enabled structure
determination at 3.1 A resolution, a significant improvement over the 6.5 A resolution
of full-length crystals. The nanobody binds to the transporter and stabilizes a single
conformational state (inward-facing), facilitating crystallization.


## Cross-References

- [ScaDMT Divalent Metal-Ion Transporter](/xray-mp-wiki/proteins/sca-dmt/) — ScaDMT^tru is a truncated N-terminal variant of full-length ScaDMT
- [DMT Superfamily (Drug/Metabolite Transporter Superfamily)](/xray-mp-wiki/concepts/dmt-superfamily/) — ScaDMT^tru is a member of the SLC11 family
- [Nanobody](/xray-mp-wiki/reagents/nanobody/) — ScaDMT^tru co-crystallized with nanobody enabled high-resolution structure determination
