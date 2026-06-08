---
title: TmPPase (Thermotoga maritima H+-Pumping Pyrophosphatase)
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [pump, enzyme, membrane-protein]
sources: [doi/10.1038##ncomms13596]
verified: false
---

# TmPPase (Thermotoga maritima H+-Pumping Pyrophosphatase)

## Overview

TmPPase (H+-pumping inorganic pyrophosphatase from Thermotoga maritima) is a membrane-bound enzyme that catalyzes the hydrolysis of inorganic pyrophosphate (PPi) and couples the released energy to proton translocation across the membrane. This enzyme belongs to the P-type ion pump family and is found in the thermophilic bacterium Thermotoga maritima. The crystal structure reveals a dimeric arrangement with 16 transmembrane helices per monomer. Multiple conformational states have been captured, including substrate-analogue-bound, resting-state (Ca:Mg-bound), tungstate-bound, and product-bound forms, providing insights into the catalytic cycle and ion translocation mechanism of M-PPases.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms13596 | Not specified (supplementary only) | Not specified (supplementary only) | Not specified (supplementary only) |  | IDP (inositol pyrophosphate) |
| doi/10.1038##ncomms13596 | Not specified (supplementary only) | Not specified (supplementary only) | Not specified (supplementary only) |  | Ca:Mg |
| doi/10.1038##ncomms13596 | Not specified (supplementary only) | Not specified (supplementary only) | Not specified (supplementary only) |  | WO4 (tungstate) |
| doi/10.1038##ncomms13596 | Not specified (supplementary only) | Not specified (supplementary only) | Not specified (supplementary only) |  | Pi2 (product) |

## Expression and Purification

No purification described.

## Crystallization

No crystallization described.

## Biological / Functional Insights

### Active Site Architecture and Mg2+ Coordination

The active site (hydrolytic center) of TmPPase coordinates a Mg:IDP complex
through water-mediated interactions and direct coordination with conserved
aspartate residues. Key active site residues include D6.35 (helix 6),
D11.57 (helix 11), and N12.43 (helix 12), which form the catalytic center
for PPi hydrolysis. The Mg2+ ion is coordinated in a geometry essential for
catalysis, analogous to the Mg2+ coordination observed in VrPPase.

### Ion Gate and Sodium Binding

TmPPase features an ion gate with a bound Na+ ion observed in the
substrate-analogue-bound state (TmPPase:IDP). The Na+ ion (shown in purple
in electron density maps) is coordinated at the ion gate, positioned between
key transmembrane helices. This sodium binding site is distinct from the
allosteric sodium site found in GPCRs and represents a functional ion
translocation pathway specific to H+-PPases.

### Helix 6 Curvature and Conformational Changes

Helix 6 undergoes significant curvature changes between catalytic states of
TmPPase. The transition between substrate-analogue-bound, resting-state,
tungstate-bound, and product-bound conformations involves repositioning of
D6.35 and neighboring residues. Helix 6 curvature analysis reveals distinct
helical geometries (alpha, 3_10, pi helix) across the four main states,
supporting a conformational cycle coupled to ion translocation.

### Helix 16 Rearrangement

Helix 16 undergoes substantial curvature changes between catalytic states,
complementing the helix 6 movements. The D16.39 residue at helix 16
participates in ion pair interactions that break upon substrate binding.
The K16.50 residue shows state-dependent repositioning, coordinating with
D6.50 and D6.53 in the resting state and becoming disordered in the
substrate-bound state.

### TMH12 Movement and Ion Pair Dynamics

TMH12 undergoes significant movement across the four states of TmPPase.
The K12.50 residue at helix 12 participates in ion pair interactions with
D6.43 that break upon substrate binding. This movement is coupled to the
opening and closing of the active site and is conserved between TmPPase
and VrPPase.

### Helix 6 and Helix 16 Coordination

The coordinated movement of helices 6 and 16 between the resting state
(TmPPase:Ca:Mg) and substrate-bound state (TmPPase:IDP) involves repositioning
of D6.43 and D16.39. In the Ca:Mg-bound state, a salt-bridge network is
observed, while in the IDP-bound state, Na+ binding replaces the K+ ions
that were coordinated by D6.50 and D6.53.


## Cross-References

- [VrH+PPase (Vigna radiata H+-Pumping Inorganic Pyrophosphatase)](/xray-mp-wiki/proteins/vrh-ppase/) — Plant homolog with similar dimeric architecture and catalytic mechanism
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — P-type pumps operate via alternating-access conformational changes
- [Sodium Ion (Na+)](/xray-mp-wiki/reagents/ligands/sodium-ion/) — Sodium ion bound at the ion gate of TmPPase in substrate-bound state
- [ABI-PP (Inositol pyrophosphate)](/xray-mp-wiki/reagents/ligands/abi-pp/) — IDP substrate analog used to trap substrate-bound conformation
