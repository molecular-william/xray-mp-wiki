---
title: "MlotiK1 (Mesorhizobium loti Cyclic Nucleotide-Regulated Potassium Channel)"
created: 2026-06-17
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.0711533105]
verified: agent
uniprot_id: Q98GN8
---

# MlotiK1 (Mesorhizobium loti Cyclic Nucleotide-Regulated Potassium Channel)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q98GN8">UniProt: Q98GN8</a>

<span class="expr-badge">Mesorhizobium loti</span>

## Overview

MlotiK1 is a bacterial cyclic nucleotide-regulated potassium channel from Mesorhizobium loti, a member of the six-transmembrane helix (6 TM) tetrameric cation channel superfamily. It is a non-voltage-gated 6 TM channel, meaning its S1-S4 domain does not function as a voltage sensor. The crystal structure of MlotiK1 (Clayton et al., PNAS 2008, 3.1 A resolution, space group R3) was determined in the presence of 200 uM cAMP, with the C-terminal cyclic nucleotide-binding (CNB) domains disordered and not resolved. This was the first structure of a non-voltage-gated 6 TM channel, revealing how the S1-S4 domain and its associated S4-S5 linker serve as a clamp constraining the gate of the pore. The structure revealed a compact S1-S4 domain with a 3_10 helical conformation in S4 that buries positively charged residues within the protein core, distinct from the voltage-sensor paddle architecture of voltage-gated channels. A prominent feature is that Phe-203 side chains fill the central cavity, suggesting a cavity-based gating mechanism closer to the selectivity filter than the canonical helix bundle crossing gate. Mutagenesis (F203A, Y215A) increased rubidium uptake rates approximately 6-fold, supporting a gating role for these residues.

## Publications

### doi/10.1073##pnas.0711533105

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3beh">3BEH</a></td>
      <td>3.1</td>
      <td>R3</td>
      <td>MlotiK1 channel from Mesorhizobium loti, full-length transmembrane regions (CNB domains disordered)</td>
      <td>200 uM cAMP (present during crystallization; K+ in pore)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length MlotiK1 from Mesorhizobium loti, expressed and purified as described in Nimigean et al. (2004) and Nimigean & Pagel (2007)

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
      <td>Protein expression</td>
      <td>Expression in E. coli</td>
      <td></td>
      <td></td>
      <td>Protein expressed and purified according to variations of protocols described in Nimigean et al. (2004) and Nimigean & Pagel (2007)</td>
    </tr>
    <tr>
      <td>Purification</td>
      <td>Size-exclusion chromatography</td>
      <td></td>
      <td>150 mM KCl</td>
      <td>Purified protein in buffer with 150 mM KCl</td>
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
      <td>MlotiK1 at 10 mg/ml in 200 uM cAMP, 5 mM lauryl dimethylamide oxide (<a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a>), 150 mM KCl</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>10% <a href="/xray-mp-wiki/reagents/additives/peg2000/">PEG 2000</a>, 100 mM trisodium <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> pH 5.6</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in the presence of substoichiometric amounts of cAMP (200 uM). KCl replaced by RbCl or CsCl by size exclusion for heavy-atom derivatives. Best diffracting crystals grew with 200 uM cAMP present. C-terminal CNB domains disordered. Data collected from native, RbCl co-crystal, and CsCl co-crystal forms.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>vapor-diffusion</td>
    </tr>
    <tr>
      <td>Variant</td>
      <td>sitting-drop</td>
    </tr>
    <tr>
      <td>pH</td>
      <td>5.6</td>
    </tr>
    <tr>
      <td>Components</td>
      <td>- Peg: 10 % [precipitant] (PEG 2000)</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3beh">3BEH</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSVLPF</span><span class="topo-outside">LRIYAPLNA</span><span class="topo-membrane">VLAAPGLLAVAALT</span><span class="topo-inside">IPDMSGRS</span><span class="topo-membrane">RLALAALLAVIWGAYL</span><span class="topo-outside">LQLAATLLKRRAGVVRDRTPKIAIDVL</span><span class="topo-membrane">AVLVPLAAFLLDG</span><span class="topo-inside">SP</span><span class="topo-membrane">DWSLYCAVWLLKP</span><span class="topo-outside">LRDSTFFPVLGR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">VLANEARNLIGVT</span><span class="topo-membrane">TLFGVVLFAVALAAYVI</span><span class="topo-inside">ERDIQPEKFGSI</span><span class="topo-unknown">PQAMWWAVVTLSTTGY</span><span class="topo-inside">GDTIPQSF</span><span class="topo-membrane">AGRVLAGAVMMSGIGIF</span><span class="topo-outside">GLWAGILATGFYQEVRRGDFVRNWQ</span><span class="topo-unknown">LVAAVPLFQKLG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350     </span>
<span class="topo-line"><span class="topo-unknown">PAVLVEIVRALRARTVPAGAVICRIGEPGDRMFFVVEGSVSVATPNPVELGPGAFFGEMALISGEPRSATVSAATTVSLLSLHSADFQMLCSSSPEIAEIFRKTALERRGAAASA</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>6</td>
      <td>1</td>
      <td>6</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>7</td>
      <td>15</td>
      <td>7</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>29</td>
      <td>16</td>
      <td>29</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>37</td>
      <td>30</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>53</td>
      <td>38</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>80</td>
      <td>54</td>
      <td>80</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>93</td>
      <td>81</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>95</td>
      <td>94</td>
      <td>95</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>108</td>
      <td>96</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>133</td>
      <td>109</td>
      <td>133</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>150</td>
      <td>134</td>
      <td>150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>151</td>
      <td>162</td>
      <td>151</td>
      <td>162</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>163</td>
      <td>178</td>
      <td>163</td>
      <td>178</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>179</td>
      <td>186</td>
      <td>179</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>187</td>
      <td>203</td>
      <td>187</td>
      <td>203</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>204</td>
      <td>228</td>
      <td>204</td>
      <td>228</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>355</td>
      <td>229</td>
      <td>355</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3beh">3BEH</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSVLPFLR</span><span class="topo-outside">IYAPLN</span><span class="topo-membrane">AVLAAPGLLAVAALT</span><span class="topo-inside">IPDMSGRSRL</span><span class="topo-membrane">ALAALLAVIWGAYLL</span><span class="topo-outside">QLAATLLKRRAGVVRDRTPKIAIDV</span><span class="topo-membrane">LAVLVPLAAFLLD</span><span class="topo-inside">GSPD</span><span class="topo-membrane">WSLYCAVWLLKP</span><span class="topo-outside">LRDSTFFPVLGR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">VLANEARNLIGVT</span><span class="topo-membrane">TLFGVVLFAVALAAYVI</span><span class="topo-inside">ERDIQPEKFGSI</span><span class="topo-unknown">PQAMWWAVVTLSTTGY</span><span class="topo-inside">GDTIPQSF</span><span class="topo-membrane">AGRVLAGAVMMSGIGIF</span><span class="topo-outside">GLWAGILATGFYQEVRRGDFVRNWQLV</span><span class="topo-unknown">AAVPLFQKLG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350     </span>
<span class="topo-line"><span class="topo-unknown">PAVLVEIVRALRARTVPAGAVICRIGEPGDRMFFVVEGSVSVATPNPVELGPGAFFGEMALISGEPRSATVSAATTVSLLSLHSADFQMLCSSSPEIAEIFRKTALERRGAAASA</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>14</td>
      <td>9</td>
      <td>14</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>29</td>
      <td>15</td>
      <td>29</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>39</td>
      <td>30</td>
      <td>39</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>54</td>
      <td>40</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>79</td>
      <td>55</td>
      <td>79</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>92</td>
      <td>80</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>96</td>
      <td>93</td>
      <td>96</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>108</td>
      <td>97</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>133</td>
      <td>109</td>
      <td>133</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>150</td>
      <td>134</td>
      <td>150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>151</td>
      <td>162</td>
      <td>151</td>
      <td>162</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>163</td>
      <td>178</td>
      <td>163</td>
      <td>178</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>179</td>
      <td>186</td>
      <td>179</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>187</td>
      <td>203</td>
      <td>187</td>
      <td>203</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>204</td>
      <td>230</td>
      <td>204</td>
      <td>230</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>355</td>
      <td>231</td>
      <td>355</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3beh">3BEH</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSVL</span><span class="topo-outside">PFLRIYAPLNA</span><span class="topo-membrane">VLAAPGLLAVAALT</span><span class="topo-inside">IPDMSGRSRL</span><span class="topo-membrane">ALAALLAVIWGAYLL</span><span class="topo-outside">QLAATLLKRRAGVVRDRTPKIAIDV</span><span class="topo-membrane">LAVLVPLAAFLLD</span><span class="topo-inside">GSPD</span><span class="topo-membrane">WSLYCAVWLLKP</span><span class="topo-outside">LRDSTFFPVLGR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">VLANEARNLIGVT</span><span class="topo-membrane">TLFGVVLFAVALAAYVI</span><span class="topo-inside">ERDIQPEKFGSI</span><span class="topo-unknown">PQAMWWAVVTLSTTGYG</span><span class="topo-inside">DTIPQSF</span><span class="topo-membrane">AGRVLAGAVMMSGIGIF</span><span class="topo-outside">GLWAGILATGFYQEVRRGDFVRNWQLV</span><span class="topo-unknown">AAVPLFQKLG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350     </span>
<span class="topo-line"><span class="topo-unknown">PAVLVEIVRALRARTVPAGAVICRIGEPGDRMFFVVEGSVSVATPNPVELGPGAFFGEMALISGEPRSATVSAATTVSLLSLHSADFQMLCSSSPEIAEIFRKTALERRGAAASA</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>15</td>
      <td>5</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>29</td>
      <td>16</td>
      <td>29</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>39</td>
      <td>30</td>
      <td>39</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>54</td>
      <td>40</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>79</td>
      <td>55</td>
      <td>79</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>92</td>
      <td>80</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>96</td>
      <td>93</td>
      <td>96</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>108</td>
      <td>97</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>133</td>
      <td>109</td>
      <td>133</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>150</td>
      <td>134</td>
      <td>150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>151</td>
      <td>162</td>
      <td>151</td>
      <td>162</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>163</td>
      <td>179</td>
      <td>163</td>
      <td>179</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>180</td>
      <td>186</td>
      <td>180</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>187</td>
      <td>203</td>
      <td>187</td>
      <td>203</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>204</td>
      <td>230</td>
      <td>204</td>
      <td>230</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>355</td>
      <td>231</td>
      <td>355</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3beh">3BEH</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSVL</span><span class="topo-outside">PFLRIYAPLNA</span><span class="topo-membrane">VLAAPGLLAVAALT</span><span class="topo-inside">IPDMSGRSRL</span><span class="topo-membrane">ALAALLAVIWGAYLL</span><span class="topo-outside">QLAATLLKRRAGVVRDRTPKIAID</span><span class="topo-membrane">VLAVLVPLAAFLLD</span><span class="topo-inside">GSPD</span><span class="topo-membrane">WSLYCAVWLLKP</span><span class="topo-outside">LRDSTFFPVLGR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">VLANEARNLIGVT</span><span class="topo-membrane">TLFGVVLFAVALAAYVI</span><span class="topo-inside">ERDIQPEKFGSI</span><span class="topo-unknown">PQAMWWAVVTLSTTGYG</span><span class="topo-inside">DTIPQSF</span><span class="topo-membrane">AGRVLAGAVMMSGIGIF</span><span class="topo-outside">GLWAGILATGFYQEVRRGDFVRNWQL</span><span class="topo-unknown">VAAVPLFQKLG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350     </span>
<span class="topo-line"><span class="topo-unknown">PAVLVEIVRALRARTVPAGAVICRIGEPGDRMFFVVEGSVSVATPNPVELGPGAFFGEMALISGEPRSATVSAATTVSLLSLHSADFQMLCSSSPEIAEIFRKTALERRGAAASA</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>15</td>
      <td>5</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>29</td>
      <td>16</td>
      <td>29</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>39</td>
      <td>30</td>
      <td>39</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>54</td>
      <td>40</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>78</td>
      <td>55</td>
      <td>78</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>92</td>
      <td>79</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>96</td>
      <td>93</td>
      <td>96</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>108</td>
      <td>97</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>133</td>
      <td>109</td>
      <td>133</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>150</td>
      <td>134</td>
      <td>150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>151</td>
      <td>162</td>
      <td>151</td>
      <td>162</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>163</td>
      <td>179</td>
      <td>163</td>
      <td>179</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>180</td>
      <td>186</td>
      <td>180</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>187</td>
      <td>203</td>
      <td>187</td>
      <td>203</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>204</td>
      <td>229</td>
      <td>204</td>
      <td>229</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>230</td>
      <td>355</td>
      <td>230</td>
      <td>355</td>
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

### First structure of a non-voltage-gated 6 TM channel

MlotiK1 is the first reported structure of a non-voltage-gated 6 TM tetrameric cation channel. The structure defines the transmembrane regions (pore and S1-S4 domains) at 3.1 A resolution, revealing overall architecture similar to voltage-gated channels but with key differences in the S1-S4 domain. The CNB domains are not resolved in the structure.

### S1-S4 domain as a structural clamp on the pore gate

In MlotiK1, the S1-S4 domain and its S4-S5 linker form a cuff around the C-terminal ends of the S6 inner helices, constraining the gate in a closed conformation. Superposition with the open Kv1.2 channel shows the Kv1.2 S6 helices would clash with the MlotiK1 S4-S5 linkers. To open to the same extent as Kv1.2, the S4-S5 linkers would need to shift outward (~5 A) and upward (~5 A). This structural arrangement provides a mechanism by which the S1-S4 domain serves as a clamp to regulate pore opening.

### Compact S1-S4 domain distinct from voltage sensors

The MlotiK1 S1-S4 domain forms a compact arrangement of four transmembrane helices with interdigitated side chains forming a solid protein core. This contrasts with the voltage sensor of Kv1.2 where the S3b-S4 paddle motif is tilted away from S1 and S2, creating a water-accessible crevice. The MlotiK1 S1-S4 domain also interacts more extensively with the pore (~1200 A2 buried surface area) than in Kv1.2, and the entire domain is rotated relative to Kv1.2, paralleling the closed conformation of the gate.

### 3_10 helix in S4 buries positively charged residues

The S4 helix in MlotiK1 adopts a 3_10 helical conformation over a segment, which is more tightly wound than an alpha-helix (i to i+3 hydrogen bonding instead of i to i+4). This conformation causes every third residue to fall on the same helical face, burying positively charged residues (equivalent to R2, R3, R4, K5, R6 in Kv channels) within the core of the S1-S4 domain, shielded from the lipid environment. This is distinct from Kv1.2 where these residues are exposed to lipid. A reversible transition between 3_10 and alpha-helix could provide the structural basis for S4 rotational movements upon stimulation.

### Cavity gating by Phe-203 in the central cavity

A prominent feature of the MlotiK1 pore is that the side chains of Phe-203 fill the central cavity, which is a water-filled cavity in other potassium channels like [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/). This occludes the ion conduction pathway at a position closer to the selectivity filter than the canonical helix bundle crossing gate. The F203A mutation increased rubidium uptake rate ~6-fold (time constant 17 min vs 94 min for wild-type), and Y215A also accelerated uptake (25 min). This suggests a novel gating mechanism where the cavity can be occluded by hydrophobic side chains, representing a gate that could operate independently of the bundle crossing gate.

### S4-S5 linker in a closed 6 TM channel

The MlotiK1 structure provides the first opportunity to inspect the S4-S5 linker in the context of a closed 6 TM channel. In voltage-gated channels, the S4-S5 linker interacts with the S6 gate region during gating. In MlotiK1 (closed), the linkers form a cuff around the gate regions, restricting S6 movement. Superposition with open Kv1.2 reveals that the Kv1.2 linker is shifted outward (~5 A) and upward (~5 A) relative to MlotiK1, consistent with the role of the linker as a gating element.

### Absence of voltage-sensing machinery

MlotiK1 lacks the conserved negatively charged residues in S2 and S3 (E283 and E293 in Shaker) that are essential for voltage sensing in voltage-gated potassium channels. The compact S1-S4 domain architecture, absence of a water-accessible crevice, and burial of positively charged S4 residues within the protein core indicate MlotiK1 does not function as a voltage sensor. The S1-S4 domain instead serves a structural role as a clamp regulating the pore gate in concert with the C-terminal CNB domain.


## Cross-References

- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/">KcsA Potassium Channel</a> — KcsA was used as the molecular replacement search model for MlotiK1 structure determination; both are tetrameric potassium channels with conserved pore architecture
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/s4-s5-linker-interaction-motif/">S4-S5 Linker Interaction Motif</a> — The MlotiK1 structure reveals the S4-S5 linker conformation in a closed 6 TM channel, providing a structural template for understanding linker function in both voltage-gated and non-voltage-gated channels
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/channel-gating/">Channel Gating</a> — MlotiK1 reveals a novel cavity gating mechanism where Phe-203 side chains occlude the central cavity, representing a gate closer to the selectivity filter than the helix bundle crossing
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/peg2000/">PEG 2000</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> — Buffer component used in purification or crystallization
- <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a> — Detergent used in purification or crystallization
