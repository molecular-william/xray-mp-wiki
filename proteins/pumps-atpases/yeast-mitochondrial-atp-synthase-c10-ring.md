---
title: "Yeast Mitochondrial ATP Synthase c10 Ring"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.2284]
verified: false
---

# Yeast Mitochondrial ATP Synthase c10 Ring

## Overview

The c10 ring is the membrane-embedded rotor component of the mitochondrial ATP synthase from Saccharomyces cerevisiae, consisting of ten c-subunits arranged in a ring. Each c-subunit comprises four helical fragments forming two transmembrane helices connected by a short loop and a 3_10 helix. The structure was determined in the open conformation, revealing asymmetric packing of the c-subunits with water-mediated inter-subunit interactions. The c-ring rotates relative to the stator a-subunit, driving ATP synthesis by translocating protons across the inner mitochondrial membrane. Conserved hydrophobic residues on the inner face of the ring are critical for ring stability and proper assembly.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nsmb.2284 | 3U2F |  |  | c10 ring (10 c-subunits, open conformation) | none |

## Expression and Purification

No purification described.

## Crystallization

No crystallization described.

## Biological / Functional Insights

### Open conformation of the c10 ring

The c10 ring was captured in the open conformation, revealing the asymmetric packing of its ten c-subunits. Each c-subunit consists of an N-terminal transmembrane span (residues 3-39) containing a 3_10 helix (residues 15-18), followed by a second 3_10 helix (residues 41-43), and a C-terminal transmembrane helix (residues 44-73). The N-terminal span features an H-bonded turn stabilized by a water molecule associated with Thr16, which bridges interactions between adjacent c-subunits. Conserved residues on the inner face of the ring — Ala14, Ala20, Ala24 (conserved in animals for c8 ring formation) and residues 10, 17, 28 — form hydrophobic contacts critical for ring stability. The B-factor distribution shows the lowest values in the core (18 for C-alpha of Ser42) and highest in flexible loops (50 for C-alpha of Phe74 in chain K).

### Simulations of the c10 ring in lipid and crystallization-mimetic environments

Molecular dynamics simulations using NAMD with the CHARMM27/CMAP force field were performed on the c10 ring embedded in a model phospholipid membrane (~239 lipids, ~17,500 water molecules, ~96,000 atoms total) and in a solution mimicking the crystallization buffer (70% [MPD](/xray-mp-wiki/reagents/additives/mpd/), 300 mM NaCl; 1,524 [MPD](/xray-mp-wiki/reagents/additives/mpd/) molecules, ~4,700 water molecules, ~60,000 atoms total). Simulations were carried out at 298 K and 1 atm using periodic boundary conditions and the Particle-Mesh-Ewald algorithm for electrostatic interactions.


## Cross-References

- [Yeast V1-ATPase](/xray-mp-wiki/proteins/pumps-atpases/yeast-v1-atpase/) — Component of the same ATP synthase complex; V1 is the soluble catalytic domain and c10 ring is the membrane-embedded rotor
- [MPD](/xray-mp-wiki/reagents/additives/mpd/) — Additive used in purification or crystallization buffers
