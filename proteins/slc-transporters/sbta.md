---
title: "SbtA (High-Affinity Sodium-Dependent Bicarbonate Transporter, Synechocystis sp. PCC 6803)"
created: 2026-06-11
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, transporter, xray-crystallography]
sources: [doi/10.1073##pnas.2101632118]
verified: false
---

# SbtA (High-Affinity Sodium-Dependent Bicarbonate Transporter, Synechocystis sp. PCC 6803)

## Overview

SbtA is a high-affinity, sodium-dependent bicarbonate (HCO3-) transporter found in the cyanobacterial CO2-concentrating mechanism ([CCM](/xray-mp-wiki/concepts/miscellaneous/co2-concentrating-mechanism/)). It forms a homotrimer in the membrane, with each protomer comprising 10 transmembrane helices organized into a scaffold domain (TMs 1-2, 6-7) and a core domain (TMs 3-5, 8-10). The core domain contains the HCO3-/Na+ binding site formed by a TM cross (TM4a/b and TM9a/b). SbtA uses an [Elevator Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/elevator-mechanism/) for bicarbonate transport, where the core domain undergoes rigid-body movement to translocate HCO3- across the membrane. SbtA is allosterically inhibited by [SBTB](/xray-mp-wiki/proteins/slc-transporters/sbtb/), a PII-like regulatory protein, which binds to the cytoplasmic surface and locks SbtA in an inward-facing state.


## Publications

### doi/10.1073##pnas.2101632118

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7egl">7EGL</a></td>
      <td>2.7</td>
      <td>Not applicable (cryo-EM)</td>
      <td>Full-length SbtA (Synechocystis sp. PCC 6803) with C-terminal His-tag, co-expressed with <a href="/xray-mp-wiki/proteins/slc-transporters/sbtb/">SBTB</a></td>
      <td>HCO3-, Na+, AMP</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7egl">7EGL</a></td>
      <td>3.2</td>
      <td>(not specified)</td>
      <td>Full-length SbtA (Synechocystis sp. PCC 6803) with C-terminal His-tag, co-expressed with <a href="/xray-mp-wiki/proteins/slc-transporters/sbtb/">SBTB</a></td>
      <td>HCO3-, Na+</td>
    </tr>
  </tbody>
</table>

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
      <td>Cell culture and expression</td>
      <td>E. coli C43(DE3) heterologous expression</td>
      <td>—</td>
      <td>LB medium with 50 ug/mL <a href="/xray-mp-wiki/reagents/additives/kanamycin/">Kanamycin</a></td>
      <td>Co-expression of SbtA (C-terminal His-tag) and <a href="/xray-mp-wiki/proteins/slc-transporters/sbtb/">SBTB</a> from pRSFDuet plasmid; induced with 0.25 mM <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> at OD600=1.2; 14 h growth at 37C</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>French press and ultracentrifugation</td>
      <td>—</td>
      <td>100 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 2 mM AMP</td>
      <td>Cells homogenized by French press; membrane fraction collected at 150,000 x g for 1 h</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>100 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 2 mM AMP + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (n-dodecyl-beta-D-maltopyranoside)</td>
      <td>Solubilized for 2 h at 4C; insoluble material removed at 20,000 x g for 45 min</td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni2+-NTA agarose (Qiagen)</td>
      <td>Wash: 100 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 0.018% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 2 mM AMP, 25 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>; Elution: same buffer with 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 0.018% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td>SEC (<a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a>)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>100 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 0.18% DM, 2 mM AMP + 0.18% DM (<a href="/xray-mp-wiki/reagents/detergents/dm/">n-Decyl-β-D-maltoside</a>)</td>
      <td>Peak fractions concentrated to ~5 mg/mL for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (not explicitly specified)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified SbtA-<a href="/xray-mp-wiki/proteins/slc-transporters/sbtb/">SBTB</a> complex at ~5 mg/mL in 0.18% DM</td>
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
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystal structure solved at 3.2 A by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using the <a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a> map as template</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7egl">7EGL</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">DF</span><span class="topo-unknown">LSNFLTDFVGQ</span><span class="topo-outside">LQSP</span><span class="topo-membrane">TLAFLIGGMVIAALGT</span><span class="topo-inside">Q</span><span class="topo-membrane">LVIPEAISTIIVFMLLTKIGL</span><span class="topo-outside">TGGMAIRNSNLTEML</span><span class="topo-membrane">LPVAFSVILGILIVFIARFTLA</span><span class="topo-inside">KLPNVRTVDA</span><span class="topo-membrane">LATGGLFGAVSGSTMAA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">A</span><span class="topo-outside">LTTLEESKISYEAWA</span><span class="topo-membrane">GALYPFMDIPALVTAIVV</span><span class="topo-inside">ANIYLNKRKRKSAAA</span><span class="topo-unknown">SIEESFSKQPVAAGDYGDQTDYPRTRQEYLSQQEPEDN</span><span class="topo-inside">RVKI</span><span class="topo-membrane">WPIIEESLQGPALSAMLLGLAL</span><span class="topo-outside">GIFTKP</span><span class="topo-unknown">E</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">SVYEG</span><span class="topo-outside">FYDPL</span><span class="topo-membrane">FRGLLSILMLIMGMEAWSRIG</span><span class="topo-inside">ELRKVAQ</span><span class="topo-membrane">WYVVYSLIAPIVHGFIAFGLG</span><span class="topo-outside">MIAHYATGFSLGGVVV</span><span class="topo-membrane">LAVIAASSSDISGPPTL</span><span class="topo-inside">RAGIPSANPSAY</span><span class="topo-membrane">IGSSTAIGTPIAIGVC</span></span>
<span class="topo-ruler">       370    </span>
<span class="topo-line"><span class="topo-membrane">IPL</span><span class="topo-outside">FIGLAQTLGAG</span></span>
<details class="topo-details"><summary>Topology coordinates (26 regions)</summary>
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
      <td>2</td>
      <td>3</td>
      <td>2</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>14</td>
      <td>4</td>
      <td>14</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>18</td>
      <td>15</td>
      <td>18</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>34</td>
      <td>19</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>35</td>
      <td>35</td>
      <td>35</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>56</td>
      <td>36</td>
      <td>56</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>71</td>
      <td>57</td>
      <td>71</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>93</td>
      <td>72</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>103</td>
      <td>94</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>121</td>
      <td>104</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>122</td>
      <td>136</td>
      <td>122</td>
      <td>136</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>154</td>
      <td>137</td>
      <td>154</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>169</td>
      <td>155</td>
      <td>169</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>211</td>
      <td>208</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>233</td>
      <td>212</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>239</td>
      <td>234</td>
      <td>239</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>245</td>
      <td>240</td>
      <td>245</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>246</td>
      <td>250</td>
      <td>246</td>
      <td>250</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>271</td>
      <td>251</td>
      <td>271</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>278</td>
      <td>272</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>299</td>
      <td>279</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>315</td>
      <td>300</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>332</td>
      <td>316</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>344</td>
      <td>333</td>
      <td>344</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>363</td>
      <td>345</td>
      <td>363</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>374</td>
      <td>364</td>
      <td>374</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7egl">7EGL</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">AKPANKLVIVTEKILLKKIAKIIDESGAKGYTVMNTGGKG</span><span class="topo-unknown">SRNVRSSGQPNTSDIE</span><span class="topo-inside">ANIKFEILTETREMAEEIADRVAVKYFNDYAGIIYICSAEVLYGHTFCGPEGC</span></span>
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
      <td>2</td>
      <td>41</td>
      <td>2</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>110</td>
      <td>58</td>
      <td>110</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7egl">7EGL</a> — Chain C (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">DF</span><span class="topo-unknown">LSNFLTDFVGQ</span><span class="topo-outside">LQSP</span><span class="topo-membrane">TLAFLIGGMVIAALGT</span><span class="topo-inside">Q</span><span class="topo-membrane">LVIPEAISTIIVFMLLTKIGL</span><span class="topo-outside">TGGMAIRNSNLTEML</span><span class="topo-membrane">LPVAFSVILGILIVFIARFTLA</span><span class="topo-inside">KLPNVRTVDA</span><span class="topo-membrane">LATGGLFGAVSGSTMAA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">A</span><span class="topo-outside">LTTLEESKISYEAWA</span><span class="topo-membrane">GALYPFMDIPALVTAIVV</span><span class="topo-inside">ANIYLNKRKRKSAAA</span><span class="topo-unknown">SIEESFSKQPVAAGDYGDQTDYPRTRQEYLSQQEPEDN</span><span class="topo-inside">RVKI</span><span class="topo-membrane">WPIIEESLQGPALSAMLLGLAL</span><span class="topo-outside">GIFTKP</span><span class="topo-unknown">E</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">SVYEG</span><span class="topo-outside">FYDPL</span><span class="topo-membrane">FRGLLSILMLIMGMEAWSRIG</span><span class="topo-inside">ELRKVAQ</span><span class="topo-membrane">WYVVYSLIAPIVHGFIAFGLG</span><span class="topo-outside">MIAHYATGFSLGGVVV</span><span class="topo-membrane">LAVIAASSSDISGPPTL</span><span class="topo-inside">RAGIPSANPSAY</span><span class="topo-membrane">IGSSTAIGTPIAIGVC</span></span>
<span class="topo-ruler">       370    </span>
<span class="topo-line"><span class="topo-membrane">IPL</span><span class="topo-outside">FIGLAQTLGAG</span></span>
<details class="topo-details"><summary>Topology coordinates (26 regions)</summary>
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
      <td>2</td>
      <td>3</td>
      <td>2</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>14</td>
      <td>4</td>
      <td>14</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>18</td>
      <td>15</td>
      <td>18</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>34</td>
      <td>19</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>35</td>
      <td>35</td>
      <td>35</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>56</td>
      <td>36</td>
      <td>56</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>71</td>
      <td>57</td>
      <td>71</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>93</td>
      <td>72</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>103</td>
      <td>94</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>121</td>
      <td>104</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>122</td>
      <td>136</td>
      <td>122</td>
      <td>136</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>154</td>
      <td>137</td>
      <td>154</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>169</td>
      <td>155</td>
      <td>169</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>211</td>
      <td>208</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>233</td>
      <td>212</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>239</td>
      <td>234</td>
      <td>239</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>245</td>
      <td>240</td>
      <td>245</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>246</td>
      <td>250</td>
      <td>246</td>
      <td>250</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>271</td>
      <td>251</td>
      <td>271</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>278</td>
      <td>272</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>299</td>
      <td>279</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>315</td>
      <td>300</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>332</td>
      <td>316</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>344</td>
      <td>333</td>
      <td>344</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>363</td>
      <td>345</td>
      <td>363</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>374</td>
      <td>364</td>
      <td>374</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7egl">7EGL</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">AKPANKLVIVTEKILLKKIAKIIDESGAKGYTVMNTGGKG</span><span class="topo-unknown">SRNVRSSGQPNTSDIE</span><span class="topo-inside">ANIKFEILTETREMAEEIADRVAVKYFNDYAGIIYICSAEVLYGHTFCGPEGC</span></span>
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
      <td>2</td>
      <td>41</td>
      <td>2</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>110</td>
      <td>58</td>
      <td>110</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7egl">7EGL</a> — Chain E (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">DF</span><span class="topo-unknown">LSNFLTDFVGQ</span><span class="topo-outside">LQSP</span><span class="topo-membrane">TLAFLIGGMVIAALGT</span><span class="topo-inside">Q</span><span class="topo-membrane">LVIPEAISTIIVFMLLTKIGL</span><span class="topo-outside">TGGMAIRNSNLTEML</span><span class="topo-membrane">LPVAFSVILGILIVFIARFTLA</span><span class="topo-inside">KLPNVRTVDA</span><span class="topo-membrane">LATGGLFGAVSGSTMAA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">A</span><span class="topo-outside">LTTLEESKISYEAWA</span><span class="topo-membrane">GALYPFMDIPALVTAIVV</span><span class="topo-inside">ANIYLNKRKRKSAAA</span><span class="topo-unknown">SIEESFSKQPVAAGDYGDQTDYPRTRQEYLSQQEPEDN</span><span class="topo-inside">RVKI</span><span class="topo-membrane">WPIIEESLQGPALSAMLLGLAL</span><span class="topo-outside">GIFTKP</span><span class="topo-unknown">E</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">SVYEG</span><span class="topo-outside">FYDPL</span><span class="topo-membrane">FRGLLSILMLIMGMEAWSRIG</span><span class="topo-inside">ELRKVAQ</span><span class="topo-membrane">WYVVYSLIAPIVHGFIAFGLG</span><span class="topo-outside">MIAHYATGFSLGGVVV</span><span class="topo-membrane">LAVIAASSSDISGPPTL</span><span class="topo-inside">RAGIPSANPSAY</span><span class="topo-membrane">IGSSTAIGTPIAIGVC</span></span>
<span class="topo-ruler">       370    </span>
<span class="topo-line"><span class="topo-membrane">IPL</span><span class="topo-outside">FIGLAQTLGAG</span></span>
<details class="topo-details"><summary>Topology coordinates (26 regions)</summary>
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
      <td>2</td>
      <td>3</td>
      <td>2</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>14</td>
      <td>4</td>
      <td>14</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>18</td>
      <td>15</td>
      <td>18</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>34</td>
      <td>19</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>35</td>
      <td>35</td>
      <td>35</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>56</td>
      <td>36</td>
      <td>56</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>71</td>
      <td>57</td>
      <td>71</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>93</td>
      <td>72</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>103</td>
      <td>94</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>121</td>
      <td>104</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>122</td>
      <td>136</td>
      <td>122</td>
      <td>136</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>154</td>
      <td>137</td>
      <td>154</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>169</td>
      <td>155</td>
      <td>169</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>211</td>
      <td>208</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>233</td>
      <td>212</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>239</td>
      <td>234</td>
      <td>239</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>245</td>
      <td>240</td>
      <td>245</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>246</td>
      <td>250</td>
      <td>246</td>
      <td>250</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>271</td>
      <td>251</td>
      <td>271</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>278</td>
      <td>272</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>299</td>
      <td>279</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>315</td>
      <td>300</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>332</td>
      <td>316</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>344</td>
      <td>333</td>
      <td>344</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>363</td>
      <td>345</td>
      <td>363</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>374</td>
      <td>364</td>
      <td>374</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7egl">7EGL</a> — Chain F (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">AKPANKLVIVTEKILLKKIAKIIDESGAKGYTVMNTGGKG</span><span class="topo-unknown">SRNVRSSGQPNTSDIE</span><span class="topo-inside">ANIKFEILTETREMAEEIADRVAVKYFNDYAGIIYICSAEVLYGHTFCGPEGC</span></span>
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
      <td>2</td>
      <td>41</td>
      <td>2</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>110</td>
      <td>58</td>
      <td>110</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7egl">7EGL</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">DF</span><span class="topo-unknown">LSNFLTDFVGQ</span><span class="topo-outside">LQSP</span><span class="topo-membrane">TLAFLIGGMVIAALGT</span><span class="topo-inside">Q</span><span class="topo-membrane">LVIPEAISTIIVFMLLTKIGL</span><span class="topo-outside">TGGMAIRNSNLTEML</span><span class="topo-membrane">LPVAFSVILGILIVFIARFTLA</span><span class="topo-inside">KLPNVRTVDA</span><span class="topo-membrane">LATGGLFGAVSGSTMAA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">A</span><span class="topo-outside">LTTLEESKISYEAWA</span><span class="topo-membrane">GALYPFMDIPALVTAIVV</span><span class="topo-inside">ANIYLNKRKRKSAAA</span><span class="topo-unknown">SIEESFSKQPVAAGDYGDQTDYPRTRQEYLSQQEPEDN</span><span class="topo-inside">RVKI</span><span class="topo-membrane">WPIIEESLQGPALSAMLLGLAL</span><span class="topo-outside">GIFTKP</span><span class="topo-unknown">E</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">SVYEG</span><span class="topo-outside">FYDPL</span><span class="topo-membrane">FRGLLSILMLIMGMEAWSRIG</span><span class="topo-inside">ELRKVAQ</span><span class="topo-membrane">WYVVYSLIAPIVHGFIAFGLG</span><span class="topo-outside">MIAHYATGFSLGGVVV</span><span class="topo-membrane">LAVIAASSSDISGPPTL</span><span class="topo-inside">RAGIPSANPSAY</span><span class="topo-membrane">IGSSTAIGTPIAIGVC</span></span>
<span class="topo-ruler">       370    </span>
<span class="topo-line"><span class="topo-membrane">IPL</span><span class="topo-outside">FIGLAQTLGAG</span></span>
<details class="topo-details"><summary>Topology coordinates (26 regions)</summary>
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
      <td>2</td>
      <td>3</td>
      <td>2</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>14</td>
      <td>4</td>
      <td>14</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>18</td>
      <td>15</td>
      <td>18</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>34</td>
      <td>19</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>35</td>
      <td>35</td>
      <td>35</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>56</td>
      <td>36</td>
      <td>56</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>71</td>
      <td>57</td>
      <td>71</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>93</td>
      <td>72</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>103</td>
      <td>94</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>121</td>
      <td>104</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>122</td>
      <td>136</td>
      <td>122</td>
      <td>136</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>154</td>
      <td>137</td>
      <td>154</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>169</td>
      <td>155</td>
      <td>169</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>211</td>
      <td>208</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>233</td>
      <td>212</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>239</td>
      <td>234</td>
      <td>239</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>245</td>
      <td>240</td>
      <td>245</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>246</td>
      <td>250</td>
      <td>246</td>
      <td>250</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>271</td>
      <td>251</td>
      <td>271</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>278</td>
      <td>272</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>299</td>
      <td>279</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>315</td>
      <td>300</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>332</td>
      <td>316</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>344</td>
      <td>333</td>
      <td>344</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>363</td>
      <td>345</td>
      <td>363</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>374</td>
      <td>364</td>
      <td>374</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7egl">7EGL</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">AKPANKLVIVTEKILLKKIAKIIDESGAKGYTVMNTGGKG</span><span class="topo-unknown">SRNVRSSGQPNTSDIE</span><span class="topo-inside">ANIKFEILTETREMAEEIADRVAVKYFNDYAGIIYICSAEVLYGHTFCGPEGC</span></span>
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
      <td>2</td>
      <td>41</td>
      <td>2</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>110</td>
      <td>58</td>
      <td>110</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7egl">7EGL</a> — Chain C (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">DF</span><span class="topo-unknown">LSNFLTDFVGQ</span><span class="topo-outside">LQSP</span><span class="topo-membrane">TLAFLIGGMVIAALGT</span><span class="topo-inside">Q</span><span class="topo-membrane">LVIPEAISTIIVFMLLTKIGL</span><span class="topo-outside">TGGMAIRNSNLTEML</span><span class="topo-membrane">LPVAFSVILGILIVFIARFTLA</span><span class="topo-inside">KLPNVRTVDA</span><span class="topo-membrane">LATGGLFGAVSGSTMAA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">A</span><span class="topo-outside">LTTLEESKISYEAWA</span><span class="topo-membrane">GALYPFMDIPALVTAIVV</span><span class="topo-inside">ANIYLNKRKRKSAAA</span><span class="topo-unknown">SIEESFSKQPVAAGDYGDQTDYPRTRQEYLSQQEPEDN</span><span class="topo-inside">RVKI</span><span class="topo-membrane">WPIIEESLQGPALSAMLLGLAL</span><span class="topo-outside">GIFTKP</span><span class="topo-unknown">E</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">SVYEG</span><span class="topo-outside">FYDPL</span><span class="topo-membrane">FRGLLSILMLIMGMEAWSRIG</span><span class="topo-inside">ELRKVAQ</span><span class="topo-membrane">WYVVYSLIAPIVHGFIAFGLG</span><span class="topo-outside">MIAHYATGFSLGGVVV</span><span class="topo-membrane">LAVIAASSSDISGPPTL</span><span class="topo-inside">RAGIPSANPSAY</span><span class="topo-membrane">IGSSTAIGTPIAIGVC</span></span>
<span class="topo-ruler">       370    </span>
<span class="topo-line"><span class="topo-membrane">IPL</span><span class="topo-outside">FIGLAQTLGAG</span></span>
<details class="topo-details"><summary>Topology coordinates (26 regions)</summary>
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
      <td>2</td>
      <td>3</td>
      <td>2</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>14</td>
      <td>4</td>
      <td>14</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>18</td>
      <td>15</td>
      <td>18</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>34</td>
      <td>19</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>35</td>
      <td>35</td>
      <td>35</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>56</td>
      <td>36</td>
      <td>56</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>71</td>
      <td>57</td>
      <td>71</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>93</td>
      <td>72</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>103</td>
      <td>94</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>121</td>
      <td>104</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>122</td>
      <td>136</td>
      <td>122</td>
      <td>136</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>154</td>
      <td>137</td>
      <td>154</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>169</td>
      <td>155</td>
      <td>169</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>211</td>
      <td>208</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>233</td>
      <td>212</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>239</td>
      <td>234</td>
      <td>239</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>245</td>
      <td>240</td>
      <td>245</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>246</td>
      <td>250</td>
      <td>246</td>
      <td>250</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>271</td>
      <td>251</td>
      <td>271</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>278</td>
      <td>272</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>299</td>
      <td>279</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>315</td>
      <td>300</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>332</td>
      <td>316</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>344</td>
      <td>333</td>
      <td>344</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>363</td>
      <td>345</td>
      <td>363</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>374</td>
      <td>364</td>
      <td>374</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7egl">7EGL</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">AKPANKLVIVTEKILLKKIAKIIDESGAKGYTVMNTGGKG</span><span class="topo-unknown">SRNVRSSGQPNTSDIE</span><span class="topo-inside">ANIKFEILTETREMAEEIADRVAVKYFNDYAGIIYICSAEVLYGHTFCGPEGC</span></span>
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
      <td>2</td>
      <td>41</td>
      <td>2</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>110</td>
      <td>58</td>
      <td>110</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7egl">7EGL</a> — Chain E (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">DF</span><span class="topo-unknown">LSNFLTDFVGQ</span><span class="topo-outside">LQSP</span><span class="topo-membrane">TLAFLIGGMVIAALGT</span><span class="topo-inside">Q</span><span class="topo-membrane">LVIPEAISTIIVFMLLTKIGL</span><span class="topo-outside">TGGMAIRNSNLTEML</span><span class="topo-membrane">LPVAFSVILGILIVFIARFTLA</span><span class="topo-inside">KLPNVRTVDA</span><span class="topo-membrane">LATGGLFGAVSGSTMAA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">A</span><span class="topo-outside">LTTLEESKISYEAWA</span><span class="topo-membrane">GALYPFMDIPALVTAIVV</span><span class="topo-inside">ANIYLNKRKRKSAAA</span><span class="topo-unknown">SIEESFSKQPVAAGDYGDQTDYPRTRQEYLSQQEPEDN</span><span class="topo-inside">RVKI</span><span class="topo-membrane">WPIIEESLQGPALSAMLLGLAL</span><span class="topo-outside">GIFTKP</span><span class="topo-unknown">E</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">SVYEG</span><span class="topo-outside">FYDPL</span><span class="topo-membrane">FRGLLSILMLIMGMEAWSRIG</span><span class="topo-inside">ELRKVAQ</span><span class="topo-membrane">WYVVYSLIAPIVHGFIAFGLG</span><span class="topo-outside">MIAHYATGFSLGGVVV</span><span class="topo-membrane">LAVIAASSSDISGPPTL</span><span class="topo-inside">RAGIPSANPSAY</span><span class="topo-membrane">IGSSTAIGTPIAIGVC</span></span>
<span class="topo-ruler">       370    </span>
<span class="topo-line"><span class="topo-membrane">IPL</span><span class="topo-outside">FIGLAQTLGAG</span></span>
<details class="topo-details"><summary>Topology coordinates (26 regions)</summary>
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
      <td>2</td>
      <td>3</td>
      <td>2</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>14</td>
      <td>4</td>
      <td>14</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>18</td>
      <td>15</td>
      <td>18</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>34</td>
      <td>19</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>35</td>
      <td>35</td>
      <td>35</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>56</td>
      <td>36</td>
      <td>56</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>71</td>
      <td>57</td>
      <td>71</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>93</td>
      <td>72</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>103</td>
      <td>94</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>121</td>
      <td>104</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>122</td>
      <td>136</td>
      <td>122</td>
      <td>136</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>154</td>
      <td>137</td>
      <td>154</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>169</td>
      <td>155</td>
      <td>169</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>211</td>
      <td>208</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>233</td>
      <td>212</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>239</td>
      <td>234</td>
      <td>239</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>245</td>
      <td>240</td>
      <td>245</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>246</td>
      <td>250</td>
      <td>246</td>
      <td>250</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>271</td>
      <td>251</td>
      <td>271</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>278</td>
      <td>272</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>299</td>
      <td>279</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>315</td>
      <td>300</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>332</td>
      <td>316</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>344</td>
      <td>333</td>
      <td>344</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>363</td>
      <td>345</td>
      <td>363</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>374</td>
      <td>364</td>
      <td>374</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7egl">7EGL</a> — Chain F (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">AKPANKLVIVTEKILLKKIAKIIDESGAKGYTVMNTGGKG</span><span class="topo-unknown">SRNVRSSGQPNTSDIE</span><span class="topo-inside">ANIKFEILTETREMAEEIADRVAVKYFNDYAGIIYICSAEVLYGHTFCGPEGC</span></span>
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
      <td>2</td>
      <td>41</td>
      <td>2</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>110</td>
      <td>58</td>
      <td>110</td>
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

### Bicarbonate and sodium binding site

The substrate-binding site is formed by a TM cross where broken helices TM4a/b and TM9a/b cross over. HCO3- is coordinated by residues from TM4 and TM9. Na+ is coordinated by nearby residues. The binding site is located in the core domain, accessible from the cytoplasm in the inward-facing state.

### Elevator transport mechanism

SbtA adopts an [Elevator Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/elevator-mechanism/) for bicarbonate transport. The core domain (TMs 3-5, 8-10) undergoes rigid-body movement relative to the scaffold domain (TMs 1-2, 6-7) to translocate HCO3- across the membrane. This mechanism is shared with structurally homologous SLC family transporters including [NHAA](/xray-mp-wiki/proteins/slc-transporters/nhaa/), NhaP, NapA, and ASBT_NM, which share similar overall topology despite low sequence identity.

### Trimeric functional unit

SbtA forms a homotrimer that is the functional unit. The scaffold domain mediates inter-subunit interactions along the trimer interface. Each [SBTB](/xray-mp-wiki/proteins/slc-transporters/sbtb/) protomer binds to the cytoplasmic surface of one SbtA protomer to form a 1:1 heterodimer within the overall 3:3 complex.


## Cross-References

- <a href="/xray-mp-wiki/proteins/slc-transporters/sbtb/">SbtB (PII-Like Regulatory Protein, Synechocystis sp. PCC 6803)</a> — SbtB is the allosteric regulatory protein that binds to SbtA and inhibits bicarbonate transport
- <a href="/xray-mp-wiki/concepts/miscellaneous/co2-concentrating-mechanism/">CO2-Concentrating Mechanism</a> — SbtA is one of five dissolved inorganic carbon uptake systems in the cyanobacterial CCM
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/elevator-mechanism/">Elevator Mechanism</a> — SbtA uses an elevator mechanism for bicarbonate transport
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/allosteric-regulation/">Allosteric Regulation in Membrane Proteins</a> — SbtA is allosterically inhibited by SbtB through T-loop insertion
- <a href="/xray-mp-wiki/proteins/slc-transporters/nhaa/">NhaA Sodium/Proton Antiporter</a> — Structural homologue sharing similar TM topology and transport mechanism
- <a href="/xray-mp-wiki/proteins/slc-transporters/nap-a/">Na+/H+ Antiporter NapA from Thermus thermophilus</a> — Structural homologue sharing similar elevator transport mechanism
- <a href="/xray-mp-wiki/proteins/slc-transporters/asbt-nm/">ASBT-NM (Bacterial Homologue of the Bile Acid Sodium Symporter ASBT)</a> — Structural homologue sharing similar 10 TM topology and elevator-like transport mechanism
- <a href="/xray-mp-wiki/proteins/other-ion-channels/amt-b/">Ammonium Transporter AmtB (E. coli)</a> — Analogous regulatory system where PII protein GlnK allosterically inhibits AmtB
- <a href="/xray-mp-wiki/proteins/other-ion-channels/glnk/">GlnK PII Signal Transduction Protein (E. coli)</a> — SbtB is functionally analogous to GlnK, both being PII-family regulators
- <a href="/xray-mp-wiki/concepts/signaling-receptors/pii-protein-family/">PII Signal Transduction Protein Family</a> — SbtB is a member of the PII protein family
- <a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a> — Main structural method used (2.7 A cryo-EM structure)
- <a href="/xray-mp-wiki/methods/structure-determination/xray-crystallography/">X-ray Crystallography</a> — Complementary crystal structure at 3.2 A resolution
- <a href="/xray-mp-wiki/methods/solubilization/nanodisc-reconstitution/">Nanodisc Reconstitution</a> — SbtA-SbtB was reconstituted into POPG nanodiscs for cryo-EM
