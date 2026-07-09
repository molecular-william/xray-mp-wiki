---
title: "Deinococcus radiodurans Nramp (DraNramp)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2016.09.017, doi/10.7554##eLife.84006]
verified: regex
uniprot_id: Q9RTP8
---

# Deinococcus radiodurans Nramp (DraNramp)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q9RTP8">UniProt: Q9RTP8</a>

<span class="expr-badge">Deinococcus radiodurans</span>

## Overview

DraNramp is a divalent metal transporter from Deinococcus radiodurans belonging to the Natural resistance-associated macrophage protein (Nramp) family. It is a homologue of human DMT1 (SLC11A2) and enables manganese and [Iron](/xray-mp-wiki/reagents/additives/iron/) import in bacteria. The protein adopts a LeuT-fold architecture with 11 transmembrane segments. The first crystal structure (PDB 5KTE, 2016) was determined at 3.94 A resolution in an inward-facing, substrate-free conformation with a complete TM1a helix. Subsequent high-resolution structures across three conformations (outward-open, occluded, and inward-open) in both Mn2+-bound and metal-free states provided the first complete molecular map of the Mn2+ transport cycle (Ray et al., 2023). These structures revealed that Nramps achieve alternating access by distinct Mn2+-coordination geometries in different conformations, supported by conserved polar residue networks that gate the outer and inner vestibules. A high-resolution Cd2+-bound structure revealed differences in how Cd2+ and Mn2+ are coordinated, explaining functional differences in their transport.

## Publications

### doi/10.1016##j.str.2016.09.017

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5kte">5KTE</a></td>
      <td>3.94 A</td>
      <td>I222</td>
      <td>Full-length DraNramp from Deinococcus radiodurans with surface patch mutations (QK169-170HH, EEK251-3YYY, RR398-9HH) and N-terminal 25-residue <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Truncation</a>, co-crystallized with Fab fragment</td>
      <td>none (apo, inward-facing state)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C41(DE3)
- **Construct**: DraNramp with N-terminal 25-residue [Truncation](/xray-mp-wiki/concepts/methods-techniques/truncation/) and surface patch mutations, cloned into pET21-N8H

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
      <td>Sonication</td>
      <td>--</td>
      <td>20 mM NaPO4 pH 7.0, 75 mM imidazole-HCl pH 7.0, 500 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + --</td>
      <td>Lysis buffer supplemented with 1 mM <a href="/xray-mp-wiki/reagents/additives/pmsf/">Pmsf</a>, 1 mM <a href="/xray-mp-wiki/reagents/ligands/benzamidine/">Benzamidine</a>, 0.3 mg/mL DNase I and lysozyme</td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td>Differential centrifugation</td>
      <td>--</td>
      <td>20 mM NaPO4 pH 7.0, 75 mM imidazole-HCl pH 7.0, 500 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + --</td>
      <td>Membranes pelleted at 230,000 x g for 70 min after debris removal at 27,000 x g for 20 min</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent extraction</td>
      <td>--</td>
      <td>20 mM NaPO4 pH 7.0, 75 mM imidazole-HCl pH 7.0, 500 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 1% (w/v) beta-dodecylmaltoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Solubilization for 1 hr at 4C, clarified at 140,000 x g for 35 min, filtered through 0.45 micron filter</td>
    </tr>
    <tr>
      <td>IMAC</td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Ni-Sepharose (GE Healthcare)</td>
      <td>20 mM NaPO4 pH 7.0, 75 mM imidazole-HCl pH 7.0, 500 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 0.03% beta-DDM + 0.03% beta-DDM</td>
      <td>Pre-equilibrated with lysis buffer + 0.03% beta-DDM. Washed thrice with 50 mL. Eluted with <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> gradient to 450 mM.</td>
    </tr>
    <tr>
      <td>SEC</td>
      <td>Size-exclusion chromatography</td>
      <td>Superdex S200 (GE Healthcare)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.5, 150 mM NaCl, 0.1% (w/v) beta-decylmaltoside (<a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>) + 0.1% beta-DM</td>
      <td>Protein concentrated to ~1 mL in 50 kDa cutoff centrifugal concentrator before SEC. Pooled fractions concentrated to ~5 mg/mL.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Co-crystallization with Fab fragment, vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>DraNramp-Fab complex at ~5 mg/mL in 20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.5, 150 mM NaCl, 0.1% beta-DM</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified in detail</td>
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
      <td>Cryoprotection</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>DraNramp was co-crystallized with a monoclonal Fab fragment isolated from BALB/c mice immunized with DraNramp proteoliposomes. The crystallization construct included three surface patch mutations (QK169-170HH, EEK251-3YYY, RR398-9HH). Data collected at NE-CAT beamline at APS. Structure refined to R = 0.239, R_free = 0.274. Unit cell: 113.13, 132.08, 221.0 A.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5kte">5KTE</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHHHHHHHHATLRGTAGPRGVRRILP</span><span class="topo-outside">F</span><span class="topo-membrane">LGPAVIASIAYMDPGNFATN</span><span class="topo-inside">IEGGARYGYSLL</span><span class="topo-membrane">WVILAANLMAMVIQNLS</span><span class="topo-outside">ANLGIASGRNLPELIRERWP</span><span class="topo-membrane">RPLVWFYWIQAELVAMATDLAEFL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GAALAI</span><span class="topo-inside">QLLTGLPM</span><span class="topo-membrane">FWGAVVTGVVTFWLL</span><span class="topo-unknown">NLHHRGTRPL</span><span class="topo-outside">E</span><span class="topo-membrane">LAVGAFVLMIGVAYLV</span><span class="topo-inside">QVVLARPDLAAVGAGFVPRLQGPGSAYLA</span><span class="topo-membrane">VGIIGATVMPHVIYL</span><span class="topo-unknown">HSALTQGRIQTDTTYYYRRL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">VR</span><span class="topo-outside">LNR</span><span class="topo-membrane">VDVIAAMGLAGLINMSM</span><span class="topo-inside">LAVAAATFHGKNVENAGDLTTAYQTL</span><span class="topo-unknown">TPLLG</span><span class="topo-inside">PAASV</span><span class="topo-membrane">LFAVALLASGLSSSAVGTMAGDVIM</span><span class="topo-outside">QG</span><span class="topo-unknown">FMGFHIPLWLR</span><span class="topo-outside">R</span><span class="topo-membrane">LITMLPAFIV</span><span class="topo-inside">ILLGMDPSSVL</span><span class="topo-membrane">IL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420</span>
<span class="topo-line"><span class="topo-membrane">SQVILCFGVPFALVPLLL</span><span class="topo-outside">FTAHHDVMGAL</span><span class="topo-membrane">VTRRSFTVIGWVIAVI</span><span class="topo-inside">IIALNGY</span><span class="topo-unknown">LLWELLGG</span></span>
<details class="topo-details"><summary>Topology coordinates (31 regions)</summary>
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
      <td>26</td>
      <td>17</td>
      <td>42</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>27</td>
      <td>27</td>
      <td>43</td>
      <td>43</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>28</td>
      <td>47</td>
      <td>44</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>59</td>
      <td>64</td>
      <td>75</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>76</td>
      <td>76</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>77</td>
      <td>96</td>
      <td>93</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>126</td>
      <td>113</td>
      <td>142</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>127</td>
      <td>134</td>
      <td>143</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>135</td>
      <td>149</td>
      <td>151</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>159</td>
      <td>166</td>
      <td>175</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>160</td>
      <td>160</td>
      <td>176</td>
      <td>176</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>176</td>
      <td>177</td>
      <td>192</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>205</td>
      <td>193</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>206</td>
      <td>220</td>
      <td>222</td>
      <td>236</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>242</td>
      <td>237</td>
      <td>258</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>243</td>
      <td>245</td>
      <td>259</td>
      <td>261</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>262</td>
      <td>262</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>263</td>
      <td>288</td>
      <td>279</td>
      <td>304</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>289</td>
      <td>293</td>
      <td>305</td>
      <td>309</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>294</td>
      <td>298</td>
      <td>310</td>
      <td>314</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>299</td>
      <td>323</td>
      <td>315</td>
      <td>339</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>324</td>
      <td>325</td>
      <td>340</td>
      <td>341</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>336</td>
      <td>342</td>
      <td>352</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>337</td>
      <td>337</td>
      <td>353</td>
      <td>353</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>347</td>
      <td>354</td>
      <td>363</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>348</td>
      <td>358</td>
      <td>364</td>
      <td>374</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>359</td>
      <td>378</td>
      <td>375</td>
      <td>394</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>379</td>
      <td>389</td>
      <td>395</td>
      <td>405</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>405</td>
      <td>406</td>
      <td>421</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>406</td>
      <td>412</td>
      <td>422</td>
      <td>428</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>413</td>
      <td>420</td>
      <td>429</td>
      <td>436</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.7554##eLife.84006

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8e5v">8E5V</a></td>
      <td>2.36 A</td>
      <td>P 2 21 21</td>
      <td>WT DraNramp metal-free occluded</td>
      <td>none (apo, occluded state)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8e60">8E60</a></td>
      <td>2.38 A</td>
      <td>P 2 21 21</td>
      <td>WT DraNramp Mn2+-bound occluded</td>
      <td>Mn2+ (orthosteric and external sites)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8e6i">8E6I</a></td>
      <td>2.52 A</td>
      <td>P 2 21 21</td>
      <td>M230A DraNramp Mn2+-bound inward-open</td>
      <td>Mn2+ (orthosteric and external sites)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8e6m">8E6M</a></td>
      <td>2.48 A</td>
      <td>P 2 21 21</td>
      <td>WT DraNramp Cd2+-bound inward-open</td>
      <td>Cd2+ (orthosteric and external sites)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C41(DE3)
- **Construct**: DraNramp with N-terminal 25-residue [Truncation](/xray-mp-wiki/concepts/methods-techniques/truncation/) and surface patch mutations, cloned into pET21-N8H

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
      <td>Membrane solubilization</td>
      <td>Detergent extraction</td>
      <td>--</td>
      <td>100 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.0, 150 mM NaCl + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Membranes homogenized and solubilized in 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> for 1 hr at 4C</td>
    </tr>
    <tr>
      <td>IMAC</td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Ni-Sepharose</td>
      <td>100 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.0, 150 mM NaCl, 25 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Washed with 10 CV of wash buffer, eluted with 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> in same buffer</td>
    </tr>
    <tr>
      <td>Detergent exchange (LCP prep)</td>
      <td>On-column exchange</td>
      <td>--</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.5, 150 mM NaCl, 0.003% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> + <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a></td>
      <td>Eluted protein concentrated, exchanged into <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> buffer, and purified by SEC on Superdex S200 in 10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.5, 150 mM NaCl, 0.003% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>. Peak fractions concentrated to ~25-40 mg/mL.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>DraNramp at ~25-40 mg/mL in 10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.5, 150 mM NaCl, 0.003% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>7-10 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Mesh loops, flash-frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Protein mixed with <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> in 1:1.5 volume ratio using syringe reconstitution method. 60 nL protein bolus + 720 nL precipitant dispensed onto 96-well glass sandwich plates. Metal-free and metal-soaked (5 mM MnCl2 or Cd2+) crystals grown in various precipitant conditions. Crystals grown as 30-40 um rods. Soaking experiments performed by adding 2 uL soak solution to wells for 16-18 hr. Data collected at APS beamlines 24-ID-C and 23-ID-B.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8e5v">8E5V</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHHHHHHHHAGPRGVRRILPFL</span><span class="topo-inside">G</span><span class="topo-membrane">PAVIASIAYMDPGNFATN</span><span class="topo-outside">IEGGARYGYSLL</span><span class="topo-membrane">WVILAANLMAMVIQNLS</span><span class="topo-inside">ANLGIASGRNLPELIRERWPRPLVW</span><span class="topo-membrane">FYWIQAELVAMATDLAEFLGAA</span><span class="topo-outside">LAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">QLLTGLPMFWG</span><span class="topo-membrane">AVVTGVVTFWLLNLQK</span><span class="topo-inside">R</span><span class="topo-membrane">GTRPLELAVGAFVLMIGVAYL</span><span class="topo-outside">VQVVLARPDLAAVGAGFVPRLQGPGSA</span><span class="topo-membrane">YLAVGIIGATVMPHVIYLH</span><span class="topo-inside">SALTQGRIQTDTTEEKRRLVRLN</span><span class="topo-membrane">RV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">DVIAAMGLAGLINMS</span><span class="topo-outside">MLAVAAATFHGKNVENAGDLTTAYQTLTPLLGPAASVLFAV</span><span class="topo-membrane">ALLASGLSSSAVGTMAGDVIM</span><span class="topo-inside">QGFMGFHI</span><span class="topo-membrane">PLWLRRLITMLPAFIV</span><span class="topo-outside">ILLGMDPSSV</span><span class="topo-membrane">LILSQVILC</span></span>
<span class="topo-ruler">       370       380       390       400       410    </span>
<span class="topo-line"><span class="topo-membrane">FGVPFALV</span><span class="topo-inside">PLLLFTARRDVMGALVTRRS</span><span class="topo-membrane">FTVIGWVIAVIIIALNGYLLW</span><span class="topo-outside">ELLGG</span></span>
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
      <td>22</td>
      <td>23</td>
      <td>44</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>23</td>
      <td>23</td>
      <td>45</td>
      <td>45</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>24</td>
      <td>41</td>
      <td>46</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>53</td>
      <td>64</td>
      <td>75</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>70</td>
      <td>76</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>71</td>
      <td>95</td>
      <td>93</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>117</td>
      <td>118</td>
      <td>139</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>118</td>
      <td>131</td>
      <td>140</td>
      <td>153</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>147</td>
      <td>154</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>148</td>
      <td>170</td>
      <td>170</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>169</td>
      <td>171</td>
      <td>191</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>196</td>
      <td>192</td>
      <td>218</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>197</td>
      <td>215</td>
      <td>219</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>238</td>
      <td>238</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>255</td>
      <td>261</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>256</td>
      <td>296</td>
      <td>278</td>
      <td>318</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>297</td>
      <td>317</td>
      <td>319</td>
      <td>339</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>318</td>
      <td>325</td>
      <td>340</td>
      <td>347</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>341</td>
      <td>348</td>
      <td>363</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>342</td>
      <td>351</td>
      <td>364</td>
      <td>373</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>352</td>
      <td>368</td>
      <td>374</td>
      <td>390</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>369</td>
      <td>388</td>
      <td>391</td>
      <td>410</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>389</td>
      <td>409</td>
      <td>411</td>
      <td>431</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>414</td>
      <td>432</td>
      <td>436</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8e6i">8E6I</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHHHHHHHHAGPRGVRRILPFL</span><span class="topo-inside">G</span><span class="topo-membrane">PAVIASIAYMDPGNFATNI</span><span class="topo-outside">EGGARYGYSL</span><span class="topo-membrane">LWVILAANLMAMVIQNLS</span><span class="topo-inside">ANLGIASGRNLPELIRERWPRP</span><span class="topo-membrane">LVWFYWIQAELVAMATDLAEFLGAALAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">QLLT</span><span class="topo-outside">G</span><span class="topo-membrane">LPMFWGAVVTGVVTFWLLNL</span><span class="topo-inside">QKRGT</span><span class="topo-membrane">RPLELAVGAFVLMIGVAYLVQVV</span><span class="topo-outside">LARPDLAAVGAGFVPRLQGPGSA</span><span class="topo-membrane">YLAVGIIGATVAPHVIYLH</span><span class="topo-inside">SALTQGRIQTDTTEEKRRLVRLNR</span><span class="topo-membrane">V</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">DVIAAMGLAGLINMSML</span><span class="topo-outside">AVAAATFHGKNVENAGDLTTAYQTLTPLLGPA</span><span class="topo-membrane">ASVLFAVALLASGLSSSAVGTMAGD</span><span class="topo-inside">VIMQGFMGFHI</span><span class="topo-membrane">PLWLRRLITMLPAFIVIL</span><span class="topo-outside">LGMDP</span><span class="topo-membrane">SSVLILSQVILC</span></span>
<span class="topo-ruler">       370       380       390       400       410    </span>
<span class="topo-line"><span class="topo-membrane">FGVPFALVPLLL</span><span class="topo-inside">FTARRDVMGALVTRR</span><span class="topo-membrane">SFTVIGWVIAVIIIALNGYLLW</span><span class="topo-outside">ELLGG</span></span>
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
      <td>22</td>
      <td>23</td>
      <td>44</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>23</td>
      <td>23</td>
      <td>45</td>
      <td>45</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>24</td>
      <td>42</td>
      <td>46</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>43</td>
      <td>52</td>
      <td>65</td>
      <td>74</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>70</td>
      <td>75</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>71</td>
      <td>92</td>
      <td>93</td>
      <td>114</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>124</td>
      <td>115</td>
      <td>146</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>125</td>
      <td>147</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>126</td>
      <td>145</td>
      <td>148</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>150</td>
      <td>168</td>
      <td>172</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>173</td>
      <td>173</td>
      <td>195</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>174</td>
      <td>196</td>
      <td>196</td>
      <td>218</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>197</td>
      <td>215</td>
      <td>219</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>239</td>
      <td>238</td>
      <td>261</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>257</td>
      <td>262</td>
      <td>279</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>258</td>
      <td>289</td>
      <td>280</td>
      <td>311</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>314</td>
      <td>312</td>
      <td>336</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>315</td>
      <td>325</td>
      <td>337</td>
      <td>347</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>343</td>
      <td>348</td>
      <td>365</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>344</td>
      <td>348</td>
      <td>366</td>
      <td>370</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>349</td>
      <td>372</td>
      <td>371</td>
      <td>394</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>373</td>
      <td>387</td>
      <td>395</td>
      <td>409</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>388</td>
      <td>409</td>
      <td>410</td>
      <td>431</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>414</td>
      <td>432</td>
      <td>436</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8e6m">8E6M</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHHHHHHHHAGPRGVRRI</span><span class="topo-inside">LP</span><span class="topo-membrane">FLGPAVIASIAYMDPGNFATN</span><span class="topo-outside">IEGGARYGYSLLW</span><span class="topo-membrane">VILAANLMAMVIQNLS</span><span class="topo-inside">ANLGIASGRNLPELIRERWPRPLVW</span><span class="topo-membrane">FYWIQAELVAMATDLAEFLGAALAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">Q</span><span class="topo-outside">LLTGLPM</span><span class="topo-membrane">FWGAVVTGVVTFWLLN</span><span class="topo-inside">LQKRGT</span><span class="topo-membrane">RPLELAVGAFVLMIGVAYLV</span><span class="topo-outside">QVVLARPDLAAVGAGFVPRLQGPGSAYLA</span><span class="topo-membrane">VGIIGATVMPHVIYLH</span><span class="topo-inside">SA</span><span class="topo-unknown">LTQGRIQT</span><span class="topo-inside">DTTEEKRRLVRLNR</span><span class="topo-membrane">V</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">DVIAAMGLAGLINMSM</span><span class="topo-outside">LAVAAATFHGKNVENAGDLTTAYQTLTPLLGPAASV</span><span class="topo-membrane">LFAVALLASGLSSSAVGTMAGD</span><span class="topo-inside">VIMQGFMGFHIPL</span><span class="topo-membrane">WLRRLITMLPAFIVI</span><span class="topo-outside">LLGMDPSSV</span><span class="topo-membrane">LILSQVILC</span></span>
<span class="topo-ruler">       370       380       390       400       410    </span>
<span class="topo-line"><span class="topo-membrane">FGVPFALVPLL</span><span class="topo-inside">LFTARRDVMGALVTRR</span><span class="topo-membrane">SFTVIGWVIAVIIIALNGY</span><span class="topo-outside">LLWELLGG</span></span>
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
      <td>18</td>
      <td>23</td>
      <td>40</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>20</td>
      <td>41</td>
      <td>42</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>21</td>
      <td>41</td>
      <td>43</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>54</td>
      <td>64</td>
      <td>76</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>70</td>
      <td>77</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>71</td>
      <td>95</td>
      <td>93</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>121</td>
      <td>118</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>122</td>
      <td>128</td>
      <td>144</td>
      <td>150</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>144</td>
      <td>151</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>150</td>
      <td>167</td>
      <td>172</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>170</td>
      <td>173</td>
      <td>192</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>171</td>
      <td>199</td>
      <td>193</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>215</td>
      <td>222</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>217</td>
      <td>238</td>
      <td>239</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>225</td>
      <td>240</td>
      <td>247</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>226</td>
      <td>239</td>
      <td>248</td>
      <td>261</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>256</td>
      <td>262</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>257</td>
      <td>292</td>
      <td>279</td>
      <td>314</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>314</td>
      <td>315</td>
      <td>336</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>315</td>
      <td>327</td>
      <td>337</td>
      <td>349</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>342</td>
      <td>350</td>
      <td>364</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>343</td>
      <td>351</td>
      <td>365</td>
      <td>373</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>352</td>
      <td>371</td>
      <td>374</td>
      <td>393</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>372</td>
      <td>387</td>
      <td>394</td>
      <td>409</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>388</td>
      <td>406</td>
      <td>410</td>
      <td>428</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>407</td>
      <td>414</td>
      <td>429</td>
      <td>436</td>
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

### Inward-open conformation with complete TM1a

The DraNramp structure at 3.94 A reveals the complete TM segment 1a (absent in previous ScaNramp structure), bent outward at a 103-degree angle between TM1a and TM1b, lying nearly parallel to the membrane. This creates a large aqueous vestibule on the cytoplasmic side. The structure represents a substrate-free inward-facing conformation with the metal-binding site unoccupied.

### TM4 G153R alters metal selectivity

The G153R mutation on TM4 perturbs the closing of the outward metal-permeation pathway and alters the selectivity of the conserved metal-binding site. G153R transports more Ca2+ than wild-type while Cd2+ transport is reduced. The mutation shows additive effects with the M230A selectivity filter mutation, suggesting it distorts the binding site in favor of Ca2+ while maintaining use of the canonical metal-binding site.

### TM1a G45R locks the inward-open state

The G45R mutation on TM1a prevents conformational change by sterically blocking the essential movement of TM1a, locking the transporter in an inward-facing state. G45R drastically decreases accessibility of the outward-open conformational reporter A61C, indicating a strong preference for the inward-open conformation. The mutation does not cause steric clash in the inward-facing state but would clash in the outward-open state.

### TM1a movement is essential for transport

NEM modification of single-cysteine mutants along TM1a severely impaired metal transport for 6 of 7 positions tested, demonstrating that TM1a movement into a congested environment is an integral part of the Nramp conformational change. Tryptophan substitutions at these positions similarly impaired transport and locked the protein in the inward-facing state, confirming that unencumbered TM1a movement is essential for the conformational change and transport cycle.

### High-resolution structures map the complete Mn2+ transport cycle

High-resolution structures of DraNramp in three conformations (outward-open, occluded, inward-open) in both Mn2+-bound and metal-free states provide the first complete molecular map of the Mn2+ transport cycle. The Mn2+-coordination geometry differs across conformations: six-coordinate distorted octahedral in outward-open and occluded states, and seven-coordinate in the inward-open state. The pseudosymmetrically related alanines A53 (TM1a) and A227 (TM6b) alternately coordinate Mn2+ as the gates open and close.

### Polar residue networks gate the outer and inner vestibules

Two conserved polar networks seal the outer gate: the Q378 network (Q378-D56-T130 via conserved waters) and the T228 network (T228-N275-N82). These networks persist in the occluded and inward-open states but are disrupted in the outward-open state. The inner vestibule is gated by the R244 network (R244-E176-D263) and the Q89 network (Q89-Y54-H237). Y54 in TM1a acts as a conserved aromatic gate, progressively swinging downward to open the inner vestibule, with Y54A nearly abolishing transport while Y54F retains near-wildtype activity.

### Cd2+ and Mn2+ differ in coordination and thermodynamics

The Cd2+-bound structure (PDB 8E6M, 2.48 A) reveals inward-open conformation with differences in metal coordination. D56 adopts a different rotamer and does not directly coordinate Cd2+, while M230 (soft sulfur ligand) still coordinates. Cd2+ has six coordinating ligands (vs seven for Mn2+), with longer bond distances. ITC shows Mn2+ binding is endothermic while Cd2+ binding is exothermic. Cd2+ binding favors the inward-open state, whereas Mn2+ favors the occluded state, creating different thermodynamic landscapes for physiological vs toxic metal transport.


## Cross-References

- <a href="/xray-mp-wiki/concepts/protein-families/slc11-nramp-family/">SLC11 (NRAMP) Family</a> — DraNramp is a member of the Nramp/SLC11 family of divalent metal transporters
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — DraNramp operates via alternating access between inward-open and outward-open states
- <a href="/xray-mp-wiki/concepts/miscellaneous/leut-return-state-mechanism/">LeuT Return State Mechanism</a> — DraNramp adopts the LeuT-fold architecture common to this transporter superfamily
- <a href="/xray-mp-wiki/proteins/slc-transporters/sca-dmt/">ScaDMT</a> — Related Nramp family divalent metal transporter from Staphylococcus capitis
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">N-Dodecyl-beta-D-maltopyranoside (beta-DDM)</a> — Detergent used for membrane protein solubilization
- <a href="/xray-mp-wiki/reagents/detergents/dm/">Decylmaltoside</a> — Detergent used in SEC buffer and crystallization
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Final purification step
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — IMAC used for initial purification via His-tag
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase (LCP)</a> — LCP crystallization method used for high-resolution structures
- <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> — Detergent used in final purification and crystallization buffer
