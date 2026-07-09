---
title: "Human Aquaporin 10 (AQP10)"
created: 2026-06-16
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-018-07176-z]
verified: regex
uniprot_id: Q96PS8
---

# Human Aquaporin 10 (AQP10)

<div class="expr-badges"><span class="expr-badge expr-s-cerevisiae">S. cerevisiae</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q96PS8">UniProt: Q96PS8</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

Human [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) 10 (AQP10) is an
aquaglyceroporin expressed in human adipocytes and the small intestine that
facilitates glycerol transport. Unlike other human aquaglyceroporins, AQP10
is uniquely stimulated by low pH, with increased glycerol release during
lipolysis (fat burning) correlating with intracellular acidification. The
crystal structure of human AQP10 was determined at 2.3 Å resolution (space
group P2_1_2_1_2_1, cell dimensions a=97.1 Å, b=116.8 Å, c=138.5 Å),
revealing an exceptionally wide ar/R selectivity filter and a unique
cytoplasmic gate. Functional and structural analyses identified His80 as
the pH sensor, with protonation of His80 triggering gate opening via
interaction with Glu27 and concerted rearrangements of Phe85 and the
V76-S77 loop. This pH-gating mechanism is glycerol-specific, allowing
water but not glycerol passage at neutral pH, and represents a unique type
of aquaporin regulation important for controlling body fat mass.


## Publications

### doi/10.1038##s41467-018-07176-z

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6f7h">6F7H</a></td>
      <td>2.3</td>
      <td>P2_1_2_1_2_1</td>
      <td>Human AQP10 C-terminally truncated construct (residues 1-270), wild-type</td>
      <td>Glycerol (1 molecule per monomer)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Saccharomyces cerevisiae (strain PAP1500)
- **Construct**: Human AQP10 (wild-type) with C-terminal His tag or GFP fusion

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
      <td>Cell lysis</td>
      <td>Homogenization</td>
      <td>—</td>
      <td>Lysis buffer</td>
      <td>Yeast cells harvested and disrupted</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Ni-NTA resin</td>
      <td>Standard His-tag purification buffer</td>
      <td>Purified via C-terminal His tag</td>
    </tr>
    <tr>
      <td>Tag removal</td>
      <td>Thrombin cleavage</td>
      <td>—</td>
      <td>Cleavage buffer</td>
      <td>His tag removed by thrombin for crystallization</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td>—</td>
      <td>SEC buffer with detergent</td>
      <td>Final polishing step</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified AQP10 in detergent solution

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (sitting drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified AQP10 at appropriate concentration</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Optimized crystallization condition</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>277</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Data collected at SLS beamline X06SA, Paul Scherrer Institut, Villigen, Switzerland. Phased by molecular replacement using GlpF (pdb-id 1LDI). Space group P2_1_2_1_2_1 with cell a=97.1 Å, b=116.8 Å, c=138.5 Å, one tetramer in the asymmetric unit. Model built in COOT and refined in phenix.refine to Rwork 18.9%.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6f7h">6F7H</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MVFTQAPAEIMGHLRIR</span><span class="topo-inside">SLLARQ</span><span class="topo-membrane">CLAEFLGVFVLMLLTQGAV</span><span class="topo-outside">AQAVTSGETKGNFF</span><span class="topo-membrane">TMFLAGSLAVTIAIYVGGNV</span><span class="topo-inside">SG</span><span class="topo-unknown">AHLNPAFSLAMCI</span><span class="topo-inside">VGRLPW</span><span class="topo-membrane">VKLPIYILVQLLSAFCASGATYV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LY</span><span class="topo-outside">HDALQNYTGGNLTVTGPKETASIFATYPAPYLSLNNG</span><span class="topo-membrane">FLDQVLGTGMLIVGLLAI</span><span class="topo-inside">LDRRNKGVPAGL</span><span class="topo-membrane">EPVVVGMLILALGLSMG</span><span class="topo-outside">ANC</span><span class="topo-unknown">GIPLNPARDLGPRLF</span><span class="topo-outside">TYVAGWGPEVFSAGNG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-outside">WW</span><span class="topo-membrane">WVPVVAPLVGATVGTATYQLL</span><span class="topo-inside">VALHH</span><span class="topo-unknown">PEGPEPAQDLVSAQHKASELETPASAQMLECKL</span></span>
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
      <td>17</td>
      <td>1</td>
      <td>17</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>18</td>
      <td>23</td>
      <td>18</td>
      <td>23</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>24</td>
      <td>42</td>
      <td>24</td>
      <td>42</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>43</td>
      <td>56</td>
      <td>43</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>76</td>
      <td>57</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>77</td>
      <td>78</td>
      <td>77</td>
      <td>78</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>91</td>
      <td>79</td>
      <td>91</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>92</td>
      <td>97</td>
      <td>92</td>
      <td>97</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>122</td>
      <td>98</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>159</td>
      <td>123</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>177</td>
      <td>160</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>189</td>
      <td>178</td>
      <td>189</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>206</td>
      <td>190</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>209</td>
      <td>207</td>
      <td>209</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>210</td>
      <td>224</td>
      <td>210</td>
      <td>224</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>225</td>
      <td>242</td>
      <td>225</td>
      <td>242</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>243</td>
      <td>263</td>
      <td>243</td>
      <td>263</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>264</td>
      <td>268</td>
      <td>264</td>
      <td>268</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>269</td>
      <td>301</td>
      <td>269</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6f7h">6F7H</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MVFTQAPAEIMGHLRIR</span><span class="topo-inside">SLLARQC</span><span class="topo-membrane">LAEFLGVFVLMLLTQGAV</span><span class="topo-outside">AQAVTSGETKGNFF</span><span class="topo-membrane">TMFLAGSLAVTIAIYVGGNV</span><span class="topo-inside">SGA</span><span class="topo-unknown">HLNPAFSLAMCI</span><span class="topo-inside">VGRLPWVK</span><span class="topo-membrane">LPIYILVQLLSAFCASGATYV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">L</span><span class="topo-outside">YHDALQNYTGGNLTVTGPKETASIFATYPAPYLSLN</span><span class="topo-membrane">NGFLDQVLGTGMLIVGLLAI</span><span class="topo-inside">LDRRNKGVPAGL</span><span class="topo-membrane">EPVVVGMLILALGLSMG</span><span class="topo-outside">AN</span><span class="topo-unknown">CGIPLNPARDLGPRLFT</span><span class="topo-outside">YVAGWGPEVFSAGNG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-outside">WW</span><span class="topo-membrane">WVPVVAPLVGATVGTATY</span><span class="topo-inside">QLLVALHHP</span><span class="topo-unknown">EGPEPAQDLVSAQHKASELETPASAQMLECKL</span></span>
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
      <td>17</td>
      <td>1</td>
      <td>17</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>18</td>
      <td>24</td>
      <td>18</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>42</td>
      <td>25</td>
      <td>42</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>43</td>
      <td>56</td>
      <td>43</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>76</td>
      <td>57</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>77</td>
      <td>79</td>
      <td>77</td>
      <td>79</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>91</td>
      <td>80</td>
      <td>91</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>92</td>
      <td>99</td>
      <td>92</td>
      <td>99</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>100</td>
      <td>121</td>
      <td>100</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>122</td>
      <td>157</td>
      <td>122</td>
      <td>157</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>177</td>
      <td>158</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>189</td>
      <td>178</td>
      <td>189</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>206</td>
      <td>190</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>208</td>
      <td>207</td>
      <td>208</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>209</td>
      <td>225</td>
      <td>209</td>
      <td>225</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>226</td>
      <td>242</td>
      <td>226</td>
      <td>242</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>243</td>
      <td>260</td>
      <td>243</td>
      <td>260</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>261</td>
      <td>269</td>
      <td>261</td>
      <td>269</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>270</td>
      <td>301</td>
      <td>270</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6f7h">6F7H</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MVFTQAPAEIMGHLR</span><span class="topo-inside">IRSLL</span><span class="topo-membrane">ARQCLAEFLGVFVLMLLTQGA</span><span class="topo-outside">VAQAVTSGETKGNFF</span><span class="topo-membrane">TMFLAGSLAVTIAIYVGGNVS</span><span class="topo-inside">G</span><span class="topo-unknown">AHLNPAFSLAMCI</span><span class="topo-inside">VGRLPW</span><span class="topo-membrane">VKLPIYILVQLLSAFCASGAT</span><span class="topo-outside">YV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LYHDALQNYTGGNLTVTGPKETASIFATYPAPYLSLNNG</span><span class="topo-membrane">FLDQVLGTGMLIVGLLAI</span><span class="topo-inside">LDRRNKGVPAGL</span><span class="topo-membrane">EPVVVGMLILALGLSMG</span><span class="topo-outside">ANCG</span><span class="topo-unknown">IPLNPARDLGPRLF</span><span class="topo-outside">TYVAGWGPEVFSAGNG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-outside">WWW</span><span class="topo-membrane">VPVVAPLVGATVGTATYQLL</span><span class="topo-inside">VALHH</span><span class="topo-unknown">PEGPEPAQDLVSAQHKASELETPASAQMLECKL</span></span>
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
      <td>15</td>
      <td>1</td>
      <td>15</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>16</td>
      <td>20</td>
      <td>16</td>
      <td>20</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>21</td>
      <td>41</td>
      <td>21</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>56</td>
      <td>42</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>77</td>
      <td>57</td>
      <td>77</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>78</td>
      <td>78</td>
      <td>78</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>91</td>
      <td>79</td>
      <td>91</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>92</td>
      <td>97</td>
      <td>92</td>
      <td>97</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>118</td>
      <td>98</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>159</td>
      <td>119</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>177</td>
      <td>160</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>189</td>
      <td>178</td>
      <td>189</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>206</td>
      <td>190</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>210</td>
      <td>207</td>
      <td>210</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>224</td>
      <td>211</td>
      <td>224</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>225</td>
      <td>243</td>
      <td>225</td>
      <td>243</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>263</td>
      <td>244</td>
      <td>263</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>264</td>
      <td>268</td>
      <td>264</td>
      <td>268</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>269</td>
      <td>301</td>
      <td>269</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6f7h">6F7H</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MVFTQAPAEIMG</span><span class="topo-inside">HLRIRSLLARQ</span><span class="topo-membrane">CLAEFLGVFVLMLLTQGA</span><span class="topo-outside">VAQAVTSGETKGNFF</span><span class="topo-membrane">TMFLAGSLAVTIAIYVGGNV</span><span class="topo-inside">SG</span><span class="topo-unknown">AHLNPAFSLAMCIV</span><span class="topo-inside">GRLPW</span><span class="topo-membrane">VKLPIYILVQLLSAFCASGATYV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">L</span><span class="topo-outside">YHDALQNYTGGNLTVTGPKETASIFATYPAPYLSLNNGF</span><span class="topo-membrane">LDQVLGTGMLIVGLLAIL</span><span class="topo-inside">DRRNKGVPAGL</span><span class="topo-membrane">EPVVVGMLILALGLSMG</span><span class="topo-outside">ANCG</span><span class="topo-unknown">IPLNPARDLGPRLF</span><span class="topo-outside">TYVAGWGPEVFSAGNG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-outside">WWW</span><span class="topo-membrane">VPVVAPLVGATVGTATYQLL</span><span class="topo-inside">VALHH</span><span class="topo-unknown">PEGPEPAQDLVSAQHKASELETPASAQMLECKL</span></span>
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
      <td>12</td>
      <td>1</td>
      <td>12</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>13</td>
      <td>23</td>
      <td>13</td>
      <td>23</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>24</td>
      <td>41</td>
      <td>24</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>56</td>
      <td>42</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>76</td>
      <td>57</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>77</td>
      <td>78</td>
      <td>77</td>
      <td>78</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>92</td>
      <td>79</td>
      <td>92</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>97</td>
      <td>93</td>
      <td>97</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>121</td>
      <td>98</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>122</td>
      <td>160</td>
      <td>122</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>178</td>
      <td>161</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>189</td>
      <td>179</td>
      <td>189</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>206</td>
      <td>190</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>210</td>
      <td>207</td>
      <td>210</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>224</td>
      <td>211</td>
      <td>224</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>225</td>
      <td>243</td>
      <td>225</td>
      <td>243</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>263</td>
      <td>244</td>
      <td>263</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>264</td>
      <td>268</td>
      <td>264</td>
      <td>268</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>269</td>
      <td>301</td>
      <td>269</td>
      <td>301</td>
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

### pH-dependent glycerol gating through His80 pH sensor

AQP10 displays pH-dependent glycerol-specific gating at the intracellular
interface, in contrast to other known aquaporin structures. His80 serves as
the pH sensor: at low pH, His80 becomes protonated (double protonated state),
triggering interaction with Glu27. This causes concerted structural changes
in nearby Phe85 and the cytoplasmic V76-S77 loop, opening the gate for
glycerol passage. At neutral pH (mono protonated state), the gate remains
closed to glycerol while remaining permeable to water.

### Unusually wide ar/R selectivity filter

The aromatic/arginine (ar/R) selectivity filter of AQP10 is exceptionally
wide compared to other aquaporins. While orthodox aquaporins (e.g., hAQP2)
and other aquaglyceroporins (e.g., GlpF, AqpM, PfAQP) have narrower
constrictions, AQP10's ar/R filter has a larger minimal diameter, enabling
efficient glycerol passage when the cytoplasmic gate is open.

### Cytoplasmic gate architecture

The cytoplasmic gate region is formed by residues H80, F85, R94, E27, V76
and S77. The G73G74 motif in TM2 is critical for kinking the helix and
allowing loop B to participate in gating. MD simulations with different
protonation states of H80 identified four main conformational clusters,
ranging from closed to fully open, providing a detailed model of the
gating mechanism.

### Physiological role in adipocyte glycerol release

In human adipocytes, lipolysis (induced by isoproterenol) causes
intracellular acidification, which correlates with increased glycerol
release through AQP10. Targeting the cytoplasmic gate to induce
constitutive glycerol secretion may offer an attractive option for
treating obesity and related complications.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/">Aquaporin Family</a> — AQP10 belongs to the aquaglyceroporin subfamily of the aquaporin superfamily
- <a href="/xray-mp-wiki/proteins/other-ion-channels/human-aqp7/">Human Aquaporin 7 (AQP7)</a> — AQP7 is another human aquaglyceroporin; structural comparison with AQP10 reveals differences in selectivity filter and gating
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/ph-dependent-gating/">pH-Dependent Gating</a> — AQP10 exhibits pH-dependent glycerol gating via His80 protonation sensor
