---
title: "PL5 Designed Pentameric Transmembrane Protein"
created: 2026-06-10
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.aav7541]
verified: agent
---

# PL5 Designed Pentameric Transmembrane Protein


## Overview

PL5 is a designed homopentameric transmembrane helical bundle based on the apolar C-terminal domain of [PLB](/xray-mp-wiki/proteins/miscellaneous/phospholamban/) (PLN). It was designed to test whether apolar side-chain packing alone is sufficient to drive membrane protein folding and assembly. PL5 retains PLN's C-terminal LxxIxxx motif but replaces polar N-terminal residues (Asn, Ser, Cys) with fully hydrophobic isosteric residues (EtGly, Leu, Phe). The designed protein forms stable pentamers confirmed by MD simulation, analytical ultracentrifugation, SDS-PAGE thermal stability assays, and X-ray crystallography (PDB 6MQU, 1.75-Å resolution). The structure reveals knobs-into-holes packing at the d/e and a/g interfaces, defining a steric packing code for transmembrane helix assembly.


## Publications

### doi/10.1126##science.aav7541

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6mqu">6MQU</a></td>
      <td>1.75</td>
      <td>TBD</td>
      <td>PL5; designed pentameric transmembrane helical bundle based on PLN C-terminal domain with polar-to-apolar mutations</td>
      <td>None (all apolar side chains)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Synthetic peptide (solid-phase synthesis)
- **Construct**: PL5, PL5_EtG, PL5_EtG3 variants

**Purification:**

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
      <td>Solid-phase peptide synthesis</td>
      <td>Chemical synthesis</td>
      <td>—</td>
      <td></td>
      <td>Synthesized with C-terminal amidation. EtGly residues incorporated as S-C-alpha-ethyl-Gly for fully hydrophobic isosteres.</td>
    </tr>
    <tr>
      <td>Reconstitution in micelles</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td></td>
      <td>Peptides reconstituted in myristyl sulfobetaine micelles or <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a>/LDS for characterization.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals obtained from detergent solution. Structure solved at 1.75 A resolution.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mqu">6MQU</a> — Chain A (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30   </span>
<span class="topo-line"><span class="topo-unknown">DP</span><span class="topo-outside">EQLKW</span><span class="topo-membrane">ISFCLFLICLLLLCIIFMLY</span><span class="topo-inside">RG</span><span class="topo-unknown">?GS?</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>3</td>
      <td>7</td>
      <td>3</td>
      <td>7</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>27</td>
      <td>8</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>29</td>
      <td>28</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mqu">6MQU</a> — Chain B (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30   </span>
<span class="topo-line"><span class="topo-unknown">DP</span><span class="topo-outside">EQLKW</span><span class="topo-membrane">ISFCLFLICLLLLCIIFMLY</span><span class="topo-inside">RG</span><span class="topo-unknown">?GS?</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>3</td>
      <td>7</td>
      <td>3</td>
      <td>7</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>27</td>
      <td>8</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>29</td>
      <td>28</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mqu">6MQU</a> — Chain C (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30   </span>
<span class="topo-line"><span class="topo-unknown">D</span><span class="topo-outside">PEQLKW</span><span class="topo-membrane">ISFCLFLICLLLLCIIFMLY</span><span class="topo-inside">RG</span><span class="topo-unknown">?GS?</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>27</td>
      <td>8</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>29</td>
      <td>28</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mqu">6MQU</a> — Chain D (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30   </span>
<span class="topo-line"><span class="topo-unknown">DP</span><span class="topo-outside">EQLKW</span><span class="topo-membrane">ISFCLFLICLLLLCIIFMLY</span><span class="topo-inside">RG</span><span class="topo-unknown">?GS?</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>3</td>
      <td>7</td>
      <td>3</td>
      <td>7</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>27</td>
      <td>8</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>29</td>
      <td>28</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mqu">6MQU</a> — Chain E (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30   </span>
<span class="topo-line"><span class="topo-unknown">DPE</span><span class="topo-outside">QLKW</span><span class="topo-membrane">ISFCLFLICLLLLCIIFMLY</span><span class="topo-inside">RG</span><span class="topo-unknown">?GS?</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>4</td>
      <td>7</td>
      <td>4</td>
      <td>7</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>27</td>
      <td>8</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>29</td>
      <td>28</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Apolar packing alone drives pentameric assembly

PL5 forms stable pentamers stabilized entirely by van der Waals interactions between apolar side chains, with no interhelical hydrogen bonds. The pentamer is resistant to heating at 95 C in 2% LDS, 8 M [UREA](/xray-mp-wiki/reagents/substrates/urea/), demonstrating extreme thermostability. Analytical ultracentrifugation confirms the pentameric oligomeric state (apparent MW 18 kDa, expected 19 +/- 1.5 kDa).

### Knobs-into-holes packing code

The crystal structure reveals two distinct packing interfaces: d/e interface and a/g interface (using heptad repeat notation abcdefg). At the d/e interface, beta-branched amino acids (Ile, Val) pack tightly with their C-beta-C-gamma bonds directed inward. At the a/g interface, non-beta-branched residues are preferred because beta-branched residues would create steric clashes. This defines a steric packing code for transmembrane five-helix bundle assembly.

### Stringent steric complementarity requirement

Single conservative mutations (e.g., Leu-to-Ile at a g position) can entirely destabilize the pentamer. This demonstrates an unexpectedly stringent requirement for steric complementarity in membrane protein folding, where the hydrophobic effect is negligible unlike in soluble protein folding.


## Cross-References

- <a href="/xray-mp-wiki/proteins/miscellaneous/phospholamban/">Phospholamban (PLB)</a> — PL5 is derived from the apolar C-terminal domain of PLN; the design revealed the steric packing code underlying PLN assembly
- <a href="/xray-mp-wiki/concepts/membrane-mimetics/computational-transmembrane-protein-design/">Computational Design of Multipass Transmembrane Proteins</a> — Complementary approach to computational TM protein design using apolar packing rather than hydrogen bond networks
- <a href="/xray-mp-wiki/reagents/substrates/urea/">UREA</a> — Entity mentioned in text
