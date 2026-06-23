---
title: C. elegans TRIC-B1 Channel
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature19767]
verified: false
---

# C. elegans TRIC-B1 Channel

## Overview

TRIC-B1 is an intracellular cation channel from Caenorhabditis elegans belonging to the Trimeric Intracellular Cation (TRIC) channel family. It forms a homotrimeric complex with endogenous phosphatidylinositol-4,5-biphosphate ([PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/)) lipid molecules. Each monomer contains an hourglass-shaped hydrophilic pore within a seven-transmembrane-helix domain. The channel is permeable to monovalent cations (K+ or Na+) and displays Ca2+-dependent gating behavior. Structural and functional analyses reveal the central role of [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) in stabilizing the cytoplasmic gate and a marked Ca2+-induced conformational change in a cytoplasmic loop above the gate.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature19767 | 5EGI | 3.3 A | P41212 | CeTRIC-B1 (residues 1-247), C. elegans, Myc and 6His tags removed | [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) (phosphatidylinositol-4,5-biphosphate), Ca2+ bound at trimeric center |
| doi/10.1038##nature19767 | 5EIG (SAD derivative) | 3.9 A | C2221 | CeTRIC-B1 (residues 1-247), C. elegans, [Methylmercury Chloride](/xray-mp-wiki/reagents/additives/methylmercury-chloride/) derivative for SAD phasing | CH3HgCl derivative |

## Expression and Purification

- **Expression system**: Pichia pastoris
- **Construct**: Genes encoding TRIC-B1 from C. elegans (UniProt: Q9NA75) were synthesized with optimized codon usage. Target cDNA was inserted between EcoRI/XhoI sites of pPICZ-A vector with C-terminal fusion of c-Myc epitope and 6His tag. For crystallization, 48 amino acid residues at the flexible C-terminal region plus the Myc epitope were truncated, yielding residues 1-247 covering the transmembrane domain. Point mutations introduced via Quikchange site-directed mutagenesis. Expression vectors linearized with PmeI and transformed into P. pastoris GS115 strain by electroporation.


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
| Protein sample | CeTRIC-B1 (residues 1-247) in beta-DM with endogenous [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) |
| Reservoir | Not specified in paper |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Ca2+ bound (CaCl2 present during crystallization) |
| Notes | Space group P41212, cell dimensions a=b=102.05 A, c=279.99 A. Wavelength 1.1000 A, resolution 32-3.3 A (shell 3.42-3.3), Rmerge 11.5% (80.4%), Rpim 3.7% (25.8%), I/sigmaI 11.1 (2.8), completeness 99.9% (100.0%), redundancy 10.5. SAD derivative (5EIG): space group C2221, [Methylmercury Chloride](/xray-mp-wiki/reagents/additives/methylmercury-chloride/) derivative, wavelength 1.0073 A, resolution 46-3.9 A, Rmerge 11.7% (98.1%), completeness 99.6% (100%), redundancy 13.7. |


## Biological / Functional Insights

### PIP2-dependent cytoplasmic gate stabilization

[PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) acts as a lipid cofactor necessary for regulating the channel function. Its head group binds directly to conserved basic amino acid residues from TRIC-B1 and is located on the surface of the cytoplasmic vestibule of the pore. [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) binding stabilizes the closed state of the cytoplasmic gate. The PIP2-binding site is buried inside each monomer, distinct from the peripheral binding seen in Kir channels. Mutation of PIP2-binding residues (K129A/R133L) abolishes [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) binding and impairs channel function, as shown by fluorescence-based K+ flux assays and single-channel electrophysiology.

### Homotrimeric architecture with hourglass-shaped pore

TRIC-B1 forms a symmetrical homotrimer with a C3 axis running through its center and perpendicular to the membrane plane. Each monomer contains seven transmembrane helices (M1-7) with a 3+3+1 organization pattern: M1-3 and M4-6 form inverted repeats, while M7 is standalone and fills the crevice between M4 and M6. The ion permeation pathway traverses through the central pore within each monomer, not along the trimeric C3 axis. The pore has an hourglass shape with two bottlenecks near lysine residues and the [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) molecule. Pore-lining residues Met38, Ala126, and Ser166 (on M1, M4, and M5) were confirmed by cysteine accessibility testing with [MTSET](/xray-mp-wiki/reagents/additives/mtset/).

### Ca2+-induced conformational change in M5-6 loop

TRIC-B1 contains a Ca2+ binding site at the trimeric center, surrounded by three Trp180 residues. Upon Ca2+ binding, Trp180 switches its side chain rotamer to form a cradle-like pocket measuring ~13 A wide. Accompanying the rotamer switch, the M5-6 loop swings towards the pore region and covers the [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) head group. This conformational change was verified by disulfide-cross-linking experiments with A49C/N185C mutant. Mutation of Trp180 to Ala abolishes Ca2+ sensitivity. The M5-6 loop fences the cytoplasmic entrance of the pore and presents a patch of electronegative surface.

### Multi-state gating mechanism

Single-channel electrophysiology reveals multiple open states (O1, O2, O3) corresponding to one, two, or three monomers being open within the trimer. Wild-type TRIC-B1 shows fast transition from closed to the third open state, while the K129A/R133L mutant shows stepwise opening with dwelling on intermediate states. The channel exhibits voltage-dependent gating with sensitivity to Ca2+ applied on the cytosolic side (stimulated) and luminal side (inhibited). A mechanistic model proposes M5-6 loop as the Ca2+-sensing motif and M4 as the potential voltage-sensing helix.


## Cross-References

- [Phosphatidylinositol](/xray-mp-wiki/reagents/lipids/phosphatidylinositol/) — PIP2 is a phosphorylated derivative of phosphatidylinositol; structural comparison with Kir channels shows different PIP2-binding modes
- [Decylmaltoside (DM)](/xray-mp-wiki/reagents/detergents/dm/) — Primary detergent (beta-DM, 0.5%) used throughout purification and crystallization of TRIC-B1
- [Triton X-100](/xray-mp-wiki/reagents/detergents/triton-x-100/) — Used at 1.5% for solubilization of membrane proteins from P. pastoris cell lysate
- [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer component (25 mM, pH 7.5) used in purification buffers
- [KcsA Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) — Structural comparison with canonical tetrameric K+ channel (KcsA, PDB 1BL8) used to highlight unique TRIC architecture
- [KirBac Potassium Channels](/xray-mp-wiki/proteins/voltage-gated-channels/kirbac-potassium-channels/) — Homologous prokaryotic potassium channel; PIP2 binding compared with Kir2.2 channel
- [Tris-HCl](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component (50 mM, pH 8.0) used in cell lysis buffer
- [Allosteric Regulation in Membrane Proteins](/xray-mp-wiki/concepts/structural-mechanisms/allosteric-regulation/) — Ca2+-induced conformational change in M5-6 loop allosterically affects pore gating via PIP2 interaction
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
