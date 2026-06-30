---
title: "MvINS - Mycobacterial Insig Homolog from Mycobacterium vanbaalenii"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.aab1091]
verified: false
---

# MvINS - Mycobacterial Insig Homolog from Mycobacterium vanbaalenii

## Overview

MvINS is a mycobacterial homolog of mammalian Insig proteins, identified from Mycobacterium vanbaalenii PYR-1 through BLAST searches using human Insig-1 and Insig-2 as queries. MvINS shares 23% and 26% sequence identity with Insig-1 and Insig-2, respectively (40% similarity with both). The crystal structure was determined at 1.9 Å resolution (Hg-SAD phasing), revealing a novel six-transmembrane helix fold that is likely shared by all Insig proteins. Each MvINS protomer contains a V-shaped cavity that accommodates one diacylglycerol ([DAG](/xray-mp-wiki/reagents/lipids/dag/)) molecule, with the DAG-bound structure determined at 2.1 Å resolution. MvINS forms a homotrimer in the crystal and in solution, with the trimeric interface mediated exclusively by hydrophobic residues on TM3 and TM4. Based on the MvINS structure, a homologous model of human Insig-2 was generated, identifying residues involved in 25-hydroxycholesterol (25HC) binding and Scap association.


## Publications

### doi/10.1126##science.aab1091

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4xu4">4XU4</a></td>
      <td>1.9</td>
      <td>R3</td>
      <td>Full-length MvINS (residues 1-199)</td>
      <td>—</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4xu4">4XU4</a></td>
      <td>2.1</td>
      <td>—</td>
      <td>Full-length MvINS</td>
      <td>Diacylglycerol (bromine-derived <a href="/xray-mp-wiki/reagents/lipids/dag/">DAG</a>)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: Full-length MvINS
- **Notes**: Overexpressed in E. coli; purification details in supporting online material

**Purification:**

- **Expression system**: E. coli
- **Expression construct**: Full-length MvINS
- **Tag info**: —

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
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>—</td>
      <td>— + <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a> (n-dodecyl-N,N-dimethylamine-N-oxide)</td>
      <td>Protein extracted and purified in <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a> detergent; native structure crystals appeared under different detergents</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified MvINS in [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) or Cymal-7 detergent
**Yield**: —
**Purity**: —

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified MvINS</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals appeared in several conditions under different detergents and diffracted X-rays beyond 2.0 Å resolution. Native structure determined by Hg-SAD from mercury-derivatized crystals. DAG-bound structure obtained by co-crystallization with a bromine-derived <a href="/xray-mp-wiki/reagents/lipids/dag/">DAG</a> in Cymal-7 detergent.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4xu4">4XU4</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MRLRISEA</span><span class="topo-membrane">VVLFLLGAVAALIGDHSH</span><span class="topo-inside">VVTGTTVYHTDAVP</span><span class="topo-membrane">FVWSSPFWFPILVGAATASLA</span><span class="topo-outside">ELRLHLPAPRDGVTARQA</span><span class="topo-membrane">LGGVAAVVGTYVTTALVH</span><span class="topo-inside">AFPV</span><span class="topo-membrane">VPVTALVCAAAAITWCV</span><span class="topo-outside">LG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210</span>
<span class="topo-line"><span class="topo-outside">DGPG</span><span class="topo-membrane">AACGVVIAVIGPAVEIAL</span><span class="topo-inside">VQLGVFAYHPDSDGLFGV</span><span class="topo-membrane">APFLAPLYFAFGVVAA</span><span class="topo-outside">LLGELAVARRPQL</span><span class="topo-unknown">GPPVCDTVSRGPGAGHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>8</td>
      <td>1</td>
      <td>8</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>26</td>
      <td>9</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>40</td>
      <td>27</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>61</td>
      <td>41</td>
      <td>61</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>79</td>
      <td>62</td>
      <td>79</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>97</td>
      <td>80</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>98</td>
      <td>101</td>
      <td>98</td>
      <td>101</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>118</td>
      <td>102</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>124</td>
      <td>119</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>142</td>
      <td>125</td>
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
      <td>176</td>
      <td>161</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>189</td>
      <td>177</td>
      <td>189</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4xu4">4XU4</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MRLRISEA</span><span class="topo-membrane">VVLFLLGAVAALIGDHSH</span><span class="topo-inside">VVTGTTVYHTDAVP</span><span class="topo-membrane">FVWSSPFWFPILVGAATASLA</span><span class="topo-outside">ELRLHLPAPRDGVTARQA</span><span class="topo-membrane">LGGVAAVVGTYVTTALVH</span><span class="topo-inside">AFPV</span><span class="topo-membrane">VPVTALVCAAAAITWCV</span><span class="topo-outside">LG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210</span>
<span class="topo-line"><span class="topo-outside">DGPG</span><span class="topo-membrane">AACGVVIAVIGPAVEIAL</span><span class="topo-inside">VQLGVFAYHPDSDGLFGV</span><span class="topo-membrane">APFLAPLYFAFGVVAA</span><span class="topo-outside">LLGELAVARRPQL</span><span class="topo-unknown">GPPVCDTVSRGPGAGHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>8</td>
      <td>1</td>
      <td>8</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>26</td>
      <td>9</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>40</td>
      <td>27</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>61</td>
      <td>41</td>
      <td>61</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>79</td>
      <td>62</td>
      <td>79</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>97</td>
      <td>80</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>98</td>
      <td>101</td>
      <td>98</td>
      <td>101</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>118</td>
      <td>102</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>124</td>
      <td>119</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>142</td>
      <td>125</td>
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
      <td>176</td>
      <td>161</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>189</td>
      <td>177</td>
      <td>189</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4xu4">4XU4</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MRLRISEA</span><span class="topo-membrane">VVLFLLGAVAALIGDHSH</span><span class="topo-inside">VVTGTTVYHTDAVP</span><span class="topo-membrane">FVWSSPFWFPILVGAATASLA</span><span class="topo-outside">ELRLHLPAPRDGVTARQA</span><span class="topo-membrane">LGGVAAVVGTYVTTALVH</span><span class="topo-inside">AFPV</span><span class="topo-membrane">VPVTALVCAAAAITWCV</span><span class="topo-outside">LG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210</span>
<span class="topo-line"><span class="topo-outside">DGPG</span><span class="topo-membrane">AACGVVIAVIGPAVEIAL</span><span class="topo-inside">VQLGVFAYHPDSDGLFGV</span><span class="topo-membrane">APFLAPLYFAFGVVAA</span><span class="topo-outside">LLGELAVARRPQL</span><span class="topo-unknown">GPPVCDTVSRGPGAGHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>8</td>
      <td>1</td>
      <td>8</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>26</td>
      <td>9</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>40</td>
      <td>27</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>61</td>
      <td>41</td>
      <td>61</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>79</td>
      <td>62</td>
      <td>79</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>97</td>
      <td>80</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>98</td>
      <td>101</td>
      <td>98</td>
      <td>101</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>118</td>
      <td>102</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>124</td>
      <td>119</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>142</td>
      <td>125</td>
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
      <td>176</td>
      <td>161</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>189</td>
      <td>177</td>
      <td>189</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4xu4">4XU4</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MRLRISEA</span><span class="topo-membrane">VVLFLLGAVAALIGDHSH</span><span class="topo-inside">VVTGTTVYHTDAVP</span><span class="topo-membrane">FVWSSPFWFPILVGAATASLA</span><span class="topo-outside">ELRLHLPAPRDGVTARQA</span><span class="topo-membrane">LGGVAAVVGTYVTTALVH</span><span class="topo-inside">AFPV</span><span class="topo-membrane">VPVTALVCAAAAITWCV</span><span class="topo-outside">LG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210</span>
<span class="topo-line"><span class="topo-outside">DGPG</span><span class="topo-membrane">AACGVVIAVIGPAVEIAL</span><span class="topo-inside">VQLGVFAYHPDSDGLFGV</span><span class="topo-membrane">APFLAPLYFAFGVVAA</span><span class="topo-outside">LLGELAVARRPQL</span><span class="topo-unknown">GPPVCDTVSRGPGAGHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>8</td>
      <td>1</td>
      <td>8</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>26</td>
      <td>9</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>40</td>
      <td>27</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>61</td>
      <td>41</td>
      <td>61</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>79</td>
      <td>62</td>
      <td>79</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>97</td>
      <td>80</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>98</td>
      <td>101</td>
      <td>98</td>
      <td>101</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>118</td>
      <td>102</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>124</td>
      <td>119</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>142</td>
      <td>125</td>
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
      <td>176</td>
      <td>161</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>189</td>
      <td>177</td>
      <td>189</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4xu4">4XU4</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MRLRISEA</span><span class="topo-membrane">VVLFLLGAVAALIGDHSH</span><span class="topo-inside">VVTGTTVYHTDAVP</span><span class="topo-membrane">FVWSSPFWFPILVGAATASLA</span><span class="topo-outside">ELRLHLPAPRDGVTARQA</span><span class="topo-membrane">LGGVAAVVGTYVTTALVH</span><span class="topo-inside">AFPV</span><span class="topo-membrane">VPVTALVCAAAAITWCV</span><span class="topo-outside">LG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210</span>
<span class="topo-line"><span class="topo-outside">DGPG</span><span class="topo-membrane">AACGVVIAVIGPAVEIAL</span><span class="topo-inside">VQLGVFAYHPDSDGLFGV</span><span class="topo-membrane">APFLAPLYFAFGVVAA</span><span class="topo-outside">LLGELAVARRPQL</span><span class="topo-unknown">GPPVCDTVSRGPGAGHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>8</td>
      <td>1</td>
      <td>8</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>26</td>
      <td>9</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>40</td>
      <td>27</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>61</td>
      <td>41</td>
      <td>61</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>79</td>
      <td>62</td>
      <td>79</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>97</td>
      <td>80</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>98</td>
      <td>101</td>
      <td>98</td>
      <td>101</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>118</td>
      <td>102</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>124</td>
      <td>119</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>142</td>
      <td>125</td>
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
      <td>176</td>
      <td>161</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>189</td>
      <td>177</td>
      <td>189</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4xu4">4XU4</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MRLRISEA</span><span class="topo-membrane">VVLFLLGAVAALIGDHSH</span><span class="topo-inside">VVTGTTVYHTDAVP</span><span class="topo-membrane">FVWSSPFWFPILVGAATASLA</span><span class="topo-outside">ELRLHLPAPRDGVTARQA</span><span class="topo-membrane">LGGVAAVVGTYVTTALVH</span><span class="topo-inside">AFPV</span><span class="topo-membrane">VPVTALVCAAAAITWCV</span><span class="topo-outside">LG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210</span>
<span class="topo-line"><span class="topo-outside">DGPG</span><span class="topo-membrane">AACGVVIAVIGPAVEIAL</span><span class="topo-inside">VQLGVFAYHPDSDGLFGV</span><span class="topo-membrane">APFLAPLYFAFGVVAA</span><span class="topo-outside">LLGELAVARRPQL</span><span class="topo-unknown">GPPVCDTVSRGPGAGHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>8</td>
      <td>1</td>
      <td>8</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>26</td>
      <td>9</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>40</td>
      <td>27</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>61</td>
      <td>41</td>
      <td>61</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>79</td>
      <td>62</td>
      <td>79</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>97</td>
      <td>80</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>98</td>
      <td>101</td>
      <td>98</td>
      <td>101</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>118</td>
      <td>102</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>124</td>
      <td>119</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>142</td>
      <td>125</td>
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
      <td>176</td>
      <td>161</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>189</td>
      <td>177</td>
      <td>189</td>
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

### Novel Insig Fold and Internal Symmetry

MvINS comprises six transmembrane segments (TMs 1-6) with both N- and C-termini on the cytosolic side. TM1/TM2 and TM5/TM6 display an internal pseudo twofold symmetry around an axis perpendicular to the membrane plane and superimpose with RMSD of 1.49 Å over 60 Cα atoms. These four TMs form a helical bundle tilted counterclockwise. Connecting sequences between TM1 and TM2 form a short β-strand that caps the cavity on the periplasmic side. Given the level of sequence conservation, all Insig proteins likely exhibit the same fold.

### Homotrimeric Assembly

MvINS forms a homotrimer both in the crystal and in solution. The trimeric interface is mediated exclusively through van der Waals interactions between TM3 of one protomer and TM4 of the adjacent protomer. The trimeric assembly was confirmed by a disulfide bond-mediated cross-linking strategy (MvINS-R77C mutant), which formed a stable homotrimer upon induction of disulfide bond formation.

### DAG Binding in a V-Shaped Cavity

Each MvINS protomer encloses a V-shaped cavity that accommodates one diacylglycerol ([DAG](/xray-mp-wiki/reagents/lipids/dag/)) molecule. The [DAG](/xray-mp-wiki/reagents/lipids/dag/) head group and Sn-1 tail are coordinated by residues from TM1/2/3/6 and periplasmic β-strands, while the Sn-2 tail extends into the lipid bilayer through a cleft between TM2 and TM5. The polar head is coordinated by hydrogen bonds from Asp23 and His26 on TM1, Tyr34 on β1-2, and Tyr150 on β5-6. The Sn-1 aliphatic tail is completely buried and surrounded by hydrophobic residues mainly from TM6, while the Sn-2 chain is loosely coordinated by residues from TM2/5.

### Structural Model of Human Insig-2

Based on the MvINS structure and sequence similarity, a three-dimensional structural model for the transmembrane domain of human Insig-1/2 was generated. The model identified key residues involved in 25HC (25-hydroxycholesterol) binding and Scap association. Phe115 on the cavity-facing side of TM3 is critical for 25HC recognition. Mutations G39F, C77D, or G200F resulted in compromised mScap-TMD binding in the presence of 25HC. Residues Gln132/Trp145/Asp149 mediate interactions with Scap but are not required for 25HC binding.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO (n-Dodecyl-N,N-Dimethylamine-N-oxide)</a> — LDAO was used as the detergent for MvINS purification and initial crystallization
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating Access Mechanism</a> — MvINS provides structural insights into how Insig proteins function as sterol sensors in the SREBP pathway
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a> — Detergent used in purification or crystallization
- <a href="/xray-mp-wiki/reagents/lipids/dag/">DAG</a> — Additive used in purification or crystallization buffers
