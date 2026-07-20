---
title: "CusA Inner Membrane Efflux Pump"
created: 2026-05-27
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2009.08.029, doi/10.1038##nature09743]
verified: agent
uniprot_id: ['P38054', 'P77239']
---

# CusA Inner Membrane Efflux Pump

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P38054">UniProt: P38054</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P77239">UniProt: P77239</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

CusA is the inner-membrane component of the CusABC tripartite copper/silver efflux system in Escherichia coli. It is the sole heavy-metal efflux RND (Resistance-Nodulation-Cell Division) transporter in E. coli, specifically recognizing and conferring resistance to Ag(I) and [Cu(i)](/xray-mp-wiki/reagents/ligands/cu(i)) ions. CusA is driven by proton import and exports these toxic metal ions directly out of the cell. The protein was overproduced with an N-terminal 6xHis tag and purified by Ni2+-affinity and size exclusion chromatography. Although no crystal structure of CusA was solved in this study, a structural model was generated based on the AcrB crystal structure and sequence alignment, revealing that the periplasmic domain (residues 148-157) is positioned above the vestibule region facing the periplasm, where it interacts with the CusB membrane fusion protein.

## Publications

### doi/10.1016##j.jmb.2009.08.029

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3ooc">3OOC</a></td>
      <td>not solved</td>
      <td>--</td>
      <td>Full-length CusA with N-terminal 6xHis tag; structural model based on <a href="/xray-mp-wiki/proteins/acrB">Acrb</a> (PDB 1WXU)</td>
      <td>--</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) delta acrB
- **Construct**: Full-length CusA with N-terminal 6xHis tag, overproduced from pET15b cusA expression vector. Host strain BL21(DE3) delta acrB has deletion in chromosomal acrB gene.

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
      <td>Cell growth and induction</td>
      <td>Cells grown in 12 L LB medium with 100 ug/ml <a href="/xray-mp-wiki/reagents/antibiotics/ampicillin">Ampicillin</a> at 37 C, induced with 1 mM IPTG at OD600 ~0.5, harvested within 3 h</td>
      <td>--</td>
      <td>LB medium with 100 ug/ml ampicillin + --</td>
      <td>BL21(DE3) delta acrB host strain used</td>
    </tr>
    <tr>
      <td>Cell lysis and membrane isolation</td>
      <td>Cells disrupted with French pressure cell; membrane fraction collected and washed twice with high-salt buffer (20 mM sodium phosphate pH 7.2, 2 M KCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 1 mM EDTA, 1 mM PMSF) and once with 20 mM Hepes-NaOH (pH 7.5) containing 1 mM PMSF</td>
      <td>--</td>
      <td>100 mM sodium phosphate (pH 7.2), 10% glycerol, 1 mM EDTA, 1 mM <a href="/xray-mp-wiki/reagents/additives/pmsf">PMSF</a> (low-salt); 20 mM sodium phosphate (pH 7.2), 2 M KCl, 10% glycerol, 1 mM EDTA, 1 mM PMSF (high-salt wash) + --</td>
      <td>Membrane fraction collected by ultracentrifugation</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Membrane protein solubilized in 1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>; insoluble material removed by ultracentrifugation at 370,000g</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a>-NaOH (pH 7.5) + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Ultracentrifugation at 370,000g to remove insoluble material</td>
    </tr>
    <tr>
      <td>Ni2+ affinity chromatography</td>
      <td>Ni2+-affinity column chromatography</td>
      <td>Ni2+-affinity resin</td>
      <td>20 mM Hepes-NaOH (pH 7.5) + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>His-tagged CusA captured on Ni2+ column</td>
    </tr>
    <tr>
      <td>Size exclusion chromatography</td>
      <td>G-200 sizing column chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM Na-Hepes (pH 7.5) + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Purity >95% by 10% SDS-PAGE stained with Coomassie Brilliant Blue; concentrated to 20 mg/ml</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>not performed</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>CusA crystal structure was not solved in this study. A structural model was generated based on the AcrB crystal structure and protein sequence alignment. CusA and AcrB share only 19% sequence identity.</td>
    </tr>
  </tbody>
</table>
### doi/10.1038##nature09743

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3ne5">3NE5</a></td>
      <td>2.90 A</td>
      <td>--</td>
      <td>CusA residues 4-1043 in CusBA co-crystal structure; CusA present as trimer</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/cymal-6">Cymal 6</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) delta acrB
- **Construct**: Full-length CusA with N-terminal 6xHis tag, overproduced from pET15b cusA expression vector. Host strain BL21(DE3) delta acrB has deletion in chromosomal acrB gene.

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>0.1 mM CusA and 0.1 mM <a href="/xray-mp-wiki/proteins/cusB">Cusb</a> in 20 mM Na-HEPES pH 7.5, 0.05% CYMAL-6</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>10% PEG 6000, 0.1 M Na-HEPES pH 7.5, 0.1 M ammonium <a href="/xray-mp-wiki/reagents/buffers/acetate">Acetate</a>, 20% glycerol</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2 months</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Stepwise glycerol increase to 30% in 5% increments</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>CusA (native) - CusB (SeMet-substituted) co-crystal. Grew within 2 months in sitting-drop vapor diffusion.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ne5">3NE5</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKKIALIIGSMIAGGIISAAGFTWVAKAEPPAEKTSTAERKILFWYDPMYPNTRFDKPGKSPFMDMDLVPKYADEESS</span><span class="topo-outside">ASGVRIDPTQTQNLGVKTATVTRGPLTFAQSFPANVSYNEYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">YAIVQARAAGFIDKVYPLTVGDKVQKGTPLLDLTIPDWVEAQSEYLLLRETGGTATQTEGILERLRLAGMPEADIRRLIATQKIQTRFTLKAPIDGVITAFDLRAGMNIAKDNVVAKIQG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">MDPVWVTAAIPESIAWLVKDASQFTLTVPARPDKTLTIRKWTLLPGVDAATRTLQLRLEVDNADEALKPGMNAWLQLNTASEPMLLIPSQALIDTGSEQRVITVDADGRFVPKRVAVFQA</span></span>
<span class="topo-ruler">       370       380       390       400       410   </span>
<span class="topo-line"><span class="topo-outside">SQGVTALRSGLAEGEKVVSSGLFLIDSEANISGALERMRS</span><span class="topo-unknown">ESATHAHHHHHHH</span></span>
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
      <td>78</td>
      <td>1</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>400</td>
      <td>79</td>
      <td>400</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>401</td>
      <td>413</td>
      <td>401</td>
      <td>413</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ne5">3NE5</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">HHHHHHMGIE</span><span class="topo-inside">W</span><span class="topo-unknown">IIRRSVA</span><span class="topo-inside">NRFL</span><span class="topo-membrane">VLMGALFLSIWGTWTII</span><span class="topo-outside">NTPVDALPDLSDVQVIIKTSYPGQAPQIVENQVTYPLTTTMLSVPGAKTVRGFSQFGDSYVYVIFEDGTDPYWARSRVLEY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LNQVQGKLPAGVSAELGPDATGVGWIYEYALVDRSGKHDLADLRSLQDWFLKYELKTIPDVAEVASVGGVVKEYQVVIDPQRLAQYGISLAEVKSALDASNQEAGGSSIELAEAEYMVRA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">SGYLQTLDDFNHIVLKASENGVPVYLRDVAKVQIGPEMRRGIAELNGEGEVAGGVVILRSGKNAREVIAAVKDKLETLKSSLPEGVEIVTTYDRSQLIDRAIDNL</span><span class="topo-membrane">SGKLLEEFIVVAVVC</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">ALF</span><span class="topo-inside">LWHVRSA</span><span class="topo-membrane">LVAIISLPLGLCIAFIVMHFQ</span><span class="topo-outside">GLNANIMS</span><span class="topo-membrane">LGGIAIAVGAMVDAAIV</span><span class="topo-inside">MIENAHKRLEEWQHQHPDATLDNKTRWQVITDASVEVGPA</span><span class="topo-membrane">LFISLLIITLSFIPIFT</span><span class="topo-outside">LEGQEGR</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">LFGP</span><span class="topo-membrane">LAFTKTYAMAGAALLAIVVI</span><span class="topo-inside">PILMGYW</span><span class="topo-unknown">IRGKIPPESSNP</span><span class="topo-inside">L</span><span class="topo-unknown">NRFLIRVYHPLLLKV</span><span class="topo-inside">LHWPKTT</span><span class="topo-membrane">LLVAALSVLTVLWPLN</span><span class="topo-outside">KVGGEFLPQINEGDLLYMPSTLPGISAAEAASMLQKTD</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">KLIMSVPEVARVFGKTGKAETATDSAPLEMVETTIQLKPQEQWRPGMTMDKIIEELDNTVRLPGLANLWVPPIRNRIDMLSTGIKSPIGIKVSGTVLADIDAMAEQIEEVARTVPGVASA</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">LAERLEGGRYINVEINREKAARYGMTVADVQLFVTSAVGGAMVGETVEGIARYPINLRYPQSWRDSPQALRQLPILTPMKQQITLADVADIKVSTGPSMLKTENARPTSWIYIDARDRDM</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">VSVVHDLQKAIAEKVQLKPGTSVAFSGQFELLERANHKL</span><span class="topo-membrane">KLMVPMTLMIIFVLLYLA</span><span class="topo-inside">FRRVGEA</span><span class="topo-membrane">LLIISSVPFALVGGIWLLWWM</span><span class="topo-outside">GFHLSVAT</span><span class="topo-membrane">GTGFIALAGVAAEFGVV</span><span class="topo-inside">MLMYLRHAIE</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050    </span>
<span class="topo-line"><span class="topo-inside">AVPSLNNPQTFSEQKLDEALYHGAVLRVRPK</span><span class="topo-membrane">AMTVAVIIAGLLPILWG</span><span class="topo-outside">TGAGSEVM</span><span class="topo-membrane">SRIAAPMIGGMITAPLLSL</span><span class="topo-inside">FIIPAAYKLMWLHRH</span><span class="topo-unknown">RVRK</span></span>
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
      <td>-6</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>11</td>
      <td>4</td>
      <td>4</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>18</td>
      <td>5</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>22</td>
      <td>12</td>
      <td>15</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>39</td>
      <td>16</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>345</td>
      <td>33</td>
      <td>338</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>346</td>
      <td>363</td>
      <td>339</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>370</td>
      <td>357</td>
      <td>363</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>371</td>
      <td>391</td>
      <td>364</td>
      <td>384</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>392</td>
      <td>399</td>
      <td>385</td>
      <td>392</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>416</td>
      <td>393</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>417</td>
      <td>456</td>
      <td>410</td>
      <td>449</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>457</td>
      <td>473</td>
      <td>450</td>
      <td>466</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>474</td>
      <td>484</td>
      <td>467</td>
      <td>477</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>485</td>
      <td>504</td>
      <td>478</td>
      <td>497</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>505</td>
      <td>511</td>
      <td>498</td>
      <td>504</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>523</td>
      <td>505</td>
      <td>516</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>524</td>
      <td>524</td>
      <td>517</td>
      <td>517</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>539</td>
      <td>518</td>
      <td>532</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>540</td>
      <td>546</td>
      <td>533</td>
      <td>539</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>547</td>
      <td>562</td>
      <td>540</td>
      <td>555</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>563</td>
      <td>879</td>
      <td>556</td>
      <td>872</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>880</td>
      <td>897</td>
      <td>873</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>898</td>
      <td>904</td>
      <td>891</td>
      <td>897</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>905</td>
      <td>925</td>
      <td>898</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>926</td>
      <td>933</td>
      <td>919</td>
      <td>926</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>934</td>
      <td>950</td>
      <td>927</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>951</td>
      <td>991</td>
      <td>944</td>
      <td>984</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1008</td>
      <td>985</td>
      <td>1001</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1009</td>
      <td>1016</td>
      <td>1002</td>
      <td>1009</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1017</td>
      <td>1035</td>
      <td>1010</td>
      <td>1028</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1036</td>
      <td>1050</td>
      <td>1029</td>
      <td>1043</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1051</td>
      <td>1054</td>
      <td>1044</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ne5">3NE5</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKKIALIIGSMIAGGIISAAGFTWVAKAEPPAEKTSTAERKILFWYDPMYPNTRFDKPGKSPFMDMDLVPKYADEESS</span><span class="topo-outside">ASGVRIDPTQTQNLGVKTATVTRGPLTFAQSFPANVSYNEYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">YAIVQARAAGFIDKVYPLTVGDKVQKGTPLLDLTIPDWVEAQSEYLLLRETGGTATQTEGILERLRLAGMPEADIRRLIATQKIQTRFTLKAPIDGVITAFDLRAGMNIAKDNVVAKIQG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">MDPVWVTAAIPESIAWLVKDASQFTLTVPARPDKTLTIRKWTLLPGVDAATRTLQLRLEVDNADEALKPGMNAWLQLNTASEPMLLIPSQALIDTGSEQRVITVDADGRFVPKRVAVFQA</span></span>
<span class="topo-ruler">       370       380       390       400       410   </span>
<span class="topo-line"><span class="topo-outside">SQGVTALRSGLAEGEKVVSSGLFLIDSEANISGALERMRS</span><span class="topo-unknown">ESATHAHHHHHHH</span></span>
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
      <td>78</td>
      <td>1</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>400</td>
      <td>79</td>
      <td>400</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>401</td>
      <td>413</td>
      <td>401</td>
      <td>413</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ne5">3NE5</a> — Chain F (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKKIALIIGSMIAGGIISAAGFTWVAKAEPPAEKTSTAERKILFWYDPMYPNTRFDKPGKSPFMDMDLVPKYADEESS</span><span class="topo-outside">ASGVRIDPTQTQNLGVKTATVTRGPLTFAQSFPANVSYNEYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">YAIVQARAAGFIDKVYPLTVGDKVQKGTPLLDLTIPDWVEAQSEYLLLRETGGTATQTEGILERLRLAGMPEADIRRLIATQKIQTRFTLKAPIDGVITAFDLRAGMNIAKDNVVAKIQG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">MDPVWVTAAIPESIAWLVKDASQFTLTVPARPDKTLTIRKWTLLPGVDAATRTLQLRLEVDNADEALKPGMNAWLQLNTASEPMLLIPSQALIDTGSEQRVITVDADGRFVPKRVAVFQA</span></span>
<span class="topo-ruler">       370       380       390       400       410   </span>
<span class="topo-line"><span class="topo-outside">SQGVTALRSGLAEGEKVVSSGLFLIDSEANISGALERMRS</span><span class="topo-unknown">ESATHAHHHHHHH</span></span>
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
      <td>78</td>
      <td>1</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>400</td>
      <td>79</td>
      <td>400</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>401</td>
      <td>413</td>
      <td>401</td>
      <td>413</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ne5">3NE5</a> — Chain H (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">HHHHHHMGIE</span><span class="topo-inside">W</span><span class="topo-unknown">IIRRSVA</span><span class="topo-inside">NRFL</span><span class="topo-membrane">VLMGALFLSIWGTWTII</span><span class="topo-outside">NTPVDALPDLSDVQVIIKTSYPGQAPQIVENQVTYPLTTTMLSVPGAKTVRGFSQFGDSYVYVIFEDGTDPYWARSRVLEY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LNQVQGKLPAGVSAELGPDATGVGWIYEYALVDRSGKHDLADLRSLQDWFLKYELKTIPDVAEVASVGGVVKEYQVVIDPQRLAQYGISLAEVKSALDASNQEAGGSSIELAEAEYMVRA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">SGYLQTLDDFNHIVLKASENGVPVYLRDVAKVQIGPEMRRGIAELNGEGEVAGGVVILRSGKNAREVIAAVKDKLETLKSSLPEGVEIVTTYDRSQLIDRAIDNL</span><span class="topo-membrane">SGKLLEEFIVVAVVC</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">ALF</span><span class="topo-inside">LWHVRSA</span><span class="topo-membrane">LVAIISLPLGLCIAFIVMHFQ</span><span class="topo-outside">GLNANIMS</span><span class="topo-membrane">LGGIAIAVGAMVDAAIV</span><span class="topo-inside">MIENAHKRLEEWQHQHPDATLDNKTRWQVITDASVEVGPA</span><span class="topo-membrane">LFISLLIITLSFIPIFT</span><span class="topo-outside">LEGQEGR</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">LFGP</span><span class="topo-membrane">LAFTKTYAMAGAALLAIVVI</span><span class="topo-inside">PILMGYW</span><span class="topo-unknown">IRGKIPPESSNP</span><span class="topo-inside">L</span><span class="topo-unknown">NRFLIRVYHPLLLKV</span><span class="topo-inside">LHWPKTT</span><span class="topo-membrane">LLVAALSVLTVLWPLN</span><span class="topo-outside">KVGGEFLPQINEGDLLYMPSTLPGISAAEAASMLQKTD</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">KLIMSVPEVARVFGKTGKAETATDSAPLEMVETTIQLKPQEQWRPGMTMDKIIEELDNTVRLPGLANLWVPPIRNRIDMLSTGIKSPIGIKVSGTVLADIDAMAEQIEEVARTVPGVASA</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">LAERLEGGRYINVEINREKAARYGMTVADVQLFVTSAVGGAMVGETVEGIARYPINLRYPQSWRDSPQALRQLPILTPMKQQITLADVADIKVSTGPSMLKTENARPTSWIYIDARDRDM</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">VSVVHDLQKAIAEKVQLKPGTSVAFSGQFELLERANHKL</span><span class="topo-membrane">KLMVPMTLMIIFVLLYLA</span><span class="topo-inside">FRRVGEA</span><span class="topo-membrane">LLIISSVPFALVGGIWLLWWM</span><span class="topo-outside">GFHLSVAT</span><span class="topo-membrane">GTGFIALAGVAAEFGVV</span><span class="topo-inside">MLMYLRHAIE</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050    </span>
<span class="topo-line"><span class="topo-inside">AVPSLNNPQTFSEQKLDEALYHGAVLRVRPK</span><span class="topo-membrane">AMTVAVIIAGLLPILWG</span><span class="topo-outside">TGAGSEVM</span><span class="topo-membrane">SRIAAPMIGGMITAPLLSL</span><span class="topo-inside">FIIPAAYKLMWLHRH</span><span class="topo-unknown">RVRK</span></span>
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
      <td>-6</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>11</td>
      <td>4</td>
      <td>4</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>18</td>
      <td>5</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>22</td>
      <td>12</td>
      <td>15</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>39</td>
      <td>16</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>345</td>
      <td>33</td>
      <td>338</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>346</td>
      <td>363</td>
      <td>339</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>370</td>
      <td>357</td>
      <td>363</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>371</td>
      <td>391</td>
      <td>364</td>
      <td>384</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>392</td>
      <td>399</td>
      <td>385</td>
      <td>392</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>416</td>
      <td>393</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>417</td>
      <td>456</td>
      <td>410</td>
      <td>449</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>457</td>
      <td>473</td>
      <td>450</td>
      <td>466</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>474</td>
      <td>484</td>
      <td>467</td>
      <td>477</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>485</td>
      <td>504</td>
      <td>478</td>
      <td>497</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>505</td>
      <td>511</td>
      <td>498</td>
      <td>504</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>523</td>
      <td>505</td>
      <td>516</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>524</td>
      <td>524</td>
      <td>517</td>
      <td>517</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>539</td>
      <td>518</td>
      <td>532</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>540</td>
      <td>546</td>
      <td>533</td>
      <td>539</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>547</td>
      <td>562</td>
      <td>540</td>
      <td>555</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>563</td>
      <td>879</td>
      <td>556</td>
      <td>872</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>880</td>
      <td>897</td>
      <td>873</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>898</td>
      <td>904</td>
      <td>891</td>
      <td>897</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>905</td>
      <td>925</td>
      <td>898</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>926</td>
      <td>933</td>
      <td>919</td>
      <td>926</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>934</td>
      <td>950</td>
      <td>927</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>951</td>
      <td>991</td>
      <td>944</td>
      <td>984</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1008</td>
      <td>985</td>
      <td>1001</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1009</td>
      <td>1016</td>
      <td>1002</td>
      <td>1009</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1017</td>
      <td>1035</td>
      <td>1010</td>
      <td>1028</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1036</td>
      <td>1050</td>
      <td>1029</td>
      <td>1043</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1051</td>
      <td>1054</td>
      <td>1044</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ne5">3NE5</a> — Chain I (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">HHHHHHMGIE</span><span class="topo-inside">W</span><span class="topo-unknown">IIRRSVA</span><span class="topo-inside">NRFL</span><span class="topo-membrane">VLMGALFLSIWGTWTII</span><span class="topo-outside">NTPVDALPDLSDVQVIIKTSYPGQAPQIVENQVTYPLTTTMLSVPGAKTVRGFSQFGDSYVYVIFEDGTDPYWARSRVLEY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LNQVQGKLPAGVSAELGPDATGVGWIYEYALVDRSGKHDLADLRSLQDWFLKYELKTIPDVAEVASVGGVVKEYQVVIDPQRLAQYGISLAEVKSALDASNQEAGGSSIELAEAEYMVRA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">SGYLQTLDDFNHIVLKASENGVPVYLRDVAKVQIGPEMRRGIAELNGEGEVAGGVVILRSGKNAREVIAAVKDKLETLKSSLPEGVEIVTTYDRSQLIDRAIDNL</span><span class="topo-membrane">SGKLLEEFIVVAVVC</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">ALF</span><span class="topo-inside">LWHVRSA</span><span class="topo-membrane">LVAIISLPLGLCIAFIVMHFQ</span><span class="topo-outside">GLNANIMS</span><span class="topo-membrane">LGGIAIAVGAMVDAAIV</span><span class="topo-inside">MIENAHKRLEEWQHQHPDATLDNKTRWQVITDASVEVGPA</span><span class="topo-membrane">LFISLLIITLSFIPIFT</span><span class="topo-outside">LEGQEGR</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">LFGP</span><span class="topo-membrane">LAFTKTYAMAGAALLAIVVI</span><span class="topo-inside">PILMGYW</span><span class="topo-unknown">IRGKIPPESSNP</span><span class="topo-inside">L</span><span class="topo-unknown">NRFLIRVYHPLLLKV</span><span class="topo-inside">LHWPKTT</span><span class="topo-membrane">LLVAALSVLTVLWPLN</span><span class="topo-outside">KVGGEFLPQINEGDLLYMPSTLPGISAAEAASMLQKTD</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">KLIMSVPEVARVFGKTGKAETATDSAPLEMVETTIQLKPQEQWRPGMTMDKIIEELDNTVRLPGLANLWVPPIRNRIDMLSTGIKSPIGIKVSGTVLADIDAMAEQIEEVARTVPGVASA</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">LAERLEGGRYINVEINREKAARYGMTVADVQLFVTSAVGGAMVGETVEGIARYPINLRYPQSWRDSPQALRQLPILTPMKQQITLADVADIKVSTGPSMLKTENARPTSWIYIDARDRDM</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">VSVVHDLQKAIAEKVQLKPGTSVAFSGQFELLERANHKL</span><span class="topo-membrane">KLMVPMTLMIIFVLLYLA</span><span class="topo-inside">FRRVGEA</span><span class="topo-membrane">LLIISSVPFALVGGIWLLWWM</span><span class="topo-outside">GFHLSVAT</span><span class="topo-membrane">GTGFIALAGVAAEFGVV</span><span class="topo-inside">MLMYLRHAIE</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050    </span>
<span class="topo-line"><span class="topo-inside">AVPSLNNPQTFSEQKLDEALYHGAVLRVRPK</span><span class="topo-membrane">AMTVAVIIAGLLPILWG</span><span class="topo-outside">TGAGSEVM</span><span class="topo-membrane">SRIAAPMIGGMITAPLLSL</span><span class="topo-inside">FIIPAAYKLMWLHRH</span><span class="topo-unknown">RVRK</span></span>
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
      <td>-6</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>11</td>
      <td>4</td>
      <td>4</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>18</td>
      <td>5</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>22</td>
      <td>12</td>
      <td>15</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>39</td>
      <td>16</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>345</td>
      <td>33</td>
      <td>338</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>346</td>
      <td>363</td>
      <td>339</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>370</td>
      <td>357</td>
      <td>363</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>371</td>
      <td>391</td>
      <td>364</td>
      <td>384</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>392</td>
      <td>399</td>
      <td>385</td>
      <td>392</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>416</td>
      <td>393</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>417</td>
      <td>456</td>
      <td>410</td>
      <td>449</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>457</td>
      <td>473</td>
      <td>450</td>
      <td>466</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>474</td>
      <td>484</td>
      <td>467</td>
      <td>477</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>485</td>
      <td>504</td>
      <td>478</td>
      <td>497</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>505</td>
      <td>511</td>
      <td>498</td>
      <td>504</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>523</td>
      <td>505</td>
      <td>516</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>524</td>
      <td>524</td>
      <td>517</td>
      <td>517</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>539</td>
      <td>518</td>
      <td>532</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>540</td>
      <td>546</td>
      <td>533</td>
      <td>539</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>547</td>
      <td>562</td>
      <td>540</td>
      <td>555</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>563</td>
      <td>879</td>
      <td>556</td>
      <td>872</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>880</td>
      <td>897</td>
      <td>873</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>898</td>
      <td>904</td>
      <td>891</td>
      <td>897</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>905</td>
      <td>925</td>
      <td>898</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>926</td>
      <td>933</td>
      <td>919</td>
      <td>926</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>934</td>
      <td>950</td>
      <td>927</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>951</td>
      <td>991</td>
      <td>944</td>
      <td>984</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1008</td>
      <td>985</td>
      <td>1001</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1009</td>
      <td>1016</td>
      <td>1002</td>
      <td>1009</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1017</td>
      <td>1035</td>
      <td>1010</td>
      <td>1028</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1036</td>
      <td>1050</td>
      <td>1029</td>
      <td>1043</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1051</td>
      <td>1054</td>
      <td>1044</td>
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

### Heavy-metal specificity of CusA

CusA is the only heavy-metal efflux RND (HME-RND) transporter in E. coli, distinguishing it from the six multidrug efflux RND (HAE-RND) pumps (AcrB, AcrD, AcrF, MdtB, MdtC, and YhiV) also present in E. coli. CusA specifically recognizes and confers resistance to [Ag(i)](/xray-mp-wiki/reagents/ligands/ag(i)) and Cu(I) ions, which are highly toxic even at low concentrations. The protein works in conjunction with the periplasmic MFP CusB and the outer-membrane channel CusC to form the CusABC tripartite efflux complex.

### Structural model based on AcrB homology

Although the CusA crystal structure was not determined, a structural model was generated based on the AcrB crystal structure and sequence alignment. CusA and AcrB share only 19% protein sequence identity. The model indicates that the periplasmic domain of CusA (residues 148-157) is located directly above the vestibule region, facing the periplasm. This location corresponds to the PN2 region of AcrB. The C-terminus of CusB interacts with CusA at a position corresponding to the PC1 region of AcrB, analogous to the interaction between [ACRA](/xray-mp-wiki/proteins/acra) and AcrB.

### CusA-CusB cross-linking interaction

Chemical cross-linking with disuccinimidyl suberate (DSS) followed by LC-MS/MS analysis revealed that the N-terminal polypeptide of CusB (residues 84-101: IDPTQTQNLGVKTATVTR) directly interacts with the periplasmic domain of CusA (residues 148-157: SGKHDLADLR). This interaction was confirmed by identifying cross-linked lysine residues between the two proteins. The interaction site is consistent with the PC1 region of AcrB, where the C-terminus of AcrA binds.

### CusBA co-crystal structure and interaction interface

The co-crystal structure of the CusBA complex (2.90 A resolution) revealed that CusA exists as a trimer, with each protomer binding two CusB molecules, for a total of six CusB protomers per CusA trimer. Key interactions between CusA and CusB include: (1) four salt bridges formed by CusB residues K95, D386, E388 and R397 with CusA residues D155, R771, R777 and E584; (2) hydrogen bonds between CusB T89, the backbone oxygen of N91, and R292 with CusA K594, R147, and the backbone oxygen of Q198; (3) additional hydrogen bonds in molecule 2 of CusB where Q108, S109, S253 and N312 form hydrogen bonds with CusA Q785, Q194, D800 and Q198. The equilibrium dissociation constant (Kd) for CusA-CusB interaction was measured by isothermal titration calorimetry as 5.1 +/- 0.3 uM.

### Metal ion transport pathway through CusA

CusA is proposed to take up metal ions from both the periplasm and cytoplasm using a methionine-residue ion relay network. Metal ions enter the three-methionine binding site of CusA, formed by M573, M623 and M672, located inside the cleft between subdomains PN2 and PC1 on the periplasmic portion of CusA. Ions may also enter through methionine pairs within the transmembrane domain. The proposed pathway involves: (1) direct transfer from CusF chaperone to the three-methionine binding site (M49, M64, M66) at the N-terminal tail of CusB; (2) delivery from CusB to the three-methionine cluster (M573, M623, M672) inside the periplasmic cleft of CusA; (3) release to the nearest methionine pair (M271-M755) located above the three-methionine binding site; (4) extrusion through the [Cusc](/xray-mp-wiki/proteins/cusC) outer membrane channel.


## Cross-References

- <a href="/xray-mp-wiki/proteins/abc-transporters/acrb/">AcrB Multidrug Efflux Pump</a> — AcrB crystal structure used as template for CusA structural model; 19% sequence identity
- <a href="/xray-mp-wiki/proteins/abc-transporters/cusB/">CusB Membrane Fusion Protein</a> — CusB is the periplasmic MFP partner; cross-linking MS confirmed CusA-CusB interaction
- <a href="/xray-mp-wiki/proteins/abc-transporters/mexB/">MexB Efflux Pump</a> — MexB is a P. aeruginosa RND efflux pump homologous to CusA
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — DDM (1% solubilization, 0.05% crystallization buffer) used for CusA purification
- <a href="/xray-mp-wiki/reagents/additives/pmsf/">PMSF (Phenylmethylsulfonyl Fluoride)</a> — PMSF (1 mM) included in lysis and wash buffers as protease inhibitor
- <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">Sodium Phosphate Buffer</a> — Sodium phosphate buffer (100 mM pH 7.2) used in lysis buffer; 20 mM in high-salt wash
- <a href="/xray-mp-wiki/reagents/buffers/acetate">Acetate Buffer (Sodium Acetate)</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/ligands/cu(i)">CU(I)</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/proteins/cusC">CUSC</a> — Entity mentioned in text
