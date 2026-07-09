---
title: "Human Serotonin Transporter (SERT)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature17629, doi/10.1038##s41594-018-0026-8]
verified: regex
uniprot_id: P31645
---

# Human Serotonin Transporter (SERT)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span> <span class="expr-badge expr-hek293">HEK293</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P31645">UniProt: P31645</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

The human [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki/reagents/ligands/serotonin/) transporter (SERT, also known as SLC6A4) is a [Neurotransmitter/Sodium Symporter (NSS) Family](/xray-mp-wiki/concepts/transport-mechanisms/nss-family/) member that terminates serotonergic signalling through the Na+/Cl--coupled reuptake of [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki/reagents/ligands/serotonin/) (5-HT) from the synaptic cleft into presynaptic neurons. SERT is a primary target for antidepressant drugs including selective [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki/reagents/ligands/serotonin/) reuptake inhibitors (SSRIs) such as (S)-citalopram and [Paroxetine](/xray-mp-wiki/reagents/ligands/paroxetine/), as well as psychostimulants. X-ray crystal structures of human SERT bound to antidepressants revealed how diverse SSRIs lock the transporter in an outward-open conformation and identified an allosteric site at the extracellular vestibule.


## Publications

### doi/10.1038##nature17629

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5i6x">5I6X</a></td>
      <td>3.14</td>
      <td>C222_1</td>
      <td>SERT ts3 — human SERT with thermostabilizing mutations Y110A, I291A, T439S, surface cysteine mutations C554A, C580A, C622A, fused to C-terminal GFP, twin Strep tag, and His10 tag; complexed with <a href="/xray-mp-wiki/reagents/ligands/paroxetine/">Paroxetine</a> and 8B6 Fab</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/paroxetine/">Paroxetine</a>, <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, N-acetylglucosamine, Na+, Cl-, 8B6 Fab</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5i6x">5I6X</a></td>
      <td>3.15</td>
      <td>C222_1</td>
      <td>SERT ts3 — human SERT with thermostabilizing mutations Y110A, I291A, T439S, surface cysteine mutations C554A, C580A, C622A; complexed with (S)-citalopram and 8B6 Fab</td>
      <td>(S)-citalopram (central site and allosteric site), <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, N-acetylglucosamine, Na+, Cl-, 8B6 Fab</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5i6x">5I6X</a></td>
      <td>4.53</td>
      <td>C222_1</td>
      <td>SERT ts2 — human SERT with thermostabilizing mutations I291A, T439S, surface cysteine mutations C554A, C580A, C622A; complexed with <a href="/xray-mp-wiki/reagents/ligands/paroxetine/">Paroxetine</a> and 8B6 Fab</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/paroxetine/">Paroxetine</a>, <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, N-acetylglucosamine, Na+, Cl-, 8B6 Fab</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293S GnT- cells via baculovirus-mediated transduction (BacMam)
- **Construct**: C-terminal GFP fusion with twin Strep and His10 tags, thrombin cleavage sites
- **Notes**: SERT ts2 and ts3 variants derived from human SERT gene

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
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td></td>
      <td>50 mM Tris pH 8, 150 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 2.5 mM <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 0.5 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a>, 1 uM inhibitor + 20 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Membranes harvested and solubilized</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Strep-Tactin <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Strep-Tactin resin</td>
      <td>20 mM Tris pH 8, 150 mM NaCl, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Large-scale purification of SERT</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM Tris pH 8, 150 mM NaCl, 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.1 mM <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> + 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Monodisperse fractions collected</td>
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
      <td>SERT ts3-<a href="/xray-mp-wiki/reagents/ligands/paroxetine/">Paroxetine</a> complex with 8B6 Fab</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Outward-open conformation, C222_1 space group</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>SERT ts3-(S)-citalopram complex with 8B6 Fab</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>(S)-citalopram bound to both central and allosteric sites</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5i6x">5I6X</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">GSQGERETWGKKV</span><span class="topo-membrane">DFLLSVIGYAVDLGNV</span><span class="topo-outside">WRFPYICAQNGGGAFL</span><span class="topo-membrane">LPYTIMAIFGGIPLFY</span><span class="topo-inside">MELALGQYHRNGCISIWRKICPIFKGIGYA</span><span class="topo-membrane">ICIIAFYIASYYNTIMAWAL</span><span class="topo-outside">YYLISSFTD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">QLPWTSCKNSWNTGNCTNYFSEDNITWTLHSTSPAEEFYTRHVLQIHRSKGLQDLGG</span><span class="topo-membrane">ISWQLALCIMLIFTVIYFSI</span><span class="topo-inside">WKGVKT</span><span class="topo-membrane">SGKVVWVTATFPYIAL</span><span class="topo-outside">SVLLVRGATLPGAWRGVLFYL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">KPNWQKLLETGVW</span><span class="topo-membrane">IDAAAQIFFSLGPGFGVL</span><span class="topo-inside">LAFASYNKFNNNCYQ</span><span class="topo-membrane">DALVTSVVNCMTSFVS</span><span class="topo-outside">GFVIFTVLGYMAEMRNEDVSEVAKDAGPSLLFITYAEAIANMPASTFFAIIFFL</span><span class="topo-membrane">MLIT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LGLDSSFAGLEGV</span><span class="topo-inside">ITAVLDEFPHVWAKRRERFV</span><span class="topo-membrane">LAVVITCFFGSLVTLT</span><span class="topo-outside">FGGAYV</span><span class="topo-membrane">VKLLEEYATGPAVLTVALI</span><span class="topo-inside">EAVAVSWFYGITQFCRDVKEMLGFSPGWFWRI</span><span class="topo-membrane">CWVAISPLFLLFII</span></span>
<span class="topo-ruler">       490       500       510       520       530       540         </span>
<span class="topo-line"><span class="topo-membrane">ASFLMSP</span><span class="topo-outside">PQLRLFQYNYPYW</span><span class="topo-membrane">SIILGYAIGTSSFI</span><span class="topo-inside">CIPTYIAYRLIITPGTFKERIIKSITPETP</span><span class="topo-unknown">TLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (25 regions)</summary>
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
      <td>74</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>29</td>
      <td>87</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>45</td>
      <td>103</td>
      <td>118</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>61</td>
      <td>119</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>91</td>
      <td>135</td>
      <td>164</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>111</td>
      <td>165</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>177</td>
      <td>185</td>
      <td>250</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>197</td>
      <td>251</td>
      <td>270</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>203</td>
      <td>271</td>
      <td>276</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>219</td>
      <td>277</td>
      <td>292</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>253</td>
      <td>293</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>254</td>
      <td>271</td>
      <td>327</td>
      <td>344</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>286</td>
      <td>345</td>
      <td>359</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>302</td>
      <td>360</td>
      <td>375</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>303</td>
      <td>356</td>
      <td>376</td>
      <td>429</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>357</td>
      <td>373</td>
      <td>430</td>
      <td>446</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>393</td>
      <td>447</td>
      <td>466</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>394</td>
      <td>409</td>
      <td>467</td>
      <td>482</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>415</td>
      <td>483</td>
      <td>488</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>416</td>
      <td>434</td>
      <td>489</td>
      <td>507</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>435</td>
      <td>466</td>
      <td>508</td>
      <td>539</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>467</td>
      <td>487</td>
      <td>540</td>
      <td>560</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>488</td>
      <td>500</td>
      <td>561</td>
      <td>573</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>501</td>
      <td>514</td>
      <td>574</td>
      <td>587</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>515</td>
      <td>544</td>
      <td>588</td>
      <td>617</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5i6x">5I6X</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">GSQGERETWGKKV</span><span class="topo-membrane">DFLLSVIGYAVDLGNV</span><span class="topo-outside">WRFPYICAQNGGGAFL</span><span class="topo-membrane">LPYTIMAIFGGIPLFY</span><span class="topo-inside">MELALGQYHRNGCISIWRKICPIFKGIGYA</span><span class="topo-membrane">ICIIAFYIASYYNTIMAWAL</span><span class="topo-outside">YYLISSFTD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">QLPWTSCKNSWNTGNCTNYFSEDNITWTLHSTSPAEEFYTRHVLQIHRSKGLQDLGG</span><span class="topo-membrane">ISWQLALCIMLIFTVIYFSI</span><span class="topo-inside">WKGVKT</span><span class="topo-membrane">SGKVVWVTATFPYIAL</span><span class="topo-outside">SVLLVRGATLPGAWRGVLFYL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">KPNWQKLLETGVW</span><span class="topo-membrane">IDAAAQIFFSLGPGFGVL</span><span class="topo-inside">LAFASYNKFNNNCYQ</span><span class="topo-membrane">DALVTSVVNCMTSFVS</span><span class="topo-outside">GFVIFTVLGYMAEMRNEDVSEVAKDAGPSLLFITYAEAIANMPASTFFAIIFFL</span><span class="topo-membrane">MLIT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LGLDSSFAGLEGV</span><span class="topo-inside">ITAVLDEFPHVWAKRRERFV</span><span class="topo-membrane">LAVVITCFFGSLVTLT</span><span class="topo-outside">FGGAYV</span><span class="topo-membrane">VKLLEEYATGPAVLTVALI</span><span class="topo-inside">EAVAVSWFYGITQFCRDVKEMLGFSPGWFWRI</span><span class="topo-membrane">CWVAISPLFLLFII</span></span>
<span class="topo-ruler">       490       500       510       520       530       540         </span>
<span class="topo-line"><span class="topo-membrane">ASFLMSP</span><span class="topo-outside">PQLRLFQYNYPYW</span><span class="topo-membrane">SIILGYAIGTSSFI</span><span class="topo-inside">CIPTYIAYRLIITPGTFKERIIKSITPETP</span><span class="topo-unknown">TLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (25 regions)</summary>
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
      <td>74</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>29</td>
      <td>87</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>45</td>
      <td>103</td>
      <td>118</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>61</td>
      <td>119</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>91</td>
      <td>135</td>
      <td>164</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>111</td>
      <td>165</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>177</td>
      <td>185</td>
      <td>250</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>197</td>
      <td>251</td>
      <td>270</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>203</td>
      <td>271</td>
      <td>276</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>219</td>
      <td>277</td>
      <td>292</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>253</td>
      <td>293</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>254</td>
      <td>271</td>
      <td>327</td>
      <td>344</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>286</td>
      <td>345</td>
      <td>359</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>302</td>
      <td>360</td>
      <td>375</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>303</td>
      <td>356</td>
      <td>376</td>
      <td>429</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>357</td>
      <td>373</td>
      <td>430</td>
      <td>446</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>393</td>
      <td>447</td>
      <td>466</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>394</td>
      <td>409</td>
      <td>467</td>
      <td>482</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>415</td>
      <td>483</td>
      <td>488</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>416</td>
      <td>434</td>
      <td>489</td>
      <td>507</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>435</td>
      <td>466</td>
      <td>508</td>
      <td>539</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>467</td>
      <td>487</td>
      <td>540</td>
      <td>560</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>488</td>
      <td>500</td>
      <td>561</td>
      <td>573</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>501</td>
      <td>514</td>
      <td>574</td>
      <td>587</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>515</td>
      <td>544</td>
      <td>588</td>
      <td>617</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5i6x">5I6X</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">GSQGERETWGKKV</span><span class="topo-membrane">DFLLSVIGYAVDLGNV</span><span class="topo-outside">WRFPYICAQNGGGAFL</span><span class="topo-membrane">LPYTIMAIFGGIPLFY</span><span class="topo-inside">MELALGQYHRNGCISIWRKICPIFKGIGYA</span><span class="topo-membrane">ICIIAFYIASYYNTIMAWAL</span><span class="topo-outside">YYLISSFTD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">QLPWTSCKNSWNTGNCTNYFSEDNITWTLHSTSPAEEFYTRHVLQIHRSKGLQDLGG</span><span class="topo-membrane">ISWQLALCIMLIFTVIYFSI</span><span class="topo-inside">WKGVKT</span><span class="topo-membrane">SGKVVWVTATFPYIAL</span><span class="topo-outside">SVLLVRGATLPGAWRGVLFYL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">KPNWQKLLETGVW</span><span class="topo-membrane">IDAAAQIFFSLGPGFGVL</span><span class="topo-inside">LAFASYNKFNNNCYQ</span><span class="topo-membrane">DALVTSVVNCMTSFVS</span><span class="topo-outside">GFVIFTVLGYMAEMRNEDVSEVAKDAGPSLLFITYAEAIANMPASTFFAIIFFL</span><span class="topo-membrane">MLIT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LGLDSSFAGLEGV</span><span class="topo-inside">ITAVLDEFPHVWAKRRERFV</span><span class="topo-membrane">LAVVITCFFGSLVTLT</span><span class="topo-outside">FGGAYV</span><span class="topo-membrane">VKLLEEYATGPAVLTVALI</span><span class="topo-inside">EAVAVSWFYGITQFCRDVKEMLGFSPGWFWRI</span><span class="topo-membrane">CWVAISPLFLLFII</span></span>
<span class="topo-ruler">       490       500       510       520       530       540         </span>
<span class="topo-line"><span class="topo-membrane">ASFLMSP</span><span class="topo-outside">PQLRLFQYNYPYW</span><span class="topo-membrane">SIILGYAIGTSSFI</span><span class="topo-inside">CIPTYIAYRLIITPGTFKERIIKSITPETP</span><span class="topo-unknown">TLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (25 regions)</summary>
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
      <td>74</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>29</td>
      <td>87</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>45</td>
      <td>103</td>
      <td>118</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>61</td>
      <td>119</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>91</td>
      <td>135</td>
      <td>164</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>111</td>
      <td>165</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>177</td>
      <td>185</td>
      <td>250</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>197</td>
      <td>251</td>
      <td>270</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>203</td>
      <td>271</td>
      <td>276</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>219</td>
      <td>277</td>
      <td>292</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>253</td>
      <td>293</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>254</td>
      <td>271</td>
      <td>327</td>
      <td>344</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>286</td>
      <td>345</td>
      <td>359</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>302</td>
      <td>360</td>
      <td>375</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>303</td>
      <td>356</td>
      <td>376</td>
      <td>429</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>357</td>
      <td>373</td>
      <td>430</td>
      <td>446</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>393</td>
      <td>447</td>
      <td>466</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>394</td>
      <td>409</td>
      <td>467</td>
      <td>482</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>415</td>
      <td>483</td>
      <td>488</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>416</td>
      <td>434</td>
      <td>489</td>
      <td>507</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>435</td>
      <td>466</td>
      <td>508</td>
      <td>539</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>467</td>
      <td>487</td>
      <td>540</td>
      <td>560</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>488</td>
      <td>500</td>
      <td>561</td>
      <td>573</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>501</td>
      <td>514</td>
      <td>574</td>
      <td>587</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>515</td>
      <td>544</td>
      <td>588</td>
      <td>617</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##s41594-018-0026-8

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6awn">6AWN</a></td>
      <td>3.62</td>
      <td>C222_1</td>
      <td>SERT ts2 (Thr439) with <a href="/xray-mp-wiki/reagents/ligands/paroxetine/">Paroxetine</a> — human SERT with thermostabilizing mutations I291A, T439S, surface cysteine mutations C554A, C580A, C622A; complexed with <a href="/xray-mp-wiki/reagents/ligands/paroxetine/">Paroxetine</a> and 8B6 Fab</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/paroxetine/">Paroxetine</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6awp">6AWP</a></td>
      <td>3.80</td>
      <td>C222_1</td>
      <td>SERT ts3 with <a href="/xray-mp-wiki/reagents/ligands/fluvoxamine/">Fluvoxamine</a> — human SERT with thermostabilizing mutations Y110A, I291A, T439S, surface cysteine mutations C554A, C580A, C622A; complexed with <a href="/xray-mp-wiki/reagents/ligands/fluvoxamine/">Fluvoxamine</a> and 8B6 Fab</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/fluvoxamine/">Fluvoxamine</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6awo">6AWO</a></td>
      <td>3.53</td>
      <td>C222_1</td>
      <td>SERT ts3 with <a href="/xray-mp-wiki/reagents/ligands/sertraline/">Sertraline</a> — human SERT with thermostabilizing mutations Y110A, I291A, T439S, surface cysteine mutations C554A, C580A, C622A; complexed with <a href="/xray-mp-wiki/reagents/ligands/sertraline/">Sertraline</a> and 8B6 Fab</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/sertraline/">Sertraline</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6awq">6AWQ</a></td>
      <td>4.05</td>
      <td>C222_1</td>
      <td>SERT ts3 with <a href="/xray-mp-wiki/reagents/ligands/sertraline/">Sertraline</a> — human SERT with thermostabilizing mutations Y110A, I291A, T439S, surface cysteine mutations C554A, C580A, C622A; complexed with <a href="/xray-mp-wiki/reagents/ligands/sertraline/">Sertraline</a> and 8B6 Fab (data collected at ALS 5.0.2)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/sertraline/">Sertraline</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293S GnT- cells via baculovirus-mediated transduction (BacMam)
- **Construct**: C-terminal GFP fusion with twin Strep and His10 tags, thrombin cleavage sites
- **Notes**: SERT ts2 and ts3 variants derived from human SERT gene

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
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td></td>
      <td>50 mM Tris pH 8, 150 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 2.5 mM <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> + 20 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>HEK293S GnT- cells solubilized</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Strep-Tactin <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Strep-Tactin resin</td>
      <td>20 mM Tris pH 8, 100 mM NaCl (TBS), 1 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.2 mM <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 25 uM lipid mixture (<a href="/xray-mp-wiki/reagents/lipids/popc/">POPC</a>:<a href="/xray-mp-wiki/reagents/lipids/pope/">POPE</a>:<a href="/xray-mp-wiki/reagents/lipids/popg/">POPG</a> 1:1:1) + 1 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Eluted protein digested by thrombin and <a href="/xray-mp-wiki/reagents/additives/endoh/">ENDOH</a>; combined with 8B6 Fab at 1:1.2 ratio</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td></td>
      <td>TBS supplemented with 40 mM n-octyl beta-D-maltoside, 0.5 mM <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 25 uM lipid mixture (<a href="/xray-mp-wiki/reagents/lipids/popc/">POPC</a>:<a href="/xray-mp-wiki/reagents/lipids/pope/">POPE</a>:<a href="/xray-mp-wiki/reagents/lipids/popg/">POPG</a> 1:1:1) + 40 mM n-octyl beta-D-maltoside</td>
      <td>SERT-8B6 complex purified; concentrated to 2 mg/ml; SSRIs added to 50 uM</td>
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
      <td>SERT-Fab complex (ts2 or ts3) with SSRI inhibitor at 50 uM</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>50-100 mM Tris pH 8.5, 25-75 mM Li2SO4, 25-75 mM Na2SO4, 33.5-36% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400, 0.5% 6-aminohexanoic acid</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals flash cooled directly in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>2 ul protein to 1 ul reservoir ratio</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6awn">6AWN</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">GSQGERETWGKKVDFL</span><span class="topo-membrane">LSVIGYAVDLGNVWRFP</span><span class="topo-outside">YICAQNGGG</span><span class="topo-membrane">AFLLPYTIMAIFGGIPLFY</span><span class="topo-inside">MELALGQYHRNGCISIWRKICPIFKGIGY</span><span class="topo-membrane">AICIIAFYIASYYNTIMAWALYYLI</span><span class="topo-outside">SSFTD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">QLPWTSCKNSWNTGNCTNYFSEDNITWTLHSTSPAEEFYTRHVLQIHRSKGLQDLGGI</span><span class="topo-membrane">SWQLALCIMLIFTVIYFSIW</span><span class="topo-inside">KGVKT</span><span class="topo-membrane">SGKVVWVTATFPYIALSVLLV</span><span class="topo-outside">RGATLPGAWRGVLFYL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">KPNWQKL</span><span class="topo-membrane">LETGVWIDAAAQIFFSLGPGFGVL</span><span class="topo-inside">LAFASYNKFNNNCYQDA</span><span class="topo-membrane">LVTSVVNCMTSFVSGFV</span><span class="topo-outside">IFTVLGYMAEMRNEDVSEVAKDAGPSLLFI</span><span class="topo-unknown">TYAEAIA</span><span class="topo-outside">NMPASTFFAI</span><span class="topo-membrane">IFFLMLIT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LGLDSTFAGLEGV</span><span class="topo-inside">ITAVLDEFPHVWAKRRERFV</span><span class="topo-membrane">LAVVITCFFGSLVTLT</span><span class="topo-outside">FGGAYV</span><span class="topo-membrane">VKLLEEYATGPAVLTVALIEAV</span><span class="topo-inside">AVSWFYGITQFCRDVKEMLGFSPG</span><span class="topo-unknown">WFWRICWV</span><span class="topo-inside">A</span><span class="topo-membrane">ISPLFLLFII</span></span>
<span class="topo-ruler">       490       500       510       520       530       540         </span>
<span class="topo-line"><span class="topo-membrane">ASFLMSPP</span><span class="topo-outside">QLRLFQYNYPYWS</span><span class="topo-membrane">IILGYAIGTSSFICIPT</span><span class="topo-inside">YIAYRLIITPGTFKERIIKSITPETP</span><span class="topo-unknown">TLVPR</span></span>
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
      <td>16</td>
      <td>74</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>33</td>
      <td>90</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>42</td>
      <td>107</td>
      <td>115</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>61</td>
      <td>116</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>90</td>
      <td>135</td>
      <td>163</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>115</td>
      <td>164</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>178</td>
      <td>189</td>
      <td>251</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>198</td>
      <td>252</td>
      <td>271</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>203</td>
      <td>272</td>
      <td>276</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>224</td>
      <td>277</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>225</td>
      <td>247</td>
      <td>298</td>
      <td>320</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>271</td>
      <td>321</td>
      <td>344</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>288</td>
      <td>345</td>
      <td>361</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>289</td>
      <td>305</td>
      <td>362</td>
      <td>378</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>335</td>
      <td>379</td>
      <td>408</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>336</td>
      <td>342</td>
      <td>409</td>
      <td>415</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>343</td>
      <td>352</td>
      <td>416</td>
      <td>425</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>373</td>
      <td>426</td>
      <td>446</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>393</td>
      <td>447</td>
      <td>466</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>394</td>
      <td>409</td>
      <td>467</td>
      <td>482</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>415</td>
      <td>483</td>
      <td>488</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>416</td>
      <td>437</td>
      <td>489</td>
      <td>510</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>438</td>
      <td>461</td>
      <td>511</td>
      <td>534</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>462</td>
      <td>469</td>
      <td>535</td>
      <td>542</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>470</td>
      <td>470</td>
      <td>543</td>
      <td>543</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>488</td>
      <td>544</td>
      <td>561</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>489</td>
      <td>501</td>
      <td>562</td>
      <td>574</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>502</td>
      <td>518</td>
      <td>575</td>
      <td>591</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>519</td>
      <td>544</td>
      <td>592</td>
      <td>617</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6awp">6AWP</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">GSQGERETWGKKV</span><span class="topo-membrane">DFLLSVIGYAVDLGNVWRFP</span><span class="topo-outside">YICAQNGGGA</span><span class="topo-membrane">FLLPYTIMAIFGGIPLFY</span><span class="topo-inside">MELALGQYHRNGCISIWRKICPIFKGIGYA</span><span class="topo-membrane">ICIIAFYIASYYNTIMAWALY</span><span class="topo-outside">YLISSFTD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">QLPWTSCKNSWNTGNCTNYFSEDNITWTLHSTSPAEEFYTRHVLQIHRSKGLQDLGG</span><span class="topo-membrane">ISWQLALCIMLIFTVIYFSI</span><span class="topo-inside">WKGVKT</span><span class="topo-membrane">SGKVVWVTATFPYIALSV</span><span class="topo-outside">LLVRGATLPGAWRGVLFYL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">KPNWQKLLET</span><span class="topo-membrane">GVWIDAAAQIFFSLGPGFGVL</span><span class="topo-inside">LAFASYNKFNNNCYQD</span><span class="topo-membrane">ALVTSVVNCMTSFVSG</span><span class="topo-outside">FVIFTVLGYMAEMRNEDVSEVAKDAGPSLLFI</span><span class="topo-unknown">TYAEAIA</span><span class="topo-outside">NMPASTFFAI</span><span class="topo-membrane">IFFLMLIT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LGLDSSFAGLEGV</span><span class="topo-inside">ITAVLDEFPHVWAKRRERFV</span><span class="topo-membrane">LAVVITCFFGSLVTLT</span><span class="topo-outside">FGGAYV</span><span class="topo-membrane">VKLLEEYATGPAVLTVALIEA</span><span class="topo-inside">VAVSWFYGITQFCRDVKEMLGFSPG</span><span class="topo-unknown">WFWRICWV</span><span class="topo-inside">A</span><span class="topo-membrane">ISPLFLLFII</span></span>
<span class="topo-ruler">       490       500       510       520       530       540         </span>
<span class="topo-line"><span class="topo-membrane">ASFLMSP</span><span class="topo-outside">PQLRLFQYNYPYW</span><span class="topo-membrane">SIILGYAIGTSSFICIP</span><span class="topo-inside">TYIAYRLIITPGTFKERIIKSITPETP</span><span class="topo-unknown">TLVPR</span></span>
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
      <td>13</td>
      <td>74</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>33</td>
      <td>87</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>43</td>
      <td>107</td>
      <td>116</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>61</td>
      <td>117</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>91</td>
      <td>135</td>
      <td>164</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>112</td>
      <td>165</td>
      <td>185</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>177</td>
      <td>186</td>
      <td>250</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>197</td>
      <td>251</td>
      <td>270</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>203</td>
      <td>271</td>
      <td>276</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>221</td>
      <td>277</td>
      <td>294</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>250</td>
      <td>295</td>
      <td>323</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>271</td>
      <td>324</td>
      <td>344</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>287</td>
      <td>345</td>
      <td>360</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>303</td>
      <td>361</td>
      <td>376</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>304</td>
      <td>335</td>
      <td>377</td>
      <td>408</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>336</td>
      <td>342</td>
      <td>409</td>
      <td>415</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>343</td>
      <td>352</td>
      <td>416</td>
      <td>425</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>373</td>
      <td>426</td>
      <td>446</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>393</td>
      <td>447</td>
      <td>466</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>394</td>
      <td>409</td>
      <td>467</td>
      <td>482</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>415</td>
      <td>483</td>
      <td>488</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>416</td>
      <td>436</td>
      <td>489</td>
      <td>509</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>437</td>
      <td>461</td>
      <td>510</td>
      <td>534</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>462</td>
      <td>469</td>
      <td>535</td>
      <td>542</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>470</td>
      <td>470</td>
      <td>543</td>
      <td>543</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>487</td>
      <td>544</td>
      <td>560</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>488</td>
      <td>500</td>
      <td>561</td>
      <td>573</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>501</td>
      <td>517</td>
      <td>574</td>
      <td>590</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>518</td>
      <td>544</td>
      <td>591</td>
      <td>617</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6awo">6AWO</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">GSQGERETWGKKVDFL</span><span class="topo-membrane">LSVIGYAVDLGN</span><span class="topo-outside">VWRFPYICAQNGGGAF</span><span class="topo-membrane">LLPYTIMAIFGGI</span><span class="topo-inside">PLFYMELALGQYHRNGCISIWRKICPIFKGIGYAIC</span><span class="topo-membrane">IIAFYIASYYNT</span><span class="topo-outside">IMAWALYYLISSFTD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">QLPWTSCKNSWNTGNCTNYFSEDNITWTLHSTSPAEEFYTRHVLQIHRSKGLQDLGGISWQL</span><span class="topo-membrane">ALCIMLIFTVIYFS</span><span class="topo-inside">IWKGVKTSGK</span><span class="topo-membrane">VVWVTATFPYIA</span><span class="topo-outside">LSVLLVRGATLPGAWRGVLFYL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">KPNWQKLLETGV</span><span class="topo-membrane">WIDAAAQIFFSLGP</span><span class="topo-inside">GFGVLLAFASYNKFNNNCYQDAL</span><span class="topo-membrane">VTSVVNCMTSF</span><span class="topo-outside">VSGFVIFTVLGYMAEMRNEDVSEVAKDAGPSLLFITYAEAIANMPASTFFAIIFF</span><span class="topo-membrane">LMLIT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LGLDSSFAGL</span><span class="topo-inside">EGVITAVLDEFPHVWAKRRERFVLA</span><span class="topo-membrane">VVITCFFGSLV</span><span class="topo-outside">TLTFGGAYVVKL</span><span class="topo-membrane">LEEYATGPAVLTVAL</span><span class="topo-inside">IEAVAVSWFYGITQFCRDVKEMLGFSPGWFWRICWVA</span><span class="topo-membrane">ISPLFLLFII</span></span>
<span class="topo-ruler">       490       500       510       520       530       540         </span>
<span class="topo-line"><span class="topo-membrane">ASFLM</span><span class="topo-outside">SPPQLRLFQYNYPYWSI</span><span class="topo-membrane">ILGYAIGTSSFI</span><span class="topo-inside">CIPTYIAYRLIITPGTFKERIIKSITPETP</span><span class="topo-unknown">TLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (26 regions)</summary>
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
      <td>16</td>
      <td>74</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>28</td>
      <td>90</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>44</td>
      <td>102</td>
      <td>117</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>57</td>
      <td>118</td>
      <td>130</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>58</td>
      <td>93</td>
      <td>131</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>105</td>
      <td>167</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>182</td>
      <td>179</td>
      <td>255</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>196</td>
      <td>256</td>
      <td>269</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>206</td>
      <td>270</td>
      <td>279</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>218</td>
      <td>280</td>
      <td>291</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>252</td>
      <td>292</td>
      <td>325</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>253</td>
      <td>266</td>
      <td>326</td>
      <td>339</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>289</td>
      <td>340</td>
      <td>362</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>300</td>
      <td>363</td>
      <td>373</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>301</td>
      <td>355</td>
      <td>374</td>
      <td>428</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>356</td>
      <td>370</td>
      <td>429</td>
      <td>443</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>371</td>
      <td>395</td>
      <td>444</td>
      <td>468</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>396</td>
      <td>406</td>
      <td>469</td>
      <td>479</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>407</td>
      <td>418</td>
      <td>480</td>
      <td>491</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>419</td>
      <td>433</td>
      <td>492</td>
      <td>506</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>434</td>
      <td>470</td>
      <td>507</td>
      <td>543</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>485</td>
      <td>544</td>
      <td>558</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>486</td>
      <td>502</td>
      <td>559</td>
      <td>575</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>503</td>
      <td>514</td>
      <td>576</td>
      <td>587</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>515</td>
      <td>544</td>
      <td>588</td>
      <td>617</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>545</td>
      <td>549</td>
      <td>618</td>
      <td>622</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6awq">6AWQ</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">GSQGERETWGKKVDF</span><span class="topo-membrane">LLSVIGYAVDLGNV</span><span class="topo-outside">WRFPYICAQNGGGAF</span><span class="topo-membrane">LLPYTIMAIFGGIPLFY</span><span class="topo-inside">MELALGQYHRNGCISIWRKICPIFKGIG</span><span class="topo-membrane">YAICIIAFYIASYYNTIMA</span><span class="topo-outside">WALYYLISSFTD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">QLPWTSCKNSWNTGNCTNYFSEDNITWTLHSTSPAEEFYTRHVLQIHRSKGLQDLGGISWQL</span><span class="topo-membrane">ALCIMLIFTVIYFSIW</span><span class="topo-inside">KGVK</span><span class="topo-membrane">TSGKVVWVTATFPYIALS</span><span class="topo-outside">VLLVRGATLPGAWRGVLFYL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">KPNWQKLLETGV</span><span class="topo-membrane">WIDAAAQIFFSLGPGFGVL</span><span class="topo-inside">LAFASYNKFNNNCYQ</span><span class="topo-membrane">DALVTSVVNCMTSFV</span><span class="topo-outside">SGFVIFTVLGYMAEMRNEDVSEVAKDAGPSLLFITYAEAIANMPASTFFAIIFF</span><span class="topo-membrane">LMLIT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LGLDSSFAGLEGV</span><span class="topo-inside">ITAVLDEFPHVWAKRRERF</span><span class="topo-membrane">VLAVVITCFFGSLVT</span><span class="topo-outside">LTFGGAYVVKL</span><span class="topo-membrane">LEEYATGPAVLTVALI</span><span class="topo-inside">EAVAVSWFYGITQFCRDVKEMLGFSPGWFWRICWV</span><span class="topo-membrane">AISPLFLLFII</span></span>
<span class="topo-ruler">       490       500       510       520       530       540         </span>
<span class="topo-line"><span class="topo-membrane">ASFLM</span><span class="topo-outside">SPPQLRLFQYNYPYWSI</span><span class="topo-membrane">ILGYAIGTSSFICIP</span><span class="topo-inside">TYIAYRLIITPGTFKERIIKSITPETP</span><span class="topo-unknown">TLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (26 regions)</summary>
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
      <td>15</td>
      <td>74</td>
      <td>88</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>29</td>
      <td>89</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>44</td>
      <td>103</td>
      <td>117</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>61</td>
      <td>118</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>89</td>
      <td>135</td>
      <td>162</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>108</td>
      <td>163</td>
      <td>181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>182</td>
      <td>182</td>
      <td>255</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>198</td>
      <td>256</td>
      <td>271</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>202</td>
      <td>272</td>
      <td>275</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>220</td>
      <td>276</td>
      <td>293</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>252</td>
      <td>294</td>
      <td>325</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>253</td>
      <td>271</td>
      <td>326</td>
      <td>344</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>286</td>
      <td>345</td>
      <td>359</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>301</td>
      <td>360</td>
      <td>374</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>302</td>
      <td>355</td>
      <td>375</td>
      <td>428</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>356</td>
      <td>373</td>
      <td>429</td>
      <td>446</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>392</td>
      <td>447</td>
      <td>465</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>393</td>
      <td>407</td>
      <td>466</td>
      <td>480</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>408</td>
      <td>418</td>
      <td>481</td>
      <td>491</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>419</td>
      <td>434</td>
      <td>492</td>
      <td>507</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>435</td>
      <td>469</td>
      <td>508</td>
      <td>542</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>470</td>
      <td>485</td>
      <td>543</td>
      <td>558</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>486</td>
      <td>502</td>
      <td>559</td>
      <td>575</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>503</td>
      <td>517</td>
      <td>576</td>
      <td>590</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>518</td>
      <td>544</td>
      <td>591</td>
      <td>617</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>545</td>
      <td>549</td>
      <td>618</td>
      <td>622</td>
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

### Antidepressant binding to the central site

(S)-citalopram and [Paroxetine](/xray-mp-wiki/reagents/ligands/paroxetine/) both bind to the central binding site (S1) located between transmembrane helices 1, 3, 6, 8 and 10. The amine groups of both drugs occupy subsite A and interact with the conserved Asp98 carboxylate. Tyr95 forms a cation-pi interaction beneath the amine groups. The drugs lock SERT in an outward-open conformation, wedging between scaffold helices 3, 8, 10 and core helices 1, 6, directly blocking [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki/reagents/ligands/serotonin/) binding.

### Allosteric site identification

A second (S)-citalopram molecule was found in an allosteric site at the periphery of the extracellular vestibule, approximately 13 A from the central site. Occupancy of this allosteric site sterically hinders ligand unbinding from the central site, providing a structural explanation for (S)-citalopram's action as an allosteric ligand.

### Diverse SSRI binding modes at the central site

Structures of SERT bound to [Sertraline](/xray-mp-wiki/reagents/ligands/sertraline/), [Fluvoxamine](/xray-mp-wiki/reagents/ligands/fluvoxamine/), and [Paroxetine](/xray-mp-wiki/reagents/ligands/paroxetine/) revealed that chemically diverse SSRIs occupy the central binding site with different binding poses, explaining how the transporter accommodates structurally distinct antidepressants. In subsite A, the distance from the amine of [Sertraline](/xray-mp-wiki/reagents/ligands/sertraline/) to Asp98 is longer, while for [Fluvoxamine](/xray-mp-wiki/reagents/ligands/fluvoxamine/) and [Paroxetine](/xray-mp-wiki/reagents/ligands/paroxetine/) it is shorter. In subsite B, the meta chlorine of [Sertraline](/xray-mp-wiki/reagents/ligands/sertraline/) engages with Ser439 while the fluorines of [Fluvoxamine](/xray-mp-wiki/reagents/ligands/fluvoxamine/) form closer interactions. In subsite C, the naphthalene group of [Sertraline](/xray-mp-wiki/reagents/ligands/sertraline/) is localized higher than the benzofuran of (S)-citalopram and [Paroxetine](/xray-mp-wiki/reagents/ligands/paroxetine/). Phe341 and Phe335 undergo different rotamer conformations to accommodate different drugs. These structural differences help explain the varying affinities of different SSRIs.


## Cross-References

- <a href="/xray-mp-wiki/proteins/enzymes/leut/">LeuT Amino Acid Transporter from Aquifex aeolicus</a> — NSS family prototype sharing the LeuT-fold architecture
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/nss-family/">Neurotransmitter/Sodium Symporter (NSS) Family</a> — SERT is a human member of the NSS family (SLC6A4)
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — SERT transport follows alternating access
- <a href="/xray-mp-wiki/reagents/ligands/sertraline/">Sertraline</a> — SSRI antidepressant bound in ts3-sertraline structures
- <a href="/xray-mp-wiki/reagents/ligands/serotonin/">Serotonin (5-Hydroxytryptamine, 5-HT)</a> — Endogenous substrate of SERT
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent used for solubilization and purification
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> — Buffer used throughout purification and crystallization
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> — Additive used in purification or crystallization buffers
