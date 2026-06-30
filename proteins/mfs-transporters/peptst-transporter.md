---
title: "PepTSt Peptide Transporter from Streptococcus thermophilus"
created: 2026-06-16
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1371##journal.pone.0173126]
verified: false
---

# PepTSt Peptide Transporter from Streptococcus thermophilus

## Overview

PepTSt is a proton-dependent oligopeptide transporter (POT) from the Major Facilitator Superfamily (MFS) found in Streptococcus thermophilus. It mediates the uptake of di- and tripeptides and is a bacterial homolog of the human intestinal peptide transporters PepT1 and PepT2. Crystal structures have been determined in three different crystal forms (P2_12_12_1, C222_1, and P3_121), all capturing inward facing conformations. The P3_121 form reported here was crystallized using the short-chain detergent n-Nonyl-β-D-maltopyranoside (NM) and the MIRAS phasing method, revealing a monomeric inward facing state with the TM10-TM11 lobe bent toward the central pore, suggesting an inward facing occluded or intermediate conformation. PepTSt consists of 14 transmembrane helices (TM1-TM12 forming the canonical MFS N- and C-domains, plus TM-A and TM-B in the linker region).


## Publications

### doi/10.1371##journal.pone.0173126

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5mmt">5MMT</a></td>
      <td>3.4 A</td>
      <td>P3_1_21</td>
      <td>C-terminally hexahistidine-tagged wild-type PepTSt (Ce27) from Streptococcus thermophilus. Expressed in E. coli C41. Purified in NM (n-Nonyl-β-D-maltopyranoside) detergent.</td>
      <td>Penicillin G (present in protein sample, not identified in electron density)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4aps">4APS</a></td>
      <td>3.3 A</td>
      <td>P2_1_2_1_2_1</td>
      <td>C-terminally hexahistidine-tagged PepTSt</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4d2c">4D2C</a></td>
      <td>2.3 A</td>
      <td>C222_1</td>
      <td>C-terminally hexahistidine-tagged PepTSt</td>
      <td>Dipeptide</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4d2b">4D2B</a></td>
      <td></td>
      <td>C222_1</td>
      <td>C-terminally hexahistidine-tagged PepTSt</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4d2d">4D2D</a></td>
      <td></td>
      <td>C222_1</td>
      <td>C-terminally hexahistidine-tagged PepTSt</td>
      <td>Tripeptide</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5d58">5D58</a></td>
      <td></td>
      <td>C222_1</td>
      <td>C-terminally hexahistidine-tagged PepTSt</td>
      <td>Dipeptide</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5d59">5D59</a></td>
      <td></td>
      <td>C222_1</td>
      <td>C-terminally hexahistidine-tagged PepTSt</td>
      <td>Dipeptide</td>
    </tr>
  </tbody>
</table>
 - R-work 26.5%, R-free 28.6%

**Expression:**

- **Expression system**: [E. coli C41](/xray-mp-wiki/methods/expression-systems/e-coli-expression)
- **Construct**: C-terminally hexahistidine-tagged wild-type PepTSt (Ce27)
- **Notes**: Protein expressed in E. coli C41 cells. For SeMet labeling, protein was expressed in minimal medium supplemented with SeMet according to established protocols. Two mutant variants were prepared for phasing: L226M and F338M.

**Purification:**

- **Expression system**: E. coli C41
- **Expression construct**: C-terminally hexahistidine-tagged PepTSt (Ce27)
- **Tag info**: C-terminal 6xHis tag

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
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>Buffer with 1% detergent + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>, or <a href="/xray-mp-wiki/reagents/detergents/nm/">NM</a> at 1%</td>
      <td>Four detergents tested: <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, DDM, DM, NM. For NM, protein was purified in DM up to IMAC step, then exchanged to NM in SEC step.</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography">IMAC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td>IMAC resin</td>
      <td>Buffer with appropriate detergent + DDM (0.03%), DM (0.2%), NM (0.4%), or LMNG (0.01%)</td>
      <td>Elution by passing <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV Protease</a> over beads to cleave His tag</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">SEC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Size Exclusion Chromatography</a></td>
      <td>SEC column</td>
      <td>Buffer with appropriate detergent + As above</td>
      <td>Final purification step to obtain monodisperse PepTSt</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting-Drop Vapor Diffusion</a> (in surfo)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>PepTSt at 5-10 mg/mL purified in NM</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.05 M <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 8.0, 30% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG 550 MME</a>, 1.2% Fos-<a href="/xray-mp-wiki/reagents/ligands/choline/">Choline</a> 10</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>277 K (4 C)</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals flash frozen in liquid nitrogen without prior cryobuffer soaking</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Initial hits in 96-well sitting-drop plates. Scaling up to 24-well format was not found beneficial. <a href="/xray-mp-wiki/reagents/detergents/fos-choline-10/">Fos-Choline-10</a> additive significantly improved diffraction. Native crystals diffracted to 3.4 A maximum resolution with severe anisotropy. Data truncated and scaled anisotropically. <a href="/xray-mp-wiki/methods/structure-determination/miras/">MIRAS</a> phasing using SeMet (F338M mutant) and KAu(CN)2 derivative.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5mmt">5MMT</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEDKGKTFFG</span><span class="topo-inside">QPLGLSTLF</span><span class="topo-membrane">MTEMWERFSYYGMRAILL</span><span class="topo-outside">YYMWFLISTGDLHITRATAA</span><span class="topo-membrane">SIMAIYASMVYLSGTIG</span><span class="topo-inside">GFVADRIIGARPA</span><span class="topo-membrane">VFWGGVLIMLGHIVLAL</span><span class="topo-outside">PFGAS</span><span class="topo-membrane">ALFGSIILIII</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GTGFLKP</span><span class="topo-inside">NVSTLVGTLYDEHDRRRDAGFSIFV</span><span class="topo-membrane">FGINLGAFIAPLIVGAA</span><span class="topo-outside">QEAAGYH</span><span class="topo-membrane">VAFSLAAIGMFIGLLVY</span><span class="topo-inside">YFGGKKTLDPHYLRPTDP</span><span class="topo-unknown">LAP</span><span class="topo-inside">EEVKPLL</span><span class="topo-membrane">VKVSLAVAGFIAIIVVMNL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">VGWNSLPA</span><span class="topo-membrane">YINLLTIVAIAIPVFY</span><span class="topo-unknown">FAWMISSVKV</span><span class="topo-inside">TSTEHLRVVSYI</span><span class="topo-membrane">PLFIAAVLFWAIEEQGSVVLA</span><span class="topo-outside">TFAAERVDSSWFPVS</span><span class="topo-membrane">WFQSLNPLFIMLYTPFF</span><span class="topo-inside">AWLWT</span><span class="topo-unknown">AWKKNQP</span><span class="topo-inside">SSP</span><span class="topo-membrane">TKFAVG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LMFAGLSFLLMA</span><span class="topo-outside">IPGALYGTSGKVSP</span><span class="topo-membrane">LWLVGSWALVILGEMLI</span><span class="topo-unknown">SPVGLSVTTKLAPKAFN</span><span class="topo-inside">SQMMS</span><span class="topo-membrane">MWFLSSSVGSALNAQLV</span><span class="topo-outside">TLYNAKSEVAYF</span><span class="topo-membrane">SYFGLGSVVLGIVLVFLS</span><span class="topo-unknown">KRIQGLMQ</span></span>
<span class="topo-ruler">       490</span>
<span class="topo-line"><span class="topo-unknown">GVEAENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (30 regions)</summary>
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
      <td>11</td>
      <td>19</td>
      <td>11</td>
      <td>19</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>37</td>
      <td>20</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>57</td>
      <td>38</td>
      <td>57</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>74</td>
      <td>58</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>87</td>
      <td>75</td>
      <td>87</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>104</td>
      <td>88</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>109</td>
      <td>105</td>
      <td>109</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>127</td>
      <td>110</td>
      <td>127</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>128</td>
      <td>152</td>
      <td>128</td>
      <td>152</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>169</td>
      <td>153</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>176</td>
      <td>170</td>
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
      <td>211</td>
      <td>194</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>221</td>
      <td>215</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>222</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>248</td>
      <td>241</td>
      <td>248</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>264</td>
      <td>249</td>
      <td>264</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>286</td>
      <td>275</td>
      <td>286</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>307</td>
      <td>287</td>
      <td>307</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>308</td>
      <td>322</td>
      <td>308</td>
      <td>322</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>339</td>
      <td>323</td>
      <td>339</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>340</td>
      <td>344</td>
      <td>340</td>
      <td>344</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>352</td>
      <td>354</td>
      <td>352</td>
      <td>354</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>355</td>
      <td>372</td>
      <td>355</td>
      <td>372</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>373</td>
      <td>386</td>
      <td>373</td>
      <td>386</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>387</td>
      <td>403</td>
      <td>387</td>
      <td>403</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>421</td>
      <td>425</td>
      <td>421</td>
      <td>425</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>426</td>
      <td>442</td>
      <td>426</td>
      <td>442</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>443</td>
      <td>454</td>
      <td>443</td>
      <td>454</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>455</td>
      <td>472</td>
      <td>455</td>
      <td>472</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4aps">4APS</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEDKGKTFFG</span><span class="topo-inside">QPLGLST</span><span class="topo-membrane">LFMTEMWERFSYYGMRA</span><span class="topo-outside">ILLYYMWFLISTGDLHITRATAAS</span><span class="topo-membrane">IMAIYASMVYLSGTIG</span><span class="topo-inside">GFVADRIIGARPA</span><span class="topo-membrane">VFWGGVLIMLGHIV</span><span class="topo-outside">LALPFGASALF</span><span class="topo-membrane">GSIILIII</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GTGFLKP</span><span class="topo-inside">NVSTLVGTLYDEHDRRRDAGFSIF</span><span class="topo-membrane">VFGINLGAFIAPLIV</span><span class="topo-outside">GAAQEAAGYHVAF</span><span class="topo-membrane">SLAAIGMFIGLLVYYF</span><span class="topo-inside">GGKKTLDPHYLRPTDPLAPEEVKPLLVKV</span><span class="topo-membrane">SLAVAGFIAIIVVMNL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">V</span><span class="topo-outside">GWNSLPA</span><span class="topo-membrane">YINLLTIVAIAIPVF</span><span class="topo-inside">YFAWMI</span><span class="topo-unknown">SSVKVTSTEHLR</span><span class="topo-inside">VVSYIP</span><span class="topo-membrane">LFIAAVLFWAIEEQGSV</span><span class="topo-outside">VLATFAAERVDSSWFPVSWF</span><span class="topo-membrane">QSLNPLFIMLYTPFF</span><span class="topo-inside">AWLWTAWKKN</span><span class="topo-unknown">QPS</span><span class="topo-inside">SPTKF</span><span class="topo-membrane">AVG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LMFAGLSFLL</span><span class="topo-outside">MAIPGALYGTSGKVSPLWLV</span><span class="topo-membrane">GSWALVILGEMLIS</span><span class="topo-inside">PVGLSVTTKLAPKAFNSQMMSMWF</span><span class="topo-membrane">LSSSVGSALNAQLV</span><span class="topo-outside">TLYNAKSEVAYFS</span><span class="topo-membrane">YFGLGSVVLGIVLVF</span><span class="topo-inside">L</span><span class="topo-unknown">SKRIQGLMQ</span></span>
<span class="topo-ruler">       490 </span>
<span class="topo-line"><span class="topo-unknown">GVEGSENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (35 regions)</summary>
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
      <td>10</td>
      <td>1</td>
      <td>10</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>17</td>
      <td>11</td>
      <td>17</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>34</td>
      <td>18</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>58</td>
      <td>35</td>
      <td>58</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>74</td>
      <td>59</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>87</td>
      <td>75</td>
      <td>87</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>101</td>
      <td>88</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>112</td>
      <td>102</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>127</td>
      <td>113</td>
      <td>127</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>128</td>
      <td>151</td>
      <td>128</td>
      <td>151</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>166</td>
      <td>152</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>179</td>
      <td>167</td>
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
      <td>224</td>
      <td>196</td>
      <td>224</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>225</td>
      <td>241</td>
      <td>225</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>242</td>
      <td>248</td>
      <td>242</td>
      <td>248</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>263</td>
      <td>249</td>
      <td>263</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>264</td>
      <td>269</td>
      <td>264</td>
      <td>269</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>270</td>
      <td>281</td>
      <td>270</td>
      <td>281</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>282</td>
      <td>287</td>
      <td>282</td>
      <td>287</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>304</td>
      <td>288</td>
      <td>304</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>305</td>
      <td>324</td>
      <td>305</td>
      <td>324</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>325</td>
      <td>339</td>
      <td>325</td>
      <td>339</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>340</td>
      <td>349</td>
      <td>340</td>
      <td>349</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>350</td>
      <td>352</td>
      <td>350</td>
      <td>352</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>353</td>
      <td>357</td>
      <td>353</td>
      <td>357</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>358</td>
      <td>370</td>
      <td>358</td>
      <td>370</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>371</td>
      <td>390</td>
      <td>371</td>
      <td>390</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>391</td>
      <td>404</td>
      <td>391</td>
      <td>404</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>405</td>
      <td>428</td>
      <td>405</td>
      <td>428</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>429</td>
      <td>442</td>
      <td>429</td>
      <td>442</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>443</td>
      <td>455</td>
      <td>443</td>
      <td>455</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>456</td>
      <td>470</td>
      <td>456</td>
      <td>470</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>471</td>
      <td>471</td>
      <td>471</td>
      <td>471</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>491</td>
      <td>472</td>
      <td>491</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4d2b">4D2B</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEDKG</span><span class="topo-inside">KTFFGQPLGLSTLF</span><span class="topo-membrane">MTEMWERFSYYGMRA</span><span class="topo-outside">ILLYYMWFLISTGDLHITRATAAS</span><span class="topo-membrane">IMAIYASMVYLSGTIG</span><span class="topo-inside">GFVADRIIGARPAV</span><span class="topo-membrane">FWGGVLIMLGHIVLAL</span><span class="topo-outside">PFGASA</span><span class="topo-membrane">LFGSIILIII</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GTGFLKP</span><span class="topo-inside">NVSTLVGTLYDEHDRRRDAGFSI</span><span class="topo-membrane">FVFGINLGAFIAPLIV</span><span class="topo-outside">GAAQEAAGYHVA</span><span class="topo-membrane">FSLAAIGMFIGLLVY</span><span class="topo-inside">YFGGKKTLDPHYLRPTDPLAPEEVKPLLVKV</span><span class="topo-membrane">SLAVAGFIAIIVVMNL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">VGWNSLPA</span><span class="topo-membrane">YINLLTIVAIAIPVFYFA</span><span class="topo-inside">WMIS</span><span class="topo-unknown">SVKVTSTEH</span><span class="topo-inside">LRVVSY</span><span class="topo-membrane">IPLFIAAVLFWAIEEQGSV</span><span class="topo-outside">VLATFAAERVDSSWFPVSW</span><span class="topo-membrane">FQSLNPLFIMLYTPFFAWL</span><span class="topo-inside">WTA</span><span class="topo-unknown">WKK</span><span class="topo-inside">NQPSS</span><span class="topo-membrane">PTKFAVG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LMFAGLSFL</span><span class="topo-outside">LMAIPGALYGTSGKVSPLWLV</span><span class="topo-membrane">GSWALVILGEMLISPVG</span><span class="topo-inside">LSVTT</span><span class="topo-unknown">KLAPKAFNSQ</span><span class="topo-inside">MMSM</span><span class="topo-membrane">WFLSSSVGSALNAQL</span><span class="topo-outside">VTLYNAKSEVAYFSYF</span><span class="topo-membrane">GLGSVVLGIVLVFLS</span><span class="topo-unknown">KRIQGLMQ</span></span>
<span class="topo-ruler">       490 </span>
<span class="topo-line"><span class="topo-unknown">GVEGSENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (36 regions)</summary>
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
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>19</td>
      <td>6</td>
      <td>19</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>34</td>
      <td>20</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>58</td>
      <td>35</td>
      <td>58</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>74</td>
      <td>59</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>88</td>
      <td>75</td>
      <td>88</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>104</td>
      <td>89</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>110</td>
      <td>105</td>
      <td>110</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>111</td>
      <td>127</td>
      <td>111</td>
      <td>127</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>128</td>
      <td>150</td>
      <td>128</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>166</td>
      <td>151</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>178</td>
      <td>167</td>
      <td>178</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>193</td>
      <td>179</td>
      <td>193</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>194</td>
      <td>224</td>
      <td>194</td>
      <td>224</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>225</td>
      <td>240</td>
      <td>225</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>248</td>
      <td>241</td>
      <td>248</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>266</td>
      <td>249</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>270</td>
      <td>267</td>
      <td>270</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>271</td>
      <td>279</td>
      <td>271</td>
      <td>279</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>280</td>
      <td>285</td>
      <td>280</td>
      <td>285</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>304</td>
      <td>286</td>
      <td>304</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>305</td>
      <td>323</td>
      <td>305</td>
      <td>323</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>324</td>
      <td>342</td>
      <td>324</td>
      <td>342</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>343</td>
      <td>345</td>
      <td>343</td>
      <td>345</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>346</td>
      <td>348</td>
      <td>346</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>349</td>
      <td>353</td>
      <td>349</td>
      <td>353</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>354</td>
      <td>369</td>
      <td>354</td>
      <td>369</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>370</td>
      <td>390</td>
      <td>370</td>
      <td>390</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>391</td>
      <td>407</td>
      <td>391</td>
      <td>407</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>408</td>
      <td>412</td>
      <td>408</td>
      <td>412</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>413</td>
      <td>422</td>
      <td>413</td>
      <td>422</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>423</td>
      <td>426</td>
      <td>423</td>
      <td>426</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>427</td>
      <td>441</td>
      <td>427</td>
      <td>441</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>442</td>
      <td>457</td>
      <td>442</td>
      <td>457</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>458</td>
      <td>472</td>
      <td>458</td>
      <td>472</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>473</td>
      <td>491</td>
      <td>473</td>
      <td>491</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4d2d">4D2D</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEDKG</span><span class="topo-inside">KTFFGQPLGL</span><span class="topo-membrane">STLFMTEMWERFSYYGMRAILL</span><span class="topo-outside">YYMWFLISTGDLHITRATA</span><span class="topo-membrane">ASIMAIYASMVYLSGTIGGFVA</span><span class="topo-inside">DRIIGA</span><span class="topo-membrane">RPAVFWGGVLIMLGHIVLAL</span><span class="topo-outside">PFGAS</span><span class="topo-membrane">ALFGSIILIII</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GTGFLKPNVS</span><span class="topo-inside">TLVGTLYDEHDRRRDAGF</span><span class="topo-membrane">SIFVFGINLGAFIAPLIVGAA</span><span class="topo-outside">QEAAGYH</span><span class="topo-membrane">VAFSLAAIGMFIGLLVYYFGG</span><span class="topo-inside">KKTLDPHYLRPTDPLAPEEVKP</span><span class="topo-membrane">LLVKVSLAVAGFIAIIVVMNL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">V</span><span class="topo-outside">GWNSL</span><span class="topo-membrane">PAYINLLTIVAIAIPVFYFAW</span><span class="topo-inside">MISS</span><span class="topo-unknown">VKVT</span><span class="topo-inside">STEHLRV</span><span class="topo-membrane">VSYIPLFIAAVLFWAIEEQGSVVLA</span><span class="topo-outside">TFAAERVDSSWFPV</span><span class="topo-membrane">SWFQSLNPLFIMLYTPFFA</span><span class="topo-inside">WLWTAWKKNQPSS</span><span class="topo-membrane">PTKFAVG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LMFAGLSFLLMAI</span><span class="topo-outside">PGALYGTSGKVS</span><span class="topo-membrane">PLWLVGSWALVILGEMLISPVGL</span><span class="topo-inside">SVTTK</span><span class="topo-unknown">LAPKAF</span><span class="topo-inside">NSQMM</span><span class="topo-membrane">SMWFLSSSVGSALNAQLV</span><span class="topo-outside">TLYNAKSEVA</span><span class="topo-membrane">YFSYFGLGSVVLGIVLVFLS</span><span class="topo-inside">KRIQGL</span><span class="topo-unknown">MQ</span></span>
<span class="topo-ruler">       490 </span>
<span class="topo-line"><span class="topo-unknown">GVEGSENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (35 regions)</summary>
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
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>15</td>
      <td>6</td>
      <td>15</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>37</td>
      <td>16</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>56</td>
      <td>38</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>78</td>
      <td>57</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>84</td>
      <td>79</td>
      <td>84</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>104</td>
      <td>85</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>109</td>
      <td>105</td>
      <td>109</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>130</td>
      <td>110</td>
      <td>130</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>131</td>
      <td>148</td>
      <td>131</td>
      <td>148</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>169</td>
      <td>149</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>176</td>
      <td>170</td>
      <td>176</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>197</td>
      <td>177</td>
      <td>197</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>219</td>
      <td>198</td>
      <td>219</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>241</td>
      <td>220</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>242</td>
      <td>246</td>
      <td>242</td>
      <td>246</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>247</td>
      <td>267</td>
      <td>247</td>
      <td>267</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>268</td>
      <td>271</td>
      <td>268</td>
      <td>271</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>272</td>
      <td>275</td>
      <td>272</td>
      <td>275</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>276</td>
      <td>282</td>
      <td>276</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>307</td>
      <td>283</td>
      <td>307</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>308</td>
      <td>321</td>
      <td>308</td>
      <td>321</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>322</td>
      <td>340</td>
      <td>322</td>
      <td>340</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>341</td>
      <td>353</td>
      <td>341</td>
      <td>353</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>354</td>
      <td>373</td>
      <td>354</td>
      <td>373</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>385</td>
      <td>374</td>
      <td>385</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>386</td>
      <td>408</td>
      <td>386</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>413</td>
      <td>409</td>
      <td>413</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>414</td>
      <td>419</td>
      <td>414</td>
      <td>419</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>420</td>
      <td>424</td>
      <td>420</td>
      <td>424</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>425</td>
      <td>442</td>
      <td>425</td>
      <td>442</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>443</td>
      <td>452</td>
      <td>443</td>
      <td>452</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>453</td>
      <td>472</td>
      <td>453</td>
      <td>472</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>473</td>
      <td>478</td>
      <td>473</td>
      <td>478</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>479</td>
      <td>491</td>
      <td>479</td>
      <td>491</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5d58">5D58</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEDK</span><span class="topo-inside">GKTFFGQPLGLSTLF</span><span class="topo-membrane">MTEMWERFSYYGMRAIL</span><span class="topo-outside">LYYMWFLISTGDLHITRATAAS</span><span class="topo-membrane">IMAIYASMVYLSGTIG</span><span class="topo-inside">GFVADRIIGARPA</span><span class="topo-membrane">VFWGGVLIMLGHIVLA</span><span class="topo-outside">LPFGASA</span><span class="topo-membrane">LFGSIILIII</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GTGFLKP</span><span class="topo-inside">NVSTLVGTLYDEHDRRRDAGFSIF</span><span class="topo-membrane">VFGINLGAFIAPLIVG</span><span class="topo-outside">AAQEAAGYHVA</span><span class="topo-membrane">FSLAAIGMFIGLLVYY</span><span class="topo-inside">FGGKKTLDPHYLRPTDPLAPEEVKPLLV</span><span class="topo-membrane">KVSLAVAGFIAIIVVMN</span><span class="topo-outside">L</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">VGWNSLPA</span><span class="topo-membrane">YINLLTIVAIAIPVFYFA</span><span class="topo-inside">WMI</span><span class="topo-unknown">SSVKV</span><span class="topo-inside">TSTEHLRVVSYI</span><span class="topo-membrane">PLFIAAVLFWAIEEQGSVVLA</span><span class="topo-outside">TFAAERVDSSWFPVS</span><span class="topo-membrane">WFQSLNPLFIMLYTPFF</span><span class="topo-inside">AWLWTAWKKNQPSSPT</span><span class="topo-membrane">KFAVG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LMFAGLSFLLM</span><span class="topo-outside">AIPGALYGTSGKVSPL</span><span class="topo-membrane">WLVGSWALVILGEMLIS</span><span class="topo-unknown">PVGLSVTTKLAPKAFNSQ</span><span class="topo-inside">MMS</span><span class="topo-membrane">MWFLSSSVGSALNAQLV</span><span class="topo-outside">TLYNAKSEVAYF</span><span class="topo-membrane">SYFGLGSVVLGIVLVFL</span><span class="topo-inside">SKRI</span><span class="topo-unknown">QGLMQ</span></span>
<span class="topo-ruler">   </span>
<span class="topo-line"><span class="topo-unknown">GVE</span></span>
<details class="topo-details"><summary>Topology coordinates (30 regions)</summary>
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
      <td>19</td>
      <td>5</td>
      <td>19</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>36</td>
      <td>20</td>
      <td>36</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>37</td>
      <td>58</td>
      <td>37</td>
      <td>58</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>74</td>
      <td>59</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>87</td>
      <td>75</td>
      <td>87</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>103</td>
      <td>88</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>104</td>
      <td>110</td>
      <td>104</td>
      <td>110</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>111</td>
      <td>127</td>
      <td>111</td>
      <td>127</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>128</td>
      <td>151</td>
      <td>128</td>
      <td>151</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>167</td>
      <td>152</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>168</td>
      <td>178</td>
      <td>168</td>
      <td>178</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>194</td>
      <td>179</td>
      <td>194</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>195</td>
      <td>222</td>
      <td>195</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>239</td>
      <td>223</td>
      <td>239</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>240</td>
      <td>248</td>
      <td>240</td>
      <td>248</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>266</td>
      <td>249</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>269</td>
      <td>267</td>
      <td>269</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>286</td>
      <td>275</td>
      <td>286</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>307</td>
      <td>287</td>
      <td>307</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>308</td>
      <td>322</td>
      <td>308</td>
      <td>322</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>339</td>
      <td>323</td>
      <td>339</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>340</td>
      <td>355</td>
      <td>340</td>
      <td>355</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>356</td>
      <td>371</td>
      <td>356</td>
      <td>371</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>372</td>
      <td>387</td>
      <td>372</td>
      <td>387</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>388</td>
      <td>404</td>
      <td>388</td>
      <td>404</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>423</td>
      <td>425</td>
      <td>423</td>
      <td>425</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>426</td>
      <td>442</td>
      <td>426</td>
      <td>442</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>443</td>
      <td>454</td>
      <td>443</td>
      <td>454</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>455</td>
      <td>471</td>
      <td>455</td>
      <td>471</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>472</td>
      <td>475</td>
      <td>472</td>
      <td>475</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5d59">5D59</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEDK</span><span class="topo-inside">GKTFFGQPLGLSTL</span><span class="topo-membrane">FMTEMWERFSYYGMRAIL</span><span class="topo-outside">LYYMWFLISTGDLHITRATAAS</span><span class="topo-membrane">IMAIYASMVYLSGTIG</span><span class="topo-inside">GFVADRIIGARP</span><span class="topo-membrane">AVFWGGVLIMLGHIVLA</span><span class="topo-outside">LPFGASAL</span><span class="topo-membrane">FGSIILIII</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GTGFLKP</span><span class="topo-inside">NVSTLVGTLYDEHDRRRDAGFSIF</span><span class="topo-membrane">VFGINLGAFIAPLIVG</span><span class="topo-outside">AAQEAAGYHVA</span><span class="topo-membrane">FSLAAIGMFIGLLVYYF</span><span class="topo-inside">GGKKTLDPHYLRPTDPLAPEEVKPLL</span><span class="topo-membrane">VKVSLAVAGFIAIIVVM</span><span class="topo-outside">NL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">VGWNSLPA</span><span class="topo-membrane">YINLLTIVAIAIPVFYFA</span><span class="topo-inside">WMI</span><span class="topo-unknown">SSVKV</span><span class="topo-inside">TSTEHLRVVSYI</span><span class="topo-membrane">PLFIAAVLFWAIEEQGSVVLA</span><span class="topo-outside">TFAAERVDSSWFPVS</span><span class="topo-membrane">WFQSLNPLFIMLYTPFF</span><span class="topo-inside">AWLWTAWKKNQPSSPT</span><span class="topo-membrane">KFAVG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LMFAGLSFLLM</span><span class="topo-outside">AIPGALYGTSGKVSPL</span><span class="topo-membrane">WLVGSWALVILGEMLIS</span><span class="topo-unknown">PVGLSVTTKLAPKAFNSQ</span><span class="topo-inside">MMS</span><span class="topo-membrane">MWFLSSSVGSALNAQLV</span><span class="topo-outside">TLYNAKSEVAYF</span><span class="topo-membrane">SYFGLGSVVLGIVLVFL</span><span class="topo-inside">SKRI</span><span class="topo-unknown">QGLMQ</span></span>
<span class="topo-ruler">   </span>
<span class="topo-line"><span class="topo-unknown">GVE</span></span>
<details class="topo-details"><summary>Topology coordinates (30 regions)</summary>
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
      <td>18</td>
      <td>5</td>
      <td>18</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>36</td>
      <td>19</td>
      <td>36</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>37</td>
      <td>58</td>
      <td>37</td>
      <td>58</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>74</td>
      <td>59</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>86</td>
      <td>75</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>103</td>
      <td>87</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>104</td>
      <td>111</td>
      <td>104</td>
      <td>111</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>127</td>
      <td>112</td>
      <td>127</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>128</td>
      <td>151</td>
      <td>128</td>
      <td>151</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>167</td>
      <td>152</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>168</td>
      <td>178</td>
      <td>168</td>
      <td>178</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>195</td>
      <td>179</td>
      <td>195</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>221</td>
      <td>196</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>238</td>
      <td>222</td>
      <td>238</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>248</td>
      <td>239</td>
      <td>248</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>266</td>
      <td>249</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>269</td>
      <td>267</td>
      <td>269</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>286</td>
      <td>275</td>
      <td>286</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>307</td>
      <td>287</td>
      <td>307</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>308</td>
      <td>322</td>
      <td>308</td>
      <td>322</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>339</td>
      <td>323</td>
      <td>339</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>340</td>
      <td>355</td>
      <td>340</td>
      <td>355</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>356</td>
      <td>371</td>
      <td>356</td>
      <td>371</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>372</td>
      <td>387</td>
      <td>372</td>
      <td>387</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>388</td>
      <td>404</td>
      <td>388</td>
      <td>404</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>423</td>
      <td>425</td>
      <td>423</td>
      <td>425</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>426</td>
      <td>442</td>
      <td>426</td>
      <td>442</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>443</td>
      <td>454</td>
      <td>443</td>
      <td>454</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>455</td>
      <td>471</td>
      <td>455</td>
      <td>471</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>472</td>
      <td>475</td>
      <td>472</td>
      <td>475</td>
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

### MFS transporter with 14 transmembrane helices

PepTSt contains 14 transmembrane helices in total. TM1-TM6 form the N-terminal MFS domain (N-domain), TM7-TM12 form the C-terminal MFS domain (C-domain), and the last two helices (TM-A and TM-B) are found in the linker region between the two domains, adopting a V-shaped arrangement. This architecture is characteristic of bacterial PepT/POT transporters.

### P3_121 crystal form revealed monomeric inward facing state

The P3_121 crystal form of PepTSt (PDB 5MMT) was crystallized in NM detergent, which disrupts the dimeric form observed in longer-chain detergents like DDM and LMNG. The protein adopts an inward facing conformation where lobe TM10-TM11 is markedly bent toward the central pore, likely occluding the binding site. The extent of occlusion could not be determined due to disorder at the apex of the lobe. The structure reveals a monomeric state, important for future spectroscopic studies where dimeric forms would complicate data interpretation.

### A-motif and TM-A/TM-B functional roles

The A-motif in PepTSt (found in loop TM2-TM3) differs from the consensus MFS sequence by having an extra residue inserted prior to the second conserved glycine and often missing one or more basic residues. The salt bridge normally found between the second basic residue and the acidic residue in TM4 is absent in PepTSt, suggesting that regulated bending of TM4 may not take place in this transporter. Instead, bending of lobe TM10-TM11 appears to be the primary mechanism for forming the inward facing occluded state, possibly in combination with domain rotation and changes in TM4-TM5 and TM-A/TM-B.

### Crystal packing and diffraction anisotropy

The P3_121 and P2_12_12_1 crystal forms both exhibit ordered end-to-end packing through periplasmic-periplasmic and cytoplasmic-cytoplasmic interactions, with a complete lack of ordered lateral contacts. This manifests as severe diffraction anisotropy, with the directions of reflection intensity falloff correlating with directions where ordered packing interactions are missing. The C222_1 form, crystallized in meso, encompasses tight lateral interactions and diffracted to much better resolution (2.3 A isotropic).


## Cross-References

- <a href="/xray-mp-wiki/concepts/protein-families/mfs-transporter/">Major Facilitator Superfamily (MFS)</a> — PepTSt is a member of the MFS transporter family
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/conformational-dynamics-mfs/">Conformational Dynamics in MFS Transporters</a> — PepTSt exhibits inward facing conformations relevant to MFS transport dynamics
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/inward-facing-occluded-mfs-state/">Inward Facing Occluded State in MFS Transporters</a> — The P3_121 form represents a potential inward facing occluded state
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/rocker-switch-mechanism/">Rocker-Switch Mechanism</a> — Canonical transport mechanism for MFS transporters
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/cork-in-bottle-occlusion/">Cork-in-Bottle Occlusion</a> — Alternative occlusion mechanism for membrane transporters
