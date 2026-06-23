---
title: "GltTk (Glutamate Transporter Homologue from Thermococcus kodakarensis)"
created: 2026-06-10
updated: 2026-06-10
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.7554##eLife.45286]
verified: false
---

# GltTk (Glutamate Transporter Homologue from Thermococcus kodakarensis)

## Overview

[Glttk](/xray-mp-wiki/proteins/slc-transporters/glttk/) is a glutamate transporter homologue from the hyperthermophilic archaeon Thermococcus kodakarensis. It belongs to the SLC1 family of transporters (excitatory amino acid transporters, EAATs) and serves as a model system for studying the transport mechanism of mammalian glutamate transporters. [Glttk](/xray-mp-wiki/proteins/slc-transporters/glttk/) transports both L- and [D Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/) with identical Na+:substrate coupling stoichiometry (3:1). The crystal structure of GltTk with [D Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/) reveals how the enantiomeric substrate is accommodated with only minor rearrangements in the binding site.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.7554##eLife.45286 | 6R7R | 2.8 | P 32 2 1 | Full-length [Glttk](/xray-mp-wiki/proteins/slc-transporters/glttk/) with C-terminal His8-tag | [D Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/), 3 Na+ ions |
| doi/10.1038##s41467-2016 | 5E9S | 2.7 | — | Full-length [Glttk](/xray-mp-wiki/proteins/slc-transporters/glttk/) with C-terminal His8-tag | [L Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/) |

## Expression and Purification

- **Expression system**: Escherichia coli MC1061
- **Construct**: Full-length [Glttk](/xray-mp-wiki/proteins/slc-transporters/glttk/) with C-terminal His8-tag in pBAD24
- **Notes**: Expression induced with L-arabinose
- **Induction**: L-arabinose

### Purification Workflow

- **Expression system**: Escherichia coli MC1061
- **Expression construct**: Full-length [Glttk](/xray-mp-wiki/proteins/slc-transporters/glttk/) with C-terminal His8-tag
- **Tag info**: C-terminal His8-tag

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell harvest and membrane preparation | Centrifugation | — |  | Cells harvested and membranes prepared as described in Guskov et al., 2016 |
| Membrane solubilization | Detergent solubilization | — | [DM](/xray-mp-wiki/reagents/detergents/dm/) ([[DM](/xray-mp-wiki/reagents/detergents/dm/)](/xray-mp-wiki/reagents/detergents/dm/)) |  |
| Affinity chromatography | IMAC | — | [DM](/xray-mp-wiki/reagents/detergents/dm/) |  |
| Size-exclusion chromatography | SEC | Superdex 200 10/300 GL | 10 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) KOH, pH 8.0, 100 mM KCl + 0.15% [DM](/xray-mp-wiki/reagents/detergents/dm/) |  |

**Final sample**: Purified apo [Glttk](/xray-mp-wiki/proteins/slc-transporters/glttk/) (no sodium ions present during purification)


## Crystallization

### doi/10.7554##eLife.45286

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, hanging drop |
| Protein sample | Purified apo [Glttk](/xray-mp-wiki/proteins/slc-transporters/glttk/) in 10 mM Hepes KOH pH 8.0, 100 mM KCl, 0.15% DM, supplemented with 300 mM NaCl, 300 uM [D Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/) at 7 mg/ml |
| Reservoir | 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 10% PEG 4000, 100 mM Tris/bicine pH 8.0, 60 mM CaCl2, 60 mM MgCl2, 0.75% OG |
| Mixing ratio | 1:1 ratio of protein to reservoir |
| Temperature | 5 C |
| Cryoprotection | None (crystals flash-frozen directly) |


## Biological / Functional Insights

### D-aspartate transport by GltTk

[Glttk](/xray-mp-wiki/proteins/slc-transporters/glttk/) transports [D Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/) with the same 3:1 Na+:substrate coupling
stoichiometry as [L Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/). The Km for D-aspartate transport is
1.1 uM, comparable to 0.75 uM for [L Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/). The Kd for D-aspartate
binding at high sodium (500 mM) is 374 nM, compared to 62 nM for
[L Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/), indicating slightly lower affinity for the D-enantiomer.

### Structural accommodation of D-aspartate

The crystal structure at 2.8 A shows [D Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/) bound in the
outward-facing occluded state with highly similar binding mode to
[L Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/). Despite the mirrored spatial arrangement of functional
groups around the chiral Calpha atom, D- and [L Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/) form nearly
identical hydrogen bonding networks with conserved residues in the
binding site. Only minor changes in the positions of Calpha and Cbeta
carboxyl groups distinguish the two binding modes.

### Three sodium ion binding sites

Three peaks of electron density at positions matching the three sodium
ions in the [L Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/) complex confirm 3:1 Na+:D-aspartate coupling
stoichiometry. None of the sodium sites are directly coordinated by
substrate, consistent with the identical coupling stoichiometry for
both enantiomers.

### First transporter with enantiomeric substrate structures

[Glttk](/xray-mp-wiki/proteins/slc-transporters/glttk/) is the first amino acid transporter for which structures of both
enantiomeric substrates (L- and [D Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/)) have been determined,
providing insight into how transporters can accommodate stereoisomers.


## Cross-References

- [Glutamate Transporter Family (SLC1/EAAT)](/xray-mp-wiki/concepts/transport-mechanisms/glutamate-transporter-family/) — GltTk is an archaeal homologue of mammalian EAATs
- [Human Excitatory Amino Acid Transporter 1 (EAAT1)](/xray-mp-wiki/proteins/slc-transporters/eaat1/) — Mammalian EAAT1 is a structural and functional homolog of GltTk
- [Glttk](/xray-mp-wiki/proteins/slc-transporters/glttk/) — Referenced in glt-tk text
- [D Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/) — Referenced in glt-tk text
- [L Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/) — Referenced in glt-tk text
- [DM](/xray-mp-wiki/reagents/detergents/dm/) — Referenced in glt-tk text
- [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) — Referenced in glt-tk text
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Referenced in glt-tk text
- [OG](/xray-mp-wiki/reagents/detergents/og/) — Referenced in glt-tk text
