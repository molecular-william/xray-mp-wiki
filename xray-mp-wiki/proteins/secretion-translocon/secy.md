---
title: "Thermus thermophilus SecY Core Channel Subunit"
created: 2026-05-27
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.celrep.2015.10.025]
verified: regex
uniprot_id: ['P38383', 'Q5SHE6', 'Q5SHQ8']
---

# Thermus thermophilus SecY Core Channel Subunit

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P38383">UniProt: P38383</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q5SHE6">UniProt: Q5SHE6</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q5SHQ8">UniProt: Q5SHQ8</a>

<span class="expr-badge">Thermus thermophilus</span>

## Overview

SecY is the core channel-forming subunit of the Sec translocon, a heterotrimeric protein-conducting channel complex essential for protein translocation across the bacterial plasma membrane and integration of membrane proteins. SecY from Thermus thermophilus comprises 10 transmembrane helices that form an hourglass-shaped protein-conducting channel with a lateral gate. The channel is sealed on the periplasmic side by a plug helix and on the cytoplasmic side by the [SECG](/xray-mp-wiki/proteins/secg) loop. The lateral gate, formed by TM2, TM7, and TM8, opens laterally to allow signal peptides and nascent polypeptides to exit the channel into the lipid bilayer.


## Publications

### doi/10.1016##j.celrep.2015.10.025

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5aww">5AWW</a></td>
      <td>2.7 A</td>
      <td>I222</td>
      <td>Thermus thermophilus SecY (R252G mutation); part of full-length SecYEG heterotrimer; expressed in E. coli BL21(DE3)</td>
      <td>None</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5ch4">5CH4</a></td>
      <td>3.6 A</td>
      <td>C222_1</td>
      <td>Thermus thermophilus SecY (R252G mutation); part of SecYEG heterotrimer in peptide-bound state; expressed in E. coli BL21(DE3)</td>
      <td>SecE N-terminal MFARL peptide contacting lateral gate</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: Thermus thermophilus SecY(R252G)-His6; co-expressed with SecE and SecG from dual plasmid system

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
      <td>Membrane fraction preparation</td>
      <td>Differential centrifugation</td>
      <td>--</td>
      <td>Not specified + --</td>
      <td>Total membrane fraction from E. coli BL21(DE3) cells co-expressing <a href="/xray-mp-wiki/proteins/secyeg">SECYEG</a></td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 0.1 mM <a href="/xray-mp-wiki/reagents/additives/pmsf">PMSF</a> + 2% n-dodecyl-beta-D-maltoside (<a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>)</td>
      <td>1 hr at 4 C; ultracentrifugation at 138,000 x g for 30 min</td>
    </tr>
    <tr>
      <td>Ni-NTA affinity chromatography</td>
      <td>Affinity chromatography (His-tag on SecY)</td>
      <td>Ni-NTA agarose</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Equilibration with 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a>; wash with 40 mM imidazole; elution with 300 mM imidazole</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td>Superdex 200 10/300 GL column</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Concentrated to ~15 mg/ml using Amicon Ultra 50-kDa cutoff filter</td>
    </tr>
    <tr>
      <td>Ion-exchange chromatography</td>
      <td>Ion-exchange chromatography</td>
      <td>HiTrap SP HP column</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 0.25% n-decyl-beta-D-maltoside (DM), 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a> + 0.25% DM</td>
      <td>Elution with linear gradient of 0-100% elution buffer (1 M NaCl, 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 0.25% DM, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>)</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified <a href="/xray-mp-wiki/proteins/secyeg">SECYEG</a> complex (~15 mg/ml) mixed with liquefied <a href="/xray-mp-wiki/reagents/lipids/monoolein">Monoolein</a> at 2:3 protein-to-lipid ratio (w/w)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>About 10 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Cryocooled to 100 K for X-ray data collection</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>I222 space group; resting state structure at 2.7 A resolution</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5aww">5AWW</a> — Chain Y (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">M</span><span class="topo-unknown">VKAFWSALQ</span><span class="topo-outside">IPELRQRVLFT</span><span class="topo-membrane">LLVLAAYRLGAFI</span><span class="topo-inside">PTPGVDLDKIQEFLRTAQGGVFGIINLFSGGNFERFS</span><span class="topo-membrane">IFALGIMPYITAAIIM</span><span class="topo-outside">QILVTVVPALEKLSKEGEEGRRIINQY</span><span class="topo-membrane">TRIGGI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ALGAFQGF</span><span class="topo-inside">FLATAFLGAEGGRFLLPGWSPGPFFWFVVV</span><span class="topo-membrane">VTQVAGIALLLWMA</span><span class="topo-outside">ERITEYGIGNG</span><span class="topo-membrane">TSLIIFAGIVVEWLPQIL</span><span class="topo-inside">RTIGLIRTGEVNLV</span><span class="topo-membrane">AFLFFLAFIVLAFAGM</span><span class="topo-outside">AAVQQAERR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">IPVQYARKVVGGRVYGGQATYIPIKLNAAGV</span><span class="topo-membrane">IPIIFAAAILQIPIFL</span><span class="topo-inside">AAPFQDNPVLQGIANFFNPTRP</span><span class="topo-membrane">SGLFIEVLLVILF</span><span class="topo-outside">TYVYTAVQFDPKRIAESLREYGGFIPGIRPGEPTVKFL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440    </span>
<span class="topo-line"><span class="topo-outside">EHIVSRLTLWGAL</span><span class="topo-membrane">FLGLVTLLPQIIQ</span><span class="topo-inside">NLTGIHS</span><span class="topo-membrane">IAFSGIGLLIVVGVA</span><span class="topo-outside">LDTLRQVESQLMLRSY</span><span class="topo-unknown">EGFLSRGRLRGRNRHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (23 regions)</summary>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>10</td>
      <td>2</td>
      <td>10</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>21</td>
      <td>11</td>
      <td>21</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>22</td>
      <td>34</td>
      <td>22</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>71</td>
      <td>35</td>
      <td>71</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>87</td>
      <td>72</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>114</td>
      <td>88</td>
      <td>114</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>128</td>
      <td>115</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>158</td>
      <td>129</td>
      <td>158</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>172</td>
      <td>159</td>
      <td>172</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>173</td>
      <td>183</td>
      <td>173</td>
      <td>183</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>201</td>
      <td>184</td>
      <td>201</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>202</td>
      <td>215</td>
      <td>202</td>
      <td>215</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>231</td>
      <td>216</td>
      <td>231</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>271</td>
      <td>232</td>
      <td>271</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>272</td>
      <td>287</td>
      <td>272</td>
      <td>287</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>288</td>
      <td>309</td>
      <td>288</td>
      <td>309</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>322</td>
      <td>310</td>
      <td>322</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>323</td>
      <td>373</td>
      <td>323</td>
      <td>373</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>374</td>
      <td>386</td>
      <td>374</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>393</td>
      <td>387</td>
      <td>393</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>394</td>
      <td>408</td>
      <td>394</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>424</td>
      <td>409</td>
      <td>424</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5aww">5AWW</a> — Chain E (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60</span>
<span class="topo-line"><span class="topo-outside">M</span><span class="topo-unknown">FARLIRYFQEARAELA</span><span class="topo-outside">RVTWPTREQVVEGTQAI</span><span class="topo-membrane">LLFTLAFMVILGLYDTVF</span><span class="topo-inside">RFLIGLLR</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>17</td>
      <td>2</td>
      <td>17</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>18</td>
      <td>34</td>
      <td>18</td>
      <td>34</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>52</td>
      <td>35</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>53</td>
      <td>60</td>
      <td>53</td>
      <td>60</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5aww">5AWW</a> — Chain G (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70     </span>
<span class="topo-line"><span class="topo-inside">MDLLYTLVIL</span><span class="topo-membrane">FYLGVAGLLVYLVL</span><span class="topo-outside">VQEPKQGAGDLMGGSADLFSARGVTGGLYR</span><span class="topo-membrane">LTVILGVVFAALA</span><span class="topo-inside">LVIGLWPR</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>24</td>
      <td>11</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>54</td>
      <td>25</td>
      <td>54</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>67</td>
      <td>55</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>68</td>
      <td>75</td>
      <td>68</td>
      <td>75</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ch4">5CH4</a> — Chain Y (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MVKAFWSALQIPELRQRV</span><span class="topo-membrane">LFTLLVLAAYRLGAFI</span><span class="topo-outside">PTPGVD</span><span class="topo-unknown">LDKIQEF</span><span class="topo-outside">LRTAQGGVFGIINLFSGGNFERFS</span><span class="topo-membrane">IFALGIMPYITAAIIM</span><span class="topo-inside">QILVTVVPALEKLSKEGEEGRRIINQY</span><span class="topo-membrane">TRIGGI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ALGAFQGFFL</span><span class="topo-outside">ATAFLGAEGGRFLLPGWSPGPFFWFVV</span><span class="topo-membrane">VVTQVAGIALLLWMAERI</span><span class="topo-inside">TEYGIGNG</span><span class="topo-membrane">TSLIIFAGIVVEWLPQIL</span><span class="topo-outside">RTIGLIRTGEVNLV</span><span class="topo-membrane">AFLFFLAFIVLAFAGM</span><span class="topo-inside">AAVQQAERR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">IPVQYARGAAGYGGQATYIPIKLNAAGV</span><span class="topo-membrane">IPIIFAAAILQIPIFLA</span><span class="topo-outside">APFQDNPVLQGI</span><span class="topo-membrane">ANFFNPTRPSGLFIEVLLVILF</span><span class="topo-inside">TYVYTAVQFDPKRIAESLREYGGFIPGIRPGEPTVKFLEHI</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440 </span>
<span class="topo-line"><span class="topo-inside">VSRLTLWGAL</span><span class="topo-membrane">FLGLVTLLPQIIQNLT</span><span class="topo-outside">GI</span><span class="topo-membrane">HSIAFSGIGLLIVVGVA</span><span class="topo-inside">LDTLRQVESQLMLRSY</span><span class="topo-unknown">EGFLSRGRLRGRNRHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (23 regions)</summary>
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
      <td>18</td>
      <td>1</td>
      <td>18</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>34</td>
      <td>19</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>40</td>
      <td>35</td>
      <td>40</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>47</td>
      <td>41</td>
      <td>47</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>48</td>
      <td>71</td>
      <td>48</td>
      <td>71</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>87</td>
      <td>72</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>114</td>
      <td>88</td>
      <td>114</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>130</td>
      <td>115</td>
      <td>130</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>131</td>
      <td>157</td>
      <td>131</td>
      <td>157</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>175</td>
      <td>158</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>176</td>
      <td>183</td>
      <td>176</td>
      <td>183</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>201</td>
      <td>184</td>
      <td>201</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>202</td>
      <td>215</td>
      <td>202</td>
      <td>215</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>231</td>
      <td>216</td>
      <td>231</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>232</td>
      <td>268</td>
      <td>232</td>
      <td>271</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>269</td>
      <td>285</td>
      <td>272</td>
      <td>288</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>286</td>
      <td>297</td>
      <td>289</td>
      <td>300</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>298</td>
      <td>319</td>
      <td>301</td>
      <td>322</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>320</td>
      <td>370</td>
      <td>323</td>
      <td>373</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>371</td>
      <td>386</td>
      <td>374</td>
      <td>389</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>388</td>
      <td>390</td>
      <td>391</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>389</td>
      <td>405</td>
      <td>392</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>406</td>
      <td>421</td>
      <td>409</td>
      <td>424</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ch4">5CH4</a> — Chain E (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60</span>
<span class="topo-line"><span class="topo-inside">MFARLIRYFQEARAELARVTWPTREQVVEGTQAI</span><span class="topo-membrane">LLFTLAFMVILGLYDTVF</span><span class="topo-outside">RFLIGLLR</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>34</td>
      <td>1</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>52</td>
      <td>35</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>53</td>
      <td>60</td>
      <td>53</td>
      <td>60</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ch4">5CH4</a> — Chain G (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70     </span>
<span class="topo-line"><span class="topo-outside">MDLLYTLVIL</span><span class="topo-membrane">FYLGVAGLLVYLVLV</span><span class="topo-inside">QEPKQGAGDLMGGSADLFSARGVTGGL</span><span class="topo-membrane">YRLTVILGVVFAALA</span><span class="topo-outside">LVIGLWP</span><span class="topo-unknown">R</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>25</td>
      <td>11</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>52</td>
      <td>26</td>
      <td>52</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>67</td>
      <td>53</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>68</td>
      <td>74</td>
      <td>68</td>
      <td>74</td>
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

### Hourglass-shaped protein-conducting channel

SecY forms an hourglass-shaped channel through its pseudo-symmetrically related N-terminal and C-terminal halves, each contributing 5 transmembrane helices. The constricting region, the pore ring, consists of six conserved hydrophobic residues (I77, I81, T184, I188, I275, I403 in Thermus thermophilus numbering) that create a narrow constriction likely permitting membrane permeability while restricting ion flux. The channel is sealed on the periplasmic side by a plug helix and on the cytoplasmic side by the [SECG](/xray-mp-wiki/proteins/secg) loop, preventing uncontrolled membrane leakage.

### Lateral gate mechanism for substrate access

TM2, TM7, and TM8 of SecY form a cytoplasmic hydrophobic crack and a following rift, termed the lateral gate. This gate opens laterally to allow signal peptides and nascent polypeptide chains to exit the channel into the lipid bilayer. In the resting state, the lateral gate is closed. In the peptide-bound state, the cytoplasmic crack is expanded, with the N-terminal MFARL segment of [SECE](/xray-mp-wiki/proteins/sece) inserting into the crack, demonstrating how peptide binding induces lateral gate opening. This mechanism is conserved across bacterial and eukaryotic Sec translocons.


## Cross-References

- <a href="/xray-mp-wiki/proteins/secretion-translocon/secyeg/">Thermus thermophilus SecYEG Translocon Complex</a> — SecY is the core channel-forming subunit of the SecYEG heterotrimer
- <a href="/xray-mp-wiki/proteins/secretion-translocon/sece/">Thermus thermophilus SecE Accessory Subunit</a> — SecE essential accessory subunit that stabilizes SecY in the SecYEG complex
- <a href="/xray-mp-wiki/proteins/secretion-translocon/secg/">Thermus thermophilus SecG Accessory Subunit</a> — SecG accessory subunit that covers the cytoplasmic side of the SecY channel
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Primary lipid component for LCP crystallization of SecYEG
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — Crystallization method used for SecYEG structure determination
- <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> — Main buffer component in purification
- <a href="/xray-mp-wiki/reagents/additives/pmsf">PMSF</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a> — Cryoprotectant and buffer additive
- <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> — Detergent used in solubilization and purification
- <a href="/xray-mp-wiki/reagents/buffers/mops">MOPS</a> — Crystallization buffer component
