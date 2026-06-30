---
title: "Phosphatidylinositol Phosphate Synthase PgsA1 from Mycobacterium tuberculosis"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s42003-019-0427-1]
verified: false
---

# Phosphatidylinositol Phosphate Synthase PgsA1 from Mycobacterium tuberculosis

## Overview

Mycobacterium tuberculosis [Phosphatidylinositol](/xray-mp-wiki/reagents/lipids/phosphatidylinositol/) phosphate synthase (PgsA1)
is an integral membrane enzyme that catalyzes the formation of
[Phosphatidylinositol](/xray-mp-wiki/reagents/lipids/phosphatidylinositol/) phosphate (PIP) from CDP-diacylglycerol (CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag/)) and
[D-myo-Inositol-3-Phosphate](/xray-mp-wiki/reagents/ligands/d-myo-inositol-3-phosphate/) (ino-P). It belongs to the Class I
CDP-alcohol phosphotransferase (CDP-AP) family, which catalyzes
phosphodiester bond formation between a CDP-alcohol and a second alcohol,
releasing CMP. PgsA1 is essential for mycobacterial growth and
proliferation, as PIP is a precursor of [Phosphatidylinositol](/xray-mp-wiki/reagents/lipids/phosphatidylinositol/), which in
turn is the first building block in the biosynthesis of
[Phosphatidylinositol](/xray-mp-wiki/reagents/lipids/phosphatidylinositol/) mannosides, lipomannan, and lipoarabinomannan —
structurally complex constituents of the mycobacterial cell wall. PgsA1
is a potential drug target for novel anti-tuberculosis therapies due to
differences between eukaryotic and mycobacterial PI biosynthesis pathways.
This paper presents three crystal structures (apo at 2.9 Å, Mn-[Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/)
complex at 1.9 Å, and CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag/) complex at 1.8 Å) revealing atomic details
of substrate binding, metal coordination dynamics, and a refined catalytic
mechanism involving a substrate-induced [Carboxylate Shift](/xray-mp-wiki/concepts/structural-mechanisms/carboxylate-shift/).


## Publications

### doi/10.1038##s42003-019-0427-1

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6h53">6H53</a></td>
      <td>2.90</td>
      <td>P 21 21 21</td>
      <td>Full-length M. tuberculosis PgsA1 (Rv2612c) with TEV-cleavable N-terminal His-tag, homodimer</td>
      <td>None (apo structure)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6h5a">6H5A</a></td>
      <td>1.88</td>
      <td>P 21 21 21</td>
      <td>Full-length M. tuberculosis PgsA1 (Rv2612c) with TEV-cleavable N-terminal His-tag, homodimer</td>
      <td>Mn2+, <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> (Mn-<a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> complex)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6h59">6H59</a></td>
      <td>1.80</td>
      <td>P 21 21 2</td>
      <td>Full-length M. tuberculosis PgsA1 (Rv2612c) with TEV-cleavable N-terminal His-tag, homodimer</td>
      <td>CDP-<a href="/xray-mp-wiki/reagents/lipids/dag/">DAG</a>, Mg2+, sulfate</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length M. tuberculosis PgsA1 (Rv2612c; UniProt P9WPG7) with N-terminal His-tag and TEV-protease cleavage site

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
      <td>Cell culture and membrane preparation</td>
      <td>E. coli expression, cell lysis, membrane isolation</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Details described in Methods section</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA or similar</td>
      <td>-- + n-Octyl-β-D-glucopyranoside (OG) or similar</td>
      <td>His-tagged PgsA1 purified by IMAC</td>
    </tr>
    <tr>
      <td>TEV protease cleavage</td>
      <td>His-tagged TEV protease digestion</td>
      <td>--</td>
      <td>-- + --</td>
      <td>His-tag removed by TEV protease</td>
    </tr>
    <tr>
      <td>Reverse <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Second IMAC step</td>
      <td>Ni-NTA</td>
      <td>-- + --</td>
      <td>Cleaved protein collected in flowthrough</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified PgsA1 in detergent solution</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>100 K (data collection)</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Apo crystals obtained in one condition; Mn-<a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> complex from 100 mM <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a>, 120 mM Mn2+ in crystallization solution; CDP-<a href="/xray-mp-wiki/reagents/lipids/dag/">DAG</a> complex from co-crystallization with CDP-<a href="/xray-mp-wiki/reagents/lipids/dag/">DAG</a> and Mg2+ in LCP. Data collected at Diamond Light Source beamline I24.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6h53">6H53</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSKLPFLSRAAFARIT</span><span class="topo-inside">T</span><span class="topo-unknown">PIARGLLR</span><span class="topo-inside">VGLTPDV</span><span class="topo-membrane">VTILGTTASVAGALTLFP</span><span class="topo-outside">MGK</span><span class="topo-membrane">LFAGACVVWFFVLFDM</span><span class="topo-inside">LDGAMARERGGGTRFGAVLDAT</span><span class="topo-membrane">CDRISDGAVFCGLLW</span><span class="topo-outside">WIAFHMRDRP</span><span class="topo-membrane">LVIA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       </span>
<span class="topo-line"><span class="topo-membrane">TLICLVTSQVISY</span><span class="topo-inside">IKARAEASGLRGDGG</span><span class="topo-unknown">FIE</span><span class="topo-inside">R</span><span class="topo-membrane">PERLIIVLTGAGVS</span><span class="topo-outside">DFPFVPWPPA</span><span class="topo-membrane">LSVGMWLLAVASVITCV</span><span class="topo-inside">QRLHTVWTSPGAIDRM</span><span class="topo-unknown">AIPGKGDR</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
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
      <td>17</td>
      <td>17</td>
      <td>17</td>
      <td>17</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>25</td>
      <td>18</td>
      <td>25</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>26</td>
      <td>32</td>
      <td>26</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>50</td>
      <td>33</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>53</td>
      <td>51</td>
      <td>53</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>69</td>
      <td>54</td>
      <td>69</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>91</td>
      <td>70</td>
      <td>91</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>106</td>
      <td>92</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>116</td>
      <td>107</td>
      <td>116</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>133</td>
      <td>117</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>148</td>
      <td>134</td>
      <td>148</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>152</td>
      <td>152</td>
      <td>152</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>166</td>
      <td>153</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>176</td>
      <td>167</td>
      <td>176</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>193</td>
      <td>177</td>
      <td>193</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>194</td>
      <td>209</td>
      <td>194</td>
      <td>209</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6h53">6H53</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSKLPFLSRAAFARI</span><span class="topo-inside">TT</span><span class="topo-unknown">PIARGLLRV</span><span class="topo-inside">GLTPDVV</span><span class="topo-membrane">TILGTTASVAGALTLFP</span><span class="topo-outside">MGKL</span><span class="topo-membrane">FAGACVVWFFVLFDM</span><span class="topo-inside">LDGAMARERGGGTRFGAVLDAT</span><span class="topo-membrane">CDRISDGAVFCGLLW</span><span class="topo-outside">WIAFHMRDRPL</span><span class="topo-membrane">VIA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       </span>
<span class="topo-line"><span class="topo-membrane">TLICLVTSQVISY</span><span class="topo-inside">IKARAEASGLRGDGG</span><span class="topo-unknown">FIE</span><span class="topo-inside">R</span><span class="topo-membrane">PERLIIVLTGAGV</span><span class="topo-outside">SDFPFVPWPPA</span><span class="topo-membrane">LSVGMWLLAVASVITCVQ</span><span class="topo-inside">RLHTVWTSPGAIDRM</span><span class="topo-unknown">AIPGKGDR</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
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
      <td>16</td>
      <td>17</td>
      <td>16</td>
      <td>17</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>26</td>
      <td>18</td>
      <td>26</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>27</td>
      <td>33</td>
      <td>27</td>
      <td>33</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>34</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>54</td>
      <td>51</td>
      <td>54</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>69</td>
      <td>55</td>
      <td>69</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>91</td>
      <td>70</td>
      <td>91</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>106</td>
      <td>92</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>117</td>
      <td>107</td>
      <td>117</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>133</td>
      <td>118</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>148</td>
      <td>134</td>
      <td>148</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>152</td>
      <td>152</td>
      <td>152</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>165</td>
      <td>153</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>166</td>
      <td>176</td>
      <td>166</td>
      <td>176</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>194</td>
      <td>177</td>
      <td>194</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>195</td>
      <td>209</td>
      <td>195</td>
      <td>209</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6h5a">6H5A</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSK</span><span class="topo-inside">LPFLSRAAFARI</span><span class="topo-unknown">TTPIARGLLR</span><span class="topo-inside">VGLTPDV</span><span class="topo-membrane">VTILGTTASVAGALTLFP</span><span class="topo-outside">MGKL</span><span class="topo-membrane">FAGACVVWFFVLFDM</span><span class="topo-inside">LDGAMARERGGGTRFGAVLDAT</span><span class="topo-membrane">CDRISDGAVFCGLLW</span><span class="topo-outside">WIAFHMRDRP</span><span class="topo-membrane">LVIA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220   </span>
<span class="topo-line"><span class="topo-membrane">TLICLVTSQVISY</span><span class="topo-inside">IKARAEASGLRGDGG</span><span class="topo-membrane">FIERPERLIIVLTGAGV</span><span class="topo-outside">SDFPFVPWPPA</span><span class="topo-membrane">LSVGMWLLAVASVITCVQ</span><span class="topo-inside">RLHTVWTSPGAIDRMA</span><span class="topo-unknown">IPGKGDRENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>15</td>
      <td>4</td>
      <td>15</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>25</td>
      <td>16</td>
      <td>25</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>26</td>
      <td>32</td>
      <td>26</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>50</td>
      <td>33</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>54</td>
      <td>51</td>
      <td>54</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>69</td>
      <td>55</td>
      <td>69</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>91</td>
      <td>70</td>
      <td>91</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>106</td>
      <td>92</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>116</td>
      <td>107</td>
      <td>116</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>133</td>
      <td>117</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>148</td>
      <td>134</td>
      <td>148</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>165</td>
      <td>149</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>166</td>
      <td>176</td>
      <td>166</td>
      <td>176</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>194</td>
      <td>177</td>
      <td>194</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>195</td>
      <td>210</td>
      <td>195</td>
      <td>210</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6h5a">6H5A</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSKLPFLSRAAFAR</span><span class="topo-inside">I</span><span class="topo-unknown">TTPIARGLLRV</span><span class="topo-inside">GLTPDV</span><span class="topo-membrane">VTILGTTASVAGALTLFP</span><span class="topo-outside">MGK</span><span class="topo-membrane">LFAGACVVWFFVLFD</span><span class="topo-inside">MLDGAMARERGGGTRFGAVLDAT</span><span class="topo-membrane">CDRISDGAVFCGLLW</span><span class="topo-outside">WIAFHMRDRP</span><span class="topo-membrane">LVIA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220   </span>
<span class="topo-line"><span class="topo-membrane">TLICLVTSQVISY</span><span class="topo-inside">IKARAEASGLRGDGG</span><span class="topo-membrane">FIERPERLIIVLTGAGVS</span><span class="topo-outside">DFPFVPWPPA</span><span class="topo-membrane">LSVGMWLLAVASVITCVQ</span><span class="topo-inside">RLHTVWTSPGAIDRMAIPGKGDRENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>15</td>
      <td>15</td>
      <td>15</td>
      <td>15</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>26</td>
      <td>16</td>
      <td>26</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>27</td>
      <td>32</td>
      <td>27</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>50</td>
      <td>33</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>53</td>
      <td>51</td>
      <td>53</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>68</td>
      <td>54</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>91</td>
      <td>69</td>
      <td>91</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>106</td>
      <td>92</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>116</td>
      <td>107</td>
      <td>116</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>133</td>
      <td>117</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>148</td>
      <td>134</td>
      <td>148</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>166</td>
      <td>149</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>176</td>
      <td>167</td>
      <td>176</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>194</td>
      <td>177</td>
      <td>194</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>195</td>
      <td>223</td>
      <td>195</td>
      <td>223</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6h59">6H59</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSKLPFLSRAAF</span><span class="topo-outside">ARI</span><span class="topo-unknown">TTPIARGLLRV</span><span class="topo-outside">GLTPDV</span><span class="topo-membrane">VTILGTTASVAGALTLF</span><span class="topo-inside">PMGKL</span><span class="topo-membrane">FAGACVVWFFVLFD</span><span class="topo-outside">MLDGAMARERGGGTRFGAVLDAT</span><span class="topo-membrane">CDRISDGAVFCGLLW</span><span class="topo-inside">WIAFHMRDRP</span><span class="topo-membrane">LVIA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       </span>
<span class="topo-line"><span class="topo-membrane">TLICLVTSQVISY</span><span class="topo-outside">IKARAEASGLRGDGGF</span><span class="topo-membrane">IERPERLIIVLTGAGVSDF</span><span class="topo-inside">PFVPWPPA</span><span class="topo-membrane">LSVGMWLLAVASVITCV</span><span class="topo-outside">QRLHTVWTSPGAIDRMAI</span><span class="topo-unknown">PGKGDR</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>13</td>
      <td>15</td>
      <td>13</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>26</td>
      <td>16</td>
      <td>26</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>27</td>
      <td>32</td>
      <td>27</td>
      <td>32</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>49</td>
      <td>33</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>54</td>
      <td>50</td>
      <td>54</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>68</td>
      <td>55</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>91</td>
      <td>69</td>
      <td>91</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>106</td>
      <td>92</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>116</td>
      <td>107</td>
      <td>116</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>133</td>
      <td>117</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>149</td>
      <td>134</td>
      <td>149</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>150</td>
      <td>168</td>
      <td>150</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>176</td>
      <td>169</td>
      <td>176</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>193</td>
      <td>177</td>
      <td>193</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>194</td>
      <td>211</td>
      <td>194</td>
      <td>211</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6h59">6H59</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSKLPFLSRAAFAR</span><span class="topo-outside">I</span><span class="topo-unknown">TTPIARGLLR</span><span class="topo-outside">VGLTPDVV</span><span class="topo-membrane">TILGTTASVAGALTLFP</span><span class="topo-inside">MGKL</span><span class="topo-membrane">FAGACVVWFFVLFD</span><span class="topo-outside">MLDGAMARERGGGTRFGAVLDAT</span><span class="topo-membrane">CDRISDGAVFCGLLW</span><span class="topo-inside">WIAFHMRDRPLV</span><span class="topo-membrane">IA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       </span>
<span class="topo-line"><span class="topo-membrane">TLICLVTSQVISY</span><span class="topo-outside">IKARAEASGLRGDGG</span><span class="topo-membrane">FIERPERLIIVLTGAGV</span><span class="topo-inside">SDFPFVPWPPA</span><span class="topo-membrane">LSVGMWLLAVASVITCVQ</span><span class="topo-outside">RLHTVWTSPGAIDRMA</span><span class="topo-unknown">IPGKGDR</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>15</td>
      <td>15</td>
      <td>15</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>25</td>
      <td>16</td>
      <td>25</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>26</td>
      <td>33</td>
      <td>26</td>
      <td>33</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>34</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>54</td>
      <td>51</td>
      <td>54</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>68</td>
      <td>55</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>91</td>
      <td>69</td>
      <td>91</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>106</td>
      <td>92</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>118</td>
      <td>107</td>
      <td>118</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>133</td>
      <td>119</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>148</td>
      <td>134</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>165</td>
      <td>149</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>166</td>
      <td>176</td>
      <td>166</td>
      <td>176</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>194</td>
      <td>177</td>
      <td>194</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>195</td>
      <td>210</td>
      <td>195</td>
      <td>210</td>
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

### Drug target for tuberculosis



### Tight and relaxed states of metal site



### Inositol phosphate binding site



### Ordered substrate binding mechanism




## Cross-References

- <a href="/xray-mp-wiki/proteins/enzymes/sa-pgsa/">Phosphatidylglycerol Phosphate Synthase PgsA from Staphylococcus aureus</a> — Homologous CDP-AP family enzyme; structural and mechanistic comparison
- <a href="/xray-mp-wiki/concepts/protein-families/cdp-alcohol-phosphotransferase-family/">CDP-Alcohol Phosphotransferase Family</a> — PgsA1 belongs to the Class I CDP-alcohol phosphotransferase family
- <a href="/xray-mp-wiki/reagents/lipids/cytidine-diphosphate-diacylglycerol/">Cytidine Diphosphate Diacylglycerol (CDP-DAG)</a> — One of two substrates; CDP-DAG binding mechanism revealed in this study
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase</a> — Crystallization method used for substrate-bound PgsA1 structures
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Phasing method used to solve all three structures
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/carboxylate-shift/">Carboxylate Shift</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-docking/">Molecular Docking</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> — Buffer component in purification or crystallization
- <a href="/xray-mp-wiki/reagents/ligands/d-myo-inositol-3-phosphate/">D-myo-Inositol-3-Phosphate</a> — Related ligand or cofactor
