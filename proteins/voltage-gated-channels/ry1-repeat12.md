---
title: "Rabbit RyR1 Repeat12 Domain"
created: 2026-06-05
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein]
sources: [doi/10.1038##ncomms8947]
verified: false
---

# Rabbit RyR1 Repeat12 Domain

## Overview

The Repeat12 domain of rabbit Ryanodine Receptor Type 1 (RyR1), spanning residues 857-1054, was crystallized at 1.55 A resolution. It adopts a unique U-shaped loop (U-lid) connecting two repeat halves, with an additional three-stranded beta-sheet filling the space between the two halves. This domain is structurally distinct from the phosphorylation domain (Repeat34), which has a prominent horseshoe shape. The Repeat12 domain docks at the corner region of the full-length RyR assembly. Five malignant hyperthermia mutations and two [CPVT](/xray-mp-wiki/concepts/cpvt) mutations map to this domain. All four cysteines were mutated to alanine to facilitate crystallization.


## Publications

### doi/10.1038##ncomms8947

**Structures:**

<table class="wiki-table">
  <thead><tr>
    <th>PDB ID</th>
    <th>Resolution</th>
    <th>Space Group</th>
    <th>Construct</th>
    <th>Ligand/Co-factor</th>
  </tr></thead>
  <tbody>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5c30">5C30</a></td>
      <td>1.55 A</td>
      <td>P 3_1 2 1</td>
      <td>Rabbit RyR1 Repeat12 domain, residues 857-1054 (C-to-A mutants), native</td>
      <td>None (apo structure)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5c33">5C33</a></td>
      <td>2.35 A</td>
      <td>P 3_1 2 1</td>
      <td>Rabbit RyR1 Repeat12 domain, residues 857-1054, SeMet-labelled</td>
      <td>None (SAD phasing structure)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Notes**: All four cysteines in Repeat12 were mutated to alanine by Quikchange (Stratagene) to facilitate crystallization. Expressed as HMT fusion.


**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (sitting drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Rabbit RyR1 Repeat12 domain, 857-1054, C-to-A mutants</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not explicitly specified in paper</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not explicitly specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallized by standard vapor diffusion. Space group P 3_1 2 1. SeMet-labelled crystals used for SAD phasing.
</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### U-shaped loop (U-lid) and three-stranded beta-sheet

The Repeat12 domain features a long U-shaped structured loop (U-lid) connecting the two repeat halves. A three-stranded beta-sheet fills the space between the two halves and interacts with the first half, in part through a salt bridge between Glu917 and Arg1000. This structure is very different from the phosphorylation domain (Repeat34), which has a prominent horseshoe shape.

### Malignant hyperthermia mutation R1044C destabilizes U-lid

The human R1043C malignant hyperthermia mutation (R1044C in rabbit) affects a residue involved in multiple hydrogen bonds, including main chain atoms from the U-lid. The R1044C mutant shows two thermal transitions (Tm = 33.6 and 39.6 C) compared to a single transition at 41.1 C for wild-type, suggesting destabilization of a subdomain.

### CPVT mutation G1050S causes misfolding during expression

The G1049S mutation (G1050S in rabbit) is located in a tight loop near the end of Repeat12. The main chain conformation is in a region of the Ramachandran plot that is only allowed for [Glycine](/xray-mp-wiki/reagents/buffers/glycine) residues. While thermal melt analysis does not suggest destabilization (Tm 43.1 C), the yield of purified recombinant protein is drastically lower (40-fold compared to wild-type), suggesting significant misfolding during expression.

### Docks at the corner region of full-length RyR

Unbiased 6D docking in [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em) maps places the Repeat12 domain at the corner region of the RyR1 cap. Despite the absence of the prominent horseshoe shape seen in Repeat34, Repeat12 docking yields the corner as the top hit. However, there remains a visible mismatch because the [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em) density does not support the three-stranded beta-sheet, likely due to local mobility.


## Cross-References

- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/ryanodine-receptor/">Ryanodine Receptor (RyR)</a> — Parent protein family; Repeat12 is a domain of RyR
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/ry1/">Ryanodine Receptor Type 1 (RyR1)</a> — Related RyR isoform; Repeat12 is a domain of RyR1
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/ry2-spry1/">Mouse RyR2 SPRY1 Domain</a> — Co-crystallized domain from the same paper
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/fkbp12/">FKBP12 (FK506 Binding Protein 12)</a> — Accessory protein binding to RyR1 SPRY1 domain; Repeat12 is adjacent to SPRY1 in the sequence
- <a href="/xray-mp-wiki/methods/structure-determination/cryo-em">Cryo-Electron Microscopy</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/buffers/glycine">Glycine</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/concepts/cpvt">CPVT</a> — Entity mentioned in text
