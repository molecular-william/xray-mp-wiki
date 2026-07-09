---
title: "Human TREK-2 Potassium Channel (KCNK10)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1261512, doi/10.1038##s41467-024-48536-2]
verified: regex
uniprot_id: P57789
---

# Human TREK-2 Potassium Channel (KCNK10)


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P57789">UniProt: P57789</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

TREK-2 (KCNK10) is a member of the Two-Pore Domain (K2P) potassium
channel subfamily that plays crucial roles in controlling the electrical
activity of many different cell types. TREK-2 is regulated by a wide
variety of physical and chemical stimuli and is expressed within the
central and peripheral nervous systems, with involvement in pain
perception, neuroprotection, and anaesthesia. Like other K2P channels,
each gene encodes a subunit with two pore-forming domains that dimerise
to create a single pseudo tetrameric K+-selective channel. The channel
features a large extracellular Cap domain that is a defining feature of
K2P channels and is gated primarily by structural changes in the
selectivity filter region. TREK-2 gating involves two major
conformations: an up state (conductive) and a down state
(non-conductive), with coordinated movement of transmembrane helices
M2, M3, and M4. The down state features intramembrane-side fenestrations
that serve as binding sites for state-dependent inhibitors including
[Fluoxetine](/xray-mp-wiki/reagents/ligands/fluoxetine/) and [Norfluoxetine](/xray-mp-wiki/reagents/additives/norfluoxetine/).


## Publications

### doi/10.1126##science.1261512

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4bw5">4BW5</a></td>
      <td>3.4</td>
      <td>Not specified</td>
      <td>Human TREK-2 up state</td>
      <td>K⁺ (four ions in filter, conductive state)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4bw5">4BW5</a></td>
      <td>3.9</td>
      <td>Not specified</td>
      <td>Human TREK-2 down state</td>
      <td>K⁺ (three ions in filter, non-conductive state), lipid-like molecules in fenestration</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4bw5">4BW5</a></td>
      <td>3.7</td>
      <td>Not specified</td>
      <td>Human TREK-2 in complex with <a href="/xray-mp-wiki/reagents/additives/norfluoxetine/">Norfluoxetine</a> (down state)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/norfluoxetine/">Norfluoxetine</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4bw5">4BW5</a></td>
      <td>3.64</td>
      <td>Not specified</td>
      <td>Human TREK-2 in complex with Br-<a href="/xray-mp-wiki/reagents/ligands/fluoxetine/">Fluoxetine</a> (down state)</td>
      <td>Br-<a href="/xray-mp-wiki/reagents/ligands/fluoxetine/">Fluoxetine</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Not detailed in source texts
- **Construct**: Human TREK-2 (KCNK10) with various truncations and modifications
- **Notes**: For [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) structures (doi/10.1038##s41467-024-48536-2), construct was residues Gly67 to Glu340. A glycosylation mutant (N149Q, N152Q, N153Q) was used for some complexes. For the gating structures (doi/10.1126##science.1261512), full functional channel was used.

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified TREK-2</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Structures solved at 3.4 Å (up state), 3.9 Å (down state), 3.7 Å (<a href="/xray-mp-wiki/reagents/additives/norfluoxetine/">Norfluoxetine</a> complex), and 3.64 Å (Br-<a href="/xray-mp-wiki/reagents/ligands/fluoxetine/">Fluoxetine</a> complex). Four chains in asymmetric unit. Up state has kinked M4 at Gly312 hinge. Down state similar to <a href="/xray-mp-wiki/proteins/voltage-gated-channels/traak/">TRAAK</a> and TWIK-1 structures.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4bw5">4BW5</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGLQTVM</span><span class="topo-inside">KWKTV</span><span class="topo-membrane">VAIFVVVVVYLVTGGLVFRAL</span><span class="topo-outside">EQPFESSQKNTIALEKAEFLRDHVCVSPQELETLIQHALDADNAGVSPIG</span><span class="topo-unknown">NSSN</span><span class="topo-outside">NSSHWDL</span><span class="topo-unknown">GSAFFFAGTVITTIGYG</span><span class="topo-outside">NIAPSTE</span><span class="topo-membrane">GG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KIFCILYAIFGIPLFGFLLAGIG</span><span class="topo-unknown">DQLGTIFGKSIARVEKVFR</span><span class="topo-inside">K</span><span class="topo-unknown">KQVSQTK</span><span class="topo-inside">IRVIST</span><span class="topo-membrane">ILFILAGCIVFVTIPAVIFK</span><span class="topo-outside">YIEGWTA</span><span class="topo-unknown">LESIYFVVVTLTTVGFG</span><span class="topo-outside">DFVAGGNAGINYRE</span><span class="topo-membrane">WYKPLV</span></span>
<span class="topo-ruler">       250       260       270       280  </span>
<span class="topo-line"><span class="topo-membrane">WFWILVGLAYFAAVLSMIG</span><span class="topo-inside">DWLRVLS</span><span class="topo-unknown">KKTKEEVGEAENLYFQ</span></span>
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
      <td>7</td>
      <td>66</td>
      <td>72</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>12</td>
      <td>73</td>
      <td>77</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>33</td>
      <td>78</td>
      <td>98</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>83</td>
      <td>99</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>87</td>
      <td>149</td>
      <td>152</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>88</td>
      <td>94</td>
      <td>153</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>111</td>
      <td>160</td>
      <td>176</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>112</td>
      <td>118</td>
      <td>177</td>
      <td>183</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>143</td>
      <td>184</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>144</td>
      <td>162</td>
      <td>209</td>
      <td>227</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>163</td>
      <td>163</td>
      <td>228</td>
      <td>228</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>170</td>
      <td>229</td>
      <td>235</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>171</td>
      <td>176</td>
      <td>236</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>196</td>
      <td>242</td>
      <td>261</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>203</td>
      <td>262</td>
      <td>268</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>220</td>
      <td>269</td>
      <td>285</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>221</td>
      <td>234</td>
      <td>286</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>235</td>
      <td>259</td>
      <td>300</td>
      <td>324</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>260</td>
      <td>266</td>
      <td>325</td>
      <td>331</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>267</td>
      <td>282</td>
      <td>332</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4bw5">4BW5</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGLQTVM</span><span class="topo-inside">KWKTV</span><span class="topo-membrane">VAIFVVVVVYLVTGGLVFRAL</span><span class="topo-outside">EQPFESSQKNTIALEKAEFLRDHVCVSPQELETLIQHALDADNAGVSPIG</span><span class="topo-unknown">NSSNNS</span><span class="topo-outside">SHWDL</span><span class="topo-unknown">GSAFFFAGTVITTIGYG</span><span class="topo-outside">NIAPSTEG</span><span class="topo-membrane">G</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KIFCILYAIFGIPLFGFLLAGIG</span><span class="topo-unknown">DQLGTIFGKSIARVEKVFRK</span><span class="topo-inside">KQVSQTKIRVISTI</span><span class="topo-membrane">LFILAGCIVFVTIPAVIFKYI</span><span class="topo-outside">EGWTA</span><span class="topo-unknown">LESIYFVVVTLTTVGFG</span><span class="topo-outside">DFVAGGNAGINYR</span><span class="topo-membrane">EWYKPLV</span></span>
<span class="topo-ruler">       250       260       270       280  </span>
<span class="topo-line"><span class="topo-membrane">WFWILVGLAYFAAVLSMIG</span><span class="topo-unknown">DWLRVLS</span><span class="topo-inside">K</span><span class="topo-unknown">KTKEEVGEAENLYFQ</span></span>
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
      <td>7</td>
      <td>66</td>
      <td>72</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>12</td>
      <td>73</td>
      <td>77</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>33</td>
      <td>78</td>
      <td>98</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>83</td>
      <td>99</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>89</td>
      <td>149</td>
      <td>154</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>90</td>
      <td>94</td>
      <td>155</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>111</td>
      <td>160</td>
      <td>176</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>112</td>
      <td>119</td>
      <td>177</td>
      <td>184</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>120</td>
      <td>143</td>
      <td>185</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>144</td>
      <td>163</td>
      <td>209</td>
      <td>228</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>164</td>
      <td>177</td>
      <td>229</td>
      <td>242</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>198</td>
      <td>243</td>
      <td>263</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>203</td>
      <td>264</td>
      <td>268</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>220</td>
      <td>269</td>
      <td>285</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>221</td>
      <td>233</td>
      <td>286</td>
      <td>298</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>259</td>
      <td>299</td>
      <td>324</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>260</td>
      <td>266</td>
      <td>325</td>
      <td>331</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>267</td>
      <td>267</td>
      <td>332</td>
      <td>332</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>268</td>
      <td>282</td>
      <td>333</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4bw5">4BW5</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGLQTVM</span><span class="topo-inside">KWKTV</span><span class="topo-membrane">VAIFVVVVVYLVTGGLVFRAL</span><span class="topo-outside">EQPFESSQKNTIALEKAEFLRDHVCVSPQELETLIQHALDADNAGVSPIG</span><span class="topo-unknown">NSSN</span><span class="topo-outside">NSSHWDL</span><span class="topo-unknown">GSAFFFAGTVITTIGYG</span><span class="topo-outside">NIAPSTE</span><span class="topo-membrane">GG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KIFCILYAIFGIPLFGFLLAGIG</span><span class="topo-unknown">DQLGTIFGKSIARVEKVFR</span><span class="topo-inside">K</span><span class="topo-unknown">KQVSQTK</span><span class="topo-inside">IRVIST</span><span class="topo-membrane">ILFILAGCIVFVTIPAVIFK</span><span class="topo-outside">YIEGWTA</span><span class="topo-unknown">LESIYFVVVTLTTVGFG</span><span class="topo-outside">DFVAGGNAGINYRE</span><span class="topo-membrane">WYKPLV</span></span>
<span class="topo-ruler">       250       260       270       280  </span>
<span class="topo-line"><span class="topo-membrane">WFWILVGLAYFAAVLSMIG</span><span class="topo-inside">DWLRVLS</span><span class="topo-unknown">KKTKEEVGEAENLYFQ</span></span>
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
      <td>7</td>
      <td>66</td>
      <td>72</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>12</td>
      <td>73</td>
      <td>77</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>33</td>
      <td>78</td>
      <td>98</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>83</td>
      <td>99</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>87</td>
      <td>149</td>
      <td>152</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>88</td>
      <td>94</td>
      <td>153</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>111</td>
      <td>160</td>
      <td>176</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>112</td>
      <td>118</td>
      <td>177</td>
      <td>183</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>143</td>
      <td>184</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>144</td>
      <td>162</td>
      <td>209</td>
      <td>227</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>163</td>
      <td>163</td>
      <td>228</td>
      <td>228</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>170</td>
      <td>229</td>
      <td>235</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>171</td>
      <td>176</td>
      <td>236</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>196</td>
      <td>242</td>
      <td>261</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>203</td>
      <td>262</td>
      <td>268</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>220</td>
      <td>269</td>
      <td>285</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>221</td>
      <td>234</td>
      <td>286</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>235</td>
      <td>259</td>
      <td>300</td>
      <td>324</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>260</td>
      <td>266</td>
      <td>325</td>
      <td>331</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>267</td>
      <td>282</td>
      <td>332</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4bw5">4BW5</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGLQTVM</span><span class="topo-inside">KWKTV</span><span class="topo-membrane">VAIFVVVVVYLVTGGLVFRAL</span><span class="topo-outside">EQPFESSQKNTIALEKAEFLRDHVCVSPQELETLIQHALDADNAGVSPIG</span><span class="topo-unknown">NSSNNS</span><span class="topo-outside">SHWDL</span><span class="topo-unknown">GSAFFFAGTVITTIGYG</span><span class="topo-outside">NIAPSTEG</span><span class="topo-membrane">G</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KIFCILYAIFGIPLFGFLLAGIG</span><span class="topo-unknown">DQLGTIFGKSIARVEKVFRK</span><span class="topo-inside">KQVSQTKIRVISTI</span><span class="topo-membrane">LFILAGCIVFVTIPAVIFKYI</span><span class="topo-outside">EGWTA</span><span class="topo-unknown">LESIYFVVVTLTTVGFG</span><span class="topo-outside">DFVAGGNAGINYR</span><span class="topo-membrane">EWYKPLV</span></span>
<span class="topo-ruler">       250       260       270       280  </span>
<span class="topo-line"><span class="topo-membrane">WFWILVGLAYFAAVLSMIG</span><span class="topo-unknown">DWLRVLS</span><span class="topo-inside">K</span><span class="topo-unknown">KTKEEVGEAENLYFQ</span></span>
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
      <td>7</td>
      <td>66</td>
      <td>72</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>12</td>
      <td>73</td>
      <td>77</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>33</td>
      <td>78</td>
      <td>98</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>83</td>
      <td>99</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>89</td>
      <td>149</td>
      <td>154</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>90</td>
      <td>94</td>
      <td>155</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>111</td>
      <td>160</td>
      <td>176</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>112</td>
      <td>119</td>
      <td>177</td>
      <td>184</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>120</td>
      <td>143</td>
      <td>185</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>144</td>
      <td>163</td>
      <td>209</td>
      <td>228</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>164</td>
      <td>177</td>
      <td>229</td>
      <td>242</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>198</td>
      <td>243</td>
      <td>263</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>203</td>
      <td>264</td>
      <td>268</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>220</td>
      <td>269</td>
      <td>285</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>221</td>
      <td>233</td>
      <td>286</td>
      <td>298</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>259</td>
      <td>299</td>
      <td>324</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>260</td>
      <td>266</td>
      <td>325</td>
      <td>331</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>267</td>
      <td>267</td>
      <td>332</td>
      <td>332</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>268</td>
      <td>282</td>
      <td>333</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4bw5">4BW5</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGLQTVM</span><span class="topo-inside">KWKTV</span><span class="topo-membrane">VAIFVVVVVYLVTGGLVFRAL</span><span class="topo-outside">EQPFESSQKNTIALEKAEFLRDHVCVSPQELETLIQHALDADNAGVSPIG</span><span class="topo-unknown">NSSN</span><span class="topo-outside">NSSHWDL</span><span class="topo-unknown">GSAFFFAGTVITTIGYG</span><span class="topo-outside">NIAPSTE</span><span class="topo-membrane">GG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KIFCILYAIFGIPLFGFLLAGIG</span><span class="topo-unknown">DQLGTIFGKSIARVEKVFR</span><span class="topo-inside">K</span><span class="topo-unknown">KQVSQTK</span><span class="topo-inside">IRVIST</span><span class="topo-membrane">ILFILAGCIVFVTIPAVIFK</span><span class="topo-outside">YIEGWTA</span><span class="topo-unknown">LESIYFVVVTLTTVGFG</span><span class="topo-outside">DFVAGGNAGINYRE</span><span class="topo-membrane">WYKPLV</span></span>
<span class="topo-ruler">       250       260       270       280  </span>
<span class="topo-line"><span class="topo-membrane">WFWILVGLAYFAAVLSMIG</span><span class="topo-inside">DWLRVLS</span><span class="topo-unknown">KKTKEEVGEAENLYFQ</span></span>
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
      <td>7</td>
      <td>66</td>
      <td>72</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>12</td>
      <td>73</td>
      <td>77</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>33</td>
      <td>78</td>
      <td>98</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>83</td>
      <td>99</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>87</td>
      <td>149</td>
      <td>152</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>88</td>
      <td>94</td>
      <td>153</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>111</td>
      <td>160</td>
      <td>176</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>112</td>
      <td>118</td>
      <td>177</td>
      <td>183</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>143</td>
      <td>184</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>144</td>
      <td>162</td>
      <td>209</td>
      <td>227</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>163</td>
      <td>163</td>
      <td>228</td>
      <td>228</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>170</td>
      <td>229</td>
      <td>235</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>171</td>
      <td>176</td>
      <td>236</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>196</td>
      <td>242</td>
      <td>261</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>203</td>
      <td>262</td>
      <td>268</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>220</td>
      <td>269</td>
      <td>285</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>221</td>
      <td>234</td>
      <td>286</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>235</td>
      <td>259</td>
      <td>300</td>
      <td>324</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>260</td>
      <td>266</td>
      <td>325</td>
      <td>331</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>267</td>
      <td>282</td>
      <td>332</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4bw5">4BW5</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGLQTVM</span><span class="topo-inside">KWKTV</span><span class="topo-membrane">VAIFVVVVVYLVTGGLVFRAL</span><span class="topo-outside">EQPFESSQKNTIALEKAEFLRDHVCVSPQELETLIQHALDADNAGVSPIG</span><span class="topo-unknown">NSSNNS</span><span class="topo-outside">SHWDL</span><span class="topo-unknown">GSAFFFAGTVITTIGYG</span><span class="topo-outside">NIAPSTEG</span><span class="topo-membrane">G</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KIFCILYAIFGIPLFGFLLAGIG</span><span class="topo-unknown">DQLGTIFGKSIARVEKVFRK</span><span class="topo-inside">KQVSQTKIRVISTI</span><span class="topo-membrane">LFILAGCIVFVTIPAVIFKYI</span><span class="topo-outside">EGWTA</span><span class="topo-unknown">LESIYFVVVTLTTVGFG</span><span class="topo-outside">DFVAGGNAGINYR</span><span class="topo-membrane">EWYKPLV</span></span>
<span class="topo-ruler">       250       260       270       280  </span>
<span class="topo-line"><span class="topo-membrane">WFWILVGLAYFAAVLSMIG</span><span class="topo-unknown">DWLRVLS</span><span class="topo-inside">K</span><span class="topo-unknown">KTKEEVGEAENLYFQ</span></span>
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
      <td>7</td>
      <td>66</td>
      <td>72</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>12</td>
      <td>73</td>
      <td>77</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>33</td>
      <td>78</td>
      <td>98</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>83</td>
      <td>99</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>89</td>
      <td>149</td>
      <td>154</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>90</td>
      <td>94</td>
      <td>155</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>111</td>
      <td>160</td>
      <td>176</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>112</td>
      <td>119</td>
      <td>177</td>
      <td>184</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>120</td>
      <td>143</td>
      <td>185</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>144</td>
      <td>163</td>
      <td>209</td>
      <td>228</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>164</td>
      <td>177</td>
      <td>229</td>
      <td>242</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>198</td>
      <td>243</td>
      <td>263</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>203</td>
      <td>264</td>
      <td>268</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>220</td>
      <td>269</td>
      <td>285</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>221</td>
      <td>233</td>
      <td>286</td>
      <td>298</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>259</td>
      <td>299</td>
      <td>324</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>260</td>
      <td>266</td>
      <td>325</td>
      <td>331</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>267</td>
      <td>267</td>
      <td>332</td>
      <td>332</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>268</td>
      <td>282</td>
      <td>333</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4bw5">4BW5</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGLQTVM</span><span class="topo-inside">KWKTV</span><span class="topo-membrane">VAIFVVVVVYLVTGGLVFRAL</span><span class="topo-outside">EQPFESSQKNTIALEKAEFLRDHVCVSPQELETLIQHALDADNAGVSPIG</span><span class="topo-unknown">NSSN</span><span class="topo-outside">NSSHWDL</span><span class="topo-unknown">GSAFFFAGTVITTIGYG</span><span class="topo-outside">NIAPSTE</span><span class="topo-membrane">GG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KIFCILYAIFGIPLFGFLLAGIG</span><span class="topo-unknown">DQLGTIFGKSIARVEKVFR</span><span class="topo-inside">K</span><span class="topo-unknown">KQVSQTK</span><span class="topo-inside">IRVIST</span><span class="topo-membrane">ILFILAGCIVFVTIPAVIFK</span><span class="topo-outside">YIEGWTA</span><span class="topo-unknown">LESIYFVVVTLTTVGFG</span><span class="topo-outside">DFVAGGNAGINYRE</span><span class="topo-membrane">WYKPLV</span></span>
<span class="topo-ruler">       250       260       270       280  </span>
<span class="topo-line"><span class="topo-membrane">WFWILVGLAYFAAVLSMIG</span><span class="topo-inside">DWLRVLS</span><span class="topo-unknown">KKTKEEVGEAENLYFQ</span></span>
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
      <td>7</td>
      <td>66</td>
      <td>72</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>12</td>
      <td>73</td>
      <td>77</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>33</td>
      <td>78</td>
      <td>98</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>83</td>
      <td>99</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>87</td>
      <td>149</td>
      <td>152</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>88</td>
      <td>94</td>
      <td>153</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>111</td>
      <td>160</td>
      <td>176</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>112</td>
      <td>118</td>
      <td>177</td>
      <td>183</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>143</td>
      <td>184</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>144</td>
      <td>162</td>
      <td>209</td>
      <td>227</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>163</td>
      <td>163</td>
      <td>228</td>
      <td>228</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>170</td>
      <td>229</td>
      <td>235</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>171</td>
      <td>176</td>
      <td>236</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>196</td>
      <td>242</td>
      <td>261</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>203</td>
      <td>262</td>
      <td>268</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>220</td>
      <td>269</td>
      <td>285</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>221</td>
      <td>234</td>
      <td>286</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>235</td>
      <td>259</td>
      <td>300</td>
      <td>324</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>260</td>
      <td>266</td>
      <td>325</td>
      <td>331</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>267</td>
      <td>282</td>
      <td>332</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4bw5">4BW5</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGLQTVM</span><span class="topo-inside">KWKTV</span><span class="topo-membrane">VAIFVVVVVYLVTGGLVFRAL</span><span class="topo-outside">EQPFESSQKNTIALEKAEFLRDHVCVSPQELETLIQHALDADNAGVSPIG</span><span class="topo-unknown">NSSNNS</span><span class="topo-outside">SHWDL</span><span class="topo-unknown">GSAFFFAGTVITTIGYG</span><span class="topo-outside">NIAPSTEG</span><span class="topo-membrane">G</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KIFCILYAIFGIPLFGFLLAGIG</span><span class="topo-unknown">DQLGTIFGKSIARVEKVFRK</span><span class="topo-inside">KQVSQTKIRVISTI</span><span class="topo-membrane">LFILAGCIVFVTIPAVIFKYI</span><span class="topo-outside">EGWTA</span><span class="topo-unknown">LESIYFVVVTLTTVGFG</span><span class="topo-outside">DFVAGGNAGINYR</span><span class="topo-membrane">EWYKPLV</span></span>
<span class="topo-ruler">       250       260       270       280  </span>
<span class="topo-line"><span class="topo-membrane">WFWILVGLAYFAAVLSMIG</span><span class="topo-unknown">DWLRVLS</span><span class="topo-inside">K</span><span class="topo-unknown">KTKEEVGEAENLYFQ</span></span>
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
      <td>7</td>
      <td>66</td>
      <td>72</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>12</td>
      <td>73</td>
      <td>77</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>33</td>
      <td>78</td>
      <td>98</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>83</td>
      <td>99</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>89</td>
      <td>149</td>
      <td>154</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>90</td>
      <td>94</td>
      <td>155</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>111</td>
      <td>160</td>
      <td>176</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>112</td>
      <td>119</td>
      <td>177</td>
      <td>184</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>120</td>
      <td>143</td>
      <td>185</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>144</td>
      <td>163</td>
      <td>209</td>
      <td>228</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>164</td>
      <td>177</td>
      <td>229</td>
      <td>242</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>198</td>
      <td>243</td>
      <td>263</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>203</td>
      <td>264</td>
      <td>268</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>220</td>
      <td>269</td>
      <td>285</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>221</td>
      <td>233</td>
      <td>286</td>
      <td>298</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>259</td>
      <td>299</td>
      <td>324</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>260</td>
      <td>266</td>
      <td>325</td>
      <td>331</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>267</td>
      <td>267</td>
      <td>332</td>
      <td>332</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>268</td>
      <td>282</td>
      <td>333</td>
      <td>347</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##s41467-024-48536-2

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8qz1">8QZ1</a></td>
      <td>Not specified</td>
      <td>Not specified</td>
      <td>Human TREK-2 residues Gly67 to Glu340 in complex with Nb-Binder-58 (Nb58)</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> Nb58</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8qz2">8QZ2</a></td>
      <td>Not specified</td>
      <td>Not specified</td>
      <td>Human TREK-2 residues Gly67 to Glu340 in complex with Nb-Inhibitor-61 (Nb61)</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> Nb61</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8qz3">8QZ3</a></td>
      <td>Not specified</td>
      <td>Not specified</td>
      <td>Human TREK-2 residues Gly67 to Glu340 in complex with Nb-Activator-67 (Nb67)</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> Nb67</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8qz4">8QZ4</a></td>
      <td>Not specified</td>
      <td>Not specified</td>
      <td>Human TREK-2 residues Gly67 to Glu340 in complex with Nb-Activator-76 (Nb76)</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> Nb76</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Not detailed in source texts
- **Construct**: Human TREK-2 (KCNK10) with various truncations and modifications
- **Notes**: For [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) structures (doi/10.1038##s41467-024-48536-2), construct was residues Gly67 to Glu340. A glycosylation mutant (N149Q, N152Q, N153Q) was used for some complexes. For the gating structures (doi/10.1126##science.1261512), full functional channel was used.

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Human TREK-2 (Gly67-Glu340) mixed with <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> in 1:2 TREK-2:<a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> molar ratio</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified in detail</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals of TREK-2/nanobody complexes obtained by vapor diffusion. For Nb67 and Nb61, glycosylation mutant (N149Q, N152Q, N153Q) used. Crystals for Nb76 used crystallisation solution containing Ba²⁺.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8qz1">8QZ1</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGLQTVM</span><span class="topo-inside">KW</span><span class="topo-membrane">KTVVAIFVVVVVYLVTGGLVF</span><span class="topo-outside">RALEQPFESSQKNTIALEKAEFLRDHVCVSPQELETLIQHALDADNAGVSPIGN</span><span class="topo-unknown">SSNNS</span><span class="topo-outside">SHWDLGSA</span><span class="topo-unknown">FFFAGTVITTIGY</span><span class="topo-outside">GNIAPSTEGG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">K</span><span class="topo-membrane">IFCILYAIFGIPLFGFLLAGIG</span><span class="topo-inside">DQLGTIFGK</span><span class="topo-unknown">SIARVEKVFRKKQV</span><span class="topo-inside">SQTKIRVIST</span><span class="topo-membrane">ILFILAGCIVFVTIPAVIF</span><span class="topo-outside">KYIEGWTALES</span><span class="topo-unknown">IYFVVVTLTTVGF</span><span class="topo-outside">GDFVAGG</span><span class="topo-unknown">NAGIN</span><span class="topo-outside">YREW</span><span class="topo-membrane">YKPLV</span></span>
<span class="topo-ruler">       250       260       270       280  </span>
<span class="topo-line"><span class="topo-membrane">WFWILVGLAYFAAVLS</span><span class="topo-inside">MIGDWLRVLSKKTKEEV</span><span class="topo-unknown">GEAENLYFQ</span></span>
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
      <td>66</td>
      <td>72</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>9</td>
      <td>73</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>30</td>
      <td>75</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>84</td>
      <td>96</td>
      <td>149</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>89</td>
      <td>150</td>
      <td>154</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>90</td>
      <td>97</td>
      <td>155</td>
      <td>162</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>110</td>
      <td>163</td>
      <td>175</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>111</td>
      <td>121</td>
      <td>176</td>
      <td>186</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>143</td>
      <td>187</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>144</td>
      <td>152</td>
      <td>209</td>
      <td>217</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>166</td>
      <td>218</td>
      <td>231</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>167</td>
      <td>176</td>
      <td>232</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>195</td>
      <td>242</td>
      <td>260</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>206</td>
      <td>261</td>
      <td>271</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>219</td>
      <td>272</td>
      <td>284</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>220</td>
      <td>226</td>
      <td>285</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>227</td>
      <td>231</td>
      <td>292</td>
      <td>296</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>232</td>
      <td>235</td>
      <td>297</td>
      <td>300</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>256</td>
      <td>301</td>
      <td>321</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>257</td>
      <td>273</td>
      <td>322</td>
      <td>338</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>274</td>
      <td>282</td>
      <td>339</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8qz1">8QZ1</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGLQTVM</span><span class="topo-inside">KWK</span><span class="topo-membrane">TVVAIFVVVVVYLVTGGLVF</span><span class="topo-outside">RALEQPFESSQKNTIALEKAEFLRDHVCVSPQELETLIQHALDADNAGVSPIGNSS</span><span class="topo-unknown">NN</span><span class="topo-outside">SSHWDLGSA</span><span class="topo-unknown">FFFAGTVITTIGY</span><span class="topo-outside">GNIAPSTEGG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KIFCILYAIFGIPLFGFLLAGIGDQL</span><span class="topo-inside">GTIFGKSIAR</span><span class="topo-unknown">VEKVFRKKQVSQTKI</span><span class="topo-inside">RVIST</span><span class="topo-membrane">ILFILAGCIVFVTIPAVIF</span><span class="topo-outside">KYIEGWTALES</span><span class="topo-unknown">IYFVVVTLTTVGF</span><span class="topo-outside">GDFVAGGNA</span><span class="topo-unknown">GINY</span><span class="topo-outside">REW</span><span class="topo-membrane">YKPLV</span></span>
<span class="topo-ruler">       250       260       270       280  </span>
<span class="topo-line"><span class="topo-membrane">WFWILVGLAYFAAVLSMIG</span><span class="topo-inside">DWLRVL</span><span class="topo-unknown">SKKTKEEVGEAENLYFQ</span></span>
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
      <td>66</td>
      <td>72</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>10</td>
      <td>73</td>
      <td>75</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>30</td>
      <td>76</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>86</td>
      <td>96</td>
      <td>151</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>88</td>
      <td>152</td>
      <td>153</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>89</td>
      <td>97</td>
      <td>154</td>
      <td>162</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>110</td>
      <td>163</td>
      <td>175</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>111</td>
      <td>120</td>
      <td>176</td>
      <td>185</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>146</td>
      <td>186</td>
      <td>211</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>147</td>
      <td>156</td>
      <td>212</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>171</td>
      <td>222</td>
      <td>236</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>172</td>
      <td>176</td>
      <td>237</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>195</td>
      <td>242</td>
      <td>260</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>206</td>
      <td>261</td>
      <td>271</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>219</td>
      <td>272</td>
      <td>284</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>220</td>
      <td>228</td>
      <td>285</td>
      <td>293</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>232</td>
      <td>294</td>
      <td>297</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>233</td>
      <td>235</td>
      <td>298</td>
      <td>300</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>259</td>
      <td>301</td>
      <td>324</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>260</td>
      <td>265</td>
      <td>325</td>
      <td>330</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>266</td>
      <td>282</td>
      <td>331</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8qz2">8QZ2</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-membrane">KTVVAIFVVVVVYLVTGGLVF</span><span class="topo-inside">RALEQPFESSQKNTIALEKAEFLRDHVCVSPQELETLIQHALDADNAGVSPIGQSSQQSSHWDL</span><span class="topo-unknown">GSAFFFAGTVITTIGYG</span><span class="topo-inside">NIAPSTEG</span><span class="topo-membrane">GKIFCILYA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">IFGIPLFGFLLAGIG</span><span class="topo-outside">DQLGTIFGKSIARVEKV</span><span class="topo-unknown">FRKKQVSQTKI</span><span class="topo-outside">RVISTI</span><span class="topo-membrane">LFILAGCIVFVTIPAVIFKYI</span><span class="topo-inside">EGWTA</span><span class="topo-unknown">LESIYFVVVTLTTVGFG</span><span class="topo-inside">DFVAGGNAGINYR</span><span class="topo-membrane">EWYKPLVWFWILVGL</span></span>
<span class="topo-ruler">       250       260       270    </span>
<span class="topo-line"><span class="topo-membrane">AYFAAVLSMI</span><span class="topo-unknown">GDWLRVLSKKTKEEVGEAENLYFQ</span></span>
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
      <td>2</td>
      <td>22</td>
      <td>75</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>23</td>
      <td>86</td>
      <td>96</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>103</td>
      <td>160</td>
      <td>176</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>104</td>
      <td>111</td>
      <td>177</td>
      <td>184</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>135</td>
      <td>185</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>152</td>
      <td>209</td>
      <td>225</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>163</td>
      <td>226</td>
      <td>236</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>164</td>
      <td>169</td>
      <td>237</td>
      <td>242</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>190</td>
      <td>243</td>
      <td>263</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>195</td>
      <td>264</td>
      <td>268</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>212</td>
      <td>269</td>
      <td>285</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>213</td>
      <td>225</td>
      <td>286</td>
      <td>298</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>250</td>
      <td>299</td>
      <td>323</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>251</td>
      <td>274</td>
      <td>324</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8qz2">8QZ2</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">KTV</span><span class="topo-membrane">VAIFVVVVVYLVTGGLVFRA</span><span class="topo-inside">LEQPFESSQKNTIALEKAEFLRDHVCVSPQELETLIQHALDADNAGVSPIGQSSQQSSHWDL</span><span class="topo-unknown">GSAFFFAGTVITTIGYG</span><span class="topo-inside">NIAPSTEG</span><span class="topo-membrane">GKIFCILYA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">IFGIPLFGFLLAGIGDQL</span><span class="topo-outside">GTIFGKSIARVEKVF</span><span class="topo-unknown">RKKQ</span><span class="topo-outside">VSQTKIRVI</span><span class="topo-membrane">STILFILAGCIVFVTIPAVIF</span><span class="topo-inside">KYIEGWTA</span><span class="topo-unknown">LESIYFVVVTLTTVGFG</span><span class="topo-inside">DFVAGGNAGINYREW</span><span class="topo-membrane">YKPLVWFWILVGL</span></span>
<span class="topo-ruler">       250       260       270    </span>
<span class="topo-line"><span class="topo-membrane">AYFAAVLS</span><span class="topo-outside">MIG</span><span class="topo-unknown">DWLRVLSKKTKEEVGEAENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
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
      <td>4</td>
      <td>75</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>24</td>
      <td>78</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>86</td>
      <td>98</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>103</td>
      <td>160</td>
      <td>176</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>104</td>
      <td>111</td>
      <td>177</td>
      <td>184</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>138</td>
      <td>185</td>
      <td>211</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>153</td>
      <td>212</td>
      <td>226</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>157</td>
      <td>227</td>
      <td>230</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>158</td>
      <td>166</td>
      <td>231</td>
      <td>239</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>187</td>
      <td>240</td>
      <td>260</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>188</td>
      <td>195</td>
      <td>261</td>
      <td>268</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>212</td>
      <td>269</td>
      <td>285</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>213</td>
      <td>227</td>
      <td>286</td>
      <td>300</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>248</td>
      <td>301</td>
      <td>321</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>249</td>
      <td>251</td>
      <td>322</td>
      <td>324</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>274</td>
      <td>325</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8qz3">8QZ3</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MKTV</span><span class="topo-membrane">VAIFVVVVVYLVTGGLVF</span><span class="topo-inside">RALEQPFESSQKNTIALEKAEFLRDHVCVSPQELETLIQHALDADNAGVSPIGQSSQQSSHWDL</span><span class="topo-unknown">GSAFFFAGTVITTIGYG</span><span class="topo-inside">NIAPSTE</span><span class="topo-membrane">GGKIFCILYA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">IFGIPLFGFLLA</span><span class="topo-outside">GIGDQLGTIFGKSIARVEKVFRKKQVSQTKIRVISTI</span><span class="topo-membrane">LFILAGCIVFVTIPAVIFK</span><span class="topo-inside">YIEGWTA</span><span class="topo-unknown">LESIYFVVVTLTTVGFG</span><span class="topo-inside">DFVAGGNAGINYRE</span><span class="topo-membrane">WYKPLVWFWILVGL</span></span>
<span class="topo-ruler">       250       260       270    </span>
<span class="topo-line"><span class="topo-membrane">AYFAAVLSMIG</span><span class="topo-outside">DWLRVLSKK</span><span class="topo-unknown">TKEEVGEAENLYFQ</span></span>
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
      <td>4</td>
      <td>74</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>22</td>
      <td>78</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>23</td>
      <td>86</td>
      <td>96</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>103</td>
      <td>160</td>
      <td>176</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>104</td>
      <td>110</td>
      <td>177</td>
      <td>183</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>111</td>
      <td>132</td>
      <td>184</td>
      <td>205</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>133</td>
      <td>169</td>
      <td>206</td>
      <td>242</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>188</td>
      <td>243</td>
      <td>261</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>189</td>
      <td>195</td>
      <td>262</td>
      <td>268</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>212</td>
      <td>269</td>
      <td>285</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>213</td>
      <td>226</td>
      <td>286</td>
      <td>299</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>227</td>
      <td>251</td>
      <td>300</td>
      <td>324</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>252</td>
      <td>260</td>
      <td>325</td>
      <td>333</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>274</td>
      <td>334</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8qz3">8QZ3</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MKTVV</span><span class="topo-membrane">AIFVVVVVYLVTGGLVFRAL</span><span class="topo-inside">EQPFESSQKNTIALEKAEFLRDHVCVSPQELETLIQHALDADNAGVSPIGQSSQQSSHWDL</span><span class="topo-unknown">GSAFFFAGTVITTIGYG</span><span class="topo-inside">NIAPSTEG</span><span class="topo-membrane">GKIFCILYA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">IFGIPLFGFLLAGIG</span><span class="topo-outside">DQLGTIFGKSIARVEKVFRKKQVSQTKIRVISTILFI</span><span class="topo-membrane">LAGCIVFVTIPAVIFKY</span><span class="topo-inside">IEGWTA</span><span class="topo-unknown">LESIYFVVVTLTTVGFG</span><span class="topo-inside">DFVAGGNAGINYRE</span><span class="topo-membrane">WYKPLVWFWILVGL</span></span>
<span class="topo-ruler">       250       260       270    </span>
<span class="topo-line"><span class="topo-membrane">AYFAAVLS</span><span class="topo-outside">MIGDWLRVLSKKTKEEVG</span><span class="topo-unknown">EAENLYFQ</span></span>
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
      <td>74</td>
      <td>78</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>25</td>
      <td>79</td>
      <td>98</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>86</td>
      <td>99</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>103</td>
      <td>160</td>
      <td>176</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>104</td>
      <td>111</td>
      <td>177</td>
      <td>184</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>135</td>
      <td>185</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>172</td>
      <td>209</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>189</td>
      <td>246</td>
      <td>262</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>190</td>
      <td>195</td>
      <td>263</td>
      <td>268</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>212</td>
      <td>269</td>
      <td>285</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>213</td>
      <td>226</td>
      <td>286</td>
      <td>299</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>227</td>
      <td>248</td>
      <td>300</td>
      <td>321</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>249</td>
      <td>266</td>
      <td>322</td>
      <td>339</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>267</td>
      <td>274</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8qz4">8QZ4</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGLQT</span><span class="topo-outside">VMKWKTV</span><span class="topo-membrane">VAIFVVVVVYLVTGGLVFRAL</span><span class="topo-inside">EQPFESSQKNTIALEKAEFLRDHVCVSPQELETLIQHALDADNAGVSPIGN</span><span class="topo-unknown">SSNN</span><span class="topo-inside">SSHWDL</span><span class="topo-unknown">GSAFFFAGTVITTIGYG</span><span class="topo-inside">NIAPSTE</span><span class="topo-membrane">GG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KIFCILYAIFGIPLFGFLLAGIG</span><span class="topo-outside">DQLGTIFGKSIARVE</span><span class="topo-unknown">KVFRKKQVSQTKI</span><span class="topo-outside">RVISTI</span><span class="topo-membrane">LFILAGCIVFVTIPAVIFKY</span><span class="topo-inside">IEGWTA</span><span class="topo-unknown">LESIYFVVVTLTTVGFG</span><span class="topo-inside">DFVAGGNAGINYR</span><span class="topo-membrane">EWYKPLV</span></span>
<span class="topo-ruler">       250       260       270       280  </span>
<span class="topo-line"><span class="topo-membrane">WFWILVGLAYFAAVLSMIG</span><span class="topo-outside">DWLRVLSKKTKEE</span><span class="topo-unknown">VGEAENLYFQ</span></span>
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
      <td>5</td>
      <td>66</td>
      <td>70</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>12</td>
      <td>71</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>33</td>
      <td>78</td>
      <td>98</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>84</td>
      <td>99</td>
      <td>149</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>88</td>
      <td>150</td>
      <td>153</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>89</td>
      <td>94</td>
      <td>154</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>111</td>
      <td>160</td>
      <td>176</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>112</td>
      <td>118</td>
      <td>177</td>
      <td>183</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>143</td>
      <td>184</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>144</td>
      <td>158</td>
      <td>209</td>
      <td>223</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>171</td>
      <td>224</td>
      <td>236</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>172</td>
      <td>177</td>
      <td>237</td>
      <td>242</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>197</td>
      <td>243</td>
      <td>262</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>203</td>
      <td>263</td>
      <td>268</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>220</td>
      <td>269</td>
      <td>285</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>221</td>
      <td>233</td>
      <td>286</td>
      <td>298</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>259</td>
      <td>299</td>
      <td>324</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>260</td>
      <td>272</td>
      <td>325</td>
      <td>337</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>273</td>
      <td>282</td>
      <td>338</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8qz4">8QZ4</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGLQTVMK</span><span class="topo-outside">WKTV</span><span class="topo-membrane">VAIFVVVVVYLVTGGLVFRAL</span><span class="topo-inside">EQPFESSQKNTIALEKAEFLRDHVCVSPQELETLIQHALDADNAGVSPIGNSS</span><span class="topo-unknown">NN</span><span class="topo-inside">SSHWDL</span><span class="topo-unknown">GSAFFFAGTVITTIGYG</span><span class="topo-inside">NIAPSTE</span><span class="topo-membrane">GG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KIFCILYAIFGIPLFGFLLAGIG</span><span class="topo-outside">DQLGTIFGKSIARVEKVFRKKQVSQTKIRVISTI</span><span class="topo-membrane">LFILAGCIVFVTIPAVIFKYI</span><span class="topo-inside">EGWTA</span><span class="topo-unknown">LESIYFVVVTLTTVGFG</span><span class="topo-inside">DFVAGGNA</span><span class="topo-unknown">GIN</span><span class="topo-inside">YR</span><span class="topo-membrane">EWYKPLV</span></span>
<span class="topo-ruler">       250       260       270       280  </span>
<span class="topo-line"><span class="topo-membrane">WFWILVGLAYFAAVLSMIG</span><span class="topo-outside">DWLRVLSKKTKEE</span><span class="topo-unknown">VGEAENLYFQ</span></span>
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
      <td>8</td>
      <td>66</td>
      <td>73</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>12</td>
      <td>74</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>33</td>
      <td>78</td>
      <td>98</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>86</td>
      <td>99</td>
      <td>151</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>88</td>
      <td>152</td>
      <td>153</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>89</td>
      <td>94</td>
      <td>154</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>111</td>
      <td>160</td>
      <td>176</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>112</td>
      <td>118</td>
      <td>177</td>
      <td>183</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>143</td>
      <td>184</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>144</td>
      <td>177</td>
      <td>209</td>
      <td>242</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>198</td>
      <td>243</td>
      <td>263</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>203</td>
      <td>264</td>
      <td>268</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>220</td>
      <td>269</td>
      <td>285</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>221</td>
      <td>228</td>
      <td>286</td>
      <td>293</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>231</td>
      <td>294</td>
      <td>296</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>232</td>
      <td>233</td>
      <td>297</td>
      <td>298</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>259</td>
      <td>299</td>
      <td>324</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>260</td>
      <td>272</td>
      <td>325</td>
      <td>337</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>273</td>
      <td>282</td>
      <td>338</td>
      <td>347</td>
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

### Two-state gating mechanism (up and down conformations)

TREK-2 adopts two major conformations: the up state (3.4 Å) and
down state (3.9 Å). In the down state, the C-terminal ends of M2,
M3, and M4 project further into the cytoplasm. In the up state,
M4 is kinked at Gly312, and M2/M3 hinge at Gly201/Gly206 and
Gly248 respectively. The up state is conductive with four K⁺ ions
in the filter; the down state is non-conductive with only three
K⁺ ions. This movement represents a C-type gate mechanism at the
selectivity filter.

### Intramembrane fenestrations as drug binding sites

The down state features intramembrane-side fenestrations just
below the selectivity filter. These fenestrations provide a
hydrophobic environment for state-dependent inhibitor binding.
In the up state, the fenestration is closed by upward movement
and rotation of M4, which places Phe316 and Leu320 side chains
into the fenestration. [Norfluoxetine](/xray-mp-wiki/reagents/additives/norfluoxetine/) and [Fluoxetine](/xray-mp-wiki/reagents/ligands/fluoxetine/) bind within
the fenestration in the down state, interacting with residues
Ile194, Pro198, Cys249, Val253, Phe316, Leu320, Val276,
Leu279, and Thr280.

### State-dependent inhibition by fluoxetine/norfluoxetine

[Fluoxetine](/xray-mp-wiki/reagents/ligands/fluoxetine/) and [Norfluoxetine](/xray-mp-wiki/reagents/additives/norfluoxetine/) exhibit state-dependent inhibition
of TREK-2 by selectively binding to the closed (down) state.
The L320W mutation reduces [Norfluoxetine](/xray-mp-wiki/reagents/additives/norfluoxetine/) inhibition. Channel
activation by membrane stretch or arachidonic acid reduces
[Norfluoxetine](/xray-mp-wiki/reagents/additives/norfluoxetine/) efficacy, consistent with the up state being
the activated conformation that lacks the fenestration binding
site.

### Mechanosensitivity and pH regulation

TREK-2 is sensitive to membrane stretch, arachidonic acid, and
pH. The cytoplasmic end of M4 (Trp326) inserts into the bilayer
in the up state, coupling the cytoplasmic domain to the filter
gate. Extracellular pH sensing involves His156 in a
solvent-accessible extracellular cavity. Lipid-like density on
the channel surface in grooves at the top and bottom of M3 and
M4 may stabilize the down state.

### Nanobody modulation of TREK-2

Four nanobodies were characterized against TREK-2:
Nb-Activator-67 (partial selective activator binding to Cap
domain), Nb-Activator-76 (highly selective EC50 412 nM,
inserting W98 into intersubunit groove), Nb-Inhibitor-61
(IC50 685 nM, inserting K103 into extracellular ion exit
pathway in toxin-like mechanism), and Nb-Binder-58 (functionally
inactive tight binder). A biparatropic [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) (Nb6158) was
engineered with improved inhibitory efficacy.

### Concerted motion of M2, M3, and M4

Transition between up and down states involves coordinated
movement of all three transmembrane helices (M2, M3, M4) in
both chains of the dimer. This is supported by MD simulations
showing downward movement in the up state to adopt a
down-like conformation. Key interactions include Trp326 packing
between Met322 (M4) and Arg327 (M3) in the down state, and
Tyr315 hydrogen bonding with backbone carbonyl of Phe244 (M3)
in the up state.


## Cross-References

- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/traak/">Human TRAAK Potassium Channel</a> — Related K2P channel with shared fenestration gating mechanism
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/k2p-2-1-trek-1/">K2P 2.1 (TREK-1) Potassium Channel</a> — Related TREK subfamily member; TREK-1 I110D mutant structure
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/c-type-inactivation/">C-Type Inactivation</a> — TREK-2 gating involves selectivity filter (C-type) gating mechanism with up/down state transitions
- <a href="/xray-mp-wiki/concepts/miscellaneous/k2p-modulator-pocket/">K2P Modulator Pocket</a> — The fenestration binding site and nanobody modulation involve the K2P modulator pocket behind the selectivity filter
- <a href="/xray-mp-wiki/reagents/additives/norfluoxetine/">Norfluoxetine</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/ligands/fluoxetine/">Fluoxetine</a> — Related ligand or cofactor
- <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> — Fusion tag for crystallization or purification
