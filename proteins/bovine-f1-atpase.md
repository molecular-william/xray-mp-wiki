---
title: Bovine Mitochondrial F1-ATPase
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [pump, enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##370621a0]
verified: false
---

# Bovine Mitochondrial F1-ATPase

## Overview

Bovine mitochondrial F1-ATPase is the water-soluble catalytic domain of ATP synthase (F1F0-ATPase), the central enzyme in energy conversion in mitochondria. The crystal structure at 2.8 A resolution reveals an asymmetric assembly of five different subunits (alpha3beta3gamma delta epsilon) arranged as alternating alpha and beta subunits around a central alpha-helical gamma-subunit domain.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##370621a0 | TBD (PDB ID not stated in paper) | 2.8 A | TBD (not stated in paper) | Full bovine heart mitochondrial F1-ATPase complex (alpha3beta3gamma delta epsilon, relative molecular mass 371,000) | AMP-PNP (beta_TP, alpha subunits), ADP (beta_DP), empty (beta_E) |

## Expression and Purification

No purification described.

## Crystallization

### doi/10.1038##370621a0

| Parameter | Value |
|---|---|
| Method | X-ray crystallography with SIRAS phasing using methylmercury derivatives |
| Protein sample | Bovine mitochondrial F1-ATPase |
| Notes | Three native and three methylmercury derivative crystals. Resolution 2.85-3.5 A. Mercury sites: 4, 9, and 4 across derivatives. |


## Biological / Functional Insights

### Asymmetric structure supports binding-change mechanism

The three catalytic beta-subunits differ in conformation and bound nucleotide, directly supporting the binding-change mechanism of ATP synthesis. The subunit denoted beta_TP binds AMP-PNP (tight state), beta_DP binds ADP (loose state), and beta_E has an empty and distorted nucleotide-binding site (open state). The three alpha-subunits each bind one molecule of AMP-PNP at non-catalytic sites. The nucleotide-binding sites are at the interfaces between alpha- and beta-subunits. Beta-Tyr 368 protrudes into the alpha-subunit nucleotide site, helping explain the specificity of alpha-subunit sites for adenine nucleotides.

### Rotational catalysis hypothesis

The structure provides several features compatible with rotation of the alpha3beta3 subassembly relative to the gamma-subunit during catalysis. First, a hydrophobic sleeve surrounding the C-terminal tip of the gamma-subunit acts as a molecular bearing. Second, a central cavity permits passage of the long N-terminal helix of the gamma-subunit within the F1 core during rotation. Third, the three different catalytic site conformations are correlated with the asymmetric position of the gamma-subunit. The estimated rotation rate would be 130-270 Hz based on the Vmax of bovine ATP synthase.

### Subunit fold architecture

Each alpha- and beta-subunit consists of three domains: an N-terminal six-stranded beta-barrel, a central alpha-beta domain containing the nucleotide-binding site, and a C-terminal helical bundle of 7 and 6 helices respectively. The folds of alpha- and beta-subunits are almost identical, with nine-stranded beta-sheets and nine associated alpha-helices in the nucleotide-binding domain. The beta-barrel domains crown the particle with a continuous 24-stranded beta-sheet. In beta_E, the interaction between strands 3 and 7 of the nucleotide-binding domain is disrupted.

### Nucleotide-binding site architecture

The nucleotide pyrophosphate group binds in the same way as in RecA, within the P-loop containing the conserved GXXXXGKT S motif. In beta_TP, Ogamma-Thr 163 and one oxygen atom from each of the beta- and terminal phosphates coordinate magnesium. In beta_DP, density is observed for an ordered water molecule replacing the terminal phosphate. Beta-Tyr 345 forms a crosslink with photoactivated 2-azido-ATP in the adenine-binding pocket. The inhibitor dicyclohexylcarbodiimide (beta-Glu 199) points into the conical tunnel leading to the nucleotide sites.

### Gamma-subunit interactions with alpha3beta3

The gamma-subunit has a central alpha-helical domain containing both N- and C-terminal regions, traversing the center of the alpha3beta3 assembly. The C-terminal helix (residues 253-272) forms a hydrophobic sleeve with six proline-rich loops from alpha (287-294) and beta (274-281) subunits. The loop containing the DELSEED sequence makes a catch interaction with the gamma-subunit. The gamma-subunit prevents beta_E from adopting a nucleotide-binding conformation by obstructing rotation of its lower half.


## Cross-References

- [Rotary ATPase Mechanism](/xray-mp-wiki/concepts/rotary-atpase-mechanism/) — First structural evidence for rotational catalysis
- [V1-ATPase T. thermophilus](/xray-mp-wiki/proteins/v1-atpase-t-thermophilus/) — Related rotary ATPase with structurally similar core
- [Ilyobacter tartaricus C Subunit](/xray-mp-wiki/proteins/ilyobacter-tartaricus-c-subunit/) — Related F-type ATPase c-subunit
- [Adenosine Diphosphate (ADP)](/xray-mp-wiki/reagents/ligands/adp/) — Bound to beta_DP subunit
- [AMP-PNP (Adenylyl-Imidodiphosphate)](/xray-mp-wiki/reagents/ligands/amp-pnp/) — Nucleotide analogue bound to beta_TP and alpha subunits
- [Na+,K+-ATPase (Pig Kidney)](/xray-mp-wiki/proteins/na-k-atpase-pig-kidney/) — Another P-type ATPase pump with related energy transduction
