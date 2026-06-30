---
title: "SbtB (PII-Like Regulatory Protein, Synechocystis sp. PCC 6803)"
created: 2026-06-11
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [xray-crystallography, transporter]
sources: [doi/10.1073##pnas.2101632118]
verified: false
---

# SbtB (PII-Like Regulatory Protein, Synechocystis sp. PCC 6803)

## Overview

SbtB is a PII-like signal transduction protein from the cyanobacterium Synechocystis sp. PCC 6803 that allosterically regulates the bicarbonate transporter [SBTA](/xray-mp-wiki/proteins/slc-transporters/sbta/). SbtB forms a homotrimer in the cytoplasm, with each protomer adopting a classic PII fold characterized by four antiparallel beta-strands and flanking alpha-helices. SbtB binds adenyl nucleotides (AMP, ADP, ATP, cAMP) at the trimer interfaces, and the identity of the bound nucleotide dictates the conformation of its T-loop, which controls [SBTA](/xray-mp-wiki/proteins/slc-transporters/sbta/) binding. AMP binding stabilizes the T-loop in an extended conformation that inserts into the cytoplasmic cavity of [SBTA](/xray-mp-wiki/proteins/slc-transporters/sbta/), locking the transporter in an inward-facing state and inhibiting bicarbonate transport. cAMP binding disrupts the T-loop conformation, relieving inhibition.


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
      <td>Full-length SbtB (Synechocystis sp. PCC 6803) in complex with <a href="/xray-mp-wiki/proteins/slc-transporters/sbta/">SBTA</a></td>
      <td>AMP</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7egl">7EGL</a></td>
      <td>3.2</td>
      <td>(not specified)</td>
      <td>Full-length SbtB (Synechocystis sp. PCC 6803) in complex with <a href="/xray-mp-wiki/proteins/slc-transporters/sbta/">SBTA</a></td>
      <td>None (no AMP in crystal structure)</td>
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
      <td>Co-expression</td>
      <td>E. coli C43(DE3) with pRSFDuet-SbtA-SbtB</td>
      <td>—</td>
      <td></td>
      <td><a href="/xray-mp-wiki/proteins/slc-transporters/sbta/">SBTA</a> with C-terminal His-tag; SbtB untagged. Co-purification with <a href="/xray-mp-wiki/proteins/slc-transporters/sbta/">SBTA</a> via pull-down.</td>
    </tr>
    <tr>
      <td>Co-purification</td>
      <td>Ni-NTA affinity + SEC</td>
      <td>—</td>
      <td>100 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 2 mM AMP; 0.018% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> or 0.18% DM</td>
      <td>AMP (2 mM) in purification buffer essential for stable 1:1 SbtA-SbtB complex. ADP also supports complex; cAMP and ATP do not.</td>
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

### AMP-dependent T-loop stabilization

The T-loop of SbtB (residues ~37-54) adopts a defined conformation when AMP is bound at the trimer interface. AMP forms hydrogen bonds with residues Ser42 and Arg43 from the T-loop and Gly89 from beta4. Arg43 also hydrogen bonds with Asp86 from the alpha2-beta4 loop. These interactions collectively stabilize the T-loop in an extended conformation capable of [SBTA](/xray-mp-wiki/proteins/slc-transporters/sbta/) binding.

### Allosteric inhibition of SbtA

The T-loop inserts into the cytoplasmic cavity of [SBTA](/xray-mp-wiki/proteins/slc-transporters/sbta/) formed between its scaffold domain (TMs 1-2, 6-7) and core domain (TMs 3-5, 8-10). This locks [SBTA](/xray-mp-wiki/proteins/slc-transporters/sbta/) in an inward-facing state, preventing the conformational changes required for bicarbonate transport. The mechanism is analogous to AmtB regulation by [GLNK](/xray-mp-wiki/proteins/other-ion-channels/glnk/) in bacteria.

### Nucleotide selectivity

AMP and ADP stabilize the T-loop and promote SbtA-SbtB complex formation, while cAMP and ATP do not. cAMP binding to SbtB would cause steric clash with Arg46 and lose key hydrogen bonds from Ser42 and Arg43, distorting the T-loop and preventing [SBTA](/xray-mp-wiki/proteins/slc-transporters/sbta/) interaction. This creates a regulatory switch responsive to cellular energy and carbon status.

### PII family conservation

SbtB belongs to the PII family of signal transduction proteins, which regulate nitrogen assimilation and carbon homeostasis in bacteria and archaea. The regulation of [SBTA](/xray-mp-wiki/proteins/slc-transporters/sbta/) by SbtB closely parallels the regulation of ammonium transporter AmtB by [GLNK](/xray-mp-wiki/proteins/other-ion-channels/glnk/) in E. coli, where [GLNK](/xray-mp-wiki/proteins/other-ion-channels/glnk/) also forms a trimer with ADP at the dimer interface and inserts its T-loop to block the AmtB channel.


## Cross-References

- <a href="/xray-mp-wiki/proteins/slc-transporters/sbta/">SbtA (High-Affinity Sodium-Dependent Bicarbonate Transporter)</a> — SbtB is the allosteric regulator of SbtA bicarbonate transporter
- <a href="/xray-mp-wiki/concepts/signaling-receptors/pii-protein-family/">PII Signal Transduction Protein Family</a> — SbtB is a member of the PII protein family
- <a href="/xray-mp-wiki/proteins/other-ion-channels/glnk/">GlnK PII Signal Transduction Protein (E. coli)</a> — SbtB is functionally and structurally analogous to GlnK
- <a href="/xray-mp-wiki/proteins/other-ion-channels/amt-b/">Ammonium Transporter AmtB (E. coli)</a> — AmtB-GlnK is the paradigmatic system of PII-mediated transporter regulation
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/allosteric-regulation/">Allosteric Regulation in Membrane Proteins</a> — SbtB allosterically inhibits SbtA through T-loop insertion
- <a href="/xray-mp-wiki/concepts/miscellaneous/co2-concentrating-mechanism/">CO2-Concentrating Mechanism</a> — SbtA-SbtB system regulates bicarbonate uptake in the cyanobacterial CCM
- <a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a> — Main structural method used
- <a href="/xray-mp-wiki/methods/structure-determination/xray-crystallography/">X-ray Crystallography</a> — Complementary crystal structure
- <a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> — Buffer component in purification or crystallization
