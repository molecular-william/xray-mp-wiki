---
title: Synaptobrevin-2 (Rat Neuronal Qc-SNARE Protein)
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature08156]
verified: false
---

# Synaptobrevin-2 (Rat Neuronal Qc-SNARE Protein)

## Overview

Synaptobrevin-2 (also known as VAMP-2) is a neuronal Qc-SNARE protein from rat that resides on synaptic vesicle membranes. It contains an N-terminal proline-rich region, a SNARE motif, a short linker, and a C-terminal transmembrane domain. Synaptobrevin-2 is the vesicle-associated component of the neuronal SNARE complex, which assembles with [Syntaxin-1A (Rat Neuronal Qa-SNARE Protein)](/xray-mp-wiki/proteins/syntaxin-1a) and SNAP-25 to drive synaptic vesicle fusion. The X-ray structure of the SNARE complex including synaptobrevin-2 transmembrane region revealed continuous helical extension through the linker into the membrane.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature08156 | TBA | 3.4 A | C2 | Rat synaptobrevin-2 residues 30-116 (SNARE motif, linker, transmembrane region; lacking N-terminal proline-rich region) | None |
| doi/10.1038##nature08156 | TBA | 4.8 A | I212121 | Rat synaptobrevin-2 residues 30-116 complexed with syntaxin-1A, crystallized in n-heptyl beta-D-glucopyranoside | None |

## Expression and Purification

- **Expression system**: Escherichia coli BI21 (DE3)
- **Construct**: Rat synaptobrevin-2 (residues 1-96 and 1-116) with N-terminal His-tag, expressed from pET28a. For crystallization, residues 30-116 (lacking N-terminal proline-rich region) were cloned into pET28a via NdeI/XhoI sites.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | Expression in E. coli BI21 (DE3) from pET28a | -- | -- + -- | His-tagged synaptobrevin-2 expressed separately |
| Ni-NTA affinity chromatography | Ni-NTA affinity chromatography | Ni-NTA agarose | -- + -- | Initial purification of His-tagged synaptobrevin-2 |
| Ion-exchange chromatography | Ion-exchange chromatography | Not specified | 50 mM n-octyl beta-D-glucopyranoside + n-octyl beta-D-glucopyranoside | Purified by ion exchange chromatography in presence of 50 mM n-octyl beta-D-glucopyranoside |
| Complex assembly | In vitro complex assembly | -- | Assembled by overnight incubation of monomers at 4 C + -- | Synaptobrevin-2 used in complex assembly with [Syntaxin-1A (Rat Neuronal Qa-SNARE Protein)](/xray-mp-wiki/proteins/syntaxin-1a) and [SNAP-25A (Rat Neuronal Qbc-SNARE Protein)](/xray-mp-wiki/proteins/snap-25a) |


## Crystallization

### doi/10.1038##nature08156

| Parameter | Value |
|---|---|
| Method | Vapor diffusion in n-nonyl beta-D-glucopyranoside |
| Protein sample | Syntaxin-1A/SNAP-25/synaptobrevin-2 complex with linkers and TMRs in n-nonyl beta-D-glucopyranoside |
| Reservoir | Not specified in main text |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | C2 space group, 3.4 A resolution. Two similar complexes per asymmetric unit (r.m.s.d. 0.6 A). X-shaped assembly formed by four complexes through TMR contacts. |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion in n-heptyl beta-D-glucopyranoside |
| Protein sample | Syntaxin-1A/SNAP-25/synaptobrevin-2 complex purified and crystallized in n-heptyl beta-D-glucopyranoside |
| Reservoir | Not specified in main text |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | I212121 space group, 4.8 A resolution. Two similar complexes per asymmetric unit. C-terminal parts of synaptobrevin-2 TMRs deviate slightly, indicating conformational flexibility. |


## Biological / Functional Insights

### Continuous helical extension from SNARE motif through TMR

Synaptobrevin-2 forms a continuous alpha-helix throughout its SNARE motif, linker region, and transmembrane region. This helical continuity extends the four-helix core SNARE complex into the membrane, with the linker region forming part of the helical bundle.

### Aromatic layer contacts in linker region

The linker region of synaptobrevin-2 contributes four residues (Lys 85, Arg 86, Trp 89, Asn 92) that form a pocket burying Tyr 257 of [Syntaxin-1A (Rat Neuronal Qa-SNARE Protein)](/xray-mp-wiki/proteins/syntaxin-1a). Lys 264 of [Syntaxin-1A (Rat Neuronal Qa-SNARE Protein)](/xray-mp-wiki/proteins/syntaxin-1a) also engages in a hydrogen bond with Asn 92 of synaptobrevin-2, stabilizing the intermolecular contacts between the two SNARE proteins in the linker region.

### Transmembrane helix interactions with syntaxin-1A

Residues Met 95, Ile 98, Leu 99, Ile 102, and Ile 106 in synaptobrevin-2 largely contribute to the interaction surface with [Syntaxin-1A (Rat Neuronal Qa-SNARE Protein)](/xray-mp-wiki/proteins/syntaxin-1a) TMR residues Ile 268, Cys 271, Ile 274, and Leu 275. Beyond this region, the two TMRs veer away from each other, indicating a specific interaction interface.

### Free C-terminal tail interferes with packing

When only the TMR of synaptobrevin-2 was present in the complex, stability was lower than that of the core complex, suggesting that the free C-terminal portion of synaptobrevin-2 interferes with the packing of the four-helix bundle upstream. The crystallization construct lacks the N-terminal proline-rich region (residues 30-116).


## Cross-References

- [Syntaxin-1A (Rat Neuronal Qa-SNARE Protein)](/xray-mp-wiki/proteins/structural-adhesion/syntaxin-1a/) — Core SNARE complex partner; forms continuous helical bundle through SNARE motif, linker, and TMR
- [SNAP-25A (Rat Neuronal Qbc-SNARE Protein)](/xray-mp-wiki/proteins/structural-adhesion/snap-25a/) — Third component of the neuronal SNARE complex; assembled in trans with syntaxin-1A and synaptobrevin-2
- [Nonylglucoside (NG)](/xray-mp-wiki/reagents/detergents/nonylglucoside/) — n-nonyl beta-D-glucopyranoside used as detergent for crystallization (12 mM)
- [Heptylglucoside (HpG)](/xray-mp-wiki/reagents/detergents/heptylglucoside/) — n-heptyl beta-D-glucopyranoside used for alternative crystallization (140 mM)
- [n-Octyl beta-D-glucopyranoside (OG)](/xray-mp-wiki/reagents/detergents/og/) — n-octyl beta-D-glucopyranoside used in purification buffer (50 mM)
- [n-Dodecyl-beta-D-maltopyranoside (beta-DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — n-dodecyl beta-D-maltopyranoside (0.03% w/v) used for endosomal SNARE complex purification
- [SNARE Complex](/xray-mp-wiki/concepts/snare-complex/) — Synaptobrevin-2 is the Qc-SNARE component of the four-helix bundle SNARE complex
