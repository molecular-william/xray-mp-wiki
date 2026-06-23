---
title: "Ks-Amt5 Ammonium Sensor Histidine Kinase from Candidatus Kuenenia stuttgartiensis"
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-017-02637-3]
verified: false
---

# Ks-Amt5 Ammonium Sensor Histidine Kinase from Candidatus Kuenenia stuttgartiensis

## Overview

Ks-Amt5 (gene locus kust_3690) from the anammox bacterium "Candidatus Kuenenia stuttgartiensis" is a unique bifunctional membrane protein that combines an N-terminal ammonium transporter (Amt) domain with a C-terminal histidine kinase (HK) domain. Unlike canonical Amt/Rh family transporters that mediate ammonium uptake, Ks-Amt5 has been repurposed as an ammonium sensor/transducer. The Amt domain retains the conserved structural features of the Amt/Rh fold but contains a novel high-affinity ammonium binding site within the membrane core that is absent in assimilatory Amt proteins. The HK domain autophosphorylates at His406 in a manner modulated by ammonium binding to the Amt domain, enabling downstream signaling. The crystal structure of the Amt domain was determined at high resolution (PDB 6EU6), while the HK domains exhibited structural disorder in the crystal lattice.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-017-02637-3 | 6EU6 | 2.90 | P1 | Ks-Amt5 Amt domain (residues M1-A408) | NH4+ |

## Expression and Purification

- **Expression system**: E. coli C43(DE3)
- **Construct**: Full-length Ks-Amt5 with C-terminal His6-tag
- **Notes**: Also produced isolated Amt domain (residues M1-A408) and isolated HK domain (residues L426-K679) constructs

### Purification Workflow

- **Expression system**: E. coli C43(DE3)
- **Expression construct**: Full-length Ks-Amt5 with C-terminal His6-tag
- **Tag info**: C-terminal His6-tag (via LE linker)

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Ultracentrifugation | — |  | Cell membranes isolated after cell disruption |
| Solubilization | Detergent solubilization | — | n-Decyl-β-D-maltopyranoside (DM) | Protein solubilized from membranes |
| Affinity chromatography | Ni-NTA affinity chromatography | — |  | Standard Ni-NTA purification |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex 200 | 0.09% CYMAL-5 | SEC in buffer containing 0.09% CYMAL-5. Protein eluted as a trimer. |

**Final sample**: Purified Ks-Amt5 in SEC buffer with 0.09% CYMAL-5
**Yield**: Not specified
**Purity**: >95% by SDS-PAGE


## Crystallization

### doi/10.1038##s41467-017-02637-3

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified Ks-Amt5 in 0.09% CYMAL-5 |
| Notes | Crystals grew in space group P1. The Amt domain (residues M1-A408) formed crystal contacts; the HK domains were structurally disordered. |


## Biological / Functional Insights

### Repurposed ammonium transporter as a signal transducer

Ks-Amt5 represents the prototype of a modular sensor-transducer system that evolved from a ubiquitous ammonium transporter into a specific receptor for NH4+ cations. The Amt domain initiates a transport cycle at the selectivity filter but diverts two substrate cations into a high-affinity binding site within the membrane core, triggering conformational changes that modulate the fused histidine kinase domain.

### Novel high-affinity ammonium binding site

A unique cation-binding site situated within the membrane (~10 Å from the membrane boundary) coordinates two ammonium cations through a network of residues: Q24, E31 (helix h1), N47, D50, T51 (helix h2), and T109, T112 (helix h4). Only two acidic residues (E31 and D50) provide charge compensation. The binding geometry with five ligands per cation and short bond distances (2.2-2.4 Å) is distinct from octahedral Na+ coordination.

### Trimeric architecture with trimeric HK association

Ks-Amt5 elutes as a trimer in SEC, consistent with the strictly trimeric architecture of all Amt family members. The association of HK modules in a trimeric protein core is unprecedented, as most known HKs function as dimers. The elongated loop 5 (G186-N205, 19 residues) in the Amt domain is substantially longer than the 10-12 residues found in other Amt/Rh family members and is positioned near the C-terminus of the neighboring monomer, suggesting a mechanistic coupling between the two domains.

### Ammonium-dependent modulation of kinase activity

The in vitro kinase activity of full-length Ks-Amt5 shows strong modulation by NH4+ concentration: phosphorylation levels increase steeply at low NH4+ concentrations, followed by a decrease at high concentrations. This biphasic response is consistent with a sensor optimized for detecting low external ammonium levels. The isolated HK domain is insensitive to NH4+, confirming that the Amt domain mediates signal reception.

### Loss of transport function

Unlike canonical Amt transporters that conduct NH3, Ks-Amt5 does not translocate ammonium/methylammonium ions efficiently. The translocation pathway is obstructed by bulkier side chains (F27, Y30, F34) in helix h1 compared to Af-Amt1 (V23, F26, M30), and by a ~0.8 Å shift of the His pair (H171, H326) into the channel. This arrangement leaves the selectivity filter intact but prevents NH4+ from traversing the membrane.


## Cross-References

- [Rh/Amt/MEP Protein Family](/xray-mp-wiki/concepts/protein-families/rh-amt-mep-protein-family/) — Ks-Amt5 is a member of the Amt/Rh family with conserved structural features
- [Two-Component Signaling System (TCS) in Membrane Sensors](/xray-mp-wiki/concepts/signaling-receptors/two-component-signaling-system/) — Ks-Amt5 functions as an ammonium sensor histidine kinase, a novel TCS architecture
- [Ammonium Transporter AmtB (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/amt-b/) — Structural comparison with canonical Amt transporter
- [Amt-1 ammonium transporter from Archaeoglobus fulgidus](/xray-mp-wiki/proteins/other-ion-channels/a-fulgidus-amt1/) — Structural comparison; Ks-Amt5 Amt domain aligns with 1.2 Å RMSD to Af-Amt1
