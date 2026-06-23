---
title: TmrAB Heterodimeric ABC Transporter from Thermus thermophilus
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1073##pnas.1620009114]
verified: false
---

# TmrAB Heterodimeric ABC Transporter from Thermus thermophilus

## Overview

TmrAB (TmrA/TmrB) from *Thermus thermophilus* is a heterodimeric ABC half-transporter that serves as a structural and functional homolog of the human transporter associated with antigen processing (TAP). It is a multidrug resistance protein that transports peptides, fluorophores, and potentially lipids. TmrAB shares 27-30% sequence identity with human TAP1/TAP2 and can restore antigen processing in human TAP-deficient cells. The 2.7-Å crystal structure reveals an asymmetric inward-facing conformation with a single catalytically active ATP-binding site, making it a model system for asymmetric ABC exporters.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1620009114 |  | 2.7 | — | Full-length TmrA (TTC0976) and TmrB (TTC0977) |  |

## Expression and Purification

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: Full-length TmrA and TmrB co-expressed
- **Notes**: SeMet-labeled protein prepared using [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) Expression Media. Detailed cloning described in Materials and Methods.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | French press | — | 20 mM Hepes pH 7.5, 300 mM NaCl | Lysozyme and DNase I added. Cell debris removed by centrifugation at 10,000 x g. |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | His-tag purification | — |  | Details of purification described in Materials and Methods |
| Size-exclusion chromatography | SEC | — |  | Detailed in Materials and Methods |

**Final sample**: Purified TmrAB in 20 mM Hepes pH 7.5, 140 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/)


## Crystallization

No crystallization described.

## Biological / Functional Insights

### Functional TAP Homolog

TmrAB shares 27-30% sequence identity with human TAP1/TAP2 and can restore MHC-I surface expression in TAP1-deficient human fibroblast cells. It transports peptides (optimal length ~7-9 aa) with broad specificity, concentrating substrates up to 4,000-fold in liposomes.

### Asymmetric Inward-Facing Conformation

The 2.7-Å crystal structure reveals a unique asymmetric inward-facing state. TmrAB has only one catalytically active ATP-binding site (in TmrA). The C-terminal zipper helices rearrange during NBD closure and are essential for efficient transport.

### Periplasmic Gate Dynamics

PELDOR/DEER spectroscopy shows the periplasmic gate opens ~20 Å in detergent and ~35 Å in lipid bilayers upon vanadate trapping (mimicking the ATP hydrolysis transition state). Only the ATP hydrolysis transition state drives outward-facing conformation, unlike homodimeric ABC transporters.

### Broad Substrate Specificity

TmrAB transports peptides (7-35 aa), fluorophores (fluorescein), and may function as a lipid flippase. Activity is modulated by lipid composition, with 30% [Phosphatidylglycerol](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol/) essential for activity. The binding cavity is chemically heterogeneous: TmrA contributes charged residues, TmrB contributes hydrophobic residues.

### Lateral Lipid Entry Gate

TM4 and TM6 of TmrB form a laterally open V-shaped gate at the inner membrane leaflet for membrane-embedded substrate access. Five arginines (R177, R181, R185, R186, R188) line the rim, providing a positively charged groove for phospholipid headgroups. MD simulations confirm [POPE](/xray-mp-wiki/reagents/lipids/pope/) and [POPG](/xray-mp-wiki/reagents/lipids/popg/) binding at this site.

### Zipper Helix Mechanism

The C-terminal helices of TmrA and TmrB form a zipper-like structure that plays a crucial role in guiding conformational changes during substrate transport. Deletion of the zipper helix (Δzipper) significantly reduces transport activity without affecting K_m, indicating a role in turnover rather than substrate binding.


## Cross-References

- [ABC Transporter Family](/xray-mp-wiki/concepts/abc-transporter-family/) — TmrAB is a heterodimeric ABC exporter and member of the ABC transporter superfamily
- [ABC Transporter Allosteric Regulation](/xray-mp-wiki/concepts/abc-transporter-allosteric-regulation/) — TmrAB exhibits asymmetric ATP hydrolysis with one degenerate nucleotide-binding site
- [Conformational Asymmetry in ABC Transporters](/xray-mp-wiki/concepts/conformational-asymmetry-abc-transporters/) — TmrAB structure reveals asymmetric inward-facing state with C-terminal zipper helices
- [Buffer HEPES](/xray-mp-wiki/reagents/buffers/hepes/) — Used in purification and reconstitution buffers for TmrAB
- [POPE (1-Palmitoyl-2-Oleoyl-Phosphatidylethanolamine)](/xray-mp-wiki/reagents/lipids/pope/) — Used in MD simulations and lipid modulation studies of TmrAB
- [POPG (1-Palmitoyl-2-Oleoyl-Phosphatidylglycerol)](/xray-mp-wiki/reagents/lipids/popg/) — Used in MD simulations; 30% PG essential for TmrAB activity
- [POPC (1-Palmitoyl-2-Oleoyl-Phosphatidylcholine)](/xray-mp-wiki/reagents/lipids/popc/) — Used in liposome reconstitution for TmrAB transport assays
- [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) — Used as a minor component (5 mol%) in liposome reconstitution
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
