---
title: Mouse Bcs1 (AAA Protein Translocase)
created: 2026-06-17
updated: 2026-06-17
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein]
sources: [doi/10.1038##s41594-020-0373-0]
verified: false
---

# Mouse Bcs1 (AAA Protein Translocase)

## Overview

Bcs1 is a mitochondrial membrane-bound AAA+ ATPase that translocates folded proteins across the mitochondrial inner membrane. Its primary substrate is the Rieske iron-sulfur protein (ISP), a subunit of respiratory Complex III. Unlike canonical AAA unfoldases that thread unfolded polypeptides through a narrow central pore, Bcs1 forms a homo-heptamer that creates a large substrate-binding cavity (~35 A diameter, ~28,000 A^3 volume) sufficient to accommodate folded protein domains. Cryo-EM structures of mouse Bcs1 (mBcs1) in apo, ATPgS-bound, and ADP-bound states reveal a nucleotide-dependent conformational cycle. In the apo/ADP-bound state, the cavity is open and accessible to the mitochondrial matrix, allowing substrate entry. ATP binding drives a concerted contraction of the AAA domains, pushing the substrate across the membrane. This mechanism represents a departure from the threading mechanism of hexameric AAA proteins, making Bcs1 a prototype for a class of AAA translocases that transport folded protein substrates. mBcs1 shares 94% sequence identity with human BCS1L, whose mutations cause GRACILE syndrome and Bjoernstad syndrome.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41594-020-0373-0 | 6UKP | 3.81 |  | Full-length mouse Bcs1 (residues 1-418), apo form |  |
| doi/10.1038##s41594-020-0373-0 | 6UKS | 3.2 |  | Full-length mouse Bcs1 (residues 1-418) with ATPgS and Mg2+ | ATPgS, Mg2+ |
| doi/10.1038##s41594-020-0373-0 | 6U1Y | 2.2 |  | N-terminally truncated mouse Bcs1 (DeltaN mBcs1, residues 151-418) with AMP-PNP | AMP-PNP, Mg2+ |
| doi/10.1038##s41594-020-0373-0 | 6UKO | 4.4 |  | Full-length mouse Bcs1 (residues 1-418) with ADP | ADP |

## Expression and Purification

- **Expression system**: Pichia pastoris (yeast expression system)
- **Construct**: Full-length mouse Bcs1 (residues 1-418) with N-terminal or C-terminal hexahistidine tag in pPICZ A vector

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression and membrane preparation | Pichia pastoris expression with methanol induction for 4 days |  | 100 mM Tris, pH 8, 100 mM sucrose, 1 mM EDTA, 2 mM PMSF | Cells disrupted by Microfluidizer at 2,500 bar for three passages. Crude membranes collected by ultracentrifugation at 125,000g for 1 h. |
| Membrane solubilization | CHAPS detergent solubilization |  | 25 mM potassium phosphate, pH 7.4, 200 mM NaCl, 0.5% CHAPS | 20% CHAPS solution added slowly to 0.5% final concentration with 5 mg/ml final protein concentration at 4 C for 30 min. Insoluble material removed by centrifugation at 125,000g for 30 min. |
| Affinity chromatography | Nickel-nitrilotriacetic acid (Ni-NTA) affinity chromatography | Ni-NTA resin (Qiagen) | 25 mM Tris, pH 8, 300 mM NaCl, 10% glycerol, 10 mM imidazole, 0.1% CHAPS | Bound protein washed and eluted with imidazole gradient. |
| Size-exclusion chromatography | Superdex 200 gel filtration | Superdex 200 | 25 mM Tris, pH 8, 150 mM NaCl, 0.1% CHAPS | Purification yielded homogeneous heptameric mBcs1 as confirmed by BN-PAGE and SEC-MALS. |


## Crystallization

### doi/10.1038##s41594-020-0373-0

| Parameter | Value |
|---|---|
| Method | Cryo-EM single-particle analysis |
| Protein sample | Full-length mouse Bcs1, purified in detergent (CHAPS), with or without ATPgS.Mg2+ |
| Notes | Cryo-EM grids prepared using self-assembled monolayer supports. Data collected on a Titan Krios at 300 kV with Gatan K2 Summit detector. Two structures determined: apo (3.81 A) and ATPgS-bound (3.2 A). Data processing with MotionCor2, gCTF, and RELION. |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | DeltaN mBcs1 (residues 151-418, C-terminal His6 tag) with AMP-PNP.Mg2+ |
| Notes | X-ray crystallography of truncated mBcs1 lacking the N-terminal Bcs1-specific domain. Diffracted to 2.2 A resolution. Seven-fold symmetry confirmed by self-rotation function. Molecular replacement was unsuccessful with known AAA domains; phased using cryo-EM derived model. |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Full-length mBcs1 with ATPgS.Mg2+ |
| Notes | X-ray crystallography of full-length mBcs1. Crystals only obtained in the presence of ATPgS.Mg2+. Diffracted to 4.4 A resolution. Molecular replacement failed with known AAA structures; phased using the apo mBcs1 cryo-EM model. Bound ADP detected in the nucleotide-binding pocket despite ATPgS in the crystallization condition. |


## Biological / Functional Insights

### Homo-heptameric assembly enables folded protein translocation

Bcs1 forms a homo-heptamer (~324 kDa) rather than the canonical hexamer found in most AAA proteins. The heptameric architecture creates a larger entrance and binding cavity (~35 A average diameter, ~28,000 A^3 volume) sufficient to accommodate folded protein substrates like the 126-residue ISP extrinsic domain (~25 A effective diameter).

### Nucleotide-dependent conformational changes drive substrate translocation

ATP binding to Bcs1 induces a concerted contraction of the AAA domains, reducing the substrate-binding cavity volume. In the apo/ADP-bound state, the cavity is open and accessible to the mitochondrial matrix. ATP binding causes inter-subunit sliding movements that constrict the cavity, potentially pushing the substrate across the mitochondrial inner membrane. The Arg-finger residue R343 moves ~19 A in the apo state to interact with the gamma-phosphate in the ATPgS-bound state.

### Unique seven-stranded beta-sheet in the AAA domain

Unlike most AAA proteins that have a five-stranded beta-sheet in the RecA-like domain, Bcs1 has a seven-stranded beta-sheet with two extra beta-strands at the N terminus of the AAA domain. This unique structural feature places Bcs1 in a separate phylogenetic group of its own.

### Bcs1 lacks pore-loop and sensor-II motifs

Bcs1 lacks the conserved substrate-contact pore loop found in canonical AAA unfoldases that use a hand-over-hand threading mechanism. Additionally, the sensor-II region in the small helical domain involved in ATP binding is missing. This suggests Bcs1 uses a fundamentally different translocation mechanism compared to other AAA proteins.

### Distinct TM domain behavior in different nucleotide states

In the apo structure, the TM helices (L29-I49) were partially traced, suggesting close association of TM helices. In the ATPgS-bound structure, the TM region is entirely disordered, with the first confidently modeled residue being I49. This indicates nucleotide-dependent reorganization of the transmembrane domain.

### Human disease mutations mapped to Bcs1 structure

mBcs1 shares 94% sequence identity with human BCS1L. Mapping of disease-causing mutations onto the mBcs1 structure reveals that mutations associated with the severe GRACILE syndrome cluster at the Bcs1-specific domain and AAA domain interface, while those causing the milder Bjoernstad syndrome are distributed throughout. 14 out of 21 missense mutations involve positively charged arginine residues, underscoring the importance of electrostatic interactions in Bcs1 function.

### Putative substrate-binding cavity electrostatic properties

The cap of the putative substrate-binding cavity, made of the Bcs1-specific domain, is intensely negatively charged. The interior surface of the cavity in the apo state is negatively charged, complementary to the positively charged surface of the ISP substrate. This electrostatic complementarity likely guides substrate recognition and binding.


## Cross-References
