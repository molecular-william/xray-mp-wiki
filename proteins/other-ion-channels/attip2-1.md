---
title: "AtTIP2;1 - Arabidopsis thaliana Tonoplast Intrinsic Protein 2;1"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein]
sources: [doi/10.1371##journal.pbio.1002411]
verified: false
---

# AtTIP2;1 - Arabidopsis thaliana Tonoplast Intrinsic Protein 2;1

## Overview

AtTIP2;1 is an ammonia-permeable [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) (aquaammoniaporin) from the TIP
(Tonoplast Intrinsic Protein) subfamily of Arabidopsis thaliana. It facilitates
permeation of both water and ammonia across the vacuolar membrane. The
structure reveals an extended selectivity filter with five positions,
including a histidine (His 131) in loop C that directly participates in
substrate interactions, a unique feature among [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/). A water-filled side
pore beneath loop C is speculated to participate in deprotonating ammonium
ions, potentially increasing net ammonia permeation.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1371##journal.pbio.1002411 | 5I32 | 1.18 | — |  |  |

## Expression and Purification

- **Expression system**: Pichia pastoris
- **Construct**: Full-length AtTIP2;1 with N-terminal deca-His-tag and TEV cleavage site
- **Notes**: Up to 1.1 mg purified protein per g wet cells

### Purification Workflow

- **Expression system**: Pichia pastoris
- **Expression construct**: Full-length AtTIP2;1 with N-terminal deca-His-tag and TEV cleavage site

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Urea wash of membranes | Wash | — |  | Membranes washed with [Urea](/xray-mp-wiki/reagents/substrates/urea/) to remove peripheral proteins |
| Solubilization | Detergent solubilization | — | 10% [OG](/xray-mp-wiki/reagents/detergents/og/) ([OG](/xray-mp-wiki/reagents/detergents/og/)) | Membranes solubilized with [OG](/xray-mp-wiki/reagents/detergents/og/) |
| Nickel affinity chromatography | Affinity chromatography | Ni-NTA | 100 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) wash + 0.05% [OG](/xray-mp-wiki/reagents/detergents/og/) |  |
| Size exclusion chromatography | SEC | — | 0.05% [OG](/xray-mp-wiki/reagents/detergents/og/) |  |


## Crystallization

### doi/10.1371##journal.pbio.1002411

| Parameter | Value |
|---|---|
| Method | Hanging drop vapor diffusion |
| Reservoir | 50 mM magnesium/sodium [Acetate](/xray-mp-wiki/reagents/buffers/acetate/) pH 5.0, 28% (v/v) [Peg](/xray-mp-wiki/reagents/additives/peg/) 400 |
| Temperature | Room temperature |
| Cryoprotection | Flash-cooled in liquid nitrogen |
| Notes | Data collected at Swiss Light Source beamline X06SA (PXI), wavelength 1.0 A |


## Biological / Functional Insights

### Extended selectivity filter

AtTIP2;1 reveals an extended selectivity filter with five positions
(H2P, LCP, H5P, LEP, HEP) rather than the classical four-position
aromatic/arginine filter of water-specific [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/). The conserved
arginine (Arg 200) adopts a unique unpredicted position, stabilized by
interactions with His 63 (H2P) and His 131 (LCP).

### Ammonia permeability determinants

The relatively wide pore and polar nature of the selectivity filter
explain ammonia permeability. A histidine at position LCP in loop C
(His 131) directly participates in substrate interactions, extending
the selectivity filter.

### Water-filled side pore

A water-filled side pore beneath loop C is speculated to facilitate
deprotonation of ammonium ions via a Grotthuss-type proton shuttle
mechanism involving His 131, potentially increasing net ammonia
permeation.

### Gain-of-function in human AQP1

Mutation of the four deviating selectivity filter residues in
water-specific human [AQP1](/xray-mp-wiki/proteins/other-ion-channels/aqp1/) to corresponding TIP2 residues (F56H,
N127H, H180I, C189G) converted it into an AtTIP2;1-like ammonia
channel, demonstrating the sufficiency of the extended selectivity
filter determinants.


## Cross-References

- [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) — AtTIP2;1 is a member of the aquaporin superfamily, specifically the TIP subfamily
- [Extended Selectivity Filter](/xray-mp-wiki/concepts/transport-mechanisms/extended-selectivity-filter/) — AtTIP2;1 defines the five-position extended selectivity filter in aquaporins
- [n-Octyl-beta-D-glucoside (OG)](/xray-mp-wiki/reagents/detergents/og/) — OG used for solubilization of AtTIP2;1 from P. pastoris membranes
- [Polyethylene Glycol 400 (PEG400)](/xray-mp-wiki/reagents/additives/peg-400/) — PEG 400 used as crystallization precipitant at 28% (v/v)
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Imidazole used at 100 mM in Ni-NTA wash step
- [Urea](/xray-mp-wiki/reagents/substrates/urea/) — Referenced in the context of Urea
- [OG](/xray-mp-wiki/reagents/detergents/og/) — Referenced in the context of OG
- [Acetate](/xray-mp-wiki/reagents/buffers/acetate/) — Referenced in the context of Acetate
- [Peg](/xray-mp-wiki/reagents/additives/peg/) — Referenced in the context of Peg
- [AQP1](/xray-mp-wiki/proteins/other-ion-channels/aqp1/) — Referenced in the context of AQP1
