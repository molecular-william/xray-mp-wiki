---
title: "PepT_So2 Oligopeptide Transporter"
created: 2026-06-02
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##embor.2013.107, doi/10.1038##nsmb.2860]
verified: false
---

# PepT_So2 Oligopeptide Transporter

## Overview

PepT_So2 is a proton-dependent oligopeptide transporter from Shewanella oneidensis. It belongs to the POT (proton-dependent oligopeptide transporter) family, a subgroup of the Major Facilitator Superfamily ([MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/)). PepT_So2 uses a proton gradient to drive the uptake of di- and tri-peptides. The crystal structure reveals an inward open conformation with a central hydrophilic peptide-binding cavity and the first substrate-bound POT structure characterized. PepT_So2 uniquely forms a tetrameric assembly in detergent solution, distinguishing it from other POT family members.


## Publications

### doi/10.1038##embor.2013.107

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4lep">4LEP</a></td>
      <td>3.2 A</td>
      <td>P2_1 2_1 2_1</td>
      <td>Full-length PepT_So2 from Shewanella oneidensis, wild-type, inward open conformation, co-crystallized with <a href="/xray-mp-wiki/reagents/ligands/alafosfalin/">Alafosfalin</a></td>
      <td><a href="/xray-mp-wiki/reagents/ligands/alafosfalin/">Alafosfalin</a> (peptidomimetic phosphonodipeptide)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4lep">4LEP</a></td>
      <td>4.6 A</td>
      <td>P3_1 2 1</td>
      <td>Full-length PepT_So2 from Shewanella oneidensis, wild-type, tetrameric assembly</td>
      <td>none (crystal form without zinc, showing tetrameric arrangement)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length PepT_So2 from Shewanella oneidensis (Q8EHE6), C-terminal His-tag with tobacco etch virus (TEV) cleavage site, cloned into pNIC-CTHF-vector

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
      <td>Cell lysis and membrane fractionation</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Full-length PepT_So2 expressed in E. coli with C-terminal His-tag</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA</td>
      <td>-- + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>His-tag purification with TEV cleavage site for tag removal</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>-- + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Tetrameric state confirmed by analytical gel filtration and Blue Native PAGE</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>vapor diffusion, sitting drop</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Native crystals grew in 40% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 300, 0.1 M phosphate <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> pH 4.5, 0.12 M ZnCl2 and 3% trimethylamine N-oxide dehydrate pH 11 at 20 C. Crystals appeared after 21 days with dimensions of approximately 100 x 50 x 10 um. PepT_So2 was incubated with 50 mM <a href="/xray-mp-wiki/reagents/ligands/alafosfalin/">Alafosfalin</a> for 30 min at 4 C before crystallization. Seleno-<a href="/xray-mp-wiki/reagents/ligands/l-methionine/">L-Methionine</a> crystals grew in 38% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 300, 0.1 M phosphate <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> pH 5.2 and 0.01 M ZnCl2. P3_1 2_1 crystal form grew in 0.1 M citric acid pH 4.2, 0.1 M sodium hydrogen phosphate and 40% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 300.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4lep">4LEP</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTLGTNQV</span><span class="topo-inside">SKTHSFMTVS</span><span class="topo-membrane">LIELWERFGYYGMQA</span><span class="topo-outside">LIVYFMVQRLGFDDSRANLVW</span><span class="topo-membrane">SACAALIYVSPAIGG</span><span class="topo-inside">WVGDKILGTKRT</span><span class="topo-membrane">MLLGAGILSVGYAL</span><span class="topo-outside">MTVPTENTWFMFS</span><span class="topo-membrane">ALGVIVVGNGLF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KP</span><span class="topo-inside">NAGNLVRKIYEGDDSKIDSAFTIY</span><span class="topo-membrane">YMAVNVGSTFSMLLT</span><span class="topo-outside">PWIKDYVNAQYGNEFGWHAAF</span><span class="topo-membrane">AVCCVGILVGLGNYAL</span><span class="topo-inside">MHKSLANYG</span><span class="topo-unknown">SEPDTRP</span><span class="topo-inside">VNKKSL</span><span class="topo-membrane">AIVLALAALSVVASAIIL</span><span class="topo-outside">EY</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">EDV</span><span class="topo-membrane">ARVFVYAAGVAVLGIFFH</span><span class="topo-inside">LIR</span><span class="topo-unknown">TSE</span><span class="topo-inside">PSERAGLIAA</span><span class="topo-membrane">LILTVQTVFFFIFYQQMS</span><span class="topo-outside">TSLALFALRNVDWDF</span><span class="topo-unknown">QVFGTHL</span><span class="topo-outside">WTWSPAQ</span><span class="topo-membrane">FQALNPIWIMVLSPVL</span><span class="topo-inside">AWSYSW</span><span class="topo-unknown">AGRNNK</span><span class="topo-inside">DFSIAA</span><span class="topo-membrane">KF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">ALGFAVVAIGFFI</span><span class="topo-outside">YGFAGQFAVNGKTSSWVM</span><span class="topo-membrane">IWGYASYSLGELLVS</span><span class="topo-inside">GLGLAMIARY</span><span class="topo-unknown">VPARMG</span><span class="topo-inside">GFMMG</span><span class="topo-membrane">AYFVASGISQYLGG</span><span class="topo-outside">VVANFASVPQDLVDPLQTLPVYTNLFNKL</span><span class="topo-membrane">GVAAVVCTII</span></span>
<span class="topo-ruler">       490       500       510       520   </span>
<span class="topo-line"><span class="topo-membrane">ALAV</span><span class="topo-inside">LPLMRRLT</span><span class="topo-unknown">ESHHAHSSIENNAAASLRDVKAEQAENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (41 regions)</summary>
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
      <td>18</td>
      <td>9</td>
      <td>18</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>33</td>
      <td>19</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>54</td>
      <td>34</td>
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
      <td>81</td>
      <td>70</td>
      <td>81</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>95</td>
      <td>82</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>96</td>
      <td>108</td>
      <td>96</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>122</td>
      <td>109</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>146</td>
      <td>123</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>161</td>
      <td>147</td>
      <td>161</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>162</td>
      <td>182</td>
      <td>162</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>198</td>
      <td>183</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>207</td>
      <td>199</td>
      <td>207</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>214</td>
      <td>208</td>
      <td>214</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>215</td>
      <td>220</td>
      <td>215</td>
      <td>220</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>238</td>
      <td>221</td>
      <td>238</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>243</td>
      <td>239</td>
      <td>243</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>261</td>
      <td>244</td>
      <td>261</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>264</td>
      <td>262</td>
      <td>264</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>265</td>
      <td>267</td>
      <td>265</td>
      <td>267</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>268</td>
      <td>277</td>
      <td>268</td>
      <td>277</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>295</td>
      <td>278</td>
      <td>295</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>296</td>
      <td>310</td>
      <td>296</td>
      <td>310</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>317</td>
      <td>311</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>318</td>
      <td>324</td>
      <td>318</td>
      <td>324</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>325</td>
      <td>340</td>
      <td>325</td>
      <td>340</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>341</td>
      <td>346</td>
      <td>341</td>
      <td>346</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>347</td>
      <td>352</td>
      <td>347</td>
      <td>352</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>353</td>
      <td>358</td>
      <td>353</td>
      <td>358</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>359</td>
      <td>373</td>
      <td>359</td>
      <td>373</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>391</td>
      <td>374</td>
      <td>391</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>392</td>
      <td>406</td>
      <td>392</td>
      <td>406</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>407</td>
      <td>416</td>
      <td>407</td>
      <td>416</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>417</td>
      <td>422</td>
      <td>417</td>
      <td>422</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>423</td>
      <td>427</td>
      <td>423</td>
      <td>427</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>428</td>
      <td>441</td>
      <td>428</td>
      <td>441</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>442</td>
      <td>470</td>
      <td>442</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>484</td>
      <td>471</td>
      <td>484</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>485</td>
      <td>492</td>
      <td>485</td>
      <td>492</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>493</td>
      <td>523</td>
      <td>493</td>
      <td>523</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4lep">4LEP</a> — Chain B (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTLGTNQVS</span><span class="topo-inside">KTHSFMTVS</span><span class="topo-membrane">LIELWERFGYYGMQA</span><span class="topo-outside">LIVYFMVQRLGFDDSRANLVW</span><span class="topo-membrane">SACAALIYVSPAIGG</span><span class="topo-inside">WVGDKILGTKRT</span><span class="topo-membrane">MLLGAGILSVGYALM</span><span class="topo-outside">TVPTENTWFMFS</span><span class="topo-membrane">ALGVIVVGNGLF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KP</span><span class="topo-inside">NAGNLVRKIYEGDDSKIDSAFTIY</span><span class="topo-membrane">YMAVNVGSTFSMLLT</span><span class="topo-outside">PWIKDYVNAQYGNEFGWHAAF</span><span class="topo-membrane">AVCCVGILVGLGNYAL</span><span class="topo-inside">MHKSLANYGS</span><span class="topo-unknown">EPDTR</span><span class="topo-inside">PVNKKSL</span><span class="topo-membrane">AIVLALAALSVVASAIIL</span><span class="topo-outside">EY</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">EDV</span><span class="topo-membrane">ARVFVYAAGVAVLGIFFH</span><span class="topo-inside">LIRT</span><span class="topo-unknown">SE</span><span class="topo-inside">PSERAGLIAA</span><span class="topo-membrane">LILTVQTVFFFIFYQQMS</span><span class="topo-outside">TSLALFALRNVDWDF</span><span class="topo-unknown">QVFGTH</span><span class="topo-outside">LWTWSPAQ</span><span class="topo-membrane">FQALNPIWIMVLSPVL</span><span class="topo-inside">AWS</span><span class="topo-unknown">YSWAGRNNKDF</span><span class="topo-inside">SIAA</span><span class="topo-membrane">KF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">ALGFAVVAIGFFI</span><span class="topo-outside">YGFAGQFAVNGKTSSWVMI</span><span class="topo-membrane">WGYASYSLGELLVSGL</span><span class="topo-inside">GLAMIAR</span><span class="topo-unknown">YVPARM</span><span class="topo-inside">GGFMMG</span><span class="topo-membrane">AYFVASGISQYLGG</span><span class="topo-outside">VVANFASVPQDLVDPLQTLPVYTNLFNKL</span><span class="topo-membrane">GVAAVVCTII</span></span>
<span class="topo-ruler">       490       500       510       520   </span>
<span class="topo-line"><span class="topo-membrane">ALAV</span><span class="topo-inside">LPLMRRL</span><span class="topo-unknown">TESHHAHSSIENNAAASLRDVKAEQAENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (41 regions)</summary>
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
      <td>9</td>
      <td>1</td>
      <td>9</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>18</td>
      <td>10</td>
      <td>18</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>33</td>
      <td>19</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>54</td>
      <td>34</td>
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
      <td>81</td>
      <td>70</td>
      <td>81</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>96</td>
      <td>82</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>108</td>
      <td>97</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>122</td>
      <td>109</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>146</td>
      <td>123</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>161</td>
      <td>147</td>
      <td>161</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>162</td>
      <td>182</td>
      <td>162</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>198</td>
      <td>183</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>208</td>
      <td>199</td>
      <td>208</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>209</td>
      <td>213</td>
      <td>209</td>
      <td>213</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>214</td>
      <td>220</td>
      <td>214</td>
      <td>220</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>238</td>
      <td>221</td>
      <td>238</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>243</td>
      <td>239</td>
      <td>243</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>261</td>
      <td>244</td>
      <td>261</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>265</td>
      <td>262</td>
      <td>265</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>266</td>
      <td>267</td>
      <td>266</td>
      <td>267</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>268</td>
      <td>277</td>
      <td>268</td>
      <td>277</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>295</td>
      <td>278</td>
      <td>295</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>296</td>
      <td>310</td>
      <td>296</td>
      <td>310</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>316</td>
      <td>311</td>
      <td>316</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>317</td>
      <td>324</td>
      <td>317</td>
      <td>324</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>325</td>
      <td>340</td>
      <td>325</td>
      <td>340</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>341</td>
      <td>343</td>
      <td>341</td>
      <td>343</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>354</td>
      <td>344</td>
      <td>354</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>355</td>
      <td>358</td>
      <td>355</td>
      <td>358</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>359</td>
      <td>373</td>
      <td>359</td>
      <td>373</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>392</td>
      <td>374</td>
      <td>392</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>393</td>
      <td>408</td>
      <td>393</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>415</td>
      <td>409</td>
      <td>415</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>416</td>
      <td>421</td>
      <td>416</td>
      <td>421</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>422</td>
      <td>427</td>
      <td>422</td>
      <td>427</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>428</td>
      <td>441</td>
      <td>428</td>
      <td>441</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>442</td>
      <td>470</td>
      <td>442</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>484</td>
      <td>471</td>
      <td>484</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>485</td>
      <td>491</td>
      <td>485</td>
      <td>491</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>492</td>
      <td>523</td>
      <td>492</td>
      <td>523</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4lep">4LEP</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTLGTNQV</span><span class="topo-inside">SKTHSFMTVS</span><span class="topo-membrane">LIELWERFGYYGMQA</span><span class="topo-outside">LIVYFMVQRLGFDDSRANLVW</span><span class="topo-membrane">SACAALIYVSPAIGG</span><span class="topo-inside">WVGDKILGTKRT</span><span class="topo-membrane">MLLGAGILSVGYAL</span><span class="topo-outside">MTVPTENTWFMFS</span><span class="topo-membrane">ALGVIVVGNGLF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KP</span><span class="topo-inside">NAGNLVRKIYEGDDSKIDSAFTIY</span><span class="topo-membrane">YMAVNVGSTFSMLLT</span><span class="topo-outside">PWIKDYVNAQYGNEFGWHAAF</span><span class="topo-membrane">AVCCVGILVGLGNYAL</span><span class="topo-inside">MHKSLANYG</span><span class="topo-unknown">SEPDTRP</span><span class="topo-inside">VNKKSL</span><span class="topo-membrane">AIVLALAALSVVASAIIL</span><span class="topo-outside">EY</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">EDV</span><span class="topo-membrane">ARVFVYAAGVAVLGIFFH</span><span class="topo-inside">LIR</span><span class="topo-unknown">TSE</span><span class="topo-inside">PSERAGLIAA</span><span class="topo-membrane">LILTVQTVFFFIFYQQMS</span><span class="topo-outside">TSLALFALRNVDWDF</span><span class="topo-unknown">QVFGTHL</span><span class="topo-outside">WTWSPAQ</span><span class="topo-membrane">FQALNPIWIMVLSPVL</span><span class="topo-inside">AWSYSW</span><span class="topo-unknown">AGRNNK</span><span class="topo-inside">DFSIAA</span><span class="topo-membrane">KF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">ALGFAVVAIGFFI</span><span class="topo-outside">YGFAGQFAVNGKTSSWVM</span><span class="topo-membrane">IWGYASYSLGELLVS</span><span class="topo-inside">GLGLAMIARY</span><span class="topo-unknown">VPARMG</span><span class="topo-inside">GFMMG</span><span class="topo-membrane">AYFVASGISQYLGG</span><span class="topo-outside">VVANFASVPQDLVDPLQTLPVYTNLFNKL</span><span class="topo-membrane">GVAAVVCTII</span></span>
<span class="topo-ruler">       490       500       510       520   </span>
<span class="topo-line"><span class="topo-membrane">ALAV</span><span class="topo-inside">LPLMRRLT</span><span class="topo-unknown">ESHHAHSSIENNAAASLRDVKAEQAENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (41 regions)</summary>
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
      <td>18</td>
      <td>9</td>
      <td>18</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>33</td>
      <td>19</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>54</td>
      <td>34</td>
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
      <td>81</td>
      <td>70</td>
      <td>81</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>95</td>
      <td>82</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>96</td>
      <td>108</td>
      <td>96</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>122</td>
      <td>109</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>146</td>
      <td>123</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>161</td>
      <td>147</td>
      <td>161</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>162</td>
      <td>182</td>
      <td>162</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>198</td>
      <td>183</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>207</td>
      <td>199</td>
      <td>207</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>214</td>
      <td>208</td>
      <td>214</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>215</td>
      <td>220</td>
      <td>215</td>
      <td>220</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>238</td>
      <td>221</td>
      <td>238</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>243</td>
      <td>239</td>
      <td>243</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>261</td>
      <td>244</td>
      <td>261</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>264</td>
      <td>262</td>
      <td>264</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>265</td>
      <td>267</td>
      <td>265</td>
      <td>267</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>268</td>
      <td>277</td>
      <td>268</td>
      <td>277</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>295</td>
      <td>278</td>
      <td>295</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>296</td>
      <td>310</td>
      <td>296</td>
      <td>310</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>317</td>
      <td>311</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>318</td>
      <td>324</td>
      <td>318</td>
      <td>324</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>325</td>
      <td>340</td>
      <td>325</td>
      <td>340</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>341</td>
      <td>346</td>
      <td>341</td>
      <td>346</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>347</td>
      <td>352</td>
      <td>347</td>
      <td>352</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>353</td>
      <td>358</td>
      <td>353</td>
      <td>358</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>359</td>
      <td>373</td>
      <td>359</td>
      <td>373</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>391</td>
      <td>374</td>
      <td>391</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>392</td>
      <td>406</td>
      <td>392</td>
      <td>406</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>407</td>
      <td>416</td>
      <td>407</td>
      <td>416</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>417</td>
      <td>422</td>
      <td>417</td>
      <td>422</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>423</td>
      <td>427</td>
      <td>423</td>
      <td>427</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>428</td>
      <td>441</td>
      <td>428</td>
      <td>441</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>442</td>
      <td>470</td>
      <td>442</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>484</td>
      <td>471</td>
      <td>484</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>485</td>
      <td>492</td>
      <td>485</td>
      <td>492</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>493</td>
      <td>523</td>
      <td>493</td>
      <td>523</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4lep">4LEP</a> — Chain B (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTLGTNQVS</span><span class="topo-inside">KTHSFMTVS</span><span class="topo-membrane">LIELWERFGYYGMQA</span><span class="topo-outside">LIVYFMVQRLGFDDSRANLVW</span><span class="topo-membrane">SACAALIYVSPAIGG</span><span class="topo-inside">WVGDKILGTKRT</span><span class="topo-membrane">MLLGAGILSVGYALM</span><span class="topo-outside">TVPTENTWFMFS</span><span class="topo-membrane">ALGVIVVGNGLF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KP</span><span class="topo-inside">NAGNLVRKIYEGDDSKIDSAFTIY</span><span class="topo-membrane">YMAVNVGSTFSMLLT</span><span class="topo-outside">PWIKDYVNAQYGNEFGWHAAF</span><span class="topo-membrane">AVCCVGILVGLGNYAL</span><span class="topo-inside">MHKSLANYGS</span><span class="topo-unknown">EPDTR</span><span class="topo-inside">PVNKKSL</span><span class="topo-membrane">AIVLALAALSVVASAIIL</span><span class="topo-outside">EY</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">EDV</span><span class="topo-membrane">ARVFVYAAGVAVLGIFFH</span><span class="topo-inside">LIRT</span><span class="topo-unknown">SE</span><span class="topo-inside">PSERAGLIAA</span><span class="topo-membrane">LILTVQTVFFFIFYQQMS</span><span class="topo-outside">TSLALFALRNVDWDF</span><span class="topo-unknown">QVFGTH</span><span class="topo-outside">LWTWSPAQ</span><span class="topo-membrane">FQALNPIWIMVLSPVL</span><span class="topo-inside">AWS</span><span class="topo-unknown">YSWAGRNNKDF</span><span class="topo-inside">SIAA</span><span class="topo-membrane">KF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">ALGFAVVAIGFFI</span><span class="topo-outside">YGFAGQFAVNGKTSSWVMI</span><span class="topo-membrane">WGYASYSLGELLVSGL</span><span class="topo-inside">GLAMIAR</span><span class="topo-unknown">YVPARM</span><span class="topo-inside">GGFMMG</span><span class="topo-membrane">AYFVASGISQYLGG</span><span class="topo-outside">VVANFASVPQDLVDPLQTLPVYTNLFNKL</span><span class="topo-membrane">GVAAVVCTII</span></span>
<span class="topo-ruler">       490       500       510       520   </span>
<span class="topo-line"><span class="topo-membrane">ALAV</span><span class="topo-inside">LPLMRRL</span><span class="topo-unknown">TESHHAHSSIENNAAASLRDVKAEQAENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (41 regions)</summary>
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
      <td>9</td>
      <td>1</td>
      <td>9</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>18</td>
      <td>10</td>
      <td>18</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>33</td>
      <td>19</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>54</td>
      <td>34</td>
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
      <td>81</td>
      <td>70</td>
      <td>81</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>96</td>
      <td>82</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>108</td>
      <td>97</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>122</td>
      <td>109</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>146</td>
      <td>123</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>161</td>
      <td>147</td>
      <td>161</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>162</td>
      <td>182</td>
      <td>162</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>198</td>
      <td>183</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>208</td>
      <td>199</td>
      <td>208</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>209</td>
      <td>213</td>
      <td>209</td>
      <td>213</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>214</td>
      <td>220</td>
      <td>214</td>
      <td>220</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>238</td>
      <td>221</td>
      <td>238</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>243</td>
      <td>239</td>
      <td>243</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>261</td>
      <td>244</td>
      <td>261</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>265</td>
      <td>262</td>
      <td>265</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>266</td>
      <td>267</td>
      <td>266</td>
      <td>267</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>268</td>
      <td>277</td>
      <td>268</td>
      <td>277</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>295</td>
      <td>278</td>
      <td>295</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>296</td>
      <td>310</td>
      <td>296</td>
      <td>310</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>316</td>
      <td>311</td>
      <td>316</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>317</td>
      <td>324</td>
      <td>317</td>
      <td>324</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>325</td>
      <td>340</td>
      <td>325</td>
      <td>340</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>341</td>
      <td>343</td>
      <td>341</td>
      <td>343</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>354</td>
      <td>344</td>
      <td>354</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>355</td>
      <td>358</td>
      <td>355</td>
      <td>358</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>359</td>
      <td>373</td>
      <td>359</td>
      <td>373</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>392</td>
      <td>374</td>
      <td>392</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>393</td>
      <td>408</td>
      <td>393</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>415</td>
      <td>409</td>
      <td>415</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>416</td>
      <td>421</td>
      <td>416</td>
      <td>421</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>422</td>
      <td>427</td>
      <td>422</td>
      <td>427</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>428</td>
      <td>441</td>
      <td>428</td>
      <td>441</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>442</td>
      <td>470</td>
      <td>442</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>484</td>
      <td>471</td>
      <td>484</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>485</td>
      <td>491</td>
      <td>485</td>
      <td>491</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>492</td>
      <td>523</td>
      <td>492</td>
      <td>523</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##nsmb.2860

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4tpj">4TPJ</a></td>
      <td>3.2 A</td>
      <td>P2_1 2_1 2_1</td>
      <td>Full-length PepT_So2 from Shewanella oneidensis, wild-type, inward open conformation, co-crystallized with Ala-Ala-Ala (<a href="/xray-mp-wiki/reagents/ligands/aaa/">AAA</a>) tripeptide</td>
      <td>Ala-Ala-Ala (<a href="/xray-mp-wiki/reagents/ligands/aaa/">AAA</a>) tripeptide</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4tpg">4TPG</a></td>
      <td>3.91 A</td>
      <td>P2_1 2_1 2_1</td>
      <td>Full-length PepT_So2 from Shewanella oneidensis, wild-type, inward open conformation, co-crystallized with Ala-Tyr(L-3,5-diBr)-Ala (AY(Br)A) tripeptide</td>
      <td>Ala-Tyr(L-3,5-diBr)-Ala (AY(Br)A) tripeptide</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4tph">4TPH</a></td>
      <td>3.16 A</td>
      <td>P2_1 2_1 2_1</td>
      <td>Full-length PepT_So2 from Shewanella oneidensis, wild-type, inward open conformation, co-crystallized with Ala-Tyr(L-3,5-diBr) (AY(Br)) dipeptide</td>
      <td>Ala-Tyr(L-3,5-diBr) (AY(Br)) dipeptide</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length PepT_So2 from Shewanella oneidensis (Q8EHE6), C-terminal His-tag with tobacco etch virus (TEV) cleavage site, cloned into pNIC-CTHF-vector

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4tpj">4TPJ</a> — Chain A (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTLGTNQ</span><span class="topo-outside">VSKTHSFMT</span><span class="topo-membrane">VSLIELWERFGYYGMQALIV</span><span class="topo-inside">YFMVQRLGFDDSR</span><span class="topo-membrane">ANLVWSACAALIYVSPAIGGWV</span><span class="topo-outside">GDKILGTK</span><span class="topo-membrane">RTMLLGAGILSVGYALMTV</span><span class="topo-inside">PTENT</span><span class="topo-membrane">WFMFSALGVIVVGNGLF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KPNAG</span><span class="topo-outside">NLVRKIYE</span><span class="topo-unknown">GDD</span><span class="topo-outside">SKIDSAF</span><span class="topo-membrane">TIYYMAVNVGSTFSMLLTPWIK</span><span class="topo-inside">DYVNAQYGNEFG</span><span class="topo-membrane">WHAAFAVCCVGILVGLGNYAL</span><span class="topo-outside">MHKSLANYGSEPDTRPVN</span><span class="topo-membrane">KKSLAIVLALAALSVVASAIILEY</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">EDVARVFVYAAGVAVLGI</span><span class="topo-unknown">FFHLIRTSEPSERAGL</span><span class="topo-outside">IA</span><span class="topo-membrane">ALILTVQTVFFFIFYQQMSTSLA</span><span class="topo-inside">LFALRNVDWDFQVFGTHLWT</span><span class="topo-membrane">WSPAQFQALNPIWIMVLSPVLAW</span><span class="topo-unknown">SYSWAGRNNKDFS</span><span class="topo-outside">I</span><span class="topo-membrane">AAKF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">ALGFAVVAIGFFIYGF</span><span class="topo-inside">AGQFAVNGKTS</span><span class="topo-membrane">SWVMIWGYASYSLGELLVSGLGL</span><span class="topo-outside">AMIARY</span><span class="topo-unknown">VPARMGGF</span><span class="topo-membrane">MMGAYFVASGISQYLGGVVAN</span><span class="topo-inside">FASVPQDLVDPLQTLPVYTN</span><span class="topo-membrane">LFNKLGVAAVVCTII</span></span>
<span class="topo-ruler">       490       500       510       520   </span>
<span class="topo-line"><span class="topo-membrane">ALAVL</span><span class="topo-outside">PLMRRLT</span><span class="topo-unknown">ESHHAHSSIENNAAASLRDVKAEQAENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (34 regions)</summary>
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
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>16</td>
      <td>8</td>
      <td>16</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>36</td>
      <td>17</td>
      <td>36</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>37</td>
      <td>49</td>
      <td>37</td>
      <td>49</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>50</td>
      <td>71</td>
      <td>50</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>79</td>
      <td>72</td>
      <td>79</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>98</td>
      <td>80</td>
      <td>98</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>99</td>
      <td>103</td>
      <td>99</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>125</td>
      <td>104</td>
      <td>125</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>126</td>
      <td>133</td>
      <td>126</td>
      <td>133</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>136</td>
      <td>134</td>
      <td>136</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>137</td>
      <td>143</td>
      <td>137</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>144</td>
      <td>165</td>
      <td>144</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>166</td>
      <td>177</td>
      <td>166</td>
      <td>177</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>198</td>
      <td>178</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>216</td>
      <td>199</td>
      <td>216</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>217</td>
      <td>258</td>
      <td>217</td>
      <td>258</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>259</td>
      <td>274</td>
      <td>259</td>
      <td>274</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>275</td>
      <td>276</td>
      <td>275</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>299</td>
      <td>277</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>319</td>
      <td>300</td>
      <td>319</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>320</td>
      <td>342</td>
      <td>320</td>
      <td>342</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>343</td>
      <td>355</td>
      <td>343</td>
      <td>355</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>356</td>
      <td>356</td>
      <td>356</td>
      <td>356</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>357</td>
      <td>376</td>
      <td>357</td>
      <td>376</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>377</td>
      <td>387</td>
      <td>377</td>
      <td>387</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>388</td>
      <td>410</td>
      <td>388</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>416</td>
      <td>411</td>
      <td>416</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>417</td>
      <td>424</td>
      <td>417</td>
      <td>424</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>425</td>
      <td>445</td>
      <td>425</td>
      <td>445</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>446</td>
      <td>465</td>
      <td>446</td>
      <td>465</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>466</td>
      <td>485</td>
      <td>466</td>
      <td>485</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>486</td>
      <td>492</td>
      <td>486</td>
      <td>492</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>493</td>
      <td>523</td>
      <td>493</td>
      <td>523</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4tpj">4TPJ</a> — Chain B (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTLGTNQ</span><span class="topo-outside">VSKTHSF</span><span class="topo-membrane">MTVSLIELWERFGYYGMQALI</span><span class="topo-inside">VYFMVQRLGFDDSRA</span><span class="topo-membrane">NLVWSACAALIYVSPAIGGWVG</span><span class="topo-outside">DK</span><span class="topo-membrane">ILGTKRTMLLGAGILSVGYALMT</span><span class="topo-inside">VPTENTWF</span><span class="topo-membrane">MFSALGVIVVGNGLF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KPNAGN</span><span class="topo-outside">LVRKIYE</span><span class="topo-unknown">GDD</span><span class="topo-outside">SKIDSA</span><span class="topo-membrane">FTIYYMAVNVGSTFSMLLTP</span><span class="topo-inside">WIKDYVNAQYGNEFGWHA</span><span class="topo-membrane">AFAVCCVGILVGLGNYALMH</span><span class="topo-outside">KSLANYGSEPDTRP</span><span class="topo-membrane">VNKKSLAIVLALAALSVVASAIILEY</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">EDVARVFVYAAGVAVLGIFFH</span><span class="topo-unknown">LIRTSEPSERA</span><span class="topo-outside">GLIA</span><span class="topo-membrane">ALILTVQTVFFFIFYQQMSTSLA</span><span class="topo-inside">LFALRNVDWDFQVFGTHLWTWSP</span><span class="topo-membrane">AQFQALNPIWIMVLSPVLAW</span><span class="topo-unknown">SYSWAGRNNKDFS</span><span class="topo-outside">I</span><span class="topo-membrane">AAKF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">ALGFAVVAIGFFIYGF</span><span class="topo-inside">AGQFAVNGKTSS</span><span class="topo-membrane">WVMIWGYASYSLGELLVSGLGLA</span><span class="topo-outside">MIARY</span><span class="topo-unknown">VPARMGGF</span><span class="topo-membrane">MMGAYFVASGISQYLGGVVA</span><span class="topo-inside">NFASVPQDLVDPLQTLPVYTN</span><span class="topo-membrane">LFNKLGVAAVVCTII</span></span>
<span class="topo-ruler">       490       500       510       520   </span>
<span class="topo-line"><span class="topo-membrane">ALAVL</span><span class="topo-outside">PLMRRLT</span><span class="topo-unknown">ESHHAHSSIENNAAASLRDVKAEQAENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (34 regions)</summary>
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
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>14</td>
      <td>8</td>
      <td>14</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>35</td>
      <td>15</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>50</td>
      <td>36</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>72</td>
      <td>51</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>74</td>
      <td>73</td>
      <td>74</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>97</td>
      <td>75</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>98</td>
      <td>105</td>
      <td>98</td>
      <td>105</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>126</td>
      <td>106</td>
      <td>126</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>127</td>
      <td>133</td>
      <td>127</td>
      <td>133</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>136</td>
      <td>134</td>
      <td>136</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>137</td>
      <td>142</td>
      <td>137</td>
      <td>142</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>162</td>
      <td>143</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>180</td>
      <td>163</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>200</td>
      <td>181</td>
      <td>200</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>201</td>
      <td>214</td>
      <td>201</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>261</td>
      <td>215</td>
      <td>261</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>272</td>
      <td>262</td>
      <td>272</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>273</td>
      <td>276</td>
      <td>273</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>299</td>
      <td>277</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>322</td>
      <td>300</td>
      <td>322</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>342</td>
      <td>323</td>
      <td>342</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>343</td>
      <td>355</td>
      <td>343</td>
      <td>355</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>356</td>
      <td>356</td>
      <td>356</td>
      <td>356</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>357</td>
      <td>376</td>
      <td>357</td>
      <td>376</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>377</td>
      <td>388</td>
      <td>377</td>
      <td>388</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>389</td>
      <td>411</td>
      <td>389</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>416</td>
      <td>412</td>
      <td>416</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>417</td>
      <td>424</td>
      <td>417</td>
      <td>424</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>425</td>
      <td>444</td>
      <td>425</td>
      <td>444</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>445</td>
      <td>465</td>
      <td>445</td>
      <td>465</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>466</td>
      <td>485</td>
      <td>466</td>
      <td>485</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>486</td>
      <td>492</td>
      <td>486</td>
      <td>492</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>493</td>
      <td>523</td>
      <td>493</td>
      <td>523</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4tpg">4TPG</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTLGTNQ</span><span class="topo-inside">VSKTHSFMTVSL</span><span class="topo-membrane">IELWERFGYYGMQA</span><span class="topo-outside">LIVYFMVQRLGFDDSRANLVW</span><span class="topo-membrane">SACAALIYVSPAIG</span><span class="topo-inside">GWVGDKILGTKRT</span><span class="topo-membrane">MLLGAGILSVGYAL</span><span class="topo-outside">MTVPTENTWFMFS</span><span class="topo-membrane">ALGVIVVGNGLF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KP</span><span class="topo-inside">NAGNLVRKIYE</span><span class="topo-unknown">GDD</span><span class="topo-inside">SKIDSAFTIYY</span><span class="topo-membrane">MAVNVGSTFSMLLT</span><span class="topo-outside">PWIKDYVNAQYGNEFGWHAAF</span><span class="topo-membrane">AVCCVGILVGLGNYA</span><span class="topo-inside">LMHKSLANYGSEPDTRPVNKKSL</span><span class="topo-membrane">AIVLALAALSVVASAIIL</span><span class="topo-outside">EY</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">EDV</span><span class="topo-membrane">ARVFVYAAGVAVLGIFF</span><span class="topo-inside">HLIR</span><span class="topo-unknown">TSE</span><span class="topo-inside">PSERAGLIAAL</span><span class="topo-membrane">ILTVQTVFFFIFYQQMS</span><span class="topo-outside">TSLALFALRNVDWDFQVFGTHLWTWSPAQ</span><span class="topo-membrane">FQALNPIWIMVLSPVL</span><span class="topo-inside">AW</span><span class="topo-unknown">SYSWAGRNNKDFS</span><span class="topo-inside">IAA</span><span class="topo-membrane">KF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">ALGFAVVAIGFFI</span><span class="topo-outside">YGFAGQFAVNGKTSSWVMI</span><span class="topo-membrane">WGYASYSLGELLVS</span><span class="topo-inside">GLGLAMIARY</span><span class="topo-unknown">VPARMGG</span><span class="topo-inside">FMMGA</span><span class="topo-membrane">YFVASGISQYLGG</span><span class="topo-outside">VVANFASVPQDLVDPLQTLPVYTNLFNKL</span><span class="topo-membrane">GVAAVVCTII</span></span>
<span class="topo-ruler">       490       500       510       520   </span>
<span class="topo-line"><span class="topo-membrane">ALAV</span><span class="topo-inside">LPLMRRLT</span><span class="topo-unknown">ESHHAHSSIENNAAASLRDVKAEQAENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (39 regions)</summary>
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
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>19</td>
      <td>8</td>
      <td>19</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>33</td>
      <td>20</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>54</td>
      <td>34</td>
      <td>54</td>
      <td>Outside</td>
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
      <td>81</td>
      <td>69</td>
      <td>81</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>95</td>
      <td>82</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>96</td>
      <td>108</td>
      <td>96</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>122</td>
      <td>109</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>133</td>
      <td>123</td>
      <td>133</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>136</td>
      <td>134</td>
      <td>136</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>137</td>
      <td>147</td>
      <td>137</td>
      <td>147</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>161</td>
      <td>148</td>
      <td>161</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>162</td>
      <td>182</td>
      <td>162</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>197</td>
      <td>183</td>
      <td>197</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>220</td>
      <td>198</td>
      <td>220</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>238</td>
      <td>221</td>
      <td>238</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>243</td>
      <td>239</td>
      <td>243</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>260</td>
      <td>244</td>
      <td>260</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>261</td>
      <td>264</td>
      <td>261</td>
      <td>264</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>265</td>
      <td>267</td>
      <td>265</td>
      <td>267</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>268</td>
      <td>278</td>
      <td>268</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>295</td>
      <td>279</td>
      <td>295</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>296</td>
      <td>324</td>
      <td>296</td>
      <td>324</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>325</td>
      <td>340</td>
      <td>325</td>
      <td>340</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>341</td>
      <td>342</td>
      <td>341</td>
      <td>342</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>355</td>
      <td>343</td>
      <td>355</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>356</td>
      <td>358</td>
      <td>356</td>
      <td>358</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>359</td>
      <td>373</td>
      <td>359</td>
      <td>373</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>392</td>
      <td>374</td>
      <td>392</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>393</td>
      <td>406</td>
      <td>393</td>
      <td>406</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>407</td>
      <td>416</td>
      <td>407</td>
      <td>416</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>417</td>
      <td>423</td>
      <td>417</td>
      <td>423</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>424</td>
      <td>428</td>
      <td>424</td>
      <td>428</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>429</td>
      <td>441</td>
      <td>429</td>
      <td>441</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>442</td>
      <td>470</td>
      <td>442</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>484</td>
      <td>471</td>
      <td>484</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>485</td>
      <td>492</td>
      <td>485</td>
      <td>492</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>493</td>
      <td>523</td>
      <td>493</td>
      <td>523</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4tpg">4TPG</a> — Chain B (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTLGTNQ</span><span class="topo-inside">VSKTHSFMTVSL</span><span class="topo-membrane">IELWERFGYYGMQA</span><span class="topo-outside">LIVYFMVQRLGFDDSRANLVW</span><span class="topo-membrane">SACAALIYVSPAIG</span><span class="topo-inside">GWVGDKILGTKRT</span><span class="topo-membrane">MLLGAGILSVGYAL</span><span class="topo-outside">MTVPTENTWFMFS</span><span class="topo-membrane">ALGVIVVGNGLF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KP</span><span class="topo-inside">NAGNLVRKIYE</span><span class="topo-unknown">GDD</span><span class="topo-inside">SKIDSAFTIYY</span><span class="topo-membrane">MAVNVGSTFSMLLT</span><span class="topo-outside">PWIKDYVNAQYGNEFGWHAAF</span><span class="topo-membrane">AVCCVGILVGLGNYA</span><span class="topo-inside">LMHKSLANYGSEPDTRPVNKKSL</span><span class="topo-membrane">AIVLALAALSVVASAIIL</span><span class="topo-outside">EY</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">EDV</span><span class="topo-membrane">ARVFVYAAGVAVLGIFF</span><span class="topo-inside">HLIR</span><span class="topo-unknown">TSE</span><span class="topo-inside">PSERAGLIAAL</span><span class="topo-membrane">ILTVQTVFFFIFYQQMS</span><span class="topo-outside">TSLALFALRNVDWDFQVFGTHLWTWSPAQ</span><span class="topo-membrane">FQALNPIWIMVLSPVL</span><span class="topo-inside">AW</span><span class="topo-unknown">SYSWAGRNNKDFS</span><span class="topo-inside">IAA</span><span class="topo-membrane">KF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">ALGFAVVAIGFFI</span><span class="topo-outside">YGFAGQFAVNGKTSSWVMI</span><span class="topo-membrane">WGYASYSLGELLVS</span><span class="topo-inside">GLGLAMIARY</span><span class="topo-unknown">VPARMGG</span><span class="topo-inside">FMMGA</span><span class="topo-membrane">YFVASGISQYLGG</span><span class="topo-outside">VVANFASVPQDLVDPLQTLPVYTNLFNKL</span><span class="topo-membrane">GVAAVVCTII</span></span>
<span class="topo-ruler">       490       500       510       520   </span>
<span class="topo-line"><span class="topo-membrane">ALAV</span><span class="topo-inside">LPLMRRLT</span><span class="topo-unknown">ESHHAHSSIENNAAASLRDVKAEQAENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (39 regions)</summary>
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
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>19</td>
      <td>8</td>
      <td>19</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>33</td>
      <td>20</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>54</td>
      <td>34</td>
      <td>54</td>
      <td>Outside</td>
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
      <td>81</td>
      <td>69</td>
      <td>81</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>95</td>
      <td>82</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>96</td>
      <td>108</td>
      <td>96</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>122</td>
      <td>109</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>133</td>
      <td>123</td>
      <td>133</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>136</td>
      <td>134</td>
      <td>136</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>137</td>
      <td>147</td>
      <td>137</td>
      <td>147</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>161</td>
      <td>148</td>
      <td>161</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>162</td>
      <td>182</td>
      <td>162</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>197</td>
      <td>183</td>
      <td>197</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>220</td>
      <td>198</td>
      <td>220</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>238</td>
      <td>221</td>
      <td>238</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>243</td>
      <td>239</td>
      <td>243</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>260</td>
      <td>244</td>
      <td>260</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>261</td>
      <td>264</td>
      <td>261</td>
      <td>264</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>265</td>
      <td>267</td>
      <td>265</td>
      <td>267</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>268</td>
      <td>278</td>
      <td>268</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>295</td>
      <td>279</td>
      <td>295</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>296</td>
      <td>324</td>
      <td>296</td>
      <td>324</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>325</td>
      <td>340</td>
      <td>325</td>
      <td>340</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>341</td>
      <td>342</td>
      <td>341</td>
      <td>342</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>355</td>
      <td>343</td>
      <td>355</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>356</td>
      <td>358</td>
      <td>356</td>
      <td>358</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>359</td>
      <td>373</td>
      <td>359</td>
      <td>373</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>392</td>
      <td>374</td>
      <td>392</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>393</td>
      <td>406</td>
      <td>393</td>
      <td>406</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>407</td>
      <td>416</td>
      <td>407</td>
      <td>416</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>417</td>
      <td>423</td>
      <td>417</td>
      <td>423</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>424</td>
      <td>428</td>
      <td>424</td>
      <td>428</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>429</td>
      <td>441</td>
      <td>429</td>
      <td>441</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>442</td>
      <td>470</td>
      <td>442</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>484</td>
      <td>471</td>
      <td>484</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>485</td>
      <td>492</td>
      <td>485</td>
      <td>492</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>493</td>
      <td>523</td>
      <td>493</td>
      <td>523</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4tph">4TPH</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTLGTNQ</span><span class="topo-inside">VSKTHSFMTVSL</span><span class="topo-membrane">IELWERFGYYGMQA</span><span class="topo-outside">LIVYFMVQRLGFDDSRANLVW</span><span class="topo-membrane">SACAALIYVSPAIG</span><span class="topo-inside">GWVGDKILGTKRTM</span><span class="topo-membrane">LLGAGILSVGYALM</span><span class="topo-outside">TVPTENTWFMFS</span><span class="topo-membrane">ALGVIVVGNGLF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KP</span><span class="topo-inside">NAGNLVRKIYE</span><span class="topo-unknown">GDD</span><span class="topo-inside">SKIDSAFTIYY</span><span class="topo-membrane">MAVNVGSTFSMLLT</span><span class="topo-outside">PWIKDYVNAQYGNEFGWHAAF</span><span class="topo-membrane">AVCCVGILVGLGNYA</span><span class="topo-inside">LMHKSLANYGSEPDTRPVNKKSL</span><span class="topo-membrane">AIVLALAALSVVASAIIL</span><span class="topo-outside">EY</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">EDV</span><span class="topo-membrane">ARVFVYAAGVAVLGIFF</span><span class="topo-inside">HL</span><span class="topo-unknown">IRTSEPS</span><span class="topo-inside">ERAGLIAAL</span><span class="topo-membrane">ILTVQTVFFFIFYQQMS</span><span class="topo-outside">TSLALFALRNVDWDFQVFGTHLWTWSPAQ</span><span class="topo-membrane">FQALNPIWIMVLSPVL</span><span class="topo-inside">AW</span><span class="topo-unknown">SYSWAGRNNKDFS</span><span class="topo-inside">IAA</span><span class="topo-membrane">KF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">ALGFAVVAIGFFI</span><span class="topo-outside">YGFAGQFAVNGKTSSWVMI</span><span class="topo-membrane">WGYASYSLGELLVS</span><span class="topo-inside">GLGLAMIAR</span><span class="topo-unknown">YVPARMGGF</span><span class="topo-inside">MMG</span><span class="topo-membrane">AYFVASGISQYLGG</span><span class="topo-outside">VVANFASVPQDLVDPLQTLPVYTNLFNKL</span><span class="topo-membrane">GVAAVVCTII</span></span>
<span class="topo-ruler">       490       500       510       520   </span>
<span class="topo-line"><span class="topo-membrane">ALAV</span><span class="topo-inside">LPLMRRLT</span><span class="topo-unknown">ESHHAHSSIENNAAASLRDVKAEQAENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (39 regions)</summary>
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
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>19</td>
      <td>8</td>
      <td>19</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>33</td>
      <td>20</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>54</td>
      <td>34</td>
      <td>54</td>
      <td>Outside</td>
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
      <td>82</td>
      <td>69</td>
      <td>82</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>96</td>
      <td>83</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>108</td>
      <td>97</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>122</td>
      <td>109</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>133</td>
      <td>123</td>
      <td>133</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>136</td>
      <td>134</td>
      <td>136</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>137</td>
      <td>147</td>
      <td>137</td>
      <td>147</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>161</td>
      <td>148</td>
      <td>161</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>162</td>
      <td>182</td>
      <td>162</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>197</td>
      <td>183</td>
      <td>197</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>220</td>
      <td>198</td>
      <td>220</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>238</td>
      <td>221</td>
      <td>238</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>243</td>
      <td>239</td>
      <td>243</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>260</td>
      <td>244</td>
      <td>260</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>261</td>
      <td>262</td>
      <td>261</td>
      <td>262</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>263</td>
      <td>269</td>
      <td>263</td>
      <td>269</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>270</td>
      <td>278</td>
      <td>270</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>295</td>
      <td>279</td>
      <td>295</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>296</td>
      <td>324</td>
      <td>296</td>
      <td>324</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>325</td>
      <td>340</td>
      <td>325</td>
      <td>340</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>341</td>
      <td>342</td>
      <td>341</td>
      <td>342</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>355</td>
      <td>343</td>
      <td>355</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>356</td>
      <td>358</td>
      <td>356</td>
      <td>358</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>359</td>
      <td>373</td>
      <td>359</td>
      <td>373</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>392</td>
      <td>374</td>
      <td>392</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>393</td>
      <td>406</td>
      <td>393</td>
      <td>406</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>407</td>
      <td>415</td>
      <td>407</td>
      <td>415</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>416</td>
      <td>424</td>
      <td>416</td>
      <td>424</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>425</td>
      <td>427</td>
      <td>425</td>
      <td>427</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>428</td>
      <td>441</td>
      <td>428</td>
      <td>441</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>442</td>
      <td>470</td>
      <td>442</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>484</td>
      <td>471</td>
      <td>484</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>485</td>
      <td>492</td>
      <td>485</td>
      <td>492</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>493</td>
      <td>523</td>
      <td>493</td>
      <td>523</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4tph">4TPH</a> — Chain B (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTLGTNQ</span><span class="topo-inside">VSKTHSFMTVSL</span><span class="topo-membrane">IELWERFGYYGMQA</span><span class="topo-outside">LIVYFMVQRLGFDDSRANLVW</span><span class="topo-membrane">SACAALIYVSPAIG</span><span class="topo-inside">GWVGDKILGTKRTM</span><span class="topo-membrane">LLGAGILSVGYALM</span><span class="topo-outside">TVPTENTWFMFS</span><span class="topo-membrane">ALGVIVVGNGLF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KP</span><span class="topo-inside">NAGNLVRKIYE</span><span class="topo-unknown">GDD</span><span class="topo-inside">SKIDSAFTIYY</span><span class="topo-membrane">MAVNVGSTFSMLLT</span><span class="topo-outside">PWIKDYVNAQYGNEFGWHAAF</span><span class="topo-membrane">AVCCVGILVGLGNY</span><span class="topo-inside">ALMHKSLANYGSEPDTRPVNKKSL</span><span class="topo-membrane">AIVLALAALSVVASAIIL</span><span class="topo-outside">EY</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">EDV</span><span class="topo-membrane">ARVFVYAAGVAVLGIFF</span><span class="topo-inside">HL</span><span class="topo-unknown">IRTSEPS</span><span class="topo-inside">ERAGLIAAL</span><span class="topo-membrane">ILTVQTVFFFIFYQQMS</span><span class="topo-outside">TSLALFALRNVDWDFQVFGTHLWTWSPAQ</span><span class="topo-membrane">FQALNPIWIMVLSPVL</span><span class="topo-inside">AW</span><span class="topo-unknown">SYSWAGRNNKDFS</span><span class="topo-inside">IAAK</span><span class="topo-membrane">F</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">ALGFAVVAIGFFI</span><span class="topo-outside">YGFAGQFAVNGKTSSWVMI</span><span class="topo-membrane">WGYASYSLGELLVS</span><span class="topo-inside">GLGLAMIAR</span><span class="topo-unknown">YVPARMGGF</span><span class="topo-inside">MMG</span><span class="topo-membrane">AYFVASGISQYLGG</span><span class="topo-outside">VVANFASVPQDLVDPLQTLPVYTNLFNKL</span><span class="topo-membrane">GVAAVVCTII</span></span>
<span class="topo-ruler">       490       500       510       520   </span>
<span class="topo-line"><span class="topo-membrane">ALAV</span><span class="topo-inside">LPLMRRLT</span><span class="topo-unknown">ESHHAHSSIENNAAASLRDVKAEQAENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (39 regions)</summary>
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
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>19</td>
      <td>8</td>
      <td>19</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>33</td>
      <td>20</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>54</td>
      <td>34</td>
      <td>54</td>
      <td>Outside</td>
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
      <td>82</td>
      <td>69</td>
      <td>82</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>96</td>
      <td>83</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>108</td>
      <td>97</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>122</td>
      <td>109</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>133</td>
      <td>123</td>
      <td>133</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>136</td>
      <td>134</td>
      <td>136</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>137</td>
      <td>147</td>
      <td>137</td>
      <td>147</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>161</td>
      <td>148</td>
      <td>161</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>162</td>
      <td>182</td>
      <td>162</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>196</td>
      <td>183</td>
      <td>196</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>220</td>
      <td>197</td>
      <td>220</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>238</td>
      <td>221</td>
      <td>238</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>243</td>
      <td>239</td>
      <td>243</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>260</td>
      <td>244</td>
      <td>260</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>261</td>
      <td>262</td>
      <td>261</td>
      <td>262</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>263</td>
      <td>269</td>
      <td>263</td>
      <td>269</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>270</td>
      <td>278</td>
      <td>270</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>295</td>
      <td>279</td>
      <td>295</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>296</td>
      <td>324</td>
      <td>296</td>
      <td>324</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>325</td>
      <td>340</td>
      <td>325</td>
      <td>340</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>341</td>
      <td>342</td>
      <td>341</td>
      <td>342</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>355</td>
      <td>343</td>
      <td>355</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>356</td>
      <td>359</td>
      <td>356</td>
      <td>359</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>360</td>
      <td>373</td>
      <td>360</td>
      <td>373</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>392</td>
      <td>374</td>
      <td>392</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>393</td>
      <td>406</td>
      <td>393</td>
      <td>406</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>407</td>
      <td>415</td>
      <td>407</td>
      <td>415</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>416</td>
      <td>424</td>
      <td>416</td>
      <td>424</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>425</td>
      <td>427</td>
      <td>425</td>
      <td>427</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>428</td>
      <td>441</td>
      <td>428</td>
      <td>441</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>442</td>
      <td>470</td>
      <td>442</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>484</td>
      <td>471</td>
      <td>484</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>485</td>
      <td>492</td>
      <td>485</td>
      <td>492</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>493</td>
      <td>523</td>
      <td>493</td>
      <td>523</td>
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

### First substrate-bound POT structure

This is the first POT transporter structure solved in complex with a substrate.
[Alafosfalin](/xray-mp-wiki/reagents/ligands/alafosfalin/) binds in the central hydrophilic cavity with its N-terminal amine group
interacting with Asn151, Asn329 and Glu402, while its phosphonate moiety forms a
hydrogen bond with Tyr29 and a salt bridge with Arg25. The principle binding mode
is consistent with mutagenesis data on PEPT1, PepT_So, PepT_St, and two E. coli
transporters, indicating conserved substrate recognition across the POT family.

### Substrate-binding pocket architecture

The substrate-binding site is located in a hydrophilic cavity at the center of
the cytoplasmic crevice, formed by helices H1, H2, H4, H5 from the N-terminal
bundle and H7, H8, H10, H11 from the C-terminal bundle. A cluster of conserved
tyrosine residues (Tyr29, Tyr147, Tyr291) points toward the cavity center and
mediates interactions with peptide backbone CO- and NH-groups, enabling broad
substrate specificity. Arg25 and Glu402 are key residues for C-terminus
coordination, while Asn151, Asn329 and Tyr29 coordinate the N-terminus.

### Tetrameric assembly

Unlike other POT family members that are monomeric, PepT_So2 forms a homo-tetramer
in detergent solution as demonstrated by analytical gel filtration, Blue Native PAGE,
cross-linking, and negative stain electron microscopy. The tetramer has approximate
dimensions of 12.4 x 12.4 nm. The P3_1 2_1 crystal form shows a tetrameric
assembly in the crystal lattice, with TM12 mediating key interactions between
monomers. The P2_1 2_1 2_1 crystal form shows a dimer interface stabilized by
zinc ions, likely a crystal-packing artifact.

### Gating mechanism in inward open conformation

In the inward open conformation, the N- and C-terminal bundles interact tightly
at the periplasmic side, while a large central hydrophilic crevice faces the
intracellular side. The gating mechanism involves two conserved interaction
networks: a salt bridge between H2 and H7 (Asp47 and Arg304 in PepT_So2) and
a hydrogen bond network between H5 and H8 (Lys165, Asp166, Ser321). Tyr37
plays a key role in sealing the N- and C-terminal bundle on the periplasmic side.
The intracellular gate residue Met426 in helix H11 is displaced by approximately
6 A compared to the occluded state of PepT_So, opening the intracellular gate.

### Three peptide-binding pockets (P1, P2, P3)

The PepT_So2 substrate-binding site is divided into three pockets for peptide side
chain interactions. P1 is a small pocket formed by Ser154, Tyr29, Met158 and Pro330,
accommodating only small- to medium-sized residues. P2 is a hydrophobic pocket
dominated by Phe287, Phe288, Tyr291 and Ser406. P3 is an aromatic pocket formed by
Arg25, Tyr28, Trp54, Ile61, Tyr62, Pro65, Asn292, Phe430 and Asn437. The N-terminus
of bound peptides is clamped by Glu402, Asn151, Asn329 and Tyr147, while the C-terminus
extends into a positively charged patch (Arg25, Lys121). Dipeptides interact primarily
with Arg25, while tripeptides extend further to interact with Lys121.

### Peptide-bound crystal structures at high resolution

Three crystal structures of PepT_So2 in complex with different peptides were solved:
4TPJ ([AAA](/xray-mp-wiki/reagents/ligands/aaa/) tripeptide, 3.2 A), 4TPG (AY(Br)A tripeptide, 3.91 A), and 4TPH
(AY(Br) dipeptide, 3.16 A). All in P2_1 2_1 2_1 space group with two molecules per
asymmetric unit. Crystallization used 3% TMNO, phosphate [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) buffer pH 4.0-4.5,
36-46% [PEG](/xray-mp-wiki/reagents/additives/peg/) 300, and 0.12 M ZnCl2. The brominated tyrosine-containing peptides
provided strong anomalous densities for bromine atoms, confirming correct ligand
placement.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/pot-family/">POT Family (Proton-Dependent Oligopeptide Transporters)</a> — PepT_So2 is a member of the POT family within MFS
- <a href="/xray-mp-wiki/proteins/mfs-transporters/pept-so/">PepT_So Oligopeptide Transporter</a> — POT family member from Shewanella oneidensis, occluded conformation
- <a href="/xray-mp-wiki/proteins/mfs-transporters/pept-st/">PepT_St Proton-Dependent Oligopeptide Transporter</a> — POT family member from Streptococcus thermophilus, inward open conformation
- <a href="/xray-mp-wiki/concepts/protein-families/mfs-transporter/">Major Facilitator Superfamily (MFS)</a> — PepT_So2 belongs to the MFS of secondary active transporters
- <a href="/xray-mp-wiki/reagents/ligands/alafosfalin/">Alafosfalin</a> — Peptidomimetic phosphonodipeptide ligand co-crystallized with PepT_So2
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/scissor-switch-gating/">Scissor-Switch Gating</a> — POT-specific gating mechanism employed by PepT_So2
- <a href="/xray-mp-wiki/proteins/slc-transporters/dtpa/">E. coli DtpA Peptide Transporter</a> — POT family member from Escherichia coli
- <a href="/xray-mp-wiki/proteins/mfs-transporters/ybgH/">E. coli YbgH Peptide Transporter</a> — POT family member from Escherichia coli
- <a href="/xray-mp-wiki/reagents/ligands/aaa/">Ala-Ala-Ala (AAA)</a> — Tripeptide ligand co-crystallized with PepT_So2 (PDB 4TPJ)
- <a href="/xray-mp-wiki/reagents/ligands/aybr-a/">Ala-Tyr(L-3,5-diBr)-Ala (AY(Br)A)</a> — Brominated tripeptide ligand co-crystallized with PepT_So2 (PDB 4TPG)
- <a href="/xray-mp-wiki/reagents/ligands/aybr/">Ala-Tyr(L-3,5-diBr) (AY(Br))</a> — Brominated dipeptide ligand co-crystallized with PepT_So2 (PDB 4TPH)
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/peptide-binding-pocket/">PepT_So2 Substrate-Binding Pockets (P1, P2, P3)</a> — Three pockets identified in PepT_So2 substrate-binding cavity for side chain recognition
