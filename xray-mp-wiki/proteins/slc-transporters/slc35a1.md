---
title: "SLC35A1 Human CMP-Sialic Acid Transporter (mCST)"
created: 2026-06-03
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature24464, doi/10.7554##eLife.45221]
verified: agent
uniprot_id: Q61420
---

# SLC35A1 Human CMP-Sialic Acid Transporter (mCST)

<div class="expr-badges"><span class="expr-badge expr-p-pastoris">P. pastoris</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q61420">UniProt: Q61420</a>

<span class="expr-badge">Mus musculus</span>

## Overview

SLC35A1 is the human CMP-sialic acid transporter, a member of the SLC35 family of nucleotide sugar transporters (NSTs). It imports CMP-sialic acid into the Golgi apparatus for sialylation reactions using an antiport mechanism exchanging CMP-sialic acid for CMP. SLC35A1 is mutated in congenital disorder of glycosylation IIf, resulting in a lack of sialic acid on the surface of cells. The first crystal structures of the mouse ortholog (mCST, 91% identical to human CST) were determined by Ahuja and Whorton (2019, eLife) at 2.58 A resolution in complex with CMP (PDB 6OH2) and at 2.75 A with CMP-sialic acid (PDB 6OH3) using [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/). These structures reveal a 10-TM bundle adopting the drug/metabolite transporter (DMT) superfamily fold with a pseudo-two-fold inverted symmetry. The structures define the molecular basis for nucleotide selectivity, explain disease-causing mutations, and reveal a unique lumen-facing partially-occluded conformation that represents a key intermediate in the transport cycle.

## Publications

### doi/10.1038##nature24464

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5oge">5OGE</a></td>
      <td>N/A</td>
      <td>N/A</td>
      <td>Full-length SLC35A1 homology model</td>
      <td>CMP-sialic acid (predicted binding)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris SMD1168H
- **Construct**: mCST with N-terminal GFP-His10 tag and [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) site

### doi/10.7554##eLife.45221

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6oh2">6OH2</a></td>
      <td>2.58 A</td>
      <td>C2</td>
      <td>mCST DeltaC (lacking last 15 residues; residues 15-317)</td>
      <td>CMP</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6oh3">6OH3</a></td>
      <td>2.75 A</td>
      <td>C2</td>
      <td>mCST DeltaC (lacking last 15 residues; residues 7-317)</td>
      <td>CMP-sialic acid</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6oh4">6OH4</a></td>
      <td>3.4 x 3.4 x 4.6 A (anisotropic)</td>
      <td>P2(1)</td>
      <td>Full-length mCST (residues 15-317)</td>
      <td>CMP</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris SMD1168H
- **Construct**: mCST with N-terminal GFP-His10 tag and [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) site

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
      <td>Membrane solubilization</td>
      <td>Detergent extraction</td>
      <td>--</td>
      <td>25 mM HEPES pH 7.5, 150 mM NaCl, 5 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> + 1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Membranes resuspended and homogenized, solubilized for 1.5 hr at 4C</td>
    </tr>
    <tr>
      <td>IMAC</td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> agarose</td>
      <td>25 mM HEPES pH 7.5, 150 mM NaCl, 5 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, 0.1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Batch binding for 1.5 hr. Washed with 5 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, then 20 mM, then 40 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>. Eluted with 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td>Protease digestion</td>
      <td>--</td>
      <td>25 mM HEPES pH 7.5, 150 mM NaCl, 5 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, 0.1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a> added at 1:20 ratio, overnight at 4C to cleave GFP-His10 tag</td>
    </tr>
    <tr>
      <td>SEC</td>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> (GE Healthcare)</td>
      <td>25 mM HEPES pH 7.5, 150 mM NaCl, 0.1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Concentrated in 50 K MWCO concentrator before <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion (HDVD)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>mCST at 5 mg/mL in 25 mM HEPES pH 7.5, 150 mM NaCl, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, supplemented with 20 mM CMP</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>25.6-26.8% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400, 0.1 M Tris pH 8.5, 0.1 M magnesium acetate</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>5-13 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Increased <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400 concentration in mother liquor</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Rectangular rod-shaped crystals. Data from 5 crystals merged. Hg and Pt derivatives prepared by soaking for <a href="/xray-mp-wiki/methods/structure-determination/miras/">MIRAS</a> phasing. Anisotropic diffraction to 3.4 x 3.4 x 4.6 A.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>mCST DeltaC at 5-7 mg/mL in 25 mM HEPES pH 7.5, 150 mM NaCl, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>3-6 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals harvested directly from LCP drop and flash-frozen in liquid N2</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Protein mixed with <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a>. LCP crystals diffracted to 2.58 A (CMP complex) and 2.75 A (CMP-Sia complex). Rod-shaped crystals. For CMP-Sia complex, apyrase was added to maintain low CMP levels. Data from 26 crystals merged for CMP complex.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6oh2">6OH2</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPARENVSLFFKL</span><span class="topo-inside">Y</span><span class="topo-membrane">CLTVMTLVAAAYT</span><span class="topo-outside">VALRYTRTTAEELYF</span><span class="topo-membrane">STTAVCITEVIKLLIS</span><span class="topo-inside">VGLLAKETGSLGRFKASLSENVLGSPKELAKLS</span><span class="topo-membrane">VPSLVYAVQNNMAFLA</span><span class="topo-outside">LSNLDAAVY</span><span class="topo-membrane">QVT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">YQLKIPCTALCTVL</span><span class="topo-inside">MLNRTL</span><span class="topo-membrane">SKLQWISVFMLCGGVTLVQ</span><span class="topo-outside">WKPA</span><span class="topo-unknown">QATK</span><span class="topo-outside">VVVAQNPLLGFG</span><span class="topo-membrane">AIAIAVLCSGFAGVYF</span><span class="topo-inside">EKVLKSSDTS</span><span class="topo-unknown">LWVRNIQM</span><span class="topo-membrane">YLSGIVVTLAGTYLSDGA</span><span class="topo-outside">EIQEKGFFY</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330</span>
<span class="topo-line"><span class="topo-outside">GYTY</span><span class="topo-membrane">YVWFVIFLASVGGLYTSVVV</span><span class="topo-inside">KYTD</span><span class="topo-membrane">NIMKGFSAAAAIVLSTIASVLL</span><span class="topo-outside">FGLQITLSF</span><span class="topo-membrane">ALGALLVCVSIYLYGL</span><span class="topo-inside">PR</span><span class="topo-unknown">QDTTSNSLEVLFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (23 regions)</summary>
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
      <td>28</td>
      <td>16</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>43</td>
      <td>29</td>
      <td>43</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>59</td>
      <td>44</td>
      <td>59</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>92</td>
      <td>60</td>
      <td>92</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>108</td>
      <td>93</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>117</td>
      <td>109</td>
      <td>117</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>134</td>
      <td>118</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>140</td>
      <td>135</td>
      <td>140</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>159</td>
      <td>141</td>
      <td>159</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>163</td>
      <td>160</td>
      <td>163</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>179</td>
      <td>168</td>
      <td>179</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>180</td>
      <td>195</td>
      <td>180</td>
      <td>195</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>205</td>
      <td>196</td>
      <td>205</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>206</td>
      <td>213</td>
      <td>206</td>
      <td>213</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>214</td>
      <td>231</td>
      <td>214</td>
      <td>231</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>244</td>
      <td>232</td>
      <td>244</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>245</td>
      <td>264</td>
      <td>245</td>
      <td>264</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>265</td>
      <td>268</td>
      <td>265</td>
      <td>268</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>269</td>
      <td>290</td>
      <td>269</td>
      <td>290</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>291</td>
      <td>299</td>
      <td>291</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>315</td>
      <td>300</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>316</td>
      <td>317</td>
      <td>316</td>
      <td>317</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6oh3">6OH3</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPARE</span><span class="topo-inside">NVSLF</span><span class="topo-membrane">FKLYCLTVMTLVAAAYTVAL</span><span class="topo-outside">RYTRTTAEELYF</span><span class="topo-membrane">STTAVCITEVIKLLIS</span><span class="topo-inside">VGLLAKETGSLGRFKASLSENVLGSPKELAKLSV</span><span class="topo-membrane">PSLVYAVQNNMAFLAL</span><span class="topo-outside">SNLDA</span><span class="topo-membrane">AVYQVT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">YQLKIPCTALC</span><span class="topo-inside">TVLMLNRTLSK</span><span class="topo-membrane">LQWISVFMLCGGVTLVQW</span><span class="topo-unknown">KPAQATK</span><span class="topo-outside">VVVAQNPLL</span><span class="topo-membrane">GFGAIAIAVLCSGFAG</span><span class="topo-inside">VYFEKVLKSSDTS</span><span class="topo-unknown">LWVRNIQM</span><span class="topo-membrane">YLSGIVVTLAGTYLSDGAEIQ</span><span class="topo-outside">EKGFFY</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330</span>
<span class="topo-line"><span class="topo-outside">GYTY</span><span class="topo-membrane">YVWFVIFLASVGGLYTSVVV</span><span class="topo-inside">KYTDN</span><span class="topo-membrane">IMKGFSAAAAIVLSTIASVLL</span><span class="topo-outside">FGLQITLS</span><span class="topo-membrane">FALGALLVCVSIYLY</span><span class="topo-inside">GLPR</span><span class="topo-unknown">QDTTSNSLEVLFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (22 regions)</summary>
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
      <td>7</td>
      <td>11</td>
      <td>7</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>31</td>
      <td>12</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>43</td>
      <td>32</td>
      <td>43</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>59</td>
      <td>44</td>
      <td>59</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>93</td>
      <td>60</td>
      <td>93</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>109</td>
      <td>94</td>
      <td>109</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>114</td>
      <td>110</td>
      <td>114</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>131</td>
      <td>115</td>
      <td>131</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>142</td>
      <td>132</td>
      <td>142</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>160</td>
      <td>143</td>
      <td>160</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>168</td>
      <td>176</td>
      <td>168</td>
      <td>176</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>192</td>
      <td>177</td>
      <td>192</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>193</td>
      <td>205</td>
      <td>193</td>
      <td>205</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>206</td>
      <td>213</td>
      <td>206</td>
      <td>213</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>214</td>
      <td>234</td>
      <td>214</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>244</td>
      <td>235</td>
      <td>244</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>245</td>
      <td>264</td>
      <td>245</td>
      <td>264</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>265</td>
      <td>269</td>
      <td>265</td>
      <td>269</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>270</td>
      <td>290</td>
      <td>270</td>
      <td>290</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>291</td>
      <td>298</td>
      <td>291</td>
      <td>298</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>299</td>
      <td>313</td>
      <td>299</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>317</td>
      <td>314</td>
      <td>317</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6oh4">6OH4</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPARENVSLFFKL</span><span class="topo-inside">Y</span><span class="topo-membrane">CLTVMTLVAAAYTVAL</span><span class="topo-outside">RYTRTTAEELYF</span><span class="topo-membrane">STTAVCITEVIKLLISVGL</span><span class="topo-inside">LAKETGS</span><span class="topo-unknown">LGRFKASLSE</span><span class="topo-inside">NVLGSPKELAKL</span><span class="topo-membrane">SVPSLVYAVQNNMAFLAL</span><span class="topo-outside">SNLDA</span><span class="topo-membrane">AVYQVT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">YQLKIPCTALCT</span><span class="topo-inside">VLMLNRTLSK</span><span class="topo-membrane">LQWISVFMLCGGVTLVQW</span><span class="topo-outside">KPA</span><span class="topo-unknown">QATK</span><span class="topo-outside">VVVAQNPLL</span><span class="topo-membrane">GFGAIAIAVLCSGFAGVYF</span><span class="topo-inside">EKVLKSSDTS</span><span class="topo-unknown">LWVRNIQM</span><span class="topo-membrane">YLSGIVVTLAGTYLSDGA</span><span class="topo-outside">EIQEKGFFY</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340     </span>
<span class="topo-line"><span class="topo-outside">GYTY</span><span class="topo-membrane">YVWFVIFLASVGGLYTSVVV</span><span class="topo-inside">KYTD</span><span class="topo-membrane">NIMKGFSAAAAIVLSTIASVLLF</span><span class="topo-outside">GLQITL</span><span class="topo-membrane">SFALGALLVCVSIYLYG</span><span class="topo-inside">LPR</span><span class="topo-unknown">QDTTSIQQEATSKERIIGVSNSLEVLFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (25 regions)</summary>
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
      <td>31</td>
      <td>16</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>43</td>
      <td>32</td>
      <td>43</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>62</td>
      <td>44</td>
      <td>62</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>69</td>
      <td>63</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>79</td>
      <td>70</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>91</td>
      <td>80</td>
      <td>91</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>109</td>
      <td>92</td>
      <td>109</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>114</td>
      <td>110</td>
      <td>114</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>132</td>
      <td>115</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>133</td>
      <td>142</td>
      <td>133</td>
      <td>142</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>160</td>
      <td>143</td>
      <td>160</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>163</td>
      <td>161</td>
      <td>163</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>176</td>
      <td>168</td>
      <td>176</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>195</td>
      <td>177</td>
      <td>195</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>205</td>
      <td>196</td>
      <td>205</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>206</td>
      <td>213</td>
      <td>206</td>
      <td>213</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>214</td>
      <td>231</td>
      <td>214</td>
      <td>231</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>244</td>
      <td>232</td>
      <td>244</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>245</td>
      <td>264</td>
      <td>245</td>
      <td>264</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>265</td>
      <td>268</td>
      <td>265</td>
      <td>268</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>269</td>
      <td>291</td>
      <td>269</td>
      <td>291</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>292</td>
      <td>297</td>
      <td>292</td>
      <td>297</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>298</td>
      <td>314</td>
      <td>298</td>
      <td>314</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>315</td>
      <td>317</td>
      <td>315</td>
      <td>317</td>
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

### First crystal structure of a mammalian nucleotide sugar transporter

The mCST structures (PDB 6OH2, 6OH3) represent the first high-resolution structures of any mammalian NST. The 10-TM bundle adopts the DMT superfamily fold with pseudo-two-fold inverted symmetry between the N-terminal (TMs 1-5) and C-terminal (TMs 6-10) halves, consistent with an ancient gene duplication event.

### Nucleotide selectivity mechanism

CMP is extensively coordinated by at least 15 residues. The cytosine base is recognized by Lys55, Tyr214, and Asn210, explaining the inability to accommodate the larger guanine base of GMP. The [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) base of UMP differs at the C-4 position (carbonyl vs amine), which would alter hydrogen bonding with Asn210 and create electrostatic repulsion with Phe195. These structural features explain the >250-fold selectivity for CMP over UMP and GMP.

### Sialic acid binding cavity

The Sia moiety of CMP-Sia occupies a large cavity that was vacant in the CMP-only structure. The C-1 carboxyl interacts with Lys124 (which shifts 2 A from its position in the CMP-bound structure). The cavity adjacent to the C-5 N-acetyl group can accommodate the Neu5Gc variant, explaining why human CST can transport both Neu5Ac and Neu5Gc conjugates.

### Lumen-facing partially-occluded conformation

The mCST structures reveal a unique lumen-facing partially-occluded state not previously observed in other DMT proteins. The constriction (~6 x 4 A) between TM9 and the protein core allows CMP passage but blocks the larger CMP-Sia. TM9 is dissociated from the core while TMs 1 and 8 remain engaged, forming a lid over the substrate-binding pocket. A fully-open lumen-facing state likely requires dissociation of TMs 1 and 8 as well, resembling the conformations seen in [Vrg4 GDP-Mannose Transporter (Saccharomyces cerevisiae)](/xray-mp-wiki/proteins/slc-transporters/vrg4/) and YddG.

### Obligatory antiport mechanism

mCST functions as a nearly-obligatory antiporter requiring lumenal CMP for efficient CMP-Sia uptake (trans-stimulation). Structural comparison with the algal triose phosphate transporter GsTPT2 suggests that the occluded state involves TM9 associating with the protein core and rearrangement of TMs 5 and 10. The ~500 A2 reduction in buried surface area among TMs 1, 8, and 9 in the partially-occluded state compared to the fully-open state may explain why substrate binding is necessary to stabilize the occluded conformation.

### Disease mutation mapping

Analysis of mCST explains the effects of known disease-causing mutations in human SLC35 genes. Residues interacting with the phosphate group of CMP are hotspots for mutations causing congenital disorders of glycosylation. The T156R and E196K mutations in SLC35A1 likely impair conformational transitions during transport, while Q101H impairs substrate binding.

### Substrate-induced conformational changes detected by tryptophan fluorescence

CMP binding quenches mCST intrinsic tryptophan fluorescence through a single residue, Trp207 located at the cytoplasmic end of TM7. Mutations of Trp207 do not affect CMP binding affinity but eliminate the fluorescence response, confirming that Trp207 senses CMP-induced conformational changes rather than direct ligand contact.


## Cross-References

- <a href="/xray-mp-wiki/proteins/slc-transporters/vrg4/">Vrg4 GDP-Mannose Transporter</a> — Structural homolog and reference model for the DMT superfamily fold
- <a href="/xray-mp-wiki/proteins/slc-transporters/slc35c1/">SLC35C1 Human GDP-Fucose Transporter</a> — Related SLC35 family nucleotide sugar transporter
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/sl35-family/">SLC35 Family (Nucleotide Sugar Transporters)</a> — Transporter family classification
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase (LCP)</a> — LCP crystallization method used to obtain high-resolution structures
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">N-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent used for purification and crystallization
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/miras/">MIRAS</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
