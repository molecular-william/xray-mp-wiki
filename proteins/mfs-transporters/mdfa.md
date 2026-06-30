---
title: "Multidrug Transporter MdfA (E26T/D34M/A150E) from Escherichia coli"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1038##s41598-020-60332-8]
verified: false
---

# Multidrug Transporter MdfA (E26T/D34M/A150E) from Escherichia coli

## Overview

[MdfA Multidrug Efflux Transporter](/xray-mp-wiki/proteins/mfs-transporters/mdfA/) is a prototypical H+-dependent multidrug transporter from Escherichia coli belonging to the Major Facilitator Superfamily ([MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/)), specifically the drug/H+ antiporter-1 (DHA1) subfamily. It exports physicochemically diverse substrates by utilizing the H+ electrochemical gradient. This work describes the X-ray structures of a redesigned [MdfA Multidrug Efflux Transporter](/xray-mp-wiki/proteins/mfs-transporters/mdfA/) triple mutant (E26T/D34M/A150E) wherein the substrate-binding and protonation sites were rearranged while retaining multidrug transport function. Structures bound to [Chloramphenicol](/xray-mp-wiki/reagents/antibiotics/chloramphenicol/) (Cm), [DXC](/xray-mp-wiki/reagents/additives/deoxycholate/) ([DXC](/xray-mp-wiki/reagents/additives/deoxycholate/)), and lauryldimethylamine N-oxide ([LDAO](/xray-mp-wiki/reagents/detergents/ldao/)) reveal intermediate states during antibiotic recognition and suggest structural changes accompanying substrate-evoked deprotonation, highlighting the remarkable mechanistic flexibility in drug/H+ coupling.


## Publications

### doi/10.1038##s41598-020-60332-8

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6vrz">6VRZ</a></td>
      <td>2.0</td>
      <td>—</td>
      <td>E26T/D34M/A150E triple mutant with C-terminal deca-histidine tag (thrombin-cleaved)</td>
      <td><a href="/xray-mp-wiki/reagents/antibiotics/chloramphenicol/">Chloramphenicol</a> (Cm)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6vs2">6VS2</a></td>
      <td></td>
      <td>—</td>
      <td>E26T/D34M/A150E triple mutant</td>
      <td><a href="/xray-mp-wiki/reagents/antibiotics/chloramphenicol/">Chloramphenicol</a> (Cm)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6vs0">6VS0</a></td>
      <td></td>
      <td>—</td>
      <td>E26T/D34M/A150E triple mutant</td>
      <td><a href="/xray-mp-wiki/reagents/additives/deoxycholate/">DXC</a> (<a href="/xray-mp-wiki/reagents/additives/deoxycholate/">DXC</a>)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6vs1">6VS1</a></td>
      <td>3.0</td>
      <td>—</td>
      <td>E26T/D34M/A150E triple mutant</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21 (DE3) ΔacrABΔmacABΔyojHI
- **Construct**: E26T/D34M/A150E triple mutant in modified pET28b with C-terminal cleavable deca-histidine tag
- **Notes**: Induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at 30°C for 4 h in LB media

**Purification:**

- **Expression system**: E. coli BL21 (DE3) ΔacrABΔmacABΔyojHI
- **Expression construct**: E26T/D34M/A150E with C-terminal deca-histidine tag
- **Tag info**: Deca-histidine tag (C-terminal, removed by thrombin)

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
      <td>French pressure cell</td>
      <td>—</td>
      <td></td>
      <td>Multiple passages through pre-chilled French press</td>
    </tr>
    <tr>
      <td>Membrane extraction</td>
      <td>Solubilization</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a>-NaOH pH 7.5, 500 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 1.5 mM TCEP + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Membranes collected by ultracentrifugation at 100,000g</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA</td>
      <td>Ni-NTA column</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a>-NaOH pH 7.5, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 1.5 mM TCEP</td>
      <td>Eluted with 450 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Tag removal</td>
      <td>Thrombin cleavage</td>
      <td>—</td>
      <td></td>
      <td>Incubated with thrombin overnight to remove deca-histidine tag</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC (<a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a>)</td>
      <td>—</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.2% NG, 0.025% <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a>, 0.05% <a href="/xray-mp-wiki/reagents/additives/deoxycholate/">DXC</a>, 1.5 mM TCEP</td>
      <td></td>
    </tr>
  </tbody>
</table>
**Final sample**: ~10 mg/mL in crystallization buffer

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>~10 mg/mL E26T/D34M/A150E in 25 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.2% NG, 0.025% <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a>, 0.05% <a href="/xray-mp-wiki/reagents/additives/deoxycholate/">DXC</a>, 1.5 mM TCEP</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM MES-NaOH pH 6.0, 150 mM NaCl, 150 mM MgCl2, 20 mM Pr(OAc)3</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>24</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>10 µL hanging drops with equal volumes of protein and reservoir. Crystals obtained at pH 8.0 (Cm-bound), pH 5.0 (Cm-bound), pH 6.0 (DXC-bound), and pH 8.0 (LDAO-bound). Phase solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> combined with SAD phasing.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6vrz">6VRZ</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">QALLFPL</span><span class="topo-membrane">CLVLYTFSTYIGNMMIQPG</span><span class="topo-outside">MLAVVEQYQAGIDWVP</span><span class="topo-membrane">TSMTAYLAGGMFLQWLL</span><span class="topo-inside">GPLSDRIGRRPVM</span><span class="topo-membrane">LAGVVWFIVTCLAILLA</span><span class="topo-outside">QNIE</span><span class="topo-membrane">QFTLLRFLQGISLCFIG</span><span class="topo-inside">AVGYAAIQES</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FEEAVCIKITAL</span><span class="topo-membrane">MANVELIAPLLGPLVGAAW</span><span class="topo-outside">IHVLPW</span><span class="topo-membrane">EGMFVLFAALAAISFFG</span><span class="topo-inside">LQRAMPETATRIGEKLS</span><span class="topo-unknown">LKELGRDYKLVLK</span><span class="topo-inside">NGRFV</span><span class="topo-membrane">AGALALGFVSLPLLAWIAQS</span><span class="topo-outside">PIIIITGEQLS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">SYEYG</span><span class="topo-membrane">LLQVPIFGALIAGNLLLAR</span><span class="topo-inside">LTSRRTVRS</span><span class="topo-membrane">LIIMGGWPIMIGLLVAA</span><span class="topo-outside">AATVISSHAYLWM</span><span class="topo-membrane">TAGLSIYAFGIGLANAGLV</span><span class="topo-inside">RLTLFASDMSKGTVSA</span><span class="topo-membrane">AMGMLQMLIFTVGIEISK</span><span class="topo-outside">HAWL</span></span>
<span class="topo-ruler">       370       380       </span>
<span class="topo-line"><span class="topo-outside">NGGNGLF</span><span class="topo-membrane">NLFNLVNGILWLSLMVIFL</span><span class="topo-inside">K</span></span>
<details class="topo-details"><summary>Topology coordinates (27 regions)</summary>
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
      <td>14</td>
      <td>20</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>26</td>
      <td>21</td>
      <td>39</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>42</td>
      <td>40</td>
      <td>55</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>59</td>
      <td>56</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>72</td>
      <td>73</td>
      <td>85</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>89</td>
      <td>86</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>93</td>
      <td>103</td>
      <td>106</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>110</td>
      <td>107</td>
      <td>123</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>132</td>
      <td>124</td>
      <td>145</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>151</td>
      <td>146</td>
      <td>164</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>152</td>
      <td>157</td>
      <td>165</td>
      <td>170</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>174</td>
      <td>171</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>191</td>
      <td>188</td>
      <td>204</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>204</td>
      <td>205</td>
      <td>217</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>205</td>
      <td>209</td>
      <td>218</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>210</td>
      <td>229</td>
      <td>223</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>245</td>
      <td>243</td>
      <td>258</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>264</td>
      <td>259</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>265</td>
      <td>273</td>
      <td>278</td>
      <td>286</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>274</td>
      <td>290</td>
      <td>287</td>
      <td>303</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>291</td>
      <td>303</td>
      <td>304</td>
      <td>316</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>304</td>
      <td>322</td>
      <td>317</td>
      <td>335</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>323</td>
      <td>338</td>
      <td>336</td>
      <td>351</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>339</td>
      <td>356</td>
      <td>352</td>
      <td>369</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>367</td>
      <td>370</td>
      <td>380</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>386</td>
      <td>381</td>
      <td>399</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>387</td>
      <td>400</td>
      <td>400</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6vs2">6VS2</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">QALLFPLCLVL</span><span class="topo-membrane">YTFSTYIGNMMIQP</span><span class="topo-outside">GMLAVVEQYQAGIDWVP</span><span class="topo-membrane">TSMTAYLAGGMFLQ</span><span class="topo-inside">WLLGPLSDRIGRRPVMLAG</span><span class="topo-membrane">VVWFIVTCLAILLA</span><span class="topo-outside">QNIEQ</span><span class="topo-membrane">FTLLRFLQGISLC</span><span class="topo-inside">FIGAVGYAAIQES</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FEEAVCIKITALMAN</span><span class="topo-membrane">VELIAPLLGPLVGAAW</span><span class="topo-outside">IHVLPW</span><span class="topo-membrane">EGMFVLFAALAAIS</span><span class="topo-inside">FFGLQRAMPETATRIGEKLSL</span><span class="topo-unknown">KELGRDYKLVL</span><span class="topo-inside">KNGRFVA</span><span class="topo-membrane">GALALGFVSLPLLAWIAQS</span><span class="topo-outside">PIIIITGEQLS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">SYEYG</span><span class="topo-membrane">LLQVPIFGALIAGNLL</span><span class="topo-inside">LARLTSRRTVRSLI</span><span class="topo-membrane">IMGGWPIMIGLLVA</span><span class="topo-outside">AAATVISSHAYLWMT</span><span class="topo-membrane">AGLSIYAFGIGLANA</span><span class="topo-inside">GLVRLTLFASDMSKGTVSAAM</span><span class="topo-membrane">GMLQMLIFTVGIEIS</span><span class="topo-outside">KHAWL</span></span>
<span class="topo-ruler">       370       380       </span>
<span class="topo-line"><span class="topo-outside">NGGNGLFN</span><span class="topo-membrane">LFNLVNGILWLSLMVI</span><span class="topo-inside">FLK</span></span>
<details class="topo-details"><summary>Topology coordinates (27 regions)</summary>
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
      <td>11</td>
      <td>14</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>25</td>
      <td>25</td>
      <td>38</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>42</td>
      <td>39</td>
      <td>55</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>56</td>
      <td>56</td>
      <td>69</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>75</td>
      <td>70</td>
      <td>88</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>76</td>
      <td>89</td>
      <td>89</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>94</td>
      <td>103</td>
      <td>107</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>107</td>
      <td>108</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>135</td>
      <td>121</td>
      <td>148</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>136</td>
      <td>151</td>
      <td>149</td>
      <td>164</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>152</td>
      <td>157</td>
      <td>165</td>
      <td>170</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>171</td>
      <td>171</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>172</td>
      <td>192</td>
      <td>185</td>
      <td>205</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>203</td>
      <td>206</td>
      <td>216</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>204</td>
      <td>210</td>
      <td>217</td>
      <td>223</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>229</td>
      <td>224</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>245</td>
      <td>243</td>
      <td>258</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>261</td>
      <td>259</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>275</td>
      <td>275</td>
      <td>288</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>276</td>
      <td>289</td>
      <td>289</td>
      <td>302</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>290</td>
      <td>304</td>
      <td>303</td>
      <td>317</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>305</td>
      <td>319</td>
      <td>318</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>320</td>
      <td>340</td>
      <td>333</td>
      <td>353</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>355</td>
      <td>354</td>
      <td>368</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>356</td>
      <td>368</td>
      <td>369</td>
      <td>381</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>369</td>
      <td>384</td>
      <td>382</td>
      <td>397</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>385</td>
      <td>387</td>
      <td>398</td>
      <td>400</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6vs0">6VS0</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">QALLFPLCLVL</span><span class="topo-membrane">YTFSTYIGNMMIQ</span><span class="topo-outside">PGMLAVVEQYQAGIDWVP</span><span class="topo-membrane">TSMTAYLAGGMFLQ</span><span class="topo-inside">WLLGPLSDRIGRRPVMLAG</span><span class="topo-membrane">VVWFIVTCLAILLA</span><span class="topo-outside">QNIEQ</span><span class="topo-membrane">FTLLRFLQGISLC</span><span class="topo-inside">FIGAVGYAAIQES</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FEEAVCIKITALMA</span><span class="topo-membrane">NVELIAPLLGPLVG</span><span class="topo-outside">AAWIHVLPW</span><span class="topo-membrane">EGMFVLFAALAAI</span><span class="topo-inside">SFFGLQRAMPETATRIGEKLS</span><span class="topo-unknown">LKELGRDYKLVL</span><span class="topo-inside">KNGRFV</span><span class="topo-membrane">AGALALGFVSLPLLAWIA</span><span class="topo-outside">QSPIIIITGEQLS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">SYEYGLLQ</span><span class="topo-membrane">VPIFGALIAGNLLL</span><span class="topo-inside">ARLTSRRTVRS</span><span class="topo-membrane">LIIMGGWPIMIGLL</span><span class="topo-outside">VAAAATVISSHAYLWMTA</span><span class="topo-membrane">GLSIYAFGIGLANA</span><span class="topo-inside">GLVRLTLFASDMSKGTVSAAM</span><span class="topo-membrane">GMLQMLIFTVGIEI</span><span class="topo-outside">SKHAWL</span></span>
<span class="topo-ruler">       370       380       </span>
<span class="topo-line"><span class="topo-outside">NGGNGLFNLF</span><span class="topo-membrane">NLVNGILWLSLMVIFL</span><span class="topo-inside">K</span></span>
<details class="topo-details"><summary>Topology coordinates (27 regions)</summary>
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
      <td>11</td>
      <td>14</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>24</td>
      <td>25</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>42</td>
      <td>38</td>
      <td>55</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>56</td>
      <td>56</td>
      <td>69</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>75</td>
      <td>70</td>
      <td>88</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>76</td>
      <td>89</td>
      <td>89</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>94</td>
      <td>103</td>
      <td>107</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>107</td>
      <td>108</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>134</td>
      <td>121</td>
      <td>147</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>135</td>
      <td>148</td>
      <td>148</td>
      <td>161</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>157</td>
      <td>162</td>
      <td>170</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>170</td>
      <td>171</td>
      <td>183</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>171</td>
      <td>191</td>
      <td>184</td>
      <td>204</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>203</td>
      <td>205</td>
      <td>216</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>204</td>
      <td>209</td>
      <td>217</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>210</td>
      <td>227</td>
      <td>223</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>228</td>
      <td>248</td>
      <td>241</td>
      <td>261</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>262</td>
      <td>262</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>263</td>
      <td>273</td>
      <td>276</td>
      <td>286</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>274</td>
      <td>287</td>
      <td>287</td>
      <td>300</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>288</td>
      <td>305</td>
      <td>301</td>
      <td>318</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>306</td>
      <td>319</td>
      <td>319</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>320</td>
      <td>340</td>
      <td>333</td>
      <td>353</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>354</td>
      <td>354</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>355</td>
      <td>370</td>
      <td>368</td>
      <td>383</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>371</td>
      <td>386</td>
      <td>384</td>
      <td>399</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>387</td>
      <td>400</td>
      <td>400</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6vs1">6VS1</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">QALLFPL</span><span class="topo-membrane">CLVLYTFSTYIGNMMIQ</span><span class="topo-outside">PG</span><span class="topo-unknown">MLAVVEQY</span><span class="topo-outside">QAGIDWVP</span><span class="topo-membrane">TSMTAYLAGGMFLQ</span><span class="topo-inside">WLLGPLSDRIGRRPVML</span><span class="topo-membrane">AGVVWFIVTCLAILLA</span><span class="topo-outside">QNIEQ</span><span class="topo-membrane">FTLLRFLQGISLCFIG</span><span class="topo-inside">AVGYAAIQES</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FEEAVCIKITA</span><span class="topo-membrane">LMANVELIAPLLGPLVG</span><span class="topo-outside">AAWIHVLPWEG</span><span class="topo-membrane">MFVLFAALAAISFFGLQ</span><span class="topo-inside">RAMPETATRIGEKLSL</span><span class="topo-unknown">KELGRDYKLVL</span><span class="topo-inside">KNGRFVA</span><span class="topo-membrane">GALALGFVSLPLLAWIA</span><span class="topo-outside">QSPIIIITGEQLS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">SYEYGLLQ</span><span class="topo-membrane">VPIFGALIAGNLLLARL</span><span class="topo-inside">TSRRTVRSL</span><span class="topo-membrane">IIMGGWPIMIGLLVA</span><span class="topo-outside">AAATVISSHAYLWMTA</span><span class="topo-membrane">GLSIYAFGIGLANAGLV</span><span class="topo-inside">RLTLFASDMSKGTVSAAM</span><span class="topo-membrane">GMLQMLIFTVGIEIS</span><span class="topo-outside">KHAWL</span></span>
<span class="topo-ruler">       370       380       </span>
<span class="topo-line"><span class="topo-outside">NGGNGLFN</span><span class="topo-membrane">LFNLVNGILWLSLMVI</span><span class="topo-inside">FLK</span></span>
<details class="topo-details"><summary>Topology coordinates (29 regions)</summary>
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
      <td>14</td>
      <td>20</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>24</td>
      <td>21</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>26</td>
      <td>38</td>
      <td>39</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>34</td>
      <td>40</td>
      <td>47</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>35</td>
      <td>42</td>
      <td>48</td>
      <td>55</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>56</td>
      <td>56</td>
      <td>69</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>73</td>
      <td>70</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>89</td>
      <td>87</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>94</td>
      <td>103</td>
      <td>107</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>110</td>
      <td>108</td>
      <td>123</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>131</td>
      <td>124</td>
      <td>144</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>148</td>
      <td>145</td>
      <td>161</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>159</td>
      <td>162</td>
      <td>172</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>176</td>
      <td>173</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>192</td>
      <td>190</td>
      <td>205</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>203</td>
      <td>206</td>
      <td>216</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>204</td>
      <td>210</td>
      <td>217</td>
      <td>223</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>227</td>
      <td>224</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>228</td>
      <td>248</td>
      <td>241</td>
      <td>261</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>265</td>
      <td>262</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>274</td>
      <td>279</td>
      <td>287</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>289</td>
      <td>288</td>
      <td>302</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>290</td>
      <td>305</td>
      <td>303</td>
      <td>318</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>306</td>
      <td>322</td>
      <td>319</td>
      <td>335</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>323</td>
      <td>340</td>
      <td>336</td>
      <td>353</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>355</td>
      <td>354</td>
      <td>368</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>356</td>
      <td>368</td>
      <td>369</td>
      <td>381</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>369</td>
      <td>384</td>
      <td>382</td>
      <td>397</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>385</td>
      <td>387</td>
      <td>398</td>
      <td>400</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Polyspecific multidrug recognition via a large binding pocket

E26T/D34M/A150E uses a large, voluminous substrate-binding pocket (~3000 Å³) to interact with physicochemically disparate drugs. Substrates such as Cm, [DXC](/xray-mp-wiki/reagents/additives/deoxycholate/), and [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) bind in partially overlapping sites using only a small set (typically ≤3) of H-bonding interactions, contrasting with the extensive H-bonding networks of substrate-specific [MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) transporters like LacY. Most interactions are van der Waals and charge-charge in nature, enabling substantial flexibility in substrate recognition.

### Direct-competition-based drug/H+ coupling mechanism

A150E serves as the protonation site in E26T/D34M/A150E. Electroneutral Cm and anionic [DXC](/xray-mp-wiki/reagents/additives/deoxycholate/) trigger deprotonation by forming a direct H-bond with the side-chain carboxylate of A150E. Zwitterionic [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) promotes deprotonation through long-range charge-charge interactions (4.3 Å between [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) N1 and A150E carboxylate). All three substrates induce stoichiometric release of one proton per protein molecule.

### Fully loaded intermediate state captured

A Cm-bound, protonated structure of E26T/D34M/A150E (at pH 5.0) represents a fully loaded intermediate where both substrate and proton are bound simultaneously. This was unexpected since substrate and H+ binding to [MdfA Multidrug Efflux Transporter](/xray-mp-wiki/proteins/mfs-transporters/mdfA/) was believed to be mutually exclusive, suggesting that drug-induced deprotonation involves more intermediate states than previously envisioned.

### Structural changes accompanying deprotonation

Comparison of Cm-bound structures at pH 8.0 (deprotonated) and pH 5.0 (protonated) reveals structural changes in the transporter, particularly in Y30 and the nitryl group of Cm. As the transporter transitions from the low to high pH state, Cm forms a direct H-bond with A150E, and the nitryl group of Cm interacts with the edge of the Y30 aromatic ring. These changes have not been observed in the Q131R [MdfA Multidrug Efflux Transporter](/xray-mp-wiki/proteins/mfs-transporters/mdfA/) variant.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM (n-Dodecyl-β-D-Maltopyranoside)</a> — Primary detergent used for membrane extraction and initial purification
- <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO (Lauryldimethylamine N-oxide)</a> — Co-detergent in SEC buffer and co-crystallization ligand/substrate
- <a href="/xray-mp-wiki/reagents/additives/deoxycholate/">Deoxycholate</a> — Co-detergent/additive in SEC buffer and co-crystallization substrate
- <a href="/xray-mp-wiki/reagents/antibiotics/chloramphenicol/">Chloramphenicol</a> — Primary substrate used for co-crystallization at pH 8.0 and pH 5.0
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Buffer</a> — Used in protein purification and crystallization buffer at pH 8.0
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> — Used in membrane extraction and Ni-NTA purification at pH 7.5
- <a href="/xray-mp-wiki/reagents/buffers/mes/">MES Buffer</a> — Used in crystallization reservoir at pH 6.0
- <a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging-Drop Vapor Diffusion</a> — Crystallization method used for all MdfA structures
- <a href="/xray-mp-wiki/concepts/protein-families/mfs-transporter/">MFS</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
