---
title: Uracil:Proton Symporter UraA from Escherichia coli
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##cr.2017.83, doi/10.1038##nature11403]
verified: false
---

# Uracil:Proton Symporter UraA from Escherichia coli

## Overview

UraA from Escherichia coli is a uracil:proton symporter and a prototypical member of the nucleobase/ascorbate transporter (NAT) or nucleobase/cation symporter 2 (NCS2) family, which corresponds to the human solute carrier family SLC23. The protein consists of 14 transmembrane segments (TMs) organized into two distinct domains: a rigid core domain (TMs 1-4 and 8-11) and a flexible gate domain (TMs 5-7 and 12-14). UraA functions as a homodimer in the membrane, and dimerization is required for transport activity. The protein has been crystallized in both inward-open and occluded conformations, providing structural insight into the alternating access mechanism of SLC23 transporters.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##cr.2017.83 | not specified in paper text (refers to new structure) | 2.5 A | C2221 | Wild-type full-length UraA (residues 2-409) | uracil (occluded state) |
| doi/10.1038##nature11403 | 3QE7 | 3.2 A | not specified in paper text | Wild-type full-length UraA | beta-NG (inward-open state) |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Wild-type full-length UraA from E. coli strain O157:H7, cloned into pET21b vector. Monomeric mutants M1 (L366W & I374W) and M2 (A137W & I374W) and constitutive dimer construct (two UraA molecules connected by 12-aa GlySer linker) also expressed.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | French press cell lysis and ultracentrifugation | not specified | 25 mM Tris-HCl pH 8.0, 150 mM NaCl + not specified | Cells disrupted by French press at 10000-15000 p.s.i., membrane fractions collected at 150000 x g for 1 h |
| Solubilization | Detergent solubilization | not specified | 25 mM Tris-HCl pH 8.0, 150 mM NaCl + 1.5% DDM | 1.5% DDM (Anatrace) incubated for 1 h at 4 C |
| Affinity purification | Ni-NTA affinity chromatography | Ni-NTA (Qiagen) | 25 mM Tris-HCl pH 8.0, 150 mM NaCl, 30 mM imidazole, 1 mM uracil, 0.2% DM + 0.2% DM | Resin washed three times with wash buffer, eluted with 250 mM imidazole |
| Size exclusion chromatography | SEC | Superdex-200 10/30 (GE Healthcare) | 25 mM Tris-HCl pH 8.0, 150 mM NaCl, 1 mM uracil, indicated detergents + indicated detergents (DDM, LDAO, NG, FC-9, FC-11) | Peak fractions collected for crystallization or biochemical characterizations |


## Crystallization

### doi/10.1038##cr.2017.83

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | Wild-type full-length UraA in detergent |
| Reservoir | 1.2% Fos-Choline 9 (FC-9) and 0.06% Fos-Choline 11 (FC-11) |
| Temperature | 18 C |
| Growth time | not specified |
| Notes | Crystals grew in space group C2221. Data collected at BL41XU, SPring-8. Structure solved by W-SAD phasing at 2.5 A resolution. |


## Biological / Functional Insights

### Dimeric assembly and monomer-dimer equilibrium

UraA forms a homodimer in the crystal structure wherein the gate domains are sandwiched by two core domains. The dimerization interface involves approximately 2400 A^2 buried surface area, mediated through the gate domains with extensive hydrophobic residues on TMs 5/12/13. Size exclusion chromatography in multiple detergents (DDM, LDAO, NG) shows UraA elutes in two peaks, suggesting equilibrium between monomer and dimer. Crosslinking and static light scattering confirm that wild-type UraA exists in monomer-dimer equilibrium, while monomeric mutants (M1, M2) remain monomeric and the constitutive dimer remains dimeric.

### Dimerization is required for transport activity

Monomeric mutants M1 (L366W & I374W) and M2 (A137W & I374W) bind uracil with similar affinity to wild-type, confirming correct folding. However, transport activity is nearly abolished in the monomeric mutants in cell-based uracil uptake assays. The constitutive dimer exhibits 70% higher transport activity than wild-type. Intriguingly, dimers containing one functional and one loss-of-function protomer (E241A or H245A) show similar Km and Vmax to the constitutive dimer, suggesting one functional protomer is sufficient for transport.

### Conformational changes between inward-open and occluded states

Structural comparison between the inward-open (UraA_IO, PDB 3QE7) and occluded (UraA_Occ) conformations reveals pronounced relative motions between the core and gate domains. The core domain remains rigid while the gate domain undergoes inter- and intra-domain shifts. TM5 and TM12 rotate around an axis perpendicular to the core-gate domain interface and bend in the occluded state, with a more prominent kink in TM5. The periplasmic segment of TM5 moves towards the core domain while the cytoplasmic segment of TM12 is displaced away, resulting in the switch from occluded to inward-open state.

### Uracil coordination and proton coupling mechanism

Uracil is coordinated primarily by the core domain through H-bonds with Glu241, Glu290, and backbone amide groups of Phe73 and Gly289. Multiple water-mediated H-bonds were revealed at the improved 2.5 A resolution. A water molecule (Wat1) bridges H-bonds between Ser72 and Glu241 with the O4 group of uracil. Another water molecule (Wat2) is near Glu241 and His245. Molecular dynamics simulations suggest Glu241 and His245 play key roles in proton coupling: protonation of Glu241 leads to hydration of the substrate-binding site and disruption of the H-bond network, while protonation of His245 stabilizes the H-bond network.


## Cross-References

- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — UraA operates by alternating access between inward-open and occluded conformations
- [Elevator Mechanism](/xray-mp-wiki/concepts/elevator-mechanism/) — UraA core domain exhibits elevator-like movement relative to the dimeric gate domain
- [Rocker-Switch Mechanism](/xray-mp-wiki/concepts/rocker-switch-mechanism/) — Rocking bundle motions of gate domains contribute to alternating access in UraA
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for UraA membrane solubilization and purification
- [Lauryl Dimethylamine N-Oxide (LDAO)](/xray-mp-wiki/reagents/detergents/lDAO/) — Detergent used for SEC analysis of UraA oligomerization state
- [Uracil](/xray-mp-wiki/reagents/ligands/uracil/) — Substrate of UraA, binds in the occluded conformation
- [Fos-Choline 9 (FC-9)](/xray-mp-wiki/reagents/detergents/fos-choline-9/) — Detergent used for UraA crystallization
- [Substrate-Protonation Coupling](/xray-mp-wiki/concepts/substrate-protonation-coupling/) — UraA couples uracil transport to proton translocation
