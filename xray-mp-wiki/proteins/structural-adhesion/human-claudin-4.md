---
title: "Human Claudin-4 (hCLDN-4)"
created: 2026-06-11
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.2024651118]
verified: regex
uniprot_id: ['O14493', 'P01558']
---

# Human Claudin-4 (hCLDN-4)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/O14493">UniProt: O14493</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P01558">UniProt: P01558</a>

<span class="expr-badge">Clostridium perfringens</span>

## Overview

Human claudin-4 (hCLDN-4) is a 23-34 kDa tetraspanning tight junction membrane protein
belonging to the claudin family of 27 human isoforms. It is a critical component of
epithelial tight junctions, functioning primarily as a cation barrier to reduce paracellular
Na+ permeability. hCLDN-4 is upregulated in the large intestine and is a primary high-affinity
receptor for Clostridium perfringens enterotoxin (CpE) in humans. The crystal structure of
hCLDN-4 in complex with the C-terminal receptor-binding domain of CpE (cCpE) was solved at
3.37 A resolution (PDB 7KP4), revealing the NPLVA153 motif on extracellular segment 2 (ECS2)
as the key toxin-binding determinant. A leucine at position 3 of this motif (Leu153) imparts
high-affinity CpE binding (Kd = 2.5 nM), distinguishing hCLDN-4 as the primary human CpE
receptor, in contrast to mice where CLDN-3 and CLDN-8 serve this role.


## Publications

### doi/10.1073##pnas.2024651118

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7kp4">7KP4</a></td>
      <td>3.37</td>
      <td></td>
      <td>hCLDN-4 residues 5-186 with C-terminal affinity tag, in complex with cCpE</td>
      <td>cCpE (Clostridium perfringens enterotoxin C-terminal domain)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells via baculovirus
- **Construct**: Full-length human CLDN-4 with C-terminal tag
- **Notes**: Expressed using Bac-to-Bac baculovirus expression system

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
      <td>Membrane preparation</td>
      <td>Homogenization and centrifugation</td>
      <td>—</td>
      <td></td>
      <td>Membranes collected from Sf9 cell pellets</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>1% n-undecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/udm/">UDM</a>)</td>
      <td>Membrane proteins solubilized from Sf9 cell membranes</td>
    </tr>
    <tr>
      <td>Complex formation</td>
      <td>Incubation with cCpE</td>
      <td>—</td>
      <td></td>
      <td>Purified hCLDN-4 mixed with cCpE to form complex</td>
    </tr>
    <tr>
      <td>Gel filtration</td>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM HEPES pH 7.5, 150 mM NaCl, 0.22 M <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>hCLDN-4/cCpE complex purified to homogeneity</td>
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
      <td>Protein sample</td>
      <td>hCLDN-4/cCpE complex</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Data collected at ALS beamline 8.3.1. Structure determined by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a>. Resolution 3.37 A.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7kp4">7KP4</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MASM</span><span class="topo-outside">GLQ</span><span class="topo-membrane">VMGIALAVLGWLAVMLCCALPMW</span><span class="topo-inside">RVTAFIGSNIVTSQTIWEGLWMNCVVQSTGQMQCKVYDSLLALPQ</span><span class="topo-membrane">DLQAARALVIISIIVAALGVLLSVV</span><span class="topo-outside">GGKCTNCLEDESAKAKTM</span><span class="topo-membrane">IV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210    </span>
<span class="topo-line"><span class="topo-membrane">AGVVFLLAGLMVIVPVSWTAHN</span><span class="topo-inside">IIQDFYNPLVASGQKREM</span><span class="topo-membrane">GASLYVGWAASGLLLLGGGLLCC</span><span class="topo-outside">NCP</span><span class="topo-unknown">PRTDKPYSAKYSAARSAAASNYVGLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>5</td>
      <td>7</td>
      <td>5</td>
      <td>7</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>30</td>
      <td>8</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>75</td>
      <td>31</td>
      <td>75</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>76</td>
      <td>100</td>
      <td>76</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>118</td>
      <td>101</td>
      <td>118</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>142</td>
      <td>119</td>
      <td>142</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>143</td>
      <td>160</td>
      <td>143</td>
      <td>160</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>183</td>
      <td>161</td>
      <td>183</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>184</td>
      <td>186</td>
      <td>184</td>
      <td>186</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7kp4">7KP4</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MSTDIEKEILDLAAATERLNLTDALNSNPAGNLYDWRSSNSYPWTQKLNLHLTITATGQKYRILASKIVDFNIYSNNFNNLVKLEQSLGDGVKDHYVDISLDAGQYVLVMKANSSYSGNY</span></span>
<span class="topo-ruler">       130    </span>
<span class="topo-line"><span class="topo-inside">PYSILFQKFGLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (1 regions)</summary>
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
      <td>134</td>
      <td>191</td>
      <td>324</td>
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

### NPLVA153 motif determines CpE binding affinity

The hCLDN-4 structure reveals that CpE targets the NPLVA153 motif on ECS2.
Position 3 (Leu153) is the critical determinant of binding affinity. A leucine
at this position provides extended hydrophobic side chain length that more deeply
penetrates a surface groove on cCpE, yielding high-affinity binding (Kd = 2.5 nM).
In contrast, hCLDN-3 has valine at this position (NPVVP152), resulting in 100-fold
lower affinity (Kd = 252 nM). Mutagenesis swapping Leu153 in hCLDN-4 to Val
(hCLDN-4 L151V/A153P) decreases cCpE affinity 5-fold, while swapping Val150 in
hCLDN-3 to Leu (hCLDN-3 V150L/P152A) increases affinity 12-fold. The dissociation
rate (koff) is the dominant kinetic parameter differentiating high- vs low-affinity
claudin-CpE complexes.

### hCLDN-4 as primary human CpE receptor

Based on correlation of binding affinities, kinetics, half-lives, and claudin
expression patterns in gut, hCLDN-4 is identified as the primary CpE receptor in
humans. High-affinity (<10 nM) CpE receptors in humans are CLDN-4, CLDN-6, and
CLDN-9. In contrast, the primary CpE receptors in mice are CLDN-3 and CLDN-8,
reflecting divergence in the NPLVA motif. hCLDN-4 has a complex half-life (t1/2)
of ~2 h with cCpE, allowing sustained toxin binding necessary for cytotoxicity.

### ECH1 structural plasticity upon CpE binding

The structure of hCLDN-4 lacks a fully formed ECH1 (extracellular helix 1) that
is present in unbound claudin structures such as mCLDN-15. ECH1 is involved in
claudin cis assembly. In hCLDN-4, the SLLALP74 region appears as a bulbous density
with helical phi/psi values, representing a helical remnant of ECH1 disrupted by
cCpE binding. CpE-induced structural plasticity of ECH1 may be how enterotoxin
disables claudin lateral (cis) assemblies, contributing to tight junction disassembly.

### hCLDN-4 ion selectivity: Lys65 as cation barrier determinant

hCLDN-4 functions as a cation barrier (reduces paracellular Na+ permeability)
due to Lys65 on beta-4 of ECS1. This lysine residue provides a positive charge
that repels cations, creating a cation-tight barrier. This contrasts with hCLDN-2
(Asp65, anion barrier/cation pore) and is shared with hCLDN-9 (Lys65).


## Cross-References

- <a href="/xray-mp-wiki/proteins/structural-adhesion/human-claudin-9/">Human Claudin-9 (hCLDN-9)</a> — Related claudin-CpE complex structure; both show conserved claudin fold and NPLVA motif for CpE binding
- <a href="/xray-mp-wiki/proteins/structural-adhesion/claudin-19-mouse/">Mouse Claudin-19 (mCldn19)</a> — Related claudin-C-CPE complex structure revealing shared CpE binding mode
- <a href="/xray-mp-wiki/reagents/ligands/c-cpe/">C-CPE (Clostridium perfringens Enterotoxin)</a> — hCLDN-4 is the primary human CpE receptor; structure reveals NPLVA motif recognition
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used in purification or crystallization
- <a href="/xray-mp-wiki/reagents/detergents/udm/">UDM</a> — Detergent used in purification or crystallization
