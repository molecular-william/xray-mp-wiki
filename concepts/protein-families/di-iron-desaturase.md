---
title: Di-Iron-Containing Desaturase Family
created: 2026-06-08
updated: 2026-06-08
type: concept
category: concepts
layout: default
tags: [concept-protein-family, concept-functional]
sources: [doi/10.1038##nsmb.3049]
verified: false
---

# Di-Iron-Containing Desaturase Family

## Overview
The di-iron-containing desaturase family comprises enzymes that catalyze the introduction of double bonds into fatty acyl chains, a critical step in lipid biosynthesis. This family includes both soluble forms (such as stearoyl-acyl carrier protein desaturases from plants) and membrane-bound forms (such as stearoyl-CoA desaturase-1, SCD1, from mammals). While soluble desaturases use a carboxylate-bridged di-iron center housed within a four-helix bundle, integral membrane forms like SCD1 employ a novel histidine-coordinated dimetal center. Despite this structural divergence, both forms catalyze the same regioselective cis-dehydrogenation reaction at the delta-9 position of fatty acyl substrates, highlighting the evolutionary convergence on a common biochemical function through different metal coordination strategies.


## Mechanism/Details
The catalytic mechanism of di-iron desaturases involves the activation of molecular oxygen
at a dimetal center to abstract two pro-R hydrogen atoms from the delta-9 and delta-10
positions of the fatty acyl chain, forming a cis double bond. In soluble desaturases
(e.g., castor seed delta-9 stearoyl-ACP desaturase, PDB 1AFR), the di-iron center is
coordinated by carboxylate ligands from two EXXH motifs, forming a carboxylate-bridged
binuclear iron center housed within a four-helix bundle. This four-helix bundle scaffold
is a preferred architecture for oxygen-activation mechanisms and is conserved across
multiple di-iron center-containing enzymes, including multicomponent monooxygenases,
epoxidase BoxB, and ribonucleotide reductases.

In contrast, the membrane-bound SCD1 uses a fundamentally different metal coordination
strategy. The hSCD1 structure (PDB 4ZYO, 3.25 A) reveals a dimetal center (substituted
with Zn2+ in the crystal structure) coordinated entirely by histidine residues from
histidine-box motifs (HXXXXH, HXXHH, HXXHH). Zn1 is coordinated by five histidine
residues, while Zn2 is coordinated by four histidine residues and a water molecule.
This histidine-coordinated dimetal center is buried among transmembrane helices TM2, TM4
and cytoplasmic helices CH2, CH8, rather than within a four-helix bundle. The substrate
(stearoyl-CoA) binds in a cytoplasmic cap domain, with its acyl chain extending through
a hydrophobic tunnel toward the dimetal center. The geometry of this tunnel positions
carbons 9 and 10 of the fatty acid chain proximal to the metal center, while the CoA
head group anchors the substrate through electrostatic and hydrogen-bonding interactions
with polar residues on the protein surface.

## Examples in Membrane Protein Work
- [Stearoyl-CoA Desaturase-1 (hSCD1)](/xray-mp-wiki/proteins/enzymes/stearoyl-coa-desaturase-1/) — The hSCD1 structure (PDB 4ZYO) represents the first structural view of an integral membrane di-iron desaturase. It reveals a unique histidine-coordinated dimetal center that contrasts sharply with the carboxylate-bridged di-iron center of soluble desaturases. The substrate stearoyl-CoA binds in the cytoplasmic cap with its acyl chain extending through a hydrophobic tunnel to the metal center, where regioselective cis-dehydrogenation occurs at the delta-9 position.

## Related Concepts


## Cross-References
- [Stearoyl-CoA Desaturase-1 (hSCD1)](/xray-mp-wiki/proteins/enzymes/stearoyl-coa-desaturase-1/) — Primary example of membrane-bound di-iron desaturase; structure solved at 3.25 A (PDB 4ZYO)
- [Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/) — Primary substrate for SCD1; bound in the 4ZYO structure
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Related reagent used in purification of di-iron desaturases
- [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) — Used for Se-SAD phasing of hSCD1 structure determination
