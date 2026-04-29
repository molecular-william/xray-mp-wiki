---
title: CorA Mg²⁺ Transporter
created: 2026-04-27
updated: 2026-04-27
type: protein
tags: [transporter, membrane-protein, channel]
sources: [doi/10.1002##pro.215]
category: concepts
---
layout: default



# CorA Mg²⁺ Transporter

## Overview

CorA is the primary Mg²⁺ uptake transporter found in most bacteria and some eukaryotes. It belongs to the metal ion transporter (MIT) superfamily and is essential for maintaining intracellular magnesium homeostasis. CorA channels are homopentamers with a distinctive funnel-shaped cytoplasmic domain.

## Structure Determination

Multiple CorA structures have been solved, revealing key insights into gating mechanisms:

### Thermotoga maritima CorA (Tm-CorA)
- **PDB IDs**: 2HRC (2.9 Å), 2HRD (3.7 Å), 2HRE (3.9 Å)
- **Oligomerization**: Homopentamer
- **Architecture**: Two transmembrane helices per monomer + large cytoplasmic funnel domain
- **Key finding**: Full-length structure revealed a closed-state conformation with a constricted pore

### Archaeoglobus fulgidus CorA (Af-CorA)
- **PDB ID**: 2HRR (2.9 Å, cytoplasmic domain only)
- **Oligomerization**: Dimer (truncated construct)
- **Key finding**: Truncated cytoplasmic domain formed dimers instead of pentamers, suggesting the transmembrane domain influences oligomerization

## Structural Architecture

- **Transmembrane region**: Two helices per monomer (TM1 and TM2), forming a five-helix pore
- **Cytoplasmic domain**: Large funnel-shaped assembly formed by:
  - **N-terminal α/β/α sandwich subdomain** (residues 1–125 in Vp-ZntB homolog)
  - **C-terminal coiled-coil stalk** (residues 126–203), composed of three anti-parallel α-helices (α4, α5, α6)
- **The α6 stalk helix** is the primary contributor to monomer–monomer interaction

## Gating Mechanism

CorA gating is proposed to be regulated by intracellular Mg²⁺ levels:

1. **Closed state** (high Mg²⁺): Pore constricted at the transmembrane region; cytoplasmic domain in compact conformation
2. **Open state** (low Mg²⁺): Pore dilated; cytoplasmic domain undergoes conformational change
3. **Metal-binding sites**: Two conserved sites at monomer–monomer interfaces in the cytoplasmic domain, proposed to sense Mg²⁺ levels
4. **Gating coupling**: Metal binding at cytoplasmic domain interfaces linked to pore opening via conformational changes in the transmembrane region
5. **Pore state**: Full-length Tm-CorA crystal structures (2.9 Å) show constricted pore in closed state; Vp-ZntB full-length model (homology-based) shows more open pore

## Pentamer Formation (from ZntB comparison)

The ZntB structure (Tan et al., 2009) revealed critical insights into CorA-like pentamer formation:

- The cytoplasmic domain alone drives pentamer assembly — transmembrane spanners not required
- α6 stalk helix is the primary contributor to monomer–monomer interaction along entire funnel
- Truncation of α6 stalk (as in previously reported CorA intracellular domain dimers) causes dimer formation instead of pentamer — suggesting those dimers were artifacts of excessive truncation
- Buried surface per monomer–monomer contact: ~2100 Å² (soluble domain only); total in full-length CorA: ~4400 Å² (2720 Å² from intracellular region)

## Signature Motif

CorA transporters share a conserved signature motif between TM1 and TM2:
- **CorA motif**: YGMNFxxMPEL
- **ZntB motif**: GxxG[I,V]NxGGxP (distant relative)

This motif is located on the outer surface of the membrane and tends to be disordered in crystal structures. It is proposed to play a role in ion selectivity.

## Comparison with ZntB

| Feature | CorA | ZntB |
|---------|------|------|
| Function | Mg²⁺ uptake | Zn²⁺/Cd²⁺ efflux |
| Oligomer | Pentamer | Pentamer |
| Cytoplasmic domain | Pentamer (full-length) / Dimer (truncated) | Pentamer (intrinsic) |
| Metal binding | Mg²⁺/Co²⁺/Ca²⁺ sites | Cl⁻ ions (25/pentamer) |
| Pore state | Closed (crystal) | Open (model) |
| Sequence identity | — | 17% |

## Cross-References

- [zntb-transporter](/proteins/zntb-transporter/) — Distant homolog; zinc/cadmium exporter with similar pentameric architecture
- [mfs-transporter](/concepts/mfs-transporter/) — Major facilitator superfamily (different family)
- [kirbac](/proteins/kirbac/) — Potassium channel; tetrameric architecture comparison