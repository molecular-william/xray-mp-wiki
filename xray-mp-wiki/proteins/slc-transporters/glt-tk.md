---
title: "GltTk (Glutamate Transporter Homologue from Thermococcus kodakarensis)"
created: 2026-06-10
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.7554##eLife.45286, doi/10.1038##ncomms13420]
verified: agent
uniprot_id: Q5JID0
---

# GltTk (Glutamate Transporter Homologue from Thermococcus kodakarensis)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q5JID0">UniProt: Q5JID0</a>

<span class="expr-badge">Thermococcus kodakarensis</span>

## Overview

[Glttk](/xray-mp-wiki/proteins/slc-transporters/glttk/) is a glutamate transporter homologue from the hyperthermophilic archaeon Thermococcus kodakarensis. It belongs to the SLC1 family of transporters (excitatory amino acid transporters, EAATs) and serves as a model system for studying the transport mechanism of mammalian glutamate transporters. [Glttk](/xray-mp-wiki/proteins/slc-transporters/glttk/) transports both L- and [D Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/) with identical Na+:substrate coupling stoichiometry (3:1). The crystal structure of GltTk with [D Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/) reveals how the enantiomeric substrate is accommodated with only minor rearrangements in the binding site.


## Publications

### doi/10.7554##eLife.45286

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6r7r">6R7R</a></td>
      <td>2.8</td>
      <td>P 32 2 1</td>
      <td>Full-length <a href="/xray-mp-wiki/proteins/slc-transporters/glttk/">Glttk</a> with C-terminal His8-tag</td>
      <td><a href="/xray-mp-wiki/reagents/substrates/l-aspartate/">D Aspartate</a>, 3 Na+ ions</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli MC1061
- **Construct**: Full-length [Glttk](/xray-mp-wiki/proteins/slc-transporters/glttk/) with C-terminal [His8-Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) in pBAD24
- **Notes**: Expression induced with L-arabinose
- **Induction**: L-arabinose

**Purification:**

- **Expression system**: Escherichia coli MC1061
- **Expression construct**: Full-length [Glttk](/xray-mp-wiki/proteins/slc-transporters/glttk/) with C-terminal His8-tag
- **Tag info**: C-terminal His8-tag

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
      <td>Cell harvest and membrane preparation</td>
      <td>Centrifugation</td>
      <td>—</td>
      <td></td>
      <td>Cells harvested and membranes prepared as described in Guskov et al., 2016</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td><a href="/xray-mp-wiki/methods/purification/detergent-solubilization/">Detergent Solubilization</a></td>
      <td>—</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> (<a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>(/xray-mp-wiki/reagents/detergents/dm/))</td>
      <td></td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td>IMAC</td>
      <td>—</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/300 GL</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> KOH, pH 8.0, 100 mM <a href="/xray-mp-wiki/reagents/additives/potassium-chloride/">KCl</a> + 0.15% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td></td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified apo [Glttk](/xray-mp-wiki/proteins/slc-transporters/glttk/) (no sodium ions present during purification)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor Diffusion</a>, hanging drop</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified apo <a href="/xray-mp-wiki/proteins/slc-transporters/glttk/">Glttk</a> in 10 mM Hepes KOH pH 8.0, 100 mM KCl, 0.15% DM, supplemented with 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 300 uM <a href="/xray-mp-wiki/reagents/substrates/l-aspartate/">D Aspartate</a> at 7 mg/ml</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 10% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 4000, 100 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a>/<a href="/xray-mp-wiki/reagents/buffers/bicine/">Bicine</a> pH 8.0, 60 mM CaCl2, 60 mM MgCl2, 0.75% OG</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>1:1 ratio of protein to reservoir</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>5 C</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>None (crystals flash-frozen directly)</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6r7r">6R7R</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGKSLLRRYLD</span><span class="topo-inside">YPVLW</span><span class="topo-membrane">KILWGLVLGAVFGLI</span><span class="topo-outside">AGHFGYAGAV</span><span class="topo-membrane">KTYIKPFGDLFVRLLKMLVMPIVL</span><span class="topo-inside">ASLVVGAASISPARLGRVG</span><span class="topo-membrane">VKIVVYYLATSAMAVFFGLIV</span><span class="topo-outside">GRLFNVGANVNLGSG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">TG</span><span class="topo-unknown">KAIE</span><span class="topo-outside">AQPPSL</span><span class="topo-membrane">VQTLLNIVPTNPFASLAKGEVLPVIFFAII</span><span class="topo-inside">LGIAITYLMNRNE</span><span class="topo-unknown">ERVRKSAETLLRVFDGLAEAMYLIVGGV</span><span class="topo-membrane">MQYAPIGVFALIAYVM</span><span class="topo-outside">AEQGVRVVGPLAKVVG</span><span class="topo-membrane">AVYTG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LFLQIVITYFILL</span><span class="topo-inside">KVFGID</span><span class="topo-unknown">PIKFIRKAKDAMITAFVTRSSSGTLPVTM</span><span class="topo-inside">RVAEEEMGVDKGIFSF</span><span class="topo-membrane">TLPLGATINMDGTALY</span><span class="topo-outside">QGVTVLFVANAIGHPLTLGQQLVVV</span><span class="topo-unknown">LTAVLASIGTAGVPG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430        </span>
<span class="topo-line"><span class="topo-unknown">AGAIMLAMVLQ</span><span class="topo-outside">SVGLDLTPGSPVALAYAMILGIDA</span><span class="topo-membrane">ILDMGRTMVNVTGDLAGT</span><span class="topo-inside">VIVAKTEKELDESKWISH</span><span class="topo-unknown">HHHHHHH</span></span>
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
      <td>12</td>
      <td>16</td>
      <td>12</td>
      <td>16</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>31</td>
      <td>17</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>41</td>
      <td>32</td>
      <td>41</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>65</td>
      <td>42</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>84</td>
      <td>66</td>
      <td>84</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>105</td>
      <td>85</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>122</td>
      <td>106</td>
      <td>122</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>132</td>
      <td>127</td>
      <td>132</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>162</td>
      <td>133</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>175</td>
      <td>163</td>
      <td>175</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>203</td>
      <td>176</td>
      <td>203</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>204</td>
      <td>219</td>
      <td>204</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>235</td>
      <td>220</td>
      <td>235</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>253</td>
      <td>236</td>
      <td>253</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>254</td>
      <td>259</td>
      <td>254</td>
      <td>259</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>260</td>
      <td>267</td>
      <td>260</td>
      <td>267</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>268</td>
      <td>288</td>
      <td>268</td>
      <td>288</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>289</td>
      <td>304</td>
      <td>289</td>
      <td>304</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>305</td>
      <td>320</td>
      <td>305</td>
      <td>320</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>321</td>
      <td>345</td>
      <td>321</td>
      <td>345</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>346</td>
      <td>362</td>
      <td>346</td>
      <td>362</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>363</td>
      <td>371</td>
      <td>363</td>
      <td>371</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>372</td>
      <td>395</td>
      <td>372</td>
      <td>395</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>396</td>
      <td>413</td>
      <td>396</td>
      <td>413</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>414</td>
      <td>431</td>
      <td>414</td>
      <td>431</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6r7r">6R7R</a> — Chain B (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGKSLLRRYLDYPVLW</span><span class="topo-inside">K</span><span class="topo-membrane">ILWGLVLGAVFGLI</span><span class="topo-outside">AGHFGYAGAVKT</span><span class="topo-membrane">YIKPFGDLFVRLLKMLVMPIVL</span><span class="topo-inside">ASLVVGAASISPARLGRVG</span><span class="topo-membrane">VKIVVYYLATSAMAVFFGLIV</span><span class="topo-outside">GRLFNVGANVNLGSG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">TG</span><span class="topo-unknown">KAIEAQPP</span><span class="topo-outside">SL</span><span class="topo-membrane">VQTLLNIVPTNPFASLAKGEVLPVIFFA</span><span class="topo-inside">IILGIAITYLMNRNE</span><span class="topo-unknown">ERVRKSAETLLRVFDGLAEAMYLIVGGV</span><span class="topo-membrane">MQYAPIGVFALIAYVM</span><span class="topo-outside">AEQGVRVVGPLAKVVG</span><span class="topo-membrane">AVYTG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LFLQIVITYFILL</span><span class="topo-inside">KVFGID</span><span class="topo-unknown">PIKFIRKAKDAMITAFVTRSSSGTLPVTM</span><span class="topo-inside">RVAEEEMGVDKGIFSF</span><span class="topo-membrane">TLPLGATINMDGTALY</span><span class="topo-outside">QGVTVLFVANAIGHPLTLGQQLVVV</span><span class="topo-unknown">LTAVLASIGTAGVPG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430        </span>
<span class="topo-line"><span class="topo-unknown">AGAIMLAMVLQS</span><span class="topo-outside">VGLDLTPGSPVALAYAMILGIDA</span><span class="topo-membrane">ILDMGRTMVNVTGDLAGT</span><span class="topo-inside">VIVAKTEKELDESKWIS</span><span class="topo-unknown">HHHHHHHH</span></span>
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
      <td>17</td>
      <td>17</td>
      <td>17</td>
      <td>17</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>31</td>
      <td>18</td>
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
      <td>65</td>
      <td>44</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>84</td>
      <td>66</td>
      <td>84</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>105</td>
      <td>85</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>122</td>
      <td>106</td>
      <td>122</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>131</td>
      <td>132</td>
      <td>131</td>
      <td>132</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>160</td>
      <td>133</td>
      <td>160</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>175</td>
      <td>161</td>
      <td>175</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>203</td>
      <td>176</td>
      <td>203</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>204</td>
      <td>219</td>
      <td>204</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>235</td>
      <td>220</td>
      <td>235</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>253</td>
      <td>236</td>
      <td>253</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>254</td>
      <td>259</td>
      <td>254</td>
      <td>259</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>260</td>
      <td>267</td>
      <td>260</td>
      <td>267</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>268</td>
      <td>288</td>
      <td>268</td>
      <td>288</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>289</td>
      <td>304</td>
      <td>289</td>
      <td>304</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>305</td>
      <td>320</td>
      <td>305</td>
      <td>320</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>321</td>
      <td>345</td>
      <td>321</td>
      <td>345</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>346</td>
      <td>362</td>
      <td>346</td>
      <td>362</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>363</td>
      <td>372</td>
      <td>363</td>
      <td>372</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>373</td>
      <td>395</td>
      <td>373</td>
      <td>395</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>396</td>
      <td>413</td>
      <td>396</td>
      <td>413</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>414</td>
      <td>430</td>
      <td>414</td>
      <td>430</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6r7r">6R7R</a> — Chain C (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MG</span><span class="topo-inside">KSLLRRYLDYPVL</span><span class="topo-membrane">WKILWGLVLGAVFGLI</span><span class="topo-outside">AGHFGYAGAVKT</span><span class="topo-membrane">YIKPFGDLFVRLLKMLVMPIVL</span><span class="topo-inside">ASLVVGAASISPARLGRVG</span><span class="topo-membrane">VKIVVYYLATSAMAVFFGLIV</span><span class="topo-outside">GRLFNVGANVNLGSG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">TG</span><span class="topo-unknown">KAIEAQ</span><span class="topo-outside">PPSL</span><span class="topo-membrane">VQTLLNIVPTNPFASLAKGEVLPVIFFAII</span><span class="topo-inside">LGIAITYLMNRNE</span><span class="topo-unknown">ERVRKSAETLLRVFDGLAEAMYLIVGGV</span><span class="topo-membrane">MQYAPIGVFALIAYVM</span><span class="topo-outside">AEQGVRVVGPLAKVVG</span><span class="topo-membrane">AVYTG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LFLQIVITYFILL</span><span class="topo-inside">KVFGID</span><span class="topo-unknown">PIKFIRKAKDAMITAFVTRSSSGTLPVTM</span><span class="topo-inside">RVAEEEMGVDKGIFSF</span><span class="topo-membrane">TLPLGATINMDGTALYQG</span><span class="topo-outside">VTVLFVANAIGHPLTLGQQLVVV</span><span class="topo-unknown">LTAVLASIGTAGVPG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430        </span>
<span class="topo-line"><span class="topo-unknown">AGAIMLAMVLQ</span><span class="topo-outside">SVGLDLTPGSPVALAYAMILGIDA</span><span class="topo-membrane">ILDMGRTMVNVTGDLAGT</span><span class="topo-inside">VIVAKTEKELDESKWIS</span><span class="topo-unknown">HHHHHHHH</span></span>
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
      <td>3</td>
      <td>15</td>
      <td>3</td>
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
      <td>65</td>
      <td>44</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>84</td>
      <td>66</td>
      <td>84</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>105</td>
      <td>85</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>122</td>
      <td>106</td>
      <td>122</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>132</td>
      <td>129</td>
      <td>132</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>162</td>
      <td>133</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>175</td>
      <td>163</td>
      <td>175</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>203</td>
      <td>176</td>
      <td>203</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>204</td>
      <td>219</td>
      <td>204</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>235</td>
      <td>220</td>
      <td>235</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>253</td>
      <td>236</td>
      <td>253</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>254</td>
      <td>259</td>
      <td>254</td>
      <td>259</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>260</td>
      <td>267</td>
      <td>260</td>
      <td>267</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>268</td>
      <td>288</td>
      <td>268</td>
      <td>288</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>289</td>
      <td>304</td>
      <td>289</td>
      <td>304</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>305</td>
      <td>322</td>
      <td>305</td>
      <td>322</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>323</td>
      <td>345</td>
      <td>323</td>
      <td>345</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>346</td>
      <td>362</td>
      <td>346</td>
      <td>362</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>363</td>
      <td>371</td>
      <td>363</td>
      <td>371</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>372</td>
      <td>395</td>
      <td>372</td>
      <td>395</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>396</td>
      <td>413</td>
      <td>396</td>
      <td>413</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>414</td>
      <td>430</td>
      <td>414</td>
      <td>430</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##ncomms13420

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5e9s">5E9S</a></td>
      <td>2.7</td>
      <td>—</td>
      <td>Full-length <a href="/xray-mp-wiki/proteins/slc-transporters/glttk/">Glttk</a> with C-terminal His8-tag</td>
      <td><a href="/xray-mp-wiki/reagents/substrates/l-aspartate/">L Aspartate</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli MC1061
- **Construct**: Full-length [Glttk](/xray-mp-wiki/proteins/slc-transporters/glttk/) with C-terminal [His8-Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) in pBAD24
- **Notes**: Expression induced with L-arabinose
- **Induction**: L-arabinose

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5e9s">5E9S</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGKS</span><span class="topo-outside">L</span><span class="topo-unknown">LRRYLD</span><span class="topo-outside">YPVLWKI</span><span class="topo-membrane">LWGLVLGAVFGLIAG</span><span class="topo-inside">HFGY</span><span class="topo-membrane">AGAVKTYIKPFGDLFVRLLKMLVM</span><span class="topo-outside">PIVLASLVVGAASISPARLGRVGVKIV</span><span class="topo-membrane">VYYLATSAMAVFFGLIVGRLF</span><span class="topo-inside">NVGANVNLGSG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">TGKAIEAQPP</span><span class="topo-membrane">SLVQTLLNIVPTNP</span><span class="topo-outside">FASLAKGEVLPVIFFAIILGIAITYLMNRNEERVRKSAETLLRVFDGLAEAMYLIVGGVMQY</span><span class="topo-membrane">APIGVFALIAYVMAEQG</span><span class="topo-inside">VRVVGPLA</span><span class="topo-membrane">KVVGAVYTG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LFLQIVITY</span><span class="topo-outside">FILLKVFGID</span><span class="topo-unknown">PIKFIRKA</span><span class="topo-outside">KDA</span><span class="topo-unknown">MITAFVTRSSSGTL</span><span class="topo-outside">PVTMRVAEEEMGVDKGIFSFTLP</span><span class="topo-membrane">LGATINMDGTALYQGVT</span><span class="topo-inside">VLFVANAIGHPLTLGQQ</span><span class="topo-unknown">LVVVLTAVLASIGTAGVPG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430        </span>
<span class="topo-line"><span class="topo-unknown">AGAIMLA</span><span class="topo-inside">MVLQSVGLDLTPGSPVALAYAMILGI</span><span class="topo-membrane">DAILDMGRTMVNVTGD</span><span class="topo-outside">LAGTVIVAKTEKELDESKWISH</span><span class="topo-unknown">HHHHHHH</span></span>
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
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>11</td>
      <td>6</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>18</td>
      <td>12</td>
      <td>18</td>
      <td>Outside</td>
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
      <td>37</td>
      <td>34</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>61</td>
      <td>38</td>
      <td>61</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>88</td>
      <td>62</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>109</td>
      <td>89</td>
      <td>109</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>130</td>
      <td>110</td>
      <td>130</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>131</td>
      <td>144</td>
      <td>131</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>206</td>
      <td>145</td>
      <td>206</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>223</td>
      <td>207</td>
      <td>223</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>231</td>
      <td>224</td>
      <td>231</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>232</td>
      <td>249</td>
      <td>232</td>
      <td>249</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>250</td>
      <td>259</td>
      <td>250</td>
      <td>259</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>260</td>
      <td>267</td>
      <td>260</td>
      <td>267</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>268</td>
      <td>270</td>
      <td>268</td>
      <td>270</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>271</td>
      <td>284</td>
      <td>271</td>
      <td>284</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>285</td>
      <td>307</td>
      <td>285</td>
      <td>307</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>308</td>
      <td>324</td>
      <td>308</td>
      <td>324</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>325</td>
      <td>341</td>
      <td>325</td>
      <td>341</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>342</td>
      <td>367</td>
      <td>342</td>
      <td>367</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>368</td>
      <td>393</td>
      <td>368</td>
      <td>393</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>394</td>
      <td>409</td>
      <td>394</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>431</td>
      <td>410</td>
      <td>431</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5e9s">5E9S</a> — Chain B (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGKS</span><span class="topo-outside">LLRRYLDYPVLWKI</span><span class="topo-membrane">LWGLVLGAVFGLIAG</span><span class="topo-inside">HFGY</span><span class="topo-membrane">AGAVKTYIKPFGDLFVRLLKMLVM</span><span class="topo-outside">PIVLASLVVGAASISPARLGRVGVKIV</span><span class="topo-membrane">VYYLATSAMAVFFGLIVGRLF</span><span class="topo-inside">NVGANVNLGSG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">TGKAIEAQPP</span><span class="topo-membrane">SLVQTLLNIVPTNPF</span><span class="topo-outside">ASLAKGEVLPVIFFAIILGIAITYLMNRNEERVRKSAETLLRVFDGLAEAMYLIVGGVMQY</span><span class="topo-membrane">APIGVFALIAYVMAEQG</span><span class="topo-inside">VRVVGPLA</span><span class="topo-membrane">KVVGAVYTG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LFLQIVITY</span><span class="topo-outside">FILLKVFGID</span><span class="topo-unknown">PIKFIRKA</span><span class="topo-outside">KDA</span><span class="topo-unknown">MITAFVTRSSSGTL</span><span class="topo-outside">PVTMRVAEEEMGVDKGIFSFTL</span><span class="topo-membrane">PLGATINMDGTALYQGVT</span><span class="topo-inside">VLFVANAIGHPLTLGQQ</span><span class="topo-unknown">LVVVLTAVLASIGTAGVPG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430        </span>
<span class="topo-line"><span class="topo-unknown">AGAIMLA</span><span class="topo-inside">MVLQSVGLDLTPGSPVALAYAMILGI</span><span class="topo-membrane">DAILDMGRTMVNVTGD</span><span class="topo-outside">LAGTVIVAKTEKELDESKWISH</span><span class="topo-unknown">HHHHHHH</span></span>
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
      <td>5</td>
      <td>18</td>
      <td>5</td>
      <td>18</td>
      <td>Outside</td>
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
      <td>37</td>
      <td>34</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>61</td>
      <td>38</td>
      <td>61</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>88</td>
      <td>62</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>109</td>
      <td>89</td>
      <td>109</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>130</td>
      <td>110</td>
      <td>130</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>131</td>
      <td>145</td>
      <td>131</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>206</td>
      <td>146</td>
      <td>206</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>223</td>
      <td>207</td>
      <td>223</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>231</td>
      <td>224</td>
      <td>231</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>232</td>
      <td>249</td>
      <td>232</td>
      <td>249</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>250</td>
      <td>259</td>
      <td>250</td>
      <td>259</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>260</td>
      <td>267</td>
      <td>260</td>
      <td>267</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>268</td>
      <td>270</td>
      <td>268</td>
      <td>270</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>271</td>
      <td>284</td>
      <td>271</td>
      <td>284</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>285</td>
      <td>306</td>
      <td>285</td>
      <td>306</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>307</td>
      <td>324</td>
      <td>307</td>
      <td>324</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>325</td>
      <td>341</td>
      <td>325</td>
      <td>341</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>342</td>
      <td>367</td>
      <td>342</td>
      <td>367</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>368</td>
      <td>393</td>
      <td>368</td>
      <td>393</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>394</td>
      <td>409</td>
      <td>394</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>431</td>
      <td>410</td>
      <td>431</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5e9s">5E9S</a> — Chain C (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGKS</span><span class="topo-outside">LLRRYLDYPVLWKI</span><span class="topo-membrane">LWGLVLGAVFGLIAG</span><span class="topo-inside">HFGY</span><span class="topo-membrane">AGAVKTYIKPFGDLFVRLLKMLVM</span><span class="topo-outside">PIVLASLVVGAASISPARLGRVGVKIV</span><span class="topo-membrane">VYYLATSAMAVFFGLIVGRLF</span><span class="topo-inside">NVGANVNLGSG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">TGKAIEAQPP</span><span class="topo-membrane">SLVQTLLNIVPTNP</span><span class="topo-outside">FASLAKGEVLPVIFFAIILGIAITYLMNRNEERVRKSAETLLRVFDGLAEAMYLIVGGVMQY</span><span class="topo-membrane">APIGVFALIAYVMAEQG</span><span class="topo-inside">VRVVGPLA</span><span class="topo-membrane">KVVGAVYTG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LFLQIVITY</span><span class="topo-outside">FILLKVFGID</span><span class="topo-unknown">PIKFIRKA</span><span class="topo-outside">KDA</span><span class="topo-unknown">MITAFVTRSSSGTL</span><span class="topo-outside">PVTMRVAEEEMGVDKGIFSFTLP</span><span class="topo-membrane">LGATINMDGTALYQGVT</span><span class="topo-inside">VLFVANAIGHPLTLGQQ</span><span class="topo-unknown">LVVVLTAVLASIGTAGVPG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430        </span>
<span class="topo-line"><span class="topo-unknown">AGAIMLAMVL</span><span class="topo-inside">QSVGLDLTPGSPVALAYAMILGI</span><span class="topo-membrane">DAILDMGRTMVNVTGD</span><span class="topo-outside">LAGTVIVAKTEKELDESKWIS</span><span class="topo-unknown">HHHHHHHH</span></span>
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
      <td>5</td>
      <td>18</td>
      <td>5</td>
      <td>18</td>
      <td>Outside</td>
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
      <td>37</td>
      <td>34</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>61</td>
      <td>38</td>
      <td>61</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>88</td>
      <td>62</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>109</td>
      <td>89</td>
      <td>109</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>130</td>
      <td>110</td>
      <td>130</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>131</td>
      <td>144</td>
      <td>131</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>206</td>
      <td>145</td>
      <td>206</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>223</td>
      <td>207</td>
      <td>223</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>231</td>
      <td>224</td>
      <td>231</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>232</td>
      <td>249</td>
      <td>232</td>
      <td>249</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>250</td>
      <td>259</td>
      <td>250</td>
      <td>259</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>260</td>
      <td>267</td>
      <td>260</td>
      <td>267</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>268</td>
      <td>270</td>
      <td>268</td>
      <td>270</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>271</td>
      <td>284</td>
      <td>271</td>
      <td>284</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>285</td>
      <td>307</td>
      <td>285</td>
      <td>307</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>308</td>
      <td>324</td>
      <td>308</td>
      <td>324</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>325</td>
      <td>341</td>
      <td>325</td>
      <td>341</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>342</td>
      <td>367</td>
      <td>342</td>
      <td>367</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>368</td>
      <td>360</td>
      <td>368</td>
      <td>360</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>361</td>
      <td>370</td>
      <td>361</td>
      <td>370</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>371</td>
      <td>393</td>
      <td>371</td>
      <td>393</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>394</td>
      <td>409</td>
      <td>394</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>430</td>
      <td>410</td>
      <td>430</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### D-aspartate transport by GltTk

[Glttk](/xray-mp-wiki/proteins/slc-transporters/glttk/) transports [D Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/) with the same 3:1 Na+:substrate coupling
stoichiometry as [L Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/). The Km for D-aspartate transport is
1.1 uM, comparable to 0.75 uM for [L Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/). The Kd for D-aspartate
binding at high sodium (500 mM) is 374 nM, compared to 62 nM for
[L Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/), indicating slightly lower affinity for the D-enantiomer.

### Structural accommodation of D-aspartate

The crystal structure at 2.8 A shows [D Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/) bound in the
outward-facing occluded state with highly similar binding mode to
[L Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/). Despite the mirrored spatial arrangement of functional
groups around the chiral Calpha atom, D- and [L Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/) form nearly
identical hydrogen bonding networks with conserved residues in the
binding site. Only minor changes in the positions of Calpha and Cbeta
carboxyl groups distinguish the two binding modes.

### Three sodium ion binding sites

Three peaks of electron density at positions matching the three sodium
ions in the [L Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/) complex confirm 3:1 Na+:D-aspartate coupling
stoichiometry. None of the sodium sites are directly coordinated by
substrate, consistent with the identical coupling stoichiometry for
both enantiomers.

### First transporter with enantiomeric substrate structures

[Glttk](/xray-mp-wiki/proteins/slc-transporters/glttk/) is the first amino acid transporter for which structures of both
enantiomeric substrates (L- and [D Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/)) have been determined,
providing insight into how transporters can accommodate stereoisomers.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/glutamate-transporter-family/">Glutamate Transporter Family (SLC1/EAAT)</a> — GltTk is an archaeal homologue of mammalian EAATs
- <a href="/xray-mp-wiki/proteins/slc-transporters/eaat1/">Human Excitatory Amino Acid Transporter 1 (EAAT1)</a> — Mammalian EAAT1 is a structural and functional homolog of GltTk
- <a href="/xray-mp-wiki/proteins/slc-transporters/glttk/">Glttk</a> — Referenced in glt-tk text
- <a href="/xray-mp-wiki/reagents/substrates/l-aspartate/">D Aspartate</a> — Referenced in glt-tk text
- <a href="/xray-mp-wiki/reagents/substrates/l-aspartate/">L Aspartate</a> — Referenced in glt-tk text
- <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> — Referenced in glt-tk text
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> — Referenced in glt-tk text
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Referenced in glt-tk text
- <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a> — Referenced in glt-tk text
