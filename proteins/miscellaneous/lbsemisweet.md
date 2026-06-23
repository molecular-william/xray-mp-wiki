---
title: LbSemiSWEET from Leptospira biflexa
created: 2026-05-27
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2017.03.010, doi/10.1038##nature13670]
verified: false
---

# LbSemiSWEET from Leptospira biflexa

## Overview

LbSemiSWEET is a sugar transporter from the SWEET family found in the bacterium Leptospira biflexa. It is among the smallest characterized transporters at less than 20 kDa, with a simple geometry as a symmetric dimer of three-helix bundles. LbSemiSWEET transports a single substrate ([Glucose](/xray-mp-wiki/reagents/additives/glucose/)) and operates via an alternating-access mechanism. The SWEET family is widespread and plays critical roles in phloem loading, nectar secretion, pollen development, and seed filling in plants.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2017.03.010 | 5UHS | 2.8 | P212121 | LbSemiSWEET D57A mutant | [Glucose](/xray-mp-wiki/reagents/additives/glucose/) |
| doi/10.1016##j.cell.2017.03.010 | 5UHQ | 2.8 | P212121 | LbSemiSWEET Q20A mutant | -- |
| doi/10.1038##nature13670 | -- | 2.40 | P21 | Full-length L. biflexa serovar Patoc [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/semisweet/) | -- |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: LbSemiSWEET with C-terminal 3C protease recognition site and 10xHis-tag
- **Induction**: 0.2 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/), 22 C overnight

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Sonication | -- | TBS (50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl) | Pelleted cells resuspended in TBS and lysed by sonication |
| Solubilization | Detergent solubilization | -- | TBS with 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) (2% w/v) | Solubilized for 2 hours at 4 C; insoluble debris pelleted at 16,000 rpm |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Cobalt [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | HisPur cobalt resin | TBS with 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) (0.1%) | His-tag cleaved by 3C protease to elute protein |
| Size-exclusion chromatography | Size-exclusion chromatography | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | 10 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) (0.03%) | Peak fractions pooled, concentrated, flash frozen in liquid N2, stored at -80 C |


## Crystallization

### doi/10.1016##j.cell.2017.03.010

| Parameter | Value |
|---|---|
| Method | vapor diffusion |
| Protein sample | LbSemiSWEET D57A reconstituted with [Monovaccenin](/xray-mp-wiki/reagents/lipids/monovaccenin/) (1:1.5 wt/wt) |
| Temperature | 4 C |
| Notes | Crystals grew within one week; D57A mutation favors outward-open conformation |

| Parameter | Value |
|---|---|
| Method | vapor diffusion |
| Protein sample | LbSemiSWEET Q20A reconstituted with [Monopalmitolein](/xray-mp-wiki/reagents/lipids/monopalmitolein/) (1:1.5 wt/wt) |
| Temperature | 4 C |
| Notes | Crystals appeared within two days; Q20A mutation favors inward-open conformation |

### doi/10.1038##nature13670

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase |
| Protein sample | L. biflexa serovar Patoc [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/semisweet/) reconstituted into [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) (1:1.5 protein:lipid) |
| Temperature | 20 C |
| Notes | Crystals grew in about 1 week; captured in occluded conformation |


## Biological / Functional Insights

### Alternating-access transport mechanism

LbSemiSWEET undergoes spontaneous transitions between outward-open, occluded, and inward-open conformations. The extracellular gate (Tyr51, Ile60, Arg55, Asp57) closes first, followed by opening of the intracellular gate (Phe17, Met37, Tyr38, Phe41). The occluded state is an on-pathway intermediate that acts as an air lock, preventing simultaneous opening of both gates.

### Glucose translocation as a free ride

MD simulations reveal that [Glucose](/xray-mp-wiki/reagents/additives/glucose/) takes a free ride across the membrane, with the transporter adopting the same conformational transitions with and without substrate. The apparent Km for [Glucose](/xray-mp-wiki/reagents/additives/glucose/) is ~70 uM for D57A mutant and ~160 uM for wild-type. [Glucose](/xray-mp-wiki/reagents/additives/glucose/) binds off-center between Trp48 residues on each protomer, coordinated by Asn64 and Thr13 on one protomer.

### Gating residue mutagenesis

Alanine substitution of extracellular gate residues Tyr51, Ile60, and intracellular gate residues Phe17, Met37, and Tyr38 ablated [Glucose](/xray-mp-wiki/reagents/additives/glucose/) uptake. Asp57, Arg55, Met37, and Phe41 mutations had no significant effect on activity. The D57A mutation increased [Glucose](/xray-mp-wiki/reagents/additives/glucose/) affinity more than two-fold compared to wild-type.

### Occluded state structure

The L. biflexa [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/semisweet/) structure at 2.40 Å resolution captures an occluded conformation. At the extracellular side, D57 from one protomer forms hydrogen bonds with Y51 from the other protomer, shielding the cavity from the extracellular solution. A strong non-protein electron density is present at the cavity center, surrounded by W48 and N64 from both protomers. The antiparallel aromatic ring of tryptophan from each protomer is within 4 Å of the putative substrate. W48 and N64 are implicated as critical residues in substrate binding and translocation.


## Cross-References

- [Vibrio sp. SemiSWEET](/xray-mp-wiki/proteins/miscellaneous/vibrio-sp-semisweet/) — Related bacterial SemiSWEET crystallized in outward-open state at 1.70 Å
- [A. thaliana SWEET1](/xray-mp-wiki/proteins/miscellaneous/a-thaliana-sweet1/) — Plant SWEET1 with conserved W and N residues critical for sugar transport
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — LbSemiSWEET operates via alternating access with spontaneous conformational transitions
- [SWEET Transporter Family](/xray-mp-wiki/concepts/sweet-transporter/) — LbSemiSWEET is a member of the SWEET family of sugar transporters
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for solubilization and purification
- [Glucose](/xray-mp-wiki/reagents/additives/glucose/) — Substrate transported by LbSemiSWEET; used in crystallization
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid used in lipidic cubic phase crystallization
- [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/semisweet/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [IPTG](/xray-mp-wiki/reagents/additives/iptg/) — Additive used in purification or crystallization buffers
