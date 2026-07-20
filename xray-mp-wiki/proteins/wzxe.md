---
title: "WzxE - Lipid III Flippase from Escherichia coli"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1098##rsob.240310]
verified: agent
uniprot_id: P0AAA7
---

# WzxE - Lipid III Flippase from Escherichia coli

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P0AAA7">UniProt: P0AAA7</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

WzxE is the lipid III flippase from Escherichia coli, responsible for translocating
the enterobacterial common antigen (ECA) lipid-linked repeat unit (lipid III,
und-PP-GlcNAc-ManNAcA-Fuc4NAc) across the inner membrane. WzxE belongs to the
multidrug and toxic compound extrusion (MATE) family of transporters and is part
of the Wzx/Wzy-dependent polysaccharide export pathway. The first X-ray crystal
structures of WzxE, determined in complex with nanobodies Nb7 and Nb10, revealed
both outward-facing (2.31 A) and inward-facing (2.80 A) conformations. Each
structure comprises 12 transmembrane helices arranged as N- and C-terminal
six-helix bundles characteristic of the MATE fold. The conformational switch
between inward- and outward-facing states is mediated by a ~23 degree rotation of
transmembrane helix 7. A conserved arginine triad (R44-R239-D262) and a
C-terminal arginine cluster (R413-R415) are critical for lipid III recognition
and transport. WzxE shows high structural similarity to [NorM-VC (Vibrio cholerae NorM) - MATE Family Multidrug Efflux Transporter](/xray-mp-wiki/proteins/abc-transporters/norM-vc/) (RMSD 1.2 A over
533 residues) and the lipid II flippase [MURJ](/xray-mp-wiki/proteins/abc-transporters/murj/).

## Publications

### doi/10.1098##rsob.240310

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/9g95">9G95</a></td>
      <td>2.80</td>
      <td>C2</td>
      <td>Full-length WzxE from E. coli with Nb10 <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a>, I23 S-SAD phasing</td>
      <td>sulfate, zinc</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/9g97">9G97</a></td>
      <td>2.31</td>
      <td>C2</td>
      <td>Full-length WzxE from E. coli with Nb10 <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a>, I24 native</td>
      <td>sulfate, zinc</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/9g9m">9G9M</a></td>
      <td>2.55</td>
      <td>C2221</td>
      <td>Full-length WzxE from E. coli with Nb10 and Nb7 nanobodies, outward-facing</td>
      <td>sulfate, zinc</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/9g90">9G90</a></td>
      <td>2.69</td>
      <td>C2221</td>
      <td>Full-length WzxE from E. coli with Nb10 and Nb7 nanobodies, outward-facing</td>
      <td>sulfate, zinc</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/9g9n">9G9N</a></td>
      <td>2.80</td>
      <td>C2221</td>
      <td>Full-length WzxE from E. coli with Nb10 and Nb7 nanobodies, inward-facing (occluded)</td>
      <td>sulfate, zinc</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/9g9p">9G9P</a></td>
      <td>2.80</td>
      <td>C2221</td>
      <td>Full-length WzxE from E. coli with Nb10 and Nb7 nanobodies, inward-facing (occluded)</td>
      <td>sulfate, zinc</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length WzxE from E. coli K-12 genome, cloned into pET-based vector with TEV-cleavable C-terminal His10 tag

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
      <td>Cell lysis by Emulsiflex, differential centrifugation</td>
      <td>—</td>
      <td>25 mM Tris pH 7.5, 150 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> (v/v) + --</td>
      <td></td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Overnight detergent extraction at 4 C</td>
      <td>—</td>
      <td>25 mM Tris pH 7.5, 150 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> (v/v) + 1.5% (w/v) <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> (DM)</td>
      <td></td>
    </tr>
    <tr>
      <td>Ni-NTA affinity</td>
      <td>Batch binding onto <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> resin</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> resin (ABT)</td>
      <td>25 mM Tris pH 7.5, 150 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> (v/v) + 0.058% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ogng/">OGNG</a> + 0.008% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Washed with 20 mM and 35 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>; eluted with 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Desalting</td>
      <td>CentriPure P100 desalting column</td>
      <td>—</td>
      <td>25 mM Tris pH 7.5, 150 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> (v/v), 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 0.058% <a href="/xray-mp-wiki/reagents/detergents/ogng/">OGNG</a> + 0.008% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td></td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td>Overnight <a href="/xray-mp-wiki/reagents/enzymes/tev-protease/">TEV</a> protease digestion</td>
      <td>—</td>
      <td>25 mM Tris pH 7.5, 150 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> (v/v), 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 0.058% <a href="/xray-mp-wiki/reagents/detergents/ogng/">OGNG</a> + 0.008% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td></td>
    </tr>
    <tr>
      <td>Reverse IMAC</td>
      <td>Reverse immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> resin (ABT)</td>
      <td>25 mM Tris pH 7.5, 150 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> (v/v) + 0.058% <a href="/xray-mp-wiki/reagents/detergents/ogng/">OGNG</a> + 0.008% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Flow-through collected (<a href="/xray-mp-wiki/reagents/enzymes/tev-protease/">TEV</a>-cleaved protein does not bind)</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td>HiLoad 16/600 Superose 6</td>
      <td>—</td>
      <td>25 mM Tris pH 7.5, 150 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> (v/v) + 0.058% <a href="/xray-mp-wiki/reagents/detergents/ogng/">OGNG</a> + 0.008% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>WzxE-Nb10 complex peak pooled and concentrated using 100 kDa MWCO</td>
    </tr>
  </tbody>
</table>
**Final sample**: Concentrated WzxE-Nb10 complex in buffer B (25 mM Tris pH 7.5, 150 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.058% [OGNG](/xray-mp-wiki/reagents/detergents/ogng/), 0.008% [DDM](/xray-mp-wiki/reagents/detergents/ddm/))

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipid cubic phase (LCP) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>WzxE-Nb10 complex in buffer B, mixed with <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a>:ECP lipid mixture at 1:1 (v/v)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2-3 months for full size (~10 um)</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals harvested from LCP; 15% <a href="/xray-mp-wiki/reagents/lipids/e-coli-polar-lipids/">E. coli Polar Lipids</a> in <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Outward-facing conformation (WzxE-Nb10, PDB 9G97, 2.31 A). Initial hit appeared after 1 week. 15% <a href="/xray-mp-wiki/reagents/lipids/e-coli-polar-lipids/">E. coli Polar Lipids</a> added to <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> improved reproducibility. <a href="/xray-mp-wiki/reagents/additives/zinc-chloride/">Zinc Chloride</a> added to precipitant for larger crystals. S-SAD phasing at 2.7552 A on I23 beamline. Native data at 0.9688 A on I24 beamline.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>LCP crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>WzxE-Nb10-Nb7 complex (1.2-fold molar excess of Nb7) with 2 mM und-PP-GlcNAc substrate</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2-3 months</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Inward-facing conformation (PDB 9G9N, 2.80 A). Substrate added to protein for 16 h at 4 C with sonication. Outward-facing WzxE-Nb10-Nb7 (PDB 9G9M, 2.55 A) obtained in 0.1 M sodium <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> pH 5, 0.1 M <a href="/xray-mp-wiki/reagents/additives/lithium-sulfate/">Lithium Sulfate</a>, 0.1 M <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 30% (v/v) <a href="/xray-mp-wiki/reagents/additives/peg300/">PEG300</a> from MemMeso screen.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/9g95">9G95</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">VSL</span><span class="topo-membrane">AKASLWTAASTLVKIGAGLLVG</span><span class="topo-outside">KLLAVSFGPAGLGLAAN</span><span class="topo-membrane">FRQLITVLGVLAGAGIFNGVT</span><span class="topo-inside">KYVAQYHDNPQQLRRVVGTS</span><span class="topo-membrane">SAMVLGFSTLMALVFVLAAAPIS</span><span class="topo-outside">QGLFGNTDYQ</span><span class="topo-membrane">GLV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">RLVALVQMGIAWGNLLLALMK</span><span class="topo-inside">GFRDA</span><span class="topo-membrane">AGNALSLIVGSLIGVLAYYVSY</span><span class="topo-outside">RLGGYEG</span><span class="topo-membrane">ALLGLALIPALVVIPAAIML</span><span class="topo-inside">IKRGVIPLSYLKPSWDNGLAGQL</span><span class="topo-membrane">SKFTLMALITSVTLPVAYIMM</span><span class="topo-outside">R</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">KLLAAQYSWDEVGIWQ</span><span class="topo-membrane">GVSSISDAYLQFITASFSVYLL</span><span class="topo-inside">PTLSRLTEKRDITREVVKS</span><span class="topo-membrane">LKFVLPAVAAASFTVWLLR</span><span class="topo-outside">DFAIWLLLSNKFTAMRDL</span><span class="topo-membrane">FAWQLVGDVLKVGAYVFGYLVI</span><span class="topo-inside">AKA</span><span class="topo-membrane">S</span></span>
<span class="topo-ruler">       370       380       390       400       410       420     </span>
<span class="topo-line"><span class="topo-membrane">LRFYILAEVSQFTLLMVFAHWL</span><span class="topo-outside">IPAHGALG</span><span class="topo-membrane">AAQAYMATYIVYFSLCCGVF</span><span class="topo-inside">LLWRRRALE</span><span class="topo-unknown">ENLYFQ</span></span>
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
      <td>2</td>
      <td>4</td>
      <td>1</td>
      <td>3</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>26</td>
      <td>4</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>43</td>
      <td>26</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>64</td>
      <td>43</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>84</td>
      <td>64</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>107</td>
      <td>84</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>117</td>
      <td>107</td>
      <td>116</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>141</td>
      <td>117</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>146</td>
      <td>141</td>
      <td>145</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>168</td>
      <td>146</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>175</td>
      <td>168</td>
      <td>174</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>195</td>
      <td>175</td>
      <td>194</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>218</td>
      <td>195</td>
      <td>217</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>219</td>
      <td>239</td>
      <td>218</td>
      <td>238</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>240</td>
      <td>256</td>
      <td>239</td>
      <td>255</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>257</td>
      <td>278</td>
      <td>256</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>297</td>
      <td>278</td>
      <td>296</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>298</td>
      <td>316</td>
      <td>297</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>317</td>
      <td>334</td>
      <td>316</td>
      <td>333</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>335</td>
      <td>356</td>
      <td>334</td>
      <td>355</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>359</td>
      <td>356</td>
      <td>358</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>360</td>
      <td>382</td>
      <td>359</td>
      <td>381</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>390</td>
      <td>382</td>
      <td>389</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>391</td>
      <td>410</td>
      <td>390</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>419</td>
      <td>410</td>
      <td>418</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>420</td>
      <td>425</td>
      <td>419</td>
      <td>424</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/9g97">9G97</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">VSLAKA</span><span class="topo-membrane">SLWTAASTLVKIGAGLLVGKL</span><span class="topo-outside">LAVSFGPAGLGLAAN</span><span class="topo-membrane">FRQLITVLGVLAGAGIFNGVT</span><span class="topo-inside">KYVAQYHDNPQQLRRVVGTS</span><span class="topo-membrane">SAMVLGFSTLMALVFVLAA</span><span class="topo-outside">APISQGLFGNTDYQG</span><span class="topo-membrane">LV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">RLVALVQMGIAWGNLLLAL</span><span class="topo-inside">MKGFRDA</span><span class="topo-membrane">AGNALSLIVGSLIGVLAYYVSYRL</span><span class="topo-outside">GGYEG</span><span class="topo-membrane">ALLGLALIPALVVIPAAIM</span><span class="topo-inside">LIKRGVIPLSYLKPSWDNGLA</span><span class="topo-membrane">GQLSKFTLMALITSVTLPVAYIMM</span><span class="topo-outside">R</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">KLLAAQYSWDEVGIW</span><span class="topo-membrane">QGVSSISDAYLQFITASFSV</span><span class="topo-inside">YLLPTLSRLTEKRDITREVVKSLKF</span><span class="topo-membrane">VLPAVAAASFTVWLLRDFAIWLLL</span><span class="topo-outside">SNKFTAM</span><span class="topo-membrane">RDLFAWQLVGDVLKVGAYVFGYLVI</span><span class="topo-inside">AKA</span><span class="topo-membrane">S</span></span>
<span class="topo-ruler">       370       380       390       400       410       420     </span>
<span class="topo-line"><span class="topo-membrane">LRFYILAEVSQFTLLMVFAHWLI</span><span class="topo-outside">PAHGAL</span><span class="topo-membrane">GAAQAYMATYIVYFSLCCGV</span><span class="topo-inside">FLLWRRRALE</span><span class="topo-unknown">ENLYFQ</span></span>
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
      <td>2</td>
      <td>7</td>
      <td>1</td>
      <td>6</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>28</td>
      <td>7</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>43</td>
      <td>28</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>64</td>
      <td>43</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>84</td>
      <td>64</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>103</td>
      <td>84</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>104</td>
      <td>118</td>
      <td>103</td>
      <td>117</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>139</td>
      <td>118</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>140</td>
      <td>146</td>
      <td>139</td>
      <td>145</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>170</td>
      <td>146</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>171</td>
      <td>175</td>
      <td>170</td>
      <td>174</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>194</td>
      <td>175</td>
      <td>193</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>195</td>
      <td>215</td>
      <td>194</td>
      <td>214</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>239</td>
      <td>215</td>
      <td>238</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>240</td>
      <td>255</td>
      <td>239</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>275</td>
      <td>255</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>300</td>
      <td>275</td>
      <td>299</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>301</td>
      <td>324</td>
      <td>300</td>
      <td>323</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>325</td>
      <td>331</td>
      <td>324</td>
      <td>330</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>332</td>
      <td>356</td>
      <td>331</td>
      <td>355</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>359</td>
      <td>356</td>
      <td>358</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>360</td>
      <td>383</td>
      <td>359</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>389</td>
      <td>383</td>
      <td>388</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>409</td>
      <td>389</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>419</td>
      <td>409</td>
      <td>418</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>420</td>
      <td>425</td>
      <td>419</td>
      <td>424</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/9g9m">9G9M</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">VSL</span><span class="topo-membrane">AKASLWTAASTLVKIGAGLLVG</span><span class="topo-outside">KLLAVSFGPAGLGLAA</span><span class="topo-membrane">NFRQLITVLGVLAGAGIFNGVT</span><span class="topo-inside">KYVAQYHDNPQQLRRVVGTS</span><span class="topo-membrane">SAMVLGFSTLMALVFVLAAAPIS</span><span class="topo-outside">QGLFGNTDY</span><span class="topo-membrane">QGLV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">RLVALVQMGIAWGNLLLALMK</span><span class="topo-inside">GFRD</span><span class="topo-membrane">AAGNALSLIVGSLIGVLAYYVSY</span><span class="topo-outside">RLGGYEG</span><span class="topo-membrane">ALLGLALIPALVVIPAAIMLIK</span><span class="topo-inside">RGVIPLSYLKPSWDNGLAGQL</span><span class="topo-membrane">SKFTLMALITSVTLPVAYIMMR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">KL</span><span class="topo-outside">LAAQYSWDEVGIW</span><span class="topo-membrane">QGVSSISDAYLQFITASFSVYLL</span><span class="topo-inside">PTLSRLTEKRDITREV</span><span class="topo-membrane">VKSLKFVLPAVAAASFTVWLLR</span><span class="topo-outside">DFAIWLLLSNKFTAMRD</span><span class="topo-membrane">LFAWQLVGDVLKVGAYVFGYLVI</span><span class="topo-inside">AKAS</span></span>
<span class="topo-ruler">       370       380       390       400       410       420     </span>
<span class="topo-line"><span class="topo-membrane">LRFYILAEVSQFTLLMVFAHWLI</span><span class="topo-outside">PAHGAL</span><span class="topo-membrane">GAAQAYMATYIVYFSLCCGVF</span><span class="topo-inside">LLWRRR</span><span class="topo-unknown">ALEENLYFQ</span></span>
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
      <td>2</td>
      <td>4</td>
      <td>1</td>
      <td>3</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>26</td>
      <td>4</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>42</td>
      <td>26</td>
      <td>41</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>64</td>
      <td>42</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>84</td>
      <td>64</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>107</td>
      <td>84</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>116</td>
      <td>107</td>
      <td>115</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>141</td>
      <td>116</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>145</td>
      <td>141</td>
      <td>144</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>146</td>
      <td>168</td>
      <td>145</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>175</td>
      <td>168</td>
      <td>174</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>197</td>
      <td>175</td>
      <td>196</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>218</td>
      <td>197</td>
      <td>217</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>219</td>
      <td>242</td>
      <td>218</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>255</td>
      <td>242</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>278</td>
      <td>255</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>294</td>
      <td>278</td>
      <td>293</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>316</td>
      <td>294</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>317</td>
      <td>333</td>
      <td>316</td>
      <td>332</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>334</td>
      <td>356</td>
      <td>333</td>
      <td>355</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>360</td>
      <td>356</td>
      <td>359</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>361</td>
      <td>383</td>
      <td>360</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>389</td>
      <td>383</td>
      <td>388</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>410</td>
      <td>389</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>416</td>
      <td>410</td>
      <td>415</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>417</td>
      <td>425</td>
      <td>416</td>
      <td>424</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/9g9n">9G9N</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MVSLAK</span><span class="topo-outside">ASL</span><span class="topo-membrane">WTAASTLVKIGAGLLVGKLL</span><span class="topo-inside">AVSFGPAGLGLA</span><span class="topo-membrane">ANFRQLITVLGVLAGAGIFN</span><span class="topo-outside">GVTKYVAQYHDNPQQLRRVVGTS</span><span class="topo-membrane">SAMVLGFSTLMALVFVLAAAPIS</span><span class="topo-inside">QGLFGNTDYQ</span><span class="topo-membrane">GLV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">RLVALVQMGIAWGNLLLA</span><span class="topo-outside">LMKGFRDAA</span><span class="topo-membrane">GNALSLIVGSLIGVLAYYVSY</span><span class="topo-inside">RLGGYEG</span><span class="topo-membrane">ALLGLALIPALVVIPAAIML</span><span class="topo-outside">IKRGVIPLSYLKPSWDNGLAGQLS</span><span class="topo-membrane">KFTLMALITSVTLPVAYIMMR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">KLLAAQYSWDEVGIW</span><span class="topo-membrane">QGVSSISDAYLQFITASFSV</span><span class="topo-outside">YLLPTLSRLTEKRDITREV</span><span class="topo-membrane">VKSLKFVLPAVAAASFTVWLLR</span><span class="topo-inside">DFAIWLLLSNKFTAMRDL</span><span class="topo-membrane">FAWQLVGDVLKVGAYVFGYLVI</span><span class="topo-outside">AKAS</span></span>
<span class="topo-ruler">       370       380       390       400       410       420     </span>
<span class="topo-line"><span class="topo-membrane">LRFYILAEVSQFTLLMVFAH</span><span class="topo-inside">WLIPAHGALGA</span><span class="topo-membrane">AQAYMATYIVYFSLCCGVFLLW</span><span class="topo-outside">RRRA</span><span class="topo-unknown">LEENLYFQ</span></span>
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
      <td>6</td>
      <td>0</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>7</td>
      <td>9</td>
      <td>6</td>
      <td>8</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>29</td>
      <td>9</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>41</td>
      <td>29</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>61</td>
      <td>41</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>84</td>
      <td>61</td>
      <td>83</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>107</td>
      <td>84</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>117</td>
      <td>107</td>
      <td>116</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>138</td>
      <td>117</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>147</td>
      <td>138</td>
      <td>146</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>168</td>
      <td>147</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>175</td>
      <td>168</td>
      <td>174</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>195</td>
      <td>175</td>
      <td>194</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>219</td>
      <td>195</td>
      <td>218</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>240</td>
      <td>219</td>
      <td>239</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>255</td>
      <td>240</td>
      <td>254</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>275</td>
      <td>255</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>294</td>
      <td>275</td>
      <td>293</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>316</td>
      <td>294</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>317</td>
      <td>334</td>
      <td>316</td>
      <td>333</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>335</td>
      <td>356</td>
      <td>334</td>
      <td>355</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>360</td>
      <td>356</td>
      <td>359</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>361</td>
      <td>380</td>
      <td>360</td>
      <td>379</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>381</td>
      <td>391</td>
      <td>380</td>
      <td>390</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>392</td>
      <td>413</td>
      <td>391</td>
      <td>412</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>414</td>
      <td>417</td>
      <td>413</td>
      <td>416</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>418</td>
      <td>425</td>
      <td>417</td>
      <td>424</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/9g9p">9G9P</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MVSLAK</span><span class="topo-inside">ASL</span><span class="topo-membrane">WTAASTLVKIGAGLLVGKLLA</span><span class="topo-outside">VSFGPAGLGLA</span><span class="topo-membrane">ANFRQLITVLGVLAGAGIFN</span><span class="topo-inside">GVTKYVAQYHDNPQQLRRVVGTS</span><span class="topo-membrane">SAMVLGFSTLMALVFVLAAAPIS</span><span class="topo-outside">QGLFGNTDYQ</span><span class="topo-membrane">GLV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">RLVALVQMGIAWGNLLLA</span><span class="topo-inside">LMKGFRDAAG</span><span class="topo-membrane">NALSLIVGSLIGVLAYYVSY</span><span class="topo-outside">RLGGYEG</span><span class="topo-membrane">ALLGLALIPALVVIPAAIMLI</span><span class="topo-inside">KRGVIPLSYLKPSWDNGLAGQLS</span><span class="topo-membrane">KFTLMALITSVTLPVAYIMMR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">K</span><span class="topo-outside">LLAAQYSWDEVGIW</span><span class="topo-membrane">QGVSSISDAYLQFITASFS</span><span class="topo-inside">VYLLPTLSRLTEKRDITREVVKSL</span><span class="topo-membrane">KFVLPAVAAASFTVWLLRDFAI</span><span class="topo-outside">WLLLSNKFTAM</span><span class="topo-membrane">RDLFAWQLVGDVLKVGAYVFGY</span><span class="topo-inside">LVIAKAS</span></span>
<span class="topo-ruler">       370       380       390       400       410       420     </span>
<span class="topo-line"><span class="topo-inside">L</span><span class="topo-membrane">RFYILAEVSQFTLLMVFAHWL</span><span class="topo-outside">IPAHGAL</span><span class="topo-membrane">GAAQAYMATYIVYFSLCCGVF</span><span class="topo-inside">LLWRR</span><span class="topo-unknown">RALEENLYFQ</span></span>
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
      <td>6</td>
      <td>0</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>7</td>
      <td>9</td>
      <td>6</td>
      <td>8</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>30</td>
      <td>9</td>
      <td>29</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>41</td>
      <td>30</td>
      <td>40</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>61</td>
      <td>41</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>84</td>
      <td>61</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>107</td>
      <td>84</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>117</td>
      <td>107</td>
      <td>116</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>138</td>
      <td>117</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>148</td>
      <td>138</td>
      <td>147</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>168</td>
      <td>148</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>175</td>
      <td>168</td>
      <td>174</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>196</td>
      <td>175</td>
      <td>195</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>219</td>
      <td>196</td>
      <td>218</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>241</td>
      <td>219</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>242</td>
      <td>255</td>
      <td>241</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>274</td>
      <td>255</td>
      <td>273</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>298</td>
      <td>274</td>
      <td>297</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>299</td>
      <td>320</td>
      <td>298</td>
      <td>319</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>321</td>
      <td>331</td>
      <td>320</td>
      <td>330</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>332</td>
      <td>353</td>
      <td>331</td>
      <td>352</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>354</td>
      <td>361</td>
      <td>353</td>
      <td>360</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>362</td>
      <td>382</td>
      <td>361</td>
      <td>381</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>389</td>
      <td>382</td>
      <td>388</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>410</td>
      <td>389</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>415</td>
      <td>410</td>
      <td>414</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>416</td>
      <td>425</td>
      <td>415</td>
      <td>424</td>
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

### First crystal structure of WzxE reveals MATE family fold

The first X-ray crystal structures of WzxE reveal a 12-transmembrane helix topology with N- and C-terminal six-helix bundles characteristic of the multidrug and toxic compound extrusion (MATE) family. Despite low sequence similarity (as low as 4.6% to MATE consensus), WzxE superimposes closely with [NorM-VC (Vibrio cholerae NorM) - MATE Family Multidrug Efflux Transporter](/xray-mp-wiki/proteins/abc-transporters/norM-vc/) (RMSD 1.2 A over 533 residues, PDB 3MKT). The structure clearly identifies WzxE as a member of the MATE family flippases, structurally similar to the lipid II flippase [MURJ](/xray-mp-wiki/proteins/abc-transporters/murj/) (RMSD 2.9 A over 351 residues). TM1 and TM7 extend across both bundles, while TM3 and TM9 contain kinks due to Pro104 and bulky hydrophobic residues (W312, W320, F317) respectively.

### Conformational switch between inward- and outward-facing states

WzxE was captured in both outward-facing (PDB 9G97, 2.31 A) and inward-facing (PDB 9G9N, 2.80 A) conformations. The transition between states is mediated by a ~23 degree rotation of TM7 starting at residue N211, coupled with bending of TM1 at G19. Each helical bundle (N- and C-lobe) remains structurally conserved (max RMSD 0.76 A), with the change occurring in their spatial arrangement (max RMSD 4.56 A over 360 residues). The disordered TM2 region (residues 54-57, 54AGAG57) may play a role in substrate recognition.

### Arg-triad and C-terminal cluster critical for function

The central cavity contains positively charged residues at both cytoplasmic (K64, R143, R282) and periplasmic (R44, R239, K326) surfaces. Mutagenesis showed R44A severely reduces ECA production, establishing R44 as critical for flippase activity. The conserved D262 residue forms a R44-R239-D262 triad analogous to the R24-D25-R255 triad in [MURJ](/xray-mp-wiki/proteins/abc-transporters/murj/). The C-terminal arginine cluster (R413-R415) is also essential; alanine mutations progressively reduce ECA production. R143A-R282A double mutant retained partial activity, suggesting the C-terminal cluster provides alternative binding.

### Proposed flipping mechanism for lipid III translocation

Based on the inward- and outward-facing structures, a flipping mechanism is proposed: (1) The C-terminal arginine cluster (R413-R415) initially recruits the pyrophosphate group of lipid III at the cytoplasmic face; (2) The pyrophosphate migrates to the cytoplasmic arginine pair (R143, R282) in the inward-facing conformation; (3) A network of carboxylate residues (D71, D288, E285) interacts with the three sugar moieties of ECA; (4) The pyrophosphate shifts to the periplasmic arginine pair (R44, R239) accompanied by the conformational switch to the outward-facing state; (5) The pyrophosphate moves to the positively charged cluster (R315, R331) at the periplasmic face for handoff to the polymerase WzyE.

### No evidence for proton or chloride antiport mechanism

Despite WzxE being proposed as a proton antiporter, the positively charged central lumen appears unlikely to promote proton transport, and no negatively charged patch spans the membrane. A chloride ion found in one WzxE structure was located on the external surface, unlike the central chloride proposed as a counter-ion in [MURJ](/xray-mp-wiki/proteins/abc-transporters/murj/). The data do not support a conserved chloride antiport mechanism for WzxE or MATE family flippases. The voltage difference across the membrane remains a possible source of activation energy, as proposed for [MURJ](/xray-mp-wiki/proteins/abc-transporters/murj/).

### Nanobody-based crystallization enabled structure determination

Crystallization of WzxE required complexation with two nanobodies (Nb7 and Nb10) generated by llama immunization. Nb10 binds at the periplasmic face of the N-terminal lobe, while Nb7 binds near the C-terminal lobe. The original structure was solved by sulfur SAD phasing using multi-crystal data at 2.7552 A on Diamond I23 beamline, involving 21 datasets from 4 crystals. The native structure was refined to 2.31 A using data from the I24 beamline. Only ~15% of tested crystals diffracted beyond 3 A, highlighting the challenging nature of this membrane protein.


## Cross-References

- <a href="/xray-mp-wiki/proteins/abc-transporters/murj/">MurJ (Lipid II Flippase from Escherichia coli)</a> — Structural homolog; both are MATE family flippases with similar mechanism
- <a href="/xray-mp-wiki/proteins/abc-transporters/norM-vc/">NorM-VC (Vibrio cholerae NorM)</a> — MATE family transporter; WzxE superimposes with RMSD 1.2 A
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Used in purification (0.008% DDM and 0.058% OGNG in buffer)
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase (LCP) Crystallization</a> — Crystallization method for WzxE
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">Ammonium Sulfate</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/lithium-sulfate/">Lithium Sulfate</a> — Additive used in purification or crystallization buffers
