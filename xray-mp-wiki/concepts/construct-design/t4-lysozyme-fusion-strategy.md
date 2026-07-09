---
title: "T4 Lysozyme Fusion Strategy"
created: 2026-07-06
updated: 2026-07-06
type: concept
category: concepts
layout: default
tags: [concept-construct-design, subdirectory-construct-design]
sources: [doi/10.1126##science.1140602, doi/10.1038##nprot.2009.230]
verified: none
---

# T4 Lysozyme Fusion Strategy

## Overview
The T4 lysozyme (T4L) fusion strategy is a protein engineering approach for crystallizing G protein-coupled receptors (GPCRs) and other membrane proteins by replacing conformationally flexible regions (most commonly intracellular loop 3, ICL3) with T4 lysozyme from bacteriophage T4. This strategy provides a rigid, well-ordered soluble domain that forms crystal lattice contacts, enabling structure determination of receptors that resisted traditional crystallization approaches. The strategy was first demonstrated with the beta2-adrenergic receptor (beta2AR) and has since been applied to dozens of GPCRs.


## Mechanism/Details
In the canonical implementation, the flexible ICL3 of the GPCR (typically 30-50 residues) is replaced by residues 2-161 of T4L (approximately 20 kDa). A short linker (typically 2-5 residues such as Ala-Ala or Gly-Thr) connects T4L to the receptor at both insertion points. The resulting T4L fusion construct retains near-native ligand binding and signaling properties because ICL3 is the most variable and least structured region of the receptor. T4L provides a large hydrophilic surface that forms extensive crystal contacts in the lattice, while the receptor portion is packed in a structurally unperturbed state. The strategy can also be applied to other membrane proteins that have flexible loops amenable to replacement.


## Examples in Membrane Protein Work
- Beta2-Adrenergic Receptor (beta2AR) — First GPCR crystal structure using T4L-ICL3 fusion (PDB 2RH1, 2.4 A); represents the landmark application of this strategy
- Human A2A Adenosine Receptor — T4L-ICL3 fusion enabled structure determination (PDB 3EML); demonstrated general applicability beyond beta2AR

## Related Concepts


## Cross-References
- [Fusion Partners for Membrane Protein Crystallization](/xray-mp-wiki/concepts/construct-design/fusion-partners/) — T4L is the most widely used fusion partner, described in the broader fusion partner context
- [N-Terminal T4 Lysozyme Fusion](/xray-mp-wiki/concepts/construct-design/n-terminal-t4-lysozyme-fusion/) — Alternative T4L fusion strategy for crystallizing GPCR signaling complexes
- [T4 Lysozyme (T4L)](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) — T4L is the fusion tag used in this strategy
- [Protein Thermostabilization](/xray-mp-wiki/concepts/construct-design/thermostabilization/) — Complementary construct design strategy often used alongside T4L fusion
