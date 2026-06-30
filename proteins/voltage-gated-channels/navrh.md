---
title: "NavRh (NaChBac Orthologue from HIMB114)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature11054]
verified: false
---

# NavRh (NaChBac Orthologue from HIMB114)

## Overview

NavRh is a bacterial voltage-gated sodium channel from the marine alphaproteobacterium HIMB114 (Rickettsiales sp.) that is an orthologue of the [NaChBac Bacterial Voltage-Gated Sodium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/nachbac/) family. The 3.05 A crystal structure of NavRh (PDB 4F4L) reveals an asymmetric homotetramer with the selectivity filter in a closed conformation and voltage sensors in a depolarized (up) conformation. A hydrated Ca2+ ion is bound at an inner site within the selectivity filter, formed by the carbonyl oxygen atoms of Thr178 and Leu179. The structure is proposed to represent an inactivated conformation of a voltage-gated sodium channel, providing insights into the electromechanical coupling mechanism and C-type inactivation.

## Publications

### doi/10.1038##nature11054

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4f4l">4F4L</a></td>
      <td>3.05 A</td>
      <td>P42</td>
      <td>Full-length NavRh (G208S variant for improved diffraction), C-terminal His6 tag removed, expressed in E. coli BL21(DE3), purified in <a href="/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/">NG</a> with <a href="/xray-mp-wiki/reagents/lipids/popc/">POPC</a>:<a href="/xray-mp-wiki/reagents/lipids/pope/">POPE</a>:<a href="/xray-mp-wiki/reagents/lipids/popg/">POPG</a> (3:1:1) lipids; crystallized with 100 mM CaCl2</td>
      <td>Ca2+ (bound in selectivity filter inner site)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4dxw">4DXW</a></td>
      <td>3.7 A</td>
      <td>P42</td>
      <td>Wild-type NavRh (same expression/purification as G208S variant)</td>
      <td>Ca2+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4dxw">4DXW</a></td>
      <td>4.4 A</td>
      <td>P41212</td>
      <td>Wild-type NavRh (alternative crystal form)</td>
      <td>Ca2+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3)
- **Construct**: Full-length NavRh (codon-optimized for E. coli), with or without C-terminal His6 tag; G208S or G208A mutations for improved diffraction

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
      <td>Cell culture and expression</td>
      <td>E. coli BL21(DE3) overexpression induced with 0.2 mM <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> at D600nm of 1.5, grown at 30 C for 12 h</td>
      <td>--</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl + --</td>
      <td>Cells harvested by centrifugation; no protease inhibitors used</td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>Sonication</td>
      <td>--</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl + --</td>
      <td>Cell debris removed at 27,000g for 10 min</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Ultracentrifugation at 150,000g for 1 h</td>
      <td>--</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl + --</td>
      <td>Membrane fraction collected</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Membrane solubilization with detergent</td>
      <td>--</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 500 mM NaCl, 50 mM imidazole-HCl pH 8.0 + 1.6% n-dodecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>) for 2 h at 4 C</td>
      <td>After solubilization, supernatant clarified at 150,000g for 30 min</td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni2+-nitrilotriacetate (Qiagen)</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 500 mM NaCl, 50 mM imidazole-HCl pH 8.0, 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Eluted with 400 mM imidazole-HCl pH 8.0; His6 tag removed for crystallization</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC (<a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/30)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> (GE Healthcare)</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl, 0.4% <a href="/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/">NG</a>, 0.1 mg/mL <a href="/xray-mp-wiki/reagents/lipids/popc/">POPC</a>:<a href="/xray-mp-wiki/reagents/lipids/pope/">POPE</a>:<a href="/xray-mp-wiki/reagents/lipids/popg/">POPG</a> (3:1:1) + 0.4% <a href="/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/">NG</a></td>
      <td>Detergent exchanged to <a href="/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/">NG</a> during purification; lipids added for stability</td>
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
      <td>NavRh (G208S variant) at ~10 mg/mL in 0.4% <a href="/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/">NG</a>, <a href="/xray-mp-wiki/reagents/lipids/popc/">POPC</a>:<a href="/xray-mp-wiki/reagents/lipids/pope/">POPE</a>:<a href="/xray-mp-wiki/reagents/lipids/popg/">POPG</a> (3:1:1), 25 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>16% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400 (v/v), 100 mM MES-NaOH pH 6.0, 100 mM CaCl2</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>18 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Overnight</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Cryo-cooled in liquid nitrogen; <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400 in reservoir serves as cryoprotectant</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals belonged to space group P42 with one tetramer per asymmetric unit. CaCl2 (100 mM) was a prerequisite for obtaining well-diffracting crystals. Initial phases derived from mercury-based single-wavelength anomalous dispersion (SAD). Wild-type crystals also obtained in P41212 space group diffracting to ~4.5 and 3.7 A.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4f4l">4F4L</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110  </span>
<span class="topo-line"><span class="topo-unknown">GSHMGVG</span><span class="topo-inside">SV</span><span class="topo-membrane">AALLTVVFYIAAVMATNLY</span><span class="topo-outside">GATFPEWFGD</span><span class="topo-unknown">LSKSLYTLFQVMTLESWSMGIVR</span><span class="topo-outside">PVMNVHP</span><span class="topo-membrane">NAWVFFIPFIMLTTFTVLNLF</span><span class="topo-inside">IGII</span><span class="topo-unknown">VDAMAITKEQEEEAKTGHH</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>9</td>
      <td>8</td>
      <td>9</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>28</td>
      <td>10</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>38</td>
      <td>29</td>
      <td>38</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>61</td>
      <td>39</td>
      <td>61</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>62</td>
      <td>68</td>
      <td>62</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>89</td>
      <td>69</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>93</td>
      <td>90</td>
      <td>93</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>112</td>
      <td>94</td>
      <td>112</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4f4l">4F4L</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110  </span>
<span class="topo-line"><span class="topo-unknown">GSHMGVG</span><span class="topo-inside">SV</span><span class="topo-membrane">AALLTVVFYIAAVMATNL</span><span class="topo-outside">YGATFPEWFGD</span><span class="topo-unknown">LSKSLYTLFQVMTLESWSM</span><span class="topo-outside">GIVRPVMNVHPN</span><span class="topo-membrane">AWVFFIPFIMLTTFTVLNLF</span><span class="topo-inside">IGIIVDA</span><span class="topo-unknown">MAITKEQEEEAKTGHH</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>9</td>
      <td>8</td>
      <td>9</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>27</td>
      <td>10</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>38</td>
      <td>28</td>
      <td>38</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>57</td>
      <td>39</td>
      <td>57</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>69</td>
      <td>58</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>89</td>
      <td>70</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>96</td>
      <td>90</td>
      <td>96</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>112</td>
      <td>97</td>
      <td>112</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4f4l">4F4L</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110  </span>
<span class="topo-line"><span class="topo-unknown">GSH</span><span class="topo-inside">MGVGSV</span><span class="topo-membrane">AALLTVVFYIAAVMATNLY</span><span class="topo-outside">GATFPEWFGD</span><span class="topo-unknown">LSKSLYTLFQVMTLESWSMGIVR</span><span class="topo-outside">PVMNVHP</span><span class="topo-membrane">NAWVFFIPFIMLTTFTVLNLF</span><span class="topo-inside">IGIIVDA</span><span class="topo-unknown">MAITKEQEEEAKTGHH</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>9</td>
      <td>4</td>
      <td>9</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>28</td>
      <td>10</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>38</td>
      <td>29</td>
      <td>38</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>61</td>
      <td>39</td>
      <td>61</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>62</td>
      <td>68</td>
      <td>62</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>89</td>
      <td>69</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>96</td>
      <td>90</td>
      <td>96</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>112</td>
      <td>97</td>
      <td>112</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4f4l">4F4L</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110  </span>
<span class="topo-line"><span class="topo-unknown">GSHMGVG</span><span class="topo-inside">SV</span><span class="topo-membrane">AALLTVVFYIAAVMATNLY</span><span class="topo-outside">GATFPEWFGD</span><span class="topo-unknown">LSKSLYTLFQVMTLESWSM</span><span class="topo-outside">GIVRPVMNVHPN</span><span class="topo-membrane">AWVFFIPFIMLTTFTVLNLF</span><span class="topo-inside">IGIIVDAMA</span><span class="topo-unknown">ITKEQEEEAKTGHH</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>9</td>
      <td>8</td>
      <td>9</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>28</td>
      <td>10</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>38</td>
      <td>29</td>
      <td>38</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>57</td>
      <td>39</td>
      <td>57</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>69</td>
      <td>58</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>89</td>
      <td>70</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>98</td>
      <td>90</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>112</td>
      <td>99</td>
      <td>112</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4dxw">4DXW</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">TPFFSSLKDNRIFQ</span><span class="topo-membrane">FTVVSIIILNAVLIGATT</span><span class="topo-inside">YEL</span><span class="topo-membrane">DPLFLETIHLLDYGITIFFV</span><span class="topo-outside">IEILIRFIG</span><span class="topo-unknown">EKQKADFFK</span><span class="topo-outside">SGWNIF</span><span class="topo-membrane">DTVIVAISLIP</span><span class="topo-unknown">IPNNSSFL</span><span class="topo-inside">V</span><span class="topo-membrane">LRLLRIFRVLRLISV</span><span class="topo-outside">I</span><span class="topo-unknown">PELK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220         </span>
<span class="topo-line"><span class="topo-unknown">QIIEAILESVRRV</span><span class="topo-membrane">FFVSLLLFIILYIYATMGAIL</span><span class="topo-inside">FGNDDPSRWGD</span><span class="topo-unknown">LGISLITLFQVLTLSSWETVMLPMQEI</span><span class="topo-inside">YW</span><span class="topo-membrane">WSWVYFFSFIIICSITILNLV</span><span class="topo-outside">IAILVDVVIQKKL</span><span class="topo-unknown">E</span></span>
<details class="topo-details"><summary>Topology coordinates (21 regions)</summary>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>15</td>
      <td>2</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>33</td>
      <td>16</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>36</td>
      <td>34</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>56</td>
      <td>37</td>
      <td>56</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>65</td>
      <td>57</td>
      <td>65</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>74</td>
      <td>66</td>
      <td>74</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>75</td>
      <td>80</td>
      <td>75</td>
      <td>80</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>91</td>
      <td>81</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>99</td>
      <td>92</td>
      <td>99</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>100</td>
      <td>100</td>
      <td>100</td>
      <td>100</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>115</td>
      <td>101</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>116</td>
      <td>116</td>
      <td>116</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>133</td>
      <td>117</td>
      <td>133</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>134</td>
      <td>154</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>165</td>
      <td>155</td>
      <td>165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>192</td>
      <td>166</td>
      <td>192</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>193</td>
      <td>194</td>
      <td>193</td>
      <td>194</td>
      <td>Inside</td>
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
      <td>228</td>
      <td>216</td>
      <td>228</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>229</td>
      <td>229</td>
      <td>229</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4dxw">4DXW</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTP</span><span class="topo-outside">FFSSLKDNRIFQF</span><span class="topo-membrane">TVVSIIILNAVLIG</span><span class="topo-inside">ATTYEL</span><span class="topo-membrane">DPLFLETIHLLDYGITIF</span><span class="topo-outside">FVIEILIRFIGEKQKA</span><span class="topo-unknown">DFFK</span><span class="topo-outside">SGWNIFDTV</span><span class="topo-membrane">IVAISLIPIPNNSS</span><span class="topo-inside">F</span><span class="topo-membrane">LVLRLLRIFRVLRLI</span><span class="topo-outside">SVI</span><span class="topo-unknown">PELK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220         </span>
<span class="topo-line"><span class="topo-unknown">QIIEAILESVRRV</span><span class="topo-membrane">FFVSLLLFIILYIYATMGAIL</span><span class="topo-inside">FGNDDPSRWGD</span><span class="topo-unknown">LGISLITLFQVLTLSSWETVMLPMQEI</span><span class="topo-inside">YW</span><span class="topo-membrane">WSWVYFFSFIIICSITILNL</span><span class="topo-outside">VIAILVDVVIQKKLE</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
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
      <td>16</td>
      <td>4</td>
      <td>16</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>30</td>
      <td>17</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>36</td>
      <td>31</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>54</td>
      <td>37</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>70</td>
      <td>55</td>
      <td>70</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>74</td>
      <td>71</td>
      <td>74</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>75</td>
      <td>83</td>
      <td>75</td>
      <td>83</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>97</td>
      <td>84</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>98</td>
      <td>98</td>
      <td>98</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>113</td>
      <td>99</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>116</td>
      <td>114</td>
      <td>116</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>133</td>
      <td>117</td>
      <td>133</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>134</td>
      <td>154</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>165</td>
      <td>155</td>
      <td>165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>192</td>
      <td>166</td>
      <td>192</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>193</td>
      <td>194</td>
      <td>193</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>214</td>
      <td>195</td>
      <td>214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>229</td>
      <td>215</td>
      <td>229</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4dxw">4DXW</a> — Chain C (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTPFFSSL</span><span class="topo-outside">KDNRIFQF</span><span class="topo-membrane">TVVSIIILNAVLIG</span><span class="topo-inside">ATTYEL</span><span class="topo-membrane">DPLFLETIHLLDYGITI</span><span class="topo-outside">FFVIEILI</span><span class="topo-unknown">RFIGEKQKADFFKS</span><span class="topo-outside">GWNIF</span><span class="topo-membrane">DTVIVAISLIP</span><span class="topo-unknown">IPNNS</span><span class="topo-inside">S</span><span class="topo-membrane">FLVLRLLRIFRVLRLI</span><span class="topo-outside">SVIP</span><span class="topo-unknown">ELK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220         </span>
<span class="topo-line"><span class="topo-unknown">QIIEAILESVRRV</span><span class="topo-membrane">FFVSLLLFIILYIYATMGAIL</span><span class="topo-inside">FGNDDPSRWGD</span><span class="topo-unknown">LGISLITLFQVLTLSSWETVMLPMQ</span><span class="topo-inside">EIYW</span><span class="topo-membrane">WSWVYFFSFIIICSITIL</span><span class="topo-outside">NLVIAILVDVVIQK</span><span class="topo-unknown">KLE</span></span>
<details class="topo-details"><summary>Topology coordinates (21 regions)</summary>
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
      <td>16</td>
      <td>9</td>
      <td>16</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>30</td>
      <td>17</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>36</td>
      <td>31</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>53</td>
      <td>37</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>61</td>
      <td>54</td>
      <td>61</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>75</td>
      <td>62</td>
      <td>75</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>76</td>
      <td>80</td>
      <td>76</td>
      <td>80</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>91</td>
      <td>81</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>96</td>
      <td>92</td>
      <td>96</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>97</td>
      <td>97</td>
      <td>97</td>
      <td>97</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>113</td>
      <td>98</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>117</td>
      <td>114</td>
      <td>117</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>133</td>
      <td>118</td>
      <td>133</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>134</td>
      <td>154</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>165</td>
      <td>155</td>
      <td>165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>190</td>
      <td>166</td>
      <td>190</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>191</td>
      <td>194</td>
      <td>191</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>212</td>
      <td>195</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>226</td>
      <td>213</td>
      <td>226</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>227</td>
      <td>229</td>
      <td>227</td>
      <td>229</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4dxw">4DXW</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTPFFSSLKDNRI</span><span class="topo-outside">FQ</span><span class="topo-membrane">FTVVSIIILNAVLIG</span><span class="topo-unknown">ATTY</span><span class="topo-inside">EL</span><span class="topo-membrane">DPLFLETIHLLDYGITIFFV</span><span class="topo-outside">IEILIRFI</span><span class="topo-unknown">GEKQKADFFKS</span><span class="topo-outside">GWNIF</span><span class="topo-membrane">DTVIVAISLIPIPN</span><span class="topo-inside">NSS</span><span class="topo-membrane">FLVLRLLRIFRVLRLISVI</span><span class="topo-unknown">PELK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220         </span>
<span class="topo-line"><span class="topo-unknown">QIIEAILESVRRV</span><span class="topo-membrane">FFVSLLLFIILYIYATMGAIL</span><span class="topo-inside">FGNDDPSRWGD</span><span class="topo-unknown">LGISLITLFQVLTLSSWETVMLPMQEI</span><span class="topo-inside">YW</span><span class="topo-membrane">WSWVYFFSFIIICSITIL</span><span class="topo-outside">NLVIAILVDVVIQKK</span><span class="topo-unknown">LE</span></span>
<details class="topo-details"><summary>Topology coordinates (20 regions)</summary>
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
      <td>13</td>
      <td>1</td>
      <td>13</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>14</td>
      <td>15</td>
      <td>14</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>30</td>
      <td>16</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>34</td>
      <td>31</td>
      <td>34</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>35</td>
      <td>36</td>
      <td>35</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>56</td>
      <td>37</td>
      <td>56</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>64</td>
      <td>57</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>75</td>
      <td>65</td>
      <td>75</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>76</td>
      <td>80</td>
      <td>76</td>
      <td>80</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>94</td>
      <td>81</td>
      <td>94</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>95</td>
      <td>97</td>
      <td>95</td>
      <td>97</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>116</td>
      <td>98</td>
      <td>116</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>117</td>
      <td>133</td>
      <td>117</td>
      <td>133</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>134</td>
      <td>154</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>165</td>
      <td>155</td>
      <td>165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>192</td>
      <td>166</td>
      <td>192</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>193</td>
      <td>194</td>
      <td>193</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>212</td>
      <td>195</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>227</td>
      <td>213</td>
      <td>227</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>229</td>
      <td>228</td>
      <td>229</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4dxw">4DXW</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">TPFFSSLKDNRIFQ</span><span class="topo-membrane">FTVVSIIILNAVLIGATT</span><span class="topo-inside">YEL</span><span class="topo-membrane">DPLFLETIHLLDYGITIFFV</span><span class="topo-outside">IEILIRFIG</span><span class="topo-unknown">EKQKADFFK</span><span class="topo-outside">SGWNIF</span><span class="topo-membrane">DTVIVAISLIP</span><span class="topo-unknown">IPNNSSFL</span><span class="topo-inside">V</span><span class="topo-membrane">LRLLRIFRVLRLISV</span><span class="topo-outside">I</span><span class="topo-unknown">PELK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220         </span>
<span class="topo-line"><span class="topo-unknown">QIIEAILESVRRV</span><span class="topo-membrane">FFVSLLLFIILYIYATMGAIL</span><span class="topo-inside">FGNDDPSRWGD</span><span class="topo-unknown">LGISLITLFQVLTLSSWETVMLPMQEI</span><span class="topo-inside">YW</span><span class="topo-membrane">WSWVYFFSFIIICSITILNLV</span><span class="topo-outside">IAILVDVVIQKKL</span><span class="topo-unknown">E</span></span>
<details class="topo-details"><summary>Topology coordinates (21 regions)</summary>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>15</td>
      <td>2</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>33</td>
      <td>16</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>36</td>
      <td>34</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>56</td>
      <td>37</td>
      <td>56</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>65</td>
      <td>57</td>
      <td>65</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>74</td>
      <td>66</td>
      <td>74</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>75</td>
      <td>80</td>
      <td>75</td>
      <td>80</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>91</td>
      <td>81</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>99</td>
      <td>92</td>
      <td>99</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>100</td>
      <td>100</td>
      <td>100</td>
      <td>100</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>115</td>
      <td>101</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>116</td>
      <td>116</td>
      <td>116</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>133</td>
      <td>117</td>
      <td>133</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>134</td>
      <td>154</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>165</td>
      <td>155</td>
      <td>165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>192</td>
      <td>166</td>
      <td>192</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>193</td>
      <td>194</td>
      <td>193</td>
      <td>194</td>
      <td>Inside</td>
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
      <td>228</td>
      <td>216</td>
      <td>228</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>229</td>
      <td>229</td>
      <td>229</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4dxw">4DXW</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTP</span><span class="topo-outside">FFSSLKDNRIFQF</span><span class="topo-membrane">TVVSIIILNAVLIG</span><span class="topo-inside">ATTYEL</span><span class="topo-membrane">DPLFLETIHLLDYGITIF</span><span class="topo-outside">FVIEILIRFIGEKQKA</span><span class="topo-unknown">DFFK</span><span class="topo-outside">SGWNIFDTV</span><span class="topo-membrane">IVAISLIPIPNNSS</span><span class="topo-inside">F</span><span class="topo-membrane">LVLRLLRIFRVLRLI</span><span class="topo-outside">SVI</span><span class="topo-unknown">PELK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220         </span>
<span class="topo-line"><span class="topo-unknown">QIIEAILESVRRV</span><span class="topo-membrane">FFVSLLLFIILYIYATMGAIL</span><span class="topo-inside">FGNDDPSRWGD</span><span class="topo-unknown">LGISLITLFQVLTLSSWETVMLPMQEI</span><span class="topo-inside">YW</span><span class="topo-membrane">WSWVYFFSFIIICSITILNL</span><span class="topo-outside">VIAILVDVVIQKKLE</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
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
      <td>16</td>
      <td>4</td>
      <td>16</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>30</td>
      <td>17</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>36</td>
      <td>31</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>54</td>
      <td>37</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>70</td>
      <td>55</td>
      <td>70</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>74</td>
      <td>71</td>
      <td>74</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>75</td>
      <td>83</td>
      <td>75</td>
      <td>83</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>97</td>
      <td>84</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>98</td>
      <td>98</td>
      <td>98</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>113</td>
      <td>99</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>116</td>
      <td>114</td>
      <td>116</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>133</td>
      <td>117</td>
      <td>133</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>134</td>
      <td>154</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>165</td>
      <td>155</td>
      <td>165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>192</td>
      <td>166</td>
      <td>192</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>193</td>
      <td>194</td>
      <td>193</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>214</td>
      <td>195</td>
      <td>214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>229</td>
      <td>215</td>
      <td>229</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4dxw">4DXW</a> — Chain C (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTPFFSSL</span><span class="topo-outside">KDNRIFQF</span><span class="topo-membrane">TVVSIIILNAVLIG</span><span class="topo-inside">ATTYEL</span><span class="topo-membrane">DPLFLETIHLLDYGITI</span><span class="topo-outside">FFVIEILI</span><span class="topo-unknown">RFIGEKQKADFFKS</span><span class="topo-outside">GWNIF</span><span class="topo-membrane">DTVIVAISLIP</span><span class="topo-unknown">IPNNS</span><span class="topo-inside">S</span><span class="topo-membrane">FLVLRLLRIFRVLRLI</span><span class="topo-outside">SVIP</span><span class="topo-unknown">ELK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220         </span>
<span class="topo-line"><span class="topo-unknown">QIIEAILESVRRV</span><span class="topo-membrane">FFVSLLLFIILYIYATMGAIL</span><span class="topo-inside">FGNDDPSRWGD</span><span class="topo-unknown">LGISLITLFQVLTLSSWETVMLPMQ</span><span class="topo-inside">EIYW</span><span class="topo-membrane">WSWVYFFSFIIICSITIL</span><span class="topo-outside">NLVIAILVDVVIQK</span><span class="topo-unknown">KLE</span></span>
<details class="topo-details"><summary>Topology coordinates (21 regions)</summary>
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
      <td>16</td>
      <td>9</td>
      <td>16</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>30</td>
      <td>17</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>36</td>
      <td>31</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>53</td>
      <td>37</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>61</td>
      <td>54</td>
      <td>61</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>75</td>
      <td>62</td>
      <td>75</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>76</td>
      <td>80</td>
      <td>76</td>
      <td>80</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>91</td>
      <td>81</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>96</td>
      <td>92</td>
      <td>96</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>97</td>
      <td>97</td>
      <td>97</td>
      <td>97</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>113</td>
      <td>98</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>117</td>
      <td>114</td>
      <td>117</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>133</td>
      <td>118</td>
      <td>133</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>134</td>
      <td>154</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>165</td>
      <td>155</td>
      <td>165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>190</td>
      <td>166</td>
      <td>190</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>191</td>
      <td>194</td>
      <td>191</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>212</td>
      <td>195</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>226</td>
      <td>213</td>
      <td>226</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>227</td>
      <td>229</td>
      <td>227</td>
      <td>229</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4dxw">4DXW</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTPFFSSLKDNRI</span><span class="topo-outside">FQ</span><span class="topo-membrane">FTVVSIIILNAVLIG</span><span class="topo-unknown">ATTY</span><span class="topo-inside">EL</span><span class="topo-membrane">DPLFLETIHLLDYGITIFFV</span><span class="topo-outside">IEILIRFI</span><span class="topo-unknown">GEKQKADFFKS</span><span class="topo-outside">GWNIF</span><span class="topo-membrane">DTVIVAISLIPIPN</span><span class="topo-inside">NSS</span><span class="topo-membrane">FLVLRLLRIFRVLRLISVI</span><span class="topo-unknown">PELK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220         </span>
<span class="topo-line"><span class="topo-unknown">QIIEAILESVRRV</span><span class="topo-membrane">FFVSLLLFIILYIYATMGAIL</span><span class="topo-inside">FGNDDPSRWGD</span><span class="topo-unknown">LGISLITLFQVLTLSSWETVMLPMQEI</span><span class="topo-inside">YW</span><span class="topo-membrane">WSWVYFFSFIIICSITIL</span><span class="topo-outside">NLVIAILVDVVIQKK</span><span class="topo-unknown">LE</span></span>
<details class="topo-details"><summary>Topology coordinates (20 regions)</summary>
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
      <td>13</td>
      <td>1</td>
      <td>13</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>14</td>
      <td>15</td>
      <td>14</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>30</td>
      <td>16</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>34</td>
      <td>31</td>
      <td>34</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>35</td>
      <td>36</td>
      <td>35</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>56</td>
      <td>37</td>
      <td>56</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>64</td>
      <td>57</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>75</td>
      <td>65</td>
      <td>75</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>76</td>
      <td>80</td>
      <td>76</td>
      <td>80</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>94</td>
      <td>81</td>
      <td>94</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>95</td>
      <td>97</td>
      <td>95</td>
      <td>97</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>116</td>
      <td>98</td>
      <td>116</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>117</td>
      <td>133</td>
      <td>117</td>
      <td>133</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>134</td>
      <td>154</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>165</td>
      <td>155</td>
      <td>165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>192</td>
      <td>166</td>
      <td>192</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>193</td>
      <td>194</td>
      <td>193</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>212</td>
      <td>195</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>227</td>
      <td>213</td>
      <td>227</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>229</td>
      <td>228</td>
      <td>229</td>
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

### Asymmetric tetramer structure of NavRh

NavRh crystallizes as an asymmetric homotetramer at 3.05 A resolution. The four protomers (Mol A-D) show subtle conformational variations in the selectivity filter and more prominent divergences in the voltage-sensing domains, particularly the S3-S4 linkers. S3-S4 linkers in Mol A and Mol C are unresolved, while those in Mol B and Mol D show distinct conformations, suggesting flexibility that may allow S4 movement during voltage sensing.

### Selectivity filter binds hydrated Ca2+ in inner site

A Ca2+ ion is bound at an inner site within the selectivity filter, coordinated by the eight carbonyl oxygen atoms from Thr178 and Leu179 at distances of 3.5-4.6 A, suggesting the ion is stabilized in a fully or mostly hydrated state. The outer mouth of the selectivity filter, defined by Ser181 and Glu183, is closed. This provides structural evidence that Nav channels allow passage of mostly hydrated Na+ and that Ca2+ can block Na+ permeation by occluding the pore at the Leu179/Thr178 site.

### Voltage sensors in depolarized conformation

All four voltage-sensing domains (VSDs) of NavRh exhibit a depolarized (up) conformation with all four conserved arginine residues (R1-R4) on the S4 segment pointing extracellularly. The external negative clusters stabilize gating charges through two invariant interactions: R4 interacts with Asp48 on S2, and R3 is hydrogen-bonded to the carbonyl of Ile90 on S3. This is consistent with the 0 mV field during crystallization.

### NavRh represents an inactivated conformation

The combination of a closed inner (activation) gate, depolarized VSDs (up conformation), and closed outer mouth of the selectivity filter (Glu183 and Ser181 closing the filter entry) indicates that NavRh represents an inactivated conformation. The Glu183 residue (and its equivalents in rat Nav1.4: Glu403, Glu758, Asp1241, Asp1532) are known to be important for C-type inactivation, and their conformation in NavRh supports a role for the selectivity filter outer negative charges in the inactivation process.

### One helical turn shift of S4 compared to NavAb

Comparison of NavRh with [NAVAB](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) reveals a one helical turn shift of the S4 segment towards the extracellular side in NavRh relative to [NAVAB](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) when the charge transfer centers (CTCs) are superimposed. For each NavRh VSD, one more gating charge is transferred than for each [NAVAB](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) VSD. In NavRh, the segment from R1-R2 forms an alpha-helix, while in [NAVAB](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) the corresponding segment is a 3(10)-helix, suggesting different degrees of activation between the two channels.

### Anti-clockwise rotation of VSDs relative to pore

Viewed from the cytoplasm, the VSDs of NavRh are rotated anticlockwise around the pore axis by approximately 30 degrees compared to [NAVAB](/xray-mp-wiki/proteins/voltage-gated-channels/navab/). The relative positions of NavRh VSDs are more similar to those in the depolarized and open conformation of Kv1.2, consistent with NavRh being in a more fully activated VSD conformation despite having a closed pore.


## Cross-References

- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/navab/">NavAb Bacterial Voltage-Gated Sodium Channel</a> — Key structural comparison for voltage-sensing mechanism and S4 movement
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/nachbac/">NaChBac Bacterial Voltage-Gated Sodium Channel</a> — NavRh is an orthologue of NaChBac; functional comparison for inactivation
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/sodium-channel-gating/">Sodium Channel Gating and Selectivity</a> — Paper discusses electromechanical coupling and voltage-sensing mechanism
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/c-type-inactivation/">C-Type Inactivation</a> — NavRh structure proposed to represent an inactivated conformation
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/sodium-channel-inactivation-gating/">Sodium Channel Inactivation Gating</a> — Structural insights into inactivation mechanism of voltage-gated sodium channels
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> — Buffer component in purification or crystallization
