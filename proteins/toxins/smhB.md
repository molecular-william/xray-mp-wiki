---
title: SmhB from Serratia marcescens
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41598-021-85726-0]
verified: false
---

# SmhB from Serratia marcescens

## Overview

SmhB is the B component of the SmhABC tripartite alpha-pore-forming toxin (alpha-PFT) from Serratia marcescens MSU-97. SmhB undergoes a large-scale conformational change from a compact soluble form, with hydrophobic residues hidden within a beta-tongue motif, to an extended pore form with hydrophobic residues exposed in two transmembrane helices. The soluble SmhB structure was determined in two crystal forms, and the pore form was determined at 6.98 A resolution by molecular replacement. SmhB interacts with SmhC for membrane recognition and with SmhA to form the complete tripartite pore. Ten SmhB monomers assemble in two alternating conformations (type 1 and type 2) to form a ring with pseudo tenfold symmetry.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41598-021-85726-0 | 6ZZ5 | 1.84 A | P212121 | Full-length SmhB with C-terminal 6xHis tag | -- |
| doi/10.1038##s41598-021-85726-0 | 6ZZH | Not specified | P21 | Full-length SmhB with C-terminal 6xHis tag | -- |
| doi/10.1038##s41598-021-85726-0 | 7AOG | 6.98 A | C2 | Full-length SmhB with C-terminal 6xHis tag (pore form) | -- |

## Expression and Purification

- **Expression system**: E. coli BL21 DE3
- **Construct**: Full-length SmhB with C-terminal 6xHis tag, cloned into pET21a
- **Induction**: 1 mM IPTG at 16 C overnight
- **Media**: LB medium

### Purification Workflow

- **Expression system**: E. coli BL21 DE3
- **Expression construct**: SmhB with C-terminal 6xHis tag
- **Tag info**: C-terminal 6xHis tag

#### Steps

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
| Protein sample | SmhB at 14 mg/ml in 50 mM Tris pH8, 10 mM NaCl |
| Reservoir | 0.17 M ammonium sulfate, 25.5% PEG4000 |
| Mixing ratio | 100 nl:100 nl |
| Temperature | 16 C |
| Cryoprotection | Mother liquor with additional 20% (v/v) ethylene glycol |
| Notes | Crystals grown in 96-well plates. Soluble structure solved at 1.84 A (P212121). Second crystal form in P21. Pore form (7AOG) solved by molecular replacement using AhlB pore (PDB 6H2F) at 6.98 A. Data collected at Diamond Light Source beamline I04-1 (soluble) and I24 (pore). |


## Biological / Functional Insights

### Soluble to pore conformational change

SmhB undergoes a dramatic conformational change from a compact soluble form to an extended pore form. The beta-tongue substructure refolds to form extended hydrophobic helices (alpha3 and alpha4) that span the membrane. Two conserved latches involving a glutamine residue (Q32) on the N-terminal helix alpha1 that hydrogen bonds with the beta-sheet backbone of the beta-tongue, and a lysine-threonine interaction (K333-T78) between alpha2 and the C-terminal helix, stabilize the soluble form and are broken during pore transformation.

### Pore architecture

The SmhB pore contains ten monomers in two conformations (type 1 and type 2) that assemble into a ring with pseudo tenfold symmetry. This architecture matches the AhlB pore structure. The head domain undergoes large-scale refolding with the beta-tongue converting to extended hydrophobic helices for membrane insertion.

### Conserved binding interfaces

SmhB has two conserved binding interfaces: one for SmhC (around residues 95-123) and one for SmhA (around residues 289-308). Binding of SmhC breaks latches on SmhB, initiating the conformational change to pore form. The A component binding interface is around residues 57-71 in SmhA and 289-308 in SmhB, breaking latches on SmhA.


## Cross-References

- [SmhA](/xray-mp-wiki/proteins/toxins/smhA/) — SmhA is the A component of the SmhABC tripartite alpha-PFT, interacting with SmhB after SmhBC pro-pore formation
- [ClyA Cytotoxin](/xray-mp-wiki/proteins/toxins/clyA/) — Prototypical single-component alpha-PFT in the same ClyA family with similar beta-tongue to pore transformation
- [Pore-Forming Toxins](/xray-mp-wiki/concepts/structural-mechanisms/pore-forming-toxins/) — SmhB is a component of a tripartite alpha-pore-forming toxin in the ClyA family
