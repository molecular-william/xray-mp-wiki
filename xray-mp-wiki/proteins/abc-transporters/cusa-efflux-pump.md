---
title: "CusA Heavy-Metal Efflux RND Transporter (E. coli)"
created: 2026-06-16
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, pump, membrane-protein]
sources: [doi/10.1038##nature09395]
verified: agent
uniprot_id: P38054
---

# CusA Heavy-Metal Efflux RND Transporter (E. coli)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P38054">UniProt: P38054</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

CusA is the inner-membrane transporter component of the CusCBA tripartite efflux complex in Escherichia coli, responsible for extruding biocidal Cu(I) and Ag(I) ions. It belongs to the heavy-metal efflux (HME) subfamily of the resistance-nodulation-cell division (RND) superfamily. The crystal structures of CusA in apo, Cu(I)-bound, and Ag(I)-bound forms were determined, providing the first structural information for any HME-RND efflux pump. The structures reveal a homotrimeric architecture with distinct periplasmic (PN1, PN2, PC1, PC2) and transmembrane (DN, DC) subdomains. Metal binding occurs via a three-methionine cluster (M573, M623, M672) within a cleft of the periplasmic domain that is closed in the apo form and opens upon metal binding. Five methionine pairs/clusters (M410/M501, M403/M486, M391/M1009, M271/M755, and the M573/M623/M672 three-methionine site) form a relay network for stepwise metal transport from the cytoplasm through the transmembrane region to the central funnel for extrusion via CusC.

## Publications

### doi/10.1038##nature09395

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3k07">3K07</a></td>
      <td>Not specified</td>
      <td>R32</td>
      <td>Full-length CusA with N-terminal His6 tag</td>
      <td>Apo (no metal bound)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3k07">3K07</a></td>
      <td>Not specified</td>
      <td>R32</td>
      <td>Full-length CusA with N-terminal His6 tag</td>
      <td>Cu(I)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3k07">3K07</a></td>
      <td>Not specified</td>
      <td>R32</td>
      <td>Full-length CusA with N-terminal His6 tag</td>
      <td>Ag(I)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21(DE3)ΔacrB cells
- **Construct**: Full-length CusA with N-terminal His6 tag in pET15bΩcusA vector, ampicillin selection, IPTG induction

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
      <td>1. <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity purification</a></td>
      <td>Ni2+ <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>—</td>
      <td></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His6-tag</a>ged CusA purified by <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) affinity</td>
    </tr>
    <tr>
      <td>2. <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td>Gel filtration</td>
      <td>—</td>
      <td></td>
      <td>Final polishing step</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified CusA in detergent-containing buffer

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified CusA</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>10% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG 3350</a>, 0.1 M Na-<a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> pH 6.5, 0.4 M (NH4)2SO4, 1% Jeffamine M600, 0.05% (w/v) Cymal-6</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>25 °C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Apo-CusA, SeMet-CusA crystallized under same conditions. Heavy-atom derivatives: KAuCl4 (1 mM) or Ta6Br12 (5 mM) soaked 1.5 h. CusA-Cu(I): 2 mM [Cu(CH3CN)4]PF6, 2 mM TCEP soaked 1 h. CusA-Ag(I): 1 mM AgNO3 soaked 1 h. Data collected at APS beamline 24ID-C. Rhombohedral R32 space group, one monomer per asymmetric unit.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3k07">3K07</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGHHHHHHMIEW</span><span class="topo-inside">I</span><span class="topo-unknown">IRRSVA</span><span class="topo-inside">NRFL</span><span class="topo-membrane">VLMGALFLSIWGTWTIIN</span><span class="topo-outside">TPVDALPDLSDVQVIIKTSYPGQAPQIVENQVTYPLTTTMLSVPGAKTVRGFSQFGDSYVYVIFEDGTDPYWARSRVLE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">YLNQVQGKLPAGVSAELGPDATGVGWIYEYALVDRSGKHDLADLRSLQDWFLKYELKTIPDVAEVASVGGVVKEYQVVIDPQRLAQYGISLAEVKSALDASNQEAGGSSIELAEAEYMVR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ASGYLQTLDDFNHIVLKASENGVPVYLRDVAKVQIGPEMRRGIAELNGEGEVAGGVVILRSGKNAREVIAAVKDKLETLKSSLPEGVEIVTTYDRSQLIDRAIDNL</span><span class="topo-membrane">SGKLLEEFIVVAVV</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">CALF</span><span class="topo-inside">LWHVRSA</span><span class="topo-membrane">LVAIISLPLGLCIAFIVMHFQ</span><span class="topo-outside">GLNANIMS</span><span class="topo-membrane">LGGIAIAVGAMVDAAIV</span><span class="topo-inside">MIENAHKRLEEWQHQHPDATLDNKTRWQVITDASVEVGPA</span><span class="topo-membrane">LFISLLIITLSFIPIFT</span><span class="topo-outside">LEGQEG</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">RLFGP</span><span class="topo-membrane">LAFTKTYAMAGAALLAIVVI</span><span class="topo-inside">PILMGYW</span><span class="topo-unknown">IRGKIPPESSN</span><span class="topo-inside">P</span><span class="topo-unknown">LNRFLIRVYHPLLLKVLH</span><span class="topo-inside">WPKT</span><span class="topo-membrane">TLLVAALSVLTVLWPLN</span><span class="topo-outside">KVGGEFLPQINEGDLLYMPSTLPGISAAEAASMLQKT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">DKLIMSVPEVARVFGKTGKAETATDSAPLEMVETTIQLKPQEQWRPGMTMDKIIEELDNTVRLPGLANLWVPPIRNRIDMLSTGIKSPIGIKVSGTVLADIDAMAEQIEEVARTVPGVAS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">ALAERLEGGRYINVEINREKAARYGMTVADVQLFVTSAVGGAMVGETVEGIARYPINLRYPQSWRDSPQALRQLPILTPMKQQITLADVADIKVSTGPSMLKTENARPTSWIYIDARDRD</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">MVSVVHDLQKAIAEKVQLKPGTSVAFSGQFELLERANHKL</span><span class="topo-membrane">KLMVPMTLMIIFVLLYLA</span><span class="topo-inside">FRRV</span><span class="topo-membrane">GEALLIISSVPFALVGGIWLLWWM</span><span class="topo-outside">GFHLSVAT</span><span class="topo-membrane">GTGFIALAGVAAEFGVV</span><span class="topo-inside">MLMYLRHAI</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050     </span>
<span class="topo-line"><span class="topo-inside">EAVPSLNNPQTFSEQKLDEALYHGAVLRVRPK</span><span class="topo-membrane">AMTVAVIIAGLLPILWG</span><span class="topo-outside">TGAGSEVM</span><span class="topo-membrane">SRIAAPMIGGMITAPLLSLFI</span><span class="topo-unknown">IPAAYKLMW</span><span class="topo-inside">L</span><span class="topo-unknown">HRHRVRK</span></span>
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
      <td>1</td>
      <td>12</td>
      <td>-7</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>13</td>
      <td>13</td>
      <td>5</td>
      <td>5</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>19</td>
      <td>6</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>20</td>
      <td>23</td>
      <td>12</td>
      <td>15</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>24</td>
      <td>41</td>
      <td>16</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>346</td>
      <td>34</td>
      <td>338</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>347</td>
      <td>364</td>
      <td>339</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>365</td>
      <td>371</td>
      <td>357</td>
      <td>363</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>372</td>
      <td>392</td>
      <td>364</td>
      <td>384</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>393</td>
      <td>400</td>
      <td>385</td>
      <td>392</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>401</td>
      <td>417</td>
      <td>393</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>418</td>
      <td>457</td>
      <td>410</td>
      <td>449</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>458</td>
      <td>474</td>
      <td>450</td>
      <td>466</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>485</td>
      <td>467</td>
      <td>477</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>486</td>
      <td>505</td>
      <td>478</td>
      <td>497</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>506</td>
      <td>512</td>
      <td>498</td>
      <td>504</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>513</td>
      <td>523</td>
      <td>505</td>
      <td>515</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>524</td>
      <td>524</td>
      <td>516</td>
      <td>516</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>542</td>
      <td>517</td>
      <td>534</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>543</td>
      <td>546</td>
      <td>535</td>
      <td>538</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>547</td>
      <td>563</td>
      <td>539</td>
      <td>555</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>564</td>
      <td>880</td>
      <td>556</td>
      <td>872</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>881</td>
      <td>898</td>
      <td>873</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>899</td>
      <td>902</td>
      <td>891</td>
      <td>894</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>903</td>
      <td>926</td>
      <td>895</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>927</td>
      <td>934</td>
      <td>919</td>
      <td>926</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>935</td>
      <td>951</td>
      <td>927</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>952</td>
      <td>992</td>
      <td>944</td>
      <td>984</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>993</td>
      <td>1009</td>
      <td>985</td>
      <td>1001</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1010</td>
      <td>1017</td>
      <td>1002</td>
      <td>1009</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1018</td>
      <td>1038</td>
      <td>1010</td>
      <td>1030</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1039</td>
      <td>1047</td>
      <td>1031</td>
      <td>1039</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1048</td>
      <td>1048</td>
      <td>1040</td>
      <td>1040</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1049</td>
      <td>1055</td>
      <td>1041</td>
      <td>1047</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3k07">3K07</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGHHHHHHMIEW</span><span class="topo-inside">I</span><span class="topo-unknown">IRRSVA</span><span class="topo-inside">NRFL</span><span class="topo-membrane">VLMGALFLSIWGTWTIIN</span><span class="topo-outside">TPVDALPDLSDVQVIIKTSYPGQAPQIVENQVTYPLTTTMLSVPGAKTVRGFSQFGDSYVYVIFEDGTDPYWARSRVLE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">YLNQVQGKLPAGVSAELGPDATGVGWIYEYALVDRSGKHDLADLRSLQDWFLKYELKTIPDVAEVASVGGVVKEYQVVIDPQRLAQYGISLAEVKSALDASNQEAGGSSIELAEAEYMVR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ASGYLQTLDDFNHIVLKASENGVPVYLRDVAKVQIGPEMRRGIAELNGEGEVAGGVVILRSGKNAREVIAAVKDKLETLKSSLPEGVEIVTTYDRSQLIDRAIDNL</span><span class="topo-membrane">SGKLLEEFIVVAVV</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">CALF</span><span class="topo-inside">LWHVRSA</span><span class="topo-membrane">LVAIISLPLGLCIAFIVMHFQ</span><span class="topo-outside">GLNANIMS</span><span class="topo-membrane">LGGIAIAVGAMVDAAIV</span><span class="topo-inside">MIENAHKRLEEWQHQHPDATLDNKTRWQVITDASVEVGPA</span><span class="topo-membrane">LFISLLIITLSFIPIFT</span><span class="topo-outside">LEGQEG</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">RLFGP</span><span class="topo-membrane">LAFTKTYAMAGAALLAIVVI</span><span class="topo-inside">PILMGYW</span><span class="topo-unknown">IRGKIPPESSN</span><span class="topo-inside">P</span><span class="topo-unknown">LNRFLIRVYHPLLLKVLH</span><span class="topo-inside">WPKT</span><span class="topo-membrane">TLLVAALSVLTVLWPLN</span><span class="topo-outside">KVGGEFLPQINEGDLLYMPSTLPGISAAEAASMLQKT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">DKLIMSVPEVARVFGKTGKAETATDSAPLEMVETTIQLKPQEQWRPGMTMDKIIEELDNTVRLPGLANLWVPPIRNRIDMLSTGIKSPIGIKVSGTVLADIDAMAEQIEEVARTVPGVAS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">ALAERLEGGRYINVEINREKAARYGMTVADVQLFVTSAVGGAMVGETVEGIARYPINLRYPQSWRDSPQALRQLPILTPMKQQITLADVADIKVSTGPSMLKTENARPTSWIYIDARDRD</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">MVSVVHDLQKAIAEKVQLKPGTSVAFSGQFELLERANHKL</span><span class="topo-membrane">KLMVPMTLMIIFVLLYLA</span><span class="topo-inside">FRRV</span><span class="topo-membrane">GEALLIISSVPFALVGGIWLLWWM</span><span class="topo-outside">GFHLSVAT</span><span class="topo-membrane">GTGFIALAGVAAEFGVV</span><span class="topo-inside">MLMYLRHAI</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050     </span>
<span class="topo-line"><span class="topo-inside">EAVPSLNNPQTFSEQKLDEALYHGAVLRVRPK</span><span class="topo-membrane">AMTVAVIIAGLLPILWG</span><span class="topo-outside">TGAGSEVM</span><span class="topo-membrane">SRIAAPMIGGMITAPLLSLFI</span><span class="topo-unknown">IPAAYKLMW</span><span class="topo-inside">L</span><span class="topo-unknown">HRHRVRK</span></span>
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
      <td>1</td>
      <td>12</td>
      <td>-7</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>13</td>
      <td>13</td>
      <td>5</td>
      <td>5</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>19</td>
      <td>6</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>20</td>
      <td>23</td>
      <td>12</td>
      <td>15</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>24</td>
      <td>41</td>
      <td>16</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>346</td>
      <td>34</td>
      <td>338</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>347</td>
      <td>364</td>
      <td>339</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>365</td>
      <td>371</td>
      <td>357</td>
      <td>363</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>372</td>
      <td>392</td>
      <td>364</td>
      <td>384</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>393</td>
      <td>400</td>
      <td>385</td>
      <td>392</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>401</td>
      <td>417</td>
      <td>393</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>418</td>
      <td>457</td>
      <td>410</td>
      <td>449</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>458</td>
      <td>474</td>
      <td>450</td>
      <td>466</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>485</td>
      <td>467</td>
      <td>477</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>486</td>
      <td>505</td>
      <td>478</td>
      <td>497</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>506</td>
      <td>512</td>
      <td>498</td>
      <td>504</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>513</td>
      <td>523</td>
      <td>505</td>
      <td>515</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>524</td>
      <td>524</td>
      <td>516</td>
      <td>516</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>542</td>
      <td>517</td>
      <td>534</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>543</td>
      <td>546</td>
      <td>535</td>
      <td>538</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>547</td>
      <td>563</td>
      <td>539</td>
      <td>555</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>564</td>
      <td>880</td>
      <td>556</td>
      <td>872</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>881</td>
      <td>898</td>
      <td>873</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>899</td>
      <td>902</td>
      <td>891</td>
      <td>894</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>903</td>
      <td>926</td>
      <td>895</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>927</td>
      <td>934</td>
      <td>919</td>
      <td>926</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>935</td>
      <td>951</td>
      <td>927</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>952</td>
      <td>992</td>
      <td>944</td>
      <td>984</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>993</td>
      <td>1009</td>
      <td>985</td>
      <td>1001</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1010</td>
      <td>1017</td>
      <td>1002</td>
      <td>1009</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1018</td>
      <td>1038</td>
      <td>1010</td>
      <td>1030</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1039</td>
      <td>1047</td>
      <td>1031</td>
      <td>1039</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1048</td>
      <td>1048</td>
      <td>1040</td>
      <td>1040</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1049</td>
      <td>1055</td>
      <td>1041</td>
      <td>1047</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3k07">3K07</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGHHHHHHMIEW</span><span class="topo-inside">I</span><span class="topo-unknown">IRRSVA</span><span class="topo-inside">NRFL</span><span class="topo-membrane">VLMGALFLSIWGTWTIIN</span><span class="topo-outside">TPVDALPDLSDVQVIIKTSYPGQAPQIVENQVTYPLTTTMLSVPGAKTVRGFSQFGDSYVYVIFEDGTDPYWARSRVLE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">YLNQVQGKLPAGVSAELGPDATGVGWIYEYALVDRSGKHDLADLRSLQDWFLKYELKTIPDVAEVASVGGVVKEYQVVIDPQRLAQYGISLAEVKSALDASNQEAGGSSIELAEAEYMVR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ASGYLQTLDDFNHIVLKASENGVPVYLRDVAKVQIGPEMRRGIAELNGEGEVAGGVVILRSGKNAREVIAAVKDKLETLKSSLPEGVEIVTTYDRSQLIDRAIDNL</span><span class="topo-membrane">SGKLLEEFIVVAVV</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">CALF</span><span class="topo-inside">LWHVRSA</span><span class="topo-membrane">LVAIISLPLGLCIAFIVMHFQ</span><span class="topo-outside">GLNANIMS</span><span class="topo-membrane">LGGIAIAVGAMVDAAIV</span><span class="topo-inside">MIENAHKRLEEWQHQHPDATLDNKTRWQVITDASVEVGPA</span><span class="topo-membrane">LFISLLIITLSFIPIFT</span><span class="topo-outside">LEGQEG</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">RLFGP</span><span class="topo-membrane">LAFTKTYAMAGAALLAIVVI</span><span class="topo-inside">PILMGYW</span><span class="topo-unknown">IRGKIPPESSN</span><span class="topo-inside">P</span><span class="topo-unknown">LNRFLIRVYHPLLLKVLH</span><span class="topo-inside">WPKT</span><span class="topo-membrane">TLLVAALSVLTVLWPLN</span><span class="topo-outside">KVGGEFLPQINEGDLLYMPSTLPGISAAEAASMLQKT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">DKLIMSVPEVARVFGKTGKAETATDSAPLEMVETTIQLKPQEQWRPGMTMDKIIEELDNTVRLPGLANLWVPPIRNRIDMLSTGIKSPIGIKVSGTVLADIDAMAEQIEEVARTVPGVAS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">ALAERLEGGRYINVEINREKAARYGMTVADVQLFVTSAVGGAMVGETVEGIARYPINLRYPQSWRDSPQALRQLPILTPMKQQITLADVADIKVSTGPSMLKTENARPTSWIYIDARDRD</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">MVSVVHDLQKAIAEKVQLKPGTSVAFSGQFELLERANHKL</span><span class="topo-membrane">KLMVPMTLMIIFVLLYLA</span><span class="topo-inside">FRRV</span><span class="topo-membrane">GEALLIISSVPFALVGGIWLLWWM</span><span class="topo-outside">GFHLSVAT</span><span class="topo-membrane">GTGFIALAGVAAEFGVV</span><span class="topo-inside">MLMYLRHAI</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050     </span>
<span class="topo-line"><span class="topo-inside">EAVPSLNNPQTFSEQKLDEALYHGAVLRVRPK</span><span class="topo-membrane">AMTVAVIIAGLLPILWG</span><span class="topo-outside">TGAGSEVM</span><span class="topo-membrane">SRIAAPMIGGMITAPLLSLFI</span><span class="topo-unknown">IPAAYKLMW</span><span class="topo-inside">L</span><span class="topo-unknown">HRHRVRK</span></span>
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
      <td>1</td>
      <td>12</td>
      <td>-7</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>13</td>
      <td>13</td>
      <td>5</td>
      <td>5</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>19</td>
      <td>6</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>20</td>
      <td>23</td>
      <td>12</td>
      <td>15</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>24</td>
      <td>41</td>
      <td>16</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>346</td>
      <td>34</td>
      <td>338</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>347</td>
      <td>364</td>
      <td>339</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>365</td>
      <td>371</td>
      <td>357</td>
      <td>363</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>372</td>
      <td>392</td>
      <td>364</td>
      <td>384</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>393</td>
      <td>400</td>
      <td>385</td>
      <td>392</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>401</td>
      <td>417</td>
      <td>393</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>418</td>
      <td>457</td>
      <td>410</td>
      <td>449</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>458</td>
      <td>474</td>
      <td>450</td>
      <td>466</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>485</td>
      <td>467</td>
      <td>477</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>486</td>
      <td>505</td>
      <td>478</td>
      <td>497</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>506</td>
      <td>512</td>
      <td>498</td>
      <td>504</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>513</td>
      <td>523</td>
      <td>505</td>
      <td>515</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>524</td>
      <td>524</td>
      <td>516</td>
      <td>516</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>542</td>
      <td>517</td>
      <td>534</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>543</td>
      <td>546</td>
      <td>535</td>
      <td>538</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>547</td>
      <td>563</td>
      <td>539</td>
      <td>555</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>564</td>
      <td>880</td>
      <td>556</td>
      <td>872</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>881</td>
      <td>898</td>
      <td>873</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>899</td>
      <td>902</td>
      <td>891</td>
      <td>894</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>903</td>
      <td>926</td>
      <td>895</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>927</td>
      <td>934</td>
      <td>919</td>
      <td>926</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>935</td>
      <td>951</td>
      <td>927</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>952</td>
      <td>992</td>
      <td>944</td>
      <td>984</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>993</td>
      <td>1009</td>
      <td>985</td>
      <td>1001</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1010</td>
      <td>1017</td>
      <td>1002</td>
      <td>1009</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1018</td>
      <td>1038</td>
      <td>1010</td>
      <td>1030</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1039</td>
      <td>1047</td>
      <td>1031</td>
      <td>1039</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1048</td>
      <td>1048</td>
      <td>1040</td>
      <td>1040</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1049</td>
      <td>1055</td>
      <td>1041</td>
      <td>1047</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3k07">3K07</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGHHHHHHMIEW</span><span class="topo-inside">I</span><span class="topo-unknown">IRRSVA</span><span class="topo-inside">NRFL</span><span class="topo-membrane">VLMGALFLSIWGTWTIIN</span><span class="topo-outside">TPVDALPDLSDVQVIIKTSYPGQAPQIVENQVTYPLTTTMLSVPGAKTVRGFSQFGDSYVYVIFEDGTDPYWARSRVLE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">YLNQVQGKLPAGVSAELGPDATGVGWIYEYALVDRSGKHDLADLRSLQDWFLKYELKTIPDVAEVASVGGVVKEYQVVIDPQRLAQYGISLAEVKSALDASNQEAGGSSIELAEAEYMVR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ASGYLQTLDDFNHIVLKASENGVPVYLRDVAKVQIGPEMRRGIAELNGEGEVAGGVVILRSGKNAREVIAAVKDKLETLKSSLPEGVEIVTTYDRSQLIDRAIDNL</span><span class="topo-membrane">SGKLLEEFIVVAVV</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">CALF</span><span class="topo-inside">LWHVRSA</span><span class="topo-membrane">LVAIISLPLGLCIAFIVMHFQ</span><span class="topo-outside">GLNANIMS</span><span class="topo-membrane">LGGIAIAVGAMVDAAIV</span><span class="topo-inside">MIENAHKRLEEWQHQHPDATLDNKTRWQVITDASVEVGPA</span><span class="topo-membrane">LFISLLIITLSFIPIFT</span><span class="topo-outside">LEGQEG</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">RLFGP</span><span class="topo-membrane">LAFTKTYAMAGAALLAIVVI</span><span class="topo-inside">PILMGYW</span><span class="topo-unknown">IRGKIPPESSN</span><span class="topo-inside">P</span><span class="topo-unknown">LNRFLIRVYHPLLLKVLH</span><span class="topo-inside">WPKT</span><span class="topo-membrane">TLLVAALSVLTVLWPLN</span><span class="topo-outside">KVGGEFLPQINEGDLLYMPSTLPGISAAEAASMLQKT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">DKLIMSVPEVARVFGKTGKAETATDSAPLEMVETTIQLKPQEQWRPGMTMDKIIEELDNTVRLPGLANLWVPPIRNRIDMLSTGIKSPIGIKVSGTVLADIDAMAEQIEEVARTVPGVAS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">ALAERLEGGRYINVEINREKAARYGMTVADVQLFVTSAVGGAMVGETVEGIARYPINLRYPQSWRDSPQALRQLPILTPMKQQITLADVADIKVSTGPSMLKTENARPTSWIYIDARDRD</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">MVSVVHDLQKAIAEKVQLKPGTSVAFSGQFELLERANHKL</span><span class="topo-membrane">KLMVPMTLMIIFVLLYLA</span><span class="topo-inside">FRRV</span><span class="topo-membrane">GEALLIISSVPFALVGGIWLLWWM</span><span class="topo-outside">GFHLSVAT</span><span class="topo-membrane">GTGFIALAGVAAEFGVV</span><span class="topo-inside">MLMYLRHAI</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050     </span>
<span class="topo-line"><span class="topo-inside">EAVPSLNNPQTFSEQKLDEALYHGAVLRVRPK</span><span class="topo-membrane">AMTVAVIIAGLLPILWG</span><span class="topo-outside">TGAGSEVM</span><span class="topo-membrane">SRIAAPMIGGMITAPLLSLFI</span><span class="topo-unknown">IPAAYKLMW</span><span class="topo-inside">L</span><span class="topo-unknown">HRHRVRK</span></span>
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
      <td>1</td>
      <td>12</td>
      <td>-7</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>13</td>
      <td>13</td>
      <td>5</td>
      <td>5</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>19</td>
      <td>6</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>20</td>
      <td>23</td>
      <td>12</td>
      <td>15</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>24</td>
      <td>41</td>
      <td>16</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>346</td>
      <td>34</td>
      <td>338</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>347</td>
      <td>364</td>
      <td>339</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>365</td>
      <td>371</td>
      <td>357</td>
      <td>363</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>372</td>
      <td>392</td>
      <td>364</td>
      <td>384</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>393</td>
      <td>400</td>
      <td>385</td>
      <td>392</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>401</td>
      <td>417</td>
      <td>393</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>418</td>
      <td>457</td>
      <td>410</td>
      <td>449</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>458</td>
      <td>474</td>
      <td>450</td>
      <td>466</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>485</td>
      <td>467</td>
      <td>477</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>486</td>
      <td>505</td>
      <td>478</td>
      <td>497</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>506</td>
      <td>512</td>
      <td>498</td>
      <td>504</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>513</td>
      <td>523</td>
      <td>505</td>
      <td>515</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>524</td>
      <td>524</td>
      <td>516</td>
      <td>516</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>542</td>
      <td>517</td>
      <td>534</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>543</td>
      <td>546</td>
      <td>535</td>
      <td>538</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>547</td>
      <td>563</td>
      <td>539</td>
      <td>555</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>564</td>
      <td>880</td>
      <td>556</td>
      <td>872</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>881</td>
      <td>898</td>
      <td>873</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>899</td>
      <td>902</td>
      <td>891</td>
      <td>894</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>903</td>
      <td>926</td>
      <td>895</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>927</td>
      <td>934</td>
      <td>919</td>
      <td>926</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>935</td>
      <td>951</td>
      <td>927</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>952</td>
      <td>992</td>
      <td>944</td>
      <td>984</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>993</td>
      <td>1009</td>
      <td>985</td>
      <td>1001</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1010</td>
      <td>1017</td>
      <td>1002</td>
      <td>1009</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1018</td>
      <td>1038</td>
      <td>1010</td>
      <td>1030</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1039</td>
      <td>1047</td>
      <td>1031</td>
      <td>1039</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1048</td>
      <td>1048</td>
      <td>1040</td>
      <td>1040</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1049</td>
      <td>1055</td>
      <td>1041</td>
      <td>1047</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3k07">3K07</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGHHHHHHMIEW</span><span class="topo-inside">I</span><span class="topo-unknown">IRRSVA</span><span class="topo-inside">NRFL</span><span class="topo-membrane">VLMGALFLSIWGTWTIIN</span><span class="topo-outside">TPVDALPDLSDVQVIIKTSYPGQAPQIVENQVTYPLTTTMLSVPGAKTVRGFSQFGDSYVYVIFEDGTDPYWARSRVLE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">YLNQVQGKLPAGVSAELGPDATGVGWIYEYALVDRSGKHDLADLRSLQDWFLKYELKTIPDVAEVASVGGVVKEYQVVIDPQRLAQYGISLAEVKSALDASNQEAGGSSIELAEAEYMVR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ASGYLQTLDDFNHIVLKASENGVPVYLRDVAKVQIGPEMRRGIAELNGEGEVAGGVVILRSGKNAREVIAAVKDKLETLKSSLPEGVEIVTTYDRSQLIDRAIDNL</span><span class="topo-membrane">SGKLLEEFIVVAVV</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">CALF</span><span class="topo-inside">LWHVRSA</span><span class="topo-membrane">LVAIISLPLGLCIAFIVMHFQ</span><span class="topo-outside">GLNANIMS</span><span class="topo-membrane">LGGIAIAVGAMVDAAIV</span><span class="topo-inside">MIENAHKRLEEWQHQHPDATLDNKTRWQVITDASVEVGPA</span><span class="topo-membrane">LFISLLIITLSFIPIFT</span><span class="topo-outside">LEGQEG</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">RLFGP</span><span class="topo-membrane">LAFTKTYAMAGAALLAIVVI</span><span class="topo-inside">PILMGYW</span><span class="topo-unknown">IRGKIPPESSN</span><span class="topo-inside">P</span><span class="topo-unknown">LNRFLIRVYHPLLLKVLH</span><span class="topo-inside">WPKT</span><span class="topo-membrane">TLLVAALSVLTVLWPLN</span><span class="topo-outside">KVGGEFLPQINEGDLLYMPSTLPGISAAEAASMLQKT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">DKLIMSVPEVARVFGKTGKAETATDSAPLEMVETTIQLKPQEQWRPGMTMDKIIEELDNTVRLPGLANLWVPPIRNRIDMLSTGIKSPIGIKVSGTVLADIDAMAEQIEEVARTVPGVAS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">ALAERLEGGRYINVEINREKAARYGMTVADVQLFVTSAVGGAMVGETVEGIARYPINLRYPQSWRDSPQALRQLPILTPMKQQITLADVADIKVSTGPSMLKTENARPTSWIYIDARDRD</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">MVSVVHDLQKAIAEKVQLKPGTSVAFSGQFELLERANHKL</span><span class="topo-membrane">KLMVPMTLMIIFVLLYLA</span><span class="topo-inside">FRRV</span><span class="topo-membrane">GEALLIISSVPFALVGGIWLLWWM</span><span class="topo-outside">GFHLSVAT</span><span class="topo-membrane">GTGFIALAGVAAEFGVV</span><span class="topo-inside">MLMYLRHAI</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050     </span>
<span class="topo-line"><span class="topo-inside">EAVPSLNNPQTFSEQKLDEALYHGAVLRVRPK</span><span class="topo-membrane">AMTVAVIIAGLLPILWG</span><span class="topo-outside">TGAGSEVM</span><span class="topo-membrane">SRIAAPMIGGMITAPLLSLFI</span><span class="topo-unknown">IPAAYKLMW</span><span class="topo-inside">L</span><span class="topo-unknown">HRHRVRK</span></span>
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
      <td>1</td>
      <td>12</td>
      <td>-7</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>13</td>
      <td>13</td>
      <td>5</td>
      <td>5</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>19</td>
      <td>6</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>20</td>
      <td>23</td>
      <td>12</td>
      <td>15</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>24</td>
      <td>41</td>
      <td>16</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>346</td>
      <td>34</td>
      <td>338</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>347</td>
      <td>364</td>
      <td>339</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>365</td>
      <td>371</td>
      <td>357</td>
      <td>363</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>372</td>
      <td>392</td>
      <td>364</td>
      <td>384</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>393</td>
      <td>400</td>
      <td>385</td>
      <td>392</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>401</td>
      <td>417</td>
      <td>393</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>418</td>
      <td>457</td>
      <td>410</td>
      <td>449</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>458</td>
      <td>474</td>
      <td>450</td>
      <td>466</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>485</td>
      <td>467</td>
      <td>477</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>486</td>
      <td>505</td>
      <td>478</td>
      <td>497</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>506</td>
      <td>512</td>
      <td>498</td>
      <td>504</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>513</td>
      <td>523</td>
      <td>505</td>
      <td>515</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>524</td>
      <td>524</td>
      <td>516</td>
      <td>516</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>542</td>
      <td>517</td>
      <td>534</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>543</td>
      <td>546</td>
      <td>535</td>
      <td>538</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>547</td>
      <td>563</td>
      <td>539</td>
      <td>555</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>564</td>
      <td>880</td>
      <td>556</td>
      <td>872</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>881</td>
      <td>898</td>
      <td>873</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>899</td>
      <td>902</td>
      <td>891</td>
      <td>894</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>903</td>
      <td>926</td>
      <td>895</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>927</td>
      <td>934</td>
      <td>919</td>
      <td>926</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>935</td>
      <td>951</td>
      <td>927</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>952</td>
      <td>992</td>
      <td>944</td>
      <td>984</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>993</td>
      <td>1009</td>
      <td>985</td>
      <td>1001</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1010</td>
      <td>1017</td>
      <td>1002</td>
      <td>1009</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1018</td>
      <td>1038</td>
      <td>1010</td>
      <td>1030</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1039</td>
      <td>1047</td>
      <td>1031</td>
      <td>1039</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1048</td>
      <td>1048</td>
      <td>1040</td>
      <td>1040</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1049</td>
      <td>1055</td>
      <td>1041</td>
      <td>1047</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3k07">3K07</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGHHHHHHMIEW</span><span class="topo-inside">I</span><span class="topo-unknown">IRRSVA</span><span class="topo-inside">NRFL</span><span class="topo-membrane">VLMGALFLSIWGTWTIIN</span><span class="topo-outside">TPVDALPDLSDVQVIIKTSYPGQAPQIVENQVTYPLTTTMLSVPGAKTVRGFSQFGDSYVYVIFEDGTDPYWARSRVLE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">YLNQVQGKLPAGVSAELGPDATGVGWIYEYALVDRSGKHDLADLRSLQDWFLKYELKTIPDVAEVASVGGVVKEYQVVIDPQRLAQYGISLAEVKSALDASNQEAGGSSIELAEAEYMVR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ASGYLQTLDDFNHIVLKASENGVPVYLRDVAKVQIGPEMRRGIAELNGEGEVAGGVVILRSGKNAREVIAAVKDKLETLKSSLPEGVEIVTTYDRSQLIDRAIDNL</span><span class="topo-membrane">SGKLLEEFIVVAVV</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">CALF</span><span class="topo-inside">LWHVRSA</span><span class="topo-membrane">LVAIISLPLGLCIAFIVMHFQ</span><span class="topo-outside">GLNANIMS</span><span class="topo-membrane">LGGIAIAVGAMVDAAIV</span><span class="topo-inside">MIENAHKRLEEWQHQHPDATLDNKTRWQVITDASVEVGPA</span><span class="topo-membrane">LFISLLIITLSFIPIFT</span><span class="topo-outside">LEGQEG</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">RLFGP</span><span class="topo-membrane">LAFTKTYAMAGAALLAIVVI</span><span class="topo-inside">PILMGYW</span><span class="topo-unknown">IRGKIPPESSN</span><span class="topo-inside">P</span><span class="topo-unknown">LNRFLIRVYHPLLLKVLH</span><span class="topo-inside">WPKT</span><span class="topo-membrane">TLLVAALSVLTVLWPLN</span><span class="topo-outside">KVGGEFLPQINEGDLLYMPSTLPGISAAEAASMLQKT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">DKLIMSVPEVARVFGKTGKAETATDSAPLEMVETTIQLKPQEQWRPGMTMDKIIEELDNTVRLPGLANLWVPPIRNRIDMLSTGIKSPIGIKVSGTVLADIDAMAEQIEEVARTVPGVAS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">ALAERLEGGRYINVEINREKAARYGMTVADVQLFVTSAVGGAMVGETVEGIARYPINLRYPQSWRDSPQALRQLPILTPMKQQITLADVADIKVSTGPSMLKTENARPTSWIYIDARDRD</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">MVSVVHDLQKAIAEKVQLKPGTSVAFSGQFELLERANHKL</span><span class="topo-membrane">KLMVPMTLMIIFVLLYLA</span><span class="topo-inside">FRRV</span><span class="topo-membrane">GEALLIISSVPFALVGGIWLLWWM</span><span class="topo-outside">GFHLSVAT</span><span class="topo-membrane">GTGFIALAGVAAEFGVV</span><span class="topo-inside">MLMYLRHAI</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050     </span>
<span class="topo-line"><span class="topo-inside">EAVPSLNNPQTFSEQKLDEALYHGAVLRVRPK</span><span class="topo-membrane">AMTVAVIIAGLLPILWG</span><span class="topo-outside">TGAGSEVM</span><span class="topo-membrane">SRIAAPMIGGMITAPLLSLFI</span><span class="topo-unknown">IPAAYKLMW</span><span class="topo-inside">L</span><span class="topo-unknown">HRHRVRK</span></span>
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
      <td>1</td>
      <td>12</td>
      <td>-7</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>13</td>
      <td>13</td>
      <td>5</td>
      <td>5</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>19</td>
      <td>6</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>20</td>
      <td>23</td>
      <td>12</td>
      <td>15</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>24</td>
      <td>41</td>
      <td>16</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>346</td>
      <td>34</td>
      <td>338</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>347</td>
      <td>364</td>
      <td>339</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>365</td>
      <td>371</td>
      <td>357</td>
      <td>363</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>372</td>
      <td>392</td>
      <td>364</td>
      <td>384</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>393</td>
      <td>400</td>
      <td>385</td>
      <td>392</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>401</td>
      <td>417</td>
      <td>393</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>418</td>
      <td>457</td>
      <td>410</td>
      <td>449</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>458</td>
      <td>474</td>
      <td>450</td>
      <td>466</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>485</td>
      <td>467</td>
      <td>477</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>486</td>
      <td>505</td>
      <td>478</td>
      <td>497</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>506</td>
      <td>512</td>
      <td>498</td>
      <td>504</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>513</td>
      <td>523</td>
      <td>505</td>
      <td>515</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>524</td>
      <td>524</td>
      <td>516</td>
      <td>516</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>542</td>
      <td>517</td>
      <td>534</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>543</td>
      <td>546</td>
      <td>535</td>
      <td>538</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>547</td>
      <td>563</td>
      <td>539</td>
      <td>555</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>564</td>
      <td>880</td>
      <td>556</td>
      <td>872</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>881</td>
      <td>898</td>
      <td>873</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>899</td>
      <td>902</td>
      <td>891</td>
      <td>894</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>903</td>
      <td>926</td>
      <td>895</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>927</td>
      <td>934</td>
      <td>919</td>
      <td>926</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>935</td>
      <td>951</td>
      <td>927</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>952</td>
      <td>992</td>
      <td>944</td>
      <td>984</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>993</td>
      <td>1009</td>
      <td>985</td>
      <td>1001</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1010</td>
      <td>1017</td>
      <td>1002</td>
      <td>1009</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1018</td>
      <td>1038</td>
      <td>1010</td>
      <td>1030</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1039</td>
      <td>1047</td>
      <td>1031</td>
      <td>1039</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1048</td>
      <td>1048</td>
      <td>1040</td>
      <td>1040</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1049</td>
      <td>1055</td>
      <td>1041</td>
      <td>1047</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3k07">3K07</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGHHHHHHMIEW</span><span class="topo-inside">I</span><span class="topo-unknown">IRRSVA</span><span class="topo-inside">NRFL</span><span class="topo-membrane">VLMGALFLSIWGTWTIIN</span><span class="topo-outside">TPVDALPDLSDVQVIIKTSYPGQAPQIVENQVTYPLTTTMLSVPGAKTVRGFSQFGDSYVYVIFEDGTDPYWARSRVLE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">YLNQVQGKLPAGVSAELGPDATGVGWIYEYALVDRSGKHDLADLRSLQDWFLKYELKTIPDVAEVASVGGVVKEYQVVIDPQRLAQYGISLAEVKSALDASNQEAGGSSIELAEAEYMVR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ASGYLQTLDDFNHIVLKASENGVPVYLRDVAKVQIGPEMRRGIAELNGEGEVAGGVVILRSGKNAREVIAAVKDKLETLKSSLPEGVEIVTTYDRSQLIDRAIDNL</span><span class="topo-membrane">SGKLLEEFIVVAVV</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">CALF</span><span class="topo-inside">LWHVRSA</span><span class="topo-membrane">LVAIISLPLGLCIAFIVMHFQ</span><span class="topo-outside">GLNANIMS</span><span class="topo-membrane">LGGIAIAVGAMVDAAIV</span><span class="topo-inside">MIENAHKRLEEWQHQHPDATLDNKTRWQVITDASVEVGPA</span><span class="topo-membrane">LFISLLIITLSFIPIFT</span><span class="topo-outside">LEGQEG</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">RLFGP</span><span class="topo-membrane">LAFTKTYAMAGAALLAIVVI</span><span class="topo-inside">PILMGYW</span><span class="topo-unknown">IRGKIPPESSN</span><span class="topo-inside">P</span><span class="topo-unknown">LNRFLIRVYHPLLLKVLH</span><span class="topo-inside">WPKT</span><span class="topo-membrane">TLLVAALSVLTVLWPLN</span><span class="topo-outside">KVGGEFLPQINEGDLLYMPSTLPGISAAEAASMLQKT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">DKLIMSVPEVARVFGKTGKAETATDSAPLEMVETTIQLKPQEQWRPGMTMDKIIEELDNTVRLPGLANLWVPPIRNRIDMLSTGIKSPIGIKVSGTVLADIDAMAEQIEEVARTVPGVAS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">ALAERLEGGRYINVEINREKAARYGMTVADVQLFVTSAVGGAMVGETVEGIARYPINLRYPQSWRDSPQALRQLPILTPMKQQITLADVADIKVSTGPSMLKTENARPTSWIYIDARDRD</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">MVSVVHDLQKAIAEKVQLKPGTSVAFSGQFELLERANHKL</span><span class="topo-membrane">KLMVPMTLMIIFVLLYLA</span><span class="topo-inside">FRRV</span><span class="topo-membrane">GEALLIISSVPFALVGGIWLLWWM</span><span class="topo-outside">GFHLSVAT</span><span class="topo-membrane">GTGFIALAGVAAEFGVV</span><span class="topo-inside">MLMYLRHAI</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050     </span>
<span class="topo-line"><span class="topo-inside">EAVPSLNNPQTFSEQKLDEALYHGAVLRVRPK</span><span class="topo-membrane">AMTVAVIIAGLLPILWG</span><span class="topo-outside">TGAGSEVM</span><span class="topo-membrane">SRIAAPMIGGMITAPLLSLFI</span><span class="topo-unknown">IPAAYKLMW</span><span class="topo-inside">L</span><span class="topo-unknown">HRHRVRK</span></span>
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
      <td>1</td>
      <td>12</td>
      <td>-7</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>13</td>
      <td>13</td>
      <td>5</td>
      <td>5</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>19</td>
      <td>6</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>20</td>
      <td>23</td>
      <td>12</td>
      <td>15</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>24</td>
      <td>41</td>
      <td>16</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>346</td>
      <td>34</td>
      <td>338</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>347</td>
      <td>364</td>
      <td>339</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>365</td>
      <td>371</td>
      <td>357</td>
      <td>363</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>372</td>
      <td>392</td>
      <td>364</td>
      <td>384</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>393</td>
      <td>400</td>
      <td>385</td>
      <td>392</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>401</td>
      <td>417</td>
      <td>393</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>418</td>
      <td>457</td>
      <td>410</td>
      <td>449</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>458</td>
      <td>474</td>
      <td>450</td>
      <td>466</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>485</td>
      <td>467</td>
      <td>477</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>486</td>
      <td>505</td>
      <td>478</td>
      <td>497</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>506</td>
      <td>512</td>
      <td>498</td>
      <td>504</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>513</td>
      <td>523</td>
      <td>505</td>
      <td>515</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>524</td>
      <td>524</td>
      <td>516</td>
      <td>516</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>542</td>
      <td>517</td>
      <td>534</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>543</td>
      <td>546</td>
      <td>535</td>
      <td>538</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>547</td>
      <td>563</td>
      <td>539</td>
      <td>555</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>564</td>
      <td>880</td>
      <td>556</td>
      <td>872</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>881</td>
      <td>898</td>
      <td>873</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>899</td>
      <td>902</td>
      <td>891</td>
      <td>894</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>903</td>
      <td>926</td>
      <td>895</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>927</td>
      <td>934</td>
      <td>919</td>
      <td>926</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>935</td>
      <td>951</td>
      <td>927</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>952</td>
      <td>992</td>
      <td>944</td>
      <td>984</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>993</td>
      <td>1009</td>
      <td>985</td>
      <td>1001</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1010</td>
      <td>1017</td>
      <td>1002</td>
      <td>1009</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1018</td>
      <td>1038</td>
      <td>1010</td>
      <td>1030</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1039</td>
      <td>1047</td>
      <td>1031</td>
      <td>1039</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1048</td>
      <td>1048</td>
      <td>1040</td>
      <td>1040</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1049</td>
      <td>1055</td>
      <td>1041</td>
      <td>1047</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3k07">3K07</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGHHHHHHMIEW</span><span class="topo-inside">I</span><span class="topo-unknown">IRRSVA</span><span class="topo-inside">NRFL</span><span class="topo-membrane">VLMGALFLSIWGTWTIIN</span><span class="topo-outside">TPVDALPDLSDVQVIIKTSYPGQAPQIVENQVTYPLTTTMLSVPGAKTVRGFSQFGDSYVYVIFEDGTDPYWARSRVLE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">YLNQVQGKLPAGVSAELGPDATGVGWIYEYALVDRSGKHDLADLRSLQDWFLKYELKTIPDVAEVASVGGVVKEYQVVIDPQRLAQYGISLAEVKSALDASNQEAGGSSIELAEAEYMVR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ASGYLQTLDDFNHIVLKASENGVPVYLRDVAKVQIGPEMRRGIAELNGEGEVAGGVVILRSGKNAREVIAAVKDKLETLKSSLPEGVEIVTTYDRSQLIDRAIDNL</span><span class="topo-membrane">SGKLLEEFIVVAVV</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">CALF</span><span class="topo-inside">LWHVRSA</span><span class="topo-membrane">LVAIISLPLGLCIAFIVMHFQ</span><span class="topo-outside">GLNANIMS</span><span class="topo-membrane">LGGIAIAVGAMVDAAIV</span><span class="topo-inside">MIENAHKRLEEWQHQHPDATLDNKTRWQVITDASVEVGPA</span><span class="topo-membrane">LFISLLIITLSFIPIFT</span><span class="topo-outside">LEGQEG</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">RLFGP</span><span class="topo-membrane">LAFTKTYAMAGAALLAIVVI</span><span class="topo-inside">PILMGYW</span><span class="topo-unknown">IRGKIPPESSN</span><span class="topo-inside">P</span><span class="topo-unknown">LNRFLIRVYHPLLLKVLH</span><span class="topo-inside">WPKT</span><span class="topo-membrane">TLLVAALSVLTVLWPLN</span><span class="topo-outside">KVGGEFLPQINEGDLLYMPSTLPGISAAEAASMLQKT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">DKLIMSVPEVARVFGKTGKAETATDSAPLEMVETTIQLKPQEQWRPGMTMDKIIEELDNTVRLPGLANLWVPPIRNRIDMLSTGIKSPIGIKVSGTVLADIDAMAEQIEEVARTVPGVAS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">ALAERLEGGRYINVEINREKAARYGMTVADVQLFVTSAVGGAMVGETVEGIARYPINLRYPQSWRDSPQALRQLPILTPMKQQITLADVADIKVSTGPSMLKTENARPTSWIYIDARDRD</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">MVSVVHDLQKAIAEKVQLKPGTSVAFSGQFELLERANHKL</span><span class="topo-membrane">KLMVPMTLMIIFVLLYLA</span><span class="topo-inside">FRRV</span><span class="topo-membrane">GEALLIISSVPFALVGGIWLLWWM</span><span class="topo-outside">GFHLSVAT</span><span class="topo-membrane">GTGFIALAGVAAEFGVV</span><span class="topo-inside">MLMYLRHAI</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050     </span>
<span class="topo-line"><span class="topo-inside">EAVPSLNNPQTFSEQKLDEALYHGAVLRVRPK</span><span class="topo-membrane">AMTVAVIIAGLLPILWG</span><span class="topo-outside">TGAGSEVM</span><span class="topo-membrane">SRIAAPMIGGMITAPLLSLFI</span><span class="topo-unknown">IPAAYKLMW</span><span class="topo-inside">L</span><span class="topo-unknown">HRHRVRK</span></span>
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
      <td>1</td>
      <td>12</td>
      <td>-7</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>13</td>
      <td>13</td>
      <td>5</td>
      <td>5</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>19</td>
      <td>6</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>20</td>
      <td>23</td>
      <td>12</td>
      <td>15</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>24</td>
      <td>41</td>
      <td>16</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>346</td>
      <td>34</td>
      <td>338</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>347</td>
      <td>364</td>
      <td>339</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>365</td>
      <td>371</td>
      <td>357</td>
      <td>363</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>372</td>
      <td>392</td>
      <td>364</td>
      <td>384</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>393</td>
      <td>400</td>
      <td>385</td>
      <td>392</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>401</td>
      <td>417</td>
      <td>393</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>418</td>
      <td>457</td>
      <td>410</td>
      <td>449</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>458</td>
      <td>474</td>
      <td>450</td>
      <td>466</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>485</td>
      <td>467</td>
      <td>477</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>486</td>
      <td>505</td>
      <td>478</td>
      <td>497</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>506</td>
      <td>512</td>
      <td>498</td>
      <td>504</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>513</td>
      <td>523</td>
      <td>505</td>
      <td>515</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>524</td>
      <td>524</td>
      <td>516</td>
      <td>516</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>542</td>
      <td>517</td>
      <td>534</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>543</td>
      <td>546</td>
      <td>535</td>
      <td>538</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>547</td>
      <td>563</td>
      <td>539</td>
      <td>555</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>564</td>
      <td>880</td>
      <td>556</td>
      <td>872</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>881</td>
      <td>898</td>
      <td>873</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>899</td>
      <td>902</td>
      <td>891</td>
      <td>894</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>903</td>
      <td>926</td>
      <td>895</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>927</td>
      <td>934</td>
      <td>919</td>
      <td>926</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>935</td>
      <td>951</td>
      <td>927</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>952</td>
      <td>992</td>
      <td>944</td>
      <td>984</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>993</td>
      <td>1009</td>
      <td>985</td>
      <td>1001</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1010</td>
      <td>1017</td>
      <td>1002</td>
      <td>1009</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1018</td>
      <td>1038</td>
      <td>1010</td>
      <td>1030</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1039</td>
      <td>1047</td>
      <td>1031</td>
      <td>1039</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1048</td>
      <td>1048</td>
      <td>1040</td>
      <td>1040</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1049</td>
      <td>1055</td>
      <td>1041</td>
      <td>1047</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3k07">3K07</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGHHHHHHMIEW</span><span class="topo-inside">I</span><span class="topo-unknown">IRRSVA</span><span class="topo-inside">NRFL</span><span class="topo-membrane">VLMGALFLSIWGTWTIIN</span><span class="topo-outside">TPVDALPDLSDVQVIIKTSYPGQAPQIVENQVTYPLTTTMLSVPGAKTVRGFSQFGDSYVYVIFEDGTDPYWARSRVLE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">YLNQVQGKLPAGVSAELGPDATGVGWIYEYALVDRSGKHDLADLRSLQDWFLKYELKTIPDVAEVASVGGVVKEYQVVIDPQRLAQYGISLAEVKSALDASNQEAGGSSIELAEAEYMVR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ASGYLQTLDDFNHIVLKASENGVPVYLRDVAKVQIGPEMRRGIAELNGEGEVAGGVVILRSGKNAREVIAAVKDKLETLKSSLPEGVEIVTTYDRSQLIDRAIDNL</span><span class="topo-membrane">SGKLLEEFIVVAVV</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">CALF</span><span class="topo-inside">LWHVRSA</span><span class="topo-membrane">LVAIISLPLGLCIAFIVMHFQ</span><span class="topo-outside">GLNANIMS</span><span class="topo-membrane">LGGIAIAVGAMVDAAIV</span><span class="topo-inside">MIENAHKRLEEWQHQHPDATLDNKTRWQVITDASVEVGPA</span><span class="topo-membrane">LFISLLIITLSFIPIFT</span><span class="topo-outside">LEGQEG</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">RLFGP</span><span class="topo-membrane">LAFTKTYAMAGAALLAIVVI</span><span class="topo-inside">PILMGYW</span><span class="topo-unknown">IRGKIPPESSN</span><span class="topo-inside">P</span><span class="topo-unknown">LNRFLIRVYHPLLLKVLH</span><span class="topo-inside">WPKT</span><span class="topo-membrane">TLLVAALSVLTVLWPLN</span><span class="topo-outside">KVGGEFLPQINEGDLLYMPSTLPGISAAEAASMLQKT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">DKLIMSVPEVARVFGKTGKAETATDSAPLEMVETTIQLKPQEQWRPGMTMDKIIEELDNTVRLPGLANLWVPPIRNRIDMLSTGIKSPIGIKVSGTVLADIDAMAEQIEEVARTVPGVAS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">ALAERLEGGRYINVEINREKAARYGMTVADVQLFVTSAVGGAMVGETVEGIARYPINLRYPQSWRDSPQALRQLPILTPMKQQITLADVADIKVSTGPSMLKTENARPTSWIYIDARDRD</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">MVSVVHDLQKAIAEKVQLKPGTSVAFSGQFELLERANHKL</span><span class="topo-membrane">KLMVPMTLMIIFVLLYLA</span><span class="topo-inside">FRRV</span><span class="topo-membrane">GEALLIISSVPFALVGGIWLLWWM</span><span class="topo-outside">GFHLSVAT</span><span class="topo-membrane">GTGFIALAGVAAEFGVV</span><span class="topo-inside">MLMYLRHAI</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050     </span>
<span class="topo-line"><span class="topo-inside">EAVPSLNNPQTFSEQKLDEALYHGAVLRVRPK</span><span class="topo-membrane">AMTVAVIIAGLLPILWG</span><span class="topo-outside">TGAGSEVM</span><span class="topo-membrane">SRIAAPMIGGMITAPLLSLFI</span><span class="topo-unknown">IPAAYKLMW</span><span class="topo-inside">L</span><span class="topo-unknown">HRHRVRK</span></span>
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
      <td>1</td>
      <td>12</td>
      <td>-7</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>13</td>
      <td>13</td>
      <td>5</td>
      <td>5</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>19</td>
      <td>6</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>20</td>
      <td>23</td>
      <td>12</td>
      <td>15</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>24</td>
      <td>41</td>
      <td>16</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>346</td>
      <td>34</td>
      <td>338</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>347</td>
      <td>364</td>
      <td>339</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>365</td>
      <td>371</td>
      <td>357</td>
      <td>363</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>372</td>
      <td>392</td>
      <td>364</td>
      <td>384</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>393</td>
      <td>400</td>
      <td>385</td>
      <td>392</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>401</td>
      <td>417</td>
      <td>393</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>418</td>
      <td>457</td>
      <td>410</td>
      <td>449</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>458</td>
      <td>474</td>
      <td>450</td>
      <td>466</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>485</td>
      <td>467</td>
      <td>477</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>486</td>
      <td>505</td>
      <td>478</td>
      <td>497</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>506</td>
      <td>512</td>
      <td>498</td>
      <td>504</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>513</td>
      <td>523</td>
      <td>505</td>
      <td>515</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>524</td>
      <td>524</td>
      <td>516</td>
      <td>516</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>542</td>
      <td>517</td>
      <td>534</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>543</td>
      <td>546</td>
      <td>535</td>
      <td>538</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>547</td>
      <td>563</td>
      <td>539</td>
      <td>555</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>564</td>
      <td>880</td>
      <td>556</td>
      <td>872</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>881</td>
      <td>898</td>
      <td>873</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>899</td>
      <td>902</td>
      <td>891</td>
      <td>894</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>903</td>
      <td>926</td>
      <td>895</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>927</td>
      <td>934</td>
      <td>919</td>
      <td>926</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>935</td>
      <td>951</td>
      <td>927</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>952</td>
      <td>992</td>
      <td>944</td>
      <td>984</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>993</td>
      <td>1009</td>
      <td>985</td>
      <td>1001</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1010</td>
      <td>1017</td>
      <td>1002</td>
      <td>1009</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1018</td>
      <td>1038</td>
      <td>1010</td>
      <td>1030</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1039</td>
      <td>1047</td>
      <td>1031</td>
      <td>1039</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1048</td>
      <td>1048</td>
      <td>1040</td>
      <td>1040</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1049</td>
      <td>1055</td>
      <td>1041</td>
      <td>1047</td>
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

### Metal binding via three-methionine cluster in periplasmic cleft

The primary metal-binding site is formed by M573, M623, and M672, located in the cleft region between the PC1 and PC2 subdomains of the periplasmic domain. In the apo state, the cleft is closed. Upon Cu(I) or Ag(I) binding, the PC2 subdomain swings ~30° (hinge at G721/P810) to open the cleft. The horizontal helix (residues 665-675) tilts upward by 21°, allowing M672 to move closer to M573 and M623 to form a transient three-sulfur coordination site. TM8 also shifts vertically by ~10 Å at its N-terminal end.

### Methionine relay network for stepwise metal transport

CusA contains five methionine pairs/clusters that form a relay network: the primary three-methionine site (M573/M623/M672), and four methionine pairs - M271/M755 (periplasmic domain), M391/M1009, M403/M486, and M410/M501 (transmembrane region). CAVER analysis shows these sites form a continuous channel spanning the transmembrane region to the periplasmic funnel. Transport assay mutants (M573I, M623I, M672I, M391I, M486I, M755I) lost Ag+ transport activity, confirming their essential roles. This suggests a stepwise shuttle mechanism where metal ions pass sequentially between methionine pairs.

### Proton-relay network for energy coupling

Conserved charged residues D405 (TM4), E939, and K984 form a potential proton-relay network. Mutants D405A, E939A, and K984A lost Ag+ transport activity in reconstituted liposome assays, confirming their essential role in proton translocation and energy coupling for active metal export.

### Alternating-access mechanism

Dynamics simulations using an elastic network model suggest CusA operates through three coupled motions in which the periplasmic clefts formed by PC1 and PC2 subdomains alternately open and close. This alternating-access mechanism, similar to AcrB, allows coordinated metal ion uptake from both cytoplasm and periplasm and extrusion through the CusC outer-membrane channel.

### Substrate uptake from both cytoplasm and periplasm

The structures suggest CusA can pick up metal ions from both the cytoplasm (via methionine pairs in the transmembrane region that line a channel) and the periplasm (via the open periplasmic cleft). Metal ions bind to the three-methionine site directly through the periplasmic cleft or via the methionine pairs within the transmembrane region, then are transferred stepwise to the M271/M755 pair and released into the central funnel for extrusion through CusC.


## Cross-References
