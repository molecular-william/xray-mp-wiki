---
title: Alternating Access Mechanism
created: 2026-04-27
updated: 2026-04-27
type: concept
tags: [membrane-protein, sample-preparation]
sources: [doi/10.1016##j.bbrc.2020.11.096, doi/10.1016##j.cell.2018.11.025]


category: concepts
layout: default
---




# Alternating Access Mechanism

## Overview

The alternating access mechanism is the fundamental principle by which secondary transporters move substrates across membranes. Rather than forming a continuous pore (like [ion-channels](/xray-mp-wiki/concepts/ion-channels/)s), transporters alternate between conformations where the substrate binding site is accessible from one side of the membrane or the other, never both simultaneously.

## Three Canonical States

1. **Inward-open**: Substrate binding site accessible from the cytoplasm/intracellular side
2. **Occluded**: Both gates closed, substrate trapped within the binding pocket
3. **Outward-open**: Substrate binding site accessible from the extracellular space/periplasm

## Major Transporter Families Using Alternating Access

### Major Facilitator Superfamily (MFS)
- **Mechanism**: Rocker-switch — rigid-body rotation of N and C domain bundles
- **Examples**: LacY, GlpT, SotB, GLUTs
- **Architecture**: 12 TM helices, two 6-helix bundles

### Mitochondrial Carrier Family (SLC25)
- **Mechanism**: Domain rotation — three repeated domains each with 2 TM helices
- **Examples**: ADP/ATP carrier (AAC), citrate carrier
- **Architecture**: ~300 aa, 6 TM helices, 3 repeats

### MATE (Multidrug And Toxic compound Extrusion)
- **Mechanism**: Rocker-switch variant
- **Examples**: NtMATE2, human MATE1/2-K
- **Architecture**: 12–14 TM helices

### APC (Amino Acid-Polyamine-Organocation)
- **Mechanism**: Rocker-switch
- **Examples**: AdiC, TatB
- **Architecture**: 10 TM helices

## Energetics

### Secondary Active Transport
- Uses ion gradients (H⁺, Na⁺) established by primary pumps
- **Uniport**: Single substrate, down its gradient
- **Symport**: Substrate + ion move in same direction
- **Antiport**: Substrate and ion move in opposite directions

### Proton Coupling in Antiporters
- Substrate binding and protonation compete
- Substrate binding-induced deprotonation triggers conformational change
- Proton-motive force drives the export of toxic compounds

## Nonlinear Conformational Changes

Recent structural studies (e.g., SotB) suggest that the alternating access transition may not be a simple rigid-body motion:
- **Nonlinear movements**: Additional local conformational adjustments beyond global domain rotation
- **Local gating helix movements**: Similar to GLUT [glucose](/xray-mp-wiki/reagents/ligands/glucose/) binding
- **Implication**: The transport cycle may involve more complex structural rearrangements than previously appreciated

|## Related Concepts
|
|- [mfs-transporter](/xray-mp-wiki/concepts/mfs-transporter/) — Major Facilitator Superfamily overview
|- [sotb](/xray-mp-wiki/proteins/sotb/) — E. coli antiporter with 4 captured conformations
|- [nTMATE2-transporter](/xray-mp-wiki/proteins/nTMATE2-transporter/) — MATE family transporter
|- [adenine-nucleotide-transporter](/xray-mp-wiki/proteins/adenine-nucleotide-transporter/) — Mitochondrial carrier with domain rotation
