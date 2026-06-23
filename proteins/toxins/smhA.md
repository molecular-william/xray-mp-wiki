---
title: "SmhA from Serratia marcescens"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41598-021-85726-0]
verified: false
---

# SmhA from Serratia marcescens

## Overview

SmhA is the A component of the SmhABC tripartite alpha-pore-forming toxin (alpha-PFT) from Serratia marcescens MSU-97. SmhA shares structural similarity with the A components of other tripartite ClyA family alpha-PFTs such as NheA and AhlB. SmhA adopts a compact soluble structure with a beta-tongue motif that shields hydrophobic residues. Upon membrane binding, SmhA is proposed to undergo a conformational change from the soluble form to an extended helical pore form, providing the hydrophilic lining of the tripartite pore lumen. SmhA interacts with the SmhB component during pore assembly after formation of the SmhBC pro-pore complex.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41598-021-85726-0 | 7A26 | 2.98 A | P42 | Full-length SmhA with C-terminal 6xHis tag (SeMet) | -- |
| doi/10.1038##s41598-021-85726-0 | 7A27 | 2.57 A | P212121 | Full-length SmhA with C-terminal 6xHis tag | -- |

## Expression and Purification

- **Expression system**: E. coli BL21 DE3
- **Construct**: Full-length SmhA with C-terminal 6xHis tag, cloned into pET21a
- **Induction**: 1 mM IPTG at 16 C overnight
- **Media**: LB medium

### Purification Workflow

- **Expression system**: E. coli BL21 DE3
- **Expression construct**: SmhA with C-terminal 6xHis tag
- **Tag info**: C-terminal 6xHis tag

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Sonication | — | 50 mM Tris pH 8 | 3 x 20 s burst at 16000 nm lambda |
| Clarification | Centrifugation | — |  | 40,000 g for 15 min |
| Affinity chromatography | Ni-NTA | 5 ml Nickel Hi-trap column (GE Healthcare) | 50 mM Tris pH 8, 0.5 M NaCl | Elution with 0-1 M imidazole gradient |
| Size exclusion chromatography | SEC | Superdex 200 pg (GE Healthcare) | 50 mM Tris pH 8, 0.5 M NaCl | Pre-equilibrated with running buffer |


## Crystallization

### doi/10.1038##s41598-021-85726-0

| Parameter | Value |
|---|---|
| Method | [Sitting drop vapor diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) |
| Protein sample | SmhA at 7 mg/ml in 50 mM Tris pH8, 10 mM NaCl |
| Reservoir | SeMet: 0.1 M MES pH 6.5, 0.16 M CaCl2, 20% PEG 6000; S-Met: 0.2 M potassium nitrate, 20% PEG 3350 |
| Mixing ratio | 200 nl:200 nl |
| Temperature | 7 C |
| Cryoprotection | Mother liquor with additional 20% (v/v) ethylene glycol |
| Notes | Crystals grown in 96-well plates. SeMet structure solved by SAD at 2.98 A using CRANK2 pipeline. S-Met structure solved by molecular replacement at 2.57 A. Data collected at Diamond Light Source beamlines I03 and I04-1. |


## Biological / Functional Insights

### Structural similarity to tripartite ClyA family components

SmhA shares strong structural similarity with SmhB (PDB 6ZZ5, RMSD 2.9 A), NheA (PDB 4K1P, RMSD 3.2 A), AhlB (PDB 6GRJ, RMSD 3.3 A), Hbl-B (PDB 2NRJ, RMSD 2.8 A), and MakA (PDB 6DFP, RMSD 3.5 A). All share the same compact helical bundle tail domain and beta-tongue domain. The C-terminus shields hydrophobic residues of the beta-tongue, with differences in shielding mechanism across species.

### Predicted pore conformation

SmhA is predicted to undergo a conformational change from soluble beta-tongue to extended helical pore form, with two amphipathic helices 36 A in length formed from the head domain. These helices would cross the membrane and provide the hydrophilic lining of the tripartite pore, with hydrophobic and hydrophilic surfaces on opposite faces of the monomer.

### Intracellular loop in Gram-negative tripartite toxins

An intracellular loop between the two amphipathic helices (residues G208-A229) is present in all Gram-negative tripartite toxin A components but absent in Gram-positive Nhe/Hbl toxins, single-component ClyA, and bipartite YaxAB/XaxAB toxins. This loop may interact with intracellular components of the target cell.


## Cross-References

- [SmhB](/xray-mp-wiki/proteins/toxins/smhB/) — SmhB is the B component of the SmhABC tripartite alpha-PFT, interacting with SmhA during pore assembly
- [ClyA Cytotoxin](/xray-mp-wiki/proteins/toxins/clyA/) — Prototypical single-component alpha-PFT in the same ClyA family
- [Pore-Forming Toxins](/xray-mp-wiki/concepts/structural-mechanisms/pore-forming-toxins/) — SmhA is a component of a tripartite alpha-pore-forming toxin in the ClyA family
