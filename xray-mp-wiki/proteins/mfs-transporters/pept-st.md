---
title: "PepT_St Proton-Dependent Oligopeptide Transporter from Streptococcus thermophilus"
created: 2026-05-29
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##EMBOJ.2012.157, doi/10.1016##j.str.2018.01.005]
verified: regex
uniprot_id: ['Q5M4H8', 'Q8EKT7']
---

# PepT_St Proton-Dependent Oligopeptide Transporter from Streptococcus thermophilus

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q5M4H8">UniProt: Q5M4H8</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q8EKT7">UniProt: Q8EKT7</a>

<span class="expr-badge">Streptococcus thermophilus (strain ATCC BAA-250 / LMG 18311)</span>

## Overview

PepT_St is a proton-dependent oligopeptide transporter (POT) from Streptococcus thermophilus that mediates the uptake of di- and tripeptides across the cell membrane. It belongs to the Major Facilitator Superfamily (MFS) and adopts the canonical 12-transmembrane-helix MFS fold with N and C domains that cradle a centrally located substrate binding cavity. PepT_St exhibits broad substrate specificity for dipeptides, binding them with millimolar affinity. The structure reveals a highly adaptable binding site that accommodates diverse peptide side chains through conformational changes in binding pocket residues, water network rearrangement, and peptide repositioning. Two crystal structures have been determined: an inward open conformation from the 2012 EMBO J paper and inward-facing partially occluded conformations from the 2018 Structure paper. The 2012 structure provides key insights into the alternating access mechanism of POT family transporters, revealing a hinge-like movement in the C-terminal half that opens the intracellular gate.


## Publications

### doi/10.1038##EMBOJ.2012.157

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2xut">2XUT</a></td>
      <td>3.0 A</td>
      <td>not specified</td>
      <td>PepT_So from Shewanella oneidensis, wild type, inward occluded conformation</td>
      <td>dipeptide substrate</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C41
- **Construct**: Full-length PepT_St cloned into pNIC-CTHF vector with C-terminal His-Tag and TEV cleavage site
- **Notes**: [Kanamycin](/xray-mp-wiki/reagents/additives/kanamycin) resistance marker. Cells grown at 37°C in terrific broth media with 30 µg/ml [Kanamycin](/xray-mp-wiki/reagents/additives/kanamycin), induced with 0.2 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg) at OD600 0.6-0.8, continued at 18°C for 16-18 hours.


<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2xut">2XUT</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MNSPVDAPKWPR</span><span class="topo-inside">QIPYII</span><span class="topo-membrane">ASEACERFSFYGMRNILTPFL</span><span class="topo-outside">MTALLLSIPEELRGA</span><span class="topo-membrane">VAKDVFHSFVIGVYFFPLLG</span><span class="topo-inside">GWIADRFFGKYN</span><span class="topo-membrane">TILWLSLIYCVGHAFLAIFE</span><span class="topo-outside">HSVQ</span><span class="topo-membrane">GFYTGLFLIA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LGSGGIKP</span><span class="topo-inside">LVSSFMGDQFDQSNKSLAQKAFDMF</span><span class="topo-membrane">YFTINFGSFFASLSMPLLL</span><span class="topo-outside">KNFGAA</span><span class="topo-membrane">VAFGIPGVLMFVATVFFWL</span><span class="topo-inside">GRKRYIHMP</span><span class="topo-unknown">PEPKDPHGFLPVIRSALLTK</span><span class="topo-inside">VEGKGNIGLVLAL</span><span class="topo-membrane">I</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">GGVSAAYALVNIPTL</span><span class="topo-outside">G</span><span class="topo-membrane">IVAGLCCAMVLVMGFVG</span><span class="topo-inside">AGASLQLERARKSHPDAAVDGVRSVLRILVLF</span><span class="topo-membrane">ALVTPFWSLFDQKASTWILQA</span><span class="topo-outside">NDMVKPQW</span><span class="topo-membrane">FEPAMMQALNPLLVMLLI</span><span class="topo-inside">PFNNFV</span><span class="topo-unknown">LY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-unknown">PAIERMGVKL</span><span class="topo-inside">TALRKM</span><span class="topo-membrane">GAGIAITGLSWIVVGTIQ</span><span class="topo-outside">LMMDGGSAL</span><span class="topo-membrane">SIFWQILPYALLTFGEVLVS</span><span class="topo-inside">ATGLEFAYSQAPKAMKGTIMS</span><span class="topo-membrane">FWTLSVTVGNLWVLLANVSV</span><span class="topo-outside">KSP</span><span class="topo-unknown">TVTEQIVQTG</span><span class="topo-outside">MSV</span></span>
<span class="topo-ruler">       490       500       510       520    </span>
<span class="topo-line"><span class="topo-outside">TA</span><span class="topo-membrane">FQMFFFAGFAILAAIVF</span><span class="topo-inside">A</span><span class="topo-unknown">LYARSYQMQDHYRQATGSENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (37 regions)</summary>
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
      <td>Unknown</td>
    </tr>
    <tr>
      <td>13</td>
      <td>18</td>
      <td>13</td>
      <td>18</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>39</td>
      <td>19</td>
      <td>39</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>54</td>
      <td>40</td>
      <td>54</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>74</td>
      <td>55</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>86</td>
      <td>75</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>106</td>
      <td>87</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>110</td>
      <td>107</td>
      <td>110</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>111</td>
      <td>128</td>
      <td>111</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>153</td>
      <td>129</td>
      <td>153</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>172</td>
      <td>154</td>
      <td>172</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>173</td>
      <td>178</td>
      <td>173</td>
      <td>178</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>197</td>
      <td>179</td>
      <td>197</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>206</td>
      <td>198</td>
      <td>206</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>226</td>
      <td>207</td>
      <td>226</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>227</td>
      <td>239</td>
      <td>227</td>
      <td>239</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>255</td>
      <td>240</td>
      <td>255</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>256</td>
      <td>256</td>
      <td>256</td>
      <td>256</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>257</td>
      <td>273</td>
      <td>257</td>
      <td>273</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>274</td>
      <td>305</td>
      <td>274</td>
      <td>305</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>306</td>
      <td>326</td>
      <td>306</td>
      <td>326</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>327</td>
      <td>334</td>
      <td>327</td>
      <td>334</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>335</td>
      <td>352</td>
      <td>335</td>
      <td>352</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>353</td>
      <td>358</td>
      <td>353</td>
      <td>358</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>359</td>
      <td>370</td>
      <td>359</td>
      <td>370</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>371</td>
      <td>376</td>
      <td>371</td>
      <td>376</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>394</td>
      <td>377</td>
      <td>394</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>395</td>
      <td>403</td>
      <td>395</td>
      <td>403</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>404</td>
      <td>423</td>
      <td>404</td>
      <td>423</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>424</td>
      <td>444</td>
      <td>424</td>
      <td>444</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>464</td>
      <td>445</td>
      <td>464</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>465</td>
      <td>467</td>
      <td>465</td>
      <td>467</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>468</td>
      <td>477</td>
      <td>468</td>
      <td>477</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>478</td>
      <td>482</td>
      <td>478</td>
      <td>482</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>483</td>
      <td>499</td>
      <td>483</td>
      <td>499</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>500</td>
      <td>500</td>
      <td>500</td>
      <td>500</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>501</td>
      <td>524</td>
      <td>501</td>
      <td>524</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1016##j.str.2018.01.005

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5oxk">5OXK</a></td>
      <td>2.7 A</td>
      <td>--</td>
      <td>PepT_St wild type, full length</td>
      <td>Ala-Gln</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5oxl">5OXL</a></td>
      <td>2.5 A</td>
      <td>--</td>
      <td>PepT_St wild type, full length</td>
      <td>Ala-Leu</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5oxm">5OXM</a></td>
      <td>2.7 A</td>
      <td>--</td>
      <td>PepT_St wild type, full length</td>
      <td>Asp-Glu</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5oxn">5OXN</a></td>
      <td>2.2 A</td>
      <td>--</td>
      <td>PepT_St wild type, full length</td>
      <td>Phe-Ala</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5oxo">5OXO</a></td>
      <td>2.0 A</td>
      <td>--</td>
      <td>PepT_St wild type, full length</td>
      <td>none (apo)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5oxp">5OXP</a></td>
      <td>2.4 A</td>
      <td>--</td>
      <td>PepT_St wild type, full length</td>
      <td>phosphate</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5oxq">5OXQ</a></td>
      <td>2.2 A</td>
      <td>--</td>
      <td>PepT_St wild type, full length</td>
      <td><a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a>, phosphate</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6eia">6EIA</a></td>
      <td>--</td>
      <td>--</td>
      <td>PepT_St wild type, full length</td>
      <td><a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a>, phosphate</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C41
- **Construct**: Full-length PepT_St cloned into pNIC-CTHF vector with C-terminal His-Tag and TEV cleavage site
- **Notes**: [Kanamycin](/xray-mp-wiki/reagents/additives/kanamycin) resistance marker. Cells grown at 37°C in terrific broth media with 30 µg/ml [Kanamycin](/xray-mp-wiki/reagents/additives/kanamycin), induced with 0.2 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg) at OD600 0.6-0.8, continued at 18°C for 16-18 hours.


**Purification:**

- **Expression system**: Escherichia coli C41
- **Expression construct**: Full-length PepT_St with C-terminal His-Tag, TEV cleavage site
- **Tag info**: His-Tag, TEV cleavage site

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
      <td>Cell lysis</td>
      <td>Membrane fractionation</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Cells harvested by centrifugation, pellet stored at -20°C</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>-- + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>--</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>--</td>
      <td>-- + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>His-Tag affinity capture</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td>--</td>
      <td>-- + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>--</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified in 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm) at pH 7.5

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a></td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/mag">MAG</a> 7.8 (1-(7Z-pentadecenoyl)-rac-<a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, Avanti Lipids)</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>1:1 (volume)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallization plates set up using Mosquito-LCP robot (TTP Labtech). 50 nl mesophase dispensed in wells, overlaid with 800 nl precipitant. Laminex UV Plastic Bases with 100 µm depth wells sealed with Laminex UV Plastic 200 micron Film Covers. Crystallant contains <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a>, phosphate, and small PEGs. Overall pH between 5.0 and 5.8.
</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a></td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/mag">MAG</a> 7.8 (1-(7Z-pentadecenoyl)-rac-<a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, Avanti Lipids)</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>1:1 (volume)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Apo structure obtained by changing buffer to <a href="/xray-mp-wiki/reagents/buffers/citrate">Citrate Buffer (Sodium Citrate)</a> pH 4.5 to inhibit peptide binding. High-quality 2.0 A inward open structure.
</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a></td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/mag">MAG</a> 7.8 (1-(7Z-pentadecenoyl)-rac-<a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, Avanti Lipids)</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>1:1 (volume)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Structures with adventitiously bound <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> obtained using <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> buffer. Increasing <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> from 100 mM to 300 mM improved electron density.
</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a></td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/mag">MAG</a> 7.8 (1-(7Z-pentadecenoyl)-rac-<a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, Avanti Lipids)</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>1:1 (volume)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Structure with phosphate and <a href="/xray-mp-wiki/reagents/additives/peg">PEG</a> bound obtained using phosphate buffer instead of <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a>.
</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5oxk">5OXK</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEDKG</span><span class="topo-inside">KTFFGQPLGLS</span><span class="topo-membrane">TLFMTEMWERFSYYGMRA</span><span class="topo-outside">ILLYYMWFLISTGDLHITRATAAS</span><span class="topo-membrane">IMAIYASMVYLSGTIG</span><span class="topo-inside">GFVADRIIGARP</span><span class="topo-membrane">AVFWGGVLIMLGHIVL</span><span class="topo-outside">ALPFGASAL</span><span class="topo-membrane">FGSIILIII</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GTGFLKPNV</span><span class="topo-inside">STLVGTLYDEHDRRRDAGFSI</span><span class="topo-membrane">FVFGINLGAFIAPLIV</span><span class="topo-outside">GAAQEAAGYHVAF</span><span class="topo-membrane">SLAAIGMFIGLLVYYFG</span><span class="topo-inside">GKKTLDPHYLRPTDPLAPEEVKPLLVK</span><span class="topo-membrane">VSLAVAGFIAIIVVMNL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">V</span><span class="topo-outside">GWNSLP</span><span class="topo-membrane">AYINLLTIVAIAIPVFY</span><span class="topo-inside">FAWMI</span><span class="topo-unknown">SSVKVTSTEHLR</span><span class="topo-inside">VVSYI</span><span class="topo-membrane">PLFIAAVLFWAIEEQGSVVLA</span><span class="topo-outside">TFAAERVDSSWFPVSW</span><span class="topo-membrane">FQSLNPLFIMLYTPFF</span><span class="topo-inside">AWLWTAW</span><span class="topo-unknown">KKNQ</span><span class="topo-inside">PSSPTK</span><span class="topo-membrane">FAVG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LMFAGLSFLLMA</span><span class="topo-outside">IPGALYGTSGKVSPL</span><span class="topo-membrane">WLVGSWALVILGEMLISP</span><span class="topo-unknown">VGLSVTTKLAPKAF</span><span class="topo-inside">NSQMMS</span><span class="topo-membrane">MWFLSSSVGSALNAQLV</span><span class="topo-outside">TLYNAKSEVAY</span><span class="topo-membrane">FSYFGLGSVVLGIVLVFL</span><span class="topo-unknown">SKRIQGLMQ</span></span>
<span class="topo-ruler">       490</span>
<span class="topo-line"><span class="topo-unknown">GVEAENLYFQ</span></span>
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
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>16</td>
      <td>6</td>
      <td>16</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>34</td>
      <td>17</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>58</td>
      <td>35</td>
      <td>58</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>74</td>
      <td>59</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>86</td>
      <td>75</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>102</td>
      <td>87</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>111</td>
      <td>103</td>
      <td>111</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>129</td>
      <td>112</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>130</td>
      <td>150</td>
      <td>130</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>166</td>
      <td>151</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>179</td>
      <td>167</td>
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
      <td>223</td>
      <td>197</td>
      <td>223</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>224</td>
      <td>241</td>
      <td>224</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>242</td>
      <td>247</td>
      <td>242</td>
      <td>247</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>264</td>
      <td>248</td>
      <td>264</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>265</td>
      <td>269</td>
      <td>265</td>
      <td>269</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>270</td>
      <td>281</td>
      <td>270</td>
      <td>281</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>282</td>
      <td>286</td>
      <td>282</td>
      <td>286</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>307</td>
      <td>287</td>
      <td>307</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>308</td>
      <td>323</td>
      <td>308</td>
      <td>323</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>324</td>
      <td>339</td>
      <td>324</td>
      <td>339</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>340</td>
      <td>346</td>
      <td>340</td>
      <td>346</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>347</td>
      <td>350</td>
      <td>347</td>
      <td>350</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>351</td>
      <td>356</td>
      <td>351</td>
      <td>356</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>357</td>
      <td>372</td>
      <td>357</td>
      <td>372</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>373</td>
      <td>387</td>
      <td>373</td>
      <td>387</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>388</td>
      <td>405</td>
      <td>388</td>
      <td>405</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>406</td>
      <td>419</td>
      <td>406</td>
      <td>419</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>420</td>
      <td>425</td>
      <td>420</td>
      <td>425</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>426</td>
      <td>442</td>
      <td>426</td>
      <td>442</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>443</td>
      <td>453</td>
      <td>443</td>
      <td>453</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>454</td>
      <td>471</td>
      <td>454</td>
      <td>471</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>473</td>
      <td>490</td>
      <td>473</td>
      <td>490</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5oxl">5OXL</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEDK</span><span class="topo-inside">GKTFFGQPLGLSTLF</span><span class="topo-membrane">MTEMWERFSYYGMRAILL</span><span class="topo-outside">YYMWFLISTGDLHITRATA</span><span class="topo-membrane">ASIMAIYASMVYLSGTIG</span><span class="topo-inside">GFVADRIIGARPA</span><span class="topo-membrane">VFWGGVLIMLGHIVLAL</span><span class="topo-outside">PFGASA</span><span class="topo-membrane">LFGSIILIII</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GTGFLKP</span><span class="topo-inside">NVSTLVGTLYDEHDRRRDAGFSIFV</span><span class="topo-membrane">FGINLGAFIAPLIVGAAQ</span><span class="topo-outside">EAAGYH</span><span class="topo-membrane">VAFSLAAIGMFIGLLVYY</span><span class="topo-inside">FGGKKTLDPHYLRPTDPLAPEEVKPLL</span><span class="topo-membrane">VKVSLAVAGFIAIIVVMNL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">VGWNSL</span><span class="topo-membrane">PAYINLLTIVAIAIPVF</span><span class="topo-inside">YFAWM</span><span class="topo-unknown">ISSVKVTS</span><span class="topo-inside">TEHLRVVSYIPLF</span><span class="topo-membrane">IAAVLFWAIEEQGSVVLATFA</span><span class="topo-outside">AERVDSSWF</span><span class="topo-membrane">PVSWFQSLNPLFIMLYT</span><span class="topo-inside">PFFAWLWTAW</span><span class="topo-unknown">KKNQ</span><span class="topo-inside">PSSPTKF</span><span class="topo-membrane">AVG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LMFAGLSFLLMAIP</span><span class="topo-outside">GALYGTSGKVS</span><span class="topo-membrane">PLWLVGSWALVILGEMLIS</span><span class="topo-inside">PVGLSV</span><span class="topo-unknown">TTKLAPK</span><span class="topo-inside">AFNSQMMSMWF</span><span class="topo-membrane">LSSSVGSALNAQLVTLY</span><span class="topo-outside">NAKSEV</span><span class="topo-membrane">AYFSYFGLGSVVLGIVL</span><span class="topo-inside">VFL</span><span class="topo-unknown">SKRIQGLMQ</span></span>
<span class="topo-ruler">       490</span>
<span class="topo-line"><span class="topo-unknown">GVEAENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (37 regions)</summary>
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
      <td>19</td>
      <td>5</td>
      <td>19</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>37</td>
      <td>20</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>56</td>
      <td>38</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>74</td>
      <td>57</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>87</td>
      <td>75</td>
      <td>87</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>104</td>
      <td>88</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>110</td>
      <td>105</td>
      <td>110</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>111</td>
      <td>127</td>
      <td>111</td>
      <td>127</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>128</td>
      <td>152</td>
      <td>128</td>
      <td>152</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>170</td>
      <td>153</td>
      <td>170</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>171</td>
      <td>176</td>
      <td>171</td>
      <td>176</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>194</td>
      <td>177</td>
      <td>194</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>195</td>
      <td>221</td>
      <td>195</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>222</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>246</td>
      <td>241</td>
      <td>246</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>247</td>
      <td>263</td>
      <td>247</td>
      <td>263</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>264</td>
      <td>268</td>
      <td>264</td>
      <td>268</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>269</td>
      <td>276</td>
      <td>269</td>
      <td>276</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>277</td>
      <td>289</td>
      <td>277</td>
      <td>289</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>310</td>
      <td>290</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>319</td>
      <td>311</td>
      <td>319</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>320</td>
      <td>336</td>
      <td>320</td>
      <td>336</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>337</td>
      <td>346</td>
      <td>337</td>
      <td>346</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>347</td>
      <td>350</td>
      <td>347</td>
      <td>350</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>351</td>
      <td>357</td>
      <td>351</td>
      <td>357</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>358</td>
      <td>374</td>
      <td>358</td>
      <td>374</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>375</td>
      <td>385</td>
      <td>375</td>
      <td>385</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>386</td>
      <td>404</td>
      <td>386</td>
      <td>404</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>405</td>
      <td>410</td>
      <td>405</td>
      <td>410</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>411</td>
      <td>417</td>
      <td>411</td>
      <td>417</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>418</td>
      <td>428</td>
      <td>418</td>
      <td>428</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>429</td>
      <td>445</td>
      <td>429</td>
      <td>445</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>446</td>
      <td>451</td>
      <td>446</td>
      <td>451</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>452</td>
      <td>468</td>
      <td>452</td>
      <td>468</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>469</td>
      <td>471</td>
      <td>469</td>
      <td>471</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>490</td>
      <td>472</td>
      <td>490</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5oxm">5OXM</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEDKG</span><span class="topo-inside">KTFFGQPLGLS</span><span class="topo-membrane">TLFMTEMWERFSYYGMRA</span><span class="topo-outside">ILLYYMWFLISTGDLHITRATAAS</span><span class="topo-membrane">IMAIYASMVYLSGTIG</span><span class="topo-inside">GFVADRIIGARP</span><span class="topo-membrane">AVFWGGVLIMLGHIV</span><span class="topo-outside">LALPFGASALF</span><span class="topo-membrane">GSIILIII</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GTGFLKPNV</span><span class="topo-inside">STLVGTLYDEHDRRRDAGFSI</span><span class="topo-membrane">FVFGINLGAFIAPLIV</span><span class="topo-outside">GAAQEAAGYHVAF</span><span class="topo-membrane">SLAAIGMFIGLLVYYFG</span><span class="topo-inside">GKKTLDPHYLRPTDPLAPEEVKPLLVK</span><span class="topo-membrane">VSLAVAGFIAIIVVMNL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">VGWNSLPA</span><span class="topo-membrane">YINLLTIVAIAIPVF</span><span class="topo-inside">YFAWM</span><span class="topo-unknown">ISSVKVT</span><span class="topo-inside">STEHLRVVSYI</span><span class="topo-membrane">PLFIAAVLFWAIEEQGSVVL</span><span class="topo-outside">ATFAAERVDSSWFPVSW</span><span class="topo-membrane">FQSLNPLFIMLYTPFF</span><span class="topo-inside">AWLWTA</span><span class="topo-unknown">WKKN</span><span class="topo-inside">QPSSPT</span><span class="topo-membrane">KFAVG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LMFAGLSFLLM</span><span class="topo-outside">AIPGALYGTSGKVSPLWL</span><span class="topo-membrane">VGSWALVILGEMLISP</span><span class="topo-unknown">VGLSVTTKLAPKAFNSQM</span><span class="topo-inside">MSM</span><span class="topo-membrane">WFLSSSVGSALNAQLV</span><span class="topo-outside">TLYNAKSEVAYF</span><span class="topo-membrane">SYFGLGSVVLGIVLVF</span><span class="topo-inside">LS</span><span class="topo-unknown">KRIQGLMQ</span></span>
<span class="topo-ruler">       490</span>
<span class="topo-line"><span class="topo-unknown">GVEAENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (36 regions)</summary>
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
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>16</td>
      <td>6</td>
      <td>16</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>34</td>
      <td>17</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>58</td>
      <td>35</td>
      <td>58</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>74</td>
      <td>59</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>86</td>
      <td>75</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>101</td>
      <td>87</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>112</td>
      <td>102</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>129</td>
      <td>113</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>130</td>
      <td>150</td>
      <td>130</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>166</td>
      <td>151</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>179</td>
      <td>167</td>
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
      <td>223</td>
      <td>197</td>
      <td>223</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>224</td>
      <td>240</td>
      <td>224</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>248</td>
      <td>241</td>
      <td>248</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>263</td>
      <td>249</td>
      <td>263</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>264</td>
      <td>268</td>
      <td>264</td>
      <td>268</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>269</td>
      <td>275</td>
      <td>269</td>
      <td>275</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>276</td>
      <td>286</td>
      <td>276</td>
      <td>286</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>306</td>
      <td>287</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>323</td>
      <td>307</td>
      <td>323</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>324</td>
      <td>339</td>
      <td>324</td>
      <td>339</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>340</td>
      <td>345</td>
      <td>340</td>
      <td>345</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>346</td>
      <td>349</td>
      <td>346</td>
      <td>349</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>350</td>
      <td>355</td>
      <td>350</td>
      <td>355</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>356</td>
      <td>371</td>
      <td>356</td>
      <td>371</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>372</td>
      <td>389</td>
      <td>372</td>
      <td>389</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>405</td>
      <td>390</td>
      <td>405</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>407</td>
      <td>423</td>
      <td>407</td>
      <td>423</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>424</td>
      <td>426</td>
      <td>424</td>
      <td>426</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>427</td>
      <td>442</td>
      <td>427</td>
      <td>442</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>443</td>
      <td>454</td>
      <td>443</td>
      <td>454</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>455</td>
      <td>470</td>
      <td>455</td>
      <td>470</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>471</td>
      <td>472</td>
      <td>471</td>
      <td>472</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>473</td>
      <td>490</td>
      <td>473</td>
      <td>490</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5oxn">5OXN</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEDK</span><span class="topo-inside">GKTFFGQPLGLS</span><span class="topo-membrane">TLFMTEMWERFSYYGMRAILL</span><span class="topo-outside">YYMWFLISTGDLHITRATAA</span><span class="topo-membrane">SIMAIYASMVYLSGTIGGFVA</span><span class="topo-inside">DRIIGA</span><span class="topo-membrane">RPAVFWGGVLIMLGHIVLAL</span><span class="topo-outside">PFGASA</span><span class="topo-membrane">LFGSIILIII</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GTGFLKPNVS</span><span class="topo-inside">TLVGTLYDEHDRRRDAGFS</span><span class="topo-membrane">IFVFGINLGAFIAPLIVGAA</span><span class="topo-outside">QEAAGYHV</span><span class="topo-membrane">AFSLAAIGMFIGLLVYYFGG</span><span class="topo-inside">KKTLDPHYLRPTDPLAPEEVK</span><span class="topo-membrane">PLLVKVSLAVAGFIAIIVVMNL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">VGWNSL</span><span class="topo-membrane">PAYINLLTIVAIAIPVFYFAW</span><span class="topo-inside">MISS</span><span class="topo-unknown">VKVTS</span><span class="topo-inside">TEHLRVVSY</span><span class="topo-membrane">IPLFIAAVLFWAIEEQGSVVLATFA</span><span class="topo-outside">AERVDSSWFP</span><span class="topo-membrane">VSWFQSLNPLFIMLYTPFF</span><span class="topo-inside">AWLWTAWKKNQPSSP</span><span class="topo-membrane">TKFAVG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LMFAGLSFLLMAI</span><span class="topo-outside">PGALYGTSGKVS</span><span class="topo-membrane">PLWLVGSWALVILGEMLISPVG</span><span class="topo-inside">LSVTTKL</span><span class="topo-unknown">APKAFN</span><span class="topo-inside">SQMMS</span><span class="topo-membrane">MWFLSSSVGSALNAQLVTL</span><span class="topo-outside">YNAKSEVA</span><span class="topo-membrane">YFSYFGLGSVVLGIVLVFLS</span><span class="topo-inside">KRIQGL</span><span class="topo-unknown">MQ</span></span>
<span class="topo-ruler">       490</span>
<span class="topo-line"><span class="topo-unknown">GVEAENLYFQ</span></span>
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
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>16</td>
      <td>5</td>
      <td>16</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>37</td>
      <td>17</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>57</td>
      <td>38</td>
      <td>57</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>78</td>
      <td>58</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>84</td>
      <td>79</td>
      <td>84</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>104</td>
      <td>85</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>110</td>
      <td>105</td>
      <td>110</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>111</td>
      <td>130</td>
      <td>111</td>
      <td>130</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>131</td>
      <td>149</td>
      <td>131</td>
      <td>149</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>150</td>
      <td>169</td>
      <td>150</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>177</td>
      <td>170</td>
      <td>177</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>197</td>
      <td>178</td>
      <td>197</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>218</td>
      <td>198</td>
      <td>218</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>219</td>
      <td>240</td>
      <td>219</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>246</td>
      <td>241</td>
      <td>246</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>247</td>
      <td>267</td>
      <td>247</td>
      <td>267</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>268</td>
      <td>271</td>
      <td>268</td>
      <td>271</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>272</td>
      <td>276</td>
      <td>272</td>
      <td>276</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>277</td>
      <td>285</td>
      <td>277</td>
      <td>285</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>310</td>
      <td>286</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>320</td>
      <td>311</td>
      <td>320</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>339</td>
      <td>321</td>
      <td>339</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>340</td>
      <td>354</td>
      <td>340</td>
      <td>354</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>355</td>
      <td>373</td>
      <td>355</td>
      <td>373</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>385</td>
      <td>374</td>
      <td>385</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>386</td>
      <td>407</td>
      <td>386</td>
      <td>407</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>408</td>
      <td>414</td>
      <td>408</td>
      <td>414</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>415</td>
      <td>420</td>
      <td>415</td>
      <td>420</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>421</td>
      <td>425</td>
      <td>421</td>
      <td>425</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>426</td>
      <td>444</td>
      <td>426</td>
      <td>444</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>445</td>
      <td>452</td>
      <td>445</td>
      <td>452</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>453</td>
      <td>472</td>
      <td>453</td>
      <td>472</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>473</td>
      <td>478</td>
      <td>473</td>
      <td>478</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>479</td>
      <td>490</td>
      <td>479</td>
      <td>490</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5oxo">5OXO</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEDK</span><span class="topo-inside">GKTFFGQPLGLS</span><span class="topo-membrane">TLFMTEMWERFSYYGMRAIL</span><span class="topo-outside">LYYMWFLISTGDLHITRATAA</span><span class="topo-membrane">SIMAIYASMVYLSGTIG</span><span class="topo-inside">GFVADRIIGARP</span><span class="topo-membrane">AVFWGGVLIMLGHIVL</span><span class="topo-outside">ALPFGASAL</span><span class="topo-membrane">FGSIILIII</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GTGFLKPNV</span><span class="topo-inside">STLVGTLYDEHDRRRDAGFSI</span><span class="topo-membrane">FVFGINLGAFIAPLIVG</span><span class="topo-outside">AAQEAAGYHVAF</span><span class="topo-membrane">SLAAIGMFIGLLVYYFG</span><span class="topo-inside">GKKTLDPHYLRPTDPLAPEEVKPLL</span><span class="topo-membrane">VKVSLAVAGFIAIIVVMNL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">V</span><span class="topo-outside">GWNSLP</span><span class="topo-membrane">AYINLLTIVAIAIPVF</span><span class="topo-inside">YFAWMISS</span><span class="topo-unknown">VKVTST</span><span class="topo-inside">EHLRVVSYI</span><span class="topo-membrane">PLFIAAVLFWAIEEQGSVVLA</span><span class="topo-outside">TFAAERVDSSWFPVS</span><span class="topo-membrane">WFQSLNPLFIMLYTPFF</span><span class="topo-inside">AWLWTAWKKNQPSSPTK</span><span class="topo-membrane">FAVG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LMFAGLSFLLMAI</span><span class="topo-outside">PGALYGTSGKVSPL</span><span class="topo-membrane">WLVGSWALVILGEMLIS</span><span class="topo-inside">PVGLSVT</span><span class="topo-unknown">TKLAPKAFNSQM</span><span class="topo-inside">MSM</span><span class="topo-membrane">WFLSSSVGSALNAQLV</span><span class="topo-outside">TLYNAKSEVAY</span><span class="topo-membrane">FSYFGLGSVVLGIVLVF</span><span class="topo-inside">LSKRIQGL</span><span class="topo-unknown">MQ</span></span>
<span class="topo-ruler">       490</span>
<span class="topo-line"><span class="topo-unknown">GVEAENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (31 regions)</summary>
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
      <td>16</td>
      <td>5</td>
      <td>16</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>36</td>
      <td>17</td>
      <td>36</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>37</td>
      <td>57</td>
      <td>37</td>
      <td>57</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>74</td>
      <td>58</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>86</td>
      <td>75</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>102</td>
      <td>87</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>111</td>
      <td>103</td>
      <td>111</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>129</td>
      <td>112</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>130</td>
      <td>150</td>
      <td>130</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>167</td>
      <td>151</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>168</td>
      <td>179</td>
      <td>168</td>
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
      <td>221</td>
      <td>197</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>241</td>
      <td>222</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>242</td>
      <td>247</td>
      <td>242</td>
      <td>247</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>263</td>
      <td>248</td>
      <td>263</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>264</td>
      <td>271</td>
      <td>264</td>
      <td>271</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>286</td>
      <td>278</td>
      <td>286</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>307</td>
      <td>287</td>
      <td>307</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>308</td>
      <td>322</td>
      <td>308</td>
      <td>322</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>339</td>
      <td>323</td>
      <td>339</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>340</td>
      <td>356</td>
      <td>340</td>
      <td>356</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>357</td>
      <td>373</td>
      <td>357</td>
      <td>373</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>387</td>
      <td>374</td>
      <td>387</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>388</td>
      <td>404</td>
      <td>388</td>
      <td>404</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>405</td>
      <td>411</td>
      <td>405</td>
      <td>411</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>424</td>
      <td>426</td>
      <td>424</td>
      <td>426</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>427</td>
      <td>442</td>
      <td>427</td>
      <td>442</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>443</td>
      <td>453</td>
      <td>443</td>
      <td>453</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>454</td>
      <td>470</td>
      <td>454</td>
      <td>470</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>471</td>
      <td>478</td>
      <td>471</td>
      <td>478</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5oxp">5OXP</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEDKGK</span><span class="topo-inside">TFFGQPLGLSTLF</span><span class="topo-membrane">MTEMWERFSYYGMRAIL</span><span class="topo-outside">LYYMWFLISTGDLHITRATAAS</span><span class="topo-membrane">IMAIYASMVYLSGTIG</span><span class="topo-inside">GFVADRIIGARPA</span><span class="topo-membrane">VFWGGVLIMLGHIVLAL</span><span class="topo-outside">PFGASA</span><span class="topo-membrane">LFGSIILIII</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GTGFLKP</span><span class="topo-inside">NVSTLVGTLYD</span><span class="topo-unknown">EH</span><span class="topo-inside">DRRRDAGFSIF</span><span class="topo-membrane">VFGINLGAFIAPLIVG</span><span class="topo-outside">AAQEAAGYHVA</span><span class="topo-membrane">FSLAAIGMFIGLLVYYF</span><span class="topo-inside">GGKKTLDPHYLRPTDPLAPEEVKPLLVK</span><span class="topo-membrane">VSLAVAGFIAIIVVMNL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">V</span><span class="topo-outside">GWNSLP</span><span class="topo-membrane">AYINLLTIVAIAIPVFY</span><span class="topo-inside">FAWMI</span><span class="topo-unknown">SSVKVT</span><span class="topo-inside">STEHLRVVSYI</span><span class="topo-membrane">PLFIAAVLFWAIEEQGSVVLA</span><span class="topo-outside">TFAAERVDSSWFPVS</span><span class="topo-membrane">WFQSLNPLFIMLYTPFF</span><span class="topo-inside">AWLWTAW</span><span class="topo-unknown">KKN</span><span class="topo-inside">QPSSPT</span><span class="topo-membrane">KFAVG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LMFAGLSFLLM</span><span class="topo-outside">AIPGALYGTSGKVSPL</span><span class="topo-membrane">WLVGSWALVILGEMLISPVG</span><span class="topo-inside">LSV</span><span class="topo-unknown">TTKLAPKAF</span><span class="topo-inside">NSQMMS</span><span class="topo-membrane">MWFLSSSVGSALNAQLV</span><span class="topo-outside">TLYNAKSEVAYF</span><span class="topo-membrane">SYFGLGSVVLGIVLVFL</span><span class="topo-inside">SKRIQGLMQ</span></span>
<span class="topo-ruler">       490</span>
<span class="topo-line"><span class="topo-inside">GVEAENLY</span><span class="topo-unknown">FQ</span></span>
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
      <td>7</td>
      <td>19</td>
      <td>7</td>
      <td>19</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>36</td>
      <td>20</td>
      <td>36</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>37</td>
      <td>58</td>
      <td>37</td>
      <td>58</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>74</td>
      <td>59</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>87</td>
      <td>75</td>
      <td>87</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>104</td>
      <td>88</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>110</td>
      <td>105</td>
      <td>110</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>111</td>
      <td>127</td>
      <td>111</td>
      <td>127</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>128</td>
      <td>138</td>
      <td>128</td>
      <td>138</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>151</td>
      <td>141</td>
      <td>151</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>167</td>
      <td>152</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>168</td>
      <td>178</td>
      <td>168</td>
      <td>178</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>195</td>
      <td>179</td>
      <td>195</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>223</td>
      <td>196</td>
      <td>223</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>224</td>
      <td>241</td>
      <td>224</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>242</td>
      <td>247</td>
      <td>242</td>
      <td>247</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>264</td>
      <td>248</td>
      <td>264</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>265</td>
      <td>269</td>
      <td>265</td>
      <td>269</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>276</td>
      <td>286</td>
      <td>276</td>
      <td>286</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>307</td>
      <td>287</td>
      <td>307</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>308</td>
      <td>322</td>
      <td>308</td>
      <td>322</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>339</td>
      <td>323</td>
      <td>339</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>340</td>
      <td>346</td>
      <td>340</td>
      <td>346</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>350</td>
      <td>355</td>
      <td>350</td>
      <td>355</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>356</td>
      <td>371</td>
      <td>356</td>
      <td>371</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>372</td>
      <td>387</td>
      <td>372</td>
      <td>387</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>388</td>
      <td>407</td>
      <td>388</td>
      <td>407</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>408</td>
      <td>410</td>
      <td>408</td>
      <td>410</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>420</td>
      <td>425</td>
      <td>420</td>
      <td>425</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>426</td>
      <td>442</td>
      <td>426</td>
      <td>442</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>443</td>
      <td>454</td>
      <td>443</td>
      <td>454</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>455</td>
      <td>471</td>
      <td>455</td>
      <td>471</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>472</td>
      <td>488</td>
      <td>472</td>
      <td>488</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5oxq">5OXQ</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEDKG</span><span class="topo-inside">KTFFGQPLGL</span><span class="topo-membrane">STLFMTEMWERFSYYGMRAIL</span><span class="topo-outside">LYYMWFLISTGDLHITRATAA</span><span class="topo-membrane">SIMAIYASMVYLSGTIGGFVA</span><span class="topo-inside">DRI</span><span class="topo-membrane">IGARPAVFWGGVLIMLGHIVLA</span><span class="topo-outside">LPFGASA</span><span class="topo-membrane">LFGSIILIII</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GTGFLKPNVS</span><span class="topo-inside">TLVGTLYDEHDRRRDAGF</span><span class="topo-membrane">SIFVFGINLGAFIAPLIVG</span><span class="topo-outside">AAQEAAGYHVA</span><span class="topo-membrane">FSLAAIGMFIGLLVYYFGGK</span><span class="topo-inside">KTLDPHYLRPTDPLAPEEVKPL</span><span class="topo-membrane">LVKVSLAVAGFIAIIVVMNL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">V</span><span class="topo-outside">GWNSLP</span><span class="topo-membrane">AYINLLTIVAIAIPVFYFAW</span><span class="topo-inside">M</span><span class="topo-unknown">ISSVKVTSTEHLR</span><span class="topo-inside">VV</span><span class="topo-membrane">SYIPLFIAAVLFWAIEEQGSVVLA</span><span class="topo-outside">TFAAERVDSSWFPVS</span><span class="topo-membrane">WFQSLNPLFIMLYTPFFAWL</span><span class="topo-inside">WTAWKKNQPSS</span><span class="topo-membrane">PTKFAVG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LMFAGLSFLLMA</span><span class="topo-outside">IPGALYGTSGKVSPL</span><span class="topo-membrane">WLVGSWALVILGEMLISPVGL</span><span class="topo-inside">SVTTKL</span><span class="topo-unknown">APKAF</span><span class="topo-inside">NSQ</span><span class="topo-membrane">MMSMWFLSSSVGSALNAQLV</span><span class="topo-outside">TLYNAKSEVAY</span><span class="topo-membrane">FSYFGLGSVVLGIVLVFLS</span><span class="topo-inside">KRIQGL</span><span class="topo-unknown">MQ</span></span>
<span class="topo-ruler">       490</span>
<span class="topo-line"><span class="topo-unknown">GVEAENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (31 regions)</summary>
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
      <td>6</td>
      <td>15</td>
      <td>6</td>
      <td>15</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>36</td>
      <td>16</td>
      <td>36</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>37</td>
      <td>57</td>
      <td>37</td>
      <td>57</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>78</td>
      <td>58</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>81</td>
      <td>79</td>
      <td>81</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>103</td>
      <td>82</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>104</td>
      <td>110</td>
      <td>104</td>
      <td>110</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>111</td>
      <td>130</td>
      <td>111</td>
      <td>130</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>131</td>
      <td>148</td>
      <td>131</td>
      <td>148</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>167</td>
      <td>149</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>168</td>
      <td>178</td>
      <td>168</td>
      <td>178</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>198</td>
      <td>179</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>220</td>
      <td>199</td>
      <td>220</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>241</td>
      <td>221</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>242</td>
      <td>247</td>
      <td>242</td>
      <td>247</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>267</td>
      <td>248</td>
      <td>267</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>268</td>
      <td>268</td>
      <td>268</td>
      <td>268</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>283</td>
      <td>282</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>307</td>
      <td>284</td>
      <td>307</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>308</td>
      <td>322</td>
      <td>308</td>
      <td>322</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>342</td>
      <td>323</td>
      <td>342</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>343</td>
      <td>353</td>
      <td>343</td>
      <td>353</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>354</td>
      <td>372</td>
      <td>354</td>
      <td>372</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>373</td>
      <td>387</td>
      <td>373</td>
      <td>387</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>388</td>
      <td>408</td>
      <td>388</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>414</td>
      <td>409</td>
      <td>414</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>420</td>
      <td>422</td>
      <td>420</td>
      <td>422</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>423</td>
      <td>442</td>
      <td>423</td>
      <td>442</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>443</td>
      <td>453</td>
      <td>443</td>
      <td>453</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>454</td>
      <td>472</td>
      <td>454</td>
      <td>472</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>473</td>
      <td>478</td>
      <td>473</td>
      <td>478</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6eia">6EIA</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEDK</span><span class="topo-inside">GKTFFGQPLGL</span><span class="topo-membrane">STLFMTEMWERFSYYGMRA</span><span class="topo-outside">ILLYYMWFLISTGDLHITRATAA</span><span class="topo-membrane">SIMAIYASMVYLSGTIGGFVA</span><span class="topo-inside">DRI</span><span class="topo-membrane">IGARPAVFWGGVLIMLGHIV</span><span class="topo-outside">LALPFGASALF</span><span class="topo-membrane">GSIILIII</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GTGFLKPNVS</span><span class="topo-inside">TLVGTLYDEHDRRRDAGF</span><span class="topo-membrane">SIFVFGINLGAFIAPLIV</span><span class="topo-outside">GAAQEAAGYHVAF</span><span class="topo-membrane">SLAAIGMFIGLLVYYFGGK</span><span class="topo-inside">KTLDPHYLRPTDPLAPEEVKPL</span><span class="topo-membrane">LVKVSLAVAGFIAIIVVMNL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">V</span><span class="topo-outside">GWNSLP</span><span class="topo-membrane">AYINLLTIVAIAIPVFYFAW</span><span class="topo-inside">MISS</span><span class="topo-unknown">VKVTS</span><span class="topo-inside">TEHLRVVSY</span><span class="topo-membrane">IPLFIAAVLFWAIEEQGSVVLA</span><span class="topo-outside">TFAAERVDSSWFPVS</span><span class="topo-membrane">WFQSLNPLFIMLYTPFFAWL</span><span class="topo-inside">WTAWKKNQPSSP</span><span class="topo-membrane">TKFAVG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LMFAGLSFLLMAI</span><span class="topo-outside">PGALYGTSGKVSPL</span><span class="topo-membrane">WLVGSWALVILGEMLISPVGL</span><span class="topo-inside">SVTTKL</span><span class="topo-unknown">APKAF</span><span class="topo-inside">NSQMMS</span><span class="topo-membrane">MWFLSSSVGSALNAQLV</span><span class="topo-outside">TLYNAKSEVAY</span><span class="topo-membrane">FSYFGLGSVVLGIVLVFLS</span><span class="topo-inside">KRIQGL</span><span class="topo-unknown">MQ</span></span>
<span class="topo-ruler">       490</span>
<span class="topo-line"><span class="topo-unknown">GVEAENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (31 regions)</summary>
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
      <td>15</td>
      <td>5</td>
      <td>15</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>34</td>
      <td>16</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>57</td>
      <td>35</td>
      <td>57</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>78</td>
      <td>58</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>81</td>
      <td>79</td>
      <td>81</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>101</td>
      <td>82</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>112</td>
      <td>102</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>130</td>
      <td>113</td>
      <td>130</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>131</td>
      <td>148</td>
      <td>131</td>
      <td>148</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>166</td>
      <td>149</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>179</td>
      <td>167</td>
      <td>179</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>180</td>
      <td>198</td>
      <td>180</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>220</td>
      <td>199</td>
      <td>220</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>241</td>
      <td>221</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>242</td>
      <td>247</td>
      <td>242</td>
      <td>247</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>267</td>
      <td>248</td>
      <td>267</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>268</td>
      <td>271</td>
      <td>268</td>
      <td>271</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>285</td>
      <td>277</td>
      <td>285</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>307</td>
      <td>286</td>
      <td>307</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>308</td>
      <td>322</td>
      <td>308</td>
      <td>322</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>342</td>
      <td>323</td>
      <td>342</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>343</td>
      <td>354</td>
      <td>343</td>
      <td>354</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>355</td>
      <td>373</td>
      <td>355</td>
      <td>373</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>387</td>
      <td>374</td>
      <td>387</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>388</td>
      <td>408</td>
      <td>388</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>414</td>
      <td>409</td>
      <td>414</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>420</td>
      <td>425</td>
      <td>420</td>
      <td>425</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>426</td>
      <td>442</td>
      <td>426</td>
      <td>442</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>443</td>
      <td>453</td>
      <td>443</td>
      <td>453</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>454</td>
      <td>472</td>
      <td>454</td>
      <td>472</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>473</td>
      <td>478</td>
      <td>473</td>
      <td>478</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Extracellular gate stabilized by conserved salt bridge interactions

Two salt bridge interactions stabilize the extracellular gate in PepT_St: Arg53(H1)-Glu312(H7)
at ~2.9 A and Arg33(H1)-Glu300(H7) at ~3.8 A. The Arg53-Glu312 salt bridge is distal from
the peptide-binding site and plays a supportive role during transport (R53A reduces uptake
by 50%, E312A by 70%). The Arg33-Glu300 salt bridge is positioned next to the peptide-binding
site and is critical for transport (E300A abolishes both proton-driven and counterflow
transport). These interactions orchestrate alternating access within the POT family.

### Proton binding and the ExxERFxYY motif on helix H1

A conserved ExxERFxYY motif on helix H1 is important for proton binding during transport.
Glu25 and Arg26 form a salt bridge (~2.5-2.8 A) close to Glu22. Alanine mutants of this
motif showed measurable uptake only under counterflow conditions, indicating proton binding
is required for transport. Tyr29 retained 75% of WT uptake levels and additionally
functions in determining peptide specificity. Lys126 on helix H4 is positioned close to
the motif and may regulate proton coupling.

### Conserved tyrosines determine peptide binding affinities

The peptide-binding site contains three prominent tyrosine side chains: Tyr29 and Tyr30
from helix H1, and Tyr68 from helix H2. The Tyr29Phe mutant showed decreased affinity
for tri-alanine (IC50 1.4 mM vs 0.4 mM WT) while retaining affinity for di-Glu. The
Tyr68Phe mutant showed decreased affinity for di-Glu (IC50 1.63 mM vs 0.56 mM WT) while
retaining affinity for tri-alanine. The Tyr29Ala and Tyr68Ala mutants lost ability to
transport these peptides altogether while retaining affinity for di-Phe and di-Ala.

### Intracellular gate opening via hinge-like movement in helices H10 and H11

Comparing the inward open PepT_St structure with the occluded PepT_So structure reveals
that the intracellular gate opens through a hinge-like movement at the apex of the H10-H11
helix hairpin, specifically at Gly407 (H10) and Trp427 (H11). The cytoplasmic halves of
H7, H10, and H11 swing away from helices H4-H5, moving ~13 A from their occluded positions.
This opens the peptide-binding site to the intracellular side of the membrane without
requiring movement of the entire H10-H11 helix hairpin.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/pot-family/">POT Family (Proton-Dependent Oligopeptide Transporters)</a> — PepT_St is a member of the POT family
- <a href="/xray-mp-wiki/concepts/protein-families/mfs-transporter/">Major Facilitator Superfamily</a> — POT family is a subgroup of MFS transporters
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — POTs transport via alternating access between inward-open and outward-open states
- <a href="/xray-mp-wiki/proteins/mfs-transporters/pept-so/">PepT_So Oligopeptide Transporter</a> — Another POT family member with reported crystal structure; key comparison for alternating access
- <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG 400</a> — Cryoprotectant used in PepT_St crystallization
- <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine</a> — Used for anomalous phasing in PepT_St structure determination
- <a href="/xray-mp-wiki/reagents/additives/mercury/">Mercury(II) Chloride</a> — Heavy atom derivative used for MIRAS phasing
- <a href="/xray-mp-wiki/methods/structure-determination/miras/">Multiple Isomorphous Replacement with Anomalous Scattering (MIRAS)</a> — Phasing method used to solve the PepT_St structure
- <a href="/xray-mp-wiki/proteins/mfs-transporters/pept-so2/">PepT_So2 Oligopeptide Transporter</a> — Another POT family member from Shewanella oneidensis, inward open conformation with substrate
- <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a> — Additive used in purification or crystallization buffers
