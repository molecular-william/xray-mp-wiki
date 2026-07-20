---
title: "SLC26Dg (Deinococcus geothermalis Fumarate Transporter)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.3091]
verified: agent
uniprot_id: Q1J2S8
---

# SLC26Dg (Deinococcus geothermalis Fumarate Transporter)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q1J2S8">UniProt: Q1J2S8</a>

<span class="expr-badge">Deinococcus geothermalis (strain DSM 11300)</span>

## Overview

SLC26Dg is a prokaryotic fumarate transporter from the bacterium Deinococcus geothermalis, representing the first full-length structure of an SLC26 family member. It functions as a proton-coupled fumarate symporter, transporting dicarboxylic acids across the membrane in an electrogenic process. The SLC26 (SulP) family of anion transporters is ubiquitous in pro- and eukaryotes and includes human members whose malfunction causes severe diseases such as growth defects, chronic diarrhea, and deafness. The human protein Prestin, an SLC26 member that confers electromotility to cochlear outer hair cells, shares 46% residue similarity with SLC26Dg in its transmembrane region. The structure reveals a modular architecture combining a 14-helix transmembrane domain with a cytoplasmic STAS domain, providing a common framework for the diverse functional behavior of the SLC26 family.


## Publications

### doi/10.1038##nsmb.3091

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5da0">5DA0</a></td>
      <td>3.2</td>
      <td>C2</td>
      <td>Full-length SLC26Dg from D. geothermalis in complex with nanobody Nb5776</td>
      <td>Nanobody Nb5776 (crystallization aid); ligand-free conformation</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5iof">5IOF</a></td>
      <td>4.2</td>
      <td>P1</td>
      <td>SLC26Dg deltaSTAS (residues 1-401, truncated STAS domain) from D. geothermalis</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli MC1061
- **Construct**: SLC26Dg with C-terminal HRV 3C protease site, GFP, and His10 tag. Grown in Terrific Broth with ampicillin, induced with 0.005% L-arabinose at 25 C for 16 h.
- **Induction**: 0.005% L-arabinose
- **Media**: Terrific Broth with [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin)

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
      <td>Cell resuspension and lysis</td>
      <td>Osmotic shock and Emulsiflex C3 disruption</td>
      <td>--</td>
      <td>50 mM potassium phosphate pH 7.5, 150 mM NaCl, 1 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride">MGCL2</a>, 1 mg/ml lysozyme + --</td>
      <td>Cells resuspended and incubated with lysozyme at 4 C for 1 h before disruption</td>
    </tr>
    <tr>
      <td>Membrane vesicle preparation</td>
      <td>Ultracentrifugation</td>
      <td>--</td>
      <td>50 mM potassium phosphate pH 7.5, 150 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a> + --</td>
      <td>Membrane vesicles obtained after low-spin centrifugation and ultracentrifugation</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>50 mM potassium phosphate pH 7.5, 150 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a> + 1-1.5% n-decyl-beta-D-maltoside (<a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>, Anatrace)</td>
      <td>Membrane proteins extracted for 1 h at 0.1 g/ml in buffer A supplemented with <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a> (IMAC)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) resin</td>
      <td>Buffer containing <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> + <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>Solubilized SLC26Dg purified by IMAC; HRV 3C protease cleavage during dialysis against buffer without <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a></td>
    </tr>
    <tr>
      <td>Tag removal and <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)</td>
      <td>Superdex S200 column (GE Healthcare)</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.5, 150 mM NaCl + 0.2% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>Histidine-tagged GFP and protease removed by IMAC; cleaved protein concentrated and subjected to <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>SLC26Dg-Nb5776 complex at molar ratio 1:3; full-length monomeric SLC26Dg in complex with Nb5776</td>
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
      <td>Notes</td>
      <td>Full-length transporter initially yielded crystals at 7-A resolution; improved crystals at 3.2-A obtained after generating nanobodies against SLC26Dg and using them as crystallization aids. Space group C2, single copy in asymmetric unit. <a href="/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/">SAD</a> phasing from <a href="/xray-mp-wiki/reagents/additives/selenomethionine">Selenomethionine (SeMet)</a>-derivatized transporter.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>SLC26Dg deltaSTAS (truncated construct, residues 1-401)</td>
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
      <td>Notes</td>
      <td>Truncated construct crystallized readily in several conditions. Best crystal form space group P1 diffracting to 4.2-A resolution.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5da0">5DA0</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTVHSPRFDLRQY</span><span class="topo-inside">QREWFANP</span><span class="topo-membrane">RKDVLAGIVVALALIPEAIAFSIIAG</span><span class="topo-outside">VDPQV</span><span class="topo-membrane">GLYASFIIALITAFLG</span><span class="topo-inside">GRPGM</span><span class="topo-membrane">ISAATGAMALLMTGLVK</span><span class="topo-outside">DHGIQY</span><span class="topo-membrane">LFAATVLTGVLQVVFGW</span><span class="topo-inside">AKL</span><span class="topo-unknown">ARYL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">KF</span><span class="topo-inside">VPRSVMVG</span><span class="topo-membrane">FVNALAILIFMAQLPQF</span><span class="topo-outside">VGANWQM</span><span class="topo-membrane">YAMVAAGLAIIYLLPLVF</span><span class="topo-inside">K</span><span class="topo-membrane">AMPSALVAIVVLTV</span><span class="topo-outside">VAVVTGADVKTVGDMGTLPTALPHFQFPQVPLT</span><span class="topo-membrane">FETLAIIFPVALTLSLVGL</span><span class="topo-inside">L</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">ESLLTAQLIDERTDTTSDKNVE</span><span class="topo-membrane">SRGQGVANIVTGFFG</span><span class="topo-outside">G</span><span class="topo-membrane">MAGCAMIGQS</span><span class="topo-inside">MINVTSGGRGR</span><span class="topo-membrane">LSTFVAGAFLMVLI</span><span class="topo-outside">LALQPLLVQIPM</span><span class="topo-membrane">AALVAVMMVVAISTF</span><span class="topo-inside">DWGSLR</span><span class="topo-unknown">TLTV</span><span class="topo-inside">FPKGETVVML</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">ATVAVTVFT</span><span class="topo-outside">H</span><span class="topo-membrane">DLSLGVLIGVV</span><span class="topo-inside">LSALFFARKVSQLSQVTPVDEVDGTRTYRVRGQLFFVSTHDFLHQFDFTHPARRVVIDLSDAHFWDGSAVGALDKVMLKFMRQGTSVELRGLNAASATL</span></span>
<span class="topo-ruler">       490       500     </span>
<span class="topo-line"><span class="topo-inside">VERL</span><span class="topo-unknown">AVHDKPDALDRMGGHSLGVLP</span></span>
<details class="topo-details"><summary>Topology coordinates (32 regions)</summary>
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
      <td>14</td>
      <td>21</td>
      <td>14</td>
      <td>21</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>22</td>
      <td>47</td>
      <td>22</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>52</td>
      <td>48</td>
      <td>52</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>68</td>
      <td>53</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>73</td>
      <td>69</td>
      <td>73</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>90</td>
      <td>74</td>
      <td>90</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>96</td>
      <td>91</td>
      <td>96</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>113</td>
      <td>97</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>116</td>
      <td>114</td>
      <td>116</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>122</td>
      <td>117</td>
      <td>122</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>123</td>
      <td>130</td>
      <td>123</td>
      <td>130</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>131</td>
      <td>147</td>
      <td>131</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>154</td>
      <td>148</td>
      <td>154</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>155</td>
      <td>172</td>
      <td>155</td>
      <td>172</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>173</td>
      <td>173</td>
      <td>173</td>
      <td>173</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>187</td>
      <td>174</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>188</td>
      <td>220</td>
      <td>188</td>
      <td>220</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>239</td>
      <td>221</td>
      <td>239</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>240</td>
      <td>262</td>
      <td>240</td>
      <td>262</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>263</td>
      <td>277</td>
      <td>263</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>278</td>
      <td>278</td>
      <td>278</td>
      <td>278</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>288</td>
      <td>279</td>
      <td>288</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>289</td>
      <td>299</td>
      <td>289</td>
      <td>299</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>313</td>
      <td>300</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>325</td>
      <td>314</td>
      <td>325</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>340</td>
      <td>326</td>
      <td>340</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>341</td>
      <td>346</td>
      <td>341</td>
      <td>346</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>351</td>
      <td>360</td>
      <td>351</td>
      <td>360</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>361</td>
      <td>369</td>
      <td>361</td>
      <td>369</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>370</td>
      <td>370</td>
      <td>370</td>
      <td>370</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>371</td>
      <td>381</td>
      <td>371</td>
      <td>381</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>382</td>
      <td>484</td>
      <td>382</td>
      <td>484</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5iof">5IOF</a> — Chain A (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTVHSPRFDLRQY</span><span class="topo-outside">QREWFANPRKDVLAG</span><span class="topo-membrane">IVVALALIPEAIAFSIIAGVD</span><span class="topo-inside">P</span><span class="topo-membrane">QVGLYASFIIALITAFLG</span><span class="topo-outside">GRPGMI</span><span class="topo-membrane">SAATGAMALLMTGLV</span><span class="topo-inside">KDHGI</span><span class="topo-membrane">QYLFAATVLTGVLQVVFGWA</span><span class="topo-outside">KL</span><span class="topo-unknown">ARYL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">KF</span><span class="topo-outside">VPRSV</span><span class="topo-membrane">MVGFVNALAILIFMAQLPQF</span><span class="topo-inside">VGANW</span><span class="topo-membrane">QMYAMVAAGLAIIYLLP</span><span class="topo-outside">LVFKAM</span><span class="topo-membrane">PSALVAIVVLTVVAVVT</span><span class="topo-inside">GADVKTVGDMGTLPTALPHFQFPQVPLTFET</span><span class="topo-membrane">LAIIFPVALTLSLVGLL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">ES</span><span class="topo-outside">LLTAQLIDERTDTTSDKNVES</span><span class="topo-membrane">RGQGVANIVTGFF</span><span class="topo-inside">G</span><span class="topo-unknown">GMAGCAMIGQ</span><span class="topo-outside">SMINVTSGGRGRL</span><span class="topo-membrane">STFVAGAFLMVLILALQPLL</span><span class="topo-inside">V</span><span class="topo-membrane">QIPMAALVAVMMVVAISTFD</span><span class="topo-outside">WGSLR</span><span class="topo-unknown">TLTV</span><span class="topo-outside">FPKGETV</span><span class="topo-membrane">VML</span></span>
<span class="topo-ruler">       370       380       390       400 </span>
<span class="topo-line"><span class="topo-membrane">ATVAVTVFTH</span><span class="topo-inside">D</span><span class="topo-membrane">LSLGVLIGVVLSAL</span><span class="topo-outside">FFARKV</span><span class="topo-unknown">SQLSQVTPVD</span></span>
<details class="topo-details"><summary>Topology coordinates (32 regions)</summary>
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
      <td>14</td>
      <td>28</td>
      <td>14</td>
      <td>28</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>49</td>
      <td>29</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>50</td>
      <td>50</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>68</td>
      <td>51</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>74</td>
      <td>69</td>
      <td>74</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>89</td>
      <td>75</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>94</td>
      <td>90</td>
      <td>94</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>114</td>
      <td>95</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>116</td>
      <td>115</td>
      <td>116</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>122</td>
      <td>117</td>
      <td>122</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>123</td>
      <td>127</td>
      <td>123</td>
      <td>127</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>128</td>
      <td>147</td>
      <td>128</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>152</td>
      <td>148</td>
      <td>152</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>169</td>
      <td>153</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>175</td>
      <td>170</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>192</td>
      <td>176</td>
      <td>192</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>193</td>
      <td>223</td>
      <td>193</td>
      <td>223</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>224</td>
      <td>242</td>
      <td>224</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>263</td>
      <td>243</td>
      <td>263</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>264</td>
      <td>276</td>
      <td>264</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>277</td>
      <td>277</td>
      <td>277</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>287</td>
      <td>278</td>
      <td>287</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>288</td>
      <td>300</td>
      <td>288</td>
      <td>300</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>301</td>
      <td>320</td>
      <td>301</td>
      <td>320</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>321</td>
      <td>321</td>
      <td>321</td>
      <td>321</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>322</td>
      <td>341</td>
      <td>322</td>
      <td>341</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>342</td>
      <td>346</td>
      <td>342</td>
      <td>346</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>351</td>
      <td>357</td>
      <td>351</td>
      <td>357</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>358</td>
      <td>370</td>
      <td>358</td>
      <td>370</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>371</td>
      <td>371</td>
      <td>371</td>
      <td>371</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>372</td>
      <td>385</td>
      <td>372</td>
      <td>385</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>386</td>
      <td>391</td>
      <td>386</td>
      <td>391</td>
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

### Inward-facing, ligand-free conformation with potential substrate-binding site

The SLC26Dg structure reveals an inward-facing conformation with a large 28-A-long and 8-A-wide aqueous cavity at the interface between the core and gate domains. A putative substrate-binding site sits at the center of the transporter. The cavity is lined predominantly by hydrophobic residues, with unpaired backbone amides at the N termini of helices 3 and 10 providing hydrogen-bond donors for interaction with the two carboxylates of fumarate. Two pseudosymmetry-related glutamates (E38 and E241) lie adjacent to the ligand-binding site with their carboxylate moieties oriented toward the cytoplasm; these residues are conserved in prokaryotic but not eukaryotic SLC26 transporters and may facilitate substrate release and proton cotransport.

### Transmembrane domain architecture with inverted repeats

The transmembrane domain of SLC26Dg consists of 14 alpha-helices organized into two structurally related halves of seven TM segments each, forming intertwined inverted repeats. The pseudosymmetry-related helices 1-4 and 8-11 fold into a compact core domain, while helices 5-7 and 12-14 form an elongated gate domain that shields one side of the core. This architecture resembles the unrelated [URAA](/xray-mp-wiki/proteins/uraA) transporter (NCS2 family), aligning with an RMS deviation of 3.5 A despite no obvious sequence relationship. This structural conservation supports predictions of relatedness between SLC26, NCS2, and SLC4 families.

### STAS domain regulates transport activity

The cytoplasmic STAS domain is compact, containing four beta-strands and three alpha-helices, and shows structural similarity to STAS domains of Prestin and DauA. Expression of the isolated TM domain (SLC26Dg deltaSTAS) produced a stable protein but with strongly compromised transport activity, demonstrating that the STAS domain regulates the transport activity of the TM domain. The STAS domain interacts exclusively with the [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody) Nb5776 via complementarity determining region 2, burying 1505 A^2 of combined molecular surface.

### Electrogenic proton-fumarate symport mechanism

Transport experiments demonstrate that SLC26Dg functions as a proton-coupled fumarate symporter. Transport is strongly enhanced by an inwardly directed pH gradient and is electrogenic, with fumarate/proton symport increased by positive and decreased by negative membrane potential. The apparent Km for fumarate is 2.7 mM, indicating weak affinity. The cumulative charge of substrates per cycle is negative. Competition assays show specificity for dicarboxylates over other anions.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/dm/">Decylmaltoside (DM)</a> — Primary solubilization detergent (1-1.5%) for SLC26Dg membrane extraction
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> — Used at 10 mM pH 7.5 in [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) buffer for SLC26Dg purification
- <a href="/xray-mp-wiki/reagents/buffers/potassium-phosphate/">Potassium Phosphate</a> — Resuspension buffer (50 mM pH 7.5) for cell lysis
- <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a> — 150 mM NaCl in purification buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — 10% glycerol in membrane vesicle buffer
- <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> — Nb5776 used as crystallization aid, binds STAS domain
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) method used to obtain improved crystals of SLC26Dg-Nb5776 complex
- <a href="/xray-mp-wiki/methods/structure-determination/single-anomalous-dispersion/">Single Anomalous Dispersion (SAD)</a> — [SAD](/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/) phasing used from selenomethionine-derivatized SLC26Dg crystals
- <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride">MGCL2</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/proteins/uraA">URAA</a> — Related protein
