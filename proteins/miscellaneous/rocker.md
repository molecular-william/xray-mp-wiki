---
title: "Rocker — De Novo Designed Zn²⁺ Transporter"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1261172]
verified: false
---

# Rocker — De Novo Designed Zn²⁺ Transporter

## Overview

Rocker is a de novo designed membrane-spanning four-helical bundle that
transports first-row transition metal ions Zn²⁺ and Co²⁺, but not Ca²⁺,
across membranes. The conduction path was designed to contain two di-metal
binding sites that bind with negative cooperativity. The overall helical
bundle is formed from two tightly interacting pairs of helices, which form
individual domains that interact weakly along a more dynamic interface.
Rocker functions as a Zn²⁺/H⁺ antiporter, using a Zn²⁺ gradient to drive
reverse proton transport. This work represents the first high-resolution
structure of a designed membrane protein, demonstrating the feasibility of
designing membrane proteins with predefined structural and dynamic properties.


## Publications

### doi/10.1126##science.1261172

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4p6j">4P6J</a></td>
      <td>2.7-2.8</td>
      <td>Multiple non-isomorphous</td>
      <td>Zn²⁺-free Rocker four-helix bundle</td>
      <td>None (apo form)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Not specified
- **Construct**: De novo designed four-helix bundle with 4Glu-2His di-Zn²⁺-binding sites, ExxH motifs
- **Notes**: Designed computationally. Contains tight and loose helix-helix interfaces. Tight interface stabilized by Ala-rich packing. Loose interface packed by large Phe residues.

**Purification:**

- **Expression system**: Not specified
- **Expression construct**: Rocker four-helix bundle with designed metal-binding sites

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
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/dpc/">DPC</a> (<a href="/xray-mp-wiki/reagents/detergents/dodecylphosphocholine/">DPC</a>) for AUC and solution NMR; <a href="/xray-mp-wiki/reagents/lipids/dmpc/">DMPC</a> bilayers for SSNMR; <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> for LCP crystallization</td>
      <td>Rocker was solubilized in micelles for solution studies and reconstituted in phospholipid bilayers for SSNMR. X-ray structures obtained from both micelle and <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> LCP conditions.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (from micelles) and <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (<a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Zn²⁺-free Rocker</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> (for LCP crystallization)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Three non-isomorphous space groups obtained. Data extended between 2.7 and 2.8 Å. Structures solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a>. Dimers composed of straight alpha helices interacting along the tight interface.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4p6j">4P6J</a> — Chain A (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20      </span>
<span class="topo-line"><span class="topo-outside">Y?K</span><span class="topo-membrane">EIAHALFSALFALSELYIAV</span><span class="topo-inside">RY</span><span class="topo-unknown">?</span></span>
<details class="topo-details"><summary>Topology coordinates (4 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>23</td>
      <td>4</td>
      <td>23</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>25</td>
      <td>24</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>26</td>
      <td>26</td>
      <td>26</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4p6j">4P6J</a> — Chain B (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20      </span>
<span class="topo-line"><span class="topo-inside">Y?KE</span><span class="topo-membrane">IAHALFSALFALSELYIA</span><span class="topo-outside">VRY</span><span class="topo-unknown">?</span></span>
<details class="topo-details"><summary>Topology coordinates (4 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>22</td>
      <td>5</td>
      <td>22</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>23</td>
      <td>25</td>
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>26</td>
      <td>26</td>
      <td>26</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### De novo design of functional membrane protein

Rocker is the first designed membrane protein whose structure has been
experimentally determined at high resolution. The design combines
traditional computational design with biophysically motivated
conformational ensemble-based reasoning. The design achieved
function without high-throughput screening or directed evolution.

### Designed tight and loose helix-helix interfaces

The dimer of dimers architecture has two non-equivalent interfaces:
a "tight interface" with small interhelical distance (8.9 Å)
stabilized by Ala-rich packing (alanine coil motif), and a "loose
interface" with larger interhelical distance (12.0 Å) packed by
large Phe residues. The loose interface is thermodynamically less
stable and geometrically more flexible, facilitating ion motion.

### Negative cooperativity between metal-binding sites

Solution NMR titration showed two Zn²⁺ ions bind per tetramer at
high affinity, followed by much weaker association at a second
binding site. This negative cooperativity between the two di-Zn²⁺
binding sites is consistent with the design strategy inspired by
the [Alternating Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) of natural transporters.

### Zn²⁺/H⁺ antiport activity

Rocker transports Zn²⁺ with Michaelis-Menten kinetics (KM = 280 ±
90 µM for Zn²⁺). A Zn²⁺ gradient drives uphill proton transport
with a stoichiometry of 3-4 H⁺ per Zn²⁺. Co²⁺ is also transported
(KM = 1400 ± 200 µM, Vmax = 470 ± 40 min⁻¹). Ca²⁺ is not
transported. Proton-Zn²⁺ coupling is linked through displacement
of protons upon Zn²⁺ binding to the Glu/His ligands.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/dodecylphosphocholine/">Dodecylphosphocholine (DPC)</a> — Primary micelle-forming detergent for AUC and solution NMR characterization
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> — Buffer used in purification and sample preparation
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating Access Mechanism</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/detergents/dpc/">DPC</a> — Detergent used in purification or crystallization
- <a href="/xray-mp-wiki/reagents/lipids/dmpc/">DMPC</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Additive used in purification or crystallization buffers
