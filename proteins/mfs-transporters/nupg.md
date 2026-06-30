---
title: "NupG Nucleoside Proton Symporter from Escherichia coli"
created: 2026-05-27
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jbc.2021.100479, doi/10.1016##j.jbc.2025.108357]
verified: false
---

# NupG Nucleoside Proton Symporter from Escherichia coli

## Overview

NupG is a nucleoside proton symporter from [Escherichia coli](/xray-mp-wiki/proteins/escherichia-coli-aqpz/) belonging to the nucleoside proton symporter (NHS) family within the [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/protein-families/mfs-transporter/). It mediates the transport of nucleosides across the bacterial inner membrane via a proton-coupled mechanism. The first crystal structure of an NHS transporter was solved in this work, revealing an inward-open conformation with 12 transmembrane helices.

## Publications

### doi/10.1016##j.jbc.2021.100479

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7dl9">7DL9</a></td>
      <td>3.0</td>
      <td>P21</td>
      <td>Full-length NupG from E. coli K12, wild-type</td>
      <td>none (apo state)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7dl9">7DL9</a></td>
      <td>3.0</td>
      <td>P1</td>
      <td>Full-length NupG from E. coli K12, D323A mutant</td>
      <td>none (apo state, no visible uridine)</td>
    </tr>
  </tbody>
</table>

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
      <td>Cell lysis and membrane preparation</td>
      <td>Cell lysis and membrane fractionation</td>
      <td>—</td>
      <td>25 mM MES pH 6.0, 150 mM NaCl + 2% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Membranes incubated 2 h with 2% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> at 4°C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> affinity resin (Qiagen)</td>
      <td>25 mM MES pH 6.0, 150 mM NaCl, 20-250 mM imidazole + 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (wash), 0.4% NG (elution)</td>
      <td>Eluted with 250 mM imidazole in 0.4% NG</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/300 Increase (GE Healthcare)</td>
      <td>25 mM MES pH 6.0, 150 mM NaCl + 0.4% NG</td>
      <td>Peak fractions concentrated to 30 mg/ml for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>, in meso)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>WT NupG at 30 mg/ml, mixed with monoolein at 1:1.5 (w/w)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>P21 crystal form, diffraction to 3.8 Å, solved by molecular replacement</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>, in meso)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>NupG D323A at 30 mg/ml, mixed with monoolein at 1:1.5 (w/w)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>P1 crystal form, two molecules in asymmetric unit, solved at 3.0 Å</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7dl9">7DL9</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MNLKLQLK</span><span class="topo-membrane">ILSFLQFCLWGSWLTTLG</span><span class="topo-outside">SYMFVTLKFDGA</span><span class="topo-membrane">SIGAVYSSLGIAAVFM</span><span class="topo-inside">PALLGIVADKWLSAKWV</span><span class="topo-membrane">YAICHTIGAITLFMAAQV</span><span class="topo-outside">TTP</span><span class="topo-membrane">EAMFLVILINSFAYMPTL</span><span class="topo-inside">GLINTISYYR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LQNAGMDIVTDFPPIR</span><span class="topo-membrane">IWGTIGFIMAMWVVSLS</span><span class="topo-outside">GFELSH</span><span class="topo-membrane">MQLYIGAALSAILVLFTLT</span><span class="topo-inside">LPHIPVAKQQANQSWTTLLGLD</span><span class="topo-unknown">AFALFK</span><span class="topo-inside">NKRMAI</span><span class="topo-membrane">FFIFSMLLGAELQITNMFGN</span><span class="topo-outside">TFLHSFDK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">DPMFASSFIVQHA</span><span class="topo-membrane">SIIMSISQISETLFILTI</span><span class="topo-unknown">PFFLSRY</span><span class="topo-inside">GIK</span><span class="topo-membrane">NVMMISIVAWILRFALF</span><span class="topo-outside">AYGDPTPFGTV</span><span class="topo-membrane">LLVLSMIVYGCAFDFFNISG</span><span class="topo-inside">SVFVEKEVSPAIRASAQGMF</span><span class="topo-membrane">LMMTNGFGCIL</span></span>
<span class="topo-ruler">       370       380       390       400       410        </span>
<span class="topo-line"><span class="topo-membrane">GGIVSGKV</span><span class="topo-outside">VEMYTQNGITDWQTVW</span><span class="topo-membrane">LIFAGYSVVLAFAFMAMFK</span><span class="topo-inside">YK</span><span class="topo-unknown">HVRVPTGTQTVSH</span></span>
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
      <td>8</td>
      <td>1</td>
      <td>8</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>26</td>
      <td>9</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>38</td>
      <td>27</td>
      <td>38</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>54</td>
      <td>39</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>71</td>
      <td>55</td>
      <td>71</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>89</td>
      <td>72</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>92</td>
      <td>90</td>
      <td>92</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>110</td>
      <td>93</td>
      <td>110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>136</td>
      <td>111</td>
      <td>136</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>153</td>
      <td>137</td>
      <td>153</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>154</td>
      <td>159</td>
      <td>154</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>178</td>
      <td>160</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>200</td>
      <td>179</td>
      <td>200</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>201</td>
      <td>206</td>
      <td>201</td>
      <td>206</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>207</td>
      <td>212</td>
      <td>207</td>
      <td>212</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>213</td>
      <td>232</td>
      <td>213</td>
      <td>232</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>233</td>
      <td>253</td>
      <td>233</td>
      <td>253</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>254</td>
      <td>271</td>
      <td>254</td>
      <td>271</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>278</td>
      <td>272</td>
      <td>278</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>279</td>
      <td>281</td>
      <td>279</td>
      <td>281</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>298</td>
      <td>282</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>309</td>
      <td>299</td>
      <td>309</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>329</td>
      <td>310</td>
      <td>329</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>330</td>
      <td>349</td>
      <td>330</td>
      <td>349</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>350</td>
      <td>368</td>
      <td>350</td>
      <td>368</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>369</td>
      <td>384</td>
      <td>369</td>
      <td>384</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>385</td>
      <td>403</td>
      <td>385</td>
      <td>403</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>404</td>
      <td>405</td>
      <td>404</td>
      <td>405</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7dl9">7DL9</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MNLKLQLK</span><span class="topo-membrane">ILSFLQFCLWGSWLTTLG</span><span class="topo-outside">SYMFVTLKFDGA</span><span class="topo-membrane">SIGAVYSSLGIAAVFM</span><span class="topo-inside">PALLGIVADKWLSAKWV</span><span class="topo-membrane">YAICHTIGAITLFMAAQV</span><span class="topo-outside">TTP</span><span class="topo-membrane">EAMFLVILINSFAYMPTL</span><span class="topo-inside">GLINTISYYR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LQNAGMDIVTDFPPIR</span><span class="topo-membrane">IWGTIGFIMAMWVVSLS</span><span class="topo-outside">GFELSH</span><span class="topo-membrane">MQLYIGAALSAILVLFTLT</span><span class="topo-inside">LPHIPVAKQQANQSWTTLLGLD</span><span class="topo-unknown">AFALFK</span><span class="topo-inside">NKRMAI</span><span class="topo-membrane">FFIFSMLLGAELQITNMFGN</span><span class="topo-outside">TFLHSFDK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">DPMFASSFIVQHA</span><span class="topo-membrane">SIIMSISQISETLFILTI</span><span class="topo-unknown">PFFLSRY</span><span class="topo-inside">GIK</span><span class="topo-membrane">NVMMISIVAWILRFALF</span><span class="topo-outside">AYGDPTPFGTV</span><span class="topo-membrane">LLVLSMIVYGCAFDFFNISG</span><span class="topo-inside">SVFVEKEVSPAIRASAQGMF</span><span class="topo-membrane">LMMTNGFGCIL</span></span>
<span class="topo-ruler">       370       380       390       400       410        </span>
<span class="topo-line"><span class="topo-membrane">GGIVSGKV</span><span class="topo-outside">VEMYTQNGITDWQTVW</span><span class="topo-membrane">LIFAGYSVVLAFAFMAMFK</span><span class="topo-inside">YK</span><span class="topo-unknown">HVRVPTGTQTVSH</span></span>
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
      <td>8</td>
      <td>1</td>
      <td>8</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>26</td>
      <td>9</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>38</td>
      <td>27</td>
      <td>38</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>54</td>
      <td>39</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>71</td>
      <td>55</td>
      <td>71</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>89</td>
      <td>72</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>92</td>
      <td>90</td>
      <td>92</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>110</td>
      <td>93</td>
      <td>110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>136</td>
      <td>111</td>
      <td>136</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>153</td>
      <td>137</td>
      <td>153</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>154</td>
      <td>159</td>
      <td>154</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>178</td>
      <td>160</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>200</td>
      <td>179</td>
      <td>200</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>201</td>
      <td>206</td>
      <td>201</td>
      <td>206</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>207</td>
      <td>212</td>
      <td>207</td>
      <td>212</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>213</td>
      <td>232</td>
      <td>213</td>
      <td>232</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>233</td>
      <td>253</td>
      <td>233</td>
      <td>253</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>254</td>
      <td>271</td>
      <td>254</td>
      <td>271</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>278</td>
      <td>272</td>
      <td>278</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>279</td>
      <td>281</td>
      <td>279</td>
      <td>281</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>298</td>
      <td>282</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>309</td>
      <td>299</td>
      <td>309</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>329</td>
      <td>310</td>
      <td>329</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>330</td>
      <td>349</td>
      <td>330</td>
      <td>349</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>350</td>
      <td>368</td>
      <td>350</td>
      <td>368</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>369</td>
      <td>384</td>
      <td>369</td>
      <td>384</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>385</td>
      <td>403</td>
      <td>385</td>
      <td>403</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>404</td>
      <td>405</td>
      <td>404</td>
      <td>405</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1016##j.jbc.2025.108357

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8zoj">8ZOJ</a></td>
      <td>3.1</td>
      <td>unknown</td>
      <td>YegT K267A mutant from E. coli</td>
      <td>none (apo state)</td>
    </tr>
  </tbody>
</table>


## Biological / Functional Insights

### Uridine binding site residues

The uridine binding site is constituted by R136, T140, F143, Q225, N228, Q261, E264, Y318, and F322. Mutagenesis showed N228A and E264A reduced binding while F143A, F322A abolished binding.

### D323A mutation enhances uridine binding

The D323A mutant bound uridine with Kd 9.67 ± 2.87 µM, a 20-fold increase over WT (Kd 199.67 ± 15.01 µM). D323 does not directly contact uridine but is important for proton coupling.

### Substrate selectivity profile

NupG binds nucleosides: guanosine (Kd 46.67 µM) > adenosine (Kd 99.67 µM) > cytidine (Kd 143.67 µM) > thymidine (Kd 162.5 µM) > uridine (Kd 199.67 µM).

### Inward-open conformation of NHS transporter

Both WT and D323A NupG structures reveal identical inward-open conformations, consistent with MFS alternating-access mechanism.

### Proton-coupled substrate release mechanism via GXXXD motif

Asp323 in NupG (or Asp315 in YegT) serves as the protonation site within a conserved GXXXD motif in TM10. Deprotonation triggers local conformational changes including TM10 helix destabilization and TM8 outward shift, facilitating substrate release. MD simulations showed proton transfer from Asp323 to Glu264 reduces substrate binding affinity.

### Structural conservation between YegT and NupG

Despite only 27% sequence identity, YegT and NupG share high structural conservation (RMSD 1.57 Å over 316 Cα atoms). The GXXXD motif and protonation sites are fully conserved, suggesting a shared proton-coupled release mechanism.


## Cross-References

- <a href="/xray-mp-wiki/concepts/protein-families/mfs-transporter/">Major Facilitator Superfamily (MFS)</a> — NupG belongs to the MFS family, specifically the NHS family
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — Core transport mechanism shared by MFS transporters
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/rocker-switch-mechanism/">Rocker-Switch Mechanism</a> — MFS-specific variant of alternating access mechanism
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — NupG and YegT both crystallized by [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) method with monoolein
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent for membrane solubilization of NupG
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Primary lipid component of [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) crystallization matrix
- <a href="/xray-mp-wiki/reagents/buffers/mes/">2-(N-Morpholino)ethanesulfonic Acid (MES)</a> — Buffer used throughout NupG purification at pH 6.0
- <a href="/xray-mp-wiki/proteins/mfs-transporters/yegt/">YegT Nucleoside Proton Symporter</a> — Paralogs sharing the same NHS family and proton-coupled mechanism
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> — Immobilized metal affinity chromatography resin
- <a href="/xray-mp-wiki/reagents/additives/superdex-200">Superdex 200 Increase SEC Resin</a> — Size-exclusion chromatography resin
