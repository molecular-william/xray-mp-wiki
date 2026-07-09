---
title: "Thermus thermophilus SecYEG Translocon Complex"
created: 2026-05-27
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.celrep.2015.10.025, doi/10.1038##nature07421]
verified: regex
uniprot_id: ['P38383', 'Q5SHE6', 'Q5SHQ8']
---

# Thermus thermophilus SecYEG Translocon Complex

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P38383">UniProt: P38383</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q5SHE6">UniProt: Q5SHE6</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q5SHQ8">UniProt: Q5SHQ8</a>

<span class="expr-badge">Thermus thermophilus</span>

## Overview

The SecYEG translocon from Thermus thermophilus is a heterotrimeric protein-conducting channel that mediates protein translocation across the bacterial plasma membrane and integration of membrane proteins. The complex comprises [SECY](/xray-mp-wiki/proteins/secy) (core channel-forming subunit with 10 transmembrane helices), [SECE](/xray-mp-wiki/proteins/sece) (essential accessory subunit that stabilizes SecY), and [SECG](/xray-mp-wiki/proteins/secg) (accessory subunit with 2 transmembrane helices and a large cytoplasmic loop). The 2008 structure of SecYE (without SecG) at 3.2 A revealed a 'pre-open' state of the translocon in complex with an anti-SecY Fab fragment, showing how SecA binding induces conformational changes. The 2015 structures at 2.7 A (resting) and 3.6 A (peptide-bound) further elucidated the complete SecYEG architecture in a lipidic cubic phase environment using [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein).


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
      <td>Full-length Thermus thermophilus SecYEG complex; SecY(R252G)-His6, SecE, SecG; expressed in E. coli BL21(DE3)</td>
      <td>None</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5ch4">5CH4</a></td>
      <td>3.6 A</td>
      <td>C222_1</td>
      <td>Full-length Thermus thermophilus SecYEG complex with peptide-bound state; SecY(R252G)-His6, SecE, SecG; expressed in E. coli BL21(DE3)</td>
      <td>SecE N-terminal MFARL peptide</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: Thermus thermophilus SecY(R252G)-His6, SecE, SecG co-expressed from two plasmids (pAK22/pAK24); SecY contains R252G mutation in periplasmic loop

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
      <td>Total membrane fraction from E. coli BL21(DE3) cells co-expressing <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Sec</a>YEG</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 0.1 mM <a href="/xray-mp-wiki/reagents/additives/pmsf">PMSF</a> + 2% <a href="/xray-mp-wiki/reagents/detergents/ddm">n-dodecyl-beta-D-maltoside</a> (<a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>)</td>
      <td>1 hr at 4 C; ultracentrifugation at 138,000 x g for 30 min</td>
    </tr>
    <tr>
      <td>Ni-NTA affinity chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity chromatography</a> (<a href="/xray-mp-wiki/reagents/protein-tags/his-tag">His-tag</a>)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA agarose</a></td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Equilibration with 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a>; wash with 40 mM imidazole; elution with 300 mM imidazole</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Size-exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/resins/superdex-200">Superdex 200</a> 10/300 GL column</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Concentrated to ~15 mg/ml using Amicon Ultra 50-kDa cutoff filter</td>
    </tr>
    <tr>
      <td>Ion-exchange chromatography</td>
      <td>Ion-exchange chromatography</td>
      <td>HiTrap SP HP column</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 0.25% n-decyl-beta-D-maltoside (<a href="/xray-mp-wiki/reagents/detergents/dm">DM</a>), 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a> + 0.25% <a href="/xray-mp-wiki/reagents/detergents/dm">DM</a></td>
      <td>Elution with linear gradient of 0-100% elution buffer (1 M NaCl, 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 0.25% <a href="/xray-mp-wiki/reagents/detergents/dm">DM</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>); final sample dialyzed against 0.25% <a href="/xray-mp-wiki/reagents/detergents/dm">DM</a> and 5% glycerol</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">Lipidic cubic phase</a> crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Sec</a>YEG (~15 mg/ml) mixed with liquefied <a href="/xray-mp-wiki/reagents/lipids/monoolein">Monoolein</a> at 2:3 protein-to-lipid ratio (w/w)</td>
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
      <td>I222 space group; resting state structure at 2.7 A resolution; crystals grown using glass sandwich plates</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">Lipidic cubic phase</a> crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Sec</a>YEG mixed with liquefied <a href="/xray-mp-wiki/reagents/lipids/monoolein">Monoolein</a> at defined protein-to-lipid ratio</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Cryocooled to 100 K for X-ray data collection</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>C222_1 space group; peptide-bound state structure at 3.6 A resolution</td>
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
### doi/10.1038##nature07421

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2zjs">2ZJS</a></td>
      <td>3.2 A</td>
      <td>Not specified in paper</td>
      <td>Full-length Thermus thermophilus SecY(L2V/R252E) with C-terminal His6-tag (auto-cleaved), SecE; complexed with anti-SecY Fab fragment</td>
      <td>None (apo-SecYE in pre-open state)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: Thermus thermophilus SecY(R252G)-His6, SecE, SecG co-expressed from two plasmids (pAK22/pAK24); SecY contains R252G mutation in periplasmic loop

**Purification:**

- **Expression system**: Escherichia coli
- **Expression construct**: Full-length T. thermophilus SecY(L2V/R252E)-His6, SecE; co-expressed from two plasmids (pTT159/pSTD343)
- **Tag info**: C-terminal His6-tag on SecY; auto-cleaved during storage at 20 C for 2 weeks

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
      <td>Total membrane fraction from E. coli cells overproducing <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Sec</a>YE</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>Not specified + <a href="/xray-mp-wiki/reagents/detergents/ddm">n-dodecyl-beta-D-maltoside</a> (<a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>)</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Sec</a>YE complex solubilized from membrane fraction with <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
    </tr>
    <tr>
      <td>Purification</td>
      <td>Column chromatography (three steps)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> + gel filtration</td>
      <td>Not specified + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Three successive chromatography steps; His6-tag auto-cleaved after storage at 20 C for 2 weeks; re-chromatographed on <a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a></td>
    </tr>
    <tr>
      <td>Fab complex purification</td>
      <td>Gel filtration chromatography</td>
      <td>Gel filtration column</td>
      <td>Not specified + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Sec</a>YE mixed with stoichiometric excess of Fab; complex isolated by gel filtration</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor diffusion</a> crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified Fab-SecYE complex</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Cryocooled to 100 K for X-ray data collection at SPring-8 and PF</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Structure determined by <a href="/xray-mp-wiki/methods/phasing/multiple-anomalous-dispersion">MAD</a> method using SeMet-labelled <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Sec</a>YE crystals. Refined to Rwork/Rfree of 24.4%/28.0% at 3.2 A resolution. Asymmetric unit contains one Fab-SecYE complex. Data collected at beamline BL41XU (SPring-8) and NW12 (PF).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2zjs">2ZJS</a> — Chain Y (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MV</span><span class="topo-unknown">KAFWSAL</span><span class="topo-inside">QIPELRQRV</span><span class="topo-membrane">LFTLLVLAAYRLGAFI</span><span class="topo-outside">PTPGVD</span><span class="topo-unknown">LDKIQEFLR</span><span class="topo-outside">TAQGGVFGIINLFSGGNFERFS</span><span class="topo-membrane">IFALGIMPYITAAIIM</span><span class="topo-inside">QILVTVV</span><span class="topo-unknown">PALEKLS</span><span class="topo-inside">KEGEEGRRIINQY</span><span class="topo-membrane">TRIGGI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ALGAFQGFFL</span><span class="topo-outside">ATAFLGAEGGRFLLPGWSPGPFFWFVV</span><span class="topo-membrane">VVTQVAGIALLLWMAERI</span><span class="topo-inside">TEYGIGN</span><span class="topo-membrane">GTSLIIFAGIVVEWLPQIL</span><span class="topo-outside">RTIGLIRTGEVNL</span><span class="topo-membrane">VAFLFFLAFIVLAFAGM</span><span class="topo-inside">AAVQQAERR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">IPVQYAR</span><span class="topo-unknown">KVVGGRV</span><span class="topo-inside">YGGQATYIPIKLNAAGV</span><span class="topo-membrane">IPIIFAAAILQIPIFLA</span><span class="topo-outside">APFQDNPVLQGIANF</span><span class="topo-membrane">FNPTRPSGLFIEVLLVILFT</span><span class="topo-inside">YVYTAVQFDPKRIAESLREYGGFIPGIRPGEPTVKFL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430    </span>
<span class="topo-line"><span class="topo-inside">EHIVSRLTLWGA</span><span class="topo-membrane">LFLGLVTLLPQIIQNLT</span><span class="topo-outside">GIH</span><span class="topo-membrane">SIAFSGIGLLIVVGVA</span><span class="topo-inside">LDTLRQVESQLMLR</span><span class="topo-unknown">SYEGFLSRGRLR</span></span>
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
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>9</td>
      <td>3</td>
      <td>9</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>18</td>
      <td>10</td>
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
      <td>49</td>
      <td>41</td>
      <td>49</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>50</td>
      <td>71</td>
      <td>50</td>
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
      <td>94</td>
      <td>88</td>
      <td>94</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>101</td>
      <td>95</td>
      <td>101</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>102</td>
      <td>114</td>
      <td>102</td>
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
      <td>182</td>
      <td>176</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>201</td>
      <td>183</td>
      <td>201</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>202</td>
      <td>214</td>
      <td>202</td>
      <td>214</td>
      <td>Outside</td>
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
      <td>247</td>
      <td>232</td>
      <td>247</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>254</td>
      <td>248</td>
      <td>254</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>255</td>
      <td>271</td>
      <td>255</td>
      <td>271</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>272</td>
      <td>288</td>
      <td>272</td>
      <td>288</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>289</td>
      <td>303</td>
      <td>289</td>
      <td>303</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>304</td>
      <td>323</td>
      <td>304</td>
      <td>323</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>324</td>
      <td>372</td>
      <td>324</td>
      <td>372</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>373</td>
      <td>389</td>
      <td>373</td>
      <td>389</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>390</td>
      <td>392</td>
      <td>390</td>
      <td>392</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>393</td>
      <td>408</td>
      <td>393</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>422</td>
      <td>409</td>
      <td>422</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>423</td>
      <td>434</td>
      <td>423</td>
      <td>434</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2zjs">2ZJS</a> — Chain E (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60</span>
<span class="topo-line"><span class="topo-unknown">MFARLIRYFQE</span><span class="topo-inside">ARAELARVTWPTREQVVEGT</span><span class="topo-membrane">QAILLFTLAFMVILGLYDTVF</span><span class="topo-outside">RFLIG</span><span class="topo-unknown">LLR</span></span>
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
      <td>11</td>
      <td>1</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>31</td>
      <td>12</td>
      <td>31</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>52</td>
      <td>32</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>53</td>
      <td>57</td>
      <td>53</td>
      <td>57</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>60</td>
      <td>58</td>
      <td>60</td>
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

### Cytoplasmic SecG loop covers and seals the protein-conducting channel

The cytoplasmic loop of [SECG](/xray-mp-wiki/proteins/secg) covers the hourglass-shaped [SECY](/xray-mp-wiki/proteins/secy) channel exactly over the pore ring, contributing to channel sealing on the cytoplasmic side. The pore ring consists of six conserved residues (I77, I81, T184, I188, I275, I403 in Thermus thermophilus numbering) that likely maintain membrane permeability. Disulfide bond formation analysis and molecular dynamics simulations confirmed that the SecG loop covers the channel in the membrane environment. This arrangement prevents uncontrolled ion flux while allowing regulated protein translocation.

### Peptide-bound structure reveals lateral gate opening mechanism

The peptide-bound structure (PDB 5CH4) reveals a previously unknown state where the N-terminal MFARL segment of [SECE](/xray-mp-wiki/proteins/sece) inserts into the hydrophobic crack of another [SECY](/xray-mp-wiki/proteins/secy) monomer, expanding the cytoplasmic crack between TM2 and TM8. The hydrophobic side chains of F2 and A3 interact with I85, I89, and F322 on the cytoplasmic hydrophobic crack of SecY, while R4 interacts with conserved Q88. This mimics the early stage of signal peptide binding to the lateral gate, providing structural insight into how signal peptides induce lateral gate opening during protein translocation.

### Resting state structure at high resolution reveals complete SecYEG architecture

The 2.7 A structure of the resting state (PDB 5AWW) elucidates the detailed architecture of the intact SecYEG complex including all three subunits. [SECY](/xray-mp-wiki/proteins/secy) forms an hourglass-shaped channel with ten transmembrane helices; [SECE](/xray-mp-wiki/proteins/sece) is located at the back of SecY and stabilizes the complex; [SECG](/xray-mp-wiki/proteins/secg) comprises two transmembrane helices tightly bound to SecY through hydrophobic interactions. The plug helix seals the periplasmic side of the channel while the SecG loop covers the cytoplasmic side. The lateral gate formed by TM2, TM7, and TM8 of SecY is in a closed conformation. The crystal packing revealed a possible 2-fold symmetric dimer that differs from previously proposed dimer arrangements.

### Crystallographic asymmetric unit contains monomer with crystallographic dimer

Although both crystallographic asymmetric units contain one SecYEG complex, the packing arrangement shows a possible 2-fold symmetric dimer of SecYEG in the lipid bilayer. This dimer association pattern differs from previously proposed face-to-face or back-to-back SecYEG dimers. Due to the lack of direct transmembrane interaction between SecYEG units, the dimer architecture does not appear to be stable in the cytoplasmic membrane, supporting the notion that SecYEG functions as a monomer during co-/post-translational translocation.

### Pre-open state of SecYE revealed by Fab complex structure

The 3.2 A crystal structure of T. thermophilus SecYE in complex with an anti-SecY Fab fragment revealed a 'pre-open' state distinct from the closed state of M. jannaschii SecYEbeta. In this state, TM2, TM7, and TM8 are shifted to create a hydrophobic crack open to the cytoplasm, lined by evolutionarily conserved hydrophobic residues (Ile85, Pro273, Phe276, Ala279). The Fab fragment binds to the Pro-Gly-Ile-Arg-Pro-Gly motif in the C5 cytoplasmic domain of SecY. Molecular dynamics simulations (100 ns) showed that SecYE undergoes large conformational changes from the pre-open toward the closed state, indicating the closed form is the energetically favored ground state.

### SecA induces conformational transition of SecYE

Intermolecular disulfide cross-linking experiments identified the SecA-SecY interface: SecA(Pro202) contacts SecY(Ala259) in C4, and SecA(Leu775) contacts SecY(Pro352) in C5. The motif IV region of SecA (residues 180-188) becomes surface-exposed upon translocon binding, enabling activation of SecA ATPase. SecA binding to SecYE reduced the 92-329 intramolecular disulfide bond formation in membranembedded SecYE, suggesting SecA facilitates the transition from closed to pre-open state. The swinging of TM8 may initiate channel gate opening through exposure of the hydrophobic crack.


## Cross-References

- <a href="/xray-mp-wiki/proteins/secretion-translocon/thermotoga-maritima-seca/">Thermotoga maritima SecA ATPase</a> — SecA is the cytoplasmic ATPase motor that binds SecYEG to drive protein translocation
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Primary lipid component for LCP crystallization matrix
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltoside (DDM)</a> — Primary solubilization detergent used for membrane protein extraction
- <a href="/xray-mp-wiki/reagents/detergents/dm/">n-Decyl-beta-D-maltoside (DM)</a> — Mild detergent used for crystallization sample preparation and ion-exchange chromatography
- <a href="/xray-mp-wiki/reagents/buffers/mops/">MOPS (3-(N-morpholino)propanesulfonic acid)</a> — Crystallization reservoir buffer component
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA Agarose Resin</a> — Affinity chromatography resin for His-tagged SecY purification
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200 Increase SEC Resin</a> — Size-exclusion chromatography for complex purification and monodispersity assessment
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — Crystallization method used for both SecYEG structures
- <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> — Main buffer component in purification
- <a href="/xray-mp-wiki/reagents/additives/pmsf">PMSF</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/proteins/sece">SECE</a> — Related protein
