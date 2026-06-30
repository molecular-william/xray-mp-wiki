---
title: "A. thaliana STP10"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1038##s41477-021-00992-0, doi/10.1038##s41467-018-08176-9]
verified: false
---

# A. thaliana STP10

## Overview

A. thaliana STP10 is a high-affinity [Glucose](/xray-mp-wiki/reagents/additives/glucose/)/H+ symporter from the Sugar Transport Protein (STP) family in Arabidopsis thaliana. It belongs to the major facilitator superfamily ([MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/)) and is responsible for proton-coupled uptake of monosaccharides from the apoplast into plant cells. STP10 is expressed in pollen tubes and plays crucial roles in plant organ development, stress responses, and defense against fungal pathogens. Two X-ray crystal structures were determined: an outward-occluded conformation at 1.8 A resolution (PDB: 7AAQ) and an inward-open conformation at 2.6 A resolution (PDB: 7AAR), both with [Glucose](/xray-mp-wiki/reagents/additives/glucose/) and protons bound.


## Publications

### doi/10.1038##s41477-021-00992-0

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7aaq">7AAQ</a></td>
      <td>1.8</td>
      <td>C2</td>
      <td>Full-length STP10 (wild type)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7aar">7AAR</a></td>
      <td>2.6</td>
      <td>—</td>
      <td>STP10 E162Q D344N double mutant (inward-open conformation)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Saccharomyces cerevisiae EBY.VW4000
- **Construct**: Full-length STP10 with C-terminal His6 tag in pDR196 vector
- **Notes**: Expressed in hexose-transport-defective yeast strain EBY.VW4000

**Purification:**

- **Expression system**: Saccharomyces cerevisiae EBY.VW4000

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
      <td>Differential centrifugation</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.4, 300 mM NaCl</td>
      <td>Cells harvested and lysed; membranes collected by ultracentrifugation</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.4, 300 mM NaCl + 1% n-decyl-β-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/dm">DM</a>)</td>
      <td>Membranes solubilized for 1 h at 4°C</td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> agarose</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.4, 300 mM NaCl + 0.05% <a href="/xray-mp-wiki/reagents/detergents/dm">DM</a></td>
      <td>Wash with 30 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, elute with 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.4, 300 mM NaCl + 0.05% <a href="/xray-mp-wiki/reagents/detergents/dm">DM</a></td>
      <td>Detergent exchanged to NG/<a href="/xray-mp-wiki/reagents/detergents/og">OG</a> for crystallization</td>
    </tr>
  </tbody>
</table>
**Final sample**: STP10 in 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4, 300 mM NaCl, NG/OG

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>LCP</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified STP10 in NG/OG</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> (9.9 <a href="/xray-mp-wiki/reagents/lipids/mag/">MAG</a>)</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>2:3</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>293</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2-4 weeks</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals appeared using the sitting-drop LCP method</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7aaq">7AAQ</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAGGAFVSEGGGGGRSYEGG</span><span class="topo-inside">VTAFVIMTC</span><span class="topo-membrane">IVAAMGGLLFGYDLGISG</span><span class="topo-outside">GVTSM</span><span class="topo-unknown">EEFLTKF</span><span class="topo-outside">FPQVESQMKKAKHDTAYCKFDNQMLQ</span><span class="topo-membrane">LFTSSLYLAALVASFMASVI</span><span class="topo-inside">TRKHGRK</span><span class="topo-membrane">VSMFIGGL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">AFLIGALFNAFA</span><span class="topo-outside">VNVS</span><span class="topo-membrane">MLIIGRLLLGVGVGFANQSTPV</span><span class="topo-inside">YLSEMAPAKIRG</span><span class="topo-membrane">ALNIGFQMAITIGILVANLIN</span><span class="topo-outside">YGTSKMAQHGWR</span><span class="topo-membrane">VSLGLAAVPAVVMVIGSF</span><span class="topo-inside">ILPDTPNSMLERGKNEEAK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">QMLKKIRGADNVDHEFQDLIDAVEAAKKVENPWKNIMESKYRPAL</span><span class="topo-membrane">IFCSAIPFFQQITGINVIMF</span><span class="topo-outside">YAPVLFKTLGFGDDAALMSA</span><span class="topo-membrane">VITGVVNMLSTFVSIYAV</span><span class="topo-inside">DRYG</span><span class="topo-membrane">RRLLFLEGGIQMF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">ICQLLV</span><span class="topo-outside">GSFIGARFGTSGTGTLTPATADWIL</span><span class="topo-membrane">AFICVYVAGFAWSWGPLGWLVPS</span><span class="topo-inside">EICPLEIRPA</span><span class="topo-membrane">GQAINVSVNMFFTFLIGQFF</span><span class="topo-outside">LTMLCHMKFGL</span><span class="topo-membrane">FYFFASMVAIMTVFIYFLL</span><span class="topo-inside">PETKGV</span></span>
<span class="topo-ruler">       490       500       510    </span>
<span class="topo-line"><span class="topo-inside">PIEEMGRVWKQHWFWKKYIPEDAIIGG</span><span class="topo-unknown">HDDNNTN</span></span>
<details class="topo-details"><summary>Topology coordinates (27 regions)</summary>
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
      <td>21</td>
      <td>29</td>
      <td>21</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>47</td>
      <td>30</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>52</td>
      <td>48</td>
      <td>52</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>53</td>
      <td>59</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>60</td>
      <td>85</td>
      <td>60</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>105</td>
      <td>86</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>112</td>
      <td>106</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>132</td>
      <td>113</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>133</td>
      <td>136</td>
      <td>133</td>
      <td>136</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>158</td>
      <td>137</td>
      <td>158</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>159</td>
      <td>170</td>
      <td>159</td>
      <td>170</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>171</td>
      <td>191</td>
      <td>171</td>
      <td>191</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>192</td>
      <td>203</td>
      <td>192</td>
      <td>203</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>221</td>
      <td>204</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>285</td>
      <td>222</td>
      <td>285</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>305</td>
      <td>286</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>325</td>
      <td>306</td>
      <td>325</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>343</td>
      <td>326</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>344</td>
      <td>347</td>
      <td>344</td>
      <td>347</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>348</td>
      <td>366</td>
      <td>348</td>
      <td>366</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>367</td>
      <td>391</td>
      <td>367</td>
      <td>391</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>392</td>
      <td>414</td>
      <td>392</td>
      <td>414</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>415</td>
      <td>424</td>
      <td>415</td>
      <td>424</td>
      <td>Inside</td>
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
      <td>455</td>
      <td>445</td>
      <td>455</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>456</td>
      <td>474</td>
      <td>456</td>
      <td>474</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>507</td>
      <td>475</td>
      <td>507</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7aar">7AAR</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAGGAFVSEGGGGGR</span><span class="topo-inside">SYEGGVTAFVIM</span><span class="topo-membrane">TCIVAAMGGLLFGYDLGISGGV</span><span class="topo-outside">TSM</span><span class="topo-unknown">EEFLTKF</span><span class="topo-outside">FPQVESQMKKAKHDTAYCKFDNQMLQ</span><span class="topo-membrane">LFTSSLYLAALVASFMASVI</span><span class="topo-inside">TRKHGRK</span><span class="topo-membrane">VSMFIGGL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">AFLIGALFNAFA</span><span class="topo-outside">VNVS</span><span class="topo-membrane">MLIIGRLLLGVGVGFANQSTP</span><span class="topo-inside">VYLSQMAPAKIRGALNI</span><span class="topo-membrane">GFQMAITIGILVANLINYGT</span><span class="topo-outside">SKMAQHGW</span><span class="topo-membrane">RVSLGLAAVPAVVMVIGSFI</span><span class="topo-inside">LPDTPNSMLERGKNEEAK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">QMLKKIRGADNVDHEFQDLIDAVEAAKKVENPWKNIMESKYRPALI</span><span class="topo-membrane">FCSAIPFFQQITGINVIMFYAP</span><span class="topo-outside">VLFKTLGFGDDAAL</span><span class="topo-membrane">MSAVITGVVNMLSTFVSIYAV</span><span class="topo-inside">NRYGR</span><span class="topo-membrane">RLLFLEGGIQMF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">ICQLLVGS</span><span class="topo-outside">FIGARFGTSGTGTLTPATAD</span><span class="topo-membrane">WILAFICVYVAGFAWSWGPLGWL</span><span class="topo-inside">VPSEICPLEIRPAGQ</span><span class="topo-membrane">AINVSVNMFFTFLIGQFFL</span><span class="topo-outside">TMLCHMKFG</span><span class="topo-membrane">LFYFFASMVAIMTVFIYFLL</span><span class="topo-inside">PETKGV</span></span>
<span class="topo-ruler">       490       500       510    </span>
<span class="topo-line"><span class="topo-inside">PIEEMGRVWKQHWFWKKYIP</span><span class="topo-unknown">EDAIIGGHDDNNTN</span></span>
<details class="topo-details"><summary>Topology coordinates (27 regions)</summary>
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
      <td>27</td>
      <td>16</td>
      <td>27</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>28</td>
      <td>49</td>
      <td>28</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>52</td>
      <td>50</td>
      <td>52</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>53</td>
      <td>59</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>60</td>
      <td>85</td>
      <td>60</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>105</td>
      <td>86</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>112</td>
      <td>106</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>132</td>
      <td>113</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>133</td>
      <td>136</td>
      <td>133</td>
      <td>136</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>157</td>
      <td>137</td>
      <td>157</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>158</td>
      <td>174</td>
      <td>158</td>
      <td>174</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>175</td>
      <td>194</td>
      <td>175</td>
      <td>194</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>195</td>
      <td>202</td>
      <td>195</td>
      <td>202</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>222</td>
      <td>203</td>
      <td>222</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>223</td>
      <td>286</td>
      <td>223</td>
      <td>286</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>308</td>
      <td>287</td>
      <td>308</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>309</td>
      <td>322</td>
      <td>309</td>
      <td>322</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>343</td>
      <td>323</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>344</td>
      <td>348</td>
      <td>344</td>
      <td>348</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>349</td>
      <td>368</td>
      <td>349</td>
      <td>368</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>369</td>
      <td>388</td>
      <td>369</td>
      <td>388</td>
      <td>Outside</td>
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
      <td>426</td>
      <td>412</td>
      <td>426</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>427</td>
      <td>445</td>
      <td>427</td>
      <td>445</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>446</td>
      <td>454</td>
      <td>446</td>
      <td>454</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>455</td>
      <td>474</td>
      <td>455</td>
      <td>474</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>500</td>
      <td>475</td>
      <td>500</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##s41467-018-08176-9

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6h7d">6H7D</a></td>
      <td>2.4</td>
      <td>C2</td>
      <td>Full-length STP10 (residues 21-507 of 514) with C-terminal deca-His tag</td>
      <td><a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a></td>
    </tr>
  </tbody>
</table>
 - R-work 24.3%, R-free 26.8%

**Expression:**

- **Expression system**: Saccharomyces cerevisiae EBY.VW4000
- **Construct**: Full-length STP10 with C-terminal His6 tag in pDR196 vector
- **Notes**: Expressed in hexose-transport-defective yeast strain EBY.VW4000

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6h7d">6H7D</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAAGGAFVSEGGGGGRSYEGG</span><span class="topo-inside">VTAFVIMTC</span><span class="topo-membrane">IVAAMGGLLFGYDLGISG</span><span class="topo-outside">GVTSM</span><span class="topo-unknown">EEFLTKF</span><span class="topo-outside">FPQVESQMKKAKHDTAYCKFDNQMLQL</span><span class="topo-membrane">FTSSLYLAALVASFMASVIT</span><span class="topo-inside">RKHGR</span><span class="topo-membrane">KVSMFIGG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LAFLIGALFNAFA</span><span class="topo-outside">VNVS</span><span class="topo-membrane">MLIIGRLLLGVGVGFANQSTPV</span><span class="topo-inside">YLSEMAPAKIRG</span><span class="topo-membrane">ALNIGFQMAITIGILVANLIN</span><span class="topo-outside">YGTSKMAQHGWR</span><span class="topo-membrane">VSLGLAAVPAVVMVIGSF</span><span class="topo-inside">ILPDTPNSMLERGKNEEA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">KQMLKKIRGADNVDHEFQDLIDAVEAAKKVENPWKNIMESKYR</span><span class="topo-membrane">PALIFCSAIPFFQQITGINVIMF</span><span class="topo-outside">YAPVLFKTLGFGDDAALMS</span><span class="topo-membrane">AVITGVVNMLSTFVSIYAV</span><span class="topo-inside">DRY</span><span class="topo-membrane">GRRLLFLEGGIQM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">FICQLLV</span><span class="topo-outside">GSFIGARFGTSGTGTLTPATADWIL</span><span class="topo-membrane">AFICVYVAGFAWSWGPLGWLVPS</span><span class="topo-inside">EICPLEIRP</span><span class="topo-membrane">AGQAINVSVNMFFTFLIGQFF</span><span class="topo-outside">LTMLCHMKFGL</span><span class="topo-membrane">FYFFASMVAIMTVFIYFLL</span><span class="topo-inside">PETKG</span></span>
<span class="topo-ruler">       490       500       510       520 </span>
<span class="topo-line"><span class="topo-inside">VPIEEMGRVWKQHWFWKKYIPEDAIIGG</span><span class="topo-unknown">HDDNNTNPGLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (27 regions)</summary>
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
      <td>22</td>
      <td>30</td>
      <td>21</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>48</td>
      <td>30</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>53</td>
      <td>48</td>
      <td>52</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>60</td>
      <td>53</td>
      <td>59</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>61</td>
      <td>87</td>
      <td>60</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>107</td>
      <td>87</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>112</td>
      <td>107</td>
      <td>111</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>133</td>
      <td>112</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>137</td>
      <td>133</td>
      <td>136</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>138</td>
      <td>159</td>
      <td>137</td>
      <td>158</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>171</td>
      <td>159</td>
      <td>170</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>172</td>
      <td>192</td>
      <td>171</td>
      <td>191</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>193</td>
      <td>204</td>
      <td>192</td>
      <td>203</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>205</td>
      <td>222</td>
      <td>204</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>223</td>
      <td>283</td>
      <td>222</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>306</td>
      <td>283</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>325</td>
      <td>306</td>
      <td>324</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>344</td>
      <td>325</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>345</td>
      <td>347</td>
      <td>344</td>
      <td>346</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>348</td>
      <td>367</td>
      <td>347</td>
      <td>366</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>392</td>
      <td>367</td>
      <td>391</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>393</td>
      <td>415</td>
      <td>392</td>
      <td>414</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>416</td>
      <td>424</td>
      <td>415</td>
      <td>423</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>425</td>
      <td>445</td>
      <td>424</td>
      <td>444</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>446</td>
      <td>456</td>
      <td>445</td>
      <td>455</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>457</td>
      <td>475</td>
      <td>456</td>
      <td>474</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>476</td>
      <td>508</td>
      <td>475</td>
      <td>507</td>
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

### Proton-coupled transport mechanism

Glu162 was identified as the proton donor/acceptor residue essential for proton-coupled [Glucose](/xray-mp-wiki/reagents/additives/glucose/) transport in STP10. In the outward-occluded state, Glu162 is protonated, while in the inward-open state it is deprotonated. This protonation switch is coupled to conformational changes in the transport cycle, providing a detailed molecular basis for proton-to-[Glucose](/xray-mp-wiki/reagents/additives/glucose/) coupling in the STP family.

### Sugar binding site

[Glucose](/xray-mp-wiki/reagents/additives/glucose/) is bound in a central cavity between the N- and C-domains of STP10. Key residues involved in [Glucose](/xray-mp-wiki/reagents/additives/glucose/) coordination include Asp42, Asn46, Glu170, Arg264, Trp388, Asn392 and Trp488. The 1.8 A outward-occluded structure reveals detailed hydrogen bonding networks between [Glucose](/xray-mp-wiki/reagents/additives/glucose/) and these conserved residues.

### Intracellular gate regulation

The intracellular gate is formed by a network of salt bridges involving Glu162, Arg169, Asp344, Arg422 and Glu415. These interactions maintain the structural integrity of the ICH domain and regulate the opening and closing of the intracellular gate during the transport cycle. The double mutant E162Q/D344N was used to capture the inward-open state.

### Conserved structural elements

STP10 has 12 transmembrane helices organized into N-domain (TM1-TM6) and C-domain (TM7-TM12), with a Lid domain and intracellular helical (ICH) domain characteristic of the STP subfamily. A conserved disulfide bridge between the Lid domain and C-domain is present in all STPs. Structural elements and key residues are perfectly conserved across plant STPs.

### Lid domain and disulfide bridge regulation

The Lid domain is a unique extracellular domain in STPs that locks the mobile transmembrane domains through a conserved disulfide bridge (Cys77-Cys449). A cluster of aromatic residues (Phe55, Phe59, Phe60, Phe79, Phe87, Trp202) isolates the proton donor/acceptor pair from the extracellular space, maintaining Asp42 protonation during transport. Breaking the disulfide bridge (C77A, C449A mutants) makes the protein sensitive to alkaline pH, functioning only at pH < 5. The equivalent mutation in wheat Lr67 reintroduces pathogen susceptibility, highlighting the physiological importance of the Lid domain in plant defense.

### Proton donor/acceptor pair and high affinity glucose binding

Asp42 and Arg142 form the proton donor/acceptor pair essential for proton-coupled glucose transport. Asp42 is located on the flexible M1b helix flanked by 6 glycine residues, giving it high flexibility. At low pH (crystallization at pH 4.5), Asp42 is protonated. The μM affinity of STP10 for glucose is achieved through tight hydrophobic interactions with Phe39 and Leu43 in the N-domain, a feature not found in bacterial or human sugar transporters. The L43A mutation reduces affinity from μM to mM range (Km 391 μM), demonstrating that hydrophobic interaction is a key contributor to high affinity.

### Substrate specificity

STP10 transports D-glucose with high affinity and can also transport the non-metabolized glucose analog 2-deoxyglucose. It shows sensitivity to only some inhibitors known from bacterial and human sugar transport. The C-domain polar interactions (Q295, N301, N332) recognize specific hydroxyl groups of glucose, mediating substrate specificity.


## Cross-References

- <a href="/xray-mp-wiki/proteins/miscellaneous/a-thaliana-sweet1/">A. thaliana SWEET1</a> — Both are plant sugar transporters from Arabidopsis thaliana, solved by X-ray crystallography
- <a href="/xray-mp-wiki/concepts/protein-families/mfs-transporter/">Major Facilitator Superfamily (MFS)</a> — STP10 belongs to the MFS family of secondary active transporters
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/lid-domain/">Lid Domain in Sugar Transport Proteins (STPs)</a> — STP10 structure revealed the Lid domain, a conserved feature of all STPs
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> — Buffer component in purification or crystallization
- <a href="/xray-mp-wiki/reagents/buffers/sodium-acetate/">Sodium Acetate</a> — Buffer component in purification or crystallization
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> — Buffer component in purification or crystallization
- <a href="/xray-mp-wiki/reagents/lipids/mag/">MAG</a> — Additive used in purification or crystallization buffers
