---
title: "BasC (Bacterial Alanine-Serine-Cysteine Exchanger)"
created: 2026-06-09
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-019-09837-z]
verified: false
---

# BasC (Bacterial Alanine-Serine-Cysteine Exchanger)

## Overview

BasC is a bacterial L-amino acid transporter (LAT) from the alanine-serine-cysteine exchanger family, a prokaryotic homolog of human heteromeric amino acid transporters (HATs). LATs are obligatory exchangers with asymmetric substrate affinity (high extracellular, low intracellular), a key feature enabling regulation of intracellular amino acid pools. Crystal structures of BasC in complex with nanobody 74 (Nb74) were determined in both apo and substrate (2-aminoisobutyric acid, 2-AIB) bound forms at 2.9 and 3.4 A resolution, respectively, revealing a non-occluded inward-facing conformation. Two conserved residues, Tyr236 (TM7) and Lys154 (TM5), are responsible for the asymmetric substrate interaction. This work fills a gap in the knowledge of the transport cycle of APC superfamily transporters and provides a structural framework for understanding human LATs.

## Publications

### doi/10.1038##s41467-019-09837-z

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6f2g">6F2G</a></td>
      <td>2.9</td>
      <td>C2</td>
      <td>BasC-Nb74 complex (apo)</td>
      <td>None (apo)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6f2w">6F2W</a></td>
      <td>3.4</td>
      <td>Not specified</td>
      <td>BasC-Nb74 complex (2-AIB bound)</td>
      <td>2-aminoisobutyric acid (2-AIB)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21-CodonPlus-RIPL
- **Construct**: Full-length BasC from unclassified Enterococcus species with N-terminal His10-GFP-TEV tag

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
      <td>Membrane preparation</td>
      <td>Cell lysis by <a href="/xray-mp-wiki/methods/cell-lysis/french-press/">French press</a>, <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">ultracentrifugation</a></td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a>-Base, 150 mM NaCl, pH 7.4, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a></td>
      <td>Membrane pellet resuspended at 8-12 mg/mL protein, flash-frozen and stored at -80 C</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a>-Base, 150 mM NaCl, pH 7.4, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a> + 2% (w/v) n-decyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>)</td>
      <td>1 h solubilization at 4 C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Immobilized metal-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA Superflow</a> beads</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a>-Base, 150 mM NaCl, pH 7.4, 0.17% DM, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 20 mM <a href="/xray-mp-wiki/reagents/buffers/imidazole/">imidazole</a></td>
      <td>On-column cleavage with HRV-3C protease for 16 h. Cleaved BasC collected in flow-through.</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> incubation and <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">size-exclusion chromatography</a></td>
      <td>Gel filtration</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Superdex 200</a> 10/300 GL</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a>-Base, 150 mM NaCl, pH 7.4, 0.17% DM</td>
      <td>BasC incubated with <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">nanobody</a> Nb74 at 1:1.2 molar ratio overnight before <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a>. For 2-AIB-bound protein, all buffers contained 100 mM 2-AIB.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>BasC-Nb74 complex in <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> at ~6 mg/mL</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> pH 6.0-6.5, 200 mM NaCl, 30% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 5000 MME (apo); 100 mM Na <a href="/xray-mp-wiki/reagents/buffers/citrate/">citrate</a> pH 5.5-5.6, 200 mM (NH4)2SO4, 20-25% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG 4000</a> (holo)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td><a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine</a>-labeled protein used for experimental phasing. Apo crystals diffracted to 2.9 A (space group C2), 2-AIB-bound crystals to 3.4 A.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6f2g">6F2G</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MKE</span><span class="topo-outside">VSGI</span><span class="topo-membrane">TALTVVVGTVIGAGIFFKPTAVY</span><span class="topo-inside">GAAGAPG</span><span class="topo-membrane">LGLLAWFVAGIITIAGGLTV</span><span class="topo-outside">AEI</span></span>
<span class="topo-line"><span class="topo-outside">GTIYPQTGGMMIYLEKVYGRWLGF</span><span class="topo-membrane">LVGWAQMVIYYPANIAALAIIFATQF</span><span class="topo-inside">VNLFALSDST</span></span>
<span class="topo-line"><span class="topo-inside">I</span><span class="topo-membrane">VPTAILTSIFLMGVNFLGT</span><span class="topo-outside">K</span><span class="topo-membrane">YSGWIQTLATILKLIPLVVIIVAGLL</span><span class="topo-inside">YPGGGVIRLVPFS</span></span>
<span class="topo-line"><span class="topo-inside">VETHPV</span><span class="topo-membrane">LTSFGSALIATLFAYDGWINV</span><span class="topo-outside">GTLAGEMKNPGKMLP</span><span class="topo-membrane">KVIIGGLSIVMAVYLLTN</span></span>
<span class="topo-line"><span class="topo-membrane">IAY</span><span class="topo-inside">LFVLDSSQLAGTDT</span><span class="topo-unknown">PAALVASHL</span><span class="topo-inside">FEGIG</span><span class="topo-membrane">SKLVTIGILISVFGGINGYIISGLRVPY</span><span class="topo-outside">A</span></span>
<span class="topo-line"><span class="topo-outside">LATQKMLPFSDWFARINPKTNL</span><span class="topo-membrane">PINGGLVMLGIAIVMILTG</span><span class="topo-inside">Q</span><span class="topo-membrane">FNQLTDLIVFVIWFFITL</span></span>
<span class="topo-line"><span class="topo-membrane">TFI</span><span class="topo-outside">AVIILRKTQPDIERPYRVPFYP</span><span class="topo-membrane">VIPLIAIIGGLYIIFNTLIVQP</span><span class="topo-inside">K</span><span class="topo-membrane">NAFIGILLTLIG</span></span>
<span class="topo-line"><span class="topo-membrane">IPIY</span><span class="topo-outside">FYCKKKYGS</span><span class="topo-unknown">PEGGGLEVLFQ</span></span>
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
      <td>4</td>
      <td>7</td>
      <td>4</td>
      <td>7</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>30</td>
      <td>8</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>37</td>
      <td>31</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>57</td>
      <td>38</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>58</td>
      <td>84</td>
      <td>58</td>
      <td>84</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>110</td>
      <td>85</td>
      <td>110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>121</td>
      <td>111</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>140</td>
      <td>122</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>141</td>
      <td>141</td>
      <td>141</td>
      <td>141</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>167</td>
      <td>142</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>168</td>
      <td>186</td>
      <td>168</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>187</td>
      <td>207</td>
      <td>187</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>222</td>
      <td>208</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>243</td>
      <td>223</td>
      <td>243</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>257</td>
      <td>244</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>266</td>
      <td>258</td>
      <td>266</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>267</td>
      <td>271</td>
      <td>267</td>
      <td>271</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>272</td>
      <td>299</td>
      <td>272</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>322</td>
      <td>300</td>
      <td>322</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>341</td>
      <td>323</td>
      <td>341</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>342</td>
      <td>342</td>
      <td>342</td>
      <td>342</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>363</td>
      <td>343</td>
      <td>363</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>385</td>
      <td>364</td>
      <td>385</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>386</td>
      <td>407</td>
      <td>386</td>
      <td>407</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>408</td>
      <td>408</td>
      <td>408</td>
      <td>408</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>409</td>
      <td>424</td>
      <td>409</td>
      <td>424</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>425</td>
      <td>433</td>
      <td>425</td>
      <td>433</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6f2w">6F2W</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">MKEVSGITALT</span><span class="topo-membrane">VVVGTVIGAGIFFKP</span><span class="topo-unknown">TAVYGAA</span><span class="topo-inside">GAPG</span><span class="topo-membrane">LGLLAWFVAGIITIAGG</span><span class="topo-outside">LTVAEI</span></span>
<span class="topo-line"><span class="topo-outside">GTIYPQTGGMMI</span><span class="topo-unknown">YLEKVY</span><span class="topo-outside">GRWLGFL</span><span class="topo-membrane">VGWAQMVIYYPANIAALAIIFATQF</span><span class="topo-inside">VNLFALSDST</span></span>
<span class="topo-line"><span class="topo-inside">I</span><span class="topo-membrane">VPTAILTSIFLMGVNFL</span><span class="topo-outside">GTKY</span><span class="topo-membrane">SGWIQTLATILKLIPLVVIIVAGLL</span><span class="topo-inside">YPGGGVIRLVPFS</span></span>
<span class="topo-line"><span class="topo-inside">VETHPVL</span><span class="topo-membrane">TSFGSALIATLFAYDGWIN</span><span class="topo-outside">VGTLAGEMKNPGKMLPKVI</span><span class="topo-membrane">IGGLSIVMAVYLLTN</span></span>
<span class="topo-line"><span class="topo-membrane">IAY</span><span class="topo-inside">LFVLD</span><span class="topo-unknown">SSQLAG</span><span class="topo-inside">TDT</span><span class="topo-unknown">PAALVASHL</span><span class="topo-inside">FEGI</span><span class="topo-membrane">GSKLVTIGILISVFGGINGYIISGL</span><span class="topo-outside">RVPYA</span></span>
<span class="topo-line"><span class="topo-outside">LATQKMLPFSDWFARINPKTNLPI</span><span class="topo-membrane">NGGLVMLGIAIVMILTG</span><span class="topo-inside">Q</span><span class="topo-membrane">FNQLTDLIVFVIWFFITL</span></span>
<span class="topo-line"><span class="topo-membrane">TFI</span><span class="topo-outside">AVIILRKTQPDIERPYRVPFYPV</span><span class="topo-membrane">IPLIAIIGGLYIIFNTLIVQP</span><span class="topo-inside">K</span><span class="topo-membrane">NAFIGILLTLIG</span></span>
<span class="topo-line"><span class="topo-membrane">IPIY</span><span class="topo-outside">FYCKKKYGS</span><span class="topo-unknown">PEGGGLEVLFQ</span></span>
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
      <td>1</td>
      <td>11</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>26</td>
      <td>12</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>33</td>
      <td>27</td>
      <td>33</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>34</td>
      <td>37</td>
      <td>34</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>38</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>72</td>
      <td>55</td>
      <td>72</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>78</td>
      <td>73</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>85</td>
      <td>79</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>110</td>
      <td>86</td>
      <td>110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>121</td>
      <td>111</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>138</td>
      <td>122</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>142</td>
      <td>139</td>
      <td>142</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>167</td>
      <td>143</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>168</td>
      <td>187</td>
      <td>168</td>
      <td>187</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>188</td>
      <td>206</td>
      <td>188</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>225</td>
      <td>207</td>
      <td>225</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>243</td>
      <td>226</td>
      <td>243</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>248</td>
      <td>244</td>
      <td>248</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>254</td>
      <td>249</td>
      <td>254</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>255</td>
      <td>257</td>
      <td>255</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>266</td>
      <td>258</td>
      <td>266</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>267</td>
      <td>270</td>
      <td>267</td>
      <td>270</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>271</td>
      <td>295</td>
      <td>271</td>
      <td>295</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>296</td>
      <td>324</td>
      <td>296</td>
      <td>324</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>325</td>
      <td>341</td>
      <td>325</td>
      <td>341</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>342</td>
      <td>342</td>
      <td>342</td>
      <td>342</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>363</td>
      <td>343</td>
      <td>363</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>386</td>
      <td>364</td>
      <td>386</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>387</td>
      <td>407</td>
      <td>387</td>
      <td>407</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>408</td>
      <td>408</td>
      <td>408</td>
      <td>408</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>409</td>
      <td>424</td>
      <td>409</td>
      <td>424</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>425</td>
      <td>433</td>
      <td>425</td>
      <td>433</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Nb74 reveals sidedness of substrate interaction

Nanobody 74 binds exclusively to the cytoplasmic side of BasC, blocking efflux but not influx of L-alanine. By inhibiting inside-out oriented BasC in proteoliposomes, Nb74 enables kinetic characterization of the extracellular side alone, revealing high apparent affinity (Km ~50 uM) versus low intracellular affinity (Km ~2 mM).

### Substrate binding site in unwound TM1 and TM6

2-AIB binds at the unwound segments of TM1 and TM6. The alpha-carboxyl forms H-bonds with backbone N-atoms of Ala20 and Gly21 (TM1). The alpha-amino group bonds with carbonyls of Val17 (TM1) and Phe199, Ala200, Asp202 (TM6). The alpha-amino and alpha-carboxyl groups are essential substrate requirements, as demonstrated by inability to exchange with acetate or ethylamine.

### Substrate-induced fit mechanism

Upon 2-AIB binding, Gly19 (TM1 unwound region) shifts by 2 A to form an H-bond with Ser282 (TM8). MD simulations show that substrate dissociation is accompanied by relaxation of the TM1 unwound segment, supporting a substrate-induced fit mechanism.

### Tyr236 partially mediates substrate asymmetry

Tyr236 (TM7) is positioned at the Na1 site equivalent of sodium-dependent APC transporters. Mutation Y236F in BasC (and homologous Y280F in human Asc-1) selectively increases the cytoplasmic apparent affinity (Km(i) from ~2 mM to ~560 uM), making the transporter more symmetric without affecting extracellular affinity or Vmax.

### Lys154 supports high extracellular affinity

Lys154 (TM5) at the Na2 site equivalent interacts with Gly15 (TM1a C-terminus). Mutation K154A reduces extracellular affinity ~10-fold (to ~474 uM) and dramatically reduces Vmax (~1/20 of WT), while leaving intracellular affinity unchanged. This turns BasC into a more symmetric transporter with mM-range affinity on both sides. The homologous K194A mutation in human Asc-1 produces similar effects.

### Substrate release to cytoplasm

MD simulations show 2-AIB can dissociate from the binding site and interact simultaneously with the epsilon-amino group of Lys154 and the backbone carbonyl of Thr16 (TM1a), suggesting a pathway for substrate release to the cytoplasm.

### Comparison with GkApcT reveals occlusion mechanism

Comparison of BasC (non-occluded inward-facing) with GkApcT (occluded inward-facing) shows that tilting of TM1a and TM6b, together with accompanying TM7 movement, closes the substrate vestibule at the cytoplasmic side. TM1a-TM5 interaction is key for the occlusion process.

### Structural framework for human LATs

BasC provides the first atomic-resolution structure of a LAT family transporter. The low sequence identity (14-22%) between bacterial APC transporters and human LATs limits model reliability. BasC fills this gap, enabling structure-function analysis of human LATs, including mutations causing autism (LAT1), hearing loss (LAT2), and lysinuric protein intolerance (y+LAT1 K191E corresponds to BasC K154E).


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — BasC is an obligatory exchanger using alternating access for amino acid transport
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> — Primary buffer component throughout purification
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Used in Ni-NTA affinity chromatography
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Ni-NTA IMAC used for initial purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — SEC used as final polishing step and for nanobody complex formation
- <a href="/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/">Single-Wavelength Anomalous Diffraction (SAD)</a> — Apo structure solved by Se-Met SAD phasing
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Holo structure solved by MR using apo model
- <a href="/xray-mp-wiki/methods/cell-lysis/french-press/">French Press</a> — Used for cell lysis in BasC purification
- <a href="/xray-mp-wiki/proteins/slc-transporters/adic/">AdiC</a> — Distant bacterial APC superfamily homolog, used for structural comparison
- <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine</a> — SeMet-labeled protein used for SAD phasing
