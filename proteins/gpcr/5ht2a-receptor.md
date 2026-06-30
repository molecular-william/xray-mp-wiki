---
title: "Human 5-HT2A Receptor"
created: 2026-05-27
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41594-018-0180-z, doi/10.1038##s41594-022-00796-6, doi/10.1126##science.abl8615]
verified: false
---

# Human 5-HT2A Receptor

## Overview

The human [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki/reagents/ligands/serotonin) 2A (5-HT2A) receptor is a class A [GPCR](/xray-mp-wiki/concepts/gpcr/) and a major drug target for antipsychotics and hallucinogens. Crystal structures have been determined in complex with the second-generation antipsychotics [risperidone](/xray-mp-wiki/reagents/ligands/risperidone) (PDB 6A93, 3.0 A) and [zotepine](/xray-mp-wiki/reagents/zotepine/) (PDB 6A94, 2.9 A), revealing the inactive state conformation and a unique side-extended cavity near the orthosteric binding site. [Cryo-EM](/xray-mp-wiki/methods/cryo-em/) structures of the 5-HT2A receptor in complex with miniGo and the psychedelic agonists [lisuride](/xray-mp-wiki/reagents/lisuride/) and [methylgeromertrine](/xray-mp-wiki/reagents/methylgeromertrine/) have been determined, revealing the active-state conformation and G protein coupling interface. High-resolution X-ray structures of 5-HT2AR complexed with [serotonin](/xray-mp-wiki/reagents/serotonin/), psilocin, [LSD](/xray-mp-wiki/reagents/lsd/), [lisuride](/xray-mp-wiki/reagents/lisuride/), lumateperone, and the β-arrestin-biased agonist IHCH-7086 (PDB 7WC4-7WC9) revealed a second binding mode (extended binding pocket, EBP) for [serotonin](/xray-mp-wiki/reagents/serotonin/) and psilocin, and enabled the structure-based design of nonhallucinogenic psychedelic analogs with antidepressant-like activity.


## Publications

### doi/10.1038##s41594-018-0180-z

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6a93">6A93</a></td>
      <td>3.0 A</td>
      <td>C2</td>
      <td>Human 5-HT2A receptor with N-terminal (1-69) and C-terminal (404-471) deletions, ICL3 (Thr266-Met312) replaced with mbIIG fusion (modified apocytochrome b562 IIG), thermostability mutations S162K^3.39 and M164W^3.41. N-terminal HA signal sequence + <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag">FLAG Tag</a> + 10xHis tag + TEV protease recognition site.</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/risperidone">Risperidone</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6a94">6A94</a></td>
      <td>2.9 A</td>
      <td>C2</td>
      <td>Human 5-HT2A receptor with N-terminal (1-69) and C-terminal (404-471) deletions, ICL3 (Thr266-Met312) replaced with mbIIG fusion (modified apocytochrome b562 IIG), thermostability mutations S162K^3.39 and M164W^3.41. N-terminal HA signal sequence + <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag">FLAG Tag</a> + 10xHis tag + TEV protease recognition site.</td>
      <td>Zotepine</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: [Sf9 Cells](/xray-mp-wiki/methods/expression-systems/sf9-expression-system) (Bac-to-Bac Baculovirus Expression System)
- **Construct**: Human 5-HT2A receptor with N-terminal (1-69) and C-terminal (404-471) deletions, ICL3 (Thr266-Met312) replaced with mbIIG fusion, thermostability mutations S162K^3.39 and M164W^3.41
- **Notes**: Cloned into pFastBacI vector with HA signal sequence, [FLAG tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), 10xHis tag, [TEV protease](/xray-mp-wiki/reagents/additives/tev-protease/) recognition site. Sf9 cells cultured in [PMSF](/xray-mp-wiki/reagents/additives/pmsf/)-J1 medium with 2% FBS, infected at MOI of 2, harvested 48 h post-infection.

**Purification:**

- **Expression system**: Sf9 insect cells (baculovirus)
- **Expression construct**: 5-HT2A R-mbIIG with N/C-terminal truncations, thermostability mutations, and mbIIG fusion in ICL3
- **Tag info**: N-terminal HA signal + FLAG tag + 10xHis tag + TEV site

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
      <td>Thawing and hypotonic lysis</td>
      <td>--</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.5, 10 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">MgCl2</a>, 20 mM <a href="/xray-mp-wiki/reagents/additives/potassium-chloride-kcl/">KCl</a>, <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>-free protease inhibitor cocktail + --</td>
      <td>Thawed cell pellets disrupted in hypotonic buffer. Extensive washing by centrifugation.</td>
    </tr>
    <tr>
      <td>High-salt wash</td>
      <td>Centrifugation wash</td>
      <td>--</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.5, 1 M NaCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">MgCl2</a>, 20 mM <a href="/xray-mp-wiki/reagents/additives/potassium-chloride-kcl/">KCl</a>, protease inhibitor + --</td>
      <td>Removes soluble and membrane-associated proteins</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.5, 800 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, protease inhibitor, 25 µM <a href="/xray-mp-wiki/reagents/ligands/risperidone/">risperidone</a> or <a href="/xray-mp-wiki/reagents/ligands/zotepine/">zotepine</a> + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> (n-Dodecyl-beta-D-maltopyranoside)</td>
      <td>Ligand pre-incubated with membranes before solubilization to stabilize the receptor</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography">IMAC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">IMAC</a> resin</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.5, 800 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a> + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>C-terminal 10xHis tag used for affinity capture</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">SEC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Size Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">SEC</a> column</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.5, 800 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a> + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Final purification step to obtain monodisperse 5-HT2A-R-<a href="/xray-mp-wiki/reagents/protein-tags/bril">mbIIG</a> complex</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">LCP Crystallization</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>5-HT2A R-<a href="/xray-mp-wiki/reagents/protein-tags/bril">mbIIG</a>-<a href="/xray-mp-wiki/reagents/ligands/risperidone/">risperidone</a> or 5-HT2A R-<a href="/xray-mp-wiki/reagents/protein-tags/bril">mbIIG</a>-<a href="/xray-mp-wiki/reagents/ligands/zotepine/">zotepine</a> complex</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein">Monoolein</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Structures solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">molecular replacement</a>. Data collected at SPring-8 beamlines. Space group C2 for both complexes.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6a93">6A93</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GG</span><span class="topo-outside">THLQE</span><span class="topo-membrane">KNWSALLTAVVIILTIAGNILVIM</span><span class="topo-inside">AVSLEKKLQNATNYFL</span><span class="topo-membrane">MSLAIADMLLGFLVMPVSMLTIL</span><span class="topo-outside">YGYRWPLPSK</span><span class="topo-membrane">LCAVWIYLDVLFSTAKIWHLCA</span><span class="topo-inside">ISLDRYVAIQNPIHHSRF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">NSRTKAFLKI</span><span class="topo-membrane">IAVWTISVGISMPIPVFGLQD</span><span class="topo-outside">DSKVFKEGSC</span><span class="topo-membrane">LLADDNFVLIGSFVSFFIPLTIMV</span><span class="topo-inside">ITYFLTIKSLQKEAADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SGSGDILVGQIDDALKLANEGKVKEAQAAAEQLKTTINAYIQKYGQSISNEQKACKVLGI</span><span class="topo-membrane">VFFLFVVMWCPFFITNIMAVICK</span><span class="topo-outside">ESCNEDV</span><span class="topo-membrane">IGALLNVFVWIGYLSSAVNPLV</span><span class="topo-inside">YTLFNKTY</span></span>
<span class="topo-ruler">       370      </span>
<span class="topo-line"><span class="topo-inside">RSAFSRYIQCQY</span><span class="topo-unknown">KENK</span></span>
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
      <td>7</td>
      <td>69</td>
      <td>73</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>31</td>
      <td>74</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>47</td>
      <td>98</td>
      <td>113</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>70</td>
      <td>114</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>71</td>
      <td>80</td>
      <td>137</td>
      <td>146</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>102</td>
      <td>147</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>130</td>
      <td>169</td>
      <td>196</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>131</td>
      <td>151</td>
      <td>197</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>152</td>
      <td>161</td>
      <td>218</td>
      <td>227</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>162</td>
      <td>185</td>
      <td>228</td>
      <td>251</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>186</td>
      <td>300</td>
      <td>252</td>
      <td>327</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>301</td>
      <td>323</td>
      <td>328</td>
      <td>350</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>324</td>
      <td>330</td>
      <td>351</td>
      <td>357</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>331</td>
      <td>352</td>
      <td>358</td>
      <td>379</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>353</td>
      <td>372</td>
      <td>380</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6a94">6A94</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GG</span><span class="topo-outside">THLQE</span><span class="topo-membrane">KNWSALLTAVVIILTIAGNILVIM</span><span class="topo-inside">AVSLEKKLQNATNYF</span><span class="topo-membrane">LMSLAIADMLLGFLVMPVSMLTIL</span><span class="topo-outside">YGYRW</span><span class="topo-membrane">PLPSKLCAVWIYLDVLFSTAKIWHLCAISL</span><span class="topo-inside">DRYVAIQNPIHHSRF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">NSRTKAFLK</span><span class="topo-membrane">IIAVWTISVGISMPIPVFGLQDD</span><span class="topo-outside">SKVFKEGSC</span><span class="topo-membrane">LLADDNFVLIGSFVSFFIPLTIMVITYFL</span><span class="topo-inside">TIKSLQKEAADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SGSGDILVGQIDDALKLANEGKVKEAQAAAEQLKTTINAYIQKYGQSISNEQKACK</span><span class="topo-membrane">VLGIVFFLFVVMWCPFFITNIMAVI</span><span class="topo-outside">CKESCNEDVI</span><span class="topo-membrane">GALLNVFVWIGYLSSAVNPLVYTLF</span><span class="topo-inside">N</span><span class="topo-unknown">KTY</span></span>
<span class="topo-ruler">       370      </span>
<span class="topo-line"><span class="topo-unknown">RSAFSRYI</span><span class="topo-inside">QCQY</span><span class="topo-unknown">KENK</span></span>
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
      <td>3</td>
      <td>7</td>
      <td>69</td>
      <td>73</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>31</td>
      <td>74</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>46</td>
      <td>98</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>70</td>
      <td>113</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>71</td>
      <td>75</td>
      <td>137</td>
      <td>141</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>76</td>
      <td>105</td>
      <td>142</td>
      <td>171</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>129</td>
      <td>172</td>
      <td>195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>152</td>
      <td>196</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>153</td>
      <td>161</td>
      <td>219</td>
      <td>227</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>162</td>
      <td>190</td>
      <td>228</td>
      <td>256</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>296</td>
      <td>257</td>
      <td>323</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>297</td>
      <td>321</td>
      <td>324</td>
      <td>348</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>322</td>
      <td>331</td>
      <td>349</td>
      <td>358</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>332</td>
      <td>356</td>
      <td>359</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>357</td>
      <td>384</td>
      <td>384</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>358</td>
      <td>368</td>
      <td>385</td>
      <td>395</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>369</td>
      <td>372</td>
      <td>396</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##s41594-022-00796-6

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7um4">7UM4</a></td>
      <td></td>
      <td></td>
      <td>Human 5-HT2A receptor in complex with miniGo and lisuride (5-HTSAR-miniGo-Lisuride)</td>
      <td>lisuride</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7um4">7UM4</a></td>
      <td></td>
      <td></td>
      <td>Human 5-HT2A receptor in complex with miniGo and methylgeromertrine (5-HTSAR-miniGo-Methylgeromertrine)</td>
      <td>methylgeromertrine</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7um4">7UM4</a></td>
      <td></td>
      <td></td>
      <td>Human 5-HT2A receptor in complex with miniGo (apo-like state, CT designation)</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: [Sf9 Cells](/xray-mp-wiki/methods/expression-systems/sf9-expression-system) (Bac-to-Bac Baculovirus Expression System)
- **Construct**: Human 5-HT2A receptor with N-terminal (1-69) and C-terminal (404-471) deletions, ICL3 (Thr266-Met312) replaced with mbIIG fusion, thermostability mutations S162K^3.39 and M164W^3.41
- **Notes**: Cloned into pFastBacI vector with HA signal sequence, [FLAG tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), 10xHis tag, [TEV protease](/xray-mp-wiki/reagents/additives/tev-protease/) recognition site. Sf9 cells cultured in [PMSF](/xray-mp-wiki/reagents/additives/pmsf/)-J1 medium with 2% FBS, infected at MOI of 2, harvested 48 h post-infection.

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7um4">7UM4</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">HSLGKDDLRPSSP</span><span class="topo-outside">LLSV</span><span class="topo-membrane">FGVLILTLLGFLVAATFAWNLLVLA</span><span class="topo-inside">TIL</span><span class="topo-unknown">RVRTFHRV</span><span class="topo-inside">PHN</span><span class="topo-membrane">LVASMAVSNVLVAALVMPLSLVHELS</span><span class="topo-outside">GRRWQLGRRL</span><span class="topo-membrane">CQLWIACDVLCCTASIWNVTAIALDRY</span><span class="topo-inside">W</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">SITRHMEYTLRTRKCV</span><span class="topo-membrane">SNVMIALTWALSAVISLAPLLFG</span><span class="topo-outside">WGETYSEGSEECQVSREPS</span><span class="topo-membrane">YAVFSTVGAFYLPLCVVLFVYWKIY</span><span class="topo-inside">KAAKFRV</span><span class="topo-unknown">GSRKTNSVSPISEAVEVKDSAKQPQMVFTV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330      </span>
<span class="topo-line"><span class="topo-unknown">RHATVTFQPEGDTWR</span><span class="topo-inside">EQKEQRAAL</span><span class="topo-membrane">MVGILIGVFVLCWAPFFLTELI</span><span class="topo-outside">SPLCSCDIPAIW</span><span class="topo-membrane">KSIFLWLGYSNSFFNPLIYTA</span><span class="topo-inside">F</span><span class="topo-unknown">NKNYNSAFKNFFSRQH</span></span>
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
      <td>13</td>
      <td>22</td>
      <td>34</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>14</td>
      <td>17</td>
      <td>35</td>
      <td>38</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>42</td>
      <td>39</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>43</td>
      <td>45</td>
      <td>64</td>
      <td>66</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>53</td>
      <td>67</td>
      <td>74</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>54</td>
      <td>56</td>
      <td>75</td>
      <td>77</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>82</td>
      <td>78</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>92</td>
      <td>104</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>119</td>
      <td>114</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>120</td>
      <td>136</td>
      <td>141</td>
      <td>157</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>159</td>
      <td>158</td>
      <td>180</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>178</td>
      <td>181</td>
      <td>199</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>203</td>
      <td>200</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>204</td>
      <td>210</td>
      <td>225</td>
      <td>231</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>255</td>
      <td>232</td>
      <td>276</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>256</td>
      <td>264</td>
      <td>277</td>
      <td>285</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>265</td>
      <td>286</td>
      <td>286</td>
      <td>307</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>287</td>
      <td>298</td>
      <td>308</td>
      <td>319</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>299</td>
      <td>319</td>
      <td>320</td>
      <td>340</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>320</td>
      <td>320</td>
      <td>341</td>
      <td>341</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>336</td>
      <td>342</td>
      <td>357</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7um4">7UM4</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">G</span><span class="topo-inside">SHNGIDCSFWNESYLTGSRDERKKSLLSKFGMDEGVTFMFIGRFDRGQKGVDVLLKAIEILSSKKEFQEMRFIIIGKGDPELEGWARSLEEKHGNVKVITEMLSREFVRELYGSVDFVI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200</span>
<span class="topo-line"><span class="topo-inside">IPSYFEPFGLVALEAMCLGAIPIASAVGGLRDIITNETGILVKAGDPGELANAILKALELSRSDLSKFRENCKKRAMSFS</span></span>
<details class="topo-details"><summary>Topology coordinates (2 regions)</summary>
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
      <td>1</td>
      <td>1001</td>
      <td>1001</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>200</td>
      <td>1002</td>
      <td>1200</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7um4">7UM4</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">HSLGKDDLRPSSP</span><span class="topo-outside">LLSV</span><span class="topo-membrane">FGVLILTLLGFLVAATFAWNLLVLA</span><span class="topo-inside">TIL</span><span class="topo-unknown">RVRTFHRV</span><span class="topo-inside">PHN</span><span class="topo-membrane">LVASMAVSNVLVAALVMPLSLVHELS</span><span class="topo-outside">GRRWQLGRRL</span><span class="topo-membrane">CQLWIACDVLCCTASIWNVTAIALDRY</span><span class="topo-inside">W</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">SITRHMEYTLRTRKCV</span><span class="topo-membrane">SNVMIALTWALSAVISLAPLLFG</span><span class="topo-outside">WGETYSEGSEECQVSREPS</span><span class="topo-membrane">YAVFSTVGAFYLPLCVVLFVYWKIY</span><span class="topo-inside">KAAKFRV</span><span class="topo-unknown">GSRKTNSVSPISEAVEVKDSAKQPQMVFTV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330      </span>
<span class="topo-line"><span class="topo-unknown">RHATVTFQPEGDTWR</span><span class="topo-inside">EQKEQRAAL</span><span class="topo-membrane">MVGILIGVFVLCWAPFFLTELI</span><span class="topo-outside">SPLCSCDIPAIW</span><span class="topo-membrane">KSIFLWLGYSNSFFNPLIYTA</span><span class="topo-inside">F</span><span class="topo-unknown">NKNYNSAFKNFFSRQH</span></span>
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
      <td>13</td>
      <td>22</td>
      <td>34</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>14</td>
      <td>17</td>
      <td>35</td>
      <td>38</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>42</td>
      <td>39</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>43</td>
      <td>45</td>
      <td>64</td>
      <td>66</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>53</td>
      <td>67</td>
      <td>74</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>54</td>
      <td>56</td>
      <td>75</td>
      <td>77</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>82</td>
      <td>78</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>92</td>
      <td>104</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>119</td>
      <td>114</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>120</td>
      <td>136</td>
      <td>141</td>
      <td>157</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>159</td>
      <td>158</td>
      <td>180</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>178</td>
      <td>181</td>
      <td>199</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>203</td>
      <td>200</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>204</td>
      <td>210</td>
      <td>225</td>
      <td>231</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>255</td>
      <td>232</td>
      <td>276</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>256</td>
      <td>264</td>
      <td>277</td>
      <td>285</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>265</td>
      <td>286</td>
      <td>286</td>
      <td>307</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>287</td>
      <td>298</td>
      <td>308</td>
      <td>319</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>299</td>
      <td>319</td>
      <td>320</td>
      <td>340</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>320</td>
      <td>320</td>
      <td>341</td>
      <td>341</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>336</td>
      <td>342</td>
      <td>357</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7um4">7UM4</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">G</span><span class="topo-inside">SHNGIDCSFWNESYLTGSRDERKKSLLSKFGMDEGVTFMFIGRFDRGQKGVDVLLKAIEILSSKKEFQEMRFIIIGKGDPELEGWARSLEEKHGNVKVITEMLSREFVRELYGSVDFVI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200</span>
<span class="topo-line"><span class="topo-inside">IPSYFEPFGLVALEAMCLGAIPIASAVGGLRDIITNETGILVKAGDPGELANAILKALELSRSDLSKFRENCKKRAMSFS</span></span>
<details class="topo-details"><summary>Topology coordinates (2 regions)</summary>
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
      <td>1</td>
      <td>1001</td>
      <td>1001</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>200</td>
      <td>1002</td>
      <td>1200</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7um4">7UM4</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">HSLGKDDLRPSSP</span><span class="topo-outside">LLSV</span><span class="topo-membrane">FGVLILTLLGFLVAATFAWNLLVLA</span><span class="topo-inside">TIL</span><span class="topo-unknown">RVRTFHRV</span><span class="topo-inside">PHN</span><span class="topo-membrane">LVASMAVSNVLVAALVMPLSLVHELS</span><span class="topo-outside">GRRWQLGRRL</span><span class="topo-membrane">CQLWIACDVLCCTASIWNVTAIALDRY</span><span class="topo-inside">W</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">SITRHMEYTLRTRKCV</span><span class="topo-membrane">SNVMIALTWALSAVISLAPLLFG</span><span class="topo-outside">WGETYSEGSEECQVSREPS</span><span class="topo-membrane">YAVFSTVGAFYLPLCVVLFVYWKIY</span><span class="topo-inside">KAAKFRV</span><span class="topo-unknown">GSRKTNSVSPISEAVEVKDSAKQPQMVFTV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330      </span>
<span class="topo-line"><span class="topo-unknown">RHATVTFQPEGDTWR</span><span class="topo-inside">EQKEQRAAL</span><span class="topo-membrane">MVGILIGVFVLCWAPFFLTELI</span><span class="topo-outside">SPLCSCDIPAIW</span><span class="topo-membrane">KSIFLWLGYSNSFFNPLIYTA</span><span class="topo-inside">F</span><span class="topo-unknown">NKNYNSAFKNFFSRQH</span></span>
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
      <td>13</td>
      <td>22</td>
      <td>34</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>14</td>
      <td>17</td>
      <td>35</td>
      <td>38</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>42</td>
      <td>39</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>43</td>
      <td>45</td>
      <td>64</td>
      <td>66</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>53</td>
      <td>67</td>
      <td>74</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>54</td>
      <td>56</td>
      <td>75</td>
      <td>77</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>82</td>
      <td>78</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>92</td>
      <td>104</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>119</td>
      <td>114</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>120</td>
      <td>136</td>
      <td>141</td>
      <td>157</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>159</td>
      <td>158</td>
      <td>180</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>178</td>
      <td>181</td>
      <td>199</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>203</td>
      <td>200</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>204</td>
      <td>210</td>
      <td>225</td>
      <td>231</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>255</td>
      <td>232</td>
      <td>276</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>256</td>
      <td>264</td>
      <td>277</td>
      <td>285</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>265</td>
      <td>286</td>
      <td>286</td>
      <td>307</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>287</td>
      <td>298</td>
      <td>308</td>
      <td>319</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>299</td>
      <td>319</td>
      <td>320</td>
      <td>340</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>320</td>
      <td>320</td>
      <td>341</td>
      <td>341</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>336</td>
      <td>342</td>
      <td>357</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7um4">7UM4</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">G</span><span class="topo-inside">SHNGIDCSFWNESYLTGSRDERKKSLLSKFGMDEGVTFMFIGRFDRGQKGVDVLLKAIEILSSKKEFQEMRFIIIGKGDPELEGWARSLEEKHGNVKVITEMLSREFVRELYGSVDFVI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200</span>
<span class="topo-line"><span class="topo-inside">IPSYFEPFGLVALEAMCLGAIPIASAVGGLRDIITNETGILVKAGDPGELANAILKALELSRSDLSKFRENCKKRAMSFS</span></span>
<details class="topo-details"><summary>Topology coordinates (2 regions)</summary>
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
      <td>1</td>
      <td>1001</td>
      <td>1001</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>200</td>
      <td>1002</td>
      <td>1200</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1126##science.abl8615

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7wc4">7WC4</a></td>
      <td>3.0 A</td>
      <td></td>
      <td>Human 5-HT2AR in complex with serotonin</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/serotonin">Serotonin</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7wc5">7WC5</a></td>
      <td>3.0 A</td>
      <td></td>
      <td>Human 5-HT2AR in complex with psilocin</td>
      <td>Psilocin</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7wc6">7WC6</a></td>
      <td>2.6 A</td>
      <td></td>
      <td>Human 5-HT2AR in complex with LSD</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/lsd">LSD</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7wc7">7WC7</a></td>
      <td>2.6 A</td>
      <td></td>
      <td>Human 5-HT2AR in complex with lisuride</td>
      <td>Lisuride</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7wc8">7WC8</a></td>
      <td></td>
      <td></td>
      <td>Human 5-HT2AR in complex with lumateperone</td>
      <td>Lumateperone</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7wc9">7WC9</a></td>
      <td></td>
      <td></td>
      <td>Human 5-HT2AR in complex with IHCH-7086</td>
      <td>IHCH-7086</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: [Sf9 Cells](/xray-mp-wiki/methods/expression-systems/sf9-expression-system) (Bac-to-Bac Baculovirus Expression System)
- **Construct**: Human 5-HT2A receptor with N-terminal (1-69) and C-terminal (404-471) deletions, ICL3 (Thr266-Met312) replaced with mbIIG fusion, thermostability mutations S162K^3.39 and M164W^3.41
- **Notes**: Cloned into pFastBacI vector with HA signal sequence, [FLAG tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), 10xHis tag, [TEV protease](/xray-mp-wiki/reagents/additives/tev-protease/) recognition site. Sf9 cells cultured in [PMSF](/xray-mp-wiki/reagents/additives/pmsf/)-J1 medium with 2% FBS, infected at MOI of 2, harvested 48 h post-infection.

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wc4">7WC4</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">SLLHLQEKNW</span><span class="topo-membrane">SALLTAVVIILTIAGNILV</span><span class="topo-inside">IMAVSLEKKLQNATNYFLMS</span><span class="topo-membrane">LAIADMLLGFLVMPVSMLTIL</span><span class="topo-outside">YGYRW</span><span class="topo-membrane">PLPSKLCAVWIYLDVLFSTAKIWHL</span><span class="topo-inside">CAISLDRYVAIQNPIHHSRF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">NSRTKAFLKIIAVW</span><span class="topo-membrane">TISVGISMPIPVFGLQDDS</span><span class="topo-outside">KVFKEGS</span><span class="topo-membrane">CLLADDNFVLIGSFVSFFIPLT</span><span class="topo-inside">IMVITYFLTIKSLQKEAADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">SGSG</span><span class="topo-inside">DILVGQIDDALKLANEGKVKEAQAAAEQLKTTINAYIQKYGQSISNEQKACKVLGI</span><span class="topo-membrane">VFFLFVVMWCPFFITNIMAVICK</span><span class="topo-outside">ESCNEDVI</span><span class="topo-membrane">GALLNVFVWIGYLNSAVNPLV</span><span class="topo-inside">YTLFNKTY</span></span>
<span class="topo-ruler">       370      </span>
<span class="topo-line"><span class="topo-inside">RSAFSRYIQCQYKE</span><span class="topo-unknown">NK</span></span>
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
      <td>10</td>
      <td>67</td>
      <td>76</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>29</td>
      <td>77</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>49</td>
      <td>96</td>
      <td>115</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>50</td>
      <td>70</td>
      <td>116</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>71</td>
      <td>75</td>
      <td>137</td>
      <td>141</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>76</td>
      <td>100</td>
      <td>142</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>134</td>
      <td>167</td>
      <td>200</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>135</td>
      <td>153</td>
      <td>201</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>154</td>
      <td>160</td>
      <td>220</td>
      <td>226</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>182</td>
      <td>227</td>
      <td>248</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>240</td>
      <td>249</td>
      <td>1041</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>241</td>
      <td>244</td>
      <td>1042</td>
      <td>1045</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>245</td>
      <td>285</td>
      <td>1066</td>
      <td>1106</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>300</td>
      <td>313</td>
      <td>327</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>301</td>
      <td>323</td>
      <td>328</td>
      <td>350</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>324</td>
      <td>331</td>
      <td>351</td>
      <td>358</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>332</td>
      <td>352</td>
      <td>359</td>
      <td>379</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>353</td>
      <td>374</td>
      <td>380</td>
      <td>401</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>375</td>
      <td>376</td>
      <td>402</td>
      <td>403</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wc5">7WC5</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">SLLHLQEK</span><span class="topo-membrane">NWSALLTAVVIILTIAGNILVIM</span><span class="topo-inside">AVSLEKKLQNATNYF</span><span class="topo-membrane">LMSLAIADMLLGFLVMPVSMLTIL</span><span class="topo-outside">YGYRWPLPSK</span><span class="topo-membrane">LCAVWIYLDVLFSTAKIWHLCAIS</span><span class="topo-inside">LDRYVAIQNP</span><span class="topo-unknown">IHHSRF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">N</span><span class="topo-inside">SRTKAF</span><span class="topo-membrane">LKIIAVWTISVGISMPIPVFGLQ</span><span class="topo-outside">DDSKVFKEGSC</span><span class="topo-membrane">LLADDNFVLIGSFVSFFIPLTIMVI</span><span class="topo-inside">TYFLTIKSLQKEAADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">SGSG</span><span class="topo-inside">DILVGQIDDALKLANEGKVKEAQAAAEQLKTTINAYIQKYGQSISNEQKACKVL</span><span class="topo-membrane">GIVFFLFVVMWCPFFITNIMAVICK</span><span class="topo-outside">ESCNEDV</span><span class="topo-membrane">IGALLNVFVWIGYLNSAVNPLVYTL</span><span class="topo-inside">FNKTY</span></span>
<span class="topo-ruler">       370      </span>
<span class="topo-line"><span class="topo-inside">RSAFSRYIQCQYKE</span><span class="topo-unknown">NK</span></span>
<details class="topo-details"><summary>Topology coordinates (20 regions)</summary>
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
      <td>67</td>
      <td>74</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>31</td>
      <td>75</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>46</td>
      <td>98</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>70</td>
      <td>113</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>71</td>
      <td>80</td>
      <td>137</td>
      <td>146</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>104</td>
      <td>147</td>
      <td>170</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>114</td>
      <td>171</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>121</td>
      <td>181</td>
      <td>187</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>122</td>
      <td>127</td>
      <td>188</td>
      <td>193</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>128</td>
      <td>150</td>
      <td>194</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>151</td>
      <td>161</td>
      <td>217</td>
      <td>227</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>162</td>
      <td>186</td>
      <td>228</td>
      <td>252</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>240</td>
      <td>253</td>
      <td>1041</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>241</td>
      <td>244</td>
      <td>1042</td>
      <td>1045</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>245</td>
      <td>298</td>
      <td>1066</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>299</td>
      <td>323</td>
      <td>326</td>
      <td>350</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>324</td>
      <td>330</td>
      <td>351</td>
      <td>357</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>331</td>
      <td>355</td>
      <td>358</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>356</td>
      <td>374</td>
      <td>383</td>
      <td>401</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>375</td>
      <td>376</td>
      <td>402</td>
      <td>403</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wc6">7WC6</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">SLLHLQE</span><span class="topo-outside">KN</span><span class="topo-membrane">WSALLTAVVIILTIAGNILVIM</span><span class="topo-inside">AVSLEKKLQNATNYF</span><span class="topo-membrane">LMSLAIADMLLGFLVMPVSMLTIL</span><span class="topo-outside">YGYRWPL</span><span class="topo-membrane">PSKLCAVWIYLDVLFSTAKIWHLCA</span><span class="topo-inside">ISLDRYVAIQNP</span><span class="topo-unknown">IHHSRF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">N</span><span class="topo-inside">SRTKAFLKI</span><span class="topo-membrane">IAVWTISVGISMPIPVFGLQD</span><span class="topo-outside">DSKVFKEGSC</span><span class="topo-membrane">LLADDNFVLIGSFVSFFIPLTIMVI</span><span class="topo-inside">TYFLTIKSLQKEAADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDA</span><span class="topo-unknown">G</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">SGSG</span><span class="topo-inside">DILVGQIDDALKLANEGKVKEAQAAAEQLKTTINAYIQKYGQSISNEQKACKVL</span><span class="topo-membrane">GIVFFLFVVMWCPFFITNIMAVICK</span><span class="topo-outside">ESCNEDVI</span><span class="topo-membrane">GALLNVFVWIGYLNSAVNPLVYTL</span><span class="topo-inside">FNKTY</span></span>
<span class="topo-ruler">       370      </span>
<span class="topo-line"><span class="topo-inside">RSAFSRYIQCQYKE</span><span class="topo-unknown">NK</span></span>
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
      <td>7</td>
      <td>67</td>
      <td>73</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>9</td>
      <td>74</td>
      <td>75</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>31</td>
      <td>76</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>46</td>
      <td>98</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>70</td>
      <td>113</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>71</td>
      <td>77</td>
      <td>137</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>102</td>
      <td>144</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>114</td>
      <td>169</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>121</td>
      <td>181</td>
      <td>187</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>122</td>
      <td>130</td>
      <td>188</td>
      <td>196</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>131</td>
      <td>151</td>
      <td>197</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>152</td>
      <td>161</td>
      <td>218</td>
      <td>227</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>162</td>
      <td>186</td>
      <td>228</td>
      <td>252</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>239</td>
      <td>253</td>
      <td>1040</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>244</td>
      <td>1041</td>
      <td>1045</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>245</td>
      <td>298</td>
      <td>1066</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>299</td>
      <td>323</td>
      <td>326</td>
      <td>350</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>324</td>
      <td>331</td>
      <td>351</td>
      <td>358</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>332</td>
      <td>355</td>
      <td>359</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>356</td>
      <td>374</td>
      <td>383</td>
      <td>401</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>375</td>
      <td>376</td>
      <td>402</td>
      <td>403</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wc7">7WC7</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">SLLH</span><span class="topo-outside">LQEK</span><span class="topo-membrane">NWSALLTAVVIILTIAGNILVIM</span><span class="topo-inside">AVSLEKKLQNATNYF</span><span class="topo-membrane">LMSLAIADMLLGFLVMPVSMLTIL</span><span class="topo-outside">YGYRWPLPSK</span><span class="topo-membrane">LCAVWIYLDVLFSTAKIWHLCAI</span><span class="topo-inside">SLDRYVAIQNP</span><span class="topo-unknown">IHHSRF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">N</span><span class="topo-inside">SRTKAFL</span><span class="topo-membrane">KIIAVWTISVGISMPIPVFGLQ</span><span class="topo-outside">DDSKVFKEGSC</span><span class="topo-membrane">LLADDNFVLIGSFVSFFIPLTIMVI</span><span class="topo-inside">TYFLTIKSLQKEAADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDA</span><span class="topo-unknown">G</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">SGSG</span><span class="topo-inside">DILVGQIDDALKLANEGKVKEAQAAAEQLKTTINAYIQKYGQSISNEQKACKVL</span><span class="topo-membrane">GIVFFLFVVMWCPFFITNIMAVICK</span><span class="topo-outside">ESCNEDV</span><span class="topo-membrane">IGALLNVFVWIGYLNSAVNPLVYT</span><span class="topo-inside">LFNKTY</span></span>
<span class="topo-ruler">       370      </span>
<span class="topo-line"><span class="topo-inside">RSAFSRYIQCQYKE</span><span class="topo-unknown">NK</span></span>
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
      <td>4</td>
      <td>67</td>
      <td>70</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>8</td>
      <td>71</td>
      <td>74</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>31</td>
      <td>75</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>46</td>
      <td>98</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>70</td>
      <td>113</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>71</td>
      <td>80</td>
      <td>137</td>
      <td>146</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>103</td>
      <td>147</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>104</td>
      <td>114</td>
      <td>170</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>121</td>
      <td>181</td>
      <td>187</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>122</td>
      <td>128</td>
      <td>188</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>150</td>
      <td>195</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>151</td>
      <td>161</td>
      <td>217</td>
      <td>227</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>162</td>
      <td>186</td>
      <td>228</td>
      <td>252</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>239</td>
      <td>253</td>
      <td>1040</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>244</td>
      <td>1041</td>
      <td>1045</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>245</td>
      <td>298</td>
      <td>1066</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>299</td>
      <td>323</td>
      <td>326</td>
      <td>350</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>324</td>
      <td>330</td>
      <td>351</td>
      <td>357</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>331</td>
      <td>354</td>
      <td>358</td>
      <td>381</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>355</td>
      <td>374</td>
      <td>382</td>
      <td>401</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>375</td>
      <td>376</td>
      <td>402</td>
      <td>403</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wc8">7WC8</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">SLL</span><span class="topo-outside">HLQEKN</span><span class="topo-membrane">WSALLTAVVIILTIAGNILVIM</span><span class="topo-inside">AVSLEKKLQNATNYF</span><span class="topo-membrane">LMSLAIADMLLGFLVMPVSMLTIL</span><span class="topo-outside">YGYRWPL</span><span class="topo-membrane">PSKLCAVWIYLDVLFSTAKIWHLCA</span><span class="topo-inside">ISLDRYVAIQNPI</span><span class="topo-unknown">HHSRF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">N</span><span class="topo-inside">SRTKAFLKI</span><span class="topo-membrane">IAVWTISVGISMPIPVFGLQD</span><span class="topo-outside">DSKVFKEGSC</span><span class="topo-membrane">LLADDNFVLIGSFVSFFIPLTIMVI</span><span class="topo-inside">TYFLTIKSLQKEAADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDA</span><span class="topo-unknown">G</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">SGSG</span><span class="topo-inside">DILVGQIDDALKLANEGKVKEAQAAAEQLKTTINAYIQKYGQSISNEQKACKVL</span><span class="topo-membrane">GIVFFLFVVMWCPFFITNIMAVICK</span><span class="topo-outside">ESCNEDV</span><span class="topo-membrane">IGALLNVFVWIGYLNSAVNPLVYTL</span><span class="topo-inside">FNKTY</span></span>
<span class="topo-ruler">       370      </span>
<span class="topo-line"><span class="topo-inside">RSAFSRYIQCQYKE</span><span class="topo-unknown">NK</span></span>
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
      <td>3</td>
      <td>67</td>
      <td>69</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>9</td>
      <td>70</td>
      <td>75</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>31</td>
      <td>76</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>46</td>
      <td>98</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>70</td>
      <td>113</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>71</td>
      <td>77</td>
      <td>137</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>102</td>
      <td>144</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>115</td>
      <td>169</td>
      <td>181</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>121</td>
      <td>182</td>
      <td>187</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>122</td>
      <td>130</td>
      <td>188</td>
      <td>196</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>131</td>
      <td>151</td>
      <td>197</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>152</td>
      <td>161</td>
      <td>218</td>
      <td>227</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>162</td>
      <td>186</td>
      <td>228</td>
      <td>252</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>239</td>
      <td>253</td>
      <td>1040</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>244</td>
      <td>1041</td>
      <td>1045</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>245</td>
      <td>298</td>
      <td>1066</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>299</td>
      <td>323</td>
      <td>326</td>
      <td>350</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>324</td>
      <td>330</td>
      <td>351</td>
      <td>357</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>331</td>
      <td>355</td>
      <td>358</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>356</td>
      <td>374</td>
      <td>383</td>
      <td>401</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>375</td>
      <td>376</td>
      <td>402</td>
      <td>403</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wc9">7WC9</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">SLLH</span><span class="topo-outside">LQEKN</span><span class="topo-membrane">WSALLTAVVIILTIAGNILVIM</span><span class="topo-inside">AVSLEKKLQNATNYF</span><span class="topo-membrane">LMSLAIADMLLGFLVMPVSMLTIL</span><span class="topo-outside">YGYRWP</span><span class="topo-membrane">LPSKLCAVWIYLDVLFSTAKIWHLCAISL</span><span class="topo-inside">DRYVAIQNP</span><span class="topo-unknown">IHHSRF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">N</span><span class="topo-inside">SRTKAF</span><span class="topo-membrane">LKIIAVWTISVGISMPIPVFGLQ</span><span class="topo-outside">DDSKVFKEGSC</span><span class="topo-membrane">LLADDNFVLIGSFVSFFIPLTIMVITYFL</span><span class="topo-inside">TIKSLQKEAADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDA</span><span class="topo-unknown">G</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">SGSG</span><span class="topo-inside">DILVGQIDDALKLANEGKVKEAQAAAEQLKTTINAYIQKYGQSISNEQKACK</span><span class="topo-membrane">VLGIVFFLFVVMWCPFFITNIMAVI</span><span class="topo-outside">CKESCNEDVI</span><span class="topo-membrane">GALLNVFVWIGYLNSAVNPLVYTL</span><span class="topo-inside">FNKTY</span></span>
<span class="topo-ruler">       370      </span>
<span class="topo-line"><span class="topo-inside">RSAFSRYIQCQYKE</span><span class="topo-unknown">NK</span></span>
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
      <td>4</td>
      <td>67</td>
      <td>70</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>9</td>
      <td>71</td>
      <td>75</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>31</td>
      <td>76</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>46</td>
      <td>98</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>70</td>
      <td>113</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>71</td>
      <td>76</td>
      <td>137</td>
      <td>142</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>105</td>
      <td>143</td>
      <td>171</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>114</td>
      <td>172</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>121</td>
      <td>181</td>
      <td>187</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>122</td>
      <td>127</td>
      <td>188</td>
      <td>193</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>128</td>
      <td>150</td>
      <td>194</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>151</td>
      <td>161</td>
      <td>217</td>
      <td>227</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>162</td>
      <td>190</td>
      <td>228</td>
      <td>256</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>239</td>
      <td>257</td>
      <td>1040</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>244</td>
      <td>1041</td>
      <td>1045</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>245</td>
      <td>296</td>
      <td>1066</td>
      <td>323</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>297</td>
      <td>321</td>
      <td>324</td>
      <td>348</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>322</td>
      <td>331</td>
      <td>349</td>
      <td>358</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>332</td>
      <td>355</td>
      <td>359</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>356</td>
      <td>374</td>
      <td>383</td>
      <td>401</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>375</td>
      <td>376</td>
      <td>402</td>
      <td>403</td>
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

### Side-extended cavity unique to 5-HT2A

Comparison of the 5-HT2A and 5-HT2C receptor structures reveals a unique side-extended cavity near the orthosteric binding site in 5-HT2A. This cavity is formed by residues Phe234^5.38, Phe213^4.63, and the rotameric conformation of Phe234^5.38, which differs from the equivalent residues in 5-HT2B and 5-HT2C. Docking studies suggest that the 5-HT2A-selective antagonist pimavanserin binds to this side-extended cavity, with the fluorobenzyl ring engaging Trp336^6.48 through edge-to-face pi interactions.

### Antipsychotics stabilize inactive conformation via PIF motif

[Risperidone](/xray-mp-wiki/reagents/risperidone/) and [zotepine](/xray-mp-wiki/reagents/zotepine/) effectively stabilize the inactive conformation of 5-HT2A by forming direct contacts with residues at the bottom of the ligand-binding pocket, particularly those in the PIF motif (Ile163^3.40, Phe332^6.44, Trp336^6.48). Both antipsychotics make direct contacts with Phe332^6.44 and are sandwiched between residues at positions 5.46 and 7.39. Mutation of these residues to alanine or leucine substantially decreases or abolishes inverse agonist activity, confirming their importance in stabilizing the inactive state.

### Conformational differences among 5-HT2 receptors

Among aminergic receptor structures, 5-HT2A is most similar to 5-HT2C and less similar to 5-HT2B. The 5-HT2B receptor exhibits outward shifts of TM5 and TM6 and an inward shift of TM3 compared with 5-HT2A, similar to differences observed between inactive and agonist-bound 5-HT2C structures. The extracellular loop 2 (ECL2) of 5-HT2B contains six additional residues and one turn shorter TM4 compared to 5-HT2A, resulting in a unique ECL2 conformation that influences the ligand-binding pocket architecture.

### Comparison with D2R binding site

Comparison of 5-HT2A and D2 [dopamine](/xray-mp-wiki/reagents/dopamine/) receptor structures reveals that while [risperidone](/xray-mp-wiki/reagents/risperidone/) occupies a similar position in both receptors (fluorobenzisoxazol ring in the bottom hydrophobic cleft), significant differences exist around extracellular loops 1 and 2 (ECL1 and ECL2). The structure of the ligand-binding pocket at these regions differs substantially between 5-HT2A and D2R, providing a structural basis for developing receptor-selective antipsychotics.

### LSD binding mode in 5-HT2A homology model

Homology modeling of 5-HT2A based on 5-HT2B-R/[LSD](/xray-mp-wiki/reagents/lsd/) crystal structure shows that [LSD (Lysergic Acid Diethylamide)](/xray-mp-wiki/reagents/ligands/lsd) binding mode is recapitulated in the 5-HT2A receptor. Key interactions include a salt bridge between the basic amine and D138^3.32, and a hydrogen bond between the indole nitrogen and S242^5.42 (versus G221^5.42 in 5-HT2B). Docking of [LSD](/xray-mp-wiki/reagents/lsd/) and its derivatives (SSAz, RRAz, LSA) into the 5-HT2A model confirms that the crystallographic 5-HT2B binding mode is conserved. The rigidified substituent of SSAz adopts an almost identical orientation to [LSD](/xray-mp-wiki/reagents/lsd/) in receptor-bound form, while RRAz and LSA show different orientations with reduced receptor engagement.

### Extremely slow LSD dissociation kinetics at 5-HT2A

[LSD](/xray-mp-wiki/reagents/lsd/) dissociates exceptionally slowly from 5-HT2A receptors with a residence time of approximately 221 minutes at 37 degrees C. The EL2 lid residue L229 at position EL2 (equivalent to L209^EL2 in 5-HT2B) forms a structural latch. Mutation of L229A^EL2 decreases [LSD](/xray-mp-wiki/reagents/lsd/) residence time to 50 minutes, a 4.4-fold acceleration. This accelerated kinetics selectively disrupts [Beta-Arrestin](/xray-mp-wiki/concepts/beta-arrestin)2 recruitment while leaving Gq function intact, mirroring the phenotype observed at 5-HT2B receptors.

### Time-dependent augmentation of signaling

At wild-type 5-HT2A receptors, [LSD](/xray-mp-wiki/reagents/lsd/) potency and efficacy for [Beta-Arrestin](/xray-mp-wiki/concepts/beta-arrestin)2 recruitment increase with longer compound stimulation, exhibiting time-dependent augmentation. This is abrogated by the L229A^EL2 mutation, which results in weak [LSD](/xray-mp-wiki/reagents/lsd/) potency and efficacy that does not change over time. Gq-mediated IP accumulation shows time-dependent augmentation at wild-type but is not substantially affected by the EL2 mutation. This indicates that EL2-mediated residence time selectively controls the time-dependency of beta-arrestin2 translocation.

### Lipid activation of 5-HT2AR via side-extended pocket (SEP)

Crystal structures revealed that [monoolein](/xray-mp-wiki/reagents/monoolein/) binds to a side-extended pocket (SEP) in 5-HT2AR, formed by a conserved [glycine](/xray-mp-wiki/reagents/glycine/) at position G238^5.42. This SEP is distinct from the orthosteric binding pocket (OBP) and extended binding pocket (EBP). [Monoolein](/xray-mp-wiki/reagents/monoolein/) acts as a G protein-mediated calcium flux partial agonist at 5-HT2AR. The endogenous fatty acid amide oleamide, OEA, and 2OG also activate 5-HT2AR-mediated signaling via the SEP. Introducing a G238^5.42S substitution abolished the agonist activity of lipids but not of [serotonin](/xray-mp-wiki/reagents/serotonin/). Lipids did not induce robust G protein signaling at 5-HT2BR or 5-HT2CR, where the [glycine](/xray-mp-wiki/reagents/glycine/) is not conserved. These results provide a structural basis for the long-standing observation that 5-HT2AR signaling is modulated by lipids.

### Second binding mode of serotonin and psilocin at the EBP

Unlike previous docking results, crystal structures showed that the indole core of [serotonin](/xray-mp-wiki/reagents/serotonin/) or psilocin fits into a narrow cleft previously described as the extended binding pocket (EBP), lined mainly by hydrophobic side chains from residues in EL2 and transmembrane helices TM3, TM6, and TM7. Both ligands form a salt bridge between D155^3.32 and the terminal basic nitrogen as well as an extra hydrogen bond between N352^6.55 and the hydroxyl group on the indole core. Mutagenesis of EBP residues (W151^3.28, L362^7.35) substantially decreased or abolished agonist activity. The L362^7.35F substitution did not affect the potency of Gq agonism, but abolished psilocin and [lisuride](/xray-mp-wiki/reagents/lisuride/) β-arrestin association, indicating that ligand recognition in the EBP, specifically at L362^7.35, affects ligand bias.

### Structure-based design of nonhallucinogenic psychedelic analogs

Targeting the EBP enabled identification of β-arrestin-biased ligands at 5-HT2AR. After analyzing available 5-HT2AR 4-fluorophenyl antipsychotics, three rigid moieties were identified for binding the EBP: IHCH-7113 (moiety from lumateperone), IHCH-7117 (from spiperone), and IHCH-7125 (from pimozide and benperidol). IHCH-7113 was a 5-HT2AR agonist (Ki = 758.58 nM) with weak preference for β-arrestin2 over Gq signaling (bias factor = 1.52). Further optimization yielded IHCH-7079 and IHCH-7086, which showed β-arrestin2 partial agonist activity without Gq dissociation activity. Unlike IHCH-7113 and hallucinogens, IHCH-7079 and IHCH-7086 failed to produce any head-twitch response (HTR) in mice, even at doses up to 10 mg/kg. The designed compounds also blocked [LSD](/xray-mp-wiki/reagents/lsd/)-induced HTR and showed antidepressant-like effects in both ARS-induced and corticosterone-induced depression models, comparable to [LSD](/xray-mp-wiki/reagents/lsd/) microdosing.

### Hallucinogenic effect is not required for antidepressant-like activity

Acute administration of [LSD](/xray-mp-wiki/reagents/lsd/) at low doses (0.0075-0.015 mg/kg ip) significantly attenuated acute restraint stress (ARS)-induced depression-like freezing behavior in both wild-type and 5-HT2AR Y370^7.43W mutant mice, without inducing HTR. These data suggest that the hallucinogenic effect may not be required for the antidepressant-like effect of [LSD](/xray-mp-wiki/reagents/lsd/), consistent with clinical trials of microdosing. The nonhallucinogenic analogs [lisuride](/xray-mp-wiki/reagents/lisuride/), IHCH-7079, and IHCH-7086 also showed antidepressant-like effects in both ARS and corticosterone-induced depression models, with effects blocked by the 5-HT2AR-selective antagonist MDL100907.


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/risperidone">Risperidone</a> — Co-crystallized antipsychotic in PDB 6A93
- <a href="/xray-mp-wiki/reagents/ligands/lsd">LSD (Lysergic Acid Diethylamide)</a> — Primary ligand studied in earlier work; extremely slow off-rate at 5-HT2A
- <a href="/xray-mp-wiki/proteins/gpcr/5ht2b-receptor/">Human 5-HT2B Receptor</a> — Related 5-HT2 family member; template for homology model
- <a href="/xray-mp-wiki/proteins/gpcr/5ht2c-receptor/">Human 5-HT2C Receptor</a> — Related 5-HT2 family member; most similar structure to 5-HT2A
- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr-inactive-conformation/">GPCR Inactive Conformation</a> — Risperidone and zotepine stabilize the inactive state of 5-HT2A
- <a href="/xray-mp-wiki/reagents/ligands/ergotamine">Ergotamine</a> — Related ergoline ligand compared in functional assays
- <a href="/xray-mp-wiki/reagents/protein-tags/bril">bRIL Fusion Protein</a> — mbIIG fusion (BRIL variant) used for crystallization
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">Lipidic Cubic Phase Crystallization</a> — Crystallization method used for both structures
- <a href="/xray-mp-wiki/concepts/construct-design/nonhallucinogenic-psychedelic-analog-design/">Nonhallucinogenic Psychedelic Analog Design</a> — Structure-based design strategy leveraging the EBP for biased agonism
- <a href="/xray-mp-wiki/concepts/signaling-receptors/lipid-activation-5ht2a-receptor/">Lipid Activation of 5-HT2A Receptor</a> — Monoolein and oleamide activate 5-HT2AR via the SEP pocket
- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr-active-conformation/">GPCR Active Conformation</a> — Active state GPCR conformation
