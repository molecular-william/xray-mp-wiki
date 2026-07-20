---
title: "Human MT1 Melatonin Receptor"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41586-019-1141-3]
verified: pdb-check
uniprot_id: P48039
---

# Human MT1 Melatonin Receptor

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P48039">UniProt: P48039</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

The MT1 melatonin receptor (type 1A) is a class A G-protein-coupled receptor that binds the neurohormone melatonin (N-acetyl-5-methoxytryptamine) and maintains circadian rhythms. The receptor is a target for insomnia drugs such as ramelteon and the antidepressant agomelatine. High-resolution room-temperature XFEL and synchrotron structures of MT1 in complex with four agonists (ramelteon, 2-PMT, 2-iodomelatonin, and agomelatine) reveal an unusually compact binding pocket sealed from extracellular solvent by extracellular loop 2, with a narrow lateral channel between transmembrane helices IV and V that connects the binding site to the lipid bilayer.


## Publications

### doi/10.1038##s41586-019-1141-3

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6me2">6ME2</a></td>
      <td>2.80</td>
      <td>P 4 2_1 2</td>
      <td>MT1-CC (PGS fusion, N-term trunc 11 aa, C-term trunc 25 aa, 9 point mutations)</td>
      <td>ramelteon</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6me3">6ME3</a></td>
      <td>2.90</td>
      <td>P 4 2_1 2</td>
      <td>MT1-CC (PGS fusion, N-term trunc 11 aa, C-term trunc 25 aa, 9 point mutations)</td>
      <td>2-PMT (2-phenylmelatonin)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6me4">6ME4</a></td>
      <td>3.20</td>
      <td>P 4 2_1 2</td>
      <td>MT1-CC (PGS fusion, N-term trunc 11 aa, C-term trunc 25 aa, 9 point mutations)</td>
      <td>2-iodomelatonin</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6me5">6ME5</a></td>
      <td>3.20</td>
      <td>P 4 2_1 2</td>
      <td>MT1-CC (PGS fusion, N-term trunc 11 aa, C-term trunc 25 aa, 9 point mutations)</td>
      <td>agomelatine</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda (Sf9) insect cells
- **Construct**: MT1-CC (human MT1 with N-terminal 11 aa [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/), C-terminal 25 aa [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/), ICL3 residues 219-227 replaced with PGS fusion; 9 thermostabilizing point mutations)
- **Notes**: Bac-to-bac baculovirus expression system; MOI 5; harvested 48h post-infection at 27C

**Purification:**

- **Expression system**: Sf9 insect cells
- **Expression construct**: MT1-CC (PGS fusion with His10-Flag-HA-PSP tags)
- **Tag info**: N-terminal HA signal, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), 10x His tag, [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) removable

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
      <td>Dounce homogenization and ultracentrifugation</td>
      <td>—</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 1 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a></td>
      <td>Membrane fraction isolated from 3L biomass; repeated homogenization and ultracentrifugation</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 150 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> / 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA / <a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a></td>
      <td>—</td>
      <td></td>
      <td>Standard immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td>—</td>
      <td></td>
      <td>Final polishing step</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>LCP (lipid cubic phase)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>~30 mg/mL MT1-CC in 50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 150 mM NaCl, 0.05%/0.01% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>/CHS, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a></td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>2:3 (w/w)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2-4 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals appeared in LCP with P4 2_1 2 space group; ramelteon complex crystals used for XFEL data collection, 2-PMT complex crystals optimized for synchrotron</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6me2">6ME2</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GTSQPVLRGDGA</span><span class="topo-outside">RPSWLAS</span><span class="topo-membrane">ALACVLIFTIVVDILGNLLVIL</span><span class="topo-inside">SVYRNKKLRNAGNI</span><span class="topo-membrane">FVVSLAVANLVVAIYPYPLVLM</span><span class="topo-outside">SIFNNGWNFGYLHCQV</span><span class="topo-membrane">SAFLMGLSVIGSIWNITGIAID</span><span class="topo-inside">RYLYI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">CHSLKYDKLYSSKNS</span><span class="topo-membrane">LCYVLLIWLLTLAAVLPNL</span><span class="topo-outside">RAGTLQYDPRIYSCTFAQSVSSAY</span><span class="topo-membrane">TIAVVVFHFLVPMIIVIFCYLR</span><span class="topo-inside">IWILVLQVRGIDCSFWNESYLTGSRDERKKSLLSKFGMDE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">GVTFMFIGRFDRGQKG</span><span class="topo-unknown">VDVLLKAIEILS</span><span class="topo-inside">SKKEFQEMRFIIIGKGDPELEGWARSLEEKHGNVKVITEMLSREFVRELYGSVDFVIIPSYFEPFGLVALEAMCLGAIPIASAVGGLRDIIT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">NETGILVKAGDPGELANAILKALELSRSDLSKFRENCKKRAMSFSKLKPQDFRNFVT</span><span class="topo-membrane">MFVVFVLFAICFAPLNFIGL</span><span class="topo-outside">AVASDPASMVPRIPEWL</span><span class="topo-membrane">FVASYYMAYFNSCLNPIIYGL</span><span class="topo-inside">LD</span><span class="topo-unknown">QNF</span></span>
<span class="topo-ruler">       490       500   </span>
<span class="topo-line"><span class="topo-unknown">RKEYRRIIVS</span><span class="topo-inside">LCTARVFF</span><span class="topo-unknown">VDSSN</span></span>
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
      <td>13</td>
      <td>19</td>
      <td>22</td>
      <td>28</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>41</td>
      <td>29</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>55</td>
      <td>51</td>
      <td>64</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>77</td>
      <td>65</td>
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
      <td>135</td>
      <td>125</td>
      <td>144</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>136</td>
      <td>154</td>
      <td>145</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>178</td>
      <td>164</td>
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
      <td>256</td>
      <td>1001</td>
      <td>1047</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>257</td>
      <td>268</td>
      <td>1048</td>
      <td>1059</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>269</td>
      <td>405</td>
      <td>1060</td>
      <td>1196</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>406</td>
      <td>417</td>
      <td>228</td>
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
      <td>454</td>
      <td>260</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>455</td>
      <td>475</td>
      <td>277</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>476</td>
      <td>477</td>
      <td>298</td>
      <td>299</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>478</td>
      <td>490</td>
      <td>300</td>
      <td>312</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>491</td>
      <td>498</td>
      <td>313</td>
      <td>320</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6me3">6ME3</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GTSQPVLRGDGAR</span><span class="topo-outside">PSWLAS</span><span class="topo-membrane">ALACVLIFTIVVDILGNLLVILS</span><span class="topo-inside">VYRNKKLRNAGN</span><span class="topo-membrane">IFVVSLAVANLVVAIYPYPLVLM</span><span class="topo-outside">SIFNNGWNFGYLHCQV</span><span class="topo-membrane">SAFLMGLSVIGSIWNITGIAID</span><span class="topo-inside">RYLYI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">CHSLKYDKLYSSKN</span><span class="topo-membrane">SLCYVLLIWLLTLAAVLPN</span><span class="topo-outside">LRAGTLQYDPRIYSCTFAQSVSSAY</span><span class="topo-membrane">TIAVVVFHFLVPMIIVIFCYL</span><span class="topo-inside">RIWILVLQVRGIDCSFWNESYLTGSRDERKKSLLSKFGMDE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">GVTFMFIGRFDRGQKGVDVLLKAIEILSSKKEFQEMRFIIIGKGDPELEGWARSLEEKHGNVKVITEMLSREFVRELYGSVDFVIIPSYFEPFGLVALEAMCLGAIPIASAVGGLRDIIT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">NETGILVKAGDPGELANAILKALELSRSDLSKFRENCKKRAMSFSKLKPQDFRNFV</span><span class="topo-membrane">TMFVVFVLFAICFAPLNFIGLA</span><span class="topo-outside">VASDPASMVPRIPEW</span><span class="topo-membrane">LFVASYYMAYFNSCLNPIIYGL</span><span class="topo-inside">LDQNF</span></span>
<span class="topo-ruler">       490       500   </span>
<span class="topo-line"><span class="topo-inside">RKEYRRIIVSLCTARV</span><span class="topo-unknown">FFVDSSN</span></span>
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
      <td>19</td>
      <td>23</td>
      <td>28</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>42</td>
      <td>29</td>
      <td>51</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>43</td>
      <td>54</td>
      <td>52</td>
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
      <td>199</td>
      <td>188</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>200</td>
      <td>209</td>
      <td>209</td>
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
      <td>438</td>
      <td>239</td>
      <td>260</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>439</td>
      <td>453</td>
      <td>261</td>
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
      <td>496</td>
      <td>298</td>
      <td>318</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>497</td>
      <td>503</td>
      <td>319</td>
      <td>325</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6me4">6ME4</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GTSQPVLRGDGAR</span><span class="topo-outside">PSWLAS</span><span class="topo-membrane">ALACVLIFTIVVDILGNLLVIL</span><span class="topo-inside">SVYRNKKLRNAGN</span><span class="topo-membrane">IFVVSLAVANLVVAIYPYPLVLM</span><span class="topo-outside">SIFNNGWNFGYLHCQV</span><span class="topo-membrane">SAFLMGLSVIGSIWNITGIAID</span><span class="topo-inside">RYLYI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">CHSLKYDKLYSSKN</span><span class="topo-membrane">SLCYVLLIWLLTLAAVLPN</span><span class="topo-outside">LRAGTLQYDPRIYSCTFAQSVSSAY</span><span class="topo-membrane">TIAVVVFHFLVPMIIVIFCYL</span><span class="topo-inside">RIWILVLQVRGIDCSFWNESYLTGSRDERKKSLLSKFGMDE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">GVTFMFIGRFDRGQKGVDVLLKAIEILSSKKEFQEMRFIIIGKGDPELEGWARSLEEKHGNVKVITEMLSREFVRELYGSVDFVIIPSYFEPFGLVALEAMCLGAIPIASAVGGLRDIIT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">NETGILVKAGDPGELANAILKALELSRSDLSKFRENCKKRAMSFSKLKPQDFRNFVT</span><span class="topo-membrane">MFVVFVLFAICFAPLNFIGLA</span><span class="topo-outside">VASDPASMVPRIPEW</span><span class="topo-membrane">LFVASYYMAYFNSCLNPIIYGL</span><span class="topo-inside">LDQNF</span></span>
<span class="topo-ruler">       490       500   </span>
<span class="topo-line"><span class="topo-inside">RKEYRRIIVSLCTARVFF</span><span class="topo-unknown">VDSSN</span></span>
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
      <td>19</td>
      <td>23</td>
      <td>28</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>41</td>
      <td>29</td>
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
      <td>199</td>
      <td>188</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>200</td>
      <td>209</td>
      <td>209</td>
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
      <td>417</td>
      <td>228</td>
      <td>239</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>418</td>
      <td>438</td>
      <td>240</td>
      <td>260</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>439</td>
      <td>453</td>
      <td>261</td>
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
      <td>498</td>
      <td>298</td>
      <td>320</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>499</td>
      <td>503</td>
      <td>321</td>
      <td>325</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6me5">6ME5</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GTSQPVLRGDGAR</span><span class="topo-outside">PSWLAS</span><span class="topo-membrane">ALACVLIFTIVVDILGNLLVIL</span><span class="topo-inside">SVYRNKKLRNAGNI</span><span class="topo-membrane">FVVSLAVANLVVAIYPYPLVLM</span><span class="topo-outside">SIFNNGWNFGYLHCQ</span><span class="topo-membrane">VSAFLMGLSVIGSIWNITGIAI</span><span class="topo-inside">DRYLYI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">CHSLKYDKLYSSKNS</span><span class="topo-membrane">LCYVLLIWLLTLAAVLPNL</span><span class="topo-outside">RAGTLQYDPRIYSCTFAQSVSSAY</span><span class="topo-membrane">TIAVVVFHFLVPMIIVIFCYLR</span><span class="topo-inside">IWILVLQVRGIDCSFWNESYLTGSRDERKKSLLSKFGMDE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">GVTFMFIGRFDRGQKGVDVLLKAIEILSSKKEFQEMRFIIIGKGDPELEGWARSLEEKHGNVKVITEMLSREFVRELYGSVDFVIIPSYFEPFGLVALEAMCLGAIPIASAVGGLRDIIT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">NETGILVKAGDPGELANAILKALELSRSDLSKFRENCKKRAMSFSKLKPQDFRNFVT</span><span class="topo-membrane">MFVVFVLFAICFAPLNFIGL</span><span class="topo-outside">AVASDPASMVPRIPEWL</span><span class="topo-membrane">FVASYYMAYFNSCLNPIIYGL</span><span class="topo-inside">LDQNF</span></span>
<span class="topo-ruler">       490       500   </span>
<span class="topo-line"><span class="topo-inside">RKEYRRIIVSLCTARVFF</span><span class="topo-unknown">VDSSN</span></span>
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
      <td>19</td>
      <td>23</td>
      <td>28</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>41</td>
      <td>29</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>55</td>
      <td>51</td>
      <td>64</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>77</td>
      <td>65</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>92</td>
      <td>87</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>114</td>
      <td>102</td>
      <td>123</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>135</td>
      <td>124</td>
      <td>144</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>136</td>
      <td>154</td>
      <td>145</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>178</td>
      <td>164</td>
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
      <td>417</td>
      <td>228</td>
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
      <td>454</td>
      <td>260</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>455</td>
      <td>475</td>
      <td>277</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>476</td>
      <td>498</td>
      <td>298</td>
      <td>320</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>499</td>
      <td>503</td>
      <td>321</td>
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

## Biological / Functional Insights

### Lateral Ligand Access Channel

MT1 has a sealed extracellular binding pocket with a narrow lateral channel between TM4 and TM5 that connects the binding site to the lipid bilayer. This channel provides an atypical entry pathway for lipophilic ligands directly from the membrane, explaining how neutral lipophilic ligands like melatonin access the binding site without traversing the extracellular space. The channel entrance lies approximately 6.5-10.9 Å below the membrane boundary.

### YPYP Motif in Helix II

A unique YPYP motif (Y79-P80-Y81-P82) in helix II creates a bulge that shapes the ligand binding pocket. This motif is specific to melatonin receptors and GPR50, and is not found in any other human GPCR. Mutation of any residue in this motif reduces thermostability by 6-10°C and impairs receptor function.

### Compact Binding Site Architecture

The MT1 binding site is extremely compact (710 Å³ with ramelteon), among the smallest in class A GPCRs. Ligands interact primarily through aromatic stacking with F179^ECL2 and hydrogen bonds with N162^4.60 and Q181^ECL2. The small binding pocket and lateral channel impose constraints on ligand size and physicochemical properties, with 98% of high-affinity ligands being neutral at physiological pH.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/5ht2a-receptor/">Human 5-HT2A Receptor</a> — Comparison of melatonin vs serotonin receptor binding site evolution; agomelatine binds both receptors
- <a href="/xray-mp-wiki/proteins/gpcr/5ht2c-receptor/">Human 5-HT2C Receptor</a> — Agomelatine acts as antagonist at 5-HT2C; structural comparison of binding modes
- <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/proteins/gpcr/human-mt2-melatonin-receptor/">Human MT2 Melatonin Receptor</a> — Sister subtype; companion paper (10.1038/s41586-019-1144-0) describes MT2 structures revealing subtype selectivity
