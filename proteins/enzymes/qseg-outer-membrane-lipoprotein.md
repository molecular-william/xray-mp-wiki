---
title: QseG Outer Membrane Lipoprotein (E. coli)
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [membrane-protein, xray-crystallography, porin]
sources: [doi/10.1107##s2053230x23009123]
verified: false
---

# QseG Outer Membrane Lipoprotein (E. coli)

## Overview

QseG (also known as YfhG) is an outer membrane lipoprotein from enterohemorrhagic Escherichia coli (EHEC) that functions as part of the QseE/F/G three-component system regulating virulence. It is encoded by the qseG gene within the qseEF operon. QseG co-localizes with the histidine kinase QseE in the periplasmic space and is required for QseE/F activity. Crystal structures were determined at 2.3, 2.35, and 2.60 Å resolution from three different crystallization conditions. QseG consists of an N-terminal globular domain (α1-α6 plus a 3₁₀-helix) and a long C-terminal α7 helix that mediates dimerization via a left-handed coiled-coil-like structure. A disulfide bond forms between Cys56 and Cys80. The C-terminal region of α7 (residues 197-207) exhibits structural flexibility, attributed to polar amino acid substitutions at the hydrophobic coiled-coil interface. The negatively charged α7c region likely interacts with the positively charged surface of QseE.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1107##s2053230x23009123 |  | 2.30 | P2_1 | Periplasmic region (residues 56-209) of QseG from E. coli with N-terminal His-tag | None |
| doi/10.1107##s2053230x23009123 |  | 2.35 | P2_1 | Periplasmic region (residues 56-209) of QseG from E. coli | None |
| doi/10.1107##s2053230x23009123 |  | 2.60 | P2_12_12_1 | Periplasmic region (residues 56-209) of QseG from E. coli | None |

## Expression and Purification

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: QseG periplasmic region (residues 56-209) with N-terminal His-tag and TEV cleavage site in pET-28a

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell growth and lysis | E. coli cells grown at 17°C for 20 h after induction with 0.1 mM IPTG. Cells sonicated in buffer with protease inhibitors. | -- | 50 mM Tris-HCl pH 8.0, 200 mM NaCl, cOmplete Protease Inhibitor Cocktail | Centrifuged at 20,000g for 1 h at 4°C |
| Affinity chromatography | Supernatant loaded onto HiTrap TALON column | HiTrap TALON | 50 mM Tris-HCl pH 8.0, 200 mM NaCl | TEV protease added after elution for tag removal |
| Reverse affinity chromatography | Dialyzed sample loaded onto HisTrap column; flowthrough collected | HisTrap | 20 mM Tris-HCl pH 8.0, 300 mM NaCl |  |
| Size-exclusion chromatography | Purified on HiLoad 16/60 Superdex 200 | Superdex 200 | 20 mM Tris-HCl pH 8.0, 100 mM NaCl |  |


## Crystallization

### doi/10.1107##s2053230x23009123

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor-diffusion |
| Protein sample | 10 mg/mL QseG in 20 mM Tris-HCl pH 8.0, 100 mM NaCl |
| Reservoir | 0.08 M Mg acetate tetrahydrate, 0.1 M Na citrate pH 6.0, 14% (w/v) PEG MME 5000 |
| Temperature | 20°C |
| Cryoprotection | Soaked in crystallization solution supplemented with 20% ethylene glycol before flash-cooling in liquid nitrogen |
| Notes | Crystal condition 1. Also obtained in condition 2 (0.32 M LiCl, 0.1 M Na citrate pH 5.5, 14% PEG 4000) and condition 3 (0.1 M MgCl2, 0.1 M Tris pH 7.5, 13% PEG 8000). X-ray data collected at SPring-8 BL44XU with EIGER X 16M detector at 0.9 Å wavelength. |


## Biological / Functional Insights

### Coiled-coil structural polymorphism facilitates QseE interaction

QseG dimerizes through a left-handed coiled-coil formed by the α7 helices. Structural superposition of dimers from three different crystal conditions reveals significant polymorphism at the C-terminal region of the coiled-coil. Approximately one-quarter of the heptad-repeat interface positions are occupied by polar amino acids rather than hydrophobic residues, weakening the hydrophobic core and providing the flexibility needed for interaction with QseE.

### QseG is essential for full virulence

ΔqseG mutants of EHEC show reduced colony-forming units in infant rabbit models, and ΔqseG mutants of Citrobacter rodentium produce attenuated disease symptoms in mice. QseG is also essential for virulence in the fish pathogen Edwardsiella tarda, where it regulates haemolytic activity and invasion. QseG is conserved across multiple Enterobacteriaceae pathogens.


## Cross-References

- [QseE Periplasmic Sensor Domain](/xray-mp-wiki/proteins/enzymes/qsee-periplasmic-domain/) — QseG interacts with QseE in the periplasm to regulate virulence signaling
- [QseE/F/G Three-Component System](/xray-mp-wiki/concepts/miscellaneous/qse-efg-three-component-system/) — QseG is the outer membrane lipoprotein component of this system
