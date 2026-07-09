---
title: "XylE (Escherichia coli Sugar Transporter)"
created: 2026-06-02
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature11524, doi/10.1038##ncomms5521, doi/10.1038##nsmb.2569]
verified: regex
uniprot_id: P0AGF4
---

# XylE (Escherichia coli Sugar Transporter)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P0AGF4">UniProt: P0AGF4</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

XylE is an Escherichia coli homologue of the human [Glucose](/xray-mp-wiki/reagents/additives/glucose) transporters [SLC2A1](/xray-mp-wiki/proteins/glut1)-4. It belongs to the sugar porter (SP) family within the major facilitator superfamily (MFS) of secondary transporters. XylE functions as a proton-coupled xylose (H+/xylose) symporter. XylE has been crystallized in multiple conformations: an outward-facing partly occluded conformation, an inward-facing partly occluded conformation, and a new inward-facing open conformation with a detached cytoplasmic domain. The inward-open structure reveals an asymmetric rocker-switch movement of the N-domain against the C-domain during transport. Key proton-coupling residues include Asp27 (TM1), Arg133, and Glu206 (TM6); sugar-binding residues include Gln168 (TM5) and Trp392 (TM10).


## Publications

### doi/10.1038##nature11524

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4gbz">4GBZ</a></td>
      <td>2.8</td>
      <td>unknown</td>
      <td>Full-length wild-type XylE from E. coli O157:H7</td>
      <td>D-xylose</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4gbx">4GBX</a></td>
      <td>2.9</td>
      <td>unknown</td>
      <td>Full-length wild-type XylE from E. coli O157:H7</td>
      <td>D-glucose</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4gby">4GBY</a></td>
      <td>2.6</td>
      <td>unknown</td>
      <td>Full-length wild-type XylE from E. coli O157:H7</td>
      <td>6-bromo-6-deoxy-D-glucose</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) and E. coli BL21 C43(DE3)
- **Construct**: Full-length XylE, N-terminal His6-tag (pET15b); Truncated XylE residues 6-480 (pET-15b)
- **Induction**: 0.2 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg) at D600 of 1.5 (full-length); 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg) at OD600 0.5, shifted to 18C (truncated)
- **Media**: Luria-Bertani medium and Luria-Bertani (LB) medium at 37C, 250 rpm

**Purification:**

- **Expression system**: E. coli BL21(DE3)
- **Expression construct**: Full-length XylE with N-terminal [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag) (pET15b)
- **Tag info**: [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag), removed by protease

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
      <td>Cell culture</td>
      <td>Fermentation</td>
      <td>—</td>
      <td>Luria-Bertani medium</td>
      <td>12 flasks, 300 r.p.m., 4 h at 37 C after <a href="/xray-mp-wiki/reagents/additives/iptg">IPTG</a> induction</td>
    </tr>
    <tr>
      <td>Cell harvest and homogenization</td>
      <td>French press cell lysis</td>
      <td>—</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl</td>
      <td>Two passes at 10,000-15,000 lb/in2</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Ultracentrifugation</td>
      <td>—</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl</td>
      <td>150,000g for 1 h; membrane fraction harvested</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl + 1.5% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>1 h incubation at 4 C</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> (Qiagen)</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> + 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Wash with 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a>; elute with 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a></td>
    </tr>
    <tr>
      <td>Tag removal</td>
      <td>Protease cleavage</td>
      <td>—</td>
      <td></td>
      <td>Hexahistidine tag removed</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200">Superdex 200 Increase SEC Resin</a> (GE Healthcare)</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl, various detergents + various</td>
      <td></td>
    </tr>
  </tbody>
</table>
**Final sample**: 10 mg/ml in 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris) pH 8.0, 150 mM NaCl

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>XylE purified in <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallized with 20 mM <a href="/xray-mp-wiki/reagents/substrates/d-xylose">D-Xylose</a>; diffraction to 2.8 A</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>XylE purified in <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallized with 40 mM D-<a href="/xray-mp-wiki/reagents/additives/glucose">Glucose</a>; diffraction to 2.9 A</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>XylE purified in <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallized with 40 mM 6-bromo-6-deoxy-D-<a href="/xray-mp-wiki/reagents/additives/glucose">Glucose</a>; Br anomalous signal; diffraction to 2.6 A</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4gbz">4GBZ</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MNTQ</span><span class="topo-inside">YNSSYIFSIT</span><span class="topo-membrane">LVATLGGLLFGYDTAVISGTV</span><span class="topo-unknown">ESLNTV</span><span class="topo-outside">FVAPQNLSESAANS</span><span class="topo-membrane">LLGFCVASALIGCIIGGALG</span><span class="topo-inside">GYCSNRFGRRDS</span><span class="topo-membrane">LKIAAVLFFISGVGSAWP</span><span class="topo-outside">ELGFTSINPDNTVPV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">YLAG</span><span class="topo-membrane">YVPEFVIYRIIGGIGVGLASMLSP</span><span class="topo-inside">MYIAELAPAHIRG</span><span class="topo-membrane">KLVSFNQFAIIFGQLLVYCVNYFI</span><span class="topo-outside">ARSGDASWLNTDG</span><span class="topo-membrane">WRYMFASECIPALLFLMLLY</span><span class="topo-inside">TVPESPRWLMSRGKQEQAEGIL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">RKIMGNTLATQAVQEIKHSLDHGRKTGGRLLMFGVGVIV</span><span class="topo-membrane">IGVMLSIFQQFVGINVVLYYAPE</span><span class="topo-outside">VFKTLGASTDIAL</span><span class="topo-membrane">LQTIIVGVINLTFTVLAIMTV</span><span class="topo-inside">DKFGR</span><span class="topo-membrane">KPLQIIGALGMAIGMFSLG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">TAFY</span><span class="topo-outside">TQAPGIV</span><span class="topo-membrane">ALLSMLFYVAAFAMSWGPVCWVLL</span><span class="topo-inside">SEIFPNAIRGKALA</span><span class="topo-membrane">IAVAAQWLANYFVSWTFPMMDK</span><span class="topo-unknown">NSWLVAHF</span><span class="topo-outside">HN</span><span class="topo-membrane">GFSYWIYGCMGVLAALFMW</span><span class="topo-inside">KFVPETKGKTLEELEALWE</span><span class="topo-unknown">P</span></span>
<span class="topo-ruler">       490 </span>
<span class="topo-line"><span class="topo-unknown">ETKKTQQTATL</span></span>
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
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>14</td>
      <td>5</td>
      <td>14</td>
      <td>Inside</td>
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
      <td>41</td>
      <td>36</td>
      <td>41</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>42</td>
      <td>55</td>
      <td>42</td>
      <td>55</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>75</td>
      <td>56</td>
      <td>75</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>87</td>
      <td>76</td>
      <td>87</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>105</td>
      <td>88</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>124</td>
      <td>106</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>148</td>
      <td>125</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>161</td>
      <td>149</td>
      <td>161</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>162</td>
      <td>185</td>
      <td>162</td>
      <td>185</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>186</td>
      <td>198</td>
      <td>186</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>279</td>
      <td>219</td>
      <td>279</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>302</td>
      <td>280</td>
      <td>302</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>303</td>
      <td>315</td>
      <td>303</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>336</td>
      <td>316</td>
      <td>336</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>337</td>
      <td>341</td>
      <td>337</td>
      <td>341</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>342</td>
      <td>364</td>
      <td>342</td>
      <td>364</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>365</td>
      <td>371</td>
      <td>365</td>
      <td>371</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>372</td>
      <td>395</td>
      <td>372</td>
      <td>395</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>396</td>
      <td>409</td>
      <td>396</td>
      <td>409</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>410</td>
      <td>431</td>
      <td>410</td>
      <td>431</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>432</td>
      <td>439</td>
      <td>432</td>
      <td>439</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>440</td>
      <td>441</td>
      <td>440</td>
      <td>441</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>460</td>
      <td>442</td>
      <td>460</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>461</td>
      <td>479</td>
      <td>461</td>
      <td>479</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>480</td>
      <td>491</td>
      <td>480</td>
      <td>491</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4gby">4GBY</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MNTQ</span><span class="topo-outside">YNSSYIF</span><span class="topo-membrane">SITLVATLGGLLFGYDTAVIS</span><span class="topo-inside">GTVESLNTVFVAPQNLSESAANSLLG</span><span class="topo-membrane">FCVASALIGCIIGGALGGYCS</span><span class="topo-outside">NRFGR</span><span class="topo-membrane">RDSLKIAAVLFFISGVGSAWPE</span><span class="topo-inside">LGFTSINPDNTVPV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">YLAGYVP</span><span class="topo-membrane">EFVIYRIIGGIGVGLASMLSPMYI</span><span class="topo-outside">AELAPAHIRG</span><span class="topo-membrane">KLVSFNQFAIIFGQLLVYCVN</span><span class="topo-inside">YFIARSGDASWLNTDGWRY</span><span class="topo-membrane">MFASECIPALLFLMLLYTV</span><span class="topo-outside">PESPRWLMSRGKQEQAEGIL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">RKIMGNTLATQAVQEIKHSLDHGRKTGGRLLMFGVGVIV</span><span class="topo-membrane">IGVMLSIFQQFVGINVVLYYAP</span><span class="topo-inside">EVFKTLGASTDIALLQ</span><span class="topo-membrane">TIIVGVINLTFTVLAIMTV</span><span class="topo-outside">DKFGR</span><span class="topo-membrane">KPLQIIGALGMAIGMFSLG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">TA</span><span class="topo-inside">FYTQAPGIV</span><span class="topo-membrane">ALLSMLFYVAAFAMSWGPVCWVLLS</span><span class="topo-outside">EIFPNAIRGKAL</span><span class="topo-membrane">AIAVAAQWLANYFVSWTFPMMD</span><span class="topo-inside">KNSWLVAHFHNG</span><span class="topo-membrane">FSYWIYGCMGVLAALFMW</span><span class="topo-outside">KFVPETKGKTLEELEALWE</span><span class="topo-unknown">P</span></span>
<span class="topo-ruler">       490 </span>
<span class="topo-line"><span class="topo-unknown">ETKKTQQTATL</span></span>
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
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>11</td>
      <td>5</td>
      <td>11</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>32</td>
      <td>12</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>58</td>
      <td>33</td>
      <td>58</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>79</td>
      <td>59</td>
      <td>79</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>84</td>
      <td>80</td>
      <td>84</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>106</td>
      <td>85</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>127</td>
      <td>107</td>
      <td>127</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>128</td>
      <td>151</td>
      <td>128</td>
      <td>151</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>152</td>
      <td>161</td>
      <td>152</td>
      <td>161</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>162</td>
      <td>182</td>
      <td>162</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>201</td>
      <td>183</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>220</td>
      <td>202</td>
      <td>220</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>279</td>
      <td>221</td>
      <td>279</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>301</td>
      <td>280</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>302</td>
      <td>317</td>
      <td>302</td>
      <td>317</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>318</td>
      <td>336</td>
      <td>318</td>
      <td>336</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>337</td>
      <td>341</td>
      <td>337</td>
      <td>341</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>342</td>
      <td>362</td>
      <td>342</td>
      <td>362</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>363</td>
      <td>371</td>
      <td>363</td>
      <td>371</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>372</td>
      <td>396</td>
      <td>372</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>408</td>
      <td>397</td>
      <td>408</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>409</td>
      <td>430</td>
      <td>409</td>
      <td>430</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>431</td>
      <td>442</td>
      <td>431</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>460</td>
      <td>443</td>
      <td>460</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>461</td>
      <td>479</td>
      <td>461</td>
      <td>479</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>480</td>
      <td>491</td>
      <td>480</td>
      <td>491</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##ncomms5521

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4qiq">4QIQ</a></td>
      <td>3.5</td>
      <td>P3;21</td>
      <td>Truncated XylE residues 6-480 from E. coli BL21(DE3) genomic DNA</td>
      <td>D-glucose (30 mM, crystallization additive)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) and E. coli BL21 C43(DE3)
- **Construct**: Full-length XylE, N-terminal His6-tag (pET15b); Truncated XylE residues 6-480 (pET-15b)
- **Induction**: 0.2 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg) at D600 of 1.5 (full-length); 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg) at OD600 0.5, shifted to 18C (truncated)
- **Media**: Luria-Bertani medium and Luria-Bertani (LB) medium at 37C, 250 rpm

**Purification:**

- **Expression system**: E. coli BL21 C43(DE3)
- **Expression construct**: Truncated XylE residues 6-480, N-terminal [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag) (pET-15b)
- **Tag info**: [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag), removed by thrombin protease overnight at 4C with 2.5 mM CaCl2

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
      <td>Cell culture</td>
      <td>Fermentation</td>
      <td>—</td>
      <td>Luria-Bertani (LB) medium at 37C, 250 rpm</td>
      <td>Shifted to 18C at OD600 0.5; induced with 0.5 mM <a href="/xray-mp-wiki/reagents/additives/iptg">IPTG</a>; overnight culture</td>
    </tr>
    <tr>
      <td>Cell harvest and homogenization</td>
      <td>Microfluidizer M110-P cell lysis</td>
      <td>—</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl</td>
      <td>20,000 psi</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Ultracentrifugation</td>
      <td>—</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl</td>
      <td>10,000g for 30 min at 4C, then 1 h at 4C</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 7.5 + 1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> (<a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>)</td>
      <td>5% w/v <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> added, rotated 2 h at 4C; centrifuged 150,000g for 45 min at 4C</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> (Qiagen)</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> + 0.2% w/v <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>Wash with 25 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> then 50 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a>; elute with 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> in 10 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 7.5, 150 mM NaCl, 0.2% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
    </tr>
    <tr>
      <td>Tag removal</td>
      <td>Protease cleavage</td>
      <td>—</td>
      <td></td>
      <td>His-tag cleaved overnight at 4C using 1 unit human alpha-thrombin per 1 mg XylE with 2.5 mM CaCl2</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td>Superdex S200</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 7.5, 150 mM NaCl, various detergents + various (screened for optimal detergent)</td>
      <td></td>
    </tr>
  </tbody>
</table>
**Final sample**: 5-6 mg/ml

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>XylE purified in 1% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>, concentrated to 5-6 mg/ml</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Inward-facing open conformation with detached cytoplasmic domain; PDB 4QIQ</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4qiq">4QIQ</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSHMNS</span><span class="topo-outside">SYIFSITL</span><span class="topo-membrane">VATLGGLLFGYDTAVISGTVESLN</span><span class="topo-inside">TVFVAPQNLSES</span><span class="topo-membrane">AANSLLGFCVASALIGCIIGGALG</span><span class="topo-outside">GYCSNRFGRRD</span><span class="topo-membrane">SLKIAAVLFFISGVGSAWPE</span><span class="topo-inside">LGFTSINPDNTVPVY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">L</span><span class="topo-membrane">AGYVPEFVIYRIIGGIGVGLASM</span><span class="topo-outside">LSPMYIAELAPAHIRGKLVS</span><span class="topo-membrane">FNQFAIIFGQLLVYCVNYFIAR</span><span class="topo-inside">SGDASWLNTD</span><span class="topo-membrane">GWRYMFASECIPALLFLMLLY</span><span class="topo-outside">TVPESPRWLM</span><span class="topo-unknown">SRGKQEQAEGILR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">KIMGN</span><span class="topo-outside">TLATQAVQEIKHSLD</span><span class="topo-unknown">HGRKTGG</span><span class="topo-outside">RLLMFGVGVIV</span><span class="topo-membrane">IGVMLSIFQQFVGINVVLYYAPEVFK</span><span class="topo-inside">TLGAST</span><span class="topo-membrane">DIALLQTIIVGVINLTFTVLAIMTV</span><span class="topo-outside">DKFGRK</span><span class="topo-membrane">PLQIIGALGMAIGMFSLGT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470         </span>
<span class="topo-line"><span class="topo-membrane">AFY</span><span class="topo-inside">TQAPG</span><span class="topo-membrane">IVALLSMLFYVAAFAMSWGPVCW</span><span class="topo-outside">VLLSEIFPNAIRGKALAI</span><span class="topo-membrane">AVAAQWLANYFVSWTFPMMDKN</span><span class="topo-unknown">SWLVAHF</span><span class="topo-inside">HN</span><span class="topo-membrane">GFSYWIYGCMGVLAALFMWKF</span><span class="topo-outside">VPETKGKTL</span><span class="topo-unknown">EELEALWEP</span></span>
<details class="topo-details"><summary>Topology coordinates (32 regions)</summary>
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
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>7</td>
      <td>14</td>
      <td>8</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>38</td>
      <td>16</td>
      <td>39</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>50</td>
      <td>40</td>
      <td>51</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>74</td>
      <td>52</td>
      <td>75</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>85</td>
      <td>76</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>105</td>
      <td>87</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>121</td>
      <td>107</td>
      <td>122</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>144</td>
      <td>123</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>164</td>
      <td>146</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>165</td>
      <td>186</td>
      <td>166</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>196</td>
      <td>188</td>
      <td>197</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>197</td>
      <td>217</td>
      <td>198</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>227</td>
      <td>219</td>
      <td>228</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>245</td>
      <td>229</td>
      <td>246</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>246</td>
      <td>260</td>
      <td>247</td>
      <td>261</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>267</td>
      <td>262</td>
      <td>268</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>268</td>
      <td>278</td>
      <td>269</td>
      <td>279</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>304</td>
      <td>280</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>305</td>
      <td>310</td>
      <td>306</td>
      <td>311</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>335</td>
      <td>312</td>
      <td>336</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>336</td>
      <td>341</td>
      <td>337</td>
      <td>342</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>342</td>
      <td>363</td>
      <td>343</td>
      <td>364</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>368</td>
      <td>365</td>
      <td>369</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>369</td>
      <td>391</td>
      <td>370</td>
      <td>392</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>392</td>
      <td>409</td>
      <td>393</td>
      <td>410</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>410</td>
      <td>431</td>
      <td>411</td>
      <td>432</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>432</td>
      <td>438</td>
      <td>433</td>
      <td>439</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>439</td>
      <td>440</td>
      <td>440</td>
      <td>441</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>441</td>
      <td>461</td>
      <td>442</td>
      <td>462</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>462</td>
      <td>470</td>
      <td>463</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>479</td>
      <td>472</td>
      <td>480</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##nsmb.2569

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ja4">4JA4</a></td>
      <td>4.2</td>
      <td>P6_1</td>
      <td>Full-length wild-type XylE from E. coli C41(DE3), N-terminal His6-TEV tag</td>
      <td>None (apoprotein)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ja3">4JA3</a></td>
      <td>3.8</td>
      <td>C2</td>
      <td>Full-length wild-type XylE from E. coli C41(DE3), N-terminal His6-TEV tag</td>
      <td>None (apoprotein)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) and E. coli BL21 C43(DE3)
- **Construct**: Full-length XylE, N-terminal His6-tag (pET15b); Truncated XylE residues 6-480 (pET-15b)
- **Induction**: 0.2 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg) at D600 of 1.5 (full-length); 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg) at OD600 0.5, shifted to 18C (truncated)
- **Media**: Luria-Bertani medium and Luria-Bertani (LB) medium at 37C, 250 rpm

**Purification:**

- **Expression system**: E. coli C41(DE3)
- **Expression construct**: Full-length wild-type XylE from E. coli C41(DE3), N-terminal His6-TEV tag (modified pTH27 vector)
- **Tag info**: [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag) with TEV protease cleavage site, removed by TEV protease

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
      <td>Cell culture</td>
      <td>Fermentation in Terrific broth (TB) medium</td>
      <td>—</td>
      <td>Terrific broth (TB)</td>
      <td>220 r.p.m., 37 C; overexpression induced by 0.2 mM <a href="/xray-mp-wiki/reagents/additives/iptg">IPTG</a> at OD600 0.7-1.0; harvested after 16-20 h at 20 C</td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>Emulsiflex microfluidizer at 15,000 p.s.i. chamber pressure</td>
      <td>—</td>
      <td>20 mM sodium phosphate (Na-P) pH 7.5, 300 mM NaCl, 0.5 mM <a href="/xray-mp-wiki/reagents/additives/tcep">TCEP</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 1 mg/ml lysozyme, 5 U/ml DNaseI, <a href="/xray-mp-wiki/reagents/additives/edta">EDTA</a>-free Complete Protease Inhibitor Cocktail</td>
      <td>Resuspension at 4 C for 45 min; debris removed by centrifugation at 10,000g for 10 min at 4 C</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Ultracentrifugation</td>
      <td>—</td>
      <td>Same as lysis buffer</td>
      <td>104,000g (Beckman Coulter, Ti45 rotor) at 4 C for 50 min</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>20 mM Na-P pH 7.5, 300 mM NaCl, 15 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 0.5 mM <a href="/xray-mp-wiki/reagents/additives/tcep">TCEP</a>, Complete Protease Inhibitor Cocktail + 1% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> (<a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>)</td>
      <td>60 min incubation at 4 C; clarified by ultracentrifugation at 104,000g for 30 min at 4 C</td>
    </tr>
    <tr>
      <td>IMAC purification</td>
      <td>Immobilized metal ion <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a> (IMAC) with <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> beads</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> beads</td>
      <td>20 mM Na-P pH 7.5, 300 mM NaCl, 15-30 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 0.5 mM <a href="/xray-mp-wiki/reagents/additives/tcep">TCEP</a>, 0.2% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> + 0.2% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>Beads incubated with supernatant for 1 h; column washed with 15-30 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> wash buffer</td>
    </tr>
    <tr>
      <td>Tag removal</td>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV</a> protease cleavage</td>
      <td>--</td>
      <td>Same as IMAC buffer</td>
      <td>1 mg <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV</a> per ml of IMAC beads, incubated overnight at 4 C; cleavage >95% complete</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a> on HiLoad <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 16/60 GL column</td>
      <td>HiLoad <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 16/60 GL (ÄKTAexplorer 10)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a>, 150 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 0.5 mM <a href="/xray-mp-wiki/reagents/additives/tcep">TCEP</a>, 0.2% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> + 0.2% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>Peak fractions collected, concentrated to 8-18 mg/ml</td>
    </tr>
  </tbody>
</table>
**Final sample**: 8-18 mg/ml

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion crystallization; P6_1 space group; 3-fold averaging for phase improvement</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Tag-free XylE at 8-18 mg/ml in 20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a>, 150 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 0.5 mM <a href="/xray-mp-wiki/reagents/additives/tcep">TCEP</a>, 0.2% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified in text</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Inward open conformation; PDB 4JA4; 4.2 A resolution; data collected at Diamond Light Source beamline I02 (proposal MX5873/MX6603)</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion crystallization; C2 space group; 2-fold averaging for phase improvement</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Tag-free XylE at 8-18 mg/ml in 20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a>, 150 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 0.5 mM <a href="/xray-mp-wiki/reagents/additives/tcep">TCEP</a>, 0.2% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified in text</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Partially occluded inward open conformation; PDB 4JA3; 3.8 A resolution; data collected at SOLEIL synchrotron beamline PROXIMA1 (proposal 20110314)</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ja4">4JA4</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GNTQYNSS</span><span class="topo-outside">YIF</span><span class="topo-membrane">SITLVATLGGLLFGYDTAVISG</span><span class="topo-inside">TVESLNTVFVAPQNLSESAANSLLG</span><span class="topo-membrane">FCVASALIGCIIGGALG</span><span class="topo-outside">GYCSNRFGRR</span><span class="topo-membrane">DSLKIAAVLFFISGVGSAWP</span><span class="topo-inside">ELGFTSINPDNTVPV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">YLAGYV</span><span class="topo-membrane">PEFVIYRIIGGIGVGLASMLSP</span><span class="topo-outside">MYIAELAPAHIRGKLV</span><span class="topo-membrane">SFNQFAIIFGQLLVYCVN</span><span class="topo-inside">YFIARSGDASWLNTDGWRYM</span><span class="topo-membrane">FASECIPALLFLMLLYTV</span><span class="topo-outside">PESPRWLM</span><span class="topo-unknown">SRGK</span><span class="topo-outside">QEQAEGIL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">RKIMGNTLATQAVQEIKHSLDHG</span><span class="topo-unknown">RKTGGRLL</span><span class="topo-outside">MFGVGVIV</span><span class="topo-membrane">IGVMLSIFQQFVGINVVLYYA</span><span class="topo-inside">PEV</span><span class="topo-unknown">FKTLGASTDIA</span><span class="topo-inside">LLQ</span><span class="topo-membrane">TIIVGVINLTFTVLAIMTV</span><span class="topo-outside">DKFGRK</span><span class="topo-membrane">PLQIIGALGMAIGMFSLG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">T</span><span class="topo-inside">AFYTQAPGIVA</span><span class="topo-membrane">LLSMLFYVAAFAMSWGPVCW</span><span class="topo-outside">VLLSEIFPNAIRGKALA</span><span class="topo-membrane">IAVAAQWLANYFVSWTFPMM</span><span class="topo-inside">DKNSW</span><span class="topo-unknown">LVAHFH</span><span class="topo-inside">NGF</span><span class="topo-membrane">SYWIYGCMGVLAALFMWKF</span><span class="topo-outside">VPETKGKTLEELEALWE</span><span class="topo-unknown">P</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-unknown">ETKKT</span></span>
<details class="topo-details"><summary>Topology coordinates (35 regions)</summary>
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
      <td>11</td>
      <td>9</td>
      <td>11</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>33</td>
      <td>12</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>58</td>
      <td>34</td>
      <td>58</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>75</td>
      <td>59</td>
      <td>75</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>85</td>
      <td>76</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>105</td>
      <td>86</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>126</td>
      <td>106</td>
      <td>126</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>148</td>
      <td>127</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>164</td>
      <td>149</td>
      <td>164</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>165</td>
      <td>182</td>
      <td>165</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>202</td>
      <td>183</td>
      <td>202</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>220</td>
      <td>203</td>
      <td>220</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>228</td>
      <td>221</td>
      <td>228</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>232</td>
      <td>229</td>
      <td>232</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>233</td>
      <td>263</td>
      <td>233</td>
      <td>263</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>264</td>
      <td>271</td>
      <td>264</td>
      <td>271</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>272</td>
      <td>279</td>
      <td>272</td>
      <td>279</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>300</td>
      <td>280</td>
      <td>300</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>301</td>
      <td>303</td>
      <td>301</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>304</td>
      <td>314</td>
      <td>304</td>
      <td>314</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>315</td>
      <td>317</td>
      <td>315</td>
      <td>317</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>318</td>
      <td>336</td>
      <td>318</td>
      <td>336</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>337</td>
      <td>342</td>
      <td>337</td>
      <td>342</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>361</td>
      <td>343</td>
      <td>361</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>362</td>
      <td>372</td>
      <td>362</td>
      <td>372</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>373</td>
      <td>392</td>
      <td>373</td>
      <td>392</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>393</td>
      <td>409</td>
      <td>393</td>
      <td>409</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>410</td>
      <td>429</td>
      <td>410</td>
      <td>429</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>430</td>
      <td>434</td>
      <td>430</td>
      <td>434</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>435</td>
      <td>440</td>
      <td>435</td>
      <td>440</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>441</td>
      <td>443</td>
      <td>441</td>
      <td>443</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>444</td>
      <td>462</td>
      <td>444</td>
      <td>462</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>463</td>
      <td>479</td>
      <td>463</td>
      <td>479</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>480</td>
      <td>485</td>
      <td>480</td>
      <td>485</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ja3">4JA3</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GNTQYNS</span><span class="topo-inside">SYIFSITL</span><span class="topo-membrane">VATLGGLLFGYDTAVISGTVESLN</span><span class="topo-outside">TVFVAPQNLSES</span><span class="topo-membrane">AANSLLGFCVASALIGCIIGGALG</span><span class="topo-inside">GYCSNRFGRRDS</span><span class="topo-membrane">LKIAAVLFFISGVGSAWPE</span><span class="topo-outside">LGFTSINPDNTVPV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">YL</span><span class="topo-membrane">AGYVPEFVIYRIIGGIGVGLASMLS</span><span class="topo-inside">PMYIAELAPAHIRGKLVS</span><span class="topo-membrane">FNQFAIIFGQLLVYCVNYFIARS</span><span class="topo-outside">GDASWLNTD</span><span class="topo-membrane">GWRYMFASECIPALLFLMLLY</span><span class="topo-inside">TVPESPRWLMSRGKQEQAEGIL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">RKIMGNTLATQAVQEIKHSLDHGR</span><span class="topo-unknown">KTGGRLLMFGV</span><span class="topo-inside">GVIV</span><span class="topo-membrane">IGVMLSIFQQFVGINVVLYYAPEV</span><span class="topo-unknown">FKTLGA</span><span class="topo-outside">ST</span><span class="topo-membrane">DIALLQTIIVGVINLTFTVLAIMTV</span><span class="topo-inside">DKFGRK</span><span class="topo-membrane">PLQIIGALGMAIGMFSLG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">TAFY</span><span class="topo-outside">TQAPG</span><span class="topo-membrane">IVALLSMLFYVAAFAMSWGPVCW</span><span class="topo-inside">VLLSE</span><span class="topo-unknown">IFPNAIRGK</span><span class="topo-inside">ALA</span><span class="topo-membrane">IAVAAQWLANYFVSWTFPMMDK</span><span class="topo-outside">NS</span><span class="topo-unknown">WLVAHF</span><span class="topo-outside">HN</span><span class="topo-membrane">GFSYWIYGCMGVLAALFMWKF</span><span class="topo-inside">VPE</span><span class="topo-unknown">TKGKTLEELEALWEP</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-unknown">ETKKT</span></span>
<details class="topo-details"><summary>Topology coordinates (34 regions)</summary>
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
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>15</td>
      <td>8</td>
      <td>15</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>39</td>
      <td>16</td>
      <td>39</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>51</td>
      <td>40</td>
      <td>51</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>75</td>
      <td>52</td>
      <td>75</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>87</td>
      <td>76</td>
      <td>87</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>106</td>
      <td>88</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>122</td>
      <td>107</td>
      <td>122</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>123</td>
      <td>147</td>
      <td>123</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>165</td>
      <td>148</td>
      <td>165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>188</td>
      <td>166</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>189</td>
      <td>197</td>
      <td>189</td>
      <td>197</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>198</td>
      <td>218</td>
      <td>198</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>264</td>
      <td>219</td>
      <td>264</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>265</td>
      <td>275</td>
      <td>265</td>
      <td>275</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>276</td>
      <td>279</td>
      <td>276</td>
      <td>279</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>303</td>
      <td>280</td>
      <td>303</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>304</td>
      <td>309</td>
      <td>304</td>
      <td>309</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>310</td>
      <td>311</td>
      <td>310</td>
      <td>311</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>312</td>
      <td>336</td>
      <td>312</td>
      <td>336</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>337</td>
      <td>342</td>
      <td>337</td>
      <td>342</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>364</td>
      <td>343</td>
      <td>364</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>365</td>
      <td>369</td>
      <td>365</td>
      <td>369</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>370</td>
      <td>392</td>
      <td>370</td>
      <td>392</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>393</td>
      <td>397</td>
      <td>393</td>
      <td>397</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>406</td>
      <td>398</td>
      <td>406</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>407</td>
      <td>409</td>
      <td>407</td>
      <td>409</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>410</td>
      <td>431</td>
      <td>410</td>
      <td>431</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>432</td>
      <td>433</td>
      <td>432</td>
      <td>433</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>434</td>
      <td>439</td>
      <td>434</td>
      <td>439</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>440</td>
      <td>441</td>
      <td>440</td>
      <td>441</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>462</td>
      <td>442</td>
      <td>462</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>463</td>
      <td>465</td>
      <td>463</td>
      <td>465</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>466</td>
      <td>485</td>
      <td>466</td>
      <td>485</td>
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

### Outward-facing, partly occluded conformation

XylE was captured in an outward-facing, partly occluded conformation. The ligand ([D-Xylose](/xray-mp-wiki/reagents/substrates/d-xylose)) resides in the centre of the transmembrane domain, completely occluded from the intracellular side yet solvent-accessible from the extracellular side through a narrow channel. This conformation represents an important expansion to the collection of MFS conformations.

### Substrate binding site and coordination

[D-Xylose](/xray-mp-wiki/reagents/substrates/d-xylose) is bound between the N and C domains, coordinated by eight hydrogen bonds with polar residues including Gln 168 (TM5), Gln 288/Gln 289/Asn 294 (TM7), Trp 392 (TM10), and Gln 415 (TM11). Aromatic residues Phe 24, Tyr 298, Trp 392 and Trp 416 surround the substrate. Tyr 298 constitutes the constriction that prevents escape of [D-Xylose](/xray-mp-wiki/reagents/substrates/d-xylose) to the extracellular side.

### Intracellular four-helix domain

Unlike other MFS transporters of known structure, XylE contains an intracellular domain comprising four helices — three connecting the N and C domains and one at the C-terminal end. The residues constituting these helices are highly conserved in [SLC2A1](/xray-mp-wiki/proteins/glut1)-4. Extensive polar interactions with the cytosolic portion of TMs suggest a similar cytoplasmic domain likely exists in [SLC2A1](/xray-mp-wiki/proteins/glut1)-4.

### D-glucose binding and inhibition

D-[Glucose](/xray-mp-wiki/reagents/additives/glucose) binds to XylE with a Kd of about 0.77 +/- 0.01 mM but is not a transport substrate. It binds similarly to [D-Xylose](/xray-mp-wiki/reagents/substrates/d-xylose) but the extra 6-hydroxymethyl group is coordinated through van der Waals contacts by Ile 171 (TM5) and Phe 383 (TM10), and through an extra hydrogen bond with Gln 175 (TM5). D-[Glucose](/xray-mp-wiki/reagents/additives/glucose) inhibits [D-Xylose](/xray-mp-wiki/reagents/substrates/d-xylose) transport by nearly 90%.

### Sugar porter signature motifs

Conserved SP family signature motifs are found in XylE: D(N)RXGRR between TMs 2-3 and 8-9, E------R between TMs 4-5 and 10-11, PESPR at TM6C, and PETK at TM12C. These motifs are positioned on the cytoplasmic side and form an intricate hydrogen-bond network mediating interactions between TMs and the intracellular domain. More than half of single point mutations in these motifs resulted in completely abrogated or seriously impaired activities.

### Disease-related GLUT1 mutations mapped to XylE model

Homology-based structural model of [SLC2A1](/xray-mp-wiki/proteins/glut1) was generated from XylE structure and sequence conservation. Disease-related mutations from [SLC2A1](/xray-mp-wiki/proteins/glut1) deficiency syndrome were mapped: Asn 34, Ser 66, Thr 295 and Thr 310 are on the extracellular side; Gly 75 and Gly 130 are in the middle of TM2 and TM4; Arg 126 and His 337 are buried within domains suggesting regulatory role. Mutations of corresponding residues in XylE (R133C, R133H, R133L, R341W) completely lost transport activity for [D-Xylose](/xray-mp-wiki/reagents/substrates/d-xylose).

### Inward-facing open conformation with detached cytoplasmic domain

The 3.5 A resolution crystal structure (PDB 4QIQ) of XylE in a new inward-facing open conformation reveals a detached cytoplasmic domain. The N-domain (residues 8-220) and C-domain (residues 276-463) form the transmembrane core. The intracellular linker between TM6 and TM7 (residues 221-273) folds into three alpha-helices (IC1-IC3) in the outward-facing conformation but becomes disordered in the inward-open state. The N-domain r.m.s.d. is 1.1 A between conformations; C-domain r.m.s.d. is 2.9 A with large changes in helix-loop-helix between TM7-8, TM10-11 and TM11-12.

### Asymmetric rocker-switch movement

Molecular dynamics simulations reveal that XylE functions through a non-symmetric rocker-switch movement in a membrane. The periplasmic half of the N-domain shows significant movement towards the C-domain to close the periplasmic vestibule while the cytoplasmic domain detaches. This differs from the symmetric rigid body movement previously reported based on crystal structure overlays alone.

### Proton-coupling mechanism via Asp27-Arg133

Conserved Asp27 (TM1) and Arg133 form a proton-coupling pair. In the outward-facing conformation at basic pH, deprotonated Asp27 interacts with Arg133 and Glu206 (TM6). In the inward-open conformation at acidic pH, Asp27 is partially protonated and no longer interacts with Arg133. Protonation of Asp27 weakens these interactions and triggers the conformational switch from outward to inward-facing. TMD simulations with protonated vs deprotonated Asp27 showed significantly altered transport dynamics.

### Sugar binding and release mechanism

Gln168 (TM5) and Trp392 (TM10) are key sugar-binding residues. Trp392 acts as a cytoplasmic substrate-release gate, swinging ~6 A away from Gln168 in the inward- facing conformation to open a tunnel to the transporter center. Mutants Q168A and W392A showed significantly reduced transport activities. During SMD simulations, [D-Xylose](/xray-mp-wiki/reagents/substrates/d-xylose) translocates through the substrate tunnel with a total energy barrier of ~7 kcal/mol at the tunnel exit point.

### Water co-transport mechanism

MD simulations indicate XylE transports water molecules along with the substrate. A solvent-filled cavity connects the Asp27-Arg133 site to the sugar-binding site. A hydrogen bond network among water molecules forms a water wire connecting protonated Asp27 to bulk water in the cytoplasm during the inward-facing conformation. This water wire was stable during TMD simulations and broken after sugar release in SMD simulations.

### First MFS transporter with multiple conformational states resolved

This study represents the first major facilitator superfamily (MFS) transporter for which structures have been determined in more than one conformational state. The two structures — inward open (PDB 4JA4, P6_1, 4.2 A) and partially occluded inward open (PDB 4JA3, C2, 3.8 A) — together with the previously reported partially occluded outward-facing structure (PDB 4GBY) provide three snapshots along the transport cycle, establishing XylE as an important MFS model protein.

### Alternate access mechanism captured in crystal structures

The XylE structures reveal the alternate access mechanism of MFS transporters. In the inward open state, the N and C subdomains form a V-shaped structure with a wide cytoplasmic opening extending to the binding site. In the partially occluded inward open state, the C-terminal half of the interrupted transmembrane helix 10 (TM10b) moves closer to the N subdomain, partially blocking the cytoplasmic opening. The rigid body movement of the two subdomains relative to each other drives the conformational transitions.

### Conserved cytoplasmic salt bridges control substrate access

Three intersubdomain salt bridges (Glu153-Arg404, Arg160-Glu397, Arg225-Glu472) form in the partially occluded outward-facing conformation and are broken in the inward open state, controlling access to the binding site from the cytoplasm. In the partially occluded inward open state, Glu397 forms a new interaction with the N terminus of TM5. The break in TM10 renders TM10b highly dynamic, facilitating partial occlusion through interaction with TM5.

### Substrate binding site and release mechanism

The [D-Xylose](/xray-mp-wiki/reagents/substrates/d-xylose)-binding site is composed of residues from both N and C subdomains. In the inward open state, the two half-sites move apart, and Trp392 moves substantially, lowering affinity and facilitating substrate release. This explains the asymmetric transport of [SLC2A1](/xray-mp-wiki/proteins/glut1) with higher affinity for binding at the extracellular than the intracellular side.

### Periplasmic interface dominated by hydrophobic interactions

At the periplasmic side, interactions between the N and C subdomains are tighter in the inward open conformation than in the partially occluded outward open conformation, but the differences are modest. The periplasmic interface is dominated by van der Waals and hydrophobic interactions with no evidence for conserved salt bridges, suggesting a different mechanistic model is needed to explain the transition between occluded and outward open states.


## Cross-References

- <a href="/xray-mp-wiki/proteins/mfs-transporters/glut1/">Human Glucose Transporter GLUT1 (SLC2A1)</a> — Human homologue; structural comparison reveals 16 degree domain rotation between inward-open GLUT1 and outward-facing XylE
- <a href="/xray-mp-wiki/concepts/protein-families/mfs-transporter/">Major Facilitator Superfamily (MFS)</a> — XylE belongs to the MFS, specifically the sugar porter subfamily
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — XylE captures an outward-facing conformation in the alternating-access cycle
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/rocker-switch-mechanism/">Rocker-Switch Mechanism</a> — XylE asymmetric rocker-switch movement revealed by MD simulations
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent for XylE solubilization and purification
- <a href="/xray-mp-wiki/reagents/detergents/dm/">Decylmaltoside (DM)</a> — Used at 1% for XylE solubilization in ncomms5521 study
- <a href="/xray-mp-wiki/reagents/additives/peg-600/">PEG 600</a> — Crystallization precipitant at 20% for inward-open conformation
- <a href="/xray-mp-wiki/reagents/additives/calcium-acetate/">Calcium Acetate</a> — Crystallization additive at 0.2 M for inward-open conformation
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Used for Ni-NTA elution of His-tagged XylE at 300 mM
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA Agarose Resin</a> — Affinity purification of His-tagged XylE
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — SEC polishing of XylE
- <a href="/xray-mp-wiki/reagents/protein-tags/thrombin-protease/">Thrombin Protease</a> — Used to cleave His-tag from XylE
- <a href="/xray-mp-wiki/reagents/substrates/d-xylose/">D-Xylose</a> — Primary ligand studied; substrate for XylE transport
- <a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a> — Competitive inhibitor of XylE; binds with Kd 0.77 mM; also used as crystallization additive
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-dynamics-simulation/">Molecular Dynamics Simulation</a> — Used to investigate transport cycle and proton-coupling mechanism
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> — Buffer used for SEC purification and final sample preparation (20 mM HEPES pH adjusted)
- <a href="/xray-mp-wiki/reagents/additives/tcep/">Tris(2-carboxyethyl)phosphine (TCEP)</a> — Reducing agent used at 0.5 mM in lysis, solubilization, and purification buffers
- <a href="/xray-mp-wiki/reagents/protein-tags/histidine-tag/">His6-tag</a> — N-terminal His6-TEV tag used for IMAC purification of XylE in nsmb.2569 study
