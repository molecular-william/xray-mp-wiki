---
title: "Channelrhodopsin 2 (ChR2) from Chlamydomonas reinhardtii"
created: 2026-06-10
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.aan8862]
verified: regex
uniprot_id: Q8RUT8
---

# Channelrhodopsin 2 (ChR2) from Chlamydomonas reinhardtii


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q8RUT8">UniProt: Q8RUT8</a>

<span class="expr-badge">Chlamydomonas reinhardtii</span>

## Overview

Channelrhodopsin 2 (ChR2) is a light-gated cation channel from the green alga
Chlamydomonas reinhardtii. It is the most widely used optogenetic tool for
remote control of neural activity with high spatiotemporal resolution. ChR2
belongs to the microbial rhodopsin family, a group of seven-transmembrane helix
proteins that bind a [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore via a protonated Schiff base. Photon
absorption triggers all-trans to 13-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) isomerization, initiating a
photocycle that opens the ion pore. The 2.4 Å crystal structure of wild-type
ChR2 and the 2.7 Å structure of the C128T slow mutant reveal the molecular
basis for ion conduction and gating regulation.


## Publications

### doi/10.1126##science.aan8862

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6eid">6EID</a></td>
      <td>2.4</td>
      <td>—</td>
      <td>Wild-type ChR2 (residues 1-315, C-terminal truncation)</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6eid">6EID</a></td>
      <td>2.7</td>
      <td>—</td>
      <td>C128T mutant ChR2 (residues 1-315, C-terminal truncation)</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: LEXSY (Leishmania tarentolae expression system)
- **Construct**: Full-length ChR2 with C-terminal polyhistidine tag
- **Notes**: Expressed in LEXSY T7-TR cells for structural studies

**Purification:**

- **Expression system**: LEXSY (Leishmania tarentolae)
- **Expression construct**: C-terminal polyhistidine tag

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
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> / HisPur Cobalt Resin</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> pH 7.5, 0.2 M NaCl, 0.2 M L-Histidine, 2 mM 6-aminohexanoic acid, cOmplete protease inhibitor + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a> on <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> Increase 10/300 GL</td>
      <td>—</td>
      <td>50 mM NaH2PO4/Na2HPO4 pH 5.2, 0.2 M NaCl, 1 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, 2 mM 6-aminohexanoic acid, cOmplete + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Fractions with A280/A470 absorbance ratio ~1.8 were pooled</td>
    </tr>
  </tbody>
</table>
**Final sample**: 40 mg/ml in [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) buffer

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>Monoolein</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>1:1 (v/v)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>22°C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2-6 months</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>2.4 M KH2PO4/Na2HPO4, pH 5.2-5.6, 20% (w/v) <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>300 nl protein-mesophase mixture overlaid with 500 nl precipitant. Hexagonal and rod-shaped crystals grew to 30-150 um.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6eid">6EID</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYGGALSAVGRELLFVTNPVVVNGSVLVPED</span><span class="topo-inside">QCYCAGWIESRGTNGAQTA</span><span class="topo-membrane">SNVLQWLAAGFSILLLMFYA</span><span class="topo-outside">YQTWKSTCGWE</span><span class="topo-membrane">EIYVCAIEMVKVILEFFFE</span><span class="topo-inside">FKNPSMLYLATGHRV</span><span class="topo-membrane">QWLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">YAEWLLTCPVIL</span><span class="topo-outside">IHLSNLTGLSNDYSRRTMG</span><span class="topo-membrane">LLVSDIGTIVWGATSAMA</span><span class="topo-inside">TGY</span><span class="topo-membrane">VKVIFFCLGLCYGANTFF</span><span class="topo-outside">HAAKAYIEGYHTVPKGRCRQVVTGM</span><span class="topo-membrane">AWLFFVSWGMFPILFILG</span><span class="topo-inside">PEGFGVL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310     </span>
<span class="topo-line"><span class="topo-inside">SVYG</span><span class="topo-membrane">STVGHTIIDLMSKNCWGL</span><span class="topo-outside">LGHYLRVLIHEHILIHG</span><span class="topo-unknown">DIRKTTKLNIGGTEIEVETLVEDEAEAGAVNKGTGK</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>33</td>
      <td>51</td>
      <td>33</td>
      <td>51</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>71</td>
      <td>52</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>82</td>
      <td>72</td>
      <td>82</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>101</td>
      <td>83</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>116</td>
      <td>102</td>
      <td>116</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>132</td>
      <td>117</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>133</td>
      <td>151</td>
      <td>133</td>
      <td>151</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>169</td>
      <td>152</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>172</td>
      <td>170</td>
      <td>172</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>190</td>
      <td>173</td>
      <td>190</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>215</td>
      <td>191</td>
      <td>215</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>233</td>
      <td>216</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>244</td>
      <td>234</td>
      <td>244</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>245</td>
      <td>262</td>
      <td>245</td>
      <td>262</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>263</td>
      <td>279</td>
      <td>263</td>
      <td>279</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6eid">6EID</a> — Chain C (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYGGALSAVGRELLFVTNPVVVNGSVLVPED</span><span class="topo-inside">QCYCAGWIESRGTNGAQTA</span><span class="topo-membrane">SNVLQWLAAGFSILLLMFYA</span><span class="topo-outside">YQTWKSTCGWE</span><span class="topo-membrane">EIYVCAIEMVKVILEFFFE</span><span class="topo-inside">FKNPSMLYLATGHRV</span><span class="topo-membrane">QWLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">YAEWLLTCPVIL</span><span class="topo-outside">IHLSNLTGLSNDYSRRTMG</span><span class="topo-membrane">LLVSDIGTIVWGATSAMA</span><span class="topo-inside">TGY</span><span class="topo-membrane">VKVIFFCLGLCYGANTFF</span><span class="topo-outside">HAAKAYIEGYHTVPKGRCRQVVTGM</span><span class="topo-membrane">AWLFFVSWGMFPILFILG</span><span class="topo-inside">PEGFGVL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310     </span>
<span class="topo-line"><span class="topo-inside">SVYG</span><span class="topo-membrane">STVGHTIIDLMSKNCWGL</span><span class="topo-outside">LGHYLRVLIHEHILIHG</span><span class="topo-unknown">DIRKTTKLNIGGTEIEVETLVEDEAEAGAVNKGTGK</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>33</td>
      <td>51</td>
      <td>33</td>
      <td>51</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>71</td>
      <td>52</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>82</td>
      <td>72</td>
      <td>82</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>101</td>
      <td>83</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>116</td>
      <td>102</td>
      <td>116</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>132</td>
      <td>117</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>133</td>
      <td>151</td>
      <td>133</td>
      <td>151</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>169</td>
      <td>152</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>172</td>
      <td>170</td>
      <td>172</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>190</td>
      <td>173</td>
      <td>190</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>215</td>
      <td>191</td>
      <td>215</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>233</td>
      <td>216</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>244</td>
      <td>234</td>
      <td>244</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>245</td>
      <td>262</td>
      <td>245</td>
      <td>262</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>263</td>
      <td>279</td>
      <td>263</td>
      <td>279</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6eid">6EID</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYGGALSAVGRELLFVTNPVVVNGSVLVPED</span><span class="topo-inside">QCYCAGWIESRGTNGAQTA</span><span class="topo-membrane">SNVLQWLAAGFSILLLMFYA</span><span class="topo-outside">YQTWKSTCGWE</span><span class="topo-membrane">EIYVCAIEMVKVILEFFFE</span><span class="topo-inside">FKNPSMLYLATGHRV</span><span class="topo-membrane">QWLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">YAEWLLTCPVIL</span><span class="topo-outside">IHLSNLTGLSNDYSRRTMG</span><span class="topo-membrane">LLVSDIGTIVWGATSAMA</span><span class="topo-inside">TGY</span><span class="topo-membrane">VKVIFFCLGLCYGANTFF</span><span class="topo-outside">HAAKAYIEGYHTVPKGRCRQVVTGM</span><span class="topo-membrane">AWLFFVSWGMFPILFILG</span><span class="topo-inside">PEGFGVL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310     </span>
<span class="topo-line"><span class="topo-inside">SVYG</span><span class="topo-membrane">STVGHTIIDLMSKNCWGL</span><span class="topo-outside">LGHYLRVLIHEHILIHG</span><span class="topo-unknown">DIRKTTKLNIGGTEIEVETLVEDEAEAGAVNKGTGK</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>33</td>
      <td>51</td>
      <td>33</td>
      <td>51</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>71</td>
      <td>52</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>82</td>
      <td>72</td>
      <td>82</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>101</td>
      <td>83</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>116</td>
      <td>102</td>
      <td>116</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>132</td>
      <td>117</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>133</td>
      <td>151</td>
      <td>133</td>
      <td>151</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>169</td>
      <td>152</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>172</td>
      <td>170</td>
      <td>172</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>190</td>
      <td>173</td>
      <td>190</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>215</td>
      <td>191</td>
      <td>215</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>233</td>
      <td>216</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>244</td>
      <td>234</td>
      <td>244</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>245</td>
      <td>262</td>
      <td>245</td>
      <td>262</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>263</td>
      <td>279</td>
      <td>263</td>
      <td>279</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6eid">6EID</a> — Chain C (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYGGALSAVGRELLFVTNPVVVNGSVLVPED</span><span class="topo-inside">QCYCAGWIESRGTNGAQTA</span><span class="topo-membrane">SNVLQWLAAGFSILLLMFYA</span><span class="topo-outside">YQTWKSTCGWE</span><span class="topo-membrane">EIYVCAIEMVKVILEFFFE</span><span class="topo-inside">FKNPSMLYLATGHRV</span><span class="topo-membrane">QWLR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">YAEWLLTCPVIL</span><span class="topo-outside">IHLSNLTGLSNDYSRRTMG</span><span class="topo-membrane">LLVSDIGTIVWGATSAMA</span><span class="topo-inside">TGY</span><span class="topo-membrane">VKVIFFCLGLCYGANTFF</span><span class="topo-outside">HAAKAYIEGYHTVPKGRCRQVVTGM</span><span class="topo-membrane">AWLFFVSWGMFPILFILG</span><span class="topo-inside">PEGFGVL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310     </span>
<span class="topo-line"><span class="topo-inside">SVYG</span><span class="topo-membrane">STVGHTIIDLMSKNCWGL</span><span class="topo-outside">LGHYLRVLIHEHILIHG</span><span class="topo-unknown">DIRKTTKLNIGGTEIEVETLVEDEAEAGAVNKGTGK</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>33</td>
      <td>51</td>
      <td>33</td>
      <td>51</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>71</td>
      <td>52</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>82</td>
      <td>72</td>
      <td>82</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>101</td>
      <td>83</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>116</td>
      <td>102</td>
      <td>116</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>132</td>
      <td>117</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>133</td>
      <td>151</td>
      <td>133</td>
      <td>151</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>169</td>
      <td>152</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>172</td>
      <td>170</td>
      <td>172</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>190</td>
      <td>173</td>
      <td>190</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>215</td>
      <td>191</td>
      <td>215</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>233</td>
      <td>216</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>244</td>
      <td>234</td>
      <td>244</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>245</td>
      <td>262</td>
      <td>245</td>
      <td>262</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>263</td>
      <td>279</td>
      <td>263</td>
      <td>279</td>
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

### Ion conduction pathway with four cavities and three gates

The ChR2 structure reveals an ion conduction pathway comprising four cavities
(EC1, EC2, IC1, IC2) separated by three gates (ECG, CG, ICG). The [Retinal](/xray-mp-wiki/reagents/ligands/retinal/)
Schiff base (RSB) at the central gate controls and synchronizes all three
gates through an extended hydrogen-bonding network involving water molecules
and side-chain residues. Arginines R120 and R268 form the cores of the ECG
and ICG, respectively.

### DC gate controls gating lifetime

The DC gate, named after D156 (TM4) and C128 (TM3), comprises a water-mediated
bond separate from the main ion pore but directly interacting with the RSB.
This gate controls channel open lifetime. The C128T mutant, with a prolonged
open-state lifetime, disrupts the water-mediated hydrogen bond network,
replacing it with a direct hydrogen bond between T128 and D156, affecting
the Schiff base environment and gating kinetics.

### Structural comparison reveals differences from C1C2 chimera

Comparison with the C1C2 chimera structure (PDB 3UG9) shows considerable
differences. In ChR2, E90 is a key determinant of ion selectivity and is
hydrogen-bonded to the proton acceptor D253, enabling direct influence by
[Retinal](/xray-mp-wiki/reagents/ligands/retinal/) isomerization and subsequent D253 protonation. In C1C2, the
corresponding E129 is not hydrogen-bonded to D292, explaining distinct
FTIR spectroscopy responses between the two proteins.


## Cross-References

- <a href="/xray-mp-wiki/proteins/rhodopsins/channelrhodopsin-c1c2/">Channelrhodopsin C1C2</a> — Chimeric construct used for comparison; shows distinct structural and functional differences from native ChR2
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/channelrhodopsin-photocycle/">Channelrhodopsin Photocycle</a> — ChR2 structures provide molecular basis for understanding the photocycle and gating mechanism
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltoside (DDM)</a> — Used throughout purification (0.1% for affinity, 0.05% for [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/))
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Used as [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) host lipid for in meso crystallization
- <a href="/xray-mp-wiki/methods/expression-systems/lexsy-expression-system/">LEXSY Leishmania tarentolae Expression System</a> — Expression system used for ChR2 production
- <a href="/xray-mp-wiki/proteins/rhodopsins/gr/">GR (Halobacterium sp. GR Bacteriorhodopsin)</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/gpcr/opsin/">Opsin (Retinal-Free Rhodopsin Apoprotein)</a> — Related protein structure
- <a href="/xray-mp-wiki/methods/structure-determination/xray-crystallography/">X-ray Crystallography</a> — Method used in the study
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> — Immobilized metal affinity chromatography resin
- <a href="/xray-mp-wiki/reagents/additives/superdex-200">Superdex 200 Increase SEC Resin</a> — Size-exclusion chromatography resin
