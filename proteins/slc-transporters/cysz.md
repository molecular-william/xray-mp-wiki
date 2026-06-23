---
title: "CysZ bacterial sulfate permease"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, channel, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.27829]
verified: false
---

# CysZ bacterial sulfate permease

## Overview

CysZ is a bacterial inner-membrane sulfate (SO₄²⁻) permease/channel found exclusively
in prokaryotes. It belongs to a family of ~28-30 kDa integral membrane proteins that
mediate sulfate uptake for biosynthesis of cysteine and methionine. The CysZ family
shows no sequence or structural homology to any known transporter or channel fold.
Crystal structures from three bacterial species — Idiomarina loihiensis (IlCysZ,
PDB 3TX3, 2.3 Å), Pseudomonas fragi (PfCysZ, PDB 6D79, 3.2 Å), and Pseudomonas
denitrificans (PdCysZ, PDB 6D9Z, 3.4 Å) — reveal a novel fold consisting of two
long transmembrane (TM) helices and two hemi-penetrating helical hairpins that form
a tripod-like shape. PdCysZ assembles as a hexamer with D3 symmetry, organized as
a trimer of antiparallel dimers with inverted transmembrane topology — a highly
unusual arrangement shared with EmrE and Fluc channels. Functional studies show
CysZ mediates non-concentrative, channel-like sulfate flux that is not coupled
to proton or sodium gradients and is inhibited by sulfite (SO₃²⁻). A conserved
sulfate-binding site (GLR motif) at the loop between helices H1-H2 coordinates
sulfate via two arginine residues and backbone amides. The structure reveals a
putative pore and ion conduction pathway lined by highly conserved polar and charged
residues.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.7554##eLife.27829 | 3TX3 | 2.3 | C2 | IlCysZ (Idiomarina loihiensis CysZ), residues 1-200 | SO₄²⁻ (selenate soak, refined at 2.1 Å) |
| doi/10.7554##eLife.27829 | 6D79 | 3.2 | C2 | PfCysZ (Pseudomonas fragi CysZ), residues 1-200, SeMet derivative | -- |
| doi/10.7554##eLife.27829 | 6D9Z | 3.4 | P6₃ | PdCysZ (Pseudomonas denitrificans CysZ), hexamer, residues 1-200 | -- |

## Expression and Purification

- **Expression system**: E. coli BL21(DE3)pLysS
- **Construct**: CysZ genes cloned into pET-derived kanamycin-resistant vector with N-terminal deca-histidine tag and TEV protease cleavage site. Includes cysZ from I. loihiensis (UniProt Q5QUJ8), P. fragi (UniProt A0A0X8F058), P. denitrificans (UniProt M4XKU7)

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Microfluidizer | -- | 20 mM Na-Hepes pH 7.0, 200 mM NaCl, 1 mM TCEP-HCl, 20 mM Na₂SO₄ + 1% (w/v) decyl maltopyranoside (DM) | Solubilization for 1 hr at 4°C, insoluble material removed by ultracentrifugation at 100,000 x g |
| Affinity purification | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta) Sepharose | 20 mM Na-Hepes pH 7.0, 200 mM NaCl, 0.2% DM, 40 mM imidazole (wash); 250 mM imidazole (elution) + 0.2% decyl maltopyranoside (DM) | Eluted protein dialyzed overnight with His-tagged TEV protease at 4°C against 20 mM Na-Hepes pH 7.0, 200 mM NaCl, 0.2% DM, 1 mM TCEP-HCl, 20 mM Na₂SO₄ for tag cleavage |
| Reverse Ni-NTA | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta) Sepharose | Same as dialysis buffer + 0.2% decyl maltopyranoside (DM) | Passaged over Ni-NTA to remove uncleaved CysZ, TEV protease, and cleaved His₁₀ tag |
| Size-exclusion chromatography | [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | Superdex 200 10/300 HR | 20 mM Na-Hepes pH 7.0, 200 mM NaCl, 1 mM TCEP-HCl, 20 mM Na₂SO₄ + For IlCysZ: 0.06% LDAO; for PfCysZ and PdCysZ: 1% beta-OG (beta-octyl glucopyranoside) | Typical yield ~1.5 mg from 1 L culture |


## Crystallization

### doi/10.7554##eLife.27829

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | IlCysZ at 6-8 mg/mL in LDAO; PfCysZ at 5 mg/mL in beta-OG; PdCysZ at 5-8 mg/mL in beta-OG |
| Reservoir | IlCysZ: 28-32% PEG400, 0.1 M Tris-HCl pH 8.0, 0.1 M NaCl or 0.1 M MgCl2. PfCysZ: 28% PEG400, 0.1 M MES pH 6.0. PdCysZ: 22-30% PEG550MME or PEG400, 0.1 M MES pH 6.0 |
| Temperature | 4 C |
| Growth time | 1-4 days |
| Cryoprotection | Crystals flash-frozen directly without additional cryo-protectant |
| Notes | IlCysZ crystals grew overnight, rhomboid/cuboid ~200 x 100 x 50 um. PfCysZ crystals cuboid, optimized with silicone oil microbatch. PdCysZ hexagonal prism crystals with multiple crystal forms (P6_3, P2_12_12_1, P4_122). |


## Biological / Functional Insights

### Novel fold and dual-topology assembly

CysZ features a previously unknown protein fold with two long TM helices and two hemi-penetrating helical hairpins. The protein assembles with inverted transmembrane topology (antiparallel dimers), a rare arrangement shared with EmrE and Fluc fluoride channels. The PdCysZ hexamer reveals D3 symmetry organized as a trimer of antiparallel dimers.

### Non-concentrative sulfate flux

CysZ mediates sulfate translocation without coupling to ion gradients (H+ or Na+) or ATP, characteristic of a passive channel-like mechanism rather than an active transporter. Flux is non-concentrative (max ~5-fold accumulation) and is inhibited by sulfite (SO3(2-)).

### Conserved sulfate-binding GLR motif

A sulfate-binding site was identified at the loop between helices H1-H2, comprising a conserved GLR motif (G25, L26, R27, R28 in IlCysZ). Two arginine residues coordinate the sulfate ion. Mutation of these arginines (R27A/R28A) abolishes sulfate binding and uptake.

### Putative pore and conduction pathway

PoreWalker analysis identified a putative ion translocation pathway beginning at a conserved hydrophilic entrance near the E106-R110-E134-N184-H185 interaction network. The pathway widens into a large central hydrophobic cavity (~50 A across) in the hexamer. The structures captured in a closed state, suggesting conformational changes are required for ion passage.


## Cross-References

- [KcsA K+ channel](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) — Different fold, but both are bacterial channel structures
- [Bpe Fluc fluoride channel](/xray-mp-wiki/proteins/other-ion-channels/bpe-fluoride-channel/) — Shares dual-topology antiparallel dimer assembly
- [Alternating access mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — Channel mechanism vs transporter alternating access in CysZ sulfate transport
