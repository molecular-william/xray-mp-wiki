---
title: "HiTehA (TehA from Haemophilus influenzae)"
created: 2026-06-02
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature09487, doi/10.1107##s139900471500423x]
verified: false
---

# HiTehA (TehA from Haemophilus influenzae)

## Overview

HiTehA is the [TEHA](/xray-mp-wiki/proteins/other-ion-channels/teha/) anion channel protein from Haemophilus influenzae. It is a bacterial
homologue of the plant SLOW ANION CHANNEL 1 ([SLAC1 (SLOW ANION CHANNEL 1 from Arabidopsis thaliana)](/xray-mp-wiki/proteins/other-ion-channels/slac1/)) and functions as an anion-selective
channel. HiTehA forms a symmetrical trimer, with each protomer containing ten transmembrane
helices arranged from five helical hairpin pairs to create a central five-helix transmembrane
pore. The pore is gated by a highly conserved phenylalanine residue (Phe 262). The structure
was originally solved by selenomethionyl (SeMet) [SAD](/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/) phasing at 1.20 A resolution from
cryocooled crystals. A subsequent room-temperature structure at 2.3 A resolution was
determined using in situ data collection from multiple crystals in vapour-diffusion plates,
demonstrating the first in situ membrane protein structure determination at a synchrotron.


## Publications

### doi/10.1038##nature09487

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3m7b">3M7B</a></td>
      <td>1.20</td>
      <td>R3</td>
      <td>Full-length <a href="/xray-mp-wiki/proteins/other-ion-channels/teha/">TEHA</a> from Haemophilus influenzae (residues 6-313) with Flag and deca-His tag, <a href="/xray-mp-wiki/reagents/proteases/tev-protease/">TEV</a> cleavable</td>
      <td>beta-<a href="/xray-mp-wiki/reagents/detergents/og/">OG</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21(DE3) pLysS
- **Construct**: HiTehA cloned into pWaldoGFPe with C-terminal tag, purified in 20 mM Tris pH 7.5, 150 mM NaCl, 60 mM n-[OG](/xray-mp-wiki/reagents/detergents/og/)
- **Notes**: Overexpressed and purified as described by Drew et al. (2006)

**Purification:**

- **Expression system**: Escherichia coli BL21(DE3) pLysS
- **Expression construct**: HiTehA with Flag and deca-His tag, [TEV](/xray-mp-wiki/reagents/proteases/tev-protease/) cleavable
- **Tag info**: Flag and deca-His tag, cleavable by [TEV](/xray-mp-wiki/reagents/proteases/tev-protease/) protease

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
      <td>Sonication</td>
      <td>—</td>
      <td>Buffer with <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td></td>
    </tr>
    <tr>
      <td>Metal affinity purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td></td>
    </tr>
    <tr>
      <td>Analytical <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a> screening</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td>Analytical <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a> column</td>
      <td>12 different detergents tested</td>
      <td></td>
    </tr>
  </tbody>
</table>
**Final sample**: HiTehA exchanged into n-[OG](/xray-mp-wiki/reagents/detergents/og/)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>HiTehA in <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td><a href="/xray-mp-wiki/reagents/additives/peg-600/">PEG 600</a> or <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>277 K</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Original crystallization; crystals diffracted beyond 1.1 A.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3m7b">3M7B</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MNIT</span><span class="topo-inside">KPFPLPT</span><span class="topo-membrane">GYFGIPLGLAALSLAW</span><span class="topo-outside">FHLENLFPAARMV</span><span class="topo-membrane">SDVLGIVASAVWILFILMYA</span><span class="topo-inside">YKLRYY</span><span class="topo-unknown">FEEVRAEYH</span><span class="topo-inside">SPVRFS</span><span class="topo-membrane">FIALIPITTMLVGDIL</span><span class="topo-outside">YRWNPLI</span><span class="topo-membrane">AEVLIWIGTIGQLLFS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">TLRVS</span><span class="topo-inside">ELWQGGVFEQKSTHP</span><span class="topo-membrane">SFYLPAVAANFTSA</span><span class="topo-unknown">S</span><span class="topo-outside">SLALLGYHDL</span><span class="topo-membrane">GYLFFGAGMIAWIIFEP</span><span class="topo-inside">VLLQHLRISSLEPQFRAT</span><span class="topo-membrane">MGIVLAPAFVCVSAY</span><span class="topo-outside">LSINHGEVDTL</span><span class="topo-membrane">AKILWGYGFLQLFF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310    </span>
<span class="topo-line"><span class="topo-membrane">LLRLF</span><span class="topo-inside">PWIVEKGLNIGL</span><span class="topo-membrane">WAFSFGLASMANSA</span><span class="topo-outside">TAFYHGNVLQGV</span><span class="topo-membrane">SIFAFVFSNVMIGLLVLMTIY</span><span class="topo-inside">KLTKGQFFL</span><span class="topo-unknown">K</span></span>
<details class="topo-details"><summary>Topology coordinates (26 regions)</summary>
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
      <td>27</td>
      <td>12</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>40</td>
      <td>28</td>
      <td>40</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>60</td>
      <td>41</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>66</td>
      <td>61</td>
      <td>66</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>75</td>
      <td>67</td>
      <td>75</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>76</td>
      <td>81</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>97</td>
      <td>82</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>98</td>
      <td>104</td>
      <td>98</td>
      <td>104</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>125</td>
      <td>105</td>
      <td>125</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>126</td>
      <td>140</td>
      <td>126</td>
      <td>140</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>154</td>
      <td>141</td>
      <td>154</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>155</td>
      <td>155</td>
      <td>155</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>156</td>
      <td>165</td>
      <td>156</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>182</td>
      <td>166</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>200</td>
      <td>183</td>
      <td>200</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>201</td>
      <td>215</td>
      <td>201</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>226</td>
      <td>216</td>
      <td>226</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>227</td>
      <td>245</td>
      <td>227</td>
      <td>245</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>246</td>
      <td>257</td>
      <td>246</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>271</td>
      <td>258</td>
      <td>271</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>283</td>
      <td>272</td>
      <td>283</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>304</td>
      <td>284</td>
      <td>304</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>305</td>
      <td>313</td>
      <td>305</td>
      <td>313</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>314</td>
      <td>314</td>
      <td>314</td>
      <td>314</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3m7b">3M7B</a> — Chain B (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MNIT</span><span class="topo-inside">KPFPLPT</span><span class="topo-membrane">GYFGIPLGLAALSLAW</span><span class="topo-outside">FHLENLFPAARMV</span><span class="topo-membrane">SDVLGIVASAVWILFILMYA</span><span class="topo-inside">YKLRYY</span><span class="topo-unknown">FEEVRAEYH</span><span class="topo-inside">SPVRFS</span><span class="topo-membrane">FIALIPITTMLVGDIL</span><span class="topo-outside">YRWNPLI</span><span class="topo-membrane">AEVLIWIGTIGQLLFS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">TLRVS</span><span class="topo-inside">ELWQGGVFEQKSTHP</span><span class="topo-membrane">SFYLPAVAANFTSA</span><span class="topo-unknown">S</span><span class="topo-outside">SLALLGYHDL</span><span class="topo-membrane">GYLFFGAGMIAWIIFEP</span><span class="topo-inside">VLLQHLRISSLEPQFRAT</span><span class="topo-membrane">MGIVLAPAFVCVSAY</span><span class="topo-outside">LSINHGEVDTL</span><span class="topo-membrane">AKILWGYGFLQLFF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310    </span>
<span class="topo-line"><span class="topo-membrane">LLRLF</span><span class="topo-inside">PWIVEKGLNIGL</span><span class="topo-membrane">WAFSFGLASMANSA</span><span class="topo-outside">TAFYHGNVLQGV</span><span class="topo-membrane">SIFAFVFSNVMIGLLVLMTIY</span><span class="topo-inside">KLTKGQFFL</span><span class="topo-unknown">K</span></span>
<details class="topo-details"><summary>Topology coordinates (26 regions)</summary>
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
      <td>27</td>
      <td>12</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>40</td>
      <td>28</td>
      <td>40</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>60</td>
      <td>41</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>66</td>
      <td>61</td>
      <td>66</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>75</td>
      <td>67</td>
      <td>75</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>76</td>
      <td>81</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>97</td>
      <td>82</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>98</td>
      <td>104</td>
      <td>98</td>
      <td>104</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>125</td>
      <td>105</td>
      <td>125</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>126</td>
      <td>140</td>
      <td>126</td>
      <td>140</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>154</td>
      <td>141</td>
      <td>154</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>155</td>
      <td>155</td>
      <td>155</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>156</td>
      <td>165</td>
      <td>156</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>182</td>
      <td>166</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>200</td>
      <td>183</td>
      <td>200</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>201</td>
      <td>215</td>
      <td>201</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>226</td>
      <td>216</td>
      <td>226</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>227</td>
      <td>245</td>
      <td>227</td>
      <td>245</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>246</td>
      <td>257</td>
      <td>246</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>271</td>
      <td>258</td>
      <td>271</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>283</td>
      <td>272</td>
      <td>283</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>304</td>
      <td>284</td>
      <td>304</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>305</td>
      <td>313</td>
      <td>305</td>
      <td>313</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>314</td>
      <td>314</td>
      <td>314</td>
      <td>314</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3m7b">3M7B</a> — Chain C (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MNIT</span><span class="topo-inside">KPFPLPT</span><span class="topo-membrane">GYFGIPLGLAALSLAW</span><span class="topo-outside">FHLENLFPAARMV</span><span class="topo-membrane">SDVLGIVASAVWILFILMYA</span><span class="topo-inside">YKLRYY</span><span class="topo-unknown">FEEVRAEYH</span><span class="topo-inside">SPVRFS</span><span class="topo-membrane">FIALIPITTMLVGDIL</span><span class="topo-outside">YRWNPLI</span><span class="topo-membrane">AEVLIWIGTIGQLLFS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">TLRVS</span><span class="topo-inside">ELWQGGVFEQKSTHP</span><span class="topo-membrane">SFYLPAVAANFTSA</span><span class="topo-unknown">S</span><span class="topo-outside">SLALLGYHDL</span><span class="topo-membrane">GYLFFGAGMIAWIIFEP</span><span class="topo-inside">VLLQHLRISSLEPQFRAT</span><span class="topo-membrane">MGIVLAPAFVCVSAY</span><span class="topo-outside">LSINHGEVDTL</span><span class="topo-membrane">AKILWGYGFLQLFF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310    </span>
<span class="topo-line"><span class="topo-membrane">LLRLF</span><span class="topo-inside">PWIVEKGLNIGL</span><span class="topo-membrane">WAFSFGLASMANSA</span><span class="topo-outside">TAFYHGNVLQGV</span><span class="topo-membrane">SIFAFVFSNVMIGLLVLMTIY</span><span class="topo-inside">KLTKGQFFL</span><span class="topo-unknown">K</span></span>
<details class="topo-details"><summary>Topology coordinates (26 regions)</summary>
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
      <td>27</td>
      <td>12</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>40</td>
      <td>28</td>
      <td>40</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>60</td>
      <td>41</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>66</td>
      <td>61</td>
      <td>66</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>75</td>
      <td>67</td>
      <td>75</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>76</td>
      <td>81</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>97</td>
      <td>82</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>98</td>
      <td>104</td>
      <td>98</td>
      <td>104</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>125</td>
      <td>105</td>
      <td>125</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>126</td>
      <td>140</td>
      <td>126</td>
      <td>140</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>154</td>
      <td>141</td>
      <td>154</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>155</td>
      <td>155</td>
      <td>155</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>156</td>
      <td>165</td>
      <td>156</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>182</td>
      <td>166</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>200</td>
      <td>183</td>
      <td>200</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>201</td>
      <td>215</td>
      <td>201</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>226</td>
      <td>216</td>
      <td>226</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>227</td>
      <td>245</td>
      <td>227</td>
      <td>245</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>246</td>
      <td>257</td>
      <td>246</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>271</td>
      <td>258</td>
      <td>271</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>283</td>
      <td>272</td>
      <td>283</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>304</td>
      <td>284</td>
      <td>304</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>305</td>
      <td>313</td>
      <td>305</td>
      <td>313</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>314</td>
      <td>314</td>
      <td>314</td>
      <td>314</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1107##s139900471500423x

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ycr">4YCR</a></td>
      <td>2.30</td>
      <td>H3</td>
      <td>Full-length HiTehA (residues 1-313) expressed from pWaldoGFPe vector</td>
      <td>beta-<a href="/xray-mp-wiki/reagents/detergents/og/">OG</a> (<a href="/xray-mp-wiki/reagents/detergents/og/">OG</a>)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21(DE3) pLysS
- **Construct**: HiTehA cloned into pWaldoGFPe with C-terminal tag, purified in 20 mM Tris pH 7.5, 150 mM NaCl, 60 mM n-[OG](/xray-mp-wiki/reagents/detergents/og/)
- **Notes**: Overexpressed and purified as described by Drew et al. (2006)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (sitting drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>HiTehA at 20 mg/mL in 20 mM Tris pH 7.5, 150 mM NaCl, 60 mM <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M NaCl, 120 mM Tris pH 9.4, 20% (v/v) <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>1:1 (100 nL + 100 nL)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>277 K (crystal growth), ambient for data collection</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>7-10 days</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in 96-well sitting-drop plates (CrystalQuick X) using Mosquito robot. Data collected directly in-plate at room temperature on Diamond I24 with Pilatus3 6M detector.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ycr">4YCR</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">PLPTGY</span><span class="topo-membrane">FGIPLGLAALSLA</span><span class="topo-inside">WFHLENLFPAARMV</span><span class="topo-membrane">SDVLGIVASAVWILFILM</span><span class="topo-outside">YAYKLRYY</span><span class="topo-unknown">FEEVRAEYH</span><span class="topo-outside">SPVRFSFI</span><span class="topo-membrane">ALIPITTMLVGDIL</span><span class="topo-inside">YRWNPLI</span><span class="topo-membrane">AEVLIWIGTIGQLLFSTL</span><span class="topo-outside">RVSEL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WQGGVFEQKSTHPSFY</span><span class="topo-membrane">LPAVAANFTSA</span><span class="topo-unknown">S</span><span class="topo-inside">SLALLGYHDL</span><span class="topo-membrane">GYLFFGAGMIAWIIFEP</span><span class="topo-outside">VLLQHLRISSLEPQFRATMG</span><span class="topo-membrane">IVLAPAFVCVSAY</span><span class="topo-inside">LSINHGEVDTL</span><span class="topo-membrane">AKILWGYGFLQLFFLLR</span><span class="topo-outside">LFPW</span></span>
<span class="topo-ruler">       250       260       270       280       290         </span>
<span class="topo-line"><span class="topo-outside">IVEKGLNIGL</span><span class="topo-membrane">WAFSFGLASMANSA</span><span class="topo-inside">TAFYHGNVLQGV</span><span class="topo-membrane">SIFAFVFSNVMIGLLVLMTIY</span><span class="topo-outside">KL</span></span>
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
      <td>6</td>
      <td>8</td>
      <td>13</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>19</td>
      <td>14</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>20</td>
      <td>33</td>
      <td>27</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>51</td>
      <td>41</td>
      <td>58</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>59</td>
      <td>59</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>68</td>
      <td>67</td>
      <td>75</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>69</td>
      <td>76</td>
      <td>76</td>
      <td>83</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>90</td>
      <td>84</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>97</td>
      <td>98</td>
      <td>104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>115</td>
      <td>105</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>136</td>
      <td>123</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>147</td>
      <td>144</td>
      <td>154</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>148</td>
      <td>155</td>
      <td>155</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>149</td>
      <td>158</td>
      <td>156</td>
      <td>165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>175</td>
      <td>166</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>176</td>
      <td>195</td>
      <td>183</td>
      <td>202</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>208</td>
      <td>203</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>209</td>
      <td>219</td>
      <td>216</td>
      <td>226</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>236</td>
      <td>227</td>
      <td>243</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>237</td>
      <td>250</td>
      <td>244</td>
      <td>257</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>264</td>
      <td>258</td>
      <td>271</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>265</td>
      <td>276</td>
      <td>272</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>297</td>
      <td>284</td>
      <td>304</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>299</td>
      <td>305</td>
      <td>306</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ycr">4YCR</a> — Chain B (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">PLPTGY</span><span class="topo-membrane">FGIPLGLAALSLA</span><span class="topo-inside">WFHLENLFPAARMV</span><span class="topo-membrane">SDVLGIVASAVWILFILM</span><span class="topo-outside">YAYKLRYY</span><span class="topo-unknown">FEEVRAEYH</span><span class="topo-outside">SPVRFSFI</span><span class="topo-membrane">ALIPITTMLVGDIL</span><span class="topo-inside">YRWNPLI</span><span class="topo-membrane">AEVLIWIGTIGQLLFSTL</span><span class="topo-outside">RVSEL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WQGGVFEQKSTHPSFY</span><span class="topo-membrane">LPAVAANFTSA</span><span class="topo-unknown">S</span><span class="topo-inside">SLALLGYHDL</span><span class="topo-membrane">GYLFFGAGMIAWIIFEP</span><span class="topo-outside">VLLQHLRISSLEPQFRATMG</span><span class="topo-membrane">IVLAPAFVCVSAY</span><span class="topo-inside">LSINHGEVDTL</span><span class="topo-membrane">AKILWGYGFLQLFFLLR</span><span class="topo-outside">LFPW</span></span>
<span class="topo-ruler">       250       260       270       280       290         </span>
<span class="topo-line"><span class="topo-outside">IVEKGLNIGL</span><span class="topo-membrane">WAFSFGLASMANSA</span><span class="topo-inside">TAFYHGNVLQGV</span><span class="topo-membrane">SIFAFVFSNVMIGLLVLMTIY</span><span class="topo-outside">KL</span></span>
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
      <td>6</td>
      <td>8</td>
      <td>13</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>19</td>
      <td>14</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>20</td>
      <td>33</td>
      <td>27</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>51</td>
      <td>41</td>
      <td>58</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>59</td>
      <td>59</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>68</td>
      <td>67</td>
      <td>75</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>69</td>
      <td>76</td>
      <td>76</td>
      <td>83</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>90</td>
      <td>84</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>97</td>
      <td>98</td>
      <td>104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>115</td>
      <td>105</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>136</td>
      <td>123</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>147</td>
      <td>144</td>
      <td>154</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>148</td>
      <td>155</td>
      <td>155</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>149</td>
      <td>158</td>
      <td>156</td>
      <td>165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>175</td>
      <td>166</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>176</td>
      <td>195</td>
      <td>183</td>
      <td>202</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>208</td>
      <td>203</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>209</td>
      <td>219</td>
      <td>216</td>
      <td>226</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>236</td>
      <td>227</td>
      <td>243</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>237</td>
      <td>250</td>
      <td>244</td>
      <td>257</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>264</td>
      <td>258</td>
      <td>271</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>265</td>
      <td>276</td>
      <td>272</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>297</td>
      <td>284</td>
      <td>304</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>299</td>
      <td>305</td>
      <td>306</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ycr">4YCR</a> — Chain C (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">PLPTGY</span><span class="topo-membrane">FGIPLGLAALSLA</span><span class="topo-inside">WFHLENLFPAARMV</span><span class="topo-membrane">SDVLGIVASAVWILFILM</span><span class="topo-outside">YAYKLRYY</span><span class="topo-unknown">FEEVRAEYH</span><span class="topo-outside">SPVRFSFI</span><span class="topo-membrane">ALIPITTMLVGDIL</span><span class="topo-inside">YRWNPLI</span><span class="topo-membrane">AEVLIWIGTIGQLLFSTL</span><span class="topo-outside">RVSEL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WQGGVFEQKSTHPSFY</span><span class="topo-membrane">LPAVAANFTSA</span><span class="topo-unknown">S</span><span class="topo-inside">SLALLGYHDL</span><span class="topo-membrane">GYLFFGAGMIAWIIFEP</span><span class="topo-outside">VLLQHLRISSLEPQFRATMG</span><span class="topo-membrane">IVLAPAFVCVSAY</span><span class="topo-inside">LSINHGEVDTL</span><span class="topo-membrane">AKILWGYGFLQLFFLLR</span><span class="topo-outside">LFPW</span></span>
<span class="topo-ruler">       250       260       270       280       290         </span>
<span class="topo-line"><span class="topo-outside">IVEKGLNIGL</span><span class="topo-membrane">WAFSFGLASMANSA</span><span class="topo-inside">TAFYHGNVLQGV</span><span class="topo-membrane">SIFAFVFSNVMIGLLVLMTIY</span><span class="topo-outside">KL</span></span>
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
      <td>6</td>
      <td>8</td>
      <td>13</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>19</td>
      <td>14</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>20</td>
      <td>33</td>
      <td>27</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>51</td>
      <td>41</td>
      <td>58</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>59</td>
      <td>59</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>68</td>
      <td>67</td>
      <td>75</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>69</td>
      <td>76</td>
      <td>76</td>
      <td>83</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>90</td>
      <td>84</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>97</td>
      <td>98</td>
      <td>104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>115</td>
      <td>105</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>136</td>
      <td>123</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>147</td>
      <td>144</td>
      <td>154</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>148</td>
      <td>155</td>
      <td>155</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>149</td>
      <td>158</td>
      <td>156</td>
      <td>165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>175</td>
      <td>166</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>176</td>
      <td>195</td>
      <td>183</td>
      <td>202</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>208</td>
      <td>203</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>209</td>
      <td>219</td>
      <td>216</td>
      <td>226</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>236</td>
      <td>227</td>
      <td>243</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>237</td>
      <td>250</td>
      <td>244</td>
      <td>257</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>264</td>
      <td>258</td>
      <td>271</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>265</td>
      <td>276</td>
      <td>272</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>297</td>
      <td>284</td>
      <td>304</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>299</td>
      <td>305</td>
      <td>306</td>
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

### Room-temperature in situ structure determination

The first membrane protein structure determined at room temperature using in situ data
collection at a synchrotron. Data from 56 crystals (63 partial wedges) were merged using
BLEND software after radiation damage assessment. The final dataset reached 2.3 A resolution
with R_meas = 0.107, R_p.i.m. = 0.044, completeness = 92.9%, and multiplicity = 4.9.
The room-temperature structure is very similar to the cryogenic structure (RMSD 0.66 A
for all atoms), with a notable loop shift in the TM6-TM7 connecting loop (max 2.9 A
at Ser192). The gating residue Phe262 remains in the same position and orientation.

### OG detergent binding in the channel cavity

The electron density from both room-temperature and 100 K data revealed one
[OG](/xray-mp-wiki/reagents/detergents/og/) ([OG](/xray-mp-wiki/reagents/detergents/og/)) detergent molecule inside the channel cavity on the cytoplasmic side,
which was not reported in the original 1.2 A structure. The hydrophobic alkyl tail of OG
reaches deep into the channel, surrounded by hydrophobic residues including Phe262, Ile203,
Leu18, Leu144.

### Trimeric organization of HiTehA

HiTehA forms tight trimers with three-fold axes aligned to the crystal lattice. Subunits
bury 8,947 A^2 of total surface area within trimer interfaces. The trimeric state was
confirmed both by size-exclusion multi-angle light-scattering ([SEC-MALS](/xray-mp-wiki/methods/quality-assessment/sec-mals/)) measurements
and by chemical cross-linking experiments.

### Novel ten-helix transmembrane fold

Each HiTehA protomer has ten transmembrane helices arranged from five tandemly repeated
helical hairpins with quasi-five-fold symmetry. An inner pentad of outwardly directed
odd-numbered transmembrane helices creates a pore through each protomer perpendicular to
the membrane plane. Even-numbered helices from the five hairpins surround the inner pore
as an outer layer.

### Phe 262 gate occluding the central pore

The central pore through each HiTehA protomer is occluded by the side chain of Phe 262
in the wild-type structure. The gating role of Phe 262 is conserved in [SLAC1 (SLOW ANION CHANNEL 1 from Arabidopsis thaliana)](/xray-mp-wiki/proteins/other-ion-channels/slac1/) as Phe 450.
The room-temperature structure confirms Phe262 is in the same position and orientation as
in the cryogenic structure.


## Cross-References

- <a href="/xray-mp-wiki/proteins/other-ion-channels/slac1/">SLAC1 (SLOW ANION CHANNEL 1 from Arabidopsis thaliana)</a> — HiTehA is the bacterial homologue of plant SLAC1; structure used for homology modeling
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/anion-channel-gating/">Anion Channel Gating via Phenylalanine Gate</a> — Phe 262 in HiTehA (Phe 450 in SLAC1) is the conserved gating residue
- <a href="/xray-mp-wiki/methods/structure-determination/xray-crystallography/">X-ray Crystallography</a> — First in situ room-temperature synchrotron X-ray structure of a membrane protein
- <a href="/xray-mp-wiki/concepts/methods-techniques/in-situ-crystallography/">In situ Crystallography</a> — HiTehA was the first membrane protein structure determined by in situ data collection
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/quality-assessment/sec-mals/">SEC-MALS</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/other-ion-channels/teha/">TEHA</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg-600/">PEG 600</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used in purification or crystallization
