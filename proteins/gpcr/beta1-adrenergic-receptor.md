---
title: "Turkey Beta1-Adrenergic Receptor (beta1AR)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1100185108, doi/10.1126##science.aau5595]
verified: false
---

# Turkey Beta1-Adrenergic Receptor (beta1AR)

## Overview

The turkey beta1-adrenergic receptor (beta1AR) is a class A G-protein-coupled receptor (GPCR) that mediates physiological effects of catecholamines such as adrenaline and noradrenaline. Crystal structures have been determined for both inactive and active states, including the thermostabilized beta36-M23 construct bound to antagonists and active-state structures bound to agonists in complex with conformation-specific nanobodies. Comparison of inactive and active states bound to the same ligands reveals that the orthosteric binding site contracts by 24-42% upon activation, with shorter hydrogen bonds and up to 30% more atomic contacts between receptor and ligand, explaining the higher agonist affinity of the active state.


## Publications

### doi/10.1073##pnas.1100185108

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2vt4">2VT4</a></td>
      <td>2.7</td>
      <td>—</td>
      <td>beta36-M23 (deletions at N-term, C-term, and CL3; 6 thermostabilizing mutations)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/cyanopindolol/">Cyanopindolol</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Baculovirus expression in Sf9 insect cells
- **Construct**: beta36-M23 (thermostabilized) or wild-type beta1AR for active-state structures
- **Notes**: The beta36 construct has deletions in flexible regions at N and C termini and cytoplasmic loop 3 (CL3). Six thermostabilizing mutations (M23) introduced for tolerance to short-chain detergents.

**Purification:**

- **Expression system**: Sf9 insect cells (baculovirus)
- **Expression construct**: beta1AR36-M23
- **Tag info**: His-tag (Ni2+-affinity)

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
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>beta-decylmaltoside</td>
      <td>Receptor solubilized from membranes</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td>Ni2+-affinity</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/)</td>
      <td></td>
      <td>First purification step</td>
    </tr>
    <tr>
      <td>Ligand affinity chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/alprenolol/">Alprenolol</a> sepharose affinity</td>
      <td>—</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/octylthioglucoside/">OTG</a> (0.35%)</td>
      <td>Detergent exchange to <a href="/xray-mp-wiki/reagents/detergents/octylthioglucoside/">OTG</a> performed on the ligand affinity column. For carazolol-bound crystals, detergent was exchanged to <a href="/xray-mp-wiki/reagents/detergents/hega-10/">HEGA-10</a> (0.35%) and receptor eluted with 50 microM <a href="/xray-mp-wiki/reagents/ligands/carazolol/">Carazolol</a>.</td>
    </tr>
  </tbody>
</table>
**Final sample**: 5.5-9 mg/mL in crystallization buffer

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>5.5 mg/mL (cyanopindolol/iodocyanopindolol) or 9 mg/mL (<a href="/xray-mp-wiki/reagents/ligands/carazolol/">Carazolol</a>)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M N-(2-acetamido)iminodiacetate-NaOH pH 6.9-7.3, 29-33% <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> 600 (<a href="/xray-mp-wiki/reagents/ligands/cyanopindolol/">Cyanopindolol</a>); or 0.1 M <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> pH 8.1, 40% <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> 400 (<a href="/xray-mp-wiki/reagents/ligands/carazolol/">Carazolol</a>)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>293</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>60% <a href="/xray-mp-wiki/reagents/additives/peg-600/">Peg600</a> (t148), 40% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a> (t1118), or 35% <a href="/xray-mp-wiki/reagents/additives/peg-600/">Peg600</a> + 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> (t468). No additional cryoprotectant for t756.</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grew in space groups P21 (<a href="/xray-mp-wiki/reagents/ligands/carazolol/">Carazolol</a>) or C2 (cyanopindolol/iodocyanopindolol). Data collected at ESRF ID23-2 and SLS X06SA.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2vt4">2VT4</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGAELLSQQ</span><span class="topo-inside">W</span><span class="topo-membrane">EAGMSLLMALVVLLIVAGNVLVI</span><span class="topo-outside">AAIGSTQRLQTLTNLFIT</span><span class="topo-membrane">SLACADLVV</span></span>
<span class="topo-line"><span class="topo-membrane">GLLVVPFGATLVV</span><span class="topo-inside">RGTW</span><span class="topo-membrane">LWGSFLCELWTSLDVLCVTASIETLC</span><span class="topo-outside">VIAIDRYLAITSPFRYQ</span></span>
<span class="topo-line"><span class="topo-outside">SLMTRARAKVII</span><span class="topo-membrane">CTVWAISALVSFLPIMMHWWRD</span><span class="topo-inside">ED</span><span class="topo-unknown">PQALKCYQ</span><span class="topo-inside">DPGCC</span><span class="topo-membrane">DFVTNRAYAIA</span></span>
<span class="topo-line"><span class="topo-membrane">SSIISFYIPLLIMIF</span><span class="topo-outside">VALRVYREAKEQI</span><span class="topo-unknown">RKIDRASKRKRVMLM</span><span class="topo-outside">REHKALKTLG</span><span class="topo-membrane">IIMGVFT</span></span>
<span class="topo-line"><span class="topo-membrane">LCWLPFFLVNIVNVFN</span><span class="topo-inside">RDLVPD</span><span class="topo-membrane">WLFVAFNWLGYANSAMNPII</span><span class="topo-outside">YCRS</span><span class="topo-unknown">PDFRKAFKRL</span><span class="topo-outside">LA</span><span class="topo-unknown">FP</span></span>
<span class="topo-line"><span class="topo-unknown">RKADRRLHHHHHH</span></span>
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
      <td>9</td>
      <td>31</td>
      <td>39</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>10</td>
      <td>40</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>33</td>
      <td>41</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>51</td>
      <td>64</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>73</td>
      <td>82</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>74</td>
      <td>77</td>
      <td>104</td>
      <td>107</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>103</td>
      <td>108</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>104</td>
      <td>132</td>
      <td>134</td>
      <td>162</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>154</td>
      <td>163</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>156</td>
      <td>185</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>164</td>
      <td>187</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>165</td>
      <td>169</td>
      <td>195</td>
      <td>199</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>195</td>
      <td>200</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>208</td>
      <td>226</td>
      <td>238</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>209</td>
      <td>223</td>
      <td>239</td>
      <td>253</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>224</td>
      <td>233</td>
      <td>284</td>
      <td>293</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>256</td>
      <td>294</td>
      <td>316</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>257</td>
      <td>262</td>
      <td>317</td>
      <td>322</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>263</td>
      <td>282</td>
      <td>323</td>
      <td>342</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>283</td>
      <td>286</td>
      <td>343</td>
      <td>346</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>296</td>
      <td>347</td>
      <td>356</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>297</td>
      <td>298</td>
      <td>357</td>
      <td>358</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>299</td>
      <td>313</td>
      <td>359</td>
      <td>373</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1126##science.aau5595

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6h7j">6H7J</a></td>
      <td>3.0</td>
      <td>—</td>
      <td>beta1AR with Nb80 or Nb6B9 <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a></td>
      <td><a href="/xray-mp-wiki/reagents/ligands/isoprenaline/">Isoprenaline</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6h7l">6H7L</a></td>
      <td>3.2</td>
      <td>—</td>
      <td>beta1AR with Nb80 or Nb6B9 <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a></td>
      <td><a href="/xray-mp-wiki/reagents/ligands/dobutamine/">Dobutamine</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6h7m">6H7M</a></td>
      <td>3.1</td>
      <td>—</td>
      <td>beta1AR with Nb80 or Nb6B9 <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a></td>
      <td><a href="/xray-mp-wiki/reagents/ligands/salbutamol/">Salbutamol</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6h7o">6H7O</a></td>
      <td>3.0</td>
      <td>—</td>
      <td>beta1AR with Nb80 or Nb6B9 <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a></td>
      <td><a href="/xray-mp-wiki/reagents/ligands/cyanopindolol/">Cyanopindolol</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Baculovirus expression in Sf9 insect cells
- **Construct**: beta36-M23 (thermostabilized) or wild-type beta1AR for active-state structures
- **Notes**: The beta36 construct has deletions in flexible regions at N and C termini and cytoplasmic loop 3 (CL3). Six thermostabilizing mutations (M23) introduced for tolerance to short-chain detergents.

**Purification:**

- **Expression system**: Sf9 insect cells (baculovirus)
- **Expression construct**: beta1AR (wild-type or modified for nanobody complex formation)
- **Tag info**: His-tag

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
      <td>Membrane preparation and solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td></td>
      <td>Standard membrane protein solubilization procedures</td>
    </tr>
    <tr>
      <td>Purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity-chromatography</a> and size-exclusion chromatography</td>
      <td>—</td>
      <td></td>
      <td>Purified in complex with Nb80 or Nb6B9 nanobodies and respective agonist ligands</td>
    </tr>
  </tbody>
</table>
**Final sample**: beta1AR-nanobody-agonist complex for crystallization

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>beta1AR-nanobody-agonist complex</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>293</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Four crystal structures determined with resolutions between 3.0-3.2 A. Data collected at ESRF (beamlines ID23-2, ID30-A3, ID29, ID30B, MASSIF-1) and Diamond Light Source (beamline I24).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6h7j">6H7J</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">SD</span><span class="topo-outside">KIIHLTDDSFDTDVLKADGAILVDFWAEWSGPSKMIAPILDEIADEYQGKLTVAKLNI</span></span>
<span class="topo-line"><span class="topo-outside">DQNPGTAPKYGIRGIPTLLLFKNGEVAATKVGALS</span><span class="topo-unknown">KGQLKEFLDAN</span><span class="topo-outside">LA</span><span class="topo-unknown">E</span></span>
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
      <td>3</td>
      <td>95</td>
      <td>3</td>
      <td>95</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>106</td>
      <td>96</td>
      <td>106</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>107</td>
      <td>108</td>
      <td>107</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6h7j">6H7J</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">A</span><span class="topo-outside">AAKV</span><span class="topo-membrane">MSLLMALVVLLIVAGNVLV</span><span class="topo-inside">IAAIGSTQRLQTLTNLFITS</span><span class="topo-membrane">LACADLVVGLLVVPFG</span></span>
<span class="topo-line"><span class="topo-membrane">AT</span><span class="topo-outside">LVVRGTWLWGSF</span><span class="topo-membrane">LCELWTSLDVLCVTASIETLC</span><span class="topo-inside">VIAIDRYLAITSPFRYQSLMTRARA</span></span>
<span class="topo-line"><span class="topo-inside">KVIIC</span><span class="topo-membrane">TVWAISALVSFLPIMMHWWR</span><span class="topo-outside">DED</span><span class="topo-unknown">PQALKCYQ</span><span class="topo-outside">DPGCCDFVT</span><span class="topo-membrane">NRAYAIASSIISFYI</span></span>
<span class="topo-line"><span class="topo-membrane">PLLIMIF</span><span class="topo-inside">VYLRVYREAKEQIRKIDRASKRKTSRVMAMKEHKALKTLG</span><span class="topo-membrane">IIMGVFTLCWLPF</span></span>
<span class="topo-line"><span class="topo-membrane">FLVNIVNV</span><span class="topo-outside">FNRDLVPDWL</span><span class="topo-membrane">FVAFNWLGYANSAMNPII</span><span class="topo-inside">YCRS</span><span class="topo-unknown">PDFRKAFKRL</span><span class="topo-inside">L</span><span class="topo-unknown">AFPRKADRR</span></span>
<span class="topo-line"><span class="topo-unknown">LHHHHHH</span></span>
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
      <td>40</td>
      <td>43</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>24</td>
      <td>44</td>
      <td>62</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>44</td>
      <td>63</td>
      <td>82</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>62</td>
      <td>83</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>74</td>
      <td>101</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>95</td>
      <td>113</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>96</td>
      <td>125</td>
      <td>134</td>
      <td>163</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>126</td>
      <td>145</td>
      <td>164</td>
      <td>183</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>148</td>
      <td>184</td>
      <td>186</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>156</td>
      <td>187</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>157</td>
      <td>165</td>
      <td>195</td>
      <td>203</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>187</td>
      <td>204</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>188</td>
      <td>227</td>
      <td>226</td>
      <td>293</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>248</td>
      <td>294</td>
      <td>314</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>249</td>
      <td>258</td>
      <td>315</td>
      <td>324</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>276</td>
      <td>325</td>
      <td>342</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>280</td>
      <td>343</td>
      <td>346</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>281</td>
      <td>290</td>
      <td>347</td>
      <td>356</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>291</td>
      <td>291</td>
      <td>357</td>
      <td>357</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6h7l">6H7L</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">SD</span><span class="topo-outside">KIIHLTDDSFDTDVLKADGAILVDFWAEWSGPSKMIAPILDEIADEYQGKLTVAKLNI</span></span>
<span class="topo-line"><span class="topo-outside">DQNPGTAPKYGIRGIPTLLLFKNGEVAATKVGALS</span><span class="topo-unknown">KGQLKEFLDANL</span><span class="topo-outside">AE</span></span>
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
      <td>3</td>
      <td>95</td>
      <td>3</td>
      <td>95</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>107</td>
      <td>96</td>
      <td>107</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>108</td>
      <td>109</td>
      <td>108</td>
      <td>109</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6h7l">6H7L</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">A</span><span class="topo-outside">AAKV</span><span class="topo-membrane">MSLLMALVVLLIVAGNVLVIA</span><span class="topo-inside">AIGSTQRLQTLTNLFI</span><span class="topo-membrane">TSLACADLVVGLLVVPFG</span></span>
<span class="topo-line"><span class="topo-membrane">AT</span><span class="topo-outside">LVVRGTWLWGSF</span><span class="topo-membrane">LCELWTSLDVLCVTASIETLCV</span><span class="topo-inside">IAIDRYLAITSPFRYQSLMTRARA</span></span>
<span class="topo-line"><span class="topo-inside">KVII</span><span class="topo-membrane">CTVWAISALVSFLPIMMHWW</span><span class="topo-outside">RDED</span><span class="topo-unknown">PQALKCYQ</span><span class="topo-outside">DPGCCDFVT</span><span class="topo-membrane">NRAYAIASSIISFYI</span></span>
<span class="topo-line"><span class="topo-membrane">PLLIMIF</span><span class="topo-inside">VYLRVYREAKEQIRKIDRASKRKTSRVMAMKEHKALK</span><span class="topo-membrane">TLGIIMGVFTLCWLPF</span></span>
<span class="topo-line"><span class="topo-membrane">FLVNIV</span><span class="topo-outside">NVFNRDLVPDWLF</span><span class="topo-membrane">VAFNWLGYANSAMNPIIY</span><span class="topo-inside">CRS</span><span class="topo-unknown">PDFRKAFKRL</span><span class="topo-inside">LA</span><span class="topo-unknown">FPRKADRR</span></span>
<span class="topo-line"><span class="topo-unknown">LHHHHHH</span></span>
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
      <td>40</td>
      <td>43</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>26</td>
      <td>44</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>42</td>
      <td>65</td>
      <td>80</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>62</td>
      <td>81</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>74</td>
      <td>101</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>96</td>
      <td>113</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>124</td>
      <td>135</td>
      <td>162</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>144</td>
      <td>163</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>148</td>
      <td>183</td>
      <td>186</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>156</td>
      <td>187</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>157</td>
      <td>165</td>
      <td>195</td>
      <td>203</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>187</td>
      <td>204</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>188</td>
      <td>224</td>
      <td>226</td>
      <td>290</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>225</td>
      <td>246</td>
      <td>291</td>
      <td>312</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>247</td>
      <td>259</td>
      <td>313</td>
      <td>325</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>260</td>
      <td>277</td>
      <td>326</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>278</td>
      <td>280</td>
      <td>344</td>
      <td>346</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>281</td>
      <td>290</td>
      <td>347</td>
      <td>356</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>291</td>
      <td>292</td>
      <td>357</td>
      <td>358</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6h7m">6H7M</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">SD</span><span class="topo-inside">KIIHLTDDSFDTDVLKADGAILVDFWAEWSGPSKMIAPILDEIADEYQGKLTVAKLNI</span></span>
<span class="topo-line"><span class="topo-inside">DQNPGTAPKYGIRGIPTLLLFKNGEVAATKVGALS</span><span class="topo-unknown">KGQLKEFLDANL</span><span class="topo-inside">AE</span></span>
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
      <td>3</td>
      <td>95</td>
      <td>3</td>
      <td>95</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>107</td>
      <td>96</td>
      <td>107</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>108</td>
      <td>109</td>
      <td>108</td>
      <td>109</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6h7m">6H7M</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">A</span><span class="topo-inside">AAKV</span><span class="topo-membrane">MSLLMALVVLLIVAGNVLVI</span><span class="topo-outside">AAIGSTQRLQTLTNLFIT</span><span class="topo-membrane">SLACADLVVGLLVVPFG</span></span>
<span class="topo-line"><span class="topo-membrane">AT</span><span class="topo-inside">LVVRGTWLWGSF</span><span class="topo-membrane">LCELWTSLDVLCVTASIETLCV</span><span class="topo-outside">IAIDRYLAITSPFRYQSLMTRARA</span></span>
<span class="topo-line"><span class="topo-outside">KVII</span><span class="topo-membrane">CTVWAISALVSFLPIMMHWW</span><span class="topo-inside">RDED</span><span class="topo-unknown">PQALKCYQ</span><span class="topo-inside">DPGCCDFVT</span><span class="topo-membrane">NRAYAIASSIISFYI</span></span>
<span class="topo-line"><span class="topo-membrane">PLLIMIF</span><span class="topo-outside">VYLRVYREAKEQIRKIDRASKRKTSRVMAMKEHKALKTL</span><span class="topo-membrane">GIIMGVFTLCWLPF</span></span>
<span class="topo-line"><span class="topo-membrane">FLVNIV</span><span class="topo-inside">NVFNRDLVPDWL</span><span class="topo-membrane">FVAFNWLGYANSAMNPIIY</span><span class="topo-outside">CRS</span><span class="topo-unknown">PDFRKAFKRL</span><span class="topo-outside">LA</span><span class="topo-unknown">FPRKADRR</span></span>
<span class="topo-line"><span class="topo-unknown">LHHHHHH</span></span>
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
      <td>40</td>
      <td>43</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>25</td>
      <td>44</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>43</td>
      <td>64</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>62</td>
      <td>82</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>74</td>
      <td>101</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>96</td>
      <td>113</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>124</td>
      <td>135</td>
      <td>162</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>144</td>
      <td>163</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>148</td>
      <td>183</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>156</td>
      <td>187</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>157</td>
      <td>165</td>
      <td>195</td>
      <td>203</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>187</td>
      <td>204</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>188</td>
      <td>226</td>
      <td>226</td>
      <td>292</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>227</td>
      <td>246</td>
      <td>293</td>
      <td>312</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>247</td>
      <td>258</td>
      <td>313</td>
      <td>324</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>277</td>
      <td>325</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>278</td>
      <td>280</td>
      <td>344</td>
      <td>346</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>281</td>
      <td>290</td>
      <td>347</td>
      <td>356</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>291</td>
      <td>292</td>
      <td>357</td>
      <td>358</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6h7o">6H7O</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">S</span><span class="topo-inside">DKIIHLTDDSFDTDVLKADGAILVDFWAEWSGPSKMIAPILDEIADEYQGKLTVAKLNI</span></span>
<span class="topo-line"><span class="topo-inside">DQNPGTAPKYGIRGIPTLLLFKNGEVAATKVGALS</span><span class="topo-unknown">KGQLKEFLDANL</span><span class="topo-inside">A</span><span class="topo-unknown">E</span></span>
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
      <td>95</td>
      <td>2</td>
      <td>95</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>107</td>
      <td>96</td>
      <td>107</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>108</td>
      <td>108</td>
      <td>108</td>
      <td>108</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6h7o">6H7O</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">A</span><span class="topo-inside">AAKV</span><span class="topo-membrane">MSLLMALVVLLIVAGNVLVI</span><span class="topo-outside">AAIGSTQRLQTLTNLFITS</span><span class="topo-membrane">LACADLVVGLLVVPFG</span></span>
<span class="topo-line"><span class="topo-membrane">AT</span><span class="topo-inside">LVVRGTWLWGSF</span><span class="topo-membrane">LCELWTSLDVLCVTASIETLC</span><span class="topo-outside">VIAIDRYLAITSPFRYQSLMTRARA</span></span>
<span class="topo-line"><span class="topo-outside">KVIIC</span><span class="topo-membrane">TVWAISALVSFLPIMMHWW</span><span class="topo-inside">RDED</span><span class="topo-unknown">PQALKCYQ</span><span class="topo-inside">DPGCCDFVT</span><span class="topo-membrane">NRAYAIASSIISFYI</span></span>
<span class="topo-line"><span class="topo-membrane">PLLIMIF</span><span class="topo-outside">VYLRVYREAKEQIRKIDRASKRKTSRVMAMKEHKALKTLG</span><span class="topo-membrane">IIMGVFTLCWLPF</span></span>
<span class="topo-line"><span class="topo-membrane">FLVNIV</span><span class="topo-inside">NVFNRDLVPDWL</span><span class="topo-membrane">FVAFNWLGYANSAMNPII</span><span class="topo-outside">YCRS</span><span class="topo-unknown">PDFRKAFKRL</span><span class="topo-outside">L</span><span class="topo-unknown">AFPRKADRR</span></span>
<span class="topo-line"><span class="topo-unknown">LHHHHHH</span></span>
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
      <td>40</td>
      <td>43</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>25</td>
      <td>44</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>44</td>
      <td>64</td>
      <td>82</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>62</td>
      <td>83</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>74</td>
      <td>101</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>95</td>
      <td>113</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>96</td>
      <td>125</td>
      <td>134</td>
      <td>163</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>126</td>
      <td>144</td>
      <td>164</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>148</td>
      <td>183</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>156</td>
      <td>187</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>157</td>
      <td>165</td>
      <td>195</td>
      <td>203</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>187</td>
      <td>204</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>188</td>
      <td>227</td>
      <td>226</td>
      <td>293</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>246</td>
      <td>294</td>
      <td>312</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>247</td>
      <td>258</td>
      <td>313</td>
      <td>324</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>276</td>
      <td>325</td>
      <td>342</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>280</td>
      <td>343</td>
      <td>346</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>281</td>
      <td>290</td>
      <td>347</td>
      <td>356</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>291</td>
      <td>291</td>
      <td>357</td>
      <td>357</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Two conformations of helix 6 in beta1AR

Eight new structures of beta1AR-M23 from four different crystals with three different antagonists reveal only two distinct conformations of the cytoplasmic end of helix 6: bent and straight. In the bent conformation, the Arg139-Glu285 salt bridge (ionic lock) is present, similar to dark-state rhodopsin. In the straight conformation, the ends of helices 3 and 6 are too far apart for the ionic lock to form.

### Ionic lock distance correlates with basal activity

In the bent conformation, the R3.50-E6.30 distance is 3.7-3.9 A, significantly longer than in rhodopsin (2.8-3.2 A), suggesting a weaker interaction that could explain the higher basal activity of beta1AR compared to rhodopsin.

### HKAL sequence as conformational switch

The His286-Lys287-Ala288-Leu289 (HKAL) sequence at the cytoplasmic end of H6 acts as a conformational switch. The bent conformation shows a marked kink at Ala288/Lys287, while the straight conformation has an extended helix. Mutations in this region are associated with constitutive activity in various GPCRs and human diseases.

### Orthosteric binding site contraction upon activation

Comparison of inactive and active state structures of beta1AR bound to the identical ligands ([Isoprenaline](/xray-mp-wiki/reagents/ligands/isoprenaline/), [Salbutamol](/xray-mp-wiki/reagents/ligands/salbutamol/), [Dobutamine](/xray-mp-wiki/reagents/ligands/dobutamine/), [Cyanopindolol](/xray-mp-wiki/reagents/ligands/cyanopindolol/)) reveals that the orthosteric binding site volume decreases by 24-42% upon activation. Potential hydrogen bonds become shorter, and there is up to a 30% increase in the number of atomic contacts between receptor and ligand. These changes explain the increase in agonist affinity of GPCRs in the active state.

### Partial occlusion of the orthosteric binding pocket entrance

In beta2AR, Tyr308(7.35) makes van der Waals contact with Phe193(ECL2) to occlude the binding pocket entrance. In beta1AR, the equivalent residues are Phe201(ECL2) and Phe325(7.35), which are not in van der Waals contact. The F325Y mutation in beta1AR slows the rate of ligand association, but does not significantly affect agonist affinity for the high-affinity state, suggesting that occlusion of the binding pocket entrance is not the primary determinant of increased agonist affinity in the active state.

### Active state of beta1AR is virtually identical to agonist-bound beta2AR active state

The overall structure of the beta1AR-nanobody complexes bound to agonists is virtually identical to the agonist-bound Nb6B9-beta2AR complex (0.5 A RMSD of 1601 atoms). This suggests a conserved mechanism of activation across related GPCRs.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/beta2-adrenergic-receptor/">Human Beta2-Adrenergic Receptor (beta2 AR)</a> — Close structural homolog for comparison of GPCR active and inactive states
- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr-active-state-high-affinity-agonist-binding/">GPCR Active State High-Affinity Agonist Binding</a> — Concept explaining the structural basis for increased agonist affinity in the active state
- <a href="/xray-mp-wiki/reagents/ligands/cyanopindolol/">Cyanopindolol</a> — Referenced in the context of Cyanopindolol
- <a href="/xray-mp-wiki/reagents/ligands/carazolol/">Carazolol</a> — Referenced in the context of Carazolol
- <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> — Referenced in the context of Nanobody
- <a href="/xray-mp-wiki/reagents/ligands/isoprenaline/">Isoprenaline</a> — Referenced in the context of Isoprenaline
- <a href="/xray-mp-wiki/reagents/ligands/dobutamine/">Dobutamine</a> — Referenced in the context of Dobutamine
- <a href="/xray-mp-wiki/reagents/ligands/salbutamol/">Salbutamol</a> — Referenced in the context of Salbutamol
- <a href="/xray-mp-wiki/reagents/ligands/alprenolol/">Alprenolol</a> — Referenced in the context of Alprenolol
- <a href="/xray-mp-wiki/reagents/detergents/octylthioglucoside/">OTG</a> — Referenced in the context of OTG
