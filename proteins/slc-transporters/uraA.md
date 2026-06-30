---
title: "Uracil:Proton Symporter UraA from Escherichia coli"
created: 2026-06-02
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature09885, doi/10.1038##cr.2017.83, doi/10.1038##nature11403, doi/10.1038##s41467-024-51814-8]
verified: false
---

# Uracil:Proton Symporter UraA from Escherichia coli

## Overview

UraA from Escherichia coli is a [URACIL](/xray-mp-wiki/reagents/ligands/uracil/):proton symporter and a prototypical member of the nucleobase/ascorbate transporter (NAT) or nucleobase/cation symporter 2 (NCS2) family, which corresponds to the human solute carrier family SLC23. The first crystal structure of UraA (PDB 3QE7, 2.8 A resolution) revealed a novel structural fold with 14 transmembrane segments (TMs) organized into two inverted repeats, with a pair of antiparallel beta-strands between TM3 and TM10 that serve as an organizing center for the structure. The protein is spatially arranged into a rigid core domain (TMs 1-4 and 8-11) and a flexible gate domain (TMs 5-7 and 12-14). [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) binds at the interface between the two domains, coordinated mainly by residues from the core domain including Glu241, His245, and Glu290. Alternating access of the substrate is achieved through conformational changes of the gate domain relative to the core domain. UraA functions as a homodimer in the membrane, and dimerization is required for transport activity.


## Publications

### doi/10.1038##nature09885

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3qe7">3QE7</a></td>
      <td>2.8 A</td>
      <td>P6_22</td>
      <td>Full-length UraA (residues 2-409) from E. coli strain O157:H7 cloned into pET21b vector with C-terminal His-tag; <a href="/xray-mp-wiki/reagents/ligands/uracil/">URACIL</a> bound</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/uracil/">URACIL</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length UraA from E. coli strain O157:H7, cloned into pET21b vector with C-terminal His-tag. Monomeric mutants M1 (L366W & I374W) and M2 (A137W & I374W) and constitutive dimer construct (two UraA molecules connected by 12-aa GlySer linker) also expressed. For the original structure (nature09885), [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) was added at 1 mM when cells were induced and included in all purification buffers.

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
      <td><a href="/xray-mp-wiki/methods/cell-lysis/french-press/">French Press Cell Lysis</a> and ultracentrifugation</td>
      <td>not specified</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl + not specified</td>
      <td>Cells disrupted by French press at 10000-15000 p.s.i., membrane fractions collected at 150000 x g for 1 h</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>not specified</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl + 1.5% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Membrane fraction incubated with 1.5% w/v <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> for 1 h at 4 C, then ultracentrifuged at 150000 x g for 30 min</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> (Qiagen)</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl, 30 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 1 mM <a href="/xray-mp-wiki/reagents/ligands/uracil/">URACIL</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Resin washed three times with 10 ml wash buffer each; protein eluted with 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> in wash buffer. 1 mM <a href="/xray-mp-wiki/reagents/ligands/uracil/">URACIL</a> included throughout.</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">SEC</a> buffer exchange</td>
      <td>Gel filtration chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/30 (GE Healthcare)</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl, indicated detergent, 1 mM <a href="/xray-mp-wiki/reagents/ligands/uracil/">URACIL</a> + 0.4% beta-NG (for crystallization)</td>
      <td>Protein concentrated to ~10 mg/ml before SEC; peak fractions collected for crystallization. All buffers contained 1 mM <a href="/xray-mp-wiki/reagents/ligands/uracil/">URACIL</a>.</td>
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
      <td>Full-length UraA (C-terminal His-tag) in 0.4% beta-NG, with 1 mM <a href="/xray-mp-wiki/reagents/ligands/uracil/">URACIL</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>25% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a>, 100 mM MES-NaOH pH 6.5, 300 mM Li2SO4</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>18 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>~1 month</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals appeared overnight and grew to 50 x 50 x 100 um hexagonal rods in about one month. Space group P6_22. Crystals diffracted beyond 2.9 A at SPring-8 beamline BL41XU. Phasing by Hg-SIRAS using <a href="/xray-mp-wiki/reagents/additives/mercury/">Mercury (HgCl2) - Aquaporin Inhibitor</a> derivatives obtained by soaking crystals for 24 h in mother liquor containing 1 mg/ml (C2H5HgO)HPO2. Structure refined at 2.8 A resolution.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3qe7">3QE7</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTR</span><span class="topo-outside">RAIGVSERPPLLQTIPLSL</span><span class="topo-membrane">QHLFAMFGATVLVPV</span><span class="topo-inside">LFHIN</span><span class="topo-membrane">PATVLLFNGIGTLLY</span><span class="topo-outside">LFICKGKIP</span><span class="topo-membrane">AYLGSSFAFI</span><span class="topo-inside">SPVLLLLPLGYEVALGG</span><span class="topo-membrane">FIMCGVLFCLVSFIVKKA</span><span class="topo-outside">GT</span><span class="topo-unknown">GWLDVL</span><span class="topo-outside">F</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">PPA</span><span class="topo-membrane">AMGAIVAVIGLELAGVAA</span><span class="topo-inside">GMAGLLPAEGQTPDSKT</span><span class="topo-membrane">IIISITTLAVTVLGSVL</span><span class="topo-outside">FRGFLAI</span><span class="topo-membrane">IPILIGVLVGYALSFAMGIVD</span><span class="topo-inside">TTPIINAHWFALPTLYTPRFEWFAILTIL</span><span class="topo-membrane">PAALVVIA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">EHVGHL</span><span class="topo-outside">VVTANIVKKDLLRDPGL</span><span class="topo-membrane">HRSMFANGLSTVISGFF</span><span class="topo-inside">G</span><span class="topo-membrane">STPNTTYGEN</span><span class="topo-outside">IGVMAITRVYSTWVIGGA</span><span class="topo-membrane">AIFAILLSCVGKLAAAIQMIP</span><span class="topo-inside">L</span><span class="topo-membrane">PVMGGVSLLLYGVIGASGI</span><span class="topo-outside">RVLIESKVDY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420         </span>
<span class="topo-line"><span class="topo-outside">NKAQNL</span><span class="topo-membrane">ILTSVILIIGVSGAKV</span><span class="topo-inside">NIGAAEL</span><span class="topo-membrane">KGMALATIVGIGLSLIFKL</span><span class="topo-outside">IS</span><span class="topo-unknown">VLRPEEVVLDAEDADITDK</span></span>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>22</td>
      <td>4</td>
      <td>22</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>37</td>
      <td>23</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>42</td>
      <td>38</td>
      <td>42</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>57</td>
      <td>43</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>58</td>
      <td>66</td>
      <td>58</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>76</td>
      <td>67</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>77</td>
      <td>93</td>
      <td>77</td>
      <td>93</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>111</td>
      <td>94</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>113</td>
      <td>112</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>119</td>
      <td>114</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>120</td>
      <td>123</td>
      <td>120</td>
      <td>123</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>141</td>
      <td>124</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>158</td>
      <td>142</td>
      <td>158</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>175</td>
      <td>159</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>176</td>
      <td>182</td>
      <td>176</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>203</td>
      <td>183</td>
      <td>203</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>204</td>
      <td>232</td>
      <td>204</td>
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
      <td>263</td>
      <td>247</td>
      <td>263</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>264</td>
      <td>280</td>
      <td>264</td>
      <td>280</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>281</td>
      <td>281</td>
      <td>281</td>
      <td>281</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>291</td>
      <td>282</td>
      <td>291</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>292</td>
      <td>309</td>
      <td>292</td>
      <td>309</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>330</td>
      <td>310</td>
      <td>330</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>331</td>
      <td>331</td>
      <td>331</td>
      <td>331</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>332</td>
      <td>350</td>
      <td>332</td>
      <td>350</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>351</td>
      <td>366</td>
      <td>351</td>
      <td>366</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>382</td>
      <td>367</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>389</td>
      <td>383</td>
      <td>389</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>408</td>
      <td>390</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>410</td>
      <td>409</td>
      <td>410</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>411</td>
      <td>429</td>
      <td>411</td>
      <td>429</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3qe7">3QE7</a> — Chain B (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTR</span><span class="topo-outside">RAIGVSERPPLLQTIPLSL</span><span class="topo-membrane">QHLFAMFGATVLVPV</span><span class="topo-inside">LFHIN</span><span class="topo-membrane">PATVLLFNGIGTLLY</span><span class="topo-outside">LFICKGKIP</span><span class="topo-membrane">AYLGSSFAFI</span><span class="topo-inside">SPVLLLLPLGYEVALGG</span><span class="topo-membrane">FIMCGVLFCLVSFIVKKA</span><span class="topo-outside">GT</span><span class="topo-unknown">GWLDVL</span><span class="topo-outside">F</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">PPA</span><span class="topo-membrane">AMGAIVAVIGLELAGVAA</span><span class="topo-inside">GMAGLLPAEGQTPDSKT</span><span class="topo-membrane">IIISITTLAVTVLGSVL</span><span class="topo-outside">FRGFLAI</span><span class="topo-membrane">IPILIGVLVGYALSFAMGIVD</span><span class="topo-inside">TTPIINAHWFALPTLYTPRFEWFAILTIL</span><span class="topo-membrane">PAALVVIA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">EHVGHL</span><span class="topo-outside">VVTANIVKKDLLRDPGL</span><span class="topo-membrane">HRSMFANGLSTVISGFF</span><span class="topo-inside">G</span><span class="topo-membrane">STPNTTYGEN</span><span class="topo-outside">IGVMAITRVYSTWVIGGA</span><span class="topo-membrane">AIFAILLSCVGKLAAAIQMIP</span><span class="topo-inside">L</span><span class="topo-membrane">PVMGGVSLLLYGVIGASGI</span><span class="topo-outside">RVLIESKVDY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420         </span>
<span class="topo-line"><span class="topo-outside">NKAQNL</span><span class="topo-membrane">ILTSVILIIGVSGAKV</span><span class="topo-inside">NIGAAEL</span><span class="topo-membrane">KGMALATIVGIGLSLIFKL</span><span class="topo-outside">IS</span><span class="topo-unknown">VLRPEEVVLDAEDADITDK</span></span>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>22</td>
      <td>4</td>
      <td>22</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>37</td>
      <td>23</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>42</td>
      <td>38</td>
      <td>42</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>57</td>
      <td>43</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>58</td>
      <td>66</td>
      <td>58</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>76</td>
      <td>67</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>77</td>
      <td>93</td>
      <td>77</td>
      <td>93</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>111</td>
      <td>94</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>113</td>
      <td>112</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>119</td>
      <td>114</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>120</td>
      <td>123</td>
      <td>120</td>
      <td>123</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>141</td>
      <td>124</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>158</td>
      <td>142</td>
      <td>158</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>175</td>
      <td>159</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>176</td>
      <td>182</td>
      <td>176</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>203</td>
      <td>183</td>
      <td>203</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>204</td>
      <td>232</td>
      <td>204</td>
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
      <td>263</td>
      <td>247</td>
      <td>263</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>264</td>
      <td>280</td>
      <td>264</td>
      <td>280</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>281</td>
      <td>281</td>
      <td>281</td>
      <td>281</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>291</td>
      <td>282</td>
      <td>291</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>292</td>
      <td>309</td>
      <td>292</td>
      <td>309</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>330</td>
      <td>310</td>
      <td>330</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>331</td>
      <td>331</td>
      <td>331</td>
      <td>331</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>332</td>
      <td>350</td>
      <td>332</td>
      <td>350</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>351</td>
      <td>366</td>
      <td>351</td>
      <td>366</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>382</td>
      <td>367</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>389</td>
      <td>383</td>
      <td>389</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>408</td>
      <td>390</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>410</td>
      <td>409</td>
      <td>410</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>411</td>
      <td>429</td>
      <td>411</td>
      <td>429</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##cr.2017.83

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5xls">5XLS</a></td>
      <td>2.5 A</td>
      <td>C2221</td>
      <td>Wild-type full-length UraA (residues 2-409)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/uracil/">URACIL</a> (occluded state)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length UraA from E. coli strain O157:H7, cloned into pET21b vector with C-terminal His-tag. Monomeric mutants M1 (L366W & I374W) and M2 (A137W & I374W) and constitutive dimer construct (two UraA molecules connected by 12-aa GlySer linker) also expressed. For the original structure (nature09885), [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) was added at 1 mM when cells were induced and included in all purification buffers.

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
      <td><a href="/xray-mp-wiki/methods/cell-lysis/french-press/">French Press Cell Lysis</a> and ultracentrifugation</td>
      <td>not specified</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl + not specified</td>
      <td>Cells disrupted by French press at 10000-15000 p.s.i., membrane fractions collected at 150000 x g for 1 h</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>not specified</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl + 1.5% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>1.5% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (Anatrace) incubated for 1 h at 4 C</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> (Qiagen)</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl, 30 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 1 mM <a href="/xray-mp-wiki/reagents/ligands/uracil/">URACIL</a>, 0.2% <a href="/xray-mp-wiki/reagents/detergents/dm">DM</a> + 0.2% DM</td>
      <td>Resin washed three times with wash buffer, eluted with 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td>SEC</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/30 (GE Healthcare)</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl, 1 mM <a href="/xray-mp-wiki/reagents/ligands/uracil/">URACIL</a>, indicated detergents + indicated detergents (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a>, NG, <a href="/xray-mp-wiki/reagents/detergents/fos-choline-9/">FC-9</a>, <a href="/xray-mp-wiki/reagents/detergents/fos-choline-11/">FC-11</a>)</td>
      <td>Peak fractions collected for crystallization or biochemical characterizations</td>
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
      <td>Wild-type full-length UraA in detergent</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>1.2% Fos-<a href="/xray-mp-wiki/reagents/ligands/choline/">Choline</a> 9 (<a href="/xray-mp-wiki/reagents/detergents/fos-choline-9/">FC-9</a>) and 0.06% Fos-<a href="/xray-mp-wiki/reagents/ligands/choline/">Choline</a> 11 (<a href="/xray-mp-wiki/reagents/detergents/fos-choline-11/">FC-11</a>)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>18 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grew in space group C2221. Data collected at BL41XU, SPring-8. Structure solved by W-SAD phasing at 2.5 A resolution.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5xls">5XLS</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTRR</span><span class="topo-outside">AIGVSERPPL</span><span class="topo-membrane">LQTIPLSLQHLFAMFGATVLV</span><span class="topo-inside">PVLFHINP</span><span class="topo-membrane">ATVLLFNGIGTLLYLFI</span><span class="topo-outside">CKGKIP</span><span class="topo-membrane">AYLGSSFAFISP</span><span class="topo-inside">VLLLLPLGYEVAL</span><span class="topo-membrane">GGFIMCGVLFCLVSFI</span><span class="topo-outside">VKKAGTGWLDVL</span><span class="topo-membrane">F</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">PPAAMGAIVAVIGLELAGVAA</span><span class="topo-inside">GMAGLLPAEGQTPDSKTII</span><span class="topo-membrane">ISITTLAVTVLGSVLF</span><span class="topo-outside">RGF</span><span class="topo-membrane">LAIIPILIGVLVGYALS</span><span class="topo-inside">FAMGIVDTTPIINAHWFALPTLYTPRFEWFAI</span><span class="topo-membrane">LTILPAALVVIA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">EHVGH</span><span class="topo-outside">LVVTANIVKKDLLRDPGLHRS</span><span class="topo-membrane">MFANGLSTVISGFFG</span><span class="topo-inside">S</span><span class="topo-membrane">TPNTTYGENIGVM</span><span class="topo-outside">AITRVYSTW</span><span class="topo-membrane">VIGGAAIFAILLSCV</span><span class="topo-unknown">GKLAAAIQM</span><span class="topo-inside">IPLP</span><span class="topo-membrane">VMGGVSLLLYGVIGASGIRVL</span><span class="topo-outside">IESKVDY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430     </span>
<span class="topo-line"><span class="topo-outside">NKA</span><span class="topo-membrane">QNLILTSVILIIGVSGAKV</span><span class="topo-inside">NIGAAEL</span><span class="topo-membrane">KGMALATIVGIGLSLIFKLI</span><span class="topo-outside">SVL</span><span class="topo-unknown">RPEEVVLDEVDADITDKHHHHHH</span></span>
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
      <td>5</td>
      <td>14</td>
      <td>5</td>
      <td>14</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>35</td>
      <td>15</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>43</td>
      <td>36</td>
      <td>43</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>60</td>
      <td>44</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>66</td>
      <td>61</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>78</td>
      <td>67</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>91</td>
      <td>79</td>
      <td>91</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>107</td>
      <td>92</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>119</td>
      <td>108</td>
      <td>119</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>120</td>
      <td>141</td>
      <td>120</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>160</td>
      <td>142</td>
      <td>160</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>176</td>
      <td>161</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>179</td>
      <td>177</td>
      <td>179</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>180</td>
      <td>196</td>
      <td>180</td>
      <td>196</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>228</td>
      <td>197</td>
      <td>228</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>245</td>
      <td>229</td>
      <td>245</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>246</td>
      <td>266</td>
      <td>246</td>
      <td>266</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>267</td>
      <td>281</td>
      <td>267</td>
      <td>281</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>282</td>
      <td>282</td>
      <td>282</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>295</td>
      <td>283</td>
      <td>295</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>296</td>
      <td>304</td>
      <td>296</td>
      <td>304</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>305</td>
      <td>319</td>
      <td>305</td>
      <td>319</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>320</td>
      <td>328</td>
      <td>320</td>
      <td>328</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>329</td>
      <td>332</td>
      <td>329</td>
      <td>332</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>353</td>
      <td>333</td>
      <td>353</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>354</td>
      <td>363</td>
      <td>354</td>
      <td>363</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>364</td>
      <td>382</td>
      <td>364</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>389</td>
      <td>383</td>
      <td>389</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>409</td>
      <td>390</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>412</td>
      <td>410</td>
      <td>412</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##nature11403

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3qe7">3QE7</a></td>
      <td>3.2 A</td>
      <td>P6_22</td>
      <td>Wild-type full-length UraA</td>
      <td>beta-NG (inward-open state)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length UraA from E. coli strain O157:H7, cloned into pET21b vector with C-terminal His-tag. Monomeric mutants M1 (L366W & I374W) and M2 (A137W & I374W) and constitutive dimer construct (two UraA molecules connected by 12-aa GlySer linker) also expressed. For the original structure (nature09885), [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) was added at 1 mM when cells were induced and included in all purification buffers.

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3qe7">3QE7</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTR</span><span class="topo-outside">RAIGVSERPPLLQTIPLSL</span><span class="topo-membrane">QHLFAMFGATVLVPV</span><span class="topo-inside">LFHIN</span><span class="topo-membrane">PATVLLFNGIGTLLY</span><span class="topo-outside">LFICKGKIP</span><span class="topo-membrane">AYLGSSFAFI</span><span class="topo-inside">SPVLLLLPLGYEVALGG</span><span class="topo-membrane">FIMCGVLFCLVSFIVKKA</span><span class="topo-outside">GT</span><span class="topo-unknown">GWLDVL</span><span class="topo-outside">F</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">PPA</span><span class="topo-membrane">AMGAIVAVIGLELAGVAA</span><span class="topo-inside">GMAGLLPAEGQTPDSKT</span><span class="topo-membrane">IIISITTLAVTVLGSVL</span><span class="topo-outside">FRGFLAI</span><span class="topo-membrane">IPILIGVLVGYALSFAMGIVD</span><span class="topo-inside">TTPIINAHWFALPTLYTPRFEWFAILTIL</span><span class="topo-membrane">PAALVVIA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">EHVGHL</span><span class="topo-outside">VVTANIVKKDLLRDPGL</span><span class="topo-membrane">HRSMFANGLSTVISGFF</span><span class="topo-inside">G</span><span class="topo-membrane">STPNTTYGEN</span><span class="topo-outside">IGVMAITRVYSTWVIGGA</span><span class="topo-membrane">AIFAILLSCVGKLAAAIQMIP</span><span class="topo-inside">L</span><span class="topo-membrane">PVMGGVSLLLYGVIGASGI</span><span class="topo-outside">RVLIESKVDY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420         </span>
<span class="topo-line"><span class="topo-outside">NKAQNL</span><span class="topo-membrane">ILTSVILIIGVSGAKV</span><span class="topo-inside">NIGAAEL</span><span class="topo-membrane">KGMALATIVGIGLSLIFKL</span><span class="topo-outside">IS</span><span class="topo-unknown">VLRPEEVVLDAEDADITDK</span></span>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>22</td>
      <td>4</td>
      <td>22</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>37</td>
      <td>23</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>42</td>
      <td>38</td>
      <td>42</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>57</td>
      <td>43</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>58</td>
      <td>66</td>
      <td>58</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>76</td>
      <td>67</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>77</td>
      <td>93</td>
      <td>77</td>
      <td>93</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>111</td>
      <td>94</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>113</td>
      <td>112</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>119</td>
      <td>114</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>120</td>
      <td>123</td>
      <td>120</td>
      <td>123</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>141</td>
      <td>124</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>158</td>
      <td>142</td>
      <td>158</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>175</td>
      <td>159</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>176</td>
      <td>182</td>
      <td>176</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>203</td>
      <td>183</td>
      <td>203</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>204</td>
      <td>232</td>
      <td>204</td>
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
      <td>263</td>
      <td>247</td>
      <td>263</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>264</td>
      <td>280</td>
      <td>264</td>
      <td>280</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>281</td>
      <td>281</td>
      <td>281</td>
      <td>281</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>291</td>
      <td>282</td>
      <td>291</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>292</td>
      <td>309</td>
      <td>292</td>
      <td>309</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>330</td>
      <td>310</td>
      <td>330</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>331</td>
      <td>331</td>
      <td>331</td>
      <td>331</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>332</td>
      <td>350</td>
      <td>332</td>
      <td>350</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>351</td>
      <td>366</td>
      <td>351</td>
      <td>366</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>382</td>
      <td>367</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>389</td>
      <td>383</td>
      <td>389</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>408</td>
      <td>390</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>410</td>
      <td>409</td>
      <td>410</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>411</td>
      <td>429</td>
      <td>411</td>
      <td>429</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3qe7">3QE7</a> — Chain B (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTR</span><span class="topo-outside">RAIGVSERPPLLQTIPLSL</span><span class="topo-membrane">QHLFAMFGATVLVPV</span><span class="topo-inside">LFHIN</span><span class="topo-membrane">PATVLLFNGIGTLLY</span><span class="topo-outside">LFICKGKIP</span><span class="topo-membrane">AYLGSSFAFI</span><span class="topo-inside">SPVLLLLPLGYEVALGG</span><span class="topo-membrane">FIMCGVLFCLVSFIVKKA</span><span class="topo-outside">GT</span><span class="topo-unknown">GWLDVL</span><span class="topo-outside">F</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">PPA</span><span class="topo-membrane">AMGAIVAVIGLELAGVAA</span><span class="topo-inside">GMAGLLPAEGQTPDSKT</span><span class="topo-membrane">IIISITTLAVTVLGSVL</span><span class="topo-outside">FRGFLAI</span><span class="topo-membrane">IPILIGVLVGYALSFAMGIVD</span><span class="topo-inside">TTPIINAHWFALPTLYTPRFEWFAILTIL</span><span class="topo-membrane">PAALVVIA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">EHVGHL</span><span class="topo-outside">VVTANIVKKDLLRDPGL</span><span class="topo-membrane">HRSMFANGLSTVISGFF</span><span class="topo-inside">G</span><span class="topo-membrane">STPNTTYGEN</span><span class="topo-outside">IGVMAITRVYSTWVIGGA</span><span class="topo-membrane">AIFAILLSCVGKLAAAIQMIP</span><span class="topo-inside">L</span><span class="topo-membrane">PVMGGVSLLLYGVIGASGI</span><span class="topo-outside">RVLIESKVDY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420         </span>
<span class="topo-line"><span class="topo-outside">NKAQNL</span><span class="topo-membrane">ILTSVILIIGVSGAKV</span><span class="topo-inside">NIGAAEL</span><span class="topo-membrane">KGMALATIVGIGLSLIFKL</span><span class="topo-outside">IS</span><span class="topo-unknown">VLRPEEVVLDAEDADITDK</span></span>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>22</td>
      <td>4</td>
      <td>22</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>37</td>
      <td>23</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>42</td>
      <td>38</td>
      <td>42</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>57</td>
      <td>43</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>58</td>
      <td>66</td>
      <td>58</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>76</td>
      <td>67</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>77</td>
      <td>93</td>
      <td>77</td>
      <td>93</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>111</td>
      <td>94</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>113</td>
      <td>112</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>119</td>
      <td>114</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>120</td>
      <td>123</td>
      <td>120</td>
      <td>123</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>141</td>
      <td>124</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>158</td>
      <td>142</td>
      <td>158</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>175</td>
      <td>159</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>176</td>
      <td>182</td>
      <td>176</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>203</td>
      <td>183</td>
      <td>203</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>204</td>
      <td>232</td>
      <td>204</td>
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
      <td>263</td>
      <td>247</td>
      <td>263</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>264</td>
      <td>280</td>
      <td>264</td>
      <td>280</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>281</td>
      <td>281</td>
      <td>281</td>
      <td>281</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>291</td>
      <td>282</td>
      <td>291</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>292</td>
      <td>309</td>
      <td>292</td>
      <td>309</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>330</td>
      <td>310</td>
      <td>330</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>331</td>
      <td>331</td>
      <td>331</td>
      <td>331</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>332</td>
      <td>350</td>
      <td>332</td>
      <td>350</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>351</td>
      <td>366</td>
      <td>351</td>
      <td>366</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>382</td>
      <td>367</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>389</td>
      <td>383</td>
      <td>389</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>408</td>
      <td>390</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>410</td>
      <td>409</td>
      <td>410</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>411</td>
      <td>429</td>
      <td>411</td>
      <td>429</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##s41467-024-51814-8

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8omz">8OMZ</a></td>
      <td>3.5 A</td>
      <td></td>
      <td>UraA(G320P) mutant in complex with synthetic <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> Sy45; wide inward-open conformation</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8omz">8OMZ</a></td>
      <td>3.7 A</td>
      <td></td>
      <td>UraA(G320P) mutant in complex with synthetic <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> Sy45 with 1 mM <a href="/xray-mp-wiki/reagents/ligands/uracil/">URACIL</a></td>
      <td><a href="/xray-mp-wiki/reagents/ligands/uracil/">URACIL</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length UraA from E. coli strain O157:H7, cloned into pET21b vector with C-terminal His-tag. Monomeric mutants M1 (L366W & I374W) and M2 (A137W & I374W) and constitutive dimer construct (two UraA molecules connected by 12-aa GlySer linker) also expressed. For the original structure (nature09885), [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) was added at 1 mM when cells were induced and included in all purification buffers.

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>UraA(G320P)-Sy45 complex in 0.2% DM, supplemented with 1% NG; final protein concentration 10 mg/ml</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>50 mM Tris.HCl pH 8.4, 50 mM magnesium acetate, 35% (v/v) <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a>, 0.1% (w/v) benzamidine hydrochloride</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>18 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Apo crystals of UraA(G320P)-Sy45 diffracted to 3.5 A resolution at PETRA III beamline P13. Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using occluded UraA structure and SWISS-MODEL of Sy45. Uracil-liganded crystals were obtained using 40% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a> and 1 mM <a href="/xray-mp-wiki/reagents/ligands/uracil/">URACIL</a> in reservoir, with apo crystals used as seeds, diffracting to 3.7 A at SLS X06DA beamline.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8omz">8OMZ</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MST</span><span class="topo-inside">RRAIGVSERPPL</span><span class="topo-membrane">LQTIPLSLQHLFAMFGATVLV</span><span class="topo-outside">PVLFHINPATV</span><span class="topo-membrane">LLFNGIGTLLYLFIC</span><span class="topo-inside">KGKIP</span><span class="topo-membrane">AYLGSSFAFISP</span><span class="topo-outside">VLLLLPLGYEVALGG</span><span class="topo-membrane">FIMCGVLFCLVSFI</span><span class="topo-inside">VKKAGTGWLDV</span><span class="topo-membrane">L</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">FPPAAMGAIVAVIGLELA</span><span class="topo-outside">GVAAGMAGLLPAEGQTPDSKTIIISIT</span><span class="topo-membrane">TLAVTVLGSVLFRG</span><span class="topo-unknown">F</span><span class="topo-membrane">LAIIPILIGVLV</span><span class="topo-outside">GYALSFAMGIVDTTPIINAHWFALPTLYTPRFEWFAI</span><span class="topo-membrane">LTILPAALVVI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">AEHVGH</span><span class="topo-inside">LVVTANIVKKDLLRDPGLH</span><span class="topo-membrane">RSMFANGLSTVISG</span><span class="topo-outside">FFGS</span><span class="topo-membrane">TPNTTYGENIGV</span><span class="topo-inside">MAITRVYST</span><span class="topo-membrane">WVIGGAAIFAILLS</span><span class="topo-outside">CVPKLAAAIQMIPLPVMGG</span><span class="topo-membrane">VSLLLYGVIGASGIRVLI</span><span class="topo-inside">ESKVD</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       </span>
<span class="topo-line"><span class="topo-inside">YNKA</span><span class="topo-membrane">QNLILTSVILIIGVS</span><span class="topo-outside">GAKVNIGAAELKG</span><span class="topo-membrane">MALATIVGIGLSLIFKLI</span><span class="topo-inside">SVL</span><span class="topo-unknown">RPEEVVLDAEDADITDKALEVLFQ</span></span>
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
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>15</td>
      <td>3</td>
      <td>14</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>36</td>
      <td>15</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>37</td>
      <td>47</td>
      <td>36</td>
      <td>46</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>62</td>
      <td>47</td>
      <td>61</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>67</td>
      <td>62</td>
      <td>66</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>79</td>
      <td>67</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>94</td>
      <td>79</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>108</td>
      <td>94</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>119</td>
      <td>108</td>
      <td>118</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>120</td>
      <td>138</td>
      <td>119</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>165</td>
      <td>138</td>
      <td>164</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>179</td>
      <td>165</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>181</td>
      <td>192</td>
      <td>180</td>
      <td>191</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>193</td>
      <td>229</td>
      <td>192</td>
      <td>228</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>230</td>
      <td>246</td>
      <td>229</td>
      <td>245</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>247</td>
      <td>265</td>
      <td>246</td>
      <td>264</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>266</td>
      <td>279</td>
      <td>265</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>283</td>
      <td>279</td>
      <td>282</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>295</td>
      <td>283</td>
      <td>294</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>296</td>
      <td>304</td>
      <td>295</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>305</td>
      <td>318</td>
      <td>304</td>
      <td>317</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>319</td>
      <td>337</td>
      <td>318</td>
      <td>336</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>355</td>
      <td>337</td>
      <td>354</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>356</td>
      <td>364</td>
      <td>355</td>
      <td>363</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>365</td>
      <td>379</td>
      <td>364</td>
      <td>378</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>380</td>
      <td>392</td>
      <td>379</td>
      <td>391</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>393</td>
      <td>410</td>
      <td>392</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>413</td>
      <td>410</td>
      <td>412</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>414</td>
      <td>437</td>
      <td>413</td>
      <td>436</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8omz">8OMZ</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GS</span><span class="topo-inside">SSQVQLVESGGGSVQAGGSLRLSCAASGNIAYIHYLGWFRQAPGKEREGVAALSTTLGNTYYADSVKGRFTVSLDNAKNTVYLQMNSLKPEDTALYYCAAAYFGYSSPLAHERYMYWG</span></span>
<span class="topo-ruler">       130       140       150    </span>
<span class="topo-line"><span class="topo-inside">QGTQVTVSA</span><span class="topo-unknown">GRAGEQKLISEEDLNSAVDHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>2</td>
      <td>-3</td>
      <td>-2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>129</td>
      <td>-1</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>154</td>
      <td>126</td>
      <td>150</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8omz">8OMZ</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MST</span><span class="topo-inside">RRAIGVSERPPL</span><span class="topo-membrane">LQTIPLSLQHLFAMFGATVLV</span><span class="topo-outside">PVLFHINPATV</span><span class="topo-membrane">LLFNGIGTLLYLFIC</span><span class="topo-inside">KGKIP</span><span class="topo-membrane">AYLGSSFAFISP</span><span class="topo-outside">VLLLLPLGYEVALGG</span><span class="topo-membrane">FIMCGVLFCLVSFI</span><span class="topo-inside">VKKAGTGWLDV</span><span class="topo-membrane">L</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">FPPAAMGAIVAVIGLELA</span><span class="topo-outside">GVAAGMAGLLPAEGQTPDSKTIIISIT</span><span class="topo-membrane">TLAVTVLGSVLFRG</span><span class="topo-unknown">F</span><span class="topo-membrane">LAIIPILIGVLV</span><span class="topo-outside">GYALSFAMGIVDTTPIINAHWFALPTLYTPRFEWFAI</span><span class="topo-membrane">LTILPAALVVI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">AEHVGH</span><span class="topo-inside">LVVTANIVKKDLLRDPGLH</span><span class="topo-membrane">RSMFANGLSTVISG</span><span class="topo-outside">FFGS</span><span class="topo-membrane">TPNTTYGENIGV</span><span class="topo-inside">MAITRVYST</span><span class="topo-membrane">WVIGGAAIFAILLS</span><span class="topo-outside">CVPKLAAAIQMIPLPVMGG</span><span class="topo-membrane">VSLLLYGVIGASGIRVLI</span><span class="topo-inside">ESKVD</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       </span>
<span class="topo-line"><span class="topo-inside">YNKA</span><span class="topo-membrane">QNLILTSVILIIGVS</span><span class="topo-outside">GAKVNIGAAELKG</span><span class="topo-membrane">MALATIVGIGLSLIFKLI</span><span class="topo-inside">SVL</span><span class="topo-unknown">RPEEVVLDAEDADITDKALEVLFQ</span></span>
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
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>15</td>
      <td>3</td>
      <td>14</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>36</td>
      <td>15</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>37</td>
      <td>47</td>
      <td>36</td>
      <td>46</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>62</td>
      <td>47</td>
      <td>61</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>67</td>
      <td>62</td>
      <td>66</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>79</td>
      <td>67</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>94</td>
      <td>79</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>108</td>
      <td>94</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>119</td>
      <td>108</td>
      <td>118</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>120</td>
      <td>138</td>
      <td>119</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>165</td>
      <td>138</td>
      <td>164</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>179</td>
      <td>165</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>181</td>
      <td>192</td>
      <td>180</td>
      <td>191</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>193</td>
      <td>229</td>
      <td>192</td>
      <td>228</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>230</td>
      <td>246</td>
      <td>229</td>
      <td>245</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>247</td>
      <td>265</td>
      <td>246</td>
      <td>264</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>266</td>
      <td>279</td>
      <td>265</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>283</td>
      <td>279</td>
      <td>282</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>295</td>
      <td>283</td>
      <td>294</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>296</td>
      <td>304</td>
      <td>295</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>305</td>
      <td>318</td>
      <td>304</td>
      <td>317</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>319</td>
      <td>337</td>
      <td>318</td>
      <td>336</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>355</td>
      <td>337</td>
      <td>354</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>356</td>
      <td>364</td>
      <td>355</td>
      <td>363</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>365</td>
      <td>379</td>
      <td>364</td>
      <td>378</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>380</td>
      <td>392</td>
      <td>379</td>
      <td>391</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>393</td>
      <td>410</td>
      <td>392</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>413</td>
      <td>410</td>
      <td>412</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>414</td>
      <td>437</td>
      <td>413</td>
      <td>436</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8omz">8OMZ</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GS</span><span class="topo-inside">SSQVQLVESGGGSVQAGGSLRLSCAASGNIAYIHYLGWFRQAPGKEREGVAALSTTLGNTYYADSVKGRFTVSLDNAKNTVYLQMNSLKPEDTALYYCAAAYFGYSSPLAHERYMYWG</span></span>
<span class="topo-ruler">       130       140       150    </span>
<span class="topo-line"><span class="topo-inside">QGTQVTVSA</span><span class="topo-unknown">GRAGEQKLISEEDLNSAVDHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>2</td>
      <td>-3</td>
      <td>-2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>129</td>
      <td>-1</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>154</td>
      <td>126</td>
      <td>150</td>
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

### Novel structural fold of NAT/NCS2 transporters

UraA revealed a novel fold not seen in any previously determined membrane protein structure. The 14 TMs are arranged into two inverted repeats (TMs 1-7 and TMs 8-14). A pair of short antiparallel beta-strands located between TM3 and TM10 serves as an organizing center for the core domain, providing the structural basis for substrate recognition.

### Uracil recognition and binding mechanism

[URACIL](/xray-mp-wiki/reagents/ligands/uracil/) is coordinated primarily by residues from the core domain. Two Glu residues (Glu241 and Glu290) anchor [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) by each making two hydrogen bonds. The backbone amide nitrogen atoms of Phe73 and Gly289 form additional hydrogen bonds with the two oxygen atoms of [URACIL](/xray-mp-wiki/reagents/ligands/uracil/). His245 contributes indirectly via a water-mediated hydrogen bond (the hydroxyl of beta-NG in the crystal structure mimics a water molecule at this position). Van der Waals interactions involve Ala31, Phe73, Tyr288, and Tyr342. Phe73 blocks [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) access from the periplasm. Mutation of Glu241, His245, or Glu290 to Ala abrogates both [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) binding and transport.

### Domain architecture and alternating access mechanism

UraA is organized into a core domain (TMs 1-4, 8-11) and a gate domain (TMs 5-7, 12-14). The interface between the two domains forms the uracil-binding pocket. Structural analysis suggests alternating access of the substrate is achieved through conformational changes of the gate domain relative to the core domain around the bound [URACIL](/xray-mp-wiki/reagents/ligands/uracil/). The core domain provides substrate selectivity and proton/sodium translocation, while gate domain conformational changes enable substrate transport.

### Proton coupling mechanism

UraA is a proton-coupled symporter. Glu241, His245, and Glu290, all capable of protonation/deprotonation, are clustered at the core-gate interface and are essential for [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) binding. The proposed model suggests that substrate-free UraA is outward-open with deprotonated Glu residues. Upon [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) and H+ binding, at least one Glu is protonated, triggering gate domain closure to the inward-open conformation as seen in the structure. Proton translocation likely occurs from Glu to His245 and onward into the cytoplasm. In sodium symporters of the NAT family, Na+ neutralizes conserved Glu/Asp residues for substrate binding instead of protons.

### Dimeric assembly and monomer-dimer equilibrium

UraA forms a homodimer in the crystal structure wherein the gate domains are sandwiched by two core domains. The dimerization interface involves approximately 2400 A^2 buried surface area, mediated through the gate domains with extensive hydrophobic residues on TMs 5/12/13. [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) in multiple detergents ([DDM](/xray-mp-wiki/reagents/detergents/ddm/), [LDAO](/xray-mp-wiki/reagents/detergents/ldao/), NG) shows UraA elutes in two peaks, suggesting equilibrium between monomer and dimer. Crosslinking and [Static Light Scattering](/xray-mp-wiki/methods/quality-assessment/static-light-scattering/) confirm that wild-type UraA exists in monomer-dimer equilibrium.

### Dimerization is required for transport activity

Monomeric mutants M1 (L366W & I374W) and M2 (A137W & I374W) bind [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) with similar affinity to wild-type, confirming correct folding. However, transport activity is nearly abolished in the monomeric mutants in cell-based [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) uptake assays. The constitutive dimer exhibits 70% higher transport activity than wild-type. Intriguingly, dimers containing one functional and one loss-of-function protomer (E241A or H245A) show similar Km and Vmax to the constitutive dimer, suggesting one functional protomer is sufficient for transport.

### Conformational changes between inward-open and occluded states

Structural comparison between the inward-open (UraA_IO, PDB 3QE7) and occluded (UraA_Occ) conformations reveals pronounced relative motions between the core and gate domains. The core domain remains rigid while the gate domain undergoes inter- and intra-domain shifts. TM5 and TM12 rotate around an axis perpendicular to the core-gate domain interface and bend in the occluded state, with a more prominent kink in TM5. The periplasmic segment of TM5 moves towards the core domain while the cytoplasmic segment of TM12 is displaced away, resulting in the switch from occluded to inward-open state.

### Interdomain-linkers control conformational transitions in elevator transport

A wide inward-open conformation of UraA (UraA_WIO) was resolved by crystallizing the G320P mutant in complex with synthetic [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) Sy45. Comparison of UraA_WIO with the occluded state (UraA_OCC) reveals that the interdomain-linkers (TM4-5 and TM11-12) are not mere tethers but actively define the rotation axis and conformational space of the transport domain. The linkers consist of short amphipathic spacer helices flanked by conserved [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) (flexible, near transport domain) and proline (rigid, near scaffold domain) residues. Mutation of these residues (G112P, P121G, G320P, P330G) severely compromises [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) transport.

### G320P and P330G mutations differentially affect conformational equilibrium

The G320P mutation in the external interdomain-linker shifts the conformational equilibrium away from the inward-open state toward a more outward-open conformation, while P330G constrains the transporter toward an occluded-like state with strongly reduced surface exposure of both internal and external cavities. Both mutants bind [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) with increased affinity (up to 20-fold for P330G) despite being transport incompetent, suggesting they are trapped in specific conformational states. Hydrogen-deuterium exchange mass spectrometry ([HDX-MS](/xray-mp-wiki/methods/quality-assessment/hdx-ms/)) and cysteine alkylation experiments confirm altered conformational dynamics.

### Functional relevance of spacer helix architecture

The short interdomain-linkers in UraA contain alpha-helical spacer helices flanked by [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) and proline residues that act as molecular hinges. The conserved proline near the scaffold domain (P121 in cytoplasmic linker, P330 in external linker) fixes the orientation of the spacer helix relative to the scaffold. The conserved [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) near the transport domain (G112, G320) provides flexibility during the elevator motion. This architecture defines the rotation axis, which runs approximately parallel to scaffold helices TM5 and TM12, resulting in a nearly orthogonal displacement of the substrate binding site for shortest translocation path. Interdomain-linkers with similar spacer helix architecture are observed in other elevator transporters (SLC4, SLC13, SLC26 families).


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — UraA operates by alternating access between inward-open and occluded conformations
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/elevator-mechanism/">Elevator Mechanism</a> — UraA core domain exhibits elevator-like movement relative to the dimeric gate domain
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/rocker-switch-mechanism/">Rocker-Switch Mechanism</a> — Rocking bundle motions of gate domains contribute to alternating access in UraA
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent used for UraA membrane solubilization and purification
- <a href="/xray-mp-wiki/reagents/detergents/ldao/">Lauryl Dimethylamine N-Oxide (LDAO)</a> — Detergent used for SEC analysis of UraA oligomerization state
- <a href="/xray-mp-wiki/reagents/ligands/uracil/">Uracil</a> — Substrate of UraA, binds in the occluded conformation
- <a href="/xray-mp-wiki/reagents/detergents/fos-choline-9/">Fos-Choline 9 (FC-9)</a> — Detergent used for UraA crystallization
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/substrate-protonation-coupling/">Substrate-Protonation Coupling</a> — UraA couples uracil transport to proton translocation
- <a href="/xray-mp-wiki/methods/cell-lysis/french-press/">French Press Cell Lysis</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
