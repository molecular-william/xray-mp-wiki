---
title: "Human Claudin-9 (hCLDN-9)"
created: 2026-06-11
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1908929116]
verified: agent
uniprot_id: ['O95484', 'P01558']
---

# Human Claudin-9 (hCLDN-9)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/O95484">UniProt: O95484</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P01558">UniProt: P01558</a>

<span class="expr-badge">Clostridium perfringens</span>

## Overview

Human claudin-9 (hCLDN-9) is a tetraspanning tight junction membrane protein belonging
to the claudin family of 27 human isoforms. It is the highest-expressing claudin in
the inner ear and is essential for hearing, acting as a cation barrier to reduce
Na+ and K+ permeability in the endolymphatic system. hCLDN-9 also serves as an entry
coreceptor for hepatitis C virus (HCV) and is a high-affinity receptor for Clostridium
perfringens enterotoxin (CpE). Crystal structures of hCLDN-9 in complex with the
C-terminal receptor-binding domain of CpE (cCpE) were solved at 3.2 and 3.3 A
resolution, revealing the complete claudin structure with two distinct conformations
(closed and open) that show how CpE binding disrupts claudin self-assembly and tight
junction integrity.


## Publications

### doi/10.1073##pnas.1908929116

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ov2">6OV2</a></td>
      <td>3.2</td>
      <td>P2(1)2(1)2(1)</td>
      <td>Full-length human CLDN-9 with C-terminal His6 tag, in complex with cCpE (closed conformer)</td>
      <td>cCpE</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ov2">6OV2</a></td>
      <td>3.3</td>
      <td>P2(1)2(1)2(1)</td>
      <td>Full-length human CLDN-9 with C-terminal His6 tag, in complex with cCpE (open conformer)</td>
      <td>cCpE</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells via baculovirus
- **Construct**: Full-length human CLDN-9 with C-terminal His10 tag
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
      <td>20 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Membrane proteins solubilized for 2 h at 4 C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> affinity</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td></td>
      <td>His10-tagged hCLDN-9 purified by nickel affinity</td>
    </tr>
    <tr>
      <td>Complex formation</td>
      <td>Incubation with cCpE</td>
      <td>—</td>
      <td></td>
      <td>Purified hCLDN-9 mixed with cCpE at 1:1.5 molar ratio</td>
    </tr>
    <tr>
      <td>Gel filtration</td>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM HEPES pH 7.5, 150 mM NaCl, 0.22 M <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>hCLDN-9/cCpE complex purified to homogeneity</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>hCLDN-9/cCpE complex</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>150 mM Na(C2H5COO), NaO2As(CH3)2, Bis-Tris propane pH 4.5, 25% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 1500</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals cryoprotected and flash-frozen in liquid nitrogen. Data collected at ALS beamline 8.3.1. Structures determined by MR using homology model of hCLDN-9 and cCpE. Two distinct conformers captured: closed (cCpE deep in palm) and open (cCpE rocked outward).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ov2">6OV2</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAST</span><span class="topo-inside">GLEL</span><span class="topo-membrane">LGMTLAVLGWLGTLVSCALPLWK</span><span class="topo-outside">VTAFIGNSIVVAQVVWEGLWMSCVVQSTGQMQCKVYDSLLAL</span><span class="topo-membrane">PQDLQAARALCVIALLLALLGLLVAI</span><span class="topo-inside">TGAQCTTCVEDEGAKARIVLT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       </span>
<span class="topo-line"><span class="topo-membrane">AGVILLLAGILVLIPVCWTAHA</span><span class="topo-outside">IIQDFYNPLVAEALKREL</span><span class="topo-membrane">GASLYLGWAAAALLMLGGGLLC</span><span class="topo-inside">CTCP</span><span class="topo-unknown">PPQVERPRGPRLGYSIPSRSGASGLDKRDYV</span></span>
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
      <td>8</td>
      <td>5</td>
      <td>8</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>31</td>
      <td>9</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>73</td>
      <td>32</td>
      <td>73</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>99</td>
      <td>74</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>100</td>
      <td>120</td>
      <td>100</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>142</td>
      <td>121</td>
      <td>142</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>143</td>
      <td>160</td>
      <td>143</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>182</td>
      <td>161</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>186</td>
      <td>183</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ov2">6OV2</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">DIEK</span><span class="topo-outside">EILDLAAATERLNLTDALNSNPAGNLYDWRSSNSYPWTQKLNLHLTITATGQKYRILASKIVDFNIYSNNFNNLVKLEQSLGDGVKDHYVDISLDAGQYVLVMKANSSYSGNYPYS</span></span>
<span class="topo-ruler">       130 </span>
<span class="topo-line"><span class="topo-outside">ILFQKFGLVPR</span></span>
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
      <td>5</td>
      <td>131</td>
      <td>198</td>
      <td>324</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ov2">6OV2</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAST</span><span class="topo-inside">GLEL</span><span class="topo-membrane">LGMTLAVLGWLGTLVSCALPLWK</span><span class="topo-outside">VTAFIGNSIVVAQVVWEGLWMSCVVQSTGQMQCKVYDSLLAL</span><span class="topo-membrane">PQDLQAARALCVIALLLALLGLLVAI</span><span class="topo-inside">TGAQCTTCVEDEGAKARIVLT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       </span>
<span class="topo-line"><span class="topo-membrane">AGVILLLAGILVLIPVCWTAHA</span><span class="topo-outside">IIQDFYNPLVAEALKREL</span><span class="topo-membrane">GASLYLGWAAAALLMLGGGLLC</span><span class="topo-inside">CTCP</span><span class="topo-unknown">PPQVERPRGPRLGYSIPSRSGASGLDKRDYV</span></span>
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
      <td>8</td>
      <td>5</td>
      <td>8</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>31</td>
      <td>9</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>73</td>
      <td>32</td>
      <td>73</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>99</td>
      <td>74</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>100</td>
      <td>120</td>
      <td>100</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>142</td>
      <td>121</td>
      <td>142</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>143</td>
      <td>160</td>
      <td>143</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>182</td>
      <td>161</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>186</td>
      <td>183</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ov2">6OV2</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">DIEK</span><span class="topo-outside">EILDLAAATERLNLTDALNSNPAGNLYDWRSSNSYPWTQKLNLHLTITATGQKYRILASKIVDFNIYSNNFNNLVKLEQSLGDGVKDHYVDISLDAGQYVLVMKANSSYSGNYPYS</span></span>
<span class="topo-ruler">       130 </span>
<span class="topo-line"><span class="topo-outside">ILFQKFGLVPR</span></span>
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
      <td>5</td>
      <td>131</td>
      <td>198</td>
      <td>324</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Complete claudin structure with left-handed 4-TM bundle

hCLDN-9 reveals a left-handed four-transmembrane-helix bundle. The extracellular
domain consists of a five-stranded beta-sheet (four from ECS1, one from ECS2)
forming a hand-like epitope. ECS1 is fortified by a Cys54-Cys64 disulfide bond.
An additional Cys25-Cys84 disulfide links TM1 to TM2. The improved resolution
allows visualization of all nonterminal residues, resulting in the most complete
claudin structure to date.

### hCLDN-9 ion selectivity: Lys65 as cation barrier determinant

hCLDN-9 functions as a cation barrier. Sequence and structure comparison with
hCLDN-2 (anion barrier, Asp65) and hCLDN-4 (cation barrier, Lys65) identifies
hCLDN-9 Lys65 as a key residue for ion selectivity. Lys65 lies below the Cys54-Cys64
disulfide bond on beta-4. Residues at positions 31, 48, 53, and 65 on beta-1 to
beta-4 align on the same plane and could create a single-sided half-pore.

### CpE-induced claudin self-assembly disruption via lever mechanism

The cCpE-bound hCLDN-9 structures reveal two conformers: a closed form where
cCpE sits deep in the claudin palm, and an open form where cCpE rocks outward
via a rigid-body lever-like motion. Both conformers disrupt the two epitopes
known to enable claudin cis self-assembly. In the closed form, cCpE binding
breaks 80% (4 of 5) of the interatomic bonds at the cis interaction epitope.
In the open form, all cis interactions are abolished. CpE binding to the NPLVA153
motif on ECS2 also disrupts trans interactions. These mechanisms explain how CpE
dissociates tight junctions in gut epithelium.

### hCLDN-9 is a high-affinity CpE receptor

Biolayer interferometry (BLI) measurements show that hCLDN-9 binds CpE with a
Kd of 5.1 nM and cCpE with a Kd of 3.6 nM, comparable to the well-characterized
CpE receptors hCLDN-3 and hCLDN-4. CpE is cytotoxic to hCLDN-9-expressing Sf9
cells (59.2% decrease in viability), while cCpE (lacking the cytotoxic domain)
is not. This demonstrates that hCLDN-9 is a functional CpE receptor.


## Cross-References

- <a href="/xray-mp-wiki/proteins/structural-adhesion/claudin-19-mouse/">Mouse Claudin-19 (mCldn19)</a> — Related claudin structure in complex with C-CPE; both show conserved claudin fold and CpE binding mode
- <a href="/xray-mp-wiki/reagents/ligands/c-cpe/">C-CPE (Clostridium perfringens Enterotoxin)</a> — hCLDN-9 is a high-affinity CpE receptor; structures reveal mechanisms of CpE-induced TJ disassembly
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used in purification or crystallization
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used in purification or crystallization
