---
title: Na+/H+ Antiporter NapA from Thermus thermophilus
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature12484]
verified: false
---

# Na+/H+ Antiporter NapA from Thermus thermophilus

## Overview

NapA from Thermus thermophilus is a Na+/H+ antiporter belonging to the CPA2 clade of the monovalent cation proton antiporter (CPA) superfamily. It catalyzes the electrogenic exchange of Na+ (or Li+) for H+ across the membrane, playing a critical role in intracellular pH homeostasis and sodium concentration regulation. The protein consists of 13 transmembrane helices organized into a core domain (helices 1-6) and a dimerization domain (helices -1 and 7-12), forming a homodimer in the membrane. NapA was crystallized in an outward-facing conformation at 3.0 A resolution, revealing a negatively charged extracellular cavity with the strictly conserved aspartate residue (Asp 157) positioned for ion binding. The structure supports a two-domain elevator/rocking bundle mechanism for alternating access, with the core domain rotating approximately 20 degrees against the dimerization domain during transport.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature12484 | not specified | 3.0 A | C222_1 | Full-length NapA from Thermus thermophilus (Uniprot Q72IM4), GFP-His8 fusion with TEV cleavage site | zinc (2 ions per monomer) |

 - R-work not specified%, R-free not specified%; Data collection: X-ray diffraction at 3.0 A resolution, solved by multiple isomorphous replacement with anomalous scattering (MIRAS) with mercury and selenomethionine derivatization, multi-crystal averaging

## Expression and Purification

- **Expression system**: Escherichia coli Lemo21(DE3)
- **Construct**: Full-length NapA from Thermus thermophilus (Uniprot Q72IM4) cloned into pWaldoGFPe vector as GFP-His8 fusion; expressed with IPTG induction at 25 C overnight

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Cell lysis and membrane fractionation | not specified | 1x PBS, 150 mM NaCl + not specified | Membranes isolated from 5 L E. coli cultures |
| Solubilization | Detergent solubilization | not specified | 1x PBS, 150 mM NaCl, 10 mM imidazole + 1% DDM | Solubilized in 1% DDM for 2 h |
| Ni-NTA affinity capture | Ni-NTA affinity chromatography | Ni-NTA Superflow resin | 1x PBS, 150 mM NaCl, 20 mM imidazole, 0.1% DDM + 0.1% DDM | Washed with 20 mM and 50 mM imidazole |
| Elution | Ni-NTA affinity elution | Ni-NTA Superflow resin | 1x PBS, 150 mM NaCl, 250 mM imidazole, 0.6% NM + 0.6% NM | Eluted in NM-containing buffer |
| Tag cleavage | TEV protease cleavage | not specified | 20 mM Tris-HCl pH 7.5, 150 mM NaCl, 0.5% NM + 0.5% NM | Dialyzed overnight with His6-tagged TEV protease |
| Second Ni-NTA purification | Ni-NTA affinity chromatography | Ni-NTA His-Trap column | 20 mM Tris-HCl pH 7.5, 150 mM NaCl, 0.5% NM + 0.5% NM | Cleaved NapA collected in flow-through |


## Crystallization

### doi/10.1038##nature12484

| Parameter | Value |
|---|---|
| Method | Vapour diffusion |
| Protein sample | Cleaved NapA in NM detergent |
| Reservoir | not specified |
| Temperature | not specified |
| Growth time | not specified |
| Notes | Crystals grown at pH 7.8 or 9.0; data collected at Diamond Light Source I02, I03 and ESRF ID 23-1, 23-2; protein derivatized with 2.5 mM mercury acetate; structure solved by MIRAS with multi-crystal averaging at 3.0 A resolution in space group C222_1; crystals contain 4 molecules in asymmetric unit; 2 zinc ions bound per monomer on periplasmic surface |


## Biological / Functional Insights

### Two-domain elevator mechanism for alternating access

The NapA structure reveals a two-domain architecture with a core domain (helices 1-6) and a dimerization domain (helices -1 and 7-12). The core and dimerization domains are in different positions compared to the inward-facing NhaA structure, with a 20-degree rotation of the core domain relative to the dimerization domain. This rotation opens a negatively charged cavity to the extracellular side, allowing access to the strictly conserved aspartate (Asp 157) that coordinates ion binding. The elevator movement carries the substrate-binding domain across the membrane, resembling the mechanism seen in the glutamate transporter GltPh and the bile acid sodium symporter ASBT_NM.

### Dimer assembly and dimerization interface

NapA purifies as a homodimer with an extensive interface burying 1,800 A^2 of surface area. The dimer has a crystallographic two-fold operator approximately parallel to the transmembrane helices, formed by tight hydrophobic helix-helix packing between TM-1 on one monomer and TM7 on the other, with additional contacts between the ends of TM2 and TM9. NapA lacks the beta-hairpin domain present in NhaA that mediates extracellular dimer contacts; instead, the dimer interface resembles that modeled in the NhaP1 electron crystallography structure.

### Ion-binding site and conserved residues

The substrate-binding cavity is open to the extracellular side and is negatively charged, lined with glutamate residues. Near the base of the cavity are two highly conserved aspartates, Asp 156 and Asp 157, located on TM5. Asp 157 is strictly conserved and ideally positioned for binding both protons and sodium ions. Lys 305 (TM10) forms a salt bridge with Asp 156 in the outward-facing state. Mutation of Glu 333 (TM11b) decreased Na+ affinity (>15-fold) and Lys 305 mutation decreased both Na+ and Li+ affinity (>20-fold), confirming their functional importance.


## Cross-References

- [Na+/H+ Antiporter NhaA from Escherichia coli](/xray-mp-wiki/proteins/nhaa/) — Structural homologue and comparison protein; inward-facing NhaA structure used for alternating access model
- [Elevator Mechanism](/xray-mp-wiki/concepts/elevator-mechanism/) — NapA provides structural evidence for the elevator transport mechanism
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — NapA operates by alternating access between outward-facing and inward-facing states
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for NapA membrane solubilization at 1%
- [n-Nonyl-beta-D-maltopyranoside (NM)](/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-maltopyranoside/) — Used for NapA elution and purification at 0.6% and 0.5%
