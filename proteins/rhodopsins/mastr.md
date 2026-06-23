---
title: MastR (Mastigocladopsis repens Rhodopsin)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1074##jbc.RA120.014118]
verified: false
---

# MastR (Mastigocladopsis repens Rhodopsin)

## Overview

MastR (Mastigocladopsis repens rhodopsin, also known as MrHR) is a cyanobacterial chloride-pumping microbial rhodopsin representing the third group of known anion pumps with a characteristic Thr-Ser-Asp (TSD) motif in the ion transport pathway. The crystal structure was determined at 2.33 A resolution using the [Bicelle Crystallization](/xray-mp-wiki/methods/crystallization/bicelle-crystallization/) method, revealing a trimeric arrangement reminiscent of [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) (BR)-like proton pumps. The structure shows two chloride ion-binding sites: a primary site adjacent the protonated [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) Schiff base (PRSB) coordinated by Thr-74 and Ser-78 of the TSD motif, and a secondary crystal-contact site. The MastR-T74D mutant structure (2.50 A) converts the chloride pump into an efficient proton pump by replacing the chloride ion with the carboxylate side chain of Asp-74, maintaining the extended hydrogen-bonding network required for outward proton transport. The strong structural similarity between MastR and BR explains why functional conversion from Cl- to H+ pump is possible for MastR but not for archaeal halorhodopsins.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1074##jbc.RA120.014118 | 6X13 | 2.33 A | not specified | Full-length MastR with C-terminal hexahistidine tag (wild-type, chloride pump) | all-trans-[Retinal](/xray-mp-wiki/reagents/ligands/retinal/), chloride ion |
| doi/10.1074##jbc.RA120.014118 | 6WP8 | 2.50 A | not specified | MastR T74D mutant with C-terminal hexahistidine tag (proton pump) | all-trans-[Retinal](/xray-mp-wiki/reagents/ligands/retinal/) |

## Expression and Purification

- **Expression system**: Escherichia coli C43(DE3)
- **Construct**: Full-length MastR with C-terminal His6 tag in pET21a(+)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Emulsiflex C3 homogenizer | — | 50 mM MES pH 6.5, 300 mM NaCl, protease inhibitor cocktail |  |
| Membrane preparation | Ultracentrifugation | — |  | Crude membranes pelleted at 125,000 x g for 1 h |
| Solubilization | Detergent solubilization | — | 50 mM MES pH 6.5, 300 mM NaCl + 2% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |  |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | HisTrap 1 mL Ni-NTA | 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 50 mM MES pH 6.5, 300 mM NaCl | Detergent exchanged to 2% OG during wash before elution |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | — | 10 mM MES pH 6.5, 300 mM NaCl, 0.8% OG | Purity >95% by SDS-PAGE (A537nm/A280nm > 0.6) |


## Crystallization

### doi/10.1074##jbc.RA120.014118

| Parameter | Value |
|---|---|
| Method | [Bicelle Crystallization](/xray-mp-wiki/methods/crystallization/bicelle-crystallization/) |
| Reservoir | 24% [PEG 2000](/xray-mp-wiki/reagents/additives/peg2000/) MME, 100 mM sodium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) pH 5.0, 200 mM [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/) |
| Temperature | 20°C |
| Notes | Bicelles composed of DMPC-[CHAPSO](/xray-mp-wiki/reagents/detergents/chapso/) (2.8:1 ratio, 24% w/v). Crystals grown in hanging drops |


## Biological / Functional Insights

### TSD motif and chloride binding

The primary chloride ion is coordinated by Thr-74 and Ser-78 of the TSD motif (d(Cl-O) = 3.1 A and 3.0 A, respectively) and connected via a bridging water molecule (d(Cl-O) = 3.1 A) to the PRSB (d = 2.8 A) and the carboxyl group of Asp-200. The T74A mutation reduced chloride affinity from KD 2 mM to 85 mM, while S78T decreased affinity ~200-fold.

### BR-like trimeric assembly

MastR forms trimers in the crystal and in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) micelles (as shown by CD spectroscopy with bilobed spectra showing a positive peak at ~510 nm and negative at ~560 nm relative to 540 nm lambda-max). The trimer interface involves helix B interacting with helices D' and E' of adjacent protomers. Unlike eubacterial pumps, MastR lacks pentamer-inducing structural features (extended helix B and 3-omega motif).

### Functional conversion via T74D mutation

The MastR-T74D mutation converts the chloride pump into an efficient proton pump. The carboxylate side chain of Asp-74 fills the space occupied by Cl- in wild-type, maintaining the extended hydrogen-bonding network. The BR-like structure of MastR, including proper positioning of the Schiff base water and Ala-53 equivalent, enables this conversion, unlike archaeal halorhodopsins where similar mutations fail.

### Chloride transport pathway

The putative chloride entrance is between the B-C and F-G loops, gated by Glu-192 and Glu-182 (homologous to BR's proton-release pathway Glu-204/Glu-194). After photoisomerization, the chloride ion moves toward the cytoplasmic side, with His-166 identified as part of the chloride release pathway (H166A mutation slows photocycle >10-fold). Asp-85 deprotonation accompanies chloride translocation, with reprotonation preventing backflow.


## Cross-References

- [Pharaonis Halorhodopsin (NpHR)](/xray-mp-wiki/proteins/rhodopsins/pharaonis-halorhodopsin/) — Both are chloride-pumping microbial rhodopsins with similar chloride-binding motif
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — MastR shows closest structural homology to BR, with BR-like trimeric assembly and overall fold
- [CIR (Nonlabens marinus)](/xray-mp-wiki/proteins/rhodopsins/cir-nonlabens-marinus/) — CIR represents the eubacterial group of chloride-pumping rhodopsins, distinct from MastR's cyanobacterial group
- [DTG/DTS Rhodopsin Motif](/xray-mp-wiki/concepts/dtg-dts-rhodopsin/) — MastR contains a TSD motif, related to the function-determining motifs in ion-pumping rhodopsins
- [Bicelle Crystallization](/xray-mp-wiki/methods/crystallization/bicelle-crystallization/) — Method used in structure determination or purification
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Method used in structure determination or purification
- [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [PEG 2000](/xray-mp-wiki/reagents/additives/peg2000/) — Additive used in purification or crystallization buffers
