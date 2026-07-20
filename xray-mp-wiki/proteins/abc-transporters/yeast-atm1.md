---
title: "Yeast Mitochondrial ABC Transporter Atm1"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, pump, membrane-protein]
sources: [doi/10.1126##science.1246729]
verified: agent
uniprot_id: P40416
---

# Yeast Mitochondrial ABC Transporter Atm1

<div class="expr-badges"><span class="expr-badge expr-s-cerevisiae">S. cerevisiae</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P40416">UniProt: P40416</a>

<span class="expr-badge">Saccharomyces cerevisiae</span>

## Overview

Yeast Atm1 (ABC transporter of mitochondria 1) is a mitochondrial inner membrane ABC exporter from *Saccharomyces cerevisiae* that functions in the export of a sulfur-containing molecule required for cytosolic-nuclear iron-sulfur (Fe/S) protein biogenesis and cellular [IRON](/xray-mp-wiki/reagents/additives/iron/) regulation. Crystal structures were determined in nucleotide-free and glutathione-bound forms at 3.06 and 3.38 Å resolution, respectively, both in inward-facing, open conformations. The structures reveal that Atm1 forms a domain-swapped dimer with 12 transmembrane helices enclosing a 6900 Å³ positively charged cavity. A defining feature is the complete resolution of two C-terminal α-helices that interact in a crossover fashion to stabilize the dimer in the inward-facing open conformation, a structural element not observed previously in any other ABC transporter crystal structure. Mutations in the human ortholog ABCB7 cause X-linked sideroblastic anemia with cerebellar ataxia (XLSA/A).


## Publications

### doi/10.1126##science.1246729

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4myc">4MYC</a></td>
      <td>3.06</td>
      <td>—</td>
      <td>S. cerevisiae Atm1Δ98 (residues 99-678), C-terminal Strep-tag</td>
      <td>None (nucleotide-free)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4myh">4MYH</a></td>
      <td>3.38</td>
      <td>—</td>
      <td>S. cerevisiae Atm1Δ98 (residues 99-678), C-terminal Strep-tag</td>
      <td><a href="/xray-mp-wiki/reagents/additives/glutathione/">GSH</a> (<a href="/xray-mp-wiki/reagents/additives/glutathione/">GSH</a>)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Saccharomyces cerevisiae
- **Construct**: Atm1Δ98 lacking the first 98 residues (mitochondrial presequence), with C-terminal Strep-tag; residues 99-678
- **Notes**: Expressed in S. cerevisiae; the processed mature form (residues 99-678) was used for crystallization

**Purification:**

- **Expression system**: Saccharomyces cerevisiae
- **Expression construct**: Atm1Δ98 (residues 99-678) with C-terminal Strep-tag
- **Tag info**: C-terminal Strep-tag; five residues of the Strep-tag visible in the C-terminal helix structure

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
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Strep-tag affinity purification</td>
      <td>—</td>
      <td></td>
      <td>Purified via C-terminal Strep-tag; <a href="/xray-mp-wiki/reagents/additives/glutathione/">GSH</a> co-purified with protein throughout purification at low temperature</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td>—</td>
      <td></td>
      <td>Final purification step in detergent solution</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified Atm1Δ98 in detergent solution; contained bound [GSH](/xray-mp-wiki/reagents/additives/glutathione/) (Kd = 23 μM) as verified by mass spectrometry
**Yield**: —
**Purity**: —

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallization details in Supporting Online Material. Data collected at X06SA beamline, Swiss Light Source, Paul Scherrer Institute. ATPase activity of Atm1 was almost fully recovered after detergent solubilization of crystals.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4myc">4MYC</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">YIWPKGNNK</span><span class="topo-membrane">VRIRVLIALGLLISAKILNVQVPFFF</span><span class="topo-inside">KQTIDSMNIAWDDPTVALPAAIGLTIL</span><span class="topo-membrane">CYGVARFGSVLFGELRNAVFAKV</span><span class="topo-outside">AQNAIRTVSLQTFQHLMKLDLGWHLSRQTGGLTRA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">MDRGTKGISQV</span><span class="topo-membrane">LTAMVFHIIPISFEISVVCGILT</span><span class="topo-inside">YQFGA</span><span class="topo-membrane">SFAAITFSTMLLYSIFTIKTTAWR</span><span class="topo-outside">THFRRDANKADNKAASVALDSLINFEAVKYFNNEKYLADKYNGSLMNYRDSQIK</span><span class="topo-membrane">VSQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">SLAFLNSGQNLIFTTALTAMM</span><span class="topo-inside">YMGCTGVIGGNLTVGDLV</span><span class="topo-membrane">LINQLVFQLSVPLNFLGSVY</span><span class="topo-outside">RDLKQSLIDMETLFKLRKNEVKIKNAERPLMLPENVPYDITFENVTFGYHPDRKILKNASF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">TIPAGWKTAIVGSSGSGKSTILKLVFRFYDPESGRILINGRDIKEYDIDALRKVIGVVPQDTPLFNDTIWENVKFGRIDATDEEVITVVEKAQLAPLIKKLPQGFDTIVGERGLMISGGE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590        </span>
<span class="topo-line"><span class="topo-outside">KQRLAIARVLLKNARIMFFDEATSALDTHTEQALLRTIRDNFTSGSRTSVYIAHRLRTIADADKIIVLDNGRVREEGKHLELLAMPGSLYRELWTIQEDLDHLENELKDQQELWSHPQ</span></span>
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
      <td>9</td>
      <td>98</td>
      <td>106</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>35</td>
      <td>107</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>62</td>
      <td>133</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>85</td>
      <td>160</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>86</td>
      <td>131</td>
      <td>183</td>
      <td>228</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>154</td>
      <td>229</td>
      <td>251</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>159</td>
      <td>252</td>
      <td>256</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>183</td>
      <td>257</td>
      <td>280</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>184</td>
      <td>237</td>
      <td>281</td>
      <td>334</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>238</td>
      <td>261</td>
      <td>335</td>
      <td>358</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>279</td>
      <td>359</td>
      <td>376</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>299</td>
      <td>377</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>598</td>
      <td>397</td>
      <td>695</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4myc">4MYC</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">YIWPKGNNK</span><span class="topo-membrane">VRIRVLIALGLLISAKILNVQVPFFF</span><span class="topo-inside">KQTIDSMNIAWDDPTVALPAAIGLTI</span><span class="topo-membrane">LCYGVARFGSVLFGELRNAVFAKV</span><span class="topo-outside">AQNAIRTVSLQTFQHLMKLDLGWHLSRQTGGLTRA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">MDRGTKGISQV</span><span class="topo-membrane">LTAMVFHIIPISFEISVVCGILTY</span><span class="topo-inside">QFGA</span><span class="topo-membrane">SFAAITFSTMLLYSIFTIKTTAWR</span><span class="topo-outside">THFRRDANKADNKAASVALDSLINFEAVKYFNNEKYLADKYNGSLMNYRDSQI</span><span class="topo-membrane">KVSQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">SLAFLNSGQNLIFTTALTAMM</span><span class="topo-inside">YMGCTGVIGGNLTVGDLV</span><span class="topo-membrane">LINQLVFQLSVPLNFLGSVY</span><span class="topo-outside">RDLKQSLIDMETLFKLRKNEVKIKNAERPLMLPENVPYDITFENVTFGYHPDRKILKNASF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">TIPAGWKTAIVGSSGSGKSTILKLVFRFYDPESGRILINGRDIKEYDIDALRKVIGVVPQDTPLFNDTIWENVKFGRIDATDEEVITVVEKAQLAPLIKKLPQGFDTIVGERGLMISGGE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590        </span>
<span class="topo-line"><span class="topo-outside">KQRLAIARVLLKNARIMFFDEATSALDTHTEQALLRTIRDNFTSGSRTSVYIAHRLRTIADADKIIVLDNGRVREEGKHLELLAMPGSLYRELWTIQEDLDHLENELKDQQELWSHPQ</span></span>
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
      <td>9</td>
      <td>98</td>
      <td>106</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>35</td>
      <td>107</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>61</td>
      <td>133</td>
      <td>158</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>85</td>
      <td>159</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>86</td>
      <td>131</td>
      <td>183</td>
      <td>228</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>155</td>
      <td>229</td>
      <td>252</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>156</td>
      <td>159</td>
      <td>253</td>
      <td>256</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>183</td>
      <td>257</td>
      <td>280</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>184</td>
      <td>236</td>
      <td>281</td>
      <td>333</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>237</td>
      <td>261</td>
      <td>334</td>
      <td>358</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>279</td>
      <td>359</td>
      <td>376</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>299</td>
      <td>377</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>598</td>
      <td>397</td>
      <td>695</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4myh">4MYH</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">YIWPKGNNKVRIRVL</span><span class="topo-membrane">IALGLLISAKILNVQVPFFF</span><span class="topo-inside">KQTIDSMNIAWDDPTVALPAAIGLTIL</span><span class="topo-membrane">CYGVARFGSVLFGELR</span><span class="topo-outside">NAVFAKVAQNAIRTVSLQTFQHLMKLDLGWHLSRQTGGLTRA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">MDRGTKGISQVLTAMVFHI</span><span class="topo-membrane">IPISFEISVVCGILT</span><span class="topo-inside">YQFGA</span><span class="topo-membrane">SFAAITFSTMLLYSIF</span><span class="topo-outside">TIKTTAWRTHFRRDANKADNKAASVALDSLINFEAVKYFNNEKYLADKYNGSLMNYRDSQIKVSQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">SLAFLN</span><span class="topo-membrane">SGQNLIFTTALTAMM</span><span class="topo-inside">YMGCTGVIGGNLTVGDLV</span><span class="topo-membrane">LINQLVFQLSVPLN</span><span class="topo-outside">FLGSVYRDLKQSLIDMETLFKLRKNEVKIKNAERPLMLPENVPYDITFENVTFGYHPDRKILKNASF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">TIPAGWKTAIVGSSGSGKSTILKLVFRFYDPESGRILINGRDIKEYDIDALRKVIGVVPQDTPLFNDTIWENVKFGRIDATDEEVITVVEKAQLAPLIKKLPQGFDTIVGERGLMISGGE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590        </span>
<span class="topo-line"><span class="topo-outside">KQRLAIARVLLKNARIMFFDEATSALDTHTEQALLRTIRDNFTSGSRTSVYIAHRLRTIADADKIIVLDNGRVREEGKHLELLAMPGSLYRELWTIQEDLDHLENELKDQQELWSHPQ</span></span>
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
      <td>15</td>
      <td>98</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>35</td>
      <td>113</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>62</td>
      <td>133</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>78</td>
      <td>160</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>139</td>
      <td>176</td>
      <td>236</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>154</td>
      <td>237</td>
      <td>251</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>159</td>
      <td>252</td>
      <td>256</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>175</td>
      <td>257</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>176</td>
      <td>246</td>
      <td>273</td>
      <td>343</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>247</td>
      <td>261</td>
      <td>344</td>
      <td>358</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>279</td>
      <td>359</td>
      <td>376</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>293</td>
      <td>377</td>
      <td>390</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>294</td>
      <td>598</td>
      <td>391</td>
      <td>695</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4myh">4MYH</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">YIWPKGNNKVRIRVLI</span><span class="topo-membrane">ALGLLISAKILNVQVPFFF</span><span class="topo-inside">KQTIDSMNIAWDDPTVALPAAIGLTI</span><span class="topo-membrane">LCYGVARFGSVLFGELR</span><span class="topo-outside">NAVFAKVAQNAIRTVSLQTFQHLMKLDLGWHLSRQTGGLTRA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">MDRGTKGISQVLTAMVFHII</span><span class="topo-membrane">PISFEISVVCGILTY</span><span class="topo-inside">QFGA</span><span class="topo-membrane">SFAAITFSTMLLYSIF</span><span class="topo-outside">TIKTTAWRTHFRRDANKADNKAASVALDSLINFEAVKYFNNEKYLADKYNGSLMNYRDSQIKVSQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">SLAFLN</span><span class="topo-membrane">SGQNLIFTTALTAMM</span><span class="topo-inside">YMGCTGVIGGNLTVGDLV</span><span class="topo-membrane">LINQLVFQLSVPLN</span><span class="topo-outside">FLGSVYRDLKQSLIDMETLFKLRKNEVKIKNAERPLMLPENVPYDITFENVTFGYHPDRKILKNASF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">TIPAGWKTAIVGSSGSGKSTILKLVFRFYDPESGRILINGRDIKEYDIDALRKVIGVVPQDTPLFNDTIWENVKFGRIDATDEEVITVVEKAQLAPLIKKLPQGFDTIVGERGLMISGGE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590        </span>
<span class="topo-line"><span class="topo-outside">KQRLAIARVLLKNARIMFFDEATSALDTHTEQALLRTIRDNFTSGSRTSVYIAHRLRTIADADKIIVLDNGRVREEGKHLELLAMPGSLYRELWTIQEDLDHLENELKDQQELWSHPQ</span></span>
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
      <td>16</td>
      <td>98</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>35</td>
      <td>114</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>61</td>
      <td>133</td>
      <td>158</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>78</td>
      <td>159</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>140</td>
      <td>176</td>
      <td>237</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>155</td>
      <td>238</td>
      <td>252</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>156</td>
      <td>159</td>
      <td>253</td>
      <td>256</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>175</td>
      <td>257</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>176</td>
      <td>246</td>
      <td>273</td>
      <td>343</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>247</td>
      <td>261</td>
      <td>344</td>
      <td>358</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>279</td>
      <td>359</td>
      <td>376</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>293</td>
      <td>377</td>
      <td>390</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>294</td>
      <td>598</td>
      <td>391</td>
      <td>695</td>
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

### Glutathione Binding Site

[GSH](/xray-mp-wiki/reagents/additives/glutathione/) binds in the large positively charged cavity formed by the Atm1 dimer, interacting with residues R280 and R284 (TM4), N343 (TM5), and N390, S394, R397, and D398 (TM6). The binding site is located close to the inner membrane surface on the matrix side. All GSH-coordinating residues are conserved in Atm1-like proteins, including human ABCB7 and bacterial homologs. One residue, D398 (corresponding to human E433), is mutated to lysine in patients with XLSA/A, demonstrating the physiological relevance of [GSH](/xray-mp-wiki/reagents/additives/glutathione/) ligand binding. [GSH](/xray-mp-wiki/reagents/additives/glutathione/) binds with an apparent Kd of 23 μM as measured by microscale thermophoresis.

### Role in Iron-Sulfur Cluster Biogenesis

Atm1, together with [GSH](/xray-mp-wiki/reagents/additives/glutathione/) ([GSH](/xray-mp-wiki/reagents/additives/glutathione/)) and the sulfhydryl oxidase Erv1, is essential for the export of a sulfur-containing molecule from mitochondria that is used by the cytosolic Fe/S protein assembly (CIA) system. This exported molecule is required for maturation of cytosolic-nuclear Fe/S proteins including DNA polymerases, primases, and helicases. The substrate may be [GSH](/xray-mp-wiki/reagents/additives/glutathione/) persulfide (GSSH) or a GSH-coordinated [2Fe-2S] cluster, both of which are consistent with the structural and biochemical data.

### C-Terminal α-Helices Stabilize the Dimer

A unique structural feature of Atm1 is the complete resolution of the C terminus, consisting of a 24-amino-acid α-helix. Two such helices from each monomer interact tightly in a crossover fashion (2.65-4.0 Å distances), stabilizing the inward-facing, open conformation. This feature has not been observed in any other ABC transporter crystal structure and likely represents a common structural element of ABC exporters that keeps the NBDs in close vicinity despite being nucleotide-free.

### Domain-Swapped Architecture

The Atm1 dimer adopts a domain-swapped arrangement where the long TM4 and TM5 helices from each monomer reach out to the other monomer, creating an intertwined, V-shaped molecule. This configuration encloses a 6900 Å³ positively charged cavity on the matrix side of the inner membrane. The two TM6 helices bend out of the membrane, forming a kink at residue S394, providing flexibility to accommodate the [GSH](/xray-mp-wiki/reagents/additives/glutathione/) ligand.

### XLSA/A Disease Mutations

Three XLSA/A patient mutations map to the Atm1 structure: E208D (long TM2 helix), I400M (between TM5 and TM6), and V411L (TM6). All mutations are conservative, indicating that even subtle changes in ABCB7 function lead to disease. The V376 (yeast) / V411L (human) mutation lies at the dimer interface, where the valine side chain undergoes hydrophobic interactions with its counterpart, tightly closing the transmembrane channel toward the intermembrane space.


## Cross-References

- <a href="/xray-mp-wiki/proteins/abc-transporters/naatm1/">NaAtm1 ABC Exporter from Novosphingobium aromaticivorans</a> — Bacterial homolog of Atm1; companion paper in same Science issue; GSH bound at similar location
- <a href="/xray-mp-wiki/proteins/abc-transporters/abcb10/">Human ABCB10 Mitochondrial ATP-Binding Cassette Transporter</a> — Related mitochondrial ABC transporter for structural comparison
- <a href="/xray-mp-wiki/reagents/additives/glutathione/">Glutathione (GSH)</a> — GSH is the bound ligand in the structure and likely a component of the exported substrate
- <a href="/xray-mp-wiki/proteins/enzymes/leut/">LeuT Amino Acid Transporter from Aquifex aeolicus</a> — Representative transporter for comparative transport mechanism studies
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/iron/">IRON</a> — Additive used in purification or crystallization buffers
