---
title: "CusB Membrane Fusion Protein"
created: 2026-05-27
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2009.08.029, doi/10.1038##nature09743]
verified: false
---

# CusB Membrane Fusion Protein

## Overview

CusB is a periplasmic membrane fusion protein (MFP) from Escherichia coli, functioning as a critical adaptor in the CusABC tripartite copper/silver efflux system. It bridges the inner-membrane efflux pump CusA and the outer-membrane channel CusC, mediating resistance to Cu+ and Ag+ ions. CusB is the first MFP structure solved from a heavy-metal efflux RND transporter. The protein adopts an elongated conformation with four distinct domains: three beta-strand domains and a unique three-helix bundle alpha-helical domain (Domain 4), contrasting with the two-helical hairpin motif found in other MFPs. Two distinct conformations (open and compact) were captured in a single crystal, demonstrating remarkable conformational flexibility. CusB contains multiple metal-binding sites for [Cu(i)](/xray-mp-wiki/reagents/ligands/cu(i)) and Ag(I), each coordinated by methionine residues, representing the first MFP-ligand complex structures.

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2l9p">2L9P</a></td>
      <td>3.40 A</td>
      <td>I222</td>
      <td>Full-length CusB with C-terminal 6xHis tag (residues 1-369)</td>
      <td>Apo</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2l9q">2L9Q</a></td>
      <td>3.78 A</td>
      <td>I222</td>
      <td>Full-length CusB with C-terminal 6xHis tag</td>
      <td>Copper(I) (Cu+)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2l9r">2L9R</a></td>
      <td>3.84 A</td>
      <td>I222</td>
      <td>Full-length CusB with C-terminal 6xHis tag</td>
      <td>Silver(I) (Ag+)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3)
- **Construct**: Full-length CusB with C-terminal 6xHis tag, overproduced from pET15b cusB expression vector

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
      <td>Cells grown in 12 L LB medium with 100 ug/ml <a href="/xray-mp-wiki/reagents/antibiotics/ampicillin">Ampicillin</a> at 37 C, induced with 1 mM IPTG at OD600 ~0.5</td>
      <td>--</td>
      <td>LB medium with 100 ug/ml ampicillin + --</td>
      <td>Cells harvested within 4 h of induction</td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>Cells resuspended in 20 mM Na-<a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> (pH 7.2), 100 mM NaCl and disrupted with French pressure cell; debris removed by centrifugation at 20,000 rpm for 45 min at 4 C</td>
      <td>--</td>
      <td>20 mM Na-Hepes (pH 7.2), 100 mM NaCl + --</td>
      <td>Crude lysate collected</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Crude lysate supplemented with 0.5% n-dodecyl-beta-D-maltoside (<a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>)</td>
      <td>--</td>
      <td>20 mM Na-Hepes (pH 7.2), 100 mM NaCl + 0.5% DDM</td>
      <td>Membrane fraction solubilized</td>
    </tr>
    <tr>
      <td>Ni2+ affinity chromatography</td>
      <td>Ni2+-affinity column chromatography</td>
      <td>Ni2+-affinity resin</td>
      <td>20 mM Na-Hepes (pH 7.2), 100 mM NaCl + 0.5% DDM</td>
      <td>His-tagged CusB captured on Ni2+ column</td>
    </tr>
    <tr>
      <td>Size exclusion chromatography</td>
      <td>G-200 sizing column chromatography</td>
      <td>Superdex 200</td>
      <td>20 mM Na-Hepes (pH 7.2), 100 mM NaCl + 0.5% DDM</td>
      <td>Monodisperse fraction collected</td>
    </tr>
    <tr>
      <td>Concentration and storage</td>
      <td>Protein concentrated to 20 mg/ml</td>
      <td>--</td>
      <td>20 mM Na-Hepes (pH 7.5), 0.04% DDM + 0.04% DDM</td>
      <td>Purity >95% by 10% SDS-PAGE stained with Coomassie Brilliant Blue</td>
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
      <td>20 mg/ml CusB in 20 mM Na-Hepes (pH 7.5), 0.04% DDM</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>not specified in methods section</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Apo-CusB crystals grown at room temperature; Cu(I) and <a href="/xray-mp-wiki/reagents/ligands/ag(i">Ag(i)</a>) complexes obtained by soaking metal ions into apo-crystals. Space group I222 for all forms. Two distinct conformations (molecules A and B) found in asymmetric unit.</td>
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
      <td>CusB residues 79-400 (molecule 1) and 79-402 (molecule 2) in CusBA co-crystal; CusB forms hexameric channel with six protomers per <a href="/xray-mp-wiki/proteins/cusA">Cusa</a> trimer</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/cymal-6">Cymal 6</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3)
- **Construct**: Full-length CusB with C-terminal 6xHis tag, overproduced from pET15b cusB expression vector

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>0.1 mM CusA (native) and 0.1 mM CusB (SeMet-substituted) in 20 mM Na-HEPES pH 7.5, 0.05% CYMAL-6</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>10% PEG 6000, 0.1 M Na-HEPES pH 7.5, 0.1 M ammonium acetate, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a></td>
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
      <td>CusA-CusB co-crystal. SAD phasing used with six selenium sites per CusB molecule. Model consists of 1,686 amino acid residues (CusA residues 4-1043, CusB mol 1 residues 79-400, CusB mol 2 residues 79-402).</td>
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
<span class="topo-line"><span class="topo-unknown">MKKIALIIGSMIAGGIISAAGFTWVAKAEPPAEKTSTAERKILFWYDPMYPNTRFDKPGK</span></span>
<span class="topo-line"><span class="topo-unknown">SPFMDMDLVPKYADEESS</span><span class="topo-outside">ASGVRIDPTQTQNLGVKTATVTRGPLTFAQSFPANVSYNEYQ</span></span>
<span class="topo-line"><span class="topo-outside">YAIVQARAAGFIDKVYPLTVGDKVQKGTPLLDLTIPDWVEAQSEYLLLRETGGTATQTEG</span></span>
<span class="topo-line"><span class="topo-outside">ILERLRLAGMPEADIRRLIATQKIQTRFTLKAPIDGVITAFDLRAGMNIAKDNVVAKIQG</span></span>
<span class="topo-line"><span class="topo-outside">MDPVWVTAAIPESIAWLVKDASQFTLTVPARPDKTLTIRKWTLLPGVDAATRTLQLRLEV</span></span>
<span class="topo-line"><span class="topo-outside">DNADEALKPGMNAWLQLNTASEPMLLIPSQALIDTGSEQRVITVDADGRFVPKRVAVFQA</span></span>
<span class="topo-line"><span class="topo-outside">SQGVTALRSGLAEGEKVVSSGLFLIDSEANISGALERMRS</span><span class="topo-unknown">ESATHAHHHHHHH</span></span>
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
<span class="topo-line"><span class="topo-unknown">HHHHHHMGIE</span><span class="topo-inside">W</span><span class="topo-unknown">IIRRSVA</span><span class="topo-inside">NRFL</span><span class="topo-membrane">VLMGALFLSIWGTWTII</span><span class="topo-outside">NTPVDALPDLSDVQVIIKTSY</span></span>
<span class="topo-line"><span class="topo-outside">PGQAPQIVENQVTYPLTTTMLSVPGAKTVRGFSQFGDSYVYVIFEDGTDPYWARSRVLEY</span></span>
<span class="topo-line"><span class="topo-outside">LNQVQGKLPAGVSAELGPDATGVGWIYEYALVDRSGKHDLADLRSLQDWFLKYELKTIPD</span></span>
<span class="topo-line"><span class="topo-outside">VAEVASVGGVVKEYQVVIDPQRLAQYGISLAEVKSALDASNQEAGGSSIELAEAEYMVRA</span></span>
<span class="topo-line"><span class="topo-outside">SGYLQTLDDFNHIVLKASENGVPVYLRDVAKVQIGPEMRRGIAELNGEGEVAGGVVILRS</span></span>
<span class="topo-line"><span class="topo-outside">GKNAREVIAAVKDKLETLKSSLPEGVEIVTTYDRSQLIDRAIDNL</span><span class="topo-membrane">SGKLLEEFIVVAVVC</span></span>
<span class="topo-line"><span class="topo-membrane">ALF</span><span class="topo-inside">LWHVRSA</span><span class="topo-membrane">LVAIISLPLGLCIAFIVMHFQ</span><span class="topo-outside">GLNANIMS</span><span class="topo-membrane">LGGIAIAVGAMVDAAIV</span><span class="topo-inside">MIEN</span></span>
<span class="topo-line"><span class="topo-inside">AHKRLEEWQHQHPDATLDNKTRWQVITDASVEVGPA</span><span class="topo-membrane">LFISLLIITLSFIPIFT</span><span class="topo-outside">LEGQEGR</span></span>
<span class="topo-line"><span class="topo-outside">LFGP</span><span class="topo-membrane">LAFTKTYAMAGAALLAIVVI</span><span class="topo-inside">PILMGYW</span><span class="topo-unknown">IRGKIPPESSNP</span><span class="topo-inside">L</span><span class="topo-unknown">NRFLIRVYHPLLLKV</span><span class="topo-inside">L</span></span>
<span class="topo-line"><span class="topo-inside">HWPKTT</span><span class="topo-membrane">LLVAALSVLTVLWPLN</span><span class="topo-outside">KVGGEFLPQINEGDLLYMPSTLPGISAAEAASMLQKTD</span></span>
<span class="topo-line"><span class="topo-outside">KLIMSVPEVARVFGKTGKAETATDSAPLEMVETTIQLKPQEQWRPGMTMDKIIEELDNTV</span></span>
<span class="topo-line"><span class="topo-outside">RLPGLANLWVPPIRNRIDMLSTGIKSPIGIKVSGTVLADIDAMAEQIEEVARTVPGVASA</span></span>
<span class="topo-line"><span class="topo-outside">LAERLEGGRYINVEINREKAARYGMTVADVQLFVTSAVGGAMVGETVEGIARYPINLRYP</span></span>
<span class="topo-line"><span class="topo-outside">QSWRDSPQALRQLPILTPMKQQITLADVADIKVSTGPSMLKTENARPTSWIYIDARDRDM</span></span>
<span class="topo-line"><span class="topo-outside">VSVVHDLQKAIAEKVQLKPGTSVAFSGQFELLERANHKL</span><span class="topo-membrane">KLMVPMTLMIIFVLLYLA</span><span class="topo-inside">FRR</span></span>
<span class="topo-line"><span class="topo-inside">VGEA</span><span class="topo-membrane">LLIISSVPFALVGGIWLLWWM</span><span class="topo-outside">GFHLSVAT</span><span class="topo-membrane">GTGFIALAGVAAEFGVV</span><span class="topo-inside">MLMYLRHAIE</span></span>
<span class="topo-line"><span class="topo-inside">AVPSLNNPQTFSEQKLDEALYHGAVLRVRPK</span><span class="topo-membrane">AMTVAVIIAGLLPILWG</span><span class="topo-outside">TGAGSEVM</span><span class="topo-membrane">SRIA</span></span>
<span class="topo-line"><span class="topo-membrane">APMIGGMITAPLLSL</span><span class="topo-inside">FIIPAAYKLMWLHRH</span><span class="topo-unknown">RVRK</span></span>
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
<span class="topo-line"><span class="topo-unknown">MKKIALIIGSMIAGGIISAAGFTWVAKAEPPAEKTSTAERKILFWYDPMYPNTRFDKPGK</span></span>
<span class="topo-line"><span class="topo-unknown">SPFMDMDLVPKYADEESS</span><span class="topo-outside">ASGVRIDPTQTQNLGVKTATVTRGPLTFAQSFPANVSYNEYQ</span></span>
<span class="topo-line"><span class="topo-outside">YAIVQARAAGFIDKVYPLTVGDKVQKGTPLLDLTIPDWVEAQSEYLLLRETGGTATQTEG</span></span>
<span class="topo-line"><span class="topo-outside">ILERLRLAGMPEADIRRLIATQKIQTRFTLKAPIDGVITAFDLRAGMNIAKDNVVAKIQG</span></span>
<span class="topo-line"><span class="topo-outside">MDPVWVTAAIPESIAWLVKDASQFTLTVPARPDKTLTIRKWTLLPGVDAATRTLQLRLEV</span></span>
<span class="topo-line"><span class="topo-outside">DNADEALKPGMNAWLQLNTASEPMLLIPSQALIDTGSEQRVITVDADGRFVPKRVAVFQA</span></span>
<span class="topo-line"><span class="topo-outside">SQGVTALRSGLAEGEKVVSSGLFLIDSEANISGALERMRS</span><span class="topo-unknown">ESATHAHHHHHHH</span></span>
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
<span class="topo-line"><span class="topo-unknown">MKKIALIIGSMIAGGIISAAGFTWVAKAEPPAEKTSTAERKILFWYDPMYPNTRFDKPGK</span></span>
<span class="topo-line"><span class="topo-unknown">SPFMDMDLVPKYADEESS</span><span class="topo-outside">ASGVRIDPTQTQNLGVKTATVTRGPLTFAQSFPANVSYNEYQ</span></span>
<span class="topo-line"><span class="topo-outside">YAIVQARAAGFIDKVYPLTVGDKVQKGTPLLDLTIPDWVEAQSEYLLLRETGGTATQTEG</span></span>
<span class="topo-line"><span class="topo-outside">ILERLRLAGMPEADIRRLIATQKIQTRFTLKAPIDGVITAFDLRAGMNIAKDNVVAKIQG</span></span>
<span class="topo-line"><span class="topo-outside">MDPVWVTAAIPESIAWLVKDASQFTLTVPARPDKTLTIRKWTLLPGVDAATRTLQLRLEV</span></span>
<span class="topo-line"><span class="topo-outside">DNADEALKPGMNAWLQLNTASEPMLLIPSQALIDTGSEQRVITVDADGRFVPKRVAVFQA</span></span>
<span class="topo-line"><span class="topo-outside">SQGVTALRSGLAEGEKVVSSGLFLIDSEANISGALERMRS</span><span class="topo-unknown">ESATHAHHHHHHH</span></span>
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
<span class="topo-line"><span class="topo-unknown">HHHHHHMGIE</span><span class="topo-inside">W</span><span class="topo-unknown">IIRRSVA</span><span class="topo-inside">NRFL</span><span class="topo-membrane">VLMGALFLSIWGTWTII</span><span class="topo-outside">NTPVDALPDLSDVQVIIKTSY</span></span>
<span class="topo-line"><span class="topo-outside">PGQAPQIVENQVTYPLTTTMLSVPGAKTVRGFSQFGDSYVYVIFEDGTDPYWARSRVLEY</span></span>
<span class="topo-line"><span class="topo-outside">LNQVQGKLPAGVSAELGPDATGVGWIYEYALVDRSGKHDLADLRSLQDWFLKYELKTIPD</span></span>
<span class="topo-line"><span class="topo-outside">VAEVASVGGVVKEYQVVIDPQRLAQYGISLAEVKSALDASNQEAGGSSIELAEAEYMVRA</span></span>
<span class="topo-line"><span class="topo-outside">SGYLQTLDDFNHIVLKASENGVPVYLRDVAKVQIGPEMRRGIAELNGEGEVAGGVVILRS</span></span>
<span class="topo-line"><span class="topo-outside">GKNAREVIAAVKDKLETLKSSLPEGVEIVTTYDRSQLIDRAIDNL</span><span class="topo-membrane">SGKLLEEFIVVAVVC</span></span>
<span class="topo-line"><span class="topo-membrane">ALF</span><span class="topo-inside">LWHVRSA</span><span class="topo-membrane">LVAIISLPLGLCIAFIVMHFQ</span><span class="topo-outside">GLNANIMS</span><span class="topo-membrane">LGGIAIAVGAMVDAAIV</span><span class="topo-inside">MIEN</span></span>
<span class="topo-line"><span class="topo-inside">AHKRLEEWQHQHPDATLDNKTRWQVITDASVEVGPA</span><span class="topo-membrane">LFISLLIITLSFIPIFT</span><span class="topo-outside">LEGQEGR</span></span>
<span class="topo-line"><span class="topo-outside">LFGP</span><span class="topo-membrane">LAFTKTYAMAGAALLAIVVI</span><span class="topo-inside">PILMGYW</span><span class="topo-unknown">IRGKIPPESSNP</span><span class="topo-inside">L</span><span class="topo-unknown">NRFLIRVYHPLLLKV</span><span class="topo-inside">L</span></span>
<span class="topo-line"><span class="topo-inside">HWPKTT</span><span class="topo-membrane">LLVAALSVLTVLWPLN</span><span class="topo-outside">KVGGEFLPQINEGDLLYMPSTLPGISAAEAASMLQKTD</span></span>
<span class="topo-line"><span class="topo-outside">KLIMSVPEVARVFGKTGKAETATDSAPLEMVETTIQLKPQEQWRPGMTMDKIIEELDNTV</span></span>
<span class="topo-line"><span class="topo-outside">RLPGLANLWVPPIRNRIDMLSTGIKSPIGIKVSGTVLADIDAMAEQIEEVARTVPGVASA</span></span>
<span class="topo-line"><span class="topo-outside">LAERLEGGRYINVEINREKAARYGMTVADVQLFVTSAVGGAMVGETVEGIARYPINLRYP</span></span>
<span class="topo-line"><span class="topo-outside">QSWRDSPQALRQLPILTPMKQQITLADVADIKVSTGPSMLKTENARPTSWIYIDARDRDM</span></span>
<span class="topo-line"><span class="topo-outside">VSVVHDLQKAIAEKVQLKPGTSVAFSGQFELLERANHKL</span><span class="topo-membrane">KLMVPMTLMIIFVLLYLA</span><span class="topo-inside">FRR</span></span>
<span class="topo-line"><span class="topo-inside">VGEA</span><span class="topo-membrane">LLIISSVPFALVGGIWLLWWM</span><span class="topo-outside">GFHLSVAT</span><span class="topo-membrane">GTGFIALAGVAAEFGVV</span><span class="topo-inside">MLMYLRHAIE</span></span>
<span class="topo-line"><span class="topo-inside">AVPSLNNPQTFSEQKLDEALYHGAVLRVRPK</span><span class="topo-membrane">AMTVAVIIAGLLPILWG</span><span class="topo-outside">TGAGSEVM</span><span class="topo-membrane">SRIA</span></span>
<span class="topo-line"><span class="topo-membrane">APMIGGMITAPLLSL</span><span class="topo-inside">FIIPAAYKLMWLHRH</span><span class="topo-unknown">RVRK</span></span>
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
<span class="topo-line"><span class="topo-unknown">HHHHHHMGIE</span><span class="topo-inside">W</span><span class="topo-unknown">IIRRSVA</span><span class="topo-inside">NRFL</span><span class="topo-membrane">VLMGALFLSIWGTWTII</span><span class="topo-outside">NTPVDALPDLSDVQVIIKTSY</span></span>
<span class="topo-line"><span class="topo-outside">PGQAPQIVENQVTYPLTTTMLSVPGAKTVRGFSQFGDSYVYVIFEDGTDPYWARSRVLEY</span></span>
<span class="topo-line"><span class="topo-outside">LNQVQGKLPAGVSAELGPDATGVGWIYEYALVDRSGKHDLADLRSLQDWFLKYELKTIPD</span></span>
<span class="topo-line"><span class="topo-outside">VAEVASVGGVVKEYQVVIDPQRLAQYGISLAEVKSALDASNQEAGGSSIELAEAEYMVRA</span></span>
<span class="topo-line"><span class="topo-outside">SGYLQTLDDFNHIVLKASENGVPVYLRDVAKVQIGPEMRRGIAELNGEGEVAGGVVILRS</span></span>
<span class="topo-line"><span class="topo-outside">GKNAREVIAAVKDKLETLKSSLPEGVEIVTTYDRSQLIDRAIDNL</span><span class="topo-membrane">SGKLLEEFIVVAVVC</span></span>
<span class="topo-line"><span class="topo-membrane">ALF</span><span class="topo-inside">LWHVRSA</span><span class="topo-membrane">LVAIISLPLGLCIAFIVMHFQ</span><span class="topo-outside">GLNANIMS</span><span class="topo-membrane">LGGIAIAVGAMVDAAIV</span><span class="topo-inside">MIEN</span></span>
<span class="topo-line"><span class="topo-inside">AHKRLEEWQHQHPDATLDNKTRWQVITDASVEVGPA</span><span class="topo-membrane">LFISLLIITLSFIPIFT</span><span class="topo-outside">LEGQEGR</span></span>
<span class="topo-line"><span class="topo-outside">LFGP</span><span class="topo-membrane">LAFTKTYAMAGAALLAIVVI</span><span class="topo-inside">PILMGYW</span><span class="topo-unknown">IRGKIPPESSNP</span><span class="topo-inside">L</span><span class="topo-unknown">NRFLIRVYHPLLLKV</span><span class="topo-inside">L</span></span>
<span class="topo-line"><span class="topo-inside">HWPKTT</span><span class="topo-membrane">LLVAALSVLTVLWPLN</span><span class="topo-outside">KVGGEFLPQINEGDLLYMPSTLPGISAAEAASMLQKTD</span></span>
<span class="topo-line"><span class="topo-outside">KLIMSVPEVARVFGKTGKAETATDSAPLEMVETTIQLKPQEQWRPGMTMDKIIEELDNTV</span></span>
<span class="topo-line"><span class="topo-outside">RLPGLANLWVPPIRNRIDMLSTGIKSPIGIKVSGTVLADIDAMAEQIEEVARTVPGVASA</span></span>
<span class="topo-line"><span class="topo-outside">LAERLEGGRYINVEINREKAARYGMTVADVQLFVTSAVGGAMVGETVEGIARYPINLRYP</span></span>
<span class="topo-line"><span class="topo-outside">QSWRDSPQALRQLPILTPMKQQITLADVADIKVSTGPSMLKTENARPTSWIYIDARDRDM</span></span>
<span class="topo-line"><span class="topo-outside">VSVVHDLQKAIAEKVQLKPGTSVAFSGQFELLERANHKL</span><span class="topo-membrane">KLMVPMTLMIIFVLLYLA</span><span class="topo-inside">FRR</span></span>
<span class="topo-line"><span class="topo-inside">VGEA</span><span class="topo-membrane">LLIISSVPFALVGGIWLLWWM</span><span class="topo-outside">GFHLSVAT</span><span class="topo-membrane">GTGFIALAGVAAEFGVV</span><span class="topo-inside">MLMYLRHAIE</span></span>
<span class="topo-line"><span class="topo-inside">AVPSLNNPQTFSEQKLDEALYHGAVLRVRPK</span><span class="topo-membrane">AMTVAVIIAGLLPILWG</span><span class="topo-outside">TGAGSEVM</span><span class="topo-membrane">SRIA</span></span>
<span class="topo-line"><span class="topo-membrane">APMIGGMITAPLLSL</span><span class="topo-inside">FIIPAAYKLMWLHRH</span><span class="topo-unknown">RVRK</span></span>
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
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Unique three-helix bundle Domain 4

Unlike other known MFP structures (AcrA, MexA, MacA) which possess a two-helical hairpin motif, CusB Domain 4 folds into a three-helix bundle. This helix-turn-helix-turn-helix secondary structure creates an approximately 27-A-long structure, making it at least 20 A shorter than the two-helical hairpin domains of MexA and AcrA. CusB is the only periplasmic MFP protein known to possess this three-helical domain instead of a two-helical hairpin motif. The three-helix bundle is presumably located near the outer membrane and may interact with the periplasmic domain of [Cusc](/xray-mp-wiki/proteins/cusC).

### Conformational flexibility and hinge motion

Two distinct conformations of CusB were captured in a single crystal, suggesting the MFP is highly flexible. Molecule A adopts a more open conformation while molecule B exhibits a compact form. Superimposition gives an overall RMSD of 2.6 A over C-alpha atoms. The hinge region, composed of two loops (residues 116-120 and 240-242) between Domains 2 and 3, permits rigid-body movement. When Domains 1+2 are superimposed, the alpha-helical domains differ by approximately 21 degrees. When Domains 3+4 are superimposed, the beta-barrels of Domain 1 shift by approximately 23 degrees. This flexibility may allow CusB to accommodate different states during the efflux cycle.

### Multiple metal-binding sites with methionine coordination

CusB contains multiple Cu(I) and Ag(I) binding sites, each coordinated by one methionine residue. In the CusB-Cu(I) complex, four Cu+ binding sites were identified in the asymmetric unit: sites C1 and C2 in molecule A, and C1' and C2' in molecule B. Site C1 is located in Domain 1 (N- and C-termini region) and is coordinated by M324, F358, and R368. Site C2 is in Domain 4 (three-helix bundle) and is coordinated by M190, W158, and Q162. For Ag(I), a single binding site A1 was identified next to M324 in molecule A, coordinated by the same residues M324, F358, and R368. This methionine-only coordination mode is distinct from other copper tolerance proteins (CusF, CucR, Atx1) which use two-methionine or two-cysteine binding pockets.

### CusA-CusB interaction interface

Cross-linking mass spectrometry revealed that the N-terminal region of CusB (residues 84-101, polypeptide beta: IDPTQTQNLGVKTATVTR) directly interacts with the periplasmic domain of CusA (residues 148-157, polypeptide alpha: SGKHDLADLR). Domain 1 of CusB, formed by the N- and C-terminal ends, interacts with the periplasmic domain of the CusA transporter. This interaction site corresponds to the PC1 region of [Acrb](/xray-mp-wiki/proteins/acrB), analogous to how AcrA interacts with AcrB. The structural model of CusA was generated based on the AcrB crystal structure and sequence alignment, indicating that the CusA periplasmic domain (residues 148-157) is located directly above the vestibule region, facing the periplasm.

### Hexameric CusB channel formation

The co-crystal structure revealed that six CusB protomers assemble into a continuous funnel-like channel with the central channel formed along the crystallographic three-fold symmetry axis. Domain 1 and the lower half of domain 2 create a cap-like structure, while the upper half of domain 2, together with domains 3 and 4, contribute to the central channel. The channel is approximately 62 A in length with an average internal diameter of approximately 37 A, giving a volume of approximately 65,000 A^3. The inner surface is predominantly negatively charged, suggesting capacity to bind positively charged metal ions. The narrowest section is at residue D232 of each CusB protomer, close to the hinge region between domains 3 and 4. The widest section forms at the top edge with an inner diameter of approximately 56 A. The alpha-helices of domain 4 create an inverted conical structure.

### CusA-CusB binding affinity by ITC

Isothermal titration calorimetry measurements determined the equilibrium dissociation constant for CusB binding to the CusA pump as 5.1 +/- 0.3 uM. This micromolar-range affinity is consistent with a functional adaptor interaction in the tripartite efflux complex.

### Metal ion relay via N-terminal methionine residues

The N-terminal residues M49, M64 and M66 of CusB are proposed to form a three-methionine metal-binding site. Although these residues are intrinsically disordered and not visible in electron density maps, the co-crystal structure shows that the N-terminal tails of CusB molecules are located outside the cleft between PC1 and PC2 subdomains of the CusA pump. This positioning suggests CusB may help transfer metal ions via the N-terminal three-methionine binding site into the periplasmic cleft of CusA. The proposed metal transport pathway is: (1) Cu(I)/Ag(I) ions delivered from CusF chaperone to the three-methionine binding site (M49, M64, M66) at the CusB N-terminal tail; (2) transfer from CusB to the three-methionine cluster (M573, M623, M672) inside the periplasmic cleft of CusA; (3) release to the nearest methionine pair (M271-M755) located above the three-methionine binding site of CusA; (4) extrusion through the CusC channel.

### CusC3-CusB6-CusA3 tripartite complex model

A structural model of the complete CusC3-CusB6-CusA3 tripartite efflux complex was constructed based on the CusBA crystal complex structure and the predicted CusC model. The final model represents a 750-kDa complex that spans both the inner and outer membranes of E. coli and extrudes Cu(I) and Ag(I) ions. This model integrates the trimeric CusA pump, hexameric CusB channel, and predicted trimeric CusC outer membrane channel into a functional efflux assemblage.


## Cross-References

- <a href="/xray-mp-wiki/proteins/abc-transporters/acrb/">AcrB Multidrug Efflux Pump</a> — AcrB is the prototypical RND efflux pump; CusA structural model based on AcrB structure
- <a href="/xray-mp-wiki/proteins/abc-transporters/mexB/">MexB Efflux Pump</a> — MexB is a P. aeruginosa RND efflux pump homologous to CusA
- <a href="/xray-mp-wiki/proteins/abc-transporters/acra/">AcrA Membrane Fusion Protein</a> — AcrA is the MFP partner of AcrB; CusB compared structurally to AcrA
- <a href="/xray-mp-wiki/proteins/mexA/">MexA Membrane Fusion Protein</a> — MexA is the P. aeruginosa MFP homolog; CusB superimposed with MexA showing domain similarities
- <a href="/xray-mp-wiki/proteins/abc-transporters/tolc/">TolC Outer Membrane Channel</a> — TolC is the outer-membrane channel of the AcrAB-TolC system; CusC is the functional homolog in CusABC
- <a href="/xray-mp-wiki/proteins/oprM/">OprM Outer Membrane Channel</a> — OprM is the P. aeruginosa outer-membrane channel; similar elongated alpha-helical tunnel structure
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — DDM (0.5% solubilization, 0.04% crystallization) used throughout purification and crystallization
- <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine (SeMet)</a> — SeMet-CusB used for MAD phasing in structure determination
- <a href="/xray-mp-wiki/proteins/cusC">CUSC</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> — Entity mentioned in text
