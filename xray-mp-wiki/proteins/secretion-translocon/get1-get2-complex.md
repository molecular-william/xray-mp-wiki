---
title: "Get1/Get2 GET Insertase Complex"
created: 2026-06-16
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-023-42867-2]
verified: regex
uniprot_id: ['G0SFE0', 'O43681']
---

# Get1/Get2 GET Insertase Complex

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span> <span class="expr-badge expr-s-cerevisiae">S. cerevisiae</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/G0SFE0">UniProt: G0SFE0</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/O43681">UniProt: O43681</a>

<span class="expr-badge">Thermochaetoides thermophila DSM 1495</span>

## Overview

The Get1/Get2 complex (also known as WRB/CAML in metazoans) is the membrane protein insertase of the eukaryotic [GET pathway](/xray-mp-wiki/concepts/miscellaneous/get-pathway/), responsible for inserting tail-anchored (TA) membrane proteins into the endoplasmic reticulum (ER) membrane. The complex forms a 2:2 heterotetramer of Get1 and Get2 subunits, with each Get1/Get2 heterodimer containing a membrane-embedded hydrophilic groove that facilitates TA protein insertion. The GET insertase exhibits conformational plasticity (state 1 and state 2) dictated by interactions of the Get2 helix alpha3' with Get3.


## Publications

### doi/10.1038##s41467-023-42867-2

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8cr1">8CR1</a></td>
      <td>3.2</td>
      <td>not reported</td>
      <td>H. sapiens Get2^DeltaN-Get1/Get3 in PMAL-C8 amphipol (wild type, state 2)</td>
      <td>phosphatidylinositol at heterotetramer interface</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8cr2">8CR2</a></td>
      <td>4.2</td>
      <td>not reported</td>
      <td>H. sapiens Get2^DeltaN/Deltaalpha3'-Get1/Get3 in PMAL-C8 amphipol (Deltaalpha3' mutant, state 1)</td>
      <td>lipid/amphipathic density in central membrane cavity</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8odu">8ODU</a></td>
      <td>5.0</td>
      <td>not reported</td>
      <td>C. thermophilum Get2^DeltaN-Get1/Get3 in A835 amphipol (state 1)</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8odv">8ODV</a></td>
      <td>4.7</td>
      <td>not reported</td>
      <td>C. thermophilum Get2^DeltaN-Get1/Get3 in nanodisc (state 1)</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: S. cerevisiae (for ctGet1/Get2); Sf9 insect cells (for hsGet1/Get2)
- **Construct**: Codon-optimized ctGet1/ctGet2 in pMT929 vector under GAL1 promoter (yeast); hsGet2^DeltaN-Get1 fusion in pFastBac1 (insect cells)
- **Induction**: Galactose induction (yeast); Baculovirus infection (insect cells)

**Purification:**

- **Expression system**: S. cerevisiae / [Sf9](/xray-mp-wiki/methods/expression-systems/sf9-expression-system/) insect cells
- **Expression construct**: Get1/Get2 complex with C-terminal tags
- **Tag info**: [His6-tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) or Strep-tag II, cleavable

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
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (for amphipol reconstitution) or LMNG (for nanodisc)</td>
      <td></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> / Strep-Tactin</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Amphipol reconstitution or nanodisc assembly</td>
      <td>Bio-beads detergent removal</td>
      <td>—</td>
      <td></td>
      <td>Reconstituted in PMAL-C8 amphipol or A835 amphipol for cryo-EM; nanodisc assembled with MSP1E3D1 scaffold protein</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 150 mM NaCl, 2 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a></td>
      <td></td>
    </tr>
  </tbody>
</table>

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8cr1">8CR1</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GAMAAGVAGWGVEAEEFEDAPDVEP</span><span class="topo-inside">LEPTLSNIIEQRSLKWIFVGGKGGVGKTTCSCSLAVQLSKGRESVLIISTDPAHNISDAFDQKFSKVPTKVKGYDNLFAMEIDPSLGVAELPDEF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FEEDNMLSMGKKMMQEAMSAFPGIDEAMSYAEVMRLVKGMNFSVVVFDTAPTGHTLRLLNFPTIVERGLGRLMQIKNQISPFISQMC</span><span class="topo-unknown">NMLGLGDM</span><span class="topo-inside">NADQLASKLEETLPVIRSVSEQFKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">PEQTTFICVCIAEFLSLYETERLIQELAKCKIDTHNIIVNQLVFPDPEKPCKMCEARHKIQAKYLDQMEDLYEDFHIVKLPLLPHEVRGADKVNTFSALLLEPYKP</span><span class="topo-unknown">PSAQGSWSHPQFEK</span></span>
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
      <td>25</td>
      <td>-1</td>
      <td>23</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>26</td>
      <td>207</td>
      <td>24</td>
      <td>205</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>215</td>
      <td>206</td>
      <td>213</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>216</td>
      <td>346</td>
      <td>214</td>
      <td>344</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>347</td>
      <td>360</td>
      <td>345</td>
      <td>358</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8cr1">8CR1</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDSFRIF</span><span class="topo-membrane">RLVGCALLALGVRAFVC</span><span class="topo-outside">KYLSIF</span><span class="topo-membrane">APFLTLQLAYMGLYKYFPKSEK</span><span class="topo-inside">KIKTTVLTAALLLSGIPAEVIN</span><span class="topo-membrane">RSMDTYSKMGEVFTDLCVYFFTFIFC</span><span class="topo-outside">HELLDYW</span><span class="topo-unknown">GSEVPGSGSENLY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">FQSGSGSMSSA</span><span class="topo-outside">AADH</span><span class="topo-membrane">WAWLLVLSFVFGCNVLRILLPSFSS</span><span class="topo-inside">FMSRVLQKDAEQESQMRAEIQDMKQELSTVNMMDEFARYARLERKINKMTDKLKTHVKARTAQLAKIKWV</span><span class="topo-membrane">ISVAFYVLQA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310 </span>
<span class="topo-line"><span class="topo-membrane">ALMISLIWKYYSVPVA</span><span class="topo-outside">VVPSKWI</span><span class="topo-membrane">TPLDRLVAFPTRVAGGVGITCWILVCNKVVAIV</span><span class="topo-unknown">LHPFSGSGSLEVLFQ</span></span>
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
      <td>6</td>
      <td>185</td>
      <td>190</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>24</td>
      <td>192</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>30</td>
      <td>209</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>52</td>
      <td>215</td>
      <td>236</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>53</td>
      <td>74</td>
      <td>237</td>
      <td>258</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>100</td>
      <td>259</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>107</td>
      <td>285</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>131</td>
      <td>292</td>
      <td>315</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>132</td>
      <td>135</td>
      <td>1005</td>
      <td>1008</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>136</td>
      <td>160</td>
      <td>1009</td>
      <td>1033</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>230</td>
      <td>1034</td>
      <td>1103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>256</td>
      <td>1104</td>
      <td>1129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>257</td>
      <td>263</td>
      <td>1130</td>
      <td>1136</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>264</td>
      <td>296</td>
      <td>1137</td>
      <td>1169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>297</td>
      <td>311</td>
      <td>1170</td>
      <td>1184</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8cr1">8CR1</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GAMAAGVAGWGVEAEEFEDAPDVEP</span><span class="topo-inside">LEPTLSNIIEQRSLKWIFVGGKGGVGKTTCSCSLAVQLSKGRESVLIISTDPAHNISDAFDQKFSKVPTKVKGYDNLFAMEIDPSLGVAELPDEF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FEEDNMLSMGKKMMQEAMSAFPGIDEAMSYAEVMRLVKGMNFSVVVFDTAPTGHTLRLLNFPTIVERGLGRLMQIKNQISPFISQMC</span><span class="topo-unknown">NMLGLGDM</span><span class="topo-inside">NADQLASKLEETLPVIRSVSEQFKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">PEQTTFICVCIAEFLSLYETERLIQELAKCKIDTHNIIVNQLVFPDPEKPCKMCEARHKIQAKYLDQMEDLYEDFHIVKLPLLPHEVRGADKVNTFSALLLEPYKP</span><span class="topo-unknown">PSAQGSWSHPQFEK</span></span>
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
      <td>25</td>
      <td>-1</td>
      <td>23</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>26</td>
      <td>207</td>
      <td>24</td>
      <td>205</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>215</td>
      <td>206</td>
      <td>213</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>216</td>
      <td>346</td>
      <td>214</td>
      <td>344</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>347</td>
      <td>360</td>
      <td>345</td>
      <td>358</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8cr1">8CR1</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDSFRIF</span><span class="topo-membrane">RLVGCALLALGVRAFVCK</span><span class="topo-outside">YLSIF</span><span class="topo-membrane">APFLTLQLAYMGLYKYFPKSEK</span><span class="topo-inside">KIKTTVLTAALLLSGIPAEVIN</span><span class="topo-membrane">RSMDTYSKMGEVFTDLCVYFFTFIFC</span><span class="topo-outside">HELLDYW</span><span class="topo-unknown">GSEVPGSGSENLY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">FQSGSGSMSSA</span><span class="topo-outside">AADH</span><span class="topo-membrane">WAWLLVLSFVFGCNVLRILLPSFSS</span><span class="topo-inside">FMSRVLQKDAEQESQMRAEIQDMKQELSTVNMMDEFARYARLERKINKMTDKLKTHVKARTAQLAKIKWV</span><span class="topo-membrane">ISVAFYVLQA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310 </span>
<span class="topo-line"><span class="topo-membrane">ALMISLIWKYYSVPVA</span><span class="topo-outside">VVPSKWI</span><span class="topo-membrane">TPLDRLVAFPTRVAGGVGITCWILVCNKVVAIV</span><span class="topo-unknown">LHPFSGSGSLEVLFQ</span></span>
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
      <td>6</td>
      <td>185</td>
      <td>190</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>25</td>
      <td>192</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>30</td>
      <td>210</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>52</td>
      <td>215</td>
      <td>236</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>53</td>
      <td>74</td>
      <td>237</td>
      <td>258</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>100</td>
      <td>259</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>107</td>
      <td>285</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>131</td>
      <td>292</td>
      <td>315</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>132</td>
      <td>135</td>
      <td>1005</td>
      <td>1008</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>136</td>
      <td>160</td>
      <td>1009</td>
      <td>1033</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>230</td>
      <td>1034</td>
      <td>1103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>256</td>
      <td>1104</td>
      <td>1129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>257</td>
      <td>263</td>
      <td>1130</td>
      <td>1136</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>264</td>
      <td>296</td>
      <td>1137</td>
      <td>1169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>297</td>
      <td>311</td>
      <td>1170</td>
      <td>1184</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8cr2">8CR2</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GAMAAGVAGWGVEAEEFEDAPDVE</span><span class="topo-inside">PLEPTLSNIIEQRSLKWIFVGGKGGVGKTTCSCSLAVQLSKGRESVLIISTDPAHNISDAFDQKFSKVPTKVKGYDNLFAMEIDPS</span><span class="topo-unknown">LGVAELPDEF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">FEEDNMLSMGKKMMQEAMSAF</span><span class="topo-inside">PGIDEAMSYAEVMRLVKGMNFSVVVFDTAPTGHTLRLLNFPTIVERGLGRLMQ</span><span class="topo-unknown">IKNQISPFISQMCNMLGLGDMNA</span><span class="topo-inside">DQLASKLEETLPVIRSVSEQFKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">PEQTTFICVCIAEFLSLYETERLIQELAKCKIDTHNIIVNQLVFPDPEKPCKMCEARHKIQAKYLDQMEDLYEDFHIVKLPLLPHEVRGADKVNTFSALLLEPYKP</span><span class="topo-unknown">PSAQGSWSHPQFEK</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>24</td>
      <td>-1</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>25</td>
      <td>110</td>
      <td>23</td>
      <td>108</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>111</td>
      <td>141</td>
      <td>109</td>
      <td>139</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>142</td>
      <td>194</td>
      <td>140</td>
      <td>192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>193</td>
      <td>215</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>218</td>
      <td>346</td>
      <td>216</td>
      <td>344</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>347</td>
      <td>360</td>
      <td>345</td>
      <td>358</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8cr2">8CR2</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GAMAAGVAGWGVEAEEFEDAPDVE</span><span class="topo-inside">PLEPTLSNIIEQRSLKWIFVGGKGGVGKTTCSCSLAVQLSKGRESVLIISTDPAHNISDAFDQKFSKVPTKVKGYDNLFAMEIDPS</span><span class="topo-unknown">LGVAELPDEF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">FEEDNMLSMGKKMMQEAMSAF</span><span class="topo-inside">PGIDEAMSYAEVMRLVKGMNFSVVVFDTAPTGHTLRLLNFPTIVERGLGRL</span><span class="topo-unknown">MQIKNQISPFISQMCNMLGLGDMNADQLA</span><span class="topo-inside">SKLEETLPVIRSVSEQFKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">PEQTTFICVCIAEFLSLYETERLIQELAKCKIDTHNIIVNQLVFPDPEKPCKMCEARHKIQAKYLDQMEDLYEDFHIVKLPLLPHEVRGADKVNTFSALLLEPYKP</span><span class="topo-unknown">PSAQGSWSHPQFEK</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>24</td>
      <td>-1</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>25</td>
      <td>110</td>
      <td>23</td>
      <td>108</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>111</td>
      <td>141</td>
      <td>109</td>
      <td>139</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>142</td>
      <td>192</td>
      <td>140</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>221</td>
      <td>191</td>
      <td>219</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>222</td>
      <td>346</td>
      <td>220</td>
      <td>344</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>347</td>
      <td>360</td>
      <td>345</td>
      <td>358</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8cr2">8CR2</a> — Chain C (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDSFRIFRLVGCALLALGVRAFVCKYLSIFAPFLTLQLAYMGLYKYFPKSEKKIKTTGGGGGIPAEVINRSMDTYSKMGEVFTDLCVYFFTFIFCHELLDYWGSEVPGSGSENLYFQSGS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">GSMSSAAADHWAWLLVLSFVFGCNVLRIL</span><span class="topo-inside">LPSFSSFMSRVLQKDAEQESQMRAEIQDMKQELSTVNMMDEFARYARLERKINKMTDKLKTHVKARTAQLAKIKWVIS</span><span class="topo-membrane">VAFYVLQAALMIS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300      </span>
<span class="topo-line"><span class="topo-membrane">LIWK</span><span class="topo-outside">YY</span><span class="topo-unknown">SVPVAVVPSKWITPLDRLVAFPTRVAGGVGITCWILVCNKVVAIVLHPFSGSGSLEVLFQ</span></span>
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
      <td>149</td>
      <td>879</td>
      <td>1027</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>150</td>
      <td>227</td>
      <td>1028</td>
      <td>1105</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>244</td>
      <td>1106</td>
      <td>1122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>246</td>
      <td>1123</td>
      <td>1124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>247</td>
      <td>306</td>
      <td>1125</td>
      <td>1184</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8cr2">8CR2</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDSF</span><span class="topo-inside">RI</span><span class="topo-membrane">FRLVGCALLALGVRAFV</span><span class="topo-outside">CKYLSIFA</span><span class="topo-membrane">PFLTLQLAYMGLYKYFP</span><span class="topo-inside">KS</span><span class="topo-unknown">EKKIKTTGGGGGIP</span><span class="topo-inside">AEVINRSMD</span><span class="topo-membrane">TYSKMGEVFTDLCVYFFTFIFC</span><span class="topo-outside">HELLDYW</span><span class="topo-unknown">GSEVPGSGSENLYFQSGS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">GSMSSA</span><span class="topo-outside">AADHWA</span><span class="topo-membrane">WLLVLSFVFGCNVLRIL</span><span class="topo-inside">LPSFSSFMSRVLQKDAEQESQMRAEIQDMKQELSTVNMMDEFARYARLERKINKMTDKLKTHVKARTAQLAKIKWVI</span><span class="topo-membrane">SVAFYVLQAALMIS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300      </span>
<span class="topo-line"><span class="topo-membrane">LIWK</span><span class="topo-outside">YY</span><span class="topo-unknown">SVPVAVVPSKWITPLDRLVAFPTRV</span><span class="topo-membrane">AGGVGITCWILVCNKVVAIVL</span><span class="topo-inside">HP</span><span class="topo-unknown">FSGSGSLEVLFQ</span></span>
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
      <td>4</td>
      <td>185</td>
      <td>188</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>6</td>
      <td>189</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>23</td>
      <td>191</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>31</td>
      <td>208</td>
      <td>215</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>48</td>
      <td>216</td>
      <td>232</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>50</td>
      <td>233</td>
      <td>234</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>64</td>
      <td>235</td>
      <td>248</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>65</td>
      <td>73</td>
      <td>254</td>
      <td>262</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>95</td>
      <td>263</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>96</td>
      <td>102</td>
      <td>285</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>126</td>
      <td>292</td>
      <td>315</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>127</td>
      <td>132</td>
      <td>1005</td>
      <td>1010</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>149</td>
      <td>1011</td>
      <td>1027</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>226</td>
      <td>1028</td>
      <td>1104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>227</td>
      <td>244</td>
      <td>1105</td>
      <td>1122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>246</td>
      <td>1123</td>
      <td>1124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>247</td>
      <td>270</td>
      <td>1125</td>
      <td>1148</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>272</td>
      <td>292</td>
      <td>1150</td>
      <td>1170</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>293</td>
      <td>294</td>
      <td>1171</td>
      <td>1172</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>306</td>
      <td>1173</td>
      <td>1184</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8odu">8ODU</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MEPTLQSILDQRSLRWIFVGGKGGVGKTTTSCSLAIQLAKVRRSVLLLSTDPAHNLSDAFSQKFGKEARLVEGFDNLYAMEIDPNGSMQDLL</span><span class="topo-unknown">AGQTGDGDAGMGGV</span><span class="topo-outside">GVMQDLAYAIPGID</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">EAMSFAEVLKQVNSLSYETIVFDTAPTGHTLRFLQFPTVLEKALAKVSQL</span><span class="topo-unknown">SGQYGSLLNGILGGSGTLPNG</span><span class="topo-outside">QTLSDVMEKLDSLRVTISEVNAQFKDERLTTFVCVCIPEFLSLYETERM</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330    </span>
<span class="topo-line"><span class="topo-outside">IQELANYGIDTHCIVVNQLLFPKPGSDCEQCTARRRMQKKYLDQIEELYDEEFNVVKMPLLVEEVRGKERLEKFSEMLIKPFVPPE</span><span class="topo-unknown">WSHPQFEK</span></span>
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
      <td>92</td>
      <td>14</td>
      <td>105</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>106</td>
      <td>106</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>107</td>
      <td>170</td>
      <td>120</td>
      <td>183</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>171</td>
      <td>191</td>
      <td>184</td>
      <td>204</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>192</td>
      <td>326</td>
      <td>205</td>
      <td>339</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>334</td>
      <td>340</td>
      <td>347</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8odu">8ODU</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MEPTLQSILDQRSLRWIFVGGKGGVGKTTTSCSLAIQLAKVRRSVLLLSTDPAHNLSDAFSQKFGKEARLVEGFDNLYAMEIDPNGSMQDLL</span><span class="topo-unknown">AGQTGDGDAGMGGV</span><span class="topo-outside">GVMQDLAYAIPGID</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">EAMSFAEVLKQVNSLSYETIVFDTAPTGHTLRFLQFPTVLEKALAKVS</span><span class="topo-unknown">QLSGQYGSLLNGILGGSGTLPNG</span><span class="topo-outside">QTLSDVMEKLDSLRVTISEVNAQFKDERLTTFVCVCIPEFLSLYETERM</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330    </span>
<span class="topo-line"><span class="topo-outside">IQELANYGIDTHCIVVNQLLFPKPGSDCEQCTARRRMQKKYLDQIEELYDEEFNVVKMPLLVEEVRGKERLEKFSEMLIKPFVPPE</span><span class="topo-unknown">WSHPQFEK</span></span>
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
      <td>92</td>
      <td>14</td>
      <td>105</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>106</td>
      <td>106</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>107</td>
      <td>168</td>
      <td>120</td>
      <td>181</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>169</td>
      <td>191</td>
      <td>182</td>
      <td>204</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>192</td>
      <td>326</td>
      <td>205</td>
      <td>339</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>334</td>
      <td>340</td>
      <td>347</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8odu">8ODU</a> — Chain C (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGRPTPLWRFLHTLLAVALGLAVIMLSPFGGTKLERDRAAAAVAGSASEREWLASLTDSYPLVKTGLGGGLFWAFATGEAILLGTRWLFLSKKKKAATAAAKVNNNNGEGDDAELDSVEQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">AIELALEFFPAIRQPVEYL</span><span class="topo-inside">RPKVAVAMRYVDVGMTLWRDVMLALFVLGAVAWWRA</span><span class="topo-unknown">GSGSENLYFQSGSGS</span><span class="topo-inside">MS</span><span class="topo-membrane">LLLVIFLLELVVQLVNTIG</span><span class="topo-outside">AKTINNLLWRFYLSIPGSPLAKDFAEQRA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">KQKEYLQVRHDLNATSSQDEFAKWARLQRKHDKLMDELEKKKSQLDAHRTSFSRK</span><span class="topo-membrane">LTIYRWILTRGMQWFLCF</span><span class="topo-inside">WFSSQPMFWLPYGWFPYWVEWLVSFPNAPMGSVSIV</span><span class="topo-membrane">VWQSACSGVLA</span></span>
<span class="topo-ruler">       370       380       390       400         </span>
<span class="topo-line"><span class="topo-membrane">LVIEAVMAVVR</span><span class="topo-unknown">YTGGTGMQKQRQPVPAAGGAPGTSKKDLGSGSLEVLFQ</span></span>
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
      <td>117</td>
      <td>183</td>
      <td>299</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>119</td>
      <td>131</td>
      <td>301</td>
      <td>313</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>132</td>
      <td>138</td>
      <td>314</td>
      <td>320</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>140</td>
      <td>175</td>
      <td>322</td>
      <td>357</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>190</td>
      <td>358</td>
      <td>372</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>191</td>
      <td>192</td>
      <td>1001</td>
      <td>1002</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>211</td>
      <td>1003</td>
      <td>1021</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>212</td>
      <td>295</td>
      <td>1022</td>
      <td>1105</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>296</td>
      <td>313</td>
      <td>1106</td>
      <td>1123</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>349</td>
      <td>1124</td>
      <td>1159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>350</td>
      <td>371</td>
      <td>1160</td>
      <td>1181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>372</td>
      <td>409</td>
      <td>1182</td>
      <td>1219</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8odu">8ODU</a> — Chain D (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGRPTPLWRFLHTLLAVALGLAVIMLSPFGGTKLERDRAAAAVAGSASEREWLASLTDSYPLVKTGLGGGLFWAFATGEAILLGTRWLFLSKKKKAATAAAKVNNNNGEGDDAELDSVEQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">AIELALEFFPAIRQPVEY</span><span class="topo-inside">LRPKVAVAMRYVDVGMTLWRDVMLALFVLGAVAWWRA</span><span class="topo-unknown">GSGSENLYFQSGSGS</span><span class="topo-inside">MSL</span><span class="topo-membrane">LLVIFLLELVVQLVNTIGA</span><span class="topo-outside">KTINNLLWRFYLSIPGSPLAKDFAEQRA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">KQKEYLQVRHDLNATSSQDEFAKWARLQRKHDKLMDELEKKKSQLDAHRTSFSRK</span><span class="topo-membrane">LTIYRWILTRGMQWFLCF</span><span class="topo-inside">WFSSQPMFWLPYGWFPYWVEWLVSFPNAPMGSVSIVVW</span><span class="topo-membrane">QSACSGVLA</span></span>
<span class="topo-ruler">       370       380       390       400         </span>
<span class="topo-line"><span class="topo-membrane">LVIEAVMAVVR</span><span class="topo-unknown">YTGGTGMQKQRQPVPAAGGAPGTSKKDLGSGSLEVLFQ</span></span>
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
      <td>117</td>
      <td>183</td>
      <td>299</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>119</td>
      <td>131</td>
      <td>301</td>
      <td>313</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>132</td>
      <td>138</td>
      <td>314</td>
      <td>320</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>139</td>
      <td>175</td>
      <td>321</td>
      <td>357</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>190</td>
      <td>358</td>
      <td>372</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>191</td>
      <td>193</td>
      <td>1001</td>
      <td>1003</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>212</td>
      <td>1004</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>295</td>
      <td>1023</td>
      <td>1105</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>296</td>
      <td>313</td>
      <td>1106</td>
      <td>1123</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>351</td>
      <td>1124</td>
      <td>1161</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>352</td>
      <td>371</td>
      <td>1162</td>
      <td>1181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>372</td>
      <td>409</td>
      <td>1182</td>
      <td>1219</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8odv">8ODV</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MEPTLQSILDQRSLRWIFVGGKGGVGKTTTSCSLAIQLAKVRRSVLLLSTDPAHNLSDAFSQKFGKEARLVEGFDNLYAMEIDPNGSMQDLL</span><span class="topo-unknown">AGQTGDGDAGMGGV</span><span class="topo-inside">GVMQDLAYAIPGID</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">EAMSFAEVLKQVNSLSYETIVFDTAPTGHTLRFLQFPTVLEKALAKVSQLSG</span><span class="topo-unknown">QYGSLLNGILGGSGTLPNG</span><span class="topo-inside">QTLSDVMEKLDSLRVTISEVNAQFKDERLTTFVCVCIPEFLSLYETERM</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330    </span>
<span class="topo-line"><span class="topo-inside">IQELANYGIDTHCIVVNQLLFPKPGSDCEQCTARRRMQKKYLDQIEELYDEEFNVVKMPLLVEEVRGKERLEKFSEMLIKPFVPPE</span><span class="topo-unknown">WSHPQFEK</span></span>
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
      <td>92</td>
      <td>14</td>
      <td>105</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>106</td>
      <td>106</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>107</td>
      <td>172</td>
      <td>120</td>
      <td>185</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>191</td>
      <td>186</td>
      <td>204</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>192</td>
      <td>326</td>
      <td>205</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>334</td>
      <td>340</td>
      <td>347</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8odv">8ODV</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MEPTLQSILDQRSLRWIFVGGKGGVGKTTTSCSLAIQLAKVRRSVLLLSTDPAHNLSDAFSQKFGKEARLVEGFDNLYAMEIDPNGSMQDLL</span><span class="topo-unknown">AGQTGDGDAGMGGV</span><span class="topo-inside">GVMQDLAYAIPGID</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">EAMSFAEVLKQVNSLSYETIVFDTAPTGHTLRFLQFPTVLEKALAKVSQLSG</span><span class="topo-unknown">QYGSLLNGILGGSGTLPNG</span><span class="topo-inside">QTLSDVMEKLDSLRVTISEVNAQFKDERLTTFVCVCIPEFLSLYETERM</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330    </span>
<span class="topo-line"><span class="topo-inside">IQELANYGIDTHCIVVNQLLFPKPGSDCEQCTARRRMQKKYLDQIEELYDEEFNVVKMPLLVEEVRGKERLEKFSEMLIKPFVPPE</span><span class="topo-unknown">WSHPQFEK</span></span>
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
      <td>92</td>
      <td>14</td>
      <td>105</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>106</td>
      <td>106</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>107</td>
      <td>172</td>
      <td>120</td>
      <td>185</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>191</td>
      <td>186</td>
      <td>204</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>192</td>
      <td>326</td>
      <td>205</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>334</td>
      <td>340</td>
      <td>347</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8odv">8ODV</a> — Chain C (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGRPTPLWRFLHTLLAVALGLAVIMLSPFGGTKLERDRAAAAVAGSASEREWLASLTDSYPLVKTGLGGGLFWAFATGEAILLGTRWLFLSKKKKAATAAAKVNNNNGEGDDAELDS</span><span class="topo-inside">VEQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">AIELALEFFPA</span><span class="topo-unknown">IRQPVEYLRPKVAVAMRYVDVG</span><span class="topo-outside">MTLWRDVMLALFVLGAVAWWRA</span><span class="topo-unknown">GSGSENLYFQSGSGSM</span><span class="topo-membrane">SLLLVIFLLELVVQLVNTI</span><span class="topo-inside">GAKTINNLLWRFYLSIPGSPLAKDFAEQRA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">KQKEYLQVRHDLNATSSQDEFAKWARLQRKHDKLMDELEKKKSQLDAHRTSFSRKLT</span><span class="topo-membrane">IYRWILTRGMQWFLCFWFS</span><span class="topo-outside">SQPMFWLPYGWFPYWVEWLVSFPNAPMGSVS</span><span class="topo-membrane">IVVWQSACSGVLA</span></span>
<span class="topo-ruler">       370       380       390       400         </span>
<span class="topo-line"><span class="topo-membrane">LVIEAVMAV</span><span class="topo-inside">VR</span><span class="topo-unknown">YTGGTGMQKQRQPVPAAGGAPGTSKKDLGSGSLEVLFQ</span></span>
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
      <td>117</td>
      <td>183</td>
      <td>299</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>118</td>
      <td>131</td>
      <td>300</td>
      <td>313</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>152</td>
      <td>314</td>
      <td>334</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>154</td>
      <td>175</td>
      <td>336</td>
      <td>357</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>190</td>
      <td>358</td>
      <td>372</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>192</td>
      <td>210</td>
      <td>1002</td>
      <td>1020</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>297</td>
      <td>1021</td>
      <td>1107</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>298</td>
      <td>316</td>
      <td>1108</td>
      <td>1126</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>317</td>
      <td>347</td>
      <td>1127</td>
      <td>1157</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>348</td>
      <td>369</td>
      <td>1158</td>
      <td>1179</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>370</td>
      <td>371</td>
      <td>1180</td>
      <td>1181</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>372</td>
      <td>409</td>
      <td>1182</td>
      <td>1219</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8odv">8ODV</a> — Chain D (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGRPTPLWRFLHTLLAVALGLAVIMLSPFGGTKLERDRAAAAVAGSASEREWLASLTDSYPLVKTGLGGGLFWAFATGEAILLGTRWLFLSKKKKAATAAAKVNNNNGEGDDAELDS</span><span class="topo-inside">VEQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">AIELALEFFPA</span><span class="topo-unknown">IRQPVEYLRPKVAVAMRYVDVG</span><span class="topo-outside">MTLWRDVMLALFVLGAVAWWRA</span><span class="topo-unknown">GSGSENLYFQSGSGSM</span><span class="topo-membrane">SLLLVIFLLELVVQLVNTI</span><span class="topo-inside">GAKTINNLLWRFYLSIPGSPLAKDFAEQRA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">KQKEYLQVRHDLNATSSQDEFAKWARLQRKHDKLMDELEKKKSQLDAHRTSFSRKLT</span><span class="topo-membrane">IYRWILTRGMQWFLCFWF</span><span class="topo-outside">SSQPMFWLPYGWFPYWVEWLVSFPNAPMGSVS</span><span class="topo-membrane">IVVWQSACSGVLA</span></span>
<span class="topo-ruler">       370       380       390       400         </span>
<span class="topo-line"><span class="topo-membrane">LVIEAVMAV</span><span class="topo-inside">VR</span><span class="topo-unknown">YTGGTGMQKQRQPVPAAGGAPGTSKKDLGSGSLEVLFQ</span></span>
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
      <td>117</td>
      <td>183</td>
      <td>299</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>118</td>
      <td>131</td>
      <td>300</td>
      <td>313</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>152</td>
      <td>314</td>
      <td>334</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>154</td>
      <td>175</td>
      <td>336</td>
      <td>357</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>190</td>
      <td>358</td>
      <td>372</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>192</td>
      <td>210</td>
      <td>1002</td>
      <td>1020</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>297</td>
      <td>1021</td>
      <td>1107</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>298</td>
      <td>315</td>
      <td>1108</td>
      <td>1125</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>316</td>
      <td>347</td>
      <td>1126</td>
      <td>1157</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>348</td>
      <td>369</td>
      <td>1158</td>
      <td>1179</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>370</td>
      <td>371</td>
      <td>1180</td>
      <td>1181</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>372</td>
      <td>409</td>
      <td>1182</td>
      <td>1219</td>
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

### GET insertase conformational states (state 1 and state 2)

The GET insertase adopts two distinct conformations: state 1 (observed in C. thermophilum and hsGet1/Get2^Deltaalpha3') where the hydrophilic grooves point inward toward each other and helix alpha3' interacts with Get1 TMD2 of the opposing heterodimer; and state 2 (observed in wild type hsGet1/Get2) where the grooves point outward and helix alpha3' binds the Get3 TABD, enabling lateral release of the TA protein.

### Membrane thinning by the GET insertase

The GET insertase induces significant thinning of the lipid bilayer in the vicinity of the hydrophilic groove and Get2 TMD3. Atomistic MD simulations show the membrane is notably thinner near hsGet1/Get2, independent of lipid composition. This thinning lowers the energetic barrier for TA protein insertion by reducing the hydrophobic distance the polar C-terminal extension must cross.

### Conserved core fold of Get1/Get2 heterodimer

The core fold of the Get1/Get2 heterodimer is conserved from lower to higher eukaryotes, maintaining key features including the hydrophilic groove, helix alpha3', the ER cap, and the amphipathic helix (AH). The structure from C. thermophilum shows the same overall architecture as the human complex.


## Cross-References

- <a href="/xray-mp-wiki/proteins/secretion-translocon/get3/">Get3 (TRC40) TA Protein Targeting Factor</a> — Get3 delivers TA proteins to the Get1/Get2 insertase complex
- <a href="/xray-mp-wiki/concepts/miscellaneous/hydrophilic-groove-insertion/">Hydrophilic Groove Insertion Mechanism</a> — The GET insertase uses a hydrophilic groove to facilitate TA protein membrane insertion
- <a href="/xray-mp-wiki/concepts/miscellaneous/get-pathway/">GET Pathway for Tail-Anchored Protein Insertion</a> — Get1/Get2 is the membrane insertase complex of the GET pathway
