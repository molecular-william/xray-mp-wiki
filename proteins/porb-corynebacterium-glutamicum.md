---
title: Porin B (PorB) from Corynebacterium glutamicum
created: 2026-05-07
updated: 2026-05-07
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography, porin, bacterial]
sources: [doi/10.1016##J.JMB.2008.04.017]
---

# Porin B (PorB) from Corynebacterium glutamicum

## Overview

Porin B (PorB) is an alpha-helical porin from Corynebacterium glutamicum, a mycolata bacterium with a mycolic acid cell wall layer similar to the outer membrane of Gram-negative bacteria. PorB forms an anion-selective channel in the bacterial outer envelope. The crystal structure was determined at 1.8 A resolution (crystal form I) using a platinum derivative for phasing, with 16 independent molecular structures solved in four different crystal forms. The core structure consists of 70 residues forming four alpha-helices tied together by a disulfide bridge (Cys22-Cys81). The native channel is proposed to be a pentameric oligomer based on conductivity measurements and crystal packing analysis. This is the first reported alpha-helical porin in a bacterial outer envelope, as all other known porins from mycolata consist of beta-barrels.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##J.JMB.2008.04.017 | not specified (deposited; multiple PDB codes for 4 crystal forms) | 1.8 A (Form I), 2.9 A (Form II), 3.2 A (Form III), 4.2 A (Form IV) | P41212 (I), P6522 (II), P43212 (III), P6422 (IV) | Mature PorB (99 residues, 10,638 Da); 70-residue core (residues 18-87) defined in all forms | 42 Zn2+ ion sites; platinum derivative; cacodylate |

## Expression and Purification

- **Expression system**: Escherichia coli (recombinant expression as GST fusion)
- **Construct**: PorB fused to glutathione S-transferase (GST), cleaved with factor Xa protease; 3 additional N-terminal linker residues (Gly, Ile, Leu) retained

### Purification Workflow

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| GST affinity chromatography | GST affinity column (GE Healthcare) | Glutathione-Sepharose | Buffer A: 140 mM NaCl, 2.7 mM KCl, 10 mM Na2HPO4, 1.8 mM KH2PO4 pH 7.3, 0.1 mM PMSF, Benzonase | GST fusion protein expressed in E. coli; cleaved on-column with factor Xa (11 U per gram wet cells) in buffer B |
| Size-exclusion chromatography | S75-26/60 SEC column (GE Healthcare) | Sephacryl S-75 | 150 mM NaCl, 50 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/)-HCl pH 8.0 | Separated monomer (11 +/- 2 kDa, major peak) from dimer/trimer (29 +/- 3 kDa, minor peak); only monomer peak yielded analyzable crystals |
| Concentration and dialysis | Vivaspin concentrator (MWCO 3000), dialysis against water (MWCO 3500) | -- | Concentrated to 1.0-3.5 mg/mL; dialyzed against water at 4 C | Total yield ~0.5 mg per liter culture; purification performed without detergent |


## Crystallization

### doi/10.1016##J.JMB.2008.04.017

| Parameter | Value |
|---|---|
| Method | Sitting-drop and hanging-drop vapor diffusion |
| Protein sample | PorB monomer peak at 1.0-3.5 mg/mL |
| Reservoir | Multiple crystal forms with different conditions (Tables in paper) |
| Mixing ratio | not specified |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | Reservoir buffer with [MPD](/xray-mp-wiki/reagents/additives/mpd/) increased by 2% (v/v); shock-frozen in nitrogen at 100 K |
| Notes | Four crystal forms obtained from monomer peak material; dimer/trimer peak yielded only disordered crystals. Screens from Hampton Research, Jena Bioscience, and Emerald. |


## Biological / Functional Insights

### Pentameric channel model

The native PorB channel is proposed as a C5-symmetric pentamer based on conductivity measurements (0.7 nS), anion selectivity, and crystal packing analysis. Contact type C from crystal forms (polar interior, nonpolar exterior) was expanded from C2 to C5 symmetry. The channel is ~40 A long, matching the mycolic acid layer thickness. Arg42 defines the channel constriction. The channel is inactivated by citrate (chelating divalent cations) and by EDTA (~35 mM), suggesting the native channel is stabilized by divalent metal ion cross-links.

### Alpha-helical porin architecture

PorB represents a novel porin architecture: all four alpha-helices surround a nonpolar interior with a conserved disulfide bridge (Cys22-Cys81). The strictly conserved core residues (Cys22, Gly33, Leu44, Ala45, Ala75, Arg77, Ala78, Cys81, Gly82, Val84) maintain structural stability. The N- and C-terminal extensions (29 residues total) are highly variable in conformation across crystal forms but conserved in sequence, suggesting a role in oligomerization.


## Cross-References

- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — SEC used to separate monomer from dimer/trimer peaks
- [Cacodylate (Sodium Dimethylarsenate)](/xray-mp-wiki/reagents/buffers/cacodylate/) — Observed as bound ligand in crystal form I contact type C dimers alongside Zn2+ ion sites
