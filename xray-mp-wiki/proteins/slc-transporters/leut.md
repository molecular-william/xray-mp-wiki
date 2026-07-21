---
title: "LeuT Amino Acid Transporter from Aquifex aeolicus"
created: 2026-06-16
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1038##nature03978, doi/10.1038##nature06038, doi/10.1038##nature12179, doi/10.1038##nature10737, doi/10.1038##ncomms11673, doi/10.1021##bi101148w, doi/10.1038##nsmb.2215, doi/10.1038##s41467-020-14735-w, doi/10.1073##pnas.0811322106, doi/10.1126##science.1147614, doi/10.1126##science.1166777]
verified: agent
uniprot_id: O67854
---

# LeuT Amino Acid Transporter from Aquifex aeolicus


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/O67854">UniProt: O67854</a>

<span class="expr-badge">Aquifex aeolicus</span>

## Overview

LeuT is a bacterial amino acid transporter from Aquifex aeolicus that belongs to the Neurotransmitter/Sodium Symporter (NSS) family. It was the first crystal structure of an NSS family member, revealing the general architecture of Na+-coupled neurotransmitter transporters. LeuT mediates the Na+-dependent uptake of L-leucine and has served as the primary structural template for understanding the entire NSS family, including human serotonin, dopamine, and GABA transporters. In 2007, the structure of LeuT in complex with tricyclic antidepressants (TCAs) revealed the molecular basis of noncompetitive inhibition: TCAs bind in the extracellular-facing vestibule about 11 A above the substrate and two sodium ions, stabilizing the extracellular gate in a closed conformation and slowing substrate release by as much as 700-fold.

## Publications

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1038/nature03978 (1 structure, 2 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2a65">2A65</a></td>
      <td>1.65</td>
      <td>C2</td>
      <td>LeuT from A. aeolicus, residues 5-133 and 135-513</td>
      <td>L-leucine, Na+ (2 ions), Cl-</td>
    </tr>
  </tbody>
</table>

**Purification:**

- **Expression system**: E. coli C41
- **Expression construct**: LeuT from A. aeolicus with C-terminal His-tag
- **Tag info**: C-terminal His-tag, removed by thrombin cleavage

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
      <td>Fermentation</td>
      <td>—</td>
      <td>Terrific broth</td>
      <td>Induced with 0.1 mM <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> at 20 C for 20 h</td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td>Cell lysis and membrane fractionation</td>
      <td>—</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Membranes isolated from disrupted C41 cells</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td>20 mM Tris-HCl pH 8.0, 190 mM NaCl, 10 mM KCl, 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 1 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Membranes solubilized with 40 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Thrombin digestion and SEC</td>
      <td>Size-exclusion chromatography</td>
      <td>—</td>
      <td>20 mM Tris-HCl pH 8.0, 190 mM NaCl, 10 mM KCl + 40 mM beta-<a href="/xray-mp-wiki/reagents/detergents/og/">[OG</a>](/xray-mp-wiki/reagents/detergents/n-octyl-beta-d-glucopyranoside/)</td>
      <td>Thrombin cleavage of C-terminal His-tag before <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
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
      <td>LeuT in 40 mM beta-<a href="/xray-mp-wiki/reagents/detergents/n-octyl-beta-d-glucopyranoside/">OG</a>, ~7 mg/ml</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M HEPES-NaOH pH 7.0, 18-22% PEG 550 MME, 0.2 M NaCl</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>18</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Cryoprotected with 35% PEG 550 MME and 40 mM beta-<a href="/xray-mp-wiki/reagents/detergents/n-octyl-beta-d-glucopyranoside/">OG</a>. Space group C2.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>vapor-diffusion</td>
    </tr>
    <tr>
      <td>Variant</td>
      <td>hanging-drop</td>
    </tr>
    <tr>
      <td>pH</td>
      <td>7.0</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>18 C</td>
    </tr>
    <tr>
      <td>Components</td>
      <td>- Peg: 18-22 % [precipitant] (PEG 550 MME)  
- Sodium Chloride: 0.2 M [salt]</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2a65">2A65</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPPP</span><span class="topo-unknown">NA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGT</span><span class="topo-unknown">AADGLNFLW</span><span class="topo-inside">TPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITY</span><span class="topo-outside">ASYVRKDQDIV</span><span class="topo-membrane">LSGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFI</span><span class="topo-unknown">TLPAIF</span><span class="topo-inside">SQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-outside">RGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EY</span><span class="topo-unknown">IPKIME</span><span class="topo-inside">ETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHESAGTL</span><span class="topo-unknown">VPR</span></span>
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
      <td>12</td>
      <td>5</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>32</td>
      <td>13</td>
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
      <td>124</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>132</td>
      <td>125</td>
      <td>132</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>134</td>
      <td>133</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>222</td>
      <td>213</td>
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
      <td>241</td>
      <td>232</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>265</td>
      <td>242</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>276</td>
      <td>266</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>297</td>
      <td>277</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>325</td>
      <td>298</td>
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
      <td>339</td>
      <td>332</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
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
      <td>396</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>426</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>427</td>
      <td>428</td>
      <td>427</td>
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
      <td>444</td>
      <td>438</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>469</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>471</td>
      <td>470</td>
      <td>471</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>477</td>
      <td>472</td>
      <td>477</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>478</td>
      <td>483</td>
      <td>478</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>516</td>
      <td>503</td>
      <td>601</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>517</td>
      <td>519</td>
      <td>602</td>
      <td>604</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2a65">2A65</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPPP</span><span class="topo-unknown">NA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGT</span><span class="topo-unknown">AADGLNFLW</span><span class="topo-inside">TPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITY</span><span class="topo-outside">ASYVRKDQDIV</span><span class="topo-membrane">LSGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFI</span><span class="topo-unknown">TLPAIF</span><span class="topo-inside">SQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-outside">RGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EY</span><span class="topo-unknown">IPKIME</span><span class="topo-inside">ETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHESAGTL</span><span class="topo-unknown">VPR</span></span>
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
      <td>12</td>
      <td>5</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>32</td>
      <td>13</td>
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
      <td>124</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>132</td>
      <td>125</td>
      <td>132</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>134</td>
      <td>133</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>222</td>
      <td>213</td>
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
      <td>241</td>
      <td>232</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>265</td>
      <td>242</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>276</td>
      <td>266</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>297</td>
      <td>277</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>325</td>
      <td>298</td>
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
      <td>339</td>
      <td>332</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
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
      <td>396</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>426</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>427</td>
      <td>428</td>
      <td>427</td>
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
      <td>444</td>
      <td>438</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>469</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>471</td>
      <td>470</td>
      <td>471</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>477</td>
      <td>472</td>
      <td>477</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>478</td>
      <td>483</td>
      <td>478</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>516</td>
      <td>503</td>
      <td>601</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>517</td>
      <td>519</td>
      <td>602</td>
      <td>604</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1038##nature06038 (1 structure, 8 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2qei">2QEI</a></td>
      <td>1.7-1.9</td>
      <td>—</td>
      <td>LeuT-leucine-sodium in complex with clomipramine</td>
      <td>L-leucine, Na+ (2 ions), clomipramine</td>
    </tr>
  </tbody>
</table>

**Purification:**

- **Expression system**: E. coli
- **Expression construct**: LeuT from A. aeolicus

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
      <td>Expression and purification</td>
      <td>As described in doi/10.1038##nature03978</td>
      <td>—</td>
      <td></td>
      <td>LeuT expressed and purified as previously described for cocrystallization with TCAs</td>
    </tr>
    <tr>
      <td>TCA addition</td>
      <td>Incubation with inhibitor</td>
      <td>—</td>
      <td></td>
      <td>TCAs added to final concentration of 10 mM, incubated on ice for 15 min before crystallization trials</td>
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
      <td>LeuT-leucine-sodium with 10 mM TCA</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>17-22% PEG 550 MME, 100 mM HEPES-NaOH pH 7-7.5, 200 mM NaCl</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>18</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>7-10 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Gradually increased starting PEG 550 MME to 35%</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Cocrystallization of LeuT with <a href="/xray-mp-wiki/reagents/ligands/clomipramine/">CMI</a>, <a href="/xray-mp-wiki/reagents/ligands/desipramine/">Desipramine</a>, or <a href="/xray-mp-wiki/reagents/ligands/imipramine/">Imipramine</a>. Also prepared LeuT-alanine-<a href="/xray-mp-wiki/reagents/ligands/clomipramine/">CMI</a> complex with 100 mM alanine in all buffers.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>vapor-diffusion</td>
    </tr>
    <tr>
      <td>Variant</td>
      <td>hanging-drop</td>
    </tr>
    <tr>
      <td>pH</td>
      <td>7</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>18 C</td>
    </tr>
    <tr>
      <td>Components</td>
      <td>- Peg: 17-22 % [precipitant] (PEG 550 MME)  
- Sodium Chloride: 200 mM [salt]</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2qei">2QEI</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEV</span><span class="topo-outside">KREHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPPP</span><span class="topo-unknown">NA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGT</span><span class="topo-unknown">AADGLNFL</span><span class="topo-inside">WTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITYA</span><span class="topo-outside">SYVRKDQDIV</span><span class="topo-membrane">LSGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFI</span><span class="topo-unknown">TLPAIF</span><span class="topo-inside">SQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-outside">RGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIPKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHESAGTLA</span><span class="topo-unknown">PR</span></span>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>12</td>
      <td>4</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>32</td>
      <td>13</td>
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
      <td>124</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>132</td>
      <td>125</td>
      <td>132</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>134</td>
      <td>133</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>222</td>
      <td>213</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>230</td>
      <td>223</td>
      <td>230</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>231</td>
      <td>241</td>
      <td>231</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>266</td>
      <td>242</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>276</td>
      <td>267</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>297</td>
      <td>277</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>325</td>
      <td>298</td>
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
      <td>339</td>
      <td>332</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
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
      <td>396</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>426</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>427</td>
      <td>428</td>
      <td>427</td>
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
      <td>444</td>
      <td>438</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>469</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>483</td>
      <td>470</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>517</td>
      <td>503</td>
      <td>601</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>518</td>
      <td>519</td>
      <td>602</td>
      <td>603</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2qei">2QEI</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEV</span><span class="topo-outside">KREHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPPP</span><span class="topo-unknown">NA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGT</span><span class="topo-unknown">AADGLNFL</span><span class="topo-inside">WTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITYA</span><span class="topo-outside">SYVRKDQDIV</span><span class="topo-membrane">LSGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFI</span><span class="topo-unknown">TLPAIF</span><span class="topo-inside">SQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-outside">RGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIPKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHESAGTLA</span><span class="topo-unknown">PR</span></span>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>12</td>
      <td>4</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>32</td>
      <td>13</td>
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
      <td>124</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>132</td>
      <td>125</td>
      <td>132</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>134</td>
      <td>133</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>222</td>
      <td>213</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>230</td>
      <td>223</td>
      <td>230</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>231</td>
      <td>241</td>
      <td>231</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>266</td>
      <td>242</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>276</td>
      <td>267</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>297</td>
      <td>277</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>325</td>
      <td>298</td>
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
      <td>339</td>
      <td>332</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
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
      <td>396</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>426</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>427</td>
      <td>428</td>
      <td>427</td>
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
      <td>444</td>
      <td>438</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>469</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>483</td>
      <td>470</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>517</td>
      <td>503</td>
      <td>601</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>518</td>
      <td>519</td>
      <td>602</td>
      <td>603</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2qei">2QEI</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEV</span><span class="topo-outside">KREHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPPP</span><span class="topo-unknown">NA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGT</span><span class="topo-unknown">AADGLNFL</span><span class="topo-inside">WTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITYA</span><span class="topo-outside">SYVRKDQDIV</span><span class="topo-membrane">LSGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFI</span><span class="topo-unknown">TLPAIF</span><span class="topo-inside">SQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-outside">RGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIPKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHESAGTLA</span><span class="topo-unknown">PR</span></span>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>12</td>
      <td>4</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>32</td>
      <td>13</td>
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
      <td>124</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>132</td>
      <td>125</td>
      <td>132</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>134</td>
      <td>133</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>222</td>
      <td>213</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>230</td>
      <td>223</td>
      <td>230</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>231</td>
      <td>241</td>
      <td>231</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>266</td>
      <td>242</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>276</td>
      <td>267</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>297</td>
      <td>277</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>325</td>
      <td>298</td>
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
      <td>339</td>
      <td>332</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
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
      <td>396</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>426</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>427</td>
      <td>428</td>
      <td>427</td>
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
      <td>444</td>
      <td>438</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>469</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>483</td>
      <td>470</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>517</td>
      <td>503</td>
      <td>601</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>518</td>
      <td>519</td>
      <td>602</td>
      <td>603</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2qei">2QEI</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEV</span><span class="topo-outside">KREHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPPP</span><span class="topo-unknown">NA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGT</span><span class="topo-unknown">AADGLNFL</span><span class="topo-inside">WTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITYA</span><span class="topo-outside">SYVRKDQDIV</span><span class="topo-membrane">LSGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFI</span><span class="topo-unknown">TLPAIF</span><span class="topo-inside">SQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-outside">RGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIPKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHESAGTLA</span><span class="topo-unknown">PR</span></span>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>12</td>
      <td>4</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>32</td>
      <td>13</td>
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
      <td>124</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>132</td>
      <td>125</td>
      <td>132</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>134</td>
      <td>133</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>222</td>
      <td>213</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>230</td>
      <td>223</td>
      <td>230</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>231</td>
      <td>241</td>
      <td>231</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>266</td>
      <td>242</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>276</td>
      <td>267</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>297</td>
      <td>277</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>325</td>
      <td>298</td>
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
      <td>339</td>
      <td>332</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
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
      <td>396</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>426</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>427</td>
      <td>428</td>
      <td>427</td>
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
      <td>444</td>
      <td>438</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>469</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>483</td>
      <td>470</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>517</td>
      <td>503</td>
      <td>601</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>518</td>
      <td>519</td>
      <td>602</td>
      <td>603</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2qei">2QEI</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEV</span><span class="topo-outside">KREHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPPP</span><span class="topo-unknown">NA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGT</span><span class="topo-unknown">AADGLNFL</span><span class="topo-inside">WTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITYA</span><span class="topo-outside">SYVRKDQDIV</span><span class="topo-membrane">LSGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFI</span><span class="topo-unknown">TLPAIF</span><span class="topo-inside">SQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-outside">RGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIPKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHESAGTLA</span><span class="topo-unknown">PR</span></span>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>12</td>
      <td>4</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>32</td>
      <td>13</td>
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
      <td>124</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>132</td>
      <td>125</td>
      <td>132</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>134</td>
      <td>133</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>222</td>
      <td>213</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>230</td>
      <td>223</td>
      <td>230</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>231</td>
      <td>241</td>
      <td>231</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>266</td>
      <td>242</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>276</td>
      <td>267</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>297</td>
      <td>277</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>325</td>
      <td>298</td>
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
      <td>339</td>
      <td>332</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
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
      <td>396</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>426</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>427</td>
      <td>428</td>
      <td>427</td>
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
      <td>444</td>
      <td>438</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>469</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>483</td>
      <td>470</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>517</td>
      <td>503</td>
      <td>601</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>518</td>
      <td>519</td>
      <td>602</td>
      <td>603</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2qei">2QEI</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEV</span><span class="topo-outside">KREHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPPP</span><span class="topo-unknown">NA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGT</span><span class="topo-unknown">AADGLNFL</span><span class="topo-inside">WTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITYA</span><span class="topo-outside">SYVRKDQDIV</span><span class="topo-membrane">LSGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFI</span><span class="topo-unknown">TLPAIF</span><span class="topo-inside">SQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-outside">RGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIPKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHESAGTLA</span><span class="topo-unknown">PR</span></span>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>12</td>
      <td>4</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>32</td>
      <td>13</td>
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
      <td>124</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>132</td>
      <td>125</td>
      <td>132</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>134</td>
      <td>133</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>222</td>
      <td>213</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>230</td>
      <td>223</td>
      <td>230</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>231</td>
      <td>241</td>
      <td>231</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>266</td>
      <td>242</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>276</td>
      <td>267</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>297</td>
      <td>277</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>325</td>
      <td>298</td>
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
      <td>339</td>
      <td>332</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
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
      <td>396</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>426</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>427</td>
      <td>428</td>
      <td>427</td>
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
      <td>444</td>
      <td>438</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>469</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>483</td>
      <td>470</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>517</td>
      <td>503</td>
      <td>601</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>518</td>
      <td>519</td>
      <td>602</td>
      <td>603</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2qei">2QEI</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEV</span><span class="topo-outside">KREHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPPP</span><span class="topo-unknown">NA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGT</span><span class="topo-unknown">AADGLNFL</span><span class="topo-inside">WTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITYA</span><span class="topo-outside">SYVRKDQDIV</span><span class="topo-membrane">LSGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFI</span><span class="topo-unknown">TLPAIF</span><span class="topo-inside">SQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-outside">RGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIPKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHESAGTLA</span><span class="topo-unknown">PR</span></span>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>12</td>
      <td>4</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>32</td>
      <td>13</td>
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
      <td>124</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>132</td>
      <td>125</td>
      <td>132</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>134</td>
      <td>133</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>222</td>
      <td>213</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>230</td>
      <td>223</td>
      <td>230</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>231</td>
      <td>241</td>
      <td>231</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>266</td>
      <td>242</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>276</td>
      <td>267</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>297</td>
      <td>277</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>325</td>
      <td>298</td>
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
      <td>339</td>
      <td>332</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
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
      <td>396</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>426</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>427</td>
      <td>428</td>
      <td>427</td>
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
      <td>444</td>
      <td>438</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>469</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>483</td>
      <td>470</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>517</td>
      <td>503</td>
      <td>601</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>518</td>
      <td>519</td>
      <td>602</td>
      <td>603</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2qei">2QEI</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEV</span><span class="topo-outside">KREHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPPP</span><span class="topo-unknown">NA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGT</span><span class="topo-unknown">AADGLNFL</span><span class="topo-inside">WTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITYA</span><span class="topo-outside">SYVRKDQDIV</span><span class="topo-membrane">LSGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFI</span><span class="topo-unknown">TLPAIF</span><span class="topo-inside">SQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-outside">RGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIPKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHESAGTLA</span><span class="topo-unknown">PR</span></span>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>12</td>
      <td>4</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>32</td>
      <td>13</td>
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
      <td>124</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>132</td>
      <td>125</td>
      <td>132</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>134</td>
      <td>133</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>222</td>
      <td>213</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>230</td>
      <td>223</td>
      <td>230</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>231</td>
      <td>241</td>
      <td>231</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>266</td>
      <td>242</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>276</td>
      <td>267</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>297</td>
      <td>277</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>325</td>
      <td>298</td>
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
      <td>339</td>
      <td>332</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
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
      <td>396</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>426</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>427</td>
      <td>428</td>
      <td>427</td>
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
      <td>444</td>
      <td>438</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>469</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>483</td>
      <td>470</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>517</td>
      <td>503</td>
      <td>601</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>518</td>
      <td>519</td>
      <td>602</td>
      <td>603</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1038##nature12179 (1 structure, 2 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3ze4">3ZE4</a></td>
      <td>2.4</td>
      <td>—</td>
      <td>LeuT from A. aeolicus, apo inward-open state</td>
      <td>none (apo state)</td>
    </tr>
  </tbody>
</table>

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3tt3">3TT3</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVKREHWAT</span><span class="topo-outside">RLGLI</span><span class="topo-membrane">LAMAGNAVGLGNFLRFPVQA</span><span class="topo-inside">AENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLM</span><span class="topo-outside">WIEWAMGRYGGAQGHGTTPAIFYLLWRNRFAKILGV</span><span class="topo-membrane">FGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPPPNATDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVS</span><span class="topo-outside">ILIRGISKGIERF</span><span class="topo-membrane">AKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGT</span><span class="topo-unknown">AADGLNFL</span><span class="topo-inside">WTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGF</span><span class="topo-outside">GAIITYASAVRKDQDIVLSGLTA</span><span class="topo-membrane">ATLNEAAEVILGGSIS</span><span class="topo-inside">IPAAVAFFGVANAVAIAKAGAF</span><span class="topo-unknown">NLGFITLPAIF</span><span class="topo-inside">SQTAG</span><span class="topo-membrane">GTFLGFLWFFLLFFAGLVASIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">QPMIAFLEDELKLSRKHAVLW</span><span class="topo-membrane">TAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLT</span><span class="topo-outside">ELIIFFWIFGADKAWEEINRGGIIKVPR</span><span class="topo-unknown">IYYYVMR</span><span class="topo-outside">Y</span><span class="topo-membrane">ITPAFLAVLLVVWAREYI</span><span class="topo-inside">PKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLT</span><span class="topo-outside">FLVFLAERRRNHE</span><span class="topo-unknown">SAGTLVPR</span></span>
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
      <td>1</td>
      <td>10</td>
      <td>1</td>
      <td>10</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>15</td>
      <td>11</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>35</td>
      <td>16</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>43</td>
      <td>36</td>
      <td>43</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>59</td>
      <td>44</td>
      <td>59</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>95</td>
      <td>60</td>
      <td>95</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>124</td>
      <td>96</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>166</td>
      <td>125</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>181</td>
      <td>167</td>
      <td>181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>182</td>
      <td>194</td>
      <td>182</td>
      <td>194</td>
      <td>Outside</td>
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
      <td>222</td>
      <td>213</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>230</td>
      <td>223</td>
      <td>230</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>231</td>
      <td>241</td>
      <td>231</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>259</td>
      <td>242</td>
      <td>259</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>260</td>
      <td>282</td>
      <td>260</td>
      <td>282</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>298</td>
      <td>283</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>320</td>
      <td>299</td>
      <td>320</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>331</td>
      <td>321</td>
      <td>331</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>332</td>
      <td>336</td>
      <td>332</td>
      <td>336</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>337</td>
      <td>360</td>
      <td>337</td>
      <td>360</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>361</td>
      <td>381</td>
      <td>361</td>
      <td>381</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>382</td>
      <td>396</td>
      <td>382</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>418</td>
      <td>400</td>
      <td>418</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>419</td>
      <td>446</td>
      <td>419</td>
      <td>446</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>447</td>
      <td>453</td>
      <td>447</td>
      <td>453</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>454</td>
      <td>454</td>
      <td>454</td>
      <td>454</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>455</td>
      <td>472</td>
      <td>455</td>
      <td>472</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>473</td>
      <td>483</td>
      <td>473</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>498</td>
      <td>484</td>
      <td>498</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>499</td>
      <td>511</td>
      <td>499</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3tt3">3TT3</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVKREHWAT</span><span class="topo-outside">RLGLI</span><span class="topo-membrane">LAMAGNAVGLGNFLRFPVQA</span><span class="topo-inside">AENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLM</span><span class="topo-outside">WIEWAMGRYGGAQGHGTTPAIFYLLWRNRFAKILGV</span><span class="topo-membrane">FGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPPPNATDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVS</span><span class="topo-outside">ILIRGISKGIERF</span><span class="topo-membrane">AKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGT</span><span class="topo-unknown">AADGLNFL</span><span class="topo-inside">WTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGF</span><span class="topo-outside">GAIITYASAVRKDQDIVLSGLTA</span><span class="topo-membrane">ATLNEAAEVILGGSIS</span><span class="topo-inside">IPAAVAFFGVANAVAIAKAGAF</span><span class="topo-unknown">NLGFITLPAIF</span><span class="topo-inside">SQTAG</span><span class="topo-membrane">GTFLGFLWFFLLFFAGLVASIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">QPMIAFLEDELKLSRKHAVLW</span><span class="topo-membrane">TAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLT</span><span class="topo-outside">ELIIFFWIFGADKAWEEINRGGIIKVPR</span><span class="topo-unknown">IYYYVMR</span><span class="topo-outside">Y</span><span class="topo-membrane">ITPAFLAVLLVVWAREYI</span><span class="topo-inside">PKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLT</span><span class="topo-outside">FLVFLAERRRNHE</span><span class="topo-unknown">SAGTLVPR</span></span>
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
      <td>1</td>
      <td>10</td>
      <td>1</td>
      <td>10</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>15</td>
      <td>11</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>35</td>
      <td>16</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>43</td>
      <td>36</td>
      <td>43</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>59</td>
      <td>44</td>
      <td>59</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>95</td>
      <td>60</td>
      <td>95</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>124</td>
      <td>96</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>166</td>
      <td>125</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>181</td>
      <td>167</td>
      <td>181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>182</td>
      <td>194</td>
      <td>182</td>
      <td>194</td>
      <td>Outside</td>
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
      <td>222</td>
      <td>213</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>230</td>
      <td>223</td>
      <td>230</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>231</td>
      <td>241</td>
      <td>231</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>259</td>
      <td>242</td>
      <td>259</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>260</td>
      <td>282</td>
      <td>260</td>
      <td>282</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>298</td>
      <td>283</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>320</td>
      <td>299</td>
      <td>320</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>331</td>
      <td>321</td>
      <td>331</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>332</td>
      <td>336</td>
      <td>332</td>
      <td>336</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>337</td>
      <td>360</td>
      <td>337</td>
      <td>360</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>361</td>
      <td>381</td>
      <td>361</td>
      <td>381</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>382</td>
      <td>396</td>
      <td>382</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>418</td>
      <td>400</td>
      <td>418</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>419</td>
      <td>446</td>
      <td>419</td>
      <td>446</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>447</td>
      <td>453</td>
      <td>447</td>
      <td>453</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>454</td>
      <td>454</td>
      <td>454</td>
      <td>454</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>455</td>
      <td>472</td>
      <td>455</td>
      <td>472</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>473</td>
      <td>483</td>
      <td>473</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>498</td>
      <td>484</td>
      <td>498</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>499</td>
      <td>511</td>
      <td>499</td>
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
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1038##nature10737 (1 structure, 6 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3tt1">3TT1</a></td>
      <td>3.10</td>
      <td>P2(1)2(1)2(1)</td>
      <td>LeuTK(Y108F) Fab complex, outward-open state</td>
      <td>L-leucine, Na+, 2B12 Antibody Fragment Fab</td>
    </tr>
  </tbody>
</table>

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3tt1">3TT1</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGG</span><span class="topo-membrane">AFMIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYFVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPE</span><span class="topo-unknown">PPPNA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIRVF</span><span class="topo-inside">LLETPNGT</span><span class="topo-unknown">AADGLNFL</span><span class="topo-inside">WTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITY</span><span class="topo-outside">ASYVRKDQDIVL</span><span class="topo-membrane">SGLTAATLNEAAEVILGGSIS</span><span class="topo-inside">IPAAVAFFGVANAVAIAKAG</span><span class="topo-unknown">AFNLGF</span><span class="topo-inside">I</span><span class="topo-unknown">TLPAIF</span><span class="topo-inside">SQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRK</span><span class="topo-membrane">HAVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFW</span><span class="topo-outside">IFG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-outside">RGGIIKVPRI</span><span class="topo-membrane">YYYVMRYITPAFLAVLLVVWAREYI</span><span class="topo-inside">PKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERR</span><span class="topo-unknown">RNHESAGTLVPR</span></span>
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
      <td>12</td>
      <td>5</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>32</td>
      <td>13</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>41</td>
      <td>33</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>63</td>
      <td>42</td>
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
      <td>124</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>129</td>
      <td>125</td>
      <td>129</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>134</td>
      <td>130</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>214</td>
      <td>191</td>
      <td>214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>222</td>
      <td>215</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>230</td>
      <td>223</td>
      <td>230</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>231</td>
      <td>241</td>
      <td>231</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>265</td>
      <td>242</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>277</td>
      <td>266</td>
      <td>277</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>298</td>
      <td>278</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>318</td>
      <td>299</td>
      <td>318</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>319</td>
      <td>324</td>
      <td>319</td>
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
      <td>339</td>
      <td>332</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>376</td>
      <td>368</td>
      <td>376</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>396</td>
      <td>377</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>425</td>
      <td>400</td>
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
      <td>472</td>
      <td>448</td>
      <td>472</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>473</td>
      <td>483</td>
      <td>473</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>507</td>
      <td>503</td>
      <td>507</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>508</td>
      <td>519</td>
      <td>508</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3tt1">3TT1</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRLG</span><span class="topo-membrane">LILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGG</span><span class="topo-membrane">AFMIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYFVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPE</span><span class="topo-unknown">PPPNA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIRVF</span><span class="topo-inside">LLETPNGT</span><span class="topo-unknown">AADGLNFL</span><span class="topo-inside">WTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITY</span><span class="topo-outside">ASYVRKDQDIVL</span><span class="topo-membrane">SGLTAATLNEAAEVILGGSIS</span><span class="topo-inside">IPAAVAFFGVANAVAIAKAG</span><span class="topo-unknown">AFNLGF</span><span class="topo-inside">I</span><span class="topo-unknown">TLPAIF</span><span class="topo-inside">SQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRK</span><span class="topo-membrane">HAVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFW</span><span class="topo-outside">IFG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-outside">RGGIIKVPRI</span><span class="topo-membrane">YYYVMRYITPAFLAVLLVVWAREYI</span><span class="topo-inside">PKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERR</span><span class="topo-unknown">RNHESAGTLVPR</span></span>
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
      <td>41</td>
      <td>33</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>63</td>
      <td>42</td>
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
      <td>124</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>129</td>
      <td>125</td>
      <td>129</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>134</td>
      <td>130</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>214</td>
      <td>191</td>
      <td>214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>222</td>
      <td>215</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>230</td>
      <td>223</td>
      <td>230</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>231</td>
      <td>241</td>
      <td>231</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>265</td>
      <td>242</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>277</td>
      <td>266</td>
      <td>277</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>298</td>
      <td>278</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>318</td>
      <td>299</td>
      <td>318</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>319</td>
      <td>324</td>
      <td>319</td>
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
      <td>339</td>
      <td>332</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>376</td>
      <td>368</td>
      <td>376</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>396</td>
      <td>377</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>425</td>
      <td>400</td>
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
      <td>472</td>
      <td>448</td>
      <td>472</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>473</td>
      <td>483</td>
      <td>473</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>507</td>
      <td>503</td>
      <td>507</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>508</td>
      <td>519</td>
      <td>508</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3tt1">3TT1</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGG</span><span class="topo-membrane">AFMIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYFVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPE</span><span class="topo-unknown">PPPNA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIRVF</span><span class="topo-inside">LLETPNGT</span><span class="topo-unknown">AADGLNFL</span><span class="topo-inside">WTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITY</span><span class="topo-outside">ASYVRKDQDIVL</span><span class="topo-membrane">SGLTAATLNEAAEVILGGSIS</span><span class="topo-inside">IPAAVAFFGVANAVAIAKAG</span><span class="topo-unknown">AFNLGF</span><span class="topo-inside">I</span><span class="topo-unknown">TLPAIF</span><span class="topo-inside">SQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRK</span><span class="topo-membrane">HAVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFW</span><span class="topo-outside">IFG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-outside">RGGIIKVPRI</span><span class="topo-membrane">YYYVMRYITPAFLAVLLVVWAREYI</span><span class="topo-inside">PKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERR</span><span class="topo-unknown">RNHESAGTLVPR</span></span>
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
      <td>12</td>
      <td>5</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>32</td>
      <td>13</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>41</td>
      <td>33</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>63</td>
      <td>42</td>
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
      <td>124</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>129</td>
      <td>125</td>
      <td>129</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>134</td>
      <td>130</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>214</td>
      <td>191</td>
      <td>214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>222</td>
      <td>215</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>230</td>
      <td>223</td>
      <td>230</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>231</td>
      <td>241</td>
      <td>231</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>265</td>
      <td>242</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>277</td>
      <td>266</td>
      <td>277</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>298</td>
      <td>278</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>318</td>
      <td>299</td>
      <td>318</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>319</td>
      <td>324</td>
      <td>319</td>
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
      <td>339</td>
      <td>332</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>376</td>
      <td>368</td>
      <td>376</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>396</td>
      <td>377</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>425</td>
      <td>400</td>
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
      <td>472</td>
      <td>448</td>
      <td>472</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>473</td>
      <td>483</td>
      <td>473</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>507</td>
      <td>503</td>
      <td>507</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>508</td>
      <td>519</td>
      <td>508</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3tt1">3TT1</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRLG</span><span class="topo-membrane">LILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGG</span><span class="topo-membrane">AFMIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYFVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPE</span><span class="topo-unknown">PPPNA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIRVF</span><span class="topo-inside">LLETPNGT</span><span class="topo-unknown">AADGLNFL</span><span class="topo-inside">WTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITY</span><span class="topo-outside">ASYVRKDQDIVL</span><span class="topo-membrane">SGLTAATLNEAAEVILGGSIS</span><span class="topo-inside">IPAAVAFFGVANAVAIAKAG</span><span class="topo-unknown">AFNLGF</span><span class="topo-inside">I</span><span class="topo-unknown">TLPAIF</span><span class="topo-inside">SQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRK</span><span class="topo-membrane">HAVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFW</span><span class="topo-outside">IFG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-outside">RGGIIKVPRI</span><span class="topo-membrane">YYYVMRYITPAFLAVLLVVWAREYI</span><span class="topo-inside">PKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERR</span><span class="topo-unknown">RNHESAGTLVPR</span></span>
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
      <td>41</td>
      <td>33</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>63</td>
      <td>42</td>
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
      <td>124</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>129</td>
      <td>125</td>
      <td>129</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>134</td>
      <td>130</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>214</td>
      <td>191</td>
      <td>214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>222</td>
      <td>215</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>230</td>
      <td>223</td>
      <td>230</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>231</td>
      <td>241</td>
      <td>231</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>265</td>
      <td>242</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>277</td>
      <td>266</td>
      <td>277</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>298</td>
      <td>278</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>318</td>
      <td>299</td>
      <td>318</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>319</td>
      <td>324</td>
      <td>319</td>
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
      <td>339</td>
      <td>332</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>376</td>
      <td>368</td>
      <td>376</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>396</td>
      <td>377</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>425</td>
      <td>400</td>
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
      <td>472</td>
      <td>448</td>
      <td>472</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>473</td>
      <td>483</td>
      <td>473</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>507</td>
      <td>503</td>
      <td>507</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>508</td>
      <td>519</td>
      <td>508</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3tt1">3TT1</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGG</span><span class="topo-membrane">AFMIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYFVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPE</span><span class="topo-unknown">PPPNA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIRVF</span><span class="topo-inside">LLETPNGT</span><span class="topo-unknown">AADGLNFL</span><span class="topo-inside">WTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITY</span><span class="topo-outside">ASYVRKDQDIVL</span><span class="topo-membrane">SGLTAATLNEAAEVILGGSIS</span><span class="topo-inside">IPAAVAFFGVANAVAIAKAG</span><span class="topo-unknown">AFNLGF</span><span class="topo-inside">I</span><span class="topo-unknown">TLPAIF</span><span class="topo-inside">SQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRK</span><span class="topo-membrane">HAVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFW</span><span class="topo-outside">IFG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-outside">RGGIIKVPRI</span><span class="topo-membrane">YYYVMRYITPAFLAVLLVVWAREYI</span><span class="topo-inside">PKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERR</span><span class="topo-unknown">RNHESAGTLVPR</span></span>
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
      <td>12</td>
      <td>5</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>32</td>
      <td>13</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>41</td>
      <td>33</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>63</td>
      <td>42</td>
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
      <td>124</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>129</td>
      <td>125</td>
      <td>129</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>134</td>
      <td>130</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>214</td>
      <td>191</td>
      <td>214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>222</td>
      <td>215</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>230</td>
      <td>223</td>
      <td>230</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>231</td>
      <td>241</td>
      <td>231</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>265</td>
      <td>242</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>277</td>
      <td>266</td>
      <td>277</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>298</td>
      <td>278</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>318</td>
      <td>299</td>
      <td>318</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>319</td>
      <td>324</td>
      <td>319</td>
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
      <td>339</td>
      <td>332</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>376</td>
      <td>368</td>
      <td>376</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>396</td>
      <td>377</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>425</td>
      <td>400</td>
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
      <td>472</td>
      <td>448</td>
      <td>472</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>473</td>
      <td>483</td>
      <td>473</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>507</td>
      <td>503</td>
      <td>507</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>508</td>
      <td>519</td>
      <td>508</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3tt1">3TT1</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRLG</span><span class="topo-membrane">LILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGG</span><span class="topo-membrane">AFMIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYFVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPE</span><span class="topo-unknown">PPPNA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIRVF</span><span class="topo-inside">LLETPNGT</span><span class="topo-unknown">AADGLNFL</span><span class="topo-inside">WTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITY</span><span class="topo-outside">ASYVRKDQDIVL</span><span class="topo-membrane">SGLTAATLNEAAEVILGGSIS</span><span class="topo-inside">IPAAVAFFGVANAVAIAKAG</span><span class="topo-unknown">AFNLGF</span><span class="topo-inside">I</span><span class="topo-unknown">TLPAIF</span><span class="topo-inside">SQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRK</span><span class="topo-membrane">HAVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFW</span><span class="topo-outside">IFG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-outside">RGGIIKVPRI</span><span class="topo-membrane">YYYVMRYITPAFLAVLLVVWAREYI</span><span class="topo-inside">PKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERR</span><span class="topo-unknown">RNHESAGTLVPR</span></span>
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
      <td>41</td>
      <td>33</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>63</td>
      <td>42</td>
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
      <td>124</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>129</td>
      <td>125</td>
      <td>129</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>134</td>
      <td>130</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>214</td>
      <td>191</td>
      <td>214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>222</td>
      <td>215</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>230</td>
      <td>223</td>
      <td>230</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>231</td>
      <td>241</td>
      <td>231</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>265</td>
      <td>242</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>277</td>
      <td>266</td>
      <td>277</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>298</td>
      <td>278</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>318</td>
      <td>299</td>
      <td>318</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>319</td>
      <td>324</td>
      <td>319</td>
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
      <td>339</td>
      <td>332</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>376</td>
      <td>368</td>
      <td>376</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>396</td>
      <td>377</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>425</td>
      <td>400</td>
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
      <td>472</td>
      <td>448</td>
      <td>472</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>473</td>
      <td>483</td>
      <td>473</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>507</td>
      <td>503</td>
      <td>507</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>508</td>
      <td>519</td>
      <td>508</td>
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
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1038##ncomms11673 (3 structures, 4 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5jae">5JAE</a></td>
      <td>2.50</td>
      <td>P21</td>
      <td>LeuT from A. aeolicus, outward-oriented Na+- and substrate-free state at pH 6.5</td>
      <td>none (Na+- and substrate-free state)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5jaf">5JAF</a></td>
      <td>3.08</td>
      <td>C2</td>
      <td>LeuT from A. aeolicus, outward-oriented Na+- and substrate-free state at pH 5.0</td>
      <td>none (Na+- and substrate-free state)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5jag">5JAG</a></td>
      <td>2.58</td>
      <td>C2</td>
      <td>LeuT T354H mutant, outward-oriented Na+- and substrate-free state at pH 6.5</td>
      <td>none (Na+- and substrate-free state)</td>
    </tr>
  </tbody>
</table>

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5jae">5JAE</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEV</span><span class="topo-outside">KREHWATRLG</span><span class="topo-membrane">LILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">KFLVGLVPEPP</span><span class="topo-unknown">PN</span><span class="topo-inside">ATDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILI</span><span class="topo-outside">RGISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGT</span><span class="topo-unknown">AADGLN</span><span class="topo-inside">FLWTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">PGV</span><span class="topo-membrane">WIAAVGQIFFTLSLGFGAIITY</span><span class="topo-outside">ASYVRKDQDIVLS</span><span class="topo-membrane">GLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAG</span><span class="topo-unknown">AFNLGF</span><span class="topo-inside">I</span><span class="topo-unknown">TLPAIF</span><span class="topo-inside">SQTAGGTFLGF</span><span class="topo-membrane">LWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAF</span><span class="topo-outside">LEDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVM</span><span class="topo-inside">FLNKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFW</span><span class="topo-outside">IFG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-outside">RGGIIKVPRI</span><span class="topo-membrane">YYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIPKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTVW</span><span class="topo-membrane">ITRFYIIGLFLFLTFLV</span><span class="topo-outside">FLAERRRNHES</span><span class="topo-unknown">AGTLVPR</span></span>
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
      <td>4</td>
      <td>13</td>
      <td>4</td>
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
      <td>120</td>
      <td>90</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>121</td>
      <td>131</td>
      <td>121</td>
      <td>131</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>166</td>
      <td>134</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>222</td>
      <td>213</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>228</td>
      <td>223</td>
      <td>228</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>229</td>
      <td>243</td>
      <td>229</td>
      <td>243</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>265</td>
      <td>244</td>
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
      <td>318</td>
      <td>298</td>
      <td>318</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>319</td>
      <td>324</td>
      <td>319</td>
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
      <td>366</td>
      <td>343</td>
      <td>366</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>367</td>
      <td>377</td>
      <td>367</td>
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
      <td>399</td>
      <td>395</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>425</td>
      <td>400</td>
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
      <td>469</td>
      <td>448</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>484</td>
      <td>470</td>
      <td>484</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>485</td>
      <td>501</td>
      <td>485</td>
      <td>501</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>502</td>
      <td>512</td>
      <td>502</td>
      <td>512</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5jae">5JAE</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEV</span><span class="topo-outside">KREHWATRLG</span><span class="topo-membrane">LILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGG</span><span class="topo-membrane">AFMIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">KFLVGLVPEPPPNATDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILI</span><span class="topo-outside">RGISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGT</span><span class="topo-unknown">AADGLNFLW</span><span class="topo-inside">TPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">PGV</span><span class="topo-membrane">WIAAVGQIFFTLSLGFGAIITY</span><span class="topo-outside">ASYVRKDQDIVLS</span><span class="topo-membrane">GLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFI</span><span class="topo-unknown">TLPAIFS</span><span class="topo-inside">QTAGGTFLGF</span><span class="topo-membrane">LWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAF</span><span class="topo-outside">LEDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVM</span><span class="topo-inside">FLNKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFW</span><span class="topo-outside">IFG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-outside">RGGIIKVPRI</span><span class="topo-membrane">YYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIPKI</span><span class="topo-unknown">MEET</span><span class="topo-inside">H</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTVW</span><span class="topo-membrane">ITRFYIIGLFLFLTFLV</span><span class="topo-outside">FLAERRRNH</span><span class="topo-unknown">ESAGTLVPR</span></span>
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
      <td>4</td>
      <td>13</td>
      <td>4</td>
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
      <td>41</td>
      <td>33</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>63</td>
      <td>42</td>
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
      <td>120</td>
      <td>90</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>121</td>
      <td>166</td>
      <td>121</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>222</td>
      <td>213</td>
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
      <td>243</td>
      <td>232</td>
      <td>243</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>265</td>
      <td>244</td>
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
      <td>325</td>
      <td>298</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>332</td>
      <td>326</td>
      <td>332</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>333</td>
      <td>342</td>
      <td>333</td>
      <td>342</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>366</td>
      <td>343</td>
      <td>366</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>367</td>
      <td>377</td>
      <td>367</td>
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
      <td>399</td>
      <td>395</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>425</td>
      <td>400</td>
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
      <td>469</td>
      <td>448</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>475</td>
      <td>470</td>
      <td>475</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>480</td>
      <td>484</td>
      <td>480</td>
      <td>484</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>485</td>
      <td>501</td>
      <td>485</td>
      <td>501</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>502</td>
      <td>510</td>
      <td>502</td>
      <td>510</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5jaf">5JAF</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEV</span><span class="topo-outside">KREHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRF</span><span class="topo-inside">PVQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRFAKI</span><span class="topo-membrane">LGVFGLWIPLVVAIYYVYIESWTLG</span><span class="topo-unknown">FAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">KFLV</span><span class="topo-inside">GLVPEP</span><span class="topo-unknown">PPNA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSLF</span><span class="topo-membrane">AYIVFLITMFINVSILI</span><span class="topo-outside">RGISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVI</span><span class="topo-inside">RVFLLETPNGT</span><span class="topo-unknown">AADGLNFL</span><span class="topo-inside">WT</span><span class="topo-unknown">PD</span><span class="topo-inside">FEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">PGV</span><span class="topo-membrane">WIAAVGQIFFTLSLGFGAIITY</span><span class="topo-outside">ASYVRKDQDIVLS</span><span class="topo-membrane">GLTAATLNEKAEVILGGS</span><span class="topo-inside">ISIPAAVAFFGVANAVAIAKAG</span><span class="topo-unknown">AFNLGF</span><span class="topo-inside">I</span><span class="topo-unknown">TLPAIFSQ</span><span class="topo-inside">TAGGTFLGF</span><span class="topo-membrane">LWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMI</span><span class="topo-outside">AFLEDELKLSRKHA</span><span class="topo-membrane">VLWTAAIVFFSAHLVM</span><span class="topo-inside">FLNKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELII</span><span class="topo-outside">FFWIFG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-outside">RGGIIKVPRI</span><span class="topo-membrane">YYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIP</span><span class="topo-unknown">KIMEE</span><span class="topo-inside">TH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTVW</span><span class="topo-membrane">ITRFYIIGLFLFLTFL</span><span class="topo-outside">VFLAERRR</span><span class="topo-unknown">NHESAGTLVPR</span></span>
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
      <td>4</td>
      <td>12</td>
      <td>4</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>31</td>
      <td>13</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>43</td>
      <td>32</td>
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
      <td>92</td>
      <td>64</td>
      <td>92</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>117</td>
      <td>93</td>
      <td>117</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>118</td>
      <td>124</td>
      <td>118</td>
      <td>124</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>125</td>
      <td>130</td>
      <td>125</td>
      <td>130</td>
      <td>Inside</td>
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
      <td>230</td>
      <td>223</td>
      <td>230</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>231</td>
      <td>232</td>
      <td>231</td>
      <td>232</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>235</td>
      <td>243</td>
      <td>235</td>
      <td>243</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>265</td>
      <td>244</td>
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
      <td>296</td>
      <td>279</td>
      <td>296</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>297</td>
      <td>318</td>
      <td>297</td>
      <td>318</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>319</td>
      <td>324</td>
      <td>319</td>
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
      <td>333</td>
      <td>326</td>
      <td>333</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>334</td>
      <td>342</td>
      <td>334</td>
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
      <td>378</td>
      <td>365</td>
      <td>378</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>379</td>
      <td>394</td>
      <td>379</td>
      <td>394</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>395</td>
      <td>399</td>
      <td>395</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>422</td>
      <td>400</td>
      <td>422</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>423</td>
      <td>428</td>
      <td>423</td>
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
      <td>469</td>
      <td>448</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>473</td>
      <td>470</td>
      <td>473</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>479</td>
      <td>484</td>
      <td>479</td>
      <td>484</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>485</td>
      <td>500</td>
      <td>485</td>
      <td>500</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>501</td>
      <td>508</td>
      <td>501</td>
      <td>508</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5jag">5JAG</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEV</span><span class="topo-outside">KREHWATRLG</span><span class="topo-membrane">LILAMAGNAVGLGNFLRFPVQA</span><span class="topo-inside">AEN</span><span class="topo-membrane">GGGAFMIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNR</span><span class="topo-membrane">FAKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">KFLVGLVPEPP</span><span class="topo-unknown">PNA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSLF</span><span class="topo-membrane">AYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIRVF</span><span class="topo-inside">LLETPNGT</span><span class="topo-unknown">AADGLNFL</span><span class="topo-inside">WTPDFEKL</span><span class="topo-membrane">KD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">PGVWIAAVGQIFFTLSL</span><span class="topo-outside">GFGAIITYASYVRKDQDIVLSG</span><span class="topo-membrane">LTAATLNEKAEVILGGSIS</span><span class="topo-inside">IPAAVAFFGVAN</span><span class="topo-unknown">AVAIAKA</span><span class="topo-inside">G</span><span class="topo-unknown">AFNLGF</span><span class="topo-inside">I</span><span class="topo-unknown">TLPAIFS</span><span class="topo-inside">QTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLHSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRK</span><span class="topo-membrane">HAVLWTAAIVFFSAHLVM</span><span class="topo-inside">FLNKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFW</span><span class="topo-outside">IFG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-outside">RGGIIKVPRI</span><span class="topo-membrane">YYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIP</span><span class="topo-unknown">KIMEE</span><span class="topo-inside">TH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTVW</span><span class="topo-membrane">ITRFYIIGLFLFLTFLVFL</span><span class="topo-outside">AERR</span><span class="topo-unknown">RNHESAGTLVPR</span></span>
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
      <td>4</td>
      <td>13</td>
      <td>4</td>
      <td>13</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>35</td>
      <td>14</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>38</td>
      <td>36</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>63</td>
      <td>39</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>88</td>
      <td>64</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>120</td>
      <td>89</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>121</td>
      <td>131</td>
      <td>121</td>
      <td>131</td>
      <td>Inside</td>
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
      <td>185</td>
      <td>168</td>
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
      <td>214</td>
      <td>191</td>
      <td>214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>222</td>
      <td>215</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>230</td>
      <td>223</td>
      <td>230</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>231</td>
      <td>238</td>
      <td>231</td>
      <td>238</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>257</td>
      <td>239</td>
      <td>257</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>258</td>
      <td>279</td>
      <td>258</td>
      <td>279</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>298</td>
      <td>280</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>310</td>
      <td>299</td>
      <td>310</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>317</td>
      <td>311</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>318</td>
      <td>318</td>
      <td>318</td>
      <td>318</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>319</td>
      <td>324</td>
      <td>319</td>
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
      <td>332</td>
      <td>326</td>
      <td>332</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>333</td>
      <td>339</td>
      <td>333</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>376</td>
      <td>368</td>
      <td>376</td>
      <td>Outside</td>
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
      <td>399</td>
      <td>395</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>425</td>
      <td>400</td>
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
      <td>469</td>
      <td>448</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>473</td>
      <td>470</td>
      <td>473</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>479</td>
      <td>484</td>
      <td>479</td>
      <td>484</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>485</td>
      <td>503</td>
      <td>485</td>
      <td>503</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>504</td>
      <td>507</td>
      <td>504</td>
      <td>507</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1021##bi101148w (1 structure, 4 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3mpn">3MPN</a></td>
      <td>2.25</td>
      <td>C2</td>
      <td>LeuT F177R1 spin-labeled mutant</td>
      <td>R1 nitroxide spin label</td>
    </tr>
  </tbody>
</table>

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3mpn">3MPN</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">REHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYYVYIESWTLGFAIKFLV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">GLVPEPPP</span><span class="topo-unknown">NA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMCINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGTAADGLNFLWTPDFEKLKDPGV</span><span class="topo-membrane">W</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">IAAVGQIFFTLSLGFGAIITYA</span><span class="topo-outside">SYVRKDQDIV</span><span class="topo-membrane">LSGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFITLPAIFSQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIMQPMI</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">AFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FGADKAWEEINRGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIPKIMEETHWTV</span><span class="topo-membrane">W</span></span>
<span class="topo-ruler">       490       500       </span>
<span class="topo-line"><span class="topo-membrane">ITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHE</span></span>
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
      <td>8</td>
      <td>5</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>28</td>
      <td>13</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>39</td>
      <td>33</td>
      <td>43</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>59</td>
      <td>44</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>85</td>
      <td>64</td>
      <td>89</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>120</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>121</td>
      <td>128</td>
      <td>125</td>
      <td>132</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>130</td>
      <td>133</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>131</td>
      <td>162</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>163</td>
      <td>181</td>
      <td>167</td>
      <td>185</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>182</td>
      <td>186</td>
      <td>186</td>
      <td>190</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>187</td>
      <td>208</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>209</td>
      <td>239</td>
      <td>213</td>
      <td>243</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>262</td>
      <td>244</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>263</td>
      <td>272</td>
      <td>267</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>273</td>
      <td>293</td>
      <td>277</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>294</td>
      <td>335</td>
      <td>298</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>336</td>
      <td>363</td>
      <td>340</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>373</td>
      <td>368</td>
      <td>377</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>374</td>
      <td>392</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>393</td>
      <td>395</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>396</td>
      <td>422</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>423</td>
      <td>440</td>
      <td>427</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>441</td>
      <td>465</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>466</td>
      <td>479</td>
      <td>470</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>480</td>
      <td>498</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>499</td>
      <td>507</td>
      <td>503</td>
      <td>511</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3mpn">3MPN</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">REHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYYVYIESWTLGFAIKFLV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">GLVPEPPP</span><span class="topo-unknown">NA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMCINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGTAADGLNFLWTPDFEKLKDPGV</span><span class="topo-membrane">W</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">IAAVGQIFFTLSLGFGAIITYA</span><span class="topo-outside">SYVRKDQDIV</span><span class="topo-membrane">LSGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFITLPAIFSQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIMQPMI</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">AFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FGADKAWEEINRGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIPKIMEETHWTV</span><span class="topo-membrane">W</span></span>
<span class="topo-ruler">       490       500       </span>
<span class="topo-line"><span class="topo-membrane">ITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHE</span></span>
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
      <td>8</td>
      <td>5</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>28</td>
      <td>13</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>39</td>
      <td>33</td>
      <td>43</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>59</td>
      <td>44</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>85</td>
      <td>64</td>
      <td>89</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>120</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>121</td>
      <td>128</td>
      <td>125</td>
      <td>132</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>130</td>
      <td>133</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>131</td>
      <td>162</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>163</td>
      <td>181</td>
      <td>167</td>
      <td>185</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>182</td>
      <td>186</td>
      <td>186</td>
      <td>190</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>187</td>
      <td>208</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>209</td>
      <td>239</td>
      <td>213</td>
      <td>243</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>262</td>
      <td>244</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>263</td>
      <td>272</td>
      <td>267</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>273</td>
      <td>293</td>
      <td>277</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>294</td>
      <td>335</td>
      <td>298</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>336</td>
      <td>363</td>
      <td>340</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>373</td>
      <td>368</td>
      <td>377</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>374</td>
      <td>392</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>393</td>
      <td>395</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>396</td>
      <td>422</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>423</td>
      <td>440</td>
      <td>427</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>441</td>
      <td>465</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>466</td>
      <td>479</td>
      <td>470</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>480</td>
      <td>498</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>499</td>
      <td>507</td>
      <td>503</td>
      <td>511</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3mpn">3MPN</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">REHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYYVYIESWTLGFAIKFLV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">GLVPEPPP</span><span class="topo-unknown">NA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMCINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGTAADGLNFLWTPDFEKLKDPGV</span><span class="topo-membrane">W</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">IAAVGQIFFTLSLGFGAIITYA</span><span class="topo-outside">SYVRKDQDIV</span><span class="topo-membrane">LSGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFITLPAIFSQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIMQPMI</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">AFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FGADKAWEEINRGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIPKIMEETHWTV</span><span class="topo-membrane">W</span></span>
<span class="topo-ruler">       490       500       </span>
<span class="topo-line"><span class="topo-membrane">ITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHE</span></span>
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
      <td>8</td>
      <td>5</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>28</td>
      <td>13</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>39</td>
      <td>33</td>
      <td>43</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>59</td>
      <td>44</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>85</td>
      <td>64</td>
      <td>89</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>120</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>121</td>
      <td>128</td>
      <td>125</td>
      <td>132</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>130</td>
      <td>133</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>131</td>
      <td>162</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>163</td>
      <td>181</td>
      <td>167</td>
      <td>185</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>182</td>
      <td>186</td>
      <td>186</td>
      <td>190</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>187</td>
      <td>208</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>209</td>
      <td>239</td>
      <td>213</td>
      <td>243</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>262</td>
      <td>244</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>263</td>
      <td>272</td>
      <td>267</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>273</td>
      <td>293</td>
      <td>277</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>294</td>
      <td>335</td>
      <td>298</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>336</td>
      <td>363</td>
      <td>340</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>373</td>
      <td>368</td>
      <td>377</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>374</td>
      <td>392</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>393</td>
      <td>395</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>396</td>
      <td>422</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>423</td>
      <td>440</td>
      <td>427</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>441</td>
      <td>465</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>466</td>
      <td>479</td>
      <td>470</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>480</td>
      <td>498</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>499</td>
      <td>507</td>
      <td>503</td>
      <td>511</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3mpn">3MPN</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">REHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYYVYIESWTLGFAIKFLV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">GLVPEPPP</span><span class="topo-unknown">NA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMCINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGTAADGLNFLWTPDFEKLKDPGV</span><span class="topo-membrane">W</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">IAAVGQIFFTLSLGFGAIITYA</span><span class="topo-outside">SYVRKDQDIV</span><span class="topo-membrane">LSGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFITLPAIFSQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIMQPMI</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">AFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FGADKAWEEINRGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIPKIMEETHWTV</span><span class="topo-membrane">W</span></span>
<span class="topo-ruler">       490       500       </span>
<span class="topo-line"><span class="topo-membrane">ITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHE</span></span>
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
      <td>8</td>
      <td>5</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>28</td>
      <td>13</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>39</td>
      <td>33</td>
      <td>43</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>59</td>
      <td>44</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>85</td>
      <td>64</td>
      <td>89</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>120</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>121</td>
      <td>128</td>
      <td>125</td>
      <td>132</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>130</td>
      <td>133</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>131</td>
      <td>162</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>163</td>
      <td>181</td>
      <td>167</td>
      <td>185</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>182</td>
      <td>186</td>
      <td>186</td>
      <td>190</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>187</td>
      <td>208</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>209</td>
      <td>239</td>
      <td>213</td>
      <td>243</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>262</td>
      <td>244</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>263</td>
      <td>272</td>
      <td>267</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>273</td>
      <td>293</td>
      <td>277</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>294</td>
      <td>335</td>
      <td>298</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>336</td>
      <td>363</td>
      <td>340</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>373</td>
      <td>368</td>
      <td>377</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>374</td>
      <td>392</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>393</td>
      <td>395</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>396</td>
      <td>422</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>423</td>
      <td>440</td>
      <td>427</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>441</td>
      <td>465</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>466</td>
      <td>479</td>
      <td>470</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>480</td>
      <td>498</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>499</td>
      <td>507</td>
      <td>503</td>
      <td>511</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1038/nsmb.2215 (1 structure, 8 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3usg">3USG</a></td>
      <td>2.5</td>
      <td>C2</td>
      <td>LeuT-Leu complex in DMPC-CHAPSO bicelles</td>
      <td>L-leucine, Na+ (2 ions)</td>
    </tr>
  </tbody>
</table>

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3usg">3USG</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRLG</span><span class="topo-membrane">LILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGG</span><span class="topo-membrane">AFMIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNR</span><span class="topo-membrane">FAKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPP</span><span class="topo-unknown">PNA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGTAADGLNFLWTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITY</span><span class="topo-outside">ASYVRKDQDIVL</span><span class="topo-membrane">SGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFITLPAIFSQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRK</span><span class="topo-membrane">HAVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFW</span><span class="topo-outside">IFGADKAWEEINRGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAREYI</span><span class="topo-inside">PKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRN</span><span class="topo-unknown">HESAGTLVPR</span></span>
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
      <td>41</td>
      <td>33</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>63</td>
      <td>42</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>88</td>
      <td>64</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>124</td>
      <td>89</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>131</td>
      <td>125</td>
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
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>241</td>
      <td>213</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>265</td>
      <td>242</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>277</td>
      <td>266</td>
      <td>277</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>297</td>
      <td>278</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>339</td>
      <td>298</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>376</td>
      <td>368</td>
      <td>376</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>396</td>
      <td>377</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>425</td>
      <td>400</td>
      <td>425</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>426</td>
      <td>444</td>
      <td>426</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>472</td>
      <td>445</td>
      <td>472</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>473</td>
      <td>483</td>
      <td>473</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>509</td>
      <td>503</td>
      <td>509</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>510</td>
      <td>519</td>
      <td>510</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3usg">3USG</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRLG</span><span class="topo-membrane">LILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGG</span><span class="topo-membrane">AFMIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNR</span><span class="topo-membrane">FAKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPP</span><span class="topo-unknown">PNA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGTAADGLNFLWTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITY</span><span class="topo-outside">ASYVRKDQDIVL</span><span class="topo-membrane">SGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFITLPAIFSQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRK</span><span class="topo-membrane">HAVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFW</span><span class="topo-outside">IFGADKAWEEINRGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAREYI</span><span class="topo-inside">PKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRN</span><span class="topo-unknown">HESAGTLVPR</span></span>
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
      <td>41</td>
      <td>33</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>63</td>
      <td>42</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>88</td>
      <td>64</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>124</td>
      <td>89</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>131</td>
      <td>125</td>
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
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>241</td>
      <td>213</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>265</td>
      <td>242</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>277</td>
      <td>266</td>
      <td>277</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>297</td>
      <td>278</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>339</td>
      <td>298</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>376</td>
      <td>368</td>
      <td>376</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>396</td>
      <td>377</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>425</td>
      <td>400</td>
      <td>425</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>426</td>
      <td>444</td>
      <td>426</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>472</td>
      <td>445</td>
      <td>472</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>473</td>
      <td>483</td>
      <td>473</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>509</td>
      <td>503</td>
      <td>509</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>510</td>
      <td>519</td>
      <td>510</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3usg">3USG</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRLG</span><span class="topo-membrane">LILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGG</span><span class="topo-membrane">AFMIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNR</span><span class="topo-membrane">FAKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPP</span><span class="topo-unknown">PNA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGTAADGLNFLWTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITY</span><span class="topo-outside">ASYVRKDQDIVL</span><span class="topo-membrane">SGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFITLPAIFSQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRK</span><span class="topo-membrane">HAVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFW</span><span class="topo-outside">IFGADKAWEEINRGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAREYI</span><span class="topo-inside">PKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRN</span><span class="topo-unknown">HESAGTLVPR</span></span>
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
      <td>41</td>
      <td>33</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>63</td>
      <td>42</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>88</td>
      <td>64</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>124</td>
      <td>89</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>131</td>
      <td>125</td>
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
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>241</td>
      <td>213</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>265</td>
      <td>242</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>277</td>
      <td>266</td>
      <td>277</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>297</td>
      <td>278</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>339</td>
      <td>298</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>376</td>
      <td>368</td>
      <td>376</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>396</td>
      <td>377</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>425</td>
      <td>400</td>
      <td>425</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>426</td>
      <td>444</td>
      <td>426</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>472</td>
      <td>445</td>
      <td>472</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>473</td>
      <td>483</td>
      <td>473</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>509</td>
      <td>503</td>
      <td>509</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>510</td>
      <td>519</td>
      <td>510</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3usg">3USG</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRLG</span><span class="topo-membrane">LILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGG</span><span class="topo-membrane">AFMIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNR</span><span class="topo-membrane">FAKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPP</span><span class="topo-unknown">PNA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGTAADGLNFLWTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITY</span><span class="topo-outside">ASYVRKDQDIVL</span><span class="topo-membrane">SGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFITLPAIFSQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRK</span><span class="topo-membrane">HAVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFW</span><span class="topo-outside">IFGADKAWEEINRGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAREYI</span><span class="topo-inside">PKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRN</span><span class="topo-unknown">HESAGTLVPR</span></span>
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
      <td>41</td>
      <td>33</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>63</td>
      <td>42</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>88</td>
      <td>64</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>124</td>
      <td>89</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>131</td>
      <td>125</td>
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
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>241</td>
      <td>213</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>265</td>
      <td>242</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>277</td>
      <td>266</td>
      <td>277</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>297</td>
      <td>278</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>339</td>
      <td>298</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>376</td>
      <td>368</td>
      <td>376</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>396</td>
      <td>377</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>425</td>
      <td>400</td>
      <td>425</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>426</td>
      <td>444</td>
      <td>426</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>472</td>
      <td>445</td>
      <td>472</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>473</td>
      <td>483</td>
      <td>473</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>509</td>
      <td>503</td>
      <td>509</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>510</td>
      <td>519</td>
      <td>510</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3usg">3USG</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRLG</span><span class="topo-membrane">LILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGG</span><span class="topo-membrane">AFMIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNR</span><span class="topo-membrane">FAKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPP</span><span class="topo-unknown">PNA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGTAADGLNFLWTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITY</span><span class="topo-outside">ASYVRKDQDIVL</span><span class="topo-membrane">SGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFITLPAIFSQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRK</span><span class="topo-membrane">HAVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFW</span><span class="topo-outside">IFGADKAWEEINRGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAREYI</span><span class="topo-inside">PKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRN</span><span class="topo-unknown">HESAGTLVPR</span></span>
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
      <td>41</td>
      <td>33</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>63</td>
      <td>42</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>88</td>
      <td>64</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>124</td>
      <td>89</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>131</td>
      <td>125</td>
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
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>241</td>
      <td>213</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>265</td>
      <td>242</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>277</td>
      <td>266</td>
      <td>277</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>297</td>
      <td>278</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>339</td>
      <td>298</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>376</td>
      <td>368</td>
      <td>376</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>396</td>
      <td>377</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>425</td>
      <td>400</td>
      <td>425</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>426</td>
      <td>444</td>
      <td>426</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>472</td>
      <td>445</td>
      <td>472</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>473</td>
      <td>483</td>
      <td>473</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>509</td>
      <td>503</td>
      <td>509</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>510</td>
      <td>519</td>
      <td>510</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3usg">3USG</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRLG</span><span class="topo-membrane">LILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGG</span><span class="topo-membrane">AFMIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNR</span><span class="topo-membrane">FAKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPP</span><span class="topo-unknown">PNA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGTAADGLNFLWTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITY</span><span class="topo-outside">ASYVRKDQDIVL</span><span class="topo-membrane">SGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFITLPAIFSQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRK</span><span class="topo-membrane">HAVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFW</span><span class="topo-outside">IFGADKAWEEINRGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAREYI</span><span class="topo-inside">PKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRN</span><span class="topo-unknown">HESAGTLVPR</span></span>
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
      <td>41</td>
      <td>33</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>63</td>
      <td>42</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>88</td>
      <td>64</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>124</td>
      <td>89</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>131</td>
      <td>125</td>
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
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>241</td>
      <td>213</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>265</td>
      <td>242</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>277</td>
      <td>266</td>
      <td>277</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>297</td>
      <td>278</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>339</td>
      <td>298</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>376</td>
      <td>368</td>
      <td>376</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>396</td>
      <td>377</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>425</td>
      <td>400</td>
      <td>425</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>426</td>
      <td>444</td>
      <td>426</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>472</td>
      <td>445</td>
      <td>472</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>473</td>
      <td>483</td>
      <td>473</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>509</td>
      <td>503</td>
      <td>509</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>510</td>
      <td>519</td>
      <td>510</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3usg">3USG</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRLG</span><span class="topo-membrane">LILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGG</span><span class="topo-membrane">AFMIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNR</span><span class="topo-membrane">FAKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPP</span><span class="topo-unknown">PNA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGTAADGLNFLWTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITY</span><span class="topo-outside">ASYVRKDQDIVL</span><span class="topo-membrane">SGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFITLPAIFSQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRK</span><span class="topo-membrane">HAVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFW</span><span class="topo-outside">IFGADKAWEEINRGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAREYI</span><span class="topo-inside">PKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRN</span><span class="topo-unknown">HESAGTLVPR</span></span>
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
      <td>41</td>
      <td>33</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>63</td>
      <td>42</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>88</td>
      <td>64</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>124</td>
      <td>89</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>131</td>
      <td>125</td>
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
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>241</td>
      <td>213</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>265</td>
      <td>242</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>277</td>
      <td>266</td>
      <td>277</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>297</td>
      <td>278</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>339</td>
      <td>298</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>376</td>
      <td>368</td>
      <td>376</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>396</td>
      <td>377</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>425</td>
      <td>400</td>
      <td>425</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>426</td>
      <td>444</td>
      <td>426</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>472</td>
      <td>445</td>
      <td>472</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>473</td>
      <td>483</td>
      <td>473</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>509</td>
      <td>503</td>
      <td>509</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>510</td>
      <td>519</td>
      <td>510</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3usg">3USG</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRLG</span><span class="topo-membrane">LILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGG</span><span class="topo-membrane">AFMIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNR</span><span class="topo-membrane">FAKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPP</span><span class="topo-unknown">PNA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGTAADGLNFLWTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITY</span><span class="topo-outside">ASYVRKDQDIVL</span><span class="topo-membrane">SGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFITLPAIFSQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRK</span><span class="topo-membrane">HAVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFW</span><span class="topo-outside">IFGADKAWEEINRGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAREYI</span><span class="topo-inside">PKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRN</span><span class="topo-unknown">HESAGTLVPR</span></span>
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
      <td>41</td>
      <td>33</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>63</td>
      <td>42</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>88</td>
      <td>64</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>124</td>
      <td>89</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>131</td>
      <td>125</td>
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
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>241</td>
      <td>213</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>265</td>
      <td>242</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>277</td>
      <td>266</td>
      <td>277</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>297</td>
      <td>278</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>339</td>
      <td>298</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>376</td>
      <td>368</td>
      <td>376</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>396</td>
      <td>377</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>425</td>
      <td>400</td>
      <td>425</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>426</td>
      <td>444</td>
      <td>426</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>472</td>
      <td>445</td>
      <td>472</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>473</td>
      <td>483</td>
      <td>473</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>509</td>
      <td>503</td>
      <td>509</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>510</td>
      <td>519</td>
      <td>510</td>
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
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1038##s41467-020-14735-w (1 structure, 2 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6xwm">6XWM</a></td>
      <td>2.60</td>
      <td>P1</td>
      <td>LeuT W8A mutant, Na+/L-Phe-bound inward-facing occluded state</td>
      <td>L-phenylalanine, Na+ (2 ions)</td>
    </tr>
  </tbody>
</table>

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6xwm">6XWM</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVKREHAATRL</span><span class="topo-inside">GLI</span><span class="topo-membrane">LAMAGNAVGLGNFLRFPVQA</span><span class="topo-outside">AENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIE</span><span class="topo-inside">WAMGRYGGAQGHGTTPAIFYLLWRNRFAKI</span><span class="topo-membrane">LGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-outside">GLVPEPPPNATDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSIL</span><span class="topo-inside">IRGISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVI</span><span class="topo-outside">RVFLLETPNGT</span><span class="topo-unknown">AADGLNFLW</span><span class="topo-outside">TPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAI</span><span class="topo-inside">ITYASYVRKDQDIVLSG</span><span class="topo-membrane">LTAATLNEKAEVILGGSI</span><span class="topo-outside">SIPAAVAFFGVANAVAIAKAGAF</span><span class="topo-unknown">NLGFITLPAIFS</span><span class="topo-outside">QTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPM</span><span class="topo-inside">IAFLEDELKLSRKHAV</span><span class="topo-membrane">LWTAAIVFFSAHLVMFL</span><span class="topo-outside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELI</span><span class="topo-inside">IFFWIFG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-inside">RGGIIKVPRI</span><span class="topo-membrane">YYYVMRYITPAFLAVLLVVWAR</span><span class="topo-unknown">EYIPKI</span><span class="topo-outside">MEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-outside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFL</span><span class="topo-inside">VFLAERRRNH</span><span class="topo-unknown">ESAGTLVPR</span></span>
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
      <td>13</td>
      <td>15</td>
      <td>13</td>
      <td>15</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>35</td>
      <td>16</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>43</td>
      <td>36</td>
      <td>43</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>62</td>
      <td>44</td>
      <td>62</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>92</td>
      <td>63</td>
      <td>92</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>124</td>
      <td>93</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>166</td>
      <td>125</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>183</td>
      <td>167</td>
      <td>183</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>184</td>
      <td>190</td>
      <td>184</td>
      <td>190</td>
      <td>Inside</td>
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
      <td>Outside</td>
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
      <td>241</td>
      <td>232</td>
      <td>241</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>262</td>
      <td>242</td>
      <td>262</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>263</td>
      <td>279</td>
      <td>263</td>
      <td>279</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>297</td>
      <td>280</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>320</td>
      <td>298</td>
      <td>320</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>332</td>
      <td>321</td>
      <td>332</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>333</td>
      <td>339</td>
      <td>333</td>
      <td>339</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>363</td>
      <td>340</td>
      <td>363</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>379</td>
      <td>364</td>
      <td>379</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>380</td>
      <td>396</td>
      <td>380</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>421</td>
      <td>400</td>
      <td>421</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>422</td>
      <td>428</td>
      <td>422</td>
      <td>428</td>
      <td>Inside</td>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>448</td>
      <td>469</td>
      <td>448</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>475</td>
      <td>470</td>
      <td>475</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>476</td>
      <td>483</td>
      <td>476</td>
      <td>483</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>500</td>
      <td>484</td>
      <td>500</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>501</td>
      <td>510</td>
      <td>501</td>
      <td>510</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6xwm">6XWM</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVKREHAATRL</span><span class="topo-inside">GLI</span><span class="topo-membrane">LAMAGNAVGLGNFLRFPVQA</span><span class="topo-outside">AENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIE</span><span class="topo-inside">WAMGRYGGAQGHGTTPAIFYLLWRNRFAKI</span><span class="topo-membrane">LGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-outside">GLVPEPPPNATDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSIL</span><span class="topo-inside">IRGISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVI</span><span class="topo-outside">RVFLLETPNGTAADGLNFLWTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAI</span><span class="topo-inside">ITYASYVRKDQDIVLSG</span><span class="topo-membrane">LTAATLNEKAEVILGGSI</span><span class="topo-outside">SIPAAVAFFGVANAVAIAKAGAF</span><span class="topo-unknown">NLGFITLPAIFSQ</span><span class="topo-outside">TAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPM</span><span class="topo-inside">IAFLEDELKLSRKHAV</span><span class="topo-membrane">LWTAAIVFFSAHLVMFL</span><span class="topo-outside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELI</span><span class="topo-inside">IFFWIFG</span><span class="topo-unknown">ADKAWEEI</span><span class="topo-inside">NRGGIIKVPRI</span><span class="topo-membrane">YYYVMRYITPAFLAVLLVVWAR</span><span class="topo-unknown">EYIPKIM</span><span class="topo-outside">EETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-outside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFL</span><span class="topo-inside">VFLAERR</span><span class="topo-unknown">RNHESAGTLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (30 regions)</summary>
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
      <td>13</td>
      <td>15</td>
      <td>13</td>
      <td>15</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>35</td>
      <td>16</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>43</td>
      <td>36</td>
      <td>43</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>62</td>
      <td>44</td>
      <td>62</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>92</td>
      <td>63</td>
      <td>92</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>124</td>
      <td>93</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>166</td>
      <td>125</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>183</td>
      <td>167</td>
      <td>183</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>184</td>
      <td>190</td>
      <td>184</td>
      <td>190</td>
      <td>Inside</td>
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
      <td>241</td>
      <td>212</td>
      <td>241</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>262</td>
      <td>242</td>
      <td>262</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>263</td>
      <td>279</td>
      <td>263</td>
      <td>279</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>297</td>
      <td>280</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>320</td>
      <td>298</td>
      <td>320</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>333</td>
      <td>321</td>
      <td>333</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>334</td>
      <td>339</td>
      <td>334</td>
      <td>339</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>363</td>
      <td>340</td>
      <td>363</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>379</td>
      <td>364</td>
      <td>379</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>380</td>
      <td>396</td>
      <td>380</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>421</td>
      <td>400</td>
      <td>421</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>422</td>
      <td>428</td>
      <td>422</td>
      <td>428</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>429</td>
      <td>436</td>
      <td>429</td>
      <td>436</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>437</td>
      <td>447</td>
      <td>437</td>
      <td>447</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>448</td>
      <td>469</td>
      <td>448</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>476</td>
      <td>470</td>
      <td>476</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>477</td>
      <td>483</td>
      <td>477</td>
      <td>483</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>500</td>
      <td>484</td>
      <td>500</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>501</td>
      <td>507</td>
      <td>501</td>
      <td>507</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1073##pnas.0811322106 (1 structure, 2 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3gjd">3GJD</a></td>
      <td>2.80</td>
      <td>P2(1)</td>
      <td>LeuT-E290S mutant, S1:Leu/S2:OG state</td>
      <td>L-leucine (S1), n-octyl-beta-D-glucopyranoside (OG, S2), Na+ (2 ions)</td>
    </tr>
  </tbody>
</table>

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3gjd">3GJD</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPPP</span><span class="topo-unknown">NA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGTAADGLNFLWTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">PGV</span><span class="topo-membrane">WIAAVGQIFFTLSLGFGAIITYA</span><span class="topo-outside">SYVRKDQDIV</span><span class="topo-membrane">LSGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFITLPAIFSQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FGADKAWEEINRGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIPKIMEETH</span></span>
<span class="topo-ruler">       490       500       510     </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHESAGT</span></span>
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
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>12</td>
      <td>5</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>32</td>
      <td>13</td>
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
      <td>124</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>132</td>
      <td>125</td>
      <td>132</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>134</td>
      <td>133</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>243</td>
      <td>213</td>
      <td>243</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>266</td>
      <td>244</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>276</td>
      <td>267</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>297</td>
      <td>277</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>339</td>
      <td>298</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
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
      <td>396</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>426</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>427</td>
      <td>444</td>
      <td>427</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>469</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>483</td>
      <td>470</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>515</td>
      <td>503</td>
      <td>515</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3gjd">3GJD</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPPP</span><span class="topo-unknown">NA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGTAADGLNFLWTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">PGV</span><span class="topo-membrane">WIAAVGQIFFTLSLGFGAIITYA</span><span class="topo-outside">SYVRKDQDIV</span><span class="topo-membrane">LSGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFITLPAIFSQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FGADKAWEEINRGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIPKIMEETH</span></span>
<span class="topo-ruler">       490       500       510     </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHESAGT</span></span>
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
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>12</td>
      <td>5</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>32</td>
      <td>13</td>
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
      <td>124</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>132</td>
      <td>125</td>
      <td>132</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>134</td>
      <td>133</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>243</td>
      <td>213</td>
      <td>243</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>266</td>
      <td>244</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>276</td>
      <td>267</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>297</td>
      <td>277</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>339</td>
      <td>298</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
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
      <td>396</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>426</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>427</td>
      <td>444</td>
      <td>427</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>469</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>483</td>
      <td>470</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>515</td>
      <td>503</td>
      <td>515</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1126##science.1147614 (1 structure, 1 sequence)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2qju">2QJU</a></td>
      <td>2.9</td>
      <td>—</td>
      <td>LeuT with bound leucine, Na+, and desipramine</td>
      <td>L-leucine, Na+ (2 ions), desipramine</td>
    </tr>
  </tbody>
</table>

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2qju">2QJU</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">REHWATRLGLI</span><span class="topo-membrane">LAMAGNAVGLGNFLRFPVQA</span><span class="topo-outside">AENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-inside">AMGRYGGAQGHGTTPAIFYLLWRNR</span><span class="topo-membrane">FAKILGVFGLWIPLVVAIYYVYIESWTLGFAIKFLV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">GLVPEPPP</span><span class="topo-unknown">NA</span><span class="topo-outside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILI</span><span class="topo-inside">RGISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIRVF</span><span class="topo-outside">LLETPNGT</span><span class="topo-unknown">AADGLNFL</span><span class="topo-outside">WTPDFEKLKDP</span><span class="topo-membrane">GVW</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">IAAVGQIFFTLSLGFGAIITY</span><span class="topo-inside">ASYVRKDQDIVL</span><span class="topo-membrane">SGLTAATLNEKAEVILGGSIS</span><span class="topo-outside">IPAAVAFFGV</span><span class="topo-unknown">ANAVAIAKA</span><span class="topo-outside">G</span><span class="topo-unknown">AFNLGF</span><span class="topo-outside">I</span><span class="topo-unknown">TLPAIF</span><span class="topo-outside">SQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIMQPMI</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">AF</span><span class="topo-inside">LEDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-outside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-inside">FG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-inside">RGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-outside">EY</span><span class="topo-unknown">IPKIME</span><span class="topo-outside">ETHWTV</span><span class="topo-membrane">W</span></span>
<span class="topo-ruler">       490       500       510 </span>
<span class="topo-line"><span class="topo-membrane">ITRFYIIGLFLFLTFLVF</span><span class="topo-inside">LAERRRNHESAGT</span></span>
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
      <td>11</td>
      <td>5</td>
      <td>15</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>31</td>
      <td>16</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>39</td>
      <td>36</td>
      <td>43</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>59</td>
      <td>44</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>84</td>
      <td>64</td>
      <td>88</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>120</td>
      <td>89</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>121</td>
      <td>128</td>
      <td>125</td>
      <td>132</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>130</td>
      <td>133</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>131</td>
      <td>162</td>
      <td>135</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>163</td>
      <td>180</td>
      <td>167</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>181</td>
      <td>186</td>
      <td>185</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>187</td>
      <td>210</td>
      <td>191</td>
      <td>214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>218</td>
      <td>215</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>219</td>
      <td>226</td>
      <td>223</td>
      <td>230</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>227</td>
      <td>237</td>
      <td>231</td>
      <td>241</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>238</td>
      <td>261</td>
      <td>242</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>273</td>
      <td>266</td>
      <td>277</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>274</td>
      <td>294</td>
      <td>278</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>295</td>
      <td>304</td>
      <td>299</td>
      <td>308</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>305</td>
      <td>313</td>
      <td>309</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>314</td>
      <td>314</td>
      <td>318</td>
      <td>318</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>315</td>
      <td>320</td>
      <td>319</td>
      <td>324</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>321</td>
      <td>321</td>
      <td>325</td>
      <td>325</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>322</td>
      <td>327</td>
      <td>326</td>
      <td>331</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>328</td>
      <td>335</td>
      <td>332</td>
      <td>339</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>336</td>
      <td>362</td>
      <td>340</td>
      <td>366</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>363</td>
      <td>373</td>
      <td>367</td>
      <td>377</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>374</td>
      <td>392</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>393</td>
      <td>395</td>
      <td>397</td>
      <td>399</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>396</td>
      <td>422</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>423</td>
      <td>424</td>
      <td>427</td>
      <td>428</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>425</td>
      <td>433</td>
      <td>429</td>
      <td>437</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>434</td>
      <td>440</td>
      <td>438</td>
      <td>444</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>441</td>
      <td>465</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>466</td>
      <td>467</td>
      <td>470</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>468</td>
      <td>473</td>
      <td>472</td>
      <td>477</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>474</td>
      <td>479</td>
      <td>478</td>
      <td>483</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>480</td>
      <td>498</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>499</td>
      <td>511</td>
      <td>503</td>
      <td>515</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1126##science.1166777 (7 structures, 14 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3f4j">3F4J</a></td>
      <td></td>
      <td>—</td>
      <td>LeuT from A. aeolicus cocrystallized with glycine</td>
      <td>glycine, Na+ (2 ions)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3f48">3F48</a></td>
      <td></td>
      <td>—</td>
      <td>LeuT from A. aeolicus cocrystallized with alanine</td>
      <td>alanine, Na+ (2 ions)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3f3e">3F3E</a></td>
      <td></td>
      <td>—</td>
      <td>LeuT from A. aeolicus cocrystallized with 30 mM leucine</td>
      <td>leucine, Na+ (2 ions)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3f3d">3F3D</a></td>
      <td></td>
      <td>—</td>
      <td>LeuT from A. aeolicus cocrystallized with methionine</td>
      <td>methionine, Na+ (2 ions)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3f4i">3F4I</a></td>
      <td></td>
      <td>—</td>
      <td>LeuT from A. aeolicus, selenomethionine complex</td>
      <td>selenomethionine, Na+ (2 ions)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3f3c">3F3C</a></td>
      <td></td>
      <td>—</td>
      <td>LeuT from A. aeolicus cocrystallized with L-4-fluorophenylalanine</td>
      <td>L-4-fluorophenylalanine, Na+ (2 ions)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3f3a">3F3A</a></td>
      <td></td>
      <td>—</td>
      <td>LeuT from A. aeolicus cocrystallized with tryptophan, open-to-out conformation</td>
      <td>tryptophan, Na+ (2 ions)</td>
    </tr>
  </tbody>
</table>

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3f4j">3F4J</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPPP</span><span class="topo-unknown">NA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGTAADGLNFLWTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">PGV</span><span class="topo-membrane">WIAAVGQIFFTLSLGFGAIITY</span><span class="topo-outside">ASYVRKDQDIV</span><span class="topo-membrane">LSGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFITLPAIFSQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FGADKAWEEINRGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIPKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHESAGT</span><span class="topo-unknown">LVPR</span></span>
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
      <td>12</td>
      <td>5</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>32</td>
      <td>13</td>
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
      <td>124</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>132</td>
      <td>125</td>
      <td>132</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>134</td>
      <td>133</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>243</td>
      <td>213</td>
      <td>243</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>265</td>
      <td>244</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>276</td>
      <td>266</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>297</td>
      <td>277</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>339</td>
      <td>298</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
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
      <td>396</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>426</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>427</td>
      <td>444</td>
      <td>427</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>469</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>483</td>
      <td>470</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>515</td>
      <td>503</td>
      <td>515</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>516</td>
      <td>519</td>
      <td>516</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3f4j">3F4J</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPPP</span><span class="topo-unknown">NA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGTAADGLNFLWTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">PGV</span><span class="topo-membrane">WIAAVGQIFFTLSLGFGAIITY</span><span class="topo-outside">ASYVRKDQDIV</span><span class="topo-membrane">LSGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFITLPAIFSQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FGADKAWEEINRGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIPKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHESAGT</span><span class="topo-unknown">LVPR</span></span>
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
      <td>12</td>
      <td>5</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>32</td>
      <td>13</td>
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
      <td>124</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>132</td>
      <td>125</td>
      <td>132</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>134</td>
      <td>133</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>243</td>
      <td>213</td>
      <td>243</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>265</td>
      <td>244</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>276</td>
      <td>266</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>297</td>
      <td>277</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>339</td>
      <td>298</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
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
      <td>396</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>426</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>427</td>
      <td>444</td>
      <td>427</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>469</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>483</td>
      <td>470</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>515</td>
      <td>503</td>
      <td>515</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>516</td>
      <td>519</td>
      <td>516</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3f48">3F48</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPPP</span><span class="topo-unknown">NA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILI</span><span class="topo-outside">RGISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGT</span><span class="topo-unknown">AADGLNFL</span><span class="topo-inside">WTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITY</span><span class="topo-outside">ASYVRKDQDIVL</span><span class="topo-membrane">SGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFI</span><span class="topo-unknown">TLPAIF</span><span class="topo-inside">SQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-outside">RGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIPKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHESAGTA</span><span class="topo-unknown">VPR</span></span>
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
      <td>12</td>
      <td>5</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>32</td>
      <td>13</td>
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
      <td>124</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>132</td>
      <td>125</td>
      <td>132</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>134</td>
      <td>133</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>222</td>
      <td>213</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>230</td>
      <td>223</td>
      <td>230</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>231</td>
      <td>241</td>
      <td>231</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>265</td>
      <td>242</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>277</td>
      <td>266</td>
      <td>277</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>297</td>
      <td>278</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>325</td>
      <td>298</td>
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
      <td>339</td>
      <td>332</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
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
      <td>396</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>426</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>427</td>
      <td>428</td>
      <td>427</td>
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
      <td>444</td>
      <td>438</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>469</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>483</td>
      <td>470</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>516</td>
      <td>503</td>
      <td>601</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>517</td>
      <td>519</td>
      <td>602</td>
      <td>604</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3f48">3F48</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPPP</span><span class="topo-unknown">NA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILI</span><span class="topo-outside">RGISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGT</span><span class="topo-unknown">AADGLNFL</span><span class="topo-inside">WTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITY</span><span class="topo-outside">ASYVRKDQDIVL</span><span class="topo-membrane">SGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFI</span><span class="topo-unknown">TLPAIF</span><span class="topo-inside">SQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-outside">RGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIPKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHESAGTA</span><span class="topo-unknown">VPR</span></span>
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
      <td>12</td>
      <td>5</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>32</td>
      <td>13</td>
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
      <td>124</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>132</td>
      <td>125</td>
      <td>132</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>134</td>
      <td>133</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>222</td>
      <td>213</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>230</td>
      <td>223</td>
      <td>230</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>231</td>
      <td>241</td>
      <td>231</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>265</td>
      <td>242</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>277</td>
      <td>266</td>
      <td>277</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>297</td>
      <td>278</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>325</td>
      <td>298</td>
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
      <td>339</td>
      <td>332</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
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
      <td>396</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>426</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>427</td>
      <td>428</td>
      <td>427</td>
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
      <td>444</td>
      <td>438</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>469</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>483</td>
      <td>470</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>516</td>
      <td>503</td>
      <td>601</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>517</td>
      <td>519</td>
      <td>602</td>
      <td>604</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3f3e">3F3E</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFPVQA</span><span class="topo-inside">AENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNR</span><span class="topo-membrane">FAKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPPP</span><span class="topo-unknown">NA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGTAADGLNFLWTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITYA</span><span class="topo-outside">SYVRKDQDIV</span><span class="topo-membrane">LSGLTAATLNEKAEVILGGSIS</span><span class="topo-inside">IPAAVAFFGVANAVAIAKAGAFNLGFITLPAIFSQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FGADKAWEEINRGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIPKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHESAGT</span><span class="topo-unknown">LVPR</span></span>
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
      <td>12</td>
      <td>5</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>35</td>
      <td>13</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>43</td>
      <td>36</td>
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
      <td>88</td>
      <td>64</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>124</td>
      <td>89</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>132</td>
      <td>125</td>
      <td>132</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>134</td>
      <td>133</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>241</td>
      <td>213</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>266</td>
      <td>242</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>276</td>
      <td>267</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>298</td>
      <td>277</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>339</td>
      <td>299</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
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
      <td>396</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>426</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>427</td>
      <td>444</td>
      <td>427</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>469</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>483</td>
      <td>470</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>515</td>
      <td>503</td>
      <td>515</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>516</td>
      <td>519</td>
      <td>516</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3f3e">3F3E</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFPVQA</span><span class="topo-inside">AENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNR</span><span class="topo-membrane">FAKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPPP</span><span class="topo-unknown">NA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGTAADGLNFLWTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITYA</span><span class="topo-outside">SYVRKDQDIV</span><span class="topo-membrane">LSGLTAATLNEKAEVILGGSIS</span><span class="topo-inside">IPAAVAFFGVANAVAIAKAGAFNLGFITLPAIFSQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FGADKAWEEINRGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIPKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHESAGT</span><span class="topo-unknown">LVPR</span></span>
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
      <td>12</td>
      <td>5</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>35</td>
      <td>13</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>43</td>
      <td>36</td>
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
      <td>88</td>
      <td>64</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>124</td>
      <td>89</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>132</td>
      <td>125</td>
      <td>132</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>134</td>
      <td>133</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>241</td>
      <td>213</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>266</td>
      <td>242</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>276</td>
      <td>267</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>298</td>
      <td>277</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>339</td>
      <td>299</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
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
      <td>396</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>426</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>427</td>
      <td>444</td>
      <td>427</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>469</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>483</td>
      <td>470</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>515</td>
      <td>503</td>
      <td>515</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>516</td>
      <td>519</td>
      <td>516</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3f3d">3F3D</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNR</span><span class="topo-membrane">FAKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPPP</span><span class="topo-unknown">NA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGT</span><span class="topo-unknown">AADGLNFL</span><span class="topo-inside">WTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">PGV</span><span class="topo-membrane">WIAAVGQIFFTLSLGFGAIITYA</span><span class="topo-outside">SYVRKDQDIV</span><span class="topo-membrane">LSGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAG</span><span class="topo-unknown">AFNLGF</span><span class="topo-inside">I</span><span class="topo-unknown">TLPAIF</span><span class="topo-inside">SQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-outside">RGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EY</span><span class="topo-unknown">IPKIME</span><span class="topo-inside">ETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHESAGTM</span><span class="topo-unknown">VPR</span></span>
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
      <td>12</td>
      <td>5</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>32</td>
      <td>13</td>
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
      <td>88</td>
      <td>64</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>124</td>
      <td>89</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>132</td>
      <td>125</td>
      <td>132</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>134</td>
      <td>133</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>222</td>
      <td>213</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>230</td>
      <td>223</td>
      <td>230</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>231</td>
      <td>243</td>
      <td>231</td>
      <td>243</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>266</td>
      <td>244</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>276</td>
      <td>267</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>297</td>
      <td>277</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>318</td>
      <td>298</td>
      <td>318</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>319</td>
      <td>324</td>
      <td>319</td>
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
      <td>339</td>
      <td>332</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
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
      <td>396</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>426</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>427</td>
      <td>428</td>
      <td>427</td>
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
      <td>444</td>
      <td>438</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>469</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>471</td>
      <td>470</td>
      <td>471</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>477</td>
      <td>472</td>
      <td>477</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>478</td>
      <td>483</td>
      <td>478</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>516</td>
      <td>503</td>
      <td>601</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>517</td>
      <td>519</td>
      <td>602</td>
      <td>604</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3f3d">3F3D</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNR</span><span class="topo-membrane">FAKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPPP</span><span class="topo-unknown">NA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGT</span><span class="topo-unknown">AADGLNFL</span><span class="topo-inside">WTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">PGV</span><span class="topo-membrane">WIAAVGQIFFTLSLGFGAIITYA</span><span class="topo-outside">SYVRKDQDIV</span><span class="topo-membrane">LSGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAG</span><span class="topo-unknown">AFNLGF</span><span class="topo-inside">I</span><span class="topo-unknown">TLPAIF</span><span class="topo-inside">SQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-outside">RGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EY</span><span class="topo-unknown">IPKIME</span><span class="topo-inside">ETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHESAGTM</span><span class="topo-unknown">VPR</span></span>
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
      <td>12</td>
      <td>5</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>32</td>
      <td>13</td>
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
      <td>88</td>
      <td>64</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>124</td>
      <td>89</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>132</td>
      <td>125</td>
      <td>132</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>134</td>
      <td>133</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>222</td>
      <td>213</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>230</td>
      <td>223</td>
      <td>230</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>231</td>
      <td>243</td>
      <td>231</td>
      <td>243</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>266</td>
      <td>244</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>276</td>
      <td>267</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>297</td>
      <td>277</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>318</td>
      <td>298</td>
      <td>318</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>319</td>
      <td>324</td>
      <td>319</td>
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
      <td>339</td>
      <td>332</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
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
      <td>396</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>426</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>427</td>
      <td>428</td>
      <td>427</td>
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
      <td>444</td>
      <td>438</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>469</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>471</td>
      <td>470</td>
      <td>471</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>477</td>
      <td>472</td>
      <td>477</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>478</td>
      <td>483</td>
      <td>478</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>516</td>
      <td>503</td>
      <td>601</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>517</td>
      <td>519</td>
      <td>602</td>
      <td>604</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3f4i">3F4I</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPPP</span><span class="topo-unknown">NA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILI</span><span class="topo-outside">RGISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGTAADGLNFLWTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITY</span><span class="topo-outside">ASYVRKDQDIVL</span><span class="topo-membrane">SGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFITLPAIFSQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FGADKAWEEINRGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIPKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHESAGT</span><span class="topo-unknown">LVPR</span></span>
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
      <td>12</td>
      <td>5</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>32</td>
      <td>13</td>
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
      <td>124</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>132</td>
      <td>125</td>
      <td>132</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>134</td>
      <td>133</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>241</td>
      <td>213</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>265</td>
      <td>242</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>277</td>
      <td>266</td>
      <td>277</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>297</td>
      <td>278</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>339</td>
      <td>298</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
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
      <td>396</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>426</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>427</td>
      <td>444</td>
      <td>427</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>469</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>483</td>
      <td>470</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>515</td>
      <td>503</td>
      <td>515</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>516</td>
      <td>519</td>
      <td>516</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3f4i">3F4I</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPPP</span><span class="topo-unknown">NA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILI</span><span class="topo-outside">RGISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGTAADGLNFLWTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITY</span><span class="topo-outside">ASYVRKDQDIVL</span><span class="topo-membrane">SGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFITLPAIFSQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FGADKAWEEINRGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIPKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHESAGT</span><span class="topo-unknown">LVPR</span></span>
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
      <td>12</td>
      <td>5</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>32</td>
      <td>13</td>
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
      <td>124</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>132</td>
      <td>125</td>
      <td>132</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>134</td>
      <td>133</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>241</td>
      <td>213</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>265</td>
      <td>242</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>277</td>
      <td>266</td>
      <td>277</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>297</td>
      <td>278</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>339</td>
      <td>298</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
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
      <td>396</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>426</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>427</td>
      <td>444</td>
      <td>427</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>469</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>483</td>
      <td>470</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>515</td>
      <td>503</td>
      <td>515</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>516</td>
      <td>519</td>
      <td>516</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3f3c">3F3C</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPPP</span><span class="topo-unknown">NA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGT</span><span class="topo-unknown">AADGLNFLW</span><span class="topo-inside">TPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">PGV</span><span class="topo-membrane">WIAAVGQIFFTLSLGFGAIITY</span><span class="topo-outside">ASYVRKDQDIVL</span><span class="topo-membrane">SGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFG</span><span class="topo-unknown">VANAVAIAKA</span><span class="topo-inside">GAFNLGFI</span><span class="topo-unknown">TLPAIF</span><span class="topo-inside">SQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-outside">RGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIPKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHESAGT</span><span class="topo-unknown">LVPR</span></span>
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
      <td>12</td>
      <td>5</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>32</td>
      <td>13</td>
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
      <td>124</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>132</td>
      <td>125</td>
      <td>132</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>134</td>
      <td>133</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>222</td>
      <td>213</td>
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
      <td>243</td>
      <td>232</td>
      <td>243</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>265</td>
      <td>244</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>277</td>
      <td>266</td>
      <td>277</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>297</td>
      <td>278</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>307</td>
      <td>298</td>
      <td>307</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>308</td>
      <td>317</td>
      <td>308</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>318</td>
      <td>325</td>
      <td>318</td>
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
      <td>339</td>
      <td>332</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
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
      <td>396</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>426</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>427</td>
      <td>428</td>
      <td>427</td>
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
      <td>444</td>
      <td>438</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>469</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>483</td>
      <td>470</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>515</td>
      <td>503</td>
      <td>515</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>516</td>
      <td>519</td>
      <td>516</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3f3c">3F3C</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRL</span><span class="topo-membrane">GLILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGGAF</span><span class="topo-membrane">MIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNRF</span><span class="topo-membrane">AKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPPP</span><span class="topo-unknown">NA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILIR</span><span class="topo-outside">GISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGT</span><span class="topo-unknown">AADGLNFLW</span><span class="topo-inside">TPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">PGV</span><span class="topo-membrane">WIAAVGQIFFTLSLGFGAIITY</span><span class="topo-outside">ASYVRKDQDIVL</span><span class="topo-membrane">SGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFG</span><span class="topo-unknown">VANAVAIAKA</span><span class="topo-inside">GAFNLGFI</span><span class="topo-unknown">TLPAIF</span><span class="topo-inside">SQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FG</span><span class="topo-unknown">ADKAWEEIN</span><span class="topo-outside">RGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIPKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHESAGT</span><span class="topo-unknown">LVPR</span></span>
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
      <td>12</td>
      <td>5</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>32</td>
      <td>13</td>
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
      <td>124</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>132</td>
      <td>125</td>
      <td>132</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>134</td>
      <td>133</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>185</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>222</td>
      <td>213</td>
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
      <td>243</td>
      <td>232</td>
      <td>243</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>265</td>
      <td>244</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>277</td>
      <td>266</td>
      <td>277</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>297</td>
      <td>278</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>307</td>
      <td>298</td>
      <td>307</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>308</td>
      <td>317</td>
      <td>308</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>318</td>
      <td>325</td>
      <td>318</td>
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
      <td>339</td>
      <td>332</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
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
      <td>396</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>426</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>427</td>
      <td>428</td>
      <td>427</td>
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
      <td>444</td>
      <td>438</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>469</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>483</td>
      <td>470</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
      <td>502</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>503</td>
      <td>515</td>
      <td>503</td>
      <td>515</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>516</td>
      <td>519</td>
      <td>516</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3f3a">3F3A</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRLG</span><span class="topo-membrane">LILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGG</span><span class="topo-membrane">AFMIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNR</span><span class="topo-membrane">FAKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPP</span><span class="topo-unknown">PNA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILI</span><span class="topo-outside">RGISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGTAADGLNFLWTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITY</span><span class="topo-outside">ASYVRKDQDIVL</span><span class="topo-membrane">SGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFITLPAIFSQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FGADKAWEEINRGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIPKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHE</span><span class="topo-unknown">SAGTLVPR</span></span>
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
      <td>41</td>
      <td>33</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>63</td>
      <td>42</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>88</td>
      <td>64</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>124</td>
      <td>89</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>131</td>
      <td>125</td>
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
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>241</td>
      <td>213</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>265</td>
      <td>242</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>277</td>
      <td>266</td>
      <td>277</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>297</td>
      <td>278</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>339</td>
      <td>298</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
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
      <td>396</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>426</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>427</td>
      <td>444</td>
      <td>427</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>469</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>483</td>
      <td>470</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3f3a">3F3A</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEVK</span><span class="topo-outside">REHWATRLG</span><span class="topo-membrane">LILAMAGNAVGLGNFLRFP</span><span class="topo-inside">VQAAENGGG</span><span class="topo-membrane">AFMIPYIIAFLLVGIPLMWIEW</span><span class="topo-outside">AMGRYGGAQGHGTTPAIFYLLWRNR</span><span class="topo-membrane">FAKILGVFGLWIPLVVAIYYVYIESWTLGFAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KFLV</span><span class="topo-inside">GLVPEPP</span><span class="topo-unknown">PNA</span><span class="topo-inside">TDPDSILRPFKEFLYSYIGVPKGDEPILKPSL</span><span class="topo-membrane">FAYIVFLITMFINVSILI</span><span class="topo-outside">RGISKG</span><span class="topo-membrane">IERFAKIAMPTLFILAVFLVIR</span><span class="topo-inside">VFLLETPNGTAADGLNFLWTPDFEKLKD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">GVWIAAVGQIFFTLSLGFGAIITY</span><span class="topo-outside">ASYVRKDQDIVL</span><span class="topo-membrane">SGLTAATLNEKAEVILGGSI</span><span class="topo-inside">SIPAAVAFFGVANAVAIAKAGAFNLGFITLPAIFSQTAGGTF</span><span class="topo-membrane">LGFLWFFLLFFAGLTSSIAIM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">QPMIAFL</span><span class="topo-outside">EDELKLSRKH</span><span class="topo-membrane">AVLWTAAIVFFSAHLVMFL</span><span class="topo-inside">NKS</span><span class="topo-membrane">LDEMDFWAGTIGVVFFGLTELIIFFWI</span><span class="topo-outside">FGADKAWEEINRGGIIKV</span><span class="topo-membrane">PRIYYYVMRYITPAFLAVLLVVWAR</span><span class="topo-inside">EYIPKIMEETH</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-inside">WTV</span><span class="topo-membrane">WITRFYIIGLFLFLTFLVF</span><span class="topo-outside">LAERRRNHE</span><span class="topo-unknown">SAGTLVPR</span></span>
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
      <td>41</td>
      <td>33</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>63</td>
      <td>42</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>88</td>
      <td>64</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>124</td>
      <td>89</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>131</td>
      <td>125</td>
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
      <td>166</td>
      <td>135</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>167</td>
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
      <td>212</td>
      <td>191</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>241</td>
      <td>213</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>265</td>
      <td>242</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>277</td>
      <td>266</td>
      <td>277</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>297</td>
      <td>278</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>339</td>
      <td>298</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>367</td>
      <td>340</td>
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
      <td>396</td>
      <td>378</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>397</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>426</td>
      <td>400</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>427</td>
      <td>444</td>
      <td>427</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>469</td>
      <td>445</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>483</td>
      <td>470</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>502</td>
      <td>484</td>
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
</details>


## Biological / Functional Insights

### TCA binding site in the extracellular-facing vestibule

The tricyclic antidepressants clomipramine, desipramine, and imipramine bind to LeuT in the extracellular-facing vestibule, about 11 A above the substrate and two sodium ions. The TCAs are cradled by the C-terminal half of TM1, the N-terminal regions of TM6 and TM10, the approximate midpoint of TM3, and the sharp turn of EL4. The binding site has a pronounced negative electrostatic potential that enhances binding of positively charged inhibitors.

### Noncompetitive inhibition mechanism

TCAs noncompetitively inhibit LeuT by stabilizing the occluded state. Clomipramine reduces the rate at which leucine dissociates from LeuT by as much as 700-fold. The mechanism involves stabilization of the salt bridge between Arg30 and Asp404 (the extracellular gate) and allosteric preclusion of movement of TM1a and TM6b.

### Structural changes upon TCA binding

Two conformational changes occur upon TCA binding: (1) The guanidinium group of Arg30 forms a direct salt bridge with Asp404, displacing intervening water molecules and shielding the ion pair from solvent. (2) Ala319 in EL4 flips towards the extracellular side (clomipramine) or the EL4 residues shift upward by up to 1.4 A (imipramine/desipramine) to accommodate the inhibitor.


## Cross-References

- <a href="/xray-mp-wiki/proteins/slc-transporters/leubat/">LeuBAT (LeuT Engineered for Antidepressant Pharmacology)</a> — Engineered LeuT variant for antidepressant pharmacology studies
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/nss-family/">Neurotransmitter/Sodium Symporter (NSS) Family</a> — LeuT is the NSS family prototype
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — Core transport mechanism revealed by LeuT structures
- <a href="/xray-mp-wiki/reagents/ligands/clomipramine/">Clomipramine (CMI)</a> — TCA used in cocrystal structures of LeuT
- <a href="/xray-mp-wiki/reagents/ligands/desipramine/">Desipramine</a> — TCA used in cocrystal structures of LeuT
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/tca-inhibition-mechanism/">Tricyclic Antidepressant (TCA) Inhibition Mechanism in NSS Transporters</a> — TCA inhibition mechanism revealed by LeuT-TCA structures
- <a href="/xray-mp-wiki/reagents/ligands/imipramine/">Imipramine</a> — Related ligand or cofactor
- <a href="/xray-mp-wiki/reagents/detergents/n-octyl-beta-d-glucopyranoside/">OG</a> — Detergent used in purification or crystallization
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
