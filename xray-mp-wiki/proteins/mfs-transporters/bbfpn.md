---
title: "BbFPN — Putative Bacterial Ferroportin Homologue from Bdellovibrio bacteriovorus"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms9545]
verified: agent
uniprot_id: Q6MLJ0
---

# BbFPN — Putative Bacterial Ferroportin Homologue from Bdellovibrio bacteriovorus

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q6MLJ0">UniProt: Q6MLJ0</a>

<span class="expr-badge">Bdellovibrio bacteriovorus</span>

## Overview

BbFPN is a putative bacterial homologue of ferroportin (FPN/SLC40A1) from Bdellovibrio bacteriovorus (formerly Bd2019). It is a divalent transition-metal cation transporter selective for Fe2+, Co2+, Mn2+, and Ni2+, and functions as a uniporter. Despite undetectable sequence similarity, BbFPN adopts the major facilitator superfamily (MFS) fold with 12 transmembrane helices divided into N-lobe (TM1-TM6) and C-lobe (TM7-TM12). Crystal structures were determined in both outward-facing (2.2 Å) and inward-facing (3.3 Å) conformations, capturing two extreme states of the MFS transport cycle. BbFPN serves as a structural model for understanding ferroportin-mediated [Iron](/xray-mp-wiki/reagents/additives/iron/) export and hepcidin-mediated regulation in humans.


## Publications

### doi/10.1038##ncomms9545

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5ayn">5AYN</a></td>
      <td>2.2 A</td>
      <td>P2,2,2,1</td>
      <td>BbFPNΔC (C-terminal 8 residues deleted), full-length BbFPN residues</td>
      <td>K+ (outward-facing state)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5aym">5AYM</a></td>
      <td>3.0 A</td>
      <td>P2,2,2,1</td>
      <td>BbFPNΔC, Fe2+-soaked outward-facing state</td>
      <td>Fe2+ (anomalous scattering)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5ayo">5AYO</a></td>
      <td>3.3 A</td>
      <td>P2,2,2,1</td>
      <td>BbFPNΔC (C-terminal 8 residues deleted)</td>
      <td>none (inward-facing state)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length BbFPN (Bd2019) and BbFPNΔC (C-terminal 8 residues deleted for crystallization)

**Purification:**

- **Expression system**: E. coli
- **Expression construct**: BbFPN with affinity tag (protocol A and protocol B)

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
      <td>Purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a> (protocol A and protocol B)</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.0, 500 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.004% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> (protocol B final buffer) + 0.004% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> (protocol B)</td>
      <td>Two purification protocols used (A and B); protocol A for Hg-derivatized crystals, protocol B for form I and form II crystals</td>
    </tr>
  </tbody>
</table>
**Final sample**: 2.5-2.9 mg/ml in 20 mM Tris pH 8.0, 500 mM NaCl, 10% glycerol, 0.004% LMNG

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic Cubic Phase (LCP)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified BbFPNΔC in 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.0, 500 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.004% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a></td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>monoolein</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>2:3 (wt/wt)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Three crystal forms obtained. Hg-derivative/Fe2+-soaked crystals (Form I-like): 100 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.5, 50-200 mM K-formate, 50-100 mM (NH4)2HPO4, 26-32% PEG550MME. Hg-derivative: 1 mM CH3HgCl, 2.5 h soak. Fe2+-soaked: 5 mM FeSO4, 12 h soak. Form I: 100 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.5, 100 mM NaK-tartrate, 100 mM KNO3, 30% PEG550MME. Form II: 100 mM Na-acetate pH 4.0, 200-300 mM K-formate, 10 mM ZnSO4, 10-20 mM ZnCl2, 27-30% PEG550MME.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ayn">5AYN</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKVQSL</span><span class="topo-inside">LRIETQL</span><span class="topo-membrane">LLGRLLTRSGDQAWDFVVPFAL</span><span class="topo-outside">LVIFPGKLQVA</span><span class="topo-membrane">AFYYLIVKIGTFLLTPSSG</span><span class="topo-inside">KWIDTHPRIQV</span><span class="topo-membrane">VKWGVWLQFFAILAGMVFFGML</span><span class="topo-outside">DGLVRAGGRESWLLS</span><span class="topo-membrane">VLFIALA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LSGVMASLGSQITDISVG</span><span class="topo-inside">NDLAPSLVAPEKLTHFN</span><span class="topo-membrane">SWLRRIDLATEVGAPILAGALF</span><span class="topo-unknown">AFHPEQL</span><span class="topo-outside">PL</span><span class="topo-membrane">AGLFLIGLWNLVSFVPEYFL</span><span class="topo-inside">LRNVIQRSGLKIKVLTEA</span><span class="topo-unknown">QSWKDTFH</span><span class="topo-inside">INLRGSFS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">DPIF</span><span class="topo-membrane">WLILSYALLWLSVLSPHGVLLA</span><span class="topo-outside">AYLKDEMRLPETEI</span><span class="topo-membrane">GLFRGLGAVFGLISTVSFPYL</span><span class="topo-inside">VRRLGLISS</span><span class="topo-membrane">SRWHLGFQGVTLGIAVTAFAM</span><span class="topo-outside">GSTAS</span><span class="topo-membrane">VYVFLGCILLSRVGLYGFSNGEF</span><span class="topo-inside">E</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440</span>
<span class="topo-line"><span class="topo-inside">LRQRLIPEGRRGELN</span><span class="topo-membrane">SLSSLTTTSATLILFSAGSLL</span><span class="topo-outside">PQTEDF</span><span class="topo-membrane">KYLVYVSLAAVLLANVVFIK</span><span class="topo-inside">WSSR</span><span class="topo-unknown">QGVVTSGSENLYFQ</span></span>
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
      <td>7</td>
      <td>13</td>
      <td>7</td>
      <td>13</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>35</td>
      <td>14</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>46</td>
      <td>36</td>
      <td>46</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>65</td>
      <td>47</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>76</td>
      <td>66</td>
      <td>76</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>98</td>
      <td>77</td>
      <td>98</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>99</td>
      <td>113</td>
      <td>99</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>138</td>
      <td>114</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>155</td>
      <td>139</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>156</td>
      <td>177</td>
      <td>156</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>185</td>
      <td>186</td>
      <td>185</td>
      <td>186</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>187</td>
      <td>206</td>
      <td>187</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>224</td>
      <td>207</td>
      <td>224</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>233</td>
      <td>244</td>
      <td>233</td>
      <td>244</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>245</td>
      <td>266</td>
      <td>245</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>280</td>
      <td>267</td>
      <td>280</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>281</td>
      <td>301</td>
      <td>281</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>302</td>
      <td>310</td>
      <td>302</td>
      <td>310</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>331</td>
      <td>311</td>
      <td>331</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>332</td>
      <td>336</td>
      <td>332</td>
      <td>336</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>337</td>
      <td>359</td>
      <td>337</td>
      <td>359</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>360</td>
      <td>375</td>
      <td>360</td>
      <td>375</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>376</td>
      <td>396</td>
      <td>376</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>402</td>
      <td>397</td>
      <td>402</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>403</td>
      <td>422</td>
      <td>403</td>
      <td>422</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>423</td>
      <td>426</td>
      <td>423</td>
      <td>426</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5aym">5AYM</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKVQSL</span><span class="topo-outside">LRIETQLL</span><span class="topo-membrane">LGRLLTRSGDQAWDFVV</span><span class="topo-inside">PFALLVIFPGKLQVAAFY</span><span class="topo-membrane">YLIVKIGTFLLTPSSG</span><span class="topo-outside">KWIDTHPRIQVVKW</span><span class="topo-membrane">GVWLQFFAILAGMVFF</span><span class="topo-inside">GMLDGLVRAGGRESWLLSV</span><span class="topo-membrane">LFIALA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LSGVMASLGSQITDI</span><span class="topo-outside">SVGNDLAPSLVAPEKLTHFN</span><span class="topo-membrane">SWLRRIDLATEVGAPILA</span><span class="topo-inside">GALF</span><span class="topo-unknown">AFHPEQL</span><span class="topo-inside">PLAGL</span><span class="topo-membrane">FLIGLWNLVSFVPEY</span><span class="topo-outside">FLLRNVIQRSGLKIKVL</span><span class="topo-unknown">TEAQSWKDTFHINLR</span><span class="topo-outside">GSFS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">DPIF</span><span class="topo-membrane">WLILSYALLWLSVLSPH</span><span class="topo-inside">GVLLAAYLKDEMRLPETEIGLFRG</span><span class="topo-membrane">LGAVFGLISTVSFPYL</span><span class="topo-outside">VRRLGLIS</span><span class="topo-membrane">SSRWHLGFQGVTLGI</span><span class="topo-inside">AVTAFAMGSTASVYVFLGC</span><span class="topo-membrane">ILLSRVGLYGFSNGEF</span><span class="topo-outside">E</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440</span>
<span class="topo-line"><span class="topo-outside">LRQRLIPEGRRGELN</span><span class="topo-membrane">SLSSLTTTSATLILFS</span><span class="topo-inside">AGSLLPQTEDFKYLVYV</span><span class="topo-membrane">SLAAVLLANVVFIKW</span><span class="topo-outside">SSR</span><span class="topo-unknown">QGVVTSGSENLYFQ</span></span>
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
      <td>7</td>
      <td>14</td>
      <td>7</td>
      <td>14</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>31</td>
      <td>15</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>49</td>
      <td>32</td>
      <td>49</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>50</td>
      <td>65</td>
      <td>50</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>79</td>
      <td>66</td>
      <td>79</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>95</td>
      <td>80</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>96</td>
      <td>114</td>
      <td>96</td>
      <td>114</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>135</td>
      <td>115</td>
      <td>135</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>155</td>
      <td>136</td>
      <td>155</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>156</td>
      <td>173</td>
      <td>156</td>
      <td>173</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>174</td>
      <td>177</td>
      <td>174</td>
      <td>177</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>189</td>
      <td>185</td>
      <td>189</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>204</td>
      <td>190</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>221</td>
      <td>205</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>237</td>
      <td>244</td>
      <td>237</td>
      <td>244</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>245</td>
      <td>261</td>
      <td>245</td>
      <td>261</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>285</td>
      <td>262</td>
      <td>285</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>301</td>
      <td>286</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>302</td>
      <td>309</td>
      <td>302</td>
      <td>309</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>324</td>
      <td>310</td>
      <td>324</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>325</td>
      <td>343</td>
      <td>325</td>
      <td>343</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>359</td>
      <td>344</td>
      <td>359</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>360</td>
      <td>375</td>
      <td>360</td>
      <td>375</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>376</td>
      <td>391</td>
      <td>376</td>
      <td>391</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>392</td>
      <td>408</td>
      <td>392</td>
      <td>408</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>409</td>
      <td>423</td>
      <td>409</td>
      <td>423</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>424</td>
      <td>426</td>
      <td>424</td>
      <td>426</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ayo">5AYO</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKV</span><span class="topo-outside">QSLLRIET</span><span class="topo-membrane">QLLLGRLLTRSGDQAWDFVVPFALL</span><span class="topo-inside">VIFPGKL</span><span class="topo-membrane">QVAAFYYLIVKIGTFLLTPSS</span><span class="topo-outside">GKWIDTHPRIQVV</span><span class="topo-membrane">KWGVWLQFFAILAGMVFFGML</span><span class="topo-inside">DGLVRAGGRESW</span><span class="topo-membrane">LLSVLFIALA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LSGVMASLGSQITD</span><span class="topo-outside">ISVGNDLAPSLVAPEKLTHFNSW</span><span class="topo-membrane">LRRIDLATEVGAPILAGALFA</span><span class="topo-inside">FHPEQLPL</span><span class="topo-membrane">AGLFLIGLWNLVSFVPEYFL</span><span class="topo-outside">LRNVIQRSGLKIKVLT</span><span class="topo-unknown">EAQSWKDTFHINLRGSF</span><span class="topo-outside">S</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">DPIFW</span><span class="topo-membrane">LILSYALLWLSVLSPHGVLLAAYLK</span><span class="topo-inside">DEMRLPE</span><span class="topo-membrane">TEIGLFRGLGAVFGLISTVSFPYL</span><span class="topo-outside">VRRLGLI</span><span class="topo-membrane">SSSRWHLGFQGVTLGIAVTAF</span><span class="topo-inside">AMGSTASV</span><span class="topo-membrane">YVFLGCILLSRVGLYGFSNGE</span><span class="topo-outside">FE</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440</span>
<span class="topo-line"><span class="topo-outside">LRQRLIPEGRRGELNSLS</span><span class="topo-membrane">SLTTTSATLILFSAGSLL</span><span class="topo-inside">PQTED</span><span class="topo-membrane">FKYLVYVSLAAVLLANVVFIKWS</span><span class="topo-outside">SR</span><span class="topo-unknown">QGVVTSGSENLYFQ</span></span>
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
      <td>4</td>
      <td>11</td>
      <td>4</td>
      <td>11</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>36</td>
      <td>12</td>
      <td>36</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>37</td>
      <td>43</td>
      <td>37</td>
      <td>43</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>64</td>
      <td>44</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>77</td>
      <td>65</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>98</td>
      <td>78</td>
      <td>98</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>99</td>
      <td>110</td>
      <td>99</td>
      <td>110</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>111</td>
      <td>134</td>
      <td>111</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>157</td>
      <td>135</td>
      <td>157</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>178</td>
      <td>158</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>186</td>
      <td>179</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>187</td>
      <td>206</td>
      <td>187</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>222</td>
      <td>207</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>245</td>
      <td>240</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>270</td>
      <td>246</td>
      <td>270</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>271</td>
      <td>277</td>
      <td>271</td>
      <td>277</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>301</td>
      <td>278</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>302</td>
      <td>308</td>
      <td>302</td>
      <td>308</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>309</td>
      <td>329</td>
      <td>309</td>
      <td>329</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>330</td>
      <td>337</td>
      <td>330</td>
      <td>337</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>358</td>
      <td>338</td>
      <td>358</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>359</td>
      <td>378</td>
      <td>359</td>
      <td>378</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>379</td>
      <td>396</td>
      <td>379</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>401</td>
      <td>397</td>
      <td>401</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>402</td>
      <td>424</td>
      <td>402</td>
      <td>424</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>425</td>
      <td>426</td>
      <td>425</td>
      <td>426</td>
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

### MFS fold of a transition-metal transporter

BbFPN adopts the canonical MFS fold with 12 TM helices organized into N-lobe (TM1-TM6) and C-lobe (TM7-TM12) connected by a long cytoplasmic loop. This is the first MFS transporter shown to mediate cation transport. Despite low sequence homology, the structural fold is conserved, demonstrating that the FPN family shares common topology with MFS transporters.

### Outward- and inward-facing conformational states

Comparison of the outward-facing (2.2 Å) and inward-facing (3.3 Å) structures reveals intra-domain conformational rearrangements during the transport cycle. The intracellular side of the N-lobe is flexible while the C-lobe is rigid; induced fit of the flexible N-lobe to the rigid C-lobe facilitates intracellular gate formation during the outward-to-inward transition. On the extracellular side, the C-lobe is flexible while the N-lobe is rigid.

### Metal-binding site

A substrate metal-binding site was identified based on structural and mutational analyses. Fe2+ coordination involves residues including Asp24, Asn196, and likely utilizes cation-π interactions with Phe200. The binding site is located in the central cavity between the N- and C-lobes. Isothermal titration calorimetry confirmed Co2+ binding affinity.

### Structural model for hepcidin-ferroportin interaction

A homology model of human ferroportin (hFPN) was constructed based on the BbFPN outward-facing structure. The model suggests that hepcidin-binding residues (Phe324, Cys326, Tyr333, Asp504, His507) cluster inside the central cavity, not on the extracellular loop as previously thought. This suggests hepcidin enters the central cavity between N and C lobes to interact with hFPN, providing new insights into hepcidin-mediated downregulation.


## Cross-References

- <a href="/xray-mp-wiki/concepts/protein-families/mfs-transporter/">Major Facilitator Superfamily (MFS)</a> — BbFPN adopts the MFS fold despite undetectable sequence similarity
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — BbFPN structures capture outward- and inward-facing states of the transport cycle
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Lipid used for LCP crystallization of BbFPN
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase (LCP) Crystallization</a> — Method used for all BbFPN crystal forms
- <a href="/xray-mp-wiki/reagents/additives/peg550mme/">PEG550MME</a> — Precipitant in all BbFPN crystallization conditions
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Buffer</a> — Buffer used in purification and crystallization of BbFPN
- <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG (Lauryldimaltoside Neopentyl Glycol)</a> — Detergent used in final purification buffer for BbFPN
- <a href="/xray-mp-wiki/reagents/buffers/acetate/">Acetate Buffer</a> — Buffer component in Form II crystallization condition (Na-acetate pH 4.0)
- <a href="/xray-mp-wiki/reagents/additives/iron/">Iron</a> — Referenced in the context of Iron
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Referenced in the context of Glycerol
