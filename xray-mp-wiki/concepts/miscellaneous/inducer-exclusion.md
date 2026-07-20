---
title: "Inducer Exclusion"
created: 2026-06-03
updated: 2026-06-03
type: concept
category: concepts
layout: default
tags: [concept-functional, subdirectory-miscellaneous]
sources: [doi/10.1038##nature12232]
verified: regex
---

# Inducer Exclusion

## Overview
Inducer exclusion is a mechanism of [Carbon Catabolite Repression](/xray-mp-wiki/concepts/miscellaneous/carbon-catabolite-repression/) in which unphosphorylated enzyme IIA^Glc (EIIA^Glc) directly inhibits non-PTS sugar transporters, preventing the uptake of secondary carbon sources. This inhibition serves a dual purpose: it directly blocks secondary carbon source uptake, and it downregulates the expression of corresponding catabolic systems by reducing the intracellular level of inducer molecules. The lac operon regulation in E. coli is the best-known example of inducer exclusion. Inducer exclusion is a form of negative allosteric modulation where a regulatory protein binds to a transporter and stabilizes it in an inactive conformation.


## Mechanism/Details
When [Glucose](/xray-mp-wiki/reagents/additives/glucose/) or other preferred PTS substrates are available, the phosphotransferase system (PTS) maintains EIIA^Glc in its unphosphorylated state. Unphosphorylated EIIA^Glc directly binds to and inhibits target transporters. For the [Maltose](/xray-mp-wiki/reagents/additives/maltose/) transporter (MalFGK2), two EIIA^Glc molecules bind to the cytoplasmic ATPase subunits ([MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/abc-transporters/malK/)), wedging between the nucleotide-binding domain (NBD) of one [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/abc-transporters/malK/) and the regulatory domain of the opposite [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/abc-transporters/malK/). This locks the transporter in an inward-facing (resting) conformation, preventing the NBD closure and ATP hydrolysis required for the transport cycle. EIIA^Glc is a classical Monod-Wyman-Changeux allosteric inhibitor. The N-terminal region of EIIA^Glc (residues 1-18) functions as a membrane anchor, increasing the effective concentration of EIIA^Glc at the membrane surface and lowering the IC50 by 60-fold.


## Examples in Membrane Protein Work
- [Maltose](/xray-mp-wiki/reagents/additives/maltose/) Transporter (MalFGK2) — Two EIIA^Glc molecules bind to [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/abc-transporters/malK/) subunits at a canonical surface, with 1,500 A^2 buried surface area per EIIA^Glc (55% at NBD interface, 45% at regulatory domain interface). The binding is independent of [Maltose](/xray-mp-wiki/reagents/additives/maltose/) presence. Full-length EIIA^Glc has IC50 = 1.61 +/- 0.04 uM; Delta(1-18) [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) mutant has IC50 = 91 +/- 3 uM (60-fold difference). Hill coefficients are 1.53 and 1.60, respectively, indicating cooperative binding. Max inhibition is 95% for full-length and 94.7% for [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) mutant.
- Lactose Permease (LacY) — Unphosphorylated EIIA^Glc binds to and inhibits LacY, an [MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) transporter. Binding of EIIA^Glc to LacY is enhanced by the presence of lactose substrate. The mechanism is likely different from the [Maltose](/xray-mp-wiki/reagents/additives/maltose/) transporter since LacY is an [MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) transporter rather than an ABC transporter.
- [Melibiose](/xray-mp-wiki/reagents/ligands/melibiose/) Permease ([MELB](/xray-mp-wiki/proteins/mfs-transporters/melbst/)) — Unphosphorylated EIIA^Glc binds to and inhibits [MELB](/xray-mp-wiki/proteins/mfs-transporters/melbst/), another [MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) transporter. Binding of EIIA^Glc to [MELB](/xray-mp-wiki/proteins/mfs-transporters/melbst/) is enhanced by the presence of the corresponding sugar substrate, similar to LacY.

## Related Concepts


## Cross-References
- [EIIA^Glc (Escherichia coli Enzyme IIA^Glc)](/xray-mp-wiki/proteins/abc-transporters/eiiaglc/) — Key regulatory protein; unphosphorylated form directly inhibits target transporters
- [Maltose Transporter (MalFGK2)](/xray-mp-wiki/proteins/abc-transporters/maltose-transporter-malfgk2/) — ABC transporter inhibited by EIIA^Glc through inducer exclusion
- [Carbon Catabolite Repression](/xray-mp-wiki/concepts/miscellaneous/carbon-catabolite-repression/) — Inducer exclusion is a primary mechanism of CCR in E. coli
- [Allosteric Regulation in Membrane Proteins](/xray-mp-wiki/concepts/structural-mechanisms/allosteric-regulation/) — EIIA^Glc acts as an allosteric inhibitor of target transporters
- [ABC Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/) — Maltose transporter is an ABC importer subject to inducer exclusion
- [MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) — Related biological concept
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) — Related biological concept
- [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/abc-transporters/malK/) — Related protein structure
- [MELB](/xray-mp-wiki/proteins/mfs-transporters/melbst/) — Related protein structure
- [Glucose](/xray-mp-wiki/reagents/additives/glucose/) — Additive used in purification or crystallization buffers
