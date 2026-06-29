---
title: "Human Complement C5a Receptor 1 (C5aR1)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature25025, doi/10.1038##s41594-018-0067-z]
verified: false
---

# Human Complement C5a Receptor 1 (C5aR1)

## Overview

The human complement C5a receptor 1 (C5aR1, also known as CD88) is a class A G protein-coupled receptor that mediates the pro-inflammatory effects of the anaphylatoxin C5a. It is expressed on cells of myeloid origin and plays a critical role in the complement cascade. C5aR1 has been implicated in inflammatory disorders including sepsis, arthritis, and Alzheimer's disease. Crystal structures of C5aR1 in complex with peptide and non-peptide antagonists revealed both orthosteric and allosteric binding mechanisms, providing a structural framework for drug development.


## Publications

### doi/10.1038##nature25025

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5o9h">5O9H</a></td>
      <td>2.7</td>
      <td>P12_11</td>
      <td>C5aR1 StaR (residues 30-333), thermostabilized with 11 mutations (S85A, I91A, I142A, N146R, L156A, F172A, R232A, A234E, L311E, S317E, N321E), N-terminal 29 residues deleted, C-terminal 17 residues deleted</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/ndt9513727/">NDT9513727</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda Sf9 cells using pFastBac baculovirus method
- **Construct**: [BRIL (Thermostabilized Apocytochrome b562RIL)](/xray-mp-wiki/reagents/protein-tags/bril/)-C5aR chimera with N-terminal signal peptide plus [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), TEV cleavage site, C-terminal 8xHis tag
- **Notes**: Ligand ([NDT9513727](/xray-mp-wiki/reagents/ligands/ndt9513727/) or avacopan) added at 100 [NM](/xray-mp-wiki/reagents/detergents/nm/) to cell media during expression

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
      <td>Expression</td>
      <td>Transient transfection of HEK293T cells</td>
      <td></td>
      <td></td>
      <td>cDNA encoding human C5aR1 or C5aR1 StaR construct; cells collected after 48 h</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Homogenization and ultracentrifugation</td>
      <td></td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.4, 1 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a></td>
      <td>Homogenized 30 s at max speed, centrifuged at 48,000g for 30 min at 4 C</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td></td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a>-NaOH pH 7.5, 150 mM NaCl, 1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Incubated at 4 C for 1 h; cleared by centrifugation at 16,000g for 15 min</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (LCP)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>C5aR1 StaR with <a href="/xray-mp-wiki/reagents/ligands/ndt9513727/">NDT9513727</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Two-syringe mixing method; <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> used as lipid; 11 crystals used for data collection</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5o9h">5O9H</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">NTLRVPDIL</span><span class="topo-membrane">ALVIFAVVFLVGVLGNALVVWVTA</span><span class="topo-outside">FEAKRTINAI</span><span class="topo-membrane">WFLNLAVADFLACLAL</span></span>
<span class="topo-line"><span class="topo-membrane">PALF</span><span class="topo-inside">TSIVQHHHWPFGGA</span><span class="topo-membrane">ACSILPSLILLNMYASILLLATIS</span><span class="topo-outside">ADRFLLVFKPAWCQRFRG</span></span>
<span class="topo-line"><span class="topo-outside">AGLAW</span><span class="topo-membrane">ILCAVAWGLALLLTIPSALYR</span><span class="topo-inside">VVREEYFPPKVLCGVD</span><span class="topo-unknown">YS</span><span class="topo-inside">HDKRR</span><span class="topo-membrane">ERAVAIVRLVL</span></span>
<span class="topo-line"><span class="topo-membrane">GFLWPLLTLTIC</span><span class="topo-outside">YTFILLRTWSARETRSTKTLKV</span><span class="topo-membrane">VVAVVASFFIFWLPYQVTGIM</span><span class="topo-inside">MSFLE</span></span>
<span class="topo-line"><span class="topo-inside">PSS</span><span class="topo-unknown">PTFLLLKK</span><span class="topo-inside">L</span><span class="topo-membrane">DSLCVSFAYINCCINPIIYVVA</span><span class="topo-outside">GQGFQ</span><span class="topo-unknown">GRER</span><span class="topo-outside">KS</span><span class="topo-unknown">LPELLREVL</span><span class="topo-outside">TEESVV</span></span>
<span class="topo-line"><span class="topo-outside">R</span><span class="topo-unknown">ESKAAAHHHHHHHHHH</span></span>
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
      <td>10</td>
      <td>31</td>
      <td>39</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>34</td>
      <td>40</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>44</td>
      <td>64</td>
      <td>73</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>64</td>
      <td>74</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>78</td>
      <td>94</td>
      <td>107</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>102</td>
      <td>108</td>
      <td>131</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>125</td>
      <td>132</td>
      <td>154</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>126</td>
      <td>146</td>
      <td>155</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>147</td>
      <td>162</td>
      <td>176</td>
      <td>191</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>165</td>
      <td>169</td>
      <td>194</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>192</td>
      <td>199</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>193</td>
      <td>214</td>
      <td>222</td>
      <td>243</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>235</td>
      <td>244</td>
      <td>264</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>236</td>
      <td>243</td>
      <td>265</td>
      <td>272</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>251</td>
      <td>273</td>
      <td>280</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>252</td>
      <td>252</td>
      <td>281</td>
      <td>281</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>253</td>
      <td>274</td>
      <td>282</td>
      <td>303</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>279</td>
      <td>304</td>
      <td>308</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>285</td>
      <td>313</td>
      <td>314</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>294</td>
      <td>315</td>
      <td>323</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>295</td>
      <td>301</td>
      <td>324</td>
      <td>330</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5o9h">5O9H</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">NTLR</span><span class="topo-membrane">VPDILALVIFAVVFLVGVLGNAL</span><span class="topo-outside">VVWVTAFEAKRTINAIWFLN</span><span class="topo-membrane">LAVADFLACLAL</span></span>
<span class="topo-line"><span class="topo-membrane">PALFTSIV</span><span class="topo-inside">QHHHWPF</span><span class="topo-membrane">GGAACSILPSLILLNMYASILLLA</span><span class="topo-outside">TISADRFLLVFKPAWCQRFRG</span></span>
<span class="topo-line"><span class="topo-outside">AGLAWILC</span><span class="topo-membrane">AVAWGLALLLTIPSALYRV</span><span class="topo-inside">VREEYFPPKVLCGVDYSHDKR</span><span class="topo-membrane">RERAVAIVRLVL</span></span>
<span class="topo-line"><span class="topo-membrane">GFLWPLLTLT</span><span class="topo-outside">ICYTFILLRTWSARETRSTKTLKVVVAV</span><span class="topo-membrane">VASFFIFWLPYQVTGIMMSFL</span><span class="topo-inside">E</span></span>
<span class="topo-line"><span class="topo-inside">PSSPTFLL</span><span class="topo-membrane">LKKLDSLCVSFAYINCCINPII</span><span class="topo-outside">YVVAGQ</span><span class="topo-unknown">GFQGRE</span><span class="topo-outside">RKS</span><span class="topo-unknown">LPELLREVL</span><span class="topo-outside">TEESVV</span></span>
<span class="topo-line"><span class="topo-outside">RE</span><span class="topo-unknown">SKAAAHHHHHHHHHH</span></span>
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
      <td>5</td>
      <td>31</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>28</td>
      <td>35</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>48</td>
      <td>58</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>68</td>
      <td>78</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>75</td>
      <td>98</td>
      <td>104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>76</td>
      <td>99</td>
      <td>105</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>100</td>
      <td>128</td>
      <td>129</td>
      <td>157</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>147</td>
      <td>158</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>168</td>
      <td>177</td>
      <td>197</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>169</td>
      <td>190</td>
      <td>198</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>218</td>
      <td>220</td>
      <td>247</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>219</td>
      <td>239</td>
      <td>248</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>240</td>
      <td>248</td>
      <td>269</td>
      <td>277</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>270</td>
      <td>278</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>271</td>
      <td>276</td>
      <td>300</td>
      <td>305</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>285</td>
      <td>312</td>
      <td>314</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>294</td>
      <td>315</td>
      <td>323</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>295</td>
      <td>302</td>
      <td>324</td>
      <td>331</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1038##s41594-018-0067-z

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6c1q">6C1Q</a></td>
      <td>2.9</td>
      <td>P2_1</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL (Thermostabilized Apocytochrome b562RIL)</a>-C5aR chimera (N-terminal <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL (Thermostabilized Apocytochrome b562RIL)</a> fusion replacing residues 1-29), TEV cleavage site after R330, C-terminal 8xHis tag</td>
      <td>PMX53, <a href="/xray-mp-wiki/reagents/ligands/ndt9513727/">NDT9513727</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6c1r">6C1R</a></td>
      <td>2.2</td>
      <td>P2_1</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL (Thermostabilized Apocytochrome b562RIL)</a>-C5aR chimera (N-terminal <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL (Thermostabilized Apocytochrome b562RIL)</a> fusion replacing residues 1-29), TEV cleavage site after R330, C-terminal 8xHis tag</td>
      <td>PMX53, avacopan</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda Sf9 cells using pFastBac baculovirus method
- **Construct**: [BRIL (Thermostabilized Apocytochrome b562RIL)](/xray-mp-wiki/reagents/protein-tags/bril/)-C5aR chimera with N-terminal signal peptide plus [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), TEV cleavage site, C-terminal 8xHis tag
- **Notes**: Ligand ([NDT9513727](/xray-mp-wiki/reagents/ligands/ndt9513727/) or avacopan) added at 100 [NM](/xray-mp-wiki/reagents/detergents/nm/) to cell media during expression

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
      <td>Osmotic shock</td>
      <td></td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> pH 7.5, 150 ug/ml <a href="/xray-mp-wiki/reagents/ligands/benzamidine/">Benzamidine</a>, 0.2 ug/ml leupeptin, 2 mg/ml <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a></td>
      <td>Sf9 cells lysed by osmotic shock; membrane fractions collected at 25,000g for 30 min at 4 C</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td></td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> pH 7.8, 750 mM NaCl, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 150 ug/ml <a href="/xray-mp-wiki/reagents/ligands/benzamidine/">Benzamidine</a>, 0.2 ug/ml leupeptin, 2 mg/ml <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a>, 5 U Salt Active Nuclease + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.2% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 0.2% cholate</td>
      <td>2 h at 4 C; all steps in presence of 100 <a href="/xray-mp-wiki/reagents/detergents/nm/">NM</a> <a href="/xray-mp-wiki/reagents/ligands/ndt9513727/">NDT9513727</a> (or avacopan) and 100 <a href="/xray-mp-wiki/reagents/detergents/nm/">NM</a> PMX53</td>
    </tr>
    <tr>
      <td>Affinity chromatography (Ni-NTA)</td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA Agarose Resin</a> agarose</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> pH 7.5, 500 mM NaCl, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 150 ug/ml <a href="/xray-mp-wiki/reagents/ligands/benzamidine/">Benzamidine</a>, 0.2 ug/ml leupeptin, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Batch binding for 2 h at 4 C; washed three times</td>
    </tr>
    <tr>
      <td>Affinity chromatography (anti-Flag M1)</td>
      <td>Anti-<a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> M1 <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Anti-<a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> M1 antibody resin (homemade)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> pH 7.5, 100 mM NaCl, 0.01% MNG, 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 200 ug/ml <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> peptide, 5 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> + 0.01% MNG, 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Detergent exchanged from <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> to MNG on the M1 resin; eluted with <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> peptide and <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a></td>
    </tr>
    <tr>
      <td>TEV cleavage</td>
      <td>Overnight <a href="/xray-mp-wiki/reagents/enzymes/tev-protease/">TEV</a> protease digestion</td>
      <td></td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> pH 7.5, 100 mM NaCl, 0.01% MNG, 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> + 0.01% MNG, 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td><a href="/xray-mp-wiki/reagents/enzymes/tev-protease/">TEV</a> protease (homemade); 4 C overnight</td>
    </tr>
    <tr>
      <td>Size exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> Increase (GE Healthcare)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> pH 7.5, 100 mM NaCl, 0.01% MNG, 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> + 0.01% MNG, 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Monodisperse receptor obtained; concentrated to 40-50 mg/ml with ligands at 10 uM each</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic mesophase (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL (Thermostabilized Apocytochrome b562RIL)</a>-C5aR with PMX53 and <a href="/xray-mp-wiki/reagents/ligands/ndt9513727/">NDT9513727</a> (or avacopan)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Protein mixed with <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a>; crystals grown in lipidic mesophase</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6c1q">6C1Q</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">DYKDDDDVDA</span><span class="topo-inside">DLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDA</span><span class="topo-unknown">QKATPPKLEDK</span></span>
<span class="topo-line"><span class="topo-unknown">SPD</span><span class="topo-inside">SPEMKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKY</span><span class="topo-unknown">LSN</span><span class="topo-inside">TLR</span></span>
<span class="topo-line"><span class="topo-inside">V</span><span class="topo-membrane">PDILALVIFAVVFLVGVLGNALVVWVTA</span><span class="topo-outside">FEAKRTINAI</span><span class="topo-membrane">WFLNLAVADFLSCLALPILFT</span></span>
<span class="topo-line"><span class="topo-membrane">SIV</span><span class="topo-inside">QHHHWPFGG</span><span class="topo-membrane">AACSILPSLILLNMYASILLLATISA</span><span class="topo-outside">DRFLLVFKPIWCQNFRGAGLAW</span></span>
<span class="topo-line"><span class="topo-membrane">IACAVAWGLALLLTIPSFLYR</span><span class="topo-inside">VVREEYFPPKVLCGVDYSHDKR</span><span class="topo-membrane">RERAVAIVRLVLGFLWP</span></span>
<span class="topo-line"><span class="topo-membrane">LLTLTICYT</span><span class="topo-outside">FILLRTWSR</span><span class="topo-unknown">RATR</span><span class="topo-outside">STKTLK</span><span class="topo-membrane">VVVAVVASFFIFWLPYQVTGIMMSF</span><span class="topo-inside">LEPSS</span><span class="topo-unknown">PT</span></span>
<span class="topo-line"><span class="topo-unknown">FLLLKKL</span><span class="topo-membrane">DSLCVSFAYINCCINPIIYVVAGQ</span><span class="topo-outside">GFQ</span><span class="topo-unknown">GRLRK</span><span class="topo-outside">S</span><span class="topo-unknown">LPSLLRNV</span><span class="topo-outside">LT</span><span class="topo-unknown">EESVVRENLY</span></span>
<span class="topo-line"><span class="topo-unknown">FQ</span></span>
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
      <td>11</td>
      <td>49</td>
      <td>11</td>
      <td>49</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>114</td>
      <td>64</td>
      <td>114</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>121</td>
      <td>118</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>149</td>
      <td>122</td>
      <td>149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>159</td>
      <td>150</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>183</td>
      <td>160</td>
      <td>183</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>184</td>
      <td>192</td>
      <td>184</td>
      <td>192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>218</td>
      <td>193</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>240</td>
      <td>219</td>
      <td>240</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>241</td>
      <td>261</td>
      <td>241</td>
      <td>261</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>283</td>
      <td>262</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>309</td>
      <td>284</td>
      <td>309</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>310</td>
      <td>318</td>
      <td>310</td>
      <td>318</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>328</td>
      <td>323</td>
      <td>328</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>329</td>
      <td>353</td>
      <td>329</td>
      <td>353</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>354</td>
      <td>358</td>
      <td>354</td>
      <td>358</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>359</td>
      <td>367</td>
      <td>359</td>
      <td>367</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>368</td>
      <td>391</td>
      <td>368</td>
      <td>391</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>392</td>
      <td>394</td>
      <td>392</td>
      <td>394</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>400</td>
      <td>400</td>
      <td>400</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>401</td>
      <td>408</td>
      <td>401</td>
      <td>408</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>409</td>
      <td>410</td>
      <td>409</td>
      <td>410</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6c1r">6C1R</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">DYKDDDDVDAD</span><span class="topo-outside">LEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDA</span><span class="topo-unknown">QKATPPKLEDK</span></span>
<span class="topo-line"><span class="topo-unknown">SPDSPEM</span><span class="topo-outside">KDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAY</span><span class="topo-unknown">IQKYL</span><span class="topo-outside">SNTLR</span></span>
<span class="topo-line"><span class="topo-outside">V</span><span class="topo-membrane">PDILALVIFAVVFLVGVLGNALVVWV</span><span class="topo-inside">TAFEAKRTINAIW</span><span class="topo-membrane">FLNLAVADFLSCLALPILFT</span></span>
<span class="topo-line"><span class="topo-membrane">SIV</span><span class="topo-outside">QHHHWPF</span><span class="topo-membrane">GGAACSILPSLILLNMYASILLLATIS</span><span class="topo-inside">ADRFLLVFKPIWCQNFRGAGLAW</span></span>
<span class="topo-line"><span class="topo-inside">I</span><span class="topo-membrane">ACAVAWGLALLLTIPSFLYRV</span><span class="topo-outside">VREEYFPPKVLCGVDYSHDK</span><span class="topo-membrane">RRERAVAIVRLVLGFLWP</span></span>
<span class="topo-line"><span class="topo-membrane">LLTLTICYT</span><span class="topo-inside">FILLRTWSRR</span><span class="topo-unknown">ATR</span><span class="topo-inside">STKTLKV</span><span class="topo-membrane">VVAVVASFFIFWLPYQVTGIMMSFL</span><span class="topo-outside">EPSS</span><span class="topo-unknown">PT</span></span>
<span class="topo-line"><span class="topo-unknown">FLLLKK</span><span class="topo-outside">L</span><span class="topo-membrane">DSLCVSFAYINCCINPIIYVVA</span><span class="topo-inside">GQGF</span><span class="topo-unknown">QGRLR</span><span class="topo-inside">KS</span><span class="topo-unknown">LPSLLRNVL</span><span class="topo-inside">TEES</span><span class="topo-unknown">VVRENLY</span></span>
<span class="topo-line"><span class="topo-unknown">FQ</span></span>
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
      <td>12</td>
      <td>49</td>
      <td>12</td>
      <td>49</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>110</td>
      <td>68</td>
      <td>110</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>121</td>
      <td>116</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>147</td>
      <td>122</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>160</td>
      <td>148</td>
      <td>160</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>183</td>
      <td>161</td>
      <td>183</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>184</td>
      <td>190</td>
      <td>184</td>
      <td>190</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>217</td>
      <td>191</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>241</td>
      <td>218</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>262</td>
      <td>242</td>
      <td>262</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>263</td>
      <td>282</td>
      <td>263</td>
      <td>282</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>309</td>
      <td>283</td>
      <td>309</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>310</td>
      <td>319</td>
      <td>310</td>
      <td>319</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>329</td>
      <td>323</td>
      <td>329</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>330</td>
      <td>354</td>
      <td>330</td>
      <td>354</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>355</td>
      <td>358</td>
      <td>355</td>
      <td>358</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>359</td>
      <td>366</td>
      <td>359</td>
      <td>366</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>367</td>
      <td>367</td>
      <td>367</td>
      <td>367</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>389</td>
      <td>368</td>
      <td>389</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>390</td>
      <td>393</td>
      <td>390</td>
      <td>393</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>399</td>
      <td>400</td>
      <td>399</td>
      <td>400</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>401</td>
      <td>409</td>
      <td>401</td>
      <td>409</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>410</td>
      <td>413</td>
      <td>410</td>
      <td>413</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Extra-helical allosteric binding mechanism of NDT9513727

[NDT9513727](/xray-mp-wiki/reagents/ligands/ndt9513727/) binds between transmembrane helices 3, 4, and 5 in an extra-helical pocket within the lipid bilayer. The extended benzodioxolane packs against TM4, the 2-phenyl group interacts between TM3 and TM5 involving Ile124(3.40), Ala128(3.44), and Pro214(5.50), and the [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) core hydrogen bonds to Trp213(5.49). This Trp213 interaction is key for species selectivity.

### Orthosteric binding of PMX53 to C5aR

The cyclic hexapeptide PMX53 binds in the orthosteric site of C5aR, occupying the central binding pocket with its tryptophan residue accommodated by a hydrophobic cage formed by F44(1.39), L92(2.60), I96(2.64), P113(3.29), I116(3.32), and V286(7.39). Polar interactions are mediated by R175(4.64), R178, C188, Y258(6.51), T261(6.54), and D282(7.35), along with ordered water molecules. PMX53 stabilizes the inactive conformation by restraining the I116(3.32) and V286(7.39) activation switch.

### Allosteric action of non-peptide C5aR antagonists

Avacopan and [NDT9513727](/xray-mp-wiki/reagents/ligands/ndt9513727/) bind to the same allosteric site between TM3, TM4, TM5, and TM6, but with different binding poses. Both antagonists form hydrophobic interactions with a conserved 'core triad' of I124(3.40), P214(5.50), and F251(6.44), stabilizing the inactive state of the receptor. Docking studies suggest that other non-peptide antagonists (W54011, CP-447697) also bind to this allosteric site. The hydrogen bond interaction with W213(5.49) is critical for antagonist activity.

### Unique conformation of helix 8

C5aR features a unique reversed orientation of helix 8 that inserts between the cytoplasmic segments of TM1 and TM7, with its C-terminal end pointing to the center of the cytoplasmic surface. This conformation may provide minimal steric hindrance for G protein binding but could sterically block arrestin recruitment, providing a structural basis for the minimal involvement of arrestins in C5aR signaling.

### Water-mediated polar networks in C5aR

An extensive water-mediated polar network exists in the orthosteric site, mediating PMX53 binding. On the cytoplasmic side, a polar network involving ordered water molecules and conserved residues (N55(1.50), D82(2.50), N119(3.35), S123(3.39), W255(6.48), N292(7.45), N296(7.49), Y300(7.53) in the NPxxY motif) helps stabilize the inactive state. A sodium ion coordinated by D82(2.50), N292(7.45), and water molecules was also assigned.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Detergent used for membrane solubilization
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> — Buffer used in purification and crystallization
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> — Buffer used in cell lysis
- <a href="/xray-mp-wiki/reagents/detergents/lmng/">Lauryl Maltose Neopentyl Glycol (LMNG)</a> — Detergent used in final purification steps after exchange from DDM
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — LCP method used for C5aR crystallization
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Final purification step using Superdex 200 Increase
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Ni-NTA and anti-Flag M1 affinity steps used in purification
- <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Baculovirus Expression System in Sf9 Cells</a> — Expression system used for BRIL-C5aR production
- <a href="/xray-mp-wiki/proteins/rhodopsins/gr/">GR (Halobacterium sp. GR Bacteriorhodopsin)</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/cys-loop-receptors/elic/">ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel)</a> — Related protein structure
