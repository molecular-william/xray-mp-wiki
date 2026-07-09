---
title: "Mhp1 Benzyl-Hydantoin Transporter from Microbacterium liquefaciens"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1164440, doi/10.1126##science.1186303]
verified: regex
---

# Mhp1 Benzyl-Hydantoin Transporter from Microbacterium liquefaciens

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


## Overview

Mhp1 is a member of the Nucleobase-Cation-Symport-1 (NCS1) family from Microbacterium liquefaciens that transports [Benzyl-Hydantoin](/xray-mp-wiki/reagents/ligands/benzyl-hydantoin/) and related nucleobase derivatives in a sodium-dependent manner. The structure was determined by X-ray crystallography in three conformations: an outward-facing open state (2.85 Å resolution), an outward-facing occluded state bound to [Benzyl-Hydantoin](/xray-mp-wiki/reagents/ligands/benzyl-hydantoin/) (4 Å resolution), and a substrate-free inward-facing state (3.8 Å resolution). Together, these three structures capture all major conformational states of the alternating access transport cycle, providing a complete structural basis for the mechanism.


## Publications

### doi/10.1126##science.1164440

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/— (see supporting material)">— (SEE SUPPORTING MATERIAL)</a></td>
      <td>2.85</td>
      <td>—</td>
      <td>Full-length Mhp1</td>
      <td>—</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/— (see supporting material)">— (SEE SUPPORTING MATERIAL)</a></td>
      <td>4.0</td>
      <td>—</td>
      <td>Full-length Mhp1</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/benzyl-hydantoin/">Benzyl-Hydantoin</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli (see supporting material)
- **Construct**: Full-length Mhp1
- **Notes**: Details in supporting online material (reference 24)

**Purification:**

- **Expression system**: E. coli
- **Expression construct**: Full-length Mhp1
- **Tag info**: His-tag (see supporting material)

<table class="wiki-table">
  <thead><tr>
    <th>Step</th>
    <th>Method</th>
    <th>Resin / Column</th>
    <th>Buffer + Detergent</th>
    <th>Notes</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>Expression</td>
      <td>E. coli fermentation</td>
      <td>—</td>
      <td>— + —</td>
      <td>Overexpression in E. coli</td>
    </tr>
    <tr>
      <td>Purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> (see supporting material)</td>
      <td>—</td>
      <td>— + —</td>
      <td>Details in supporting online material</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified Mhp1 in detergent solution
**Yield**: —
**Purity**: —

### doi/10.1126##science.1186303

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/— (see supporting material)">— (SEE SUPPORTING MATERIAL)</a></td>
      <td>3.8</td>
      <td>—</td>
      <td>Full-length Mhp1 (residues 6-470)</td>
      <td>—</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli (see supporting material)
- **Construct**: Full-length Mhp1
- **Notes**: Details in supporting online material (reference 24)


## Biological / Functional Insights

### Inverted Topology Repeat Architecture

Mhp1 contains 12 transmembrane helices arranged in two inverted repeats of five helices (TMs 1-5 and TMs 6-10) followed by two additional transmembrane helices. The two repeats are related by a 168° rotation around an axis parallel to the membrane plane. This inverted topology repeat is a common feature of many membrane transporters.

### Substrate Binding Site

The substrate [Benzyl-Hydantoin](/xray-mp-wiki/reagents/ligands/benzyl-hydantoin/) binds at the breaks in discontinuous TMs 1 and 6, facing TMs 3 and 8. Key interactions include pi-stacking with Trp117 (TM3) and Trp220 (TM6), and hydrogen bonding with Asn318 and Gln121. Trp220 moves into the binding site upon substrate binding, forming a pi-stacking interaction with the benzyl moiety.

### Sodium Coupling

A sodium-binding site is located at the C-terminal end of TM1a interacting with TM8, involving carbonyl oxygens of Ala38 and Ile41 (TM1), Ala309 (TM8), and side chain hydroxyls of Ser312 and Thr313. Fluorescence quenching experiments confirmed that sodium enhances [Benzyl-Hydantoin](/xray-mp-wiki/reagents/ligands/benzyl-hydantoin/) affinity over 10-fold (Kd from 0.88 mM to 0.054 mM), and vice versa, demonstrating coupled binding.

### Three Conformational States of the Transport Cycle

Three crystal structures of Mhp1 capture the complete alternating access cycle: outward-facing (substrate-free), occluded (substrate-bound), and inward-facing (substrate-free). The transition from outward-facing to occluded involves the N-terminal end of TM10 acting as an extracellular thin gate, folding over the bound substrate. The transition from occluded to inward-facing involves a 30° rotation (with 3 Å translation) of the hash motif (TMs 3, 4, 8, 9) relative to the bundle (TMs 1, 2, 6, 7) around an axis 40° to the membrane plane. TM5 acts as an intracellular thin gate that bends to open the inward-facing cavity.

### Rocking-Bundle Mechanism

The conformational changes between outward- and inward-facing states of Mhp1 are consistent with the rocking-bundle model. The bundle (TMs 1, 2, 6, 7) and hash motif (TMs 3, 4, 8, 9) move as rigid bodies relative to each other, with no substantial conformational changes within individual helices TMs 1 and 6 (unlike the flexing mechanism proposed for [LEUT](/xray-mp-wiki/proteins/enzymes/leut/) and [ADIC](/xray-mp-wiki/proteins/slc-transporters/adic/)). TMs 5 and 10 function as flexible helices that bend during the transition. This mechanism is supported by molecular dynamics simulations using dynamic importance sampling (DIMS MD), which show no large steric or energetic barriers to the proposed transition.

### Thick Gate and Thin Gate Model

The transport mechanism involves two types of gates. Thin gates (TM10 for extracellular, TM5 for intracellular) control rapid access and egress of substrates on the nanosecond timescale and can sample open/closed states stochastically. The thick gate (hash motif — TMs 3, 4, 8, 9) undergoes a slower 30° rotation that is the rate-limiting step of the transport process. MD simulations showed the thick gate does not spontaneously transition within 1.6 microseconds of simulation, confirming it as the rate-determining step.

### Comparison with LeuT Superfamily Members

The inward-facing Mhp1 structure resembles the inward-facing [VSGLT](/xray-mp-wiki/proteins/slc-transporters/vsglt/) more closely than the outward-facing [LEUT](/xray-mp-wiki/proteins/enzymes/leut/). The RMSD between Mhp1 outward- and inward-facing states is 3.3 Å. Bundle residues from all three conformations superpose with RMSD 0.7 Å, hash motif residues with RMSD 0.9 Å, and C-terminal helices with RMSD 0.9 Å, confirming rigid body movements between states.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/ncs1-family/">Nucleobase-Cation-Symport-1 (NCS1) Family</a> — Mhp1 is the founding structurally characterized member of the NCS1 family
- <a href="/xray-mp-wiki/proteins/slc-transporters/vsglt/">V. parahaemolyticus Sodium-Galactose Transporter (vSGLT)</a> — vSGLT shares the same structural fold and inward-facing Mhp1 resembles inward-facing vSGLT
- <a href="/xray-mp-wiki/proteins/enzymes/leut/">LeuT Amino Acid Transporter</a> — LeuT shares a nearly identical fold and was used for structural comparison
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating Access Mechanism</a> — Mhp1 three-state structure provides a complete picture of the alternating access cycle
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/rocking-bundle-mechanism/">Rocking-Bundle Mechanism</a> — Mhp1 conformational changes are consistent with the rocking-bundle model
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/slc-transporters/adic/">ADIC</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine (SeMet)</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/ligands/benzyl-hydantoin/">Benzyl-Hydantoin</a> — Related ligand or cofactor
