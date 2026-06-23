---
title: "E. coli YebT Tube-like MCE Protein"
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2017.03.019]
verified: false
---

# E. coli YebT Tube-like MCE Protein

## Overview

YebT (also known as MAM7) is a periplasm-spanning MCE (mammalian cell entry) protein from Escherichia coli that forms an elongated tube-like hexameric barrel. YebT consists of seven tandem MCE domains that stack into seven hexameric rings, forming a ~570 kDa complex approximately 230 A long and 90 A in diameter. The structure spans the periplasmic space between the inner and outer membranes of Gram-negative bacteria, creating a continuous channel of sufficient length to directly transport lipids without the need for a periplasmic shuttle protein. YebT is anchored in the inner membrane via six transmembrane helices, with its C terminus extending up to 230 A away from the membrane.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2017.03.019 | 5UW8 | ~20 A (EMDB: EMD-8611) | not applicable | Full-length YebT (residues 1-440 approximately), with N-terminal transmembrane helices | none |

## Expression and Purification

- **Expression system**: E. coli Rosetta2 DE3
- **Construct**: yebST operon cloned into pBAD-His for bicistronic YebS-YebT co-expression with C-terminal 6xHis tag on YebT

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Emulsiflex-C3 cell disruptor | -- | 50 mM [TRIS](/xray-mp-wiki/reagents/buffers/tris) pH 8.0, 300 mM NaCl, 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) + -- | Membrane fraction prepared by ultracentrifugation |
| Solubilization | Membrane solubilization with detergent | -- | 50 mM [TRIS](/xray-mp-wiki/reagents/buffers/tris) pH 8.0, 300 mM NaCl, 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) + n-Dodecyl-beta-D-maltopyranoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm)) | YebT solubilized from membrane fraction |
| His-tag affinity purification | Metal affinity chromatography | [Ni-NTA Agarose Resin](/xray-mp-wiki/reagents/additives/nickel-nta) agarose | 50 mM [TRIS](/xray-mp-wiki/reagents/buffers/tris) pH 8.0, 300 mM NaCl, 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) (wash), 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) (elution) + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Full-length YebT purified; YebS co-expression construct but only YebT obtained in significant amounts |
| Gel filtration | Size-exclusion chromatography | Superdex 200 | 20 mM [TRIS](/xray-mp-wiki/reagents/buffers/tris) pH 8.0, 150 mM NaCl + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Hexameric YebT tube-like complex |


## Crystallization

No crystallization described.

## Biological / Functional Insights

### Seven-ringed tube architecture spanning the periplasm

YebT forms a ~570 kDa hexameric assembly of six copies of the YebT polypeptide,
each containing seven tandem MCE domains. The seven MCE domains stack into seven
hexameric rings, forming an elongated tube approximately 230 A long and 90 A in
diameter. The tube resembles other macromolecular barrels such as the proteasome,
ClpXP, and GroEL. A fuzzy density at one end likely corresponds to a detergent
micelle and the N-terminal transmembrane helices from each YebT chain. The C terminus
of YebT can extend up to 230 A from the inner membrane, spanning the ~225 A distance
between the inner and outer membranes in E. coli.

### Hexameric ring stacking determined by tandem MCE domains

Each ring of density in the YebT reconstruction exhibits apparent 6-fold symmetry
and is similar in overall size and shape to the hexameric ring formed by [E. coli MlaD MCE Protein](/xray-mp-wiki/proteins/mlaD).
Polyalanine MCE models derived from the [E. coli MlaD MCE Protein](/xray-mp-wiki/proteins/mlaD) hexamer fit well into each density
ring. The number of stacked rings corresponds directly to the number of tandem
MCE domains in the primary sequence: YebT has seven MCE domains yielding seven
rings. This suggests a modular assembly principle where the domain architecture
of an MCE protein determines the architecture of its hexameric assembly.

### Lipid transport without periplasmic shuttle

Unlike the Mla system which uses [E. coli MlaC Periplasmic Lipid-Binding Protein](/xray-mp-wiki/proteins/mlaC) as a soluble periplasmic lipid shuttle, YebT
creates a continuous channel directly spanning the periplasm. This allows YebT
to potentially transport lipids or other hydrophobic molecules directly between
the inner and outer membranes without requiring a separate carrier protein. YebT
may associate with the inner membrane protein YebS as part of a larger transport
complex.


## Cross-References

- [E. coli MlaD MCE Protein](/xray-mp-wiki/proteins/structural-adhesion/mlaD/) — YebT shares the same MCE domain fold; MlaD hexameric ring serves as structural template
- [E. coli PqiB Syringe-like MCE Protein](/xray-mp-wiki/proteins/structural-adhesion/pqiB/) — PqiB shares the same modular stacking principle but with only three MCE domains
- [E. coli MlaC Lipid-Binding Protein](/xray-mp-wiki/proteins/structural-adhesion/mlaC/) — MlaC shuttles lipids in the Mla system; YebT bypasses the need for a shuttle by direct spanning
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for YebT solubilization from membranes
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Used for Ni-NTA affinity chromatography
- [MCE Protein Family](/xray-mp-wiki/concepts/protein-families/mce-protein-family/) — YebT is a seven-domain MCE protein with unique tube-like architecture
- [Ni-NTA Agarose Resin](/xray-mp-wiki/reagents/additives/nickel-nta) — Entity mentioned in text
- [TRIS](/xray-mp-wiki/reagents/buffers/tris) — Entity mentioned in text
