---
title: "Human 5-HT1B Serotonin Receptor"
created: 2026-06-21
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1232807]
verified: false
---

# Human 5-HT1B Serotonin Receptor

## Overview

The human 5-HT1B receptor is a class A G protein-coupled receptor for serotonin (5-hydroxytryptamine, 5-HT). It couples preferentially to Gi proteins and is widely expressed in the central nervous system. 5-HT1B receptors are therapeutic targets for migraine treatment (triptan class drugs) and are implicated in mood disorders. Crystal structures of 5-HT1B in complex with ergotamine (ERG) and dihydroergotamine (DHE) were determined using BRIL fusion constructs and LCP crystallization, revealing the molecular basis for ligand recognition and selectivity across serotonin receptor subtypes.


## Publications

### doi/10.1126##science.1232807

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4iar">4IAR</a></td>
      <td>2.7</td>
      <td>C2</td>
      <td>Human 5-HT1B-BRIL fusion (ICL3 residues L240-M305 replaced by BRIL; N-terminal truncation at N32; L138³·⁴¹W thermostabilizing mutation), in complex with ergotamine (ERG)</td>
      <td>Ergotamine (ERG)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4iar">4IAR</a></td>
      <td>2.8</td>
      <td>C222</td>
      <td>Human 5-HT1B-BRIL fusion (5-HT1B-2 construct, ICL3 residues L240-K303 replaced by BRIL; N-terminal truncation at N32; L138³·⁴¹W mutation), in complex with dihydroergotamine (DHE)</td>
      <td>Dihydroergotamine (DHE)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda (Sf9) insect cells via baculovirus
- **Construct**: Human 5-HT1B with BRIL fusion replacing ICL3; N-terminal HA signal sequence + Flag tag + 10×His tag + TEV protease site; N32 truncation; L138³·⁴¹W thermostabilizing mutation

**Purification:**

- **Expression system**: Spodoptera frugiperda Sf9 insect cells
- **Expression construct**: 5-HT1B-BRIL fusion (ICL3 replacement) with N-terminal HA-Flag-10×His-TEV tag
- **Tag info**: 10×His tag + Flag tag, cleaved by AcTEV protease

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
      <td>Cell culture and expression</td>
      <td>Baculovirus infection (P2, MOI 5)</td>
      <td>--</td>
      <td>Sf9 cells in suspension + --</td>
      <td>48 h post-infection at 27 °C</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Hypotonic lysis and high-salt wash</td>
      <td>--</td>
      <td>10 mM HEPES pH 7.5, 10 mM MgCl₂, 20 mM KCl + protease inhibitors; then 1.0 M NaCl, 10 mM HEPES pH 7.5, 10 mM MgCl₂, 20 mM KCl + --</td>
      <td>Washed membranes resuspended in buffer with 50 µM ligand (ERG or DHE) + 2 mg/ml iodoacetamide</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>--</td>
      <td>50 mM HEPES pH 7.5, 200 mM NaCl, 20 mM imidazole + 1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.2% (w/v) <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>4 °C, 1 h incubation; supernatant clarified at 160,000×g for 30 min</td>
    </tr>
    <tr>
      <td>Immobilized metal affinity chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> IMAC</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> IMAC resin (Clontech)</td>
      <td>Wash I: 50 mM HEPES pH 7.5, 800 mM NaCl, 50 µM ligand, 20 mM imidazole, 10% glycerol, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 10 mM ATP, 10 mM MgCl₂; Wash II: 50 mM HEPES pH 7.5, 500 mM NaCl, 50 mM imidazole, 50 µM ligand, 10% glycerol, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> / 0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> (Wash I); 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> / 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> (Wash II)</td>
      <td>Eluted with 250 mM imidazole in 50 mM HEPES pH 7.5, 500 mM NaCl, 50 µM ligand, 10% glycerol, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
    </tr>
    <tr>
      <td>Buffer exchange</td>
      <td>PD MiniTrap G-25 desalting</td>
      <td>PD MiniTrap G-25 (GE Healthcare)</td>
      <td>50 mM HEPES pH 7.5, 500 mM NaCl, 50 µM ligand, 10% glycerol, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Removes imidazole</td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td>AcTEV protease treatment</td>
      <td>--</td>
      <td>50 mM HEPES pH 7.5, 500 mM NaCl, 50 µM ligand, 10% glycerol, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Overnight at 4 °C; His-tagged AcTEV and cleaved fragment removed by second <a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> IMAC incubation</td>
    </tr>
    <tr>
      <td>Concentration</td>
      <td>Centrifugal concentration</td>
      <td>--</td>
      <td>50 mM HEPES pH 7.5, 500 mM NaCl, 50 µM ligand, 10% glycerol, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Concentrated to 50-80 mg/ml using 100 kDa MWCO Vivaspin; purity >95% by SDS-PAGE; single peak by aSEC</td>
    </tr>
  </tbody>
</table>
**Final sample**: 50-80 mg/ml in 50 mM HEPES pH 7.5, 500 mM NaCl, 50 µM ligand (ERG or DHE), 10% glycerol, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)
**Yield**: --
**Purity**: >95% by SDS-PAGE; monodisperse by aSEC

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>5-HT1B-1/ERG complex (construct 5-HT1B-1)</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>Monoolein (54% w/w) + cholesterol (6% w/w)</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>40% (w/w) protein solution, 54% monoolein, 6% cholesterol</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 °C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2-3 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals harvested from LCP matrix; flash frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grew to 20-50 µm; 40 nL protein-lipid overlaid with 800 nL precipitant; 96-well glass sandwich plates</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>5-HT1B-2/DHE complex (construct 5-HT1B-2)</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>Monoolein (54% w/w) + cholesterol (6% w/w)</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>40% (w/w) protein solution, 54% monoolein, 6% cholesterol</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 °C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2-3 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals harvested from LCP matrix; flash frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grew to 20-50 µm; data from 56 crystals merged for 2.8 Å structure</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4iar">4IAR</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GGTCSAKD</span><span class="topo-inside">YIYQDSISLPWKVL</span><span class="topo-membrane">LVMLLALITLATTLSNAFVIA</span><span class="topo-outside">TVYRTRKLHTPANYLI</span><span class="topo-membrane">ASLAVTDLLVSILVMPIST</span><span class="topo-inside">MYTVTGRWTLGQV</span><span class="topo-membrane">VCDFWLSSDITCCTASIWHLCV</span><span class="topo-outside">IALDRYW</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">AITDAVEYSAKRTPKRAAVM</span><span class="topo-membrane">IALVWVFSISISLPPFF</span><span class="topo-inside">WRQA</span><span class="topo-unknown">KAEEEV</span><span class="topo-inside">SECVVNTDH</span><span class="topo-membrane">ILYTVYSTVGAFYFPTLLLIA</span><span class="topo-outside">LYGRIYVEARSRIADLEDNWETLNDNLKVIEKADNAAQVKDAL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TKMRAAALDAQKATPPKLEDKSPDSPEMKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLAARERKATKTL</span><span class="topo-membrane">GIILGAFIVCWLPFFIISLV</span><span class="topo-inside">MPI</span><span class="topo-unknown">CKDAC</span><span class="topo-inside">WFHLA</span></span>
<span class="topo-ruler">       370       380       390       400 </span>
<span class="topo-line"><span class="topo-inside">I</span><span class="topo-membrane">FDFFTWLGYLNSLINPIIYTM</span><span class="topo-outside">SN</span><span class="topo-unknown">EDFKQAFHKL</span><span class="topo-outside">IRFK</span><span class="topo-unknown">CTS</span></span>
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
      <td>8</td>
      <td>30</td>
      <td>37</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>22</td>
      <td>38</td>
      <td>51</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>43</td>
      <td>52</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>44</td>
      <td>59</td>
      <td>73</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>78</td>
      <td>89</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>91</td>
      <td>108</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>113</td>
      <td>121</td>
      <td>142</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>140</td>
      <td>143</td>
      <td>169</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>157</td>
      <td>170</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>158</td>
      <td>161</td>
      <td>187</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>162</td>
      <td>167</td>
      <td>191</td>
      <td>196</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>168</td>
      <td>176</td>
      <td>197</td>
      <td>205</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>197</td>
      <td>206</td>
      <td>226</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>327</td>
      <td>227</td>
      <td>316</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>347</td>
      <td>317</td>
      <td>336</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>348</td>
      <td>350</td>
      <td>337</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>351</td>
      <td>355</td>
      <td>340</td>
      <td>344</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>356</td>
      <td>361</td>
      <td>345</td>
      <td>350</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>362</td>
      <td>382</td>
      <td>351</td>
      <td>371</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>384</td>
      <td>372</td>
      <td>373</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>385</td>
      <td>394</td>
      <td>374</td>
      <td>383</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>395</td>
      <td>398</td>
      <td>384</td>
      <td>387</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>399</td>
      <td>401</td>
      <td>388</td>
      <td>390</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4iar">4IAR</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GGTCSAKD</span><span class="topo-inside">YIYQDSISLPWKVL</span><span class="topo-membrane">LVMLLALITLATTLSNAFVIA</span><span class="topo-outside">TVYRTRKLHTPANYLI</span><span class="topo-membrane">ASLAVTDLLVSILVMPIST</span><span class="topo-inside">MYTVTGRWTLGQV</span><span class="topo-membrane">VCDFWLSSDITCCTASIWHLCV</span><span class="topo-outside">IALDRYW</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">AITDAVEYSAKRTPKRAAVM</span><span class="topo-membrane">IALVWVFSISISLPPFF</span><span class="topo-inside">WRQA</span><span class="topo-unknown">KAEEEV</span><span class="topo-inside">SECVVNTDH</span><span class="topo-membrane">ILYTVYSTVGAFYFPTLLLIA</span><span class="topo-outside">LYGRIYVEARSRIADLEDNWETLNDNLKVIEKADNAAQVKDAL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TKMRAAALDAQKATPPKLEDKSPDSPEMKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLAARERKATKTL</span><span class="topo-membrane">GIILGAFIVCWLPFFIISLV</span><span class="topo-inside">MPI</span><span class="topo-unknown">CKDAC</span><span class="topo-inside">WFHLA</span></span>
<span class="topo-ruler">       370       380       390       400 </span>
<span class="topo-line"><span class="topo-inside">I</span><span class="topo-membrane">FDFFTWLGYLNSLINPIIYTM</span><span class="topo-outside">SN</span><span class="topo-unknown">EDFKQAFHKL</span><span class="topo-outside">IRFK</span><span class="topo-unknown">CTS</span></span>
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
      <td>8</td>
      <td>30</td>
      <td>37</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>22</td>
      <td>38</td>
      <td>51</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>43</td>
      <td>52</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>44</td>
      <td>59</td>
      <td>73</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>78</td>
      <td>89</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>91</td>
      <td>108</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>113</td>
      <td>121</td>
      <td>142</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>140</td>
      <td>143</td>
      <td>169</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>157</td>
      <td>170</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>158</td>
      <td>161</td>
      <td>187</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>162</td>
      <td>167</td>
      <td>191</td>
      <td>196</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>168</td>
      <td>176</td>
      <td>197</td>
      <td>205</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>197</td>
      <td>206</td>
      <td>226</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>327</td>
      <td>227</td>
      <td>316</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>347</td>
      <td>317</td>
      <td>336</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>348</td>
      <td>350</td>
      <td>337</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>351</td>
      <td>355</td>
      <td>340</td>
      <td>344</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>356</td>
      <td>361</td>
      <td>345</td>
      <td>350</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>362</td>
      <td>382</td>
      <td>351</td>
      <td>371</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>384</td>
      <td>372</td>
      <td>373</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>385</td>
      <td>394</td>
      <td>374</td>
      <td>383</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>395</td>
      <td>398</td>
      <td>384</td>
      <td>387</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>399</td>
      <td>401</td>
      <td>388</td>
      <td>390</td>
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

### Extended binding pocket differs between 5-HT1B and 5-HT2B

Comparison of the 5-HT1B/ERG and 5-HT2B/ERG structures reveals that the orthosteric binding pocket is conserved, but the extended binding site differs significantly between the two receptors. The tripeptide moiety of ERG and DHE extends into an extended binding pocket created by extracellular loop 2 (ECL2), where sequence divergence between 5-HT1B and 5-HT2B accounts for differences in ligand selectivity. This extended pocket is a key determinant of triptan drug selectivity for 5-HT1B/1D over 5-HT2B receptors.

### Membrane-embedded ligand entry via TM5-TM6 gap

Like the S1P1 receptor, 5-HT1B shows a gap between the extracellular ends of TM5 and TM6 that may provide a membrane-embedded access route for ligands. The N-terminal cap and ECL2 restrict direct access from the extracellular milieu, suggesting that lipophilic ergolines and triptans access the binding pocket through the lipid bilayer.

### BRIL fusion strategy for GPCR crystallization

The 5-HT1B structures used BRIL (thermostabilized apocytochrome b₅₆₂ RIL mutant) replacing ICL3, enabling LCP crystallization. Two different BRIL junction sites were tested (5-HT1B-1: L240-M305 replaced; 5-HT1B-2: L240-K303 replaced), with the L138³·⁴¹W mutation further stabilizing the receptor. Both constructs showed ligand binding properties similar to wild type, validating the fusion approach.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/human-5-ht2b-receptor/">Human 5-HT2B Receptor</a> — Closely related serotonin receptor; structural comparison for ligand selectivity
- <a href="/xray-mp-wiki/reagents/ligands/ergotamine/">Ergotamine (ERG)</a> — Ligand used for 5-HT1B-1 structure determination
- <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL (Thermostabilized apocytochrome b562 RIL)</a> — Fusion protein used for crystallization
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent for solubilization and purification
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — LCP method used for 5-HT1B crystallization
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Primary lipid for LCP matrix
