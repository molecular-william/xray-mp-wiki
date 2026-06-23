---
title: Vp-ZntB Cytoplasmic Domain (Vibrio parahaemolyticus Zinc Transporter)
created: 2026-05-26
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1002##pro.215]
verified: false
---

# Vp-ZntB Cytoplasmic Domain (Vibrio parahaemolyticus Zinc Transporter)

## Overview

ZntB is a distant homolog of the [CorA Mg2+ Transporter](/xray-mp-wiki/concepts/cora-mg-transporter/) within the [Metal Ion Transporter (MIT) Superfamily](/xray-mp-wiki/concepts/mit-superfamily/). ZntB from Salmonella typhimurium facilitates efflux of Zn2+ and Cd2+, but not Mg2+. The crystal structure of the cytoplasmic domain of ZntB from Vibrio parahaemolyticus (Vp-ZntB) was determined at 1.90 A resolution, revealing a funnel-shaped homopentamer composed of two subdomains per monomer: an N-terminal alpha/beta/alpha sandwich (residues 1-125) and a C-terminal coiled-coil subdomain (residues 126-203). The structure is similar to the full-length CorA from Thermatoga maritima but differs from previously reported dimeric structures of truncated CorA intracellular domains. No Zn2+ or Cd2+ binding sites were identified; instead, 25 well-defined Cl- ions were observed bound to the protein. Continuum electrostatics calculations suggest the central pore is highly attractive for cations, especially divalents, with bound Cl- ions enhancing cation transport.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1002##pro.215 | 3CK6 | 1.90 | P 1 21 1 | Vp-ZntB cytoplasmic domain residues 1-203, homopentamer (5 molecules in asymmetric unit). Construct used for crystallography: Vp-ZntB(1-203) with N-terminal His6 tag and TEV protease cleavage site, SeMet-labeled. | 25 Cl- ions (5 per monomer) |

## Expression and Purification

- **Expression system**: Escherichia coli (SeMet-labeled protein expressed using the high-throughput ligation-independent cloning system from Stols et al., 2002)
- **Construct**: Vp-ZntB cytoplasmic domain (residues 1-203) from Vibrio parahaemolyticus with N-terminal His6 tag and TEV protease cleavage site

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Affinity purification | Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA | Not specified in detail + -- | His6-tagged Vp-ZntB cytoplasmic domain purified by Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/). The tag was removed by TEV protease cleavage. |
| Size-exclusion chromatography | Size-exclusion chromatography | Not specified | Not specified in detail + -- | Final purification step to obtain monodisperse protein for crystallization |


## Crystallization

### doi/10.1002##pro.215

| Parameter | Value |
|---|---|
| Method | Vapor diffusion crystallization |
| Protein sample | Purified Vp-ZntB cytoplasmic domain (SeMet-labeled) |
| Reservoir | 0.2 M MgCl2, 20% (w/v) [PEG](/xray-mp-wiki/reagents/additives/peg/) 3350, 0.1 M MES (pH not specified) |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Crystals belong to space group P21. Unit cell: a = 64.67, b = 130.18, c = 80.05 A, beta = 103.4 deg. Data collected at Se absorption edge (0.9793 A peak, 0.9795 A inflection), Zn absorption edge (1.2823 A), and low energy (1.7712 A for Cl- anomalous signal). Structure solved by SAD phasing using HKL-3000, model built with COOT, refined with REFMAC to 1.90 A resolution. MW of monomer: 29,021.6 Da (249 residues including tag). |


## Biological / Functional Insights

### Funnel-shaped homopentamer architecture

The Vp-ZntB cytoplasmic domain forms a funnel-shaped homopentamer similar to full-length [Thermotoga maritima CorA (TmCorA) Magnesium Channel](/xray-mp-wiki/proteins/slc-transporters/tm-cora/). Each monomer has an N-terminal alpha/beta/alpha sandwich subdomain (residues 1-125) with a twisted central beta-sheet of seven anti-parallel strands, and a C-terminal coiled-coil subdomain (residues 126-203) with three long anti-parallel alpha-helices (alpha4, alpha5, alpha6). The alpha6 stalk helix is the primary contributor to monomer-monomer interactions along the entire funnel length. The coiled-coil subdomain exclusively contributes to pentamer formation, with heptad sequence repeats characteristic of coiled-coil structures.

### Chloride ion binding and electrostatic properties

25 well-ordered Cl- ions (5 per monomer) were identified bound to the protein using low-energy anomalous diffraction data at 7 keV. The Cl- ions are not located at monomer-monomer interfaces but are largely associated with the alpha/beta/alpha subdomain. They form a Cl- ring in the middle of the cytoplasmic pentamer, neutralizing local positive charges. Continuum electrostatics calculations show that the Cl- ions create strong negative electrostatic potential along the central pore, making it highly attractive for cations (especially divalents) and enhancing cation transport. Including Cl- ions in calculations completely removes a potential barrier in the vestibule region.

### Comparison with CorA and pentamer stability

The Vp-ZntB homopentamer is similar to full-length [Thermotoga maritima CorA (TmCorA) Magnesium Channel](/xray-mp-wiki/proteins/slc-transporters/tm-cora/), but the two reported CorA intracellular domain dimers ([Thermotoga maritima CorA (TmCorA) Magnesium Channel](/xray-mp-wiki/proteins/slc-transporters/tm-cora/) 1-266 and Af-CorA) are likely artifacts of extensive [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation/) of the stalk helix alpha6. The monomer-monomer interface buries ~2100 A2 per pair with favorable Gibbs free energy Delta G of -8.6 kcal/mol, indicating the intracellular domain is sufficient to assemble a pentamer. The full-length Vp-ZntB model based on [Thermotoga maritima CorA (TmCorA) Magnesium Channel](/xray-mp-wiki/proteins/slc-transporters/tm-cora/) shows a more open pore than [Thermotoga maritima CorA (TmCorA) Magnesium Channel](/xray-mp-wiki/proteins/slc-transporters/tm-cora/), with charged residue constriction sites (D235, K238, R241, D242) and transmembrane constrictions (S263, F259, F252).

### No metal ion binding in cytoplasmic domain

No structurally ordered Mg2+, Zn2+, or other divalent metal ions were identified in the high-resolution structure, despite crystallization buffer containing 0.2M MgCl2. This does not exclude the possibility of metal ion binding to the transmembrane domain. The ZntB transporter has the signature motif GxxG[I,V]NxGGxP located between two transmembrane alpha-helices, which differs from the CorA motif YGMNFxxMPEL, potentially explaining differences in cation selectivity (ZntB transports Zn2+/Cd2+ but not Mg2+).

### Aspartate ring at pore constriction

D242 of Vp-ZntB forms an "aspartate ring" at the narrowest pore segment, with five D242 side chains pointing to the center of the channel. This is equivalent to the D277 ring in [Thermotoga maritima CorA (TmCorA) Magnesium Channel](/xray-mp-wiki/proteins/slc-transporters/tm-cora/). The Vp-ZntB D242 corresponds to S284 in [Thermotoga maritima CorA (TmCorA) Magnesium Channel](/xray-mp-wiki/proteins/slc-transporters/tm-cora/). The strong electrostatic well at Z = -35 A is primarily contributed by residues D235, K238, R241, and D242, with D242 as the strongest contributor.


## Cross-References

- [CorA Mg2+ Transporter](/xray-mp-wiki/concepts/cora-mg-transporter/) — ZntB is a distant homolog of the CorA Mg2+ transporter within the MIT superfamily
- [NhaA Na+/H+ Antiporter](/xray-mp-wiki/proteins/slc-transporters/nhaa/) — Related membrane transporter with ion transport mechanism
- [Metal Ion Transporter (MIT) Superfamily](/xray-mp-wiki/concepts/metal-ion-transporter-superfamily/) — ZntB belongs to the MIT superfamily of metal ion transporters
- [Metal Ion Transporter (MIT) Superfamily](/xray-mp-wiki/concepts/mit-superfamily/) — Related biological concept
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Thermotoga maritima CorA (TmCorA) Magnesium Channel](/xray-mp-wiki/proteins/slc-transporters/tm-cora/) — Related protein structure
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
