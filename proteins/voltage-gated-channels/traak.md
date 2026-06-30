---
title: "Human TRAAK Potassium Channel"
created: 2026-05-28
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.neuron.2021.07.009, doi/10.1038##nature14013, doi/10.7554##eLife.50403, doi/10.1126##science.1213808, doi/10.1073##pnas.1218950110]
verified: false
---

# Human TRAAK Potassium Channel

## Overview

TRAAK (tandem pore domain potassium channel 4, KCNK4) is a mechanosensitive two-pore domain K+ (K2P) channel expressed in the nervous system. It is localized exclusively to nodes of Ranvier in myelinated axons throughout the mammalian central and peripheral nervous system, where it accounts for approximately 20-25% of nodal background K+ conductance, maintaining the resting membrane potential. Approximately 80% of myelinated nerve fibers contain TRAAK in an all-nodes or no-nodes per axon fashion. TRAAK displays basal leak K+ activity that can be activated ~100-fold by mechanical force. Gain-of-function mutations (A198E, A270P) cause the neurodevelopmental disorder FHEIG. The channel is twofold symmetric, formed from two polypeptide chains each encoding two nonidentical repeats corresponding to canonical K+ channel subunits.


## Publications

### doi/10.1016##j.neuron.2021.07.009

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7lj5">7LJ5</a></td>
      <td>2.3</td>
      <td>P21</td>
      <td>Human TRAAK with N-terminal extension, C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> (119 aa removed), His-tag, co-crystallized with mouse monoclonal Fab</td>
      <td>K+, Fab</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7lj6">7LJ6</a></td>
      <td>2.7</td>
      <td>P21</td>
      <td>Human TRAAK A198E mutant with N-terminal extension, C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a>, His-tag, co-crystallized with Fab</td>
      <td>K+, Fab</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7lj7">7LJ7</a></td>
      <td>2.9</td>
      <td>P21</td>
      <td>Human TRAAK A270P mutant with N-terminal extension, C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a>, His-tag, co-crystallized with Fab</td>
      <td>K+, Fab</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7lj8">7LJ8</a></td>
      <td>3.3</td>
      <td>P21</td>
      <td>Human TRAAK G158D mutant with N-terminal extension, C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a>, His-tag</td>
      <td>K+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris
- **Construct**: Human TRAAK (UniProt Q9NYG8-2) with additional 26 aa N-terminal extension, C-terminally truncated by 119 aa (residues 1-300 or similar), His-tag
- **Notes**: For 2014 Nature paper, construct was residues 1-290 with N104Q/N108Q and C-terminal PreScission-cleavable EGFP-10xHis fusion. Same construct used for 2021 Neuron paper and 2013 PNAS paper.

**Purification:**

- **Expression system**: Pichia pastoris
- **Expression construct**: Human TRAAK with N-terminal extension, C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/), His-tag

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
      <td>Pichia pastoris expression</td>
      <td>—</td>
      <td></td>
      <td>Human TRAAK expressed in Pichia pastoris cells</td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>Microfluidizer</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Membrane collection</td>
      <td>Centrifugation</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>1% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td></td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td>1% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>His-tag purification with <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> elution at 250 mM</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM Tris (pH 8.8), 150 mM NaCl + 0.03% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified TRAAK mutants in 0.03% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>, 20 mM Tris (pH 8.8), 150 mM NaCl, co-crystallized with mouse monoclonal antibody Fab fragment</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>50 mM Tris (pH 8.8), 64-200 mM CaCl2, 27-33% (vol/vol) <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>1-5 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Mother liquor supplemented to 30% (vol/vol) <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a>, crystals plunged into liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Lower calcium concentrations gave increased nucleation and rapid growth</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7lj5">7LJ5</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTTAPQEPPARPLQAGSGAGPAPGRAM</span><span class="topo-inside">RSTTLL</span><span class="topo-membrane">ALLALVLLYLVSGALVFRAL</span><span class="topo-outside">EQPHEQQAQRELGEVREKFLRAHPCVSDQELGLLIKEVADALGGGADPET</span><span class="topo-unknown">QSTSQS</span><span class="topo-outside">SHSAWDL</span><span class="topo-unknown">GSAF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">FFSGTIITTIGYG</span><span class="topo-outside">NVALRTD</span><span class="topo-membrane">AGRLFCIFYALVGIPLFGILLAGVG</span><span class="topo-unknown">DRLGSSLRHGIGHIEAIFL</span><span class="topo-inside">KWHVPPELVRVLSEM</span><span class="topo-membrane">LFLLIGCLLFVLTPTFVFC</span><span class="topo-outside">YMEDWSK</span><span class="topo-unknown">LEAIYFVIVTLTTVG</span></span>
<span class="topo-ruler">       250       260       270       280       290         </span>
<span class="topo-line"><span class="topo-unknown">FG</span><span class="topo-outside">DYVAGADPRQDS</span><span class="topo-membrane">PAYQPLVWFWILLGLAYFASVLTTIG</span><span class="topo-inside">NWLRVV</span><span class="topo-unknown">SRRTSNSLEVLFQ</span></span>
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
      <td>28</td>
      <td>33</td>
      <td>28</td>
      <td>33</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>53</td>
      <td>34</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>103</td>
      <td>54</td>
      <td>103</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>116</td>
      <td>110</td>
      <td>116</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>133</td>
      <td>117</td>
      <td>133</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>134</td>
      <td>140</td>
      <td>134</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>165</td>
      <td>141</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>166</td>
      <td>184</td>
      <td>166</td>
      <td>184</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>185</td>
      <td>199</td>
      <td>185</td>
      <td>199</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>218</td>
      <td>200</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>225</td>
      <td>219</td>
      <td>225</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>242</td>
      <td>226</td>
      <td>242</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>243</td>
      <td>254</td>
      <td>243</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>280</td>
      <td>255</td>
      <td>280</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>281</td>
      <td>286</td>
      <td>281</td>
      <td>286</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7lj5">7LJ5</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTTAPQEPPARPLQAGSGAGPAPGRAM</span><span class="topo-inside">RSTTL</span><span class="topo-membrane">LALLALVLLYLVSGALVF</span><span class="topo-outside">RALEQPHEQQAQRELGEVREKFLRAHPCVSDQELGLLIKEVADALGGGADPETQST</span><span class="topo-unknown">SQSSH</span><span class="topo-outside">SAWDL</span><span class="topo-unknown">GSAF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">FFSGTIITTIGYG</span><span class="topo-outside">NVALRTD</span><span class="topo-membrane">AGRLFCIFYALVGIPLFGILLA</span><span class="topo-unknown">GVGDRLGSSLRHGIGHIEAIFLK</span><span class="topo-inside">WHVPPELVRVLSEMLFL</span><span class="topo-membrane">LIGCLLFVLTPTFVFCYM</span><span class="topo-outside">EDWS</span><span class="topo-unknown">KLEAIYFVIVTLTTVG</span></span>
<span class="topo-ruler">       250       260       270       280       290         </span>
<span class="topo-line"><span class="topo-unknown">FG</span><span class="topo-outside">DYVAGADPRQDS</span><span class="topo-membrane">PAYQPLVWFWILLGLAYFASVLTTIG</span><span class="topo-unknown">NWLRVV</span><span class="topo-inside">S</span><span class="topo-unknown">RRTSNSLEVLFQ</span></span>
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
      <td>28</td>
      <td>32</td>
      <td>28</td>
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
      <td>106</td>
      <td>51</td>
      <td>106</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>116</td>
      <td>112</td>
      <td>116</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>133</td>
      <td>117</td>
      <td>133</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>134</td>
      <td>140</td>
      <td>134</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>162</td>
      <td>141</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>185</td>
      <td>163</td>
      <td>185</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>186</td>
      <td>202</td>
      <td>186</td>
      <td>202</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>220</td>
      <td>203</td>
      <td>220</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>224</td>
      <td>221</td>
      <td>224</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>225</td>
      <td>242</td>
      <td>225</td>
      <td>242</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>243</td>
      <td>254</td>
      <td>243</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>280</td>
      <td>255</td>
      <td>280</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>281</td>
      <td>286</td>
      <td>281</td>
      <td>286</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>287</td>
      <td>287</td>
      <td>287</td>
      <td>287</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##nature14013

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4wfe">4WFE</a></td>
      <td>2.5</td>
      <td>P21</td>
      <td>Human TRAAK residues 1-290, N104Q/N108Q, C-terminal PreScission-cleavable EGFP-10xHis tag, co-crystallized with mouse monoclonal 13E9 Fab</td>
      <td>K+, Fab (13E9)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4wfg">4WFG</a></td>
      <td>3.0</td>
      <td>P21</td>
      <td>Human TRAAK residues 1-290, N104Q/N108Q, C-terminal PreScission-cleavable EGFP-10xHis tag, co-crystallized with mouse monoclonal 13E9 Fab</td>
      <td>Tl+, Fab (13E9)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4wff">4WFF</a></td>
      <td>2.5</td>
      <td>P21</td>
      <td>Human TRAAK residues 1-290, N104Q/N108Q, C-terminal PreScission-cleavable EGFP-10xHis tag, co-crystallized with mouse monoclonal 13E9 Fab</td>
      <td>K+, Fab (13E9)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4wfh">4WFH</a></td>
      <td>3.0</td>
      <td>P21</td>
      <td>Human TRAAK residues 1-290, N104Q/N108Q, C-terminal PreScission-cleavable EGFP-10xHis tag, co-crystallized with mouse monoclonal 13E9 Fab</td>
      <td>Tl+, Fab (13E9)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris
- **Construct**: Human TRAAK (UniProt Q9NYG8-2) with additional 26 aa N-terminal extension, C-terminally truncated by 119 aa (residues 1-300 or similar), His-tag
- **Notes**: For 2014 Nature paper, construct was residues 1-290 with N104Q/N108Q and C-terminal PreScission-cleavable EGFP-10xHis fusion. Same construct used for 2021 Neuron paper and 2013 PNAS paper.

**Purification:**

- **Expression system**: Pichia pastoris
- **Expression construct**: TRAAK residues 1-290, N104Q/N108Q, C-terminal PreScission-cleavable EGFP-10xHis tag

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
      <td>Cell disruption</td>
      <td>Milling (Retsch MM301)</td>
      <td>—</td>
      <td>50 mM Tris pH 8.0, 150 mM KCl + 60 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>Frozen Pichia cells milled 5x3 min at 25 Hz, 1 g pellet per 4 ml lysis buffer with protease inhibitors (pepstatin, leupeptin, aprotinin, soy <a href="/xray-mp-wiki/reagents/additives/trypsin/">Trypsin</a> inhibitor, benzamidine, PMSF) and 0.1 mg/ml DNase I</td>
    </tr>
    <tr>
      <td>Membrane extraction</td>
      <td>Stirring extraction</td>
      <td>—</td>
      <td>50 mM Tris pH 8.0, 150 mM KCl + 6 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>Extraction for 3 h stirring at 4 C, followed by centrifugation at 35,000g for 45 min</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Cobalt affinity</td>
      <td>Cobalt resin (Clontech)</td>
      <td>50 mM Tris pH 8.0, 150 mM KCl + 6 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>1 ml resin per 5 g cell pellet, 3 h stirring. Washes in 10 mM, 30 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>; elution in 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> pH 8.0</td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td><a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a> cleavage</td>
      <td>—</td>
      <td>50 mM Tris pH 8.0, 150 mM KCl, 1 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> + 6 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a> at ~1:50 (wt:wt), incubated with gentle rocking overnight at 4 C</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> (GE Healthcare)</td>
      <td>20 mM Tris pH 8.0, 150 mM KCl, 1 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> + 4 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>Concentrated 50 kDa MWCO before <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
    </tr>
    <tr>
      <td>Fab complex formation</td>
      <td>Complex formation</td>
      <td>—</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a> buffer (20 mM Tris pH 8.0, 150 mM KCl, 1 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>) + 4 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>Purified TRAAK (~10 mg/ml) incubated with purified 13E9 Fab (~30 mg/ml) at 1:2.5 molar ratio for 10 min at 4 C; complex separated from excess Fab on <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified TRAAK-Fab complex concentrated to 30 mg/ml in <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a> buffer (20 mM Tris pH 8.0, 150 mM KCl, 1 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, 4 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>) for K+ conditions; 150 mM TlNO3 replaced KCl for Tl+ conditions</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Drops of 0.25-0.35 ul protein added to equal volume of reservoir</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4wfe">4WFE</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTTAPQEPPARPLQAGSGAGPAPGRAM</span><span class="topo-inside">RSTTLL</span><span class="topo-membrane">ALLALVLLYLVSGALVFRAL</span><span class="topo-outside">EQPHEQQAQRELGEVREKFLRAHPCVSDQELGLLIKEVADALGGGADPET</span><span class="topo-unknown">QSTSQS</span><span class="topo-outside">SHSAWDL</span><span class="topo-unknown">GSAF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">FFSGTIITTIGYG</span><span class="topo-outside">NVALRTD</span><span class="topo-membrane">AGRLFCIFYALVGIPLFGILLAGVG</span><span class="topo-unknown">DRLGSSLRHGIGHIEAIFLK</span><span class="topo-inside">WHVPPELVRVLSAM</span><span class="topo-membrane">LFLLIGCLLFVLTPTFVFCY</span><span class="topo-outside">MEDWSK</span><span class="topo-unknown">LEAIYFVIVTLTTVG</span></span>
<span class="topo-ruler">       250       260       270       280       290         </span>
<span class="topo-line"><span class="topo-unknown">FG</span><span class="topo-outside">DYVAGADPRQDS</span><span class="topo-membrane">PAYQPLVWFWILLGLAYFASVLT</span><span class="topo-inside">TIGNWLRVV</span><span class="topo-unknown">SRRTSNSLEVLFQ</span></span>
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
      <td>28</td>
      <td>33</td>
      <td>28</td>
      <td>33</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>53</td>
      <td>34</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>103</td>
      <td>54</td>
      <td>103</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>116</td>
      <td>110</td>
      <td>116</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>133</td>
      <td>117</td>
      <td>133</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>134</td>
      <td>140</td>
      <td>134</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>165</td>
      <td>141</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>166</td>
      <td>185</td>
      <td>166</td>
      <td>185</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>186</td>
      <td>199</td>
      <td>186</td>
      <td>199</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>219</td>
      <td>200</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>225</td>
      <td>220</td>
      <td>225</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>242</td>
      <td>226</td>
      <td>242</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>243</td>
      <td>254</td>
      <td>243</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>277</td>
      <td>255</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>278</td>
      <td>286</td>
      <td>278</td>
      <td>286</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4wfe">4WFE</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTTAPQEPPARPLQAGSGAGPAPGRAM</span><span class="topo-inside">RSTTL</span><span class="topo-membrane">LALLALVLLYLVSGALVFR</span><span class="topo-outside">ALEQPHEQQAQRELGEVREKFLRAHPCVSDQELGLLIKEVADALGGGADPETQS</span><span class="topo-unknown">TSQS</span><span class="topo-outside">SHSAWDL</span><span class="topo-unknown">GSAF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">FFSGTIITTIGYG</span><span class="topo-outside">NVALRTD</span><span class="topo-membrane">AGRLFCIFYALVGIPLFGILLA</span><span class="topo-unknown">GVGDRLGSSLRHGIGHIEAIFLK</span><span class="topo-inside">WHVPPELVRVLSAMLFL</span><span class="topo-membrane">LIGCLLFVLTPTFVFCYME</span><span class="topo-outside">DWS</span><span class="topo-unknown">KLEAIYFVIVTLT</span><span class="topo-outside">TVG</span></span>
<span class="topo-ruler">       250       260       270       280       290         </span>
<span class="topo-line"><span class="topo-outside">FGDYVAGADPRQDS</span><span class="topo-membrane">PAYQPLVWFWILLGLAYFASVLTTIG</span><span class="topo-inside">NWLRVV</span><span class="topo-unknown">SRRTSNSLEVLFQ</span></span>
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
      <td>28</td>
      <td>32</td>
      <td>28</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>51</td>
      <td>33</td>
      <td>51</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>105</td>
      <td>52</td>
      <td>105</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>116</td>
      <td>110</td>
      <td>116</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>133</td>
      <td>117</td>
      <td>133</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>134</td>
      <td>140</td>
      <td>134</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>162</td>
      <td>141</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>185</td>
      <td>163</td>
      <td>185</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>186</td>
      <td>202</td>
      <td>186</td>
      <td>202</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>221</td>
      <td>203</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>224</td>
      <td>222</td>
      <td>224</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>225</td>
      <td>237</td>
      <td>225</td>
      <td>237</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>238</td>
      <td>254</td>
      <td>238</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>280</td>
      <td>255</td>
      <td>280</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>281</td>
      <td>286</td>
      <td>281</td>
      <td>286</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4wfg">4WFG</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTTAPQEPPARPLQAGSGAGPAPGRAM</span><span class="topo-inside">RSTTLL</span><span class="topo-membrane">ALLALVLLYLVSGALVFRA</span><span class="topo-outside">LEQPHEQQAQRELGEVREKFLRAHPCVSDQELGLLIKEVADALGGGADPET</span><span class="topo-unknown">QSTSQS</span><span class="topo-outside">SHSAWDL</span><span class="topo-unknown">GSAF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">FFSGTIITTIGYG</span><span class="topo-outside">NVALRTDA</span><span class="topo-membrane">GRLFCIFYALVGIPLFGILLAGVG</span><span class="topo-unknown">DRLGSSLRHGIGHIEAIFLK</span><span class="topo-inside">WHVPPELVRVLSAM</span><span class="topo-membrane">LFLLIGCLLFVLTPTFVFC</span><span class="topo-outside">YMEDWSK</span><span class="topo-unknown">LEAIYFVIVTLTTVG</span></span>
<span class="topo-ruler">       250       260       270       280       290         </span>
<span class="topo-line"><span class="topo-unknown">FG</span><span class="topo-outside">DYVAGADPRQDSP</span><span class="topo-membrane">AYQPLVWFWILLGLAYFASVLT</span><span class="topo-inside">TIGNWLRVV</span><span class="topo-unknown">SRRTSNSLEVLFQ</span></span>
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
      <td>28</td>
      <td>33</td>
      <td>28</td>
      <td>33</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>52</td>
      <td>34</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>53</td>
      <td>103</td>
      <td>53</td>
      <td>103</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>116</td>
      <td>110</td>
      <td>116</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>133</td>
      <td>117</td>
      <td>133</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>134</td>
      <td>141</td>
      <td>134</td>
      <td>141</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>165</td>
      <td>142</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>166</td>
      <td>185</td>
      <td>166</td>
      <td>185</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>186</td>
      <td>199</td>
      <td>186</td>
      <td>199</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>218</td>
      <td>200</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>225</td>
      <td>219</td>
      <td>225</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>242</td>
      <td>226</td>
      <td>242</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>243</td>
      <td>255</td>
      <td>243</td>
      <td>255</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>277</td>
      <td>256</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>278</td>
      <td>286</td>
      <td>278</td>
      <td>286</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4wfg">4WFG</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTTAPQEPPARPLQAGSGAGPAPGRAM</span><span class="topo-inside">RSTTL</span><span class="topo-membrane">LALLALVLLYLVSGALVF</span><span class="topo-outside">RALEQPHEQQAQRELGEVREKFLRAHPCVSDQELGLLIKEVADALGGGADPETQS</span><span class="topo-unknown">TSQS</span><span class="topo-outside">SHSAWDL</span><span class="topo-unknown">GSAF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">FFSGTIITTIGYG</span><span class="topo-outside">NVALRTDA</span><span class="topo-membrane">GRLFCIFYALVGIPLFGILLA</span><span class="topo-unknown">GVGDRLGSSLRHGIGHIEAIFLK</span><span class="topo-inside">WHVPPELVRVLSAMLFL</span><span class="topo-membrane">LIGCLLFVLTPTFVFCYM</span><span class="topo-outside">EDWS</span><span class="topo-unknown">KLEAIYFVIVTLTTVG</span></span>
<span class="topo-ruler">       250       260       270       280       290         </span>
<span class="topo-line"><span class="topo-unknown">FG</span><span class="topo-outside">DYVAGADPRQDS</span><span class="topo-membrane">PAYQPLVWFWILLGLAYFASVLT</span><span class="topo-unknown">TIGNWLRV</span><span class="topo-inside">V</span><span class="topo-unknown">SRRTSNSLEVLFQ</span></span>
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
      <td>28</td>
      <td>32</td>
      <td>28</td>
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
      <td>105</td>
      <td>51</td>
      <td>105</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>116</td>
      <td>110</td>
      <td>116</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>133</td>
      <td>117</td>
      <td>133</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>134</td>
      <td>141</td>
      <td>134</td>
      <td>141</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>162</td>
      <td>142</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>185</td>
      <td>163</td>
      <td>185</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>186</td>
      <td>202</td>
      <td>186</td>
      <td>202</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>220</td>
      <td>203</td>
      <td>220</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>224</td>
      <td>221</td>
      <td>224</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>225</td>
      <td>242</td>
      <td>225</td>
      <td>242</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>243</td>
      <td>254</td>
      <td>243</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>277</td>
      <td>255</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>278</td>
      <td>285</td>
      <td>278</td>
      <td>285</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>286</td>
      <td>286</td>
      <td>286</td>
      <td>286</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4wff">4WFF</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTTAPQEPPARPLQAGSGAGPAPGRAM</span><span class="topo-inside">RSTTL</span><span class="topo-membrane">LALLALVLLYLVSGALVFRA</span><span class="topo-outside">LEQPHEQQAQRELGEVREKFLRAHPCVSDQELGLLIKEVADALGGGADPET</span><span class="topo-unknown">QSTSQS</span><span class="topo-outside">SHSAWDL</span><span class="topo-unknown">GSAF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">FFSGTIITTIGYG</span><span class="topo-outside">NVALRTD</span><span class="topo-membrane">AGRLFCIFYALVGIPLFGILLAGVG</span><span class="topo-unknown">DRLGSSLRHGIGHIEAIFLK</span><span class="topo-inside">WHVPPELVRVLSAM</span><span class="topo-membrane">LFLLIGCLLFVLTPTFVFC</span><span class="topo-outside">YMEDWSK</span><span class="topo-unknown">LEAIYFVIVTLTTVG</span></span>
<span class="topo-ruler">       250       260       270       280       290         </span>
<span class="topo-line"><span class="topo-unknown">FG</span><span class="topo-outside">DYVAGADPRQDSP</span><span class="topo-membrane">AYQPLVWFWILLGLAYFASVLT</span><span class="topo-inside">TIGNWLRVV</span><span class="topo-unknown">SRRTSNSLEVLFQ</span></span>
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
      <td>28</td>
      <td>32</td>
      <td>28</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>52</td>
      <td>33</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>53</td>
      <td>103</td>
      <td>53</td>
      <td>103</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>116</td>
      <td>110</td>
      <td>116</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>133</td>
      <td>117</td>
      <td>133</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>134</td>
      <td>140</td>
      <td>134</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>165</td>
      <td>141</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>166</td>
      <td>185</td>
      <td>166</td>
      <td>185</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>186</td>
      <td>199</td>
      <td>186</td>
      <td>199</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>218</td>
      <td>200</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>225</td>
      <td>219</td>
      <td>225</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>242</td>
      <td>226</td>
      <td>242</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>243</td>
      <td>255</td>
      <td>243</td>
      <td>255</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>277</td>
      <td>256</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>278</td>
      <td>286</td>
      <td>278</td>
      <td>286</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4wff">4WFF</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTTAPQEPPARPLQAGSGAGPAPGRAM</span><span class="topo-inside">RSTT</span><span class="topo-membrane">LLALLALVLLYLVSGALVF</span><span class="topo-outside">RALEQPHEQQAQRELGEVREKFLRAHPCVSDQELGLLIKEVADALGGGADPETQS</span><span class="topo-unknown">TSQS</span><span class="topo-outside">SHSAWDL</span><span class="topo-unknown">GSAF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">FFSGTIITTIGYG</span><span class="topo-outside">NVALRTD</span><span class="topo-membrane">AGRLFCIFYALVGIPLFGILLA</span><span class="topo-unknown">GVGDRLGSSLRHGIGHIEAIFLK</span><span class="topo-inside">WHVPPELVRVLSAM</span><span class="topo-membrane">LFLLIGCLLFVLTPTFVFCYM</span><span class="topo-outside">EDWS</span><span class="topo-unknown">KLEAIYFVIVTLTTVG</span></span>
<span class="topo-ruler">       250       260       270       280       290         </span>
<span class="topo-line"><span class="topo-unknown">FG</span><span class="topo-outside">DYVAGADPRQDS</span><span class="topo-membrane">PAYQPLVWFWILLGLAYFASVL</span><span class="topo-inside">TTIGNWLR</span><span class="topo-unknown">VVSRRTSNSLEVLFQ</span></span>
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
      <td>28</td>
      <td>31</td>
      <td>28</td>
      <td>31</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>50</td>
      <td>32</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>105</td>
      <td>51</td>
      <td>105</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>116</td>
      <td>110</td>
      <td>116</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>133</td>
      <td>117</td>
      <td>133</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>134</td>
      <td>140</td>
      <td>134</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>162</td>
      <td>141</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>185</td>
      <td>163</td>
      <td>185</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>186</td>
      <td>199</td>
      <td>186</td>
      <td>199</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>220</td>
      <td>200</td>
      <td>220</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>224</td>
      <td>221</td>
      <td>224</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>225</td>
      <td>242</td>
      <td>225</td>
      <td>242</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>243</td>
      <td>254</td>
      <td>243</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>276</td>
      <td>255</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>284</td>
      <td>277</td>
      <td>284</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4wfh">4WFH</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTTAPQEPPARPLQAGSGAGPAPGRAM</span><span class="topo-inside">RSTTL</span><span class="topo-membrane">LALLALVLLYLVSGALVFRAL</span><span class="topo-outside">EQPHEQQAQRELGEVREKFLRAHPCVSDQELGLLIKEVADALGGGADPET</span><span class="topo-unknown">QSTSQS</span><span class="topo-outside">SHSAWDL</span><span class="topo-unknown">GSAF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">FFSGTIITTIGYG</span><span class="topo-outside">NVALRTD</span><span class="topo-membrane">AGRLFCIFYALVGIPLFGILLAGVG</span><span class="topo-unknown">DRLGSSLRHGIGHIEAIFLK</span><span class="topo-inside">WHVPPELVRVLSAM</span><span class="topo-membrane">LFLLIGCLLFVLTPTFVFC</span><span class="topo-outside">YMEDWSK</span><span class="topo-unknown">LEAIYFVIVTLTTVG</span></span>
<span class="topo-ruler">       250       260       270       280       290         </span>
<span class="topo-line"><span class="topo-unknown">FG</span><span class="topo-outside">DYVAGADPRQDSP</span><span class="topo-membrane">AYQPLVWFWILLGLAYFASVLT</span><span class="topo-inside">TIGNWLRVV</span><span class="topo-unknown">SRRTSNSLEVLFQ</span></span>
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
      <td>28</td>
      <td>32</td>
      <td>28</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>53</td>
      <td>33</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>103</td>
      <td>54</td>
      <td>103</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>116</td>
      <td>110</td>
      <td>116</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>133</td>
      <td>117</td>
      <td>133</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>134</td>
      <td>140</td>
      <td>134</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>165</td>
      <td>141</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>166</td>
      <td>185</td>
      <td>166</td>
      <td>185</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>186</td>
      <td>199</td>
      <td>186</td>
      <td>199</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>218</td>
      <td>200</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>225</td>
      <td>219</td>
      <td>225</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>242</td>
      <td>226</td>
      <td>242</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>243</td>
      <td>255</td>
      <td>243</td>
      <td>255</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>277</td>
      <td>256</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>278</td>
      <td>286</td>
      <td>278</td>
      <td>286</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4wfh">4WFH</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTTAPQEPPARPLQAGSGAGPAPGRAM</span><span class="topo-inside">RSTT</span><span class="topo-membrane">LLALLALVLLYLVSGALVFR</span><span class="topo-outside">ALEQPHEQQAQRELGEVREKFLRAHPCVSDQELGLLIKEVADALGGGADPETQS</span><span class="topo-unknown">TSQS</span><span class="topo-outside">SHSAWDL</span><span class="topo-unknown">GSAF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">FFSGTIITTIGYG</span><span class="topo-outside">NVALRTD</span><span class="topo-membrane">AGRLFCIFYALVGIPLFGILLAGVG</span><span class="topo-unknown">DRLGSSLRHGIGHIEAIFLK</span><span class="topo-inside">WHVPPELVRVLSAM</span><span class="topo-membrane">LFLLIGCLLFVLTPTFVFCYM</span><span class="topo-outside">EDWS</span><span class="topo-unknown">KLEAIYFVIVTLT</span><span class="topo-outside">TVG</span></span>
<span class="topo-ruler">       250       260       270       280       290         </span>
<span class="topo-line"><span class="topo-outside">FGDYVAGADPRQDS</span><span class="topo-membrane">PAYQPLVWFWILLGLAYFAS</span><span class="topo-unknown">VLTTIGNWLRVVSRRTSNSLEVLFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (14 regions)</summary>
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
      <td>28</td>
      <td>31</td>
      <td>28</td>
      <td>31</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>51</td>
      <td>32</td>
      <td>51</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>105</td>
      <td>52</td>
      <td>105</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>116</td>
      <td>110</td>
      <td>116</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>133</td>
      <td>117</td>
      <td>133</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>134</td>
      <td>140</td>
      <td>134</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>165</td>
      <td>141</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>166</td>
      <td>185</td>
      <td>166</td>
      <td>185</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>186</td>
      <td>199</td>
      <td>186</td>
      <td>199</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>220</td>
      <td>200</td>
      <td>220</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>224</td>
      <td>221</td>
      <td>224</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>225</td>
      <td>237</td>
      <td>225</td>
      <td>237</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>238</td>
      <td>254</td>
      <td>238</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>274</td>
      <td>255</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.7554##eLife.50403

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6pis">6PIS</a></td>
      <td>2.8</td>
      <td>not reported</td>
      <td>Mouse TRAAK (human TRAAK 1-26 signal + mouse TRAAK 1-275 N81Q/N84Q) with C-terminal PreScission-cleavable EGFP-10xHis, co-crystallized with Armenian hamster monoclonal 1B10 Fab</td>
      <td>K+, Fab (1B10)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris
- **Construct**: Human TRAAK (UniProt Q9NYG8-2) with additional 26 aa N-terminal extension, C-terminally truncated by 119 aa (residues 1-300 or similar), His-tag
- **Notes**: For 2014 Nature paper, construct was residues 1-290 with N104Q/N108Q and C-terminal PreScission-cleavable EGFP-10xHis fusion. Same construct used for 2021 Neuron paper and 2013 PNAS paper.

**Purification:**

- **Expression system**: Pichia pastoris SMD1163
- **Expression construct**: Human TRAAK 1-26 signal - mouse TRAAK 1-275 (N81Q/N84Q) - PreScission-cleavable EGFP-10xHis

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
      <td><a href="/xray-mp-wiki/reagents/additives/methanol/">Methanol</a> induction in fermenter</td>
      <td>—</td>
      <td></td>
      <td>P. pastoris SMD1163 transformed, expressed via <a href="/xray-mp-wiki/reagents/additives/methanol/">Methanol</a> induction in fermenter</td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>Milling</td>
      <td>—</td>
      <td>50 mM Tris pH 8.0, 150 mM KCl, 60 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>Frozen cells milled with protease inhibitors and DNase I</td>
    </tr>
    <tr>
      <td>Extraction</td>
      <td>Stirring extraction</td>
      <td>—</td>
      <td>50 mM Tris pH 8.0, 150 mM KCl + 6 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>3 h stirring at 4 C, then centrifugation at 35,000g for 45 min</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Cobalt affinity</td>
      <td>Cobalt resin</td>
      <td>50 mM Tris pH 8.0, 150 mM KCl + 6 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>1 mL resin/5 g cell pellet, 3 h stirring. Serial washes with 10 mM, 30 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>; elution with 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td><a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a></td>
      <td>—</td>
      <td>50 mM Tris pH 8.0, 150 mM KCl, 1 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> + 6 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>~1:50 (wt:wt) <a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a>, overnight at 4 C</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> (GE Healthcare)</td>
      <td>20 mM Tris pH 8.0, 150 mM KCl, 1 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> + 1 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>Concentrated 50 kDa MWCO. Peak fractions pooled for subsequent procedures</td>
    </tr>
  </tbody>
</table>

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6pis">6PIS</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTTAPQEPPARPLQAGSGAGPAPGRAM</span><span class="topo-inside">RSTTL</span><span class="topo-membrane">LALLALVLLYLVSGALV</span><span class="topo-outside">FQALEQPHEQQAQKKMDHGRDQFLRDHPCVSQKSLEDFIKLLVEALGGGANP</span><span class="topo-unknown">ETSWTQSSQHS</span><span class="topo-outside">SAWNLGSA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">F</span><span class="topo-unknown">FFSGTIITTIGY</span><span class="topo-outside">GNIVLHTDAGR</span><span class="topo-membrane">LFCIFYALVGIPLFGMLLAGVG</span><span class="topo-unknown">DRLGSSLRRGIGHIEAIFLK</span><span class="topo-inside">WHVPPGLVRSLSAV</span><span class="topo-membrane">LFLLIGCLLFVLTPTFV</span><span class="topo-outside">FSYMESWSKLEA</span><span class="topo-unknown">IYFVIVTLTTV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310</span>
<span class="topo-line"><span class="topo-unknown">GF</span><span class="topo-outside">GDYVP</span><span class="topo-unknown">GDGTGQNSPAY</span><span class="topo-outside">Q</span><span class="topo-membrane">PLVWFWILFGLAYFASVLTTIG</span><span class="topo-inside">NWL</span><span class="topo-unknown">RAVSRRTRAEMGGLTAQSNSLEVLFQ</span></span>
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
      <td>28</td>
      <td>32</td>
      <td>28</td>
      <td>32</td>
      <td>Inside</td>
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
      <td>101</td>
      <td>50</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>121</td>
      <td>113</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>133</td>
      <td>122</td>
      <td>133</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>134</td>
      <td>144</td>
      <td>134</td>
      <td>144</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>166</td>
      <td>145</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>186</td>
      <td>167</td>
      <td>186</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>187</td>
      <td>200</td>
      <td>187</td>
      <td>200</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>201</td>
      <td>217</td>
      <td>201</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>229</td>
      <td>218</td>
      <td>229</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>230</td>
      <td>242</td>
      <td>230</td>
      <td>242</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>243</td>
      <td>247</td>
      <td>243</td>
      <td>247</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>259</td>
      <td>259</td>
      <td>259</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>260</td>
      <td>281</td>
      <td>260</td>
      <td>281</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>282</td>
      <td>284</td>
      <td>282</td>
      <td>284</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6pis">6PIS</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTTAPQEPPARPLQAGSGAGPAPGRAM</span><span class="topo-inside">RST</span><span class="topo-membrane">TLLALLALVLLYLVSGALV</span><span class="topo-outside">FQALEQPHEQQAQKKMDHGRDQFLRDHPCVSQKSLEDFIKLLVEALGGGANP</span><span class="topo-unknown">ETSWTQSSQH</span><span class="topo-outside">SSAWNLGSA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">F</span><span class="topo-unknown">FFSGTIITTIGY</span><span class="topo-outside">GNIVLHTDAGRL</span><span class="topo-membrane">FCIFYALVGIPLFGMLLAGVG</span><span class="topo-unknown">DRLGSSLRRGIGHIEAIFLK</span><span class="topo-inside">WHVPPGLVRSLSAV</span><span class="topo-membrane">LFLLIGCLLFVLTPTFVF</span><span class="topo-outside">SYMESWSKLEA</span><span class="topo-unknown">IYFVIVTLTTV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310</span>
<span class="topo-line"><span class="topo-unknown">GF</span><span class="topo-outside">GDYVP</span><span class="topo-unknown">GDGTGQNS</span><span class="topo-outside">PA</span><span class="topo-membrane">YQPLVWFWILFGLAYFASVLTTIG</span><span class="topo-inside">NWL</span><span class="topo-unknown">RAVSRRTRAEMGGLTAQSNSLEVLFQ</span></span>
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
      <td>28</td>
      <td>30</td>
      <td>28</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>49</td>
      <td>31</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>101</td>
      <td>50</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>121</td>
      <td>112</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>133</td>
      <td>122</td>
      <td>133</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>134</td>
      <td>145</td>
      <td>134</td>
      <td>145</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>146</td>
      <td>166</td>
      <td>146</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>186</td>
      <td>167</td>
      <td>186</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>187</td>
      <td>200</td>
      <td>187</td>
      <td>200</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>201</td>
      <td>218</td>
      <td>201</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>229</td>
      <td>219</td>
      <td>229</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>230</td>
      <td>242</td>
      <td>230</td>
      <td>242</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>243</td>
      <td>247</td>
      <td>243</td>
      <td>247</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>257</td>
      <td>256</td>
      <td>257</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>281</td>
      <td>258</td>
      <td>281</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>282</td>
      <td>284</td>
      <td>282</td>
      <td>284</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1126##science.1213808

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3um7">3UM7</a></td>
      <td>3.8</td>
      <td>P212121</td>
      <td>Human TRAAK residues 1-300 (C-terminally truncated), N104Q/N108Q, no fusion tag</td>
      <td>K+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris
- **Construct**: Human TRAAK (UniProt Q9NYG8-2) with additional 26 aa N-terminal extension, C-terminally truncated by 119 aa (residues 1-300 or similar), His-tag
- **Notes**: For 2014 Nature paper, construct was residues 1-290 with N104Q/N108Q and C-terminal PreScission-cleavable EGFP-10xHis fusion. Same construct used for 2021 Neuron paper and 2013 PNAS paper.

**Purification:**

- **Expression system**: Pichia pastoris
- **Expression construct**: Human TRAAK residues 1-300 (C-terminally truncated by 119 aa), N104Q/N108Q, no fusion tag

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
      <td>Pichia pastoris expression</td>
      <td>—</td>
      <td></td>
      <td>Human TRAAK recombinantly expressed and purified from Pichia pastoris. Mutations N104Q/N108Q removed N-linked glycosylation sites.</td>
    </tr>
    <tr>
      <td>Purification</td>
      <td>Not detailed in main text</td>
      <td>—</td>
      <td></td>
      <td>Full purification details in Supporting Online Material. Construct was truncated at Gln300 to remove predicted intrinsically unstructured C-terminal region.</td>
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
      <td>Purified TRAAK (untagged construct, N104Q/N108Q, truncated to Gln300) in 150 mM KCl</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>150 mM KCl (native); TINO3 substituted for KCl (derivative)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Native crystals diffracted to 3.8 A. Structure solved by multi-wavelength anomalous dispersion (<a href="/xray-mp-wiki/methods/structure-determination/mad-phasing/">MAD</a>) using TINO3-soaked crystals. Additional CH3Hg+ derivatized crystals used for sequence register assignment. Space group P212121. No Fab or antibody used for crystallization.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3um7">3UM7</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTTAPQEPPARPLQAGSGAGPAPG</span><span class="topo-outside">RAMRST</span><span class="topo-membrane">TLLALLALVLLYLVSGALVFRAL</span><span class="topo-inside">EQPHEQQAQRELGEVREKFLRAHPCVSDQELGLLIKEVADALGGGADPETQST</span><span class="topo-unknown">SQSSH</span><span class="topo-inside">SAWDL</span><span class="topo-unknown">GSAF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">FFSGTIITTIGYG</span><span class="topo-inside">NVALRTD</span><span class="topo-membrane">AGRLFCIFYALVGIPLFGILLAGVGDRLGSSLR</span><span class="topo-outside">HGIGHIEAIFLKWH</span><span class="topo-unknown">VP</span><span class="topo-outside">PELVRVL</span><span class="topo-membrane">SAMLFLLIGCLLFVLTPTFVFCYM</span><span class="topo-inside">EDWSK</span><span class="topo-unknown">LEAIYFVIVTLTTVG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300         </span>
<span class="topo-line"><span class="topo-unknown">FG</span><span class="topo-inside">DYVAGADPRQDS</span><span class="topo-membrane">PAYQPLVWFWILLGLAYFASVLTTIG</span><span class="topo-outside">NWLRVVSRRT</span><span class="topo-unknown">RAEMGGLTAQSNSLEVLFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
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
      <td>24</td>
      <td>1</td>
      <td>24</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>25</td>
      <td>30</td>
      <td>25</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>53</td>
      <td>31</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>106</td>
      <td>54</td>
      <td>106</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>107</td>
      <td>111</td>
      <td>107</td>
      <td>111</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>112</td>
      <td>116</td>
      <td>112</td>
      <td>116</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>133</td>
      <td>117</td>
      <td>133</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>134</td>
      <td>140</td>
      <td>134</td>
      <td>140</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>173</td>
      <td>141</td>
      <td>173</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>174</td>
      <td>187</td>
      <td>174</td>
      <td>187</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>188</td>
      <td>189</td>
      <td>188</td>
      <td>189</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>190</td>
      <td>196</td>
      <td>190</td>
      <td>196</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>197</td>
      <td>220</td>
      <td>197</td>
      <td>220</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>225</td>
      <td>221</td>
      <td>225</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>242</td>
      <td>226</td>
      <td>242</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>243</td>
      <td>254</td>
      <td>243</td>
      <td>254</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>280</td>
      <td>255</td>
      <td>280</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>281</td>
      <td>290</td>
      <td>281</td>
      <td>290</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>291</td>
      <td>309</td>
      <td>291</td>
      <td>309</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3um7">3UM7</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTTAPQEPPARPLQAGSGAGPAPGRA</span><span class="topo-outside">MRS</span><span class="topo-membrane">TTLLALLALVLLYLVSGALVFR</span><span class="topo-inside">ALEQPHEQQAQRELGEVREKFLRAHPCVSDQELGLLIKEVADALGGGADPETQ</span><span class="topo-unknown">STSQSSH</span><span class="topo-inside">SAWDL</span><span class="topo-unknown">GSAF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">FFSGTIITTIGYG</span><span class="topo-inside">NVALRTDA</span><span class="topo-membrane">GRLFCIFYALVGIPLFGILLAGVGDRLG</span><span class="topo-outside">S</span><span class="topo-unknown">SLRHGI</span><span class="topo-outside">GHI</span><span class="topo-unknown">EAIFLKWHVPPEL</span><span class="topo-outside">VRVLSA</span><span class="topo-membrane">MLFLLIGCLLFVLTPTFVFCYM</span><span class="topo-inside">EDWS</span><span class="topo-unknown">KLEAIYFVIVTLTTVG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300         </span>
<span class="topo-line"><span class="topo-unknown">FG</span><span class="topo-inside">DYVAGADPRQDSP</span><span class="topo-membrane">AYQPLVWFWILLGLAYFASVLTTIG</span><span class="topo-outside">NWLRVVSRRT</span><span class="topo-unknown">RAEMGGLTAQSNSLEVLFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (21 regions)</summary>
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
      <td>26</td>
      <td>1</td>
      <td>26</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>27</td>
      <td>29</td>
      <td>27</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>51</td>
      <td>30</td>
      <td>51</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>104</td>
      <td>52</td>
      <td>104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>111</td>
      <td>105</td>
      <td>111</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>112</td>
      <td>116</td>
      <td>112</td>
      <td>116</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>133</td>
      <td>117</td>
      <td>133</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>134</td>
      <td>141</td>
      <td>134</td>
      <td>141</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>169</td>
      <td>142</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>170</td>
      <td>170</td>
      <td>170</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>171</td>
      <td>176</td>
      <td>171</td>
      <td>176</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>177</td>
      <td>179</td>
      <td>177</td>
      <td>179</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>180</td>
      <td>192</td>
      <td>180</td>
      <td>192</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>193</td>
      <td>198</td>
      <td>193</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>220</td>
      <td>199</td>
      <td>220</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>224</td>
      <td>221</td>
      <td>224</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>225</td>
      <td>242</td>
      <td>225</td>
      <td>242</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>243</td>
      <td>255</td>
      <td>243</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>280</td>
      <td>256</td>
      <td>280</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>281</td>
      <td>290</td>
      <td>281</td>
      <td>290</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>291</td>
      <td>309</td>
      <td>291</td>
      <td>309</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1073##pnas.1218950110

**Expression:**

- **Expression system**: Pichia pastoris
- **Construct**: Human TRAAK (UniProt Q9NYG8-2) with additional 26 aa N-terminal extension, C-terminally truncated by 119 aa (residues 1-300 or similar), His-tag
- **Notes**: For 2014 Nature paper, construct was residues 1-290 with N104Q/N108Q and C-terminal PreScission-cleavable EGFP-10xHis fusion. Same construct used for 2021 Neuron paper and 2013 PNAS paper.

**Purification:**

- **Expression system**: Pichia pastoris
- **Expression construct**: Human TRAAK residues 1-300 (C-terminally truncated by 119 aa), N104Q/N108Q, C-terminal PreScission-cleavable EGFP-10xHis fusion (same construct as original TRAAK structure)

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
      <td>Cell disruption</td>
      <td>Milling (Retsch MM301)</td>
      <td>—</td>
      <td>50 mM Tris (pH 8.0), 150 mM KCl, 60 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>, 0.1 mg/mL DNase I, protease inhibitors</td>
      <td>Frozen Pichia cells milled 5x3 min at 25 Hz, 1 g pellet per 4 mL lysis buffer</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Stirring extraction + centrifugation</td>
      <td>—</td>
      <td>6 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>Membranes prepared for 3 h with gentle stirring, then centrifugation at 35,000 x g for 45 min</td>
    </tr>
    <tr>
      <td>Cobalt <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Cobalt resin (Clontech)</td>
      <td>50 mM Tris (pH 8.0), 150 mM KCl + 6 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>1 mL resin per 5 g cell pellet; serial washes with 10 mM, 30 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>; elution with 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td><a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a></td>
      <td>—</td>
      <td>50 mM Tris (pH 8.0), 150 mM KCl, 1 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> + 6 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>~1:50 (wt:wt) <a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a>, overnight at 4 C</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> (GE Healthcare)</td>
      <td>20 mM Tris (pH 8.0), 150 mM KCl, 1 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> + 4 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>Concentrated using 50-kDa MWCO</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (Fab-mediated crystallization)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>TRAAK-Fab complex (mouse monoclonal Fab against TRAAK)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Mouse monoclonal antibodies raised against TRAAK purified in dodecyl-beta-D-maltopyranoside. Positive clones identified by ELISA and Western blot. Fab from one antibody clone used for crystallization. Diffraction data collected to 2.75 A Bragg spacings. Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using a Fab search model.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Domain-swapped chain connectivity in TRAAK

The 2.75-A resolution TRAAK-Fab structure reveals a domain-swapped
chain connectivity in which two opposing outer helices exchange 180
degrees around the channel. This was not apparent in the original
3.8-A structure (PDB 3UM7). The domain swap involves only four
amino acids (His76-Val79) at the top of the helical cap, which adopt
an unambiguous crossover conformation. Fluorescent Fab labeling on
live HEK cells confirmed that domain-swapped TRAAK exists in cell
membranes, suggesting this is the generally correct model.

### Gated membrane side opening

A conformational change in inner helix 2 (IH2) of one subunit seals
a side opening to the membrane bilayer. The intracellular C-terminus
of IH2 is elevated, its extracellular N-terminal end moves, and the
connecting segment undergoes substantial reorganization. New
interactions between Phe272, Val275, Ile279, and Leu283 on IH2 and
residues on IH1 and pore helix 2 close the opening. The other
subunit retains an open conformation similar to the original
structure, suggesting this gating may relate to mechanosensitivity.

### Implications for mechanosensitivity

TRAAK channels gate in response to chemical or mechanical membrane
perturbation. The conformational changes around the selectivity
filter associated with IH2 movement may transmit signals across
the membrane. Although the selectivity filter is not perceptibly
altered, the structural changes around it may alter its dynamics
or dynamics to influence ion conduction. TRAAK is thought to gate
at the selectivity filter rather than through a canonical inner
helical gate.

### Localization to nodes of Ranvier

TRAAK is localized exclusively to nodes of Ranvier throughout the
mammalian central and peripheral nervous system, as shown by
immunohistochemistry with specific monoclonal antibodies. It is not
found in axon initial segments, sensory endings, synapses,
astrocytes, or microglia. Approximately 80% of myelinated nerve
fibers contain TRAAK in an all-nodes or no-nodes per axon fashion.
Within single teased sciatic nerve fibers, all nodes are either
TRAAK-positive or TRAAK-negative, suggesting two distinct classes
of myelinated neurons.

### Role in nodal membrane physiology

TRAAK contributes to the leak K+ current in mammalian nodes of
Ranvier. Using the TRAAK inhibitor RU2 and node-clamp
electrophysiology on rat sciatic nerve fibers, TRAAK was shown to
account for approximately 19% of the total outward nodal current.
TRAAK stabilizes the resting membrane potential by approximately
4 mV hyperpolarization, thereby increasing NaV channel availability
for action potential propagation. Blocking TRAAK with RU2
depolarizes the node, reduces action potential amplitude, and
amplifies spike amplitude rundown during high-frequency (100 Hz)
stimulation.

### Anti-TRAAK monoclonal antibody 1B10 Fab complex structure

The X-ray crystal structure of mouse TRAAK in complex with the
Fab fragment of monoclonal antibody 1B10 was determined at 2.8
angstroms resolution (PDB 6PIS). The antibody binds to a large
1003-square-angstrom epitope spanning both subunits of the dimeric
channel, with cap helix 1 of one protomer forming ~2/3 of the
surface and cap helix 2 from the second protomer forming ~1/3.
Most epitope-forming residues are poorly conserved among K2P
channels, explaining the high specificity for TRAAK.

### Helical cap and extracellular pharmacology of K2P channels

The original 3.8 A TRAAK structure (PDB 3UM7) revealed a
previously unobserved helical cap extending ~35 A above the
membrane, formed by the outer helix-pore helix connection of pore
domain 1. The rigid helical bundle restricts molecular access to
the pore entryway, explaining why K2P channels are resistant to
extracellular pore-blocking toxins that effectively inhibit
tetrameric K+ channels. The cap may also serve as a binding site
for endogenous modulators.

### Two-fold symmetry and fenestrations

TRAAK forms a two-fold symmetric dimer with two non-identical pore
domains per protomer, unlike canonical four-fold symmetric K+
channels. Despite overall asymmetry, the selectivity filter
converges to nearly perfect four-fold symmetry (RMSD 0.6 A vs
[KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/)). Openings between subunits (fenestrations) expose the central
cavity to the lipid membrane, providing access for hydrophobic
inhibitors and coupling membrane properties to channel gating.
Electron density within fenestrations is consistent with bound
alkyl chains of ~11 carbons.

### Amphipathic helix as mechanosensitive element

The pore domain 1 inner helix kinks at Pro155 and projects
laterally along the cytoplasmic membrane surface. This amphipathic
extension, with hydrophobic residues on one face and basic residues
(Arg167, Arg173, His174, His178, Lys185) on the other, is
positioned to interact with both lipid tails and acidic head groups.
This tendril-like structure may be the molecular sensor for TRAAK's
response to mechanical and chemical properties of the lipid bilayer.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/dm/">Decylmaltoside (DM)</a> — Primary solubilization detergent (1% for solubilization, 0.03-0.4% for final sample)
- <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a> — PEG400 (27-33%) used as crystallization precipitant and cryoprotectant
- <a href="/xray-mp-wiki/reagents/additives/calcium-chloride/">Calcium Chloride (CaCl2)</a> — 64-200 mM CaCl2 in crystallization reservoir
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> — 50 mM Tris (pH 8.8) in crystallization and 20 mM Tris (pH 8.8) in purification buffer
- <a href="/xray-mp-wiki/methods/expression-systems/pichia-pastoris/">Pichia pastoris Expression System</a> — TRAAK expressed in Pichia pastoris
- <a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging-Drop Vapor Diffusion</a> — Crystallization method used for all TRAAK structures
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/k2p-2-1-trek-1/">K2P 2.1 (TREK-1) Potassium Channel</a> — Related mechanosensitive K2P channel with shared gating mechanism
- <a href="/xray-mp-wiki/proteins/kcsA/">KcsA Potassium Channel</a> — Canonical K+ channel used for structural comparison; TRAAK differs in fourfold vs twofold symmetry and domain-swapped connectivity
- <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
