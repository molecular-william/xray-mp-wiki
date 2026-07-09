---
title: "Human Adenosine A2A Receptor (A2AR)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1164772, doi/10.1016##j.str.2011.06.014, doi/10.1038##NATURE18966, doi/10.1016##j.bbrc.2023.149393, doi/10.1016##j.str.2017.12.013, doi/10.1021##acs.jmedchem.0c01856, doi/10.1021##acs.jmedchem.2c00462, doi/10.1002##anie.202003788, doi/10.1038##NATURE10136, doi/10.1107##S2052252519013137, doi/10.1038##nature10750, doi/10.1038##s41598-020-76277-x, doi/10.1126##science.1219218, doi/10.1126##science.1202793, doi/10.1124##mol.114.097360, doi/10.1124##molpharm.122.000633, doi/10.1107##S1600576719012846, doi/10.1107##s2052252522001907, doi/10.1038##s41467-017-00630-4]
verified: regex
uniprot_id: ['P29274', 'P63092']
---

# Human Adenosine A2A Receptor (A2AR)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P29274">UniProt: P29274</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P63092">UniProt: P63092</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

The human adenosine A2A receptor (A2AR) is a class A GPCR that regulates glutamate and [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine/) release in the brain and is a therapeutic target for Parkinson's disease and cancer. The first crystal structure was determined at 2.6 A resolution using the T4 lysozyme fusion strategy, with the antagonist [ZM241385](/xray-mp-wiki/reagents/ligands/zm241385/) bound. Multiple additional structures have been solved for thermostabilized constructs (StaR2, GL31, [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) fusions) in complex with xanthine ligands, chromone antagonists, nucleoside antagonists, and in complex with mini-Gs and [Fab2838 Antibody Fragment](/xray-mp-wiki/reagents/antibodies/fab2838/), revealing details of agonist and antagonist binding, receptor activation, and G-protein coupling.


## Publications

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1126##science.1164772 (1 structure, 1 sequence)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3eml">3EML</a></td>
      <td>2.6</td>
      <td>not specified</td>
      <td>A2A-T4L-deltaC (human A2AR residues 1-316, ICL3 Leu209-Ala221 replaced with <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a>, C-terminal tail Ala317-Ser412 deleted), expressed in Sf9 insect cells</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/zm241385/">ZM241385</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: A2A-T4L-deltaC (human A2AR residues 1-316, ICL3 replaced by [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/), C-terminal tail deleted)

**Purification:**

- **Expression system**: Sf9 insect cells
- **Expression construct**: A2A-T4L-deltaC (human A2AR residues 1-316, ICL3 Leu209-Ala221 replaced with [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/), C-terminal tail Ala317-Ser412 deleted)
- **Tag info**: [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) fusion in ICL3

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
      <td>Protein expression</td>
      <td>Baculovirus expression in Sf9 cells</td>
      <td>--</td>
      <td>not specified + --</td>
      <td>Receptor stabilized during purification with NaCl, saturating <a href="/xray-mp-wiki/reagents/ligands/theophylline/">Theophylline</a>, and cholesteryl hemisuccinate (<a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>)</td>
    </tr>
    <tr>
      <td>Ligand exchange</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/theophylline/">Theophylline</a> to <a href="/xray-mp-wiki/reagents/ligands/zm241385/">ZM241385</a> exchange</td>
      <td>--</td>
      <td>not specified + --</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/zm241385/">ZM241385</a> exchanged from <a href="/xray-mp-wiki/reagents/ligands/theophylline/">Theophylline</a> in the last purification step</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>In meso (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">[LCP</a>](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/))</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified A2A-<a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a>-deltaC bound to <a href="/xray-mp-wiki/reagents/ligands/zm241385/">ZM241385</a></td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> and <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> mixture</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Diffraction data from 13 crystals combined to yield 2.6 A dataset. Phases obtained by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using beta2AR-<a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> (PDB 2RH1). Final model includes residues Ile3-Gln310 of <a href="/xray-mp-wiki/proteins/human-adenosine-a2a-receptor-a2ar/">A2AR</a>, residues 2-161 of <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a>, five stearic acid lipids, eight sulfate ions, and <a href="/xray-mp-wiki/reagents/ligands/zm241385/">ZM241385</a>.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3eml">3EML</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">DYKDDDDAMGQPVGAPP</span><span class="topo-outside">IMGSS</span><span class="topo-membrane">VYITVELAIAVLAILGNVLVCWA</span><span class="topo-inside">VWLNSNLQNVT</span><span class="topo-membrane">NYFVVSLAAADIAVGVLAIPFAITI</span><span class="topo-outside">STGFCAACHGCL</span><span class="topo-membrane">FIACFVLVLTQSSIFSLLAIAIDRY</span><span class="topo-inside">IA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">IRIPLRYNGLVTGTR</span><span class="topo-membrane">AKGIIAICWVLSFAIGLTPMLGW</span><span class="topo-outside">NNCGQ</span><span class="topo-unknown">PKEGKNH</span><span class="topo-outside">SQGCGEGQVACLFEDVVPMN</span><span class="topo-membrane">YMVYFNFFACVLVPLLLMLGVYLRIFL</span><span class="topo-inside">AARRQLNIFEMLRIDEGLRLKIY</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">KDTEGYYTIGIGHLLTKSPSLNAAKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRW</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">YNQTPNRAKRVITTFRTGTWDAYRSTLQKEVHAA</span><span class="topo-membrane">KSLAIIVGLFALCWLPLHIINC</span><span class="topo-outside">FTFFCPDCSHAPLWL</span><span class="topo-membrane">MYLAIVLSHTNSVVNPFIYAYR</span><span class="topo-inside">I</span><span class="topo-unknown">REFRQTFRKIIRS</span><span class="topo-inside">HVLRQ</span><span class="topo-unknown">QEPFKAHH</span></span>
<span class="topo-ruler">        </span>
<span class="topo-line"><span class="topo-unknown">HHHHHHHH</span></span>
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
      <td>17</td>
      <td>-14</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>18</td>
      <td>22</td>
      <td>3</td>
      <td>7</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>45</td>
      <td>8</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>46</td>
      <td>56</td>
      <td>31</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>81</td>
      <td>42</td>
      <td>66</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>93</td>
      <td>67</td>
      <td>78</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>118</td>
      <td>79</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>135</td>
      <td>104</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>136</td>
      <td>158</td>
      <td>121</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>159</td>
      <td>163</td>
      <td>144</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>170</td>
      <td>149</td>
      <td>155</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>171</td>
      <td>190</td>
      <td>156</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>217</td>
      <td>176</td>
      <td>202</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>394</td>
      <td>203</td>
      <td>232</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>416</td>
      <td>233</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>417</td>
      <td>431</td>
      <td>255</td>
      <td>269</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>432</td>
      <td>453</td>
      <td>270</td>
      <td>291</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>454</td>
      <td>454</td>
      <td>292</td>
      <td>292</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>455</td>
      <td>467</td>
      <td>293</td>
      <td>305</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>468</td>
      <td>472</td>
      <td>306</td>
      <td>310</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>473</td>
      <td>488</td>
      <td>311</td>
      <td>326</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1016##j.str.2011.06.014 (3 structures, 3 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3pwh">3PWH</a></td>
      <td>3.29</td>
      <td>I222</td>
      <td>A2A-StaR2 (human A2AR with thermostabilizing mutations A54L, T88A, R107A, K122A, N154A, L202A, L235A, V239A, S277A), expressed in baculovirus/Sf9 system, purified in <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td><a href="/xray-mp-wiki/reagents/ligands/zm241385/">ZM241385</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3rey">3REY</a></td>
      <td>3.30</td>
      <td>I222</td>
      <td>A2A-StaR2 as above</td>
      <td>XAC</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3rfm">3RFM</a></td>
      <td>3.60</td>
      <td>I222</td>
      <td>A2A-StaR2 as above</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/caffeine/">Caffeine</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: A2A-T4L-deltaC (human A2AR residues 1-316, ICL3 replaced by [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/), C-terminal tail deleted)

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3pwh">3PWH</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MPIMGS</span><span class="topo-outside">SVY</span><span class="topo-membrane">ITVELAIAVLAILGNVLVCWAVWL</span><span class="topo-inside">NSNLQNV</span><span class="topo-membrane">TNYFVVSLAAADILVGVLAIPFA</span><span class="topo-outside">ITISTGFCAACHGCLFIAC</span><span class="topo-membrane">FVLVLAQSSIFSLLAIAIDRY</span><span class="topo-inside">IAIAIPLRYNGLVTG</span><span class="topo-membrane">TR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">AAGIIAICWVLSFAIGLT</span><span class="topo-outside">PMLGWNNCGQP</span><span class="topo-unknown">KEGKNHSQ</span><span class="topo-outside">GCGEGQVACLFEDVVPMNYM</span><span class="topo-membrane">VYFNFFACVLVPLLLMLGVYLRIFA</span><span class="topo-inside">AARRQLKQMESQPLPGERARSTLQKEVHA</span><span class="topo-membrane">AKSAAIIAG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320         </span>
<span class="topo-line"><span class="topo-membrane">LFALCWLPLHII</span><span class="topo-outside">NCFTFFCPDCSHAPLWLMYL</span><span class="topo-membrane">AIVLAHTNSVVNPFIYAYRI</span><span class="topo-inside">REFRQTFRKIIRS</span><span class="topo-unknown">HVLRQQEPFKAAAAHHHHHHHHHH</span></span>
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
      <td>6</td>
      <td>1</td>
      <td>6</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>7</td>
      <td>9</td>
      <td>7</td>
      <td>9</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>33</td>
      <td>10</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>40</td>
      <td>34</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>63</td>
      <td>41</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>82</td>
      <td>64</td>
      <td>82</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>103</td>
      <td>83</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>104</td>
      <td>118</td>
      <td>104</td>
      <td>118</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>138</td>
      <td>119</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>149</td>
      <td>139</td>
      <td>149</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>150</td>
      <td>157</td>
      <td>150</td>
      <td>157</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>158</td>
      <td>177</td>
      <td>158</td>
      <td>177</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>202</td>
      <td>178</td>
      <td>202</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>203</td>
      <td>231</td>
      <td>203</td>
      <td>231</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>232</td>
      <td>252</td>
      <td>232</td>
      <td>252</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>253</td>
      <td>272</td>
      <td>253</td>
      <td>272</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>273</td>
      <td>292</td>
      <td>273</td>
      <td>292</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>293</td>
      <td>305</td>
      <td>293</td>
      <td>305</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>306</td>
      <td>329</td>
      <td>306</td>
      <td>329</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3rey">3REY</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MPIMGS</span><span class="topo-outside">SVY</span><span class="topo-membrane">ITVELAIAVLAILGNVLVCWAVW</span><span class="topo-inside">LNSNLQNVTN</span><span class="topo-membrane">YFVVSLAAADILVGVLAIPFAI</span><span class="topo-outside">TISTGFCAACHGCL</span><span class="topo-membrane">FIACFVLVLAQSSIFSLLAIAID</span><span class="topo-inside">RYIAIAIPLRYNGLVTGTR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">A</span><span class="topo-membrane">AGIIAICWVLSFAIGLTPMLGW</span><span class="topo-outside">NNCGQP</span><span class="topo-unknown">KEGKNHSQ</span><span class="topo-outside">GCGEGQVACLFEDVVPM</span><span class="topo-membrane">NYMVYFNFFACVLVPLLLMLGVYLR</span><span class="topo-inside">IFAAARRQLKQMESQPLPGERARSTLQKEVHAA</span><span class="topo-membrane">KSAAIIAG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320         </span>
<span class="topo-line"><span class="topo-membrane">LFALCWLPLHIINCF</span><span class="topo-outside">TFFCPDCSHAPLWLMY</span><span class="topo-membrane">LAIVLAHTNSVVNPFIYAYRI</span><span class="topo-inside">REFRQTFRKIIRS</span><span class="topo-unknown">HVLRQQEPFKAAAAHHHHHHHHHH</span></span>
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
      <td>6</td>
      <td>1</td>
      <td>6</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>7</td>
      <td>9</td>
      <td>7</td>
      <td>9</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>32</td>
      <td>10</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>42</td>
      <td>33</td>
      <td>42</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>64</td>
      <td>43</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>78</td>
      <td>65</td>
      <td>78</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>101</td>
      <td>79</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>121</td>
      <td>102</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>143</td>
      <td>122</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>144</td>
      <td>149</td>
      <td>144</td>
      <td>149</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>150</td>
      <td>157</td>
      <td>150</td>
      <td>157</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>158</td>
      <td>174</td>
      <td>158</td>
      <td>174</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>175</td>
      <td>199</td>
      <td>175</td>
      <td>199</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>200</td>
      <td>232</td>
      <td>200</td>
      <td>232</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>233</td>
      <td>255</td>
      <td>233</td>
      <td>255</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>256</td>
      <td>271</td>
      <td>256</td>
      <td>271</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>272</td>
      <td>292</td>
      <td>272</td>
      <td>292</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>293</td>
      <td>305</td>
      <td>293</td>
      <td>305</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>306</td>
      <td>329</td>
      <td>306</td>
      <td>329</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3rfm">3RFM</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MPIMGS</span><span class="topo-inside">SVY</span><span class="topo-membrane">ITVELAIAVLAILGNVLVCWAVWL</span><span class="topo-outside">NSNLQNV</span><span class="topo-membrane">TNYFVVSLAAADILVGVLAIPFA</span><span class="topo-inside">ITISTGFCAACHGCLF</span><span class="topo-membrane">IACFVLVLAQSSIFSLLAIAIDR</span><span class="topo-outside">YIAIAIPLRYNGLVTG</span><span class="topo-membrane">TR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">AAGIIAICWVLSFAIGLTPML</span><span class="topo-inside">GWNNCGQP</span><span class="topo-unknown">KEGKNHSQ</span><span class="topo-inside">GCGEGQVACLFEDVVPMN</span><span class="topo-membrane">YMVYFNFFACVLVPLLLMLGVYLR</span><span class="topo-outside">IFAAARRQLKQMESQPLPGERARSTLQKEVHAA</span><span class="topo-membrane">KSAAIIAG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320         </span>
<span class="topo-line"><span class="topo-membrane">LFALCWLPLHIINCF</span><span class="topo-inside">TFFCPDCSHAPLWLMY</span><span class="topo-membrane">LAIVLAHTNSVVNPFIYAYRI</span><span class="topo-outside">REFRQTFRKIIRS</span><span class="topo-unknown">HVLRQQEPFKAAAAHHHHHHHHHH</span></span>
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
      <td>6</td>
      <td>1</td>
      <td>6</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>7</td>
      <td>9</td>
      <td>7</td>
      <td>9</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>33</td>
      <td>10</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>40</td>
      <td>34</td>
      <td>40</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>63</td>
      <td>41</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>79</td>
      <td>64</td>
      <td>79</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>102</td>
      <td>80</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>118</td>
      <td>103</td>
      <td>118</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>141</td>
      <td>119</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>149</td>
      <td>142</td>
      <td>149</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>150</td>
      <td>157</td>
      <td>150</td>
      <td>157</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>158</td>
      <td>175</td>
      <td>158</td>
      <td>175</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>199</td>
      <td>176</td>
      <td>199</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>200</td>
      <td>232</td>
      <td>200</td>
      <td>232</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>233</td>
      <td>255</td>
      <td>233</td>
      <td>255</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>256</td>
      <td>271</td>
      <td>256</td>
      <td>271</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>272</td>
      <td>292</td>
      <td>272</td>
      <td>292</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>293</td>
      <td>305</td>
      <td>293</td>
      <td>305</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>306</td>
      <td>329</td>
      <td>306</td>
      <td>329</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1038##NATURE18966 (1 structure, 2 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5g53">5G53</a></td>
      <td>3.4</td>
      <td>P 2_1 2_1 2_1</td>
      <td>Wild-type human A2AR (residues 1-308), C-terminal His10 tag with TEV protease cleavage site, N154A mutation, in complex with engineered mini-Gs</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/neca/">NECA</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: A2A-T4L-deltaC (human A2AR residues 1-316, ICL3 replaced by [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/), C-terminal tail deleted)

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5g53">5G53</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MPIMG</span><span class="topo-outside">SSV</span><span class="topo-membrane">YITVELAIAVLAILGNVLVCWA</span><span class="topo-inside">VWLNSNLQNVTN</span><span class="topo-membrane">YFVVSLAAADIAVGVLAIPFAI</span><span class="topo-outside">TISTGFCAACHGCLFI</span><span class="topo-membrane">ACFVLVLTQSSIFSLLAIAID</span><span class="topo-inside">RYIAIRIPLRYNGLVTGT</span><span class="topo-membrane">R</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">AKGIIAICWVLSFAIGLT</span><span class="topo-outside">PMLGWNNC</span><span class="topo-unknown">GQPKEGKAHSQG</span><span class="topo-outside">CGEGQVACLFEDVVPMNY</span><span class="topo-membrane">MVYFNFFACVLVPLLLMLGVYLR</span><span class="topo-inside">IFLAARRQLKQM</span><span class="topo-unknown">ESQPLPGERARS</span><span class="topo-inside">TLQKEVHAA</span><span class="topo-membrane">KSLAIIVG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310    </span>
<span class="topo-line"><span class="topo-membrane">LFALCWLPLHIINC</span><span class="topo-outside">FTFFCPDCSHAPLWL</span><span class="topo-membrane">MYLAIVLSHTNSVVNPFIYAY</span><span class="topo-inside">RI</span><span class="topo-unknown">REFRQTFRKIIRSHVLEN</span><span class="topo-inside">LY</span><span class="topo-unknown">FQ</span></span>
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
      <td>6</td>
      <td>8</td>
      <td>6</td>
      <td>8</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>30</td>
      <td>9</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>42</td>
      <td>31</td>
      <td>42</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>64</td>
      <td>43</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>80</td>
      <td>65</td>
      <td>80</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>101</td>
      <td>81</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>119</td>
      <td>102</td>
      <td>119</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>120</td>
      <td>138</td>
      <td>120</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>146</td>
      <td>139</td>
      <td>146</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>176</td>
      <td>159</td>
      <td>176</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>199</td>
      <td>177</td>
      <td>199</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>200</td>
      <td>211</td>
      <td>200</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>224</td>
      <td>232</td>
      <td>224</td>
      <td>232</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>233</td>
      <td>254</td>
      <td>233</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>255</td>
      <td>269</td>
      <td>255</td>
      <td>269</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>270</td>
      <td>290</td>
      <td>270</td>
      <td>290</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>291</td>
      <td>292</td>
      <td>291</td>
      <td>292</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>310</td>
      <td>293</td>
      <td>310</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>311</td>
      <td>312</td>
      <td>311</td>
      <td>312</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5g53">5G53</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GIEKQLQKDKQVYRA</span><span class="topo-inside">THRLLLLGADNSGKSTIVKQMR</span><span class="topo-unknown">IYHGGSGGSGGTSGI</span><span class="topo-inside">FETKFQVDKVNFHMFDVGGQRDERRKWIQCFNDVTAIIFVVDSSDYNRLQEALNDFKSIWNNRWLRTI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220         </span>
<span class="topo-line"><span class="topo-inside">SVILFLNKQDLLAEKVLAGKSKIEDYFPEFARYTTPEDATPEPGEDPRVTRAKYFIRDEFLRISTASGDGRHYCYPHFTC</span><span class="topo-unknown">AVD</span><span class="topo-inside">TENARRIFNDCRDIIQRMHLRQYELL</span></span>
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
      <td>16</td>
      <td>37</td>
      <td>40</td>
      <td>61</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>200</td>
      <td>208</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>229</td>
      <td>369</td>
      <td>394</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1016##j.bbrc.2023.149393 (1 structure, 1 sequence)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8wdt">8WDT</a></td>
      <td>3.34</td>
      <td>not specified</td>
      <td>Thermostabilized mutant A2AR-Rag31</td>
      <td>trans-photoNECA</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: A2A-T4L-deltaC (human A2AR residues 1-316, ICL3 replaced by [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/), C-terminal tail deleted)

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8wdt">8WDT</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFADYKDDDDGAPP</span><span class="topo-outside">IMGS</span><span class="topo-membrane">SVYITVELAIAVLAILGNVLVCWAV</span><span class="topo-inside">WLNSNLQNVT</span><span class="topo-membrane">NYFVVSLAAADIAVGVLAIPFAITIS</span><span class="topo-outside">TGFCAACHG</span><span class="topo-membrane">CLAIACFVLVLTQSSIFSL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LAIAIDRYI</span><span class="topo-inside">AIRIPLRYNGLVTGT</span><span class="topo-membrane">RAKGIIAICWVLSFAIGLTPML</span><span class="topo-outside">GWNNCG</span><span class="topo-unknown">QPKEGKQH</span><span class="topo-outside">SQGCGEGQVACLFEDVVPM</span><span class="topo-membrane">NYMVYFNFFLCVLVPLLLMLGVYLAIFL</span><span class="topo-inside">AARRQAKQMESQP</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350 </span>
<span class="topo-line"><span class="topo-inside">LPGERARSTLQKEVHA</span><span class="topo-membrane">AKSLAIIVGLFALCWLPLHIINCF</span><span class="topo-outside">TFFCPDCSHAPLW</span><span class="topo-membrane">LMYAAIVLSHTNSVVNPFIYAYR</span><span class="topo-inside">IREFRQTFRKIIRSHV</span><span class="topo-unknown">LRQQEPFKAHHHHHHHHHH</span></span>
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
      <td>27</td>
      <td>-24</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>31</td>
      <td>3</td>
      <td>6</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>56</td>
      <td>7</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>66</td>
      <td>32</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>92</td>
      <td>42</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>101</td>
      <td>68</td>
      <td>76</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>129</td>
      <td>77</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>130</td>
      <td>144</td>
      <td>105</td>
      <td>119</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>166</td>
      <td>120</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>172</td>
      <td>142</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>180</td>
      <td>148</td>
      <td>155</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>181</td>
      <td>199</td>
      <td>156</td>
      <td>174</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>227</td>
      <td>175</td>
      <td>202</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>228</td>
      <td>256</td>
      <td>203</td>
      <td>231</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>257</td>
      <td>280</td>
      <td>232</td>
      <td>255</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>281</td>
      <td>293</td>
      <td>256</td>
      <td>268</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>316</td>
      <td>269</td>
      <td>291</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>317</td>
      <td>332</td>
      <td>292</td>
      <td>307</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>351</td>
      <td>308</td>
      <td>326</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1016##j.str.2017.12.013 (2 structures, 2 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5wf5">5WF5</a></td>
      <td>2.60</td>
      <td>P21</td>
      <td>A2AAR-<a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> D52N variant truncated after residue 316, N-terminal <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a>, C-terminal His10 tag, ICL3 replaced by cysteine-free <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a></td>
      <td><a href="/xray-mp-wiki/reagents/ligands/uk-432097/">UK432097</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5wf6">5WF6</a></td>
      <td>2.90</td>
      <td>P21</td>
      <td>A2AAR-<a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> S91A variant truncated after residue 316, N-terminal <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a>, C-terminal His10 tag, ICL3 replaced by cysteine-free <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a></td>
      <td><a href="/xray-mp-wiki/reagents/ligands/uk-432097/">UK432097</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: A2A-T4L-deltaC (human A2AR residues 1-316, ICL3 replaced by [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/), C-terminal tail deleted)

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5wf5">5WF5</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFADYKDDDDAMGQPVGAPP</span><span class="topo-outside">IMG</span><span class="topo-membrane">SSVYITVELAIAVLAILGNV</span><span class="topo-inside">LVCWAVWLNSNLQNVTNYFVVSL</span><span class="topo-membrane">AAANIAVGVLAIPFAITIS</span><span class="topo-outside">TGFCAAC</span><span class="topo-membrane">HGCLFIACFVLVLTQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">SSIF</span><span class="topo-inside">SLLAIAIDRYIAIRIPLRYNGLVTGTRAKGIIAIC</span><span class="topo-membrane">WVLSFAIGLTPMLGWNNC</span><span class="topo-outside">GQ</span><span class="topo-unknown">PKEGKNHS</span><span class="topo-outside">QGCGEGQVACL</span><span class="topo-membrane">FEDVVPMNYMVYFNFFACVLVPLL</span><span class="topo-inside">LMLGVYLRIFLAARRQLN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">IFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQ</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">QKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYRSTLQKEVHAAKSLAIIV</span><span class="topo-membrane">GLFALCWLPLHIINCFTFFC</span><span class="topo-outside">PDCSH</span><span class="topo-membrane">APLWLMYLAIVLSHTNSVVN</span><span class="topo-inside">PFIYAYRI</span><span class="topo-unknown">REFRQTFRKI</span></span>
<span class="topo-ruler">       490       500    </span>
<span class="topo-line"><span class="topo-unknown">IRSH</span><span class="topo-inside">V</span><span class="topo-unknown">LRQQEPFKAHHHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (18 regions)</summary>
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
      <td>34</td>
      <td>36</td>
      <td>3</td>
      <td>5</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>56</td>
      <td>6</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>79</td>
      <td>26</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>98</td>
      <td>49</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>99</td>
      <td>105</td>
      <td>68</td>
      <td>74</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>124</td>
      <td>75</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>159</td>
      <td>94</td>
      <td>128</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>177</td>
      <td>129</td>
      <td>146</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>179</td>
      <td>147</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>188</td>
      <td>198</td>
      <td>157</td>
      <td>167</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>222</td>
      <td>168</td>
      <td>191</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>223</td>
      <td>417</td>
      <td>192</td>
      <td>239</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>418</td>
      <td>437</td>
      <td>240</td>
      <td>259</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>438</td>
      <td>442</td>
      <td>260</td>
      <td>264</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>462</td>
      <td>265</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>463</td>
      <td>470</td>
      <td>285</td>
      <td>292</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>484</td>
      <td>293</td>
      <td>306</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>485</td>
      <td>485</td>
      <td>307</td>
      <td>307</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5wf6">5WF6</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFADYKDDDDAMGQPVGAPP</span><span class="topo-outside">IMGS</span><span class="topo-membrane">SVYITVELAIAVLAILGNV</span><span class="topo-inside">LVCWAVWLNSNLQNVTNYFVVSL</span><span class="topo-membrane">AAADIAVGVLAIPFAITIS</span><span class="topo-outside">TGFCAACH</span><span class="topo-membrane">GCLFIACFVLVLTQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">SAIFSL</span><span class="topo-inside">LAIAIDRYIAIRIPLRYNGLVTGTRAKGIIAI</span><span class="topo-membrane">CWVLSFAIGLTPMLGWN</span><span class="topo-outside">NC</span><span class="topo-unknown">GQPKEGKNHSQ</span><span class="topo-outside">GCGEGQVACLFEDV</span><span class="topo-membrane">VPMNYMVYFNFFACVLVPLLL</span><span class="topo-inside">MLGVYLRIFLAARRQLN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">IFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQ</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">QKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYRSTLQKEVHAAKSLAI</span><span class="topo-membrane">IVGLFALCWLPLHIINCFTFFC</span><span class="topo-outside">PDCSHAPLW</span><span class="topo-membrane">LMYLAIVLSHTNSVVNPF</span><span class="topo-inside">IYAYRI</span><span class="topo-unknown">REFRQTFRKI</span></span>
<span class="topo-ruler">       490       500    </span>
<span class="topo-line"><span class="topo-unknown">IRSH</span><span class="topo-inside">V</span><span class="topo-unknown">LRQQEPFKAHHHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (18 regions)</summary>
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
      <td>34</td>
      <td>37</td>
      <td>3</td>
      <td>6</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>56</td>
      <td>7</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>79</td>
      <td>26</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>98</td>
      <td>49</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>99</td>
      <td>106</td>
      <td>68</td>
      <td>75</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>107</td>
      <td>126</td>
      <td>76</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>127</td>
      <td>158</td>
      <td>96</td>
      <td>127</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>175</td>
      <td>128</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>176</td>
      <td>177</td>
      <td>145</td>
      <td>146</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>202</td>
      <td>158</td>
      <td>171</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>223</td>
      <td>172</td>
      <td>192</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>415</td>
      <td>193</td>
      <td>237</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>416</td>
      <td>437</td>
      <td>238</td>
      <td>259</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>438</td>
      <td>446</td>
      <td>260</td>
      <td>268</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>447</td>
      <td>464</td>
      <td>269</td>
      <td>286</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>465</td>
      <td>470</td>
      <td>287</td>
      <td>292</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>484</td>
      <td>293</td>
      <td>306</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>485</td>
      <td>485</td>
      <td>307</td>
      <td>307</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1021##acs.jmedchem.0c01856 (1 structure, 1 sequence)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7aro">7ARO</a></td>
      <td>1.9</td>
      <td>P212121</td>
      <td>A2A-StaR2-<a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a> with 9 thermostabilizing mutations, N-terminal deletion, C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> after L315, <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a> fused into ICL3</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/luf5833/">LUF5833 (Compound 8)</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: A2A-T4L-deltaC (human A2AR residues 1-316, ICL3 replaced by [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/), C-terminal tail deleted)

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7aro">7ARO</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">DYKDDDD</span><span class="topo-outside">GAPPIMGSS</span><span class="topo-membrane">VYITVELAIAVLAILGNVLVCWAVWL</span><span class="topo-inside">NSNLQNV</span><span class="topo-membrane">TNYFVVSLAAADILVGVLAIPFAIT</span><span class="topo-outside">ISTGFCAACHGCL</span><span class="topo-membrane">FIACFVLVLAQSSIFSLLAIAIDR</span><span class="topo-inside">YIAIAIPLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">YNGLVTG</span><span class="topo-membrane">TRAAGIIAICWVLSFAIGLTPMLGW</span><span class="topo-outside">NNCGQPKEGKAHSQGCGEGQVACLFEDVVPM</span><span class="topo-membrane">NYMVYFNFFACVLVPLLLMLGVYLR</span><span class="topo-inside">IFAAARRQLADLEDNWETLNDNLKVIEKADNA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">AQVKDALTKMRAAALDAQ</span><span class="topo-unknown">KATPPKLEDKSPDSPEMKDFRH</span><span class="topo-inside">GFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLERARSTLQKEVHAA</span><span class="topo-membrane">KSAAIIAGLFALCWLPLHIINCF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430   </span>
<span class="topo-line"><span class="topo-outside">TFFCPDCSHAPLW</span><span class="topo-membrane">LMYLAIVLAHTNSVVNPFIYAYR</span><span class="topo-inside">IREFRQTFRKIIRS</span><span class="topo-unknown">HVLRQQEPFKAAAHHHHHHHHHH</span></span>
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
      <td>-8</td>
      <td>-2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>16</td>
      <td>-1</td>
      <td>7</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>42</td>
      <td>8</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>43</td>
      <td>49</td>
      <td>34</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>50</td>
      <td>74</td>
      <td>41</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>87</td>
      <td>66</td>
      <td>78</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>111</td>
      <td>79</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>127</td>
      <td>103</td>
      <td>118</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>128</td>
      <td>152</td>
      <td>119</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>153</td>
      <td>183</td>
      <td>144</td>
      <td>174</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>208</td>
      <td>175</td>
      <td>199</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>209</td>
      <td>217</td>
      <td>200</td>
      <td>208</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>258</td>
      <td>1001</td>
      <td>1041</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>280</td>
      <td>1042</td>
      <td>1063</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>281</td>
      <td>323</td>
      <td>1064</td>
      <td>1106</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>324</td>
      <td>337</td>
      <td>219</td>
      <td>232</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>360</td>
      <td>233</td>
      <td>255</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>361</td>
      <td>373</td>
      <td>256</td>
      <td>268</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>374</td>
      <td>396</td>
      <td>269</td>
      <td>291</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>410</td>
      <td>292</td>
      <td>305</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>411</td>
      <td>433</td>
      <td>306</td>
      <td>328</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1021##acs.jmedchem.2c00462 (2 structures, 2 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8cu7">8CU7</a></td>
      <td>2.05</td>
      <td>not specified</td>
      <td>A2A-StaR2-<a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a> with StaR2 mutations, N-terminal deletion, C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> after L315, <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a> fused into ICL3</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/lj-4517/">LJ-4517 (Compound 2)</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8cu6">8CU6</a></td>
      <td>2.80</td>
      <td>not specified</td>
      <td>A2A-StaR2-S277-<a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a> with StaR2 mutations, N-terminal deletion, C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> after L315, <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a> fused into ICL3</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/lj-4517/">LJ-4517 (Compound 2)</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: A2A-T4L-deltaC (human A2AR residues 1-316, ICL3 replaced by [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/), C-terminal tail deleted)

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8cu7">8CU7</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFADYKDD</span><span class="topo-inside">DDGAPPIMGSS</span><span class="topo-membrane">VYITVELAIAVLAILGNVLVCWAVWL</span><span class="topo-outside">NSNLQNV</span><span class="topo-membrane">TNYFVVSLAAADILVGVLAIPFAIT</span><span class="topo-inside">ISTGFCAACHGCLF</span><span class="topo-membrane">IACFVLVLAQSSIFSL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LAIAIDRY</span><span class="topo-outside">IAIAIPLRYNGLVTG</span><span class="topo-membrane">TRAAGIIAICWVLSFAIGLTPML</span><span class="topo-inside">GWNNCGQPKEGKAHSQGCGEGQVACLFEDVVPM</span><span class="topo-membrane">NYMVYFNFFACVLVPLLLMLGVYLRI</span><span class="topo-outside">FAAARRQLADLEDNW</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQK</span><span class="topo-unknown">ATPPKLEDKSPD</span><span class="topo-outside">SPEMKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLERARSTLQKEVHAA</span><span class="topo-membrane">KSAAIIA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       </span>
<span class="topo-line"><span class="topo-membrane">GLFALCWLPLHIINCF</span><span class="topo-inside">TFFCPDCSHAPLW</span><span class="topo-membrane">LMYLAIVLAHTNSVVNPFIYAYR</span><span class="topo-outside">IREFRQTFRKIIRSHVL</span><span class="topo-unknown">RQQEPFKAHHHHHHHHHH</span></span>
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
      <td>21</td>
      <td>-24</td>
      <td>-4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>32</td>
      <td>-3</td>
      <td>7</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>58</td>
      <td>8</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>59</td>
      <td>65</td>
      <td>34</td>
      <td>40</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>90</td>
      <td>41</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>104</td>
      <td>66</td>
      <td>79</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>128</td>
      <td>80</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>143</td>
      <td>104</td>
      <td>118</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>144</td>
      <td>166</td>
      <td>119</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>199</td>
      <td>142</td>
      <td>174</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>225</td>
      <td>175</td>
      <td>200</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>226</td>
      <td>233</td>
      <td>201</td>
      <td>208</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>275</td>
      <td>1001</td>
      <td>1042</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>276</td>
      <td>287</td>
      <td>1043</td>
      <td>1054</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>288</td>
      <td>339</td>
      <td>1055</td>
      <td>1106</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>353</td>
      <td>219</td>
      <td>232</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>354</td>
      <td>376</td>
      <td>233</td>
      <td>255</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>377</td>
      <td>389</td>
      <td>256</td>
      <td>268</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>412</td>
      <td>269</td>
      <td>291</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>413</td>
      <td>429</td>
      <td>292</td>
      <td>308</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>430</td>
      <td>447</td>
      <td>309</td>
      <td>326</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8cu6">8CU6</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFADYKDDDDG</span><span class="topo-outside">APPIM</span><span class="topo-membrane">GSSVYITVELAIAVLAILGNVLVCW</span><span class="topo-inside">AVWLNSNLQNVTNY</span><span class="topo-membrane">FVVSLAAADILVGVLAIPFAITIST</span><span class="topo-outside">GFCAACH</span><span class="topo-membrane">GCLFIACFVLVLAQSSIFSL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LAIA</span><span class="topo-inside">IDRYIAIAIPLRYNGLVTGTRAA</span><span class="topo-membrane">GIIAICWVLSFAIGLTPMLGWN</span><span class="topo-outside">NCGQPKEGKAHSQGCGEGQVACLFEDV</span><span class="topo-membrane">VPMNYMVYFNFFACVLVPLLLMLGVY</span><span class="topo-inside">LRIFAAARRQLADLEDNW</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">ETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQK</span><span class="topo-unknown">ATPPKLEDKSPD</span><span class="topo-inside">SPEMKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLERARSTLQKEVHAAKSA</span><span class="topo-membrane">AIIA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       </span>
<span class="topo-line"><span class="topo-membrane">GLFALCWLPLHIINCFTFFC</span><span class="topo-outside">PDCSH</span><span class="topo-membrane">APLWLMYLAIVLSHTNSVVNPFI</span><span class="topo-inside">YAYRIREFRQTFRKIIRSHVL</span><span class="topo-unknown">RQQEPFKAHHHHHHHHHH</span></span>
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
      <td>24</td>
      <td>-24</td>
      <td>-1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>0</td>
      <td>4</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>54</td>
      <td>5</td>
      <td>29</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>68</td>
      <td>30</td>
      <td>43</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>93</td>
      <td>44</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>100</td>
      <td>69</td>
      <td>75</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>124</td>
      <td>76</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>147</td>
      <td>100</td>
      <td>122</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>169</td>
      <td>123</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>196</td>
      <td>145</td>
      <td>171</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>197</td>
      <td>222</td>
      <td>172</td>
      <td>197</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>223</td>
      <td>233</td>
      <td>198</td>
      <td>208</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>275</td>
      <td>1001</td>
      <td>1042</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>276</td>
      <td>287</td>
      <td>1043</td>
      <td>1054</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>288</td>
      <td>339</td>
      <td>1055</td>
      <td>1106</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>356</td>
      <td>219</td>
      <td>235</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>357</td>
      <td>380</td>
      <td>236</td>
      <td>259</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>381</td>
      <td>385</td>
      <td>260</td>
      <td>264</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>386</td>
      <td>408</td>
      <td>265</td>
      <td>287</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>429</td>
      <td>288</td>
      <td>308</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>430</td>
      <td>447</td>
      <td>309</td>
      <td>326</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1002##anie.202003788 (1 structure, 1 sequence)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6zdr">6ZDR</a></td>
      <td>2.13</td>
      <td>not specified</td>
      <td>A2AAR-STAR2 (StaR2-<a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a> thermostabilized construct)</td>
      <td>Chromone 5d</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: A2A-T4L-deltaC (human A2AR residues 1-316, ICL3 replaced by [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/), C-terminal tail deleted)

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zdr">6ZDR</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">DYKDDDDG</span><span class="topo-inside">APPIMGSSV</span><span class="topo-membrane">YITVELAIAVLAILGNVLVCWAVWL</span><span class="topo-outside">NSNLQNVT</span><span class="topo-membrane">NYFVVSLAAADILVGVLAIPFAIT</span><span class="topo-inside">ISTGFCAACHGCL</span><span class="topo-membrane">FIACFVLVLAQSSIFSLLAIAID</span><span class="topo-outside">RYIAIAIPLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">YNGLVTGTR</span><span class="topo-membrane">AAGIIAICWVLSFAIGLTPMLGWN</span><span class="topo-inside">NCGQPKEGKAHSQGCGEGQVACLFEDVV</span><span class="topo-membrane">PMNYMVYFNFFACVLVPLLLMLGVYL</span><span class="topo-outside">RIFAAARRQLADLEDNWETLNDNLKVIEKADNA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">AQVKDALTKMRAAALDAQK</span><span class="topo-unknown">ATPPKLEDKSPDSPEMKDF</span><span class="topo-outside">RHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLERARSTLQKEVHAA</span><span class="topo-membrane">KSAAIIAGLFALCWLPLHIINCF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430   </span>
<span class="topo-line"><span class="topo-membrane">TFF</span><span class="topo-inside">CPDCSHAPLWL</span><span class="topo-membrane">MYLAIVLAHTNSVVNPFIYAYRI</span><span class="topo-outside">REFRQTFRKIIRS</span><span class="topo-unknown">HVLRQQEPFKAAAHHHHHHHHHH</span></span>
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
      <td>8</td>
      <td>-8</td>
      <td>-1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>17</td>
      <td>0</td>
      <td>8</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>42</td>
      <td>9</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>43</td>
      <td>50</td>
      <td>34</td>
      <td>41</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>74</td>
      <td>42</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>87</td>
      <td>66</td>
      <td>78</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>110</td>
      <td>79</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>129</td>
      <td>102</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>153</td>
      <td>121</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>154</td>
      <td>181</td>
      <td>145</td>
      <td>172</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>207</td>
      <td>173</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>217</td>
      <td>199</td>
      <td>208</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>259</td>
      <td>1001</td>
      <td>1042</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>260</td>
      <td>278</td>
      <td>1043</td>
      <td>1061</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>279</td>
      <td>323</td>
      <td>1062</td>
      <td>1106</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>324</td>
      <td>337</td>
      <td>219</td>
      <td>232</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>363</td>
      <td>233</td>
      <td>258</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>374</td>
      <td>259</td>
      <td>269</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>375</td>
      <td>397</td>
      <td>270</td>
      <td>292</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>398</td>
      <td>410</td>
      <td>293</td>
      <td>305</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>411</td>
      <td>433</td>
      <td>306</td>
      <td>328</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1038##NATURE10136 (1 structure, 1 sequence)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2ydo">2YDO</a></td>
      <td>3.0</td>
      <td>C2</td>
      <td>A2AR-GL31 thermostabilized mutant as above</td>
      <td>Adenosine</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: A2A-T4L-deltaC (human A2AR residues 1-316, ICL3 replaced by [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/), C-terminal tail deleted)

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2ydo">2YDO</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MPIMG</span><span class="topo-outside">SSV</span><span class="topo-membrane">YITVELAIAVLAILGNVLVCW</span><span class="topo-inside">AVWLNSNLQNVTNY</span><span class="topo-membrane">FVVSAAAADILVGVLAIPFAI</span><span class="topo-outside">AISTGFCAACHGCLF</span><span class="topo-membrane">IACFVLVLTASSIFSLLAIAID</span><span class="topo-inside">RYIAIRIPLRYNGLVTGTR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">A</span><span class="topo-membrane">KGIIAICWVLSFAIGLT</span><span class="topo-outside">PMLGWNNCGQPKEGKAHSQGCGEGQVACLFEDVVPMNYM</span><span class="topo-membrane">VYFNFFACVLVPLLLMLGVYLRIFL</span><span class="topo-inside">AARRQLKQMES</span><span class="topo-unknown">QPLPGERARS</span><span class="topo-inside">TLQKEVHAA</span><span class="topo-membrane">KSLAIIVG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320     </span>
<span class="topo-line"><span class="topo-membrane">LFALCWLPLHI</span><span class="topo-outside">INCFTFFCPDCSHAPLWLMY</span><span class="topo-membrane">LAIVLSHTNSVVNPFIYAY</span><span class="topo-inside">RI</span><span class="topo-unknown">REFRQTFRKIIRSHVLRQ</span><span class="topo-inside">Q</span><span class="topo-unknown">EPFKAAAAENLY</span><span class="topo-inside">F</span><span class="topo-unknown">Q</span></span>
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
      <td>1</td>
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>8</td>
      <td>6</td>
      <td>8</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>29</td>
      <td>9</td>
      <td>29</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>43</td>
      <td>30</td>
      <td>43</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>64</td>
      <td>44</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>79</td>
      <td>65</td>
      <td>79</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>101</td>
      <td>80</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>121</td>
      <td>102</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>138</td>
      <td>122</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>177</td>
      <td>139</td>
      <td>177</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>202</td>
      <td>178</td>
      <td>202</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>203</td>
      <td>213</td>
      <td>203</td>
      <td>213</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>223</td>
      <td>214</td>
      <td>223</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>224</td>
      <td>232</td>
      <td>224</td>
      <td>232</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>233</td>
      <td>251</td>
      <td>233</td>
      <td>251</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>252</td>
      <td>271</td>
      <td>252</td>
      <td>271</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>272</td>
      <td>290</td>
      <td>272</td>
      <td>290</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>291</td>
      <td>292</td>
      <td>291</td>
      <td>292</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>310</td>
      <td>293</td>
      <td>310</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>311</td>
      <td>311</td>
      <td>311</td>
      <td>311</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>312</td>
      <td>323</td>
      <td>312</td>
      <td>323</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>324</td>
      <td>324</td>
      <td>324</td>
      <td>324</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>325</td>
      <td>325</td>
      <td>325</td>
      <td>325</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1107##S2052252519013137 (2 structures, 2 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ps7">6PS7</a></td>
      <td>3.3</td>
      <td>not specified</td>
      <td>A2AR-<a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> fusion expressed in Sf9 insect cells; purified in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>/CHS; LSP-SFX</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/caffeine/">Caffeine</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ps8">6PS8</a></td>
      <td>3.5</td>
      <td>not specified</td>
      <td>A2AR-<a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> fusion as above; LSP-SFX</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/zm241385/">ZM241385</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: A2A-T4L-deltaC (human A2AR residues 1-316, ICL3 replaced by [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/), C-terminal tail deleted)

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ps7">6PS7</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">ALSYIFCLVFADYKDDD</span><span class="topo-outside">DGAPPI</span><span class="topo-membrane">MGSSVYITVELAIAVLAILGNVLVCW</span><span class="topo-inside">AVWLNSNLQNVTNY</span><span class="topo-membrane">FVVSLAAADIAVGVLAIPFAITIST</span><span class="topo-outside">GFCAACH</span><span class="topo-membrane">GCLFIACFVLVLTQSSIFSLLAIAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">DRYIAIRIPLRYNGLVTGTR</span><span class="topo-membrane">AKGIIAICWVLSFAIGLTPMLGWN</span><span class="topo-outside">NCGQPKEGKNHSQGCGEGQVACLFEDVV</span><span class="topo-membrane">PMNYMVYFNFFACVLVPLLLMLGVYL</span><span class="topo-inside">RIFLAARRQLADLEDNWETLND</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">NLKVIEKADNAAQVKDALTKMRAAALDAQKA</span><span class="topo-unknown">TPPKLEDKSPDSPEM</span><span class="topo-inside">KDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLERARSTLQKEVHAAKSL</span><span class="topo-membrane">AIIVGLFAL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440  </span>
<span class="topo-line"><span class="topo-membrane">CWLPLHIINCFTFFC</span><span class="topo-outside">PDCSHA</span><span class="topo-membrane">PLWLMYLAIVLSHTNSVVNPFIY</span><span class="topo-inside">AYRIREFRQTFRKIIRSHVL</span><span class="topo-unknown">RQQEPFKAHHHHHHHHHH</span></span>
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
      <td>17</td>
      <td>-19</td>
      <td>-3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>18</td>
      <td>23</td>
      <td>-2</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>24</td>
      <td>49</td>
      <td>4</td>
      <td>29</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>63</td>
      <td>30</td>
      <td>43</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>88</td>
      <td>44</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>89</td>
      <td>95</td>
      <td>69</td>
      <td>75</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>120</td>
      <td>76</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>121</td>
      <td>140</td>
      <td>101</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>164</td>
      <td>121</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>192</td>
      <td>145</td>
      <td>172</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>218</td>
      <td>173</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>228</td>
      <td>199</td>
      <td>208</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>271</td>
      <td>1001</td>
      <td>1043</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>272</td>
      <td>286</td>
      <td>1044</td>
      <td>1058</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>287</td>
      <td>334</td>
      <td>1059</td>
      <td>1106</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>335</td>
      <td>351</td>
      <td>219</td>
      <td>235</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>352</td>
      <td>375</td>
      <td>236</td>
      <td>259</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>376</td>
      <td>381</td>
      <td>260</td>
      <td>265</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>382</td>
      <td>404</td>
      <td>266</td>
      <td>288</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>405</td>
      <td>424</td>
      <td>289</td>
      <td>308</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>425</td>
      <td>442</td>
      <td>309</td>
      <td>326</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ps8">6PS8</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GTSQPVLRGDGAR</span><span class="topo-outside">PSW</span><span class="topo-membrane">LASALACVLIFTIVVDILGNLLVIL</span><span class="topo-inside">SVYRNKKLRNAGN</span><span class="topo-membrane">IFVVSLAVANLVVAIYPYPLVLM</span><span class="topo-outside">SIFNNGWNFGYLHCQV</span><span class="topo-membrane">SAFLMGLSVIGSIWNITGIAID</span><span class="topo-inside">RYLYI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">CHSLKYDKLYSSKN</span><span class="topo-membrane">SLCYVLLIWLLTLAAVLPN</span><span class="topo-outside">LRAGTLQYDPRIYSCTFAQSVSSAY</span><span class="topo-membrane">TIAVVVFHFLVPMIIVIFCYLR</span><span class="topo-inside">IWILVLQVRGIDCSFWNESYLTGSRDERKKSLLSKFGMDE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">GVTFMFIGRFDRGQKGVDVLLKAIEILSSKKEFQEMRFIIIGKGDPELEGWARSLEEKHGNVKVITEMLSREFVRELYGSVDFVIIPSYFEPFGLVALEAMCLGAIPIASAVGGLRDIIT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">NETGILVKAGDPGELANAILKALELSRSDLSKFRENCKKRAMSFSKLKPQDFRNFV</span><span class="topo-membrane">TMFVVFVLFAICFAPLNFIGL</span><span class="topo-outside">AVASDPASMVPRIPEW</span><span class="topo-membrane">LFVASYYMAYFNSCLNPIIYGL</span><span class="topo-inside">LDQNF</span></span>
<span class="topo-ruler">       490       500   </span>
<span class="topo-line"><span class="topo-inside">RKEYRRIIVSLCTARVFFV</span><span class="topo-unknown">DSSN</span></span>
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
      <td>13</td>
      <td>10</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>14</td>
      <td>16</td>
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>41</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>54</td>
      <td>51</td>
      <td>63</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>77</td>
      <td>64</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>93</td>
      <td>87</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>115</td>
      <td>103</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>134</td>
      <td>125</td>
      <td>143</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>135</td>
      <td>153</td>
      <td>144</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>154</td>
      <td>178</td>
      <td>163</td>
      <td>187</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>200</td>
      <td>188</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>201</td>
      <td>209</td>
      <td>210</td>
      <td>218</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>210</td>
      <td>405</td>
      <td>1001</td>
      <td>1196</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>406</td>
      <td>416</td>
      <td>228</td>
      <td>238</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>417</td>
      <td>437</td>
      <td>239</td>
      <td>259</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>438</td>
      <td>453</td>
      <td>260</td>
      <td>275</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>454</td>
      <td>475</td>
      <td>276</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>476</td>
      <td>499</td>
      <td>298</td>
      <td>321</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>500</td>
      <td>503</td>
      <td>322</td>
      <td>325</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1038##nature10750 (1 structure)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3pkk">3PKK</a></td>
      <td>3.0</td>
      <td>P41212</td>
      <td>Full-length human A2AR (residues 1-316, N154Q), expressed in Pichia pastoris, purified in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>/CHS, in complex with <a href="/xray-mp-wiki/reagents/antibodies/fab2838/">Fab2838 Antibody Fragment</a></td>
      <td><a href="/xray-mp-wiki/reagents/ligands/zm241385/">ZM241385</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: A2A-T4L-deltaC (human A2AR residues 1-316, ICL3 replaced by [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/), C-terminal tail deleted)

</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1038##s41598-020-76277-x (3 structures, 3 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6lpj">6LPJ</a></td>
      <td>1.80</td>
      <td>C2221</td>
      <td>Human A2AR with <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a> fused in ICL3, expressed in Sf9 insect cells, purified in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>/CHS</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/zm241385/">ZM241385</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6lpk">6LPK</a></td>
      <td>1.80</td>
      <td>C2221</td>
      <td>Human A2AR with <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a> fused in ICL3 as above</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/zm241385/">ZM241385</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6lpl">6LPL</a></td>
      <td>2.00</td>
      <td>C2221</td>
      <td>Human A2AR with <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a> fused in ICL3 as above</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/zm241385/">ZM241385</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: A2A-T4L-deltaC (human A2AR residues 1-316, ICL3 replaced by [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/), C-terminal tail deleted)

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6lpj">6LPJ</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFADYKDDDD</span><span class="topo-outside">GAPPIMG</span><span class="topo-membrane">SSVYITVELAIAVLAILGNVLVCWA</span><span class="topo-inside">VWLNSNLQNVTN</span><span class="topo-membrane">YFVVSLAAADIAVGVLAIPFAITIS</span><span class="topo-outside">TGFCAACH</span><span class="topo-membrane">GCLFIACFVLVLTQSSIFSL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LAIAID</span><span class="topo-inside">RYIAIRIPLRYNGLVTGTR</span><span class="topo-membrane">AKGIIAICWVLSFAIGLTPMLGWN</span><span class="topo-outside">NCGQPKEGKNHSQGCGEGQVACLFEDVV</span><span class="topo-membrane">PMNYMVYFNFFACVLVPLLLMLGVYLR</span><span class="topo-inside">IFLAARRQLADLEDNW</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">ETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQK</span><span class="topo-unknown">ATPPKLEDKSPDSPE</span><span class="topo-inside">MKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLERARSTLQKEVHAAK</span><span class="topo-membrane">SLAIIV</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       </span>
<span class="topo-line"><span class="topo-membrane">GLFALCWLPLHIINCFTFF</span><span class="topo-outside">CPDCSHAPLW</span><span class="topo-membrane">LMYLAIVLSHTNSVVNPFIYAY</span><span class="topo-inside">RIREFRQTFRKIIRSHV</span><span class="topo-unknown">LRQQEPFKAHHHHHHHHHH</span></span>
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
      <td>23</td>
      <td>-24</td>
      <td>-2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>24</td>
      <td>30</td>
      <td>-1</td>
      <td>5</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>55</td>
      <td>6</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>56</td>
      <td>67</td>
      <td>31</td>
      <td>42</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>92</td>
      <td>43</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>100</td>
      <td>68</td>
      <td>75</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>126</td>
      <td>76</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>127</td>
      <td>145</td>
      <td>102</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>146</td>
      <td>169</td>
      <td>121</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>197</td>
      <td>145</td>
      <td>172</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>198</td>
      <td>224</td>
      <td>173</td>
      <td>199</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>225</td>
      <td>233</td>
      <td>200</td>
      <td>208</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>275</td>
      <td>1001</td>
      <td>1042</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>276</td>
      <td>290</td>
      <td>1043</td>
      <td>1057</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>291</td>
      <td>339</td>
      <td>1058</td>
      <td>1106</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>354</td>
      <td>219</td>
      <td>233</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>355</td>
      <td>379</td>
      <td>234</td>
      <td>258</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>380</td>
      <td>389</td>
      <td>259</td>
      <td>268</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>411</td>
      <td>269</td>
      <td>290</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>428</td>
      <td>291</td>
      <td>307</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>429</td>
      <td>447</td>
      <td>308</td>
      <td>326</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6lpk">6LPK</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFADYKDDDD</span><span class="topo-inside">GAPPIMG</span><span class="topo-membrane">SSVYITVELAIAVLAILGNVLVCW</span><span class="topo-outside">AVWLNSNLQNVTNY</span><span class="topo-membrane">FVVSLAAADIAVGVLAIPFAITIS</span><span class="topo-inside">TGFCAACH</span><span class="topo-membrane">GCLFIACFVLVLTQSSIFSL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LAIAI</span><span class="topo-outside">DRYIAIRIPLRYNGLVTGTRAK</span><span class="topo-membrane">GIIAICWVLSFAIGLTPMLGWN</span><span class="topo-inside">NCGQPKEGKNHSQGCGEGQVACLFEDV</span><span class="topo-membrane">VPMNYMVYFNFFACVLVPLLLMLGVYL</span><span class="topo-outside">RIFLAARRQLADLEDNW</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQK</span><span class="topo-unknown">ATPPKLEDKSPDSPE</span><span class="topo-outside">MKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLERARSTLQKEVHAAKS</span><span class="topo-membrane">LAIIV</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       </span>
<span class="topo-line"><span class="topo-membrane">GLFALCWLPLHIINCFTFFC</span><span class="topo-inside">PDCSHAPL</span><span class="topo-membrane">WLMYLAIVLSHTNSVVNPFIYAY</span><span class="topo-outside">RIREFRQTFRKIIRSHV</span><span class="topo-unknown">LRQQEPFKAHHHHHHHHHH</span></span>
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
      <td>23</td>
      <td>-24</td>
      <td>-2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>24</td>
      <td>30</td>
      <td>-1</td>
      <td>5</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>54</td>
      <td>6</td>
      <td>29</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>68</td>
      <td>30</td>
      <td>43</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>92</td>
      <td>44</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>100</td>
      <td>68</td>
      <td>75</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>125</td>
      <td>76</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>126</td>
      <td>147</td>
      <td>101</td>
      <td>122</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>169</td>
      <td>123</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>196</td>
      <td>145</td>
      <td>171</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>197</td>
      <td>223</td>
      <td>172</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>233</td>
      <td>199</td>
      <td>208</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>275</td>
      <td>1001</td>
      <td>1042</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>276</td>
      <td>290</td>
      <td>1043</td>
      <td>1057</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>291</td>
      <td>339</td>
      <td>1058</td>
      <td>1106</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>355</td>
      <td>219</td>
      <td>234</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>356</td>
      <td>380</td>
      <td>235</td>
      <td>259</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>381</td>
      <td>388</td>
      <td>260</td>
      <td>267</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>389</td>
      <td>411</td>
      <td>268</td>
      <td>290</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>428</td>
      <td>291</td>
      <td>307</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>429</td>
      <td>447</td>
      <td>308</td>
      <td>326</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6lpl">6LPL</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFADYKDDDD</span><span class="topo-inside">GAPPIMGSSV</span><span class="topo-membrane">YITVELAIAVLAILGNVLVCWAVWL</span><span class="topo-outside">NSNLQNV</span><span class="topo-membrane">TNYFVVSLAAADIAVGVLAIPFAI</span><span class="topo-inside">TISTGFCAACHGCLF</span><span class="topo-membrane">IACFVLVLTQSSIFSL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LAIAIDRY</span><span class="topo-outside">IAIRIPLRYNGLVTG</span><span class="topo-membrane">TRAKGIIAICWVLSFAIGLTPML</span><span class="topo-inside">GWNNCGQPKEGKNHSQGCGEGQVACLFEDVVPMN</span><span class="topo-membrane">YMVYFNFFACVLVPLLLMLGVYLRIF</span><span class="topo-outside">LAARRQLADLEDNW</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQK</span><span class="topo-unknown">ATPPKLEDKSPDSPE</span><span class="topo-outside">MKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLERARSTLQKEVHAA</span><span class="topo-membrane">KSLAIIV</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       </span>
<span class="topo-line"><span class="topo-membrane">GLFALCWLPLHIINCF</span><span class="topo-inside">TFFCPDCSHAPLWL</span><span class="topo-membrane">MYLAIVLSHTNSVVNPFIYAYRI</span><span class="topo-outside">REFRQTFRKIIRSHV</span><span class="topo-unknown">LRQQEPFKAHHHHHHHHHH</span></span>
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
      <td>23</td>
      <td>-24</td>
      <td>-2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>24</td>
      <td>33</td>
      <td>-1</td>
      <td>8</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>58</td>
      <td>9</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>59</td>
      <td>65</td>
      <td>34</td>
      <td>40</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>89</td>
      <td>41</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>104</td>
      <td>65</td>
      <td>79</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>128</td>
      <td>80</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>143</td>
      <td>104</td>
      <td>118</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>144</td>
      <td>166</td>
      <td>119</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>200</td>
      <td>142</td>
      <td>175</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>201</td>
      <td>226</td>
      <td>176</td>
      <td>201</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>227</td>
      <td>233</td>
      <td>202</td>
      <td>208</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>275</td>
      <td>1001</td>
      <td>1042</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>276</td>
      <td>290</td>
      <td>1043</td>
      <td>1057</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>291</td>
      <td>339</td>
      <td>1058</td>
      <td>1106</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>353</td>
      <td>219</td>
      <td>232</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>354</td>
      <td>376</td>
      <td>233</td>
      <td>255</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>377</td>
      <td>390</td>
      <td>256</td>
      <td>269</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>391</td>
      <td>413</td>
      <td>270</td>
      <td>292</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>414</td>
      <td>428</td>
      <td>293</td>
      <td>307</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>429</td>
      <td>447</td>
      <td>308</td>
      <td>326</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1126##science.1219218 (1 structure)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ey">4EY</a></td>
      <td>1.8</td>
      <td>not specified</td>
      <td>A2AAR-BRIL-deltaC (human A2AAR with ICL3 replaced by apocytochrome b562RIL, C-terminal tail deleted), expressed in Sf9 insect cells</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/zm241385/">ZM241385</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: A2A-T4L-deltaC (human A2AR residues 1-316, ICL3 replaced by [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/), C-terminal tail deleted)

**Purification:**

- **Expression system**: Sf9 insect cells
- **Expression construct**: A2AAR-BRIL-deltaC (human A2AAR with ICL3 replaced by apocytochrome b562RIL, C-terminal tail deleted)
- **Tag info**: [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) (apocytochrome b562RIL) fusion in ICL3

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
      <td>Protein expression</td>
      <td>Baculovirus expression in Sf9 cells</td>
      <td>--</td>
      <td>not specified + --</td>
      <td>Receptor stabilized with 0.8 M Na+ during purification</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>not specified</td>
      <td>--</td>
      <td>not specified + --</td>
      <td>Purification in presence of Na+ and <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
    </tr>
    <tr>
      <td>Ligand exchange</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/theophylline/">Theophylline</a> to <a href="/xray-mp-wiki/reagents/ligands/zm241385/">ZM241385</a> exchange</td>
      <td>--</td>
      <td>not specified + --</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/zm241385/">ZM241385</a> exchanged from <a href="/xray-mp-wiki/reagents/ligands/theophylline/">Theophylline</a></td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified A2AAR-BRIL-deltaC with [ZM241385](/xray-mp-wiki/reagents/ligands/zm241385/) bound

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>In meso (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">[LCP</a>](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/))</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified A2AAR-<a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a>-deltaC bound to <a href="/xray-mp-wiki/reagents/ligands/zm241385/">ZM241385</a> in presence of ~0.15 M Na+</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> and <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> mixture</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Structure solved at 1.8 A, the highest resolution GPCR structure at the time. 57 ordered water molecules identified. Phases obtained by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a>.</td>
    </tr>
  </tbody>
</table>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1126##science.1202793 (1 structure, 1 sequence)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3qak">3QAK</a></td>
      <td>2.7</td>
      <td>—</td>
      <td>A2AAR-T4L-deltaC (human A2AAR with ICL3 replaced by <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a>, C-terminal tail deleted) bound to agonist <a href="/xray-mp-wiki/reagents/ligands/uk-432097/">UK-432097</a>, expressed in Sf9 insect cells</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/uk-432097/">UK-432097</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: A2A-T4L-deltaC (human A2AR residues 1-316, ICL3 replaced by [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/), C-terminal tail deleted)

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3qak">3QAK</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">DYKDDDDAMGQPVGAPP</span><span class="topo-outside">IMGS</span><span class="topo-membrane">SVYITVELAIAVLAILGNVLVCW</span><span class="topo-inside">AVWLNSNLQNVTNYF</span><span class="topo-membrane">VVSLAAADIAVGVLAIPFAITIS</span><span class="topo-outside">TGFCAACH</span><span class="topo-membrane">GCLFIACFVLVLTQSSIFSLLAIAI</span><span class="topo-inside">DRYIA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">IRIPLRYNGLVTGTRAK</span><span class="topo-membrane">GIIAICWVLSFAIGLTPMLGWNN</span><span class="topo-outside">CGQ</span><span class="topo-unknown">PKEGKNHSQ</span><span class="topo-outside">GCGEGQVACLFEDV</span><span class="topo-membrane">VPMNYMVYFNFFACVLVPLLLMLGVYL</span><span class="topo-inside">RIFLAARRQLNIFEMLRIDEGLRLKIY</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">KDTEGYYTIGIGHLLTKSPSLNAAKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRW</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">YNQTPNRAKRVITTFRTGTWDAYRSTLQKEVHAAK</span><span class="topo-membrane">SLAIIVGLFALCWLPLHIINCFTFFC</span><span class="topo-outside">PDCSHA</span><span class="topo-membrane">PLWLMYLAIVLSHTNSVVNPFIYAYR</span><span class="topo-inside">IREFRQTFRKIIRSHVL</span><span class="topo-unknown">RQQEPFKAHH</span></span>
<span class="topo-ruler">        </span>
<span class="topo-line"><span class="topo-unknown">HHHHHHHH</span></span>
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
      <td>17</td>
      <td>-14</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>18</td>
      <td>21</td>
      <td>3</td>
      <td>6</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>22</td>
      <td>44</td>
      <td>7</td>
      <td>29</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>45</td>
      <td>59</td>
      <td>30</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>82</td>
      <td>45</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>90</td>
      <td>68</td>
      <td>75</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>115</td>
      <td>76</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>137</td>
      <td>101</td>
      <td>122</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>138</td>
      <td>160</td>
      <td>123</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>163</td>
      <td>146</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>172</td>
      <td>149</td>
      <td>157</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>173</td>
      <td>186</td>
      <td>158</td>
      <td>171</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>187</td>
      <td>213</td>
      <td>172</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>214</td>
      <td>223</td>
      <td>199</td>
      <td>208</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>224</td>
      <td>383</td>
      <td>1002</td>
      <td>1161</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>384</td>
      <td>395</td>
      <td>222</td>
      <td>233</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>396</td>
      <td>421</td>
      <td>234</td>
      <td>259</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>422</td>
      <td>427</td>
      <td>260</td>
      <td>265</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>428</td>
      <td>453</td>
      <td>266</td>
      <td>291</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>454</td>
      <td>470</td>
      <td>292</td>
      <td>308</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>488</td>
      <td>309</td>
      <td>326</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1124##mol.114.097360 (2 structures, 2 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ug2">4UG2</a></td>
      <td>2.6</td>
      <td>P212121</td>
      <td>A2AR-GL31 thermostabilized mutant (mutations L48A, A54L, T65A, Q89A, N154A, C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> after Ala316, His10 tag) expressed in baculovirus/Sf9 system, purified in DM</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/cgs21680/">CGS21680</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4uhr">4UHR</a></td>
      <td>2.6</td>
      <td>P21</td>
      <td>A2AR-GL31 thermostabilized mutant as above</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/cgs21680/">CGS21680</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: A2A-T4L-deltaC (human A2AR residues 1-316, ICL3 replaced by [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/), C-terminal tail deleted)

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ug2">4UG2</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MPIMG</span><span class="topo-inside">SSV</span><span class="topo-membrane">YITVELAIAVLAILGNVLVC</span><span class="topo-outside">WAVWLNSNLQNVTNYFV</span><span class="topo-membrane">VSAAAADILVGVLAIPFAIAI</span><span class="topo-inside">STGFCAACHGCL</span><span class="topo-membrane">FIACFVLVLTASSIFSLLAIA</span><span class="topo-outside">IDRYIAIRIPLRYNGLVTGTR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">AKGI</span><span class="topo-membrane">IAICWVLSFAIGLTPMLGWN</span><span class="topo-inside">NCGQPKEGKAHSQGCGEGQVACLFEDVV</span><span class="topo-membrane">PMNYMVYFNFFACVLVPLLLMLGVYL</span><span class="topo-outside">RIFLAARRQL</span><span class="topo-unknown">KQMESQPLPGER</span><span class="topo-outside">ARSTLQKEVHAAKS</span><span class="topo-membrane">LAIIVG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320     </span>
<span class="topo-line"><span class="topo-membrane">LFALCWLPLHIINCF</span><span class="topo-inside">TFFCPDCSHAPLWL</span><span class="topo-membrane">MYLAIVLSHTNSVVNPFIY</span><span class="topo-outside">AYRI</span><span class="topo-unknown">REFRQTFRKIIR</span><span class="topo-outside">SHVLR</span><span class="topo-unknown">QQEPFKAAAAENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (18 regions)</summary>
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
      <td>6</td>
      <td>8</td>
      <td>6</td>
      <td>8</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>28</td>
      <td>9</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>45</td>
      <td>29</td>
      <td>45</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>66</td>
      <td>46</td>
      <td>66</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>78</td>
      <td>67</td>
      <td>78</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>99</td>
      <td>79</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>100</td>
      <td>124</td>
      <td>100</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>144</td>
      <td>125</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>172</td>
      <td>145</td>
      <td>172</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>198</td>
      <td>173</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>208</td>
      <td>199</td>
      <td>208</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>234</td>
      <td>221</td>
      <td>234</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>235</td>
      <td>255</td>
      <td>235</td>
      <td>255</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>256</td>
      <td>269</td>
      <td>256</td>
      <td>269</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>270</td>
      <td>288</td>
      <td>270</td>
      <td>288</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>289</td>
      <td>292</td>
      <td>289</td>
      <td>292</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>304</td>
      <td>293</td>
      <td>304</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>305</td>
      <td>309</td>
      <td>305</td>
      <td>309</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4uhr">4UHR</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MPIMG</span><span class="topo-inside">SSV</span><span class="topo-membrane">YITVELAIAVLAILGNVLVCW</span><span class="topo-outside">AVWLNSNLQNVTNYF</span><span class="topo-membrane">VVSAAAADILVGVLAIPFAIA</span><span class="topo-inside">ISTGFCAACHGCLF</span><span class="topo-membrane">IACFVLVLTASSIFSLLAIAID</span><span class="topo-outside">RYIAIRIPLRYNGLVTGTR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">AK</span><span class="topo-membrane">GIIAICWVLSFAIGLTPML</span><span class="topo-inside">GWNNCGQPKEGKA</span><span class="topo-unknown">HSQ</span><span class="topo-inside">GCGEGQVACLFEDVVPMNY</span><span class="topo-membrane">MVYFNFFACVLVPLLLMLGVYLRIFL</span><span class="topo-outside">AARRQLKQMESQPLPGERARSTLQKEVHAA</span><span class="topo-membrane">KSLAIIVG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320     </span>
<span class="topo-line"><span class="topo-membrane">LFALCWLPLHI</span><span class="topo-inside">INCFTFFCPDC</span><span class="topo-unknown">S</span><span class="topo-inside">HAPLWLMY</span><span class="topo-membrane">LAIVLSHTNSVVNPFIYAYR</span><span class="topo-outside">I</span><span class="topo-unknown">REFRQTFRKIIRSHVLRQQEPF</span><span class="topo-outside">KAAAA</span><span class="topo-unknown">ENLYFQ</span></span>
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
      <td>6</td>
      <td>8</td>
      <td>6</td>
      <td>8</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>29</td>
      <td>9</td>
      <td>29</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>44</td>
      <td>30</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>65</td>
      <td>45</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>79</td>
      <td>66</td>
      <td>79</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>101</td>
      <td>80</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>122</td>
      <td>102</td>
      <td>122</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>123</td>
      <td>141</td>
      <td>123</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>154</td>
      <td>142</td>
      <td>154</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>176</td>
      <td>158</td>
      <td>176</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>202</td>
      <td>177</td>
      <td>202</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>203</td>
      <td>232</td>
      <td>203</td>
      <td>232</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>233</td>
      <td>251</td>
      <td>233</td>
      <td>251</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>252</td>
      <td>262</td>
      <td>252</td>
      <td>262</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>264</td>
      <td>271</td>
      <td>264</td>
      <td>271</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>272</td>
      <td>291</td>
      <td>272</td>
      <td>291</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>292</td>
      <td>292</td>
      <td>292</td>
      <td>292</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>314</td>
      <td>293</td>
      <td>314</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>315</td>
      <td>319</td>
      <td>315</td>
      <td>319</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1124##molpharm.122.000633 (1 structure, 1 sequence)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8gne">8GNE</a></td>
      <td>3.2</td>
      <td>not specified</td>
      <td>A2AR-Rant21 construct stabilized in inactive-state conformation, in complex with <a href="/xray-mp-wiki/reagents/antibodies/fab2838/">Fab2838 Antibody Fragment</a></td>
      <td>Istradefylline</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: A2A-T4L-deltaC (human A2AR residues 1-316, ICL3 replaced by [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/), C-terminal tail deleted)

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8gne">8GNE</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">DYDDDDK</span><span class="topo-inside">GAPPIMGS</span><span class="topo-membrane">SVYITVELAIAVLAILGNVLVCWAVW</span><span class="topo-outside">LNSNLQNVT</span><span class="topo-membrane">NYFVVSLAAADIAVGVLAIPFAITIS</span><span class="topo-inside">TGFCAACHG</span><span class="topo-membrane">CLFIACFVLVLTQSSIFSLLAIAID</span><span class="topo-outside">RYIAIRIPLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">YNGLVTGTR</span><span class="topo-membrane">AKGIIAICWVLSFAIGLTPMLGW</span><span class="topo-inside">NNCGQPKEGKQHSQGCGEGQVACLFEDVV</span><span class="topo-membrane">PMNYMVYFNFFACVLVPLLLMLGVYLR</span><span class="topo-outside">IFLAARRQLADLEDNWETLNDNLKVIEKA</span><span class="topo-unknown">D</span><span class="topo-outside">NA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">AQVKDALTKMRAAALDAQK</span><span class="topo-unknown">ATPPKLEDKSPDSPE</span><span class="topo-outside">MKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLERARSTLQKEVHAA</span><span class="topo-membrane">KSLAIIVGLFALCWLPLHIINCF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430 </span>
<span class="topo-line"><span class="topo-membrane">TFF</span><span class="topo-inside">CPDCSHAPLW</span><span class="topo-membrane">LMYLAIVLSHTNSVVNPFIYAYR</span><span class="topo-outside">IREFRQTFRKIIRSHVLR</span><span class="topo-unknown">QQEPFKAHHHHHHHHHH</span></span>
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
      <td>1</td>
      <td>7</td>
      <td>-8</td>
      <td>-2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>15</td>
      <td>-1</td>
      <td>6</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>41</td>
      <td>7</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>50</td>
      <td>33</td>
      <td>41</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>76</td>
      <td>42</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>77</td>
      <td>85</td>
      <td>68</td>
      <td>76</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>110</td>
      <td>77</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>129</td>
      <td>102</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>152</td>
      <td>121</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>153</td>
      <td>181</td>
      <td>144</td>
      <td>172</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>208</td>
      <td>173</td>
      <td>199</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>209</td>
      <td>217</td>
      <td>200</td>
      <td>208</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>237</td>
      <td>1001</td>
      <td>1020</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>238</td>
      <td>238</td>
      <td>1021</td>
      <td>1021</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>239</td>
      <td>259</td>
      <td>1022</td>
      <td>1042</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>260</td>
      <td>274</td>
      <td>1043</td>
      <td>1057</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>275</td>
      <td>323</td>
      <td>1058</td>
      <td>1106</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>324</td>
      <td>337</td>
      <td>219</td>
      <td>232</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>363</td>
      <td>233</td>
      <td>258</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>373</td>
      <td>259</td>
      <td>268</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>374</td>
      <td>396</td>
      <td>269</td>
      <td>291</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>414</td>
      <td>292</td>
      <td>309</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>415</td>
      <td>431</td>
      <td>310</td>
      <td>326</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1107##S1600576719012846 (0 structures)</strong></summary>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: A2A-T4L-deltaC (human A2AR residues 1-316, ICL3 replaced by [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/), C-terminal tail deleted)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/">Serial Femtosecond Crystallography</a> (SFX)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>A2AAR-<a href="/xray-mp-wiki/reagents/ligands/zm241385/">ZM241385</a> complex in LCP matrix</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>293 K</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>1 week</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>SFX structure solved using HVC injector at SACLA at atmospheric pressure. 190,041 diffraction patterns collected, 10,510 indexed. No 7.9/9.7 <a href="/xray-mp-wiki/reagents/lipids/mag/">MAG</a> additives needed.</td>
    </tr>
  </tbody>
</table>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1107##s2052252522001907 (0 structures)</strong></summary>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: A2A-T4L-deltaC (human A2AR residues 1-316, ICL3 replaced by [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/), C-terminal tail deleted)

**Crystallization:**


</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1038##s41467-017-00630-4 (0 structures)</strong></summary>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: A2A-T4L-deltaC (human A2AR residues 1-316, ICL3 replaced by [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/), C-terminal tail deleted)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Notes</td>
      <td><a href="/xray-mp-wiki/concepts/serial-millisecond-crystallography/">SMX</a> room-temperature structure at SLS beamline X06SA. EIGER 16M detector at 50 Hz, 20×5 µm beam, 1.5×10¹² ph/s flux. Data collected in 6.6 h from ~240,000 indexed diffraction patterns (50 µm nozzle, 30×30×5 µm³ crystals). Native-SAD phasing achieved in under 5 h. Comparison with cryo dataset (4 h, 6 crystals, 2.0 Å) and SFX dataset (LCLS, 22 min, 3563 patterns, 1.7 Å).</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Notes</td>
      <td>SFX structure at LCLS CXI experimental station. 10% transmission, ~10¹¹ ph/pulse, 1×1 µm² beam. CSPAD detector. 3563 indexable patterns collected in 22 min. Data converged; better SA-omit map for <a href="/xray-mp-wiki/reagents/ligands/zm241385/">ZM241385</a> compared to <a href="/xray-mp-wiki/concepts/serial-millisecond-crystallography/">SMX</a> and cryo data. Rfree/Rwork: not specified in this study.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Notes</td>
      <td>Conventional cryo-crystallography comparison dataset. 4 h beamtime, 350° fine-sliced data from 6 cryo-selected crystals. 20×5 µm² beam at 10% transmission. Data processed with XDS. Resolution slightly better than <a href="/xray-mp-wiki/concepts/serial-millisecond-crystallography/">SMX</a> (2.14 Å) but worse than SFX (1.7 Å). Weaker density around water molecules compared to SFX maps.</td>
    </tr>
  </tbody>
</table>
</details>


## Biological / Functional Insights

### First crystal structure of the human A2A adenosine receptor

The 2.6 A crystal structure of the human A2A adenosine receptor bound to the antagonist [ZM241385](/xray-mp-wiki/reagents/ligands/zm241385/) revealed the first atomic-resolution view of this important drug target. The [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) fusion strategy was applied, with ICL3 replaced by T4 lysozyme and the C-terminal tail deleted. The structure revealed three distinct features: (1) a markedly different ECL2 organization compared to beta-ARs and rhodopsin, (2) [ZM241385](/xray-mp-wiki/reagents/ligands/zm241385/) binding in an extended conformation perpendicular to the membrane plane and colinear with TM VII, and (3) a subtle divergence in helical positions redefining the antagonist-binding cavity closer to helices VI and VII with limited interactions with helices III and V.

### ECL2 organization and disulfide bond network

The ECL2 of A2AR lacks prominent secondary structure (beta-sheet or alpha-helix) observed in rhodopsin and beta-ARs, instead forming a spatially constrained random coil with three disulfide linkages to ECL1. Two disulfide bonds (Cys71-Cys159 and Cys74-Cys146) are unique to A2AR; the third (Cys77-Cys166) is conserved among class A GPCRs. A fourth intraloop disulfide bond in ECL3 (Cys259-Cys262, CPDC motif) creates a kink constraining ECL3 and orienting His264 at the top of the ligand-binding site.

### DRY motif and ICL2 interactions

The conserved DRY motif (Asp101-Arg102-Tyr103) in A2AR does not participate in the canonical ionic lock seen in rhodopsin. Instead, Asp101 forms a hydrogen bond with Tyr112 in ICL2 and Thr41 at the base of helix II. This hydrogen-bonding pattern, also seen in turkey beta1AR but not beta2AR, correlates with low basal activity. A short helical section in ICL2 of A2AR and beta1AR is absent in beta2AR, which exhibits high basal activity.

### Toggle switch and inverse agonist mechanism

[ZM241385](/xray-mp-wiki/reagents/ligands/zm241385/) has a 14 A^2 contact area with Trp246(6.48), the conserved toggle switch tryptophan on helix VI. This contact is intermediate between [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) in rhodopsin (36 A^2) and [Carazolol](/xray-mp-wiki/reagents/ligands/carazolol/) in beta2AR (no direct contact), suggesting [ZM241385](/xray-mp-wiki/reagents/ligands/zm241385/) stabilizes the A2AR in an inactive state by limiting the range of motion of the toggle switch.

### Ligand-binding cavity redefinition

The A2AR structure demonstrates that the ligand-binding pocket can vary in position and orientation among class A GPCRs, rather than being a conserved scaffold with different side chains. The empirically determined positions of [ZM241385](/xray-mp-wiki/reagents/ligands/zm241385/) substituents deviate substantially from earlier molecular modeling studies based on rhodopsin and beta-AR homology models, explaining the structural basis for A2A receptor selectivity.

### A2AR-mini-Gs complex structure

The first structure of a GPCR bound to an engineered mini-Gs at 3.4 A resolution revealed the GPCR-G-protein interface spanning 1,048 A^2 and involving 20 receptor residues and 17 mini-Gs residues. The cytoplasmic end of H6 moves 14 A outward upon G-protein binding.

### Caffeine dual binding mode

At 2.1 A, [Caffeine](/xray-mp-wiki/reagents/ligands/caffeine/) occupies the orthosteric pocket in two orientations (A and B) at approximately 50:50 ratio, related by 180 degree rotation around the N1-C10 bond.

### Fab2838 allosteric inverse-agonist mechanism

[Fab2838 Antibody Fragment](/xray-mp-wiki/reagents/antibodies/fab2838/) binds the intracellular surface of A2AR with its CDR-H3 penetrating the receptor core, locking helices III and VI together and stabilizing the inactive conformation. This demonstrates bidirectional signal transfer between G-protein-binding and ligand-binding pockets.

### GL31 thermostabilized agonist-bound structures

The A2AR-GL31 construct with 11 thermostabilizing mutations enabled the first agonist-bound A2AR structures ([NECA](/xray-mp-wiki/reagents/ligands/neca/) at 2.6 A, adenosine at 3.0 A). Agonist binding induces significant conformational changes including a 5.6 A outward displacement of the H6 cytoplasmic end and Pro285 isomerization from trans to cis conformation in H7.

### Xanthine antagonist binding modes in A2A-StaR2

The StaR2 construct with thermostabilizing mutations traps the receptor in the inverse agonist conformation with the ionic lock intact. Structures with [ZM241385](/xray-mp-wiki/reagents/ligands/zm241385/) (3PWH), XAC (3REY), and [Caffeine](/xray-mp-wiki/reagents/ligands/caffeine/) (3RFM) revealed the binding modes and the complete ICL3 structure.

### High-resolution structure of A2AAR-BRIL at 1.8 A reveals ordered water molecules

The 1.8 A crystal structure of human A2AAR with ICL3 replaced by apocytochrome b562RIL ([BRIL](/xray-mp-wiki/reagents/protein-tags/bril/)) enabled identification of 57 ordered water molecules inside the receptor, comprising three major clusters. The intracellular (IC) cluster near the conserved D[E]RY motif contains ~20 water molecules. The central cluster harbors a sodium ion. The extracellular (EC) cluster is near the ligand-binding pocket.

### Sodium ion allosteric site in the central water cluster

A [Sodium Ion (Na+)](/xray-mp-wiki/reagents/ligands/sodium-ion/) was identified in the central water cluster, coordinated by Asp52(2.50), Ser91(3.39), and three water molecules in a distorted octahedral geometry. The Na+ is bound at a site involving highly conserved residues Asn24(1.50), Asp52(2.50), Ser91(3.39), Trp246(6.48), Asn280(7.45), Asn284(7.49), and Tyr288(7.53). Comparison with the active-like state (PDB 3QAK) shows the pocket collapses from 200 to 70 A^3 upon activation, precluding Na+ binding and explaining the negative allosteric effect of Na+ on agonist binding.

### Cholesterol stabilizes helix VI conformation

Three [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) molecules were identified per receptor. Two cholesterols (CLR2 and CLR3) occupy hydrophobic grooves along helix VI and form extensive contacts with Phe255(6.57), with CLR2 forming a hydrogen bond with Ser263 main-chain carboxyl and CLR3 interacting with Cys259 in ECL3. This specific [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) binding stabilizes the position of Asn253(6.55) in the ligand-binding pocket, consistent with observations that cholesteryl hemisuccinate ([CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)) increases thermostability.

### Ordered lipids and bilayer reconstruction

The structure includes 23 ordered lipid chains and three cholesterols forming an almost-complete lipid bilayer around each protein molecule. One lipid (OLA) intercalates inside the transmembrane bundle between helices I and VII, protruding into the ligand-binding pocket, stabilizing the conformation of the first eight N-terminal residues of helix I.

### Amiloride docking into the sodium allosteric site

Docking studies of [Amiloride](/xray-mp-wiki/reagents/ligands/amiloride/) into the central cluster cavity showed its charged guanidinium group interacting with Asp52(2.50), mimicking the Na+/water cluster. This is consistent with earlier evidence that Na+ and [Amiloride](/xray-mp-wiki/reagents/ligands/amiloride/) share an allosteric binding site on GPCRs. [Amiloride](/xray-mp-wiki/reagents/ligands/amiloride/) reduced [3H][ZM241385](/xray-mp-wiki/reagents/ligands/zm241385/) binding and competed with Na+ for the same site.

### Agonist-induced conformational changes in A2AAR (UK-432097-bound structure)

The 2.7 A crystal structure of human A2AAR–T4L-ΔC in complex with the full agonist [UK-432097](/xray-mp-wiki/reagents/ligands/uk-432097/) revealed the first agonist-bound GPCR structure in an active-like state without G protein or [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) stabilization (Xu et al., Science 2011). Comparison with the antagonist-bound ([ZM241385](/xray-mp-wiki/reagents/ligands/zm241385/)) structure shows that agonist binding triggers a series of conformational changes: (1) His250(6.52) moves ~1.8 A inward forming a hydrogen bond with the agonist ribose carbonyl; (2) conserved Trp246(6.48) indole shifts ~1.9 A to avoid steric clash with the ribose ring, facilitating rotation and tilt of the intracellular side of helix VI; (3) the NPxxY motif (Asn284–Tyr288) at the cytoplasmic end of helix VII shifts 4–5 A inward; (4) helices V and VI undergo pronounced intracellular movements while their extracellular ends remain relatively fixed. The [UK-432097](/xray-mp-wiki/reagents/ligands/uk-432097/) agonist (778 Da) forms an extensive interaction network including 11 hydrogen bonds, one aromatic stacking interaction, and numerous van der Waals contacts.

### Common GPCR activation mechanism

Comparison of agonist-bound A2AAR, [OPSIN](/xray-mp-wiki/proteins/gpcr/opsin/), and nanobody-stabilized beta2AR reveals a shared GPCR activation mechanism. A stable core bundle of helices I–IV supports a mobile module of helices V–VII. Although the molecular triggers differ (helix V inward movement in beta2AR vs. helix III/VI/VII changes in A2AAR), the overall direction of helical movements is similar. RMSD fingerprint analysis shows correlation of R^2 = 0.64 for helices I–VI between A2AAR and rhodopsin activation transitions. The ionic lock between Arg(3.50) (D[E]RY motif) and Glu(6.30) is already broken in the antagonist-bound A2AAR structure.

### Conformationally selective agonist UK-432097

This study demonstrated that agonist-bound GPCR structures can be obtained at high resolution without G protein or [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) stabilization by using conformationally selective ligands such as [UK-432097](/xray-mp-wiki/reagents/ligands/uk-432097/), which predominantly stabilizes a single receptor conformation through an extensive ligand-receptor interaction network. This challenges the assumption that agonists always increase receptor dynamics.

### CGS21680 binding to A2AR reveals extended extracellular binding vestibule

The 2.6 A crystal structure of CGS21680-bound A2AR-GL31 (PDB 4UG2, 4UHR) reveals that the selective agonist [CGS21680](/xray-mp-wiki/reagents/ligands/cgs21680/) binds with its adenosine moiety in the canonical orthosteric pocket, but the (2-carboxyethyl)phenylethylamino extension protrudes into an extended vestibule formed by TM2, TM7, EL2, and EL3. This extension makes van der Waals contacts with Glu169(EL2), His264(EL3), Leu267(7.32), and Ile274(7.39), with the amine group forming a hydrogen bond with Ser67(2.65). The binding pocket narrows at the extracellular surface due to an inward tilt of TM2 when [CGS21680](/xray-mp-wiki/reagents/ligands/cgs21680/) is bound. Three ordered water molecules (W1, W2, W3) were identified, with W1 bridging Ser67(2.65) to the ligand. Mutagenesis showed Leu267A causes a 24-fold reduction in [CGS21680](/xray-mp-wiki/reagents/ligands/cgs21680/) potency, while mutations S67A, E169A, and H264A impair basal activity, indicating the extracellular region modulates constitutive receptor activity. Comparison of monoclinic and orthorhombic crystal forms revealed conformational flexibility in EL2/EL3.

### KW-6356 structural basis of inverse agonism and insurmountable antagonism

[KW-6356](/xray-mp-wiki/reagents/ligands/kw-6356/) is a novel non-xanthine A2A receptor antagonist/inverse agonist (pKi = 9.93) with slow dissociation kinetics (koff = 0.016 min-1). The cocrystal structure at 2.3 A reveals the furyl moiety extends deep into the orthosteric pocket making contact with His250(6.52) and Trp246(6.48) - key residues for receptor activation. Steric conflict between the furyl group and His250(6.52) in the active conformation prevents [KW-6356](/xray-mp-wiki/reagents/ligands/kw-6356/) from binding to the active state, explaining its inverse agonist properties. The oxanyl group occupies the bottom of the pocket, while the p-methylnicotinamide group stabilizes the extracellular loop conformation via hydrogen bonds with Thr256(6.58) and CH-pi interactions with His264(ECL3) and Met270(7.35). These features together contribute to slow dissociation and insurmountable antagonism, where [KW-6356](/xray-mp-wiki/reagents/ligands/kw-6356/) reduces both potency and maximal response of [CGS21680](/xray-mp-wiki/reagents/ligands/cgs21680/). In contrast, istradefylline binds equally well to active and inactive states, consistent with its neutral antagonist and surmountable antagonism profile.


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/zm241385/">ZM241385</a> — High-affinity antagonist bound in the first crystal structure
- <a href="/xray-mp-wiki/proteins/gpcr/beta2-adrenergic-receptor/">Human Beta2-Adrenergic Receptor (beta2 AR)</a> — Used as molecular replacement search model (PDB 2RH1)
- <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4 Lysozyme (T4L)</a> — Fusion partner used for crystallization
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Lipid used for in meso crystallization
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesteryl Hemisuccinate (CHS)</a> — Stabilizing additive used throughout purification
- <a href="/xray-mp-wiki/reagents/ligands/theophylline/">Theophylline</a> — Nonspecific antagonist used for stabilization during purification
- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr/">GPCR</a> — A2AR is a class A GPCR
- <a href="/xray-mp-wiki/reagents/ligands/caffeine/">Caffeine</a> — Xanthine antagonist co-crystallized with StaR2 construct (PDB 3RFM)
- <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL (apocytochrome b562RIL)</a> — Fusion protein used to replace ICL3 for high-resolution 1.8 A crystallization
- <a href="/xray-mp-wiki/reagents/ligands/sodium-ion/">Sodium Ion</a> — Identified in the central water cluster as an allosteric modulator of A2AAR
- <a href="/xray-mp-wiki/concepts/signaling-receptors/sodium-allosteric-modulation/">Sodium Allosteric Modulation</a> — Structural basis for allosteric regulation of GPCRs by sodium ions
- <a href="/xray-mp-wiki/proteins/gpcr/human-adenosine-a2a-receptor-a2ar/">Human Adenosine A2A Receptor (A2AR)</a> — [A2AAR](/xray-mp-wiki/proteins/human-adenosine-a2a-receptor-a2ar)-D52N is a point mutant of the wild-type A2AR
- <a href="/xray-mp-wiki/proteins/gpcr/human-adenosine-a2a-receptor-a2ar/">Human Adenosine A2A Receptor S91A Variant (A2AAR-S91A)</a> — Another sodium-site variant solved in the same study
- <a href="/xray-mp-wiki/reagents/ligands/lj-4517/">LJ-4517 (Compound 2)</a> — Nucleoside antagonist for comparison with nucleoside agonist [UK432097](/xray-mp-wiki/reagents/ligands/uk-432097)
- <a href="/xray-mp-wiki/reagents/ligands/uk-432097/">UK432097</a> — Full agonist co-crystallized with [A2AAR](/xray-mp-wiki/proteins/human-adenosine-a2a-receptor-a2ar)-D52N (PDB 5WF5)
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Detergent used for solubilization and purification
- <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> — Added to [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) mixture for membrane protein stability
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — Crystallization method used for structure determination
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement) using Phaser
- <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression">Baculovirus Expression System</a> — Expression system used for protein production
- <a href="/xray-mp-wiki/proteins/gpcr/human-adenosine-a2a-receptor-a2ar/">Human Adenosine A2A Receptor D52N Variant (A2AAR-D52N)</a> — Sodium-site variant solved in the same study with PDB 5WF5
- <a href="/xray-mp-wiki/proteins/human-adenosine-a2a-receptor-a2ar">Human Adenosine A2A Receptor (A2AR)</a> — A2A-StaR2-[BRIL](/xray-mp-wiki/reagents/protein-tags/bril) is an engineered construct of the human A2AR
- <a href="/xray-mp-wiki/proteins/a2a-psb1-bril">A2A-PSB1-bRIL Adenosine A2A Receptor</a> — Another thermostabilized A2AR-[BRIL](/xray-mp-wiki/reagents/protein-tags/bril) construct for comparison
- <a href="/xray-mp-wiki/reagents/ligands/lj-4517">LJ-4517 (Compound 2)</a> — Co-crystallized nucleoside antagonist ligand in PDB 8CU7
- <a href="/xray-mp-wiki/reagents/ligands/luf5833">LUF5833 (Compound 8)</a> — Co-crystallized partial agonist ligand in PDB 7ARO
- <a href="/xray-mp-wiki/reagents/ligands/theophylline">Theophylline</a> — Used for initial crystal formation and receptor stabilization
- <a href="/xray-mp-wiki/reagents/ligands/neca">NECA</a> — Full agonist reference structure (PDB 2YDV) for comparison
- <a href="/xray-mp-wiki/reagents/ligands/zm241385">ZM241385</a> — Antagonist reference structure (PDB 5IU4/6WQA) for comparison
- <a href="/xray-mp-wiki/reagents/detergents/ddm">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Detergent used for solubilization and purification
- <a href="/xray-mp-wiki/reagents/additives/sodium-thiocyanate">Sodium Thiocyanate (NaSCN)</a> — Crystallization additive in the reservoir solution
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">LCP</a> — Crystallization method used for structure determination
- <a href="/xray-mp-wiki/proteins/gpcr/human-adenosine-a2a-receptor-a2ar/">Human Adenosine A2A Receptor A2A-StaR2-bRIL (PDB 7ARO)</a> — Parent construct without S277A mutation, same [BRIL](/xray-mp-wiki/reagents/protein-tags/bril) fusion design
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> — Buffer used in purification and crystallization
- <a href="/xray-mp-wiki/reagents/additives/sodium-thiocyanate/">Sodium Thiocyanate (NaSCN)</a> — Crystallization additive in the reservoir solution
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a> — Purification method used in protein preparation
