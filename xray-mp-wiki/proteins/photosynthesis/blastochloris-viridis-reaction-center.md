---
title: "Blastochloris viridis Photosynthetic Reaction Center (RC_vir)"
created: 2026-06-16
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein]
sources: [doi/10.1021##bi900545e]
verified: agent
uniprot_id: ['P06008', 'P06009', 'P06010', 'P07173']
---

# Blastochloris viridis Photosynthetic Reaction Center (RC_vir)

<div class="expr-badges"><span class="expr-badge expr-native-tissue">Native tissue</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P06008">UniProt: P06008</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P06009">UniProt: P06009</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P06010">UniProt: P06010</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P07173">UniProt: P07173</a>

<span class="expr-badge">Blastochloris viridis</span>

## Overview

The photosynthetic reaction center from Blastochloris viridis (RC_vir, formerly Rhodopseudomonas viridis) is a multisubunit membrane protein complex that converts light energy into chemical energy through electron transfer. It is structurally homologous to the D1/D2 subunits of [Photosystem II](/xray-mp-wiki/proteins/photosynthesis/photosystem-ii/) (PSII) and was the first integral membrane protein from which a high-resolution X-ray structure was obtained. The 1.86 Å lipidic sponge phase ([LSP](/xray-mp-wiki/concepts/membrane-mimetics/lipidic-sponge-phase/)) crystal structure (PDB 2WJM) revealed lipid molecules interacting with the protein surface, including a covalently bound [Diacylglycerol](/xray-mp-wiki/reagents/lipids/diacylglycerol/) on the N-terminus of the tetraheme cytochrome c subunit, a [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) molecule displaced at the QB [Ubiquinone](/xray-mp-wiki/reagents/cofactors/ubiquinone/) binding site, and a 36 Å continuous electron density feature at the interface of transmembrane helices of the H- and M-subunits likely arising from an unidentified lipid.

## Publications

### doi/10.1021##bi900545e

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2wjm">2WJM</a></td>
      <td>1.86</td>
      <td>P2(1)2(1)2</td>
      <td>Full-length Blastochloris viridis reaction center (tetraheme cytochrome c, L-, M-, H-subunits)</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/diacylglycerol/">Diacylglycerol</a>, <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a>, <a href="/xray-mp-wiki/reagents/cofactors/ubiquinone/">Ubiquinone</a> (displaced)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2wjn">2WJN</a></td>
      <td>1.86</td>
      <td>P2(1)2(1)2</td>
      <td>Full-length RC_vir (high-dose data set showing radiation damage effects)</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/diacylglycerol/">Diacylglycerol</a> (partial radiation damage), <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Blastochloris viridis (native organism)
- **Construct**: Native reaction center purified from B. viridis membranes

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
      <td>1. Membrane solubilization with <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a> (4% w/v)</td>
      <td>Dropwise addition, 3 h stirring at room temperature in darkness</td>
      <td>—</td>
      <td>20 mM Tris-HCl, pH 8.5, 1% <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a></td>
      <td></td>
    </tr>
    <tr>
      <td>2. Anion-exchange chromatography</td>
      <td>POROS HQ column, continuous salt gradient (0-500 mM NaCl)</td>
      <td>—</td>
      <td>20 mM Tris-HCl, pH 8.5, 1% <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a></td>
      <td></td>
    </tr>
    <tr>
      <td>3. Gel filtration chromatography</td>
      <td>HiPrep 16/60 Sephacryl S-200 high-resolution column</td>
      <td>—</td>
      <td>10 mM Tris-HCl, pH 8.5, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a>, 0.1 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a></td>
      <td></td>
    </tr>
    <tr>
      <td>4. Buffer exchange and concentration</td>
      <td>100 kDa MWCO Vivaspin concentrator, 3 cycles of concentration/dilution</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">Sodium Phosphate</a>, pH 6.8, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a>, 10 μM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic sponge phase (<a href="/xray-mp-wiki/concepts/membrane-mimetics/lipidic-sponge-phase/">LSP</a>) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified RC_vir at 20-25 mg/mL in 20 mM <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">Sodium Phosphate</a> pH 6.8, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a>, 10 μM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.55 M <a href="/xray-mp-wiki/reagents/buffers/sodium-acetate/">Sodium Acetate</a>, 0.75 M HEPES pH 6.3, 0.1 g/mL Na/K-PO4</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>293 K (room temperature)</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2 weeks</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td><a href="/xray-mp-wiki/concepts/membrane-mimetics/lipidic-sponge-phase/">LSP</a> prepared by mixing <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> with water (60:40 v/v) to form LCP, then adding <a href="/xray-mp-wiki/concepts/membrane-mimetics/lipidic-sponge-phase/">LSP</a> initiating solution (20% Jeffamine M-600, 1 M HEPES pH 8.0, 0.7 M (NH4)2SO4, 2.5% 1,2,3-heptanetriol) at 1:4 (v/v). Hanging-drop vapor-diffusion method with 1 μL <a href="/xray-mp-wiki/concepts/membrane-mimetics/lipidic-sponge-phase/">LSP</a> precipitant + 1 μL protein + 1 μL 1 M trisodium <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a>. Diamond-shaped crystals 0.25 x 0.25 x 0.15 mm. <a href="/xray-mp-wiki/concepts/structural-mechanisms/type-i-crystal-packing/">Type I Crystal Packing</a> with stacked antiparallel planes.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2wjm">2WJM</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">CFEPPPATTTQTGFRGLSMGEVLHPATVKAKKERDAQYPPALAAVKAEGPPVSQVYKNVKVLGNLTEAEFLRTMTAITEWVSPQEGCTYCHDENNLASEAKYPYVVARRMLEMTRAINTN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WTQHVAQTGVTCYTCHRGTPLPPYVRYLEPTLPLNNRETPTHVERVETRSGYVVRLAKYTAYSALNYDPFTMFLANDKRQVRVVPQTALPLVGVSRGKERRPLSDAYATFALMMSISDSL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330      </span>
<span class="topo-line"><span class="topo-outside">GTNCTFCHNAQTFESWGKKSTPQRAIAWWGIRMVRDLNMNYLAPLNASLPASRLGRQGEAPQADCRTCHQGVTKPLFGASRLKDYPELGPIK</span><span class="topo-unknown">AAAK</span></span>
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
      <td>332</td>
      <td>1</td>
      <td>332</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>336</td>
      <td>333</td>
      <td>336</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2wjm">2WJM</a> — Chain H (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MYHGALAQHLDIAQL</span><span class="topo-membrane">VWYAQWLVIWTVVLLYLR</span><span class="topo-inside">REDRREGYPLVE</span><span class="topo-unknown">PLGLVKLAPEDGQVY</span><span class="topo-inside">ELPYPKTFVLPHGGTVTVPRRRPETRELKLAQTDGFEGAPLQPTGNPLVDAVGPASYAER</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">AEVVDATVDGKAKIVPLRVATDFSIAEGDVDPRGLPVVAADGVEAGTVTDLWVDRSEHYFRYLELSVAGSARTALIPLGFCDVKKDKIVVTSILSEQFANVPRLQSRDQITLREEDKVSA</span></span>
<span class="topo-ruler">       250        </span>
<span class="topo-line"><span class="topo-inside">YYAGGLLYATPERAESLL</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>15</td>
      <td>1</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>33</td>
      <td>16</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>45</td>
      <td>34</td>
      <td>45</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>60</td>
      <td>46</td>
      <td>60</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>61</td>
      <td>258</td>
      <td>61</td>
      <td>258</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2wjm">2WJM</a> — Chain L (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">ALLSFERKYRVRGGTLIGGDLFDFWVGPYFVGF</span><span class="topo-membrane">FGVSAIFFIFLGVSLIGY</span><span class="topo-outside">AASQGPTWDPFAISINPPDLKYGLGAAPLLEGGFW</span><span class="topo-membrane">QAITVCALGAFISWMLRE</span><span class="topo-inside">VEISRKLGIGWHV</span><span class="topo-membrane">PL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">AFCVPIFMFCVLQVFR</span><span class="topo-outside">PLLLGSWGHAFPYGILSHLDWVNNFGYQYLNWHYNP</span><span class="topo-membrane">GHMSSVSFLFVNAMALGLHGG</span><span class="topo-inside">LILSVANPGDGDKVKTAEHENQYFRDVVGYSIGALSIHR</span><span class="topo-membrane">LGLFLASN</span></span>
<span class="topo-ruler">       250       260       270    </span>
<span class="topo-line"><span class="topo-membrane">IFLTGAFGTI</span><span class="topo-outside">ASGPFWTRGWPEWWGWWLDIPFWS</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>34</td>
      <td>1</td>
      <td>33</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>52</td>
      <td>34</td>
      <td>51</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>53</td>
      <td>87</td>
      <td>52</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>105</td>
      <td>87</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>118</td>
      <td>105</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>136</td>
      <td>118</td>
      <td>135</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>172</td>
      <td>136</td>
      <td>171</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>193</td>
      <td>172</td>
      <td>192</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>194</td>
      <td>232</td>
      <td>193</td>
      <td>231</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>233</td>
      <td>250</td>
      <td>232</td>
      <td>249</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>251</td>
      <td>274</td>
      <td>250</td>
      <td>273</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2wjm">2WJM</a> — Chain M (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">ADYQTIYTQIQARGPHITVSGEWGDNDRVGKPFYSYWLGKIGDAQIGPIYL</span><span class="topo-membrane">GASGIAAFAFGSTAILIIL</span><span class="topo-outside">FNMAAEVHFDPLQFFRQFFWLGLYPPKAQYGMGIPPLHDGGWWLM</span><span class="topo-membrane">AGLF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MTLSLGSWWIRVYS</span><span class="topo-inside">RARALGLGT</span><span class="topo-membrane">HIAWNFAAAIFFVLCIGCI</span><span class="topo-outside">HPTLVGSWSEGVPFGIWPHIDWLTAFSIRYGNFYYCP</span><span class="topo-membrane">WHGFSIGFAYGCGLLFAAHG</span><span class="topo-inside">ATILAVARFGGDREIEQITDR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320    </span>
<span class="topo-line"><span class="topo-inside">GTAVERAALFWRWTIGFNATIESVHR</span><span class="topo-membrane">WGWFFSLMVMVSASVGIL</span><span class="topo-outside">LTGTFVDNWYLWCVKHGAAPDYPAYLPATPDPASLPGAPK</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>52</td>
      <td>1</td>
      <td>51</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>71</td>
      <td>52</td>
      <td>70</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>116</td>
      <td>71</td>
      <td>115</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>134</td>
      <td>116</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>143</td>
      <td>134</td>
      <td>142</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>144</td>
      <td>162</td>
      <td>143</td>
      <td>161</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>199</td>
      <td>162</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>219</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>266</td>
      <td>219</td>
      <td>265</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>267</td>
      <td>284</td>
      <td>266</td>
      <td>283</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>285</td>
      <td>324</td>
      <td>284</td>
      <td>323</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2wjn">2WJN</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">CFEPPPATTTQTGFRGLSMGEVLHPATVKAKKERDAQYPPALAAVKAEGPPVSQVYKNVKVLGNLTEAEFLRTMTAITEWVSPQEGCTYCHDENNLASEAKYPYVVARRMLEMTRAINTN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WTQHVAQTGVTCYTCHRGTPLPPYVRYLEPTLPLNNRETPTHVERVETRSGYVVRLAKYTAYSALNYDPFTMFLANDKRQVRVVPQTALPLVGVSRGKERRPLSDAYATFALMMSISDSL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330      </span>
<span class="topo-line"><span class="topo-outside">GTNCTFCHNAQTFESWGKKSTPQRAIAWWGIRMVRDLNMNYLAPLNASLPASRLGRQGEAPQADCRTCHQGVTKPLFGASRLKDYPELGPIK</span><span class="topo-unknown">AAAK</span></span>
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
      <td>332</td>
      <td>1</td>
      <td>332</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>336</td>
      <td>333</td>
      <td>336</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2wjn">2WJN</a> — Chain H (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MYHGALAQHLDIAQL</span><span class="topo-membrane">VWYAQWLVIWTVVLLYLR</span><span class="topo-inside">REDRREGYPLVE</span><span class="topo-unknown">PLGLVKLAPEDGQVY</span><span class="topo-inside">ELPYPKTFVLPHGGTVTVPRRRPETRELKLAQTDGFEGAPLQPTGNPLVDAVGPASYAER</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">AEVVDATVDGKAKIVPLRVATDFSIAEGDVDPRGLPVVAADGVEAGTVTDLWVDRSEHYFRYLELSVAGSARTALIPLGFCDVKKDKIVVTSILSEQFANVPRLQSRDQITLREEDKVSA</span></span>
<span class="topo-ruler">       250        </span>
<span class="topo-line"><span class="topo-inside">YYAGGLLYATPERAESLL</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>15</td>
      <td>1</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>33</td>
      <td>16</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>45</td>
      <td>34</td>
      <td>45</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>60</td>
      <td>46</td>
      <td>60</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>61</td>
      <td>258</td>
      <td>61</td>
      <td>258</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2wjn">2WJN</a> — Chain L (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">ALLSFERKYRVRGGTLIGGDLFDFWVGPYFVGF</span><span class="topo-membrane">FGVSAIFFIFLGVSLIGY</span><span class="topo-outside">AASQGPTWDPFAISINPPDLKYGLGAAPLLEGGFWQA</span><span class="topo-membrane">ITVCALGAFISWMLREV</span><span class="topo-inside">EISRKLGIGWH</span><span class="topo-membrane">VPL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">AFCVPIFMFCVLQVF</span><span class="topo-outside">RPLLLGSWGHAFPYGILSHLDWVNNFGYQYLNWHYNPG</span><span class="topo-membrane">HMSSVSFLFVNAMALGLHGGL</span><span class="topo-inside">ILSVANPGDGDKVKTAEHENQYFRDVVGYSIGALSI</span><span class="topo-membrane">HRLGLFLASN</span></span>
<span class="topo-ruler">       250       260       270    </span>
<span class="topo-line"><span class="topo-membrane">IFLTGAF</span><span class="topo-outside">GTIASGPFWTRGWPEWWGWWLDIPFWS</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>34</td>
      <td>1</td>
      <td>33</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>52</td>
      <td>34</td>
      <td>51</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>53</td>
      <td>89</td>
      <td>52</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>106</td>
      <td>89</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>117</td>
      <td>106</td>
      <td>116</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>135</td>
      <td>117</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>173</td>
      <td>135</td>
      <td>172</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>194</td>
      <td>173</td>
      <td>193</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>195</td>
      <td>230</td>
      <td>194</td>
      <td>229</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>247</td>
      <td>230</td>
      <td>246</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>248</td>
      <td>274</td>
      <td>247</td>
      <td>273</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2wjn">2WJN</a> — Chain M (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">ADYQTIYTQIQARGPHITVSGEWGDNDRVGKPFYSYWLGKIGDAQIGPI</span><span class="topo-membrane">YLGASGIAAFAFGSTAI</span><span class="topo-outside">LIILFNMAAEVHFDPLQFFRQFFWLGLYPPKAQYGMGIPPLHDGGWWLMAGL</span><span class="topo-membrane">F</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MTLSLGSWWIRVYSR</span><span class="topo-inside">ARALGLGT</span><span class="topo-membrane">HIAWNFAAAIFFVLC</span><span class="topo-outside">IGCIHPTLVGSWSEGVPFGIWPHIDWLTAFSIRYGNFYYCP</span><span class="topo-membrane">WHGFSIGFAYGCGLLFAAHGA</span><span class="topo-inside">TILAVARFGGDREIEQITDR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320    </span>
<span class="topo-line"><span class="topo-inside">GTAVERAALFWRWTIGFNATIESV</span><span class="topo-membrane">HRWGWFFSLMVMVSASVG</span><span class="topo-outside">ILLTGTFVDNWYLWCVKHGAAPDYPAYLPATPDPASLPGAPK</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>50</td>
      <td>1</td>
      <td>49</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>67</td>
      <td>50</td>
      <td>66</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>68</td>
      <td>119</td>
      <td>67</td>
      <td>118</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>120</td>
      <td>135</td>
      <td>119</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>143</td>
      <td>135</td>
      <td>142</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>144</td>
      <td>158</td>
      <td>143</td>
      <td>157</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>159</td>
      <td>199</td>
      <td>158</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>220</td>
      <td>199</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>264</td>
      <td>220</td>
      <td>263</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>265</td>
      <td>282</td>
      <td>264</td>
      <td>281</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>283</td>
      <td>324</td>
      <td>282</td>
      <td>323</td>
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

### Covalently bound diacylglycerol on cytochrome c subunit

A [Diacylglycerol](/xray-mp-wiki/reagents/lipids/diacylglycerol/) molecule is covalently attached to the N-terminal cysteine of the tetraheme cytochrome c subunit through a thioether bond. This prokaryotic posttranslational modification facilitates association of the cytochrome c subunit to the membrane and assists organization of quaternary structure. One fatty acid tail sits in a well-defined groove interacting with the M-branch accessory [Bacteriochlorophyll](/xray-mp-wiki/reagents/cofactors/bacteriochlorophyll/) by van der Waals forces; the other points perpendicular to the membrane plane and is weaker in electron density.

### Monoolein displaces ubiquinone at the QB binding site

The mobile [Ubiquinone](/xray-mp-wiki/reagents/cofactors/ubiquinone/) (QB) at the secondary quinone binding site appears to be displaced by a [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) molecule from the [Lipidic Sponge Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-sponge-phase-crystallization/) medium. Hydrogen bonds between the [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) hydroxyl groups and surrounding amino acids (Asn-L213, Glu-L212, His-L190, Leu-L193, Phe-L216, Ser-L223) are well satisfied. Time-resolved absorption spectroscopy on RC_sph LSP-grown crystals showed reduced QB occupancy (20 ± 10%) compared to detergent solution (50 ± 10%), consistent with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) competition.

### 36 Å continuous electron density feature at H- and M-subunit interface

A 36 Å long continuous electron density feature was observed at the interface of transmembrane helices of the H- and M-subunits, stretching across the entire membrane bilayer. This feature is longer than an [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) molecule and exceeds the length of membrane fatty acids in their fully extended conformation (~20 Å). It likely arises from an unidentified lipid molecule that is approximately perpendicular to the membrane plane.

### Radiation sensitivity of the thioether bond

The thioether bond connecting [Diacylglycerol](/xray-mp-wiki/reagents/lipids/diacylglycerol/) to the N-terminal cysteine of the cytochrome c subunit is sensitive to radiation damage. A high-dose data set (PDB 2WJN) showed reduced occupancy of the sulfur atom and lipid moiety, with negative Fo-Fc electron density appearing on the sulfur atom and the 2Fo-Fc electron density of the thioether bond no longer continuous at the same sigma level. This is consistent with specific radiation damage preferentially affecting bonds involving heavier atoms.

### Type I crystal packing without membrane-plane crystal contacts

LSP-grown RC_vir crystals belong to space group P2(1)2(1)2 with one molecule per asymmetric unit. Molecules are arranged in stacked antiparallel planes. Unlike LCP-grown RC_sph crystals where a bound [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) headgroup establishes strong lateral crystal contacts, no crystal contacts within the membrane plane are observed in the RC_vir [LSP](/xray-mp-wiki/concepts/membrane-mimetics/lipidic-sponge-phase/) structure. The hydrophobic slab has a thickness of 34 Å, accounting for approximately 39% of the crystal volume.


## Cross-References

- <a href="/xray-mp-wiki/concepts/membrane-mimetics/lipidic-sponge-phase/">LSP</a> — Related biological concept
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/type-i-crystal-packing/">Type I Crystal Packing</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-sponge-phase-crystallization/">Lipidic Sponge Phase Crystallization</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/photosynthesis/photosystem-ii/">Photosystem II</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> — Buffer component used in purification or crystallization
- <a href="/xray-mp-wiki/reagents/buffers/sodium-acetate/">Sodium Acetate</a> — Buffer component used in purification or crystallization
- <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">Sodium Phosphate</a> — Buffer component used in purification or crystallization
- <a href="/xray-mp-wiki/reagents/cofactors/bacteriochlorophyll/">Bacteriochlorophyll</a> — Related ligand or cofactor
- <a href="/xray-mp-wiki/reagents/cofactors/ubiquinone/">Ubiquinone</a> — Related ligand or cofactor
