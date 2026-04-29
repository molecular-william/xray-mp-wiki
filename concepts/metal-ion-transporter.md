---
title: Metal Ion Transporter (MIT) Superfamily
created: 2026-04-27
updated: 2026-04-27
type: concept
tags: [transporter, membrane-protein]
sources: [doi/10.1002##pro.215]
category: concepts
---
layout: default



# Metal Ion Transporter (MIT) Superfamily

## Overview

The metal ion transporter (MIT) superfamily is a large and diverse group of essential membrane proteins found in all three kingdoms of life. They are involved in metal ion transport (uptake or efflux) across cellular membranes, maintaining metal homeostasis which is critical for cellular function.

## Major Families

### CorA Family
- **Function**: Mg²⁺ uptake (primary magnesium transporter in most bacteria)
- **Architecture**: Homopentamer; 2 TM helices per monomer; large cytoplasmic funnel domain
- **Members**: CorA (bacteria), Cch1/Mid1 (eukaryotes)
- **Structures**: Multiple X-ray structures (Tm-CorA, Af-CorA, Vp-ZntB homolog)
- **Gating**: Regulated by intracellular Mg²⁺ [amicon-filters](/xray-mp-wiki/methods/purification/amicon-filters/) via metal-binding sites

### ZntB Family
- **Function**: Zn²⁺/Cd²⁺ efflux (zinc/cadmium exporters)
- **Architecture**: Distant homolog of CorA; pentameric cytoplasmic domain
- **Members**: ZntB (Salmonella, Vibrio)
- **Structures**: Vp-ZntB cytoplasmic domain (PDB: 3CK6, 1.90 Å)
- **Key difference**: Binds Cl⁻ ions rather than metal ions in the cytoplasmic domain

## Common Features

- **Membrane topology**: Typically 2 transmembrane helices per subunit
- **Oligomerization**: Often pentameric (CorA-type)
- **Cytoplasmic domain**: Large soluble domain involved in gating/regulation
- **Metal selectivity**: Determined by the transmembrane pore and signature motifs
- **Essentiality**: Most MIT transporters are essential for cell viability

## Signature Motifs

Different MIT families have characteristic sequence motifs in the transmembrane region:

| Family | Signature Motif | Location |
|--------|----------------|----------|
| CorA | YGMNFxxMPEL | Between TM1 and TM2 |
| ZntB | GxxG[I,V]NxGGxP | Between TM1 and TM2 |

## Functional Importance

- **Magnesium**: Essential cofactor for ATPases, polymerases, ribosomes
- **Zinc**: Essential for structural (zinc fingers) and catalytic (metalloenzymes) roles
- **Cadmium**: Toxic; efflux systems prevent accumulation
- **Homeostasis**: Tight regulation prevents both deficiency and toxicity

## Cross-References

- [cora-mg-transporter](/xray-mp-wiki/concepts/cora-mg-transporter/) — Mg²⁺ uptake transporter; archetypal MIT member
- [zntb-transporter](/xray-mp-wiki/proteins/zntb-transporter/) — Zn²⁺/Cd²⁺ exporter; distant CorA homolog
- [mfs-transporter](/xray-mp-wiki/concepts/mfs-transporter/) — Major facilitator superfamily (different family)