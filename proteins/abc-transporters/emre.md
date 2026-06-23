---
title: "EmrE (E. coli Small Multidrug Resistance Transporter)"
created: 2026-06-08
updated: 2026-06-09
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.0709387104, doi/10.7554##eLife.76766, doi/10.1073##pnas.2403273121]
verified: false
---

# EmrE (E. coli Small Multidrug Resistance Transporter)

## Overview

EmrE is a small multidrug resistance (SMR) family proton-coupled multidrug efflux transporter from Escherichia coli. It functions as a dual-topology antiporter that exports a broad spectrum of structurally diverse antiseptics and antimicrobials, including polyaromatic cations, quaternary ammonium compounds, and quaternary phosphoniums. The first X-ray crystal structure, published in 2007 (Chen et al., PNAS), established that EmrE forms an antiparallel homodimer with the 'dual topology' model, where the two monomers adopt opposite orientations in the membrane. Selenomethionine markers clearly demonstrated the antiparallel arrangement, with the first three transmembrane helices from each monomer surrounding the substrate binding chamber while the fourth helices mediate dimer formation. Higher-resolution crystal structures were later solved using a multipurpose monobody crystallization chaperone (L10), revealing six structures at 2.9-3.9 A resolution: a low-pH proton-bound state (PDB 7MH6, 2.9 A) and five complexes with diverse substrates including methyl viologen, harmane, methyltriphenylphosphonium, tetraphenylphosphonium, and benzyltrimethylammonium. These structures reveal that binding site tryptophan and glutamate residues adopt different rotamers to accommodate diverse substrates without major backbone rearrangements.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.0709387104 | 3B5D | 3.8 | C2 | EmrE in complex with tetraphenylphosphonium (TPP+), C2 crystal form. Selenomethionine-labeled protein for experimental phasing. | Tetraphenylphosphonium (TPP+) |
| doi/10.1073##pnas.0709387104 | 3B61 | 4.5 | C2 | EmrE apo structure, C2 crystal form. | None |
| doi/10.1073##pnas.0709387104 | 3B62 | 4.4 | P21 | EmrE in complex with tetraphenylphosphonium (TPP+), P21 crystal form. | Tetraphenylphosphonium (TPP+) |
| doi/10.7554##eLife.76766 | 7MH6 | 2.9 | C121 | EmrE3 mutant (E25N, W31I, V34M) with L10 monobody, low pH (proton-bound) state | None |
| doi/10.7554##eLife.76766 | 7MGX | 3.1 | P1 | EmrE3/L10 in complex with methyl viologen | Methyl viologen |
| doi/10.7554##eLife.76766 | 7SVX | 3.8 | C121 | EmrE3/L10 in complex with harmane | Harmane |
| doi/10.7554##eLife.76766 | 7SSU | 3.2 | C121 | EmrE3/L10 in complex with methyltriphenylphosphonium (MeTPP+) | Methyltriphenylphosphonium |
| doi/10.7554##eLife.76766 | 7SV9 | 3.4 | C121 | EmrE3/L10 in complex with tetraphenylphosphonium (TPP+) | Tetraphenylphosphonium |
| doi/10.7554##eLife.76766 | 7T00 | 3.9 | C121 | EmrE3/L10 in complex with benzyltrimethylammonium | Benzyltrimethylammonium |

## Expression and Purification

- **Expression system**: Escherichia coli C41 (DE3)
- **Construct**: EmrE3 (E25N, W31I, V34M) with N-terminal hexahistidine tag and thrombin cut site in pET15b

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell growth and lysis | Cells grown in Studier's autoinduction medium at 37 C overnight (15-18 hr). Pellets resuspended in breaking buffer (50 mM [Tris-Cl](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 100 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10 mM TCEP) with DNase, MgCl2, PMSF, lysozyme, pepstatin, leupeptin. Lysed by sonication. | -- | 50 mM [Tris-Cl](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 100 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10 mM TCEP + -- | Lysate extracted with 2% n-Decyl-beta-D-Maltopyranoside ([DM](/xray-mp-wiki/reagents/detergents/dm/)) for 2 hr at room temperature |
| Affinity chromatography | Clarified lysate loaded onto TALON cobalt resin, washed with wash buffer + 10 mM imidazole, eluted with 400 mM imidazole | [TALON](/xray-mp-wiki/reagents/additives/talon/) cobalt resin (Clontech) | 20 mM [Tris-Cl](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 100 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 5 mM [DM](/xray-mp-wiki/reagents/detergents/dm/) + 5 mM [DM](/xray-mp-wiki/reagents/detergents/dm/) | Eluted with wash buffer supplemented with 400 mM imidazole |
| Thrombin cleavage and SEC | Buffer exchanged into wash buffer using PD-10 desalting columns. His tags cleaved with thrombin (1 U/mg EmrE3) overnight at 21 C. Final [size exclusion chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) using [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) column. | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) (GE Healthcare) | 10 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 100 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 4 mM [DM](/xray-mp-wiki/reagents/detergents/dm/) + 4 mM [DM](/xray-mp-wiki/reagents/detergents/dm/) | SEC performed for final polishing step |


## Crystallization

### doi/10.7554##eLife.76766

| Parameter | Value |
|---|---|
| Method | [Hanging-drop vapor diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) with monobody L10 chaperone |
| Protein sample | EmrE3 (10 mg/mL) + L10 monobody (10 mg/mL) at 2.1:1 molar ratio, supplemented with 6.6 mM LDAO |
| Reservoir | 0.2 M [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 0.1 M sodium cacodylate pH 5.2, 34% [PEG 600](/xray-mp-wiki/reagents/additives/peg-600/) (low pH, no substrate) |
| Temperature | 20 C |
| Growth time | ~4 weeks |
| Cryoprotection | Flash frozen in liquid nitrogen |
| Notes | Crystals formed in 96-well plates. Space group C121 (apo, TPP+, MeTPP+, harmane, benzyltrimethylammonium) or P1 (methyl viologen). Substrate-bound crystals grown in 0.1 M LiNO3 or 0.1 M (NH4)2SO4, 0.1 M ADA pH 6.5 or 0.1 M HEPES pH 7.1-7.3, 30-35% PEG 600 with substrates added from stock solutions (1 mM methyl viologen, 500 uM harmane, 300 uM benzyltrimethylammonium, 100 uM TPP+, 300 uM MeTPP+). Structures solved by molecular replacement using L10 monobody and Gdx-Clo helices as search models. |


## Biological / Functional Insights

### Dual topology antiparallel homodimer

The 2007 X-ray structure (3.8 A, PDB 3B5D) provided definitive evidence for the antiparallel (dual topology) orientation of the EmrE homodimer. Selenomethionine-labeled crystals allowed unambiguous identification of the N-terminal region position relative to the membrane. The two monomers are oriented in opposite directions, with TM1-TM3 from each monomer surrounding the substrate binding chamber and TM4 helices participating only in dimer formation. This arrangement supports the "dual topology" model where small membrane proteins with an even number of TMs can insert in both orientations.

### Multipurpose crystallization chaperone for SMR proteins

A monobody (L10) originally developed for Gdx-Clo was repurposed as a crystallization chaperone for EmrE by introducing three conservative mutations (E25N, W31I, V34M) in loop 1. The EmrE3 mutant retains wild-type transport activity (Km within 2-fold of WT) and binds monobody L10 with Kd = 850 nM. The monobody mediates most crystal contacts, enabling both Gdx-Clo and EmrE to crystallize in a nearly identical unit cell despite 1-2 A displacements of binding pocket helices.

### Sidechain flexibility enables substrate polyspecificity

The EmrE binding site uses sidechain rearrangements rather than backbone movements to accommodate structurally diverse substrates. Key residues E14 and W63 adopt different rotamers depending on the bound substrate. E14 sidechains act like calipers, moving apart for large quaternary ammoniums or closer together for flat aromatic substrates. W63 rotamerizes to expand or narrow the binding pocket.

### Structural basis of the binding pocket

The substrate binding site is formed by residues from both subunits at the midpoint of the membrane, with two essential E14 residues defining the pocket edges. At pH 5.2 (proton-bound), both E14 residues are protonated. Substrates bind between the E14 residues, with their center of mass midway between the carboxylates. Aromatic residues Y60 and W63 contribute via ring stacking interactions.

### Comparison to Gdx-Clo reveals subtype-specific differences

The Qac-type EmrE and Gdx-type Gdx-Clo share high structural similarity (Calpha RMSD 1.2 A for the dimer) but differ in their H-bond network architecture. Gdx-Clo has a polarized stack of H-bond donors and acceptors (W16/E13/S42/W62) that constrains the central glutamate, whereas EmrE lacks this stack.

### Single-particle cryo-EM and structural validation

The crystal structure agrees closely with helical density from low-resolution EM maps and with computational models. Comparison to an NMR-based model of the S64V mutant (PDB 7JK8) shows a 2.3 A overall RMSD with differences in subunit packing and Y60 rotamer orientation.


## Cross-References

- [Antibiotic Efflux Pump](/xray-mp-wiki/concepts/transport-mechanisms/antibiotic-efflux-pump/) — EmrE is a multidrug efflux pump belonging to the SMR family
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — EmrE functions via dual-topology alternating access
- [SMR (Small Multidrug Resistance) Family](/xray-mp-wiki/concepts/protein-families/sm-family/) — EmrE is the founding member of the SMR family
- [Decylmaltoside (DM)](/xray-mp-wiki/reagents/detergents/dm/) — Primary detergent used for EmrE purification and crystallization
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Reference detergent for SMR family purification
- [Lauryldimethylamine N-oxide (LDAO)](/xray-mp-wiki/reagents/detergents/ldao/) — Used as crystallization additive
- [PEG 600](/xray-mp-wiki/reagents/additives/peg-600/) — Precipitant for crystallization
- [TALON](/xray-mp-wiki/reagents/additives/talon/) — Used for affinity purification
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Buffer used in purification
- [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer used in size exclusion chromatography
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Used for elution in affinity chromatography
- [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/) — Salt used in purification buffers
- [Hanging-drop vapor diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) — Crystallization method
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Final polishing step in purification
