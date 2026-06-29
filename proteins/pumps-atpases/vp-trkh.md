---
title: "TrkH from Vibrio parahaemolyticus (VpTrkH)"
created: 2026-06-09
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature09731]
verified: false
---

# TrkH from Vibrio parahaemolyticus (VpTrkH)

## Overview

[TRKH](/xray-mp-wiki/proteins/pumps-atpases/trkh/) from Vibrio parahaemolyticus (VpTrkH) is a potassium ion channel belonging to the Trk/Ktr/Kdp superfamily of cation transport systems. The structure reveals a homodimeric architecture with each protomer composed of four transmembrane domains (D0-D3) surrounding a central pore domain (D4). The selectivity filter is structurally similar to that of [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/), with a conserved TVGYG signature sequence, but the pore helix dipole is oriented differently. VpTrkH is the first high-resolution structure of a Trk family potassium channel and provides insight into potassium uptake mechanisms in bacteria.


## Publications

### doi/10.1038##nature09731

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3pjz">3PJZ</a></td>
      <td>3.5</td>
      <td>P2(1)2(1)2(1)</td>
      <td>Full-length VpTrkH with C-terminal deca-histidine tag; expressed in Escherichia coli; SeMet-labeled for phasing</td>
      <td>K+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3pjz">3PJZ</a></td>
      <td>3.5</td>
      <td>P2(1)2(1)2(1)</td>
      <td>Full-length VpTrkH with C-terminal deca-histidine tag</td>
      <td>Rb+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3pjz">3PJZ</a></td>
      <td>4.2</td>
      <td>P2(1)2(1)2(1)</td>
      <td>Full-length VpTrkH with C-terminal deca-histidine tag</td>
      <td>Ba2+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3pjz">3PJZ</a></td>
      <td>3.9</td>
      <td>P2(1)2(1)2(1)</td>
      <td>SeMet-labeled full-length VpTrkH with C-terminal deca-histidine tag; used for SAD phasing</td>
      <td>--</td>
    </tr>
  </tbody>
</table>

**Purification:**

- **Expression system**: Escherichia coli BL21(DE3)
- **Expression construct**: Full-length VpTrkH with C-terminal deca-histidine tag; expressed with [IPTG](/xray-mp-wiki/reagents/additives/iptg/) induction; SeMet-labeled for phasing in minimal medium supplemented with [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/)
- **Tag info**: C-terminal deca-histidine tag, cleaved by TEV protease

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
      <td>Cell lysis</td>
      <td>Microfluidizer or French press</td>
      <td>--</td>
      <td>Not specified in supp info + --</td>
      <td>Cells harvested and lysed for membrane preparation</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Cobalt <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Co2+ IMAC column (<a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> resin)</td>
      <td>Not specified in supp info + --</td>
      <td>Deca-histidine tagged VpTrkH purified on cobalt affinity column</td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td>TEV protease digestion</td>
      <td>—</td>
      <td>Not specified in supp info + --</td>
      <td>Deca-histidine tag removed by TEV protease</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td>Not specified</td>
      <td>Not specified in supp info + --</td>
      <td>VpTrkH elutes as a single peak on gel filtration (see Supp Fig 2a)</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified VpTrkH, confirmed as dimer by chemical crosslinking
**Yield**: --
**Purity**: >95% by SDS-PAGE

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified VpTrkH (SeMet-labeled or native)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals belong to space group P2(1)2(1)2(1). Four data sets: SeMet SAD (3.9 A), native K+ (3.5 A), native Ba2+ (4.2 A), native Rb+ (3.5 A). Data collected at APS. Structure solved by SeMet SAD phasing. Substrate ions (K+, Rb+, Ba2+) soaked or included in crystallization conditions.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3pjz">3PJZ</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">MQFRSI</span><span class="topo-membrane">IRIVGLLLALFSVTMLAPALVALLY</span><span class="topo-inside">RDGAG</span><span class="topo-membrane">VPFVTTFFVLLFCGAMCWFPNR</span><span class="topo-outside">RH</span></span>
<span class="topo-line"><span class="topo-outside">KHELKSRDG</span><span class="topo-membrane">FLIVVLFWTVLGSAGSLPFLIA</span><span class="topo-inside">DNPNISV</span><span class="topo-unknown">TDAFFESFSALTTTGATV</span><span class="topo-inside">IVGL</span></span>
<span class="topo-line"><span class="topo-inside">DELPK</span><span class="topo-membrane">AILFYRQFLQWFGGMGIIVLAVAI</span><span class="topo-outside">LPVLGIGG</span><span class="topo-unknown">MQLYRAEIPGPVKDTK</span><span class="topo-outside">MTPRIAE</span></span>
<span class="topo-line"><span class="topo-outside">TA</span><span class="topo-membrane">KALWYIYLSLTIACAVAFWLAGMT</span><span class="topo-inside">P</span><span class="topo-unknown">FDAISHSFSTIAIGGFST</span><span class="topo-inside">HDASMGYFDS</span><span class="topo-membrane">YAINL</span></span>
<span class="topo-line"><span class="topo-membrane">ITVVFLLISACNFTLHF</span><span class="topo-outside">AAFASGGVHPKYYWKDP</span><span class="topo-membrane">EFRAFIFIQVLLFLVCFLLLLK</span><span class="topo-inside">HHSY</span></span>
<span class="topo-line"><span class="topo-inside">TSP</span><span class="topo-unknown">YDAFDQALFQTVSISTTAGFTTT</span><span class="topo-inside">GFADWP</span><span class="topo-membrane">LFLPVLLLFSSFIGGCAG</span><span class="topo-outside">STGGGMKVIR</span></span>
<span class="topo-line"><span class="topo-outside">ILLLTLQGARELKRLVHPRAVYTIKVGGSALPQRVVDAV</span><span class="topo-membrane">WGFFSAYALVFVVCMLGLIAT</span></span>
<span class="topo-line"><span class="topo-membrane">GMD</span><span class="topo-inside">E</span><span class="topo-unknown">LSAFSAVAATLNNLGPGLG</span><span class="topo-inside">EVALHFGDVND</span><span class="topo-membrane">KAKWVLIVSMLFGRLEIFTLL</span><span class="topo-outside">ILLTP</span></span>
<span class="topo-line"><span class="topo-outside">TFWR</span><span class="topo-unknown">SAAAENLYFQ</span></span>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>31</td>
      <td>7</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>36</td>
      <td>32</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>58</td>
      <td>37</td>
      <td>58</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>59</td>
      <td>69</td>
      <td>59</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>91</td>
      <td>70</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>98</td>
      <td>92</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>116</td>
      <td>99</td>
      <td>116</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>117</td>
      <td>125</td>
      <td>117</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>126</td>
      <td>149</td>
      <td>126</td>
      <td>149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>157</td>
      <td>150</td>
      <td>157</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>173</td>
      <td>158</td>
      <td>173</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>174</td>
      <td>182</td>
      <td>174</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>206</td>
      <td>183</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>207</td>
      <td>207</td>
      <td>207</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>225</td>
      <td>208</td>
      <td>225</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>226</td>
      <td>235</td>
      <td>226</td>
      <td>235</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>257</td>
      <td>236</td>
      <td>257</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>258</td>
      <td>274</td>
      <td>258</td>
      <td>274</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>296</td>
      <td>275</td>
      <td>296</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>297</td>
      <td>303</td>
      <td>297</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>304</td>
      <td>326</td>
      <td>304</td>
      <td>326</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>327</td>
      <td>332</td>
      <td>327</td>
      <td>332</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>350</td>
      <td>333</td>
      <td>350</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>351</td>
      <td>399</td>
      <td>351</td>
      <td>399</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>423</td>
      <td>400</td>
      <td>423</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>424</td>
      <td>424</td>
      <td>424</td>
      <td>424</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>425</td>
      <td>443</td>
      <td>425</td>
      <td>443</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>444</td>
      <td>454</td>
      <td>444</td>
      <td>454</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>455</td>
      <td>475</td>
      <td>455</td>
      <td>475</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>476</td>
      <td>484</td>
      <td>476</td>
      <td>484</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>485</td>
      <td>494</td>
      <td>485</td>
      <td>494</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3pjz">3PJZ</a> — Chain B (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">MQFRSI</span><span class="topo-membrane">IRIVGLLLALFSVTMLAPALVALLY</span><span class="topo-inside">RDGAG</span><span class="topo-membrane">VPFVTTFFVLLFCGAMCWFPNR</span><span class="topo-outside">RH</span></span>
<span class="topo-line"><span class="topo-outside">KHELKSRDG</span><span class="topo-membrane">FLIVVLFWTVLGSAGSLPFLIA</span><span class="topo-inside">DNPNISV</span><span class="topo-unknown">TDAFFESFSALTTTGATV</span><span class="topo-inside">IVGL</span></span>
<span class="topo-line"><span class="topo-inside">DELPK</span><span class="topo-membrane">AILFYRQFLQWFGGMGIIVLAV</span><span class="topo-outside">AILPVLGIGG</span><span class="topo-unknown">MQLYRAEIPGPVKDTK</span><span class="topo-outside">MTPRIAE</span></span>
<span class="topo-line"><span class="topo-outside">TA</span><span class="topo-membrane">KALWYIYLSLTIACAVAFWLAGMT</span><span class="topo-inside">P</span><span class="topo-unknown">FDAISHSFSTIAIGGFST</span><span class="topo-inside">HDASMGYFDS</span><span class="topo-membrane">YAINL</span></span>
<span class="topo-line"><span class="topo-membrane">ITVVFLLISACNFTLHF</span><span class="topo-outside">AAFASGGVHPKYYWKDP</span><span class="topo-membrane">EFRAFIFIQVLLFLVCFLLLLK</span><span class="topo-inside">HHSY</span></span>
<span class="topo-line"><span class="topo-inside">TSP</span><span class="topo-unknown">YDAFDQALFQTVSISTTAGFTTT</span><span class="topo-inside">GFADWP</span><span class="topo-membrane">LFLPVLLLFSSFIGGCAG</span><span class="topo-outside">STGGGMKVIR</span></span>
<span class="topo-line"><span class="topo-outside">ILLLTLQGARELKRLVHPRAVYTIKVGGSALPQRVVDAV</span><span class="topo-membrane">WGFFSAYALVFVVCMLGLIAT</span></span>
<span class="topo-line"><span class="topo-membrane">GMD</span><span class="topo-inside">E</span><span class="topo-unknown">LSAFSAVAATLNNLGPGLG</span><span class="topo-inside">EVALHFGDVND</span><span class="topo-membrane">KAKWVLIVSMLFGRLEIFTLL</span><span class="topo-outside">ILLTP</span></span>
<span class="topo-line"><span class="topo-outside">TFWR</span><span class="topo-unknown">SAAAENLYFQ</span></span>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>31</td>
      <td>7</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>36</td>
      <td>32</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>58</td>
      <td>37</td>
      <td>58</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>59</td>
      <td>69</td>
      <td>59</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>91</td>
      <td>70</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>98</td>
      <td>92</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>116</td>
      <td>99</td>
      <td>116</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>117</td>
      <td>125</td>
      <td>117</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>126</td>
      <td>147</td>
      <td>126</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>157</td>
      <td>148</td>
      <td>157</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>173</td>
      <td>158</td>
      <td>173</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>174</td>
      <td>182</td>
      <td>174</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>206</td>
      <td>183</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>207</td>
      <td>207</td>
      <td>207</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>225</td>
      <td>208</td>
      <td>225</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>226</td>
      <td>235</td>
      <td>226</td>
      <td>235</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>257</td>
      <td>236</td>
      <td>257</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>258</td>
      <td>274</td>
      <td>258</td>
      <td>274</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>296</td>
      <td>275</td>
      <td>296</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>297</td>
      <td>303</td>
      <td>297</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>304</td>
      <td>326</td>
      <td>304</td>
      <td>326</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>327</td>
      <td>332</td>
      <td>327</td>
      <td>332</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>350</td>
      <td>333</td>
      <td>350</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>351</td>
      <td>399</td>
      <td>351</td>
      <td>399</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>423</td>
      <td>400</td>
      <td>423</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>424</td>
      <td>424</td>
      <td>424</td>
      <td>424</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>425</td>
      <td>443</td>
      <td>425</td>
      <td>443</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>444</td>
      <td>454</td>
      <td>444</td>
      <td>454</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>455</td>
      <td>475</td>
      <td>455</td>
      <td>475</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>476</td>
      <td>484</td>
      <td>476</td>
      <td>484</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>485</td>
      <td>494</td>
      <td>485</td>
      <td>494</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3pjz">3PJZ</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">MQFRSI</span><span class="topo-membrane">IRIVGLLLALFSVTMLAPALVALLY</span><span class="topo-inside">RDGAG</span><span class="topo-membrane">VPFVTTFFVLLFCGAMCWFPNR</span><span class="topo-outside">RH</span></span>
<span class="topo-line"><span class="topo-outside">KHELKSRDG</span><span class="topo-membrane">FLIVVLFWTVLGSAGSLPFLIA</span><span class="topo-inside">DNPNISV</span><span class="topo-unknown">TDAFFESFSALTTTGATV</span><span class="topo-inside">IVGL</span></span>
<span class="topo-line"><span class="topo-inside">DELPK</span><span class="topo-membrane">AILFYRQFLQWFGGMGIIVLAVAI</span><span class="topo-outside">LPVLGIGG</span><span class="topo-unknown">MQLYRAEIPGPVKDTK</span><span class="topo-outside">MTPRIAE</span></span>
<span class="topo-line"><span class="topo-outside">TA</span><span class="topo-membrane">KALWYIYLSLTIACAVAFWLAGMT</span><span class="topo-inside">P</span><span class="topo-unknown">FDAISHSFSTIAIGGFST</span><span class="topo-inside">HDASMGYFDS</span><span class="topo-membrane">YAINL</span></span>
<span class="topo-line"><span class="topo-membrane">ITVVFLLISACNFTLHF</span><span class="topo-outside">AAFASGGVHPKYYWKDP</span><span class="topo-membrane">EFRAFIFIQVLLFLVCFLLLLK</span><span class="topo-inside">HHSY</span></span>
<span class="topo-line"><span class="topo-inside">TSP</span><span class="topo-unknown">YDAFDQALFQTVSISTTAGFTTT</span><span class="topo-inside">GFADWP</span><span class="topo-membrane">LFLPVLLLFSSFIGGCAG</span><span class="topo-outside">STGGGMKVIR</span></span>
<span class="topo-line"><span class="topo-outside">ILLLTLQGARELKRLVHPRAVYTIKVGGSALPQRVVDAV</span><span class="topo-membrane">WGFFSAYALVFVVCMLGLIAT</span></span>
<span class="topo-line"><span class="topo-membrane">GMD</span><span class="topo-inside">E</span><span class="topo-unknown">LSAFSAVAATLNNLGPGLG</span><span class="topo-inside">EVALHFGDVND</span><span class="topo-membrane">KAKWVLIVSMLFGRLEIFTLL</span><span class="topo-outside">ILLTP</span></span>
<span class="topo-line"><span class="topo-outside">TFWR</span><span class="topo-unknown">SAAAENLYFQ</span></span>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>31</td>
      <td>7</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>36</td>
      <td>32</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>58</td>
      <td>37</td>
      <td>58</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>59</td>
      <td>69</td>
      <td>59</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>91</td>
      <td>70</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>98</td>
      <td>92</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>116</td>
      <td>99</td>
      <td>116</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>117</td>
      <td>125</td>
      <td>117</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>126</td>
      <td>149</td>
      <td>126</td>
      <td>149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>157</td>
      <td>150</td>
      <td>157</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>173</td>
      <td>158</td>
      <td>173</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>174</td>
      <td>182</td>
      <td>174</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>206</td>
      <td>183</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>207</td>
      <td>207</td>
      <td>207</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>225</td>
      <td>208</td>
      <td>225</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>226</td>
      <td>235</td>
      <td>226</td>
      <td>235</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>257</td>
      <td>236</td>
      <td>257</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>258</td>
      <td>274</td>
      <td>258</td>
      <td>274</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>296</td>
      <td>275</td>
      <td>296</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>297</td>
      <td>303</td>
      <td>297</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>304</td>
      <td>326</td>
      <td>304</td>
      <td>326</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>327</td>
      <td>332</td>
      <td>327</td>
      <td>332</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>350</td>
      <td>333</td>
      <td>350</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>351</td>
      <td>399</td>
      <td>351</td>
      <td>399</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>423</td>
      <td>400</td>
      <td>423</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>424</td>
      <td>424</td>
      <td>424</td>
      <td>424</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>425</td>
      <td>443</td>
      <td>425</td>
      <td>443</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>444</td>
      <td>454</td>
      <td>444</td>
      <td>454</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>455</td>
      <td>475</td>
      <td>455</td>
      <td>475</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>476</td>
      <td>484</td>
      <td>476</td>
      <td>484</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>485</td>
      <td>494</td>
      <td>485</td>
      <td>494</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3pjz">3PJZ</a> — Chain B (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">MQFRSI</span><span class="topo-membrane">IRIVGLLLALFSVTMLAPALVALLY</span><span class="topo-inside">RDGAG</span><span class="topo-membrane">VPFVTTFFVLLFCGAMCWFPNR</span><span class="topo-outside">RH</span></span>
<span class="topo-line"><span class="topo-outside">KHELKSRDG</span><span class="topo-membrane">FLIVVLFWTVLGSAGSLPFLIA</span><span class="topo-inside">DNPNISV</span><span class="topo-unknown">TDAFFESFSALTTTGATV</span><span class="topo-inside">IVGL</span></span>
<span class="topo-line"><span class="topo-inside">DELPK</span><span class="topo-membrane">AILFYRQFLQWFGGMGIIVLAV</span><span class="topo-outside">AILPVLGIGG</span><span class="topo-unknown">MQLYRAEIPGPVKDTK</span><span class="topo-outside">MTPRIAE</span></span>
<span class="topo-line"><span class="topo-outside">TA</span><span class="topo-membrane">KALWYIYLSLTIACAVAFWLAGMT</span><span class="topo-inside">P</span><span class="topo-unknown">FDAISHSFSTIAIGGFST</span><span class="topo-inside">HDASMGYFDS</span><span class="topo-membrane">YAINL</span></span>
<span class="topo-line"><span class="topo-membrane">ITVVFLLISACNFTLHF</span><span class="topo-outside">AAFASGGVHPKYYWKDP</span><span class="topo-membrane">EFRAFIFIQVLLFLVCFLLLLK</span><span class="topo-inside">HHSY</span></span>
<span class="topo-line"><span class="topo-inside">TSP</span><span class="topo-unknown">YDAFDQALFQTVSISTTAGFTTT</span><span class="topo-inside">GFADWP</span><span class="topo-membrane">LFLPVLLLFSSFIGGCAG</span><span class="topo-outside">STGGGMKVIR</span></span>
<span class="topo-line"><span class="topo-outside">ILLLTLQGARELKRLVHPRAVYTIKVGGSALPQRVVDAV</span><span class="topo-membrane">WGFFSAYALVFVVCMLGLIAT</span></span>
<span class="topo-line"><span class="topo-membrane">GMD</span><span class="topo-inside">E</span><span class="topo-unknown">LSAFSAVAATLNNLGPGLG</span><span class="topo-inside">EVALHFGDVND</span><span class="topo-membrane">KAKWVLIVSMLFGRLEIFTLL</span><span class="topo-outside">ILLTP</span></span>
<span class="topo-line"><span class="topo-outside">TFWR</span><span class="topo-unknown">SAAAENLYFQ</span></span>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>31</td>
      <td>7</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>36</td>
      <td>32</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>58</td>
      <td>37</td>
      <td>58</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>59</td>
      <td>69</td>
      <td>59</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>91</td>
      <td>70</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>98</td>
      <td>92</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>116</td>
      <td>99</td>
      <td>116</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>117</td>
      <td>125</td>
      <td>117</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>126</td>
      <td>147</td>
      <td>126</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>157</td>
      <td>148</td>
      <td>157</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>173</td>
      <td>158</td>
      <td>173</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>174</td>
      <td>182</td>
      <td>174</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>206</td>
      <td>183</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>207</td>
      <td>207</td>
      <td>207</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>225</td>
      <td>208</td>
      <td>225</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>226</td>
      <td>235</td>
      <td>226</td>
      <td>235</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>257</td>
      <td>236</td>
      <td>257</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>258</td>
      <td>274</td>
      <td>258</td>
      <td>274</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>296</td>
      <td>275</td>
      <td>296</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>297</td>
      <td>303</td>
      <td>297</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>304</td>
      <td>326</td>
      <td>304</td>
      <td>326</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>327</td>
      <td>332</td>
      <td>327</td>
      <td>332</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>350</td>
      <td>333</td>
      <td>350</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>351</td>
      <td>399</td>
      <td>351</td>
      <td>399</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>423</td>
      <td>400</td>
      <td>423</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>424</td>
      <td>424</td>
      <td>424</td>
      <td>424</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>425</td>
      <td>443</td>
      <td>425</td>
      <td>443</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>444</td>
      <td>454</td>
      <td>444</td>
      <td>454</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>455</td>
      <td>475</td>
      <td>455</td>
      <td>475</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>476</td>
      <td>484</td>
      <td>476</td>
      <td>484</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>485</td>
      <td>494</td>
      <td>485</td>
      <td>494</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3pjz">3PJZ</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">MQFRSI</span><span class="topo-membrane">IRIVGLLLALFSVTMLAPALVALLY</span><span class="topo-inside">RDGAG</span><span class="topo-membrane">VPFVTTFFVLLFCGAMCWFPNR</span><span class="topo-outside">RH</span></span>
<span class="topo-line"><span class="topo-outside">KHELKSRDG</span><span class="topo-membrane">FLIVVLFWTVLGSAGSLPFLIA</span><span class="topo-inside">DNPNISV</span><span class="topo-unknown">TDAFFESFSALTTTGATV</span><span class="topo-inside">IVGL</span></span>
<span class="topo-line"><span class="topo-inside">DELPK</span><span class="topo-membrane">AILFYRQFLQWFGGMGIIVLAVAI</span><span class="topo-outside">LPVLGIGG</span><span class="topo-unknown">MQLYRAEIPGPVKDTK</span><span class="topo-outside">MTPRIAE</span></span>
<span class="topo-line"><span class="topo-outside">TA</span><span class="topo-membrane">KALWYIYLSLTIACAVAFWLAGMT</span><span class="topo-inside">P</span><span class="topo-unknown">FDAISHSFSTIAIGGFST</span><span class="topo-inside">HDASMGYFDS</span><span class="topo-membrane">YAINL</span></span>
<span class="topo-line"><span class="topo-membrane">ITVVFLLISACNFTLHF</span><span class="topo-outside">AAFASGGVHPKYYWKDP</span><span class="topo-membrane">EFRAFIFIQVLLFLVCFLLLLK</span><span class="topo-inside">HHSY</span></span>
<span class="topo-line"><span class="topo-inside">TSP</span><span class="topo-unknown">YDAFDQALFQTVSISTTAGFTTT</span><span class="topo-inside">GFADWP</span><span class="topo-membrane">LFLPVLLLFSSFIGGCAG</span><span class="topo-outside">STGGGMKVIR</span></span>
<span class="topo-line"><span class="topo-outside">ILLLTLQGARELKRLVHPRAVYTIKVGGSALPQRVVDAV</span><span class="topo-membrane">WGFFSAYALVFVVCMLGLIAT</span></span>
<span class="topo-line"><span class="topo-membrane">GMD</span><span class="topo-inside">E</span><span class="topo-unknown">LSAFSAVAATLNNLGPGLG</span><span class="topo-inside">EVALHFGDVND</span><span class="topo-membrane">KAKWVLIVSMLFGRLEIFTLL</span><span class="topo-outside">ILLTP</span></span>
<span class="topo-line"><span class="topo-outside">TFWR</span><span class="topo-unknown">SAAAENLYFQ</span></span>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>31</td>
      <td>7</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>36</td>
      <td>32</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>58</td>
      <td>37</td>
      <td>58</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>59</td>
      <td>69</td>
      <td>59</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>91</td>
      <td>70</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>98</td>
      <td>92</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>116</td>
      <td>99</td>
      <td>116</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>117</td>
      <td>125</td>
      <td>117</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>126</td>
      <td>149</td>
      <td>126</td>
      <td>149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>157</td>
      <td>150</td>
      <td>157</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>173</td>
      <td>158</td>
      <td>173</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>174</td>
      <td>182</td>
      <td>174</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>206</td>
      <td>183</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>207</td>
      <td>207</td>
      <td>207</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>225</td>
      <td>208</td>
      <td>225</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>226</td>
      <td>235</td>
      <td>226</td>
      <td>235</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>257</td>
      <td>236</td>
      <td>257</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>258</td>
      <td>274</td>
      <td>258</td>
      <td>274</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>296</td>
      <td>275</td>
      <td>296</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>297</td>
      <td>303</td>
      <td>297</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>304</td>
      <td>326</td>
      <td>304</td>
      <td>326</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>327</td>
      <td>332</td>
      <td>327</td>
      <td>332</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>350</td>
      <td>333</td>
      <td>350</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>351</td>
      <td>399</td>
      <td>351</td>
      <td>399</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>423</td>
      <td>400</td>
      <td>423</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>424</td>
      <td>424</td>
      <td>424</td>
      <td>424</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>425</td>
      <td>443</td>
      <td>425</td>
      <td>443</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>444</td>
      <td>454</td>
      <td>444</td>
      <td>454</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>455</td>
      <td>475</td>
      <td>455</td>
      <td>475</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>476</td>
      <td>484</td>
      <td>476</td>
      <td>484</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>485</td>
      <td>494</td>
      <td>485</td>
      <td>494</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3pjz">3PJZ</a> — Chain B (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">MQFRSI</span><span class="topo-membrane">IRIVGLLLALFSVTMLAPALVALLY</span><span class="topo-inside">RDGAG</span><span class="topo-membrane">VPFVTTFFVLLFCGAMCWFPNR</span><span class="topo-outside">RH</span></span>
<span class="topo-line"><span class="topo-outside">KHELKSRDG</span><span class="topo-membrane">FLIVVLFWTVLGSAGSLPFLIA</span><span class="topo-inside">DNPNISV</span><span class="topo-unknown">TDAFFESFSALTTTGATV</span><span class="topo-inside">IVGL</span></span>
<span class="topo-line"><span class="topo-inside">DELPK</span><span class="topo-membrane">AILFYRQFLQWFGGMGIIVLAV</span><span class="topo-outside">AILPVLGIGG</span><span class="topo-unknown">MQLYRAEIPGPVKDTK</span><span class="topo-outside">MTPRIAE</span></span>
<span class="topo-line"><span class="topo-outside">TA</span><span class="topo-membrane">KALWYIYLSLTIACAVAFWLAGMT</span><span class="topo-inside">P</span><span class="topo-unknown">FDAISHSFSTIAIGGFST</span><span class="topo-inside">HDASMGYFDS</span><span class="topo-membrane">YAINL</span></span>
<span class="topo-line"><span class="topo-membrane">ITVVFLLISACNFTLHF</span><span class="topo-outside">AAFASGGVHPKYYWKDP</span><span class="topo-membrane">EFRAFIFIQVLLFLVCFLLLLK</span><span class="topo-inside">HHSY</span></span>
<span class="topo-line"><span class="topo-inside">TSP</span><span class="topo-unknown">YDAFDQALFQTVSISTTAGFTTT</span><span class="topo-inside">GFADWP</span><span class="topo-membrane">LFLPVLLLFSSFIGGCAG</span><span class="topo-outside">STGGGMKVIR</span></span>
<span class="topo-line"><span class="topo-outside">ILLLTLQGARELKRLVHPRAVYTIKVGGSALPQRVVDAV</span><span class="topo-membrane">WGFFSAYALVFVVCMLGLIAT</span></span>
<span class="topo-line"><span class="topo-membrane">GMD</span><span class="topo-inside">E</span><span class="topo-unknown">LSAFSAVAATLNNLGPGLG</span><span class="topo-inside">EVALHFGDVND</span><span class="topo-membrane">KAKWVLIVSMLFGRLEIFTLL</span><span class="topo-outside">ILLTP</span></span>
<span class="topo-line"><span class="topo-outside">TFWR</span><span class="topo-unknown">SAAAENLYFQ</span></span>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>31</td>
      <td>7</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>36</td>
      <td>32</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>58</td>
      <td>37</td>
      <td>58</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>59</td>
      <td>69</td>
      <td>59</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>91</td>
      <td>70</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>98</td>
      <td>92</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>116</td>
      <td>99</td>
      <td>116</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>117</td>
      <td>125</td>
      <td>117</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>126</td>
      <td>147</td>
      <td>126</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>157</td>
      <td>148</td>
      <td>157</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>173</td>
      <td>158</td>
      <td>173</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>174</td>
      <td>182</td>
      <td>174</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>206</td>
      <td>183</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>207</td>
      <td>207</td>
      <td>207</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>225</td>
      <td>208</td>
      <td>225</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>226</td>
      <td>235</td>
      <td>226</td>
      <td>235</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>257</td>
      <td>236</td>
      <td>257</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>258</td>
      <td>274</td>
      <td>258</td>
      <td>274</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>296</td>
      <td>275</td>
      <td>296</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>297</td>
      <td>303</td>
      <td>297</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>304</td>
      <td>326</td>
      <td>304</td>
      <td>326</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>327</td>
      <td>332</td>
      <td>327</td>
      <td>332</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>350</td>
      <td>333</td>
      <td>350</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>351</td>
      <td>399</td>
      <td>351</td>
      <td>399</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>423</td>
      <td>400</td>
      <td>423</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>424</td>
      <td>424</td>
      <td>424</td>
      <td>424</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>425</td>
      <td>443</td>
      <td>425</td>
      <td>443</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>444</td>
      <td>454</td>
      <td>444</td>
      <td>454</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>455</td>
      <td>475</td>
      <td>455</td>
      <td>475</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>476</td>
      <td>484</td>
      <td>476</td>
      <td>484</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>485</td>
      <td>494</td>
      <td>485</td>
      <td>494</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3pjz">3PJZ</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">MQFRSI</span><span class="topo-membrane">IRIVGLLLALFSVTMLAPALVALLY</span><span class="topo-inside">RDGAG</span><span class="topo-membrane">VPFVTTFFVLLFCGAMCWFPNR</span><span class="topo-outside">RH</span></span>
<span class="topo-line"><span class="topo-outside">KHELKSRDG</span><span class="topo-membrane">FLIVVLFWTVLGSAGSLPFLIA</span><span class="topo-inside">DNPNISV</span><span class="topo-unknown">TDAFFESFSALTTTGATV</span><span class="topo-inside">IVGL</span></span>
<span class="topo-line"><span class="topo-inside">DELPK</span><span class="topo-membrane">AILFYRQFLQWFGGMGIIVLAVAI</span><span class="topo-outside">LPVLGIGG</span><span class="topo-unknown">MQLYRAEIPGPVKDTK</span><span class="topo-outside">MTPRIAE</span></span>
<span class="topo-line"><span class="topo-outside">TA</span><span class="topo-membrane">KALWYIYLSLTIACAVAFWLAGMT</span><span class="topo-inside">P</span><span class="topo-unknown">FDAISHSFSTIAIGGFST</span><span class="topo-inside">HDASMGYFDS</span><span class="topo-membrane">YAINL</span></span>
<span class="topo-line"><span class="topo-membrane">ITVVFLLISACNFTLHF</span><span class="topo-outside">AAFASGGVHPKYYWKDP</span><span class="topo-membrane">EFRAFIFIQVLLFLVCFLLLLK</span><span class="topo-inside">HHSY</span></span>
<span class="topo-line"><span class="topo-inside">TSP</span><span class="topo-unknown">YDAFDQALFQTVSISTTAGFTTT</span><span class="topo-inside">GFADWP</span><span class="topo-membrane">LFLPVLLLFSSFIGGCAG</span><span class="topo-outside">STGGGMKVIR</span></span>
<span class="topo-line"><span class="topo-outside">ILLLTLQGARELKRLVHPRAVYTIKVGGSALPQRVVDAV</span><span class="topo-membrane">WGFFSAYALVFVVCMLGLIAT</span></span>
<span class="topo-line"><span class="topo-membrane">GMD</span><span class="topo-inside">E</span><span class="topo-unknown">LSAFSAVAATLNNLGPGLG</span><span class="topo-inside">EVALHFGDVND</span><span class="topo-membrane">KAKWVLIVSMLFGRLEIFTLL</span><span class="topo-outside">ILLTP</span></span>
<span class="topo-line"><span class="topo-outside">TFWR</span><span class="topo-unknown">SAAAENLYFQ</span></span>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>31</td>
      <td>7</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>36</td>
      <td>32</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>58</td>
      <td>37</td>
      <td>58</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>59</td>
      <td>69</td>
      <td>59</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>91</td>
      <td>70</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>98</td>
      <td>92</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>116</td>
      <td>99</td>
      <td>116</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>117</td>
      <td>125</td>
      <td>117</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>126</td>
      <td>149</td>
      <td>126</td>
      <td>149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>157</td>
      <td>150</td>
      <td>157</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>173</td>
      <td>158</td>
      <td>173</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>174</td>
      <td>182</td>
      <td>174</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>206</td>
      <td>183</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>207</td>
      <td>207</td>
      <td>207</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>225</td>
      <td>208</td>
      <td>225</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>226</td>
      <td>235</td>
      <td>226</td>
      <td>235</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>257</td>
      <td>236</td>
      <td>257</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>258</td>
      <td>274</td>
      <td>258</td>
      <td>274</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>296</td>
      <td>275</td>
      <td>296</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>297</td>
      <td>303</td>
      <td>297</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>304</td>
      <td>326</td>
      <td>304</td>
      <td>326</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>327</td>
      <td>332</td>
      <td>327</td>
      <td>332</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>350</td>
      <td>333</td>
      <td>350</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>351</td>
      <td>399</td>
      <td>351</td>
      <td>399</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>423</td>
      <td>400</td>
      <td>423</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>424</td>
      <td>424</td>
      <td>424</td>
      <td>424</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>425</td>
      <td>443</td>
      <td>425</td>
      <td>443</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>444</td>
      <td>454</td>
      <td>444</td>
      <td>454</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>455</td>
      <td>475</td>
      <td>455</td>
      <td>475</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>476</td>
      <td>484</td>
      <td>476</td>
      <td>484</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>485</td>
      <td>494</td>
      <td>485</td>
      <td>494</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3pjz">3PJZ</a> — Chain B (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">MQFRSI</span><span class="topo-membrane">IRIVGLLLALFSVTMLAPALVALLY</span><span class="topo-inside">RDGAG</span><span class="topo-membrane">VPFVTTFFVLLFCGAMCWFPNR</span><span class="topo-outside">RH</span></span>
<span class="topo-line"><span class="topo-outside">KHELKSRDG</span><span class="topo-membrane">FLIVVLFWTVLGSAGSLPFLIA</span><span class="topo-inside">DNPNISV</span><span class="topo-unknown">TDAFFESFSALTTTGATV</span><span class="topo-inside">IVGL</span></span>
<span class="topo-line"><span class="topo-inside">DELPK</span><span class="topo-membrane">AILFYRQFLQWFGGMGIIVLAV</span><span class="topo-outside">AILPVLGIGG</span><span class="topo-unknown">MQLYRAEIPGPVKDTK</span><span class="topo-outside">MTPRIAE</span></span>
<span class="topo-line"><span class="topo-outside">TA</span><span class="topo-membrane">KALWYIYLSLTIACAVAFWLAGMT</span><span class="topo-inside">P</span><span class="topo-unknown">FDAISHSFSTIAIGGFST</span><span class="topo-inside">HDASMGYFDS</span><span class="topo-membrane">YAINL</span></span>
<span class="topo-line"><span class="topo-membrane">ITVVFLLISACNFTLHF</span><span class="topo-outside">AAFASGGVHPKYYWKDP</span><span class="topo-membrane">EFRAFIFIQVLLFLVCFLLLLK</span><span class="topo-inside">HHSY</span></span>
<span class="topo-line"><span class="topo-inside">TSP</span><span class="topo-unknown">YDAFDQALFQTVSISTTAGFTTT</span><span class="topo-inside">GFADWP</span><span class="topo-membrane">LFLPVLLLFSSFIGGCAG</span><span class="topo-outside">STGGGMKVIR</span></span>
<span class="topo-line"><span class="topo-outside">ILLLTLQGARELKRLVHPRAVYTIKVGGSALPQRVVDAV</span><span class="topo-membrane">WGFFSAYALVFVVCMLGLIAT</span></span>
<span class="topo-line"><span class="topo-membrane">GMD</span><span class="topo-inside">E</span><span class="topo-unknown">LSAFSAVAATLNNLGPGLG</span><span class="topo-inside">EVALHFGDVND</span><span class="topo-membrane">KAKWVLIVSMLFGRLEIFTLL</span><span class="topo-outside">ILLTP</span></span>
<span class="topo-line"><span class="topo-outside">TFWR</span><span class="topo-unknown">SAAAENLYFQ</span></span>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>31</td>
      <td>7</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>36</td>
      <td>32</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>58</td>
      <td>37</td>
      <td>58</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>59</td>
      <td>69</td>
      <td>59</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>91</td>
      <td>70</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>98</td>
      <td>92</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>116</td>
      <td>99</td>
      <td>116</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>117</td>
      <td>125</td>
      <td>117</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>126</td>
      <td>147</td>
      <td>126</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>157</td>
      <td>148</td>
      <td>157</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>173</td>
      <td>158</td>
      <td>173</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>174</td>
      <td>182</td>
      <td>174</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>206</td>
      <td>183</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>207</td>
      <td>207</td>
      <td>207</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>225</td>
      <td>208</td>
      <td>225</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>226</td>
      <td>235</td>
      <td>226</td>
      <td>235</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>257</td>
      <td>236</td>
      <td>257</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>258</td>
      <td>274</td>
      <td>258</td>
      <td>274</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>296</td>
      <td>275</td>
      <td>296</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>297</td>
      <td>303</td>
      <td>297</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>304</td>
      <td>326</td>
      <td>304</td>
      <td>326</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>327</td>
      <td>332</td>
      <td>327</td>
      <td>332</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>350</td>
      <td>333</td>
      <td>350</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>351</td>
      <td>399</td>
      <td>351</td>
      <td>399</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>423</td>
      <td>400</td>
      <td>423</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>424</td>
      <td>424</td>
      <td>424</td>
      <td>424</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>425</td>
      <td>443</td>
      <td>425</td>
      <td>443</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>444</td>
      <td>454</td>
      <td>444</td>
      <td>454</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>455</td>
      <td>475</td>
      <td>455</td>
      <td>475</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>476</td>
      <td>484</td>
      <td>476</td>
      <td>484</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>485</td>
      <td>494</td>
      <td>485</td>
      <td>494</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### First structure of a Trk family potassium channel

VpTrkH represents the first high-resolution crystal structure of a Trk family
potassium ion channel. The structure reveals a homodimeric architecture with
each protomer containing five domains (D0-D4). Domains D0-D3 each consist of
two transmembrane helices (M1-M2) forming a peripheral ring around the central
ion conduction pore formed by D4. The overall fold is distinct from other
potassium channels but the selectivity filter shares structural similarity with
[KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/).

### Selectivity filter architecture

The VpTrkH selectivity filter contains the conserved TVGYG sequence motif,
similar to [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) and other K+ channels. However, the pore helix dipole is
oriented differently compared to [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/), with the positive end of the helix
dipole directed away from the selectivity filter rather than toward it. This
suggests that the mechanism of ion selectivity and conduction in [TRKH](/xray-mp-wiki/proteins/pumps-atpases/trkh/) may
differ from canonical potassium channels. The electron density in the
selectivity filter reveals a single K+ ion binding site rather than the
multiple sites observed in [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/).

### Dimeric architecture and domain organization

VpTrkH forms a homodimer with each protomer comprising ~480 residues organized
into five domains (D0-D4). Domains D0-D3 form a peripheral collar surrounding
the central D4 pore domain. The D4 domain from each protomer contributes a
pore helix and selectivity filter. The dimer interface is formed primarily by
D4M1 and the D4 pore helix from both protomers, creating a hydrophobic seal
at the center of the dimer interface. An intramembrane loop between D3M2 and
D4M1 contains conserved [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) residues and forms a constriction at the
permeation pathway.

### Ion permeation pathway

The ion conduction pathway of VpTrkH passes through the D4 pore domain, with
the selectivity filter at the extracellular side. The permeation pathway is
constricted at the intracellular side by an intramembrane loop, with Arg468
and Glu470 forming a narrow constriction. This constriction may regulate ion
access to the selectivity filter. The large central cavity is sealed off from
the lipid bilayer by hydrophobic residues at the dimer interface.

### Comparison with KcsA potassium channel

Despite sharing the TVGYG selectivity filter motif, VpTrkH and [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) have
markedly different overall architectures. [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) is a tetramer with each subunit
contributing one pore domain, while VpTrkH is a dimer with each protomer
contributing its own pore domain. The pore helix orientation differs between
the two channels, with the [TRKH](/xray-mp-wiki/proteins/pumps-atpases/trkh/) pore helix dipole oriented away from the
selectivity filter. These differences suggest that [TRKH](/xray-mp-wiki/proteins/pumps-atpases/trkh/) may utilize a distinct
mechanism for K+ selectivity and conduction compared to the canonical KcsA-like
channels.


## Cross-References

- <a href="/xray-mp-wiki/proteins/pumps-atpases/trkh/">TrkH (Potassium Channel from Klebsiella pneumoniae)</a> — Homologous TrkH potassium channel from a different bacterial species; VpTrkH provides the first high-resolution structure defining the TrkH fold
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/">KcsA Potassium Channel</a> — KcsA is the canonical potassium channel used for structural comparison of selectivity filter architecture
- <a href="/xray-mp-wiki/proteins/pumps-atpases/trka/">TrkA (ATP-binding Regulatory Subunit from Klebsiella pneumoniae)</a> — TrkA is the cytoplasmic regulatory subunit that associates with TrkH to form the functional K+ transporter complex
- <a href="/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/">Single-Wavelength Anomalous Diffraction</a> — Structure solved by SeMet SAD phasing (3.9 A SeMet data)
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine (SeMet)</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/glycine/">Glycine</a> — Buffer component in purification or crystallization
