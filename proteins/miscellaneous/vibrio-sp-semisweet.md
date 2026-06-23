---
title: Vibrio sp. SemiSWEET
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature13670]
verified: false
---

# Vibrio sp. SemiSWEET

## Overview

Vibrio sp. [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/semisweet/) is a bacterial sugar transporter from the [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/semisweet/) family found in Vibrio sp. N418. It is among the smallest characterized transporters, consisting of a single three-helix bundle per monomer that forms symmetric parallel dimers to generate the translocation pathway. Vibrio sp. [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/semisweet/) crystallized in an outward-open conformation at 1.70 Å resolution, providing high-resolution insight into the [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/semisweet/) transport mechanism.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature13670 | -- | 1.70 | I4122 | Full-length Vibrio sp. N418 [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/semisweet/) with C-terminal His-tag | -- |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Full-length Vibrio sp. N418 [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/semisweet/) with C-terminal 3C protease site and His-tag
- **Induction**: 0.2 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/), 22 C overnight

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Sonication | -- | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl | Pelleted cells resuspended and lysed by sonication |
| Solubilization | Detergent solubilization | -- | Cell lysate supernatant + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) (2% w/v) | Solubilized for 2 hours at 4 C; debris removed by centrifugation at 16,000 rpm |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Cobalt [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | HisPur Cobalt Resin | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | His-tag cleaved with [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) |
| Size-exclusion chromatography | Size-exclusion chromatography | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | 10 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Peak fractions pooled, concentrated, flash-frozen in liquid nitrogen, stored at -80 C |


## Crystallization

### doi/10.1038##nature13670

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase |
| Protein sample | Vibrio sp. [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/semisweet/) reconstituted into [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) (1:1.5 protein:lipid) |
| Temperature | 20 C |
| Notes | Crystals appeared within 2 days; grew to full size in about 1 week |


## Biological / Functional Insights

### Symmetric parallel dimer architecture

Two [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/semisweet/) monomers form symmetrical parallel dimers, generating the translocation pathway. The dimer interface is extensive, encompassing approximately 1,970 Å². The majority of non-packing hydrophilic residues within the membrane point to the center of the dimer interface, compatible with a putative translocation route at the interface. The dimer remains stable during SDS-PAGE, indicating stable assembly in solution.

### Outward-open conformation with solvent-filled cavity

Vibrio sp. [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/semisweet/) adopts an outward-open conformation with a solvent-filled cavity between the two protomers at the central two-fold axis. The cavity transverses approximately halfway across the membrane and is completely separated from the lipid bilayer by the surrounding six transmembrane helices but remains accessible from the extracellular side. The cavity measures 9.2 Å at the narrowest point, sufficient for small molecule diffusion. W59 and N75 are the only two invariant residues across 66 analyzed [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/semisweet/) sequences, strategically positioned at the center of the cavity to form a putative binding pocket.

### Rocking-type transport mechanism

Vibrio sp. [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/semisweet/) and L. biflexa [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/semisweet/) represent outward-open and occluded conformations respectively, indicating a rocking-type movement during the transport cycle. The dimer interface of Vibrio sp. [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/semisweet/) opens more towards the extracellular side than L. biflexa [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/semisweet/) and is approximately 10 Å wider at the extracellular surface, achieved mainly through a 10-degree rotation of the protomer around the part near the intracellular membrane surface.

### PQ motif and dimer interface stabilization

The conserved PQ-dipetide motif is embedded in the membrane and is part of TM1, not positioned in a loop as previously assumed. The CO and NH moieties of the side chain amide group of Q29 form hydrogen bonds with the NH and CO from two consecutive backbone amides immediately N-terminal to TM2 of the other protomer, bringing the L1-2 loop to the dimer interface and stabilizing its conformation. The proline preceding glutamine induces a kink in the helix, increasing flexibility of the transmembrane helix.


## Cross-References

- [LbSemiSWEET from Leptospira biflexa](/xray-mp-wiki/proteins/miscellaneous/lbsemisweet/) — Related bacterial SemiSWEET crystallized in occluded state at 2.4 Å
- [TySemiSWEET from Thermotoga yellowstonii](/xray-mp-wiki/proteins/miscellaneous/tysemisweet/) — Another bacterial SemiSWEET that transports sucrose
- [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/semisweet/) — Vibrio sp. SemiSWEET is a member of the SemiSWEET family
- [SWEET Transporter Family](/xray-mp-wiki/concepts/sweet-transporter/) — SemiSWEETs are bacterial homologues of SWEET transporters
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — Vibrio sp. SemiSWEET undergoes alternating access transport
- [Rocker-Switch Mechanism](/xray-mp-wiki/concepts/rocker-switch-mechanism/) — SemiSWEETs operate via rocking-type movement
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for solubilization and purification
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid used in lipidic cubic phase crystallization
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [IPTG](/xray-mp-wiki/reagents/additives/iptg/) — Additive used in purification or crystallization buffers
