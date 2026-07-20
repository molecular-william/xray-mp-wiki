---
title: "GPR6 High Constitutive Activity and Orphan Receptor Signaling"
created: 2026-06-11
updated: 2026-06-11
type: concept
category: concepts
layout: default
tags: [concept-functional, subdirectory-signaling-receptors]
sources: [doi/10.1126##scisignal.ado8741]
verified: regex
---

# GPR6 High Constitutive Activity and Orphan Receptor Signaling

## Overview
[GPR6 — Orphan G Protein-Coupled Receptor Implicated in Parkinson's Disease](/xray-mp-wiki/proteins/gpcr/gpr6/) is an orphan class A GPCR exhibiting one of the highest levels of constitutive
(basal) activity among all GPCRs, signaling through Gαs without requiring addition
of an exogenous agonist. Structural studies combined with MD simulations, Markov
State Models (MSM), [Native Mass Spectrometry](/xray-mp-wiki/methods/quality-assessment/native-mass-spectrometry/), and functional assays revealed that
this high constitutive activity is likely driven by an endogenous lipid-like molecule
(tentatively modeled as [Oleic Acid](/xray-mp-wiki/reagents/lipids/oleic-acid/)) bound in the orthosteric pocket, rather than
being an intrinsic conformational preference of the apoprotein. MSM simulations
show that in the absence of ligand, the apo receptor strongly prefers the inactive
conformation (83% stationary probability). The lipid enters from the membrane through
a TM3-TM5 opening gated by Phe152(3.36), which acts as a key conformational switch.
Inverse agonists like CVN424 lock Phe152 in the inactive conformation, blocking
receptor activation.


## Mechanism/Details
The constitutive activity of [GPR6 — Orphan G Protein-Coupled Receptor Implicated in Parkinson's Disease](/xray-mp-wiki/proteins/gpcr/gpr6/) is proposed to operate through the following
molecular mechanism:

1. A single-chain lipid from the membrane enters the orthosteric pocket through
   an opening between TM3 and TM5, gated by Phe152(3.36).
2. The lipid headgroup interacts with a triad of charged/polar residues in the
   extracellular region: His128(2.60), Gln132(ECL1), and Arg220(ECL2).
3. The lipid tail occupies a hydrophobic cavity, stabilizing Phe152(3.36) in its
   active rotamer conformation, which disrupts π-stacking with Trp292(6.48) (the
   toggle switch) and Phe234(5.47).
4. Disruption of the toggle switch leads to a cascade of rearrangements including
   outward movement of TM5 (5.3 Å) and TM6 (8.2 Å), inward movement of TM7 (3.6 Å),
   collapse of the sodium-binding pocket, and rearrangements in the DRY and NPxxY
   motifs.
5. The opened cytoplasmic cavity enables Gαs coupling through the α5 helix,
   with Arg166(3.50) forming a π-cation interaction with Tyr391 of Gαs.

Inverse agonists (IAGs) such as CVN424 and compound 3h bind in the orthosteric
pocket and lock Phe152(3.36) in its inactive conformation, maintaining the receptor
in the inactive state. The high structural similarity of the ligand-binding pocket
between [GPR6 — Orphan G Protein-Coupled Receptor Implicated in Parkinson's Disease](/xray-mp-wiki/proteins/gpcr/gpr6/), GPR3, and GPR12 (86% sequence identity of 14 lining residues) suggests
a common mechanism of constitutive activity among these paralogs.


## Examples in Membrane Protein Work


## Related Concepts


## Cross-References
- [Native Mass Spectrometry](/xray-mp-wiki/methods/quality-assessment/native-mass-spectrometry/) — Method used in structure determination or purification
- [GPR6 — Orphan G Protein-Coupled Receptor Implicated in Parkinson's Disease](/xray-mp-wiki/proteins/gpcr/gpr6/) — Related protein structure
- [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine/) — Related ligand or cofactor
- [Oleic Acid](/xray-mp-wiki/reagents/lipids/oleic-acid/) — Additive used in purification or crystallization buffers
