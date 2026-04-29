---
title: PorB (Porin B from Corynebacterium glutamicum)
created: 2026-04-28
updated: 2026-04-28
type: protein
tags: [channel, porin, membrane-protein, xray-crystallography]
sources: [doi/10.1016##J.JMB.2008.04.017]
---
layout: default

# PorB — Porin B from *Corynebacterium glutamicum*

## Overview

PorB is a putative α-helical porin from the mycolic acid-containing bacterium *Corynebacterium glutamicum*. It forms an anion-selective channel in the mycolic acid layer of the cell wall, which is a protective nonpolar barrier similar to the outer membrane of Gram-negative bacteria. This structure is notable as the first reported α-helical porin from a bacterial outer envelope — all previously known bacterial outer membrane porins are β-barrels.

## Structure Determination

- **Resolution**: 1.8 Å (Form I, highest resolution)
- **Space groups**: 4 different crystal forms:
  - Form I: P4₁2₁2, 1.8 Å, BESSY (Pt-SIRAS phasing)
  - Form II: P6₅22, 2.9 Å, SLS
  - Form III: P4₃2₁2, 3.2 Å, SLS (PHASER MR + Pt-MAD confirmative)
  - Form IV: P6₄22, 4.2 Å, SLS
- **Total structures**: 16 independent PorB molecules in 4 crystal packing arrangements
- **Phasing**: Form I — Pt derivative (K₂Pt(NO₂)₄), SIRAS with SHARP; Forms II/III/IV — molecular replacement
- **Refinement**: ARP/wARP + REFMAC5, TLS refinement (each monomer as TLS group)
- **Synchrotrons**: BESSY (Berlin) and SLS (Swiss Light Source)

## Protein Architecture

### Core Structure (Residues 18–87, 70 residues)

- **4 α-helices** surrounding a nonpolar interior
- **Disulfide bridge** between Cys22 and Cys81 — critical for structural stability
- **Amphiphilic surface**: polar residues face inward (channel), nonpolar residues face outward (membrane)
- **Strictly conserved residues**: Cys22, Gly33, Leu44, Ala45, Ala75, Arg77, Ala78, Cys81, Gly82, Val84

### N- and C-terminal Extensions

- 29 residues (positions 1–17 and 88–99) with variable conformations depending on crystal packing
- Rich in serines and asparagines — likely important for oligomerization
- Protrude without defined structure from the core
- Well-conserved within PorB and PorC groups across corynebacteria

## Oligomeric Channel Model

The native PorB is proposed to be a **pentamer (C₅ symmetry)** based on:

1. **Conductivity matching**: 0.7 nS measured; pentamer model gives 1.2 nS (within error)
2. **Anion selectivity**: Pentameric channel constriction at Arg42 matches anion selectivity
3. **Channel dimensions**: ~40 Å length, matches mycolic acid layer thickness
4. **Crystal contact type C**: Recurring C₂-symmetric crystal contact has polar interior + nonpolar exterior — expansion to C₅ gives correct channel architecture

### Intersubunit Stabilization

- Three intersubunit salt bridges (including Arg77)
- Two Ca²⁺ cross-links between subunits
- One intra-subunit Ca²⁺ between Glu53 and Glu68
- Interface area: 625 Å² per subunit interface

### Citrate Block Mechanism

- Native PorB is inactivated by ~100 mM citrate
- **Revised mechanism**: Citrate acts as a chelator, extracting Ca²⁺/Zn²⁺ cross-links that hold the channel together, causing collapse
- Supported by: numerous Zn²⁺ sites in crystal; EDTA (~35 mM) also inactivates channels in lipid bilayers

## Expression and Purification

- **Expression**: *E. coli* as GST (glutathione S-transferase) fusion protein
- **Cleavage**: Factor Xa on-column cleavage (4 h at 25°C)
- **Purification**: 
  - GST affinity column → Factor Xa cleavage → SEC (S75-26/60, GE Healthcare)
  - **No detergent used in purification** — unusual for a membrane protein
  - Two peaks observed: major monomer (~11 kDa), minor dimer/trimer (~29 kDa)
- **Yield**: ~0.5 mg per liter of culture medium
- **Concentration**: 1.0–3.5 mg/ml (monomer peak), 0.8–1.0 mg/ml (dimer/trimer peak)
- **Buffer**: 150 mM NaCl, 50 mM Tris-HCl pH 8.0

## Crystallization

- **Screens**: Hampton Research, Jena Bioscience, Emerald
- **Method**: Sitting-drop screening; hanging-drop for analyzable crystals
- **Detergent**: Required for crystallization (despite detergent-free purification) — specific detergents listed in paper Table 1 (image, not extracted)
- **Concentration**: 1.0–3.5 mg/ml (monomer peak gave crystallizable crystals)
- **Cryoprotection**: MPD (2-methyl-2,4-pentanediol) increased by 2% from reservoir concentration; shock-frozen at 100 K in N₂ stream

## Biological Context

- **Organism**: *Corynebacterium glutamicum* — industrial amino acid producer (L-glutamate, L-lysine, ~1 megaton/year)
- **Cell wall**: Mycolic acid layer (22–38 carbon atoms) — protective nonpolar barrier
- **Homologs**: PorA (cation-selective), PorH (cation-selective), PorC (anion-selective, homolog of PorB)
- **Medical relevance**: Corynebacteria include human pathogens (*C. diphtheriae*, *M. tuberculosis*, *M. leprae*)
- **Comparison**: *M. smegmatis* porin is a C₈-symmetric octamer forming a 16-stranded β-barrel (MspA) — different architecture from α-helical PorB

## Related Channels

- [acrB](/proteins/acrB/) — Tripartite multidrug efflux pump from *E. coli*
- [ion-channels](/concepts/ion-channels/) — General ion channel class

## Cross-References

- Channel-forming proteins in bacterial outer membranes
- [xray-crystallography](/methods/structure-determination/xray-crystallography/) — Structure determination method
- 2-methyl-2,4-pentanediol (MPD) — Cryoprotectant used for data collection
- [size-exclusion-chromatography](/methods/purification/size-exclusion-chromatography/) — Purification method (S75-26/60)
- [affinity-chromatography](/methods/purification/affinity-chromatography/) — GST affinity purification