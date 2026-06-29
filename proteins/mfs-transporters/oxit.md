---
title: "Oxalate Transporter OxIT from Oxalobacter formigenes"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-023-36883-5]
verified: false
---

# Oxalate Transporter OxIT from Oxalobacter formigenes

## Overview

Oxalate transporter OxIT is an oxalate:formate antiporter (OFA) from the gut bacterium Oxalobacter formigenes. It belongs to the Major Facilitator Superfamily (MFS) and catalyzes the strict antiport of oxalate for formate across the cell membrane with high substrate specificity optimized for the C2 dicarboxylate oxalate. OxIT selectively discriminates oxalate from larger C4 dicarboxylates such as [Succinate (Succinic Acid)](/xray-mp-wiki/reagents/ligands/succinate) and oxaloacetate, preventing unwanted uptake of metabolic intermediates. The transporter has a high turnover rate (over 1000/s) and serves as a virtual proton pump that creates a proton motive force for bacterial [ATP](/xray-mp-wiki/reagents/ligands/atp) synthesis. OxIT is essential for the oxalate-degrading capability of O. formigenes, which reduces kidney stone risk in host animals.


## Publications

### doi/10.1038##s41467-023-36883-5

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8hpk">8HPK</a></td>
      <td>3.0</td>
      <td>not specified</td>
      <td>OxIT from O. formigenes in complex with D5901Fab antibody fragment</td>
      <td>oxalate</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8hpj">8HPJ</a></td>
      <td>3.3</td>
      <td>not specified</td>
      <td>OxIT from O. formigenes in complex with 20D033Fv antibody fragment</td>
      <td>ligand-free</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: OxIT with N-terminal Strep-II tag and C-terminal His8 tag
- **Notes**: Expressed from pRSF-OxIT vector; induced by [IPTG](/xray-mp-wiki/reagents/additives/iptg) with all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal)

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
      <td>Cell lysis and membrane fractionation</td>
      <td>not specified</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 200 mM <a href="/xray-mp-wiki/reagents/additives/potassium-acetate">Potassium Acetate</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/edta">EDTA</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/pmsf">PMSF</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/mgcl2">MGCL2</a>, 20 ug/mL DNase I, 0.23 mg/mL lysozyme + not specified</td>
      <td>Cells disrupted with Emulsiflex C-5; debris removed by centrifugation at 9,600xg for 30min; membranes collected at 185,000xg for 1h</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>not specified</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a>-KOH pH 8.0, 200 mM <a href="/xray-mp-wiki/reagents/additives/potassium-acetate">Potassium Acetate</a>, 10 mM potassium oxalate, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a> + 40 mM <a href="/xray-mp-wiki/reagents/detergents/ddm">n-Dodecyl-beta-D-maltopyranoside (DDM)</a></td>
      <td>Membrane fraction solubilized in buffer A with <a href="/xray-mp-wiki/reagents/detergents/ddm">n-Dodecyl-beta-D-maltopyranoside (DDM)</a></td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography">Ni-NTA Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA Agarose Resin</a> Superflow (QIAGEN) or HisTrap FF crude (GE Healthcare)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a>-KOH pH 8.0, 200 mM <a href="/xray-mp-wiki/reagents/additives/potassium-acetate">Potassium Acetate</a>, 10 mM potassium oxalate, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 1 mM <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>, 30-50 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> (wash); 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> (elution) + <a href="/xray-mp-wiki/reagents/detergents/ddm">n-Dodecyl-beta-D-maltopyranoside (DDM)</a></td>
      <td>Column washed with 1 mM <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> and 30-50 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a>; eluted with 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>OxIT-D5901Fab complex at 10 mg/mL in 20 mM <a href="/xray-mp-wiki/reagents/buffers/mes">MES</a>-KOH pH 6.2, 200 mM <a href="/xray-mp-wiki/reagents/additives/potassium-acetate">Potassium Acetate</a>, 10 mM potassium oxalate, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 0.51 mM <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M sodium <a href="/xray-mp-wiki/reagents/buffers/citrate">Citrate Buffer (Sodium Citrate)</a> pH 5.5, 0.05 M NaCl, 26% <a href="/xray-mp-wiki/reagents/additives/peg400">PEG400</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Grown overnight at 4 C; crystals flash-frozen in liquid nitrogen</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">Lipidic Cubic Phase Crystallization</a> (in meso)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>OxIT-20D033Fv complex in lipidic mesophase (50% protein, 45% <a href="/xray-mp-wiki/reagents/lipids/monoolein">Monoolein</a>, 5% <a href="/xray-mp-wiki/reagents/additives/cholesterol">Cholesterol</a>)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals obtained in 1 week using NT8-<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">Lipidic Cubic Phase Crystallization</a> crystallization robot; harvested from lipidic mesophase using Mesh Litholoops</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8hpk">8HPK</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MNNPQTGQST</span><span class="topo-outside">GLLGNRWFYL</span><span class="topo-membrane">VLAVLLMCMISGVQYSWTLYA</span><span class="topo-inside">NPVKDNLGVSLAAV</span><span class="topo-membrane">QTAFT</span></span>
<span class="topo-line"><span class="topo-membrane">LSQVIQAGSQPGGGYFV</span><span class="topo-outside">DKFGP</span><span class="topo-membrane">RIPLMFGGAMVLAGWTFMGMV</span><span class="topo-inside">DSVP</span><span class="topo-membrane">ALYALYTLAGAGV</span></span>
<span class="topo-line"><span class="topo-membrane">GIVYGIAMNTA</span><span class="topo-outside">NRWFPDKRG</span><span class="topo-membrane">LASGFTAAGYGLGVLPFLPLISSVL</span><span class="topo-inside">KVEGV</span><span class="topo-membrane">GAAFMYTGLI</span></span>
<span class="topo-line"><span class="topo-membrane">MGILIILIAFVI</span><span class="topo-outside">RFPGQ</span><span class="topo-unknown">QGAKK</span><span class="topo-outside">QIVVTDKDFNSGEMLRTP</span><span class="topo-membrane">QFWVLWTAFFSVNFGGLLLV</span></span>
<span class="topo-line"><span class="topo-membrane">ANSV</span><span class="topo-inside">PYGRSLGLAAGVLT</span><span class="topo-membrane">IGVSIQNLFNGGCRPFWGFVS</span><span class="topo-outside">DKIGR</span><span class="topo-membrane">YKTMSVVFGINAVVLA</span></span>
<span class="topo-line"><span class="topo-membrane">LFPTIA</span><span class="topo-inside">ALGDV</span><span class="topo-membrane">AFIAMLAIAFFTWGGSYALFPSTN</span><span class="topo-outside">SDIFGTAYSA</span><span class="topo-membrane">RNYGFFWAAKATASI</span></span>
<span class="topo-line"><span class="topo-membrane">FGGGLGA</span><span class="topo-inside">AIATNFGWN</span><span class="topo-membrane">TAFLITAITSFIAFALATFVIP</span><span class="topo-outside">RMGRPVK</span><span class="topo-unknown">KMVKLSPEEKAVHHH</span></span>
<span class="topo-line"><span class="topo-unknown">HHHHHHH</span></span>
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
      <td>1</td>
      <td>10</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>20</td>
      <td>11</td>
      <td>20</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>21</td>
      <td>41</td>
      <td>21</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>55</td>
      <td>42</td>
      <td>55</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>77</td>
      <td>56</td>
      <td>77</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>82</td>
      <td>78</td>
      <td>82</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>103</td>
      <td>83</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>104</td>
      <td>107</td>
      <td>104</td>
      <td>107</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>131</td>
      <td>108</td>
      <td>131</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>140</td>
      <td>132</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>165</td>
      <td>141</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>166</td>
      <td>170</td>
      <td>166</td>
      <td>170</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>171</td>
      <td>192</td>
      <td>171</td>
      <td>192</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>193</td>
      <td>197</td>
      <td>193</td>
      <td>197</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>198</td>
      <td>202</td>
      <td>198</td>
      <td>202</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>203</td>
      <td>220</td>
      <td>203</td>
      <td>220</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>244</td>
      <td>221</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>258</td>
      <td>245</td>
      <td>258</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>279</td>
      <td>259</td>
      <td>279</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>284</td>
      <td>280</td>
      <td>284</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>285</td>
      <td>306</td>
      <td>285</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>311</td>
      <td>307</td>
      <td>311</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>312</td>
      <td>335</td>
      <td>312</td>
      <td>335</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>336</td>
      <td>345</td>
      <td>336</td>
      <td>345</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>346</td>
      <td>367</td>
      <td>346</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>376</td>
      <td>368</td>
      <td>376</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>398</td>
      <td>377</td>
      <td>398</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>399</td>
      <td>405</td>
      <td>399</td>
      <td>405</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>406</td>
      <td>427</td>
      <td>406</td>
      <td>427</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8hpj">8HPJ</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MNNPQTGQST</span><span class="topo-inside">GLLGNRWF</span><span class="topo-membrane">YLVLAVLLMCMISGVQYSW</span><span class="topo-outside">TLYANPVKDNLGVSLAAVQTA</span><span class="topo-membrane">FT</span></span>
<span class="topo-line"><span class="topo-membrane">LSQVIQAGSQPGGGYFV</span><span class="topo-inside">DKFGP</span><span class="topo-membrane">RIPLMFGGAMVLAGWTFM</span><span class="topo-outside">GMVDSVPALY</span><span class="topo-membrane">ALYTLAGAGV</span></span>
<span class="topo-line"><span class="topo-membrane">GIVYGIAMNTAN</span><span class="topo-inside">RWFPDKRG</span><span class="topo-membrane">LASGFTAAGYGLGVLPFLPLI</span><span class="topo-outside">SSVLKVEGVGAAF</span><span class="topo-membrane">MYTGLI</span></span>
<span class="topo-line"><span class="topo-membrane">MGILIILIAFVI</span><span class="topo-inside">RFPG</span><span class="topo-unknown">QQGAKKQ</span><span class="topo-inside">IVVTDKDFNSGEM</span><span class="topo-membrane">LRTPQFWVLWTAFFSVNFGGLLLV</span></span>
<span class="topo-line"><span class="topo-membrane">A</span><span class="topo-outside">NSVPYGRSLGLAAGVLTI</span><span class="topo-membrane">GVSIQNLFNGGCRPFWGFVS</span><span class="topo-inside">DKIGR</span><span class="topo-membrane">YKTMSVVFGINAVVLA</span></span>
<span class="topo-line"><span class="topo-membrane">LFPTIA</span><span class="topo-outside">ALGDV</span><span class="topo-membrane">AFIAMLAIAFFTWGGSYALFPSTN</span><span class="topo-inside">SDIFGTAYS</span><span class="topo-membrane">ARNYGFFWAAKATASI</span></span>
<span class="topo-line"><span class="topo-membrane">FG</span><span class="topo-outside">GGLGAAIATNFGWNTA</span><span class="topo-membrane">FLITAITSFIAFALATFVIP</span><span class="topo-inside">RMGRPVKKMVKL</span><span class="topo-unknown">SPEEKAVHHH</span></span>
<span class="topo-line"><span class="topo-unknown">HHHHHHH</span></span>
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
      <td>1</td>
      <td>10</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>18</td>
      <td>11</td>
      <td>18</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>37</td>
      <td>19</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>58</td>
      <td>38</td>
      <td>58</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>77</td>
      <td>59</td>
      <td>77</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>82</td>
      <td>78</td>
      <td>82</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>100</td>
      <td>83</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>110</td>
      <td>101</td>
      <td>110</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>111</td>
      <td>132</td>
      <td>111</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>133</td>
      <td>140</td>
      <td>133</td>
      <td>140</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>161</td>
      <td>141</td>
      <td>161</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>162</td>
      <td>174</td>
      <td>162</td>
      <td>174</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>175</td>
      <td>192</td>
      <td>175</td>
      <td>192</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>193</td>
      <td>196</td>
      <td>193</td>
      <td>196</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>197</td>
      <td>203</td>
      <td>197</td>
      <td>203</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>204</td>
      <td>216</td>
      <td>204</td>
      <td>216</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>217</td>
      <td>241</td>
      <td>217</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>242</td>
      <td>259</td>
      <td>242</td>
      <td>259</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>260</td>
      <td>279</td>
      <td>260</td>
      <td>279</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>284</td>
      <td>280</td>
      <td>284</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>285</td>
      <td>306</td>
      <td>285</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>311</td>
      <td>307</td>
      <td>311</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>312</td>
      <td>335</td>
      <td>312</td>
      <td>335</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>336</td>
      <td>344</td>
      <td>336</td>
      <td>344</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>362</td>
      <td>345</td>
      <td>362</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>363</td>
      <td>378</td>
      <td>363</td>
      <td>378</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>379</td>
      <td>398</td>
      <td>379</td>
      <td>398</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>399</td>
      <td>410</td>
      <td>399</td>
      <td>410</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>411</td>
      <td>427</td>
      <td>411</td>
      <td>427</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Substrate-specific discrimination mechanism

The ligand-binding pocket contains basic residues (Q34, Y35, R272, Y328, K355) that form salt bridges with oxalate while preventing conformational switch to the occluded state without an acidic substrate. The pocket accommodates oxalate but excludes larger C4 dicarboxylates. In the ligand-free outward-facing state, charge repulsion between Arg272 and Lys355 at the empty binding site stabilizes the open conformation, preventing transition to the occluded form. This ensures OxIT functions as an antiporter where conformational switching without substrate is disallowed.

### Gln34 latch mechanism

Gln34, along with the hydrogen bond between Thr38 and Val240, functions as a periplasmic gate latch that prevents transition from the occluded to outward-facing conformation. MD simulations revealed a single side-chain flip of Gln34 triggers opening to the outside, breaking the Thr38-Val240 hydrogen bond. The Q34A mutant showed partial loss of binding and transport activity. This latch mechanism ensures the transport cycle proceeds in the correct direction.

### Rocker-switch motion with domain bending

The transition between occluded and outward-facing states involves a rocker-switch motion of N- and C-terminal domains, but unlike other MFS proteins, it is accompanied by conspicuous bending at TM1, 2, 4, 7, 8, and 11. The C-alpha RMSD between conformations is 2.6-2.7 A overall, with 1.5-1.6 A for individual domains. Bending at [Glycine](/xray-mp-wiki/reagents/buffers/glycine) residues and tilting of surrounding helices enables the conformational change.


## Cross-References

- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">Lipidic Cubic Phase Crystallization</a> — Crystallization method used for structure determination
- <a href="/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography">Immobilized Metal Affinity Chromatography (IMAC)</a> — Purification method used in protein preparation
- <a href="/xray-mp-wiki/reagents/ligands/succinate">Succinate</a> — Related entity
- <a href="/xray-mp-wiki/reagents/buffers/citrate">Citrate</a> — Buffer component in purification and crystallization
- <a href="/xray-mp-wiki/reagents/additives/potassium-acetate">Potassium Acetate</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/glycine">Glycine</a> — Buffer component in purification and crystallization
- <a href="/xray-mp-wiki/reagents/detergents/ddm">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Detergent used for membrane protein solubilization
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA Agarose Resin</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/cholesterol">Cholesterol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/ligands/retinal">Retinal</a> — Related entity
