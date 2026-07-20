---
title: "Triton X-100"
created: 2026-06-11
updated: 2026-06-23
type: reagent
category: reagents
layout: default
tags: [detergent-nonionic, solubilization-detergent, subdirectory-detergents]
sources: [doi/10.1016##j.jmb.2007.10.014, doi/10.1016##j.str.2012.11.010, doi/10.1016##j.str.2016.04.003, doi/10.1038##nature11744]
verified: agent
---

# Triton X-100

## Overview

Triton X-100 is a nonionic octylphenyl polyethoxylate detergent used for solubilizing membrane proteins and dissolving cellular membranes. In GlpG Rhomboid Intramembrane Protease (E. coli) studies, Triton X-100 was used at 1% to dissolve spheroplast membranes and expose all cysteine residues on the protein surface for AMS modification studies. It can also alter the temporal sequence of light-driven proton release in Archaerhodopsin-2 (aR2) when used for solubilization.


## Properties

- **Chemical name**: octylphenoxypolyethoxyethanol
- **Chemical formula**: C14H22O(C2H4O)n
- **Molecular weight**: ~647 g/mol (n ~9.5)
- **Class**: nonionic octylphenyl polyethoxylate
- **CMC**: 0.010-0.016 % w/v
- **Head group**: polyethylene glycol chain
- **Tail length**: octylphenyl group

## Use in Membrane Protein Work

### Membrane solubilization for accessibility studies

1% Triton X-100 was used to dissolve spheroplast membranes in GlpG Rhomboid Intramembrane Protease (E. coli) L1 loop accessibility studies, allowing all cysteine residues on the protein surface to become modifiable by AMS (2-acetamido-3-(maleimido)propanesulfonic acid). This confirmed that all L1 loop cysteine mutants are exposed on the protein surface when the membrane is dissolved.


### Protein solubilization for functional studies

Triton X-100 was used to solubilize Archaerhodopsin-2 (aR2) for functional studies. Solubilization with Triton X-100 was found to revert the temporal sequence of light-induced proton uptake and release, suggesting that trimeric assembly is required for normal proton pump kinetics.


### Membrane protein complex purification

Triton X-100 was used at 3% w/v to solubilize Escherichia coli membrane proteins containing EcHyd-1 and its cytochrome b partner. Cell membrane proteins at 10 mg/ml were stirred overnight at 4 deg.C. The partially purified sample was then subjected to Superdex 200 gel filtration in 0.02% Triton X-100 buffer in an anaerobic glove box.


## Examples from This Wiki

| Protein | Concentration | Context | Result |
|---|---|---|---|
| GlpG Rhomboid Intramembrane Protease (E. coli) | 1% | 1% Triton X-100 used to dissolve spheroplast membranes in GlpG L1 loop accessibility studies
 | All L1 loop cysteine mutants exposed on protein surface |
| Archaerhodopsin-2 | not specified | Triton X-100 used to solubilize aR2 for functional studies | Reverted temporal sequence of light-induced proton uptake and release |
| Escherichia coli Hydrogenase 1 (EcHyd-1) | 3% (solubilization), 0.02% (SEC) | Triton X-100 used for membrane solubilization of EcHyd-1-cytochrome b complex
 | Partially purified sample subjected to Superdex 200 gel filtration |
| [bcMalT (Bacillus cereus Maltose Transporter)](/xray-mp-wiki/proteins/enzymes/bc-malt/) | 0.12% (w/w) | Triton X-100 used in proteoliposome preparation for bcMalT functional assays. Preformed liposomes (E. coli polar lipid extract) destabilized with 0.12% Triton X-100 before bcMalT reconstitution at 1:100 (w/w) ratio.
 | bcMalT reconstituted into proteoliposomes for [3H]-maltose uptake measurements by facilitated diffusion |

## Advantages and Disadvantages

### Advantages

- Highly effective for initial membrane solubilization - efficiently dissolves cellular membranes and exposes all protein surface residues for biochemical modification studies, as demonstrated for GlpG rhomboid protease L1 loop accessibility studies.
- Low cost and widely available compared to specialized detergents like LMNG or DDM, making it suitable for large-scale membrane preparations and initial extraction steps.
- Compatible with subsequent detergent exchange protocols - proteins initially solubilized in Triton X-100 can be exchanged into milder detergents for downstream purification and crystallization.

### Disadvantages

- Strong solubilizing properties can denature sensitive membrane proteins and disrupt protein-protein interactions, as the harsh hydrophobic interactions may extract lipids essential for protein stability.
- High UV absorbance at 280 nm due to the aromatic ring in the octylphenyl group interferes with standard protein concentration measurements by spectrophotometry.
- Not suitable for crystallography due to polydispersity and large micelle size - must be exchanged for milder, crystallography-compatible detergents like DDM, LMNG, or OG before crystallization trials.
- Environmental and regulatory concerns - Triton X-100 is classified as a substance of very high concern (SVHC) under REACH due to the persistence of its degradation product, 4-tert-octylphenol.

## Comparison with Related Reagents

| detergent | comparison |
|---|---|
| DDM (n-Dodecyl-beta-D-maltopyranoside) | DDM is a milder, non-denaturing alternative to Triton X-100 for membrane protein solubilization. While Triton X-100 is more effective at extracting proteins from membranes, DDM is preferred for maintaining native protein conformation and is compatible with crystallography. DDM has low UV absorbance, unlike Triton X-100. |
| LMNG (Lauryl Maltose Neopentyl Glycol) | LMNG provides superior stabilization for GPCRs and other sensitive membrane proteins compared to Triton X-100. Triton X-100 is more aggressive in solubilization but often denatures GPCRs, while LMNG maintains receptor activity and enables high-resolution structure determination. Triton X-100 is significantly less expensive. |
| OG (n-Octyl-beta-D-glucopyranoside) | OG is a short-chain detergent commonly used for crystallization of bacterial membrane proteins, while Triton X-100 is primarily used for initial solubilization and functional studies. OG has a very high CMC (~18-20 mM) and is easy to remove by dialysis, unlike Triton X-100 which forms large micelles and is difficult to remove. |

## Cross-References

- [GlpG Rhomboid Protease](/xray-mp-wiki/proteins/enzymes/glpg/) — Used at 1% for membrane solubilization in L1 loop accessibility studies
- [Archaerhodopsin-2](/xray-mp-wiki/proteins/rhodopsins/archaerhodopsin-2/) — Related archaeal rhodopsin; Triton X-100 solubilization affects proton pump kinetics
- [Escherichia coli Hydrogenase 1 (EcHyd-1)](/xray-mp-wiki/proteins/enzymes/ec-hyd-1/) — Used at 3% for membrane solubilization of EcHyd-1-cytochrome b complex
