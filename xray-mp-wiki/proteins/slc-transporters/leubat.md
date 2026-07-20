---
title: "LeuBAT (LeuT Engineered for Antidepressant Pharmacology)"
created: 2026-06-08
updated: 2026-07-13
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature12648]
verified: agent
uniprot_id: O67854
---

# LeuBAT (LeuT Engineered for Antidepressant Pharmacology)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/O67854">UniProt: O67854</a>

<span class="expr-badge">Aquifex aeolicus</span>

## Overview

LeuBAT is an engineered mutant of the bacterial leucine transporter [LEUT](/xray-mp-wiki/proteins/enzymes/leut/) from Aquifex aeolicus that harbours human biogenic amine transporter (BAT)-like pharmacology. By introducing 13 mutations around the primary binding pocket, LeuBAT binds the SSRI [Sertraline](/xray-mp-wiki/reagents/ligands/sertraline/) with a Kd of 18 nM and displays high-affinity binding to a range of SSRIs, SNRIs, and TCAs. Twelve crystal structures of LeuBAT in complex with four classes of antidepressants reveal that chemically diverse inhibitors share a remarkably similar binding mode in which they straddle transmembrane helix 3, wedge between TM3/TM8 and TM1/TM6, and lock the transporter in a sodium- and chloride-bound outward-facing open conformation.

## Publications

### doi/10.1038##nature12648

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4mm4">4MM4</a></td>
      <td></td>
      <td></td>
      <td>LeuBAT Delta13 mutant with BAT-like pharmacology in complex with antidepressants</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/sertraline/">Sertraline</a>, <a href="/xray-mp-wiki/reagents/ligands/paroxetine/">Paroxetine</a>, <a href="/xray-mp-wiki/reagents/ligands/fluoxetine/">Fluoxetine</a>, <a href="/xray-mp-wiki/reagents/ligands/fluvoxamine/">Fluvoxamine</a>, <a href="/xray-mp-wiki/reagents/ligands/duloxetine/">Duloxetine</a>, <a href="/xray-mp-wiki/reagents/ligands/desvenlafaxine/">Desvenlafaxine</a>, <a href="/xray-mp-wiki/reagents/ligands/clomipramine/">CMI</a>, <a href="/xray-mp-wiki/reagents/ligands/mazindol/">Mazindol</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli, LeuBAT mutants expressed and purified as for wild-type [LEUT](/xray-mp-wiki/proteins/enzymes/leut/)
- **Construct**: Delta13 LeuBAT with 13 mutations: L9S, I17A, L25A, A50S, V33I, N21S, A22S, T254S, S256G, I359G, Q250L, A53D, W6L (and other mutations enabling BAT-like pharmacology)

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
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>IMAC</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0 250 mM NaCl + 1% Lauryl <a href="/xray-mp-wiki/reagents/additives/maltose/">Maltose</a> Neopentyl Glycol (MNG-3)</td>
      <td>Cell membranes solubilized; protein purified by IMAC in 0.02% MNG-3</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td>--</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0 150 mM NaCl 40 mM <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a> + 40 mM <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a></td>
      <td>Buffer exchanged into <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a> for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>LeuBAT at 2.5 mg/ml with saturating <a href="/xray-mp-wiki/reagents/ligands/serotonin/">Serotonin (5-Hydroxytryptamine, 5-HT)</a> or <a href="/xray-mp-wiki/reagents/ligands/mazindol/">Mazindol</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM NaPi pH 7.0 100 mM NaCl 32-34% <a href="/xray-mp-wiki/reagents/additives/peg300/">PEG300</a>; or 100 mM <a href="/xray-mp-wiki/reagents/buffers/glycine/">Glycine</a> pH 9.4 0.1 M Li2SO4 29-31% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in presence of <a href="/xray-mp-wiki/reagents/ligands/serotonin/">Serotonin (5-Hydroxytryptamine, 5-HT)</a> soaked for 1 h in crystallization solution containing antidepressants; 12 crystal structures determined; <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using LeuT-Trp (PDB 3F3A) as search probe</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4mm4">4MM4</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRLG</span><span class="topo-membrane">LILAMAGYAVDLGNFLRFP</span><span class="topo-inside">VQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVASYYVYIESWTLG</span><span class="topo-inside">FAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">KFLVGLVPEPP</span><span class="topo-unknown">PNA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSLF</span><span class="topo-membrane">AYIVFLITMFINVSILI</span><span class="topo-outside">RGISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVI</span><span class="topo-inside">RVFLLETPNGT</span><span class="topo-unknown">AADGLNFLW</span><span class="topo-inside">TPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">PGVW</span><span class="topo-membrane">IAAVGQIFFSLGLGFGVLITF</span><span class="topo-outside">ASYVRKDQDIVLS</span><span class="topo-membrane">GLTAATLNEKASVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKA</span><span class="topo-unknown">GAFNLGF</span><span class="topo-inside">I</span><span class="topo-unknown">TLPAIF</span><span class="topo-inside">SQTAGGTFLGF</span><span class="topo-membrane">LWFFLLFFAGLTSSIAGM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QGMIAFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVM</span><span class="topo-inside">FLNKSLDE</span><span class="topo-membrane">MDFWATGIGVVFFGLTELIIFFW</span><span class="topo-outside">IFG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-outside">RGGIIKVPRI</span><span class="topo-membrane">YYYVMRYITPAFLAVLLVVWA</span><span class="topo-inside">REY</span><span class="topo-unknown">IPKIMEE</span><span class="topo-inside">TH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTVWI</span><span class="topo-membrane">TRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHE</span><span class="topo-unknown">SAGTLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (39 regions)</summary>
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
      <td>13</td>
      <td>5</td>
      <td>13</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>32</td>
      <td>14</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>43</td>
      <td>33</td>
      <td>43</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>63</td>
      <td>44</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>89</td>
      <td>64</td>
      <td>89</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>117</td>
      <td>90</td>
      <td>117</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>118</td>
      <td>131</td>
      <td>118</td>
      <td>131</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>134</td>
      <td>132</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>167</td>
      <td>135</td>
      <td>167</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>184</td>
      <td>168</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>185</td>
      <td>190</td>
      <td>185</td>
      <td>190</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>211</td>
      <td>191</td>
      <td>211</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>212</td>
      <td>222</td>
      <td>212</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>231</td>
      <td>223</td>
      <td>231</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>232</td>
      <td>244</td>
      <td>232</td>
      <td>244</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>245</td>
      <td>265</td>
      <td>245</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>278</td>
      <td>266</td>
      <td>278</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>297</td>
      <td>279</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>317</td>
      <td>298</td>
      <td>317</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>318</td>
      <td>324</td>
      <td>318</td>
      <td>324</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>325</td>
      <td>325</td>
      <td>325</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>331</td>
      <td>326</td>
      <td>331</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>332</td>
      <td>342</td>
      <td>332</td>
      <td>342</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>367</td>
      <td>343</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>377</td>
      <td>368</td>
      <td>377</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>378</td>
      <td>394</td>
      <td>378</td>
      <td>394</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>395</td>
      <td>402</td>
      <td>395</td>
      <td>402</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>403</td>
      <td>425</td>
      <td>403</td>
      <td>425</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>426</td>
      <td>428</td>
      <td>426</td>
      <td>428</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>429</td>
      <td>437</td>
      <td>429</td>
      <td>437</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>438</td>
      <td>447</td>
      <td>438</td>
      <td>447</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>448</td>
      <td>468</td>
      <td>448</td>
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
      <td>478</td>
      <td>472</td>
      <td>478</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>479</td>
      <td>485</td>
      <td>479</td>
      <td>485</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>486</td>
      <td>502</td>
      <td>486</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>511</td>
      <td>503</td>
      <td>511</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>519</td>
      <td>512</td>
      <td>519</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4mm4">4MM4</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRLG</span><span class="topo-membrane">LILAMAGYAVDLGNFLRFP</span><span class="topo-inside">VQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVASYYVYIESWTLG</span><span class="topo-inside">FAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">KFLVGLVPEPP</span><span class="topo-unknown">PNA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSLFA</span><span class="topo-membrane">YIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVI</span><span class="topo-inside">RVFLLETPNGT</span><span class="topo-unknown">AADGLNFLW</span><span class="topo-inside">TPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">PGVW</span><span class="topo-membrane">IAAVGQIFFSLGLGFGVLITF</span><span class="topo-outside">ASYVRKDQDIVLS</span><span class="topo-membrane">GLTAATLNEKASVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKA</span><span class="topo-unknown">GAFNLGF</span><span class="topo-inside">I</span><span class="topo-unknown">TLPAIF</span><span class="topo-inside">SQTAGGTFLGF</span><span class="topo-membrane">LWFFLLFFAGLTSSIAGM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QGMIAFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVM</span><span class="topo-inside">FLNKSLDE</span><span class="topo-membrane">MDFWATGIGVVFFGLTELIIFFW</span><span class="topo-outside">IFG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-outside">RGGIIKVPRI</span><span class="topo-membrane">YYYVMRYITPAFLAVLLVVWA</span><span class="topo-inside">REYIP</span><span class="topo-unknown">KIMEE</span><span class="topo-inside">TH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTVWI</span><span class="topo-membrane">TRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHE</span><span class="topo-unknown">SAGTLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (39 regions)</summary>
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
      <td>13</td>
      <td>5</td>
      <td>13</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>32</td>
      <td>14</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>43</td>
      <td>33</td>
      <td>43</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>63</td>
      <td>44</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>89</td>
      <td>64</td>
      <td>89</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>117</td>
      <td>90</td>
      <td>117</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>118</td>
      <td>131</td>
      <td>118</td>
      <td>131</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>134</td>
      <td>132</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>168</td>
      <td>135</td>
      <td>168</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>169</td>
      <td>185</td>
      <td>169</td>
      <td>185</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>186</td>
      <td>190</td>
      <td>186</td>
      <td>190</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>211</td>
      <td>191</td>
      <td>211</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>212</td>
      <td>222</td>
      <td>212</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>231</td>
      <td>223</td>
      <td>231</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>232</td>
      <td>244</td>
      <td>232</td>
      <td>244</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>245</td>
      <td>265</td>
      <td>245</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>278</td>
      <td>266</td>
      <td>278</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>297</td>
      <td>279</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>317</td>
      <td>298</td>
      <td>317</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>318</td>
      <td>324</td>
      <td>318</td>
      <td>324</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>325</td>
      <td>325</td>
      <td>325</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>331</td>
      <td>326</td>
      <td>331</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>332</td>
      <td>342</td>
      <td>332</td>
      <td>342</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>367</td>
      <td>343</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>377</td>
      <td>368</td>
      <td>377</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>378</td>
      <td>394</td>
      <td>378</td>
      <td>394</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>395</td>
      <td>402</td>
      <td>395</td>
      <td>402</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>403</td>
      <td>425</td>
      <td>403</td>
      <td>425</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>426</td>
      <td>428</td>
      <td>426</td>
      <td>428</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>429</td>
      <td>437</td>
      <td>429</td>
      <td>437</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>438</td>
      <td>447</td>
      <td>438</td>
      <td>447</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>448</td>
      <td>468</td>
      <td>448</td>
      <td>468</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>469</td>
      <td>473</td>
      <td>469</td>
      <td>473</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>474</td>
      <td>478</td>
      <td>474</td>
      <td>478</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>479</td>
      <td>485</td>
      <td>479</td>
      <td>485</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>486</td>
      <td>502</td>
      <td>486</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>511</td>
      <td>503</td>
      <td>511</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>519</td>
      <td>512</td>
      <td>519</td>
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

### Shared binding mode for diverse antidepressants

Despite chemical diversity, all SSRIs ([Sertraline](/xray-mp-wiki/reagents/ligands/sertraline/), [Paroxetine](/xray-mp-wiki/reagents/ligands/paroxetine/), [Fluoxetine](/xray-mp-wiki/reagents/ligands/fluoxetine/), [Fluvoxamine](/xray-mp-wiki/reagents/ligands/fluvoxamine/)), SNRIs ([Duloxetine](/xray-mp-wiki/reagents/ligands/duloxetine/), [Desvenlafaxine](/xray-mp-wiki/reagents/ligands/desvenlafaxine/)), and TCAs ([CMI](/xray-mp-wiki/reagents/ligands/clomipramine/)) bind to the primary orthosteric pocket in a similar orientation. The amine groups are proximal to the carboxyl group of Asp24 and form hydrogen bonds with main-chain carbonyls of Tyr21, Ala22, and Phe253. The halogenated aromatic rings insert into a hydrophobic groove formed by Pro101, Val104, Ala105, Ser356, and Gly359. This common binding mode defines three subsites (A, B, C) within the primary pocket.

### Outward-facing open conformation

All 12 LeuBAT-antidepressant structures adopt an outward-facing open conformation with sodium and chloride ions bound. This contrasts with the LeuT-TCA structures where TCAs bind in the extracellular vestibule. The inhibitors lock the transporter in this conformation, explaining their competitive inhibition mechanism at human BATs versus the non-competitive mechanism seen in wild-type [LEUT](/xray-mp-wiki/proteins/enzymes/leut/).

### Pharmacological validation

LeuBAT was validated as a model for human [SERT](/xray-mp-wiki/proteins/slc-transporters/ssert/) by mutational analysis. Mutations Y21A, D24E, F259Y, and S355T in LeuBAT showed similar effects on [Sertraline](/xray-mp-wiki/reagents/ligands/sertraline/) binding as the homologous mutations (Y95A, D98E, F341Y, S438T) in human [SERT](/xray-mp-wiki/proteins/slc-transporters/ssert/), demonstrated by a linear logKd vs logKi relationship. The pharmacological profile of LeuBAT is a hybrid of human DAT, NET, and [SERT](/xray-mp-wiki/proteins/slc-transporters/ssert/) properties.

### Chloride binding site

The outward-facing open conformation of LeuBAT includes a chloride ion binding site. This is consistent with the chloride dependence of human monoamine transporters and explains why chloride is required for high-affinity inhibitor binding in [SERT](/xray-mp-wiki/proteins/slc-transporters/ssert/).


## Cross-References

- <a href="/xray-mp-wiki/proteins/slc-transporters/d-dat/">Drosophila Dopamine Transporter (dDAT)</a> — Related biogenic amine transporter for comparison
- <a href="/xray-mp-wiki/reagents/ligands/sertraline/">Sertraline</a> — SSRI co-crystallized with LeuBAT
- <a href="/xray-mp-wiki/reagents/detergents/lmng/">Lauryl Maltose Neopentyl Glycol (LMNG)</a> — Detergent used for solubilization and purification
- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr-active-conformation/">GPCR Active Conformation</a> — LeuBAT represents outward-facing open conformation relevant to transporter mechanism
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/enzymes/leut/">LEUT</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/slc-transporters/ssert/">SERT</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/maltose/">Maltose</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg300/">PEG300</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a> — Additive used in purification or crystallization buffers
