---
title: Undecaprenyl Pyrophosphate Phosphatase (UppP/BacA) from Escherichia coli
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein]
sources: [doi/10.1038##s41467-018-03547-8]
verified: false
---

# Undecaprenyl Pyrophosphate Phosphatase (UppP/BacA) from Escherichia coli

## Overview

Undecaprenyl pyrophosphate phosphatase (UppP, also known as BacA) is a 30 kDa polytopic integral membrane protein from Escherichia coli that catalyzes the dephosphorylation of undecaprenyl pyrophosphate (C55-PP) to undecaprenyl phosphate (C55-P), recycling the essential lipid carrier for bacterial cell wall peptidoglycan biosynthesis. The crystal structure of UppP from E. coli (EcUppP) was determined at 2.0 Å resolution, revealing an unexpected inverted topology repeat with interdigitated reentrant helices that form the active site deep within the membrane bilayer. The structure establishes Ser27 as the catalytic nucleophile, with Glu21, Glu17, and Arg174 playing critical roles in the phosphatase mechanism. UppP belongs to the PAP2 (type II phosphatidic acid phosphatase) family and was first identified in a screen for bacitracin resistance genes. The structure reveals a dimeric arrangement with each monomer containing ten transmembrane helices and two reentrant helix-loop-helix motifs that coordinate substrate binding and catalysis within the membrane mid-plane. Remarkably, the UppP fold shares structural similarity with cross-membrane transporters (ZIP zinc transporter, MFS transporters, ClC transporter, and CitS symporter), suggesting a potential dual function as both a phosphatase and a flippase for the C55-P reaction product.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-018-03547-8 |  | 2.00 | C222 | Full-length EcUppP with N-terminal hexahistidine tag (removed by thrombin) | Monoolein |

## Expression and Purification

- **Expression system**: Escherichia coli C41 (DE3) (Sigma)
- **Construct**: Full-length UppP from E. coli K-12 (ATCC 10798) in pET28a vector with N-terminal hexahistidine tag and thrombin cleavage site
- **Notes**: Overexpressed in ZYP-5052 autoinduction media at 37°C for 3 h, then 27°C overnight

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1. Membrane preparation | Cell lysis by Emulsiflex-C5 homogenizer; membranes collected by ultracentrifugation at 200,000 × g for 1 h | — | 20 mM HEPES pH 7.5, 500 mM NaCl, 10% glycerol | Cells resuspended with lysozyme, DNaseI, MgCl2, and protease inhibitors |
| 2. Solubilization | Detergent solubilization for 1 h | — | 20 mM HEPES pH 7.5, 500 mM NaCl, 10% glycerol + 1% (w/v) N-dodecyl-β-D-maltopyranoside (DDM) | Insoluble material removed by centrifugation |
| 3. Ni-NTA affinity chromatography | Immobilized metal affinity chromatography | Ni-NTA Superflow (Qiagen) | 20 mM HEPES pH 7.5, 500 mM NaCl, 0.016% DDM; eluted with 250 mM imidazole | Column pre-equilibrated with 30 mM imidazole; washed with 60 mM imidazole |
| 4. Desalting and tag removal | Desalting and overnight thrombin cleavage | — | 20 mM HEPES pH 8.0, 150 mM NaCl, 0.016% DDM | Hexahistidine tag removed by thrombin |
| 5. Size-exclusion chromatography | Gel filtration | Superdex 200 Increase 10/300 GL | 20 mM HEPES pH 7.0, 150 mM NaCl, 0.016% DDM | Purified protein concentrated to 12 mg/mL using 50 kDa MWCO concentrator |


## Crystallization

### doi/10.1038##s41467-018-03547-8

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | Purified UppP at 12 mg/mL in 20 mM HEPES pH 7.0, 150 mM NaCl, 0.016% DDM |
| Lipid | Monoolein (Sigma), 2:3 (v/v) protein-to-lipid ratio |
| Temperature | 20°C |
| Notes | Initial crystals with 40% PEG 200, 100 mM NaCl, 100 mM LiSO4, 100 mM NaCitrate pH 5. Optimized crystals harvested using MicroMounts and frozen directly in liquid nitrogen. Mercury derivatized crystals: sixfold molar excess ethyl mercury phosphate incubated for 30 min at 4°C before LCP preparation. Crystals grown in 45% PEG 200, 150 mM MgCl2, 400 mM LiSO4, 100 mM NaCitrate pH 5. |


## Biological / Functional Insights

### Inverted topology repeat and interdigitated architecture

EcUppP adopts an interdigitated inverted topology repeat (IITR) fold, the first observation of this fold in an enzyme. The N-repeat (residues 1-150) and C-repeat (residues 151-273) are related by a pseudo-twofold symmetry axis parallel to the membrane plane. Each repeat contains a reentrant helix-loop-helix motif (inner arch) followed by three transmembrane helices (outer arch). The repeats interdigitate such that the N-repeat's inner arch pairs with the C-repeat's outer arch and vice versa, creating two structural domains.

### Reentrant helix active site architecture

The active site is formed by two antiparallel reentrant helix-loop-helix motifs (first: Glu17-Arg35, second: Gly171-Leu181) that create a positively charged basin at the bottom of an electronegative funnel. The reentrant helices insert from opposite sides of the membrane with their N-termini meeting at the membrane mid-plane where the pyrophosphate substrate is coordinated. This architecture creates an internalized active site accessible from the periplasmic side via a deep cleft.

### Ser27 catalytic nucleophile and SRS motif

Ser27 is unambiguously identified as the catalytic nucleophile based on the 2.0 Å structure and mutagenesis (S27A completely abrogates activity). Ser27 projects from the N-terminal end of helix α2 into the active site. It is part of a highly conserved SRS (Ser-Arg-Ser) motif in the second reentrant loop that shows similarity to the P-loop motif of dual specificity phosphatases (DUSPs). Arg174 in this motif coordinates and polarizes the phosphate moiety.

### Glu21 as catalytic base with Glu17 carboxyl-carboxylate pair

Glu21 forms a hydrogen bond (3.1 Å) with the Ser27 side chain hydroxyl and is positioned to act as the activating general base for both the nucleophilic attack and subsequent hydrolysis steps. Glu17 is located directly adjacent to Glu21, forming a carboxyl-carboxylate interaction (2.8 Å) that modulates Glu21's pKa for its general base role. This carboxyl-carboxylate pair is a functionally important catalytic feature.

### His30 structural role and metal-dependent activity

His30, previously proposed as the catalytic nucleophile, actually plays a purely structural role. It forms hydrogen bonds with the backbone carbonyls of Val25 and Ser26 to stabilize the 3_10 helical nature of the N-terminal region of α2, and with Tyr260 to provide structural stabilization between α2 and α10. His30Ala reduces activity due to destabilization rather than loss of catalytic function. UppP activity is metal-dependent with strong preference for Mg2+ and Ca2+, with a putative cation-binding site coordinated by Ser173, Ser175, and backbone carbonyls.

### Structural similarity to cross-membrane transporters

DALI search revealed structural similarity to the ZIP zinc transporter (Z-score 4.1), MFS multidrug transporter MdfA (Z-score 4.1), ClC chloride transporter (Z-score 3.6), and CitS sodium-dependent citrate symporter (Z-score 3.5). These transporters share the inverted repeat topology and reentrant helical regions. The similarity to the ClC transporter is particularly notable as ClC uses reentrant helices to coordinate Cl- anions, analogous to how UppP coordinates the pyrophosphate moiety of C55-PP.

### Potential flippase function

The shared structural features with transporters — particularly the interlocked inverted repeat that enables alternating access — raise the intriguing possibility that UppP not only functions as a C55-PP phosphatase but also plays a role in recycling the C55-P product back across the membrane. A hydrophobic pocket formed by amphipathic helix α3b at the cytoplasmic interface may bind the C55 hydrophobic tail. Similar structural characteristics are observed in the MurJ lipid II flippase, which also binds lipidic substrates.


## Cross-References
