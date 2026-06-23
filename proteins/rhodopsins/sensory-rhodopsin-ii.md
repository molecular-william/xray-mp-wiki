---
title: "Sensory Rhodopsin II (NpSRII)"
created: 2026-06-08
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1062977, doi/10.1073##pnas.181203898, doi/10.1038##NATURE01109, doi/10.1016##j.jmb.2011.07.022, doi/10.1016##j.jmb.2011.11.025]
verified: false
---

# Sensory Rhodopsin II (NpSRII)

## Overview

Sensory Rhodopsin II (NpSRII) is a phototaxis receptor from the haloarchaeon
Natronobacterium pharaonis that mediates blue-light avoidance. It is a member
of the microbial rhodopsin family, a group of seven-transmembrane helix
proteins that bind a [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore. NpSRII shares ~27% sequence identity
with [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) (BR) and ~40% identity with other sensory rhodopsins.
The 2.4 A crystal structure of NpSRII was determined by X-ray diffraction
of 3D crystals grown in a cubic lipid phase, providing insights into color
tuning and transducer interaction mechanisms. The 2.6 A crystal structure of
the active state of uncomplexed NpSRII (PDB 3QDC) revealed large
conformational changes in helices F and G that are more pronounced than in
the transducer-bound complex, providing insights into signal transduction
and proton pumping mechanisms.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##NATURE01109 | 1H2S | 1.94 | Orthorhombic | NpSRII in complex with HtrII_114 (transducer residues 1-114) | all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) |
| doi/10.1016##j.jmb.2011.07.022 | 3QAP | 1.9 | C2221 | Uncomplexed NpSRII ground state | all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) |
| doi/10.1016##j.jmb.2011.07.022 | 3QDC | 2.6 | C2221 | Uncomplexed NpSRII active state (M/O intermediate) | 13-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) |

## Expression and Purification

- **Expression system**: Natronobacterium pharaonis (native source)
- **Notes**: Expressed in native host; purified for crystallographic studies

### Purification Workflow

#### Source: doi/10.1126##science.1062977


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Solubilization and purification | Affinity/purification using octylglucoside | — | Octylglucoside-containing buffer + beta-octylglucoside | Purified NpSRII at 28.0 mg/ml preincubated with H. salinarum polar lipids (11.2 mg/ml) |

#### Source: doi/10.1016##j.jmb.2011.07.022

- **Expression system**: E. coli BL21(DE3)
- **Expression construct**: NpSRII with C-terminal 7x His tag in pET27bmod

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Heterologous expression in E. coli | — |  | NpSRII-His was expressed in E. coli strain BL21(DE3) using pET27bmod vector |
| Purification | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) and DEAE cellulose chromatography | — |  | Purified as described previously (Hohenfeld et al. 1999, FEBS Lett.; Shimono et al. 1997). [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) removed by DEAE cellulose chromatography. NpSRII-His reconstituted into purple membrane lipids (protein-to-lipid ratio ~1:1) |


## Crystallization

### doi/10.1126##science.1062977

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) |
| Protein-to-lipid ratio | 1:1 (v/v) |
| Temperature | 22°C |
| Growth time | Overnight incubation then crystallization |
| Notes | 10 ul aliquots of octylglucoside-purified NpSRII (28.0 mg/ml) preincubated with H. salinarum polar lipids were mixed with 10 ul of [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) and centrifuged for 1 hour at 11,000g at 22°C. After overnight incubation at 2°C, crystals appeared within 36 hours. |

### doi/10.1016##j.jmb.2011.07.022

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) |
| Protein-to-lipid ratio | ~1:1 |
| Temperature | 22°C |
| Notes | Crystals grown as described previously (Hohenfeld et al. 1999; Shimono et al. 1997). Active state trapped in crystals by laser illumination (488 nm, 0.33 W, 2 s). Cryostream blocked during illumination. Optimal conditions produced ~35% M-state and ~25% O-state. Crystal space group C2221. |


## Biological / Functional Insights

### Color tuning mechanism in sensory rhodopsins

The NpSRII structure reveals the structural basis for the blue-shifted absorption (497 nm) compared to [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) (568 nm). The 71-nm blue shift results from: (1) displacement of Arg72 by 1.1 A with rotation away from the Schiff base, strengthening the Schiff base/counterion interaction; (2) removal of two hydroxyls near the beta-ionone ring (Ser141 and Thr142 in BR replaced by Gly130 and Ala131 in NpSRII); (3) changes in tilt and slant of the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) polyene chain. Mutagenic substitution of 10 residues in the retinal-binding pocket with corresponding BR residues produced only a ~25 nm red shift, indicating that spectral tuning results from precise positioning of residues and backbone differences that cannot be deduced from primary structure alone.

### Structural basis for lack of proton pumping in sensory rhodopsins

The NpSRII structure explains why sensory rhodopsins do not efficiently pump protons. The cytoplasmic channel lacks a hydrogen-bonded water network due to replacement of the Asp96-Thr46 pair in BR with Phe86-Leu40, presenting a hydrophobic barrier. The extracellular region lacks proton release machinery (a pair of glutamic acid residues connected to the Schiff base by a 3D hydrogen-bonded network). The presence of a beta-octylglucoside detergent molecule inserted with its C8 tail perpendicular to the bilayer into the seven-helix bundle further attests to the greater hydrophobicity of the cytoplasmic side.

### Transducer interaction interface

Sensory rhodopsins transmit signals by protein-protein interaction with cognate integral membrane transducer proteins (HtrI/HtrII) that control cytoplasmic phosphorylation pathways. The interaction specificities of SRI with HtrI and SRII with HtrII are determined by the transmembrane helices of the Htr subunits, indicating interaction occurs within or near the membrane. The NpSRII structure shows a detergent molecule inserted into the seven-helix bundle, providing insights into the protein-protein interaction surface.

### 2.1-Å resolution structure: retinal conformation, chloride binding, and expanded color tuning mechanism

A 2.1-Å resolution X-ray structure of pSRII solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) as a search model revealed the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) in a largely unbent 6-s-trans conformation, in contrast to the bent [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) in BR and [Halorhodopsin (HR) from Halobacterium salinarum](/xray-mp-wiki/proteins/rhodopsins/halorhodopsin/). Three non-conserved residues in the retinal-binding pocket — Val-108, Gly-130, and Thr-204 (versus Met, Ser, and Ala in BR/HR/SRI) — modify the polarity near the beta-ionone ring and Schiff base. Thr-204 places its hydroxyl group 4.5 Å from the Schiff-base nitrogen, contributing to the blue-shifted absorption (497 nm vs 568 nm for BR). A putative chloride ion was identified coordinated to Arg-72, Tyr-73, waters 406 and 407, and the backbone amide of Phe-69, coupled to the Schiff base via a hydrogen-bond network. The structure also revealed a positively charged cytoplasmic surface patch (Lys-157, Ser-158, Arg-162, Arg-164, Asn-165, Asp-214) proposed to interact electrostatically with the HtrII transducer protein's conserved cytoplasmic domain GDGDLD.

### 1.94 A structure of SRII-HtrII complex reveals transmembrane signalling mechanism

The 1.94 A X-ray structure of the NpSRII-HtrII_114 complex, crystallized
in lipidic cubic phase, provides an atomic picture of the first signal
transduction step in phototaxis. The complex forms a dimer via a
crystallographic two-fold axis, with TM1 and TM2 of the transducer
packing against helices F and G of the receptor. The transducer extends
beyond the extracellular side by ~3 helical turns (residues 44-59). The
structure supports a mechanism where light-activated outward movement of
helix F (hinged at Pro175) collides tangentially with TM2, inducing a
clockwise rotation of the cytoplasmic end of TM2. This rotation
propagates the signal to the downstream two-component signalling cascade,
establishing a common mechanism for transmembrane signalling in
phototaxis and chemotaxis. High B-factors at the cytoplasmic ends of TM2
and helix F indicate increased flexibility facilitating the active/inactive
state transition.

### Active state of uncomplexed NpSRII reveals amplified conformational changes

The 2.6 A crystal structure of the active state of uncomplexed NpSRII
(PDB 3QDC) revealed large conformational changes in helices F and G that
are similar in nature to those observed in the NpSRII-NpHtrII complex
(PDB 2F95) but nearly twice as large in amplitude. Helix F moves by
~0.3 A towards the cytoplasm while helix G moves ~0.7 A towards the
extracellular side. The extracellular F-G loop moves out of the membrane
plane. The 13-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) configuration in the active state was confirmed,
and a water molecule adjacent to the Schiff base (analogous to W402 in BR)
was found to be absent due to Schiff base deprotonation. The E-F loop
changes conformation and becomes more compressed. These findings indicate
that the NpHtrII transducer opposes the structural rearrangements in the
receptor, and this opposition constitutes the physical basis of signal
transfer.

### Implications for proton pumping inhibition by transducer binding

Comparison of the active states of free NpSRII and NpSRII-NpHtrII complex
reveals structural differences that explain the inhibition of proton
pumping upon transducer binding. In free NpSRII, the active state shows a
slight outward tilt of the G helix combined with E-F loop changes that may
facilitate formation of a water chain needed for [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) reprotonation.
These changes are not observed in the M-state of complexed NpSRII. The
active state transition also results in disappearance of a water molecule
that hydrogen bonds to the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) in the ground state. The transducer may
affect NpSRII dynamics either directly by influencing conformational
changes or indirectly by shielding helices F and G from the lipid bilayer,
which would increase the energy of the active state when transducer is
bound.


## Cross-References

- [n-Octyl-beta-D-glucoside (OG)](/xray-mp-wiki/reagents/detergents/og/) — OG used for NpSRII purification and crystallization
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Monoolein used as the host lipid for LCP crystallization
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — Closely related archaeal rhodopsin used for structural comparison of active state and proton pumping mechanism
- [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) — Chromophore covalently bound to NpSRII via protonated Schiff base; isomerizes from all-trans to 13-cis upon light activation
- [Microbial Rhodopsins](/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/) — NpSRII is a member of the microbial rhodopsin family; active state structure informs understanding of rhodopsin signal transduction
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [Halorhodopsin (HR) from Halobacterium salinarum](/xray-mp-wiki/proteins/rhodopsins/halorhodopsin/) — Related protein structure
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
