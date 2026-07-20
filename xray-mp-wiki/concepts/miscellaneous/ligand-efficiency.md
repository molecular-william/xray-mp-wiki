---
title: "Ligand Efficiency in Drug Discovery"
created: 2026-05-29
updated: 2026-05-29
type: concept
category: concepts
layout: default
tags: [concept-functional, subdirectory-miscellaneous]
sources: [doi/10.1021##acs.jmedchem.5b00892]
verified: regex
---

# Ligand Efficiency in Drug Discovery

## Overview
Ligand efficiency (LE) is a metric used in drug discovery to assess how efficiently a molecule utilizes its atomic composition to achieve binding affinity. It normalizes the binding free energy by the number of heavy atoms in the molecule, providing a size- independent measure of binding quality. The formula is LE = -RT(ln Ki) / N, where N is the number of heavy atoms. Higher ligand efficiency indicates that a molecule achieves good binding affinity with fewer atoms, which is particularly important in fragment-based drug discovery (FBDD) where small fragments are optimized into larger lead compounds.


## Mechanism/Details
Ligand efficiency provides a normalized metric for comparing compounds of different sizes. A fragment with pKi 5.6 and 22 heavy atoms has LE = 0.36, while a fragment with pKi 6.9 and 23 heavy atoms has LE = 0.47. The higher LE indicates that the latter compound achieves better binding per atom, making it a more efficient starting point for lead optimization. In FBDD campaigns targeting GPCRs, ligand efficiency is used to prioritize fragment hits for further development, as high-LE fragments are more likely to yield high-affinity leads upon optimization.


## Examples in Membrane Protein Work
- [Metabotropic Glutamate Receptor 5 (mGlu5)](/xray-mp-wiki/proteins/gpcr/metabotropic-glutamate-receptor-5/) — Fragment screening of mGlu5-StaR using high-concentration radioligand binding assay identified pyrimidine hit 5 with pKi 5.6 and LE 0.36. The related compound 6, incorporating a 3-fluoro-5-cyanophenyl motif, achieved pKi 6.9 and LE 0.47, demonstrating superior ligand efficiency. Compound 6 was progressed to compound 12 (pKi 8.4, LE improved) and ultimately to compound 14 (pKi 9.3) through structure-based drug design.


## Related Concepts


## Cross-References
- [Negative Allosteric Modulation](/xray-mp-wiki/concepts/signaling-receptors/negative-allosteric-modulation/) — Ligand efficiency was used to optimize mGlu5 NAMs
- [HTL14242 (Compound 25)](/xray-mp-wiki/reagents/ligands/htl14242/) — Final optimized compound derived from high-LE fragment
- [MPEP](/xray-mp-wiki/reagents/ligands/mpep/) — Reference compound used in fragment screening
- [Metabotropic Glutamate Receptor 5 (mGlu5)](/xray-mp-wiki/proteins/gpcr/metabotropic-glutamate-receptor-5/) — Related protein structure
