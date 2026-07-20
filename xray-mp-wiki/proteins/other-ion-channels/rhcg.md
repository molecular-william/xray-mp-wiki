---
title: "Human Rhesus C Glycoprotein (RhCG)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [channel, transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1003587107]
verified: agent
uniprot_id: Q9UBD6
---

# Human Rhesus C Glycoprotein (RhCG)

<div class="expr-badges"><span class="expr-badge expr-hek293">HEK293</span> <span class="expr-badge expr-mammalian">Mammalian</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q9UBD6">UniProt: Q9UBD6</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

RhCG (Rhesus C glycoprotein) is a human ammonia channel belonging to the Rh family of proteins. It forms a homotrimeric complex that plays an essential role in ammonia excretion and renal pH regulation. Each monomer contains 12 transmembrane helices, one more than bacterial homologs. The X-ray structure of human RhCG determined at 2.1 Å resolution reveals the mechanism of ammonia transport. RhCG conducts NH3 through a hydrophobic channel lumen featuring twin coplanar histidines (H185 and H344) that facilitate substrate passage. A unique feature not present in Amt proteins is a lateral "shunt" pocket extending from the cytosolic aperture to the membrane hydrocarbon region.


## Publications

### doi/10.1073##pnas.1003587107

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3hd6">3HD6</a></td>
      <td>2.1 A</td>
      <td>--</td>
      <td>Human RhCG expressed in HEK293S cells</td>
      <td>--</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293S (Mammalian)
- **Construct**: Full-length human RhCG with [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/)
- **Notes**: Expressed using tetracycline-inducible system (Reeves et al., 2002). Predicted mass 55.163 kDa, measured 55.1+/-0.1 kDa by MALDI mass spectroscopy, confirming singly glycosylated species.

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
      <td>FLAG affinity purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> affinity resin</td>
      <td>-- + --</td>
      <td>RhCG purified using <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> affinity tag</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td>--</td>
      <td>-- + --</td>
      <td>Purified by <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a> after <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> affinity</td>
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
      <td>Purified RhCG</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Cryoprotected crystals</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown by vapor diffusion. Data collected at beamline 8.3.1 of the Advanced Light Source (Lawrence Berkeley National Laboratories).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3hd6">3HD6</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GPSSP</span><span class="topo-inside">SAWNTNLRWRL</span><span class="topo-membrane">PLTCLLLQVIMVILFGV</span><span class="topo-outside">FVRYDF</span><span class="topo-unknown">EADAHWWSERTHKNLSDM</span><span class="topo-outside">ENEFYYRY</span><span class="topo-membrane">PSFQDVHVMVFVGFGFLM</span><span class="topo-inside">TFLQRYGFSA</span><span class="topo-membrane">VGFNFLLAAFGIQWALLMQGW</span><span class="topo-outside">FHFLQD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">RYIVVGVEN</span><span class="topo-membrane">LINADFCVASVCVAFGAV</span><span class="topo-inside">LGKVSP</span><span class="topo-membrane">IQLLIMTFFQVTLFAVNEFIL</span><span class="topo-outside">LNLLKVKD</span><span class="topo-membrane">AGGSMTIHTFGAYFGLTVT</span><span class="topo-inside">RILYRRNLEQSKERQNSVYQSDLF</span><span class="topo-membrane">AMIGTLFLWMYWPSF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">NSA</span><span class="topo-outside">ISYHGDSQHRA</span><span class="topo-membrane">AINTYCSLAACVLTSVAI</span><span class="topo-inside">SSALHKKGKLDMVH</span><span class="topo-membrane">IQNATLAGGVAVGTAA</span><span class="topo-outside">EMMLMP</span><span class="topo-membrane">YGALIIGFVCGIISTLGF</span><span class="topo-unknown">VYLTPFLESRL</span><span class="topo-inside">HIQDTC</span><span class="topo-membrane">GINNLHGIPGIIGGIVG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">AVT</span><span class="topo-outside">AAS</span><span class="topo-unknown">ASLEVYGKEGLVHSFDFQGFNG</span><span class="topo-outside">DWTARTQGKFQ</span><span class="topo-membrane">IYGLLVTLAMALMGGIIVGLIL</span><span class="topo-inside">RLPFWGQPSDENCFEDAVYWEMPEGNS</span><span class="topo-unknown">TVYIPEDPTFKPSGPSVPSVPMVSPLPMASSV</span></span>
<span class="topo-ruler">       490</span>
<span class="topo-line"><span class="topo-unknown">PLVPGGLVPR</span></span>
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
      <td>5</td>
      <td>-4</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>16</td>
      <td>1</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>33</td>
      <td>12</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>39</td>
      <td>29</td>
      <td>34</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>57</td>
      <td>35</td>
      <td>52</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>65</td>
      <td>53</td>
      <td>60</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>83</td>
      <td>61</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>93</td>
      <td>79</td>
      <td>88</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>114</td>
      <td>89</td>
      <td>109</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>129</td>
      <td>110</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>147</td>
      <td>125</td>
      <td>142</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>153</td>
      <td>143</td>
      <td>148</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>174</td>
      <td>149</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>182</td>
      <td>170</td>
      <td>177</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>201</td>
      <td>178</td>
      <td>196</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>202</td>
      <td>225</td>
      <td>197</td>
      <td>220</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>243</td>
      <td>221</td>
      <td>238</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>254</td>
      <td>239</td>
      <td>249</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>272</td>
      <td>250</td>
      <td>267</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>286</td>
      <td>268</td>
      <td>281</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>302</td>
      <td>282</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>303</td>
      <td>308</td>
      <td>298</td>
      <td>303</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>309</td>
      <td>326</td>
      <td>304</td>
      <td>321</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>327</td>
      <td>337</td>
      <td>322</td>
      <td>332</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>338</td>
      <td>343</td>
      <td>333</td>
      <td>338</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>363</td>
      <td>339</td>
      <td>358</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>366</td>
      <td>359</td>
      <td>361</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>388</td>
      <td>362</td>
      <td>383</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>389</td>
      <td>399</td>
      <td>384</td>
      <td>394</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>421</td>
      <td>395</td>
      <td>416</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>422</td>
      <td>448</td>
      <td>417</td>
      <td>443</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>490</td>
      <td>444</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3hd6">3HD6</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GPSSP</span><span class="topo-inside">SAWNTNLRWRL</span><span class="topo-membrane">PLTCLLLQVIMVILFGV</span><span class="topo-outside">FVRYDF</span><span class="topo-unknown">EADAHWWSERTHKNLSDM</span><span class="topo-outside">ENEFYYRY</span><span class="topo-membrane">PSFQDVHVMVFVGFGFLM</span><span class="topo-inside">TFLQRYGFSA</span><span class="topo-membrane">VGFNFLLAAFGIQWALLMQGW</span><span class="topo-outside">FHFLQD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">RYIVVGVEN</span><span class="topo-membrane">LINADFCVASVCVAFGAV</span><span class="topo-inside">LGKVSP</span><span class="topo-membrane">IQLLIMTFFQVTLFAVNEFIL</span><span class="topo-outside">LNLLKVKD</span><span class="topo-membrane">AGGSMTIHTFGAYFGLTVT</span><span class="topo-inside">RILYRRNLEQSKERQNSVYQSDLF</span><span class="topo-membrane">AMIGTLFLWMYWPSF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">NSA</span><span class="topo-outside">ISYHGDSQHRA</span><span class="topo-membrane">AINTYCSLAACVLTSVAI</span><span class="topo-inside">SSALHKKGKLDMVH</span><span class="topo-membrane">IQNATLAGGVAVGTAA</span><span class="topo-outside">EMMLMP</span><span class="topo-membrane">YGALIIGFVCGIISTLGF</span><span class="topo-unknown">VYLTPFLESRL</span><span class="topo-inside">HIQDTC</span><span class="topo-membrane">GINNLHGIPGIIGGIVG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">AVT</span><span class="topo-outside">AAS</span><span class="topo-unknown">ASLEVYGKEGLVHSFDFQGFNG</span><span class="topo-outside">DWTARTQGKFQ</span><span class="topo-membrane">IYGLLVTLAMALMGGIIVGLIL</span><span class="topo-inside">RLPFWGQPSDENCFEDAVYWEMPEGNS</span><span class="topo-unknown">TVYIPEDPTFKPSGPSVPSVPMVSPLPMASSV</span></span>
<span class="topo-ruler">       490</span>
<span class="topo-line"><span class="topo-unknown">PLVPGGLVPR</span></span>
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
      <td>5</td>
      <td>-4</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>16</td>
      <td>1</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>33</td>
      <td>12</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>39</td>
      <td>29</td>
      <td>34</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>57</td>
      <td>35</td>
      <td>52</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>65</td>
      <td>53</td>
      <td>60</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>83</td>
      <td>61</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>93</td>
      <td>79</td>
      <td>88</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>114</td>
      <td>89</td>
      <td>109</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>129</td>
      <td>110</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>147</td>
      <td>125</td>
      <td>142</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>153</td>
      <td>143</td>
      <td>148</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>174</td>
      <td>149</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>182</td>
      <td>170</td>
      <td>177</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>201</td>
      <td>178</td>
      <td>196</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>202</td>
      <td>225</td>
      <td>197</td>
      <td>220</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>243</td>
      <td>221</td>
      <td>238</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>254</td>
      <td>239</td>
      <td>249</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>272</td>
      <td>250</td>
      <td>267</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>286</td>
      <td>268</td>
      <td>281</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>302</td>
      <td>282</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>303</td>
      <td>308</td>
      <td>298</td>
      <td>303</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>309</td>
      <td>326</td>
      <td>304</td>
      <td>321</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>327</td>
      <td>337</td>
      <td>322</td>
      <td>332</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>338</td>
      <td>343</td>
      <td>333</td>
      <td>338</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>363</td>
      <td>339</td>
      <td>358</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>366</td>
      <td>359</td>
      <td>361</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>388</td>
      <td>362</td>
      <td>383</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>389</td>
      <td>399</td>
      <td>384</td>
      <td>394</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>421</td>
      <td>395</td>
      <td>416</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>422</td>
      <td>448</td>
      <td>417</td>
      <td>443</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>490</td>
      <td>444</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3hd6">3HD6</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GPSSP</span><span class="topo-inside">SAWNTNLRWRL</span><span class="topo-membrane">PLTCLLLQVIMVILFGV</span><span class="topo-outside">FVRYDF</span><span class="topo-unknown">EADAHWWSERTHKNLSDM</span><span class="topo-outside">ENEFYYRY</span><span class="topo-membrane">PSFQDVHVMVFVGFGFLM</span><span class="topo-inside">TFLQRYGFSA</span><span class="topo-membrane">VGFNFLLAAFGIQWALLMQGW</span><span class="topo-outside">FHFLQD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">RYIVVGVEN</span><span class="topo-membrane">LINADFCVASVCVAFGAV</span><span class="topo-inside">LGKVSP</span><span class="topo-membrane">IQLLIMTFFQVTLFAVNEFIL</span><span class="topo-outside">LNLLKVKD</span><span class="topo-membrane">AGGSMTIHTFGAYFGLTVT</span><span class="topo-inside">RILYRRNLEQSKERQNSVYQSDLF</span><span class="topo-membrane">AMIGTLFLWMYWPSF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">NSA</span><span class="topo-outside">ISYHGDSQHRA</span><span class="topo-membrane">AINTYCSLAACVLTSVAI</span><span class="topo-inside">SSALHKKGKLDMVH</span><span class="topo-membrane">IQNATLAGGVAVGTAA</span><span class="topo-outside">EMMLMP</span><span class="topo-membrane">YGALIIGFVCGIISTLGF</span><span class="topo-unknown">VYLTPFLESRL</span><span class="topo-inside">HIQDTC</span><span class="topo-membrane">GINNLHGIPGIIGGIVG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">AVT</span><span class="topo-outside">AAS</span><span class="topo-unknown">ASLEVYGKEGLVHSFDFQGFNG</span><span class="topo-outside">DWTARTQGKFQ</span><span class="topo-membrane">IYGLLVTLAMALMGGIIVGLIL</span><span class="topo-inside">RLPFWGQPSDENCFEDAVYWEMPEGNS</span><span class="topo-unknown">TVYIPEDPTFKPSGPSVPSVPMVSPLPMASSV</span></span>
<span class="topo-ruler">       490</span>
<span class="topo-line"><span class="topo-unknown">PLVPGGLVPR</span></span>
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
      <td>5</td>
      <td>-4</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>16</td>
      <td>1</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>33</td>
      <td>12</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>39</td>
      <td>29</td>
      <td>34</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>57</td>
      <td>35</td>
      <td>52</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>65</td>
      <td>53</td>
      <td>60</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>83</td>
      <td>61</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>93</td>
      <td>79</td>
      <td>88</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>114</td>
      <td>89</td>
      <td>109</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>129</td>
      <td>110</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>147</td>
      <td>125</td>
      <td>142</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>153</td>
      <td>143</td>
      <td>148</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>174</td>
      <td>149</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>182</td>
      <td>170</td>
      <td>177</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>201</td>
      <td>178</td>
      <td>196</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>202</td>
      <td>225</td>
      <td>197</td>
      <td>220</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>243</td>
      <td>221</td>
      <td>238</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>254</td>
      <td>239</td>
      <td>249</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>272</td>
      <td>250</td>
      <td>267</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>286</td>
      <td>268</td>
      <td>281</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>302</td>
      <td>282</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>303</td>
      <td>308</td>
      <td>298</td>
      <td>303</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>309</td>
      <td>326</td>
      <td>304</td>
      <td>321</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>327</td>
      <td>337</td>
      <td>322</td>
      <td>332</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>338</td>
      <td>343</td>
      <td>333</td>
      <td>338</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>363</td>
      <td>339</td>
      <td>358</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>366</td>
      <td>359</td>
      <td>361</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>388</td>
      <td>362</td>
      <td>383</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>389</td>
      <td>399</td>
      <td>384</td>
      <td>394</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>421</td>
      <td>395</td>
      <td>416</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>422</td>
      <td>448</td>
      <td>417</td>
      <td>443</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>490</td>
      <td>444</td>
      <td>485</td>
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

### NH3 transport mechanism

RhCG conducts NH3 through a hydrophobic channel lumen. Conserved features include acidic residues lining the channel apertures (E166, D218, D278, E329) that attract NH4+, a largely hydrophobic lumen that excludes NH4+ and facilitates passage of neutral NH3, and twin coplanar histidines (H185 and H344) in the center of the channel that are essential for optimal NH3 permeation. The absence of ordered water molecules in the hydrophobic lumen further supports exclusion of charged NH4+.

### Phe gate and extracellular aperture

The extracellular pore is gated by phenylalanines F130 and F235. Unlike Amt proteins where F130 obstructs the pore, in RhCG, F130 is locked in an open conformation by interactions with D129, which is hydrogen-bonded to Y254 of an adjacent monomer and H67. This restricts F130 mobility, keeping the gate constitutively open. F235 retains freedom of motion, and mutation to valine reduces NH3 transport.

### The RhCG shunt

A unique feature of RhCG not present in Amt proteins is a lateral pocket termed the "shunt" extending from the cytosolic aperture to the membrane hydrocarbon region. This shunt is lined by residues conserved among human Rh glycoproteins and is also present in NeRh, suggesting it is common to the Rh subfamily. The cytosolic aperture features an acidic residue E329 that may recruit charged NH4+.

### Renal pH regulation model

In kidney epithelial cells, RhCG is expressed on both apical and basal surfaces of acid-secreting intercalated cells. NH3 transport through RhCG is driven by the progressively lowered pH from interstitium to epithelial cell cytosol to urinary space. Urinary acidification by V-type H+-ATPase and H+/K+-ATPase shifts the NH4+/NH3 equilibrium, trapping NH4+ in urine (up to 200 mM) while maintaining low intracellular NH4+ (~8 mM), enabling net NH4+ excretion essential for acid-base homeostasis.


## Cross-References

- <a href="/xray-mp-wiki/proteins/other-ion-channels/amt-b/">Ammonium Transporter AmtB (E. coli)</a> — RhCG is structurally and functionally related to AmtB; both are trimeric ammonia channels with conserved twin-His motifs
- <a href="/xray-mp-wiki/concepts/protein-families/rh-amt-mep-protein-family/">Rh/Amt/MEP Protein Family</a> — RhCG is a member of the Rh family within the broader Rh/Amt/MEP superfamily
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a> — Fusion tag for crystallization or purification
