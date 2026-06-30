---
title: "TrkH (Potassium Channel from Klebsiella pneumoniae)"
created: 2026-06-03
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature12056]
verified: false
---

# TrkH (Potassium Channel from Klebsiella pneumoniae)

## Overview

TrkH is a potassium channel protein from the bacterium Klebsiella pneumoniae that forms a homodimer and associates with the cytoplasmic ATPase [TRKA](/xray-mp-wiki/proteins/trka) to form the functional TrkH-[TRKA](/xray-mp-wiki/proteins/trka) potassium transporter complex. TrkH contains a single transmembrane helix per subunit in the membrane and a large cytoplasmic domain that forms a dimeric structure. The channel conducts monovalent cations including K+, Na+, and Li+ and is regulated by [ATP](/xray-mp-wiki/reagents/ligands/atp) and [ADP](/xray-mp-wiki/reagents/ligands/adp) through binding to the associated [TRKA](/xray-mp-wiki/proteins/trka) subunit.


## Publications

### doi/10.1038##nature12056

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4j9u">4J9U</a></td>
      <td>3.8</td>
      <td>P21</td>
      <td>TrkH-TrkA complex, TrkH subunit, 28,063 protein atoms in asymmetric unit</td>
      <td>NADH</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3pjz">3PJZ</a></td>
      <td>Not specified</td>
      <td>Not specified</td>
      <td>Isolated TrkH, compared with TrkH in TrkH-TrkA complex</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

**Purification:**

- **Expression system**: Not specified
- **Expression construct**: His-tagged TrkH-[TRKA](/xray-mp-wiki/proteins/trka) complex
- **Tag info**: His-tag

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
      <td>Affinity chromatography</td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Co2+ IMAC column</td>
      <td></td>
      <td>His-tagged TrkH-<a href="/xray-mp-wiki/proteins/trka">TRKA</a> complex purified on Co2+ IMAC</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td>--</td>
      <td></td>
      <td>10.2 mL peak fraction collected; TrkH and <a href="/xray-mp-wiki/proteins/trka">TRKA</a> both ~50 kD by SDS-PAGE</td>
    </tr>
  </tbody>
</table>
**Final sample**: TrkH-[TRKA](/xray-mp-wiki/proteins/trka) complex, both subunits ~50 kD

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>TrkH-<a href="/xray-mp-wiki/proteins/trka">TRKA</a> complex with <a href="/xray-mp-wiki/reagents/cofactors/nadh">NADH</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallized with Ta6Br12 for anomalous phasing; 3.8 A resolution; P21 space group; 28,063 protein atoms in asymmetric unit</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4j9u">4J9U</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MQFRSI</span><span class="topo-membrane">IRIVGLLLALFSVTMLAPALV</span><span class="topo-outside">ALLYRDGAGVP</span><span class="topo-membrane">FVTTFFVLLFCGAMCWFPN</span><span class="topo-inside">RRHKH</span><span class="topo-unknown">ELK</span><span class="topo-inside">SRDGF</span><span class="topo-membrane">LIVVLFWTVLGSAGSLP</span><span class="topo-outside">FLIADNPNISVTDA</span><span class="topo-unknown">FFESFSALTTTGA</span><span class="topo-outside">TVIVGL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">DELPKAILF</span><span class="topo-membrane">YRQFLQWFGGMGIIVLAVA</span><span class="topo-inside">ILPVLGIGGM</span><span class="topo-unknown">QLYRAEIPGPVKDTKMTPR</span><span class="topo-inside">IAETA</span><span class="topo-membrane">KALWYIYLSLTIACAVAFWLA</span><span class="topo-outside">GMTPFDA</span><span class="topo-unknown">ISHSFSTIAIGGFS</span><span class="topo-outside">THDASMGYFDSYA</span><span class="topo-membrane">INL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">ITVVFLLISACNFTLHF</span><span class="topo-inside">AAFASGGVHPKYYWKDP</span><span class="topo-membrane">EFRAFIFIQVLLFLVCFLL</span><span class="topo-outside">LLKHHSYTSPYDAFDQA</span><span class="topo-unknown">LFQTVSISTTAGF</span><span class="topo-outside">TTTGFADWPLF</span><span class="topo-membrane">LPVLLLFSSFIGGCAG</span><span class="topo-inside">STGGGMKVIR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">ILLLTLQGARELKRLVHPRAVYTIKVGGSALPQRVVDAV</span><span class="topo-membrane">WGFFSAYALVFVVCMLGLIA</span><span class="topo-outside">TGMDELSA</span><span class="topo-unknown">FSAVAATLNNLGP</span><span class="topo-outside">GLGEVALHFGDVNDK</span><span class="topo-membrane">AKWVLIVSMLFGRLEIFTLL</span><span class="topo-inside">ILLTP</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-inside">TFWR</span><span class="topo-unknown">S</span></span>
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
      <td>6</td>
      <td>1</td>
      <td>6</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>27</td>
      <td>7</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>38</td>
      <td>28</td>
      <td>38</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>57</td>
      <td>39</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>58</td>
      <td>62</td>
      <td>58</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>65</td>
      <td>63</td>
      <td>65</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>66</td>
      <td>70</td>
      <td>66</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>87</td>
      <td>71</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>101</td>
      <td>88</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>114</td>
      <td>102</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>115</td>
      <td>129</td>
      <td>115</td>
      <td>129</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>148</td>
      <td>130</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>158</td>
      <td>149</td>
      <td>158</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>177</td>
      <td>159</td>
      <td>177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>178</td>
      <td>182</td>
      <td>178</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>203</td>
      <td>183</td>
      <td>203</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>204</td>
      <td>210</td>
      <td>204</td>
      <td>210</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>224</td>
      <td>211</td>
      <td>224</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>225</td>
      <td>237</td>
      <td>225</td>
      <td>237</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>238</td>
      <td>257</td>
      <td>238</td>
      <td>257</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>258</td>
      <td>274</td>
      <td>258</td>
      <td>274</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>293</td>
      <td>275</td>
      <td>293</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>294</td>
      <td>310</td>
      <td>294</td>
      <td>310</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>323</td>
      <td>311</td>
      <td>323</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>324</td>
      <td>334</td>
      <td>324</td>
      <td>334</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>335</td>
      <td>350</td>
      <td>335</td>
      <td>350</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>351</td>
      <td>399</td>
      <td>351</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>419</td>
      <td>400</td>
      <td>419</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>420</td>
      <td>427</td>
      <td>420</td>
      <td>427</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>428</td>
      <td>440</td>
      <td>428</td>
      <td>440</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>441</td>
      <td>455</td>
      <td>441</td>
      <td>455</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>456</td>
      <td>475</td>
      <td>456</td>
      <td>475</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>476</td>
      <td>484</td>
      <td>476</td>
      <td>484</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>485</td>
      <td>485</td>
      <td>485</td>
      <td>485</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4j9u">4J9U</a> — Chain B (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MQFRSI</span><span class="topo-membrane">IRIVGLLLALFSVTMLAPALV</span><span class="topo-outside">ALLYRDGAGVP</span><span class="topo-membrane">FVTTFFVLLFCGAMCWFPN</span><span class="topo-inside">RRHKH</span><span class="topo-unknown">ELK</span><span class="topo-inside">SRDGF</span><span class="topo-membrane">LIVVLFWTVLGSAGSLP</span><span class="topo-outside">FLIADNPNISVTDA</span><span class="topo-unknown">FFESFSALTTTGA</span><span class="topo-outside">TVIVGL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">DELPKAILF</span><span class="topo-membrane">YRQFLQWFGGMGIIVLAVA</span><span class="topo-inside">ILPVLGIGGM</span><span class="topo-unknown">QLYRAEIPGPVKDTKMTPR</span><span class="topo-inside">IAETA</span><span class="topo-membrane">KALWYIYLSLTIACAVAFWLA</span><span class="topo-outside">GMTPFDA</span><span class="topo-unknown">ISHSFSTIAIGGFS</span><span class="topo-outside">THDASMGYFDSYA</span><span class="topo-membrane">INL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">ITVVFLLISACNFTLHF</span><span class="topo-inside">AAFASGGVHPKYYWKDP</span><span class="topo-membrane">EFRAFIFIQVLLFLVCFLL</span><span class="topo-outside">LLKHHSYTSPYDAFDQA</span><span class="topo-unknown">LFQTVSISTTAGF</span><span class="topo-outside">TTTGFADWPLF</span><span class="topo-membrane">LPVLLLFSSFIGGCAG</span><span class="topo-inside">STGGGMKVIR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">ILLLTLQGARELKRLVHPRAVYTIKVGGSALPQRVVDAV</span><span class="topo-membrane">WGFFSAYALVFVVCMLGLIA</span><span class="topo-outside">TGMDELSA</span><span class="topo-unknown">FSAVAATLNNLGP</span><span class="topo-outside">GLGEVALHFGDVNDK</span><span class="topo-membrane">AKWVLIVSMLFGRLEIFTLL</span><span class="topo-inside">ILLTP</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-inside">TFWR</span><span class="topo-unknown">S</span></span>
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
      <td>6</td>
      <td>1</td>
      <td>6</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>27</td>
      <td>7</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>38</td>
      <td>28</td>
      <td>38</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>57</td>
      <td>39</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>58</td>
      <td>62</td>
      <td>58</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>65</td>
      <td>63</td>
      <td>65</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>66</td>
      <td>70</td>
      <td>66</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>87</td>
      <td>71</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>101</td>
      <td>88</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>114</td>
      <td>102</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>115</td>
      <td>129</td>
      <td>115</td>
      <td>129</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>148</td>
      <td>130</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>158</td>
      <td>149</td>
      <td>158</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>177</td>
      <td>159</td>
      <td>177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>178</td>
      <td>182</td>
      <td>178</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>203</td>
      <td>183</td>
      <td>203</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>204</td>
      <td>210</td>
      <td>204</td>
      <td>210</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>224</td>
      <td>211</td>
      <td>224</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>225</td>
      <td>237</td>
      <td>225</td>
      <td>237</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>238</td>
      <td>257</td>
      <td>238</td>
      <td>257</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>258</td>
      <td>274</td>
      <td>258</td>
      <td>274</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>293</td>
      <td>275</td>
      <td>293</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>294</td>
      <td>310</td>
      <td>294</td>
      <td>310</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>323</td>
      <td>311</td>
      <td>323</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>324</td>
      <td>334</td>
      <td>324</td>
      <td>334</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>335</td>
      <td>350</td>
      <td>335</td>
      <td>350</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>351</td>
      <td>399</td>
      <td>351</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>419</td>
      <td>400</td>
      <td>419</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>420</td>
      <td>427</td>
      <td>420</td>
      <td>427</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>428</td>
      <td>440</td>
      <td>428</td>
      <td>440</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>441</td>
      <td>455</td>
      <td>441</td>
      <td>455</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>456</td>
      <td>475</td>
      <td>456</td>
      <td>475</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>476</td>
      <td>484</td>
      <td>476</td>
      <td>484</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>485</td>
      <td>485</td>
      <td>485</td>
      <td>485</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4j9u">4J9U</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MKIIILGAGQVGGTLAENLVGENNDITIVDNNADRLRELQDKYDLRVVNGHASHPDVLHEAGAQDADMLVAVTNTDETNMAACQVAFTLFNTPNRVARIRSPEYLAEKEALFKSGAIPVD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">HLIAPEELVTSYIERLIQYPGALQVVSFAEQKVSLVAVKAY</span><span class="topo-unknown">YG</span><span class="topo-inside">GPLVGNALSALREH</span><span class="topo-unknown">MPHI</span><span class="topo-inside">DTRVAAIFRQGRPIRPQGTTIIEADDEVFFVAASNHIRSVMSELQRLEKPYRRIMIVGG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">GNIGASLAKRLEQTYSVKLIERDYQRAEKLSEQLENTIVFCGDAADQELLTEENIDQVDVFIALTNEDETNIMSAMLAKRMGAKKVMVLIQRGAYVDLVQGGVIDVAISPQQATISALLT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450        </span>
<span class="topo-line"><span class="topo-inside">HVRRADIVNVSSLRRGAAEAIEAVAHGDETTSKVVGRAIGDIKLPPGTTIGAVVRGEEVLIAHDRTVIEQDDHVVMFLVDKKYVPDVEALFQPSPFF</span><span class="topo-unknown">L</span></span>
<details class="topo-details"><summary>Topology coordinates (6 regions)</summary>
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
      <td>161</td>
      <td>1</td>
      <td>161</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>162</td>
      <td>163</td>
      <td>162</td>
      <td>163</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>164</td>
      <td>177</td>
      <td>164</td>
      <td>177</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>181</td>
      <td>178</td>
      <td>181</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>182</td>
      <td>457</td>
      <td>182</td>
      <td>457</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>458</td>
      <td>458</td>
      <td>458</td>
      <td>458</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4j9u">4J9U</a> — Chain F (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MKIIILGAGQVGGTLAENLVGENNDITIVDNNADRLRELQDKYDLRVVNGHASHPDVLHEAGAQDADMLVAVTNTDETNMAACQVAFTLFNTPNRVARIRSPEYLAEKEALFKSGAIPVD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">HLIAPEELVTSYIERLIQYPGALQVVSFAEQKVSLVAVKAYYGGPLVGNALSALREH</span><span class="topo-unknown">MPHI</span><span class="topo-inside">DTRVAAIFRQGRPIRPQGTTIIEADDEVFFVAASNHIRSVMSELQRLEKPYRRIMIVGG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">GNIGASLAKRLEQTYSVKLIERDYQRAEKLSEQLENTIVFCGDAADQELLTEENIDQVDVFIALTNEDETNIMSAMLAKRMGAKKVMVLIQRGAYVDLVQGGVIDVAISPQQATISALLT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450        </span>
<span class="topo-line"><span class="topo-inside">HVRRADIVNVSSLRRGAAEAIEAVA</span><span class="topo-unknown">HGD</span><span class="topo-inside">ETTSKVVGRAIGDIKLPPGTTIGAVVRGEEVLI</span><span class="topo-unknown">AH</span><span class="topo-inside">DRTVIEQDDHVVMFLVDKKYVPDVEALFQP</span><span class="topo-unknown">SPFFL</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>177</td>
      <td>1</td>
      <td>177</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>181</td>
      <td>178</td>
      <td>181</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>182</td>
      <td>385</td>
      <td>182</td>
      <td>385</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>386</td>
      <td>388</td>
      <td>386</td>
      <td>388</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>389</td>
      <td>421</td>
      <td>389</td>
      <td>421</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>422</td>
      <td>423</td>
      <td>422</td>
      <td>423</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>424</td>
      <td>453</td>
      <td>424</td>
      <td>453</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>454</td>
      <td>458</td>
      <td>454</td>
      <td>458</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4j9u">4J9U</a> — Chain G (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MKIIILGAGQVGGTLAENLVGENNDITIVDNNADRLRELQDKYDLRVVNGHASHPDVLHEAGAQDADMLVAVTNTDETNMAACQVAFTLFNTPNRVARIRSPEYLAEKEALFKSGAIPVD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">HLIAPEELVTSYIERLIQYPGALQVVSFAEQKVSLVAVKAY</span><span class="topo-unknown">YG</span><span class="topo-inside">GPLVGNALSALREH</span><span class="topo-unknown">MPH</span><span class="topo-inside">IDTRVAAIFRQGRPIRPQGTTIIEADDEVFFVAASNHIRSVMSELQRLEKPYRRIMIVGG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">GNIGASLAKRLEQTYSVKLIERDYQRAEKLSEQLENTIVFCGDAADQELLTEENIDQVDVFIALTNEDETNIMSAMLAKRMGAKKVMVLIQRGAYVDLVQGGVIDVAISPQQATISALLT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450        </span>
<span class="topo-line"><span class="topo-inside">HVRRADIVNVSSLRRGAAEAIEAVAHGDETTSKVVGRAIGDIKLPPGTTIGAVVRGEEVLIAHDRTVIEQDDHVVMFLVDKKYVPDVEALFQPSPFF</span><span class="topo-unknown">L</span></span>
<details class="topo-details"><summary>Topology coordinates (6 regions)</summary>
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
      <td>161</td>
      <td>1</td>
      <td>161</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>162</td>
      <td>163</td>
      <td>162</td>
      <td>163</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>164</td>
      <td>177</td>
      <td>164</td>
      <td>177</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>180</td>
      <td>178</td>
      <td>180</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>181</td>
      <td>457</td>
      <td>181</td>
      <td>457</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>458</td>
      <td>458</td>
      <td>458</td>
      <td>458</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4j9u">4J9U</a> — Chain H (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MKIIILGAGQVGGTLAENLVGENNDITIVDNNADRLRELQDKYDLRVVNGHASHPDVLHEAGAQDADMLVAVTNTDETNMAACQVAFTLFNTPNRVARIRSPEYLAEKEALFKSGAIPVD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">HLIAPEELVTSYIERLIQYPGALQVVSFAEQKVSLVAVKAYYGGPLVGNALSALREH</span><span class="topo-unknown">MPH</span><span class="topo-inside">IDTRVAAIFRQGRPIRPQGTTIIEADDEVFFVAASNHIRSVMSELQRLEKPYRRIMIVGG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">GNIGASLAKRLEQTYSVKLIERDYQRAEKLSEQLENTIVFCGDAADQELLTEENIDQVDVFIALTNEDETNIMSAMLAKRMGAKKVMVLIQRGAYVDLVQGGVIDVAISPQQATISALLT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450        </span>
<span class="topo-line"><span class="topo-inside">HVRRADIVNVSSLRRGAAEAIEAVAHGDETTSKVVGRAIGDIKLPPGTTIGAVVRGEEVLIAHDRTVIEQDDHVVMFLVDKKYVPDVEALFQP</span><span class="topo-unknown">SPFFL</span></span>
<details class="topo-details"><summary>Topology coordinates (4 regions)</summary>
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
      <td>177</td>
      <td>1</td>
      <td>177</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>180</td>
      <td>178</td>
      <td>180</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>181</td>
      <td>453</td>
      <td>181</td>
      <td>453</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>454</td>
      <td>458</td>
      <td>454</td>
      <td>458</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
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
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MQFRSI</span><span class="topo-membrane">IRIVGLLLALFSVTMLAPALVALLY</span><span class="topo-inside">RDGAG</span><span class="topo-membrane">VPFVTTFFVLLFCGAMCWFPNR</span><span class="topo-outside">RHKHELKSRDG</span><span class="topo-membrane">FLIVVLFWTVLGSAGSLPFLIA</span><span class="topo-inside">DNPNISV</span><span class="topo-unknown">TDAFFESFSALTTTGATV</span><span class="topo-inside">IVGL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">DELPK</span><span class="topo-membrane">AILFYRQFLQWFGGMGIIVLAVAI</span><span class="topo-outside">LPVLGIGG</span><span class="topo-unknown">MQLYRAEIPGPVKDTK</span><span class="topo-outside">MTPRIAETA</span><span class="topo-membrane">KALWYIYLSLTIACAVAFWLAGMT</span><span class="topo-inside">P</span><span class="topo-unknown">FDAISHSFSTIAIGGFST</span><span class="topo-inside">HDASMGYFDS</span><span class="topo-membrane">YAINL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">ITVVFLLISACNFTLHF</span><span class="topo-outside">AAFASGGVHPKYYWKDP</span><span class="topo-membrane">EFRAFIFIQVLLFLVCFLLLLK</span><span class="topo-inside">HHSYTSP</span><span class="topo-unknown">YDAFDQALFQTVSISTTAGFTTT</span><span class="topo-inside">GFADWP</span><span class="topo-membrane">LFLPVLLLFSSFIGGCAG</span><span class="topo-outside">STGGGMKVIR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">ILLLTLQGARELKRLVHPRAVYTIKVGGSALPQRVVDAV</span><span class="topo-membrane">WGFFSAYALVFVVCMLGLIATGMD</span><span class="topo-inside">E</span><span class="topo-unknown">LSAFSAVAATLNNLGPGLG</span><span class="topo-inside">EVALHFGDVND</span><span class="topo-membrane">KAKWVLIVSMLFGRLEIFTLL</span><span class="topo-outside">ILLTP</span></span>
<span class="topo-ruler">       490    </span>
<span class="topo-line"><span class="topo-outside">TFWR</span><span class="topo-unknown">SAAAENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (32 regions)</summary>
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
</details>
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
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MQFRSI</span><span class="topo-membrane">IRIVGLLLALFSVTMLAPALVALLY</span><span class="topo-inside">RDGAG</span><span class="topo-membrane">VPFVTTFFVLLFCGAMCWFPNR</span><span class="topo-outside">RHKHELKSRDG</span><span class="topo-membrane">FLIVVLFWTVLGSAGSLPFLIA</span><span class="topo-inside">DNPNISV</span><span class="topo-unknown">TDAFFESFSALTTTGATV</span><span class="topo-inside">IVGL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">DELPK</span><span class="topo-membrane">AILFYRQFLQWFGGMGIIVLAV</span><span class="topo-outside">AILPVLGIGG</span><span class="topo-unknown">MQLYRAEIPGPVKDTK</span><span class="topo-outside">MTPRIAETA</span><span class="topo-membrane">KALWYIYLSLTIACAVAFWLAGMT</span><span class="topo-inside">P</span><span class="topo-unknown">FDAISHSFSTIAIGGFST</span><span class="topo-inside">HDASMGYFDS</span><span class="topo-membrane">YAINL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">ITVVFLLISACNFTLHF</span><span class="topo-outside">AAFASGGVHPKYYWKDP</span><span class="topo-membrane">EFRAFIFIQVLLFLVCFLLLLK</span><span class="topo-inside">HHSYTSP</span><span class="topo-unknown">YDAFDQALFQTVSISTTAGFTTT</span><span class="topo-inside">GFADWP</span><span class="topo-membrane">LFLPVLLLFSSFIGGCAG</span><span class="topo-outside">STGGGMKVIR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">ILLLTLQGARELKRLVHPRAVYTIKVGGSALPQRVVDAV</span><span class="topo-membrane">WGFFSAYALVFVVCMLGLIATGMD</span><span class="topo-inside">E</span><span class="topo-unknown">LSAFSAVAATLNNLGPGLG</span><span class="topo-inside">EVALHFGDVND</span><span class="topo-membrane">KAKWVLIVSMLFGRLEIFTLL</span><span class="topo-outside">ILLTP</span></span>
<span class="topo-ruler">       490    </span>
<span class="topo-line"><span class="topo-outside">TFWR</span><span class="topo-unknown">SAAAENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (32 regions)</summary>
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
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### TrkH-TrkA complex architecture

The TrkH-[TRKA](/xray-mp-wiki/proteins/trka) complex crystallizes in P21 space group with four TrkH subunits and four [TRKA](/xray-mp-wiki/proteins/trka) subunits in the asymmetric unit, likely forming two biological units. Each TrkH subunit contributes a helix (D3M2b) to the TrkH-[TRKA](/xray-mp-wiki/proteins/trka) interface, and salt bridges form between TrkH and [TRKA](/xray-mp-wiki/proteins/trka) subunits. The dimer interface in TrkH is formed by two helices visible in electron density maps.

### Ion selectivity of TrkH-TrkA

Single-channel recordings show the TrkH-[TRKA](/xray-mp-wiki/proteins/trka) complex conducts K+, Na+, and Li+ under bi-ionic conditions. The channel was recorded at +50 mV in symmetrical 200 mM KCl, with current amplitudes of ~9.6 pA (Level 1) and ~18.8 pA (Level 2). Under bi-ionic conditions with 200 mM K+ in the pipette and 200 mM Na+ or Li+ in the bath, the reversal potential shifted by about 10 mV, indicating selectivity for these monovalent cations.

### Redox regulation via cysteine modification

The TrkH I220C mutant was used to study redox regulation. [MTSET](/xray-mp-wiki/reagents/additives/mtset) (1 mM) treatment reduced channel activity (Level 1 current from 9.7 to 5.6 pA for TrkH I220C alone, and from 9.7 to 4.6 pA for TrkH I220C-[TRKA](/xray-mp-wiki/proteins/trka) complex). Activity was reversible upon addition of 20 mM [DTT](/xray-mp-wiki/reagents/additives/dtt), indicating disulfide-linked modification.

### Comparison with isolated TrkH structure

The TrkH structure in the TrkH-[TRKA](/xray-mp-wiki/proteins/trka) complex was compared with isolated TrkH from PDB 3PJZ. Superposition of the TrkH dimers and of domains D1 and D3, including the intramembrane loop and D3M2b, reveals conformational differences between the isolated and complexed states.


## Cross-References

- <a href="/xray-mp-wiki/proteins/pumps-atpases/trka/">TrkA (ATP-binding Regulatory Subunit from Klebsiella pneumoniae)</a> — TrkA forms the cytoplasmic ATPase component that associates with TrkH to form the functional TrkH-TrkA potassium transporter complex
- <a href="/xray-mp-wiki/reagents/ligands/atp-gamma-s/">ATPγS (Adenosine 5'-O-(3-thiotriphosphate))</a> — ATPγS binds to TrkA in the isolated TrkA tetramer structure, providing structural basis for ATP recognition
- <a href="/xray-mp-wiki/reagents/cofactors/nadh/">NADH (Nicotinamide Adenine Dinucleotide, Reduced Form)</a> — NADH binds to the TrkH-TrkA complex and was used for anomalous phasing in the 3.8 A structure
- <a href="/xray-mp-wiki/reagents/additives/dtt/">Dithiothreitol (DTT)</a> — DTT (20 mM) reverses MTSET-induced modification of TrkH I220C, restoring channel activity
- <a href="/xray-mp-wiki/reagents/additives/mtset/">MTSET (2-trimethylammonium)ethyl methanethiosulfonate)</a> — MTSET (1 mM) covalently modifies TrkH I220C cysteine, reducing channel activity in a reversible manner
- <a href="/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/">Single-Wavelength Anomalous Diffraction</a> — Ta6Br12 clusters used for anomalous dispersion phasing of the TrkH-TrkA complex structure
- <a href="/xray-mp-wiki/reagents/ligands/adp">ADP</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/ligands/atp">ATP</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/dtt">DTT</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/cofactors/nadh">NADH</a> — Entity mentioned in text
