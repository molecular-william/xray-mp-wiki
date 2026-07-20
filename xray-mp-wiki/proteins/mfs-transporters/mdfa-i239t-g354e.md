---
title: "MdfA Multidrug Transporter I239T/G354E Variant (E. coli)"
created: 2026-06-16
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1038##s42003-019-0446-y]
verified: agent
uniprot_id: P0AEY8
---

# MdfA Multidrug Transporter I239T/G354E Variant (E. coli)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P0AEY8">UniProt: P0AEY8</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

[MdfA Multidrug Efflux Transporter](/xray-mp-wiki/proteins/mfs-transporters/mdfA/) is a prototypical H+-coupled multidrug transporter from E. coli belonging to the Major Facilitator Superfamily ([MFS](/xray-mp-wiki/concepts/protein-families/major-facilitator-superfamily/)). The I239T/G354E variant was engineered with altered substrate specificity, including the ability to export short dicationic compounds like methyl viologen (MV) which wild-type [MdfA Multidrug Efflux Transporter](/xray-mp-wiki/proteins/mfs-transporters/mdfA/) cannot transport. This work presents X-ray crystal structures of I239T/G354E in complexes with three electrically different ligands — [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) (zwitterionic), MV (dicationic), and [DXC](/xray-mp-wiki/reagents/additives/deoxycholate/) (monoanionic) — at resolutions up to 2.2 Å. The structures reveal two discrete, non-overlapping substrate-binding sites (LDAO1 and LDAO2) within the transporter, with D34 and G354E serving as independent protonation sites enabling a drug/H+ stoichiometry of 1:2 or 2:2. The dual drug-binding sites can accommodate one or two drugs of various sizes and shapes, contributing to broad substrate specificity. Long-range electrostatic interactions, enhanced >10-fold by the low-dielectric membrane environment, mediate recognition of zwitterionic and cationic substrates and play a key role in substrate-triggered deprotonation. The study also reveals the mechanistic basis for distinguishing substrates from inhibitors in H+-dependent multidrug transporters.

## Publications

### doi/10.1038##s42003-019-0446-y

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6oom">6OOM</a></td>
      <td>2.2</td>
      <td>C2</td>
      <td>I239T/G354E mutant with C-terminal deca-histidine tag in modified pET28b vector, thrombin-cleaved</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a> (n-dodecyl-n,n-dimethylamine-n-oxide)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6oop">6OOP</a></td>
      <td>2.8</td>
      <td>C2</td>
      <td>I239T/G354E mutant with C-terminal deca-histidine tag</td>
      <td>MV (methyl viologen)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ooq">6OOQ</a></td>
      <td>3.0</td>
      <td>C2</td>
      <td>I239T/G354E mutant with C-terminal deca-histidine tag</td>
      <td><a href="/xray-mp-wiki/reagents/additives/deoxycholate/">DXC</a> (<a href="/xray-mp-wiki/reagents/additives/deoxycholate/">DXC</a>)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) ΔacrABΔmacABΔyojHI
- **Construct**: I239T/G354E variant in modified pET28b with C-terminal deca-histidine tag
- **Notes**: Induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at 30°C for 4 h in LB media

**Purification:**

- **Expression system**: E. coli BL21(DE3) ΔacrABΔmacABΔyojHI
- **Expression construct**: I239T/G354E with C-terminal deca-histidine tag
- **Tag info**: Deca-histidine tag (C-terminal)

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
      <td>1% (w/v) n-dodecyl-β-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Membranes collected by ultracentrifugation and extracted with <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> column</td>
      <td></td>
      <td>Purified by <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td>—</td>
      <td></td>
      <td>Final polishing step</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified I239T/G354E in detergent-containing buffer

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified I239T/G354E</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>24 °C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>All three structures (LDAO-bound, MV-bound, DXC-bound) crystallized in C2 space group. Phase solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> combined with SAD phasing. Data collected at APS beamline 24ID-C. LDAO-bound at pH 8.0 (2.2 Å), MV-bound at pH 8.0 (2.8 Å), DXC-bound at pH 6.0 (3.0 Å).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6oom">6OOM</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">ARLGRQALLFPL</span><span class="topo-membrane">CLVLYEFSTYIGNDMIQP</span><span class="topo-outside">GMLAVVEQYQAGIDWVP</span><span class="topo-membrane">TSMTAYLAGGMFLQWLL</span><span class="topo-inside">GPLSDRIGRRPV</span><span class="topo-membrane">MLAGVVWFIVTCLAILLA</span><span class="topo-outside">QNIE</span><span class="topo-membrane">QFTLLRFLQGISLCFIG</span><span class="topo-inside">AVGYA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">AIQESFEEAVCIKITA</span><span class="topo-membrane">LMANVALIAPLLGPLVG</span><span class="topo-outside">AAWIHVLPWE</span><span class="topo-membrane">GMFVLFAALAAISFFGLQ</span><span class="topo-inside">RAMPETATRIGEKLS</span><span class="topo-unknown">LKELGRDYKLVLK</span><span class="topo-inside">NGRFV</span><span class="topo-membrane">AGALALGFVSLPLLAWTAQS</span><span class="topo-outside">PIIIIT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">GEQLSSYEYG</span><span class="topo-membrane">LLQVPIFGALIAGNLLLAR</span><span class="topo-inside">LTSRRTVRSL</span><span class="topo-membrane">IIMGGWPIMIGLLVAAA</span><span class="topo-outside">ATVISSHAYLW</span><span class="topo-membrane">MTAGLSIYAFGIGLANAGLV</span><span class="topo-inside">RLTLFASDMSKGTVSA</span><span class="topo-membrane">AMEMLQMLIFTVGIEIS</span></span>
<span class="topo-ruler">       370       380       390  </span>
<span class="topo-line"><span class="topo-membrane">K</span><span class="topo-outside">HAWLNGGNGLF</span><span class="topo-membrane">NLFNLVNGILWLSLMVIF</span><span class="topo-inside">LK</span></span>
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
      <td>12</td>
      <td>9</td>
      <td>20</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>30</td>
      <td>21</td>
      <td>38</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>47</td>
      <td>39</td>
      <td>55</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>64</td>
      <td>56</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>76</td>
      <td>73</td>
      <td>84</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>94</td>
      <td>85</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>95</td>
      <td>98</td>
      <td>103</td>
      <td>106</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>115</td>
      <td>107</td>
      <td>123</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>136</td>
      <td>124</td>
      <td>144</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>153</td>
      <td>145</td>
      <td>161</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>154</td>
      <td>163</td>
      <td>162</td>
      <td>171</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>181</td>
      <td>172</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>182</td>
      <td>196</td>
      <td>190</td>
      <td>204</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>197</td>
      <td>209</td>
      <td>205</td>
      <td>217</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>210</td>
      <td>214</td>
      <td>218</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>234</td>
      <td>223</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>250</td>
      <td>243</td>
      <td>258</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>269</td>
      <td>259</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>270</td>
      <td>279</td>
      <td>278</td>
      <td>287</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>296</td>
      <td>288</td>
      <td>304</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>297</td>
      <td>307</td>
      <td>305</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>308</td>
      <td>327</td>
      <td>316</td>
      <td>335</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>328</td>
      <td>343</td>
      <td>336</td>
      <td>351</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>361</td>
      <td>352</td>
      <td>369</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>362</td>
      <td>372</td>
      <td>370</td>
      <td>380</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>373</td>
      <td>390</td>
      <td>381</td>
      <td>398</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>391</td>
      <td>392</td>
      <td>399</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6oop">6OOP</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">ARLGRQALLFPL</span><span class="topo-membrane">CLVLYEFSTYIGNDMIQPGM</span><span class="topo-outside">LAVVEQYQAGIDWVP</span><span class="topo-membrane">TSMTAYLAGGMFLQWLL</span><span class="topo-inside">GPLSDRIGRRPVM</span><span class="topo-membrane">LAGVVWFIVTCLAILLA</span><span class="topo-outside">QNIE</span><span class="topo-membrane">QFTLLRFLQGISLCFIGA</span><span class="topo-inside">VGYA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">AIQESFEEAVCIKITA</span><span class="topo-membrane">LMANVALIAPLLGPLVGAAW</span><span class="topo-outside">IHVL</span><span class="topo-membrane">PWEGMFVLFAALAAISFFG</span><span class="topo-inside">LQRAMPETATRIGEKLS</span><span class="topo-unknown">LKELGRDYKLV</span><span class="topo-membrane">LKNGRFVAGALALGFVSLPLLAWTAQS</span><span class="topo-outside">PIIIIT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">GEQLSSYEYG</span><span class="topo-membrane">LLQVPIFGALIAGNLLLARLT</span><span class="topo-inside">SRR</span><span class="topo-membrane">TVRSLIIMGGWPIMIGLLVA</span><span class="topo-outside">AAATVISSHAYLWMT</span><span class="topo-membrane">AGLSIYAFGIGLANAGLVRLT</span><span class="topo-inside">LFASDMSKGTV</span><span class="topo-membrane">SAAMEMLQMLIFTVGIEIS</span></span>
<span class="topo-ruler">       370       380       390  </span>
<span class="topo-line"><span class="topo-outside">KHAWLNGGNGLFNLF</span><span class="topo-membrane">NLVNGILWLSLMVIFLK</span></span>
<details class="topo-details"><summary>Topology coordinates (25 regions)</summary>
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
      <td>9</td>
      <td>20</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>32</td>
      <td>21</td>
      <td>40</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>47</td>
      <td>41</td>
      <td>55</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>64</td>
      <td>56</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>77</td>
      <td>73</td>
      <td>85</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>94</td>
      <td>86</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>95</td>
      <td>98</td>
      <td>103</td>
      <td>106</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>116</td>
      <td>107</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>117</td>
      <td>136</td>
      <td>125</td>
      <td>144</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>156</td>
      <td>145</td>
      <td>164</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>157</td>
      <td>160</td>
      <td>165</td>
      <td>168</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>179</td>
      <td>169</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>196</td>
      <td>188</td>
      <td>204</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>197</td>
      <td>207</td>
      <td>205</td>
      <td>215</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>208</td>
      <td>234</td>
      <td>216</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>250</td>
      <td>243</td>
      <td>258</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>271</td>
      <td>259</td>
      <td>279</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>274</td>
      <td>280</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>294</td>
      <td>283</td>
      <td>302</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>295</td>
      <td>309</td>
      <td>303</td>
      <td>317</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>330</td>
      <td>318</td>
      <td>338</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>331</td>
      <td>341</td>
      <td>339</td>
      <td>349</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>342</td>
      <td>360</td>
      <td>350</td>
      <td>368</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>361</td>
      <td>375</td>
      <td>369</td>
      <td>383</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>376</td>
      <td>392</td>
      <td>384</td>
      <td>400</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ooq">6OOQ</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">ARLGRQALLFPLCLVL</span><span class="topo-membrane">YEFSTYIGNDMIQ</span><span class="topo-outside">PGMLAVVEQYQAGIDWVP</span><span class="topo-membrane">TSMTAYLAGGMFLQ</span><span class="topo-inside">WLLGPLSDRIGRRPVMLAG</span><span class="topo-membrane">VVWFIVTCLAILLA</span><span class="topo-outside">QNIEQ</span><span class="topo-membrane">FTLLRFLQGISLC</span><span class="topo-inside">FIGAVGYA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">AIQESFEEAVCIKITALMA</span><span class="topo-membrane">NVALIAPLLGPLVGAAW</span><span class="topo-outside">IHVLPWE</span><span class="topo-membrane">GMFVLFAALAAISF</span><span class="topo-inside">FGLQRAMPETATRIGEKLSLKELGRDYKLVLKNGRFV</span><span class="topo-membrane">AGALALGFVSLPLLAWTA</span><span class="topo-outside">QSPIIIIT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">GEQLSSYEYG</span><span class="topo-membrane">LLQVPIFGALIAGNLLL</span><span class="topo-inside">ARLTSRRTVRSL</span><span class="topo-membrane">IIMGGWPIMIGLLVA</span><span class="topo-outside">AAATVISSHAYLWMT</span><span class="topo-membrane">AGLSIYAFGIGLANA</span><span class="topo-inside">GLVRLTLFASDMSKGTVSAAM</span><span class="topo-membrane">EMLQMLIFTVGIEIS</span></span>
<span class="topo-ruler">       370       380       390  </span>
<span class="topo-line"><span class="topo-outside">KHAWLNGGNGLFNL</span><span class="topo-membrane">FNLVNGILWLSLMVI</span><span class="topo-inside">FLK</span></span>
<details class="topo-details"><summary>Topology coordinates (25 regions)</summary>
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
      <td>16</td>
      <td>9</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>29</td>
      <td>25</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>47</td>
      <td>38</td>
      <td>55</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>61</td>
      <td>56</td>
      <td>69</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>80</td>
      <td>70</td>
      <td>88</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>94</td>
      <td>89</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>95</td>
      <td>99</td>
      <td>103</td>
      <td>107</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>100</td>
      <td>112</td>
      <td>108</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>139</td>
      <td>121</td>
      <td>147</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>156</td>
      <td>148</td>
      <td>164</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>157</td>
      <td>163</td>
      <td>165</td>
      <td>171</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>177</td>
      <td>172</td>
      <td>185</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>214</td>
      <td>186</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>232</td>
      <td>223</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>233</td>
      <td>250</td>
      <td>241</td>
      <td>258</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>267</td>
      <td>259</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>268</td>
      <td>279</td>
      <td>276</td>
      <td>287</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>294</td>
      <td>288</td>
      <td>302</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>295</td>
      <td>309</td>
      <td>303</td>
      <td>317</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>324</td>
      <td>318</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>325</td>
      <td>345</td>
      <td>333</td>
      <td>353</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>346</td>
      <td>360</td>
      <td>354</td>
      <td>368</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>361</td>
      <td>374</td>
      <td>369</td>
      <td>382</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>375</td>
      <td>389</td>
      <td>383</td>
      <td>397</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>390</td>
      <td>392</td>
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

### Two discrete non-overlapping substrate-binding sites

The LDAO-bound structure of I239T/G354E reveals two distinct substrate-binding sites (LDAO1 and LDAO2) within the central cavity. LDAO1 is located in the N-domain and interacts primarily with D34; LDAO2 is in the C-domain and interacts with G354E. The two sites are separated by ~20 Å and the transporter can bind and export two [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) molecules simultaneously, with each substrate molecule triggering proton release from its respective protonation site (D34 for LDAO1, G354E for LDAO2).

### D34 and G354E as dual protonation sites

The LDAO-bound I239T/G354E structure reveals that D34 and G354E serve as independent protonation sites. Upon [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) binding, two protons are released (one from each site) — confirmed by fluorescence measurement showing 2.0 ± 0.1 H+ released per I239T/G354E molecule. [MdfA Multidrug Efflux Transporter](/xray-mp-wiki/proteins/mfs-transporters/mdfA/) (lacking G354E) or D34A/I239T/G354E (lacking D34) release only one proton per molecule upon [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) binding, while D34A/I239T (lacking both) fails to release any protons. This establishes a drug/H+ stoichiometry of 1:2 (short dicationic) or 2:2 (two monocationic drugs) for I239T/G354E.

### Long-range electrostatic interactions in multidrug recognition

The study demonstrates that zwitterionic ([LDAO](/xray-mp-wiki/reagents/detergents/ldao/)) and cationic (MV) substrates are recognized by I239T/G354E via long-range charge-charge interactions enhanced >10-fold by the low-dielectric membrane environment. For MV binding, D34 and G354E are 8.3 Å and 5.8 Å from the positively charged N2 of MV, respectively, yet these electrostatic interactions effectively mediate substrate-triggered deprotonation. Unlike H-bonds, these interactions lack stringent geometric requirements, enabling the transporter to accommodate structurally diverse cationic drugs and explaining how additional drug-binding/protonation sites can be introduced into [MdfA Multidrug Efflux Transporter](/xray-mp-wiki/proteins/mfs-transporters/mdfA/).

### Substrate vs. inhibitor distinction in H+-coupled antiporters

Comparison of [DXC](/xray-mp-wiki/reagents/additives/deoxycholate/) binding to [MdfA Multidrug Efflux Transporter](/xray-mp-wiki/proteins/mfs-transporters/mdfA/) (transportable substrate) vs. I239T/G354E (non-transportable inhibitor) reveals the molecular basis for substrate/inhibitor distinction. In [MdfA Multidrug Efflux Transporter](/xray-mp-wiki/proteins/mfs-transporters/mdfA/)/Q131R, D34 forms an H-bond with the C1-OH of [DXC](/xray-mp-wiki/reagents/additives/deoxycholate/) to trigger deprotonation; in I239T/G354E, G354E alters the [DXC](/xray-mp-wiki/reagents/additives/deoxycholate/) binding pose so that no such interaction is made with D34 or G354E, preventing deprotonation. This suggests that potent therapeutics could evade extrusion by H+-coupled antiporters if they lack the ability to trigger deprotonation, e.g., by methylation of key hydroxyl groups.

### Polyspecificity through combined H-bond and electrostatic mechanisms

[MdfA Multidrug Efflux Transporter](/xray-mp-wiki/proteins/mfs-transporters/mdfA/) interacts with electrically distinct substrates differently: H-bonds for electroneutral ([Chloramphenicol](/xray-mp-wiki/reagents/antibiotics/chloramphenicol/)) and anionic ([DXC](/xray-mp-wiki/reagents/additives/deoxycholate/)) substrates; charge-charge interactions for zwitterionic ([LDAO](/xray-mp-wiki/reagents/detergents/ldao/)) and cationic (MV) substrates. Broad substrate specificity arises from the preponderance of non-specific hydrophobic interactions combined with long-range electrostatic interactions, making [MdfA Multidrug Efflux Transporter](/xray-mp-wiki/proteins/mfs-transporters/mdfA/) polyspecific rather than truly nonspecific. Specificity arises when H-bonds select certain drugs and size/shape constraints apply; promiscuity exists because many structurally dissimilar cationic compounds are recognized through flexible electrostatic interactions.


## Cross-References

- <a href="/xray-mp-wiki/proteins/mfs-transporters/mdfa/">MdfA Multidrug Efflux Transporter</a> — Parent/background entity for the I239T/G354E engineered variant
- <a href="/xray-mp-wiki/concepts/protein-families/mfs-transporter/">Major Facilitator Superfamily (MFS)</a> — MdfA belongs to the MFS/DHA1 subfamily
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating Access Mechanism</a> — Relevant transport mechanism for MdfA
- <a href="/xray-mp-wiki/concepts/protein-families/major-facilitator-superfamily/">MFS</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/mfs-transporters/mdfA/">MdfA Multidrug Efflux Transporter</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/deoxycholate/">DXC</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/antibiotics/chloramphenicol/">Chloramphenicol</a> — Antibiotic used in selection
