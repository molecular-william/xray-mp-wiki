---
title: "Gloeobacter Rhodopsin (GR) from Gloeobacter violaceus"
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41598-019-47445-5]
verified: false
---

# Gloeobacter Rhodopsin (GR) from Gloeobacter violaceus

## Overview

Gloeobacter rhodopsin (GR) is a light-driven proton pump from the
cyanobacterium Gloeobacter violaceus PCC 7421, which lacks thylakoid
membranes. GR is a microbial rhodopsin with seven transmembrane helices
and all-trans-retinal covalently bound via a protonated Schiff base to
Lys257. It belongs to the XR-type subgroup of eubacterial proton pumps
and features extended helices A, B and G, a 3-omega motif (Phe38, Trp95,
Tyr106), and a flipped B-C loop with antiparallel beta-sheet structure.
GR has carotenoid-binding capability similar to xanthorhodopsin (XR)
and shows pH-dependent pentameric oligomerization. Under specific
conditions, GR exhibits an inverted proton flux, an optogenetically
relevant feature. The crystal structure was solved at 2.0 Angstrom
resolution from crystals grown in bicelles.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41598-019-47445-5 | 6NWD | 2.0 | C 2 2 2 1 | Full-length GR with C-terminal 6xHis tag | All-trans retinal (chromophore) |

## Expression and Purification

- **Expression system**: Escherichia coli C43(DE3)
- **Construct**: Full-length GR with C-terminal 6xHis tag

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1. Solubilization | Detergent solubilization | — | 1.0% n-Octyl-beta-D-glucopyranoside (OG) or n-dodecyl-beta-D-maltoside (DDM) | Solubilization at room temperature; ultracentrifugation at 100,000 x g to remove unsolubilized material |
| 2. Affinity chromatography | Immobilized metal affinity chromatography (IMAC) | TALON Co2+ column |  | Eluted by lowering pH |
| 3. Size-exclusion chromatography | Gel filtration | Superdex 200 10/300 GL | 20 mM HEPES pH 7.5, 300 mM NaCl + 1.0% OG or 0.04% DDM |  |


## Crystallization

### doi/10.1038##s41598-019-47445-5

| Parameter | Value |
|---|---|
| Method | Bicelle crystallization (hanging drop) |
| Protein sample | Purified GR at ~15 mg/mL in 1% OG |
| Temperature | Room temperature |
| Growth time | Several weeks |
| Notes | GR in 1% OG mixed with 24% (w/v) DMPC:CHAPSO bicelles at 1:2 ratio (final 8% bicelles). Plate-like crystals grown at pH 3.4 in the dark. X-ray data collected at APS beamline 23ID-D with Pilatus 6M detector. |


## Biological / Functional Insights

### Overall structure of GR and relationship to XR

GR has overall similarity to xanthorhodopsin (XR, RMSD 1.69 Angstrom) with seven transmembrane helices. Like XR, GR has a B-C loop with antiparallel beta-sheet oriented towards helices A and B (flipped orientation), extended helices A, B and G, and a 3-omega motif (Phe38/Trp95/Tyr106) that tethers the B-C loop. The extracellular side of TM helices A, E and G are slightly tilted inward compared to XR.

### Hydrogen bonding network in XR-type proton pumps

GR has an Asp121-His87 pair as the Schiff base counterion (similar to XR and TR), confirming this as a conserved feature in XR-type proton pumps and proteorhodopsins. GR lacks the Glu194/Glu204 pair of BR; instead, a hydrogen-bonded network connecting Arg118, Gln246, and Asp115 is established, with Asp115 potentially serving as the proton donor for proton release.

### pH-dependent pentameric oligomerization

DEER-EPR spectroscopy revealed that GR forms pentamers at pH 8.0 and monomers at pH 3.0 in DDM micelles. Two characteristic DEER distance peaks at 19 Angstrom and 29 Angstrom matched the expected distances from a pentameric model. His87 on helix B is proposed to play a key role in the protomer interacting surface, with the His87-Asp121 interaction disrupted at low pH.

### Structural determinants of oligomerization in bacterial pumps

The paper proposes a new classification of bacterial pumps based on the relationship between oligomerization states and conserved structural determinants. Eubacterial pumps with extended helices, 3-omega motif, and flipped B-C loop (XR-type: GR, XR, TR, KR2, CIR) form pentamers. Those with extended helices but lacking the 3-omega motif (proteorhodopsins: BPR, GPR, ESR) form pentamers/hexamers. Archaeal rhodopsins and trimeric eubacterial rhodopsins lack both features and form trimers exclusively.


## Cross-References

- [3 Omega Motif in Microbial Rhodopsins](/xray-mp-wiki/concepts/structural-mechanisms/3-omega-motif/) — GR has a conserved 3-omega motif (Phe38, Trp95, Tyr106) essential for B-C loop orientation
- [Microbial Rhodopsins](/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/) — GR is a microbial rhodopsin; the paper provides structural basis for function and oligomerization
- [Proton Pump Mechanism in Bacteriorhodopsin](/xray-mp-wiki/concepts/transport-mechanisms/proton-pump-mechanism/) — GR is a light-driven proton pump with a distinct hydrogen bonding network compared to BR
- [Xanthorhodopsin (XR)](/xray-mp-wiki/proteins/rhodopsins/xanthorhodopsin/) — GR is structurally most similar to XR (RMSD 1.69 Angstroms) and shares the XR-type proton pump features
- [Bacteriorhodopsin (bR)](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — Compared with BR (RMSD 3.33 Angstroms) to highlight structural differences in hydrogen bonding network and oligomerization
