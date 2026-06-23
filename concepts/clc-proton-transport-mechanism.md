---
title: CLC Cl-/H+ Exchange Transport Mechanism
created: 2026-06-08
updated: 2026-06-08
type: concept
category: concepts
layout: default
tags: [concept-transport-mechanism, subdirectory-concepts]
sources: [doi/10.1073##pnas.1901822116, doi/10.1073##pnas.1205764109, doi/10.1126##science.1195230]
verified: false
---

# CLC Cl-/H+ Exchange Transport Mechanism

## Overview
CLC Cl-/H+ exchange transporters couple the downhill movement of chloride ions (Cl-) to the uphill movement of protons (H+) across membranes, with a stoichiometry of 2 Cl- per 1 H+. The mechanism centers on a conserved glutamate residue (the \"glutamate gate\" or Egate), whose carboxylate side chain acts as a surrogate Cl- ion that can accept a proton and shuttle it between the external solution and the central Cl- binding site. This shuttle mechanism explains how CLC transporters achieve coupled exchange while CLC channels (lacking this glutamate) mediate passive Cl- flow. The mechanism was elucidated through studies on EcCLC (E. coli) and CmCLC (C. merolae) transporters using mutagenesis, flux assays, and X-ray crystallography.


## Mechanism/Details
The transport cycle involves the Egate glutamate switching between three conformations: an external position, the outer Cl- binding site, and the central Cl- binding site. When the glutamate carboxylate occupies the central Cl- site, it can exchange H+ with the intracellular solution via an internal glutamate residue (Ein, E203 in EcCLC). The cycle requires Cl- ions to destabilize the Egate carboxylate, promoting its exit from the anion pathway and enabling H+ exchange.

Key experimental findings supporting this mechanism include:
- H+ transport depends on both the Egate glutamate and the presence of Cl- ions. In the E148A mutant (Egate removed), H+ transport ceases unless carboxylate-containing molecules (glutamate, gluconate) are supplied in solution, confirming that a mobile carboxylate group mediates H+ transfer.
- Solution-mediated H+ transport in the E148A mutant requires the Ein residue (E203), showing it follows the same H+ pathway.
- A crystal structure of EcCLC E148A shows electron density compatible with a glutamate molecule from solution extending into the anion pathway to reach the central Cl- binding site.
- Cl- ions and the Egate carboxylate compete for the same binding sites in the anion pathway. Cl- is required for H+ transport in wild-type but inhibits solution-mediated H+ transport in E148A mutants.
- Aspartate at the Egate position cannot fully replace glutamate because its shorter side chain cannot easily reach the central Cl- site, resulting in drastically slower H+ transport.
- In CmCLC, where threonine naturally occupies the Ein position, Cl--driven H+ transport still occurs, demonstrating that Ein is important but not universally essential.

The Mindell (2010) perspective on the Feng et al. CmCLC structure proposed a "plunger" mechanism where movements of a single side chain (the gating glutamate) alternately allow access to one side of the membrane or the other, acting as a plunger to expel bound Cl- to the cytoplasm and to deliver (or accept) the transported proton well into the translocation pathway. This mechanism requires only minimal conformational change compared to the dramatic movements seen in other transporter families (rocking bundles, sliding pistons). The model also predicts a channel-like state with a continuous aqueous pathway, where Cl- ions encounter an energetic "hill" preventing rapid permeation - an open state predicted to occur when the gating glutamate is protonated and rotated away from the ion path, favored at low pH.

## Examples in Membrane Protein Work
- [CLC-ec1](/xray-mp-wiki/proteins/slc-transporters/clc-ec1/) — Paradigm CLC transporter from E. coli; Egate residue E148, Ein residue E203
- [CmCLC](/xray-mp-wiki/proteins/slc-transporters/cmclc/) — Eukaryotic CLC transporter from C. merolae; Ein position is threonine rather than glutamate
- [STCLC](/xray-mp-wiki/proteins/slc-transporters/stclc/) — Salmonella typhimurium CLC homolog used for structural comparison

## Related Concepts


## Cross-References
- [CLC-ec1 Cl-/H+ Antiporter](/xray-mp-wiki/proteins/slc-transporters/clc-ec1/) — CLC-ec1 is the primary model system for studying the CLC Cl-/H+ exchange mechanism
- [Proton Wire](/xray-mp-wiki/concepts/proton-wire/) — The Egate glutamate may participate in a proton transfer network within the CLC transport pathway
