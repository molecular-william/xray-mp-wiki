---
title: "CaiT Carnitine Antiporter from Escherichia coli"
created: 2026-06-05
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.1788, doi/10.1038##NATURE09310, doi/10.1073##pnas.1309071110]
verified: agent
uniprot_id: ['B4EY22', 'P31553']
---

# CaiT Carnitine Antiporter from Escherichia coli

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/B4EY22">UniProt: B4EY22</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P31553">UniProt: P31553</a>

<span class="expr-badge">Proteus mirabilis</span>

## Overview

CaiT is an [L-Carnitine](/xray-mp-wiki/reagents/ligands/l-carnitine/)/[Gamma-Butyrobetaine (4-Trimethylaminobutyrate)](/xray-mp-wiki/reagents/ligands/gamma-butyrobetaine/) antiporter from Escherichia coli that belongs to the betaine/[Choline](/xray-mp-wiki/reagents/ligands/choline/)/carnitine transporter (BCCT) family. Unlike other BCCT family members which are Na+/H+-dependent symporters, CaiT functions as a precursor/product antiporter independently of the ion gradient. The crystal structure at 3.15 A resolution reveals a homotrimeric complex with each protomer containing 12 transmembrane helices and 4 [L-Carnitine](/xray-mp-wiki/reagents/ligands/l-carnitine/) molecules outlining the transport pathway across the membrane. High-resolution structures of CaiT from Proteus mirabilis (PmCaiT, 2.3 A) and E. coli (EcCaiT, 3.5 A) revealed the fully open inward-facing conformation and demonstrated a Na+-independent mechanism in which a methionine sulphur (Met331) coordinates the substrate in place of a sodium ion. Mutagenesis studies identified a primary binding site at the center of the protein and a secondary substrate-binding site at the bottom of the intracellular vestibule, providing mechanistic insights into the antiport process. The structures also revealed a regulatory extracellular substrate-binding site that mediates cooperative substrate binding with Hill coefficients up to 1.7.


## Publications

### doi/10.1038##nsmb.1788

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3hfx">3HFX</a></td>
      <td>3.15 A</td>
      <td>P6(3)</td>
      <td>CaiT from E. coli, residues 12-504, C-terminal GFP-His10 tag with <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV</a> cleavage site, Met353 mutated to Leu; homotrimer</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/l-carnitine/">L-Carnitine</a> (4 molecules per protomer)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C41
- **Construct**: CaiT from E. coli cloned into pET28-derivative vector with C-terminal GFP-His10 tag and [TEV](/xray-mp-wiki/reagents/additives/tev-protease/) protease cleavage site; Met353 mutated to Leu by sequencing; cultured in Terrific broth, induced with 0.3 mM [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg/) at 18 C for 20 h

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
      <td>Cell membrane isolation</td>
      <td>Cell lysis and membrane fractionation</td>
      <td>not applicable</td>
      <td>not specified + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Cells cultured in Terrific broth, induced with 0.3 mM <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG (Isopropyl-beta-D-thiogalactopyranoside)</a> at 18 C for 20 h; membranes isolated from disrupted C41 cells</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>not applicable</td>
      <td>not specified + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (1% w/v)</td>
      <td>Membranes solubilized with 1% (w/v) n-dodecyl beta-D-maltoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
    </tr>
    <tr>
      <td>Metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a> (first pass)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) metal ion <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl, 200 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>GFP-CaiT eluted from <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) column; contains C-terminal GFP-His10 tag</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV</a> protease cleavage</td>
      <td>Protease digestion</td>
      <td>not applicable</td>
      <td>not specified + not specified</td>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV</a> protease cleavage site between GFP-His10 and CaiT; removes GFP-His10 tag</td>
    </tr>
    <tr>
      <td>Metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a> (second pass)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) metal ion <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/)</td>
      <td>not specified + not specified</td>
      <td>Second Ni-column separates CaiT from <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV</a>-His and GFP-His; CaiT flows through</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/300 GL column (GE Healthcare)</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a>-NaOH pH 7.5, 150 mM NaCl, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Final <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) purification; concentrated to 10 mg/ml using 100-kDa Amicon Ultra-4 tube at 4 C</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>CaiT at 10 mg/ml in 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a>-NaOH pH 7.5, 20-26% (v/v) <a href="/xray-mp-wiki/reagents/additives/peg-400/">Polyethylene Glycol 400 (PEG 400)</a>, 0.1 M NaCl, 18 mM N-<a href="/xray-mp-wiki/reagents/detergents/og/">OG</a>, 5 mM <a href="/xray-mp-wiki/reagents/ligands/l-carnitine/">L-Carnitine</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown by hanging-drop vapor diffusion at 20 C. Heavy atom derivatives obtained by soaking crystals in mother liquor containing 5 mM ethylmercurithiosalicylic acid and sodium salt. Cryoprotected with reservoir solution containing 30% <a href="/xray-mp-wiki/reagents/additives/peg-400/">Polyethylene Glycol 400 (PEG 400)</a>, 0.020% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, and 10 mM N-<a href="/xray-mp-wiki/reagents/detergents/og/">OG</a>. Space group P6(3), cell dimensions a=b=134.2 A, c=85.1 A, alpha=beta=90 deg, gamma=120 deg. Phased by SIRAS using <a href="/xray-mp-wiki/reagents/additives/mercury/">Mercury (HgCl2) - Aquaporin Inhibitor</a> peak-wavelength (1.0039 A) dataset. Model contains residues 12-504, nine <a href="/xray-mp-wiki/reagents/additives/mercury/">Mercury (HgCl2) - Aquaporin Inhibitor</a> atoms, and four <a href="/xray-mp-wiki/reagents/ligands/l-carnitine/">L-Carnitine</a> molecules. Rwork/Rfree = 0.262/0.281.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>vapor-diffusion</td>
    </tr>
    <tr>
      <td>Variant</td>
      <td>hanging-drop</td>
    </tr>
    <tr>
      <td>pH</td>
      <td>7.5</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Components</td>
      <td>- Hepes: 0.1 M [buffer]  
- Peg 400: 20-26 % [precipitant] (Polyethylene Glycol 400 (PEG 400))  
- Sodium Chloride: 0.1 M [salt]  
- L Carnitine: 5 mM [additive]</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3hfx">3HFX</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKNEKRKTGIE</span><span class="topo-outside">PKVF</span><span class="topo-membrane">FPPLIIVGILCWL</span><span class="topo-inside">TVRD</span><span class="topo-unknown">LDAANVVINAVFSY</span><span class="topo-membrane">VTNVWGWAFEWYMVVML</span><span class="topo-outside">FGWFWLVFGPYAKKRLGNEPPEFSTASWIFMMF</span><span class="topo-membrane">ASCTSAAVLFWGS</span><span class="topo-inside">IEIYYYISTPP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FGLEPNSTGAKEL</span><span class="topo-membrane">GLAYSLFHWGPLPWAT</span><span class="topo-outside">YSFLSVAFAYFFFVRKMEVIRPSSTLVPLVGEKHAKGLFGTIVDN</span><span class="topo-membrane">FYLVALIFAMGTSLGLATPLV</span><span class="topo-inside">TECMQWLFGIPHTLQLD</span><span class="topo-membrane">AIIITCWI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">ILNAIC</span><span class="topo-outside">VACGLQKGVRI</span><span class="topo-membrane">ASDVRSYLSFLMLGWVFIVSG</span><span class="topo-inside">A</span><span class="topo-unknown">SFIMNYFTDSVGML</span><span class="topo-inside">L</span><span class="topo-unknown">MYLPRMLFYTD</span><span class="topo-inside">PIAKGGFP</span><span class="topo-membrane">QGWTVFYWAWWVIYA</span><span class="topo-outside">IQMSIFLARISRGRTVRELCFGMVLGL</span><span class="topo-membrane">TASTW</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">ILWTVLGSN</span><span class="topo-inside">TLLLIDKNIINIPNLIEQYG</span><span class="topo-unknown">VARAIIETWA</span><span class="topo-inside">ALPLSTA</span><span class="topo-membrane">TMWGFFILCFIATVTLVNACS</span><span class="topo-outside">YTLAMSTCREVRDGEEPPLL</span><span class="topo-membrane">VRIGWSILVGIIGIVL</span><span class="topo-inside">LALGGLKP</span><span class="topo-membrane">IQTAIIAGG</span></span>
<span class="topo-ruler">       490       500    </span>
<span class="topo-line"><span class="topo-membrane">CPLFFV</span><span class="topo-outside">NIMVTLSFIKDAKQNWKD</span></span>
<details class="topo-details"><summary>Topology coordinates (33 regions)</summary>
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
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>15</td>
      <td>12</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>28</td>
      <td>16</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>32</td>
      <td>29</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>46</td>
      <td>33</td>
      <td>46</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>63</td>
      <td>47</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>96</td>
      <td>64</td>
      <td>96</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>109</td>
      <td>97</td>
      <td>109</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>133</td>
      <td>110</td>
      <td>133</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>149</td>
      <td>134</td>
      <td>149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>194</td>
      <td>150</td>
      <td>194</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>215</td>
      <td>195</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>232</td>
      <td>216</td>
      <td>232</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>233</td>
      <td>246</td>
      <td>233</td>
      <td>246</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>247</td>
      <td>257</td>
      <td>247</td>
      <td>257</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>278</td>
      <td>258</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>279</td>
      <td>279</td>
      <td>279</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>293</td>
      <td>280</td>
      <td>293</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>294</td>
      <td>294</td>
      <td>294</td>
      <td>294</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>305</td>
      <td>295</td>
      <td>305</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>306</td>
      <td>313</td>
      <td>306</td>
      <td>313</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>314</td>
      <td>328</td>
      <td>314</td>
      <td>328</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>329</td>
      <td>355</td>
      <td>329</td>
      <td>355</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>356</td>
      <td>369</td>
      <td>356</td>
      <td>369</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>370</td>
      <td>389</td>
      <td>370</td>
      <td>389</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>399</td>
      <td>390</td>
      <td>399</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>400</td>
      <td>406</td>
      <td>400</td>
      <td>406</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>407</td>
      <td>427</td>
      <td>407</td>
      <td>427</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>428</td>
      <td>447</td>
      <td>428</td>
      <td>447</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>448</td>
      <td>463</td>
      <td>448</td>
      <td>463</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>464</td>
      <td>471</td>
      <td>464</td>
      <td>471</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>486</td>
      <td>472</td>
      <td>486</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>487</td>
      <td>504</td>
      <td>487</td>
      <td>504</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3hfx">3HFX</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKNEKRKTGIE</span><span class="topo-outside">PKVF</span><span class="topo-membrane">FPPLIIVGILCWL</span><span class="topo-inside">TVRD</span><span class="topo-unknown">LDAANVVINAVFSY</span><span class="topo-membrane">VTNVWGWAFEWYMVVML</span><span class="topo-outside">FGWFWLVFGPYAKKRLGNEPPEFSTASWIFMMF</span><span class="topo-membrane">ASCTSAAVLFWGS</span><span class="topo-inside">IEIYYYISTPP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FGLEPNSTGAKEL</span><span class="topo-membrane">GLAYSLFHWGPLPWAT</span><span class="topo-outside">YSFLSVAFAYFFFVRKMEVIRPSSTLVPLVGEKHAKGLFGTIVDN</span><span class="topo-membrane">FYLVALIFAMGTSLGLATPLV</span><span class="topo-inside">TECMQWLFGIPHTLQLD</span><span class="topo-membrane">AIIITCWI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">ILNAIC</span><span class="topo-outside">VACGLQKGVRI</span><span class="topo-membrane">ASDVRSYLSFLMLGWVFIVSG</span><span class="topo-inside">A</span><span class="topo-unknown">SFIMNYFTDSVGML</span><span class="topo-inside">L</span><span class="topo-unknown">MYLPRMLFYTD</span><span class="topo-inside">PIAKGGFP</span><span class="topo-membrane">QGWTVFYWAWWVIYA</span><span class="topo-outside">IQMSIFLARISRGRTVRELCFGMVLGL</span><span class="topo-membrane">TASTW</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">ILWTVLGSN</span><span class="topo-inside">TLLLIDKNIINIPNLIEQYG</span><span class="topo-unknown">VARAIIETWA</span><span class="topo-inside">ALPLSTA</span><span class="topo-membrane">TMWGFFILCFIATVTLVNACS</span><span class="topo-outside">YTLAMSTCREVRDGEEPPLL</span><span class="topo-membrane">VRIGWSILVGIIGIVL</span><span class="topo-inside">LALGGLKP</span><span class="topo-membrane">IQTAIIAGG</span></span>
<span class="topo-ruler">       490       500    </span>
<span class="topo-line"><span class="topo-membrane">CPLFFV</span><span class="topo-outside">NIMVTLSFIKDAKQNWKD</span></span>
<details class="topo-details"><summary>Topology coordinates (33 regions)</summary>
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
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>15</td>
      <td>12</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>28</td>
      <td>16</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>32</td>
      <td>29</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>46</td>
      <td>33</td>
      <td>46</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>63</td>
      <td>47</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>96</td>
      <td>64</td>
      <td>96</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>109</td>
      <td>97</td>
      <td>109</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>133</td>
      <td>110</td>
      <td>133</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>149</td>
      <td>134</td>
      <td>149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>194</td>
      <td>150</td>
      <td>194</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>215</td>
      <td>195</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>232</td>
      <td>216</td>
      <td>232</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>233</td>
      <td>246</td>
      <td>233</td>
      <td>246</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>247</td>
      <td>257</td>
      <td>247</td>
      <td>257</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>278</td>
      <td>258</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>279</td>
      <td>279</td>
      <td>279</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>293</td>
      <td>280</td>
      <td>293</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>294</td>
      <td>294</td>
      <td>294</td>
      <td>294</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>305</td>
      <td>295</td>
      <td>305</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>306</td>
      <td>313</td>
      <td>306</td>
      <td>313</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>314</td>
      <td>328</td>
      <td>314</td>
      <td>328</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>329</td>
      <td>355</td>
      <td>329</td>
      <td>355</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>356</td>
      <td>369</td>
      <td>356</td>
      <td>369</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>370</td>
      <td>389</td>
      <td>370</td>
      <td>389</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>399</td>
      <td>390</td>
      <td>399</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>400</td>
      <td>406</td>
      <td>400</td>
      <td>406</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>407</td>
      <td>427</td>
      <td>407</td>
      <td>427</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>428</td>
      <td>447</td>
      <td>428</td>
      <td>447</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>448</td>
      <td>463</td>
      <td>448</td>
      <td>463</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>464</td>
      <td>471</td>
      <td>464</td>
      <td>471</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>486</td>
      <td>472</td>
      <td>486</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>487</td>
      <td>504</td>
      <td>487</td>
      <td>504</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3hfx">3HFX</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKNEKRKTGIE</span><span class="topo-outside">PKVF</span><span class="topo-membrane">FPPLIIVGILCWL</span><span class="topo-inside">TVRD</span><span class="topo-unknown">LDAANVVINAVFSY</span><span class="topo-membrane">VTNVWGWAFEWYMVVML</span><span class="topo-outside">FGWFWLVFGPYAKKRLGNEPPEFSTASWIFMMF</span><span class="topo-membrane">ASCTSAAVLFWGS</span><span class="topo-inside">IEIYYYISTPP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FGLEPNSTGAKEL</span><span class="topo-membrane">GLAYSLFHWGPLPWAT</span><span class="topo-outside">YSFLSVAFAYFFFVRKMEVIRPSSTLVPLVGEKHAKGLFGTIVDN</span><span class="topo-membrane">FYLVALIFAMGTSLGLATPLV</span><span class="topo-inside">TECMQWLFGIPHTLQLD</span><span class="topo-membrane">AIIITCWI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">ILNAIC</span><span class="topo-outside">VACGLQKGVRI</span><span class="topo-membrane">ASDVRSYLSFLMLGWVFIVSG</span><span class="topo-inside">A</span><span class="topo-unknown">SFIMNYFTDSVGML</span><span class="topo-inside">L</span><span class="topo-unknown">MYLPRMLFYTD</span><span class="topo-inside">PIAKGGFP</span><span class="topo-membrane">QGWTVFYWAWWVIYA</span><span class="topo-outside">IQMSIFLARISRGRTVRELCFGMVLGL</span><span class="topo-membrane">TASTW</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">ILWTVLGSN</span><span class="topo-inside">TLLLIDKNIINIPNLIEQYG</span><span class="topo-unknown">VARAIIETWA</span><span class="topo-inside">ALPLSTA</span><span class="topo-membrane">TMWGFFILCFIATVTLVNACS</span><span class="topo-outside">YTLAMSTCREVRDGEEPPLL</span><span class="topo-membrane">VRIGWSILVGIIGIVL</span><span class="topo-inside">LALGGLKP</span><span class="topo-membrane">IQTAIIAGG</span></span>
<span class="topo-ruler">       490       500    </span>
<span class="topo-line"><span class="topo-membrane">CPLFFV</span><span class="topo-outside">NIMVTLSFIKDAKQNWKD</span></span>
<details class="topo-details"><summary>Topology coordinates (33 regions)</summary>
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
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>15</td>
      <td>12</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>28</td>
      <td>16</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>32</td>
      <td>29</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>46</td>
      <td>33</td>
      <td>46</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>63</td>
      <td>47</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>96</td>
      <td>64</td>
      <td>96</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>109</td>
      <td>97</td>
      <td>109</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>133</td>
      <td>110</td>
      <td>133</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>149</td>
      <td>134</td>
      <td>149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>194</td>
      <td>150</td>
      <td>194</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>215</td>
      <td>195</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>232</td>
      <td>216</td>
      <td>232</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>233</td>
      <td>246</td>
      <td>233</td>
      <td>246</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>247</td>
      <td>257</td>
      <td>247</td>
      <td>257</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>278</td>
      <td>258</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>279</td>
      <td>279</td>
      <td>279</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>293</td>
      <td>280</td>
      <td>293</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>294</td>
      <td>294</td>
      <td>294</td>
      <td>294</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>305</td>
      <td>295</td>
      <td>305</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>306</td>
      <td>313</td>
      <td>306</td>
      <td>313</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>314</td>
      <td>328</td>
      <td>314</td>
      <td>328</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>329</td>
      <td>355</td>
      <td>329</td>
      <td>355</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>356</td>
      <td>369</td>
      <td>356</td>
      <td>369</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>370</td>
      <td>389</td>
      <td>370</td>
      <td>389</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>399</td>
      <td>390</td>
      <td>399</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>400</td>
      <td>406</td>
      <td>400</td>
      <td>406</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>407</td>
      <td>427</td>
      <td>407</td>
      <td>427</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>428</td>
      <td>447</td>
      <td>428</td>
      <td>447</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>448</td>
      <td>463</td>
      <td>448</td>
      <td>463</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>464</td>
      <td>471</td>
      <td>464</td>
      <td>471</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>486</td>
      <td>472</td>
      <td>486</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>487</td>
      <td>504</td>
      <td>487</td>
      <td>504</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##NATURE09310

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
      <td></td>
      <td>2.3 A</td>
      <td>not specified</td>
      <td>PmCaiT from Proteus mirabilis, full-length; <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine (SeMet)</a>-substituted; inward-open fully open conformation</td>
      <td>none (transport site occupied by Trp323 side chain)</td>
    </tr>
    <tr>
      <td></td>
      <td>3.5 A</td>
      <td>not specified</td>
      <td>EcCaiT from E. coli, full-length; inward-open conformation with bound <a href="/xray-mp-wiki/reagents/ligands/gamma-butyrobetaine/">Gamma-Butyrobetaine (4-Trimethylaminobutyrate)</a> substrate</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/gamma-butyrobetaine/">Gamma-Butyrobetaine (4-Trimethylaminobutyrate)</a> (central transport site + extracellular binding pocket)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C41
- **Construct**: CaiT from E. coli cloned into pET28-derivative vector with C-terminal GFP-His10 tag and [TEV](/xray-mp-wiki/reagents/additives/tev-protease/) protease cleavage site; Met353 mutated to Leu by sequencing; cultured in Terrific broth, induced with 0.3 mM [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg/) at 18 C for 20 h

### doi/10.1073##pnas.1309071110

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4m8j">4M8J</a></td>
      <td>3.29 A</td>
      <td>not specified</td>
      <td>PmCaiT R262E mutant from Proteus mirabilis; inward-open substrate-bound conformation; solved by molecular replacement using PDB 2WSW</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/gamma-butyrobetaine/">Gamma-Butyrobetaine (4-Trimethylaminobutyrate)</a> (rotated orientation with carboxyl group contacting unwound TM1')</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C41
- **Construct**: CaiT from E. coli cloned into pET28-derivative vector with C-terminal GFP-His10 tag and [TEV](/xray-mp-wiki/reagents/additives/tev-protease/) protease cleavage site; Met353 mutated to Leu by sequencing; cultured in Terrific broth, induced with 0.3 mM [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg/) at 18 C for 20 h

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4m8j">4M8J</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSKDNKKA</span><span class="topo-outside">GIEPKVF</span><span class="topo-membrane">FPPLIIVGILCWLT</span><span class="topo-inside">VRDLDA</span><span class="topo-unknown">SNEVINAVFSY</span><span class="topo-membrane">VTNVWGWAFEWYMVIMFG</span><span class="topo-outside">GWFWLVFGRYAKKRLGDEKPEFSTASWIFMMF</span><span class="topo-membrane">ASCTSAAVLFWGS</span><span class="topo-inside">IEIYYYISSPP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FGMEGYSAPAKEI</span><span class="topo-membrane">GLAYSLFHWGPLPWATY</span><span class="topo-outside">SFLSVAFAYFFFVRKMEVIRPSSTLVPLVGEKHVNGLFGTVVDN</span><span class="topo-membrane">FYLVALILAMGTSLGLATPLVT</span><span class="topo-inside">ECIQYLFGIPHTLQLD</span><span class="topo-membrane">AIIISCWI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LLNAIC</span><span class="topo-outside">VAFGLQKGVKIA</span><span class="topo-membrane">SDVETYLSFLMLGWVFIVGG</span><span class="topo-inside">ASFIVNYFTDSVGTLLMYMPRMLFYTDPIGKGGFP</span><span class="topo-membrane">QAWTVFYWAWWVIYA</span><span class="topo-outside">IQMSIFLARISKGRTVRELCLGMV</span><span class="topo-membrane">SGLTAGTW</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LIWTILGGN</span><span class="topo-inside">TLQLIDQNILNIPQLIDQYG</span><span class="topo-unknown">VPRAIIETWA</span><span class="topo-inside">ALPLSTA</span><span class="topo-membrane">TMWGFFILCFIATVTLINACS</span><span class="topo-outside">YTLAMSTCRSMKEGADPPLL</span><span class="topo-membrane">VRIGWSVLVGIIGIILL</span><span class="topo-inside">ALGGLKP</span><span class="topo-membrane">IQTAIIAGG</span></span>
<span class="topo-ruler">       490       500    </span>
<span class="topo-line"><span class="topo-membrane">CPLFFVN</span><span class="topo-outside">IMVTLSFIKDAKVHWK</span><span class="topo-unknown">D</span></span>
<details class="topo-details"><summary>Topology coordinates (30 regions)</summary>
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
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>15</td>
      <td>9</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>29</td>
      <td>16</td>
      <td>29</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>35</td>
      <td>30</td>
      <td>35</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>46</td>
      <td>36</td>
      <td>46</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>64</td>
      <td>47</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>96</td>
      <td>65</td>
      <td>96</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>109</td>
      <td>97</td>
      <td>109</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>133</td>
      <td>110</td>
      <td>133</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>150</td>
      <td>134</td>
      <td>150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>151</td>
      <td>194</td>
      <td>151</td>
      <td>194</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>216</td>
      <td>195</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>232</td>
      <td>217</td>
      <td>232</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>233</td>
      <td>246</td>
      <td>233</td>
      <td>246</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>247</td>
      <td>258</td>
      <td>247</td>
      <td>258</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>278</td>
      <td>259</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>313</td>
      <td>279</td>
      <td>313</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>314</td>
      <td>328</td>
      <td>314</td>
      <td>328</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>329</td>
      <td>352</td>
      <td>329</td>
      <td>352</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>369</td>
      <td>353</td>
      <td>369</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>370</td>
      <td>389</td>
      <td>370</td>
      <td>389</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>399</td>
      <td>390</td>
      <td>399</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>400</td>
      <td>406</td>
      <td>400</td>
      <td>406</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>407</td>
      <td>427</td>
      <td>407</td>
      <td>427</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>428</td>
      <td>447</td>
      <td>428</td>
      <td>447</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>448</td>
      <td>464</td>
      <td>448</td>
      <td>464</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>465</td>
      <td>471</td>
      <td>465</td>
      <td>471</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>487</td>
      <td>472</td>
      <td>487</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>488</td>
      <td>503</td>
      <td>488</td>
      <td>503</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>504</td>
      <td>504</td>
      <td>504</td>
      <td>504</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4m8j">4M8J</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSKDNKKA</span><span class="topo-outside">GIEPKVF</span><span class="topo-membrane">FPPLIIVGILCWLT</span><span class="topo-inside">VRDLDA</span><span class="topo-unknown">SNEVINAVFSY</span><span class="topo-membrane">VTNVWGWAFEWYMVIMFG</span><span class="topo-outside">GWFWLVFGRYAKKRLGDEKPEFSTASWIFMMF</span><span class="topo-membrane">ASCTSAAVLFWGS</span><span class="topo-inside">IEIYYYISSPP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FGMEGYSAPAKEI</span><span class="topo-membrane">GLAYSLFHWGPLPWATY</span><span class="topo-outside">SFLSVAFAYFFFVRKMEVIRPSSTLVPLVGEKHVNGLFGTVVDN</span><span class="topo-membrane">FYLVALILAMGTSLGLATPLVT</span><span class="topo-inside">ECIQYLFGIPHTLQLD</span><span class="topo-membrane">AIIISCWI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LLNAIC</span><span class="topo-outside">VAFGLQKGVKIA</span><span class="topo-membrane">SDVETYLSFLMLGWVFIVGG</span><span class="topo-inside">ASFIVNYFTDSVGTLLMYMPRMLFYTDPIGKGGFP</span><span class="topo-membrane">QAWTVFYWAWWVIYA</span><span class="topo-outside">IQMSIFLARISKGRTVRELCLGMV</span><span class="topo-membrane">SGLTAGTW</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LIWTILGGN</span><span class="topo-inside">TLQLIDQNILNIPQLIDQYG</span><span class="topo-unknown">VPRAIIETWA</span><span class="topo-inside">ALPLSTA</span><span class="topo-membrane">TMWGFFILCFIATVTLINACS</span><span class="topo-outside">YTLAMSTCRSMKEGADPPLL</span><span class="topo-membrane">VRIGWSVLVGIIGIILL</span><span class="topo-inside">ALGGLKP</span><span class="topo-membrane">IQTAIIAGG</span></span>
<span class="topo-ruler">       490       500    </span>
<span class="topo-line"><span class="topo-membrane">CPLFFVN</span><span class="topo-outside">IMVTLSFIKDAKVHWK</span><span class="topo-unknown">D</span></span>
<details class="topo-details"><summary>Topology coordinates (30 regions)</summary>
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
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>15</td>
      <td>9</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>29</td>
      <td>16</td>
      <td>29</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>35</td>
      <td>30</td>
      <td>35</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>46</td>
      <td>36</td>
      <td>46</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>64</td>
      <td>47</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>96</td>
      <td>65</td>
      <td>96</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>109</td>
      <td>97</td>
      <td>109</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>133</td>
      <td>110</td>
      <td>133</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>150</td>
      <td>134</td>
      <td>150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>151</td>
      <td>194</td>
      <td>151</td>
      <td>194</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>216</td>
      <td>195</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>232</td>
      <td>217</td>
      <td>232</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>233</td>
      <td>246</td>
      <td>233</td>
      <td>246</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>247</td>
      <td>258</td>
      <td>247</td>
      <td>258</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>278</td>
      <td>259</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>313</td>
      <td>279</td>
      <td>313</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>314</td>
      <td>328</td>
      <td>314</td>
      <td>328</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>329</td>
      <td>352</td>
      <td>329</td>
      <td>352</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>369</td>
      <td>353</td>
      <td>369</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>370</td>
      <td>389</td>
      <td>370</td>
      <td>389</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>399</td>
      <td>390</td>
      <td>399</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>400</td>
      <td>406</td>
      <td>400</td>
      <td>406</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>407</td>
      <td>427</td>
      <td>407</td>
      <td>427</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>428</td>
      <td>447</td>
      <td>428</td>
      <td>447</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>448</td>
      <td>464</td>
      <td>448</td>
      <td>464</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>465</td>
      <td>471</td>
      <td>465</td>
      <td>471</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>487</td>
      <td>472</td>
      <td>487</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>488</td>
      <td>503</td>
      <td>488</td>
      <td>503</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>504</td>
      <td>504</td>
      <td>504</td>
      <td>504</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4m8j">4M8J</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSKDNKKA</span><span class="topo-outside">GIEPKVF</span><span class="topo-membrane">FPPLIIVGILCWLT</span><span class="topo-inside">VRDLDA</span><span class="topo-unknown">SNEVINAVFSY</span><span class="topo-membrane">VTNVWGWAFEWYMVIMFG</span><span class="topo-outside">GWFWLVFGRYAKKRLGDEKPEFSTASWIFMMF</span><span class="topo-membrane">ASCTSAAVLFWGS</span><span class="topo-inside">IEIYYYISSPP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FGMEGYSAPAKEI</span><span class="topo-membrane">GLAYSLFHWGPLPWATY</span><span class="topo-outside">SFLSVAFAYFFFVRKMEVIRPSSTLVPLVGEKHVNGLFGTVVDN</span><span class="topo-membrane">FYLVALILAMGTSLGLATPLVT</span><span class="topo-inside">ECIQYLFGIPHTLQLD</span><span class="topo-membrane">AIIISCWI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LLNAIC</span><span class="topo-outside">VAFGLQKGVKIA</span><span class="topo-membrane">SDVETYLSFLMLGWVFIVGG</span><span class="topo-inside">ASFIVNYFTDSVGTLLMYMPRMLFYTDPIGKGGFP</span><span class="topo-membrane">QAWTVFYWAWWVIYA</span><span class="topo-outside">IQMSIFLARISKGRTVRELCLGMV</span><span class="topo-membrane">SGLTAGTW</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LIWTILGGN</span><span class="topo-inside">TLQLIDQNILNIPQLIDQYG</span><span class="topo-unknown">VPRAIIETWA</span><span class="topo-inside">ALPLSTA</span><span class="topo-membrane">TMWGFFILCFIATVTLINACS</span><span class="topo-outside">YTLAMSTCRSMKEGADPPLL</span><span class="topo-membrane">VRIGWSVLVGIIGIILL</span><span class="topo-inside">ALGGLKP</span><span class="topo-membrane">IQTAIIAGG</span></span>
<span class="topo-ruler">       490       500    </span>
<span class="topo-line"><span class="topo-membrane">CPLFFVN</span><span class="topo-outside">IMVTLSFIKDAKVHWK</span><span class="topo-unknown">D</span></span>
<details class="topo-details"><summary>Topology coordinates (30 regions)</summary>
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
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>15</td>
      <td>9</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>29</td>
      <td>16</td>
      <td>29</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>35</td>
      <td>30</td>
      <td>35</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>46</td>
      <td>36</td>
      <td>46</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>64</td>
      <td>47</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>96</td>
      <td>65</td>
      <td>96</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>109</td>
      <td>97</td>
      <td>109</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>133</td>
      <td>110</td>
      <td>133</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>150</td>
      <td>134</td>
      <td>150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>151</td>
      <td>194</td>
      <td>151</td>
      <td>194</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>216</td>
      <td>195</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>232</td>
      <td>217</td>
      <td>232</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>233</td>
      <td>246</td>
      <td>233</td>
      <td>246</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>247</td>
      <td>258</td>
      <td>247</td>
      <td>258</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>278</td>
      <td>259</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>313</td>
      <td>279</td>
      <td>313</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>314</td>
      <td>328</td>
      <td>314</td>
      <td>328</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>329</td>
      <td>352</td>
      <td>329</td>
      <td>352</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>369</td>
      <td>353</td>
      <td>369</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>370</td>
      <td>389</td>
      <td>370</td>
      <td>389</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>399</td>
      <td>390</td>
      <td>399</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>400</td>
      <td>406</td>
      <td>400</td>
      <td>406</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>407</td>
      <td>427</td>
      <td>407</td>
      <td>427</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>428</td>
      <td>447</td>
      <td>428</td>
      <td>447</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>448</td>
      <td>464</td>
      <td>448</td>
      <td>464</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>465</td>
      <td>471</td>
      <td>465</td>
      <td>471</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>487</td>
      <td>472</td>
      <td>487</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>488</td>
      <td>503</td>
      <td>488</td>
      <td>503</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>504</td>
      <td>504</td>
      <td>504</td>
      <td>504</td>
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

### BCCT family antiporter with unique Na+-independent mechanism

CaiT belongs to the betaine/[Choline](/xray-mp-wiki/reagents/ligands/choline/)/carnitine transporter (BCCT) family but functions as a precursor/product antiporter independently of the ion gradient, unlike all other BCCT members which are Na+ or H+ dependent symporters. The conserved Na+-binding motif (Gly-X-Gly in TM3) is altered to Cys-Thr-Ser in CaiT, and key Na+-coordinating residues from [BetP (Na+/Betaine Symporter from Corynebacterium glutamicum)](/xray-mp-wiki/proteins/slc-transporters/betp/) are mutated (Ser468 to Leu422 in TM10, Met310 to Ser263 in TM7), disrupting the Na+-binding site.

### Four L-carnitine binding sites outline transport pathway

The crystal structure reveals four [L-Carnitine](/xray-mp-wiki/reagents/ligands/l-carnitine/) molecules per protomer: LC-I (primary binding site, center of protein), LC-II (secondary cytoplasmic site at bottom of intracellular vestibule), LC-III (extracellular surface cavity), and LC-IV (entrance of intracellular vestibule). LC-I forms hydrogen bonds with Gly253, Gly254, Gly257, Ser310, Ser313, and Trp316, and cation-pi interactions with Trp316 and Tyr319. LC-II interacts with Tyr327 and Gln330. LC-III interacts with Gly310, Trp316, and Tyr114. LC-IV contacts Glu85 and Arg337.

### Mutagenesis reveals functional binding sites

Mutagenesis of LC-II-interacting residues Y327L and Q330L markedly reduced carnitine uptake, supporting the existence of a cytoplasmic secondary substrate-binding site (Sin1). W316L (Trp316L) reduced transport rate by approximately 70%, while Y114L had minor effect, indicating the importance of aromatic residues at the periplasmic barrier top in transport activity.

### Cytoplasmic gate conformational rearrangement

Structural comparison with [BetP (Na+/Betaine Symporter from Corynebacterium glutamicum)](/xray-mp-wiki/proteins/slc-transporters/betp/) (occluded state) reveals that Tyr327 and Gln330 in CaiT (corresponding to Trp377 and Phe380 in BetP) coordinate with LC-II and deviate to allow inward or outward permeation, suggesting LC-II binding is associated with conformational rearrangements favoring opening of the cytoplasmic gate. Intracellular portions of TM3, TM4, TM8, and TM10 in CaiT deviate by approximately 2 Angstroms from corresponding [BetP (Na+/Betaine Symporter from Corynebacterium glutamicum)](/xray-mp-wiki/proteins/slc-transporters/betp/) portions.

### Homotrimeric architecture with 12 TM helices

CaiT crystallizes as a homotrimer with a threefold axis perpendicular to the membrane plane. Each protomer contains 12 transmembrane helices (TM1-TM12) with both N and C termini exposed to the cytoplasm. The monomer resembles a cylinder with maximum height of 52 Angstroms and maximum diameter of 45 Angstroms. TM3-TM12 form a structural core similar to the Na+-coupled symporter [BetP (Na+/Betaine Symporter from Corynebacterium glutamicum)](/xray-mp-wiki/proteins/slc-transporters/betp/) and cores of unrelated transporters [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/enzymes/leut/), [V. parahaemolyticus Sodium-Galactose Transporter (vSGLT)](/xray-mp-wiki/proteins/slc-transporters/vsglt/), and [Mhp1 Benzyl-Hydantoin Transporter from Microbacterium liquefaciens](/xray-mp-wiki/proteins/slc-transporters/mhp1/).

### Na+-independent transport mechanism via methionine coordination

The 2.3 A structure of PmCaiT reveals a Na+-independent transport mechanism unique among BCCT family members. In Na+-dependent transporters like [BetP (Na+/Betaine Symporter from Corynebacterium glutamicum)](/xray-mp-wiki/proteins/slc-transporters/betp/) and [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/enzymes/leut/), a sodium ion (Na1) coordinates the substrate carboxyl group. In CaiT, Met331 in TM8 positions its sulphur atom to coordinate the [Gamma-Butyrobetaine (4-Trimethylaminobutyrate)](/xray-mp-wiki/reagents/ligands/gamma-butyrobetaine/) carboxyl group, substituting for the missing Na1 ion. This explains CaiT's ability to function without sodium or proton gradients. A single Met331 to valine mutation reduces Kd by ~4-fold and Vmax by ~10-fold but does not restore Na+-dependence, confirming that a single side-chain substitution is insufficient to recreate a Na+-binding site.

### Fully open inward-facing conformation completes alternating access mechanism

Both CaiT structures (PmCaiT at 2.3 A, EcCaiT at 3.5 A) show the fully open inward-facing conformation, with a cytoplasmic funnel approximately 25 A deep and 15 A wide. Access from the cytoplasm is unhindered by obstructing side chains. Together with the outward-open and occluded states observed in other BCCT and [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/enzymes/leut/)-fold transporters, these structures complete the set of functional states describing the alternating access mechanism. EcCaiT contains two bound [Gamma-Butyrobetaine (4-Trimethylaminobutyrate)](/xray-mp-wiki/reagents/ligands/gamma-butyrobetaine/) molecules - one in the central transport site and one in an extracellular binding pocket.

### Cooperative substrate binding via regulatory extracellular site

Substrate-binding curves for CaiT reconstituted into proteoliposomes are sigmoidal,
indicating positive cooperativity with Hill coefficients of 1.4-1.7. The extracellular
substrate-binding site (the second site observed in EcCaiT, coordinated by Tyr114 and
Trp316 via cation-pi interactions) functions as a regulatory site. When occupied by
substrate, it displaces two water molecules, causing small shifts that propagate via
Glu111 to the central transport site, increasing binding affinity. Trp316Ala mutation
reduces Kd, Km, and Vmax by ~5-, 3.5-, and 2.5-fold respectively, confirming the profound
effect of the regulatory site on transport activity. In PmCaiT, access to this second
site is blocked by a crystal contact, and the regulatory site is empty, explaining why
the central transport site is also empty in that structure.

### Arginine 262 replaces Na2 site sodium in CaiT

In CaiT, the positively charged sidechain of R262 in TM5' occupies the position corresponding to the Na2 site found in Na+-dependent [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/enzymes/leut/)-type transporters ([LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/enzymes/leut/), [V. parahaemolyticus Sodium-Galactose Transporter (vSGLT)](/xray-mp-wiki/proteins/slc-transporters/vsglt/), [Mhp1 Benzyl-Hydantoin Transporter from Microbacterium liquefaciens](/xray-mp-wiki/proteins/slc-transporters/mhp1/), BetP). Mutagenesis of R262 to alanine or glutamate renders CaiT Na+-dependent, with transport activity restored 30-40% by a membrane potential in the presence of Na+, indicating substrate/Na+ co-transport (electrogenic). The apparent Km(Na+) was 0.45 mM for R262E and 0.70 mM for R262A. Unlike the protonatable K158 in [ApcT Amino Acid Transporter from Methanocaldococcus jannaschii](/xray-mp-wiki/proteins/slc-transporters/apct/), R262 does not undergo protonation/deprotonation cycles, as CaiT is maximally active at pH 7.

### R262 oscillation mechanism mimics sodium binding/unbinding

Homology modeling of CaiT on [BetP (Na+/Betaine Symporter from Corynebacterium glutamicum)](/xray-mp-wiki/proteins/slc-transporters/betp/) structures in outward-open and closed conformations reveals that R262 occupies different positions in each state, stabilized by distinct hydrogen bond networks. In the inward-open conformation, R262 interacts with T100 (TM1'), S259 (TM5'), and T421 (TM8'). In the modeled closed state, it interacts with S266 (TM5') and T100 (TM1'). In the outward-open conformation, R262 interacts with S101 (TM1') and S266 (TM5'). This oscillatory movement of the R262 sidechain between different hydrogen bond partners mimics Na+ binding and unbinding in Na+-dependent transporters, triggering alternating access conformational changes.

### R262E mutant structure reveals rotated substrate orientation

The crystal structure of PmCaiT R262E at 3.29 A resolution reveals a 90-degree rotation of bound [Gamma-Butyrobetaine (4-Trimethylaminobutyrate)](/xray-mp-wiki/reagents/ligands/gamma-butyrobetaine/) compared to the wild-type EcCaiT structure. In this orientation, the carboxyl group forms polar contacts with the unwound part of TM1' (backbone carbonyl of S98, sidechain of S101). The trimethyl ammonium head group fits into the tryptophan box (W323, W324, W147). The W323 sidechain rotates 90 degrees to accommodate this orientation. Substrate binding affinity is reduced ~10-fold in R262 mutants (Kd 38-40 mM vs 3.6 mM wild-type).


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/bcct-family/">Betaine/Choline/Carnitine Transporter (BCCT) Family</a> — CaiT belongs to the BCCT family; unique Na+-independent antiport mechanism distinguishes it from other BCCT members
- <a href="/xray-mp-wiki/proteins/slc-transporters/betp/">BetP Betaine Transporter from Bacillus subtilis</a> — Structural comparison with BetP (occluded state) provides insights into cytoplasmic gate mechanism
- <a href="/xray-mp-wiki/proteins/enzymes/leut/">LeuT Amino Acid Transporter from Aquifex aeolicus</a> — Core architecture comparison; LC-II reciprocal position of LeuT second binding site; outward-facing conformational state speculation
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — CaiT operates via alternating-access mechanism between inward-facing and outward-facing conformations
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent for CaiT solubilization, purification, and cryoprotection
- <a href="/xray-mp-wiki/reagents/detergents/n-octyl-beta-d-glucopyranoside/">n-Octyl-beta-D-glucopyranoside (OG)</a> — Detergent used in crystallization and cryoprotection
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES (4-(2-hydroxyethyl)-1-piperazineethanesulfonic acid)</a> — Buffer used in [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) and crystallization (HEPES-NaOH pH 7.5)
- <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV Protease (Tobacco Etch Virus Protease)</a> — [TEV](/xray-mp-wiki/reagents/additives/tev-protease/) protease used for cleavage of C-terminal GFP-His10 tag during purification
- <a href="/xray-mp-wiki/reagents/additives/mercury/">Mercury (HgCl2)</a> — Mercury compound (ethylmercurithiosalicylate) used for SIRAS phasing in crystal structure determination
- <a href="/xray-mp-wiki/reagents/ligands/l-carnitine/">L-Carnitine</a> — Endogenous substrate and ligand of CaiT; four molecules observed per protomer in crystal structure
- <a href="/xray-mp-wiki/reagents/ligands/gamma-butyrobetaine/">Gamma-Butyrobetaine</a> — Endogenous substrate of CaiT antiport exchange with L-carnitine
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/arginine-oscillation-mechanism/">Arginine Oscillation Mechanism in LeuT-Type Transporters</a> — This paper establishes the arginine oscillation model where R262 mimics Na+ binding/unbinding in CaiT
