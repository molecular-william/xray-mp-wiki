---
title: "MtrE Outer Membrane Channel from Neisseria gonorrhoeae"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [porin, membrane-protein, xray-crystallography]
sources: [doi/10.1371##journal.pone.0097475]
verified: false
---

# MtrE Outer Membrane Channel from Neisseria gonorrhoeae

## Overview

MtrE is the outer membrane channel component of the [MtrCDE Tripartite Multidrug Efflux Pump](/xray-mp-wiki/concepts/transport-mechanisms/mtrcde-tripartite-efflux-pump/) from Neisseria gonorrhoeae. It belongs to the hydrophobic and amphiphilic efflux resistance-nodulation-cell division (HAE-RND) family of outer membrane channels. MtrE forms a homotrimeric channel that creates a vertical tunnel extending from the outer membrane surface down to the periplasmic end, representing an open conformational state. An aspartate ring (D402/D405 from each protomer) at the periplasmic entrance acts as a selectivity gate.


## Publications

### doi/10.1371##journal.pone.0097475

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4mt1">4MT1</a></td>
      <td>3.29</td>
      <td>P6_3_22</td>
      <td>Full-length MtrE (residues 1-445) with C-terminal 6xHis tag</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C43(DE3)
- **Construct**: Full-length MtrE with C-terminal 6xHis tag in pBAD22b vector
- **Notes**: Cells grown in LB medium with 100 ug/ml [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/) at 37 C to OD600=0.5, then cooled to 25 C for induction.
- **Induction**: 0.2% (w/v) arabinose at 25 C for 16 h

**Purification:**

- **Expression system**: E. coli C43(DE3)
- **Expression construct**: Full-length MtrE with C-terminal 6xHis tag
- **Tag info**: C-terminal 6xHis tag

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
      <td>Cell disruption</td>
      <td>French press</td>
      <td>—</td>
      <td>20 mM Na-HEPES pH 7.5, 300 mM NaCl, 1 mM PMSF</td>
      <td></td>
    </tr>
    <tr>
      <td>Membrane collection</td>
      <td>Ultracentrifugation</td>
      <td>—</td>
      <td></td>
      <td>Total membrane fraction collected</td>
    </tr>
    <tr>
      <td>Pre-extraction</td>
      <td>Detergent wash</td>
      <td>—</td>
      <td>0.5% (w/v) sodium lauroyl sarcosinate, 20 mM Na-HEPES pH 7.5, 50 mM NaCl</td>
      <td>30 min incubation at room temperature to pre-extract inner membrane proteins</td>
    </tr>
    <tr>
      <td>Outer membrane collection</td>
      <td>Ultracentrifugation and wash</td>
      <td>—</td>
      <td>20 mM Na-HEPES pH 7.5, 50 mM NaCl</td>
      <td>Washed twice</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>2% (w/v) n-dodecyl beta-D-maltoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Insoluble material removed by ultracentrifugation at 100,000xg</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni2+-affinity column</td>
      <td>—</td>
      <td></td>
      <td>Purified protein >95% pure by SDS-PAGE</td>
    </tr>
  </tbody>
</table>
**Final sample**: 15 mg/ml in 20 mM Na-HEPES pH 7.5, 200 mM NaCl, 0.05% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm/)
**Purity**: >95% by SDS-PAGE

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>15 mg/ml MtrE in 20 mM Na-HEPES pH 7.5, 200 mM NaCl, 0.05% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>20% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400, 0.2 M <a href="/xray-mp-wiki/reagents/buffers/sodium-acetate/">Sodium Acetate</a> pH 4.6, 0.25 M MgSO4, 2% (w/v) <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a> (OG)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>30% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400, 0.2 M <a href="/xray-mp-wiki/reagents/buffers/sodium-acetate/">Sodium Acetate</a> pH 4.6, 0.25 M MgSO4, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 2% OG</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>2 ul protein + 2 ul reservoir. Crystals grew within two weeks to 0.2 x 0.2 x 0.2 mm. Diffraction data to 3.29 A.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4mt1">4MT1</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">AKFFIDRPI</span><span class="topo-membrane">FAWVISIFIIAAGI</span><span class="topo-outside">FGIKSLPVSQYPSVAAPTITLHAIYPGASAQVMEGS</span></span>
<span class="topo-line"><span class="topo-outside">VLSVIERNMNGVEGLDYMSTSADSSGSGSVSLTFTPDTDENLAQVEVQNKLSEVLSTLPA</span></span>
<span class="topo-line"><span class="topo-outside">TVQQYGVTVSKARSNFLMIVMLSSDVQSTEEMNDYAQRNVVPELQRIEGVGQVRLFGAQR</span></span>
<span class="topo-line"><span class="topo-outside">AMRIWVDPKKLQNYNLSFADVGSALSAQNIQISAGSIGSLPAVRGQTVTATVTAQGQLGT</span></span>
<span class="topo-line"><span class="topo-outside">AEEFGNVILRANTDGSNIYLKDVAKVGLGMEDYSSSTRLNGVNTTGMAVMLSNSGNAMAT</span></span>
<span class="topo-line"><span class="topo-outside">AKAVKERLAVLEKYFPQGMSWKTPYDTSKFVEISIEKVI</span><span class="topo-membrane">HTLIEAMVLVFVVMYL</span><span class="topo-inside">FLQNI</span></span>
<span class="topo-line"><span class="topo-inside">RYT</span><span class="topo-membrane">LIPTIVVPISLLGGFAF</span><span class="topo-outside">ISYMGMSINVLTMF</span><span class="topo-membrane">AMILVIGIVVDDAI</span><span class="topo-inside">VVVENVERIMAG</span></span>
<span class="topo-line"><span class="topo-inside">EGLPPKEATKKAMGQISGAV</span><span class="topo-membrane">IGITAVLISVFVPL</span><span class="topo-outside">AMFSGAAGNIYKQFA</span><span class="topo-membrane">LTMASSIAFSA</span></span>
<span class="topo-line"><span class="topo-membrane">FLALTLT</span><span class="topo-inside">PALCAT</span><span class="topo-unknown">MLKTIPKGHHEEKK</span><span class="topo-inside">G</span><span class="topo-unknown">FFGWFNKKFDSWTHGYEGRVAKVLR</span><span class="topo-inside">KTFRM</span><span class="topo-membrane">MV</span></span>
<span class="topo-line"><span class="topo-membrane">VYIGLAVVGVFLF</span><span class="topo-outside">MRLPTSFLPTEDQGFVMVSVQLPAGATKERTDATLAQVTQLAKSIPE</span></span>
<span class="topo-line"><span class="topo-outside">IENIITVSGFSFSGSGQNMAMGFAIFKDWNERTASGSDAVAVAGKLTGMMMGTLKDGFGI</span></span>
<span class="topo-line"><span class="topo-outside">AVVPPPILEL</span><span class="topo-unknown">GN</span><span class="topo-outside">GSGLSINLQDRNNTGHTALLAKRNELIQKMRASGLFDPSTVRAGGLED</span></span>
<span class="topo-line"><span class="topo-outside">SPQLKIDINRAAAAAQGISFADIRTALASALSSSYVSDFPNQGRLQRVMVQADEDARMQP</span></span>
<span class="topo-line"><span class="topo-outside">ADILNLTVPNKSGVAVPLSTIATVSWENGTEQSVRFNGYPSMKLSASPATGVSTGQAMEA</span></span>
<span class="topo-line"><span class="topo-outside">VQKMVDELGGGYSFEWGGQSSEEAKGGSQTLIL</span><span class="topo-membrane">YGLAVAAVFLVLAAL</span><span class="topo-inside">YESWSI</span><span class="topo-membrane">PLAVIL</span></span>
<span class="topo-line"><span class="topo-membrane">VIPLGLIGAAAGV</span><span class="topo-outside">TGRNLFEGLLGSVPSFANDIYFQV</span><span class="topo-membrane">GFVTVMGLSAKNAI</span><span class="topo-inside">LIIEFAKDL</span></span>
<span class="topo-line"><span class="topo-inside">QAQGKSAVEAALEAARLRFRPI</span><span class="topo-membrane">IMTSFAFILGVVPLYI</span><span class="topo-outside">AAGASSASQRAIG</span><span class="topo-membrane">TTVFWGMLV</span></span>
<span class="topo-line"><span class="topo-membrane">GTLLSVFLV</span><span class="topo-unknown">PLFYVVVR</span><span class="topo-inside">KFF</span><span class="topo-unknown">KETAHEHEMAVRHASK</span></span>
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
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>10</td>
      <td>2</td>
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
      <td>339</td>
      <td>25</td>
      <td>339</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>355</td>
      <td>340</td>
      <td>355</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>356</td>
      <td>363</td>
      <td>356</td>
      <td>363</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>364</td>
      <td>380</td>
      <td>364</td>
      <td>380</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>381</td>
      <td>394</td>
      <td>381</td>
      <td>394</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>408</td>
      <td>395</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>440</td>
      <td>409</td>
      <td>440</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>441</td>
      <td>454</td>
      <td>441</td>
      <td>454</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>455</td>
      <td>469</td>
      <td>455</td>
      <td>469</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>470</td>
      <td>487</td>
      <td>470</td>
      <td>487</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>488</td>
      <td>493</td>
      <td>488</td>
      <td>493</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>494</td>
      <td>507</td>
      <td>494</td>
      <td>507</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>508</td>
      <td>508</td>
      <td>508</td>
      <td>508</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>509</td>
      <td>533</td>
      <td>509</td>
      <td>533</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>534</td>
      <td>538</td>
      <td>534</td>
      <td>538</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>539</td>
      <td>553</td>
      <td>539</td>
      <td>553</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>554</td>
      <td>670</td>
      <td>554</td>
      <td>670</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>671</td>
      <td>672</td>
      <td>671</td>
      <td>672</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>673</td>
      <td>873</td>
      <td>673</td>
      <td>873</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>874</td>
      <td>888</td>
      <td>874</td>
      <td>888</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>889</td>
      <td>894</td>
      <td>889</td>
      <td>894</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>895</td>
      <td>913</td>
      <td>895</td>
      <td>913</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>914</td>
      <td>937</td>
      <td>914</td>
      <td>937</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>938</td>
      <td>951</td>
      <td>938</td>
      <td>951</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>952</td>
      <td>982</td>
      <td>952</td>
      <td>982</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>983</td>
      <td>998</td>
      <td>983</td>
      <td>998</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>999</td>
      <td>1011</td>
      <td>999</td>
      <td>1011</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1012</td>
      <td>1029</td>
      <td>1012</td>
      <td>1029</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1030</td>
      <td>1037</td>
      <td>1030</td>
      <td>1037</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1038</td>
      <td>1040</td>
      <td>1038</td>
      <td>1040</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1041</td>
      <td>1056</td>
      <td>1041</td>
      <td>1056</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4mt1">4MT1</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">AKFFIDRPI</span><span class="topo-membrane">FAWVISIFIIAAGI</span><span class="topo-outside">FGIKSLPVSQYPSVAAPTITLHAIYPGASAQVMEGS</span></span>
<span class="topo-line"><span class="topo-outside">VLSVIERNMNGVEGLDYMSTSADSSGSGSVSLTFTPDTDENLAQVEVQNKLSEVLSTLPA</span></span>
<span class="topo-line"><span class="topo-outside">TVQQYGVTVSKARSNFLMIVMLSSDVQSTEEMNDYAQRNVVPELQRIEGVGQVRLFGAQR</span></span>
<span class="topo-line"><span class="topo-outside">AMRIWVDPKKLQNYNLSFADVGSALSAQNIQISAGSIGSLPAVRGQTVTATVTAQGQLGT</span></span>
<span class="topo-line"><span class="topo-outside">AEEFGNVILRANTDGSNIYLKDVAKVGLGMEDYSSSTRLNGVNTTGMAVMLSNSGNAMAT</span></span>
<span class="topo-line"><span class="topo-outside">AKAVKERLAVLEKYFPQGMSWKTPYDTSKFVEISIEKVI</span><span class="topo-membrane">HTLIEAMVLVFVVMYL</span><span class="topo-inside">FLQNI</span></span>
<span class="topo-line"><span class="topo-inside">RYT</span><span class="topo-membrane">LIPTIVVPISLLGGFAF</span><span class="topo-outside">ISYMGMSINVLTMF</span><span class="topo-membrane">AMILVIGIVVDDAI</span><span class="topo-inside">VVVENVERIMAG</span></span>
<span class="topo-line"><span class="topo-inside">EGLPPKEATKKAMGQISGAV</span><span class="topo-membrane">IGITAVLISVFVPL</span><span class="topo-outside">AMFSGAAGNIYKQFA</span><span class="topo-membrane">LTMASSIAFSA</span></span>
<span class="topo-line"><span class="topo-membrane">FLALTLT</span><span class="topo-inside">PALCAT</span><span class="topo-unknown">MLKTIPKGHHEEKK</span><span class="topo-inside">G</span><span class="topo-unknown">FFGWFNKKFDSWTHGYEGRVAKVLR</span><span class="topo-inside">KTFRM</span><span class="topo-membrane">MV</span></span>
<span class="topo-line"><span class="topo-membrane">VYIGLAVVGVFLF</span><span class="topo-outside">MRLPTSFLPTEDQGFVMVSVQLPAGATKERTDATLAQVTQLAKSIPE</span></span>
<span class="topo-line"><span class="topo-outside">IENIITVSGFSFSGSGQNMAMGFAIFKDWNERTASGSDAVAVAGKLTGMMMGTLKDGFGI</span></span>
<span class="topo-line"><span class="topo-outside">AVVPPPILEL</span><span class="topo-unknown">GN</span><span class="topo-outside">GSGLSINLQDRNNTGHTALLAKRNELIQKMRASGLFDPSTVRAGGLED</span></span>
<span class="topo-line"><span class="topo-outside">SPQLKIDINRAAAAAQGISFADIRTALASALSSSYVSDFPNQGRLQRVMVQADEDARMQP</span></span>
<span class="topo-line"><span class="topo-outside">ADILNLTVPNKSGVAVPLSTIATVSWENGTEQSVRFNGYPSMKLSASPATGVSTGQAMEA</span></span>
<span class="topo-line"><span class="topo-outside">VQKMVDELGGGYSFEWGGQSSEEAKGGSQTLIL</span><span class="topo-membrane">YGLAVAAVFLVLAAL</span><span class="topo-inside">YESWSI</span><span class="topo-membrane">PLAVIL</span></span>
<span class="topo-line"><span class="topo-membrane">VIPLGLIGAAAGV</span><span class="topo-outside">TGRNLFEGLLGSVPSFANDIYFQV</span><span class="topo-membrane">GFVTVMGLSAKNAI</span><span class="topo-inside">LIIEFAKDL</span></span>
<span class="topo-line"><span class="topo-inside">QAQGKSAVEAALEAARLRFRPI</span><span class="topo-membrane">IMTSFAFILGVVPLYI</span><span class="topo-outside">AAGASSASQRAIG</span><span class="topo-membrane">TTVFWGMLV</span></span>
<span class="topo-line"><span class="topo-membrane">GTLLSVFLV</span><span class="topo-unknown">PLFYVVVR</span><span class="topo-inside">KFF</span><span class="topo-unknown">KETAHEHEMAVRHASK</span></span>
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
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>10</td>
      <td>2</td>
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
      <td>339</td>
      <td>25</td>
      <td>339</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>355</td>
      <td>340</td>
      <td>355</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>356</td>
      <td>363</td>
      <td>356</td>
      <td>363</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>364</td>
      <td>380</td>
      <td>364</td>
      <td>380</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>381</td>
      <td>394</td>
      <td>381</td>
      <td>394</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>408</td>
      <td>395</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>440</td>
      <td>409</td>
      <td>440</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>441</td>
      <td>454</td>
      <td>441</td>
      <td>454</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>455</td>
      <td>469</td>
      <td>455</td>
      <td>469</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>470</td>
      <td>487</td>
      <td>470</td>
      <td>487</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>488</td>
      <td>493</td>
      <td>488</td>
      <td>493</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>494</td>
      <td>507</td>
      <td>494</td>
      <td>507</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>508</td>
      <td>508</td>
      <td>508</td>
      <td>508</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>509</td>
      <td>533</td>
      <td>509</td>
      <td>533</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>534</td>
      <td>538</td>
      <td>534</td>
      <td>538</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>539</td>
      <td>553</td>
      <td>539</td>
      <td>553</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>554</td>
      <td>670</td>
      <td>554</td>
      <td>670</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>671</td>
      <td>672</td>
      <td>671</td>
      <td>672</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>673</td>
      <td>873</td>
      <td>673</td>
      <td>873</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>874</td>
      <td>888</td>
      <td>874</td>
      <td>888</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>889</td>
      <td>894</td>
      <td>889</td>
      <td>894</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>895</td>
      <td>913</td>
      <td>895</td>
      <td>913</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>914</td>
      <td>937</td>
      <td>914</td>
      <td>937</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>938</td>
      <td>951</td>
      <td>938</td>
      <td>951</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>952</td>
      <td>982</td>
      <td>952</td>
      <td>982</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>983</td>
      <td>998</td>
      <td>983</td>
      <td>998</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>999</td>
      <td>1011</td>
      <td>999</td>
      <td>1011</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1012</td>
      <td>1029</td>
      <td>1012</td>
      <td>1029</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1030</td>
      <td>1037</td>
      <td>1030</td>
      <td>1037</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1038</td>
      <td>1040</td>
      <td>1038</td>
      <td>1040</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1041</td>
      <td>1056</td>
      <td>1041</td>
      <td>1056</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4mt1">4MT1</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">AKFFIDRPI</span><span class="topo-membrane">FAWVISIFIIAAGI</span><span class="topo-outside">FGIKSLPVSQYPSVAAPTITLHAIYPGASAQVMEGS</span></span>
<span class="topo-line"><span class="topo-outside">VLSVIERNMNGVEGLDYMSTSADSSGSGSVSLTFTPDTDENLAQVEVQNKLSEVLSTLPA</span></span>
<span class="topo-line"><span class="topo-outside">TVQQYGVTVSKARSNFLMIVMLSSDVQSTEEMNDYAQRNVVPELQRIEGVGQVRLFGAQR</span></span>
<span class="topo-line"><span class="topo-outside">AMRIWVDPKKLQNYNLSFADVGSALSAQNIQISAGSIGSLPAVRGQTVTATVTAQGQLGT</span></span>
<span class="topo-line"><span class="topo-outside">AEEFGNVILRANTDGSNIYLKDVAKVGLGMEDYSSSTRLNGVNTTGMAVMLSNSGNAMAT</span></span>
<span class="topo-line"><span class="topo-outside">AKAVKERLAVLEKYFPQGMSWKTPYDTSKFVEISIEKVI</span><span class="topo-membrane">HTLIEAMVLVFVVMYL</span><span class="topo-inside">FLQNI</span></span>
<span class="topo-line"><span class="topo-inside">RYT</span><span class="topo-membrane">LIPTIVVPISLLGGFAF</span><span class="topo-outside">ISYMGMSINVLTMF</span><span class="topo-membrane">AMILVIGIVVDDAI</span><span class="topo-inside">VVVENVERIMAG</span></span>
<span class="topo-line"><span class="topo-inside">EGLPPKEATKKAMGQISGAV</span><span class="topo-membrane">IGITAVLISVFVPL</span><span class="topo-outside">AMFSGAAGNIYKQFA</span><span class="topo-membrane">LTMASSIAFSA</span></span>
<span class="topo-line"><span class="topo-membrane">FLALTLT</span><span class="topo-inside">PALCAT</span><span class="topo-unknown">MLKTIPKGHHEEKK</span><span class="topo-inside">G</span><span class="topo-unknown">FFGWFNKKFDSWTHGYEGRVAKVLR</span><span class="topo-inside">KTFRM</span><span class="topo-membrane">MV</span></span>
<span class="topo-line"><span class="topo-membrane">VYIGLAVVGVFLF</span><span class="topo-outside">MRLPTSFLPTEDQGFVMVSVQLPAGATKERTDATLAQVTQLAKSIPE</span></span>
<span class="topo-line"><span class="topo-outside">IENIITVSGFSFSGSGQNMAMGFAIFKDWNERTASGSDAVAVAGKLTGMMMGTLKDGFGI</span></span>
<span class="topo-line"><span class="topo-outside">AVVPPPILEL</span><span class="topo-unknown">GN</span><span class="topo-outside">GSGLSINLQDRNNTGHTALLAKRNELIQKMRASGLFDPSTVRAGGLED</span></span>
<span class="topo-line"><span class="topo-outside">SPQLKIDINRAAAAAQGISFADIRTALASALSSSYVSDFPNQGRLQRVMVQADEDARMQP</span></span>
<span class="topo-line"><span class="topo-outside">ADILNLTVPNKSGVAVPLSTIATVSWENGTEQSVRFNGYPSMKLSASPATGVSTGQAMEA</span></span>
<span class="topo-line"><span class="topo-outside">VQKMVDELGGGYSFEWGGQSSEEAKGGSQTLIL</span><span class="topo-membrane">YGLAVAAVFLVLAAL</span><span class="topo-inside">YESWSI</span><span class="topo-membrane">PLAVIL</span></span>
<span class="topo-line"><span class="topo-membrane">VIPLGLIGAAAGV</span><span class="topo-outside">TGRNLFEGLLGSVPSFANDIYFQV</span><span class="topo-membrane">GFVTVMGLSAKNAI</span><span class="topo-inside">LIIEFAKDL</span></span>
<span class="topo-line"><span class="topo-inside">QAQGKSAVEAALEAARLRFRPI</span><span class="topo-membrane">IMTSFAFILGVVPLYI</span><span class="topo-outside">AAGASSASQRAIG</span><span class="topo-membrane">TTVFWGMLV</span></span>
<span class="topo-line"><span class="topo-membrane">GTLLSVFLV</span><span class="topo-unknown">PLFYVVVR</span><span class="topo-inside">KFF</span><span class="topo-unknown">KETAHEHEMAVRHASK</span></span>
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
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>10</td>
      <td>2</td>
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
      <td>339</td>
      <td>25</td>
      <td>339</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>355</td>
      <td>340</td>
      <td>355</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>356</td>
      <td>363</td>
      <td>356</td>
      <td>363</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>364</td>
      <td>380</td>
      <td>364</td>
      <td>380</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>381</td>
      <td>394</td>
      <td>381</td>
      <td>394</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>408</td>
      <td>395</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>440</td>
      <td>409</td>
      <td>440</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>441</td>
      <td>454</td>
      <td>441</td>
      <td>454</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>455</td>
      <td>469</td>
      <td>455</td>
      <td>469</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>470</td>
      <td>487</td>
      <td>470</td>
      <td>487</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>488</td>
      <td>493</td>
      <td>488</td>
      <td>493</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>494</td>
      <td>507</td>
      <td>494</td>
      <td>507</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>508</td>
      <td>508</td>
      <td>508</td>
      <td>508</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>509</td>
      <td>533</td>
      <td>509</td>
      <td>533</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>534</td>
      <td>538</td>
      <td>534</td>
      <td>538</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>539</td>
      <td>553</td>
      <td>539</td>
      <td>553</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>554</td>
      <td>670</td>
      <td>554</td>
      <td>670</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>671</td>
      <td>672</td>
      <td>671</td>
      <td>672</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>673</td>
      <td>873</td>
      <td>673</td>
      <td>873</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>874</td>
      <td>888</td>
      <td>874</td>
      <td>888</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>889</td>
      <td>894</td>
      <td>889</td>
      <td>894</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>895</td>
      <td>913</td>
      <td>895</td>
      <td>913</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>914</td>
      <td>937</td>
      <td>914</td>
      <td>937</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>938</td>
      <td>951</td>
      <td>938</td>
      <td>951</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>952</td>
      <td>982</td>
      <td>952</td>
      <td>982</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>983</td>
      <td>998</td>
      <td>983</td>
      <td>998</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>999</td>
      <td>1011</td>
      <td>999</td>
      <td>1011</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1012</td>
      <td>1029</td>
      <td>1012</td>
      <td>1029</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1030</td>
      <td>1037</td>
      <td>1030</td>
      <td>1037</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1038</td>
      <td>1040</td>
      <td>1038</td>
      <td>1040</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1041</td>
      <td>1056</td>
      <td>1041</td>
      <td>1056</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Open conformational state of MtrE

The MtrE structure reveals a fully open channel with a continuous vertical tunnel from the outer membrane surface to the periplasmic tip. The interior diameter at the widest section (outer membrane surface) is ~22 A. The volume of the continuous channel is ~45,000 A^3. The dilation of MtrE is higher than any reported open state of TolC, with D405 side chain O(delta2) atoms 11.8 A apart (vs 6.2-9.9 A in TolC).

### Periplasmic aspartate selectivity gate

An aspartate ring composed of six aspartate residues (D402 and D405 from each of three protomers) is located at the periplasmic entrance. The internal diameter is ~12 A, creating the narrowest region of the tunnel. This ring acts as a selectivity gate and can be blocked by large cations such as hexamminecobalt(III). The open state likely reflects the low-pH form (crystallized at pH 4.6), which neutralizes the aspartate ring.

### Intra- and inter-protomer grooves for MtrC interaction

The periplasmic domain of the MtrE trimer forms three intra-protomer and three inter-protomer grooves lined with charged and polar residues (E161, R168, E407, E414, Q421 at intra-protomer; Q167, N178, E198, E202, R215, R219 at inter-protomer). Residues E414, Q421, and N178 are important for MtrCDE function. These grooves likely provide interaction sites for the MtrC membrane fusion protein.

### MtrC-mediated gating of the MtrE channel

The opening and closing of the MtrE channel may be regulated by conformational changes in the MtrC membrane fusion protein, which propagate motion from the MtrD inner membrane efflux pump. As MtrD is a PMF-dependent pump, active proton translocation likely provides the energy to open and close MtrE.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/mtrcde-tripartite-efflux-pump/">MtrCDE Tripartite Multidrug Efflux Pump</a> — MtrE is the outer membrane channel component of this tripartite efflux system
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltoside (DDM)</a> — Used for MtrE solubilization and purification
- <a href="/xray-mp-wiki/reagents/detergents/og/">n-Octyl-beta-D-glucoside (OG)</a> — Used as crystallization additive
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/antibiotics/ampicillin/">Ampicillin</a> — Antibiotic used in selection
- <a href="/xray-mp-wiki/reagents/buffers/sodium-acetate/">Sodium Acetate</a> — Buffer component in purification or crystallization
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used in purification or crystallization
