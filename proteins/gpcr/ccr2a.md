---
title: "CC Chemokine Receptor 2A (CCR2A)"
created: 2026-05-29
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2018.10.027]
verified: false
---

# CC Chemokine Receptor 2A (CCR2A)

## Overview

CC chemokine receptor 2A (CCR2A) is a class A G protein-coupled receptor and the major isoform of CCR2 expressed by mononuclear cells and vascular smooth muscle cells. CCR2 is a widely studied chemokine receptor involved in inflammatory diseases. CCR2A serves as the primary binding target for the chemokine CCL2 (monocyte chemoattractant protein-1) and is implicated in atherosclerosis, rheumatoid arthritis, and multiple sclerosis. Two crystal structures of CCR2A in complex with the orthosteric antagonist [MK-0812](/xray-mp-wiki/reagents/ligands/mk-0812/) were solved, providing structural insights into antagonist binding and selectivity over CCR5.


## Publications

### doi/10.1016##j.str.2018.10.027

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6gps">6GPS</a></td>
      <td>3.30</td>
      <td>P21</td>
      <td>Full-length CCR2A with <a href="/xray-mp-wiki/reagents/protein-tags/rubredoxin/">Rubredoxin</a> fusion in ICL3 (residues L226-R240 replaced) and five point mutations: N14Q, C70Y(1.60), G175N(4.60), A241D(6.33), K311E(8.49). C-terminal His6/FLAG tag. Truncated at C-terminus residue R313(8.51).</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/mk-0812/">MK-0812</a> (orthosteric antagonist)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6gpx">6GPX</a></td>
      <td>2.70</td>
      <td>P21</td>
      <td>N- and C-terminally truncated CCR2A. Removed 28 N-terminal residues and 53 C-terminal residues. <a href="/xray-mp-wiki/reagents/protein-tags/rubredoxin/">Rubredoxin</a> fusion in ICL3. Reverted K311E mutation back to WT K311. C-terminal end resolved up to residue G321. Chain A selected for highest quality data.</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/mk-0812/">MK-0812</a> (orthosteric antagonist)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: High Five insect cells (BTI-TN-5B1-4, Trichoplusia ni ovarian cells), [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) expression system
- **Construct**: Full-length and truncated CCR2A constructs with [Rubredoxin](/xray-mp-wiki/reagents/protein-tags/rubredoxin/) fusion in ICL3, point mutations for stabilization (N14Q, C70Y, G175N, A241D, K311E), C-terminal His6/FLAG tag. High Five cells infected at 10^6 cells/mL, grown in Wave cultivation bags up to 8.5 L.

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
      <td>Thawing in hypotonic buffer (10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES (HEPES Buffer)</a> pH 7.5, 10 mM MgCl2, 20 mM KCl), N2 disruption bomb at 50 bar</td>
      <td>--</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES (HEPES Buffer)</a> pH 7.5, 10 mM MgCl2, 20 mM KCl, 0.5 mg/mL DNase, EDTA-free protease inhibitor cocktail + --</td>
      <td>Membranes washed, supplemented with 30% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> and 2 mg/mL <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a>, incubated 1 h at 4 C</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Solubilization of membranes with detergent</td>
      <td>--</td>
      <td>Membrane preparation buffer + 1.0% <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Solubilized for at least 2 hours at 4 C; clarified by centrifugation at 100,000 x g for 1 h</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON Cobalt Affinity Resin</a> Superflow Metal Affinity Resin (Ni-IMAC)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON Cobalt Affinity Resin</a> Superflow</td>
      <td>25 mM HEPES pH 7.5, 150 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 30 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> (wash); 200 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> (elution) + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>6 eluates of 10 min each; 1 mL resin per 1 L culture. Elution buffer: 25 mM HEPES pH 7.5, 150 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.005% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 200 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 10 mM MgCl2</td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td><a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a> treatment overnight at 4 C</td>
      <td>--</td>
      <td>Buffer without <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> (post PD-10 desalting) + --</td>
      <td>10 U/mg protein; removed C-terminal <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a> and His tags</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size Exclusion Chromatography</a></td>
      <td>HiLoad <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200 Increase SEC Resin</a> pg 200 column</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200 Increase SEC Resin</a> pg 200</td>
      <td>25 mM HEPES pH 7.5, 150 mM NaCl, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.005% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 1 uM <a href="/xray-mp-wiki/reagents/ligands/mk-0812/">MK-0812</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a>, 0.005% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Concentrated to 40-50 mg/mL using 30 kDa MWCO concentrator; yields varied 0.5-2 mg/L depending on construct</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<<<<<<< HEAD
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>), conventional glass sandwich plates</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> crystallization with IMISX in-situ plates</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not specified</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**
=======
| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane preparation | Thawing in hypotonic buffer (10 mM [HEPES (HEPES Buffer)](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 10 mM MgCl2, 20 mM KCl), N2 disruption bomb at 50 bar | -- | 10 mM [HEPES (HEPES Buffer)](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 10 mM MgCl2, 20 mM KCl, 0.5 mg/mL DNase, EDTA-free protease inhibitor cocktail + -- | Membranes washed, supplemented with 30% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) and 2 mg/mL [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/), incubated 1 h at 4 C |
| Solubilization | Solubilization of membranes with detergent | -- | Membrane preparation buffer + 1.0% [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/), 0.1% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Solubilized for at least 2 hours at 4 C; clarified by centrifugation at 100,000 x g for 1 h |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon/) Superflow Metal Affinity Resin (Ni-IMAC) | [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon/) Superflow | 25 mM HEPES pH 7.5, 150 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.05% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 30 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (wash); 200 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (elution) + 0.05% [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/), 0.05% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | 6 eluates of 10 min each; 1 mL resin per 1 L culture. Elution buffer: 25 mM HEPES pH 7.5, 150 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.005% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 200 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 10 mM MgCl2 |
| Tag cleavage | [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) treatment overnight at 4 C | -- | Buffer without [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (post PD-10 desalting) + -- | 10 U/mg protein; removed C-terminal [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) and His tags |
| [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | HiLoad [Superdex 200 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200/) pg 200 column | [Superdex 200 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200/) pg 200 | 25 mM HEPES pH 7.5, 150 mM NaCl, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.005% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 1 uM [MK-0812](/xray-mp-wiki/reagents/ligands/mk-0812/) + 0.05% [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/), 0.005% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Concentrated to 40-50 mg/mL using 30 kDa MWCO concentrator; yields varied 0.5-2 mg/L depending on construct |
>>>>>>> d0e2c437136bdf2885afc6a99e0a9d4117821696

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6gps">6GPS</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">LSTSRSRFIRNTQESGEEVTTFFDYDYGAPCHKFD</span><span class="topo-outside">VKQIGAQL</span><span class="topo-membrane">LPPLYSLVFIFGFVGNM</span></span>
<span class="topo-line"><span class="topo-membrane">LVVL</span><span class="topo-inside">ILINYKKLKCLTDI</span><span class="topo-membrane">YLLNLAISDLLFLITLPLWA</span><span class="topo-outside">HSAANEWVFGN</span><span class="topo-membrane">AMCKLFTGLYH</span></span>
<span class="topo-line"><span class="topo-membrane">IGYFGGIFFIIL</span><span class="topo-inside">LTIDRYLAIVHAVFALKARTVTFGVV</span><span class="topo-membrane">TSVITWLVAVFASVPNIIF</span><span class="topo-outside">TKC</span></span>
<span class="topo-line"><span class="topo-outside">QKEDSVYVCGPYFPR</span><span class="topo-membrane">GWNNFHTIMRNILGLVLPLLIMVI</span><span class="topo-inside">CYSGILKTLLRMKKYTCTVCG</span></span>
<span class="topo-line"><span class="topo-inside">YIYNPEDGDPDNGVNPGTDFKDIPDDWVCPLCGVGKDQFEEVEEEKKRHRDVRV</span><span class="topo-membrane">IFTIMI</span></span>
<span class="topo-line"><span class="topo-membrane">VYFLFWTPYNIVILL</span><span class="topo-outside">NTFQEFF</span><span class="topo-unknown">GLSNCE</span><span class="topo-outside">STSQLDQ</span><span class="topo-membrane">ATQVTETLGMTHCCINPIIYAFV</span><span class="topo-inside">GE</span></span>
<span class="topo-line"><span class="topo-inside">EFRSLFHIALG</span><span class="topo-unknown">CRIAPLQKPVCGGPGVRPGKNVKVTTQGLLDGRGKGKSIGRAPEASLQD</span></span>
<span class="topo-line"><span class="topo-unknown">KEGAEVLFQ</span></span>
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
      <td>35</td>
      <td>2</td>
      <td>36</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>36</td>
      <td>43</td>
      <td>37</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>64</td>
      <td>45</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>78</td>
      <td>66</td>
      <td>79</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>98</td>
      <td>80</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>99</td>
      <td>109</td>
      <td>100</td>
      <td>110</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>132</td>
      <td>111</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>133</td>
      <td>158</td>
      <td>134</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>177</td>
      <td>160</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>195</td>
      <td>179</td>
      <td>196</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>219</td>
      <td>197</td>
      <td>220</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>294</td>
      <td>221</td>
      <td>244</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>245</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>316</td>
      <td>322</td>
      <td>266</td>
      <td>272</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>328</td>
      <td>273</td>
      <td>278</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>329</td>
      <td>335</td>
      <td>279</td>
      <td>285</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>336</td>
      <td>358</td>
      <td>286</td>
      <td>308</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>359</td>
      <td>371</td>
      <td>309</td>
      <td>321</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>372</td>
      <td>429</td>
      <td>322</td>
      <td>379</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6gpx">6GPX</a> — Chain A (7 TMs, alpha)**

<<<<<<< HEAD
<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GAPCHKF</span><span class="topo-outside">DVKQIGA</span><span class="topo-membrane">QLLPPLYSLVFIFGFVGNMLVV</span><span class="topo-inside">LILINYKKLKCLTDIYLL</span><span class="topo-membrane">NLAISD</span></span>
<span class="topo-line"><span class="topo-membrane">LLFLITLPLWAHSA</span><span class="topo-outside">ANEWVFG</span><span class="topo-membrane">NAMCKLFTGLYHIGYFGGIFFII</span><span class="topo-inside">LLTIDRYLAIVH</span><span class="topo-unknown">AVFA</span></span>
<span class="topo-line"><span class="topo-unknown">LKAR</span><span class="topo-inside">TVTFGVVT</span><span class="topo-membrane">SVITWLVAVFASVPNIIFTK</span><span class="topo-outside">CQKEDSVYVCGPYFPR</span><span class="topo-membrane">GWNNFHTIMRNI</span></span>
<span class="topo-line"><span class="topo-membrane">LGLVLPLLIMV</span><span class="topo-inside">ICYSGILKTLLRMKKYTCTVCGYIYNPEDGDPDNGVNPGTDFKDIPDDW</span></span>
<span class="topo-line"><span class="topo-inside">VCPLCGVGKDQFEEVE</span><span class="topo-unknown">EEKKRH</span><span class="topo-inside">RDVRVIF</span><span class="topo-membrane">TIMIVYFLFWTPYNIVILLNTF</span><span class="topo-outside">QEFFGLSNC</span></span>
<span class="topo-line"><span class="topo-outside">ESTSQLDQ</span><span class="topo-membrane">ATQVTETLGMTHCCINPII</span><span class="topo-inside">YAFVGEKFRSLFHIALGE</span><span class="topo-unknown">VLFQ</span></span>
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
      <td>29</td>
      <td>35</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>14</td>
      <td>36</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>36</td>
      <td>43</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>37</td>
      <td>54</td>
      <td>65</td>
      <td>82</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>74</td>
      <td>83</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>81</td>
      <td>103</td>
      <td>109</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>104</td>
      <td>110</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>116</td>
      <td>133</td>
      <td>144</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>124</td>
      <td>145</td>
      <td>152</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>125</td>
      <td>132</td>
      <td>153</td>
      <td>160</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>152</td>
      <td>161</td>
      <td>180</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>153</td>
      <td>168</td>
      <td>181</td>
      <td>196</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>169</td>
      <td>191</td>
      <td>197</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>192</td>
      <td>256</td>
      <td>220</td>
      <td>284</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>257</td>
      <td>262</td>
      <td>285</td>
      <td>290</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>263</td>
      <td>269</td>
      <td>291</td>
      <td>297</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>270</td>
      <td>291</td>
      <td>298</td>
      <td>319</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>292</td>
      <td>308</td>
      <td>320</td>
      <td>336</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>309</td>
      <td>327</td>
      <td>337</td>
      <td>355</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>328</td>
      <td>345</td>
      <td>356</td>
      <td>373</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>346</td>
      <td>349</td>
      <td>374</td>
      <td>377</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>
=======
| Parameter | Value |
|---|---|
| Method | [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) ([LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/)), conventional glass sandwich plates |
| Temperature | 20 C |
>>>>>>> d0e2c437136bdf2885afc6a99e0a9d4117821696

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6gpx">6GPX</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GAPCHK</span><span class="topo-outside">FDVKQIGA</span><span class="topo-membrane">QLLPPLYSLVFIFGFVGNMLVVL</span><span class="topo-inside">ILINYKKLKCLTDIYL</span><span class="topo-membrane">LNLAISD</span></span>
<span class="topo-line"><span class="topo-membrane">LLFLITLPLWAHSA</span><span class="topo-outside">ANEWVFGN</span><span class="topo-membrane">AMCKLFTGLYHIGYFGGIFFII</span><span class="topo-inside">LLTIDRYLAIVHAVFA</span></span>
<span class="topo-line"><span class="topo-inside">LKARTVTFGVVT</span><span class="topo-membrane">SVITWLVAVFASVPNIIFT</span><span class="topo-outside">KCQKEDSVYVCGPY</span><span class="topo-membrane">FPRGWNNFHTIMRNI</span></span>
<span class="topo-line"><span class="topo-membrane">LGLVLPLL</span><span class="topo-inside">IMVICYSGILKTL</span><span class="topo-unknown">LRMKKYTCTVCGYIYNPEDGDPDNGVNPGTDFKDIPDDW</span></span>
<span class="topo-line"><span class="topo-unknown">VCPLCGVGKDQFEEVEEEKKRHR</span><span class="topo-inside">DVRVIFT</span><span class="topo-membrane">IMIVYFLFWTPYNIVILLNTFQEFFGL</span><span class="topo-outside">SNC</span></span>
<span class="topo-line"><span class="topo-outside">ESTS</span><span class="topo-membrane">QLDQATQVTETLGMTHCCINPII</span><span class="topo-inside">YAFV</span><span class="topo-unknown">GEKFRSLFHIALGEVLFQ</span></span>
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
      <td>29</td>
      <td>34</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>7</td>
      <td>14</td>
      <td>35</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>37</td>
      <td>43</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>53</td>
      <td>66</td>
      <td>81</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>74</td>
      <td>82</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>82</td>
      <td>103</td>
      <td>110</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>104</td>
      <td>111</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>132</td>
      <td>133</td>
      <td>160</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>151</td>
      <td>161</td>
      <td>179</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>152</td>
      <td>165</td>
      <td>180</td>
      <td>193</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>188</td>
      <td>194</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>189</td>
      <td>201</td>
      <td>217</td>
      <td>229</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>263</td>
      <td>229</td>
      <td>229</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>264</td>
      <td>270</td>
      <td>241</td>
      <td>247</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>271</td>
      <td>297</td>
      <td>248</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>304</td>
      <td>275</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>305</td>
      <td>327</td>
      <td>282</td>
      <td>304</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>328</td>
      <td>331</td>
      <td>305</td>
      <td>308</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>332</td>
      <td>349</td>
      <td>309</td>
      <td>326</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### E291(7.39) is a key residue for orthosteric antagonist binding

The side chain of E291(7.39) forms a charge-reinforced hydrogen bond (2.5 A) with the secondary amine of [MK-0812](/xray-mp-wiki/reagents/ligands/mk-0812/) in the orthosteric pocket. This interaction is absent with BMS-681, where the tertiary amine cannot form this bond. E291(7.39) is present in most chemokine receptors and mutation studies have shown it is important for small-molecule ligand binding to CXCR4, CCR5, CCR2, and US28. Previous mutations of E291(7.39) to alanine in CCR2 reduced binding affinities for INCB3344, SB-282241, TAK-779, and Teijin antagonists. This residue is a key determinant for high-affinity orthosteric antagonist binding in chemokine receptors.

### H121(3.33) confers CCR2 selectivity over CCR5

The non-conserved residue H121(3.33) is located in the orthosteric pocket and shows divergent sequences between [CC Chemokine Receptor 2A (CCR2A)](/xray-mp-wiki/proteins/gpcr/ccr2a/) and CCR5. Structural modeling of pyrimidine amide (PA) class antagonists revealed that these ligands interact with H121(3.33), providing a basis for CCR2 selectivity over CCR5. Mutation of H121(3.33) affected the CCR2-selective Teijin ligand but not the dual antagonist TAK-779, indicating that interaction with H121(3.33) can be exploited for designing selective CCR2 antagonists.

### Stabilization by combined mutations and rubredoxin fusion

Full-length CCR2A was stabilized by a combination of [Rubredoxin](/xray-mp-wiki/reagents/protein-tags/rubredoxin/) fusion in ICL3 and five point mutations (N14Q, C70Y, G175N, A241D, K311E), achieving a melting temperature (Tm) of 55.6 C by DSF. Rubredoxin fusion alone gave Tm 43.7 C, and mutations alone gave Tm 51.0 C, showing synergistic stabilization. MK-0812 binding further increased Tm to 68.1 C, a 12.5 C shift. Multiple antagonists were tested by DSF, with MK-0812 giving the highest thermal shift (68.1 C), followed by AZD-6942 (63.2 C), INCB3344 (62.2 C), INCB3284 (60.4 C), and cpd 8c (58.2 C).

### Inactive conformation confirmed

Both CCR2A structures adopt the inactive chemokine receptor signature: intracellular ends of TM3 and TM6 are close together, and the conserved R138(3.50) of the [DRY Motif](/xray-mp-wiki/concepts/dry-motif/) interacts with D137(3.49) and T77(2.39), disrupting the G-protein binding site. Y305(7.53) on TM7 is twisted outward and points toward TM2, identical to the inactive CCR2B structure. This conformation is consistent with antagonist-bound states.


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/mk-0812/">MK-0812</a> — Co-crystallized orthosteric antagonist; highest thermal stabilization (Tm 68.1 C)
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Primary lipid component of [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) crystallization matrix
- <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> — Co-component of LCP matrix (10:1 [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/):[Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/))
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent for membrane solubilization and purification
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesterol Hydrogen Succinate (CHS)</a> — Co-detergent used during solubilization and purification
- <a href="/xray-mp-wiki/reagents/additives/talon/">TALON Cobalt Affinity Resin</a> — Ni-IMAC resin used for affinity purification of His-tagged [CC Chemokine Receptor 2A (CCR2A)](/xray-mp-wiki/proteins/gpcr/ccr2a/)
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200 Increase SEC Resin</a> — [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) resin for final purification step
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — Primary crystallization method used for both [CC Chemokine Receptor 2A (CCR2A)](/xray-mp-wiki/proteins/gpcr/ccr2a/) structures
- <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Baculovirus Expression System</a> — Referenced in [CC Chemokine Receptor 2A (CCR2A)](/xray-mp-wiki/proteins/gpcr/ccr2a/)
- <a href="/xray-mp-wiki/reagents/additives/12-propanediol/">1,2-Propanediol</a> — Referenced in [CC Chemokine Receptor 2A (CCR2A)](/xray-mp-wiki/proteins/gpcr/ccr2a/)
- <a href="/xray-mp-wiki/reagents/buffers/ammonium-acetate/">Ammonium Acetate</a> — Referenced in [CC Chemokine Receptor 2A (CCR2A)](/xray-mp-wiki/proteins/gpcr/ccr2a/)
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Referenced in [CC Chemokine Receptor 2A (CCR2A)](/xray-mp-wiki/proteins/gpcr/ccr2a/)
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Referenced in [CC Chemokine Receptor 2A (CCR2A)](/xray-mp-wiki/proteins/gpcr/ccr2a/)
- <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a> — Referenced in [CC Chemokine Receptor 2A (CCR2A)](/xray-mp-wiki/proteins/gpcr/ccr2a/)
- <a href="/xray-mp-wiki/reagents/additives/potassium-nitrate/">Potassium Nitrate (KNO3)</a> — Referenced in [CC Chemokine Receptor 2A (CCR2A)](/xray-mp-wiki/proteins/gpcr/ccr2a/)
- <a href="/xray-mp-wiki/reagents/buffers/bis-tris-propane/">Bis-Tris Propane Buffer</a> — Referenced in [CC Chemokine Receptor 2A (CCR2A)](/xray-mp-wiki/proteins/gpcr/ccr2a/)
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Hydroxymethyl) Aminomethane</a> — Referenced in [CC Chemokine Receptor 2A (CCR2A)](/xray-mp-wiki/proteins/gpcr/ccr2a/)
- <a href="/xray-mp-wiki/reagents/protein-tags/rubredoxin/">Rubredoxin</a> — Referenced in [CC Chemokine Receptor 2A (CCR2A)](/xray-mp-wiki/proteins/gpcr/ccr2a/)
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size Exclusion Chromatography</a> — Referenced in [CC Chemokine Receptor 2A (CCR2A)](/xray-mp-wiki/proteins/gpcr/ccr2a/)
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Referenced in [CC Chemokine Receptor 2A (CCR2A)](/xray-mp-wiki/proteins/gpcr/ccr2a/)
- <a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a> — Referenced in [CC Chemokine Receptor 2A (CCR2A)](/xray-mp-wiki/proteins/gpcr/ccr2a/)
- <a href="/xray-mp-wiki/concepts/dry-motif/">DRY Motif</a> — Referenced in [CC Chemokine Receptor 2A (CCR2A)](/xray-mp-wiki/proteins/gpcr/ccr2a/)
- <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a> — Referenced in [CC Chemokine Receptor 2A (CCR2A)](/xray-mp-wiki/proteins/gpcr/ccr2a/)
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES (HEPES Buffer)</a> — Referenced in [CC Chemokine Receptor 2A (CCR2A)](/xray-mp-wiki/proteins/gpcr/ccr2a/)
- <a href="/xray-mp-wiki/proteins/gpcr/ccr2a/">CC Chemokine Receptor 2A (CCR2A)</a> — Referenced in [CC Chemokine Receptor 2A (CCR2A)](/xray-mp-wiki/proteins/gpcr/ccr2a/)
