---
title: "Melibiose Permease from Salmonella typhimurium (MelBSt)"
created: 2026-06-04
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms4009, doi/10.1038##s42003-021-02462-x]
verified: false
---

# Melibiose Permease from Salmonella typhimurium (MelBSt)

## Overview

[Melibiose](/xray-mp-wiki/reagents/ligands/melibiose) permease (MelB) from Salmonella typhimurium is a Na+-coupled sugar symporter belonging to the glycoside-pentoside-hexuronide:cation symporter family (TC 2.A.2), a subgroup of the Major Facilitator Superfamily ([MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/)). MelB catalyzes the electrogenic symport of galactosides coupled to Na+, Li+, or H+, transducing the free energy of downhill cation translocation to drive sugar accumulation against a concentration gradient. The protein shares >85% primary sequence identity with the well-studied E. coli MelB and adopts the typical [MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) fold of 12 transmembrane helices organized in two pseudo-symmetrical alpha-helical bundles. Crystal structures in two outward conformations reveal a previously unidentified pyramidal cation-binding site formed by three conserved acidic residues and illuminate the structural basis for Na+/melibiose symport and conformational cycling in [MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) transporters.


## Publications

### doi/10.1038##ncomms4009

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4m64">4M64</a></td>
      <td>3.35 A</td>
      <td>P3221</td>
      <td>Full-length MelBSt, Leu5->Met mutation, <a href="/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/">C-terminal</a> <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His10</a> tag</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/2npg">2NPG</a> (4-nitrophenyl-alpha-D-galactopyranoside)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli DW2 strain (melA+, delta melB, delta lacZY)
- **Construct**: Full-length MelBSt with Leu5->Met mutation and [C-terminal](/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/) [His10](/xray-mp-wiki/reagents/protein-tags/his6-tag/) tag

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
      <td>Cell culture and membrane preparation</td>
      <td>Fermentation and membrane fractionation</td>
      <td>not specified</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 7.5, 200 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a> + not specified</td>
      <td>Cells grown in LB broth with 50 mM KP(i), 45 mM (NH(4))(H(2)PO(4)), 0.5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 100 mg/L <a href="/xray-mp-wiki/reagents/antibiotics/ampicillin/">ampicillin</a> at 30 C. Membranes harvested by <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">ultracentrifugation</a> at 144,651 g for 3 h.</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>not specified</td>
      <td>not specified + 1.5% <a href="/xray-mp-wiki/reagents/detergents/udm/">UDM</a> (<a href="/xray-mp-wiki/reagents/detergents/udm">UDM</a>)</td>
      <td>Membranes at 14 mg/ml extracted with 1.5% <a href="/xray-mp-wiki/reagents/detergents/udm">UDM</a> followed by <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">ultracentrifugation</a> at 265,000 g for 30 min.</td>
    </tr>
    <tr>
      <td>Cobalt-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a> (<a href="/xray-mp-wiki/reagents/additives/talon/">Talon</a> resins)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">Talon</a> resins (cobalt-affinity)</td>
      <td>50 mM NaP(i) pH 7.6, 200 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 0.035% <a href="/xray-mp-wiki/reagents/detergents/udm">UDM</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> + 0.035% <a href="/xray-mp-wiki/reagents/detergents/udm">UDM</a></td>
      <td>Column pre-equilibrated with buffer containing 5 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a>. Wash with 35 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> buffer. Elution with 200 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a>.</td>
    </tr>
    <tr>
      <td>Concentration and dialysis</td>
      <td>Concentration and buffer exchange</td>
      <td>not specified</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 7.1, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a> + not specified</td>
      <td>Concentrated with VIVASPIN 20 (50 kDa cutoff), dialyzed twice against 1 L of buffer.</td>
    </tr>
  </tbody>
</table>
**Final sample**: MelBSt in 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.1, 100 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">hanging-drop</a> <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Phospholipid-treated MelBSt at 7 mg/ml with 5 mM <a href="/xray-mp-wiki/reagents/ligands/2npg">2NPG</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM <a href="/xray-mp-wiki/reagents/buffers/mops/">MOPS</a> pH 6.5, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 50 mM CaCl2, 35-37% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG 400</a>, 0.08% <a href="/xray-mp-wiki/reagents/detergents/octyl-beta-d-galactopyranoside">Octyl-beta-D-galactopyranoside</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>23 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">hanging-drop</a> <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a> method. Protein mixed 2 ul with 2 ul reservoir. Crystals frozen with liquid nitrogen. Data collected at ALS BL 5.0.2 (wavelength 1.004 A, 100 K). Asymmetric unit contains four molecules (Mol-ABCD) with twinning and pseudo-translation symmetries. Two conformations observed: outward partially occluded (Mol-A/C) and partial outward (Mol-B/D).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4m64">4M64</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MSISMTTKLSYG</span><span class="topo-membrane">FGAFGKDFAIGIVYMYLMYYYT</span><span class="topo-outside">DVVGLSVG</span><span class="topo-membrane">LVGTLFLVARIWDAINDPIM</span><span class="topo-inside">GWIVNATRSRWGKFKPWI</span><span class="topo-membrane">LIGTLTNSLVLFLLFSAHLFE</span><span class="topo-outside">GTAQ</span><span class="topo-membrane">VVFVCVTYILWGMTY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">TIMDIPFW</span><span class="topo-inside">SLVPTITLDKREREQLVPFPR</span><span class="topo-membrane">FFASLAGFVTAGITLPFVSYVG</span><span class="topo-outside">GADR</span><span class="topo-membrane">GFGFQMFTLVLIAFFIASTI</span><span class="topo-inside">VTLRNVHEVYSSDN</span><span class="topo-unknown">GVTAGRPHLTLKTIVGLIYKNDQ</span><span class="topo-inside">LSCL</span><span class="topo-membrane">LGMA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LAYNIASNIINGFAIYYF</span><span class="topo-outside">TYVIGDADL</span><span class="topo-membrane">FPYYLSYAGAANLLTLIVF</span><span class="topo-inside">PRLVKMLSRRILW</span><span class="topo-membrane">AGASVMPVLSCAGLFAM</span><span class="topo-outside">ALADIHNAA</span><span class="topo-membrane">LIVAAGIFLNIGTALFWV</span><span class="topo-inside">LQVIMVADTVDYGEFKL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">NIRCESIAY</span><span class="topo-membrane">SVQTMVVKGGSAFAAFFI</span><span class="topo-unknown">ALVLGL</span><span class="topo-outside">IGYTPNVAQSAQTLQ</span><span class="topo-membrane">GMQFIMIVLPVLFFMMTLVL</span><span class="topo-inside">YFRYYRLNGDMLRKIQIHLLD</span><span class="topo-unknown">KYRKTPPFVEQPDSPAISVVATSDVKAHHHH</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-unknown">HHHHHH</span></span>
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
      <td>12</td>
      <td>1</td>
      <td>12</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>34</td>
      <td>13</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>42</td>
      <td>35</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>62</td>
      <td>43</td>
      <td>62</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>80</td>
      <td>63</td>
      <td>80</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>101</td>
      <td>81</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>105</td>
      <td>102</td>
      <td>105</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>128</td>
      <td>106</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>149</td>
      <td>129</td>
      <td>149</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>150</td>
      <td>171</td>
      <td>150</td>
      <td>171</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>172</td>
      <td>175</td>
      <td>172</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>195</td>
      <td>176</td>
      <td>195</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>209</td>
      <td>196</td>
      <td>209</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>210</td>
      <td>232</td>
      <td>210</td>
      <td>232</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>233</td>
      <td>236</td>
      <td>233</td>
      <td>236</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>237</td>
      <td>258</td>
      <td>237</td>
      <td>258</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>259</td>
      <td>267</td>
      <td>259</td>
      <td>267</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>268</td>
      <td>286</td>
      <td>268</td>
      <td>286</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>287</td>
      <td>299</td>
      <td>287</td>
      <td>299</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>316</td>
      <td>300</td>
      <td>316</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>317</td>
      <td>325</td>
      <td>317</td>
      <td>325</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>343</td>
      <td>326</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>344</td>
      <td>369</td>
      <td>344</td>
      <td>369</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>370</td>
      <td>387</td>
      <td>370</td>
      <td>387</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>388</td>
      <td>393</td>
      <td>388</td>
      <td>393</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>394</td>
      <td>408</td>
      <td>394</td>
      <td>408</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>409</td>
      <td>428</td>
      <td>409</td>
      <td>428</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>429</td>
      <td>449</td>
      <td>429</td>
      <td>449</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>450</td>
      <td>486</td>
      <td>450</td>
      <td>486</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##s42003-021-02462-x

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7l17">7L17</a></td>
      <td>3.05 A</td>
      <td>P 31 2 1</td>
      <td>D59C MelB_St mutant with bound alpha-NPG</td>
      <td>alpha-NPG (4-nitrophenyl-alpha-D-galactopyranoside)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7l16">7L16</a></td>
      <td>3.15 A</td>
      <td>P 31 2 1</td>
      <td>D59C MelB_St mutant with bound DDMB (dodecyl-beta-D-melibioside)</td>
      <td>DDMB (dodecyl-beta-D-melibioside)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli DW2 strain (melA+, delta melB, delta lacZY)
- **Construct**: Full-length MelBSt with Leu5->Met mutation and [C-terminal](/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/) [His10](/xray-mp-wiki/reagents/protein-tags/his6-tag/) tag

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7l17">7L17</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">SISMTTKLSY</span><span class="topo-membrane">GFGAFGKDFAIGIVYMYLMYYY</span><span class="topo-inside">TDVVGLSVGL</span><span class="topo-membrane">VGTLFLVARIWDAINCPIMG</span><span class="topo-outside">WIVNATRSRWGKFKPW</span><span class="topo-membrane">ILIGTLTNSLVLFLLFSAHLF</span><span class="topo-inside">EGTA</span><span class="topo-membrane">QVVFVCVTYILWGMTYT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">IMDIPFW</span><span class="topo-outside">SLVPTITLDKREREQLV</span><span class="topo-membrane">PFPRFFASLAGFVTAGITLPFVSYVG</span><span class="topo-inside">GADRG</span><span class="topo-membrane">FGFQMFTLVLIAFFIASTIV</span><span class="topo-outside">TLRNVHEVYSSDNGVTAGRPHLT</span><span class="topo-unknown">LKTIVGLIYK</span><span class="topo-outside">NDQLS</span><span class="topo-membrane">CLLGMAL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">AYNIASNIINGFAI</span><span class="topo-inside">YYFTYVIGDADLF</span><span class="topo-membrane">PYYLSYAGAANLLTLIVF</span><span class="topo-unknown">PRLVKM</span><span class="topo-outside">LSR</span><span class="topo-membrane">RILWAGASVMPVLSCAGLFA</span><span class="topo-inside">MALADIHNAA</span><span class="topo-membrane">LIVAAGIFLNIGTALFWVLQV</span><span class="topo-outside">IMVADTVDYGEFKLN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">IRCESIAY</span><span class="topo-membrane">SVQTMVVKGGSAFAAFFIALV</span><span class="topo-inside">LGLIGYTPNVAQSAQTLQGMQF</span><span class="topo-membrane">IMIVLPVLFFMMTLVLYFRY</span><span class="topo-outside">YRLNGDMLRKIQIHLLDKYRKT</span><span class="topo-unknown">PPFVEQPDSPAISVVATSDVKAHHHHH</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-unknown">HHHHH</span></span>
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
      <td>10</td>
      <td>2</td>
      <td>11</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>32</td>
      <td>12</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>42</td>
      <td>34</td>
      <td>43</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>62</td>
      <td>44</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>78</td>
      <td>64</td>
      <td>79</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>99</td>
      <td>80</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>100</td>
      <td>103</td>
      <td>101</td>
      <td>104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>127</td>
      <td>105</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>128</td>
      <td>144</td>
      <td>129</td>
      <td>145</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>170</td>
      <td>146</td>
      <td>171</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>171</td>
      <td>175</td>
      <td>172</td>
      <td>176</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>195</td>
      <td>177</td>
      <td>196</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>218</td>
      <td>197</td>
      <td>219</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>219</td>
      <td>228</td>
      <td>220</td>
      <td>229</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>229</td>
      <td>233</td>
      <td>230</td>
      <td>234</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>254</td>
      <td>235</td>
      <td>255</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>255</td>
      <td>267</td>
      <td>256</td>
      <td>268</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>268</td>
      <td>285</td>
      <td>269</td>
      <td>286</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>286</td>
      <td>291</td>
      <td>287</td>
      <td>292</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>292</td>
      <td>294</td>
      <td>293</td>
      <td>295</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>314</td>
      <td>296</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>315</td>
      <td>324</td>
      <td>316</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>325</td>
      <td>345</td>
      <td>326</td>
      <td>346</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>346</td>
      <td>368</td>
      <td>347</td>
      <td>369</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>369</td>
      <td>389</td>
      <td>370</td>
      <td>390</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>390</td>
      <td>411</td>
      <td>391</td>
      <td>412</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>412</td>
      <td>431</td>
      <td>413</td>
      <td>432</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>432</td>
      <td>453</td>
      <td>433</td>
      <td>454</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7l16">7L16</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">SI</span><span class="topo-membrane">SMTTKLSYGFGAFGKDFAIGIVYMYLM</span><span class="topo-inside">YYYTDVVGLSVGLV</span><span class="topo-membrane">GTLFLVARIWDAINCPIMGWIVN</span><span class="topo-outside">ATRSRWGKF</span><span class="topo-membrane">KPWILIGTLTNSLVLFLLFSA</span><span class="topo-inside">HLFEGTA</span><span class="topo-membrane">QVVFVCVTYILWGMTYT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">IMDIPFWSLVP</span><span class="topo-outside">TITLDK</span><span class="topo-membrane">REREQLVPFPRFFASLAGFVTAGIT</span><span class="topo-unknown">LPFVSY</span><span class="topo-inside">VGGADRG</span><span class="topo-membrane">FGFQMFTLVLIAFFIASTIVTLRNV</span><span class="topo-outside">HEVYSSDNGVTAGRPHLT</span><span class="topo-unknown">LKTIVGLIY</span><span class="topo-membrane">KNDQLSCLLGMAL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">AYNIASNIING</span><span class="topo-inside">FAIYYFTYVIGDADLFPYYL</span><span class="topo-membrane">SYAGAANLLTLIVFPRLVKML</span><span class="topo-outside">S</span><span class="topo-membrane">RRILWAGASVMPVLSCA</span><span class="topo-inside">GLFAMALADIHNAALIVA</span><span class="topo-membrane">AGIFLNIGTALFWVLQVIMVADTV</span><span class="topo-outside">DYGEFKLN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">IRC</span><span class="topo-membrane">ESIAYSVQTMVVKGGSAFAAFFI</span><span class="topo-inside">ALVLGLIGYTPNVAQSAQTLQGMQFIMIV</span><span class="topo-membrane">LPVLFFMMTLVLYFRYYRLNG</span><span class="topo-outside">DMLRKIQIHLLDKYRKT</span><span class="topo-unknown">PPFVEQPDSPAISVVATSDVKAHHHHH</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-unknown">HHHHH</span></span>
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
      <td>2</td>
      <td>2</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>29</td>
      <td>4</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>43</td>
      <td>31</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>66</td>
      <td>45</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>75</td>
      <td>68</td>
      <td>76</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>76</td>
      <td>96</td>
      <td>77</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>103</td>
      <td>98</td>
      <td>104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>131</td>
      <td>105</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>137</td>
      <td>133</td>
      <td>138</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>138</td>
      <td>162</td>
      <td>139</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>168</td>
      <td>164</td>
      <td>169</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>169</td>
      <td>175</td>
      <td>170</td>
      <td>176</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>200</td>
      <td>177</td>
      <td>201</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>201</td>
      <td>218</td>
      <td>202</td>
      <td>219</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>219</td>
      <td>227</td>
      <td>220</td>
      <td>228</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>228</td>
      <td>251</td>
      <td>229</td>
      <td>252</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>252</td>
      <td>271</td>
      <td>253</td>
      <td>272</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>272</td>
      <td>292</td>
      <td>273</td>
      <td>293</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>293</td>
      <td>293</td>
      <td>294</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>310</td>
      <td>295</td>
      <td>311</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>328</td>
      <td>312</td>
      <td>329</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>329</td>
      <td>352</td>
      <td>330</td>
      <td>353</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>353</td>
      <td>363</td>
      <td>354</td>
      <td>364</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>364</td>
      <td>386</td>
      <td>365</td>
      <td>387</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>415</td>
      <td>388</td>
      <td>416</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>416</td>
      <td>436</td>
      <td>417</td>
      <td>437</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>437</td>
      <td>453</td>
      <td>438</td>
      <td>454</td>
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

### Pyramidal cation-binding site

Three conserved acidic residues (Asp19, Asp55, Asp59) form a pyramidal-shaped cation-binding site for Na+, Li+, or H+. This site is in close proximity to the sugar-binding site and represents a previously unidentified cation-binding motif. The small ionic radius of Na+ and Li+ requires coordination ligands in closer distance, and metal binding induces relatively large movement of helices. Asp124 is required for completion of the Na+-binding site. Na+ binding recruits Asp124, resulting in movement of helix IV with Tyr120 and Trp128 for aromatic stacking with the bound sugar. Na+ and Li+ are more effective activators than H+.

### Sugar-binding site and aromatic stacking

The sugar-binding site is located mainly in the amino-terminal domain. Asp124, Tyr120, Trp128, and Arg149 contribute to sugar selectivity and affinity. The aromatic residues Trp128 and Tyr120 contribute to affinity by CH/pi-interactions with the pyranosyl ring of the sugar. The [salt bridge](/xray-mp-wiki/concepts/salt-bridge/) between Asp19 and Arg149 is involved in sugar binding. In the Mol-B conformation (inactive state), this [salt bridge](/xray-mp-wiki/concepts/salt-bridge/) is broken and Trp128 is displaced from the cavity, suggesting deformation of the sugar-binding site. Helix IV physically connects both cosubstrate sites.

### Helix IV as a mechanical linker

Helix IV, in the middle of the [N-terminal](/xray-mp-wiki/concepts/structural-mechanisms/n-terminus/) domain, physically connects both cosubstrate sites (cation and sugar). In addition to Tyr120 and Asp124, Lys18 H-bonds with the backbone atom of Met123, which links helices I-IV. This underscores the crucial role of helix IV in cooperative binding and transport. Na+ binding leads to movement of helix IV, which recruits Asp124, optimizing the pyramidal shape of the cavity with Asp55 and Asp59, and aligning Tyr120 and Trp128 for aromatic stacking with the sugar, thereby increasing affinity. Sugar affinity is increased by more than threefold in the presence of Na+ or Li+.

### Ionic locks and conformational cycling

Three cytoplasmic interdomain ionic locks stabilize the outward-facing conformation. Lock-1 (L-1): Arg295 (helix IX) forms H-bonds with Gln143 (helix V) and Pro287 (helix VIII). Lock-2 (L-2): Arg141 (helix V) forms four H-bonded ion pairs with Asp351 and Asp354 (helix X). Lock-3 (L-3): Arg363 (loop10-11) forms ion pair and two H-bonding interactions with Val204, Asp208, and Gly74, holding the [N-terminal](/xray-mp-wiki/concepts/structural-mechanisms/n-terminus/) domain in outward-facing conformation. On the [periplasmic](/xray-mp-wiki/concepts/miscellaneous/periplasm/) side, Asp35 (helix I) organizes L-4 by forming a [salt bridge](/xray-mp-wiki/concepts/salt-bridge/) and H-bond with Arg175 (helix VI). Replacing Arg363, Arg141, or Arg295 with Cys yields conformationally compromised mutants that fail to transport but retain affinity. These ionic locks are not present in inward conformers, suggesting a sequential lock formation mechanism for the outward state.

### Sugar specificity determinant pocket from high-resolution D59C structures

Two high-resolution X-ray structures of the D59C MelB_St mutant bound to alpha-NPG (PDB 7L17, 3.05 A) or DDMB (PDB 7L16, 3.15 A) reveal a narrow sugar specificity determinant pocket formed by residues from five transmembrane helices (I, IV, V, X, XI). The galactosyl moiety is recognized through a comprehensive salt-bridge-assisted H-bonding network involving Lys18, Asp19 (helix I), Tyr120, Asp124, Trp128 (helix IV), Arg149 (helix V), Trp342 (helix X), and Thr373, Val376 (helix XI). This explains MelBs specificity for galactosides over glucosides.

### Structural basis for cooperative binding between sugar and cation sites

The conserved cation-binding pocket is proposed to involve Asp55, Asp59, Gly117, Thr121, and Lys377 from helices II, IV, and XI. The C6-OH of the galactosyl ring approaches within 6.9 A of the cation site, providing a direct structural connection. Four out of six cation-site positions are conserved in human MFSD2A, suggesting a common cation-binding mechanism across the GPH family. The close connection between the two specificity determinant pockets provides the structural foundation for the obligatory coupling of this transporter family.

### D59C mutation converts symport to uniport enabling crystallization

The D59C mutation abolishes cation binding and all three modes of cation-coupled melibiose transport (Na+, Li+, H+ symport) while retaining sugar binding and translocation. Asp59 is proposed as the H+-binding residue. This uncoupling made crystallization feasible, yielding reproducible high-quality crystals. The D59C mutant exhibits improved thermostability (Tm = 60 C, 6 C higher than WT) as detected by CD spectroscopy. A transport kinetic model was proposed: an 8-step cycle for symport (WT) and a 6-step cycle for uniport (D59C).

### Alternating access mechanism for Na+/melibiose symport

A sequential binding kinetic model explains reversible cation/melibiose symport based on an alternating-access mechanism. The structural and functional studies integrate conformational states with kinetic steps. [Melibiose](/xray-mp-wiki/reagents/ligands/melibiose) influx down a sugar concentration gradient starts from an intermediate state and proceeds via the outward-facing conformation. Active transport of [Melibiose](/xray-mp-wiki/reagents/ligands/melibiose) against a concentration gradient is driven by the electrochemical gradient of Na+, Li+, or H+. In the absence of sugar, MelB/Na+ complexes preferentially populate outward conformations, preventing bound Na+ from futile cycling. Sugar binding to the cytoplasmic stretch of helix V (Arg141-Arg149) triggers locking/unlocking processes associated with cascade of structural rearrangements for reorientation of the sugar-binding pocket.


## Cross-References

- <a href="/xray-mp-wiki/concepts/protein-families/mfs-transporter/">Major Facilitator Superfamily (MFS)</a> — MelB belongs to the glycoside-pentoside-hexuronide:cation symporter family, a subgroup of MFS
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/conformational-dynamics-mfs/">Conformational Dynamics in MFS Transporters</a> — MelB structures reveal outward partially occluded and outward inactive conformations
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — MelB operates by alternating access between inward- and outward-facing conformations
- <a href="/xray-mp-wiki/proteins/mfs-transporters/lac-y/">Lactose Permease of Escherichia coli (LacY)</a> — Closely related MFS transporter with similar sugar specificity and location of sugar-recognition sites
- <a href="/xray-mp-wiki/reagents/detergents/udm/">n-Undecyl-beta-D-maltoside (UDM)</a> — Primary detergent used for MelBSt solubilization during purification
- <a href="/xray-mp-wiki/reagents/ligands/dansyl-galactopyranoside-d2g/">Dansyl-galactopyranoside (D2G)</a> — Fluorescent galactopyranoside probe used in FRET and binding assays for MelB
- <a href="/xray-mp-wiki/reagents/ligands/melibiose/">Melibiose</a> — Primary sugar substrate transported by MelB, Kd ~1 mM with Na+ or Li+
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/">C-terminal</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/proteins/enzymes/leut/">LeuT Amino Acid Transporter</a> — LeuT is another model secondary transporter with resolved substrate-binding mechanism
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/">ITC</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/ethylene-glycol/">Ethylene Glycol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
