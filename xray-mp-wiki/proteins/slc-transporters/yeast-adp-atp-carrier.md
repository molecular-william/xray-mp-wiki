---
title: "Yeast ADP/ATP Carrier (Aac2p and Aac3p)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1320692111]
verified: agent
uniprot_id: P18239
---

# Yeast ADP/ATP Carrier (Aac2p and Aac3p)

<div class="expr-badges"><span class="expr-badge expr-s-cerevisiae">S. cerevisiae</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P18239">UniProt: P18239</a>

<span class="expr-badge">Saccharomyces cerevisiae</span>

## Overview

The yeast ADP/ATP carriers (Aac2p and Aac3p) are archetypal members of the
mitochondrial carrier family that import ADP from the cytosol into the
mitochondrial matrix and export newly synthesized ATP to the cytosol. These
carriers cycle between a cytoplasmic state (c-state), in which the carrier
accepts ADP from the intermembrane space, and a matrix state (m-state), in
which it accepts ATP from the mitochondrial matrix. The crystal structures
of carboxyatractyloside (CATR)-inhibited Aac2p and Aac3p were determined at
2.5–3.4-Å resolution. Each carrier consists of six transmembrane α-helices
(H1–H6) arranged with threefold pseudosymmetry, forming a central cavity
open to the cytoplasmic side but closed to the mitochondrial matrix by three
interdomain salt-bridge interactions. A conserved glutamine residue braces
one of these salt bridges, contributing to an energy barrier that prevents
conversion to the m-state without substrate binding.


## Publications

### doi/10.1073/PNAS.1320692111

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4c9g">4C9G</a></td>
      <td>2.5</td>
      <td>C2221</td>
      <td>Full-length Saccharomyces cerevisiae Aac2p with N-terminal His tag</td>
      <td>CATR (carboxyatractyloside)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4c9g">4C9G</a></td>
      <td>3.2</td>
      <td>P212121</td>
      <td>Full-length S. cerevisiae Aac2p with N-terminal His tag</td>
      <td>CATR</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4c9g">4C9G</a></td>
      <td>3.4</td>
      <td>P212121</td>
      <td>Full-length S. cerevisiae Aac3p with N-terminal His tag</td>
      <td>CATR</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4c9g">4C9G</a></td>
      <td>3.2</td>
      <td>P21</td>
      <td>Full-length S. cerevisiae Aac3p with N-terminal His tag</td>
      <td>CATR</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Saccharomyces cerevisiae strain WB12
- **Construct**: AAC2 or AAC3 gene in modified pYES3 vector with N-terminal His tag and Factor Xa cleavage site
- **Notes**: Mitochondria prepared from disrupted cells

**Purification:**

- **Expression system**: S. cerevisiae WB12
- **Expression construct**: Aac2p or Aac3p with N-terminal His tag

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
      <td>Mitochondrial preparation</td>
      <td>Cell disruption</td>
      <td>—</td>
      <td></td>
      <td>Mitochondria isolated from disrupted yeast cells</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>undecyl-beta-D-maltoside</td>
      <td>Protein solubilized with undecyl-beta-D-maltoside</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni Sepharose <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>—</td>
      <td></td>
      <td>Purified by Ni Sepharose; detergent exchanged on-column</td>
    </tr>
    <tr>
      <td>Detergent exchange (Aac2p)</td>
      <td>On-column detergent exchange</td>
      <td>—</td>
      <td>5-cyclohexyl-1-pentyl-beta-D-maltoside (CYMAL-5)</td>
      <td>Exchanged while bound to Ni Sepharose resin</td>
    </tr>
    <tr>
      <td>Detergent exchange (Aac3p)</td>
      <td>On-column detergent exchange</td>
      <td>—</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/dm/">n-Decyl-β-D-maltoside</a> (DM)</td>
      <td>Exchanged while bound to Ni Sepharose resin</td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td>Factor Xa protease cleavage</td>
      <td>—</td>
      <td></td>
      <td>N-terminal His tag cleaved by Factor Xa</td>
    </tr>
    <tr>
      <td>Concentration</td>
      <td>Concentration</td>
      <td>—</td>
      <td></td>
      <td>Protein concentrated for crystallization</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified Aac2p or Aac3p in respective maltoside detergent

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Both proteins crystallized in two different crystal forms; data collected at ESRF beamline ID23-2</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4c9g">4C9G</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSSNAQVKTPLPPAPAPKKESNF</span><span class="topo-outside">LIDFLMG</span><span class="topo-membrane">GVSAAVAKTAASPIERVKL</span><span class="topo-inside">LIQNQDEMLKQGTLDRKYAG</span><span class="topo-unknown">ILDCFKRTATQE</span><span class="topo-inside">GVISF</span><span class="topo-membrane">WRGNTANVIRYFPTQAL</span><span class="topo-unknown">NFAFKDKIKAMF</span><span class="topo-outside">GFKKE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">EGYAKWFAGNLASG</span><span class="topo-membrane">GAAGALSLLFVYSLDYART</span><span class="topo-inside">RLAADS</span><span class="topo-unknown">KSSKKGGA</span><span class="topo-inside">RQFNG</span><span class="topo-unknown">LIDVYKKTLKS</span><span class="topo-inside">DG</span><span class="topo-membrane">VAGLYRGFLPSVVGIVVYRGLYFGMY</span><span class="topo-outside">DSL</span><span class="topo-unknown">KPLLLTGSLEGSF</span><span class="topo-outside">LASF</span><span class="topo-membrane">LLGWVVTTG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310        </span>
<span class="topo-line"><span class="topo-membrane">ASTCSYPLDTVRR</span><span class="topo-inside">RMMMTSGQAVKYDGAFDCLRKIVAAEGVGSLFKG</span><span class="topo-membrane">CGANILRGVAGAGVISMY</span><span class="topo-outside">DQLQ</span><span class="topo-unknown">MILFGKKFK</span></span>
<details class="topo-details"><summary>Topology coordinates (24 regions)</summary>
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
      <td>1</td>
      <td>23</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>24</td>
      <td>30</td>
      <td>24</td>
      <td>30</td>
      <td>Outside</td>
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
      <td>69</td>
      <td>50</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>81</td>
      <td>70</td>
      <td>81</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>86</td>
      <td>82</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>103</td>
      <td>87</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>104</td>
      <td>115</td>
      <td>104</td>
      <td>115</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>116</td>
      <td>134</td>
      <td>116</td>
      <td>134</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>135</td>
      <td>153</td>
      <td>135</td>
      <td>153</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>154</td>
      <td>159</td>
      <td>154</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>167</td>
      <td>160</td>
      <td>167</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>168</td>
      <td>172</td>
      <td>168</td>
      <td>172</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>183</td>
      <td>173</td>
      <td>183</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>184</td>
      <td>185</td>
      <td>184</td>
      <td>185</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>186</td>
      <td>211</td>
      <td>186</td>
      <td>211</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>212</td>
      <td>214</td>
      <td>212</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>227</td>
      <td>215</td>
      <td>227</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>228</td>
      <td>231</td>
      <td>228</td>
      <td>231</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>232</td>
      <td>253</td>
      <td>232</td>
      <td>253</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>254</td>
      <td>287</td>
      <td>254</td>
      <td>287</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>305</td>
      <td>288</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>309</td>
      <td>306</td>
      <td>309</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>318</td>
      <td>310</td>
      <td>318</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4c9g">4C9G</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSSNAQVKTPLPPAPAPKKESNF</span><span class="topo-outside">LIDFLMG</span><span class="topo-membrane">GVSAAVAKTAASPIERVKL</span><span class="topo-inside">LIQNQDEMLKQGTLDRKYAG</span><span class="topo-unknown">ILDCFKRTATQE</span><span class="topo-inside">GVISF</span><span class="topo-membrane">WRGNTANVIRYFPTQAL</span><span class="topo-unknown">NFAFKDKIKAMF</span><span class="topo-outside">GFKKE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">EGYAKWFAGNLASG</span><span class="topo-membrane">GAAGALSLLFVYSLDYART</span><span class="topo-inside">RLAADS</span><span class="topo-unknown">KSSKKGGA</span><span class="topo-inside">RQFNG</span><span class="topo-unknown">LIDVYKKTLKS</span><span class="topo-inside">DG</span><span class="topo-membrane">VAGLYRGFLPSVVGIVVYRGLYFGMY</span><span class="topo-outside">DSL</span><span class="topo-unknown">KPLLLTGSLEGSF</span><span class="topo-outside">LASF</span><span class="topo-membrane">LLGWVVTTG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310        </span>
<span class="topo-line"><span class="topo-membrane">ASTCSYPLDTVRR</span><span class="topo-inside">RMMMTSGQAVKYDGAFDCLRKIVAAEGVGSLFKG</span><span class="topo-membrane">CGANILRGVAGAGVISMY</span><span class="topo-outside">DQLQ</span><span class="topo-unknown">MILFGKKFK</span></span>
<details class="topo-details"><summary>Topology coordinates (24 regions)</summary>
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
      <td>1</td>
      <td>23</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>24</td>
      <td>30</td>
      <td>24</td>
      <td>30</td>
      <td>Outside</td>
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
      <td>69</td>
      <td>50</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>81</td>
      <td>70</td>
      <td>81</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>86</td>
      <td>82</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>103</td>
      <td>87</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>104</td>
      <td>115</td>
      <td>104</td>
      <td>115</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>116</td>
      <td>134</td>
      <td>116</td>
      <td>134</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>135</td>
      <td>153</td>
      <td>135</td>
      <td>153</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>154</td>
      <td>159</td>
      <td>154</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>167</td>
      <td>160</td>
      <td>167</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>168</td>
      <td>172</td>
      <td>168</td>
      <td>172</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>183</td>
      <td>173</td>
      <td>183</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>184</td>
      <td>185</td>
      <td>184</td>
      <td>185</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>186</td>
      <td>211</td>
      <td>186</td>
      <td>211</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>212</td>
      <td>214</td>
      <td>212</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>227</td>
      <td>215</td>
      <td>227</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>228</td>
      <td>231</td>
      <td>228</td>
      <td>231</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>232</td>
      <td>253</td>
      <td>232</td>
      <td>253</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>254</td>
      <td>287</td>
      <td>254</td>
      <td>287</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>305</td>
      <td>288</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>309</td>
      <td>306</td>
      <td>309</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>318</td>
      <td>310</td>
      <td>318</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4c9g">4C9G</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSSNAQVKTPLPPAPAPKKESNF</span><span class="topo-outside">LIDFLMG</span><span class="topo-membrane">GVSAAVAKTAASPIERVKL</span><span class="topo-inside">LIQNQDEMLKQGTLDRKYAG</span><span class="topo-unknown">ILDCFKRTATQE</span><span class="topo-inside">GVISF</span><span class="topo-membrane">WRGNTANVIRYFPTQAL</span><span class="topo-unknown">NFAFKDKIKAMF</span><span class="topo-outside">GFKKE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">EGYAKWFAGNLASG</span><span class="topo-membrane">GAAGALSLLFVYSLDYART</span><span class="topo-inside">RLAADS</span><span class="topo-unknown">KSSKKGGA</span><span class="topo-inside">RQFNG</span><span class="topo-unknown">LIDVYKKTLKS</span><span class="topo-inside">DG</span><span class="topo-membrane">VAGLYRGFLPSVVGIVVYRGLYFGMY</span><span class="topo-outside">DSL</span><span class="topo-unknown">KPLLLTGSLEGSF</span><span class="topo-outside">LASF</span><span class="topo-membrane">LLGWVVTTG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310        </span>
<span class="topo-line"><span class="topo-membrane">ASTCSYPLDTVRR</span><span class="topo-inside">RMMMTSGQAVKYDGAFDCLRKIVAAEGVGSLFKG</span><span class="topo-membrane">CGANILRGVAGAGVISMY</span><span class="topo-outside">DQLQ</span><span class="topo-unknown">MILFGKKFK</span></span>
<details class="topo-details"><summary>Topology coordinates (24 regions)</summary>
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
      <td>1</td>
      <td>23</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>24</td>
      <td>30</td>
      <td>24</td>
      <td>30</td>
      <td>Outside</td>
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
      <td>69</td>
      <td>50</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>81</td>
      <td>70</td>
      <td>81</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>86</td>
      <td>82</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>103</td>
      <td>87</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>104</td>
      <td>115</td>
      <td>104</td>
      <td>115</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>116</td>
      <td>134</td>
      <td>116</td>
      <td>134</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>135</td>
      <td>153</td>
      <td>135</td>
      <td>153</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>154</td>
      <td>159</td>
      <td>154</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>167</td>
      <td>160</td>
      <td>167</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>168</td>
      <td>172</td>
      <td>168</td>
      <td>172</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>183</td>
      <td>173</td>
      <td>183</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>184</td>
      <td>185</td>
      <td>184</td>
      <td>185</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>186</td>
      <td>211</td>
      <td>186</td>
      <td>211</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>212</td>
      <td>214</td>
      <td>212</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>227</td>
      <td>215</td>
      <td>227</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>228</td>
      <td>231</td>
      <td>228</td>
      <td>231</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>232</td>
      <td>253</td>
      <td>232</td>
      <td>253</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>254</td>
      <td>287</td>
      <td>254</td>
      <td>287</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>305</td>
      <td>288</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>309</td>
      <td>306</td>
      <td>309</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>318</td>
      <td>310</td>
      <td>318</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4c9g">4C9G</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSSNAQVKTPLPPAPAPKKESNF</span><span class="topo-outside">LIDFLMG</span><span class="topo-membrane">GVSAAVAKTAASPIERVKL</span><span class="topo-inside">LIQNQDEMLKQGTLDRKYAG</span><span class="topo-unknown">ILDCFKRTATQE</span><span class="topo-inside">GVISF</span><span class="topo-membrane">WRGNTANVIRYFPTQAL</span><span class="topo-unknown">NFAFKDKIKAMF</span><span class="topo-outside">GFKKE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">EGYAKWFAGNLASG</span><span class="topo-membrane">GAAGALSLLFVYSLDYART</span><span class="topo-inside">RLAADS</span><span class="topo-unknown">KSSKKGGA</span><span class="topo-inside">RQFNG</span><span class="topo-unknown">LIDVYKKTLKS</span><span class="topo-inside">DG</span><span class="topo-membrane">VAGLYRGFLPSVVGIVVYRGLYFGMY</span><span class="topo-outside">DSL</span><span class="topo-unknown">KPLLLTGSLEGSF</span><span class="topo-outside">LASF</span><span class="topo-membrane">LLGWVVTTG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310        </span>
<span class="topo-line"><span class="topo-membrane">ASTCSYPLDTVRR</span><span class="topo-inside">RMMMTSGQAVKYDGAFDCLRKIVAAEGVGSLFKG</span><span class="topo-membrane">CGANILRGVAGAGVISMY</span><span class="topo-outside">DQLQ</span><span class="topo-unknown">MILFGKKFK</span></span>
<details class="topo-details"><summary>Topology coordinates (24 regions)</summary>
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
      <td>1</td>
      <td>23</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>24</td>
      <td>30</td>
      <td>24</td>
      <td>30</td>
      <td>Outside</td>
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
      <td>69</td>
      <td>50</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>81</td>
      <td>70</td>
      <td>81</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>86</td>
      <td>82</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>103</td>
      <td>87</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>104</td>
      <td>115</td>
      <td>104</td>
      <td>115</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>116</td>
      <td>134</td>
      <td>116</td>
      <td>134</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>135</td>
      <td>153</td>
      <td>135</td>
      <td>153</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>154</td>
      <td>159</td>
      <td>154</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>167</td>
      <td>160</td>
      <td>167</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>168</td>
      <td>172</td>
      <td>168</td>
      <td>172</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>183</td>
      <td>173</td>
      <td>183</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>184</td>
      <td>185</td>
      <td>184</td>
      <td>185</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>186</td>
      <td>211</td>
      <td>186</td>
      <td>211</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>212</td>
      <td>214</td>
      <td>212</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>227</td>
      <td>215</td>
      <td>227</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>228</td>
      <td>231</td>
      <td>228</td>
      <td>231</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>232</td>
      <td>253</td>
      <td>232</td>
      <td>253</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>254</td>
      <td>287</td>
      <td>254</td>
      <td>287</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>305</td>
      <td>288</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>309</td>
      <td>306</td>
      <td>309</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>318</td>
      <td>310</td>
      <td>318</td>
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

### Domain-based alternating-access mechanism

The structures support a domain-based alternating-access transport
mechanism for mitochondrial carriers. The three homologous sequence
repeats fold into three structural domains, each comprising two
transmembrane helices and a matrix helix. The odd-numbered α-helices
(H1, H3, H5) contain kinks at proline or serine residues, functioning
as lever arms that couple substrate-induced disruption of the matrix
salt-bridge network to formation of the cytoplasmic salt-bridge network.
The simultaneous movement of three domains around a central translocation
pathway is unique among transport proteins.

### Matrix salt-bridge network and glutamine brace

The matrix side of the cavity is closed by a salt-bridge network formed
by charged residues of the Px[DE]xx[KR] signature motifs. A conserved
glutamine residue braces the salt bridge between domains 1 and 3,
forming hydrogen bonds with both charged residues. This glutamine brace
contributes to an energy barrier that must be overcome by substrate
binding, enforcing a strict equimolar exchange. Yeast ADP/ATP carriers
have one brace, while carriers such as the [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) carrier Ctp1 may
have two or three.

### Cytoplasmic salt-bridge network forms during transport

Experimental evidence demonstrates that a conserved YFxx[KR] motif on
the cytoplasmic side forms a salt-bridge network when the carrier is
in the m-state. Mutagenesis with charge-reversed networks showed that
mutants with all positively or all negatively charged cytoplasmic
networks were inactive, but when the network residues were interchanged
(six mutations), transport activity was restored to ~14% of wild-type.
The restored activity remained sensitive to CATR and [Bongkrekic Acid](/xray-mp-wiki/reagents/ligands/bongkrekic-acid/),
confirming specific transport.

### Cardiolipin binding and structural role

Three [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) molecules bind in pockets between the matrix helices
and the matrix end of the even-numbered transmembrane helices. The
[Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) phosphate groups are positioned near the N-terminal ends of
helices, interacting with helix dipoles and forming hydrogen bonds to
exposed amide groups. Conserved [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) residues (including those in
YWFG and [YF]xG motifs) are key to forming the binding sites.
[Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) may act as 'grease' at a dynamic interface, protecting
mobile regions and allowing close packing.

### Serine kink in H3 mimics proline

In over 40% of ADP/ATP carrier sequences, the conserved proline on H3
is substituted by serine (Ser147 in Aac2p). The serine side-chain makes
an unusual hydrogen bond to its own backbone amide group, mimicking the
structure of proline and maintaining the ~50° kink angle. This rare
arrangement is stabilized by a network of side-chain interactions,
including a hydrogen bond to Tyr177 on matrix helix h34.

### C-terminal region folds into the cavity

The yeast ADP/ATP carrier structures reveal the complete C-terminal
region, which is missing from bovine AAC1 structures. H6 adopts a sharp
turn at Gly314 and folds back into the central cavity, where Phe317
forms hydrophobic contacts with Met29 and an anion-π interaction with
Asp26. This C-terminal region may form an additional component of the
cytoplasmic gate.


## Cross-References

- <a href="/xray-mp-wiki/proteins/slc-transporters/bovine-adp-atp-carrier/">Bovine ADP/ATP Carrier (AAC1)</a> — Orthologous carrier; used as molecular replacement search model; structural comparison
- <a href="/xray-mp-wiki/proteins/slc-transporters/thermothelomyces-thermophila-adp-atp-carrier/">Thermothelomyces thermophila ADP/ATP Carrier</a> — Related fungal ADP/ATP carrier for structural comparison
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — Yeast ADP/ATP carriers provide structural basis for domain-based alternating-access transport
- <a href="/xray-mp-wiki/reagents/lipids/cardiolipin/">Cardiolipin</a> — Three cardiolipin molecules tightly bound at interdomain interfaces
- <a href="/xray-mp-wiki/reagents/ligands/bongkrekic-acid/">Bongkrekic Acid</a> — Specific inhibitor that locks the carrier in the matrix state (m-state)
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/">ABC Transporter Family</a> — ADP/ATP carriers and ABC transporters both exemplify alternating-access transport mechanisms
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> — Buffer component in purification or crystallization
- <a href="/xray-mp-wiki/reagents/buffers/glycine/">Glycine</a> — Buffer component in purification or crystallization
- <a href="/xray-mp-wiki/reagents/detergents/dm/">n-Decyl-β-D-maltoside</a> — Detergent used in purification or crystallization
