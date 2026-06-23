---
title: Uracil:Proton Symporter UraA from Escherichia coli
created: 2026-06-02
updated: 2026-06-09
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature09885, doi/10.1038##cr.2017.83, doi/10.1038##nature11403, doi/10.1038##s41467-024-51814-8]
verified: false
---

# Uracil:Proton Symporter UraA from Escherichia coli

## Overview

UraA from Escherichia coli is a [URACIL](/xray-mp-wiki/reagents/ligands/uracil/):proton symporter and a prototypical member of the nucleobase/ascorbate transporter (NAT) or nucleobase/cation symporter 2 (NCS2) family, which corresponds to the human solute carrier family SLC23. The first crystal structure of UraA (PDB 3QE7, 2.8 A resolution) revealed a novel structural fold with 14 transmembrane segments (TMs) organized into two inverted repeats, with a pair of antiparallel beta-strands between TM3 and TM10 that serve as an organizing center for the structure. The protein is spatially arranged into a rigid core domain (TMs 1-4 and 8-11) and a flexible gate domain (TMs 5-7 and 12-14). [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) binds at the interface between the two domains, coordinated mainly by residues from the core domain including Glu241, His245, and Glu290. Alternating access of the substrate is achieved through conformational changes of the gate domain relative to the core domain. UraA functions as a homodimer in the membrane, and dimerization is required for transport activity.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature09885 | 3QE7 | 2.8 A | P6_22 | Full-length UraA (residues 2-409) from E. coli strain O157:H7 cloned into pET21b vector with C-terminal His-tag; [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) bound | [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) |
| doi/10.1038##cr.2017.83 | not specified in paper text (refers to new occluded structure) | 2.5 A | C2221 | Wild-type full-length UraA (residues 2-409) | [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) (occluded state) |
| doi/10.1038##nature11403 | 3QE7 | 3.2 A | P6_22 | Wild-type full-length UraA | beta-NG (inward-open state) |
| doi/10.1038##s41467-024-51814-8 |  | 3.5 A |  | UraA(G320P) mutant in complex with synthetic [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) Sy45; wide inward-open conformation |  |
| doi/10.1038##s41467-024-51814-8 |  | 3.7 A |  | UraA(G320P) mutant in complex with synthetic [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) Sy45 with 1 mM [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) | [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Full-length UraA from E. coli strain O157:H7, cloned into pET21b vector with C-terminal His-tag. Monomeric mutants M1 (L366W & I374W) and M2 (A137W & I374W) and constitutive dimer construct (two UraA molecules connected by 12-aa GlySer linker) also expressed. For the original structure (nature09885), [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) was added at 1 mM when cells were induced and included in all purification buffers.

### Purification Workflow

*Source: doi/10.1038##nature09885*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | [French Press Cell Lysis](/xray-mp-wiki/methods/cell-lysis/french-press/) and ultracentrifugation | not specified | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl + not specified | Cells disrupted by French press at 10000-15000 p.s.i., membrane fractions collected at 150000 x g for 1 h |
| Solubilization | Detergent solubilization | not specified | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl + 1.5% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Membrane fraction incubated with 1.5% w/v [DDM](/xray-mp-wiki/reagents/detergents/ddm/) for 1 h at 4 C, then ultracentrifuged at 150000 x g for 30 min |
| Affinity purification | Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA (Qiagen) | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 30 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 1 mM [URACIL](/xray-mp-wiki/reagents/ligands/uracil/), 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Resin washed three times with 10 ml wash buffer each; protein eluted with 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) in wash buffer. 1 mM [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) included throughout. |
| SEC buffer exchange | Gel filtration chromatography | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 10/30 (GE Healthcare) | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, indicated detergent, 1 mM [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) + 0.4% beta-NG (for crystallization) | Protein concentrated to ~10 mg/ml before SEC; peak fractions collected for crystallization. All buffers contained 1 mM [URACIL](/xray-mp-wiki/reagents/ligands/uracil/). |

### Purification Workflow

*Source: doi/10.1038##cr.2017.83*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | [French Press Cell Lysis](/xray-mp-wiki/methods/cell-lysis/french-press/) and ultracentrifugation | not specified | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl + not specified | Cells disrupted by French press at 10000-15000 p.s.i., membrane fractions collected at 150000 x g for 1 h |
| Solubilization | Detergent solubilization | not specified | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl + 1.5% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | 1.5% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) (Anatrace) incubated for 1 h at 4 C |
| Affinity purification | Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA (Qiagen) | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 30 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 1 mM [URACIL](/xray-mp-wiki/reagents/ligands/uracil/), 0.2% DM + 0.2% DM | Resin washed three times with wash buffer, eluted with 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 10/30 (GE Healthcare) | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 1 mM [URACIL](/xray-mp-wiki/reagents/ligands/uracil/), indicated detergents + indicated detergents ([DDM](/xray-mp-wiki/reagents/detergents/ddm/), [LDAO](/xray-mp-wiki/reagents/detergents/ldao/), NG, [FC-9](/xray-mp-wiki/reagents/detergents/fos-choline-9/), [FC-11](/xray-mp-wiki/reagents/detergents/fos-choline-11/)) | Peak fractions collected for crystallization or biochemical characterizations |


## Crystallization

### doi/10.1038##nature09885

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | Full-length UraA (C-terminal His-tag) in 0.4% beta-NG, with 1 mM [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) |
| Reservoir | 25% [PEG400](/xray-mp-wiki/reagents/additives/peg-400/), 100 mM MES-NaOH pH 6.5, 300 mM Li2SO4 |
| Temperature | 18 C |
| Growth time | ~1 month |
| Notes | Crystals appeared overnight and grew to 50 x 50 x 100 um hexagonal rods in about one month. Space group P6_22. Crystals diffracted beyond 2.9 A at SPring-8 beamline BL41XU. Phasing by Hg-SIRAS using [Mercury (HgCl2) - Aquaporin Inhibitor](/xray-mp-wiki/reagents/additives/mercury/) derivatives obtained by soaking crystals for 24 h in mother liquor containing 1 mg/ml (C2H5HgO)HPO2. Structure refined at 2.8 A resolution. |

### doi/10.1038##cr.2017.83

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | Wild-type full-length UraA in detergent |
| Reservoir | 1.2% Fos-[Choline](/xray-mp-wiki/reagents/ligands/choline/) 9 ([FC-9](/xray-mp-wiki/reagents/detergents/fos-choline-9/)) and 0.06% Fos-[Choline](/xray-mp-wiki/reagents/ligands/choline/) 11 ([FC-11](/xray-mp-wiki/reagents/detergents/fos-choline-11/)) |
| Temperature | 18 C |
| Growth time | not specified |
| Notes | Crystals grew in space group C2221. Data collected at BL41XU, SPring-8. Structure solved by W-SAD phasing at 2.5 A resolution. |

### doi/10.1038##s41467-024-51814-8

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | UraA(G320P)-Sy45 complex in 0.2% DM, supplemented with 1% NG; final protein concentration 10 mg/ml |
| Reservoir | 50 mM Tris.HCl pH 8.4, 50 mM magnesium acetate, 35% (v/v) [PEG400](/xray-mp-wiki/reagents/additives/peg-400/), 0.1% (w/v) benzamidine hydrochloride |
| Temperature | 18 C |
| Growth time | not specified |
| Notes | Apo crystals of UraA(G320P)-Sy45 diffracted to 3.5 A resolution at PETRA III beamline P13. Structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using occluded UraA structure and SWISS-MODEL of Sy45. Uracil-liganded crystals were obtained using 40% [PEG400](/xray-mp-wiki/reagents/additives/peg-400/) and 1 mM [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) in reservoir, with apo crystals used as seeds, diffracting to 3.7 A at SLS X06DA beamline. |


## Biological / Functional Insights

### Novel structural fold of NAT/NCS2 transporters

UraA revealed a novel fold not seen in any previously determined membrane protein structure. The 14 TMs are arranged into two inverted repeats (TMs 1-7 and TMs 8-14). A pair of short antiparallel beta-strands located between TM3 and TM10 serves as an organizing center for the core domain, providing the structural basis for substrate recognition.

### Uracil recognition and binding mechanism

[URACIL](/xray-mp-wiki/reagents/ligands/uracil/) is coordinated primarily by residues from the core domain. Two Glu residues (Glu241 and Glu290) anchor [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) by each making two hydrogen bonds. The backbone amide nitrogen atoms of Phe73 and Gly289 form additional hydrogen bonds with the two oxygen atoms of [URACIL](/xray-mp-wiki/reagents/ligands/uracil/). His245 contributes indirectly via a water-mediated hydrogen bond (the hydroxyl of beta-NG in the crystal structure mimics a water molecule at this position). Van der Waals interactions involve Ala31, Phe73, Tyr288, and Tyr342. Phe73 blocks [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) access from the periplasm. Mutation of Glu241, His245, or Glu290 to Ala abrogates both [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) binding and transport.

### Domain architecture and alternating access mechanism

UraA is organized into a core domain (TMs 1-4, 8-11) and a gate domain (TMs 5-7, 12-14). The interface between the two domains forms the uracil-binding pocket. Structural analysis suggests alternating access of the substrate is achieved through conformational changes of the gate domain relative to the core domain around the bound [URACIL](/xray-mp-wiki/reagents/ligands/uracil/). The core domain provides substrate selectivity and proton/sodium translocation, while gate domain conformational changes enable substrate transport.

### Proton coupling mechanism

UraA is a proton-coupled symporter. Glu241, His245, and Glu290, all capable of protonation/deprotonation, are clustered at the core-gate interface and are essential for [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) binding. The proposed model suggests that substrate-free UraA is outward-open with deprotonated Glu residues. Upon [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) and H+ binding, at least one Glu is protonated, triggering gate domain closure to the inward-open conformation as seen in the structure. Proton translocation likely occurs from Glu to His245 and onward into the cytoplasm. In sodium symporters of the NAT family, Na+ neutralizes conserved Glu/Asp residues for substrate binding instead of protons.

### Dimeric assembly and monomer-dimer equilibrium

UraA forms a homodimer in the crystal structure wherein the gate domains are sandwiched by two core domains. The dimerization interface involves approximately 2400 A^2 buried surface area, mediated through the gate domains with extensive hydrophobic residues on TMs 5/12/13. [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) in multiple detergents ([DDM](/xray-mp-wiki/reagents/detergents/ddm/), [LDAO](/xray-mp-wiki/reagents/detergents/ldao/), NG) shows UraA elutes in two peaks, suggesting equilibrium between monomer and dimer. Crosslinking and [Static Light Scattering](/xray-mp-wiki/methods/quality-assessment/static-light-scattering/) confirm that wild-type UraA exists in monomer-dimer equilibrium.

### Dimerization is required for transport activity

Monomeric mutants M1 (L366W & I374W) and M2 (A137W & I374W) bind [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) with similar affinity to wild-type, confirming correct folding. However, transport activity is nearly abolished in the monomeric mutants in cell-based [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) uptake assays. The constitutive dimer exhibits 70% higher transport activity than wild-type. Intriguingly, dimers containing one functional and one loss-of-function protomer (E241A or H245A) show similar Km and Vmax to the constitutive dimer, suggesting one functional protomer is sufficient for transport.

### Conformational changes between inward-open and occluded states

Structural comparison between the inward-open (UraA_IO, PDB 3QE7) and occluded (UraA_Occ) conformations reveals pronounced relative motions between the core and gate domains. The core domain remains rigid while the gate domain undergoes inter- and intra-domain shifts. TM5 and TM12 rotate around an axis perpendicular to the core-gate domain interface and bend in the occluded state, with a more prominent kink in TM5. The periplasmic segment of TM5 moves towards the core domain while the cytoplasmic segment of TM12 is displaced away, resulting in the switch from occluded to inward-open state.

### Interdomain-linkers control conformational transitions in elevator transport

A wide inward-open conformation of UraA (UraA_WIO) was resolved by crystallizing the G320P mutant in complex with synthetic [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) Sy45. Comparison of UraA_WIO with the occluded state (UraA_OCC) reveals that the interdomain-linkers (TM4-5 and TM11-12) are not mere tethers but actively define the rotation axis and conformational space of the transport domain. The linkers consist of short amphipathic spacer helices flanked by conserved [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) (flexible, near transport domain) and proline (rigid, near scaffold domain) residues. Mutation of these residues (G112P, P121G, G320P, P330G) severely compromises [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) transport.

### G320P and P330G mutations differentially affect conformational equilibrium

The G320P mutation in the external interdomain-linker shifts the conformational equilibrium away from the inward-open state toward a more outward-open conformation, while P330G constrains the transporter toward an occluded-like state with strongly reduced surface exposure of both internal and external cavities. Both mutants bind [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) with increased affinity (up to 20-fold for P330G) despite being transport incompetent, suggesting they are trapped in specific conformational states. Hydrogen-deuterium exchange mass spectrometry ([HDX-MS](/xray-mp-wiki/methods/quality-assessment/hdx-ms/)) and cysteine alkylation experiments confirm altered conformational dynamics.

### Functional relevance of spacer helix architecture

The short interdomain-linkers in UraA contain alpha-helical spacer helices flanked by [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) and proline residues that act as molecular hinges. The conserved proline near the scaffold domain (P121 in cytoplasmic linker, P330 in external linker) fixes the orientation of the spacer helix relative to the scaffold. The conserved [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) near the transport domain (G112, G320) provides flexibility during the elevator motion. This architecture defines the rotation axis, which runs approximately parallel to scaffold helices TM5 and TM12, resulting in a nearly orthogonal displacement of the substrate binding site for shortest translocation path. Interdomain-linkers with similar spacer helix architecture are observed in other elevator transporters (SLC4, SLC13, SLC26 families).


## Cross-References

- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — UraA operates by alternating access between inward-open and occluded conformations
- [Elevator Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/elevator-mechanism/) — UraA core domain exhibits elevator-like movement relative to the dimeric gate domain
- [Rocker-Switch Mechanism](/xray-mp-wiki/concepts/structural-mechanisms/rocker-switch-mechanism/) — Rocking bundle motions of gate domains contribute to alternating access in UraA
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for UraA membrane solubilization and purification
- [Lauryl Dimethylamine N-Oxide (LDAO)](/xray-mp-wiki/reagents/detergents/ldao/) — Detergent used for SEC analysis of UraA oligomerization state
- [Uracil](/xray-mp-wiki/reagents/ligands/uracil/) — Substrate of UraA, binds in the occluded conformation
- [Fos-Choline 9 (FC-9)](/xray-mp-wiki/reagents/detergents/fos-choline-9/) — Detergent used for UraA crystallization
- [Substrate-Protonation Coupling](/xray-mp-wiki/concepts/transport-mechanisms/substrate-protonation-coupling/) — UraA couples uracil transport to proton translocation
- [French Press Cell Lysis](/xray-mp-wiki/methods/cell-lysis/french-press/) — Method used in structure determination or purification
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
