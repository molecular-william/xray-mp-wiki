---
title: Carboxylate Shift
created: 2026-06-08
updated: 2026-06-08
type: concept
category: concepts
layout: default
tags: [concept-functional, membrane-protein]
sources: [doi/10.1038##s42003-019-0427-1]
verified: false
---

# Carboxylate Shift

## Overview
The carboxylate shift is a catalytic mechanism observed in Class I
CDP-alcohol phosphotransferases (CDP-APs) in which binding of the
second alcohol substrate ([D-myo-Inositol-3-Phosphate](/xray-mp-wiki/reagents/ligands/d-myo-inositol-3-phosphate/) in the case of
PgsA1) induces a rearrangement of catalytic aspartate side chains and
a corresponding shift in the position of a bound divalent metal ion
(Mg2+ or Mn2+). This primes the active site for proton abstraction
and nucleophilic attack.


## Mechanism/Details
Class I CDP-alcohol phosphotransferases possess a conserved signature
motif D1xxD2G1xxAR...G2xxxD3xxxD4, in which the four aspartates
coordinate catalytically important divalent metal ions (Mg2+, Mn2+,
or Co2+). Crystal structures of M. tuberculosis PgsA1 reveal two
distinct states of the dinuclear metal site:

In the "relaxed" state (observed with CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag/) bound), the two metal
ions are 5.4 Å apart, with the second metal (Mg-2) coordinated by
D89 and D93 in one conformation. When [D-myo-Inositol-3-Phosphate](/xray-mp-wiki/reagents/ligands/d-myo-inositol-3-phosphate/)
binds, it induces a "tight" state in which the metal-metal distance
decreases to 4.6 Å, achieved through a carboxylate shift of the
coordinating aspartates D89 and D93. This movement positions D93 —
the presumed catalytic base — optimally for proton abstraction from
the 1′ hydroxyl of the inositol substrate, enabling nucleophilic
attack on the β-phosphorus of CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag/).

The carboxylate shift thus provides a substrate-induced priming
mechanism: CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag/) binding first primes the dinuclear metal site,
and subsequent ino-P binding triggers the shift to the catalytic
conformation. This ordered substrate binding mechanism ensures
catalysis occurs only when both substrates are properly positioned,
preventing wasteful hydrolysis and ensuring reaction fidelity.

This refined mechanism was proposed based on three high-resolution
crystal structures of M. tuberculosis PgsA1: apo (2.9 Å),
Mn-[Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) complex (1.9 Å), and CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag/) complex (1.8 Å), supported
by [Molecular Docking](/xray-mp-wiki/methods/structure-determination/molecular-docking/) and mutagenesis studies.


## Examples in Membrane Protein Work
- M. tuberculosis PgsA1 — The carboxylate shift of D89 and D93 mediates transition between "relaxed" (5.4 Å metal-metal distance, CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag/) bound) and "tight" (4.6 Å, substrate-bound) states during catalysis
- CDP-alcohol phosphotransferases (general) — The carboxylate shift mechanism appears to be a general feature of Class I CDP-APs, suggested by conserved aspartate residues in the signature motif across all domains of life

## Related Concepts
- []() — 
- []() — 

## Cross-References
- [Phosphatidylinositol Phosphate Synthase PgsA1 from Mycobacterium tuberculosis](/xray-mp-wiki/proteins/enzymes/mt-pgsa1/) — Carboxylate shift mechanism observed in PgsA1 crystal structures
- [CDP-Alcohol Phosphotransferase Family](/xray-mp-wiki/concepts/cdp-alcohol-phosphotransferase-family/) — The carboxylate shift is a proposed general mechanism for this family
- [Phosphatidylglycerol Phosphate Synthase PgsA from Staphylococcus aureus](/xray-mp-wiki/proteins/enzymes/sa-pgsa/) — Homologous enzyme; mechanism may be conserved across PgsA orthologs
- [Molecular Docking](/xray-mp-wiki/methods/structure-determination/molecular-docking/) — Method used in structure determination or purification
- [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) — Buffer component used in purification or crystallization
- [D-myo-Inositol-3-Phosphate](/xray-mp-wiki/reagents/ligands/d-myo-inositol-3-phosphate/) — Related ligand or cofactor
- [DAG](/xray-mp-wiki/reagents/lipids/dag/) — Additive used in purification or crystallization buffers
