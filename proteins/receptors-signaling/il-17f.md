---
title: "Interleukin-17F (IL-17F)"
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.immuni.2020.02.004]
verified: false
---

# Interleukin-17F (IL-17F)

## Overview

IL-17F is a secreted cytokine and a member of the IL-17 cytokine family. It forms homodimers and plays a key role in innate and adaptive immune responses, contributing to chronic inflammatory and autoimmune disorders. IL-17F shares structural homology with [IL-17A](/xray-mp-wiki/proteins/receptors-signaling/il-17a/) but has distinct receptor binding properties. Unlike [IL-17A](/xray-mp-wiki/proteins/receptors-signaling/il-17a/), IL-17F forms a symmetrical 2:1 complex with [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) (two receptor chains per cytokine homodimer), competing with the shared co-receptor [IL-17RA](/xray-mp-wiki/proteins/receptors-signaling/il-17ra/) for cytokine binding. IL-17F can also form heterodimers with [IL-17A](/xray-mp-wiki/proteins/receptors-signaling/il-17a/) ([IL-17A](/xray-mp-wiki/proteins/receptors-signaling/il-17a/)/F). The crystal structure of IL-17F in complex with [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) revealed that [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) binding preserves the two-fold symmetry of the cytokine, while [IL-17RA](/xray-mp-wiki/proteins/receptors-signaling/il-17ra/) binding induces large conformational changes that break symmetry.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.immuni.2020.02.004 | 6HGO | not specified | not specified | Human IL-17F, residues 31-163 of UniProt entry Q96PD4, fused to the Myeloid cell surface antigen CD33 signal peptide, with C-terminal APP6-tag (synthetic peptide EFRHDS derived from human Amyloid Precursor Protein) for crystallization
 | -- |
| doi/10.1016##j.immuni.2020.02.004 | 6HG4 | 3.3 A | P321 | Human IL-17F homodimer in complex with [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) ECD (residues 21-467)
 | [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) (2 chains) |
| doi/10.1016##j.immuni.2020.02.004 | 6HG9 | not specified | R32 | Human IL-17F homodimer in complex with [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) ECD (residues 21-467)
 | [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) (2 chains) |

## Expression and Purification

- **Expression system**: HEK293S cells (human embryonic kidney cells deficient in N-acetylglucosaminyl-transferase I)

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Co-expression | Transient co-expression in HEK293S cells | -- | V3 medium (Novartis medium, patent WO 2011/134920 A1) + -- | Co-expression of [IL-17A](/xray-mp-wiki/proteins/receptors-signaling/il-17a/) and IL-17F led to production of [IL-17A](/xray-mp-wiki/proteins/receptors-signaling/il-17a/), IL-17F, and [IL-17A](/xray-mp-wiki/proteins/receptors-signaling/il-17a/)/F heterodimer; cells grown to 3 x 10^6 cells/mL
 |
| Supernatant collection | Supernatant harvesting | -- | -- + -- | Supernatant collected from transfected HEK293S cells; IL-17F expressed as secreted protein with CD33 signal peptide and APP6-tag
 |
| Purification | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) and SEC | -- | -- + -- | IL-17F purified from supernatant; concentrated to 16.5 mg/mL in PBS pH 7.3 for crystallization
 |


## Crystallization

### doi/10.1016##j.immuni.2020.02.004

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Unliganded IL-17F at 16.5 mg/mL in PBS pH 7.3
 |
| Reservoir | 0.2 M [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/), 20% (w/v) [PEG](/xray-mp-wiki/reagents/additives/peg/) 3350 |
| Temperature | 293 K |
| Growth time | not specified |
| Cryoprotection | not specified |
| Notes | Crystals grew in sitting drops; nearly isomorphous to published structure (Hymowitz et al., 2001); structure determined by rigid-body refinement using PDB entry 1JPY
 |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | IL-17F:[IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/)(21-467) complex at 5.1-5.7 mg/mL in PBS pH 7.4, 10 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/)
 |
| Reservoir | 20% (w/v) [PEG](/xray-mp-wiki/reagents/additives/peg/) 3350, 0.2 M ammonium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) tribasic pH 7.0 |
| Temperature | 293 K |
| Growth time | not specified |
| Cryoprotection | Stepwise transfer to mother solution containing 40% (w/v) [PEG](/xray-mp-wiki/reagents/additives/peg/) 1500, flash-cooling in liquid nitrogen
 |
| Notes | Crystal form I, space group P321, diffracted to 3.3 A resolution
 |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | IL-17F:[IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/)(21-467) complex at 5.1-5.7 mg/mL in PBS pH 7.4, 10 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/)
 |
| Reservoir | 20% (w/v) [PEG](/xray-mp-wiki/reagents/additives/peg/) 3350, 0.2 M [Ammonium Formate](/xray-mp-wiki/reagents/additives/ammonium-formate/) |
| Temperature | 293 K |
| Growth time | not specified |
| Cryoprotection | Stepwise transfer to mother solution containing 40% (w/v) [PEG](/xray-mp-wiki/reagents/additives/peg/) 1500, flash-cooling in liquid nitrogen
 |
| Notes | Crystal form II, space group R32
 |


## Biological / Functional Insights

### IL-17F forms a symmetrical 2:1 complex with IL-17RC

IL-17F binds symmetrically to two [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) receptor chains, forming a 2:1 complex. This contrasts with the expected 1:1 asymmetric complex with [IL-17RA](/xray-mp-wiki/proteins/receptors-signaling/il-17ra/). [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) binding preserves the two-fold symmetry of the cytokine and does not shift the beta-hairpins, while [IL-17RA](/xray-mp-wiki/proteins/receptors-signaling/il-17ra/) binding induces large conformational changes that break the symmetry of the IL-17F homodimer.

### IL-17F has three binding sub-sites (S1-S3)

Three main binding sub-sites on IL-17F (S1-S3) are exploited by both [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) and [IL-17RA](/xray-mp-wiki/proteins/receptors-signaling/il-17ra/). S1 is a hydrophobic site bound by Leu47 and Leu49 of [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) (or Leu58 and Trp62 of [IL-17RA](/xray-mp-wiki/proteins/receptors-signaling/il-17ra/)). S2 involves interactions with Tyr132 of [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) R2. S3 includes a buried salt-bridge between Asp281 of [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) and Arg77F. The binding sites overlap extensively between [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) and [IL-17RA](/xray-mp-wiki/proteins/receptors-signaling/il-17ra/).

### IL-17F can signal through IL-17RC independently of IL-17RA

The symmetrical [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/):IL-17F complex provides a structural basis for IL-17RA-independent signaling. IL-17F signaling through [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) induced il33 gene expression in mouse lung epithelial cells in vivo under conditions of [IL-17RA](/xray-mp-wiki/proteins/receptors-signaling/il-17ra/) disruption, suggesting homodimeric [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) signaling complexes can function independently.

### IL-17F has lower biological activity than IL-17A

The much lower biological activity of IL-17F compared to [IL-17A](/xray-mp-wiki/proteins/receptors-signaling/il-17a/) may be a consequence of its poor ability to drive formation of significant amounts of the heteromeric [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/):[IL-17RA](/xray-mp-wiki/proteins/receptors-signaling/il-17ra/) complex. [TR-FRET](/xray-mp-wiki/methods/quality-assessment/tr-fret/) assays showed IL-17F requires approximately 250-fold higher concentrations than [IL-17A](/xray-mp-wiki/proteins/receptors-signaling/il-17a/) to achieve a similar [TR-FRET](/xray-mp-wiki/methods/quality-assessment/tr-fret/) signal.


## Cross-References

- [Interleukin-17 Receptor C (IL-17RC)](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) — Primary receptor forming symmetrical 2:1 complex with IL-17F
- [Interleukin-17 Receptor A (IL-17RA)](/xray-mp-wiki/proteins/receptors-signaling/il-17ra/) — Shared co-receptor that forms asymmetric 1:1 complex with IL-17F
- [Interleukin-17A (IL-17A)](/xray-mp-wiki/proteins/receptors-signaling/il-17a/) — Related cytokine in the IL-17 family; can form heterodimer with IL-17F
- [Homodimeric Signaling](/xray-mp-wiki/concepts/homodimeric-signaling/) — IL-17F drives homodimeric IL-17RC signaling complex
- [Competitive Receptor Binding](/xray-mp-wiki/concepts/competitive-receptor-binding/) — IL-17F binding to IL-17RC competes with IL-17RA binding
- [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) — PEG 3350 used as precipitant in crystallization
- [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/) — Precipitant used for unliganded IL-17F crystallization
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [TR-FRET](/xray-mp-wiki/methods/quality-assessment/tr-fret/) — Method used in structure determination or purification
- [Ammonium Formate](/xray-mp-wiki/reagents/additives/ammonium-formate/) — Additive used in purification or crystallization buffers
