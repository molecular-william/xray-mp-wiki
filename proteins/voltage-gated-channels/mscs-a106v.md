---
title: "E. coli MscS Mechanosensitive Channel (A106V Open Form)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1159262]
verified: false
---

# E. coli MscS Mechanosensitive Channel (A106V Open Form)

## Overview

The structure of an open form of the *Escherichia coli* mechanosensitive channel of small conductance ([MSCS](/xray-mp-wiki/proteins/voltage-gated-channels/mscs/)) was determined at 3.45 Å resolution using the A106V mutant. [MSCS](/xray-mp-wiki/proteins/voltage-gated-channels/mscs/) is a heptameric channel that opens in response to membrane tension to allow rapid ion efflux, relieving turgor pressure during hypo-osmotic shock. The A106V structure reveals a pore diameter of ~13 Å created by substantial rotational rearrangement of the three transmembrane helices per monomer (TM1, TM2, TM3a, and TM3b). The opening mechanism involves TM3a helices pivoting around [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) G113, moving side chains L105 and L109 out of the pore lumen in a camera-iris-like motion, breaking the hydrophobic "vapor lock" that prevents ion passage in the closed state.


## Publications

### doi/10.1126##science.1159262

**Expression:**

- **Expression system**: E. coli
- **Notes**: Functional in vivo; heptameric channel

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>A106V mutant crystals diffracted to 3.45 Å resolution</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Camera Iris Gating Mechanism

The seven TM3a helices pivot around [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) G113 as a hinge point. In the open state, TM3a helices become parallel to the sevenfold axis and the membrane normal, whereas in the closed structure they are diagonal. This motion, coupled with rigid-body clockwise rotation of TM1 and TM2, moves the pore-lining side chains L105 and L109 out of the central pore in a manner reminiscent of a mechanical camera iris. The pore diameter expands from 4.8 Å (closed) to ~13 Å (open).

### Vapor Lock Pore Gating

In the closed state, the hydrophobic side chains of L105 and L109 insert into the pore lumen, creating a hydrophobic constriction that prevents wetting of the channel pore and blocks ion passage — a mechanism termed "vapor lock." In the open A106V structure, these side chains move out from the pore center, breaking the vapor lock and allowing ion conduction.

### A110-L115 Switch

A110 (TM3a) shifts from one side of L115 (TM3b of a neighboring monomer) to the other during gating, defining an open/closed state switch. Bulky substitutions at A110 (A110V) make the channel harder to open (~42 kJ/mol), while smaller substitutions (A110G, L115V) lower the gating energy (~20-22 kJ/mol), consistent with a kinetic barrier model.

### Gating Energetics and Mutant Cycle Analysis

During gating, the methyl group of A102 slides across the TM3a surface of the neighboring subunit. Mutation cycle analysis confirms coupling between A102 and G104 (coupling energy 0.38), while A102 and G101 are independent (coupling energy 0.02). A102G mutants show flickery behavior and rapid adaptation, while A102V increases gating pressure.

### Molecular Model for Adaptation

The open-state TM3a helices are no longer close-packed but physically separated. Returning to the closed state requires repacking with a specific "knobs and holes" pattern, which can become conformationally trapped. Adaptation (desensitization + inactivation) rate is proportional to cycling between open and closed states. Mutants that rapidly flicker between states (A102G) exhibit very rapid adaptation.


## Cross-References

- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/mscs/">MSCS</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/buffers/glycine/">Glycine</a> — Buffer component in purification or crystallization
