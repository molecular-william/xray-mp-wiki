---
title: "Lysophosphatidic Acid Receptor 1 (LPA1)"
created: 2026-05-27
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2015.06.002]
verified: regex
uniprot_id: Q92633
---

# Lysophosphatidic Acid Receptor 1 (LPA1)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q92633">UniProt: Q92633</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

Lysophosphatidic acid receptor 1 (LPA1, also known as LPAR1 or EDG2) is a class A G protein-coupled receptor that binds lysophosphatidic acid (LPA), a bioactive lysophospholipid signaling molecule. LPA1 couples to multiple G protein pathways (Gq, Gi, G12/13) and mediates diverse physiological responses including cell proliferation, migration, and survival. Dysregulation of LPA1 signaling has been linked to cancer progression, hydrocephalus, and neuropathic pain. The first crystal structure of LPA1 revealed a spherical binding pocket and an extracellular ligand access pathway distinct from the related [Sphingosine](/xray-mp-wiki/reagents/lipids/sphingosine)-1-phosphate receptor [S1P1](/xray-mp-wiki/proteins/s1p1).

## Publications

### doi/10.1016##j.cell.2015.06.002

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4z34">4Z34</a></td>
      <td>3.0</td>
      <td>P212121</td>
      <td>Human LPA1 with bRIL fusion in ICL3 (R233, R247 positions), C-terminus truncated (38 residues removed), antagonist-bound</td>
      <td>ONO-9780307</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4z35">4Z35</a></td>
      <td>2.9</td>
      <td>P212121</td>
      <td>Human LPA1 with bRIL fusion in ICL3 (R233, R247 positions), C-terminus truncated (38 residues removed), antagonist-bound</td>
      <td>ONO-9910539</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4z36">4Z36</a></td>
      <td>2.9</td>
      <td>P212121</td>
      <td>Human LPA1 with engineered disulfide bond (D204A-V282C), mbRIL fusion in ICL3, C-terminus truncated, antagonist-bound</td>
      <td>ONO-3080573</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells
- **Construct**: Human LPA1 with bRIL (b562RIL) fusion in ICL3 at Ballesteros positions 5.66 (R233) and 6.24 (R247), C-terminal truncation removing 38 residues. For ONO-3080573: dsLPA1-mbRIL with engineered disulfide between D204A and V282C, mbRIL with modified disordered loop (short linker)

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
      <td>Cell culture and membrane preparation</td>
      <td>Sf9 insect cell expression</td>
      <td>--</td>
      <td>-- + --</td>
      <td>LPA1-<a href="/xray-mp-wiki/reagents/protein-tags/bril">BRIL Fusion Protein</a> construct expressed in Sf9 insect cells; membranes harvested for stability assays and purification</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Ni-NTA</td>
      <td>--</td>
      <td>His-tag on <a href="/xray-mp-wiki/reagents/protein-tags/bril">BRIL Fusion Protein</a> fusion partner used for affinity capture</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td>SEC column</td>
      <td>--</td>
      <td>Analytical SEC used for stability screening in place of CPM assay; SEC stability assays guided compound selection</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>LPA1-<a href="/xray-mp-wiki/reagents/protein-tags/bril">BRIL Fusion Protein</a> co-crystallized with <a href="/xray-mp-wiki/reagents/ligands/ono-9780307">ONO-9780307</a> or <a href="/xray-mp-wiki/reagents/ligands/ono-9910539">ONO-9910539</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not specified in main text</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified in main text</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>not specified in main text</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in <a href="/xray-mp-wiki/reagents/lipids/monoolein">Monoolein</a>-<a href="/xray-mp-wiki/reagents/lipids/cholesterol">Cholesterol</a> LCP mixture. <a href="/xray-mp-wiki/reagents/ligands/ono-9780307">ONO-9780307</a>: 86 crystals, 3.0 A resolution. <a href="/xray-mp-wiki/reagents/ligands/ono-9910539">ONO-9910539</a>: 53 crystals, 2.9 A resolution. P212121 space group.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>dsLPA1-mbRIL co-crystallized with <a href="/xray-mp-wiki/reagents/ligands/ono-3080573">ONO-3080573</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not specified in main text</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified in main text</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>not specified in main text</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Disulfide-engineered construct (D204A-V282C) with modified mbRIL fusion. 39 crystals, 2.9 A resolution. P212121 space group.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4z34">4Z34</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFAGAPAAISTSIPVISQPQFTAM</span><span class="topo-outside">NEPQCFYNESIAFFYNRSGKHLATEWNTV</span><span class="topo-membrane">SKLVMGLGITVCIFIMLANLLVMV</span><span class="topo-inside">AIYVNRRFHFPIYYL</span><span class="topo-membrane">MANLAAADFFAGLAY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">FYLMFNT</span><span class="topo-outside">GPNTRRLTV</span><span class="topo-membrane">STWLLRQGLIDTSLTASVANLLAIA</span><span class="topo-inside">IERHITVFRMQLHTRMSNRRVV</span><span class="topo-membrane">VVIVVIWTMAIVMGAIPSVGWNC</span><span class="topo-outside">ICDIENCSNMAPL</span><span class="topo-membrane">YSDSYLVFWAIFNLVTFVVMV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">VLYA</span><span class="topo-inside">HIFGYVADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKA</span><span class="topo-unknown">TPPKLEDKSPDSPE</span><span class="topo-inside">MKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLRNRD</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460    </span>
<span class="topo-line"><span class="topo-inside">TMMSLLKT</span><span class="topo-membrane">VVIVLGAFIICWTPGLVLLLLDVCC</span><span class="topo-outside">PQCDVL</span><span class="topo-membrane">AYEKFFLLLAEFNSAMNPIIYSY</span><span class="topo-inside">RDKEMSATFRQILG</span><span class="topo-unknown">RPLEVLFQGPHHHHHHHHHHDYKDDDDK</span></span>
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
      <td>37</td>
      <td>-17</td>
      <td>19</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>38</td>
      <td>66</td>
      <td>20</td>
      <td>48</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>90</td>
      <td>49</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>105</td>
      <td>73</td>
      <td>87</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>127</td>
      <td>88</td>
      <td>109</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>128</td>
      <td>136</td>
      <td>110</td>
      <td>118</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>161</td>
      <td>119</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>162</td>
      <td>183</td>
      <td>144</td>
      <td>165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>206</td>
      <td>166</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>219</td>
      <td>189</td>
      <td>201</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>244</td>
      <td>202</td>
      <td>226</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>250</td>
      <td>227</td>
      <td>232</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>293</td>
      <td>1001</td>
      <td>1043</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>307</td>
      <td>1044</td>
      <td>1057</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>308</td>
      <td>356</td>
      <td>1058</td>
      <td>1106</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>357</td>
      <td>368</td>
      <td>248</td>
      <td>259</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>369</td>
      <td>393</td>
      <td>260</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>394</td>
      <td>399</td>
      <td>285</td>
      <td>290</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>422</td>
      <td>291</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>423</td>
      <td>436</td>
      <td>314</td>
      <td>327</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>437</td>
      <td>464</td>
      <td>328</td>
      <td>355</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4z35">4Z35</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFAGAPAAISTSIPVISQPQFTAMNEP</span><span class="topo-outside">QCFYNESIAFFYNRSGKHLATEWNTVSK</span><span class="topo-membrane">LVMGLGITVCIFIMLANLLVMVAIY</span><span class="topo-inside">VNRRFHFPIY</span><span class="topo-membrane">YLMANLAAADFFAGLAY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">FYLMFNT</span><span class="topo-outside">GPNTRRLTVST</span><span class="topo-membrane">WLLRQGLIDTSLTASVANLLAIAI</span><span class="topo-inside">ERHITVFRMQLHTRMSNRR</span><span class="topo-membrane">VVVVIVVIWTMAIVMGAIPSVGWN</span><span class="topo-outside">CICDIENCSNMAPLY</span><span class="topo-membrane">SDSYLVFWAIFNLVTFVVMV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">VLYA</span><span class="topo-inside">HIFGYVADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKA</span><span class="topo-unknown">TPPKLEDKSPDSPE</span><span class="topo-inside">MKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLRNRD</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460    </span>
<span class="topo-line"><span class="topo-inside">TMMSLLKT</span><span class="topo-membrane">VVIVLGAFIICWTPGLVLLLLDVCC</span><span class="topo-outside">PQC</span><span class="topo-membrane">DVLAYEKFFLLLAEFNSAMNPIIYSYR</span><span class="topo-inside">DKEMSATFRQILG</span><span class="topo-unknown">RPLEVLFQGPHHHHHHHHHHDYKDDDDK</span></span>
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
      <td>40</td>
      <td>-17</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>41</td>
      <td>68</td>
      <td>23</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>93</td>
      <td>51</td>
      <td>75</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>103</td>
      <td>76</td>
      <td>85</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>127</td>
      <td>86</td>
      <td>109</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>128</td>
      <td>138</td>
      <td>110</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>139</td>
      <td>162</td>
      <td>121</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>181</td>
      <td>145</td>
      <td>163</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>205</td>
      <td>164</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>206</td>
      <td>220</td>
      <td>188</td>
      <td>202</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>244</td>
      <td>203</td>
      <td>226</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>250</td>
      <td>227</td>
      <td>232</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>293</td>
      <td>1001</td>
      <td>1043</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>307</td>
      <td>1044</td>
      <td>1057</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>308</td>
      <td>356</td>
      <td>1058</td>
      <td>1106</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>357</td>
      <td>368</td>
      <td>248</td>
      <td>259</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>369</td>
      <td>393</td>
      <td>260</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>394</td>
      <td>396</td>
      <td>285</td>
      <td>287</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>397</td>
      <td>423</td>
      <td>288</td>
      <td>314</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>424</td>
      <td>436</td>
      <td>315</td>
      <td>327</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>437</td>
      <td>464</td>
      <td>328</td>
      <td>355</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4z36">4Z36</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFAGAPAAISTSIPVISQPQFTAMNEP</span><span class="topo-outside">QCFYNESIAFFYNRSGKHLATEWNTV</span><span class="topo-membrane">SKLVMGLGITVCIFIMLANLLVMVAIY</span><span class="topo-inside">VNRRFHFPIYY</span><span class="topo-membrane">LMANLAAADFFAGLAY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">FYLMFNT</span><span class="topo-outside">GPNTRRLTVS</span><span class="topo-membrane">TWLLRQGLIDTSLTASVANLLAIAI</span><span class="topo-inside">ERHITVFRMQLHTRMSNRRV</span><span class="topo-membrane">VVVIVVIWTMAIVMGAIPSVGWN</span><span class="topo-outside">CICDIENCSNMAPLY</span><span class="topo-membrane">SCSYLVFWAIFNLVTFVVMV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">VLYA</span><span class="topo-inside">HIFGYVADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKG</span><span class="topo-unknown">GSGGSDSPE</span><span class="topo-inside">MKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLRNRDTMMSL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450         </span>
<span class="topo-line"><span class="topo-inside">LKT</span><span class="topo-membrane">VVIVLGAFIICWTPGLVLLLLDCCC</span><span class="topo-outside">PQC</span><span class="topo-membrane">DVLAYEKFFLLLAEFNSAMNPIIYSY</span><span class="topo-inside">RDKEMSATFRQILG</span><span class="topo-unknown">RPLEVLFQGPHHHHHHHHHHDYKDDDDK</span></span>
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
      <td>40</td>
      <td>-17</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>41</td>
      <td>66</td>
      <td>23</td>
      <td>48</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>93</td>
      <td>49</td>
      <td>75</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>104</td>
      <td>76</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>127</td>
      <td>87</td>
      <td>109</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>128</td>
      <td>137</td>
      <td>110</td>
      <td>119</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>138</td>
      <td>162</td>
      <td>120</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>182</td>
      <td>145</td>
      <td>164</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>205</td>
      <td>165</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>206</td>
      <td>220</td>
      <td>188</td>
      <td>202</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>244</td>
      <td>203</td>
      <td>226</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>250</td>
      <td>227</td>
      <td>232</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>293</td>
      <td>1001</td>
      <td>1043</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>302</td>
      <td>1044</td>
      <td>1052</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>303</td>
      <td>351</td>
      <td>1058</td>
      <td>1106</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>352</td>
      <td>363</td>
      <td>248</td>
      <td>259</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>364</td>
      <td>388</td>
      <td>260</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>389</td>
      <td>391</td>
      <td>285</td>
      <td>287</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>392</td>
      <td>417</td>
      <td>288</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>418</td>
      <td>431</td>
      <td>314</td>
      <td>327</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>432</td>
      <td>459</td>
      <td>328</td>
      <td>355</td>
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

### Spherical binding pocket with extracellular ligand access

The LPA1 binding pocket is spherical in nature, contrasting with the more linear binding pocket of [S1P1](/xray-mp-wiki/proteins/s1p1). The position of TM1 in LPA1 is shifted 3 A closer to TM7 compared to [S1P1](/xray-mp-wiki/proteins/s1p1), closing the gap that was postulated to enable membrane-embedded ligand access for [S1P1](/xray-mp-wiki/proteins/s1p1). Molecular dynamics simulations over 100 ns confirmed that the distance between TM1 and TM7 is consistently smaller and less variable in LPA1 than in [S1P1](/xray-mp-wiki/proteins/s1p1), with a difference of approximately 7 A at the extracellular tip in the absence of ligand. This structural feature suggests LPA1 preferentially receives ligands from the extracellular milieu rather than via the membrane, consistent with the biological existence of albumin-bound LPA and the delivery of LPA by autotaxin.

### Key binding pocket residues and antagonist interactions

The carboxylic acid of [ONO-9780307](/xray-mp-wiki/reagents/ligands/ono-9780307) interacts through polar and ionic bonds with His40, Lys39, and Tyr34 on the N-terminal capping helix and ECL0 loop. Arg124(3.28) and Gln125(3.29) on TM3 form ionic and polar interactions with the carboxylic acid and chiral hydroxyl group. Glu293(7.35) from TM7 stabilizes Lys39. The enhanced polar environment on TM3 and TM5 includes Asp129(3.33) on TM3 and Trp210(5.43) on TM5, which presents its indole nitrogen for hydrogen bonding. His40 is unique to LPA1 among the LPA receptor family and may be important for high-affinity antagonist binding. Calculations show protonated His40 increases binding affinity by more than 1 kcal/mol.

### Torsionally strained bioactive ligand conformation

The bioactive conformation of [ONO-9780307](/xray-mp-wiki/reagents/ligands/ono-9780307) requires a strained eclipsed torsion angle on the bond adjacent to the indane ring, with a difference of 9.6 kcal/mol between the observed conformation and the local energy minimum. The ligand positions its branching aromatic indane and dimethoxy phenyl rings adjacent to each other in the spherical binding pocket. The local energy minimum conformation is not able to bind due to projected clashes with TM6. This torsional strain was alleviated in [ONO-3080573](/xray-mp-wiki/reagents/ligands/ono-3080573) by replacing the methylene linker with an ether linkage.

### Ligand access path divergence between LPA1 and S1P1

Three key amino acid differences between LPA1 and [S1P1](/xray-mp-wiki/proteins/s1p1) account for the distinct pocket shapes: position 3.33 is aspartate in LPA1 versus phenylalanine in [S1P1](/xray-mp-wiki/proteins/s1p1); position 5.43 is tryptophan in LPA1 versus cysteine in [S1P1](/xray-mp-wiki/proteins/s1p1); position 6.51 is [Glycine](/xray-mp-wiki/reagents/buffers/glycine) in LPA1 versus leucine in [S1P1](/xray-mp-wiki/proteins/s1p1). The reduction in side chain bulk at position 6.51 opens a sub-pocket occupied by the indane ring of the antagonist series. The configuration of the extracellular region in LPA1 is constrained by two intraloop disulfide bonds in ECL2 and ECL3, and a disulfide bond connecting ECL2 with the N terminus.

### Promiscuous recognition of phosphorylated endocannabinoids

Molecular modeling predicted that the LPA1 binding pocket can accommodate phosphorylated endocannabinoids 2-ALPA (2-arachidonoyl-LPA) and pAEA (phosphorylated anandamide), which are generated through enzymatic action from endogenous cannabinoids. Cell-based assays confirmed that all phosphorylated ligands produced robust signaling via calcium response and cAMP inhibition in LPA1-expressing cells. A neurite retraction assay showed robust activation by pAEA, involving Rho GTPase activation and F-actin stress fiber formation. This links the LPA and cannabinoid receptor systems through metabolically related ligands with potential functional and therapeutic implications.

### Structure-based design of improved antagonists

Three antagonists were designed through structure-based approaches. [ONO-9910539](/xray-mp-wiki/reagents/ligands/ono-9910539) features an acetyl group in the para position of the phenyl ring for enhanced polar interactions with Trp210(5.43) and reduced lipophilicity. [ONO-3080573](/xray-mp-wiki/reagents/ligands/ono-3080573) replaced the methylene linker with an ether linkage to reduce torsional strain and substituted the metabolically labile pyrrole ring with a phenyl ring for improved metabolic stability, differentially positioning the carboxylic acid to gain interaction with Lys294(7.36) while breaking interactions with Arg124(3.28), His40, and Tyr34.


## Cross-References

- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Primary lipid component for LCP crystallization matrix
- <a href="/xray-mp-wiki/reagents/protein-tags/bril/">bRIL Fusion Protein</a> — bRIL fusion in ICL3 used for crystallization of LPA1
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — LCP method used for all three LPA1 structures
- <a href="/xray-mp-wiki/proteins/gpcr/s1p1/">Sphingosine-1-Phosphate Receptor 1 (S1P1)</a> — Closest structural and functional homolog, major comparison throughout the paper
- <a href="/xray-mp-wiki/reagents/ligands/ono-9780307/">ONO-9780307</a> — Co-crystallized antagonist for PDB 4Z34
- <a href="/xray-mp-wiki/reagents/ligands/ono-9910539/">ONO-9910539</a> — Co-crystallized antagonist for PDB 4Z35
- <a href="/xray-mp-wiki/reagents/ligands/ono-3080573/">ONO-3080573</a> — Co-crystallized antagonist for PDB 4Z36
- <a href="/xray-mp-wiki/reagents/ligands/2-ag/">2-AG (2-Arachidonoylglycerol)</a> — Endogenous cannabinoid agonist; phosphorylated form 2-ALPA activates LPA1
- <a href="/xray-mp-wiki/reagents/lipids/sphingosine/">Sphingosine</a> — Lipid component used in crystallization or solubilization
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Lipid component used in crystallization or solubilization
