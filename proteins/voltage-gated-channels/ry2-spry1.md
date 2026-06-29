---
title: "Mouse RyR2 SPRY1 Domain"
created: 2026-06-05
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein]
sources: [doi/10.1038##ncomms8947]
verified: false
---

# Mouse RyR2 SPRY1 Domain

## Overview

The SPRY1 domain of mouse Ryanodine Receptor Type 2 (RyR2), spanning residues 650-844, was crystallized at 1.2 A resolution. It adopts a beta-trefoil structure with a finger substructure (a beta-hairpin pointing away from the core) and a lid following the core. The domain is highly conserved among all three RyR isoforms, particularly the finger substructure. The SPRY1 domain is located next to [FKBP12](/xray-mp-wiki/proteins/fkbp12) in the full-length RyR assembly and plays a crucial role in [FKBP12](/xray-mp-wiki/proteins/fkbp12) binding. The 675-loop contains a hydrophobic cluster (F674, L675) critical for FKBP interaction. Disease mutations including N760D (central core disease) and D720 (multi-minicore disease) map to this domain.


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
      <td>1.21 A</td>
      <td>P 2_1 2_1 2_1</td>
      <td>Mouse RyR2 SPRY1 domain, residues 650-844, native</td>
      <td>None (apo structure)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5c33">5C33</a></td>
      <td>1.44 A</td>
      <td>P 2_1 2_1 2_1</td>
      <td>Mouse RyR2 SPRY1 domain, residues 650-844, SeMet-labelled</td>
      <td>None (MAD phasing structure)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Notes**: [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine) (SeMet) labelled SPRY1 produced using standard SeMet labeling protocol. Expressed as HMT (His-tag) fusion.


**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (sitting drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Mouse RyR2 SPRY1 domain, 650-844, ~10 mg/mL in buffer</td>
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
      <td>Crystallized by standard vapor diffusion. Space group P 2_1 2_1 2_1. SeMet-labelled crystals used for MAD phasing at synchrotron.
</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Beta-trefoil fold with finger substructure

The SPRY1 domain adopts a beta-trefoil structure consisting of three beta-helical sheets forming a trefoil knot. A finger substructure (beta-hairpin) extends away from the core, and a lid region follows the core. The finger is highly conserved among all three RyR isoforms.

### FKBP12 binding interface centered on 675-loop

The SPRY1 domain binds [FKBP12](/xray-mp-wiki/proteins/fkbp12) primarily through the 675-loop, which contains a hydrophobic cluster (F674, L675). F674 side chain fits into a pocket formed by two arginines on the FKBP surface, particularly R40 which forms a cation-pi interaction. The interface buries ~350 A^2. Insertion of His10-tag at position 675 reduces FKBP binding to less than 10% of wild-type.

### Disease mutation N760D causes SPRY1 misfolding

The central core disease mutation N760D (N759D in human, Asn771 in mouse) affects a residue involved in a hydrogen bond network with Asp753 and His747. The mutation causes ~75% misfolding of the SPRY1 domain, reducing FKBP binding by 74%. The purified mutant protein has a melting temperature ~3.5 C lower than wild-type.

### Disease mutation D720 forms salt bridge with R694

The multi-minicore disease mutation D720 is located within the finger substructure and makes a salt bridge interaction with R694. Both residues are conserved in RyR1, RyR2, and RyR3, suggesting this interaction is functionally important.


## Cross-References

- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/ryanodine-receptor/">Ryanodine Receptor (RyR)</a> — Parent protein family; SPRY1 is a domain of RyR
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/ry1/">Ryanodine Receptor Type 1 (RyR1)</a> — Related RyR isoform; SPRY1 domains are highly conserved
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/ry1-repeat12/">Rabbit RyR1 Repeat12 Domain</a> — Co-crystallized domain from the same paper; structural comparison of SPRY1 and Repeat12
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/fkbp12/">FKBP12 (FK506 Binding Protein 12)</a> — High-affinity accessory protein; SPRY1 is the primary binding determinant
- <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine (SeMet)</a> — Used for SeMet-labelled SPRY1; MAD phasing
