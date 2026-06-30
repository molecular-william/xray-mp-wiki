---
title: "PsbA2-PSII dimer from Thermosynechococcus elongatus"
created: 2026-05-27
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jbc.2022.102668]
verified: false
---

# PsbA2-PSII dimer from Thermosynechococcus elongatus

## Overview

The [Photosystem II](/xray-mp-wiki/proteins/photosynthesis/photosystem-ii/) (PSII) dimer from the thermophilic cyanobacterium Thermosynechococcus elongatus expressing only the psbA2 gene, which encodes the D1-2 variant (PsbA2). This structure was solved to reveal how the D1-2 isoform differs from the canonical D1-1 (PsbA1) and the stress-induced D1-3 (PsbA3) in terms of hydrogen bonding networks around the pheophytin cofactor, water/proton channels near the oxygen-evolving complex, and the QB binding site. The PsbA2 variant is activated under microaerobic conditions and shows altered S-state transition kinetics.

## Publications

### doi/10.1016##j.jbc.2022.102668

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a></td>
      <td>1.90 A</td>
      <td>P212121</td>
      <td>PSII dimer expressing only psbA2 gene (pABA2 strain, lacking psbA1 and psbA3)</td>
      <td>Chlorophyll a, pheophytin a, <a href="/xray-mp-wiki/reagents/ligands/plastoquinone/">Plastoquinone</a>, <a href="/xray-mp-wiki/reagents/ligands/heme/">HEME</a>, nonheme <a href="/xray-mp-wiki/reagents/additives/iron/">IRON</a>, Mn4CaO5 cluster, bicarbonate, chloride ions, <a href="/xray-mp-wiki/reagents/lipids/sulfoquinovosyl-diacylglycerol/">SQDG</a>, DGDG, <a href="/xray-mp-wiki/reagents/lipids/monogalactosyl-diacylglycerol/">MGDG</a>, carotenoids</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Thermosynechococcus elongatus (thermophilic cyanobacterium)
- **Construct**: PSII dimer from mutant strain lacking psbA1 and psbA3 genes, expressing only psbA2 gene

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
      <td>Cell growth and harvest</td>
      <td>Cultivation of psbA2-only mutant strain</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Cells cultured with 20 umol photons m-2 s-1 red LED illumination, then diluted and grown with increasing light intensity over 7-8 days.</td>
    </tr>
    <tr>
      <td>Thylakoid membrane isolation</td>
      <td>Cell disruption and membrane isolation</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Cells harvested and broken to isolate thylakoid membranes.</td>
    </tr>
    <tr>
      <td>Thylakoid solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>-- + 0.25% lauryl dimethylamine-n-oxide (<a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a>)</td>
      <td>Solubilization of thylakoid membranes with <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a>.</td>
    </tr>
    <tr>
      <td>Secondary solubilization</td>
      <td>Detergent exchange</td>
      <td>--</td>
      <td>-- + n-dodecyl-beta-D-maltoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Exchange to <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> for PSII dimer stability.</td>
    </tr>
    <tr>
      <td>PSII dimer purification</td>
      <td>Anion-exchange chromatography</td>
      <td>Anion-exchange column</td>
      <td>-- + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Purification of PSII dimers using anion-exchange column chromatography.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Oil batch method</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>PsbA2-PSII dimer</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Buffer conditions as reported previously</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>100 K (cryocooled)</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Crystals grew to approximately 1.0 x 0.4 x 0.2 mm</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Cryoprotectant solution with buffer conditions as reported previously; flash-frozen in nitrogen gas stream at 100 K</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals diffracted to 1.90 A resolution. Space group P212121. Unit cell dimensions a=122.1, b=228.2, c=286.7 A. Data collected at SPring-8 BL41XU with 1.0 A wavelength.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain A (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTTVLQRRQT</span><span class="topo-inside">ANLWERFCDWITSTENR</span><span class="topo-membrane">LYIGWFGVIMIPTLLAATI</span><span class="topo-outside">CFVIAFIAAPPVDIDGIREPVSGSLLYGNNIITAAVVPSSNAIGLHLYPIWDAASLDEWLYNGGPYQLIIFH</span><span class="topo-membrane">FL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">IGIFCYMGREWEL</span><span class="topo-inside">SYRLGMRP</span><span class="topo-membrane">WIPVAFSAPVAAAT</span><span class="topo-outside">AVLLIYPIGQGSFSDGLMLGISGTFNFMIVFQAEHNILMHPF</span><span class="topo-membrane">HMLGVAGVFGGALFAAMHGS</span><span class="topo-inside">LVTSSLIRETTETESTNYGYKFG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">QEEETYNIVAAHGYFGRLIFQYASFNNSRSLH</span><span class="topo-membrane">FFLAAWPVVGIWFAAL</span><span class="topo-outside">GISTMAFNLNGFNFNHSVVDAQGNVINTWADIINRANIGIEVMHERNAHNFPLDLA</span><span class="topo-unknown">SGELAPVAMIAPSIEA</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>1</td>
      <td>10</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>27</td>
      <td>11</td>
      <td>27</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>28</td>
      <td>46</td>
      <td>28</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>118</td>
      <td>47</td>
      <td>118</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>133</td>
      <td>119</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>141</td>
      <td>134</td>
      <td>141</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>155</td>
      <td>142</td>
      <td>155</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>156</td>
      <td>197</td>
      <td>156</td>
      <td>197</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>198</td>
      <td>217</td>
      <td>198</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>272</td>
      <td>218</td>
      <td>272</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>273</td>
      <td>288</td>
      <td>273</td>
      <td>288</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>289</td>
      <td>344</td>
      <td>289</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>360</td>
      <td>345</td>
      <td>360</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">GLPWYRVHTVLINDPGRL</span><span class="topo-membrane">IAAHLMHTALVAGWA</span><span class="topo-outside">GSMALYELATFDPSDPVLNPMWRQGMFVLPFMARLGVTGSWSGWSITGETGIDPGFWSFEGVALA</span><span class="topo-membrane">HIVLSGLLFLAACWHW</span><span class="topo-inside">VYWDL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ELFRDPRTGEPALDLPKM</span><span class="topo-membrane">FGIHLFLAGLLCFGF</span><span class="topo-outside">GAFHLTGLFGPGMWVSDPYGLTGSVQPVAPEWGPDGFNPYNPGGVVAH</span><span class="topo-membrane">HIAAGIVGIIAGLFHI</span><span class="topo-inside">LVRPPQRLYKALRMGNIE</span><span class="topo-membrane">TVLSS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">SIAAVFFAAFV</span><span class="topo-outside">VAGTMWYGSATTPIELFGPTRYQWDSSYFQQEINRRVQASLASGATLEEAWSAIPEKLAFYDYIGNNPAKGGLFRTGPMNKGDGIAQAWKGHAVFRNKEGEELFVRRMP</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">AFFESFPVILTDKNGVVKADIPFRRAESKYSFEQQGVTVSFYGGELNGQTFTDPPTVKSYARKAIFGEIFEFDTETLNSDGIFRTSPRGWFTFAH</span><span class="topo-membrane">AVFALLFFFGHIWHGA</span><span class="topo-inside">RTLFRDVFS</span></span>
<span class="topo-ruler">       490       500       510</span>
<span class="topo-line"><span class="topo-inside">GIDPELSPEQVEWGFYQKVGDVTTRR</span><span class="topo-unknown">KEAV</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>19</td>
      <td>2</td>
      <td>19</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>34</td>
      <td>20</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>99</td>
      <td>35</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>100</td>
      <td>115</td>
      <td>100</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>138</td>
      <td>116</td>
      <td>138</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>139</td>
      <td>153</td>
      <td>139</td>
      <td>153</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>154</td>
      <td>201</td>
      <td>154</td>
      <td>201</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>217</td>
      <td>202</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>235</td>
      <td>218</td>
      <td>235</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>251</td>
      <td>236</td>
      <td>251</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>252</td>
      <td>455</td>
      <td>252</td>
      <td>455</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>456</td>
      <td>471</td>
      <td>456</td>
      <td>471</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>472</td>
      <td>506</td>
      <td>472</td>
      <td>506</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>507</td>
      <td>510</td>
      <td>507</td>
      <td>510</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MVTLSSNSIF</span><span class="topo-inside">ATNRDQESSGFAWWAGNARLINLSGKL</span><span class="topo-membrane">LGAHVAHAGLIVFWAGA</span><span class="topo-outside">MTLFELAHFIPEKPMYEQGLILIPHIATLGWGVGPGGEVVDTFPFFVVGVV</span><span class="topo-membrane">HLISSAVLGFGGVYH</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">A</span><span class="topo-inside">IRGPETLEEYSSFFGYDWKDKNKM</span><span class="topo-membrane">TTILGFHLIVLGIGAL</span><span class="topo-outside">LLVAKAMFFGGLYDTWAPGGGDVRVITNPTLDPRVIFGYLLKSPFGGEGWIVSVNNLEDVVGGHIW</span><span class="topo-membrane">IGLICIAGGIWHI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LT</span><span class="topo-inside">TPFGWARRAFIWSGE</span><span class="topo-membrane">AYLSYSLGALSMMGF</span><span class="topo-outside">IATCFVWFNNTVYPSEFYGPTGPEASQAQAMTFLIRDQKLGANVGSAQGPTGLGKYLMRSPTGEIIFGGETMRFWDFRGPWLEPLRGP</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460 </span>
<span class="topo-line"><span class="topo-outside">NGLDLNKIKNDIQPWQERRAAEYMTHAPLGSLNSVGGVATEINSVNFVSPRSWLATSH</span><span class="topo-membrane">FVLAFFFLVGHLWHAG</span><span class="topo-inside">RARAAAAGFEKGIDRESEPVLSMPSLD</span></span>
<details class="topo-details"><summary>Topology coordinates (14 regions)</summary>
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
      <td>13</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>37</td>
      <td>23</td>
      <td>49</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>50</td>
      <td>66</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>105</td>
      <td>67</td>
      <td>117</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>121</td>
      <td>118</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>122</td>
      <td>145</td>
      <td>134</td>
      <td>157</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>146</td>
      <td>161</td>
      <td>158</td>
      <td>173</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>162</td>
      <td>227</td>
      <td>174</td>
      <td>239</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>242</td>
      <td>240</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>257</td>
      <td>255</td>
      <td>269</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>272</td>
      <td>270</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>418</td>
      <td>285</td>
      <td>430</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>419</td>
      <td>434</td>
      <td>431</td>
      <td>446</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>435</td>
      <td>461</td>
      <td>447</td>
      <td>473</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain D (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTIAIGRAPA</span><span class="topo-inside">ERGWFDILDDWLKRDRFVFV</span><span class="topo-membrane">GWSGILLFPCAYLALGGWLT</span><span class="topo-outside">GTTFVTSWYTHGLASSYLEGCNFLTVAVSTPANSMGHSLLLLWGPEAQGDFTRWCQLGGLWTF</span><span class="topo-membrane">IALHGAF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GLIGFMLRQF</span><span class="topo-inside">EIARLVGVRP</span><span class="topo-membrane">YNAIAFSAPIAVFVS</span><span class="topo-outside">VFLIYPLGQSSWFFAPSFGVAAIFRFLLFFQGFHNWTLNPFHM</span><span class="topo-membrane">MGVAGVLGGALLCAIHGAT</span><span class="topo-inside">VENTLFQDGEGASTFRAFNPTQA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350  </span>
<span class="topo-line"><span class="topo-inside">EETYSMVTANRFWSQIFGIAFSNKRWL</span><span class="topo-membrane">HFFMLFVPVTGLWMSAI</span><span class="topo-outside">GVVGLALNLRSYDFISQEIRAAEDPEFETFYTKNLLLNEGIRAWMAPQDQPHENFVFPEEVLPRGNAL</span></span>
<details class="topo-details"><summary>Topology coordinates (12 regions)</summary>
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
      <td>1</td>
      <td>10</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>30</td>
      <td>11</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>50</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>113</td>
      <td>51</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>130</td>
      <td>114</td>
      <td>130</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>131</td>
      <td>140</td>
      <td>131</td>
      <td>140</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>155</td>
      <td>141</td>
      <td>155</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>156</td>
      <td>198</td>
      <td>156</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>217</td>
      <td>199</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>267</td>
      <td>218</td>
      <td>267</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>268</td>
      <td>284</td>
      <td>268</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>285</td>
      <td>352</td>
      <td>285</td>
      <td>352</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain E (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80    </span>
<span class="topo-line"><span class="topo-unknown">MA</span><span class="topo-inside">GTTGERPFSDIITSVRY</span><span class="topo-membrane">WVIHSITIPALFIAG</span><span class="topo-outside">WLFVSTGLAYDVFGTPRPDSYYAQEQRSIPLVTDRFEAKQQVETFLEQ</span><span class="topo-unknown">LK</span></span>
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
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>19</td>
      <td>3</td>
      <td>19</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>34</td>
      <td>20</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>82</td>
      <td>35</td>
      <td>82</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>84</td>
      <td>83</td>
      <td>84</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain F (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40     </span>
<span class="topo-line"><span class="topo-unknown">MTSNTPNQEPV</span><span class="topo-inside">SYPIFTV</span><span class="topo-membrane">RWVAVHTLAVPTIFFLG</span><span class="topo-outside">AIAAMQFIQR</span></span>
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
      <td>11</td>
      <td>1</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>18</td>
      <td>12</td>
      <td>18</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>35</td>
      <td>19</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>45</td>
      <td>36</td>
      <td>45</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain H (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60      </span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">ARRTWLGDILRPLNSEYGKVAPGWGTT</span><span class="topo-membrane">PLMAVFMGLFLVFLL</span><span class="topo-outside">IILEIYNSTLILDGVNVSWKALG</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>28</td>
      <td>2</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>43</td>
      <td>29</td>
      <td>43</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>44</td>
      <td>66</td>
      <td>44</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain I (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        </span>
<span class="topo-line"><span class="topo-outside">METLKIT</span><span class="topo-membrane">VYIVVTFFVLLFVFGFLS</span><span class="topo-inside">GDPARNPKRKDL</span><span class="topo-unknown">E</span></span>
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
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>25</td>
      <td>8</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>26</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain J (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40</span>
<span class="topo-line"><span class="topo-unknown">MMSE</span><span class="topo-inside">GGRIPLW</span><span class="topo-membrane">IVATVAGMGVIVIVG</span><span class="topo-outside">LFFYGAYAGLGSSL</span></span>
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
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>11</td>
      <td>5</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>26</td>
      <td>12</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>40</td>
      <td>27</td>
      <td>40</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain K (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40      </span>
<span class="topo-line"><span class="topo-unknown">MIDALVLVA</span><span class="topo-outside">KLPEAYAIFDPLVDV</span><span class="topo-membrane">LPVIPVLFLALAFVWQA</span><span class="topo-inside">AVGFR</span></span>
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
      <td>9</td>
      <td>1</td>
      <td>9</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>24</td>
      <td>10</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>41</td>
      <td>25</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>46</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain L (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30       </span>
<span class="topo-line"><span class="topo-inside">MEPNPNRQPVELNR</span><span class="topo-membrane">TSLYLGLLLILVLALL</span><span class="topo-outside">FSSYFFN</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>14</td>
      <td>1</td>
      <td>14</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>30</td>
      <td>15</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>37</td>
      <td>31</td>
      <td>37</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain M (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30      </span>
<span class="topo-line"><span class="topo-outside">MEVNQLGLIAT</span><span class="topo-membrane">ALFVLVPSVFLIILYV</span><span class="topo-inside">QTESQQK</span><span class="topo-unknown">SS</span></span>
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
      <td>11</td>
      <td>1</td>
      <td>11</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>27</td>
      <td>12</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>34</td>
      <td>28</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>36</td>
      <td>35</td>
      <td>36</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain O (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKYRILMATLLAVCLGIFSLSAPAFAAKQ</span><span class="topo-outside">TLTYDDIVGTGLANKCPTLDDTARGAYPIDSSQTYRIARLCLQPTTFLVKEEPKNKRQEAEFVPTKLVTRETTSLDQIQGELKVNSDGSLT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FVEEDGIDFQPVTVQMAGGERIPLLFTVKNLVASTQPNVTSITTSTDFKGEFNVPSYRTANFLDPKGRGLASGYDSAIALPQAKEEELARANVKRFSLTKGQISLNVAKVDGRTGEIAGT</span></span>
<span class="topo-ruler">       250       260       270  </span>
<span class="topo-line"><span class="topo-outside">FESEQLSDDDMGAHEPHEVKIQGVFYASIEPA</span></span>
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
      <td>29</td>
      <td>-25</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>30</td>
      <td>272</td>
      <td>4</td>
      <td>246</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain T (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30  </span>
<span class="topo-line"><span class="topo-outside">METITYVF</span><span class="topo-membrane">IFACIIALFFFAIFFR</span><span class="topo-inside">EPPRIT</span><span class="topo-unknown">KK</span></span>
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
      <td>8</td>
      <td>1</td>
      <td>8</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>24</td>
      <td>9</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>30</td>
      <td>25</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>32</td>
      <td>31</td>
      <td>32</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain U (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQRLGRWLALAYFVGVSLLGWINWSAPTLAATASTE</span><span class="topo-outside">EELVNVVDEKLGTAYGEKIDLNNTNIAAFIQYRGLYPTLAKLIVKNAPYESVEDVLNIPGLTERQKQILRENLEHFTVTEVETA</span></span>
<span class="topo-ruler">       130    </span>
<span class="topo-line"><span class="topo-outside">LVEGGDRYNNGLYK</span></span>
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
      <td>36</td>
      <td>-29</td>
      <td>6</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>37</td>
      <td>134</td>
      <td>7</td>
      <td>104</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain V (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MLKKCVWLAVALCLCLWQFTMGTALA</span><span class="topo-outside">AELTPEVLTVPLNSEGKTITLTEKQYLEGKRLFQYACASCHVGGITKTNPSLDLRTETLALATPPRDNIEGLVDYMKNPTTYDGEQEIAEVHPS</span></span>
<span class="topo-ruler">       130       140       150       160   </span>
<span class="topo-line"><span class="topo-outside">LRSADIFPKMRNLTEKDLVAIAGHILVEPKILGDKWGGGKVYY</span></span>
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
      <td>26</td>
      <td>-25</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>27</td>
      <td>163</td>
      <td>1</td>
      <td>137</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain Y (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40      </span>
<span class="topo-line"><span class="topo-unknown">MGIFNGIIEFLSNINF</span><span class="topo-outside">EVIAQL</span><span class="topo-membrane">TMIAMIGIAGPMIIFL</span><span class="topo-inside">LAVRRGNL</span></span>
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
      <td>16</td>
      <td>1</td>
      <td>16</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>17</td>
      <td>22</td>
      <td>17</td>
      <td>22</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>38</td>
      <td>23</td>
      <td>38</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>46</td>
      <td>39</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain X (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40 </span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">TITPSLKGFF</span><span class="topo-membrane">IGLLSGAVVLGLTFAVL</span><span class="topo-inside">IAISQIDKVQRSL</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>11</td>
      <td>2</td>
      <td>11</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>28</td>
      <td>12</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>41</td>
      <td>29</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain Z (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60  </span>
<span class="topo-line"><span class="topo-outside">MTILFQL</span><span class="topo-membrane">ALAALVILSFVMVIGVPV</span><span class="topo-inside">AYASPQDWDRSKQL</span><span class="topo-membrane">IFLGSGLWIALVLVV</span><span class="topo-outside">GVLNFFVV</span></span>
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
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>25</td>
      <td>8</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>39</td>
      <td>26</td>
      <td>39</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>54</td>
      <td>40</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>62</td>
      <td>55</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain a (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTTVLQRR</span><span class="topo-inside">QTANLWERFCDWITSTENR</span><span class="topo-membrane">LYIGWFGVIMIPTLLAATI</span><span class="topo-outside">CFVIAFIAAPPVDIDGIREPVSGSLLYGNNIITAAVVPSSNAIGLHLYPIWDAASLDEWLYNGGPYQLIIFH</span><span class="topo-membrane">FL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">IGIFCYMGREWEL</span><span class="topo-inside">SYRLGMRP</span><span class="topo-membrane">WIPVAFSAPVAAAT</span><span class="topo-outside">AVLLIYPIGQGSFSDGLMLGISGTFNFMIVFQAEHNILMHPFHM</span><span class="topo-membrane">LGVAGVFGGALFAAMHGS</span><span class="topo-inside">LVTSSLIRETTETESTNYGYKFG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">QEEETYNIVAAHGYFGRLIFQYASFNNSRSLH</span><span class="topo-membrane">FFLAAWPVVGIWFAAL</span><span class="topo-outside">GISTMAFNLNGFNFNHSVVDAQGNVINTWADIINRANIGIEVMHERNAHNFPLDLA</span><span class="topo-unknown">SGELAPVAMIAPSIEA</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>1</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>27</td>
      <td>9</td>
      <td>27</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>28</td>
      <td>46</td>
      <td>28</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>118</td>
      <td>47</td>
      <td>118</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>133</td>
      <td>119</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>141</td>
      <td>134</td>
      <td>141</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>155</td>
      <td>142</td>
      <td>155</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>156</td>
      <td>199</td>
      <td>156</td>
      <td>199</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>217</td>
      <td>200</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>272</td>
      <td>218</td>
      <td>272</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>273</td>
      <td>288</td>
      <td>273</td>
      <td>288</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>289</td>
      <td>344</td>
      <td>289</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>360</td>
      <td>345</td>
      <td>360</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain b (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">GLPWYRVHTVLINDPGRL</span><span class="topo-membrane">IAAHLMHTALVAGWA</span><span class="topo-outside">GSMALYELATFDPSDPVLNPMWRQGMFVLPFMARLGVTGSWSGWSITGETGIDPGFWSFEGVALA</span><span class="topo-membrane">HIVLSGLLFLAACWHW</span><span class="topo-inside">VYWDL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ELFRDPRTGEPALDLPKM</span><span class="topo-membrane">FGIHLFLAGLLCFGF</span><span class="topo-outside">GAFHLTGLFGPGMWVSDPYGLTGSVQPVAPEWGPDGFNPYNPGGVVAHH</span><span class="topo-membrane">IAAGIVGIIAGLFHI</span><span class="topo-inside">LVRPPQRLYKALRMGNIE</span><span class="topo-membrane">TVLSS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">SIAAVFFAAFV</span><span class="topo-outside">VAGTMWYGSATTPIELFGPTRYQWDSSYFQQEINRRVQASLASGATLEEAWSAIPEKLAFYDYIGNNPAKGGLFRTGPMNKGDGIAQAWKGHAVFRNKEGEELFVRRMP</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">AFFESFPVILTDKNGVVKADIPFRRAESKYSFEQQGVTVSFYGGELNGQTFTDPPTVKSYARKAIFGEIFEFDTETLNSDGIFRTSPRGWFTFAH</span><span class="topo-membrane">AVFALLFFFGHIWHGA</span><span class="topo-inside">RTLFRDVFS</span></span>
<span class="topo-ruler">       490       500       510</span>
<span class="topo-line"><span class="topo-inside">GIDPELSPEQVEWGFYQKVGDVTTR</span><span class="topo-unknown">RKEAV</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>19</td>
      <td>2</td>
      <td>19</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>34</td>
      <td>20</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>99</td>
      <td>35</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>100</td>
      <td>115</td>
      <td>100</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>138</td>
      <td>116</td>
      <td>138</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>139</td>
      <td>153</td>
      <td>139</td>
      <td>153</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>154</td>
      <td>202</td>
      <td>154</td>
      <td>202</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>217</td>
      <td>203</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>235</td>
      <td>218</td>
      <td>235</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>251</td>
      <td>236</td>
      <td>251</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>252</td>
      <td>455</td>
      <td>252</td>
      <td>455</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>456</td>
      <td>471</td>
      <td>456</td>
      <td>471</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>472</td>
      <td>505</td>
      <td>472</td>
      <td>505</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>506</td>
      <td>510</td>
      <td>506</td>
      <td>510</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain c (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MVTLS</span><span class="topo-inside">SNSIFATNRDQESSGFAWWAGNARLINLSGKL</span><span class="topo-membrane">LGAHVAHAGLIVFWAGA</span><span class="topo-outside">MTLFELAHFIPEKPMYEQGLILIPHIATLGWGVGPGGEVVDTFPFFVVGVV</span><span class="topo-membrane">HLISSAVLGFGGVYH</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">A</span><span class="topo-inside">IRGPETLEEYSSFFGYDWKDKNKM</span><span class="topo-membrane">TTILGFHLIVLGIGAL</span><span class="topo-outside">LLVAKAMFFGGLYDTWAPGGGDVRVITNPTLDPRVIFGYLLKSPFGGEGWIVSVNNLEDVVGGHIW</span><span class="topo-membrane">IGLICIAGGIWHI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LT</span><span class="topo-inside">TPFGWARRAFIWSGE</span><span class="topo-membrane">AYLSYSLGALSMMGF</span><span class="topo-outside">IATCFVWFNNTVYPSEFYGPTGPEASQAQAMTFLIRDQKLGANVGSAQGPTGLGKYLMRSPTGEIIFGGETMRFWDFRGPWLEPLRGP</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460 </span>
<span class="topo-line"><span class="topo-outside">NGLDLNKIKNDIQPWQERRAAEYMTHAPLGSLNSVGGVATEINSVNFVSPRSWLATSH</span><span class="topo-membrane">FVLAFFFLVGHLWHAG</span><span class="topo-inside">RARAAAAGFEKGIDRESEPVLSMPSLD</span></span>
<details class="topo-details"><summary>Topology coordinates (14 regions)</summary>
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
      <td>13</td>
      <td>17</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>37</td>
      <td>18</td>
      <td>49</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>50</td>
      <td>66</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>105</td>
      <td>67</td>
      <td>117</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>121</td>
      <td>118</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>122</td>
      <td>145</td>
      <td>134</td>
      <td>157</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>146</td>
      <td>161</td>
      <td>158</td>
      <td>173</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>162</td>
      <td>227</td>
      <td>174</td>
      <td>239</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>242</td>
      <td>240</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>257</td>
      <td>255</td>
      <td>269</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>272</td>
      <td>270</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>418</td>
      <td>285</td>
      <td>430</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>419</td>
      <td>434</td>
      <td>431</td>
      <td>446</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>435</td>
      <td>461</td>
      <td>447</td>
      <td>473</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain d (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTIAIGRAPA</span><span class="topo-inside">ERGWFDILDDWLKRDRFVFV</span><span class="topo-membrane">GWSGILLFPCAYLALGGWL</span><span class="topo-outside">TGTTFVTSWYTHGLASSYLEGCNFLTVAVSTPANSMGHSLLLLWGPEAQGDFTRWCQLGGLWTFI</span><span class="topo-membrane">ALHGAF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GLIGFMLRQF</span><span class="topo-inside">EIARLVGVRP</span><span class="topo-membrane">YNAIAFSAPIAVFVS</span><span class="topo-outside">VFLIYPLGQSSWFFAPSFGVAAIFRFLLFFQGFHNWTLNPFHM</span><span class="topo-membrane">MGVAGVLGGALLCAIHGAT</span><span class="topo-inside">VENTLFQDGEGASTFRAFNPTQA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350  </span>
<span class="topo-line"><span class="topo-inside">EETYSMVTANRFWSQIFGIAFSNKRWL</span><span class="topo-membrane">HFFMLFVPVTGLWMSAI</span><span class="topo-outside">GVVGLALNLRSYDFISQEIRAAEDPEFETFYTKNLLLNEGIRAWMAPQDQPHENFVFPEEVLPRGNAL</span></span>
<details class="topo-details"><summary>Topology coordinates (12 regions)</summary>
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
      <td>1</td>
      <td>10</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>30</td>
      <td>11</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>49</td>
      <td>31</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>114</td>
      <td>50</td>
      <td>114</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>130</td>
      <td>115</td>
      <td>130</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>131</td>
      <td>140</td>
      <td>131</td>
      <td>140</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>155</td>
      <td>141</td>
      <td>155</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>156</td>
      <td>198</td>
      <td>156</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>217</td>
      <td>199</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>267</td>
      <td>218</td>
      <td>267</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>268</td>
      <td>284</td>
      <td>268</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>285</td>
      <td>352</td>
      <td>285</td>
      <td>352</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain e (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80    </span>
<span class="topo-line"><span class="topo-unknown">MAGTT</span><span class="topo-inside">GERPFSDIITSVRY</span><span class="topo-membrane">WVIHSITIPALFIAG</span><span class="topo-outside">WLFVSTGLAYDVFGTPRPDSYYAQEQRSIPLVTDRFEAKQQVETFLEQLK</span></span>
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
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>19</td>
      <td>6</td>
      <td>19</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>34</td>
      <td>20</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>84</td>
      <td>35</td>
      <td>84</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain f (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40     </span>
<span class="topo-line"><span class="topo-unknown">MTSNTPNQEPVSY</span><span class="topo-inside">PIFTV</span><span class="topo-membrane">RWVAVHTLAVPTIFFLG</span><span class="topo-outside">AIAAMQFIQR</span></span>
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
      <td>13</td>
      <td>1</td>
      <td>13</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>14</td>
      <td>18</td>
      <td>14</td>
      <td>18</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>35</td>
      <td>19</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>45</td>
      <td>36</td>
      <td>45</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain h (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60      </span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">ARRTWLGDILRPLNSEYGKVAPGWGT</span><span class="topo-membrane">TPLMAVFMGLFLVFLL</span><span class="topo-outside">IILEIYNSTLILDGVNVSWKALG</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>27</td>
      <td>2</td>
      <td>27</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>28</td>
      <td>43</td>
      <td>28</td>
      <td>43</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>44</td>
      <td>66</td>
      <td>44</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain i (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        </span>
<span class="topo-line"><span class="topo-outside">METLKIT</span><span class="topo-membrane">VYIVVTFFVLLFVFGFLS</span><span class="topo-inside">GDPARNPKRKDL</span><span class="topo-unknown">E</span></span>
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
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>25</td>
      <td>8</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>26</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain j (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">MSEGGRIPLW</span><span class="topo-membrane">IVATVAGMGVIVIVG</span><span class="topo-outside">LFFYGAYAGLGSSL</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>11</td>
      <td>2</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>26</td>
      <td>12</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>40</td>
      <td>27</td>
      <td>40</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain k (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40      </span>
<span class="topo-line"><span class="topo-unknown">MIDALVLVA</span><span class="topo-outside">KLPEAYAIFDPLVDV</span><span class="topo-membrane">LPVIPVLFLALAFVWQA</span><span class="topo-inside">AVGFR</span></span>
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
      <td>9</td>
      <td>1</td>
      <td>9</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>24</td>
      <td>10</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>41</td>
      <td>25</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>46</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain l (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30       </span>
<span class="topo-line"><span class="topo-inside">MEPNPNRQPVELNR</span><span class="topo-membrane">TSLYLGLLLILVLALL</span><span class="topo-outside">FSSYFFN</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>14</td>
      <td>1</td>
      <td>14</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>30</td>
      <td>15</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>37</td>
      <td>31</td>
      <td>37</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain m (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30      </span>
<span class="topo-line"><span class="topo-outside">MEVNQLGLIAT</span><span class="topo-membrane">ALFVLVPSVFLIILYV</span><span class="topo-inside">QTESQQK</span><span class="topo-unknown">SS</span></span>
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
      <td>11</td>
      <td>1</td>
      <td>11</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>27</td>
      <td>12</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>34</td>
      <td>28</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>36</td>
      <td>35</td>
      <td>36</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain o (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKYRILMATLLAVCLGIFSLSAPAFAAKQ</span><span class="topo-outside">TLTYDDIVGTGLANKCPTLDDTARGAYPIDSSQTYRIARLCLQPTTFLVKEEPKNKRQEAEFVPTKLVTRETTSLDQIQGELKVNSDGSLT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FVEEDGIDFQPVTVQMAGGERIPLLFTVKNLVASTQPNVTSITTSTDFKGEFNVPSYRTANFLDPKGRGLASGYDSAIALPQAKEEELARANVKRFSLTKGQISLNVAKVDGRTGEIAGT</span></span>
<span class="topo-ruler">       250       260       270  </span>
<span class="topo-line"><span class="topo-outside">FESEQLSDDDMGAHEPHEVKIQGVFYASIEPA</span></span>
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
      <td>29</td>
      <td>-25</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>30</td>
      <td>272</td>
      <td>4</td>
      <td>246</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain t (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30  </span>
<span class="topo-line"><span class="topo-outside">METITYVF</span><span class="topo-membrane">IFACIIALFFFAIFFR</span><span class="topo-inside">EPPRIT</span><span class="topo-unknown">KK</span></span>
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
      <td>8</td>
      <td>1</td>
      <td>8</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>24</td>
      <td>9</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>30</td>
      <td>25</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>32</td>
      <td>31</td>
      <td>32</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain u (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQRLGRWLALAYFVGVSLLGWINWSAPTLAATASTEE</span><span class="topo-outside">ELVNVVDEKLGTAYGEKIDLNNTNIAAFIQYRGLYPTLAKLIVKNAPYESVEDVLNIPGLTERQKQILRENLEHFTVTEVETA</span></span>
<span class="topo-ruler">       130    </span>
<span class="topo-line"><span class="topo-outside">LVEGGDRYNNGLYK</span></span>
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
      <td>37</td>
      <td>-29</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>38</td>
      <td>134</td>
      <td>8</td>
      <td>104</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain v (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MLKKCVWLAVALCLCLWQFTMGTALA</span><span class="topo-outside">AELTPEVLTVPLNSEGKTITLTEKQYLEGKRLFQYACASCHVGGITKTNPSLDLRTETLALATPPRDNIEGLVDYMKNPTTYDGEQEIAEVHPS</span></span>
<span class="topo-ruler">       130       140       150       160   </span>
<span class="topo-line"><span class="topo-outside">LRSADIFPKMRNLTEKDLVAIAGHILVEPKILGDKWGGGKVYY</span></span>
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
      <td>26</td>
      <td>-25</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>27</td>
      <td>163</td>
      <td>1</td>
      <td>137</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain y (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40      </span>
<span class="topo-line"><span class="topo-unknown">MGIFNGIIEFLSNINF</span><span class="topo-outside">EVIAQL</span><span class="topo-membrane">TMIAMIGIAGPMIIFL</span><span class="topo-inside">LAVRRGNL</span></span>
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
      <td>16</td>
      <td>1</td>
      <td>16</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>17</td>
      <td>22</td>
      <td>17</td>
      <td>22</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>38</td>
      <td>23</td>
      <td>38</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>46</td>
      <td>39</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain x (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40 </span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">TITPSLKGFFIG</span><span class="topo-membrane">LLSGAVVLGLTFAVL</span><span class="topo-inside">IAISQIDKVQRS</span><span class="topo-unknown">L</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>13</td>
      <td>2</td>
      <td>13</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>28</td>
      <td>14</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>40</td>
      <td>29</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>41</td>
      <td>41</td>
      <td>41</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain z (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60  </span>
<span class="topo-line"><span class="topo-outside">MTILFQL</span><span class="topo-membrane">ALAALVILSFVMVIGVPV</span><span class="topo-inside">AYASPQDWDRSKQ</span><span class="topo-membrane">LIFLGSGLWIALVLVV</span><span class="topo-outside">GVLNFFVV</span></span>
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
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>25</td>
      <td>8</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>38</td>
      <td>26</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>54</td>
      <td>39</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>62</td>
      <td>55</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yq2">7YQ2</a> — Chain R (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40 </span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">DWRVLVV</span><span class="topo-membrane">LLPVLLAAGWAVRN</span><span class="topo-inside">ILPYAVKQVQKLL</span><span class="topo-unknown">QKAKAA</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>8</td>
      <td>2</td>
      <td>8</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>22</td>
      <td>9</td>
      <td>22</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>23</td>
      <td>35</td>
      <td>23</td>
      <td>35</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>41</td>
      <td>36</td>
      <td>41</td>
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

### Stronger hydrogen bond between PheoD1 and D1-E130

The replacement of D1-Gln130 with glutamate (D1-Q130E) in PsbA2 strengthens the hydrogen bond between PheoD1 and the 13(1)-keto group. This is consistent with FTIR spectroscopy measurements and partially explains the altered redox potential of PheoD1 observed in [PsbA3-PSII dimer from Thermosynechococcus elongatus](/xray-mp-wiki/proteins/photosynthesis/psba3-psii/) (increasing from -522 mV in PsbA1 to -505 mV). The hydrogen bond distance between the 13(1)-keto group of PheoD1 and D1-E130 was shortened in PsbA2 compared to PsbA1.

### Loss of hydrogen bond between PheoD1 and D1-F147 in PsbA2

In PsbA1 and PsbA3, D1-Tyr147 forms a hydrogen bond with the ester group of PheoD1. In PsbA2, this residue is replaced by phenylalanine (D1-Y147F), which loses this hydrogen bond, making PheoD1 in PsbA2 the most structurally unstable among the three D1 variants. This breakage may be necessary to avoid conformational changes of transmembrane helix C caused by the D1-Pro144 substitution (Pro in PsbA2 vs Cys in PsbA1/PsbA3), which disrupts the TMH C main chain and causes a flip of D1-F147.

### Narrowing of Cl-1 channel in PsbA2

The D1-Pro173 to methionine substitution (D1-P173M) in PsbA2 causes two water molecules (W568 and W572) in the Cl-1 channel to become invisible due to the larger side chain of methionine. The average diameter of the channel region around D1-173 is approximately 0.9 A narrower in PsbA2-PSII, with the narrowest region around 2.8 A. This may limit proton egress via Grotthus-type transfer, explaining the slower reduction of P680+ by TyrZ in the S2 and S3 states observed spectroscopically.


## Cross-References

- <a href="/xray-mp-wiki/proteins/photosynthesis/psi-lhci-chlamydomonas/">PSI-LHCI supercomplex from Chlamydomonas reinhardtii</a> — Another photosystem complex from photosynthetic organisms solved by X-ray crystallography
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">N-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent used for PSII dimer purification and stabilization
- <a href="/xray-mp-wiki/reagents/detergents/ldao/">Lauryl dimethylamine-n-oxide (LDAO)</a> — Initial solubilization detergent for thylakoid membranes
- <a href="/xray-mp-wiki/proteins/photosynthesis/photosystem-ii/">Photosystem II</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/photosynthesis/psba3-psii/">PsbA3-PSII dimer from Thermosynechococcus elongatus</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/iron/">IRON</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a> — Detergent used in purification or crystallization
- <a href="/xray-mp-wiki/reagents/ligands/heme/">HEME</a> — Related ligand or cofactor
- <a href="/xray-mp-wiki/reagents/ligands/plastoquinone/">Plastoquinone</a> — Related ligand or cofactor
- <a href="/xray-mp-wiki/reagents/lipids/monogalactosyl-diacylglycerol/">MGDG</a> — Additive used in purification or crystallization buffers
