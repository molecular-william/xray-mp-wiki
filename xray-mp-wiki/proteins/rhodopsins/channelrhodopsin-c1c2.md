---
title: "Channelrhodopsin C1C2"
created: 2026-05-26
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature10870, doi/10.7554##eLife.62389]
verified: agent
uniprot_id: Q8RUT8
---

# Channelrhodopsin C1C2

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q8RUT8">UniProt: Q8RUT8</a>

<span class="expr-badge">Chlamydomonas reinhardtii</span>

## Overview

Channelrhodopsin C1C2 is a chimeric construct between Chlamydomonas reinhardtii ChR1 and ChR2, designed as a light-gated cation channel for optogenetic applications. The original crystal structure was solved at 2.3 A resolution (PDB 3UG9) by Kato et al. (2012), revealing the essential molecular architecture of channelrhodopsins including the retinal-binding pocket, dimer interface, and cation conduction pathway. Time-resolved serial femtosecond crystallography (TR-SFX) using an X-ray free electron laser later revealed early conformational changes following photoactivation, including [Retinal](/xray-mp-wiki/reagents/ligands/retinal) isomerization-induced outward shift of TM3 and downward shift of TM7 - triggers for ion pore opening.

## Publications

### doi/10.1038##nature10870

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3ug9">3UG9</a></td>
      <td>2.3 A</td>
      <td>not specified</td>
      <td>C1C2 chimera (truncated, residues 1-342)</td>
      <td>all-trans <a href="/xray-mp-wiki/reagents/ligands/retinal">Retinal</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda Sf+ insect cells (baculovirus expression system)
- **Construct**: C1C2 chimera (residues 1-342) with C-terminal TEV-EGFP-His8 tag
- **Notes**: Cultured in Sf900II at 27°C for 24h, then 20°C. Cells harvested 72h post-infection.

**Purification:**

- **Expression system**: Sf+ insect cells (baculovirus)
- **Expression construct**: C1C2 chimera residues 1-342 with C-terminal TEV-EGFP-His8 tag
- **Tag info**: C-terminal EGFP-His8 (cleaved by TEV protease)

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
      <td>Cell disruption and membrane preparation</td>
      <td>Microfluidizer (2 passes at 15,000 psi)</td>
      <td>—</td>
      <td>300 mM NaCl, 50 mM Tris-HCl pH 8.0, 5% glycerol, 0.1 mM PMSF</td>
      <td>Cell debris cleared at 10,000g for 40 min; crude membrane collected by ultracentrifugation at 43,000 rpm (Ti45) for 1h</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>300 mM NaCl, 50 mM Tris-HCl pH 8.0, 5% glycerol, 20 mM imidazole, 0.1 mM PMSF + 2.5% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.5% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) (<a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>)</td>
      <td>Insoluble material removed by ultracentrifugation at 45,000 rpm (Ti70) for 30 min</td>
    </tr>
    <tr>
      <td>Ni-NTA affinity chromatography</td>
      <td>Nickel affinity</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) (QIAGEN)</td>
      <td>300 mM NaCl, 50 mM Tris-HCl pH 8.0, 5% glycerol, 0.1 mM PMSF + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>1h binding; elution with 300 mM imidazole</td>
    </tr>
    <tr>
      <td>TEV cleavage and reverse Ni-NTA</td>
      <td>Tag removal</td>
      <td>—</td>
      <td></td>
      <td>EGFP-His8 cleaved by His-tagged <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV</a> protease; flow-through containing C1C2 collected after reloading on <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/)</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)</td>
      <td>—</td>
      <td>150 mM NaCl, 50 mM Tris-HCl pH 8.0, 5% glycerol + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Final purification step</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified C1C2 in SEC buffer with DDM/CHS

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified C1C2 in <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a> buffer with <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>/<a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a></td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>2:3 (w/w)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20°C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2-3 weeks in the dark</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>None (flash-cooled in liquid nitrogen without additional cryoprotectant)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Protein-<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> mixture dispensed by mosquito <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> robot (TTP LabTech). 100 nl protein-<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> aliquots overlaid with 1 ul precipitant on 96-well sandwich plates. Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/mad-phasing/">MAD</a> phasing using mercury-derivatized crystals. Data collected at SLS beamline X06SA and SPring-8 BL32XU. First example of <a href="/xray-mp-wiki/methods/structure-determination/mad-phasing/">MAD</a> phasing for <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>-grown crystals.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ug9">3UG9</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">STGSDATVPVATQDGPDYVFHRAHE</span><span class="topo-inside">RMLFQTSYTLENNGSVICIPNNGQCFCLAWLKSNGTNAEKLA</span><span class="topo-membrane">ANILQWITFALSALCLMFY</span><span class="topo-unknown">GYQTWKST</span><span class="topo-outside">CGW</span><span class="topo-membrane">EEIYVATIEMIKFIIEYF</span><span class="topo-inside">HEFDE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">PAVIYSSNGNKT</span><span class="topo-membrane">VWLRYAEWLLTCPVILI</span><span class="topo-outside">HLSNLTGLANDYNKRTM</span><span class="topo-membrane">GLLVSDIGTIVWGTTAAL</span><span class="topo-inside">SKGY</span><span class="topo-membrane">VRVIFFLMGLCYGIYTFFNA</span><span class="topo-outside">AKVYIEAYHTVPKGRCRQVVTG</span><span class="topo-membrane">MAWLFFVSWG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330   </span>
<span class="topo-line"><span class="topo-membrane">MFPILFILG</span><span class="topo-inside">PEGFGVLSVYG</span><span class="topo-membrane">STVGHTIIDLMSKNCWGLL</span><span class="topo-outside">GHYLRVLIHEHILIHGDIRKTTKL</span><span class="topo-unknown">NIGGTE</span><span class="topo-outside">IEVETLVEDE</span><span class="topo-unknown">AEAGAVSSEDLYFQ</span></span>
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
      <td>25</td>
      <td>24</td>
      <td>48</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>26</td>
      <td>67</td>
      <td>49</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>86</td>
      <td>91</td>
      <td>109</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>94</td>
      <td>110</td>
      <td>117</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>95</td>
      <td>97</td>
      <td>118</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>115</td>
      <td>121</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>132</td>
      <td>139</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>149</td>
      <td>156</td>
      <td>172</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>166</td>
      <td>173</td>
      <td>189</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>190</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>185</td>
      <td>188</td>
      <td>208</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>208</td>
      <td>212</td>
      <td>231</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>209</td>
      <td>230</td>
      <td>232</td>
      <td>253</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>249</td>
      <td>254</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>250</td>
      <td>260</td>
      <td>273</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>279</td>
      <td>284</td>
      <td>302</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>303</td>
      <td>303</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>304</td>
      <td>309</td>
      <td>327</td>
      <td>332</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>310</td>
      <td>319</td>
      <td>333</td>
      <td>342</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>320</td>
      <td>333</td>
      <td>343</td>
      <td>356</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ug9">3UG9</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">STGSDATVPVATQDGPDYVFHRAHE</span><span class="topo-inside">RMLFQTSYTLENNGSVICIPNNGQCFCLAWLKSNGTNAEKLA</span><span class="topo-membrane">ANILQWITFALSALCLMFY</span><span class="topo-unknown">GYQTWKST</span><span class="topo-outside">CGW</span><span class="topo-membrane">EEIYVATIEMIKFIIEYF</span><span class="topo-inside">HEFDE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">PAVIYSSNGNKT</span><span class="topo-membrane">VWLRYAEWLLTCPVILI</span><span class="topo-outside">HLSNLTGLANDYNKRTM</span><span class="topo-membrane">GLLVSDIGTIVWGTTAAL</span><span class="topo-inside">SKGY</span><span class="topo-membrane">VRVIFFLMGLCYGIYTFFNA</span><span class="topo-outside">AKVYIEAYHTVPKGRCRQVVTG</span><span class="topo-membrane">MAWLFFVSWG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330   </span>
<span class="topo-line"><span class="topo-membrane">MFPILFILG</span><span class="topo-inside">PEGFGVLSVYG</span><span class="topo-membrane">STVGHTIIDLMSKNCWGLL</span><span class="topo-outside">GHYLRVLIHEHILIHGDIRKTTKL</span><span class="topo-unknown">NIGGTE</span><span class="topo-outside">IEVETLVEDE</span><span class="topo-unknown">AEAGAVSSEDLYFQ</span></span>
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
      <td>25</td>
      <td>24</td>
      <td>48</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>26</td>
      <td>67</td>
      <td>49</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>86</td>
      <td>91</td>
      <td>109</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>94</td>
      <td>110</td>
      <td>117</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>95</td>
      <td>97</td>
      <td>118</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>115</td>
      <td>121</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>132</td>
      <td>139</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>149</td>
      <td>156</td>
      <td>172</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>166</td>
      <td>173</td>
      <td>189</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>190</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>185</td>
      <td>188</td>
      <td>208</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>208</td>
      <td>212</td>
      <td>231</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>209</td>
      <td>230</td>
      <td>232</td>
      <td>253</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>249</td>
      <td>254</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>250</td>
      <td>260</td>
      <td>273</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>279</td>
      <td>284</td>
      <td>302</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>303</td>
      <td>303</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>304</td>
      <td>309</td>
      <td>327</td>
      <td>332</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>310</td>
      <td>319</td>
      <td>333</td>
      <td>342</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>320</td>
      <td>333</td>
      <td>343</td>
      <td>356</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.7554##eLife.62389

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7c86">7C86</a></td>
      <td>2.3 A</td>
      <td>not specified</td>
      <td>C1C2 chimera (dark state, synchrotron structure)</td>
      <td>all-trans <a href="/xray-mp-wiki/reagents/ligands/retinal">Retinal</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7e6z">7E6Z</a></td>
      <td>2.5 A</td>
      <td>not specified</td>
      <td>C1C2 chimera (50 µs light-activated state)</td>
      <td>isomerized <a href="/xray-mp-wiki/reagents/ligands/retinal">Retinal</a> (twisted conformation)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7e70">7E70</a></td>
      <td>2.5 A</td>
      <td>not specified</td>
      <td>C1C2 chimera (250 µs light-activated state)</td>
      <td>isomerized <a href="/xray-mp-wiki/reagents/ligands/retinal">Retinal</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7e71">7E71</a></td>
      <td>2.5 A</td>
      <td>not specified</td>
      <td>C1C2 chimera (1 ms light-activated state)</td>
      <td>isomerized <a href="/xray-mp-wiki/reagents/ligands/retinal">Retinal</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7e6x">7E6X</a></td>
      <td>2.5 A</td>
      <td>not specified</td>
      <td>C1C2 chimera (4 ms light-activated state)</td>
      <td>isomerized <a href="/xray-mp-wiki/reagents/ligands/retinal">Retinal</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda Sf+ insect cells (baculovirus expression system)
- **Construct**: C1C2 chimera (residues 1-342) with C-terminal TEV-EGFP-His8 tag
- **Notes**: Cultured in Sf900II at 27°C for 24h, then 20°C. Cells harvested 72h post-infection.

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
      <td>Protein expression</td>
      <td>Recombinant expression in Escherichia coli</td>
      <td>--</td>
      <td>Not specified in paper + --</td>
      <td>C1C2 vector construction and protein production performed as previously reported (Kato et al., 2012)</td>
    </tr>
    <tr>
      <td>Lysis and solubilization</td>
      <td>Cell lysis and detergent solubilization</td>
      <td>--</td>
      <td>150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">sodium chloride</a>, 50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> (pH 8.0), 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-dodecyl-beta-D-maltoside (DDM)</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">cholesteryl hydrogen succinate ([CHS</a>)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Protein solubilized in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>/<a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) mixture for membrane protein stability</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) column</td>
      <td>150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">sodium chloride</a>, 50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> (pH 8.0), 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Final purification step; protein concentrated to ~15 mg/ml for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>C1C2 chimera concentrated to ~15 mg/ml in 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">sodium chloride</a>, 50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> (pH 8.0), 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20°C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2-3 weeks in the dark</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified; XFEL data collected at room temperature from LCP microjet</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Protein mixed with <a href="/xray-mp-wiki/reagents/lipids/monoolein/">monoolein</a> at 2:3 protein-to-lipid ratio (w/w). High-density microcrystals (2-5 µm) formed, optimized for TR-SFX at SACLA XFEL. Dark state structure solved at 2.3 A resolution. Time-resolved structures at 50 µs, 250 µs, 1 ms, and 4 ms were collected using 470 nm pump laser pulses.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7c86">7C86</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSRRPWLLALALAVALAAGSAGASTGSDATVPVATQDGPDYVFHRAHE</span><span class="topo-inside">RMLFQTSYTLENNGSVICIPNNGQCFCLAWLKSNGTNAEKLA</span><span class="topo-membrane">ANILQWITFALSALCLMF</span><span class="topo-outside">YGY</span><span class="topo-unknown">QTWKST</span><span class="topo-outside">CGW</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">E</span><span class="topo-membrane">EIYVATIEMIKFIIEYF</span><span class="topo-inside">HEFDEPAVIYSSNGNKTV</span><span class="topo-membrane">WLRYAEWLLTCPVIL</span><span class="topo-outside">IHLSNLTGLANDYNKRTMG</span><span class="topo-membrane">LLVSDIGTIVWGTTAA</span><span class="topo-inside">LSKGYVRV</span><span class="topo-membrane">IFFLMGLCYGIYTFFNA</span><span class="topo-outside">AKVYIEAYH</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350      </span>
<span class="topo-line"><span class="topo-outside">TVPKGRCRQVVTGM</span><span class="topo-membrane">AWLFFVSWGMFPILFIL</span><span class="topo-inside">GPEGFGVLSVYGS</span><span class="topo-membrane">TVGHTIIDLMSKNCWGL</span><span class="topo-outside">LGHYLRVLIHEHILIHGDIRKTTKLNI</span><span class="topo-unknown">GG</span><span class="topo-outside">TEIEVETLVEDEAEAGAVSSED</span><span class="topo-unknown">LYFQ</span></span>
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
      <td>48</td>
      <td>1</td>
      <td>48</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>49</td>
      <td>90</td>
      <td>49</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>108</td>
      <td>91</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>111</td>
      <td>109</td>
      <td>111</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>117</td>
      <td>112</td>
      <td>117</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>118</td>
      <td>121</td>
      <td>118</td>
      <td>121</td>
      <td>Outside</td>
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
      <td>156</td>
      <td>139</td>
      <td>156</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>171</td>
      <td>157</td>
      <td>171</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>172</td>
      <td>190</td>
      <td>172</td>
      <td>190</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>206</td>
      <td>191</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>214</td>
      <td>207</td>
      <td>214</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>231</td>
      <td>215</td>
      <td>231</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>254</td>
      <td>232</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>271</td>
      <td>255</td>
      <td>271</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>284</td>
      <td>272</td>
      <td>284</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>285</td>
      <td>301</td>
      <td>285</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>302</td>
      <td>328</td>
      <td>302</td>
      <td>328</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>329</td>
      <td>330</td>
      <td>329</td>
      <td>330</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>331</td>
      <td>352</td>
      <td>331</td>
      <td>352</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>356</td>
      <td>353</td>
      <td>356</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7c86">7C86</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSRRPWLLALALAVALAAGSAGASTGSDATVPVATQDGPDYVFHRAHE</span><span class="topo-inside">RMLFQTSYTLENNGSVICIPNNGQCFCLAWLKSNGTNAEKLA</span><span class="topo-membrane">ANILQWITFALSALCLMFYG</span><span class="topo-unknown">YQTWKST</span><span class="topo-outside">CGW</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">EEIYVATIEMIKFIIEY</span><span class="topo-inside">FHEFDEPAVIYSSNGNKTV</span><span class="topo-membrane">WLRYAEWLLTCPVIL</span><span class="topo-outside">IHLSNLTGLANDYNKRTMG</span><span class="topo-membrane">LLVSDIGTIVWGTTAAL</span><span class="topo-inside">SKGY</span><span class="topo-membrane">VRVIFFLMGLCYGIYTFF</span><span class="topo-outside">NAAKVYIEAYH</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350      </span>
<span class="topo-line"><span class="topo-outside">TVPKGRCRQVVTGMAW</span><span class="topo-membrane">LFFVSWGMFPILFILG</span><span class="topo-inside">PEGFGVLSVYG</span><span class="topo-membrane">STVGHTIIDLMSKNCWGL</span><span class="topo-outside">LGHYLRVLIHEHILIHGDIRKTTKLNI</span><span class="topo-unknown">GG</span><span class="topo-outside">TEIEVETLVEDEAEAGAVSSED</span><span class="topo-unknown">LYFQ</span></span>
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
      <td>48</td>
      <td>1</td>
      <td>48</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>49</td>
      <td>90</td>
      <td>49</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>110</td>
      <td>91</td>
      <td>110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>117</td>
      <td>112</td>
      <td>117</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>118</td>
      <td>120</td>
      <td>118</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>137</td>
      <td>121</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>156</td>
      <td>138</td>
      <td>156</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>171</td>
      <td>157</td>
      <td>171</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>172</td>
      <td>190</td>
      <td>172</td>
      <td>190</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>207</td>
      <td>191</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>211</td>
      <td>208</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>229</td>
      <td>212</td>
      <td>229</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>256</td>
      <td>230</td>
      <td>256</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>257</td>
      <td>272</td>
      <td>257</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>283</td>
      <td>273</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>301</td>
      <td>284</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>302</td>
      <td>328</td>
      <td>302</td>
      <td>328</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>329</td>
      <td>330</td>
      <td>329</td>
      <td>330</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>331</td>
      <td>352</td>
      <td>331</td>
      <td>352</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>356</td>
      <td>353</td>
      <td>356</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7e6z">7E6Z</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSRRPWLLALALAVALAAGSAGASTGSDATVPVATQDGPDYVFHRAHE</span><span class="topo-inside">RMLFQTSYTLENNGSVICIPNNGQCFCLAWLKSNGTNAEKLA</span><span class="topo-membrane">ANILQWITFALSALCLMFYG</span><span class="topo-outside">Y</span><span class="topo-unknown">QTWKST</span><span class="topo-outside">CGW</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">EEIYVATIEMIKFIIEYF</span><span class="topo-inside">HEFDEPAVIYSSNGNKT</span><span class="topo-membrane">VWLRYAEWLLTCPVIL</span><span class="topo-outside">IHLSNLTGLANDYNKRTMG</span><span class="topo-membrane">LLVSDIGTIVWGTTAAL</span><span class="topo-inside">SKGY</span><span class="topo-membrane">VRVIFFLMGLCYGIYTFF</span><span class="topo-outside">NAAKVYIEAYH</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350      </span>
<span class="topo-line"><span class="topo-outside">TVPKGRCRQVVTGM</span><span class="topo-membrane">AWLFFVSWGMFPILFILG</span><span class="topo-inside">PEGFGVLSVYG</span><span class="topo-membrane">STVGHTIIDLMSKNCWGLL</span><span class="topo-outside">GHYLRVLIHEHILIHGDIRKTTKLNI</span><span class="topo-unknown">GG</span><span class="topo-outside">TEIEVETLVEDEAEAGAVSSED</span><span class="topo-unknown">LYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>49</td>
      <td>90</td>
      <td>49</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>110</td>
      <td>91</td>
      <td>110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>111</td>
      <td>111</td>
      <td>111</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>120</td>
      <td>118</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>138</td>
      <td>121</td>
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
      <td>171</td>
      <td>156</td>
      <td>171</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>172</td>
      <td>190</td>
      <td>172</td>
      <td>190</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>207</td>
      <td>191</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>211</td>
      <td>208</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>229</td>
      <td>212</td>
      <td>229</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>254</td>
      <td>230</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>272</td>
      <td>255</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>283</td>
      <td>273</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>302</td>
      <td>284</td>
      <td>302</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>303</td>
      <td>328</td>
      <td>303</td>
      <td>328</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>331</td>
      <td>352</td>
      <td>331</td>
      <td>352</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7e6z">7E6Z</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSRRPWLLALALAVALAAGSAGASTGSDATVPVATQDGPDYVFHRAHE</span><span class="topo-inside">RMLFQTSYTLENNGSVICIPNNGQCFCLAWLKSNGTNAEKLA</span><span class="topo-membrane">ANILQWITFALSALCLMFYG</span><span class="topo-outside">Y</span><span class="topo-unknown">QTWKST</span><span class="topo-outside">CGW</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">EEIYVATIEMIKFIIEYF</span><span class="topo-inside">HEFDEPAVIYSSNGNKT</span><span class="topo-membrane">VWLRYAEWLLTCPVIL</span><span class="topo-outside">IHLSNLTGLANDYNKRTMG</span><span class="topo-membrane">LLVSDIGTIVWGTTAAL</span><span class="topo-inside">SKGY</span><span class="topo-membrane">VRVIFFLMGLCYGIYTFF</span><span class="topo-outside">NAAKVYIEAYH</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350      </span>
<span class="topo-line"><span class="topo-outside">TVPKGRCRQVVTGM</span><span class="topo-membrane">AWLFFVSWGMFPILFILG</span><span class="topo-inside">PEGFGVLSVYG</span><span class="topo-membrane">STVGHTIIDLMSKNCWGLL</span><span class="topo-outside">GHYLRVLIHEHILIHGDIRKTTKLNI</span><span class="topo-unknown">GG</span><span class="topo-outside">TEIEVETLVEDEAEAGAVSSED</span><span class="topo-unknown">LYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>49</td>
      <td>90</td>
      <td>49</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>110</td>
      <td>91</td>
      <td>110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>111</td>
      <td>111</td>
      <td>111</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>120</td>
      <td>118</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>138</td>
      <td>121</td>
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
      <td>171</td>
      <td>156</td>
      <td>171</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>172</td>
      <td>190</td>
      <td>172</td>
      <td>190</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>207</td>
      <td>191</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>211</td>
      <td>208</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>229</td>
      <td>212</td>
      <td>229</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>254</td>
      <td>230</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>272</td>
      <td>255</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>283</td>
      <td>273</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>302</td>
      <td>284</td>
      <td>302</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>303</td>
      <td>328</td>
      <td>303</td>
      <td>328</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>331</td>
      <td>352</td>
      <td>331</td>
      <td>352</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7e6x">7E6X</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSRRPWLLALALAVALAAGSAGASTGSDATVPVATQDGPDYVFHRAHE</span><span class="topo-inside">RMLFQTSYTLENNGSVICIPNNGQCFCLAWLKSNGTNAEKLA</span><span class="topo-membrane">ANILQWITFALSALCLM</span><span class="topo-outside">FYGY</span><span class="topo-unknown">QTWKST</span><span class="topo-outside">CGW</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">EE</span><span class="topo-membrane">IYVATIEMIKFIIEY</span><span class="topo-inside">FHEFDEPAVIYSSNGNKT</span><span class="topo-membrane">VWLRYAEWLLTCPVI</span><span class="topo-outside">LIHLSNLTGLANDYNKRTMGLL</span><span class="topo-membrane">VSDIGTIVWGTTAAL</span><span class="topo-inside">SKGY</span><span class="topo-membrane">VRVIFFLMGLCYGIYTF</span><span class="topo-outside">FNAAKVYIEAYH</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350      </span>
<span class="topo-line"><span class="topo-outside">TVPKGRCRQVVTGMAW</span><span class="topo-membrane">LFFVSWGMFPILFILG</span><span class="topo-inside">PEGFGVLSVYG</span><span class="topo-membrane">STVGHTIIDLMSKNCWG</span><span class="topo-outside">LLGHYLRVLIHEHILIHGDIRKTTKLNI</span><span class="topo-unknown">GG</span><span class="topo-outside">TEIEVETLVEDEAEAGAVSSED</span><span class="topo-unknown">LYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>49</td>
      <td>90</td>
      <td>49</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>107</td>
      <td>91</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>111</td>
      <td>108</td>
      <td>111</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>122</td>
      <td>118</td>
      <td>122</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>123</td>
      <td>137</td>
      <td>123</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>155</td>
      <td>138</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>156</td>
      <td>170</td>
      <td>156</td>
      <td>170</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>171</td>
      <td>192</td>
      <td>171</td>
      <td>192</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>207</td>
      <td>193</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>211</td>
      <td>208</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>228</td>
      <td>212</td>
      <td>228</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>229</td>
      <td>256</td>
      <td>229</td>
      <td>256</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>257</td>
      <td>272</td>
      <td>257</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>283</td>
      <td>273</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>300</td>
      <td>284</td>
      <td>300</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>301</td>
      <td>328</td>
      <td>301</td>
      <td>328</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>331</td>
      <td>352</td>
      <td>331</td>
      <td>352</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7e6x">7E6X</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSRRPWLLALALAVALAAGSAGASTGSDATVPVATQDGPDYVFHRAHE</span><span class="topo-inside">RMLFQTSYTLENNGSVICIPNNGQCFCLAWLKSNGTNAEKLA</span><span class="topo-membrane">ANILQWITFALSALCLM</span><span class="topo-outside">FYGY</span><span class="topo-unknown">QTWKST</span><span class="topo-outside">CGW</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">EE</span><span class="topo-membrane">IYVATIEMIKFIIEY</span><span class="topo-inside">FHEFDEPAVIYSSNGNKT</span><span class="topo-membrane">VWLRYAEWLLTCPVI</span><span class="topo-outside">LIHLSNLTGLANDYNKRTMGLL</span><span class="topo-membrane">VSDIGTIVWGTTAAL</span><span class="topo-inside">SKGY</span><span class="topo-membrane">VRVIFFLMGLCYGIYTF</span><span class="topo-outside">FNAAKVYIEAYH</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350      </span>
<span class="topo-line"><span class="topo-outside">TVPKGRCRQVVTGMAW</span><span class="topo-membrane">LFFVSWGMFPILFILG</span><span class="topo-inside">PEGFGVLSVYG</span><span class="topo-membrane">STVGHTIIDLMSKNCWG</span><span class="topo-outside">LLGHYLRVLIHEHILIHGDIRKTTKLNI</span><span class="topo-unknown">GG</span><span class="topo-outside">TEIEVETLVEDEAEAGAVSSED</span><span class="topo-unknown">LYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>49</td>
      <td>90</td>
      <td>49</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>107</td>
      <td>91</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>111</td>
      <td>108</td>
      <td>111</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>122</td>
      <td>118</td>
      <td>122</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>123</td>
      <td>137</td>
      <td>123</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>155</td>
      <td>138</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>156</td>
      <td>170</td>
      <td>156</td>
      <td>170</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>171</td>
      <td>192</td>
      <td>171</td>
      <td>192</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>207</td>
      <td>193</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>211</td>
      <td>208</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>228</td>
      <td>212</td>
      <td>228</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>229</td>
      <td>256</td>
      <td>229</td>
      <td>256</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>257</td>
      <td>272</td>
      <td>257</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>283</td>
      <td>273</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>300</td>
      <td>284</td>
      <td>300</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>301</td>
      <td>328</td>
      <td>301</td>
      <td>328</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>331</td>
      <td>352</td>
      <td>331</td>
      <td>352</td>
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

### First crystal structure of a channelrhodopsin reveals essential molecular architecture

The 2.3 A structure of C1C2 (PDB 3UG9) revealed the seven-transmembrane helix architecture with an N-terminal extracellular domain (residues 24-83), the core TM1-TM7 helices, and a C-terminal intracellular domain. Two C1C2 protomers form a tightly associated dimer via N-domain, ECL1, TM3, and TM4 interactions, with three disulfide bonds (Cys66-Cys66, Cys73-Cys73, Cys75-Cys75) stabilizing the dimer interface. 6 lipids and 43 water molecules were observed per protomer.

### Structural comparison with bacteriorhodopsin reveals distinct features

C1C2 superimposes well on bacteriorhodopsin (PDB 1IW6) with conserved TM3-6 and protonated Schiff base position, but three distinct features differentiate it: (1) additional N-terminal and C-terminal domains (N-domain for dimerization, C-domain for subcellular localization), (2) TM7 protrudes ~18 A into the intracellular space, shifted 2.7 A toward the monomer central axis, and (3) the extracellular ends of TM1 and TM2 are tilted outward by 3.0 A and 4.1 A respectively, enlarging the cavity for cation translocation.

### Retinal-binding pocket and Schiff base counterion network

All-trans retinal is covalently bound to Lys296 (ChR2: 257) via a protonated Schiff base. The counterion complex includes Glu162 (ChR2: 123, corresponding to BR Asp85) and Asp292 (ChR2: 253, corresponding to BR Asp212). Distances from the Schiff base are 4.4 A (water), 3.4 A (Glu162), and 3.0 A (Asp292). Asp292 is proposed as the primary proton acceptor in C1C2, consistent with D292A mutants almost completely abolishing photocurrents. The Cys167-Asp195 DC-pair shows a distance of 4.4-4.6 A, with Cys167 associated with the retinal pi-electron system rather than Asp195.

### Electronegative cation-conduction pathway framed by TM1, TM2, TM3, and TM7

Electrostatic surface potential reveals an electronegative pore lined by 12 polar residues (Gln95, Thr98, Ser102, Glu122, Glu129, Lys132, Glu136, Glu140, Glu162, Thr285, Asp292, Asn297). Glu136 (ChR2: 97) is essential for cation conduction. Two constriction sites occlude the cytoplasmic side: (1) Ser102, Glu129, and Asn297 form the first gate, and (2) Tyr109 (ChR2: 70) forms the second gate. Mutations at these residues affect ion selectivity and kinetics.

### Extracellular vestibule and conserved residue cluster

An extracellular vestibule (~8 A diameter) is formed by the N domain and ECL1-3, with Lys154, Lys209, and Arg213 creating a slightly electropositive surface. Deeper within, Arg159, Tyr160, Glu274, and Ser284 (conserved in ChRs and BRs) form a water-mediated hydrogen-bond network fixing TM3, TM6, and TM7 positions. The R159A mutant does not produce photocurrent despite robust membrane expression, indicating this cluster is critical for creating the extracellular vestibule.

### Absorption spectrum blueshift explained by counterion proximity

The ChR absorption maximum (470 nm) is blueshifted compared to BR (568 nm). The C1C2 structure shows that Asp292 (the counterion) is ~1 A closer to the Schiff base than the corresponding BR residue, and negatively charged residues line the conducting pathway. These environments stabilize the ground state (S0), enlarging the S0-S1 energy gap and causing the blueshift.

### Retinal kink-induced outward shift of TM3 triggers channel opening

Time-resolved TR-SFX revealed that [Retinal](/xray-mp-wiki/reagents/ligands/retinal) isomerization induces a twisted, kinked conformation that shifts toward Cys167, causing an outward shift of TM3 originating at the Pro168 helix kink. This movement propagates to the intracellular segment where His173 forms ionic interactions with Arg307 in TM7 and Glu121/Glu122 in TM2, opening the inner gate. The outward shift of TM3 is not observed in the Cys167 mutant, indicating the critical role of the Cys residue in the TM3 shift.

### Downward shift of TM7 induced by retinal isomerization

The isomerization of retinal induces a downward shift of TM7 (Helix G) at the retinal-attached residue Lys296, which becomes most prominent at 4 ms. Positive densities along Lys296 and complementary difference densities around Trp299 indicate an overall downward shift of the middle portion of TM7. This shift is similar to the L-like intermediate of [Bacteriorhodopsin](/xray-mp-wiki/proteins/bacteriorhodopsin) and represents a conserved feature of rhodopsin proteins.

### Five glutamic acid residues and three constriction sites line the ion pore

The dark state structure reveals five glutamic acid residues (E1-E5) lining the putative ion pore, with two counterion residues (C11 and C12). Three constriction sites form the inner, central, and outer gates. The inner gate is formed by Glu121, Glu122, His173, and Arg307. Light-induced conformational changes at these gates precede ion conductance, with the inward gate destabilization likely triggering water influx and pore dilation.

### Photocycle intermediates P2 accumulates in crystals with hindered P3 transition

C1C2 crystals accumulate primarily the P2 intermediate (390 nm) with the transition from P2 to P3 hindered in the crystal lattice. The P2 intermediate shows prominent spectral increase at 390 nm, suggesting a deprotonated Schiff base state. This differs from solution behavior where P3 (530 nm) forms after P2. The P1 intermediate (520 nm) forms before 10 µs, and the P3 intermediate shows a delayed rise at 530 nm after 360 µs in solution.

### DC-pair residues (Cys167 and Asp195) are critical for channel gating

The aspartate-cysteine pair (DC-pair) Cys167 and Asp195 in the [Retinal](/xray-mp-wiki/reagents/ligands/retinal) binding pocket are critical for fast channel kinetics. Mutations of these residues result in step-function opsin (SFO) mutants with long-lasting photocurrents. FTIR and structural studies suggest Asp195 functions as the internal proton donor for the deprotonated Schiff base via an internal hydrated water molecule and Cys167. The hydrogen-bonding network involving the DC-pair affects the retinal conformation after isomerization.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltoside (DDM)</a> — Detergent (2.5% for solubilization, 0.05% for purification) used for membrane protein extraction and stabilization
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesteryl Hydrogen Succinate (CHS)</a> — Stabilizing additive (0.5% for solubilization, 0.01% for purification) used to maintain C1C2 stability
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl buffer)</a> — Buffer (50 mM, pH 8.0) used throughout purification and crystallization
- <a href="/xray-mp-wiki/reagents/buffers/mes/">2-(N-morpholino)ethanesulfonic acid (MES)</a> — Buffer used in eLife 2021 crystallization reservoir
- <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride (NaCl)</a> — Salt (150-300 mM) used in purification and crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Stabilizer (5%) used in purification and crystallization buffers
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Host lipid for LCP crystallization matrix
- <a href="/xray-mp-wiki/reagents/ligands/11-cis-retinal/">All-trans retinal</a> — Chromophore covalently bound to Lys296 via Schiff base linkage; essential for light sensitivity
- <a href="/xray-mp-wiki/reagents/additives/peg/">Polyethylene glycol (PEG)</a> — Precipitant (PEG500DME) used in LCP crystallization
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — LCP method used for both original and TR-SFX C1C2 crystal growth
- <a href="/xray-mp-wiki/methods/structure-determination/mad-phasing/">Multi-wavelength Anomalous Diffraction (MAD)</a> — MAD phasing using mercury derivative was used to solve the original C1C2 structure - first application to LCP crystals
- <a href="/xray-mp-wiki/concepts/rhodopsin-mechanisms/rhodopsin-photocycle/">Rhodopsin Photocycle</a> — C1C2 photocycle intermediates (P1, P2, P3) characterized by flash photolysis
- <a href="/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/">Bacteriorhodopsin</a> — Archetypal microbial rhodopsin used for structural comparison
- <a href="/xray-mp-wiki/proteins/rhodopsins/channelrhodopsin-2/">Channelrhodopsin 2 (ChR2)</a> — Parent protein of C1C2 chimera; C1C2 is a fusion of ChR1 and ChR2
