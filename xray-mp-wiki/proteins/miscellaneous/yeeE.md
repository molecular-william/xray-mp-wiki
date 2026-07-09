---
title: "YeeE Thiosulfate Transporter from Shewanella thermophila"
created: 2026-06-10
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1126##sciadv.aba7637]
verified: regex
uniprot_id: G0GAP6
---

# YeeE Thiosulfate Transporter from Shewanella thermophila

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/G0GAP6">UniProt: G0GAP6</a>

<span class="expr-badge">Spirochaeta thermophila</span>

## Overview

YeeE is a bacterial membrane protein that mediates thiosulfate uptake for use as an inorganic sulfur source in cysteine synthesis. The crystal structure of YeeE from Shewanella thermophila at 2.5 Å resolution reveals an unprecedented hourglass-like architecture with an intramolecular pseudo 222 symmetry fold. YeeE is composed of 13 helices including 9 transmembrane α helices, with four characteristic loops (LA-LD) buried toward the center forming a constricted pathway. Three conserved cysteine residues (C22, C91, C293) along the pathway are essential for thiosulfate transport activity.


## Publications

### doi/10.1126##sciadv.aba7637

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6leo">6LEO</a></td>
      <td>2.52</td>
      <td>C2221</td>
      <td>StYeeE(1-328)-GSSGENLYFQFTS-H8 (WT)</td>
      <td>Thiosulfate</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6lep">6LEP</a></td>
      <td>2.60</td>
      <td>C2221</td>
      <td>StYeeE(1-328)-GSSGENLYFQFTS-H8 (C91A mutant)</td>
      <td>—</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C41 (DE3) heterologous expression

- **Construct**: Full-length StYeeE(1-328) with C-terminal GSSGENLYFQFTS-H8 tag, in modified pCGFP-BC vector (pKK550)

- **Induction**: 1 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at OD600=0.8, 37°C for 15 hours

- **Media**: LB Broth (Lennox) with 50 μg/ml [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/)


**Purification:**

- **Expression system**: E. coli C41 (DE3)
- **Expression construct**: StYeeE(1-328)-GSSGENLYFQFTS-H8
- **Tag info**: C-terminal H8 tag, removed by TEV(S219V) protease cleavage

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
      <td>Cell harvesting and lysis</td>
      <td>Microfluidizer</td>
      <td>—</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 1 mM EDTA-Na pH 8.0, 0.1 mM PMSF</td>
      <td>Three passes at 15,000 psi</td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td>Differential centrifugation</td>
      <td>—</td>
      <td></td>
      <td>22,500g for 30 min (remove debris), then 140,000g for 60 min (pellet membranes)</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl, 0.1 mM PMSF, 1 mM β-ME, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> pH 8.0 + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Resuspend and rotate for 45 min at 4°C, then ultracentrifuge at 140,000g for 30 min</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA</td>
      <td>Ni-NTA agarose (Qiagen)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Equilibrate with 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, wash with 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, stepwise elution with 40, 60, 100, 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td>TEV protease digestion</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>TEV(S219V) protease at 10:1 molar ratio (YeeE:TEV), dialysis against cleavage buffer</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified YeeE in 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 300 mM NaCl, 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystal structure determined at 2.5 Å resolution using SIRAS phasing with SeMet-substituted protein from 326 merged crystals. Data collected at SPring-8 BL32XU. Native structure from 515 merged crystals. C91A mutant from 93 merged crystals. Structure shows alternative conformations from oxidized/reduced forms between C22 and C91.
</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6leo">6LEO</a> — Chain A (9 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MIW</span><span class="topo-membrane">TGLLVGFLFGIVLQRG</span><span class="topo-outside">R</span><span class="topo-unknown">ICFNSAFR</span><span class="topo-outside">DVLLFKDN</span><span class="topo-membrane">YLFKLAVFTLALEMILFVL</span><span class="topo-inside">LSQVGLMQMNPKPLN</span><span class="topo-membrane">LVGNIIGGFVFGLGMVLA</span><span class="topo-outside">G</span><span class="topo-unknown">GCASGVTYRVGEGLT</span><span class="topo-outside">T</span><span class="topo-membrane">AWFAALFYGLGAYAT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KSG</span><span class="topo-inside">AFSWWLSWVGQFKSPLSVEESAYYVKGAGPTISSVLGLNPW</span><span class="topo-membrane">IPALVIAALFILWAFGTK</span><span class="topo-outside">TTSRETK</span><span class="topo-membrane">FNWKIASVCLALVAGLGF</span><span class="topo-inside">ITSTLSGRKY</span><span class="topo-unknown">GLGITGGWINLFQGFL</span><span class="topo-inside">TNSPLNW</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330         </span>
<span class="topo-line"><span class="topo-membrane">EGLEIVGIILGAGVAAAVA</span><span class="topo-outside">GEFKLRMPKNPVTY</span><span class="topo-membrane">LQVGIGGLLMGIGAVTA</span><span class="topo-inside">G</span><span class="topo-unknown">GCNIGHFLTGVPQLA</span><span class="topo-inside">L</span><span class="topo-membrane">SSWLASIFFILGNWTMAWI</span><span class="topo-outside">LF</span><span class="topo-unknown">LESSGENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (28 regions)</summary>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>19</td>
      <td>4</td>
      <td>19</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>20</td>
      <td>20</td>
      <td>20</td>
      <td>20</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>21</td>
      <td>28</td>
      <td>21</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>36</td>
      <td>29</td>
      <td>36</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>55</td>
      <td>37</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>56</td>
      <td>70</td>
      <td>56</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>88</td>
      <td>71</td>
      <td>88</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>89</td>
      <td>89</td>
      <td>89</td>
      <td>89</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>104</td>
      <td>90</td>
      <td>104</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>105</td>
      <td>105</td>
      <td>105</td>
      <td>105</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>123</td>
      <td>106</td>
      <td>123</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>124</td>
      <td>164</td>
      <td>124</td>
      <td>164</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>165</td>
      <td>182</td>
      <td>165</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>189</td>
      <td>183</td>
      <td>189</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>207</td>
      <td>190</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>217</td>
      <td>208</td>
      <td>217</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>233</td>
      <td>218</td>
      <td>233</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>234</td>
      <td>240</td>
      <td>234</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>241</td>
      <td>259</td>
      <td>241</td>
      <td>259</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>260</td>
      <td>273</td>
      <td>260</td>
      <td>273</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>274</td>
      <td>290</td>
      <td>274</td>
      <td>290</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>291</td>
      <td>291</td>
      <td>291</td>
      <td>291</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>306</td>
      <td>292</td>
      <td>306</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>307</td>
      <td>307</td>
      <td>307</td>
      <td>307</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>308</td>
      <td>326</td>
      <td>308</td>
      <td>326</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>327</td>
      <td>328</td>
      <td>327</td>
      <td>328</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>329</td>
      <td>339</td>
      <td>329</td>
      <td>339</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6lep">6LEP</a> — Chain A (9 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MIW</span><span class="topo-membrane">TGLLVGFLFGIVLQRG</span><span class="topo-outside">R</span><span class="topo-unknown">ICFNSAFR</span><span class="topo-outside">DVL</span><span class="topo-unknown">LFKDN</span><span class="topo-outside">YL</span><span class="topo-membrane">FKLAVFTLALEMILFVL</span><span class="topo-inside">LSQVGLMQMNPKPLN</span><span class="topo-membrane">LVGNIIGGFVFGLGMVLA</span><span class="topo-outside">G</span><span class="topo-unknown">GAASGVTYRVGEG</span><span class="topo-outside">LT</span><span class="topo-membrane">TAWFAALFYGLGAYAT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">K</span><span class="topo-inside">SGAFSWWLSWVGQFKSPLSVEESAYYVKGAGPTISSVLGLNPW</span><span class="topo-membrane">IPALVIAALFILWAFG</span><span class="topo-outside">T</span><span class="topo-unknown">KTTSR</span><span class="topo-outside">ETKFNW</span><span class="topo-membrane">KIASVCLALVAGLGF</span><span class="topo-inside">ITSTLSGRKYG</span><span class="topo-unknown">LGITGGWINLFQGFL</span><span class="topo-inside">TNSPLNW</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330         </span>
<span class="topo-line"><span class="topo-membrane">EGLEIVGIILGAGVAA</span><span class="topo-outside">AVAGEFKLRMPKNPVTYL</span><span class="topo-membrane">QVGIGGLLMGIGAVTA</span><span class="topo-inside">G</span><span class="topo-unknown">GCNIGHFLTGVPQLA</span><span class="topo-inside">L</span><span class="topo-membrane">SSWLASIFFILGNWTM</span><span class="topo-outside">AWILF</span><span class="topo-unknown">LESSGENLYFQ</span></span>
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
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>19</td>
      <td>4</td>
      <td>19</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>20</td>
      <td>20</td>
      <td>20</td>
      <td>20</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>21</td>
      <td>28</td>
      <td>21</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>31</td>
      <td>29</td>
      <td>31</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>36</td>
      <td>32</td>
      <td>36</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>37</td>
      <td>38</td>
      <td>37</td>
      <td>38</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>55</td>
      <td>39</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>56</td>
      <td>70</td>
      <td>56</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>88</td>
      <td>71</td>
      <td>88</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>89</td>
      <td>89</td>
      <td>89</td>
      <td>89</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>102</td>
      <td>90</td>
      <td>102</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>103</td>
      <td>104</td>
      <td>103</td>
      <td>104</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>121</td>
      <td>105</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>122</td>
      <td>164</td>
      <td>122</td>
      <td>164</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>165</td>
      <td>180</td>
      <td>165</td>
      <td>180</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>181</td>
      <td>181</td>
      <td>181</td>
      <td>181</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>186</td>
      <td>182</td>
      <td>186</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>187</td>
      <td>192</td>
      <td>187</td>
      <td>192</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>207</td>
      <td>193</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>218</td>
      <td>208</td>
      <td>218</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>219</td>
      <td>233</td>
      <td>219</td>
      <td>233</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>234</td>
      <td>240</td>
      <td>234</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>241</td>
      <td>256</td>
      <td>241</td>
      <td>256</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>257</td>
      <td>274</td>
      <td>257</td>
      <td>274</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>290</td>
      <td>275</td>
      <td>290</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>291</td>
      <td>291</td>
      <td>291</td>
      <td>291</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>306</td>
      <td>292</td>
      <td>306</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>307</td>
      <td>307</td>
      <td>307</td>
      <td>307</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>308</td>
      <td>323</td>
      <td>308</td>
      <td>323</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>324</td>
      <td>328</td>
      <td>324</td>
      <td>328</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>329</td>
      <td>339</td>
      <td>329</td>
      <td>339</td>
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

### Intramolecular pseudo 222 symmetry fold

YeeE adopts a previously unknown fold with 13 helices (H1-H13) including 9 transmembrane α helices. The structure exhibits intramolecular pseudo 222 symmetry with four elements (H1-H3, H4-H6, H8-H10, H11-H13) assembled around three orthogonal pseudo dyad axes. Four characteristic loops (LA-LD) are buried toward the center of YeeE and form the central constricted region surrounded by the nine helices.

### Thiosulfate binding and transport mechanism

A thiosulfate ion is bound at position I on the positively charged periplasmic concave side, coordinated by hydrogen bonds to E241, K67, and C293. Three conserved cysteine residues (C22 in LA, C91 in LB, C293 in LD) are linearly located at ~7 Å intervals along the transport pathway. MD simulations suggest thiosulfate is transferred from position I to positions II and III via S-H-S hydrogen bonds between thiosulfate sulfur and cysteine thiol groups. The mechanism does not require large conformational changes in transmembrane helices, unlike rocking bundle or alternating access mechanisms.

### Thiosulfate versus sulfate selectivity

YeeE transports thiosulfate (S2O3^2-) but not sulfate (SO4^2-). The selectivity is explained by the S-H-S hydrogen bond relay mechanism requiring an exposed sulfur atom on the substrate. Sulfate's sulfur atom is shielded by four oxygen atoms, preventing interaction with the conserved cysteine residues. This selectivity makes thiosulfate a preferred sulfur source for cysteine synthesis.


## Cross-References

- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/antibiotics/ampicillin/">Ampicillin</a> — Antibiotic used in selection
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> — Buffer component in purification or crystallization
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used in purification or crystallization
