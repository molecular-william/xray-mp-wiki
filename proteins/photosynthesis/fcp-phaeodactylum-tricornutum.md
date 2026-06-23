---
title: Fucoxanthin Chlorophyll a/c-Binding Protein (FCP) from Phaeodactylum tricornutum
created: 2026-06-10
updated: 2026-06-10
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.aav0365]
verified: false
---

# Fucoxanthin Chlorophyll a/c-Binding Protein (FCP) from Phaeodactylum tricornutum

## Overview

 chlorophyll a/c-binding protein (FCP) is a light-harvesting antenna protein from the marine diatom *Phaeodactylum tricornutum*. FCPs belong to the superfamily of transmembrane light-harvesting complex (LHC) proteins and contain the pigments Chl a, Chl c, and  (Fx), enabling them to absorb light in the blue-green region that penetrates underwater. The structure of Lhcf4 was solved as a homodimer at 1.8-Å resolution, revealing a unique pigment arrangement with nine Chls (seven Chl a, two Chl c), seven Fxs, and one diadinoxanthin (Ddx) per monomer. Unlike the trimeric LHCII of green plants, FCP forms a dimer stabilized by interactions between transmembrane C helices. FCPs display robust [Non-photochemical Quenching (NPQ) in LHC-II](/xray-mp-wiki/concepts/miscellaneous/non-photochemical-quenching/) (NPQ) via the Ddx-Dtx xanthophyll cycle, providing photoprotection under fluctuating light conditions in the ocean surface layer.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.aav0365 | TBD | 1.8 | TBD | Lhcf4 (residues 1-166 of 167 total); native FCP dimer from Phaeodactylum tricornutum | Chl a (x7), Chl c (x2), Fx (x7), Ddx (x1), phosphatidyl- (x1),  (x1), [OTG](/xray-mp-wiki/reagents/detergents/og/), a-, Ca2+ (x2) |

## Expression and Purification

- **Expression system**: Native Phaeodactylum tricornutum cells
- **Construct**: Native Lhcf4 (product of lhcf3/lhcf4 genes, 167 residues)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and harvest | Glass bead disruption | — | 20 mM tricine, 10 mM , 20 mM KCl, 5% , pH 7.8 (TMKS buffer) |  |
| Thylakoid membrane isolation | Centrifugation | — | TMKS buffer | 100,000 x g for 20 min at 4 C |
| Membrane solubilization | Detergent solubilization | — | 1% (w/v) n-dodecyl-alpha-D-maltopyranoside (alpha-) | 0.5 mg Chl a/ml for 30 min on ice |
| Anion exchange chromatography (1st column) | [Ion-Exchange Chromatography](/xray-mp-wiki/methods/ion-exchange-chromatography/) | Q-Sepharose HP | TMKS buffer with 0.03% alpha- | Wash with 0.25 M NaCl; elute with 0.25-0.42 M NaCl gradient; Lhcf4 elutes at 0.35-0.38 M NaCl |
| Anion exchange chromatography (2nd column) | [Ion-Exchange Chromatography](/xray-mp-wiki/methods/ion-exchange-chromatography/) | Q-Sepharose HP | TMKS buffer with 0.03% alpha- | Same conditions as first column to increase purity |
|  gradient centrifugation | Density gradient centrifugation | — | TMK buffer with 0.03% alpha- | 5-20% linear  gradient, 303,800 x g for 16 h |


## Crystallization

### doi/10.1126##science.aav0365

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified FCP dimer in TMK buffer with 0.03% alpha- |
| Temperature | 4 |
| Notes | Crystals diffracted to 1.8 A resolution. Phasing by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using PHASER with an LHCII search model, followed by extension to 1.8 A. |


## Biological / Functional Insights

### FCP forms a homodimer via C-helix interactions

Unlike the trimeric LHCII from green plants, FCP from P. tricornutum forms a homodimer. Two monomers are held together by hydrophobic interactions between their transmembrane C helices. The N-terminal "WYGPDR" motif and C-terminal Trp residue crucial for LHCII trimer formation are absent in Lhcf4, explaining the dimeric assembly. The N- and C-termini and loop regions are shorter in FCP compared to LHCII, and helix D found at the lumenal surface in LHCII is absent.

### Unique pigment composition enables blue-green light harvesting

Each FCP monomer binds nine Chls (seven Chl a, two Chl c) and seven Fxs, giving a much higher Fx/Chl ratio than LHCI and LHCII. The two Chl c molecules are located at opposing sides of transmembrane helices A and B, in close interaction with nearby Chls a and Fxs. Each Fx is surrounded by one or more Chls, with pi-pi distances of 4.0 A or less, enabling fast and efficient excitation energy transfer (as fast as 75 fs, >90% efficiency).

### Chl c enables efficient harvesting of the green gap

Chl c absorbs blue-green and even yellow light, which is the "green gap" where Chls a and b absorb weakly. The energy absorbed by Chls c is transferred efficiently to coupled Chls a. The close coupling of Chl c with Chl a and Fx allows Chl c to serve as an efficient harvester of the blue-green light available underwater.

### Diadinoxanthin cycle in energy dissipation

One Ddx molecule is located near the monomer-monomer interface. Its weak electron density suggests easy dissociation and involvement in the Ddx-Dtx de-epoxidation cycle that functions in energy dissipation (NPQ). Luminal acidic residues (Glu54, Asp64, Glu72, Glu82, Glu158) may be involved in pH-induced conformational changes during photoprotection. Two calcium cations coordinated at the lumenal surface may modulate this pH response.


## Cross-References

- [Pea Light-Harvesting Complex II (LHC-II)](/xray-mp-wiki/proteins/photosynthesis/pea-light-harvesting-complex-ii/) — FCP is structurally homologous to LHCII but has unique pigment composition and dimeric assembly
- [Spinach Light-Harvesting Complex II (LHC-II)](/xray-mp-wiki/proteins/photosynthesis/spinach-light-harvesting-complex-ii/) — Comparison of FCP with LHCII reveals differences in pigment binding and oligomeric state
- [Non-photochemical Quenching (NPQ)](/xray-mp-wiki/concepts/miscellaneous/non-photochemical-quenching/) — FCPs exhibit robust NPQ via the Ddx-Dtx xanthophyll cycle for photoprotection under high light
- [Lutein](/xray-mp-wiki/reagents/ligands/lutein/) — Lutein-binding sites in LHCII correspond to Fx303 and Fx305 positions in FCP
- [Fucoxanthin](/xray-mp-wiki/reagents/fucoxanthin/) — Referenced in fcp-phaeodactylum-tricornutum text
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Referenced in fcp-phaeodactylum-tricornutum text
- [Digalactosyl Diacylglycerol](/xray-mp-wiki/reagents/digalactosyl-diacylglycerol/) — Referenced in fcp-phaeodactylum-tricornutum text
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Referenced in fcp-phaeodactylum-tricornutum text
- [Mgcl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/) — Referenced in fcp-phaeodactylum-tricornutum text
- [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/) — Referenced in fcp-phaeodactylum-tricornutum text
