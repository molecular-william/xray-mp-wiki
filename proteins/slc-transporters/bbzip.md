---
title: "BbZIP (Bordetella bronchiseptica ZIP metal transporter)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-023-36048-4]
verified: false
---

# BbZIP (Bordetella bronchiseptica ZIP metal transporter)

## Overview

BbZIP (ZIPB) is a prokaryotic ZIP family divalent metal transporter from Bordetella bronchiseptica. The Zrt/Irt-like protein (ZIP) family (SLC39A) imports Zn2+, Fe2+, Mn2+, and other first-row d-block divalent metals into the cytoplasm and is ubiquitously expressed across all kingdoms of life. BbZIP was structurally characterized to establish the transport mechanism for the ZIP family. The protein adopts a two-domain architecture with a transport domain (Domain I: α1/4/5/6) that carries the binuclear metal centre (BMC) and slides vertically as a rigid body against a static scaffold domain (Domain II: α2/3/7/8) that mediates dimerization, consistent with an elevator-type transport mechanism. BbZIP has nine transmembrane helices (α0 plus the conserved α1-α8 core), with the extra N-terminal α0 present in some gufA subfamily members.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-023-36048-4 | 5TSB | 2.75 | P 2_1 2_1 2 | Full-length BbZIP with N-terminal His-tag (metal-bound inward-facing conformation, used as MR search model) | Cd2+ (binuclear metal centre) |
| doi/10.1038##s41467-023-36048-4 | 8CZJ | 2.75 | P 2_1 2_1 2_1 | Full-length BbZIP with N-terminal His-tag (apo state, metal-free) | apo (no metal) |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Full-length BbZIP from Bordetella bronchiseptica with N-terminal His-tag
- **Induction**: Not specified in detail

### Purification Workflow

- **Expression system**: E. coli
- **Tag info**: N-terminal His-tag

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane solubilization | Detergent solubilization | — | 50 mM NaH2PO4 pH 7.5, 300 mM NaCl, 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.25 mM CdCl2 + 1.5% (w/v) n-dodecyl-β-D-maltoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Membrane fraction solubilized for 1 h at 4°C |
| Affinity chromatography | Immobilized metal affinity chromatography (IMAC) | HisPur Cobalt Resin (Thermo Fisher Scientific) | 20 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.3, 300 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.25 mM CdCl2, 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Purified in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) with CdCl2 to maintain metal-bound state |
| Size-exclusion chromatography | SEC | Superdex Increase 200 (GE Healthcare) | 10 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.3, 300 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.25 mM CdCl2, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | For cysteine variants, 1 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep/) added during purification but excluded in gel filtration buffer |

**Final sample**: Purified protein in gel filtration buffer


## Crystallization

### doi/10.1038##s41467-023-36048-4

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | Purified BbZIP at 15 mg/ml |
| Lipid | Monoolein |
| Protein-to-lipid ratio | 2:3 (protein:monoolein, v/v) |
| Temperature | 21°C |
| Growth time | 1-2 weeks |
| Cryoprotection | Crystals flash-frozen in liquid nitrogen |
| Notes | Stick-shaped crystals appeared after ~1 week; crystallization at low pH (~4.0) was necessary to obtain the apo state |


## Biological / Functional Insights

### Elevator-Type Transport Mechanism

BbZIP operates via an elevator-type mechanism where Domain I (α1/α4/α5/α6) slides as a rigid body ~8 Å vertically against Domain II (α2/α3/α7/α8). The binuclear metal centre (BMC) is carried by Domain I, and its vertical translocation exposes the transport site alternately to each side of the membrane. Metal release disassembles the primary M1 site, weakening interdomain interactions and facilitating the conformational switch. A repeat-swap homology model of the outward-facing conformation (OFC) was experimentally validated by cysteine accessibility assays and Hg2+-mediated chemical crosslinking.

### Two-Domain Architecture

The apo state structure revealed that BbZIP comprises two structurally independent domains. Evolutionary covariance analysis confirmed this architecture, showing far more intradomain than interdomain predicted interactions. The greasy domain interface is lined with conserved small residues (Ala, Gly, Ser); mutation of these to bulky amino acids in human ZIP4 severely impaired transport, supporting the requirement for a smooth sliding interface typical of elevator transporters.

### Dimerization

BbZIP forms a dimer mediated by Domain II (the scaffold domain) in both detergent and native membranes. [Cryo Em](/xray-mp-wiki/methods/structure-determination/cryo-em/) in Amphipol A8-35 showed near-symmetrical dimer particles. The dimer appears dynamic, existing in a monomer-dimer equilibrium. Covariance analysis and cysteine crosslinking support a dimer interface involving α2 (Domain II of one protomer) and α8 (Domain II of the second protomer), with the scaffold domains forming a static dimeric base while the transport domains move independently.


## Cross-References

- [Elevator-type transport mechanism](/xray-mp-wiki/concepts/elevator-type-transport-mechanism/) — BbZIP is demonstrated to be an elevator-type transporter with rigid-body vertical sliding of the transport domain
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Referenced in the context of DDM
- [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) — Referenced in the context of Hepes
- [Peg](/xray-mp-wiki/reagents/additives/peg/) — Referenced in the context of Peg
- [Cryo Em](/xray-mp-wiki/methods/structure-determination/cryo-em/) — Referenced in the context of Cryo Em
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Referenced in the context of Imidazole
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Referenced in the context of Glycerol
- [TCEP](/xray-mp-wiki/reagents/additives/tcep/) — Referenced in the context of TCEP
