---

title: ZntB Transporter
created: 2026-04-27
updated: 2026-04-27
type: protein
tags: [transporter, membrane-protein, channel]
sources: [doi/10.1002##pro.215]

---
layout: default


# ZntB Transporter

## Overview

ZntB is a distant homolog of the CorA Mg²⁺ transporter within the metal ion transporter (MIT) superfamily. It facilitates efflux of Zn²⁺ and Cd²⁺ in bacteria, maintaining zinc homeostasis. The ZntB protein from *Salmonella typhimurium* was early reported as a zinc/cadmium exporter that does not transport Mg²⁺. The *Vibrio parahaemolyticus* ZntB (Vp-ZntB) shows 30% primary sequence identity with *S. typhimurium* ZntB and 17% with *Thermatoga maritima* CorA.

## Structure Determination

- **PDB ID**: 3CK6
- **Resolution**: 1.90 Å (highest resolution data set)
- **Space group**: P2₁
- **Method**: X-ray crystallography, Se-MAD phasing (Se absorption edge 0.9793 Å), low-energy anomalous diffraction at 7 keV for Cl⁻ identification
- **Construct**: Cytoplasmic domain of Vp-ZntB (residues 1–203 per monomer), homopentamer
- **Phasing**: Selenium single-wavelength anomalous diffraction (Se-MAD) + low-energy anomalous diffraction for chloride ions
- **Data collection**: Multiple wavelengths — Se peak (0.9793 Å), Zn edge (1.2823 Å), low-energy (1.7712 Å)
- **Beamlines**: 19ID and 19BM at Argonne National Laboratory

## Expression and Purification

- **Expression system**: E. coli (MCS expression system, M109 strain)
- **Construct**: Vp-ZntB cytoplasmic domain (residues 1–203), N-terminal His-tag (T7 vector with TEV cleavage site)
- **Induction**: IPTG-induced expression
- **Cell lysis**: Sonication of harvested E. coli pellets
- **Solubilization**: DDM (n-dodecyl-β-D-maltopyranoside) for membrane protein solubilization (full-length ZntB); cytoplasmic domain expressed soluble
- **Purification**:
  1. Ni-NTA affinity chromatography (His-tag), elution with imidazole
  2. TEV protease cleavage of His-tag
  3. Second Ni-NTA pass to remove cleaved tag and TEV protease
  4. Size-exclusion chromatography (Superdex 200) for final polishing
- **SEC buffer**: 20 mM HEPES pH 7.5, 150 mM NaCl, 1 mM DTT

## Crystallization

- **Method**: Vapor diffusion (hanging drop)
- **Protein concentration**: ~10 mg/mL
- **Reservoir**: 15-20% PEG 3350, 0.1 M sodium citrate pH 5.6, 0.2 M ammonium acetate
- **Temperature**: 20 °C
- **Crystal growth**: 1-2 weeks
- **Cryoprotection**: Crystallization mother liquor supplemented with 25% glycerol
- **Data collection**: Se-MAD at Se absorption edge (0.9793 Å), Zn edge (1.2823 Å), and low-energy anomalous diffraction (1.7712 Å) for Cl⁻ identification

## Structural Architecture

- **Oligomerization**: Homopentamer — funnel-shaped assembly
- **Monomer structure**: Two subdomains:
  - **N-terminal α/β/α sandwich** (residues 1–125): twisted central β-sheet (7 anti-parallel β-strands) flanked by α-helices
  - **C-terminal coiled-coil** (residues 126–203): three long anti-parallel α-helices (α4, α5, α6) with heptad repeats (a/d hydrophobic core)
- **The α6 stalk helix** is the primary contributor to monomer–monomer interaction along the entire funnel length
- **Buried surface per monomer–monomer contact**: ~2100 Å²; ΔG = −8.6 kcal/mol
- **Full-length model**: Built by homology to Tm-CorA (2.9 Å); transmembrane region shows 55% sequence similarity

## Chloride Ion Binding Sites

A striking finding: **25 well-defined Cl⁻ ions** per pentamer (5 per monomer) were observed, despite crystallization buffer containing 0.2 M MgCl₂. No Mg²⁺, Zn²⁺, or other divalent metal ions were identified.

- **Cl⁻(1) and Cl⁻(2)**: Highest anomalous peaks (6.1σ–8.5σ), largely associated with the α/β/α subdomain
- **Cl⁻(3)**: Located at N-terminal end of α3 helix, interacting with R113 (3.31 Å), A114 (3.23 Å), S112 (3.02 Å); positioned to interact with α3 helix dipole
- **Cl⁻(4)**: Interacts with R35; five peaks with heights 2.9σ–6.8σ
- **Cl⁻(5)**: Inner surface of funnel near R192; counteracts positive charge from basic residues
- **Anomalous identification**: Confirmed by low-energy anomalous diffraction at 7 keV (Cl⁻ f'' ≈ 0.913 electrons vs S f'' ≈ 0.729)

## Electrostatic Properties

- The central pore is **highly attractive for cations**, especially divalents
- 25 Cl⁻ anions neutralize positive surface patches and create strong negative electrostatic potential
- Continuum electrostatics (PBEQ/CHARMM) reveals:
  - Initial stabilization at pore entrance (Z = −80 Å)
  - Potential barrier at Z = −60 Å (contributed by K181, R185, E224)
  - Deep electrostatic well at Z = −35 Å (constriction site below membrane, formed by D235, K238, R241, D242)
- Cl⁻ ions completely remove the barrier and make the entire vestibule attractive for cations
- Divalent cations more strongly attracted than monovalent

## Pore Architecture (Full-Length Model)

- **Tm-CorA pore**: Too constricted for ion permeation (closed state)
- **Vp-ZntB model**: More open with few regions <5 Å
- **Constriction sites**:
  - Below membrane (cytosolic): D235, K238, R241, D242
  - Transmembrane: S263, F259, F252
- **External gate**: N314 (N272 in Vp-ZntB) and hydrophobic rings M291/L294 (S249/F252)

## Comparison with CorA

| Feature | Vp-ZntB | Tm-CorA |
|---------|---------|---------|
| Oligomer | Pentamer | Pentamer |
| Cytoplasmic domain | Pentamer (intrinsic) | Pentamer (full-length) / Dimer (truncated) |
| Metal binding | Cl⁻ ions (25/pentamer) | Mg²⁺/Co²⁺/Ca²⁺ binding sites |
| Pore state | Open model | Closed model |
| Sequence identity | 17% | — |

## Functional Implications

- ZntB prefers Cl⁻ over Mg²⁺ binding (pI drops from 5.24 to ~4.2 with Cl⁻ incorporation)
- The "aspartate ring" (D242) at the narrowest pore segment is analogous to D277 in Tm-CorA
- Cation selectivity attributed to signature motif: ZntB GxxG[I,V]NxGGxP vs CorA YGMNFxxMPEL
- The pentameric cytoplasmic domain alone is sufficient for assembly — transmembrane spanners not required
- **Pentamer formation determinants**:
  - α6 stalk helix is the primary contributor to monomer–monomer interaction along entire funnel
  - Buried surface per monomer–monomer contact: ~2100 Å²; ΔG = −8.6 kcal/mol (soluble domain contribution)
  - In full-length CorA, total buried surface ~4400 Å² (2720 Å² from intracellular region); ΔG = −6.7 kcal/mol
  - Soluble domain contributes ~1/4 of total interface energy in CorA — significant fraction of pentamer formation determinants
  - Truncation at middle of α6 stalk (e.g., N220 in Vp-ZntB, corresponding to Tm-CorA 1–266) would lose ~1000 Å² buried area and prevent pentamer formation
  - Previously reported CorA intracellular domain dimers likely artifacts of excessive α6 truncation

## Cross-References

- [cora-mg-transporter](/concepts/cora-mg-transporter/) — Mg²⁺ transporter; structural homolog
- [metal-ion-transporter](/concepts/metal-ion-transporter/) — MIT superfamily overview
- [mfs-transporter](/concepts/mfs-transporter/) — Major facilitator superfamily (different family)
- [spermine](/reagents/ligands/spermine/) — Polyamine ligand (related to [ion-channels](/concepts/ion-channels/) block concepts)
- [ddm](/reagents/detergents/ddm/) — Detergent used in purification
- [xray-crystallography](/methods/structure-determination/xray-crystallography/) — Structure determination method