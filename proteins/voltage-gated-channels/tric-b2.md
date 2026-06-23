---
title: C. elegans TRIC-B2 Channel
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature19767]
verified: false
---

# C. elegans TRIC-B2 Channel

## Overview

TRIC-B2 is an intracellular cation channel from Caenorhabditis elegans belonging to the Trimeric Intracellular Cation (TRIC) channel family. It forms a symmetrical homotrimeric complex with endogenous phosphatidylinositol-4,5-biphosphate ([PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/)) lipid molecules. Each monomer contains seven transmembrane helices (M1-7) with a 3+3+1 organization pattern and an hourglass-shaped hydrophilic pore. TRIC-B2 shares 57% sequence identity with [C. elegans TRIC-B1 Channel](/xray-mp-wiki/proteins/voltage-gated-channels/tric-b1/) and 34% identity with human TRIC-B. It was solved in the Ca2+-free state at 2.3 A resolution, providing a structural basis for understanding Ca2+-induced conformational changes when compared with the Ca2+-bound [C. elegans TRIC-B1 Channel](/xray-mp-wiki/proteins/voltage-gated-channels/tric-b1/) structure.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature19767 | 5EIK | 2.3 A | R32 | CeTRIC-B2 (residues 1-252), C. elegans, Myc and 6His tags removed | [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) (phosphatidylinositol-4,5-biphosphate), Ca2+-free state |
| doi/10.1038##nature19767 | 5EIK (NaAc data) | 2.3 A | R32 | CeTRIC-B2 (residues 1-252), C. elegans | [Sodium Acetate](/xray-mp-wiki/reagents/buffers/sodium-acetate/) crystallization condition |

## Expression and Purification

- **Expression system**: Pichia pastoris
- **Construct**: Gene encoding TRIC-B2 from C. elegans (UniProt: Q9NA73) was synthesized with optimized codon usage for expression in Pichia pastoris. Target cDNA was inserted between EcoRI/XhoI sites of pPICZ-C vector with C-terminal fusion of c-Myc epitope and 6His tag. For crystallization, 61 amino acid residues at the flexible C-terminal region plus the Myc epitope were truncated, yielding residues 1-252 covering the transmembrane domain. Expression vectors linearized with PmeI and transformed into P. pastoris GS115 strain by electroporation.


### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | High-pressure homogenization | -- | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) (pH 8.0), 150 mM KCl + -- | Frozen cell pellets suspended 1:10 (m:v), homogenized with T10 basic homogenizer, passed through high-pressure homogenizer at 1300 bar, 4 times |
| Membrane collection and solubilization | Centrifugation and detergent solubilization | -- | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) (pH 8.0), 150 mM KCl + Triton X-100 (1.5% v/v final concentration) | Cell lysate stirred at room temperature for 2 h, insoluble debris removed by centrifugation at 37044g for 1 h |
| Cobalt [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Affinity purification | [TALON](/xray-mp-wiki/reagents/additives/talon/) cobalt affinity beads (BD Science), 1 ml resin/30 g cell pellet | 150 mM KCl, 25 mM HEPES (pH 7.5), 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 0.5% beta-DM + 0.5% [DM](/xray-mp-wiki/reagents/detergents/dm/) (beta-DM, Anatrace) | Pre-equilibrated resin, 1-h incubation at room temperature, washed with 5 column volumes of buffer A (150 mM KCl, 25 mM HEPES pH 7.5) |
| Elution | Affinity elution | [TALON](/xray-mp-wiki/reagents/additives/talon/) beads | 150 mM KCl, 25 mM HEPES (pH 7.5), [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) gradient + 0.5% beta-DM | Elution via [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) gradient |


## Crystallization

### doi/10.1038##nature19767

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | CeTRIC-B2 (residues 1-252) in beta-DM with endogenous [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) |
| Reservoir | [Sodium Acetate](/xray-mp-wiki/reagents/buffers/sodium-acetate/) |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Ca2+-free state (no CaCl2 added) |
| Notes | Space group R32, cell dimensions a=b=126.34 A, c=135.57 A. Wavelength 1.5306 A, resolution 43-2.3 A (shell 2.38-2.3), Rmerge 11.6% (73.0%), Rpim 5.9% (36.6%), I/sigmaI 8.6 (2.0), completeness 99.2% (99.4%), redundancy 5.4. The structure was solved in the Ca2+-free state, providing a structural baseline for comparison with the Ca2+-bound [C. elegans TRIC-B1 Channel](/xray-mp-wiki/proteins/voltage-gated-channels/tric-b1/) structure. Mass spectrometry confirmed the presence of multiple [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) species (34:0, 34:1, 34:2, 34:3, 36:1, 36:2, 36:3, 36:8) in the purified protein sample. |


## Biological / Functional Insights

### Ca2+-free structure reveals open cytoplasmic vestibule

The Ca2+-free TRIC-B2 structure (2.3 A) reveals the conformation of the cytoplasmic vestibule and M5-6 loop in the absence of calcium binding. The M5-6 loop in TRIC-B2 adopts a different conformation compared to the Ca2+-bound [C. elegans TRIC-B1 Channel](/xray-mp-wiki/proteins/voltage-gated-channels/tric-b1/) structure, with the His186-Asp50 pair (TRIC-B2) versus Asn185-Ala49 pair ([C. elegans TRIC-B1 Channel](/xray-mp-wiki/proteins/voltage-gated-channels/tric-b1/)) at the monomer interface. Superposition of TRIC-B2 on [C. elegans TRIC-B1 Channel](/xray-mp-wiki/proteins/voltage-gated-channels/tric-b1/) reveals dramatic conformational differences, particularly in the M5-6 loop region which swings towards the pore upon Ca2+ binding. The [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) head group is more accessible in the Ca2+-free state.

### Structural comparison with TRIC-B1 reveals gating mechanism

[C. elegans TRIC-B1 Channel](/xray-mp-wiki/proteins/voltage-gated-channels/tric-b1/) and TRIC-B2 share similar overall structures with RMSD of C-alpha atoms at 1.1 A. However, key differences in the M5-6 loop and cytoplasmic vestibule regions reveal the Ca2+-dependent gating mechanism. In TRIC-B2, the Ca2+ binding site at the trimeric center is unoccupied, and the Trp180 residues (Ser70 at the M5 kink position) adopt a different conformation. The Ca2+-free structure provides the baseline conformation for the proposed three-state gating model.

### PIP2 binding in the Ca2+-free state

Mass spectrometry analysis confirmed that the TRIC-B2 protein sample contains multiple [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) species (34:0, 34:1, 34:2, 34:3, 36:1, 36:2, 36:3, 36:8). In the Ca2+-free state, [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) binds to the same site as in [C. elegans TRIC-B1 Channel](/xray-mp-wiki/proteins/voltage-gated-channels/tric-b1/), with its head group located on the surface of the cytoplasmic vestibule of the pore. The PIP2-binding residues are highly conserved among TRIC-A and TRIC-B homologues from various species including Homo sapiens, Mus musculus, Gallus gallus, Danio rerio, Xenopus tropicalis, and Caenorhabditis elegans.


## Cross-References

- [Phosphatidylinositol](/xray-mp-wiki/reagents/lipids/phosphatidylinositol/) — PIP2 is a phosphorylated derivative of phosphatidylinositol; mass spectrometry confirmed multiple PIP2 species in TRIC-B2 sample
- [Decylmaltoside (DM)](/xray-mp-wiki/reagents/detergents/dm/) — Primary detergent (beta-DM, 0.5%) used throughout purification and crystallization of TRIC-B2
- [Triton X-100](/xray-mp-wiki/reagents/detergents/triton-x-100/) — Used at 1.5% for solubilization of membrane proteins from P. pastoris cell lysate
- [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer component (25 mM, pH 7.5) used in purification buffers
- [C. elegans TRIC-B1 Channel](/xray-mp-wiki/proteins/voltage-gated-channels/tric-b1/) — Ca2+-bound counterpart (3.3 A); structural superposition reveals Ca2+-induced gating mechanism
- [KcsA Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) — Structural comparison with canonical tetrameric K+ channel (KcsA, PDB 1BL8) highlights unique TRIC architecture
- [KirBac Potassium Channels](/xray-mp-wiki/proteins/voltage-gated-channels/kirbac-potassium-channels/) — Homologous prokaryotic potassium channel; PIP2 binding compared with Kir2.2 channel
- [Tris-HCl](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component (50 mM, pH 8.0) used in cell lysis buffer
- [Allosteric Regulation in Membrane Proteins](/xray-mp-wiki/concepts/allosteric-regulation/) — Ca2+-induced conformational change in M5-6 loop allosterically affects pore gating via PIP2 interaction
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
