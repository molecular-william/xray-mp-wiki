---
title: "O. sativa SWEET2b (OsSWEET2b)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature15391]
verified: regex
uniprot_id: Q5N8J1
---

# O. sativa SWEET2b (OsSWEET2b)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span> <span class="expr-badge expr-p-pastoris">P. pastoris</span> <span class="expr-badge expr-native-tissue">Native tissue</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q5N8J1">UniProt: Q5N8J1</a>

<span class="expr-badge">Oryza sativa subsp. japonica</span>

## Overview

OsSWEET2b is a vacuolar glucose transporter from the SWEET family found in rice (Oryza sativa). It is a seven-transmembrane-helix protein composed of two triple-helix bundles (THBs) connected by an inversion linker helix (TM4), forming an asymmetrical transport pathway in an inward-open conformation. OsSWEET2b assembles as a homo-trimer in the membrane, with each protomer containing its own transport route. The structure reveals a conserved proline tetrad that functions as hinges for gating and an asymmetrical substrate-binding pocket that diverges from the symmetrical architecture of ancestral bacterial SemiSWEETs.


## Publications

### doi/10.1038##nature15391

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5ctg">5CTG</a></td>
      <td>3.1</td>
      <td>P2_1</td>
      <td>OsSWEET2b(deltaC15)-3C-EGFP-His; reductive methylation</td>
      <td>--</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5cth">5CTH</a></td>
      <td>3.7</td>
      <td>P2_1_2_1</td>
      <td>OsSWEET2b(deltaC15)-3C-EGFP-His; reductive methylation</td>
      <td>--</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris (native); sf9 insect cells (SeMet)
- **Construct**: OsSWEET2b(deltaC15)-3C-EGFP-His; C-terminal 15 disordered residues removed
- **Induction**: OD600 10 at 27 C for native; 48 h at 27 C for sf9

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
      <td>Cell lysis and membrane extraction</td>
      <td>Detergent extraction</td>
      <td>--</td>
      <td>3% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> with protease inhibitor cocktail</td>
      <td>4 C for 2 h</td>
    </tr>
    <tr>
      <td>Centrifugation</td>
      <td>Centrifugation</td>
      <td>--</td>
      <td>--</td>
      <td>16,000 rpm for 45 min to remove insoluble</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography">IMAC</a></td>
      <td><a href="/xray-mp-wiki/reagents/affinity-resins/cobalt-resin">Cobalt</a> resin</td>
      <td>0.3% <a href="/xray-mp-wiki/reagents/detergents/dm">DM (n-decyl-beta-D-maltoside)</a>, 20 mM imidazole</td>
      <td>4 C for 2 h; cleaved with 3C protease</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/gel-filtration">Gel Filtration</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200">Superdex 200</a></td>
      <td>10 mM Tris-HCl pH 8.0, 150 mM NaCl, 0.5% <a href="/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-maltopyranoside">NG (n-nonyl-beta-D-glucopyranoside)</a></td>
      <td>Protein concentrated to 10 mg/mL for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion">Hanging Drop</a> <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>OsSWEET2b(deltaC15) in 0.5% NG</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>30% PEG 400, 0.1 M MES pH 6.5, 10 mM MnCl2, 5% ethanol</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>22</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Form I (P2_1) plate-like crystals; directly flash-frozen without cryoprotectant</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion">Hanging Drop</a> <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>OsSWEET2b(deltaC15) in 0.5% NG</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>27% PEG 400, 0.1 M MES pH 6.0</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>22</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Form II (P2_1_2_1) cubic crystals; cryo-protected by gradual PEG400 concentration increase to 44%</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ctg">5CTG</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">DSLYDISCF</span><span class="topo-membrane">AAGLAGNIFALALFLSPV</span><span class="topo-inside">TTFKRILKAKSTERFDG</span><span class="topo-membrane">LPYLFSLLNCLICLWYGL</span><span class="topo-outside">PWVADGR</span><span class="topo-membrane">LLVATVNGIGAVFQLAYICLFI</span><span class="topo-inside">FYADSRKTRMK</span><span class="topo-membrane">IIGLLVLVVCGFALVSH</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220    </span>
<span class="topo-line"><span class="topo-membrane">AS</span><span class="topo-outside">VFFFDQPLRQQ</span><span class="topo-membrane">FVGAVSMASLISMFASPLAVM</span><span class="topo-inside">GVVIRSESVEFM</span><span class="topo-membrane">PFYLSLSTFLMSASFALYGL</span><span class="topo-outside">LLRD</span><span class="topo-membrane">FFIYFPNGLGLILGAMQLALYAY</span><span class="topo-inside">YS</span><span class="topo-unknown">SNSLEVLFQ</span></span>
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
      <td>2</td>
      <td>10</td>
      <td>2</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>28</td>
      <td>11</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>45</td>
      <td>29</td>
      <td>45</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>63</td>
      <td>46</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>70</td>
      <td>64</td>
      <td>70</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>92</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>103</td>
      <td>93</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>122</td>
      <td>104</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>133</td>
      <td>123</td>
      <td>133</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>134</td>
      <td>154</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>166</td>
      <td>155</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>186</td>
      <td>167</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>190</td>
      <td>187</td>
      <td>190</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>213</td>
      <td>191</td>
      <td>213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>214</td>
      <td>215</td>
      <td>214</td>
      <td>215</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ctg">5CTG</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">DSLYDISCF</span><span class="topo-membrane">AAGLAGNIFALALFLSPV</span><span class="topo-inside">TTFKRILKAKSTERFDG</span><span class="topo-membrane">LPYLFSLLNCLICLWYGL</span><span class="topo-outside">PWVADGR</span><span class="topo-membrane">LLVATVNGIGAVFQLAYICLFI</span><span class="topo-inside">FYADSRKTRM</span><span class="topo-membrane">KIIGLLVLVVCGFALVSH</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220    </span>
<span class="topo-line"><span class="topo-membrane">AS</span><span class="topo-outside">VFFFDQPLRQQ</span><span class="topo-membrane">FVGAVSMASLISMFASPLAVM</span><span class="topo-inside">GVVIRSESVEFM</span><span class="topo-membrane">PFYLSLSTFLMSASFALYGL</span><span class="topo-outside">LLRD</span><span class="topo-membrane">FFIYFPNGLGLILGAMQLALYAY</span><span class="topo-inside">YSSNSLEV</span><span class="topo-unknown">LFQ</span></span>
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
      <td>2</td>
      <td>10</td>
      <td>2</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>28</td>
      <td>11</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>45</td>
      <td>29</td>
      <td>45</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>63</td>
      <td>46</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>70</td>
      <td>64</td>
      <td>70</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>92</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>102</td>
      <td>93</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>122</td>
      <td>103</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>133</td>
      <td>123</td>
      <td>133</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>134</td>
      <td>154</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>166</td>
      <td>155</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>186</td>
      <td>167</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>190</td>
      <td>187</td>
      <td>190</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>213</td>
      <td>191</td>
      <td>213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>214</td>
      <td>221</td>
      <td>214</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ctg">5CTG</a> — Chain C (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MD</span><span class="topo-outside">SLYDISCF</span><span class="topo-membrane">AAGLAGNIFALALFLSPV</span><span class="topo-inside">TTFKRILKAKSTERFDG</span><span class="topo-membrane">LPYLFSLLNCLICLWYGL</span><span class="topo-outside">PWVADGR</span><span class="topo-membrane">LLVATVNGIGAVFQLAYICLFI</span><span class="topo-inside">FYADSRKTRMK</span><span class="topo-membrane">IIGLLVLVVCGFALVSH</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220    </span>
<span class="topo-line"><span class="topo-membrane">AS</span><span class="topo-outside">VFFFDQPLRQQ</span><span class="topo-membrane">FVGAVSMASLISMFASPLAVM</span><span class="topo-inside">GVVIRSESVEFM</span><span class="topo-membrane">PFYLSLSTFLMSASFALYGL</span><span class="topo-outside">LLRD</span><span class="topo-membrane">FFIYFPNGLGLILGAMQLALYAY</span><span class="topo-inside">YSSN</span><span class="topo-unknown">SLEVLFQ</span></span>
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
      <td>3</td>
      <td>10</td>
      <td>3</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>28</td>
      <td>11</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>45</td>
      <td>29</td>
      <td>45</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>63</td>
      <td>46</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>70</td>
      <td>64</td>
      <td>70</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>92</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>103</td>
      <td>93</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>122</td>
      <td>104</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>133</td>
      <td>123</td>
      <td>133</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>134</td>
      <td>154</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>166</td>
      <td>155</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>186</td>
      <td>167</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>190</td>
      <td>187</td>
      <td>190</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>213</td>
      <td>191</td>
      <td>213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>214</td>
      <td>217</td>
      <td>214</td>
      <td>217</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5cth">5CTH</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">DSLYDISCF</span><span class="topo-membrane">AAGLAGNIFALALFLSPV</span><span class="topo-inside">TTFKRILKAKSTERFDGL</span><span class="topo-membrane">PYLFSLLNCLICLWYGL</span><span class="topo-outside">PWVADGR</span><span class="topo-membrane">LLVATVNGIGAVFQLAYICL</span><span class="topo-inside">FIFYADSRKTRMKI</span><span class="topo-membrane">IGLLVLVVCGFALVSH</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220    </span>
<span class="topo-line"><span class="topo-membrane">AS</span><span class="topo-outside">VFFFDQPLRQQ</span><span class="topo-membrane">FVGAVSMASLISMFASPLA</span><span class="topo-inside">VMGVVIRSESVEFM</span><span class="topo-membrane">PFYLSLSTFLMSASFALYGL</span><span class="topo-outside">LLRD</span><span class="topo-membrane">FFIYFPNGLGLILGAMQLALYA</span><span class="topo-inside">Y</span><span class="topo-unknown">YSSNSLEVLFQ</span></span>
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
      <td>2</td>
      <td>10</td>
      <td>2</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>28</td>
      <td>11</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>46</td>
      <td>29</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>63</td>
      <td>47</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>70</td>
      <td>64</td>
      <td>70</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>90</td>
      <td>71</td>
      <td>90</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>104</td>
      <td>91</td>
      <td>104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>122</td>
      <td>105</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>133</td>
      <td>123</td>
      <td>133</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>152</td>
      <td>134</td>
      <td>152</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>153</td>
      <td>166</td>
      <td>153</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>186</td>
      <td>167</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>190</td>
      <td>187</td>
      <td>190</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>213</td>
      <td>213</td>
      <td>213</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5cth">5CTH</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MD</span><span class="topo-outside">SLYDISCF</span><span class="topo-membrane">AAGLAGNIFALALFLSPV</span><span class="topo-inside">TTFKRILKAKSTERFDGL</span><span class="topo-membrane">PYLFSLLNCLICLWYGL</span><span class="topo-outside">PWVADGR</span><span class="topo-membrane">LLVATVNGIGAVFQLAYICL</span><span class="topo-inside">FIFYADSRKTRMKI</span><span class="topo-membrane">IGLLVLVVCGFALVSH</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220    </span>
<span class="topo-line"><span class="topo-membrane">AS</span><span class="topo-outside">VFFFDQPLRQQ</span><span class="topo-membrane">FVGAVSMASLISMFASPLA</span><span class="topo-inside">VMGVVIRSESVEFMP</span><span class="topo-membrane">FYLSLSTFLMSASFALYGL</span><span class="topo-outside">LLRD</span><span class="topo-membrane">FFIYFPNGLGLILGAMQLALYA</span><span class="topo-inside">YYSSN</span><span class="topo-unknown">SLEVLFQ</span></span>
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
      <td>3</td>
      <td>10</td>
      <td>3</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>28</td>
      <td>11</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>46</td>
      <td>29</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>63</td>
      <td>47</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>70</td>
      <td>64</td>
      <td>70</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>90</td>
      <td>71</td>
      <td>90</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>104</td>
      <td>91</td>
      <td>104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>122</td>
      <td>105</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>133</td>
      <td>123</td>
      <td>133</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>152</td>
      <td>134</td>
      <td>152</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>153</td>
      <td>167</td>
      <td>153</td>
      <td>167</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>186</td>
      <td>168</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>190</td>
      <td>187</td>
      <td>190</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>217</td>
      <td>213</td>
      <td>217</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5cth">5CTH</a> — Chain C (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDSL</span><span class="topo-outside">YDISCF</span><span class="topo-membrane">AAGLAGNIFALALFLSPV</span><span class="topo-inside">TTFKRILKAKSTERFDGL</span><span class="topo-membrane">PYLFSLLNCLICLWYGL</span><span class="topo-outside">PWVADGRL</span><span class="topo-membrane">LVATVNGIGAVFQLAYICL</span><span class="topo-inside">FIFYADSRKTRMKI</span><span class="topo-membrane">IGLLVLVVCGFALVSH</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220    </span>
<span class="topo-line"><span class="topo-membrane">AS</span><span class="topo-outside">VFFFDQPLRQQ</span><span class="topo-membrane">FVGAVSMASLISMFASPLA</span><span class="topo-inside">VMGVVIRSESVEFMPF</span><span class="topo-membrane">YLSLSTFLMSASFALYGL</span><span class="topo-outside">LLRD</span><span class="topo-membrane">FFIYFPNGLGLILGAMQLALYA</span><span class="topo-inside">YYSSN</span><span class="topo-unknown">SLEVLFQ</span></span>
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
      <td>5</td>
      <td>10</td>
      <td>5</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>28</td>
      <td>11</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>46</td>
      <td>29</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>63</td>
      <td>47</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>71</td>
      <td>64</td>
      <td>71</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>90</td>
      <td>72</td>
      <td>90</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>104</td>
      <td>91</td>
      <td>104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>122</td>
      <td>105</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>133</td>
      <td>123</td>
      <td>133</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>152</td>
      <td>134</td>
      <td>152</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>153</td>
      <td>168</td>
      <td>153</td>
      <td>168</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>169</td>
      <td>186</td>
      <td>169</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>190</td>
      <td>187</td>
      <td>190</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>217</td>
      <td>213</td>
      <td>217</td>
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

### Asymmetrical THB architecture

OsSWEET2b consists of two triple-helix bundles (THBs) connected by an inversion linker helix (TM4). Unlike symmetric bacterial SemiSWEET homodimers, the two THBs in eukaryotic SWEETs have diverged to create an asymmetrical binding pocket. THB1 (TM1-3) and THB2 (TM5-7) are structurally divergent, with THB1 bending to accommodate TM4. The TM4 inversion linker connects the two THBs in opposite orientation, enabling covalent fusion of the ancestral dimer into a single polypeptide chain.

### Homo-trimeric assembly

OsSWEET2b forms a homo-trimer with each protomer containing an independent transport pathway. The trimer interface involves TM4 of one protomer interacting with TM5 and TM7 of the neighboring protomer, burying ~1700 A2 between protomers. Trimer formation was confirmed by glutaraldehyde cross-linking, site-directed disulfide cross-linking in both detergent and membranes, and co-immunoprecipitation. The quaternary structure was observed in two distinct crystal forms.

### Proline tetrad gating mechanism

Four conserved proline residues (one in each of TM1, TM2, TM5, and TM6) line the transport pathway at the intrafacial (cytosolic) side. These prolines terminate or kink the respective helices and face the transport route at a similar membrane depth. Mutagenesis of all four prolines in AtSWEET1 (P23A, P43A, P145A, P162A) abolished transport activity, suggesting they function as molecular hinges enabling concerted structural rearrangements during the transport cycle.

### Extrafacial gate and asymmetrical binding pocket

The extrafacial (luminal) gate is formed by Tyr61, Asp190, Gln132, and Ile193 in OsSWEET2b. Tyr61 hydrogen-bonds with Asp190 and interacts with Gln132 to seal the cavity from the luminal side. In the binding pocket, two conserved asparagines (Asn77 and Asn197) are essential for transport, while only one aromatic residue (Phe181 in THB2, corresponding to Trp176 in AtSWEET1) is required — contrasting with the paired tryptophans in symmetric SemiSWEETs. This confirms the asymmetrical nature of the eukaryotic SWEET binding pocket.

### Dominant-negative gate mutations

Mutations in the extrafacial gate (V188A) and intrafacial gate (P23T) of AtSWEET1 cause dominant-negative inhibition of co-expressed wild-type transporter, indicating allosteric coupling between protomers in the trimer. This suggests that conformational states are coupled among SWEET protomers, similar to cooperative transport observed in GLUT1 tetramers and AMT transporters.


## Cross-References

- <a href="/xray-mp-wiki/proteins/miscellaneous/ec-semisweet/">E. coli SemiSWEET (EcSemiSWEET)</a> — Bacterial homolog with inward-open and outward-open structures; shares conserved binding pocket residues and PQ-loop hinge
- <a href="/xray-mp-wiki/proteins/miscellaneous/a-thaliana-sweet1/">A. thaliana SWEET1</a> — Closely related plant SWEET used for structure-function mutagenesis studies
- <a href="/xray-mp-wiki/proteins/miscellaneous/tysemisweet/">TySemiSWEET</a> — Bacterial SemiSWEET homolog with conserved structural features
- <a href="/xray-mp-wiki/proteins/miscellaneous/lbsemisweet/">LbSemiSWEET</a> — Bacterial SemiSWEET homolog with outward-open and occluded structures
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/sweet-transporter/">SWEET Transporter Family</a> — OsSWEET2b is a eukaryotic member of the SWEET family
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Primary detergent for membrane extraction
- <a href="/xray-mp-wiki/reagents/detergents/dm/">DM (n-decyl-beta-D-maltoside)</a> — Detergent used in wash buffer during purification
- <a href="/xray-mp-wiki/reagents/detergents/nm/">NG (n-nonyl-beta-D-glucopyranoside)</a> — Detergent used in gel filtration and crystallization
